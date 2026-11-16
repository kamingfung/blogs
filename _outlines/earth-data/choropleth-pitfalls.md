---
id: earth-data/choropleth-pitfalls
title: Choropleth pitfalls
level: introductory
---

**Promise:** Spot the four common ways a choropleth misleads, and fix each one before the map is published.

**Trap:** "The darkest region on the map has the biggest problem." The eye reads ink by area, so a large sparse county outweighs a small dense one; what the color encodes and how it is binned decide the story.

**Assumes:** Reading a colored map. earth-data/geopandas-basics helps for following the examples.

## Outline

1. **Ink follows area, not people**: big rural units dominate the picture whatever their values; name the problem, and mention alternatives such as a cartogram or a dot-density map.
2. **Counts versus rates**: a map of raw counts mostly redraws population; divide by population or area first, and say which denominator.
3. **Small numbers make loud rates**: a unit with few people swings to the extremes by chance, so the most extreme colors often belong to the smallest units; show the count or a confidence note next to the rate.
4. **Binning writes the story**: equal-interval, quantile and natural-breaks classes on the same data give different maps; mapclassify's `EqualInterval`, `Quantiles` and `FisherJenks` [verify], and how to report the scheme.
5. **What this means for you**: a county PM2.5 map or a regional yield map is a choropleth; check the four pitfalls before it goes into a report, and say in the caption which unit, denominator and class scheme it uses.
6. **Key takeaways**

## Key takeaways

- A choropleth of raw counts is close to a population map for most human-related variables.
- The same data classed by quantiles and by equal intervals can put a given unit in different color classes.
- In a rate map, the units with the smallest populations are the most likely to show the most extreme rates.
- Results drawn on aggregation units change when the boundaries change, the modifiable areal unit problem [verify].

## Not in this module

- earth-data/mapping-pm2-5-by-county: building the county map itself.
- earth-data/sequential-diverging-categorical: which palette type the values need.
- earth-data/colourblind-safe-palettes: making the classes readable for everyone.
- earth-data/projections: why the base map should be equal-area.

## Phase 2

- **Show:** one dataset drawn four times, raw counts, rates, rates by quantiles and rates by equal intervals, so the reader sees the story change.
- **Sources to find:** a cartography text on choropleth design; mapclassify documentation; a primary source on the small-numbers problem in rate maps and on the modifiable areal unit problem.
