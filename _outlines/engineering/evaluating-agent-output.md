---
id: engineering/evaluating-agent-output
title: Evaluating agent output
level: intermediate
---

**Promise:** Decide whether an AI agent's change is correct with checks proportional to its risk, and turn repeated judgments into a small evaluation set.

**Trap:** "If the tests pass, the agent's work is right." Agents optimize toward the visible check: they can edit the test, skip the hard case, or pass a weak suite with wrong logic; passing tests is necessary, not sufficient.

**Assumes:** engineering/harness-engineering.

## Outline

1. **Why agent output needs its own review habits**: output arrives fast, fluent and confidently described; the summary the agent writes is a claim, not evidence. Read the diff, not the report.
2. **Known failure patterns**: tests weakened or deleted, errors caught and silenced, a hard case special-cased, behavior described that the code does not implement, scope creep beyond the request. Each has a cheap check.
3. **Match the check to the risk**: docs need a glance; logic changes need tests the agent did not write; anything that moves numbers needs an end-to-end comparison of outputs before and after. Name what a human reviewer must still approve.
4. **From one review to an evaluation set**: when the same kind of task recurs, save the task, the inputs and the accepted answer; rerun the set when the model, the instructions or the harness changes. Discuss model-as-judge as a scaling aid with known biases [verify].
5. **Independent second opinions**: a separate reviewer (human or another model) given the code, not the author's conclusion, catches what self-review misses; a reviewer handed your hypothesis tends to confirm it.
6. **What this means for you**: an agent's change to a forecasting pipeline is judged by the backtest metric on a fixed window against the current main branch, not by the agent's summary; record both results before review.

## Key takeaways

- An agent's own summary of its work is a claim to verify, not evidence that the work is done.
- Passing tests can be produced by weakening the tests, so the review must check whether test files changed.
- Any change that can move outputs should be compared end to end against the unchanged baseline on the same data.
- Model-as-judge evaluation has measurable biases, such as favoring longer or self-generated answers [verify].
- A small saved set of recurring tasks with accepted answers turns each model or instruction change into a measurable comparison.

## Not in this module

- The components of a harness and the verification loop inside it: engineering/harness-engineering.
- Writing the instructions the agent follows: engineering/instructions-that-agents-actually-follow.
- Writing tests for analysis code: engineering/testing-analysis-code.
- Pull-request review as a team process: engineering/git-for-a-team.

## Phase 2

- **Show:** a checklist mapping each failure pattern to the one command or diff view that exposes it.
- **Sources to find:** published evaluations of coding agents and their failure modes; papers on model-as-judge bias; benchmark documentation that describes how tasks are scored.
