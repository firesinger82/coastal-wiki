---
title: "swan diffraction obstacles"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-diffraction-obstacles.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

The phase-decoupled diffraction approximation (`DIFFRAC`) — eikonal-based formulation, the smoothing parameters `SMPAR/SMNUM`, where it modifies propagation velocities (not as a separate source term), the `OBSTACLE` polyline syntax, transmission (`TRANS`) vs reflection (`REFL`) options, specular vs scattered reflection (`RSPEC` vs `RDIFF`), how structured grids use orthogonal `CROSS(2,MCGRD)` link marking (no diagonal), how unstructured face-based `SwanFindObstacles` works, and the limitations (no phase-resolving). Use this when configuring breakwaters, harbor entrances, or coastal structures.

## Source basis

- `swanpre1.ftn:944-1286, 2106-2114` — `OBSTACLE` and `DIFFRAC` parsers.
- `SwanDiffPar.ftn90:44-204` — eikonal diffraction.
- `swancom5.ftn:1077-1608, 2148-2188, 5527-5717, 5881` — propagation velocity modification, smoothing.
- `swanser.ftn:2420-3699` — structured obstacle marking, reflection.
- `SwanPrepComp.ftn90:87`, `SwanFindObstacles.ftn90:103-127`, `SwanCompUnstruc.ftn90:780-1080`, `SwanPropvelX.ftn90:92`, `SwanPropvelS.ftn90:269` — unstructured.
- `swanmain.ftn:6394-6455` — disable in GEN4/QC scattering.

## A. DIFFRAC activation / formulation

`DIFFRAC` parsed as `DIFFRac [idiffr] [smpar] [smnum] [cgmod]` (`swanpre1.ftn:2106`).

Defaults when keyword present (`:2114`):
- `IDIFFR=1`.
- `SMPAR=0`.
- `SMNUM=0`.
- `CGMOD=1`.

Disabled for GEN4/QC scattering (`swanmain.ftn:6394, 6454`).

Eikonal-based formulation (`SwanDiffPar.ftn90:44-60`):
```
K = k · √(1 + δ)
δ = D · ∇(D∇H) / (k² · H)
```

Structured grid stores `DIFPARAM = SQRT(1 + δ)` (`swancom5.ftn:5532, 5881`).

This is the "phase-decoupled" approximation — modifies wave-number magnitude but does **not** track phase.

## B. Smoothing (SMPAR, SMNUM)

Structured grids smooth energy field before computing diffraction:
```
E(i,j) = (1−4α)·E(i,j) + α·(E(i−1,j)+E(i+1,j)+E(i,j−1)+E(i,j+1))
```
(`swancom5.ftn:5527`).

- `SMNUM` controls iteration count: `DO ISM = 1, INT(PDIFFR(2))` (`:5683-5685`).
- `SMPAR` is `α`: `TMP = PDIFFR(1)` (`:5709`).

Smoothing avoids crossing land/obstacles by checking `CROSS` and depth before applying neighbor contributions (`:5710-5717`).

Typical settings: `SMPAR=0.2, SMNUM=5` for harbor cases; defaults `0,0` effectively disable smoothing.

## C. OBSTACLE: TRANS vs REFL

`OBSTACLE` syntax includes transmission options + optional `REFLec` (`swanpre1.ftn:944-958`).

**`TRANS`**: reads coefficient in `[0,1]`, stored in `TRCOEF(1)` (`:1082-1089`). Default = 0 (full obstacle) (`:1111`).

**`REFL`**: enables reflection only with full-circle directions; reads `REFLC` (`:1147-1150`). Defaults to no reflection when absent (`:1203`).

So a default `OBSTACLE` is fully blocking; you must specify `TRANS 0.5` (50% pass-through) or `REFL 0.7` (70% reflection) explicitly.

## D. Specular vs scattered reflection (RSPEC vs RDIFF)

- `RDIFF` sets `LREFDIFF=1`; reads integer nonneg `POWN` (`swanpre1.ftn:1161-1173`).
- `RSPEC` (default) is ignored; `LREFDIFF=0`.

In `REFLECT`:
- `LREFDIFF=0` → one-bin specular filter `PRDIF(0)=1` (`swanser.ftn:3655`).
- `LREFDIFF=1` → cosine-power scattering: `PRDIF(ID) = COS(ID*DDIR)^POWN`, normalized by `SUMRD` (`:3685-3699`).

Use `RDIFF` for rough breakwaters or natural shorelines where reflection is diffuse.

## E. Obstacle segment definition (LINE)

Obstacles are polylines: `LINE` reads repeated corner points into `XCRP/YCRP`, requires ≥ 2 points (`swanpre1.ftn:1251-1286`).

Structured obstacle detection marks **only two orthogonal grid links per point** in `CROSS(2, MCGRD)`:
- Link 1 = x-neighbor.
- Link 2 = y-neighbor.

(`swanser.ftn:2420-2512`).

**There is no diagonal-link representation in structured SWAN**. Obstacles are approximated as orthogonal grid-edge crossings.

Reflection code warns: only one obstacle intersection per computational grid cell; avoid sharp edges (`swanser.ftn:3611-3619`).

## F. Quadtree / unstructured obstacles

**No quadtree-specific obstacle index** found.

Unstructured handling is face-based:
- `SwanPrepComp` calls `SwanFindObstacles` (`SwanPrepComp.ftn90:87`).
- Loops over obstacle segments + non-boundary faces (`SwanFindObstacles.ftn90:103-127`).
- Marks `cross(iface) = j` when face and obstacle segment intersect.

During unstructured computation, crossed faces mapped to two local stencil links and passed to `SWTRCF` (`SwanCompUnstruc.ftn90:1039-1080`).

So unstructured obstacle handling is more flexible than structured (any face can be crossed; no orthogonality restriction).

## G. Where diffraction enters

**Diffraction is NOT a separate source term** — it modifies propagation velocities.

Structured grids:
- `SPROXY` multiplies spatial velocities `CAX/CAY` by `DIFPARAM` (`swancom5.ftn:1077-1082`).
- Directional propagation `CAD` adjusted using `DIFPARAM, DIFPARDX, DIFPARDY` (`:1606-1608`).

Velocities enter transport matrix via `STRSXY` — `CAX/CAY` form `FXY1/FXY2` added to `IMATDA/IMATRA` (`:2148-2188`).

Unstructured:
- Diffraction computed before transport.
- `SwanTranspAc` uses modified velocities (`SwanCompUnstruc.ftn90:780-1080`).

## H. Limitations

This is **phase-decoupled, not phase-resolving** (`swanmain.ftn:6395, 6455`).

Computed diffraction state is only scalar `DIFPARAM` and gradients — derived from action density / energy / wave height, **not phase** (`swmod2.ftn:1325`, `SwanDiffPar.ftn90:174-204`).

For phase-resolving wave models (BoussInes/MILDSLP/full Navier-Stokes), use a different model (Boussinesq, BOUSS, FUNWAVE).

Disabled in:
- GEN4 (shallow-water-only physics).
- QC scattering.

## Decision Guide

| Goal | Setup |
|---|---|
| Harbor with breakwaters | `OBSTACLE LINE x1 y1 x2 y2 TRANS 0.0 REFL 0.6 RDIFF 4` (60% reflection, diffuse) |
| Submerged reef partial transmission | `OBSTACLE LINE ... TRANS 0.5` |
| Sharp breakwater specular reflection | `OBSTACLE LINE ... REFL 0.8 RSPEC` (default) |
| Diffraction near coastal structures | `DIFFRAC` (default `IDIFFR=1`) with `SMPAR=0.2, SMNUM=5` |
| Phase-resolving short-wave detail | Don't use SWAN; use Boussinesq model |
| Shallow-water surf zone | `GEN4` (auto-disables DIFFRAC) |
| Storm with main interest in offshore | Skip DIFFRAC (default off); structures don't matter at coarse grid |

## Working Rules

- For most coastal applications, DIFFRAC is unnecessary — leave default off.
- When using DIFFRAC, smoothing (`SMPAR=0.2, SMNUM=5`) is essential to avoid noise; raw DIFFRAC with `SMPAR=0` produces oscillatory `DIFPARAM`.
- Obstacle polylines: 2 points (line segment) is the simplest; many points trace curved structures.
- Avoid structures that exactly diagonal-cross grid cells — structured SWAN can only cross orthogonal links.
- For unstructured grids near coasts with structures, ensure mesh resolution ≥ structure scale × 4.
- `RDIFF POWN=2` to `8` typical for natural shorelines (sand: 4; rocky: 8); `RSPEC` for engineered concrete.
- Output `BLOCK ... DIFPARAM` to verify diffraction is active and not pathological.

## Common Pitfalls

- ▢ Setting `OBSTACLE LINE` without `TRANS` — defaults to fully blocking; if you wanted partial pass, set `TRANS=0.5`.
- ▢ `OBSTACLE` near boundary — interactions with BC; result undefined.
- ▢ Two obstacles crossing same cell — warns and may misbehave (`swanser.ftn:3611-3619`).
- ▢ Using `DIFFRAC` with `GEN4` — auto-disabled silently.
- ▢ Expecting full diffraction pattern (interference, side-lobes) — phase-decoupled doesn't reproduce these; only intensity-modulation.
- ▢ Setting `SMPAR > 0.25` — over-smoothing; physical features lost.
- ▢ Polyline with collinear points — degenerate; obstacle not detected.
- ▢ Unstructured with `OBSTACLE`: face crossings count, but if obstacle is along a vertex (no face crossing), not detected.

## Next expansion

- Comparison vs Boussinesq for harbor agitation problem.
- DIFFRAC `SMPAR/SMNUM` tuning recipe.
- Multiple-obstacle interaction validation case.

## References

- Holthuijsen et al. 2003 (phase-decoupled diffraction).
- SWAN User Manual (Obstacles and Diffraction).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/swan/source_code/swan/src`. Auto-draft = false; review_required = true.
