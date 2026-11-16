---
id: engineering/3d-printing-basics
title: 3D printing basics
level: introductory
---

**Promise:** Explain how the common 3D printing processes build a part layer by layer, and design a part that prints and holds up.

**Trap:** "A printed part is as strong as the same shape molded from the same plastic." Layers bond more weakly than the material within a layer, so strength depends on print direction, settings and process, not on the shape alone.

**Assumes:** None.

## Outline

1. **From model to layers**: a 3D model becomes a surface mesh, a slicer cuts it into layers and toolpaths, and the printer builds it bottom up. Name the file formats in plain text [verify].
2. **The main processes**: extruded filament (FDM), cured resin (SLA and related) and fused powder (SLS) differ in resolution, materials, cost and finish [verify]. Pick by what the part must do.
3. **Design rules that follow from layers**: overhangs need support beyond a critical angle, thin walls and small holes have minimums, and bridges sag [verify]. Orient the part so loads do not pull layers apart.
4. **Settings that change the part**: layer height, wall count, infill pattern and density trade time against strength and weight. Infill is the hidden lattice inside most printed parts.
5. **From prototype to use**: tolerances, shrinkage and warping, post-processing, and material choice for skin contact, heat or outdoor use. Say when printing is the wrong process.
6. **What this means for you**: printing teaches the same lesson as a forecast pipeline: the output depends on settings you can forget you chose; record them with the part, as you would record parameters with a run.

## Key takeaways

- A printed part is usually weakest across its layer lines, so orientation relative to the load matters as much as the shape [verify].
- Overhangs beyond a process-dependent angle need support material or a redesign [verify].
- Infill density and pattern change a part's weight and stiffness more than its outer shape suggests.
- The choice between filament, resin and powder processes is a trade among resolution, strength, cost and surface finish, with no single best option.

## Not in this module

- Why the cast used a lattice and which lattice: engineering/why-triangles-3d-printed-cast-geometry.
- Computing stress in a printed part: engineering/finite-elements-in-ten-minutes.

## Phase 2

- **Show:** the same bracket printed in two orientations, with arrows showing the load running along or across the layer lines.
- **Sources to find:** the ISO/ASTM additive manufacturing terminology standard; manufacturer design guides; published tensile tests of printed parts by orientation.
