---
name: blog-citation-manager
description: Use when adding citations, bibliographic references, footnotes, DOIs, arXiv/bioRxiv preprints, or dataset citations to blog posts or documentation.
---

# Blog Citation Manager: Academic Standards for the Quarto Blog

## Overview

This skill provides a standardized workflow for managing academic citations, digital object identifiers (DOIs), and bibliographies within Markdown and Jupyter Notebook blog posts on the Quarto site.

We use **Nature-style referencing** combined with standard **Markdown footnote syntax** (`[^1]`), delivering lightweight, interactive, and beautifully linked academic provenance without needing heavy third-party citation engines.

---

## When to Use

- Adding academic citations, papers, preprints, or datasets to a blog post.
- Formatting footnotes in Markdown or Jupyter Notebook cells.
- Converting raw BibTeX, URLs, DOIs, or author-date strings into unified Nature web reference format.
- Resolving and verifying DOI links, PubMed PMIDs, arXiv IDs, and dataset repositories (Zenodo, figshare, Dryad).

---

## Core Markdown Footnote Syntax

Quarto (Pandoc) compiles Markdown footnotes natively. The site filter `filters/dedupe-footnotes.lua` merges repeated `[^n]` references to one source into one numbered note. Pandoc citations (`[@key]`) are not set up: the site has no bibliography, so they render as literal text.

### In-Text Citation
Use square brackets with a caret followed by a unique numeric or alphanumeric tag:
```markdown
Recent studies demonstrate significant changes in urban precipitation patterns[^1] and boundary layer turbulent fluxes[^2].
```

Multiple citations together:
```markdown
Several empirical studies confirm this temperature sensitivity[^1]<sup>,</sup>[^3]<sup>,</sup>[^4].
```

### Bottom Reference List
Place references at the very bottom of the `.qmd` file under a `## References` heading:
```markdown
## References

[^1]: Fung, K. M., Val Martin, M. & Tai, A. P. K. Modeling the interannual variability of ozone air quality. *Atmos. Chem. Phys.* **21**, 3455–3470 (2021). https://doi.org/10.5194/acp-21-3455-2021
[^2]: Stull, R. B. *An Introduction to Boundary Layer Meteorology*. (Springer Netherlands, Dordrecht, 1988). https://doi.org/10.1007/978-94-009-3027-8
[^3]: Vaswani, A. et al. Attention is all you need. *Advances in Neural Information Processing Systems* **30**, 5998–6008 (2017). https://doi.org/10.48550/arXiv.1706.03762
```

---

## Nature Reference Style Rules for Web

### 1. General Rules
- **Authors**: List surname first, followed by initials (e.g., `Fung, K. M., Heald, C. L. & Kroll, J. H.`).
- **Rule of 5**: If there are 1 to 5 authors, list all of them. If there are 6 or more authors, list the first author followed by `et al.` (e.g., `Hersbach, H. et al.`).
- **Article Title**: Upright (not italicized), sentence case (only capitalize the first word and proper nouns), ending with a period.
- **Journal Title**: Italicized, abbreviated according to standard ISO4/CASSI abbreviations (e.g., *Nature*, *Science*, *Geophys. Res. Lett.*, *Atmos. Chem. Phys.*, *J. Clim.*).
- **Volume & Page Numbers**: Volume in **bold**, followed by a comma, page range or article number (e.g., **15**, 123–130).
- **Year**: In parentheses at the end of the citation `(2024)`.
- **DOI / URL**: Always provide a clickable HTTPS DOI or preprint URL (`https://doi.org/...`).

### 2. Formats by Source Type

| Source Type | Nature Style Format |
|---|---|
| **Journal Article** | `Author, A. B. & Author, C. D. Article title in sentence case. *Journal Abbr.* **vol**, pages (year). https://doi.org/...` |
| **Preprint (arXiv/bioRxiv)** | `Author, A. B. Preprint title. Preprint at *arXiv/bioRxiv* https://doi.org/... or https://arxiv.org/abs/... (year).` |
| **Book** | `Author, A. B. *Book Title in Title Case*. (Publisher, City, year). https://doi.org/...` |
| **Book Chapter** | `Author, A. B. in *Book Title* (eds Editor, C. & Editor, D.) 100–120 (Publisher, year).` |
| **Research Dataset** | `Author, A. B. Dataset Title. *Repository Name* https://doi.org/... (year).` |
| **Software / Codebase** | `Author, A. B. Software Name: Version. *Zenodo/GitHub* https://doi.org/... (year).` |
| **Web Page / Official Report** | `Organization/Author. Page or report title. *Website Name* https://url (year).` |

See [references/citation-styles.md](references/citation-styles.md) for full examples and conversion guides.

---

## Pre-Flight Citation Checklist

- [ ] All in-text citations have matching definitions in the `## References` section.
- [ ] Footnote numbering is sequential ($1, 2, 3\dots$).
- [ ] Authors with $\ge 6$ contributors are truncated using `et al.`.
- [ ] Journal names are properly abbreviated and italicized.
- [ ] Volume numbers are bolded (`**12**`).
- [ ] Every reference includes a live, resolving DOI or URL.
- [ ] Footnotes render properly when tested with `quarto preview`.
