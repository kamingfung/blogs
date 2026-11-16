---
id: earth-data/projections
title: Projections
level: introductory
---

**Promise:** Explain what a map projection gives up, and pick one that keeps the property your figure or measurement depends on.

**Trap:** "Some projection is the undistorted one." No flat map keeps area, shape and distance at once; each projection chooses which to keep, and the default web map keeps shape at the cost of area.

**Assumes:** Knowing that a location can be given as longitude and latitude. earth-data/geopandas-basics helps but is not required.

## Outline

1. **Peeling an orange**: a sphere cannot lie flat without stretching or tearing, so every projection distorts something; the Tissot circles idea shows where and how much.
2. **Three things to keep**: equal-area projections keep area, conformal ones keep local angles and shape, equidistant ones keep distance from a point or along a line; none keeps all three.
3. **Geographic and projected coordinates**: degrees on an ellipsoid versus meters on a plane; a datum (such as WGS 84) fixes where the ellipsoid sits, a projection flattens it; EPSG codes name the pair [verify].
4. **Choosing**: equal-area for anything colored by amount or density, conformal (such as UTM for a small area) for local measurement and navigation, a compromise projection such as Robinson for a world overview; pyproj's `CRS` and `Transformer` do the conversion.
5. **What this means for you**: the area of a field or a farm block from GPS points is only right in an equal-area or a local projected CRS; computed in degrees or Web Mercator it is wrong, and the error grows with distance from the equator.
6. **Key takeaways**

## Key takeaways

- Every flat map distorts at least one of area, shape and distance.
- Web Mercator, used by most web tile maps, inflates areas by roughly the square of the scale factor, which grows away from the equator [verify].
- An area computed from longitude and latitude in degrees has no physical unit and cannot be converted to hectares by one constant.
- A UTM zone keeps distortion small within its own 6-degree band and grows outside it [verify].

## Not in this module

- earth-data/geopandas-basics: the mechanics of `to_crs` and measuring areas in a GeoDataFrame.
- earth-data/cartopy: drawing data on a projected map.
- earth-data/an-atlantic-centred-map: moving the seam of a world map in ggplot2.
- earth-data/choropleth-pitfalls: why an equal-area base matters for a choropleth.

## Phase 2

- **Show:** the same set of equal circles on the globe drawn on Mercator, an equal-area projection and Robinson side by side.
- **Sources to find:** a cartography textbook on projection properties; PROJ and pyproj documentation; the EPSG registry entries named.
