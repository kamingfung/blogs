# Notebook tutorial posts

Reached from skill `scientific-blog-writing`. Read it before writing a post that has code. The blog is a Quarto site (`_quarto.yml`); a post with code is a Jupyter notebook (`.ipynb`), a prose post is a `.qmd` file.

## Location

```
blogs/<topic-slug>/<descriptive_name>.ipynb   # code post, with its data and images beside it
blogs/<slug>.qmd                              # prose post
```

After creating the file, register it in the matching `series/*.yml`; copy the form of a neighboring entry. The sidebar and the series pages are generated from those files, so never edit `_sidebar.yml`.

## Cell order

1. **Raw cell: front matter.** YAML with `title`, `description`, `date` and `categories`. Quarto takes the page title from it, so the notebook has no `# H1` cell.
2. **Markdown: TL;DR.** A `::: {.callout-note appearance="simple" icon=false}` block with a `## TL;DR` heading: what the reader learns and why it matters.
3. **Markdown: concept.** Explain the key concept before any code. Use plain language; define jargon inline.
4. **Code: imports.** All imports in one cell at the top. Keep `%pip install` out of the notebook; name any uncommon package in the prose.
5. **Markdown: the data.** Describe the dataset: source, time range, what each column means. Cite the source (URL or institution).
6. **Code: load and inspect.** Show `.head()` or `.describe()` so the reader sees the shape.
7. **Repeat: markdown explains, then code demonstrates,** for each concept step.
8. **Markdown: interpretation.** What the output means and what the reader should take away.
9. **Markdown: summary.** A bullet recap, with optional next steps or related posts.

## Rules

- **Real data only:** fetch from a public URL or embed verified values. Factual topics never use randomly generated data.
- **Self-contained:** the notebook runs top to bottom using only files in its own `blogs/<topic-slug>/` directory. The one outside import is the site's color module, `tools/fallcolor.py`.
- **Pre-executed:** `_quarto.yml` sets `execute: enabled: false`, so the site shows the committed cell outputs and never runs a cell. Run the notebook and commit it with its outputs.
- **Code folds by itself:** the site sets `code-fold: true`, so every code cell renders collapsed under "Show code". Do not wrap notebook code in `<details>` or a collapsed callout.
- **pandas-first:** use `pandas` for data wrangling unless another library is clearly better.
- **One concept per plot:** each figure shows exactly one idea, with a title, axis labels and units.
- Call `plt.show()`; do not use inline magic such as `%matplotlib inline`.
