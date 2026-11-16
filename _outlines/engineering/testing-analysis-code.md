---
id: engineering/testing-analysis-code
title: Testing analysis code
level: intermediate
---

**Promise:** Write small tests that catch the bugs analysis code actually has: wrong joins, dropped rows, silent missing values and results that drift.

**Trap:** "Analysis code cannot be tested because the right answer is unknown." You rarely know the final answer, but you always know properties it must have (row counts, ranges, totals, behavior on tiny hand-made inputs), and those are testable.

**Assumes:** engineering/notebooks-vs-scripts.

## Outline

1. **What goes wrong in analysis code**: joins that duplicate or drop rows, missing values filled or ignored silently, off-by-one date windows, units mixed. These run without errors, which is why they need tests.
2. **Tests on tiny hand-made data**: build a three-row input where the right answer is obvious, and check the function returns it. Cover the empty, single-row, missing-value and boundary cases. Arrange, act, assert.
3. **Property and invariant checks**: totals preserved through a reshape, no duplicate keys after a join, values inside a physical range. These hold on real data too, so they double as runtime checks.
4. **Data contracts at the boundary**: validate the schema and ranges of input data where it enters, and fail loudly with the offending rows, instead of defending against bad data deep in the code.
5. **Regression tests for results**: freeze the output of a known run and compare with a tolerance, so a refactor that should not move numbers is shown not to. Explain how to choose the tolerance and when to update the frozen output.
6. **What this means for you**: in a weekly forecasting pipeline the dangerous bug is the one that ships a plausible wrong number; a test that a join keeps one row per site and week, and a regression check against last week's backtest, catch most of them before the run.

## Key takeaways

- Most analysis bugs raise no error, so a passing run is weak evidence that the code is correct.
- A test on a tiny input with an obvious answer catches join, filter and date-window bugs that real data hides.
- Invariants such as preserved totals and unique keys can be checked both in tests and on every production run.
- A regression test with a stated tolerance shows that a refactor did not move results; updating its expected values needs a stated reason.
- Mocking the data under test hides the bugs the test exists to find; mock only real input and output boundaries.

## Not in this module

- Moving logic out of notebooks so it can be tested: engineering/notebooks-vs-scripts.
- Static type checks: engineering/type-checkers.
- Reviewing tests an AI agent wrote: engineering/evaluating-agent-output.
- Running tests in CI on every pull request: engineering/git-for-a-team.

## Phase 2

- **Show:** a three-row example where a many-to-one join silently doubles a total, with the one-line invariant that catches it.
- **Sources to find:** official pytest documentation; documentation of a property-based testing library and a dataframe validation library; published guidance on testing in research software.
