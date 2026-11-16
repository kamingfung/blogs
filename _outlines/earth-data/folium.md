---
id: earth-data/folium
title: folium
level: introductory
---

**Promise:** Build an interactive web map in folium with a basemap, layers, popups and a layer switch, and save it as one HTML file.

**Trap:** "Coordinates go in as (x, y), the same as everywhere else." folium's own calls such as `Marker` take [latitude, longitude], while GeoJSON and shapely use (longitude, latitude); swapping them puts points in the wrong hemisphere or the ocean.

**Assumes:** Some Python. earth-data/geopandas-basics helps; it is not listed in the series file (see the report).

## Outline

1. **A map is a page**: `folium.Map` writes Leaflet HTML and JavaScript; tiles come from a server, your data are embedded in the page.
2. **Points and the order trap**: `Marker`, `CircleMarker`, popups and tooltips; the [latitude, longitude] order for folium calls versus (longitude, latitude) in GeoJSON.
3. **Shapes from a GeoDataFrame**: `GeoJson` with `style_function` and `GeoJsonTooltip`, data in EPSG:4326, and `GeoDataFrame.explore` as the shortcut that wraps the same calls [verify].
4. **Layers and basemaps**: `TileLayer` choices and their attribution, `FeatureGroup` and `LayerControl` to switch layers, and saving with `save`.
5. **What this means for you**: a field-operations map of blocks, sensors or sampling points with a tooltip on each is a quick folium page; keep the analysis in the notebook and the map for looking up places.
6. **Key takeaways**

## Key takeaways

- folium's `Marker` and `Map(location=...)` take [latitude, longitude], the reverse of GeoJSON's coordinate order.
- folium expects vector data in longitude-latitude (EPSG:4326) and does not reproject a GeoJSON layer given in another CRS [verify].
- The web tiles under a folium map are Web Mercator, so areas on the map are not comparable across latitudes [verify].
- Every vector layer is embedded in the saved HTML, so the file grows with the number and detail of the shapes.

## Not in this module

- earth-data/mapping-pm2-5-by-county: a choropleth with `explore()` and cutting the embedded GeoJSON to a publishable size.
- earth-data/choropleth-pitfalls: what the colors on the map should encode.
- earth-data/cartopy: static, projected maps for papers and reports.
- earth-data/projections: why the web basemap distorts area.

## Phase 2

- **Show:** two markers built from the same coordinate pair, one in the right place and one flipped by the order swap.
- **Sources to find:** folium and Leaflet documentation; the GeoJSON specification on coordinate order; tile-provider attribution terms.
