---
id: earth-data/regridding-in-python-with-xesmf
title: Regridding in Python with xESMF
level: intermediate
---

**Promise:** Regrid an xarray Dataset with xESMF using the method the field needs, reuse the weights, and confirm the result with one check.

**Trap:** "Cell centers are all xESMF needs." Conservative remapping works on cell areas, so it needs cell corners (bounds); without them the call fails or uses bounds someone guessed.

**Assumes:** earth-data/dimensions-coordinates-and-attributes; earth-data/conservative-vs-bilinear (which method a field needs, and why).

## Outline

1. **From a method choice to a call**: the decision is already made in conservative-vs-bilinear; here it becomes `xesmf.Regridder(source, target, method)`, with the method names bilinear, conservative, conservative_normed, nearest_s2d and patch [verify].
2. **Grids and their corners**: what `lat_b` and `lon_b` hold, how to build a target grid with `xesmf.util.grid_global` or by hand, and how to add bounds to a file that lacks them, for example with cf_xarray [verify].
3. **Weights are the expensive part**: the Regridder computes a sparse weight matrix once; save it to a file and reload it to regrid many variables and many years on the same grid pair.
4. **Edges, seams and missing values**: `periodic=True` for global grids that wrap in longitude; masks for land or ocean; how NaN in the source spreads into the target and what `conservative_normed` changes [verify].
5. **What this means for you**: putting a climate-model or reanalysis field onto the grid of a crop map, an air-quality model or a forecast product is this call; the global-sum check from conservative-vs-bilinear is the one-line test that it went right.
6. **Key takeaways**

## Key takeaways

- A conservative Regridder needs cell bounds on both grids; a bilinear one needs only centers [verify].
- Building the weights takes most of the run time, so a saved weights file makes repeat regridding on the same grid pair fast.
- Without `periodic=True`, bilinear regridding of a global field leaves a strip of missing or wrong values at the longitude seam [verify].
- A conservatively regridded flux keeps its area-weighted global total to rounding error, and that sum is the check.

## Not in this module

- earth-data/conservative-vs-bilinear: why the field type decides the method; this module does not argue it again.
- earth-data/regridding-crop-data-for-climate-models: the same task in R with terra, for per-cell totals.
- earth-data/dask-and-chunking: regridding data larger than memory.
- earth-data/rasterio: reprojecting single-band GeoTIFF rasters, which uses a different tool.

## Phase 2

- **Show:** one source cell outlined on top of the target grid, with the overlap areas that become its row of weights.
- **Sources to find:** xESMF documentation and its paper or software citation; ESMF regridding method documentation; cf_xarray bounds documentation.
