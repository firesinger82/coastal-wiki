---
title: "XBeach 선박파(ship.F90) — 이동 선박 압력장(hull→수면 depression) → 선박 항주파(wake)·drawdown + 선박 운동/force 옵션"
topic: xbeach
canonical_source: self
citation_status: verified
verification_method: "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/ship.F90 (459) 직접 read — type ship(shipgeom/xCG/yCG/zCG/compute_force/compute_motion 37-44) 구조 file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — 선박 압력장 구조 verbatim"
verification_date: 2026-06-03
related:
  - models/XBeach/source-analysis/xbeach_flow_solver.md
  - models/XBeach/source-analysis/xbeach_nonh.md
---

# XBeach 선박파 (ship.F90)

> `ship.F90`(459) 직접 read. **이동 선박(moving ship)** 이 유발하는 항주파(ship wake)·drawdown 모듈(module `ship_module`). 선체(hull)가 수면에 만드는 압력 depression → 흐름/수위 강제. niche(주운·marina·선박 wake 침식) 기능.

## 1. ship type 구조 (ship.F90:31-44)

```fortran
type ship
   character :: shipgeom        ! 선체 형상 파일(draft 분포)
   real :: xCG, yCG, zCG        ! 무게중심(center of gravity) 위치
   integer :: compute_force     ! (0/1) 선박에 작용하는 force 계산
   integer :: compute_motion    ! (0/1) 파에 의한 선박 운동 계산
```
- 다중 선박(ship array) 지원, 선박별 force/motion on/off.

## 2. 메커니즘

- **압력장**: 선체 draft(흘수) 분포가 정수압 surface depression(squat/drawdown)을 강제 — 이동 압력으로 [[xbeach_flow_solver]]/[[xbeach_nonh]] 의 수면(zs)·운동량에 source. 비정수압([[xbeach_nonh]]) 모드에서 선박파(dispersive wake) 정확.
- **선박 궤적**(track) 따라 이동 → 항주파(Kelvin wake)·drawdown·return current 생성.
- `compute_motion=1`: 파-선박 상호작용(선박이 파에 흔들림, 6-DOF 부분).

## 3. 용도

marina/항만 내 선박 통항 wake → 정박선 동요·연안 침식·세굴 평가. coastal storm 모델과 별개 응용. 한국 연안엔 항만 운영 case.

## 4. 연결

- [[xbeach_nonh]] — 선박파 dispersive wake(비정수압)
- [[xbeach_flow_solver]] — 선박 압력 → 수면/운동량 source
