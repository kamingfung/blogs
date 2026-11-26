---
name: math-notation-standards
description: Use when writing, editing, or reviewing mathematical notation, equations, symbols, units, or LaTeX/MathJax markup in blog posts and notebooks. Covers upright vs italic conventions, subscript styling, vectors, chemical formulae, units spacing, and equation numbering.
---

# Mathematical Notation Standards

Adapted from J. E. Hoffman, *How To Write a Paper and Format it Using LaTeX*
(Harvard, 2020), Table I, translated to this site's stack: Quarto (Pandoc) + MathJax.

Inline math is `$...$`, display math is `$$...$$`. Both work in Markdown and in
notebook cells.

## The core rule

**Italic means "this is a variable." Upright means "this is a name."**

Every decision below follows from that one distinction. Getting it wrong is the
most common giveaway of unedited scientific writing, because the default in math
mode is italic — so anything that is *not* a variable has to be marked.

## Upright vs italic

| Wrong | Right | Why |
| --- | --- | --- |
| `$cos\theta$` | `$\cos\theta$` | Function names are names, not a product of `c·o·s` |
| `$T_{sample}$` | `$T_{\text{sample}}$` | "sample" is a label, not five variables multiplied |
| `$V_{rms}$`, `V (rms)` | `$V_{\text{rms}}$` | same |
| `$E_x$` for the x-component | `$E_x$` — keep `x` italic | here `x` *is* a variable, so italic is correct |
| `x direction` in prose | `$x$ direction` | a variable stays italic even mid-sentence |
| `X direction` | `$x$ direction` | and stays lowercase |
| `$dI/dV$` upright | `$dI/dV$` italic | differentials of variables are variables |

MathJax has `\cos \sin \tan \log \ln \exp \max \min \lim \det` built in. For a
function it does not know, use `\operatorname{}`:

```latex
$\operatorname{erf}(x)$        not  $erf(x)$
```

Use `\text{}` for words inside math. `\mathrm{}` also renders upright but does
not preserve spaces, so `\text{}` is the safer default.

## Vectors

Prefer **bold** over arrows:

```latex
$\mathbf{B}_{\text{app}}$      preferred
$\vec{B}_{\text{app}}$         acceptable, but be consistent
```

Pick one convention per post and hold it. Mixing bold and arrows in one document
reads as careless.

## Chemical formulae

Subscript the stoichiometry, and keep element symbols upright:

```latex
$\text{Sb}_2\text{Te}_3$                      not  Sb2Te3
$\text{Sb}_{2-x}\text{V}_x\text{Te}_3$        note x italic, it is a variable
$\text{PM}_{2.5}$                             not  PM2.5
```

## Numbers and units

**Always a space between the number and its unit** — a thin space in math:

```latex
$B = 5\,\text{T}$              not  $B = 5T$  or  $B=5T$
$T = 300\,\text{K}$            not  300K
$15\text{–}30\,\text{min}$
```

Every number in a post should carry a unit unless it is genuinely
dimensionless. Check that equations are dimensionally consistent before
publishing.

Ordinals are not superscripts: write `1st`, `2nd` — never `1ˢᵗ`.

## Equations

- **Number equations you refer to later**; leave one-off equations unnumbered.
- Number the *equation*, not each line of a multi-line equation.
- Define every symbol in the surrounding prose or in a previous equation. A
  symbol that appears only inside display math is undefined to the reader.
- For an equation mid-paragraph, keep the prose flowing around it — do not start
  a new logical paragraph just because a display equation intervened.

Multi-line, aligned on the relation:

```latex
$$
\begin{aligned}
d &= \sqrt{a^2 + b^2 + c^2} \\
  &= \sqrt{3^2 + 4^2 + 12^2} = 13
\end{aligned}
$$
```

### Equation numbering

Use Quarto cross-references, not `\label` and `\eqref`:

```markdown
$$
a^2 + b^2 = c^2
$$ {#eq-pythag}

See @eq-pythag.
```

The label must start with `eq-`. Quarto numbers the equation and renders the reference as "Equation 1". Manual `\tag{1}` also works and is what the older posts use; do not mix the two in one post.

## Reviewing a post

Audit only real math spans — `$...$` and `$$...$$` with fenced code stripped
first, or Python identifiers like `X_train` produce a flood of false positives.
Check for:

- function names without a backslash
- descriptive subscripts not wrapped in `\text{}`
- numbers adjacent to unit letters
- mixed vector conventions within one post
- symbols used in display math but never defined in prose
