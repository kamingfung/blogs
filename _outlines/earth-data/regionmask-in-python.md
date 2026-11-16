---
id: earth-data/regionmask-in-python
title: regionmask in Python
level: intermediate
---

**Promise:** Average a gridded field over countries, states or any set of polygons in Python, with area weights and a stated rule for border cells.

**Trap:** "A regional mean is the plain mean of the grid cells inside the polygon." On a latitude-longitude grid cells shrink toward the poles, and a border cell is either in or out unless you ask for fractions; both choices move the answer.

**Assumes:** earth-data/geopandas-basics (polygons, CRS); earth-data/dimensions-coordinates-and-attributes (selection and reductions in xarray).

## Outline

1. **A region label for every cell**: the same problem the R module solves with a point-in-polygon test, done with regionmask; a mask is a grid of region numbers or a stack of true/false layers.
2. **Where regions come from**: built-in sets such as Natural Earth countries and the IPCC AR6 regions [verify], and any GeoDataFrame through `regionmask.from_geopandas`.
3. **Two-dimensional and three-dimensional masks**: `mask` gives one integer per cell; `mask_3D` gives one boolean layer per region and makes all regional means one weighted reduction.
4. **Weights and border cells**: weight by the cosine of latitude or by true cell area with xarray's `weighted`; compare the cell-center rule with fractional overlap (`mask_3D_frac_approx`) [verify] for small regions on a coarse grid.
5. **What this means for you**: state-level air-quality averages and growing-region climate summaries are this calculation; for a region only a few cells wide, state the border rule next to the number.
6. **Key takeaways**

## Key takeaways

- An unweighted regional mean on a latitude-longitude grid over-weights the poleward cells of the region.
- By default regionmask assigns a cell to a region when the cell center falls inside the polygon [verify].
- For a region a few grid cells across, the center rule and fractional overlap can give regional means that differ by more than the signal of interest [verify].
- A three-dimensional mask turns the mean over every region into one weighted reduction over latitude and longitude.

## Not in this module

- earth-data/regional-analysis-r: the same job in R with GADM polygons and sp.
- earth-data/geopandas-basics: reading polygons and checking their CRS.
- earth-data/regridding-in-python-with-xesmf: changing the grid before or after masking.
- earth-data/choropleth-pitfalls: how to map the regional results without misleading.

## Phase 2

- **Show:** a coarse grid over one small irregular region, with cells colored by center-in, partly-in and out, and the regional mean under each rule.
- **Sources to find:** regionmask documentation and software paper; the AR6 reference-region definition; xarray weighted-reduction documentation.
