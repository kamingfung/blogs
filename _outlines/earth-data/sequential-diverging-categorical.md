---
id: earth-data/sequential-diverging-categorical
title: Sequential, diverging, categorical
level: introductory
---

**Promise:** Pick the palette type a variable needs from what its numbers mean, and center a diverging scale on the value that matters.

**Trap:** "A diverging palette suits any map because it shows more contrast." A diverging palette claims the data have a meaningful middle; on a variable without one, or with the middle off center, it invents a split that is not there.

**Assumes:** Making a plot in Matplotlib or ggplot2.

## Outline

1. **Three questions about the data**: are the values ordered, do they have a meaningful midpoint, are they classes without order; the answers pick sequential, diverging or categorical. Cyclic palettes cover direction and phase.
2. **Sequential**: one hue or a lightness ramp from low to high; for concentrations, totals and probabilities.
3. **Diverging and its midpoint**: for anomalies, differences and changes; the midpoint must sit on zero or the stated threshold, with Matplotlib's `TwoSlopeNorm` or `CenteredNorm` [verify] or symmetric limits in ggplot2.
4. **Categorical**: distinct hues of similar lightness for unordered classes, and a limit on how many classes the eye can tell apart [verify]; land cover, soil type, crop variety.
5. **What this means for you**: a temperature map and a temperature anomaly map need different palettes; a forecast anomaly or a model-minus-observation map is diverging, centered on zero.
6. **Key takeaways**

## Key takeaways

- A diverging palette is right only when the data have a meaningful midpoint, such as zero for an anomaly.
- A diverging palette with asymmetric limits and no centering norm puts the neutral color on a value other than the midpoint.
- Categorical palettes stop being readable beyond roughly eight to ten classes [verify].
- Absolute values of a positive quantity, such as a concentration, call for a sequential palette.

## Not in this module

- earth-data/colourblind-safe-palettes: checking that the chosen palette is readable for everyone.
- earth-data/colorbars: breaks, bins and out-of-range handling in ggplot2.
- earth-data/choropleth-pitfalls: class schemes for mapped values.

## Phase 2

- **Show:** a small decision tree (ordered? midpoint? classes?) next to one example map per branch.
- **Sources to find:** ColorBrewer documentation and its paper; Matplotlib colormap and normalization documentation; a perception source on the number of distinguishable categorical colors.
