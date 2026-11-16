# Outlines

Wireframes for modules that are not written yet. Quarto ignores folders that start with `_`, so nothing here is rendered or published.

One file per unwritten module: `_outlines/<series slug>/<module slug>.md`, where the module id in `series/*.yml` is `<series slug>/<module slug>`. When a module is written, move its outline's content into `blogs/`, add `path:` in the series file, and delete the outline.

Check coverage and shape with `.venv/bin/python tools/check_outlines.py`.

## Template

```markdown
---
id: <series slug>/<module slug>
title: <title from the series file>
level: <level from the series file>
---

**Promise:** one sentence, the candidate `description`: what the reader can do or explain afterwards.

**Trap:** the wrong belief a reader likely holds, and the corrected claim in one line.

**Assumes:** modules or knowledge needed (use the series file's `requires`).

## Outline

1. **<Section heading>**: one or two lines on what it establishes.
2. …   (4 to 6 sections; the last two are always "What this means for you" and nothing after it but takeaways)

## Key takeaways

- 3 to 5 claims, each one sentence, each testable. End a takeaway with `[verify]` when it states a number, a date, a named result or anything that will need a citation.

## Not in this module

- What the neighboring modules cover, by id, so this one does not repeat them.

## Phase 2

- **Show:** one line on the figure, widget or worked example that would carry the main idea (an idea only; nothing is built yet).
- **Sources to find:** the kinds of primary source needed (no DOIs or citations yet; never cite from memory).
```

## Rules for this phase

- No plots, widgets, animations, code or worked examples. No citations, DOIs or quoted numbers presented as checked: mark them `[verify]`.
- American English. Plain words first; name a term only after describing the idea.
- Takeaways are hypotheses for the writer to confirm, not published claims.
- Public or textbook knowledge only; no company data or company views.
