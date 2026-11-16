---
id: everyday-physics/why-computers-get-hot
title: "Why computers get hot"
level: introductory
---

**Promise:** Trace a computer's heat to its sources: charging and draining tiny wires and transistors billions of times a second, current leaking through switches that are off, and moving data around.

**Trap:** "Computers get hot because computing, or erasing information, has a basic energy cost." That cost, Landauer's limit, is millions of times smaller than what chips use; the heat comes from the electrical engineering of switching, not from the thermodynamics of information.

**Assumes:** everyday-physics/landauer-s-limit (the minimum heat of erasing a bit, and how far present hardware sits above it).

## Outline

1. **Every watt in becomes a watt of heat**: a computer does no lasting work on the world, so all the electricity it draws ends up as heat in the room.
2. **Switching fills and empties tiny buckets**: each wire and transistor gate is a small capacitor; every time a bit flips, charge flows in or out through resistance, and that energy turns to heat.
3. **Leakage**: transistors so small do not switch fully off, so current trickles through even when nothing happens.
4. **Why chips stopped getting faster**: shrinking transistors once cut energy per switch enough to raise clock speeds freely; around the mid-2000s the voltage could no longer fall and heat capped clock speeds [verify]; moving data now often costs more energy than computing on it [verify].
5. **What this means for you**: weather forecast centers run some of the largest supercomputers, and their power and cooling budgets limit how fine a forecast grid they can afford [verify].
6. **Key takeaways**

## Key takeaways

- All the electricity a computer draws ends up as heat.
- Most of a chip's heat comes from charging and discharging wire and gate capacitance and from leakage current.
- Clock speeds of desktop processors have stayed near a few gigahertz since the mid-2000s, mainly because of heat [verify].
- Fetching data from main memory costs more energy than an arithmetic operation on it, by a large factor [verify].

## Not in this module

- everyday-physics/landauer-s-limit: the erasure bound and its comparison with present hardware.
- everyday-physics/information-exchange-versus-energy: information as the basis of physics.
- everyday-physics/how-a-fridge-works: how heat is pumped away.

## Phase 2

- **Show:** a stacked bar of where a processor's power goes (switching, leakage, data movement), set against the Landauer minimum on a log scale.
- **Sources to find:** a computer-architecture textbook on dynamic and static power; papers on the end of Dennard scaling and on energy per operation versus memory access; a weather-center report on supercomputer power.
