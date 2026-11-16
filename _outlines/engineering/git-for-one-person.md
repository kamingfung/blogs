---
id: engineering/git-for-one-person
title: Git for one person
level: introductory
---

**Promise:** Use Git alone to answer "what changed, when and why" about any result, and to undo a bad change without fear.

**Trap:** "Git is a team tool; working alone, a folder of dated copies is enough." Alone, Git is a lab notebook for code: the value is a searchable history tying each result to the exact code that made it.

**Assumes:** Some programming; no prior module.

## Outline

1. **The problem dated copies do not solve**: which version produced the figure in last month's report, and what changed since? Describe the "final_v2_really" folder and what it cannot answer.
2. **The minimal model**: a commit is a snapshot with a message; history is a chain of snapshots; a branch is a movable label. Enough to work with, nothing more.
3. **Commits that help future you**: one logical change per commit, a message that says why, and a commit before every run whose results you will keep. Record the commit id with the result.
4. **What to keep out**: data, secrets, large outputs and generated files go in an ignore file; say where they live instead. Note what to do if a secret was committed.
5. **Getting back**: compare two versions, find the commit that changed a number, restore one file, and try an idea on a branch you can delete. Use a remote as a backup.
6. **What this means for you**: when this week's forecast differs from last week's, you want to answer in minutes whether the code, the data or the environment changed; a commit id saved with each run makes the code question a single comparison.

## Key takeaways

- Saving the commit id alongside each result ties that result to the exact code that produced it.
- A commit message that states why the change was made is the only record of a reason the code itself cannot show.
- Data, secrets and generated outputs do not belong in the repository; a secret once pushed should be treated as leaked.
- A branch for an experiment makes abandoning the idea free.
- Searching history for the commit that changed a result can be automated by bisection [verify].

## Not in this module

- Branches, pull requests, review and merge strategies with others: engineering/git-for-a-team.
- Locking the environment alongside the code: engineering/environments-that-don-t-break.
- Notebooks in version control: engineering/notebooks-vs-scripts.

## Phase 2

- **Show:** a timeline of commits with one result attached to each, and the question "what changed between these two forecasts" answered by a single comparison.
- **Sources to find:** the official Git documentation and the Pro Git book; published guidance on version control for scientific computing.
