"""Check that every unwritten module in series/*.yml has a well-formed outline in _outlines/.

    .venv/bin/python tools/check_outlines.py
"""
import glob
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ["## Outline", "## Key takeaways", "## Not in this module", "## Phase 2"]
LEADS = ["**Promise:**", "**Trap:**", "**Assumes:**"]


def main():
    gaps = unwritten_modules()
    problems = [p for m in gaps for p in check(m)]
    extra = {str(f.relative_to(ROOT)) for f in (ROOT / "_outlines").glob("*/*.md")} - {outline_path(m) for m in gaps}
    problems += [f"{f}: no unwritten module with this id" for f in sorted(extra)]
    print("\n".join(problems))
    print(f"outlines: {len(gaps)} unwritten modules, {len(problems)} problem(s)")
    sys.exit(1 if problems else 0)


def unwritten_modules():
    mods = []
    for f in sorted(glob.glob(str(ROOT / "series" / "*.yml"))):
        for part in yaml.safe_load(open(f)).get("parts") or []:
            mods += [m for m in part["modules"] if not m.get("path") and not m.get("split_from")]
    return mods


def outline_path(m):
    return f"_outlines/{m['id']}.md"


def check(m):
    path = ROOT / outline_path(m)
    if not path.exists():
        return [f"{outline_path(m)}: missing"]
    text = path.read_text()
    fm = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not fm:
        return [f"{outline_path(m)}: no frontmatter"]
    meta = yaml.safe_load(fm.group(1))
    out = [f"{outline_path(m)}: {k} is {meta.get(k)!r}, series file says {m[k]!r}"
           for k in ("id", "title", "level") if meta.get(k) != m[k]]
    out += [f"{outline_path(m)}: missing {s!r}" for s in SECTIONS + LEADS if s not in text]
    if out:
        return out
    steps = re.findall(r"^\d+\. ", section(text, "## Outline"), re.M)
    takeaways = re.findall(r"^- ", section(text, "## Key takeaways"), re.M)
    if not 4 <= len(steps) <= 6:
        out.append(f"{outline_path(m)}: {len(steps)} outline sections, want 4 to 6")
    if not 3 <= len(takeaways) <= 5:
        out.append(f"{outline_path(m)}: {len(takeaways)} takeaways, want 3 to 5")
    if re.search(r"doi\.org|```|\{ojs\}", text):
        out.append(f"{outline_path(m)}: has a DOI or code block; this phase is outline only")
    return out


def section(text, heading):
    return text.split(heading, 1)[1].split("\n## ", 1)[0]


if __name__ == "__main__":
    main()
