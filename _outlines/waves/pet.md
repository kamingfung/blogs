---
id: waves/pet
title: PET
level: introductory
---

**Promise:** Explain how PET locates a radioactive tracer from pairs of gamma rays, what a PET image shows, and why it is paired with CT or MRI.

**Trap:** Readers read a bright spot on PET as a lump of tissue; PET maps where a tracer collects, a measure of function such as glucose use, and some organs are bright in every healthy scan.

**Assumes:** waves/electromagnetic-waves; waves/ct helps for reconstruction.

## Outline

1. **A tracer that announces itself**: a molecule such as a glucose analog carries an atom that emits a positron; the body handles it like the real molecule.
2. **Two photons, one line**: the positron meets an electron and both vanish into two gamma rays flying apart; detecting both at once fixes a line through the source.
3. **From lines to an image**: millions of lines are reconstructed as in CT; timing the two arrivals narrows where on the line the event was.
4. **Counting noise and resolution**: the image is built from counts, so noise follows counting statistics; positron travel and detector size blur it to millimeters.
5. **Function needs anatomy**: PET says what is active, CT or MRI says where; combined scanners overlay both.
6. **What this means for you**: PET noise is counting noise, where variance equals the mean; the same rule governs any count data, from fruit counts to sales units, and it sets how much a low count can be trusted.

## Key takeaways

- Positron annihilation produces two gamma photons of about 511 keV traveling in nearly opposite directions. [verify]
- Coincidence detection of the two photons defines a line of response without any collimator.
- PET image intensity reflects tracer uptake, so organs with high normal uptake, such as the brain for a glucose tracer, are bright in healthy scans. [verify]
- The noise in a PET image follows Poisson counting statistics, so relative noise falls as one over the square root of the counts.

## Not in this module

- waves/ct owns tomographic reconstruction in detail and X-ray attenuation.
- waves/electromagnetic-waves owns what gamma rays are.
- waves/what-mri-sees owns the anatomical contrast that PET is paired with.
- waves/perfusion-imaging owns tracer kinetics for measuring blood delivery.

## Phase 2

- **Show:** a ring of detectors, a source inside, and coincidence lines building up until the source location emerges.
- **Sources to find:** a nuclear medicine physics textbook; a review of time-of-flight PET; clinical guidance on normal tracer uptake patterns.
