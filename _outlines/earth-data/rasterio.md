---
id: earth-data/rasterio
title: rasterio
level: intermediate
---

**Promise:** Read a GeoTIFF with rasterio, find the place each pixel covers, cut it to a polygon, and know when a change of CRS resamples the data.

**Trap:** "A GeoTIFF is an image with longitudes and latitudes spread evenly across it." A pixel's place comes from an affine transform plus a CRS, the transform points at the pixel corner, and the CRS is often in meters, not degrees.

**Assumes:** earth-data/projections (CRS); earth-data/geopandas-basics (polygons). Neither is listed in the series file; see the report.

## Outline

1. **What is in the file**: bands, data type, `crs`, `transform`, `nodata` and the profile, read from a `rasterio.open` dataset without loading the pixels.
2. **Pixels to places**: the affine transform maps row and column to x and y; `xy` and `index` go each way, and pixel corner versus center decides a half-pixel shift [verify].
3. **Read only what you need**: windows with `windows.from_bounds`, overviews for a quick look, and masking `nodata` so it does not enter a mean.
4. **Cut and change CRS**: `rasterio.mask.mask` with polygon geometries in the raster's CRS; `warp.reproject` is resampling, so the method choice from the regridding part applies; rioxarray as the bridge to xarray.
5. **What this means for you**: satellite or drone imagery of fields (for example a vegetation index per block) is this workflow: clip each block polygon, mask nodata, then summarize.
6. **Key takeaways**

## Key takeaways

- A pixel's coordinates come from the affine transform and the CRS, not from the image size.
- rasterio's `xy` returns the pixel center by default, while the transform's origin is the top-left pixel corner [verify].
- Clipping with polygons in a different CRS from the raster returns an empty or wrong result, often without an error [verify].
- Reprojecting a raster resamples it, so nearest neighbor suits classes and a mean or conservative method suits amounts.

## Not in this module

- earth-data/shadow-detection-with-scikit-image: processing the pixel values themselves.
- earth-data/conservative-vs-bilinear and earth-data/regridding-in-python-with-xesmf: the theory and the xarray tool for regridding.
- earth-data/projections: what a CRS is and how to choose one.
- earth-data/zarr: storing large gridded data in chunks.

## Phase 2

- **Show:** a small pixel grid with the transform's origin at the top-left corner, one pixel's center marked, and the half-pixel offset labeled.
- **Sources to find:** rasterio and GDAL documentation on transforms, windows, masking and warping; the GeoTIFF specification on pixel-is-area versus pixel-is-point.
