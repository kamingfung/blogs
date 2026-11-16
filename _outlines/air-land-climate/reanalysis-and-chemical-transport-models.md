---
id: air-land-climate/reanalysis-and-chemical-transport-models
title: "Reanalysis and chemical transport models"
level: intermediate
---

**Promise:** Explain how chemical transport models and atmospheric-composition reanalyses make gridded air-quality fields, and how to judge one before using it as data.

**Trap:** A reanalysis is a gridded set of observations; it is a model run nudged toward observations, and where observations are sparse it is mostly model.

**Assumes:** air-land-climate/monitors-sensors-and-satellites and air-land-climate/what-an-earth-system-model-is.

## Outline

1. **A chemical transport model**: it moves emissions through prescribed weather, runs chemistry and deposition, and outputs concentrations; unlike an Earth system model, the air's composition does not change the weather.
2. **Inputs set the answer**: emission inventories, meteorology and grid size shape results; a coarse grid cannot resolve a city plume or a valley.
3. **Data assimilation**: a reanalysis blends a model forecast with satellite and surface observations at each step, weighting each by its assumed error. [verify]
4. **Using gridded products as data**: check the grid size, which observations were assimilated, version changes over time, latency, and known biases against monitors in your region.
5. **What this means for you**: for a forecasting model, a reanalysis gives consistent historical features where no monitor exists, but a version change or a new assimilated satellite can create a jump that looks like a trend.
6. **Key takeaways**

## Key takeaways

- Chemical transport models are driven by fixed meteorology, so they cannot represent feedbacks of composition on weather.
- Atmospheric-composition reanalyses assimilate satellite observations such as aerosol optical depth and trace-gas columns. [verify]
- Changes in the observing system over time can create artificial trends in a reanalysis.
- Model grid cells of tens of kilometers smooth out urban and roadside peaks seen by monitors.

## Not in this module

- What each measurement type sees: air-land-climate/monitors-sensors-and-satellites.
- Earth system model structure and coupling: air-land-climate/what-an-earth-system-model-is and air-land-climate/coupling-land-and-atmosphere.
- Emission factors used in inventories: air-land-climate/emission-factors.

## Phase 2

- **Show:** monthly PM2.5 at one site from a monitor, a free-running model and a reanalysis, showing how assimilation pulls the model toward the monitor.
- **Sources to find:** documentation of CAMS and MERRA-2 composition reanalyses; a GEOS-Chem model description paper; evaluation studies of reanalysis PM2.5 against monitors.
