---
title: "D-Flow FM(unstructured) 보조 compute 맵 — advec(u0/q0 advection) + sethu(upwind hu/au) + setucx*(edge→cell velocity 재구성, Perot/least-square) + volume_table(1d wet/dry) + structure_parameters/m_longculverts/m_dambreak_breach(구조물) + setship + update_verticalprofiles(난류)"
topic: delft3d
canonical_source: self
citation_status: verified
verification_method: "models/Delft3D/raw/source_code/Delft3D/src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/dflowfm_kernel/compute/ 직접 read — advec.f90(u0,q0)/sethu.f90(upwind hu au)/setucxucyucxuucyunew.f90(velocity reconstruction Coriolis)/setucxcuy_leastsquare/volume_table.f90(1d node)/structure_parameters/m_longculverts/m_dambreak_breach_submodule/setship/update_verticalprofiles file:line 인용. 코어는 [[delft3d_dflowfm_kernel_scheme]]."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-04
verification_by: "Claude Opus 4.8 (1M context) — dflowfm 보조 compute 인벤토리"
verification_date: 2026-06-04
related:
  - models/Delft3D/source-analysis/delft3d_dflowfm_kernel_scheme.md
  - models/Delft3D/source-analysis/delft3d_dflowfm_overview.md
---

# D-Flow FM(unstructured) 보조 compute 맵

> `dflowfm_kernel/compute/` 의 핵심 solver([[delft3d_dflowfm_kernel_scheme]] furu/s1nod/step_reduce) 외 **보조 compute** 종합. 전 소스 커버용 map.

## 1. Advection·velocity 재구성

- **advec.f90**(1277): **운동량 advection**(u0·q0 기반) — edge velocity 의 비선형 이송. Perot-type/higher-order flux. furu 의 `ru`(explicit advection) 항 산출.
- **sethu.f90**(791): edge **upwind 수심 `hu`·통수단면 `au`** 설정 — 비정형 edge 의 wetting(상류 수심). volume·flux 의 기초.
- **setucxucyucxuucyunew.f90**(1163) / **setucxcuy_leastsquare.f90**(761): **cell-center velocity 재구성** — edge normal velocity `u` 로부터 cell 중심 `ucx/ucy`(vector) 복원(Perot 가중 또는 least-square). **Coriolis·advection·출력**에 필요(staggered 의 약점 보완). `setumod` = velocity magnitude.

## 2. Wetting/drying — volume_table

- **volume_table.f90**(967): **1D node 의 volume-depth table** — 단면(profile) 적분으로 수위↔부피 비선형 관계(1D channel·구조물). `s1nod` 연속방정식의 부피항(Nested Newton, [[delft3d_dflowfm_kernel_scheme]] §4)에 사용. 복잡 단면 wetting/drying.
- **set_kbot_ktop.f90**(721): 3D 연직 layer 의 bottom/top index(부분침수 layer).

## 3. Hydraulic structures

- **structure_parameters.f90**(1052): 구조물 파라미터(weir·gate·pump·culvert·bridge 일반 프레임).
- **m_longculverts.f90**(1654): **long culvert**(긴 암거, 마찰 포함 1D 관로) — 구조물 간 연결.
- **m_dambreak_breach_submodule.f90**(1304): **dam break / breach** — 제방·댐 붕괴 시변 개구부(breach growth) → 범람. ADCIRC TVW weir([[adcirc-weir-boundary]] §4)와 유사.

## 4. 난류·기타

- **update_verticalprofiles.f90**(963): 연직 난류량 계산 + `vertical_profile_u0`(3D velocity 연직분포).
- **setship.f90**(932): **선박**(이동 압력장→drawdown/wake, EFDC/XBeach ship 대응).
- oned_functions.f90(1247): 1D network 함수(cross-section·conveyance).

## 5. 연결

- [[delft3d_dflowfm_kernel_scheme]] — furu/s1nod/step_reduce 코어(본 보조: advec→ru, sethu→hu, volume_table→Nested Newton)
- [[delft3d_dflowfm_overview]] — FM 엔진 개관
- [[adcirc-weir-boundary]] — dam break/weir 대응
