---
id: earth-data/zarr
title: Zarr
level: intermediate
---

**Promise:** Write and read gridded data as Zarr, and set its chunk layout for the reads you will make most.

**Trap:** "Zarr is a faster NetCDF." Zarr stores each chunk as its own object, so it is fast for reads that match the chunks and slow for reads that cut across them; the layout chosen at write time decides which.

**Assumes:** earth-data/dask-and-chunking; earth-data/dimensions-coordinates-and-attributes. Neither is listed in the series file; see the report.

## Outline

1. **A store, not a file**: a Zarr store is a tree of metadata documents and one object per chunk, which suits cloud object storage and parallel writes.
2. **Writing**: `to_zarr` from xarray, chunk sizes through `encoding` or the Dask chunks, compression, and consolidated metadata so opening a store is one read [verify].
3. **Reading**: `open_zarr` or `open_dataset(engine="zarr")` gives a lazy Dask-backed Dataset; only the chunks a selection touches are fetched.
4. **Layout decides speed**: a store chunked for maps answers a one-day map in a few reads and a single-point time series in thousands; rechunking (for example with rechunker) or keeping two copies; Zarr format versions 2 and 3 [verify].
5. **What this means for you**: forecasting at a station or a farm reads one point through many times, the access pattern a map-chunked store serves worst; check the chunk layout of a cloud dataset before building on it.
6. **Key takeaways**

## Key takeaways

- Reading one grid point's full time series from a store chunked as single time steps touches one chunk per time step.
- Consolidated metadata lets xarray open a Zarr store with one metadata read instead of one per array [verify].
- Zarr's chunk layout is fixed at write time; changing it means rewriting the data.
- Zarr format version 3 changes the on-disk metadata layout, and not every reader supports it yet [verify].

## Not in this module

- earth-data/dask-and-chunking: chunks in memory and the task graph.
- earth-data/dimensions-coordinates-and-attributes: the Dataset model and CF attributes that Zarr stores.
- earth-data/rasterio: GeoTIFF and cloud-optimized GeoTIFF for single rasters.

## Phase 2

- **Show:** the same space-time cube in two chunk layouts with a counter of chunks read for a map request and a point time-series request.
- **Sources to find:** the Zarr specification for versions 2 and 3; xarray and Zarr-Python documentation; Pangeo material on analysis-ready cloud datasets.
