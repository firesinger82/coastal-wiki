---
citation_status: source-needed
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/32-wide6-open-boundary-depth-check.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: local-workflow-notes
source_id: models/ADCIRC
notes: "local user workflow (E:\\ paths) — not external doc catalog. source-needed retained; verified status requires raw file presence audit. Future home may be experience/ or source-analysis/."
---
# wide6 Open-Boundary Depth Check

Date: 2026-04-13

Target:
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6\output\oceanmesh2d\fort.14`

Purpose:
- inspect the retained `wide6` open boundary directly
- determine whether the shallowest open-boundary point is an isolated endpoint issue or a larger segment problem

## Summary

The retained `wide6` open boundary is mostly deep-water.

But:
- the shallowest open-boundary node is `217.727 m`
- this is shallower than the retained `WORK_LOG.md` claim of `283 m`
- the shallow point is not a long shallow segment
- it is a boundary-endpoint issue concentrated at the final node of the open boundary chain

## Direct Counts

Open boundary:
- count: `70` nodes

Threshold counts:
- `< 250 m`: `1`
- `< 283 m`: `1`
- `< 300 m`: `1`
- `< 500 m`: `3`
- `< 1000 m`: `7`

Interpretation:
- the open boundary is not broadly shallow
- the mismatch to the log is driven by a very small number of endpoint nodes

## Shallowest Nodes

Top shallow nodes on the retained open boundary:

1. idx `70`
   - node id: `430061`
   - lon/lat: `122.299869`, `18.155840`
   - depth: `217.727 m`

2. idx `69`
   - node id: `432008`
   - lon/lat: `122.324147`, `18.156999`
   - depth: `328.738 m`

3. idx `68`
   - node id: `433802`
   - lon/lat: `122.352857`, `18.158397`
   - depth: `395.405 m`

After that the depth rises back above `500 m`.

## Segment Interpretation

Using the retained open-boundary node order:
- only one node is below `283 m`
- only three nodes are below `500 m`
- the `< 283 m` segment is:
  - idx `70` to `70`
  - count `1`

Interpretation:
- this is not evidence of a badly placed shallow open boundary along a long reach
- it is evidence of one shallow endpoint that may have survived the cleanup rule

## Geometric Context

Open-boundary first node:
- idx `01`
- lon/lat `144.137604`, `42.575511`
- depth `572.392 m`

Open-boundary last nodes trend:
- idx `67`: `584.147 m`
- idx `68`: `395.405 m`
- idx `69`: `328.738 m`
- idx `70`: `217.727 m`

Interpretation:
- the boundary remains deep over most of its length
- shallowing happens at the trailing end near the southwest endpoint

## Judgement

What this means:
- the retained `wide6` open boundary is not obviously invalid on depth grounds alone
- but the endpoint cleanup rule was not perfectly enforced in the retained artifact

What this does **not** yet tell us:
- whether the shallow endpoint materially harms tides or surge
- whether trimming the last one to three nodes would improve validation
- whether this endpoint was intentionally kept for geometric continuity

## Next Question

The next useful check is:
- inspect the open-boundary endpoint geometry and nearby elements directly

That check should answer:
- whether the `217.727 m` node is an acceptable corner artifact
- or whether the open boundary should be shortened slightly in a future cleanup pass
