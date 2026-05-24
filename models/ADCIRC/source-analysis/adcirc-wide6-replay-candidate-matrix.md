---
title: "adcirc wide6 replay candidate matrix"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-wide6-replay-candidate-matrix.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC wide6 Replay Candidate Matrix

Date: 2026-04-13

Purpose:
- separate the retained `wide6` folder into concrete workflow branches
- classify files and steps as final, likely final, historical, or unknown
- prevent future comparison work from mixing incompatible states

Status labels:
- `confirmed final`: strongly tied to the current retained run artifacts
- `likely final`: probably part of the current retained branch, but not fully closed
- `historical only`: clearly belongs to an earlier branch
- `unknown provenance`: retained artifact exists, but exact branch tie is not yet reconstructable

## Branch Summary

### Branch A. Mesh-generation baseline

Meaning:
- the branch that produced the retained `fort.14`

Current confidence:
- strongest branch in the folder

Main signature:
- OceanMesh2D
- `mainland.shp` + `ocean_new_w6.shp`
- `GEBCO + BADA2024`
- later manual boundary correction

### Branch B. Early tidal-validation branch

Meaning:
- the first `FES2022b` validation path before later tuning

Main signature:
- `Run1`
- `FES2022b`
- no SAL tuning yet
- weaker validation metrics

### Branch C. SAL tuning branch

Meaning:
- the intermediate branch that added `fort.24`, `NTIP=2`, and depth-based Manning updates

Main signature:
- `Phase 0: SAL`
- `Phase 1: Manning`
- `run.bat` upgraded to 18 cores

### Branch D. Current retained run branch

Meaning:
- the branch reflected by the current retained `fort.13`, `fort.15`, `run.bat`, and run outputs

Main signature:
- `tide_nao99jb`
- `Run4`
- 18-core run
- validation metrics improved versus `Run1`

Important warning:
- this branch is not cleanly reproducible yet
- some retained files still do not map exactly to one retained generator script

## File Matrix

| Item | Classification | Most likely branch | Evidence | Note |
| --- | --- | --- | --- | --- |
| `input/mainland.shp` | `confirmed final` | A | referenced by `make_mesh_om2d.m`, retained in final mesh folder | core domain input |
| `input/ocean_new_w6.shp` | `confirmed final` | A | referenced by `make_mesh_om2d.m`, used in boundary-fix scripts | core offshore/open-boundary input |
| `input/korea_coast_2025.shp` | `confirmed final` | A | referenced by `make_mesh_om2d.m` | Level-2 coastline input |
| `input/DEM/gebco_450m.nc` | `confirmed final` | A | referenced by mesh and preprocessing scripts | core DEM input |
| `input/DEM/BADA2024.nc` | `confirmed final` | A | referenced by `make_mesh_om2d.m` | Korean override DEM |
| `scripts/make_mesh_om2d.m` | `confirmed final` | A | strongest direct match to retained `fort.14` | best replay anchor for mesh branch |
| `output/oceanmesh2d/fort.14` | `confirmed final` | A | structurally checked directly | real retained mesh artifact |
| `scripts/classify_boundaries.py` | `likely final` | A | matches manual boundary-correction narrative | interactive correction path |
| `scripts/fix_boundaries.py` | `likely final` | A | rewrites `fort.14` boundary block | semi-automatic correction path |
| `scripts/draw_ocean_boundary.py` | `likely final` | A | matches manual offshore-arc narrative | likely part of domain-design stage |
| `output/design/*.png` | `likely final` | A | supports domain-design narrative | design evidence, not final generator |
| `scripts/make_fort15.py` | `historical only` | B | writes `FES2022b` path; later log shows branch drift | not current retained `fort.15` |
| `scripts/validate_tidal_harmonics.py` | `likely final` | B,C,D | explicitly cited in log for multiple runs | postprocessing script reused across branches |
| `output/validation/tidal_validation_summary.txt` | `likely final` | D | matches later improved metrics | retained validation summary likely from later branch |
| `scripts/make_fort24_v2.py` | `historical only` | C | cited in `Run2` SAL step | SAL branch artifact |
| `scripts/make_fort24_and_update.py` | `historical only` | C | cited in `Run2` SAL + Manning update | not equal to current retained `fort.13` |
| `output/oceanmesh2d/fort.13.bak_phase2_3` | `historical only` | C | preserved before later phase updates | older retained state |
| `output/oceanmesh2d/fort.15.bak_phase2_3` | `historical only` | C | preserved before later phase updates | older retained state |
| `scripts/tune_phase2_3.py` | `historical only` | C | explicitly modifies `RNDAY 20 -> 30` and Manning | current `fort.13` does not match exactly |
| `scripts/make_fort15_nao99jb.py` | `likely final` | D | current `fort.15` has `tide_nao99jb`; script writes same identity | strongest retained match for current `fort.15` |
| `output/oceanmesh2d/fort.15` | `confirmed final` | D | direct retained run artifact | current branch control file |
| `output/oceanmesh2d/run.bat` | `confirmed final` | D | says `Run4 (NAO99jb + Manning tuning)` and uses 18 cores | current retained run launcher |
| `output/oceanmesh2d/fort.13` | `unknown provenance` | D | retained final artifact but Manning values do not map cleanly to retained scripts | current major provenance gap |
| `output/oceanmesh2d/fort.63.nc` | `confirmed final` | D | produced by retained run branch | current main run output |
| `output/oceanmesh2d/fort.64.nc` | `confirmed final` | D | produced by retained run branch | current main run output |
| `output/oceanmesh2d/maxele.63.nc` | `confirmed final` | D | produced by retained run branch | retained summary output |
| `output/oceanmesh2d/maxvel.63.nc` | `confirmed final` | D | produced by retained run branch | retained summary output |

## Step Matrix

| Step | Classification | Branch | Evidence | Note |
| --- | --- | --- | --- | --- |
| offshore boundary designed manually | `confirmed final` | A | `WORK_LOG.md`, boundary design scripts, retained shapefile | essential manual stage |
| OceanMesh2D mesh generation with 2-level `fs=3` setup | `confirmed final` | A | `make_mesh_om2d.m`, `matlab_log.txt`, retained `fort.14` | main mesh-generation step |
| GEBCO interpolation plus BADA override | `confirmed final` | A | `make_mesh_om2d.m`, retained DEM files | bathymetry branch anchor |
| OceanMesh2D auto boundary classification accepted as-is | `historical only` | none | contradicted by log and retained correction scripts | should not be assumed |
| manual/GUI boundary correction | `confirmed final` | A | `WORK_LOG.md`, `classify_boundaries.py`, `fix_boundaries.py` | essential retained step |
| FES2022b-only tidal validation run | `historical only` | B | `Run1` in `WORK_LOG.md` | earlier branch |
| SAL activation through `fort.24` | `historical only` | C | `Run2` in `WORK_LOG.md` | later intermediate branch |
| NAO99jb-based retained control file | `confirmed final` | D | current `fort.15`, `run.bat`, later work log context | current retained run branch |
| current Manning tuning path | `unknown provenance` | D | current `fort.13` exists, but exact generator path is not closed | biggest remaining gap |
| 18-core retained run | `confirmed final` | D | `run.bat`, retained PE folders and output timestamps | current run branch |
| later improved validation metrics | `likely final` | D | later work log metrics match retained summary | very likely current branch result |

## Strongest Closed Chain

The strongest currently closed chain is:
1. domain inputs under `input/`
2. `make_mesh_om2d.m`
3. retained `fort.14`
4. boundary correction via manual or semi-manual scripts

This chain is still not fully replayable, but it is the strongest part of `wide6`.

## Main Mixed Zone

The main mixed zone is:
- `fort.13`
- `fort.15`
- run-era tuning notes in `WORK_LOG.md`

Why:
- early log notes describe `FES2022b`
- current retained `fort.15` is `NAO99jb`
- current retained `fort.13` has Manning values not exactly reproduced by the retained generator scripts

## Practical Rule

Until provenance is closed:
- compare Python mesh tools against Branch A first
- do not ask them to match the full current retained run branch
- treat `fort.13` and `fort.15` as separate reconstruction tasks

## Immediate Follow-Up

The next high-value document is:
- `wide6 retained run branch reconstruction`

That document should focus only on:
- current `fort.13`
- current `fort.15`
- `run.bat`
- validation outputs

and ignore the earlier mesh-generation history except where necessary.
