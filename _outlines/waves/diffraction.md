---
id: waves/diffraction
title: Diffraction
level: intermediate
---

**Promise:** Predict how much a wave spreads after an opening, and compute the finest detail a lens, dish or sensor of a given size can resolve.

**Trap:** Readers think more pixels or a better lens can always show finer detail; the size of the opening and the wavelength set a hard limit that no sensor can beat.

**Assumes:** waves/interference and waves/electromagnetic-waves (the series file lists none).

## Outline

1. **Every point of an opening is a source**: treat the opening as many small sources and add their waves; the spread follows from interference.
2. **Single slit**: the first dark fringe sits where the two halves of the slit cancel, so the spread angle is about wavelength over width.
3. **Circular apertures and the resolution limit**: a round lens makes a bright spot with rings; two points are resolved when their spots are far enough apart.
4. **Gratings**: many slits make sharp, widely spaced peaks, which is how spectrometers split light by wavelength.
5. **Pixels versus optics**: a sensor's pixel size and its diffraction limit are separate; the coarser of the two decides the real resolution.
6. **What this means for you**: for a drone or satellite image, ground pixel size is not the same as resolving power; counting small fruit or spotting small lesions needs both to be small enough.

## Key takeaways

- The angular spread of a wave after an opening of width D is roughly the wavelength divided by D.
- A circular aperture of diameter D cannot resolve two points closer in angle than about 1.22 times the wavelength over D. [verify]
- A diffraction grating sends each wavelength to a different angle, with sharper peaks the more slits it has.
- Making pixels smaller than the diffraction spot adds pixels but no new detail.

## Not in this module

- waves/interference owns superposition, the double slit and the qualitative picture of diffraction.
- waves/electromagnetic-waves owns what light is.
- waves/convolution owns the point spread function as a blur kernel.
- waves/ultrasound owns how wavelength limits resolution in sound imaging.

## Phase 2

- **Show:** the diffraction pattern of a circular aperture, and two such patterns moving together until they merge.
- **Sources to find:** an optics textbook for the single-slit and circular-aperture results; a remote-sensing source on ground sample distance versus optical resolution.
