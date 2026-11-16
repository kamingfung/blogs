---
id: engineering/deploying-a-streamlit-app
title: Deploying a Streamlit app
level: introductory
---

**Promise:** Put a working Streamlit app on a URL other people can open, with pinned dependencies, secrets kept out of the code, and a plan for when it breaks.

**Trap:** "It runs on my laptop, so deploying is just uploading it." Deployment fails on what your laptop provided silently: installed packages, local files, credentials in environment variables and a machine that never sleeps.

**Assumes:** engineering/from-notebook-to-app.

## Outline

1. **What changes between laptop and server**: a clean machine with only declared dependencies, no access to your files, a different operating system, limited memory, and possibly many users at once. List each as a question to answer before deploying.
2. **Choosing where it runs**: a free community host, a general app platform, or a container on your own infrastructure. Compare on cost, privacy of data, sleep or cold-start behavior and who can see it [verify].
3. **Dependencies and data**: deploy from a lock file so the server builds the same environment; decide whether data ships with the app, loads from a URL, or comes from a database, and how fresh it must be.
4. **Secrets and access**: API keys and passwords go into the platform's secret store, never into the repository; decide who may open the app and whether it needs sign-in.
5. **Keeping it alive**: deploy from a branch so a merge redeploys; watch logs; pin the framework version so an upstream release does not break the app overnight [verify].
6. **What this means for you**: a forecast app that a planning team opens every Monday must load the latest run, say which run it shows, and fail visibly when the data is stale, rather than quietly serving last week's numbers.

## Key takeaways

- Most first deployment failures come from undeclared dependencies or local file paths, not from the app code.
- Secrets committed to a repository should be treated as leaked and rotated, even after the commit is removed.
- Free hosting tiers commonly put idle apps to sleep, so the first user after a quiet period waits for a cold start [verify].
- An app that shows data should display the data's date, so a stale deployment is visible to the user.

## Not in this module

- Structuring the notebook into an app: engineering/from-notebook-to-app.
- Lock files and reproducible environments in depth: engineering/environments-that-don-t-break.
- Branch-based workflows and CI: engineering/git-for-a-team.

## Phase 2

- **Show:** a deployment checklist with one column for the laptop and one for the server, each row a hidden assumption.
- **Sources to find:** official deployment docs of Streamlit's community hosting and one general platform; platform documentation on secret management.
