---
id: everyday-physics/why-satellite-clocks-drift
title: "Why satellite clocks drift"
level: intermediate
---

**Promise:** Explain why GPS satellite clocks would gain time against ground clocks without correction, by adding a slowing effect from their speed and a larger speeding effect from their height.

**Trap:** "Satellite clocks run slow because they move fast." Speed does slow them, but being higher in Earth's gravity speeds them up more, so on balance they run fast, by about 38 microseconds a day [verify].

**Assumes:** everyday-physics/why-orbits-don-t-fall (orbital speed at a given height) and everyday-physics/gravitational-wells (depth of Earth's potential). Neither is listed in the series file's `requires`.

## Outline

1. **GPS is a clock problem**: a receiver finds its position from how long signals take to arrive from several satellites; light covers about 30 cm per nanosecond, so small clock errors become large position errors [verify].
2. **Moving clocks run slow**: by special relativity, a clock moving at orbital speed loses about 7 microseconds a day against a clock on the ground [verify].
3. **Higher clocks run fast**: a clock higher in a gravitational well runs faster; at GPS height this gains about 45 microseconds a day [verify].
4. **Correcting it**: the satellite clocks are set to tick slightly slow before launch so that they match ground time in orbit, and receivers correct a small extra term from each orbit's slight ellipse [verify].
5. **What this means for you**: satellite-guided tractors and sprayers steer to within a few centimeters, which relies on these timing corrections and on extra signals from ground stations [verify].
6. **Key takeaways**

## Key takeaways

- A GPS position fix is a timing measurement, and one nanosecond of clock error is about 30 cm of range error [verify].
- Orbital speed makes a GPS clock lose about 7 microseconds per day [verify].
- Height in Earth's gravity makes it gain about 45 microseconds per day [verify].
- Uncorrected, the net gain of about 38 microseconds a day would add roughly 10 km of range error per day [verify].

## Not in this module

- everyday-physics/why-orbits-don-t-fall: why the satellite moves at the speed it does.
- everyday-physics/gravitational-wells: the shape and depth of Earth's potential well.
- everyday-physics/entropy-and-the-arrow-of-time: why time has a direction, a different question about time.

## Phase 2

- **Show:** clock rate against orbital height, with the speed effect, the height effect and their sum, marking the space station, GPS and geostationary heights.
- **Sources to find:** a relativity textbook or review on relativity in the Global Positioning System; the GPS interface specification for the clock offset; a precision-agriculture source on correction services.
