---
id: waves/the-dft-and-the-fft
title: The DFT and the FFT
level: intermediate
---

**Promise:** Read a discrete Fourier transform output correctly: which frequency each bin is, how fine the frequency resolution is, and why a pure tone smears across bins.

**Trap:** Readers think padding a signal with zeros or using a longer FFT gives finer frequency resolution; only a longer record of real data separates two close frequencies, and padding only draws the same spectrum more smoothly.

**Assumes:** waves/the-fourier-transform-and-audio.

## Outline

1. **From integral to sum**: the DFT asks how much of each of N test frequencies is in N samples; the test frequencies are fixed by the record length.
2. **What a bin is**: bin spacing equals the sample rate divided by N, which equals one over the record length; real signals give a mirrored second half.
3. **Leakage and windows**: a tone that does not fit a whole number of cycles into the record spreads into neighboring bins; a window trades a wider peak for lower side lobes.
4. **Zero-padding is interpolation**: padding adds points between bins but cannot separate two tones closer than one over the record length.
5. **Why the FFT is fast**: split the sum into even and odd samples, reuse the half-size results, and repeat; the answer is identical to the slow DFT.
6. **What this means for you**: a periodogram of a one-year daily series cannot separate cycles closer than about one cycle per year, whatever FFT length is used; leakage from a strong weekly cycle can hide a weak nearby one.

## Key takeaways

- DFT bins are spaced by the sample rate divided by the number of samples, which is the reciprocal of the record duration.
- A sinusoid that does not complete a whole number of cycles in the record leaks power into many bins.
- Zero-padding makes the spectrum look smoother but does not improve the ability to separate two close frequencies.
- The FFT returns exactly the same numbers as the direct DFT, in order N log N operations instead of N squared.
- For a real-valued input, the upper half of the DFT mirrors the lower half, so only half the bins carry new information.

## Not in this module

- waves/the-fourier-transform-and-audio owns the continuous transform, the spectrogram and the time-frequency trade-off.
- waves/sampling-and-aliasing owns the Nyquist limit and what happens to frequencies above it.
- waves/convolution owns why multiplying by a window blurs the spectrum, in general form.
- waves/k-space owns the two-dimensional DFT in MRI.

## Phase 2

- **Show:** the spectrum of two close tones from a short record, the same record zero-padded, and a longer record, side by side.
- **Sources to find:** a signal-processing textbook on DFT resolution and windowing; the original FFT algorithm paper; a reference on window functions.
