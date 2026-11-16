---
id: training/code-someone-else-can-run
title: Research code someone else can run
level: intermediate
---

**Promise:** Package the code behind a paper so a stranger can rerun it from a clean machine with one documented command and check that the outputs match.

**Trap:** Code that runs on my machine and sits in a public repository is reproducible; in fact attempts to rerun published research code fail more often than they succeed, mostly for missing dependencies, data and paths.

**Assumes:** engineering/notebooks-vs-scripts (when analysis should leave the notebook).

## Outline

1. **What goes wrong when strangers rerun code**: the usual failures, from absolute paths and unpinned packages to data that is "available on request".
2. **The minimum package**: pinned environment, data or a script that fetches it, one entry-point command, and the expected outputs to compare against.
3. **A README written for the stranger**: what it reproduces, how long it takes, what hardware it needs, and which figure each output feeds.
4. **Test it the way they will**: rerun from a fresh clone in a clean environment before submission, and archive the exact version the paper used.
5. **What this means for you**: a pre-submission check for any paper with code.

## Key takeaways

- Studies that attempted to rerun code published with papers found that most of it did not run without changes. [verify]
- Rerunning from a fresh clone in a clean environment finds the failures a stranger would hit before they hit them.
- Shipping the expected outputs lets a rerun be checked, not only executed.
- An archived snapshot of the exact version used in the paper stays runnable after the live repository changes.

## Not in this module

- engineering/environments-that-don-t-break and engineering/testing-analysis-code: the environment and testing mechanics.
- training/open-source-as-a-scientist: licensing, credit and maintenance.
- training/your-first-contribution-to-a-community-model: contributing to a shared model.

## Phase 2

- **Show:** a failure tree for "I cloned it and it did not run", with each branch mapped to the package item that prevents it.
- **Sources to find:** large-scale rerun studies of published research code and notebooks; journal and artifact-evaluation reproducibility policies.
