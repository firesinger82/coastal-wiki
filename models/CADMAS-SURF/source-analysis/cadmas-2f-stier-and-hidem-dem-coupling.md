---
title: "CADMAS-2F S티어 + HiDEM(DEM) 결합 — sf_* MPI/IO/메모리 지원 + 구조물파괴 DEM 연성(vf_jphdm·vf_jpcoef·mod_dem) 4번째 결합파트너"
model: CADMAS-SURF
component: src (CADMAS-2F S-tier support + HiDEM coupling)
canonical_source: self
verification_method: "CADMAS-SURF/3D2F 소스 전수 카탈로그 (raw/.../CADMAS-SURF-3D2F/Source code/, 388 파일 C티어 2노트 외 잔여). vf_* 대부분 SURF/3D 공유 확인(SMAC·VOF·k-ε·MPI·nesting·IO·입력) + sf_* 지원(sf_mpi/c_mpi/stm_mpi 27·메모리 sf_alloc/dealloc 8·restart/ENS 9). HiDEM firming read: vf_jphdm1.f:1-7(HiDEM 인터페이스 連成領域 확인, use mod_comm comm_2fc_dem)·vf_jpcoef.f:1-8(HiDEM 전용 포텐셜 Poisson)·mod_dem.f90:1-15(ihidem 플래그·comm_2fc_dem). 2상물리=EOS집합 전수 확인(RHOG/ISTATE grep clean, 표면장력·상변화 無). file:line 직접 인용."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-24
related:
  - models/CADMAS-SURF/source-analysis/cadmas-2f-twophase-compressible-gas.md
  - models/CADMAS-SURF/source-analysis/cadmas-2f-structure-coupling-cutcell.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-stier-and-auxiliary-physics.md
---

# CADMAS-2F S티어 + HiDEM(DEM) 결합

> CADMAS-2F 388 파일 중 [C티어 2노트](cadmas-2f-twophase-compressible-gas.md)(압축성 2상·sf_* 구조결합) 외 **잔여 전부**. (A) SURF/3D 공유 vf_* 확인 + (B) **HiDEM(DEM) 결합** = 4번째 결합파트너 + (C) sf_* 지원 카탈로그. 경로 루트: `raw/.../Simulators/CADMAS-SURF-3D2F/Source code/`(239 vf_* + 144 sf_* + mod_* + user_eos).

## A. SURF/3D 공유 vf_* (재분석 불요, 1줄 확인)

2F는 단상 [SURF/3D](cadmas-surf3d-architecture-source-map.md) `vf_*` 인프라 대부분 공유:
- SMAC `vf_v1cal/veuler/vflxd*`(2상은 변밀도항만 추가)·VOF `vf_f1cal/fconv*/fnf*/fbubup`(기포상승=VOF 보조, 압축기상과 별개)·k-ε `vf_k*/cnu*`·스칼라 `vf_s1cal/t1cal`(EOS 비결합 passive)·격자/공극 `vf_cg*/cind*`·MPI `vf_zxmg_*(15)/zxmp_*(21)/p0-3`·nesting `vf_pmg*(22)`·IO `vf_o*`·입력 `vf_ii*(15)`·조파 `vf_bs*/bw*/cwmak*/cwmtb*`·단층소스 `vf_faulti/faultt`+`mod_fault`([SURF/3D 보조물리 B-2](cadmas-surf3d-stier-and-auxiliary-physics.md#b-2--okada-단층--쓰나미-초기수위-지진-소스))·STOC `vf_stoc_init`.

> 2상 고유 물리는 [EOS 집합](cadmas-2f-twophase-compressible-gas.md)뿐(`vf_v1eos/user_eos/vpdrdt/cset2f/vpcoef/vgene/vmodif`). **전수 확인**: RHOG/DRDP/EOS/ISTATE grep = 정확히 그 집합 + 드라이버/Δt/옵션. 표면장력·상변화·잠열·증발/응축·캐비테이션 루틴 **전무**(grep clean, `vf_wsfmb2` `sigma`=파각진동수 not 표면장력). 2상 에너지식 없음(온도=passive).

## B. ★ HiDEM(DEM) 결합 — 4번째 결합파트너

CADMAS-2F 는 **구조물 파괴 해석 DEM 프로그램 HiDEM**(High-performance Discrete Element Method)과 연성 — 쓰나미 표류물/블록 파괴·표류 모사. STOC·STR3D(FEM)·AGENT 에 더한 4번째 MPMD 파트너:
- `mod_dem.f90`(`:1-15`): `ihidem`(연성 플래그 0=무/≠0=연성)·`nsize_dem`(DEM PE수)·`comm_2fc_dem`(통신자 프로세스수/rank)·`ihidm`(HiDEM 대표 rank)
- `vf_jphdm1.f:1-7`(`HiDEMとのインターフェイス(1):連成解析計算領域の確認`, `use mod_comm,only:comm_2fc_dem; use mod_dem`)·`vf_jphdm2.f`(인터페이스 2)
- `vf_jpcoef.f:1-8`(`HiDEM用のポテンシャル関数の連立1次方程式を作成` — HiDEM 인터페이스 전용 포텐셜 Poisson, 대각 양수화 -1.0 승, [SMAC vpcoef](cadmas-surf3d-smac-velocity-pressure-solver.md#4-압력-poisson--포텐셜-함수-pt-vf_vpcoeff)와 동형)·`vf_vpsol.f`(HiDEM Poisson solve)
- HiDEM ↔ 2FC: 압력 & 체적공극 교환(DEM 입자 영역의 유체압). `vf_cgcpr1/2.f`(이동장애물 경계값 1D/2D 복사)

> HiDEM 결합은 [STR3D FSI](str3d-contact-and-fluid-coupling.md)(FEM 연속체)와 다른 **이산요소(DEM, 개별 블록/표류물) 연성** — 표류물 충돌·구조물 붕괴 잔해. 본 repo에 HiDEM 본체는 없음(인터페이스만), comm_2fc_dem 로 외부 HiDEM 실행파일과 MPMD.

## C. sf_* 지원 카탈로그 (144 중 [cut-cell 엔진](cadmas-2f-structure-coupling-cutcell.md) 외)

- MPI 프리미티브(27): `sf_mpi_*`(allreduce/reduce/isend/irecv/send/recv/waitall d&i)·`sf_c_mpi_*`(8 C바인딩)·`sf_comm_*`·`sf_bcast/reduce_{d,i}`
- STOC-구조 MPI(10): `sf_stm_c_mpi_*`·`sf_stm_gather/scatter`·`sf_stm_comm_init/finalize`
- 메모리(8): `sf_alloc0/1·dealloc·realloc·dcopy·icopy·fill·remv`
- restart/IO/ENS(9): `sf_rd/wt_restart·send_rst·send_surf·recv_cont·rd_obst·ens_geom·ens_out·comm_init`
- 깊이/초기(8): `sf_dpth_init/update·intpl_dpth·gdpth·cinit·pos_init·prsini`

> 결론: CADMAS-2F 388 전 파일 포섭. 2상물리=EOS집합(전수확인) + sf_* 구조결합/지원 + ★HiDEM(DEM) 결합(4번째 파트너). 멀티피직스 사슬: 유체(STOC/CADMAS)→FEM(STR3D)·DEM(HiDEM)·피난(AGENT).
