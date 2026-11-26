---
name: scientific-blog-writing
description: Use when drafting, editing, formatting, reviewing, or structuring scientific and technical blog posts, writing research summaries, crafting concise and punchy TL;DRs, sizing figures/tables, or adapting scientific literature for accessible online presentation.
---

# Scientific Blog Writing: Nature-Adapted Standard

## Overview

This skill adapts the editorial and formatting rigor of the ***Nature* Author Guidelines** into an actionable standard for scientific, technical, and data science blog posts (`.qmd` files and Jupyter notebooks on a Quarto site).

The core philosophy is **broad interdisciplinary accessibility without loss of technical precision**: make complex science immediately intelligible to curious readers outside the specific subfield while maintaining publication-grade clarity, reproducible methods, and rigorous attribution.

---

## When to Use

- Writing or scaffolding a new prose (`.qmd`) or notebook (`.ipynb`) blog post. For a notebook post, read [references/notebook-tutorial.md](references/notebook-tutorial.md) first.
- Editing or reviewing an existing post for narrative flow, structure, and visual clarity.
- Crafting a concise, punchy TL;DR lead block that hooks readers with the core payoff upfront.
- Formatting display items (figures, multi-panel plots, comparison tables) with self-contained legends.
- Packaging code, mathematical formulations, and data availability blocks for full reproducibility.

**VOICE & PERSONA:** Pair with the `author-persona-voice` skill to match Ka Ming (Victor) Fung's authentic voice, pragmatic tone, and domain background.

---

## The Concise & Punchy TL;DR Formula

Every scientific blog post must open with a **concise, high-impact TL;DR** (50–90 words, 2–3 sentences or a crisp 3-bullet callout) rather than a slow, dense academic abstract. Readers scan web content and need to know the core finding, mechanism, and practical value immediately:

```
[1. The Problem / Hook] ───► [2. The Key Finding & Approach] ───► [3. The Practical Takeaway]
```

| Component | Target Length | Purpose & Guiding Question | Example Sentence |
|---|---|---|---|
| **1. The Problem / Hook** | 1 sentence | State the technical bottleneck, paradox, or limitation directly without fluff. | *Recursive forecasting with tree-based models suffers from severe error compounding over multi-week horizons.* |
| **2. Key Finding & Approach** | 1–2 sentences | Deliver the concrete discovery, benchmark metric, or methodology. | *In this post, we benchmark direct vs recursive multi-step forecasting with LightGBM in Darts, showing that direct horizon mapping cuts 14-day RMSE by 31%.* |
| **3. Practical Takeaway** | 1 sentence | State what the reader gains, the actionable advice, or reproducible code. | *Use `output_chunk_length = H` for seasonal time series; pre-executed code and training matrix inspections are provided below.* |

See [references/punchy-tldr-formula.md](references/punchy-tldr-formula.md) for complete domain examples (climate, ML, computer vision) and formatting templates.

---

## Core Editorial Guidelines (Retrofitted from Nature)

### 1. Title Crafting
- **Length**: Strict maximum of **75 characters** (including spaces). Fits comfortably on 2 lines on mobile and search cards.
- **Tone**: Informative, active, and accessible. Avoid niche jargon, raw acronyms, and unneeded punctuation.
- **Formula**: `[Active Verb / Question / Concept] + [Specific Domain or Insight]`
  - ❌ *A Novel PyTorch Implementation of Deep Residual GBDT Ensemble Architectures for Detrending Sub-Daily Meteorological Time Series* (121 chars)
  - ✅ *Detrending Extreme Temperatures with Residual Gradient Boosting* (64 chars)

### 2. Subheadings & Section Architecture (The 5 Post Archetypes)
To avoid repetitive, cookie-cutter post structures, select one of **5 distinct archetypes** based on content domain and rotate across them:

1. **Empirical Benchmark & Algorithmic Deep-Dive** (ML, time-series, algorithms):
   - *Flow*: Punchy TL;DR $\to$ The Algorithmic Dilemma $\to$ Mermaid Architecture Flow $\to$ LaTeX Math Formulation $\to$ Collapsible Production Code (collapsed callout) $\to$ Empirical Benchmark Table $\to$ Practical Engineering Advice & GitHub Repo.
2. **Scientific Discovery & Earth System Impact** (Atmospheric chemistry, climate, health):
   - *Flow*: Punchy TL;DR $\to$ Epigraph $\to$ Environmental Triad (Mermaid) $\to$ Missing Molecular Mechanism $\to$ Global Model Results Table $\to$ Interactive Policy / Parameter Sandbox $\to$ Strategic Policy & SDGs $\to$ Formal References.
3. **Intuitive First-Principles Explainer** (Physics, acoustics, thermodynamics, biology):
   - *Flow*: Punchy TL;DR $\to$ Thought Experiment / Master Analogy $\to$ First-Principles Equations with Derivation Steps $\to$ Analytical Visual Landscape (Theme-Aware SVG / Math Canvas) $\to$ Interactive Hands-on Sandbox $\to$ Real-World Applications Matrix $\to$ Macro Journey.
4. **Developer Tooling & Practical Case Study** (IDE workflows, typing, agent harnesses):
   - *Flow*: Punchy TL;DR $\to$ The "War Story" / Frustrating Bug Hook $\to$ Root Cause Code Diff $\to$ Architectural Solution Flow $\to$ Step-by-Step Configuration Recipe (IDE JSON / CLI) $\to$ "3 Things You Can Do This Week" Checklist.
5. **Interactive Geospatial & Data Science Tutorial** (NetCDF, Xarray, GeoPandas, R spatial):
   - *Flow*: Punchy TL;DR $\to$ Geospatial Pipeline Flowchart $\to$ Prerequisites Setup $\to$ Modular Step-by-Step Code Stages with Visual Map Previews $\to$ Performance Tips & CRS Gotchas $\to$ Downloadable Assets.

See [references/post-templates.md](references/post-templates.md) for full Markdown scaffolding and archetypal blueprints.

### 3. Readability & Interdisciplinary Accessibility
- **Specialized Terms**: Define them at first mention concisely, without breaking narrative momentum (e.g., *"We use eddy covariance—a statistical method that measures vertical turbulent fluxes across the boundary layer..."*).
- **Standard Nomenclature**: Use recognized scientific symbols, IUPAC chemical names, and standard unit abbreviations (SI units).
- **Abbreviations**: Spell out acronyms at first use unless universally recognized (e.g., DNA, NASA, CPU).

### 4. Visual Diagrams & Flowcharts
In addition to static figures, use rich, web-native diagrams to explain architectures and pipelines:
- **Mermaid Diagrams**: Use `{mermaid}` code fences, with the braces, for flowcharts, state transitions, and sequence flows. A plain ` ```mermaid ` fence renders as a code listing, not a diagram:
  ```markdown
  ```{mermaid}
  graph LR
      A[Raw Data] --> B[Feature Pipeline]
      B --> C[Direct Multi-Horizon Model]
      C --> D[Forecast Evaluation]
  ```
  ```
- **Semantic Inline SVG**: For custom physical schematics, coordinate systems, or multi-state systems with exact styling, dark/light theme awareness, and responsive sizing (`width="100%" viewBox="..."`).
- **HTML/CSS Process Cards**: For multi-stage algorithmic pipelines, comparison matrix cards, or clean step-by-step workflow boxes using flexbox/grid containers.

### 5. Interactive Plots & Visual Sandboxes
Where static plots only convey a snapshot, interactive elements enable readers to explore parameter spaces:
- **Interactive HTML5 / JS Sandboxes**: Inline `<canvas>` or vanilla JS widgets with interactive sliders (e.g. tuning learning rates, physical parameters, orbital mechanics, or synthesizers).
- **Plotly & Vega-Lite**: Interactive zoomable charts and multidimensional datasets embedded via HTML/JS or iframe components.
- **Self-Contained Figure Captions**: Follow the Nature standard with a bold title, panel indicators (`a`, `b`), and uncertainty ribbons.

### 6. Collapsible Code Blocks (Maximize Readability)
To ensure technical posts read as engaging scientific narratives rather than endless code dumps:
- **Notebook code cells fold by themselves**: the site sets `code-fold: true`, so each code cell renders collapsed under "Show code". Add no wrapper.
- **Collapse static code in prose posts**: multi-line boilerplate, data ingestion, hyperparameter dictionaries, and plotting scripts shown as a plain fence in a `.qmd` file go in a collapsed callout:
  ```markdown
  ::: {.callout-note collapse="true"}
  ## View implementation code (Python)

  ```python
  import numpy as np
  import pandas as pd
  # Full implementation details
  ```
  :::
  ```
- **Keep Minimal Snippets Inline**: Only display 2–4 line critical equations, core logic steps, or API call signatures inline in the main prose.

### 7. Mathematical Formulations (MathJax & LaTeX)
- Display equations using `$$...$$`. Number an equation you refer to later with a Quarto label (`$$ ... $$ {#eq-name}`, cited as `@eq-name`); skill `math-notation-standards` has the notation rules.
- Define every variable immediately after the equation:
  $$T_e = \left( \frac{S_0 (1 - \alpha)}{4 \sigma} \right)^{1/4}$$
  where $S_0$ is the solar constant ($1361\text{ W m}^{-2}$), $\alpha$ is planetary albedo ($0.30$), and $\sigma$ is the Stefan-Boltzmann constant ($5.67 \times 10^{-8}\text{ W m}^{-2}\text{ K}^{-4}$).

### 8. Reproducibility, Code & Data Statements
Always include a clear data & code availability statement at the conclusion of the post:
```markdown
## Data and Code Availability

- **Interactive Notebook**: The complete, pre-executed Jupyter Notebook is in the blog repository at `blogs/climate/energy-balance.ipynb`.
- **Source Code**: All analysis routines, training scripts, and figure generation code are hosted on GitHub at [`kamingfung/energy-balance-models`](https://github.com/kamingfung).
- **Datasets**: Meteorological input data were retrieved from the ERA5 Reanalysis archive[^1] and processed using [`xarray`](https://docs.xarray.dev).
```

---

## Markdown Dialect: MkDocs Habits That Silently Fail Here

The site renders with **Quarto (Pandoc)**. It replaced an MkDocs Material site, and both older posts and old habits carry Python-Markdown syntax. Unsupported syntax does not error: it renders as literal text in the published post.

### Mapping

Each row was checked by rendering it with Quarto 1.10.18.

| Idiom | Works? | Use instead |
| --- | --- | --- |
| `!!! warning "Title"` admonition | **no** | `::: {.callout-warning}` with a `## Title` line inside |
| `??? note "Title"` collapsible | **no** | `::: {.callout-note collapse="true"}` |
| ` ```mermaid ` fence | **no** (code listing) | ` ```{mermaid} ` |
| `*[PM2.5]: fine particulate` abbreviation | **no** | define the term in the prose at first use |
| `[TOC]` | **no** | nothing; the site sets `toc: true` |
| `<div markdown="1">` | unnecessary | Pandoc parses Markdown inside a `<div>` already |
| `==highlight==` | **no** | `[highlight]{.mark}` |
| `[@citekey]` citation | **no** (no bibliography is configured) | `[^1]` footnote plus a `## References` section |
| `[^1]` footnote, `^[inline footnote]` | **yes** | as written |
| `{#id .class}` attributes | **yes** | as written |
| `$x$` / `$$x$$` math | **yes** | as written |
| `$$ ... $$ {#eq-name}` and `@eq-name` | **yes** | as written; the label must start with `eq-` |
| Definition list (`term` / `: def`) | **yes** | as written |
| `~~strikethrough~~`, `^superscript^`, `~subscript~` | **yes** | as written |
| Table caption (`: Caption {#tbl-name}`) | **yes** | as written; cite as `@tbl-name` |
| Raw HTML widget with blank lines inside | **no** (Pandoc ends the HTML block at the first blank line) | wrap it in a ` ```{=html} ` fence |

### Verify before publishing

Render, then confirm nothing survived into the output as literal text. Scope the scan to the page body and strip code, or the patterns match scripts and code listings:

```python
# run after `quarto render`
import glob, re
PATS = ((r'^\s*(!!!|\?\?\?)\s+\w', 'admonition'), (r'\[TOC\]', 'toc marker'),
        (r'\*\[[^\]]+\]:', 'abbreviation'), (r'\[@\w', 'citation'),
        (r'(?<![=<>!])==(?!=)\w', 'highlight'), (r'\{\{\s*\w', 'template placeholder'))
for f in sorted(glob.glob("_site/**/*.html", recursive=True)):
    h = open(f, encoding="utf-8", errors="ignore").read()
    m = re.search(r'<main\b.*?</main>', h, re.S)
    if not m:
        continue
    body = re.sub(r'<(script|style|code|pre)\b[^>]*>.*?</\1>', '', m.group(0), flags=re.S)
    body = re.sub(r'<[^>]+>', '', body)
    for pat, name in PATS:
        for mm in re.finditer(pat, body, re.M):
            print(f"{f}: unrendered {name} -> {body[mm.start():mm.start()+40]!r}")
```

Expect a few legitimate hits from notebook output: plotly `hovertemplate` strings contain `{{x:.1f}}`, for instance. Anything in prose is a rendering bug, not a style question.

## Quick Reference Checklist

Before publishing any blog post, run this pre-flight check:

- [ ] **Title**: $\le 75$ characters, free of opaque acronyms.
- [ ] **TL;DR**: Concise and punchy (50–90 words / 2–3 sentences) hook delivering immediate finding, mechanism, and practical value upfront.
- [ ] **Subheadings**: All $\le 40$ characters, logical hierarchy (H2/H3).
- [ ] **Code Readability**: Lengthy implementation, data processing, and plotting code are folded: notebook cells by the site's `code-fold`, static code in a collapsed callout.
- [ ] **Diagrams & Visuals**: Flowcharts (Mermaid/SVG), interactive sandboxes/Plotly, and self-contained figure captions with bold titles.
- [ ] **Math**: Variables fully defined upon introduction; proper MathJax/LaTeX syntax.
- [ ] **Citations**: In-text numbered footnotes (`[^1]`) formatted in Nature style with DOIs.
- [ ] **Notebook Hygiene**: If `.ipynb`, pre-executed locally before commit (`execute: enabled: false` in `_quarto.yml`).
- [ ] **Navigation**: Entry registered in the matching `series/*.yml` (never edit the generated `_sidebar.yml`).
