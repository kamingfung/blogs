---
id: waves/sampling-and-aliasing
title: Sampling and aliasing
level: intermediate
---

**Promise:** Decide how often to sample a signal, and recognize when a pattern in sampled data is a fast cycle disguised as a slow one.

**Trap:** Readers think sampling at twice the highest frequency they care about is safe; the rule applies to the highest frequency present, and anything faster folds down into false low frequencies that no later processing can remove.

**Assumes:** waves/the-dft-and-the-fft.

## Outline

1. **Wagon wheels and strobes**: a wheel filmed at a fixed frame rate can seem to turn slowly or backwards; that is aliasing.
2. **The Nyquist limit**: with samples at rate fs, frequencies above fs/2 cannot be told apart from frequencies below it; show how they fold back.
3. **Aliasing is permanent**: once sampled, the alias and the true signal are the same numbers, so the fix must come before sampling: an anti-aliasing filter or a faster rate.
4. **Getting the signal back**: below the limit, the samples fix the signal completely; a smooth interpolation between them restores it.
5. **Aliasing in time and space**: the same folding produces moiré patterns in photos and wraparound in images.
6. **What this means for you**: a weekly field visit on the same weekday cannot see a weekly cycle, and a satellite that passes at the same local time each day aliases the daily cycle; check the sampling schedule before trusting a slow trend.

## Key takeaways

- A signal sampled at rate fs is fully described by its samples only if it contains no frequency above fs/2.
- A frequency above fs/2 appears in the samples at a lower frequency, folded about multiples of fs/2.
- No processing after sampling can separate an alias from a genuine low frequency.
- Audio is sampled at 44.1 kHz so that the band up to about 20 kHz, the upper limit of human hearing, is below the Nyquist limit with room for a filter. [verify]
- A sun-synchronous satellite observes each place at roughly the same local time, so it cannot resolve the daily cycle at that place. [verify]

## Not in this module

- waves/the-dft-and-the-fft owns bins, leakage and frequency resolution.
- waves/low-pass-high-pass-band-pass owns how an anti-aliasing filter is built.
- waves/beats owns slow modulation from two close frequencies, which can look like an alias.
- waves/k-space owns wraparound in MRI.

## Phase 2

- **Show:** a fast sine, its samples at a slow rate, and the slow sine that passes through the same samples.
- **Sources to find:** the original sampling-theorem papers; a signal-processing textbook; a remote-sensing source on sun-synchronous orbits and diurnal sampling.
