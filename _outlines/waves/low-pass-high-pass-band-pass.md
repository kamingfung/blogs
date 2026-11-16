---
id: waves/low-pass-high-pass-band-pass
title: Low-pass, high-pass, band-pass
level: intermediate
---

**Promise:** Describe any filter by what it does to each frequency, its gain and its delay, and pick the filter type for a given job.

**Trap:** Readers think a moving average only smooths the data; it is a low-pass filter that also delays the signal and can remove or flip some cycles completely.

**Assumes:** waves/the-fourier-transform-and-audio and waves/the-dft-and-the-fft (the series file lists none).

## Outline

1. **A filter is a gain per frequency**: a filter multiplies each frequency by its own factor; plot that factor and you have the frequency response.
2. **Three shapes**: low-pass keeps slow changes, high-pass keeps fast changes and removes drift, band-pass keeps one band; cutoff and roll-off describe the edge.
3. **Filters delay**: every filter that uses only past data shifts its output later; a trailing moving average lags by about half its window.
4. **The moving average, honestly**: its response has zeros at some frequencies and side lobes at others, so it removes some cycles exactly and lets others through, sometimes inverted.
5. **Everyday filters**: tone controls, the anti-aliasing filter before sampling, the ear and a room as filters.
6. **What this means for you**: a seven-day rolling mean removes the weekly cycle exactly but lags the trend by about three days; a smoothed sensor alarm fires late by the same lag.

## Key takeaways

- A linear filter can be described completely by the gain and phase shift it applies at each frequency.
- A trailing moving average of N samples delays a slowly changing signal by (N − 1)/2 samples.
- An N-point moving average has zero gain at the frequency of one cycle per N samples and its multiples.
- A centered moving average has no delay but needs future data, so it cannot run in real time.

## Not in this module

- waves/convolution owns how a filter is computed in time, as a sliding weighted sum.
- waves/sampling-and-aliasing owns why a low-pass filter must come before sampling.
- waves/timbre owns formants as resonant bands in instruments and voices.
- waves/the-dft-and-the-fft owns how a frequency response is measured from data.

## Phase 2

- **Show:** a noisy series with a weekly cycle, its trailing seven-day mean, and the frequency response of that mean with its zeros marked.
- **Sources to find:** a digital signal-processing textbook on frequency response and phase delay; an applied time-series text on moving-average filters.
