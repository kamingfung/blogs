---
id: engineering/instructions-that-agents-actually-follow
title: Instructions that agents actually follow
level: intermediate
---

**Promise:** Write a project instruction file for an AI coding agent that changes its behavior measurably, and tell which rules belong in prose and which belong in a check.

**Trap:** "More instructions give more control." Past a point, extra rules dilute the ones that matter, contradict each other, and get ignored; a short file of specific, checkable rules beats a long manifesto.

**Assumes:** Some experience using an AI coding assistant; no prior module.

## Outline

1. **Where instructions sit**: the agent reads a project file (AGENTS.md, CLAUDE.md and similar) [verify] at the start of a session, alongside the system prompt and the task. It competes for attention with everything else in the context window.
2. **Why rules get ignored**: vague rules ("write clean code"), rules that conflict, rules buried in long files, and rules that state a preference without a reason. Describe each failure mode by the behavior it produces.
3. **What a followable rule looks like**: imperative, one action per bullet, specific enough to check, with the reason in a short clause. Point to the place in the repo instead of copying the content into the file.
4. **Prose versus enforcement**: a rule an agent can route around is a suggestion. Move anything checkable (format, lint, tests, forbidden paths) into a command or hook, and keep prose for judgment calls that no check can capture.
5. **Maintaining the file**: add a rule only after a recurring mistake, search for an existing rule before adding one, and prune rules that no longer fire. Test a change by rerunning the same task before and after.
6. **What this means for you**: an agent asked to touch a forecasting pipeline needs to know the few things that break a weekly run (never change production parameters without review, rerun the backtest command, do not fill missing data silently); those few rules, written precisely, matter more than any style guidance.

## Key takeaways

- A short instruction file of specific rules is followed more reliably than a long one, because every added rule competes for the same attention [verify].
- A rule that can be checked by a command belongs in a hook or CI check, not only in prose.
- A rule with a stated reason is applied more sensibly to cases it did not anticipate than a bare command [verify].
- Adding a rule only in response to an observed, recurring mistake keeps the file short and each rule tied to evidence.
- The only reliable test of an instruction change is to rerun the same task before and after it.

## Not in this module

- The full harness (tools, middleware, memory, verification loop) and the instruction file as a feedback loop: engineering/harness-engineering.
- Judging whether the agent's output is right: engineering/evaluating-agent-output.
- Lint and format checks themselves: engineering/linters-and-formatters.

## Phase 2

- **Show:** the same instruction file in two versions (long and vague, short and specific) side by side, annotated with which rules the agent followed on one fixed task.
- **Sources to find:** agent vendors' official guidance on project instruction files; any published study of instruction length or position against compliance in long contexts.
