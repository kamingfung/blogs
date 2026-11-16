---
id: engineering/notebooks-vs-scripts
title: Notebooks vs scripts
level: introductory
---

**Promise:** Decide when an analysis belongs in a notebook and when in a script or package, and move it across without losing the exploration.

**Trap:** "Notebooks are for beginners; real work is in scripts." Notebooks are the right tool for exploring and explaining; the problem is running production results from out-of-order hidden state, not the format.

**Assumes:** Some Python and notebook experience; no prior module.

## Outline

1. **What each format is good at**: notebooks for looking at data, trying ideas and telling a story with outputs inline; scripts and modules for anything that must run the same way unattended, be imported or be tested.
2. **The hidden-state problem**: cells run out of order, deleted cells whose variables still exist, results that cannot be reproduced by "run all". Show why "run all from a fresh kernel" is the minimum bar.
3. **Notebooks in version control**: outputs and metadata make diffs unreadable and repositories heavy. Options: strip outputs, pair with a text format, or use a text-based notebook such as Quarto or Jupytext [verify].
4. **The migration path**: move stable logic into functions in a module, import them back into the notebook, and keep the notebook as a thin driver and explanation. The notebook shrinks; nothing is lost.
5. **Running notebooks as jobs**: parameterized execution exists [verify], but name its cost: errors surface late, and the logic is still hard to test. Use it for reports, not for core computation.
6. **What this means for you**: the weekly forecast should run from a script or pipeline that someone else can trigger; the notebook is where you investigate why this week's number moved, importing the same functions so the investigation and the production run cannot drift apart.

## Key takeaways

- A notebook result that does not survive "restart and run all" is not a result.
- Moving logic into an imported module lets a notebook and a production script share one implementation.
- Notebook files store outputs and metadata, so without stripping or pairing their diffs are mostly noise [verify].
- Executing a notebook as a scheduled job reproduces the run but not the testability of a module.

## Not in this module

- Tests for the functions you extract: engineering/testing-analysis-code.
- Turning a notebook into an interactive app: engineering/from-notebook-to-app.
- Locking the environment the script runs in: engineering/environments-that-don-t-break.
- Committing notebooks and scripts: engineering/git-for-one-person.

## Phase 2

- **Show:** one notebook in three states: exploratory, with logic extracted to a module, and as a thin driver importing that module.
- **Sources to find:** published studies of notebook reproducibility on public repositories; official docs of Jupytext, Quarto and a notebook-parameterization tool.
