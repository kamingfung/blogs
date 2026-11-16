---
id: waves/beats
title: Beats
level: introductory
---

**Promise:** Explain why two nearly equal tones swell and fade at a rate equal to their frequency difference, and use that slow rhythm to measure or shift a frequency.

**Trap:** Many readers think a beat is a third, low tone at the difference frequency; it is a slow change in loudness of one tone, and the summed signal has no spectral line at the difference frequency.

**Assumes:** waves/interference.

## Outline

1. **Two tones, slightly apart**: add two equal sines whose frequencies differ a little and watch the sum drift in and out of step, so the loudness rises and falls.
2. **Carrier and envelope**: rewrite the sum as one tone at the average frequency times a slow envelope; explain why the beat rate is the full difference, not half of it.
3. **Beats are not a tone**: show that the spectrum still holds only the two original lines; the difference tones some listeners hear come from nonlinearity in the ear, a separate effect.
4. **From beats to roughness to two notes**: as the gap widens, slow beats become a rough sound and then two separate pitches; the boundaries are set by hearing, not by the formula.
5. **Beats as a measuring tool**: tuning by ear (slow the beats to zero) and heterodyning, which mixes a high frequency with a known one to bring the difference down to a range that is easy to count.
6. **What this means for you**: two close periods in a time series beat the same way, so a slow cycle in the data can be the sum of two fast ones rather than a real slow driver.

## Key takeaways

- The sum of two equal-amplitude sines at f1 and f2 is a tone at their mean frequency whose loudness pulses |f1 − f2| times per second.
- A linear sum of two tones has no energy at the difference frequency; any heard difference tone needs a nonlinear system such as the inner ear.
- Beats are heard as separate pulses only while the difference is below roughly 15 to 20 Hz, then turn into roughness, then into two distinct pitches. [verify]
- Tuners and musicians match two pitches by slowing the beats until they stop.
- Heterodyne receivers and Doppler instruments use beating to move a high frequency down to a low one that is easy to measure. [verify]

## Not in this module

- waves/interference owns superposition and phase; this module only applies it to two frequencies.
- waves/the-mathematics-of-music owns consonance and dissonance; it uses beating, this module explains it.
- waves/sampling-and-aliasing owns false low frequencies created by sampling, which look like beats but have another cause.
- waves/ultrasound owns the Doppler flow measurement in practice.

## Phase 2

- **Show:** two sines and their sum on one axis, with the envelope drawn over the sum and a slider for the frequency gap.
- **Sources to find:** an acoustics textbook for the envelope derivation; a psychoacoustics source for the beat, roughness and two-tone boundaries; a radio-engineering text for heterodyning.
