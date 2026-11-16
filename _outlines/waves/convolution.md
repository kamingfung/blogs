---
id: waves/convolution
title: Convolution
level: intermediate
---

**Promise:** Explain convolution as the output of any linear, time-invariant system, compute it by hand for a short example, and say why blur can only be partly undone.

**Trap:** Readers think a known blur can be removed exactly by dividing it out in the frequency domain; frequencies the blur nearly erased are lost under noise, and dividing them out amplifies that noise.

**Assumes:** waves/low-pass-high-pass-band-pass.

## Outline

1. **Echoes add up**: a system that responds to a single click with a known shape responds to any input with a sum of shifted, scaled copies of that shape; that sum is convolution.
2. **Slide, multiply, sum**: compute a short convolution step by step; the moving average from the filters module is one case.
3. **The convolution theorem**: convolving in time is multiplying in frequency, which links this module to frequency responses.
4. **Blur is convolution**: a camera or scanner spreads each point into a small spot, the point spread function, and the image is the scene convolved with it.
5. **Deconvolution and its limits**: dividing by a response that is near zero blows up the noise; practical deconvolution limits how much it trusts those frequencies.
6. **What this means for you**: a delayed effect of weather on a crop, spread over several weeks, is a convolution of the weather with a lag profile, and recovering that profile from noisy data has the same noise problem as deblurring a photo.

## Key takeaways

- The output of any linear, time-invariant system equals its input convolved with its impulse response.
- Convolution in the time domain equals multiplication in the frequency domain.
- An image from a lens or scanner is the scene convolved with the instrument's point spread function.
- Deconvolution amplifies noise at frequencies where the system's response is small, so detail lost there cannot be recovered reliably.

## Not in this module

- waves/low-pass-high-pass-band-pass owns frequency response and filter types.
- waves/diffraction owns why a lens has a point spread function of finite size.
- waves/ct owns filtered back-projection, a reconstruction that uses a convolution step.
- waves/perfusion-imaging and waves/bold-and-fmri own their own uses of convolution and deconvolution.

## Phase 2

- **Show:** a sharp test image, the image blurred, and naive versus regularized deconvolution with a little noise added.
- **Sources to find:** a signal-processing textbook on linear time-invariant systems; an imaging text on point spread functions and regularized deconvolution.
