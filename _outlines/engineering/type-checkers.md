---
id: engineering/type-checkers
title: Type checkers
level: intermediate
---

**Promise:** Explain what a static type checker proves about Python code, and roll one out on an analysis codebase without drowning in errors.

**Trap:** "Type hints make Python safer at runtime." Python ignores annotations when it runs; safety comes only from a separate checker that reads them, and only as far as the annotations are true.

**Assumes:** engineering/the-sneaky-comma-inlay-type-hints.

## Outline

1. **From seeing types to checking them**: inlay hints show the inferred type to a human; a checker turns the same inference into an error that fails a build. The sneaky-comma bug is the bridge: the hint showed a tuple, the checker refuses to add it to an int.
2. **What a checker can and cannot prove**: it finds mismatches across function boundaries, missing None handling and wrong attribute access; it cannot see values loaded from files, the shape of a dataframe, or anything typed as Any. Name the gap between static types and runtime data.
3. **Gradual typing in practice**: annotate public function signatures first, let inference do the inside, and raise strictness module by module. Explain what "strict mode" switches on [verify].
4. **The tools and how they differ**: mypy, Pyright and the newer fast checkers differ in inference rules, speed and defaults [verify]. Pick one, pin its version, and run it in CI, because two checkers can disagree on the same code.
5. **Types meet data**: dataframes and arrays are where analysis code goes untyped. Options range from typed wrappers to runtime schema validation at the load boundary; the checker covers the code, the schema covers the data.
6. **What this means for you**: in a forecasting pipeline the costly bugs are a Series where a scalar was expected, or an Optional date that is None in one week's run; typed function signatures plus a schema check at load catch both before the weekly run, not after.

## Key takeaways

- Python does not enforce annotations at runtime; only a separate checker or a runtime validator acts on them.
- A checker is only as strong as the annotations it reads: one Any at a boundary silences every error downstream of it.
- Annotating function signatures first gives most of the benefit for a fraction of the effort, because inference covers function bodies.
- Two type checkers can report different errors on the same code, so a team should pin one checker and one version [verify].
- Static types cannot validate the contents of a loaded file; that needs a runtime schema check at the data boundary.

## Not in this module

- Inlay hints and the trailing-comma bug: engineering/the-sneaky-comma-inlay-type-hints.
- Formatting and lint rules: engineering/linters-and-formatters.
- Tests that check values, not types: engineering/testing-analysis-code.

## Phase 2

- **Show:** the sneaky-comma function under three conditions: no annotations (checker silent), annotated return (checker error), return typed Any (checker silent again).
- **Sources to find:** the Python typing specification and the relevant PEPs (484 and successors); official docs of mypy and Pyright; documentation of a dataframe schema validation library.
