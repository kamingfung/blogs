---
id: earth-data/colourblind-safe-palettes
title: Colourblind-safe palettes
level: introductory
---

**Promise:** Check any figure for color-vision deficiency and grayscale, and replace a failing palette with one that works.

**Trap:** "A rainbow colormap with a legend is fine for everyone." Rainbow maps such as jet put red next to green and change lightness unevenly, which hides differences from many readers and invents boundaries for all of them.

**Assumes:** Making a plot in Matplotlib or ggplot2.

## Outline

1. **Who sees what**: the common forms of color-vision deficiency, and how often they occur in men and in women [verify]; red-green confusion is the most frequent.
2. **Lightness carries the order**: a palette reads in order only if lightness rises steadily; rainbow maps have bright bands that look like fronts in the data.
3. **Test, do not guess**: simulate deficiency and grayscale on the finished figure, for example with colorspacious or a browser or OS simulator [verify]; check a print in black and white.
4. **Palettes that pass**: viridis and cividis in Matplotlib and ggplot2, Crameri's scientific colormaps (cmcrameri), the Okabe-Ito set for categories [verify]; and always a second encoding (marker, line style, direct label).
5. **What this means for you**: a red-for-bad, green-for-good dashboard or field map is the classic failure; keep the meaning but add a symbol or label and move to a palette that passes the simulation.
6. **Key takeaways**

## Key takeaways

- About 1 in 12 men and 1 in 200 women have a color-vision deficiency [verify].
- A colormap whose lightness changes unevenly creates visible bands where the data change smoothly.
- viridis and cividis keep a monotonic lightness ramp and stay readable under the common forms of color-vision deficiency [verify].
- A figure that uses color as its only encoding fails for some readers whatever the palette.

## Not in this module

- earth-data/sequential-diverging-categorical: which kind of palette the data call for.
- earth-data/colorbars: binning, limits and breaks of a ggplot2 color scale.
- earth-data/choropleth-pitfalls: what the colors encode and how they are binned.

## Phase 2

- **Show:** one temperature field drawn with jet and with viridis, each beside its simulated deuteranopia and grayscale versions.
- **Sources to find:** a vision-science source on color-vision deficiency prevalence; the papers or documentation behind viridis, cividis, Crameri's colormaps and the Okabe-Ito palette.
