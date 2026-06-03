---
title: "D-Flow FM 수치 scheme (furu + s1nod + step_reduce_hydro) — Stelling-Kernkamp semi-implicit FV: furu(edge velocity u1=fu·∇s1+ru) → s1nod(연속 SPD 행렬 A·s1=d) → Guus solver + Nested Newton(wet/dry 양정치)"
topic: delft3d
canonical_source: self
citation_status: verified
verification_method: "models/Delft3D/raw/source_code/Delft3D/src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/dflowfm_kernel/compute/ 직접 read — furu.f90(fu/ru/kfs 44, 2D kmx==0 + 3D) + s1nod.f90(continuity 행렬 bb/dd/a1 45, nonlin) + step_reduce_hydro.f90(s1nod+furu+solve_matrix Guus + firstnniteration Nested Newton 44) file:line 인용. Stelling-Duinmeijer 2003 + Kernkamp 2011."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-04
verification_by: "Claude Opus 4.8 (1M context) — furu/s1nod/step_reduce semi-implicit FV verbatim"
verification_date: 2026-06-04
related:
  - models/Delft3D/source-analysis/delft3d_dflowfm_overview.md
  - models/Delft3D/source-analysis/delft3d_adi_solver.md
---

# D-Flow FM 수치 scheme (furu / s1nod / step_reduce)

> `dflowfm_kernel/compute/` 직접 read. **D-Flow FM(unstructured)의 hydrodynamic solver** equation/code level — [[delft3d_dflowfm_overview]] 가 forward-reference 한 kernel scheme. **Stelling-Duinmeijer(2003) + Kernkamp(2011) semi-implicit staggered finite-volume**. Delft3D-FLOW 의 ADI([[delft3d_adi_solver]])와 대비되는 비정형 엔진 핵심.

## 1. Staggered FV 구성 (Kernkamp 2011)

- **water level `s1`** = cell center(nodes), **velocity `u1`** = edge(flow links) — staggered. mass + momentum conservative.
- 비정형(triangle/quad/curvi 혼합) net. `Ndx`(cell 수)·`Lnx`(edge 수).

## 2. furu.f90 — edge velocity 계수 fu/ru (`furu`, :44) ★

운동량을 **edge velocity 의 선형식**으로 표현:
```
u1(L) = fu(L)·(s1(k2) − s1(k1)) + ru(L)
```
- `fu`(L) = 수위차(barotropic pressure gradient) 계수, `ru`(L) = explicit 항(advection·Coriolis·bed friction·wind·wave 의 합). `kfs` = wet flag.
- advection(slopec, Slopedrop2D droplosses at ridge), bed friction `cfuhi3D`, 2D(kmx==0)/3D 경로. → u1 을 인접 두 cell 수위 s1 의 선형함수로 = continuity 에 대입 가능.

## 3. s1nod.f90 — 연속방정식 행렬 (`s1nod`, :45) ★

각 cell 의 **연속방정식**(`∂vol/∂t = −Σ flux`)에 furu 의 u1=fu·Δs1+ru 를 대입 → **수위 s1 의 선형계** 조립:
```
bb(n)·s1(n) − Σ_links (fu·hu·width)·s1(neighbor) = dd(n)     ! A·s1 = d
```
- `bb`(대각, a1 surface area/Δt + Σ fu·hu), `dd`(RHS, vol0/Δt + Σ ru·hu + boundary), `a1`(cell 면적). **symmetric positive-definite**(M-matrix) → 빠른 해·양정치 보장.
- `nonlin`: wetting/drying 시 vol(s1) 비선형(부피-수위 관계) → Nested Newton(§4).

## 4. step_reduce_hydro.f90 — 해법 driver (`step_reduce_hydro`, :44) ★

```
s1=s0,u1=u0 → [Nested Newton loop]: furu(fu/ru) → s1nod(A,d 조립) → solve_matrix(Guus) → s1
            → furu back-substitute → u1 → 수렴 체크
```
- **`solve_matrix`(m_solve_guus)**: "Guus" solver — minimum-degree reordering + CG/direct 류 SPD 해법(`pack_matrix`+`solve_matrix`). reduce once then conjugate-grad substitute.
- **Nested Newton**(`firstnniteration`, Casulli-Zanolli): wetting/drying 의 부피-수위 비선형을 Newton 반복으로 — **음수 수심 방지(양정치 보장)**, 무조건 안정. 큰 dt 가능.
- semi-implicit: 수위·barotropic 운동량 implicit(θ-method), advection explicit(CFL 제한 완화).

## 5. structured(ADI) vs unstructured(FM) 대비

| | Delft3D-FLOW(ADI) | D-Flow FM |
|---|---|---|
| 격자 | structured curvilinear | unstructured staggered |
| scheme | ADI 2-stage([[delft3d_adi_solver]]) | semi-implicit FV(furu/s1nod) |
| solver | double-sweep tridiagonal | Guus SPD(Nested Newton) |
| 안정 | ADI 무조건 | semi-implicit + Nested Newton |
| ref | Leendertse/Stelling | Stelling-Duinmeijer 2003·Kernkamp 2011 |

## 6. 연결

- [[delft3d_dflowfm_overview]] — FM 엔진 개관(본 노트가 그 equation-level forward-ref 충족)
- [[delft3d_adi_solver]] — structured ADI(대비)
- transport.f90 — constituent 수송(FM, [[delft3d_dflowfm_overview]])
- Stelling & Duinmeijer 2003 / Kernkamp et al. 2011 / Casulli-Zanolli(Nested Newton)
