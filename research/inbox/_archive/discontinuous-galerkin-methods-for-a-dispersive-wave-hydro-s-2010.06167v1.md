---
title: "Discontinuous Galerkin methods for a dispersive wave hydro-sediment-morphodynamic model"
source: arxiv
arxiv_id: 2010.06167v1
seed: swash zone
authors: Kazbek Kazhyken, Juha Videman, Clint Dawson
published: 2020-10-11
doi: https://doi.org/10.1016/j.cma.2021.113684
link: https://arxiv.org/abs/2010.06167v1
citation_status: draft-unsourced
action: archive
collected: 2026-06-07T00:00:34.163587+00:00
promoted_to: concepts/sediment-transport/04-code-and-tools.md#10.1
promoted_date: 2026-06-15
---

## Abstract

A dispersive wave hydro-sediment-morphodynamic model developed by complementing the shallow water hydro-sediment-morphodynamic (SHSM) equations with the dispersive term from the Green-Naghdi equations is presented. A numerical solution algorithm for the model based on the second-order Strang operator splitting is presented. The model is partitioned into two parts, (1) the SHSM equations and (2) the dispersive correction part, which are discretized using discontinuous Galerkin finite element methods. This splitting technique provides a facility to select dynamically regions of a problem domain where the dispersive term is not applied, e.g. wave breaking regions where the dispersive wave model is no longer valid. Algorithms that can handle wetting-drying and detect wave breaking are provided and a number of numerical examples are presented to validate the developed numerical solution algorithm. The results of the simulations indicate that the model is capable of predicting sediment transport and bed morphodynamic processes correctly provided that the empirical models for the suspended and bed load transport are properly calibrated. Moreover, the developed model is able to accurately capture hydrodynamics and wave dispersion effects up to swash zones, and its application is justified for simulations where dispersive wave effects are prevalent.

## Acquisition

- Open Access: download from arXiv link above
- Closed Access: use Sci-Hub suggestion below (manual approval required)
- Sci-Hub URL: https://sci-hub.se/https://doi.org/10.1016/j.cma.2021.113684

## Triage Notes

- source_type: arxiv (primary archive)
- citation_status remains draft-unsourced until full-text verified
- Never auto-promote to verified
