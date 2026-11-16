---
id: engineering/environments-that-don-t-break
title: Environments that don't break
level: introductory
---

**Promise:** Give every project its own declared, locked environment so that the same code produces the same result next month and on a colleague's machine.

**Trap:** "A requirements file with package names is reproducible." Unpinned names resolve to whatever is newest on install day; reproducibility needs a lock file with exact versions of every transitive dependency, plus the interpreter version.

**Assumes:** Some programming; no prior module.

## Outline

1. **How environments break**: a global install shared by every project, an upgrade for one project that breaks another, an unpinned dependency that changes behavior between runs. Describe the symptom before naming the cause.
2. **Isolation**: one virtual environment per project, created from a declaration in the repository, never by hand. Note the interpreter version as part of the environment.
3. **Declare, then lock**: the project file states what you need and the acceptable ranges; the lock file records exactly what was installed. Commit both. Name current tools (uv, pip-tools, conda, Poetry) in plain text [verify].
4. **Upgrading on purpose**: update the lock in its own change, rerun the tests and compare outputs, so a library upgrade that moves results is caught as a change, not discovered later as a mystery.
5. **Beyond Python packages**: system libraries, compiled extensions, operating system differences and data versions also change results; containers cover some of this at a cost. Say where locking stops.
6. **What this means for you**: a weekly forecast rerun on a fresh machine should reproduce last week's numbers from the same data; if a library upgrade moves the forecast, you want to see it in a diff of the lock file and a backtest, not in a planner's question.

## Key takeaways

- An unpinned dependency makes a project's behavior depend on the date it was installed.
- A lock file records every transitive dependency at an exact version; a list of top-level names does not.
- Upgrading dependencies in a dedicated change, with outputs compared before and after, separates library-driven changes from code-driven ones.
- Numerical results can shift between library versions even when no code changed [verify].
- A lock file does not capture the operating system, system libraries or input data, so it is necessary but not sufficient for reproducibility.

## Not in this module

- Running analysis as scripts instead of notebooks: engineering/notebooks-vs-scripts.
- Tests that catch a changed result: engineering/testing-analysis-code.
- Recording which lock file produced which result: engineering/git-for-one-person.
- Environments on a deployment server: engineering/deploying-a-streamlit-app.

## Phase 2

- **Show:** a timeline of two installs of the same requirements file a few months apart, with the resolved versions diverging.
- **Sources to find:** Python packaging standards (pyproject and lock file specifications); official docs of uv, pip and conda; any published study on reproducibility failures in scientific software.
