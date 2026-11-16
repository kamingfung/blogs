---
id: waves/timbre
title: Timbre
level: introductory
---

**Promise:** Explain what lets you tell a flute from a violin on the same note and the same loudness, beyond the list of overtone strengths.

**Trap:** Readers believe timbre is just the steady mix of harmonics; how the sound starts and changes over time, and fixed resonances in the instrument body, matter as much.

**Assumes:** waves/the-mathematics-of-music. The spectrum view in waves/the-fourier-transform-and-audio helps.

## Outline

1. **Same pitch, same loudness, different sound**: define timbre by what is left when pitch and loudness are equal.
2. **The steady recipe**: recap that a sustained note is a set of harmonics with different strengths, and that this explains part of the difference.
3. **The attack carries the identity**: cut off the first fraction of a second and many instruments become hard to name; the onset, the decay and small pitch wobbles carry much of the identity.
4. **Formants: resonances that do not move**: a voice or violin body boosts fixed frequency bands whatever note is played, which is why vowels keep their identity across pitches.
5. **Noise and inharmonic parts**: breath, bow scrape and slightly sharp piano harmonics are part of the sound, not defects.
6. **What this means for you**: a power spectrum discards timing, so two signals with the same spectrum can behave very differently; features for a time-series model need both what frequencies are present and when.

## Key takeaways

- Two sounds with the same pitch, loudness and long-term spectrum can still sound like different instruments.
- Removing the attack of a note makes many instruments much harder to identify. [verify]
- Formants are fixed resonant bands of the instrument or vocal tract, so they stay put while the harmonics move with pitch.
- The magnitude spectrum of a whole note discards the order of events, so it cannot fully describe timbre.

## Not in this module

- waves/the-fourier-transform-and-audio owns the spectrum, the spectrogram and the harmonic synthesizer.
- waves/why-octaves-sound-the-same owns pitch chroma.
- waves/low-pass-high-pass-band-pass owns filters; a formant is a band-pass resonance, but the filter mechanics live there.
- waves/standing-waves-and-resonance owns why the harmonics exist.

## Phase 2

- **Show:** two spectrograms of different instruments on one note, with the attack region marked, and the same notes with the attack cut.
- **Sources to find:** classic attack-removal listening experiments; a musical-acoustics text on formants and the source-filter model; a piano-acoustics source on inharmonicity.
