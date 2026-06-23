---
title: "Acceleration of an algebraic multigrid pressure solver using graph neural networks"
source: arxiv
arxiv_id: 2606.19251v1
seed: KHOA
authors: Eric Chillón, Artur K. Lidtke, Nguyen Anh Khoa Doan, Bernat Font
published: 2026-06-17

link: https://arxiv.org/abs/2606.19251v1
arxiv_categories: physics.comp-ph, cs.LG, physics.flu-dyn
citation_status: draft-unsourced
action: archive
collected: 2026-06-22T00:06:41.151631+00:00
---

## Abstract

Solving the pressure-Poisson equation remains the primary computational bottleneck in incompressible unstructured flow solvers primarily due to the inherent sensitivity of traditional linear solvers to mesh irregularities. This work introduces a data-driven algebraic multigrid (AMG) smoother that uses a modified graph convolutional isomorphism network (GCIN). The graph neural network predicts optimal polynomial coefficients to construct a sparse pseudo-inverse operator across diverse grid topologies. The coefficients are optimized to reduce the residual after each V-cycle iteration. By directly capturing the algebraic structure of the system from the sparse coefficient matrix, the proposed method maintains the solver's linearity while adapting to local anisotropies in unstructured grids. Our framework demonstrates significant performance gains by reducing the number of V-cycles required for a given tolerance and delivering wall-clock speedups from 4% to 37% across diverse benchmarks. Notably, the model exhibits robust generalization by maintaining efficiency on meshes up to 128 times larger than those seen in training, and by accelerating the solver's convergence on unseen industry-relevant problems such as the AirfRANS dataset.

## Acquisition

- Open Access: download from arXiv link above
- Closed Access: use Sci-Hub suggestion below (manual approval required)
- Sci-Hub URL: https://sci-hub.se/2606.19251v1

## Triage Notes

- source_type: arxiv (primary archive)
- citation_status remains draft-unsourced until full-text verified
- Never auto-promote to verified
