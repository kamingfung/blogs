---
id: earth-data/dask-and-chunking
title: Dask and chunking
level: intermediate
---

**Promise:** Open and reduce a dataset larger than memory with xarray and Dask, and choose chunks that match the calculation.

**Trap:** "Adding Dask makes the code faster." Dask makes larger-than-memory work possible and can run in parallel, but chunks that cut across the reduced dimension, or millions of tiny chunks, make it slower than plain NumPy.

**Assumes:** earth-data/dimensions-coordinates-and-attributes.

## Outline

1. **Lazy arrays**: with `chunks=` in `open_dataset` or `open_mfdataset`, xarray builds a task graph and reads nothing; `compute`, `load` and `persist` run it.
2. **What a chunk is**: a block of the array that one task holds in memory; `.chunks` shows the layout, `.chunk()` changes it, and a common target size is about 100 MB [verify].
3. **Match chunks to the question**: a time mean at each grid cell wants long chunks in time; a map for one day wants wide chunks in space; rechunking between the two is costly.
4. **Watching it run**: the Dask dashboard shows tasks, memory and spills; signs of too many tasks or too little memory per worker.
5. **What this means for you**: a multi-year climatology or a station time series pulled from a large reanalysis is a chunking question first and a code question second.
6. **Key takeaways**

## Key takeaways

- A Dask-backed xarray operation does no reading or arithmetic until `compute`, `load` or a plot asks for values.
- A reduction over time runs fastest when each chunk spans the full time dimension for a small block of space.
- Chunks of a few kilobytes produce so many tasks that scheduling overhead outweighs the work [verify].
- `persist` keeps a computed intermediate in memory, which pays off only when it is reused.

## Not in this module

- earth-data/zarr: the on-disk chunk layout that decides which reads are cheap.
- earth-data/resampling-and-grouping-in-time: the time operations themselves.
- earth-data/python-basics-for-mapping: the first use of `open_mfdataset`.

## Phase 2

- **Show:** a space-time cube cut into chunks two ways, with the chunks a time mean must touch highlighted in each.
- **Sources to find:** Dask and xarray documentation on chunking and best practices; Pangeo guidance on chunk sizes.
