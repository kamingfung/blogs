---
id: waves/perfusion-imaging
title: Perfusion imaging
level: intermediate
---

**Promise:** Explain how MRI measures how much blood reaches each piece of tissue, with an injected tracer or with magnetically labeled blood, and what the three standard perfusion numbers mean.

**Trap:** Readers think perfusion imaging measures blood flow in vessels; it measures delivery to the capillary bed per amount of tissue, a different quantity from flow in an artery.

**Assumes:** waves/k-space (series file). Also uses waves/relaxation-t1-and-t2 and waves/convolution.

## Outline

1. **Flow versus perfusion**: flow in a vessel is volume per time; perfusion is volume per time per mass of tissue fed by the capillaries.
2. **Following a tracer**: a short bolus of contrast agent passes through the brain and briefly darkens the signal through T2*; signal change gives tracer concentration over time.
3. **Blood volume, flow and transit time**: blood volume equals blood flow times mean transit time, and finding flow means deconvolving the tissue curve by the arterial input curve.
4. **Leaky vessels**: where vessels leak, as in many tumors, the tracer escapes, and a T1-based method measures the leak rate instead.
5. **No injection: arterial spin labeling**: invert the blood upstream, image downstream, subtract a control; the difference is a few percent, so averaging is needed.
6. **What this means for you**: blood volume equals flow times transit time is the same stock-equals-flux-times-residence-time rule used in box models of reservoirs, soils and the atmosphere.

## Key takeaways

- Perfusion is reported per mass of tissue, typically in milliliters per 100 grams per minute. [verify]
- Cerebral blood volume equals cerebral blood flow times mean transit time, the central volume principle. [verify]
- Tracer-based perfusion needs an arterial input function, and recovering flow from it is a deconvolution that is sensitive to noise.
- Arterial spin labeling measures perfusion without contrast agent, at the cost of a signal difference of only a few percent. [verify]

## Not in this module

- waves/what-mri-sees owns the one-line definitions of ASL and of flow methods such as time-of-flight and phase contrast.
- waves/bold-and-fmri owns blood-oxygenation signals and brain activation.
- waves/convolution owns convolution and deconvolution in general.
- waves/contrast-tr-and-te owns how timing sets T1 and T2* sensitivity.

## Phase 2

- **Show:** an arterial input curve and a tissue curve on one axis, with blood volume as the area ratio and transit time marked.
- **Sources to find:** the original central volume principle and tracer-kinetics papers; a consensus paper on arterial spin labeling; a review of dynamic susceptibility contrast methods.
