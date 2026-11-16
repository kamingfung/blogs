# Syllabus problems found while outlining

Found by the outline writers on 2026-11-16 while reading `series/*.yml`. "A requires B" means B is in A's `requires`.

## Applied

- 25 `requires` links added, listed in the pull request that applied them.
- 16 parts reordered so that no module comes before a module it requires in the same part. No module changed part.

## Still open: order

Each needs a decision, because the fix moves a whole part, drops a `requires` link or is a teaching preference.

| Series | Problem |
|---|---|
| air-land-climate | organic-aerosols-health-versus-climate (part 2) requires exposureresponse-curves (part 11) |
| air-land-climate | The CESM2 fertilizer module (part 6) and enhanced-rock-weathering (part 8) require the Earth system model modules (part 10); move that part earlier |
| statistics | the-kolmogorovsmirnov-test (part 2) requires what-a-p-value-is-not (part 5); is-the-trend-significant (part 4) requires confidence-intervals (part 5) |
| earth-data | regionmask-in-python (part 4) requires geopandas-basics (part 5) |
| training | where-your-calories-come-from and supplements-what-survives-scrutiny require reading-a-nutrition-study, the last module of part 1. Moving it first would open the series with an intermediate module; dropping the two links may be the better fix |
| cloud-formation | lift-a-parcel-yourself (introductory) comes after lapse-rates-and-stability (intermediate); better first, as the hook |
| earth-data | sequential-diverging-categorical should come before colourblind-safe-palettes; both follow the ggplot2 colorbars module, which already uses palettes |
| waves | timbre comes before the Fourier part; sampling-and-aliasing would teach better before the DFT module |
| everyday-physics | gravitational-wells (intermediate) comes before why-orbits-don-t-fall (introductory) |
| everyday-physics | why-the-shower-curtain-moves-in should come before how-aeroplanes-stay-up |
| engineering | 3d-printing-basics (introductory) comes after two intermediate modules |
| engineering | deploying-a-streamlit-app relies on lock files taught later in environments-that-don-t-break; from-notebook-to-app fits before the finished app example |
| teaching-leading | The last part (memory-and-spacing, cognitive-load) is the learning science several earlier modules lean on; move it near the start |
| teaching-leading | Parts 9 to 14 stop alternating classroom and work, which the series description promises; presenting-data-to-a-decision fits part 9 better than part 11 |

## Still open: `requires`

| Series | Proposal |
|---|---|
| cloud-formation | why-clean-air-makes-no-cloud → the-kelvin-effect (not applied: the written post explains the Kelvin effect itself); why-cloud-droplets-dont-fall should not require how-a-drop-deforms-in-air |
| aerosols-climate | ship-tracks (introductory) requires an intermediate module |
| waves | perfusion-imaging and bold-and-fmri lean on relaxation and convolution more than k-space |
| everyday-physics | entropy-and-the-arrow-of-time → how-a-fridge-works or landauer-s-limit in place of why-ice-floats |
| teaching-leading | workshops-and-retrospectives, growing-people-who-will-leave, open-courseware and cognitive-load have none |

## Overlap with written posts (outlines were narrowed; confirm in phase 2)

- air-land-climate/what-pm2-5-is-and-why-2-5: primary-and-secondary-aerosols already explains PM2.5 and settling speeds.
- teaching-leading/active-learning: belonging-and-engagement already has the meta-analysis and a technique catalog.
- training/intervals-as-ratios and waves/beats: the-mathematics-of-music already derives ratios, the beat formula and equal temperament.
- waves/contrast-tr-and-te: relaxation-t1-and-t2 already covers TR and TE.
- earth-data/folium: mapping-pm2-5-by-county already uses `explore()`, which is built on folium.

## Gaps and fixes outside the outlines

- No module teaches ice supersaturation (needed by cloud-formation/contrails) or Earth's energy budget (needed by aerosols-climate/do-clouds-warm-or-cool).
- The written Fourier post's takeaway that instruments "differ only in" overtone weights conflicts with waves/timbre.
- Series titles "Colourblind", "Colour" and "centred" in earth-data are British spellings.
