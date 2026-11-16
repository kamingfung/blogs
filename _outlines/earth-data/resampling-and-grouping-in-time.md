---
id: earth-data/resampling-and-grouping-in-time
title: Resampling and grouping in time
level: intermediate
---

**Promise:** Turn daily or hourly gridded data into monthly series, seasonal means and climatologies in xarray, and say which operation produced which.

**Trap:** "Resampling to months and grouping by month give the same result." Resampling keeps the timeline (one value per month of each year); grouping by month folds the years into a 12-value climatology.

**Assumes:** earth-data/dimensions-coordinates-and-attributes (labels, selection by label, reductions that name a dimension).

## Outline

1. **Two questions about time**: "what happened each month?" is resampling; "what is a typical January?" is grouping. Both are split, apply, combine, but they split on different keys.
2. **Resampling along the timeline**: `resample` with a frequency string, which label (period start or end) the output carries, and why a mean suits a temperature while a sum suits a precipitation total.
3. **Grouping by calendar parts**: `groupby` on `time.month`, `time.season` and `time.dayofyear`, then anomalies by subtracting the climatology with the group still attached.
4. **Months are not equal**: a seasonal mean of monthly means weights a 28-day month like a 31-day one; weight by days in the month. Model output often uses a no-leap or 360-day calendar held as cftime objects, and `convert_calendar` changes it [verify].
5. **What this means for you**: a growing season or a Southern Hemisphere harvest crosses the calendar year, so grouping by year splits one season in two; define a season label first, then group on it. The same applies to degree-day sums and to forecast verification by lead month.
6. **Key takeaways**

## Key takeaways

- `resample(time="MS").mean()` returns one value per month of each year, while `groupby("time.month").mean()` returns 12 values [verify].
- An unweighted mean of three monthly means differs from the true seasonal mean whenever the months have different lengths.
- xarray's built-in `time.season` groups December with January and February of the same calendar year, not the following one [verify].
- Rate-like fields (mm/day) are averaged when resampled; amount-like fields (mm) are summed, and mixing them up changes the answer by the number of days in the period.

## Not in this module

- earth-data/dimensions-coordinates-and-attributes: what a time coordinate is and how selection by label works.
- earth-data/dask-and-chunking: running the same operations on data larger than memory, and why chunking along time matters for them.
- earth-data/scaling-a-netcdf-subset: changing values in one region; this module changes the time resolution.

## Phase 2

- **Show:** a timeline that splits a decade of daily values into monthly bars (resample) next to the same data stacked into 12 calendar-month bars (groupby).
- **Sources to find:** xarray documentation for resample, groupby and calendar handling; the CF conventions section on calendars; a reference on day-weighted seasonal means.
