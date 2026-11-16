---
id: waves/bold-and-fmri
title: BOLD and fMRI
level: intermediate
---

**Promise:** Explain where the functional MRI signal comes from, why it lags brain activity by seconds, and how a brain map is turned from a time series into a statistical claim.

**Trap:** Readers think fMRI measures neural activity; it measures a slow change in blood oxygenation that follows activity, and the step from that signal to neurons rests on a model.

**Assumes:** waves/k-space (series file). Also uses waves/relaxation-t1-and-t2 (T2*) and waves/convolution.

## Outline

1. **Deoxygenated blood is a magnet**: deoxyhemoglobin distorts the local field and shortens T2*; oxygenated hemoglobin does not.
2. **Activity overshoots supply**: active tissue draws more fresh blood than it uses, so local deoxyhemoglobin falls and the signal rises by a few percent.
3. **The hemodynamic response**: the rise is slow, peaks seconds after the stimulus and undershoots; the measured series is the stimulus pattern convolved with this response.
4. **Fast imaging and its costs**: a whole brain every second or two needs single-shot imaging, which brings distortion and signal loss near air spaces.
5. **From time series to map**: fit a regression per voxel and then correct for testing a hundred thousand voxels at once; without the correction, noise looks like activation.
6. **What this means for you**: one regression per voxel across a whole brain is the same multiple-testing problem as testing every field or product at once; the fix and the failure are the same.

## Key takeaways

- The BOLD signal arises because deoxyhemoglobin is paramagnetic and shortens T2*.
- The hemodynamic response peaks around 4 to 6 seconds after a brief stimulus. [verify]
- Task-related BOLD changes at 3 T are typically a few percent of the baseline signal. [verify]
- Standard fMRI analysis models each voxel's time series as the stimulus convolved with a hemodynamic response function, plus noise.
- Without correction for multiple comparisons, a whole-brain analysis will report false activations even in an object with no brain activity. [verify]

## Not in this module

- waves/what-mri-sees owns the one-line definition of BOLD.
- waves/perfusion-imaging owns blood flow and blood volume measurement.
- waves/k-space owns the single-shot trajectories that make fMRI fast.
- waves/convolution owns the convolution model in general.

## Phase 2

- **Show:** a block stimulus, the hemodynamic response function, and their convolution overlaid on a noisy voxel time series.
- **Sources to find:** the original BOLD contrast papers; a review of the hemodynamic response; a methods paper on multiple-comparison correction in fMRI.
