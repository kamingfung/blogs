---
id: teaching-leading/code-review-as-feedback
title: Code review as feedback
level: intermediate
---

**Promise:** Write review comments that teach as well as catch defects: prioritized, labeled by severity, tied to stated criteria, and about the code rather than the author.

**Trap:** Code review is a gate that finds bugs; it is also the most frequent written feedback most engineers get, and the classroom rules for feedback apply to it.

**Assumes:** teaching-leading/giving-hard-feedback.

## Outline

1. **Review is feedback at volume**: an engineer may get more review comments in a month than graded comments in a degree; treat each one as teaching.
2. **Prioritize and label**: mark each comment as blocking, should-fix or optional; a wall of equal comments hides the one that matters.
3. **Criteria before the review**: a short shared checklist plays the role of a rubric; the author can check their own work first.
4. **About the code, as a question when unsure**: "this loop reads the file twice" or "what happens when the list is empty?", never "you always".
5. **Close the loop**: the author answers every point; the reviewer confirms the fix; recurring issues go into the checklist or a team note, not into fifty repeated comments.
6. **What this means for you**: in your next review, label every comment by severity, cap blocking comments at what truly blocks, and add one recurring point to a shared checklist.

## Key takeaways

- Label each review comment by severity, so the author fixes what matters first.
- A shared checklist written before review lets authors catch most issues themselves.
- Phrase comments about the code, and ask a question when you are not sure it is a problem.
- Move a comment you write often into a checklist or guide instead of repeating it.
- Slow reviews cost more learning than strict ones, because feedback arrives after the author has moved on `[verify]`.

## Not in this module

- General rules for hard feedback: teaching-leading/giving-hard-feedback.
- Writing the criteria as levels of quality: teaching-leading/rubrics.
- Docs that answer recurring questions: teaching-leading/documentation-as-teaching.
- Longer-term guidance of a junior engineer: teaching-leading/mentoring.

## Phase 2

- **Show:** the same pull request reviewed twice, once with unlabeled comments and once with labeled, prioritized comments.
- **Sources to find:** empirical studies of code review (usefulness of comments, knowledge transfer); public engineering review guidelines.
