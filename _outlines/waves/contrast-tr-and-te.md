---
id: waves/contrast-tr-and-te
title: 'Contrast: TR and TE'
level: intermediate
---

**Promise:** Choose sequence timing to make two named tissues differ as much as possible, use an inversion pulse to blank out one tissue, and explain why a "weighted" image is not a measurement.

**Trap:** Readers read a T1-weighted image as a map of T1; brightness mixes proton density, T1, T2 and the scanner settings, so it cannot be compared across protocols, and a true T1 map needs a separate measurement.

**Assumes:** waves/relaxation-t1-and-t2.

## Outline

1. **Weighted is not quantitative**: recap the spin-echo signal from the relaxation module and show that every pixel mixes three tissue properties with two settings.
2. **Choosing timing for one pair of tissues**: the contrast between two tissues peaks at a particular TR and TE; more contrast is not always more contrast per minute of scan.
3. **Inversion recovery**: flip the magnetization first, wait until one tissue crosses zero, then image; that is how fluid or fat is blanked out.
4. **Gradient echoes and flip angle**: without the refocusing pulse, the signal decays with T2*, and a smaller flip angle allows a shorter TR; one flip angle gives the most signal for a given TR and T1.
5. **From weighted images to maps**: acquire several timings and fit T1 or T2 per pixel, so values can be compared between scanners and visits.
6. **What this means for you**: image brightness is shaped by acquisition settings as much as by the subject; compare images only when the protocol is the same, or convert them to a calibrated quantity first.

## Key takeaways

- The intensity of a weighted MRI image depends on proton density, T1, T2 and the chosen TR and TE together.
- An inversion pulse followed by a wait of about T1 times ln 2 nulls the signal from a tissue with that T1, when TR is long. [verify]
- For a gradient echo, the flip angle that gives the most signal at a given TR and T1 is the Ernst angle, with cosine equal to exp(−TR/T1). [verify]
- Quantitative T1 and T2 maps need several acquisitions with different timing and a model fit per pixel.

## Not in this module

- waves/relaxation-t1-and-t2 owns the relaxation curves, the spin echo and the basic short-TR and long-TE rules.
- waves/what-mri-sees owns the vocabulary table, including the first mention of FLAIR.
- waves/k-space owns how the image is encoded, which is independent of contrast.
- waves/perfusion-imaging owns contrast agents that change T1 and T2*.

## Phase 2

- **Show:** inversion-recovery curves for fat, brain tissue and fluid, with a slider for the inversion time and a marker where each crosses zero.
- **Sources to find:** an MRI physics textbook on inversion recovery, gradient echo and the Ernst angle; a review of quantitative relaxometry.
