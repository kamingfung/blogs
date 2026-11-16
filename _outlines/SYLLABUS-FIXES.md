# Syllabus problems found while outlining

Found by the outline writers on 2026-11-16 while reading `series/*.yml`. Nothing here has been applied; each is a proposal to decide on. "A requires B" means B is in A's `requires`.

## Order (a module comes before one it requires or builds on)

| Series | Problem |
|---|---|
| air-land-climate | organic-aerosols-health-versus-climate requires exposureresponse-curves, eight parts later |
| air-land-climate | agriculture-under-climate-extremes requires how-ozone-damages-crops, which follows it |
| air-land-climate | The CESM2 fertilizer module and enhanced-rock-weathering require the Earth system model modules, which come later; move that part earlier |
| air-land-climate | ammonia-deposition-and-ozone-feedbacks (advanced) comes before stomata-and-dry-deposition and leaf-area-index |
| cloud-formation | lift-a-parcel-yourself (introductory) comes after lapse-rates-and-stability (intermediate); better first, as the hook |
| earth-data | scaling-a-netcdf-subset, regridding-crop-data-for-climate-models, downloading-building-footprints and mapping-pm2-5-by-county each come before a module they require |
| earth-data | regionmask-in-python requires geopandas-basics, which is in a later part |
| earth-data | sequential-diverging-categorical should come before colourblind-safe-palettes; both follow the ggplot2 colorbars module, which already uses palettes |
| waves | timbre comes before the Fourier part; sampling-and-aliasing would teach better before the DFT module |
| everyday-physics | information-exchange-versus-energy comes before landauer-s-limit, which it requires |
| everyday-physics | gravitational-wells (intermediate) comes before why-orbits-don-t-fall (introductory) |
| everyday-physics | why-the-shower-curtain-moves-in should come before how-aeroplanes-stay-up |
| engineering | harness-engineering comes before instructions-that-agents-actually-follow, which it requires |
| engineering | 3d-printing-basics (introductory) comes after two intermediate modules |
| engineering | deploying-a-streamlit-app relies on lock files taught later in environments-that-don-t-break; from-notebook-to-app fits before the finished app example |
| teaching-leading | code-review-as-feedback requires giving-hard-feedback, which follows it |
| teaching-leading | The last part (memory-and-spacing, cognitive-load) is the learning science several earlier modules lean on; move it near the start |
| teaching-leading | Parts 9 to 14 stop alternating classroom and work, which the series description promises; presenting-data-to-a-decision fits part 9 better than part 11 |
| training | reading-a-nutrition-study comes last but two earlier modules require it |
| training | open-source-as-a-scientist (introductory) comes after the intermediate community-model module |

## Missing or weak `requires`

| Series | Proposal |
|---|---|
| air-land-climate | ozone-titration-in-cities → nox-vocs-and-sunlight; ammonia-deposition-and-ozone-feedbacks → stomata-and-dry-deposition, leaf-area-index |
| cloud-formation | why-clean-air-makes-no-cloud → the-kelvin-effect; contrails → how-much-water-can-air-hold; why-cloud-droplets-dont-fall should not require drop-shape-in-air |
| aerosols-climate | ship-tracks (introductory) requires an intermediate module |
| earth-data | regionmask → dimensions-coordinates-and-attributes; zarr → dask-and-chunking; rasterio → projections, geopandas-basics; folium → geopandas-basics; cartopy → python-basics-for-mapping |
| waves | electromagnetic-waves → the-wave-equation; diffraction → interference; low-pass-high-pass-band-pass → the DFT module; ultrasound, seismic-waves → transverse-and-longitudinal; why-octaves-sound-the-same → the-mathematics-of-music; perfusion-imaging and bold-and-fmri lean on relaxation and convolution more than k-space |
| everyday-physics | tides → why-orbits-don-t-fall; why-satellite-clocks-drift → why-orbits-don-t-fall, gravitational-wells; entropy-and-the-arrow-of-time → how-a-fridge-works or landauer-s-limit in place of why-ice-floats |
| teaching-leading | rubrics → aligning-assessment; formative-assessment → meeting-students-where-they-are; milestones-as-assessments → decide-what-done-looks-like-first; active-learning → belonging-and-engagement; workshops-and-retrospectives, growing-people-who-will-leave, open-courseware and cognitive-load have none |
| training | what-the-ear-does-with-a-chord → why-a-string-has-harmonics; your-first-contribution-to-a-community-model → open-source-as-a-scientist |

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
