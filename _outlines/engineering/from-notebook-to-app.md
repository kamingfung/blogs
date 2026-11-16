---
id: engineering/from-notebook-to-app
title: From notebook to app
level: introductory
---

**Promise:** Turn an analysis notebook into a small interactive app that a colleague can use without reading or running the code.

**Trap:** "An app is the notebook with sliders added." An app reruns from the top on every interaction, so hidden notebook state, slow cells and hard-coded inputs break it; the work is separating inputs, computation and display.

**Assumes:** Some Python and notebook experience; no prior module.

## Outline

1. **Who the app is for**: a notebook serves its author; an app serves someone who will only change inputs and read outputs. Decide the two or three inputs and the one answer they need before writing anything.
2. **The rerun model**: in Streamlit the whole script runs again on each widget change [verify]. Explain what that means for slow data loads and for variables that a notebook kept alive between cells.
3. **Separate the three layers**: move the computation into plain functions that take inputs and return results; the app file only reads widgets, calls functions and draws. The same functions stay testable and reusable from a script.
4. **Make it fast enough**: cache data loading and expensive computation, keyed on the inputs [verify]; show progress for anything slow; refuse inputs outside the range the analysis supports instead of failing late.
5. **Say what the numbers mean**: label units, state the data source and its date, and state the assumptions the model ignores (the investment comparator's "directional, not to the cent" note is the pattern).
6. **What this means for you**: a weekly forecast often ends as a static chart pasted into a message; a small app over the same functions lets a planner change one input and see the effect, but only if the forecast logic lives in functions, not in notebook cells.

## Key takeaways

- An app framework that reruns the script on every interaction exposes any hidden state a notebook was relying on [verify].
- Moving computation into pure functions is the main step; the app layer should be thin enough to rewrite in another framework in an afternoon.
- Caching keyed on inputs is what makes a rerun-on-every-click app usable on real data [verify].
- An app without stated units, data date and assumptions invites users to read it more precisely than it deserves.

## Not in this module

- Putting the app on a server others can reach: engineering/deploying-a-streamlit-app.
- A finished example of such an app: engineering/total-return-and-reinvested-dividends.
- Why notebook state is risky in general: engineering/notebooks-vs-scripts.
- Pinning the environment the app runs in: engineering/environments-that-don-t-break.

## Phase 2

- **Show:** a three-box diagram (inputs, functions, display) with the same notebook cells sorted into each box.
- **Sources to find:** official Streamlit documentation on its execution model and caching; documentation of one alternative app framework for contrast.
