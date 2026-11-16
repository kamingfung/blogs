---
id: engineering/linters-and-formatters
title: Linters and formatters
level: introductory
---

**Promise:** Set up one formatter and one linter so that style is never discussed again and a class of bugs is caught before the code runs.

**Trap:** "Linters are about style." Formatting is about style; a linter's useful rules flag code that runs but is probably wrong (unused names, shadowed variables, mutable default arguments, bare excepts).

**Assumes:** Some programming; no prior module.

## Outline

1. **Two tools, two jobs**: a formatter rewrites layout with no options to argue about; a linter reads code and reports suspicious patterns without changing meaning. Keep the distinction sharp because people configure them as if they were one thing.
2. **What a formatter buys you**: diffs that show only real changes, no review comments on spacing, and layout that exposes intent (the parenthesized one-element tuple from the sneaky-comma module is one case). The win is consistency, not beauty.
3. **Linter rules that catch bugs, not taste**: group rules by what they prevent (undefined or unused names, risky defaults, swallowed exceptions, import cycles). Start with the bug-catching set and add style rules only when the team agrees.
4. **Where the checks run**: editor on save, a pre-commit hook, and CI as the gate that cannot be skipped. One configuration file read by all three, so the local run and the CI run agree. Name current tools (Ruff, Black, pre-commit) in plain text and mark their defaults [verify].
5. **Adopting on an existing codebase**: format everything in one dedicated commit, then turn on lint rules gradually with a baseline, so the history stays readable and nobody fixes a thousand warnings at once.
6. **What this means for you**: a weekly forecast repo touched by several people, and by AI agents, stays reviewable only if layout is automatic; a lint rule that fails CI is the cheapest guard against an unused variable that should have been a feature, or an exception swallowed in a data-loading step.

## Key takeaways

- A formatter removes a whole category of review comments because it leaves no layout choices to make.
- The highest-value linter rules flag code that runs but is likely wrong, not code that is merely untidy.
- A check that only runs in the editor is optional; the same check in CI is a rule.
- Reformatting a legacy codebase in one isolated commit keeps the blame history usable; mixing it with logic changes hides real edits.
- A single fast tool can now replace several older linters and a formatter [verify].

## Not in this module

- Static types and what a type checker proves: engineering/type-checkers.
- Seeing inferred types in the editor: engineering/the-sneaky-comma-inlay-type-hints.
- Lint and tests as the verification loop for an AI agent: engineering/harness-engineering.
- Team workflow around CI and pull requests: engineering/git-for-a-team.

## Phase 2

- **Show:** a before-and-after diff of one function: a formatter pass, then a linter report flagging a real bug that survived formatting.
- **Sources to find:** official documentation of the named formatter, linter and pre-commit framework; the language style guide (PEP 8).
