---
id: engineering/finite-elements-in-ten-minutes
title: Finite elements in ten minutes
level: intermediate
---

**Promise:** Explain what a finite element analysis computes, from mesh to stiffness matrix to stress, and judge whether an FEA result is trustworthy.

**Trap:** "A colorful stress plot from FEA is the answer." The plot is the output of a model whose mesh, material law, loads and boundary conditions you chose; change any of them and the colors change, often more than the design does.

**Assumes:** engineering/why-triangles-3d-printed-cast-geometry.

## Outline

1. **The idea in one picture**: split a shape you cannot solve into many small elements you can, connect them at nodes, and solve for how the nodes move. The cast module's truss solver is the simplest case.
2. **From element to system**: each element relates nodal forces to displacements through a small stiffness matrix; assembly sums them into one global system, the same equation the cast module wrote down. Keep the symbols that module defined.
3. **Boundary conditions and loads**: without fixed supports the system has no unique solution; wrong supports give confident wrong answers. Show this is where most real errors enter.
4. **From displacement to stress**: strain comes from how displacements vary across an element, stress from the material law. Explain why stress is least accurate at sharp corners and supports.
5. **Is the result trustworthy?**: refine the mesh until the quantity of interest stops changing, check against a hand calculation or a known solution, check reaction forces balance the loads. Name the limits of linear elastic analysis (large deformation, buckling, plastic or printed anisotropic material) [verify].
6. **What this means for you**: FEA and a forecast share the same discipline: a model's output is only as good as its inputs and its convergence check, and a confident plot is not evidence. The habit of asking "what happens if I refine or perturb this?" transfers directly.

## Key takeaways

- FEA approximates a continuous body by small elements joined at nodes and solves one linear system for the nodal displacements.
- A structure without enough boundary constraints gives a singular stiffness matrix, so supports are part of the model, not a detail.
- Computed stress near sharp corners and point supports keeps rising as the mesh is refined, so peak values there are not reliable [verify].
- A mesh-convergence check, where the quantity of interest stops changing under refinement, is the minimum evidence that a result is not a mesh artifact.
- Linear elastic FEA does not capture buckling, large deformation or the direction-dependent stiffness of 3D-printed parts without extra modeling [verify].

## Not in this module

- Why triangles, Maxwell's criterion and the cast lattice study: engineering/why-triangles-3d-printed-cast-geometry.
- How the printed part is made and why printing direction matters: engineering/3d-printing-basics.

## Phase 2

- **Show:** a cantilever beam meshed coarse, medium and fine, with tip deflection converging to the hand-calculated value and corner stress not converging.
- **Sources to find:** an introductory finite element textbook; a benchmark problem with a known analytic solution (cantilever, plate with a hole); documentation of an open-source FEA package.
