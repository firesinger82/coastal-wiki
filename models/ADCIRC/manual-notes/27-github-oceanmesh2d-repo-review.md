---
citation_status: source-needed
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/27-github-oceanmesh2d-repo-review.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: P2 catalog (audit deferred to per-note verification)
---
# GitHub OceanMesh2D Repo Review

Date: 2026-04-13

Repository:
- https://github.com/CHLNDDEV/OceanMesh2D

## What The Repo Says

Observed on the repository page:
- language focus is MATLAB
- recommended branch is `Projection`
- repository structure includes `@geodata`, `@edgefx`, `@meshgen`, `@msh`
- the README describes these as the four core classes called in sequence
- setup downloads `m_map`, `GSHHG`, and `SRTM15_PLUS`
- the page shows release `6.0.0` dated `2024-02-28`

## Why It Matters Locally

This repo matches the architecture already visible in the local `make_mesh_om2d.m` script:
- `geodata`
- `edgefx`
- `meshgen`
- `msh`

That makes it the strongest conceptual and implementation match to the current `wide6` baseline.

## Practical Assessment

Strengths:
- direct match to the local working branch
- mature ADCIRC-oriented pre/postprocessing ecosystem
- built-in concepts for bathymetry, boundaries, and mesh writing

Weaknesses:
- MATLAB dependency remains
- some working behavior may depend on OceanMesh2D internals rather than only on the visible script

## Local Relevance

Current conclusion:
- this is still the canonical upstream reference for understanding and preserving `wide6`
