---
id: waves/k-space
title: k-space
level: intermediate
---

**Promise:** Explain how gradients turn an MRI signal into samples of the image's spatial frequencies, and predict what the image looks like when k-space is sampled too coarsely, too narrowly or out of order.

**Trap:** Readers picture each k-space point as one pixel of the image; each point is one spatial frequency of the whole object, so removing part of k-space changes the whole image, not one part of it.

**Assumes:** waves/what-mri-sees and waves/the-dft-and-the-fft.

## Outline

1. **The signal is a Fourier sample**: with a gradient on, the coil signal at each moment is one value of the object's two-dimensional Fourier transform; the gradient's area sets which one.
2. **Walking through k-space**: frequency encoding moves along a line during readout; phase encoding picks the line; each repetition draws one path.
3. **Field of view and resolution**: the spacing between k-space samples sets the field of view and the largest k reached sets the pixel size.
4. **When sampling goes wrong**: too wide a spacing wraps the image onto itself; too small a k range blurs and rings at edges; motion between lines makes ghosts.
5. **Faster paths**: filling many lines per excitation, spiral paths, using k-space symmetry, and skipping lines with several receive coils or with sparsity.
6. **What this means for you**: any digital image is a sum of spatial frequencies, so compression, sharpening and resizing in an imaging pipeline act on the same quantity a scanner samples.

## Key takeaways

- The MRI coil signal at time t equals the object's Fourier transform at a k set by the time integral of the gradient.
- The field of view equals one over the k-space sample spacing, and the pixel size equals roughly one over the width of the sampled k-space.
- Sampling k-space too coarsely wraps parts of the object outside the field of view back into the image.
- Each k-space sample carries information from the whole object, so discarding the outer region blurs every edge in the image.

## Not in this module

- waves/what-mri-sees owns the first description of gradients, slice selection, and why a scan takes minutes.
- waves/the-dft-and-the-fft owns the one-dimensional DFT and its resolution.
- waves/sampling-and-aliasing owns the general Nyquist rule; wraparound is its MRI form.
- waves/bold-and-fmri owns the fast single-shot imaging that fMRI depends on.

## Phase 2

- **Show:** an image beside its k-space magnitude, with toggles to keep only the center, only the edges, or every second line.
- **Sources to find:** an MRI physics textbook on k-space; the original papers on k-space trajectories, parallel imaging and compressed sensing.
