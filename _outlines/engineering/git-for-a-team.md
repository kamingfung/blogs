---
id: engineering/git-for-a-team
title: Git for a team
level: intermediate
---

**Promise:** Work on shared analysis code with branches, pull requests and review so that main always runs and every change has a reviewer and a reason.

**Trap:** "Code review is about catching typos and style." Automated tools cover style; review's job is soundness: does the change do what it claims, on the data it will meet, and is the claimed improvement measured against a baseline?

**Assumes:** engineering/git-for-one-person.

## Outline

1. **Main as the shared contract**: main is what everyone builds on and what production runs. Every change arrives through a short-lived branch and a pull request; nobody pushes to main directly.
2. **Pull requests sized for review**: one purpose per pull request, a description of what changed, why and how to test it, small enough for a focused review. Split large work into a stack of pull requests.
3. **Automated checks first**: formatting, lint, type checks and tests run on every pull request, so human reviewers spend attention on logic and evidence, not layout.
4. **Reviewing analysis changes**: ask for the baseline, the metric and the evaluation window behind any claimed improvement; rerun surprising evidence; label findings by severity. Explain how to answer a review as well as give one.
5. **Integrating changes**: merge versus rebase, squash merges, resolving conflicts, and what rewriting shared history breaks [verify]. Pick one team rule and write it down.
6. **What this means for you**: a change to a forecasting model should arrive as a pull request with before-and-after backtest results on the same window; the reviewer approves evidence, not intent, and main stays the version that runs next Monday.

## Key takeaways

- Protecting main so that changes arrive only through reviewed pull requests keeps the production version runnable.
- Smaller pull requests get more thorough reviews than large ones [verify].
- Automated checks in CI free human reviewers to judge logic and evidence instead of style.
- A claimed improvement in a pull request needs a number, a baseline, a metric and an evaluation window to be reviewable.
- Rewriting history on a branch that others have pulled breaks their copies, so rebasing is safe only on branches you alone own.

## Not in this module

- Commits, history and branches for solo work: engineering/git-for-one-person.
- The lint, type and test tools CI runs: engineering/linters-and-formatters, engineering/type-checkers, engineering/testing-analysis-code.
- Reviewing changes written by an AI agent: engineering/evaluating-agent-output.

## Phase 2

- **Show:** a branch diagram of two pull requests landing on main, with the CI checks and review step drawn as gates.
- **Sources to find:** official Git and hosting-platform documentation on pull requests and branch protection; empirical studies of code review effectiveness and pull request size.
