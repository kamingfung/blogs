---
id: training/your-first-contribution-to-a-community-model
title: Your first contribution to a community model
level: intermediate
---

**Promise:** Take a change from your own copy of a shared scientific model (climate, crop, hydrology) back to the main project, in the form its maintainers can review and merge.

**Trap:** A first contribution should be your new science feature; in fact a small fix, test or documentation change is the one that gets merged, and science changes need agreement on how they will be validated before any code.

**Assumes:** engineering/testing-analysis-code (tests that pin down what analysis code should do); training/open-source-as-a-scientist is useful background.

## Outline

1. **Why private forks rot**: a local modification that never goes upstream must be re-applied by hand at every new release, and its results cannot be reproduced by anyone else.
2. **Read the project before the code**: contributing guide, issue tracker, governance, who reviews science changes, and how releases are tested against reference runs.
3. **Start small, in public**: open an issue first; a first pull request that fixes a bug, adds a test or corrects documentation teaches you the review process at low cost.
4. **Science changes need a validation plan**: agree on which reference cases, metrics and tolerances will show the change is an improvement before writing it.
5. **What this means for you**: a path from a local change to an issue, a small first pull request and a proposed validation plan.

## Key takeaways

- A modification kept in a private copy of a community model costs more to maintain each release than it would have cost to contribute.
- In many open-source projects, most first-time contributors never make a second contribution. [verify]
- A first pull request that is small and tied to an open issue is reviewed and merged faster than a large one. [verify]
- A science change proposed with its reference cases and acceptance tolerances is easier for maintainers to review than one judged after the code exists.

## Not in this module

- training/open-source-as-a-scientist: releasing and maintaining your own project.
- training/code-someone-else-can-run: packaging the code behind one paper.
- engineering/testing-analysis-code and engineering/git-for-a-team: the testing and version-control mechanics.

## Phase 2

- **Show:** the life of one contribution as a timeline, from local change to issue, pull request, review and release.
- **Sources to find:** contributing and governance documents of large community models; empirical software-engineering studies of newcomer retention and pull-request acceptance.
