---
title: "모델 전수 검수 원장 (AUDIT LEDGER) — 9개 모델 문서·소스코드 커버리지 추적"
scope: models
citation_status: reference
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
purpose: "사용자 지시(2026-06-16) '모든 모델은 모든 문서·코드를 전체 검수' 의 분모를 확정하고 검수 진척을 추적 가능하게 만드는 마스터 ledger. 이게 '전수' 의 정의이자 증명."
---

# 모델 전수 검수 원장 (AUDIT LEDGER)

> **목적**: 사용자 지시(2026-06-16) — *모든 모델의 모든 문서·소스코드를 전수 검수*. 본 원장은 그 **분모(전체 목록)** 와 **진척(검수 상태)** 을 한 곳에서 추적한다. 인벤토리는 `find` 결정적 수집(2026-06-16). 본 파일은 `reference` 레이어 (검수 상태 추적 도구이지 도메인 단언 아님).

## 검수 티어 (검수 단위 정의)

코드 12,500+ 파일을 의미있는 단위로 만들기 위한 3티어:

| 티어 | 의미 | 검수 의무 |
|---|---|---|
| **C (Core)** | 모델 고유 물리·수치 커널 | **필수** — source-analysis 노트 |
| **S (Support)** | prep·IO·util·parallel·build·coupling glue | 권장 |
| **T (Third-party/Vendored/Coupled)** | 외부 라이브러리(eigen·boost·petsc·netcdf·gdal·ARPACK/BLAS/LAPACK 등)·결합된 외부모델(WRF) | **면제 (N/A)** — 라이선스/출처만 기록, 코드 검수 제외 |

## 상태 범례

- ✅ **done** — 해당 단위가 ≥1 source-analysis/manual 노트로 실질 커버
- 🟡 **partial** — 일부 노트 존재하나 큰 미검수 영역 잔존
- ⬜ **todo** — 노트 없음
- ⬛ **N/A** — T티어 (검수 면제)

---

## 0. 요약 대시보드 (2026-06-16 기준)

| 모델 | 코어 소스파일 | 코어 검수 | 문서(PDF) | manual-notes | 우선순위 |
|---|--:|:--:|--:|--:|:--:|
| **SWASH** | 160 | ✅ 19 노트 (전수) | 2 | ✅ 2 | ✅ 완료 |
| **Delft3D** | engines_gpl 3,503 (+utils) | ✅ 39 노트 (엔진+utils S) | 53 | ✅ 9 (매뉴얼+도구) | ✅ 완료 |
| **ROMS** | roms/ROMS ~900 | ✅ 33 노트 (4D-Var) | 10 | ✅ 4 (+Exercise 카탈로그) | ✅ 완료 |
| **FUNWAVE** | TVD 38 + GPU 41 | ✅ 10 노트 | 39 | ✅ 3 (+검증 카탈로그) | ✅ 완료 |
| **ADCIRC** | adcirc/src 56 (+gahm·asgs) | ✅ 36 노트 (정화 2026-06-18) | 98 | 21 + web-refs(논문 30) | ✅ 완료 |
| **EFDC** | 264 (+GVC 301 legacy S) | ✅ 30 노트 (+GVC) | 6 | ✅ 7 (+Training/Grid) | ✅ 완료 |
| **XBeach** | 118 | ✅ 32 노트 | 9 | 4 | ✅ 완료 (kingsday=master 동계열) |
| **SWAN** | 77 | ✅ 29 노트 | 9 | 29 | ✅ 완료 |
| **Celeris** | WebGPU JS+CUDA | ✅ 9 노트 | 3 | 1 + web-refs(Lynett 2026) | ✅ 완료 |
| **SFINCS** 🆕 | src 36 (f90) | ✅ 8 노트 (전 코어, 검수) | readthedocs RST | ✅ 2 (numerical·params-io) | ✅ 완료 (코드+문서) |
| **LISFLOOD-FP** 🆕 | classic+swe+cuda (C++/CUDA) | ✅ 7 노트 (전 솔버, 검수) | user manual PDF | ✅ 1 (user-manual) | ✅ 완료 (코드+문서) |
| **CADMAS-SURF** 🆕 | 4 시뮬 ~1255 (f/f90) | ✅ 16 노트 (**코드 100% 포섭**: C티어 12 + S티어/커버리지 4) | 영·일 매뉴얼 19 PDF | ✅ 1 (영문 지배방정식) | ✅ 코드 100% (매뉴얼 18·바이너리3툴 후속) |

> **전수 검수 완료 (2026-06-16~18, workflow 7회 · 66 신규 노트)**: ~~SWASH·Delft3D engines·ROMS 4D-Var·핵심 매뉴얼 10종~~ + ~~polish(Delft3D utils·EFDC-GVC·도구/Training 매뉴얼·ADCIRC 30논문·Celeris·ROMS Exercise·FUNWAVE 검증)~~ ✅. 모든 단언 file:line/page 인용 + 적대 검증 통과(9건 실오류 적발→수정). **신규 모델 2(2026-06-18)**: SFINCS(Deltares compound flooding)·LISFLOOD-FP v8.2(Bristol/Sheffield 침수) — README+architecture+web-refs+manifest 생성, **모듈/솔버 deep source-analysis 는 후속 workflow**(SWASH 패턴). **잔여(선택적)**: Delft3D Library Tables·course PDF, EFDC-GVC 심층, 양호모델 추가 심화, 신규2 모델 deep.

---

## 1. SWASH 🔴 (160 코어파일 / SA 2)

**소스**: `raw/source_code/swash/src/*.ftn90` (160). **문서**: swashtech.pdf, swashuse.pdf.

### 1.1 문서
| PDF | 종류 | 노트 | 상태 |
|---|---|---|---|
| swashtech.pdf | 기술(mimetic 이산화 이론서, 부분완성) | swash-tech-documentation-overview | 🟡 (Ch2/5 deep 잔여, Ch8/9/10/12 원문 미완성) |
| swashuse.pdf | 사용자 | — | ⬜ |

### 1.2 코드 모듈 (C티어, 19 source-analysis 노트 — 2026-06-16 workflow 검수 완료)
> 160파일 → 17 신규 + 2 기존 = **19 노트 전수 커버**. 각 노트 file:line 인용 + 적대 검증 통과(grid-infra 1건 날조인용 수정).

| 모듈 | 노트 | 상태 |
|---|---|---|
| 아키텍처 전반 | swash-architecture-source-map | ✅ |
| 비정수압 압력 projection + 선형 solver | swash-nonhydrostatic-pressure-solver | ✅ |
| 명시적 수심평균 flow (ExpDep 1DH/2DH/U) | swash-explicit-depthavg-flow | ✅ |
| 명시적 다층 flow (ExpLay·ExpLayP) | swash-explicit-layered-flow | ✅ |
| 암시적 수심평균 flow (ImpDep·M) | swash-implicit-depthavg-flow | ✅ |
| 암시적 다층 flow (ImpLay·M·P) | swash-implicit-layered-flow | ✅ |
| scalar transport (염분·온도·tracer) | swash-scalar-transport | ✅ |
| 난류 closure (k-ε·Reynolds·log-law·anti-creep) | swash-turbulence-closure | ✅ |
| 경계조건·파생성·sponge | swash-boundary-wave-forcing | ✅ |
| 스펙트럼 경계파일·transfer fnc | swash-boundary-spectral-transfer | ✅ |
| 바닥마찰·바람응력 | swash-bottom-friction-wind | ✅ |
| 식생·다공성 구조물 | swash-vegetation-porosity | ✅ |
| wetting-drying·runup·수심update | swash-wetting-drying-runup | ✅ |
| 부유체·강체 운동 | swash-floating-rigid-body | ✅ |
| 초기화·격자·밀도·기하 | swash-initialization-grid | ✅ |
| time-stepping driver·field update | swash-timestepping-update-driver | ✅ |
| 입력파싱·prep 검사 | swash-input-parsing-check | ✅ |
| 출력(quantity·VTK·backup) | swash-output | ✅ |
| SWAN공유 격자·OceanPack 인프라 (S) | swash-grid-oceanpack-infra | ✅ |

---

## 2. Delft3D 🔴 (engines_gpl 3,503 / SA 21)

**소스**: `src/` 7,240파일 중 **third_party_open 2,633 = ⬛ N/A** (eigen 532·boost 338·petsc 296·proj 292·netcdf 185·expat 169·gdal 153·spherepack 118·metis 115...).

### 2.1 문서 (53 PDF — 핵심 매뉴얼 ✅, 도구·교육 잔여)
| PDF | 종류 | 노트 | 상태 |
|---|---|---|---|
| Delft3D-FLOW_User_Manual (757p) | FLOW 사용자 | delft3d-flow-user-manual(TOC/MDF) + **delft3d-flow-physics-numerics**(물리·수치 심화) | ✅ |
| Delft3D-WAVE_User_Manual (208p) | WAVE(SWAN) | **delft3d-wave-user-manual** | ✅ |
| Delft3D-WAQ_User_Manual (391p) | 수질 사용자 | **delft3d-waq-user-manual** | ✅ |
| WAQ_Processes_Technical_Reference (611p) | 수질 process 식 | **delft3d-waq-processes-tech-reference** | ✅ |
| Delft3D-PART_User_Manual (138p) | 입자추적 | **delft3d-part-user-manual** | ✅ |
| Delft3D-TIDE_User_Manual (103p) | 조석분석 | **delft3d-tide-user-manual** | ✅ |
| WAQ Library Tables(336p)·Input Desc(105p) | 수질 reference 표 | (tech-ref 노트서 언급) | 🟡 |
| GPP/QUICKPLOT/RGFGRID/QUICKIN/TRIANA/WES/DIDO/NEFIS | 전·후처리 도구 | delft3d-manuals-overview(인덱스) | 🟡 (S, 도구) |
| Conceptual/Functional Spec·course PDF·cxx-*·doxygen | 개념·교육·T | — | ⬜/⬛ |

### 2.2 코드 모듈 (engines_gpl 중심) — 2026-06-16 workflow 17 신규 노트 (총 38 SA)
> engines 전 엔진 검수 완료. 각 노트 file:line 인용 + 적대 검증 통과(special_physics 1건 radstr Sxy cos·sin 누락 적발→수정).

| 모듈 | 파일 | 티어 | 노트 | 상태 |
|---|--:|:--:|---|:--:|
| flow2d3d | 794 | C | dispatcher·adi_solver·drying·heat·turbulence·sigma_z·compute_aux·sediment + **io·inichk_general·special_physics(nearfar/roller/nonhydro)** | ✅ |
| dflowfm | 1,515 | C | kernel_scheme·mdu·overview·compute_aux + **compute_core·prepost·transport_sediment·waves·data_io·grid_utils** | ✅ (gui 342 S-tier 미검수) |
| waq (수질) | 527 | C | delwaq + **process_library·algae_models(BLOOM/protist)·kernel_integration·io_preprocess** | ✅ |
| fbc | 253 | C | **fbc_flow_boundary** (xerces ⬛T 제외) | ✅ |
| part (입자) | 119 | C | part | ✅ |
| rr (강우유출) | 111 | C | **rr_rainfall_runoff** | ✅ |
| wave (SWAN wrapper) | 81 | C | flow_wave_coupling + **wave_swan_module** | ✅ |
| rtc (실시간제어) | 56 | S | **rtc_realtime_control** | ✅ |
| dsle/dimr/d_hydro | 47 | S | dimr_coupling·engines_overview | 🟡 |
| utils_gpl | 766 | S | — | ⬜ |
| utils_lgpl | 491 | S | — | ⬜ |
| tools_gpl | 251 | S | dredge_dump·dd | 🟡 |
| third_party_open | 2,633 | T | — | ⬛ |

---

## 3. ROMS 🟠 (roms/ROMS ~900 / SA 22)

**소스**: WRF(~700, ⬛ 결합 대기모델 N/A)·roms_libs/ARPACK+BLAS+LAPACK(~360, ⬛ N/A) 제외 후 ROMS 코어.

### 3.1 문서 (10 PDF)
| PDF | 종류 | 노트 | 상태 |
|---|---|---|---|
| Exercise_1~9.pdf | 실습 튜토리얼 | — | ⬜ (examples 후보) |
| tidal_ellipse.pdf | 조석타원 분석 | roms_tidal_forcing(부분) | 🟡 |

### 3.2 코드 모듈 (roms/ROMS) — 2026-06-16 workflow 11 신규 노트 (총 33 SA)
> 4D-Var suite(Tangent·Representer·Adjoint) + Drivers·Functionals·Modules·Include·Utility 검수 완료. 적대 검증 통과(global_state g 가드 SOLITON 오기 + utility shapiro ξ/η 방향 뒤바뀜 2건 적발→수정).

| 모듈 | 파일 | 티어 | 노트 | 상태 |
|---|--:|:--:|---|:--:|
| Nonlinear (코어) | 246 | C | baroclinic_3d·barotropic_2d·advection·h/v_mixing·bbl·nonlinear_physics + **core_remaining(prsgrd·rho_eos·omega·diag)** | ✅ |
| Nonlinear/Vegetation | 10 | C | **nonlinear_vegetation** | ✅ |
| Adjoint (ADM) | 85 | C | adjoint_framework + **adjoint_model** | ✅ |
| Tangent (TLM) | 74 | C | **tangent_linear_model** | ✅ |
| Representer (RPM) | 59 | C | **representer_model** | ✅ |
| 4D-Var driver | 44 | C | 4dvar + main_driver_dispatch + **4dvar_drivers(i4dvar/rbl4dvar/r4dvar/fsv/adsen...)** | ✅ |
| Functionals (ana_*) | 43 | C | **analytical_functionals** | ✅ |
| Modules (mod_*) | 38 | C | support_modules + **global_state_modules** | ✅ |
| Include (cppdefs) | 40 | S | **include_cppdefs** | ✅ |
| Utility | 196 | S | grid_metrics·open_boundaries·tidal·atmospheric·bulk_flux·nesting·stability_gst + **io_netcdf(def/wrt/get/nf)·utility_numerics(vorticity/shapiro/scoord...)** | ✅ |
| Sediment/biology/ice/wec | — | C | sediment·biology·sea_ice·wec | ✅ |
| WRF (결합 대기모델) | ~700 | T | — | ⬛ |
| ARPACK/BLAS/LAPACK | ~360 | T | — | ⬛ |

---

## 4. FUNWAVE 🟠 (TVD 38 + GPU 41 / SA 9)

### 4.1 문서 (39 PDF — 대부분 validation 출력 caseA/B/C·sph_sol 등 → examples 티어)
| PDF | 종류 | 노트 | 상태 |
|---|---|---|---|
| funwave_tvd_2.1_manual / funwave_tvd_3.0 | 사용자 매뉴얼 | — | ⬜ |
| Intro-to-FUNWAVE-CHL-TN | 기술노트 | — | ⬜ |
| funwave_code_analysis | 코드분석 | funwave-code-graph(자체) | 🟡 |
| caseA/B/C·comp_beach·sph_sol·monai 등 ~33 | 검증 출력 | — | ⬜ (examples) |

### 4.2 코드 모듈
| 모듈 | 파일 | 티어 | 노트 | 상태 |
|---|--:|:--:|---|:--:|
| FUNWAVE-TVD/src | 38 | C | dispersion-solver·flux-tvd·physics-sources·feature-modules·infrastructure·source-map·code-graph | ✅ |
| FUNWAVE-GPU/src | 41 | C | gpu-source + **gpu-cuda-port(kernel launch·MGPU halo exchange·cuSPARSE v2)** | ✅ |

---

## 5. ADCIRC 🟢 (adcirc/src 56 +gahm +asgs / SA 60)

### 5.1 문서 (98 PDF)
| 분류 | 개수 | 노트 | 상태 |
|---|--:|---|:--:|
| 매뉴얼류 (DevGuide·theory_2004·ASGSInterfaceGuide·AdcircLite·Paraview) | ~6 | manual-notes 21 | ✅ |
| 논문 (1991~2008 Luettich·Westerink·Blain·Dietrich 등) | ~30 | foundational 후보 (web-refs 1) | 🟡 (web-refs 격상 여지) |
| UGM 발표·agenda·abstract | ~20 | — | ⬜ (대부분 N/A) |
| 기타(ice·jpeg2000·bathy·mesh png변환) | 나머지 | — | ⬜ |

### 5.2 코드 모듈
| 모듈 | 파일 | 티어 | 노트 | 상태 |
|---|--:|:--:|---|:--:|
| adcirc/src | 56 | C | gwce·momentum·timestep·wetdry·boundary·met-forcing·tidal·hotstart·3d-mode·baroclinic·dg-continuity·weir·output | ✅ |
| adcirc/prep | 18 | S | preprocessing-foundation·parallel | ✅ |
| adcirc/wind·util | 19 | S | (met-forcing·utilities 부분) | 🟡 |
| gahm/src (GAHM 비대칭 Holland wind) | ~40 | C | **adcirc_gahm_vortex_model**(GahmSolver·radius solver·ATCF isotach·OWI 출력·Vortex 마찰/translation) | ✅ |
| asgs (자동운영) | ~599 | S | output-writers + **adcirc_asgs_operational_system**(구조·tide_fac·aswip·asgs_main.sh·FigureGen) | ✅ (S요약) |

---

## 6. EFDC 🟢 (264 / SA 29) — 양호

**소스**: EFDC-GVC(301, 구버전)·EFDCPlus_Stable/EFDC(48 코어). 코어+서브시스템(hydro·transport·turbulence·sediment·sedzlj·propwash·waves·ice·toxics·water_quality·mpi·linkages·drifters·vertical·external_mode·hydraulic_structures) 전반 ✅. 문서 6 PDF 중 Theory/Manual/Implementation = manual-notes 5.
잔여: EFDC-GVC(301 구버전) 별도 검수 여부 판단 필요, GOTM_Turbulence(32, ⬛ 외부 GOTM 결합 T후보).

---

## 7. XBeach 🟢 (118 / SA 32) — 양호

xbeachlibrary(66) 코어 광범위 커버(flow_solver·morphology·nonh·q3d·wave_*·boundary·avalanching·groundwater·vegetation·ship_waves·bed_friction·single_dir·infrastructure·output 등). 문서 9 PDF 중 manual_master/kingsday·usersguide·non-hydrostatic_report·Parallellization_report. 잔여: manual-notes 3 → 매뉴얼 PDF 전수화 여지.

---

## 8. Celeris 🟢 (WebGPU JS+CUDA / SA 9) — 양호

Celeris-WebGPU(JS + .wgsl/.cu compute shader). boussinesq-solver·breaking·fv-reconstruction·render·sediment·webgpu-infra·coulwave·pipeline-graph·source-map 커버. 문서 3 PDF(Tavakkol 2017/2020·Lynett 2026) = web-refs 2. 코어 솔버 ✅.

---

## 10. CADMAS-SURF 🆕 (신규 모델 2026-06-23, SURF-3D 240 / SA 5)

**소스**: CDIT/PARI 공식 GitHub org `CADMAS-SURF` 의 `Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami` clone (`raw/source_code/`, HEAD `da7668f` 2024-08-30). 멀티스케일·멀티피직스 통합: `STOC-ML/IC`(광역, PARI 별도) → **`CADMAS-SURF/3D`**(단상 VOF NS, 240 Fortran) → `CADMAS-2F`(기액 2상) → `STR3D`(FEM 구조) → `AGENT`(피난). 총 1263 Fortran + 매뉴얼 19 PDF.

### 10.1 문서 (영·일 매뉴얼 19 PDF)
| PDF | 종류 | 노트 | 상태 |
|---|---|---|---|
| CADMAS-SURF3D_Manural_English.pdf (150p) | SURF/3D 영문 매뉴얼 | **cadmas-surf3d-english-manual-governing-equations** (Table 0-1-1 + §2 지배방정식, 소스 cross-confirm) | ✅ |
| CADMAS-SURF3D_Manual_Japanese.pdf | SURF/3D 일문 | — | ⬜ |
| STOC-CADMAS_Manual_Japanese.pdf | STOC 결합 일문 | — | ⬜ |
| CADMAS-2F_Manural_English/Japanese.pdf | 2상 매뉴얼 | — | ⬜ |
| CADMAS-STR/AGENT_Manual_*.pdf | STR3D·AGENT | — | ⬜ |

### 10.2 코드 — CADMAS-SURF/3D (C티어, 240 Fortran, SA 5 — 2026-06-23 검수)
> 메인 드라이버 + 핵심 물리 커널 전수. 각 노트 file:line 인용 + 영문 매뉴얼 식 cross-confirm (가상질량 2.5·저항 R·VOF 2.7·Sommerfeld 2.16·k-ε 상수 모두 일치).

| 서브시스템 | 노트 | 상태 |
|---|---|---|
| 아키텍처(SMAC+VOF 루프·명명규칙·데이터모델) | cadmas-surf3d-architecture-source-map | ✅ |
| SMAC 流速-압력(예측자·Poisson·MILU-BiCGSTAB·보정) | cadmas-surf3d-smac-velocity-pressure-solver | ✅ |
| VOF 자유수면(donor-acceptor·NF 머신·기포/물방울) | cadmas-surf3d-vof-free-surface | ✅ |
| k-ε 난류·porous Morison drag·파력적분 | cadmas-surf3d-turbulence-and-porous-resistance | ✅ |
| 조파(소스/파이론)·방사경계·대수칙벽 | cadmas-surf3d-wave-generation-and-boundaries | ✅ |
| 시간刻み(CFL)·親子 격자 nesting·STOC 결합(MPMD) | cadmas-surf3d-timestep-nesting-stoc-coupling | ✅ |

### 10.3 코드 — CADMAS-2F (3D2F, 388 Fortran, C티어 SA 2 — 2026-06-23)
> 단상 SURF/3D 의 `vf_*` 인프라 공유 + 신규 2축. 단상 대비 신규분만 문서화.

| 서브시스템 | 노트 | 상태 |
|---|---|---|
| 기액 압축성 2상(EOS·변밀도 one-fluid VOF·준압축성 Poisson·Picard 루프) | cadmas-2f-twophase-compressible-gas | ✅ |
| 유체-구조 결합(sf_* cut-cell 공극엔진·이동구조 FSI·가동상) | cadmas-2f-structure-coupling-cutcell | ✅ |

### 10.4 코드 — STR3D (587 Fortran, C티어 SA 3 — 2026-06-23)
> FEM 구조·지반 solver. src/(157)·contact/(108)·module/·femap/ = C티어, seq/mpi_comm/glb_comm/util = S티어(병렬통신).

| 서브시스템 | 노트 | 상태 |
|---|---|---|
| FEM 코어(Newmark-β·요소·탄소성 von Mises/Drucker-Prager+균열·Biot 지반) | str3d-fem-core-newmark-elasto-plastic | ✅ |
| 선형 solver(ICCG/BiCGStab 반복·PARDISO/MUMPS 직접·CRS) | str3d-linear-solvers | ✅ |
| 접촉역학(MPC node-to-surface·Coulomb 마찰)·CADMAS 유체결합(MPMD) | str3d-contact-and-fluid-coupling | ✅ |
> ⬛ T티어: MUMPS 4.10(`module/dmumps_*.h`, 공개 vendored)·Intel PARDISO(MKL) — 라이선스/출처만, 내부 미분석.

### 10.5 코드 — AGENT (40 Fortran, 전수 SA 1 — 2026-06-23)
| 서브시스템 | 노트 | 상태 |
|---|---|---|
| 피난 시뮬(potential-field Dijkstra 항법·Tobler hiking·수심 익사판정·CADMAS 결합·확률) | cadmas-agent-evacuation-simulator | ✅ (40 .f90 전수) |

### 10.6 S티어 + 커버리지 (코드 100% 포섭, SA 4 — 2026-06-24)
> C티어 코어 12노트 외 전 파일 카탈로그 + 적발 보조물리.

| 범위 | 노트 | 적발 보조물리 |
|---|---|---|
| SURF/3D S티어+보조 | cadmas-surf3d-stier-and-auxiliary-physics | ★Okada 단층 쓰나미소스(mod_fault)·스칼라/온도 수송·공기압·파이론 내부(Stokes5/cnoidal3/stream-func)·진단(vort/div/wlvl) |
| STR3D S티어+geo | str3d-stier-parallel-mesh-io | geo/(31)=FEM 코어 MPI 병렬쌍둥이·remesh 이동메시·dflt_damp Rayleigh·METIS 분할·FEMAP 출력 |
| 2F S티어+HiDEM | cadmas-2f-stier-and-hidem-dem-coupling | ★HiDEM(DEM) 결합(vf_jp*/mod_dem)=4번째 파트너·2상물리=EOS집합 전수확인 |
| Pre/post 4툴 | cadmas-pre-post-processors | ViewKai 소스(GFCONV)·MESH/MESH-MULTI/VR 바이너리(source-needed) |

**최종 잔여(후속)**: **매뉴얼 18종**(일문 SURF/3D·STOC-CADMAS·2F 영/일·STR 영/일·Program Instructions×4·AGENT 영/일·튜토리얼) / **Pre/post 3툴 바이너리 내부**(MESH·MESH-MULTI·VR — 소스부재, 매뉴얼 PDF 출처 필요). 코드(Fortran) = **100% 포섭 완료**. 라이선스 = repo LICENSE 부재(인용의무만, source-needed). disclosed gap: SURF/3D CFL=이류+확산만(√gH 無), STOC=MPI_COMM_SPLIT MPMD, 2F=표면장력·상변화 無, AGENT underwater_function dead-code, HiDEM 본체 repo 부재(인터페이스만).

---

## 9. 검수 진행 규약

1. 한 단위(모듈/문서) 검수 완료 시 → source-analysis(또는 manual-notes) 노트 작성 + **본 원장 상태 갱신** (⬜→🟡/✅).
2. T티어는 코드 검수 제외, 라이선스·버전·출처만 모델 README 에 기록.
3. 우선순위는 §0 대시보드 따름: SWASH → Delft3D(waq·dflowfm·fbc/rr/rtc) → ROMS(adjoint suite·Utility) → FUNWAVE → ADCIRC(gahm·asgs) → 매뉴얼 전수화.
4. 검수 깊이는 산출물 규모에 비례 (santa-method) — 커널 서브루틴은 deep, util/IO 는 요약 가능.
5. 본 원장은 [INDEX.md](../INDEX.md) 에서 진입.
