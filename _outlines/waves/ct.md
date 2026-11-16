---
id: waves/ct
title: CT
level: introductory
---

**Promise:** Explain how a CT scanner turns X-ray shadows taken from many angles into a cross-section, and what the numbers in a CT image mean.

**Trap:** Readers think a CT scanner takes a three-dimensional photograph; it measures total absorption along many lines and computes the slice, and simply smearing the shadows back gives a blurred image until a sharpening filter is applied.

**Assumes:** waves/electromagnetic-waves. The reconstruction section uses waves/convolution lightly.

## Outline

1. **One X-ray, one number**: a beam through the body is dimmed exponentially by everything along its path, so each detector reading gives the sum of absorption along one line.
2. **Many angles**: rotate source and detector; each angle gives one shadow profile, and the stack of profiles is the raw data.
3. **Back-projection and its blur**: smear every profile back across the image; the result is the true slice blurred, and a ramp filter applied first removes the blur.
4. **The link to Fourier**: each profile's Fourier transform is one line through the center of the slice's two-dimensional Fourier transform.
5. **Hounsfield units and dose**: CT numbers are absorption relative to water; the trade between noise and radiation dose.
6. **What this means for you**: X-ray CT is also used on soil cores and plant roots, so the same reconstruction and the same noise-versus-dose trade appear in plant and soil research.

## Key takeaways

- The X-ray intensity behind an object falls exponentially with the integrated attenuation along the beam path.
- Plain back-projection of the measured profiles gives a blurred slice; filtering each profile first gives the exact slice in the ideal case.
- The one-dimensional Fourier transform of a projection equals a central line through the two-dimensional Fourier transform of the slice. [verify]
- The Hounsfield scale sets water to 0 and air to about −1000. [verify]
- Lower radiation dose gives a noisier CT image, so dose and image quality trade off directly.

## Not in this module

- waves/what-mri-sees owns the comparison of CT and MRI contrast.
- waves/convolution owns filtering as convolution.
- waves/pet owns emission tomography, which shares the reconstruction step.
- waves/electromagnetic-waves owns what X-rays are.

## Phase 2

- **Show:** a simple phantom, its stack of projections, the plain back-projection and the filtered back-projection.
- **Sources to find:** a medical imaging physics textbook; the original CT reconstruction and central slice theorem papers; a review of X-ray CT in soil and root science.
