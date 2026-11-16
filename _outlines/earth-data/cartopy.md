---
id: earth-data/cartopy
title: Cartopy
level: intermediate
---

**Promise:** Put gridded and point data on any projection with Cartopy and have it land in the right place, with no seam and readable gridlines.

**Trap:** "The projection argument tells Cartopy where my data are." `projection` sets the map; `transform` states the coordinate system of the data, and leaving it out draws longitudes and latitudes as if they were map coordinates.

**Assumes:** earth-data/projections (what a projection keeps); earth-data/python-basics-for-mapping (a first Cartopy map).

## Outline

1. **Two coordinate systems on one axes**: a GeoAxes made with `plt.axes(projection=...)` has the map's CRS; every plot call takes `transform=` for the data's CRS, usually `ccrs.PlateCarree()` for longitude and latitude.
2. **Gridded fields**: `pcolormesh` versus `contourf`, why `pcolormesh` wants cell edges, and closing the gap at the date line with `add_cyclic_point` [verify].
3. **Regions and context**: `set_extent` for a regional map, `coastlines` and `add_feature` for borders and land, and a projection centered on the region rather than the world.
4. **Gridlines and labels**: `gridlines(draw_labels=True)` and which projections can label their own lines [verify].
5. **What this means for you**: a regional map of a forecast, an anomaly or a pollutant field uses exactly these calls; the `transform` check is the one that catches a map that looks fine and is wrong.
6. **Key takeaways**

## Key takeaways

- On a non-PlateCarree map, omitting `transform=ccrs.PlateCarree()` places longitude-latitude data at the wrong locations without raising an error.
- A global field on a 0 to 360 longitude grid shows a blank strip at the seam until a cyclic point is added [verify].
- `projection` and `transform` take the same kind of object but answer different questions: where the map is drawn and where the data live.
- Not every Cartopy projection supports labeled gridlines [verify].

## Not in this module

- earth-data/python-basics-for-mapping: the first CESM map; this module assumes it.
- earth-data/projections: choosing which projection to use.
- earth-data/an-atlantic-centred-map: the ggplot2 way to move the seam.
- earth-data/colorbars and earth-data/sequential-diverging-categorical: the color scale on the map.
- earth-data/folium: interactive web maps.

## Phase 2

- **Show:** the same point set drawn on an Orthographic map twice, with and without `transform`, so the misplacement is visible.
- **Sources to find:** Cartopy documentation on projections, transforms and gridliners; Matplotlib pcolormesh documentation.
