---
title: "Delft3D-FLOW(structured) 보조 compute 맵 — adv2d(2D advection) + calbf/calksc/trtrou(bed roughness) + tur2d(HLES 수평난류) + sourmu(운동량 source) + Z-layer(z_uzd/z_vermom_finvol/z_difuflux) + culver(culvert) + f0isf1"
topic: delft3d
canonical_source: self
citation_status: verified
verification_method: "models/Delft3D/raw/source_code/Delft3D/src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src/compute/ 직접 read — adv2d/calbf/calksc/trtrou/tur2d/sourmu/z_uzd/z_vermom_finvol/z_difuflux/culver/f0isf1.f90 파일·subroutine 인용. ADI 코어는 [[delft3d_adi_solver]]."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-04
verification_by: "Claude Opus 4.8 (1M context) — flow2d3d 보조 compute 인벤토리"
verification_date: 2026-06-04
related:
  - models/Delft3D/source-analysis/delft3d_adi_solver.md
  - models/Delft3D/source-analysis/delft3d_turbulence.md
  - models/Delft3D/source-analysis/delft3d_sigma_z.md
---

# Delft3D-FLOW(structured) 보조 compute 맵

> `flow2d3d_kernel/src/compute/` 의 ADI 코어([[delft3d_adi_solver]] adi/sud/uzd/difu) 외 **보조 compute 루틴** 종합. 전 소스 커버용 map.

## 1. Advection·운동량 source

- **adv2d.f90**(558): **2D depth-averaged advection**(운동량 이송, 2D run 또는 barotropic). cyclic/upwind/flux scheme.
- **sourmu.f90**(491): **운동량 source 항** 조립(wind·atm pressure·tide-generating·secondary flow·structure 등 외력을 운동량 RHS 로).

## 2. Bed roughness (calbf / calksc / trtrou)

- **calbf.f90**(441): **bottom friction** 계수 — Chézy/Manning/White-Colebrook 에서 `taubot` 산출(uzd/sud bottom drag).
- **calksc.f90**(430): bed roughness height `ksc`(Nikuradse) — wave-current·ripple 의존 roughness.
- **trtrou.f90**(974): **trachytope** roughness — land-use/cover 별 roughness 합성(composite, 식생·urban·bedform 분류 → Chézy). 공간변화 조도 시스템.

## 3. 수평 난류 — tur2d (HLES)

- **tur2d.f90**(823): **HLES**(Horizontal Large Eddy Simulation) — 2D 수평 난류(sub-grid horizontal eddy viscosity, Uittenbogaard). ROMS hmixing([[../ROMS/source-analysis/roms_horizontal_mixing]] Smagorinsky)·연직 [[delft3d_turbulence]]와 별개.

## 4. Z-layer compute (z_*)

σ-layer 외 **Z-coordinate**([[delft3d_sigma_z]]) 전용:
- **z_uzd.f90**(1481): Z-layer 운동량(UZD 의 Z 버전, layer 절단 처리).
- **z_vermom_finvol.f90**(523): Z-layer **연직 운동량 finite-volume**(비정수압/연직 advection).
- **z_difuflux.f90**(488): Z-layer transport **diffusive flux**(difu 의 Z 버전).
- z_cucbp_nhfull / z_disbub: Z 비정수압·기포 plume.

## 5. 구조물·기타

- **culver.f90**(604): **culvert**(암거) 구조물 — 수위차 기반 통수량.
- **f0isf1.f90**(507): time level 복사(`f0 = f1`, 시간전진 swap).
- disbub.f90: bubble screen(기포막, oxygenation/방류).

## 6. 연결

- [[delft3d_adi_solver]] — ADI 코어(본 보조가 지원: calbf→taubot, sourmu→운동량, adv2d/z_uzd)
- [[delft3d_turbulence]] — 연직 난류(tur2d=수평 별개)
- [[delft3d_sigma_z]] — Z-layer(z_* compute)
- [[../ROMS/source-analysis/roms_horizontal_mixing]] — tur2d HLES 대응
