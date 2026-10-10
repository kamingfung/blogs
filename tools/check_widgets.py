"""Fail the build when an OJS widget renders empty or errors.

An OJS widget can fail in ways the render never sees, because Quarto does not
run the cells: a cell that throws at runtime, a cell waiting on a value that
never arrives, or a page whose scripts never load. The page still builds; the
card frame renders and stays empty, or shows an error only in the browser. The
only reliable check is to open the page in a real browser and look inside each
card.

So this serves the rendered site, opens every page that loads the OJS runtime,
and requires, within a timeout, that every `.sim-card` holds at least one live
control or chart and that no cell reports an error. A script that fails to load
is reported by name, so an infrastructure fault is never mistaken for a broken
widget.

Verified against two deliberate breakages: a cell referencing an undefined name
(caught on that page only, as an OJS cell error) and a missing OJS runtime
(caught on every page).

    python tools/check_widgets.py [_site] [--timeout SECONDS]

Exit status is non-zero if any page fails. Uses the system Chrome through
Playwright, so no browser download is needed; GitHub's ubuntu-latest runners
ship Chrome.
"""

from __future__ import annotations

import argparse
import functools
import http.server
import socketserver
import sys
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

# What a working card contains once OJS has run. Not plain `svg`: the heading
# anchor inside a card can be an svg icon, which is there even when OJS is dead.
LIVE = 'input, select, textarea, .sim-readout, svg[class^="plot"], figure[class^="plot"]'

PROBE = f"""() => [...document.querySelectorAll('.sim-card')].map(card => ({{
    live: card.querySelectorAll('{LIVE}').length,
    errors: card.querySelectorAll('.observablehq--error').length,
}}))"""


class _QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args) -> None:
        pass


class _Server(socketserver.ThreadingTCPServer):
    # A Quarto page requests ~25 assets at once. Python's default listen backlog
    # of 5 drops connections under that burst, and a dropped script kills OJS on
    # the page with no error. Measured: at 5, three runs failed 1, 3 and 1 random
    # pages, each on a different dropped script; at 128, three runs were clean.
    # Every "silent OJS hang" seen while porting this site was this, not OJS.
    request_queue_size = 128
    daemon_threads = True
    allow_reuse_address = True


def serve(root: Path) -> tuple[socketserver.TCPServer, int]:
    server = _Server(("127.0.0.1", 0), functools.partial(_QuietHandler, directory=str(root)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, server.server_address[1]


def check_page(page, url: str, timeout_s: float) -> tuple[bool, str]:
    failed_scripts: list[str] = []
    page.on("requestfailed", lambda r: r.url.endswith(".js") and failed_scripts.append(r.url))
    page.goto(url, wait_until="load")
    deadline = timeout_s * 1000
    waited = 0
    while True:
        cards = page.evaluate(PROBE)
        errors = sum(c["errors"] for c in cards)
        if errors:
            return False, f"{errors} OJS cell error(s)"
        empty = sum(1 for c in cards if c["live"] == 0)
        if cards and not empty:
            return True, f"{len(cards)} card(s) live after {waited / 1000:.1f}s"
        if waited >= deadline:
            if failed_scripts:  # an infrastructure fault, not a widget bug; say which
                return False, f"script failed to load: {failed_scripts[0].rsplit('/', 1)[-1]}"
            if not cards:
                return False, "loads the OJS runtime but has no .sim-card"
            return False, f"{empty} of {len(cards)} card(s) still empty after {timeout_s:.0f}s"
        page.wait_for_timeout(250)
        waited += 250


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("site", nargs="?", default="_site")
    ap.add_argument("--timeout", type=float, default=30.0)
    args = ap.parse_args()

    root = Path(args.site).resolve()
    pages = sorted(
        p.relative_to(root).as_posix()
        for p in root.rglob("*.html")
        if "quarto-ojs-runtime" in p.read_text(errors="ignore")
    )
    if not pages:
        print(f"check_widgets: no OJS pages under {root}", file=sys.stderr)
        return 1

    server, port = serve(root)
    failures = 0
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(channel="chrome", headless=True)
            for rel in pages:
                page = browser.new_page()
                ok, detail = check_page(page, f"http://127.0.0.1:{port}/{rel}", args.timeout)
                page.close()
                failures += not ok
                print(f"{'ok  ' if ok else 'FAIL'}  {rel}  ({detail})")
            browser.close()
    finally:
        server.shutdown()

    print(f"check_widgets: {len(pages) - failures} of {len(pages)} OJS pages live")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
