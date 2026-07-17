---
title: "모델 전수 검수 원장 (AUDIT LEDGER) — 12개 모델 문서·소스코드 커버리지 추적 (전 모델 종결 2026-07-12)"
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

## 0. 요약 대시보드 (2026-06-16 기준; 카운트 실측 = `bash tools/count-notes.sh --check`)

> **종결 = snapshot 판정 (freshness 규약, 2026-07-12 Codex F-7)**: 각 모델의 "종결"은 검수 당시 소스 snapshot(각 모델 manifest 의 clone sha/버전)에 대한 판정이며 **최신 upstream 에 대한 영구 보증이 아니다**. 실제 프로젝트에서 해당 모델을 사용하기 **직전에** upstream delta(신규 릴리스·검수 sha 와의 차이)를 확인하고, 유의미한 변경이 있으면 해당 모듈만 재검수한다. 상시 upstream 추적은 하지 않음(자동수집 중단 정책과 정합). 기록 위치: 각 모델 섹션에 `audited_ref`(검수 sha/버전)·`latest_release_checked`·`checked_at` 을 사용 시점에 추가.

| 모델 | 코어 소스파일 | 코어 검수 | 문서(PDF) | manual-notes | 우선순위 |
|---|--:|:--:|--:|--:|:--:|
| **SWASH** | 160 | ✅ 21 노트 (전수 + linear/unstructured-solvers 2026-07-04 + **핀포인트 4갭 소스직독 해소 2026-07-12**) | 2 | ✅ 3 | ✅ **종결(코드+문서축, 2026-07-17 I-6)** — swashtech Ch2/5 deep note 신설로 재검토 해소(§1 참조) |
| **Delft3D** | engines_gpl 3,503 (+utils) | ✅ 48 노트 (엔진 C + utils S, 실측 2026-07-12) | 53 | ✅ 11 (매뉴얼+도구) | ✅ **종결**(2026-07-12; FM θ 0.55·ADI CFL 경고체계·z_turclo 동형 3갭 해소, §2 판정) |
| **ROMS** | roms/ROMS ~900 | ✅ 37 노트 (4D-Var suite + 2026-07 심화, 실측) | 10 | ✅ 4 (+Exercise 카탈로그) | ✅ **종결**(2026-07-12; flag 0건 판정, §3) |
| **FUNWAVE** | TVD 38 + GPU 41 | ✅ 11 노트 (wk-data2d·build-blackwell 포함 실측) | 39 | ✅ 3 (+검증 카탈로그) | ✅ **종결**(2026-07-12; ★Cd 기본 0.0 마찰 off 갭 해소) |
| **ADCIRC** | adcirc/src 56 (+gahm·asgs) | ✅ 38 노트 (정화 2026-06-18 + VSSOL 2026-07-11 + **NFFR flux 경계 2026-07-12 사용자 지목 보강**) | 98 | 21 + web-refs(논문 30) | ✅ **종결**(2026-07-11; 종결 후 보강 허용) |
| **EFDC** | 264 (+GVC 301 legacy S) | ✅ 38 노트 (+GVC legacy·**CALUVW 전단솔버 2026-07-11 = 마지막 코어 갭**) | 6 | ✅ 9 (+Training/Grid·Ch5/Ch6 cross-walk) | ✅ **종결**(2026-07-11; GVC 불요·GOTM T티어 판정) |
| **XBeach** | 118 | ✅ 33 노트 (intrawave 2026-07-07 포함 실측) | 9 | ✅ 4 | ✅ **종결**(2026-07-12; eps·wetz 산정식 갭 해소) |
| **SWAN** | 77 | ✅ 30 노트 (58파일 커버리지 감사 + swancom1 crosswalk + **swanmain 후반 source-map 2026-07-17**) | 9 | 29 | ✅ **종결(코드+문서축, 2026-07-17 I-6)** — swanmain 반박 수용·C 재분류·foundation 정정으로 재검토 해소(§11 참조) |
| **Celeris** | WebGPU JS+CUDA | ✅ 9 노트 | 3 | 1 + web-refs(Lynett 2026) | ✅ **종결**(2026-07-12; breaking 계수·FrictionCalc·dt 정적 3갭 해소) |
| **SFINCS** 🆕 | src 36 (f90) | ✅ 9 노트 (전 코어 + infiltration 2026-07-07) | readthedocs + **v2.4.0 릴리스** | ✅ 5 (numerical·params-io·model-building·testbed 77케이스·changelog) | ✅ **종결**(2026-07-12; flag 0건, §12 판정) |
| **LISFLOOD-FP** 🆕 | classic+swe+cuda (C++/CUDA) | ✅ 8 노트 (전 솔버 + mwdg2-adaptive 2026-07-07) | user manual PDF | ✅ 1 (user-manual) | ✅ **종결**(2026-07-12; tol_h 1e-3 하드코딩 갭 해소, §13 판정) |
| **CADMAS-SURF** 🆕 | 4 시뮬 ~1255 (f/f90) | ✅ 17 노트 (**코드 100% 포섭**: C티어 13(entrapped-air 포함) + S티어/커버리지 4) | **26 PDF 전수** | ✅ 5 (SURF3D·2F·STR·AGENT 영문 cross-confirm + 카탈로그) | ✅ **종결**(2026-07-12; 잔여=일문매뉴얼 중복·바이너리 3툴 내부·LICENSE 부재 — 전부 disclosed 비코어 판정) |
| **ShorelineS** 🆕 | functions 136 (.m) | 🟡 4 노트 (architecture-map + transport 7공식 + coastline_change + 파랑/사구/스핏 — 코어 물리 1차 완료) | 3 PDF (repo doc/ 동봉) | ✅ 1 (Roelvink 2020 Frontiers 발췌·코드 대조) | 🟡 **신설+코어 1차 2026-07-17**(§14 — 잔여: 회절 기하·mud 본문·위상 처리 deep) |

> **전수 검수 완료 (2026-06-16~18, workflow 7회 · 66 신규 노트)**: ~~SWASH·Delft3D engines·ROMS 4D-Var·핵심 매뉴얼 10종~~ + ~~polish(Delft3D utils·EFDC-GVC·도구/Training 매뉴얼·ADCIRC 30논문·Celeris·ROMS Exercise·FUNWAVE 검증)~~ ✅. 모든 단언 file:line/page 인용 + 적대 검증 통과(9건 실오류 적발→수정). **신규 모델 2(2026-06-18)**: SFINCS(Deltares compound flooding)·LISFLOOD-FP v8.2(Bristol/Sheffield 침수) — README+architecture+web-refs+manifest 생성, **모듈/솔버 deep source-analysis 는 후속 workflow**(SWASH 패턴). **잔여(선택적)**: Delft3D Library Tables·course PDF, ~~EFDC-GVC 심층~~(**불요 판정 2026-07-04** — DSI 공식 비권장·무지원 + repo 동결 2021-11 sha 68dc93f + mainline 12.4 SGZ 가 후속 통합 구현 + [efdc_gvc_legacy](EFDC/source-analysis/efdc_gvc_legacy.md) verified 로 계보·구조·SGZ 대조 기커버. EFDC+ 버전 provenance 확정: **12.4**, aaefdc.f90:22, sha 3ed76b6 — manifest 참조), ~~신규2 모델 deep~~(SFINCS·LISFLOOD-FP 완료 2026-06 확인), 양호모델 추가 심화.

---

## 1. SWASH 🟢 **종결 2026-07-12** (160 코어파일 / SA 21 — 구 "SA 2" 헤더는 초기 stale)

**소스**: `raw/source_code/swash/src/*.ftn90` (160). **문서**: swashtech.pdf, swashuse.pdf.

> **종결 판정(2026-07-12)**: 코드 160파일 = 19노트 전수(2026-06-16) + linear-solvers·unstructured-solvers 심화 2편(2026-07-04) = **SA 21**. cross-model 대조가 flag 한 마지막 핀포인트 갭 4건을 소스 직독으로 당일 해소 — ①`iturb==2`=full 3D k-ε 선형(`VISC FULL KEPS LIN`, SwashReadInput.ftn90:1252-1276) ②θ 기본값(THETAC/S/U/W=0.5, NONHYD θ=-1 sentinel→CheckPrep 1.0 완전implicit) ③`FRIC` 카드 기본 MANNing n=0.019·생략 시 off ④breaking β=-1 sentinel→0.3(BDF 시 0.15) 자동선택(SwashCheckPrep.ftn90:1065-1090). ~~잔여 swashtech Ch2/5 deep 은 원문 미완성 문서라 비코어 판정~~
>
> **✅재검토 종결(2026-07-17, I-6)**: 재판정 결과 Codex 지적이 옳았음 — Ch2·Ch5 §5.7 은 코어 이론(Hamiltonian 구조·mimetic 연산자·질량/운동량/에너지 보존 증명 = 스킴 설계 원리의 근거)이라 '비코어' 판정 철회. **deep note 신설**: [swash-tech-ch2-ch5-mimetic-conservation](SWASH/manual-notes/swash-tech-ch2-ch5-mimetic-conservation.md) (페이지·식번호 실측: Eq.2.8 div=-gradᵀ 축·전역 보존 3조건 p.53·삼각격자 로컬 보존 4요건 p.82-83·반이산 한계 disclosed). 문서 상태 실측 갱신: placeholder 는 Ch8/9/10/12 에 **Ch4 추가**, Ch1 §1.1·Ch6(`??` 참조) 부분 미완. 문서축 종결.

### 1.1 문서
| PDF | 종류 | 노트 | 상태 |
|---|---|---|---|
| swashtech.pdf | 기술(mimetic 이산화 이론서, 부분완성) | swash-tech-documentation-overview + **swash-tech-ch2-ch5-mimetic-conservation (deep, 2026-07-17)** | ✅ (Ch2/5 deep 완료; 원문 placeholder = Ch4·8·9·10·12, 부분 미완 = Ch1§1.1·Ch6 — disclosed) |
| swashuse.pdf | 사용자 | swash-user-manual | ✅ |

### 1.2 코드 모듈 (C티어, 21 source-analysis 노트 — 2026-06-16 전수 + 2026-07-04 심화 2편)
> 160파일 → 17 신규 + 2 기존 = 19 노트 전수 커버(2026-06-16), 이후 solver 심화 2편 추가 = **21**. 각 노트 file:line 인용 + 적대 검증 통과(grid-infra 1건 날조인용 수정).

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
| 선형 solver 심화 (PCG/SIP/BiCGSTAB/tridiag/ILU, 2026-07-04) | swash-linear-solvers | ✅ |
| 비정형 격자 솔버 + Perot 재구성 (SwashUServ, 2026-07-04) | swash-unstructured-solvers | ✅ |

---

## 2. Delft3D 🟢 **종결 2026-07-12** (engines_gpl 3,503 / SA 48 + MN 11 — 구 "SA 21" 헤더 stale)

> **종결 판정(2026-07-12)**: 전 엔진 C티어 검수(2026-06-16 workflow)+WAQ 4편·morphology·difu 계열 후속 심화 = **SA 48 실측**. cross-model flag 마지막 3건 소스직독 해소 — ①FM `Teta0` 기본 **0.55**(m_flowparameters.f90:851, '0.5<θ<1') ②ADI advection explicit 정량 CFL = `chkadv.f90` 반스텝 Courant 점검(>1 시 G051 경고+권장 dt, 하드스톱 아님 — Stelling 1984 정의) ③Z-model `z_turclo/z_tratur` = σ판과 동일 closure·동일 Ri-감쇠 상수(z_turclo.f90:398-399 = turclo.f90:350-359) 대조 확인, 전용 노트 불요. 잔여 S/⬜ 는 아래 표 판정 — 도구 GUI·utils 는 S요약([delft3d_utils_libraries](Delft3D/source-analysis/delft3d_utils_libraries.md))·비코어, doxygen ⬛.

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
| WAQ Library Tables(336p)·Input Desc(105p) | 수질 reference 표 | **delft3d-waq-library-tables-input-funcspec** (index+대표엔트리, 2026-07-04) | ✅ |
| GPP/QUICKPLOT/RGFGRID/QUICKIN/TRIANA/WES/DIDO/NEFIS | 전·후처리 도구 | delft3d-manuals-overview(인덱스) | 🟡 (S, 도구) |
| Conceptual/Functional Spec·course PDF·cxx-*·doxygen | 개념·교육·T | **delft3d-waq-library-tables-input-funcspec** §3 (Functional Description 6모듈 + course 4종 index, 식無 종결) / cxx-*·doxygen ⬛ 자동생성 | ✅(Func/course)/⬛(doxygen) |

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
| dsle/dimr/d_hydro | 47 | S | dimr_coupling·engines_overview — S요약 충분 판정(2026-07-12: 결합 오케스트레이션, 물리 커널 아님) | ✅ (S요약) |
| utils_gpl | 766 | S | **delft3d_utils_libraries**(S-tier 개요) | ✅ (S요약) |
| utils_lgpl | 491 | S | **delft3d_utils_libraries**(S-tier 개요) | ✅ (S요약) |
| tools_gpl | 251 | S | dredge_dump·dd — S요약 충분 판정(2026-07-12: 전·후처리 도구) | ✅ (S요약) |
| third_party_open | 2,633 | T | — | ⬛ |

---

## 3. ROMS 🟢 **종결 2026-07-12** (roms/ROMS ~900 / SA 37 + MN 4 — 구 "SA 22" 헤더 stale)

**소스**: WRF(~700, ⬛ 결합 대기모델 N/A)·roms_libs/ARPACK+BLAS+LAPACK(~360, ⬛ N/A) 제외 후 ROMS 코어.

> **종결 판정(2026-07-12)**: cross-model 대조노트(시간적분·저면마찰·연직혼합·침수노출) flag **0건** — nonlinear 코어·4D-Var suite(TLM/ADM/RPM)·GST·sea-ice·BBL·biology·KPP·EOS·wetdry·tracer timestep 전부 verified 소급(SFINCS 와 같은 판정-종결형). SA 37 실측(step3d_t·kpp·eos·wetdry 등 2026-07 후속 심화 포함). 문서 잔여는 비코어 — Exercise 는 카탈로그([roms-exercises-catalog](ROMS/manual-notes/roms-exercises-catalog.md)) 기커버(examples 티어), tidal_ellipse.pdf 는 분석 유틸 문서(roms_tidal_forcing 부분 커버로 충분 판정).

### 3.1 문서 (10 PDF)
| PDF | 종류 | 노트 | 상태 |
|---|---|---|---|
| Exercise_1~9.pdf | 실습 튜토리얼 | **roms-exercises-catalog**(카탈로그) | ✅ (examples 티어) |
| tidal_ellipse.pdf | 조석타원 분석 | roms_tidal_forcing(부분) — 충분 판정(2026-07-12: 분석 유틸 문서, 코어 아님) | ✅ |

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

## 4. FUNWAVE 🟢 **종결 2026-07-12** (TVD 38 + GPU 41 / SA 11 — 구 "SA 9" 헤더 stale)

> **종결 판정(2026-07-12)**: 코드 TVD 38+GPU 41 = C티어 전수(SA 11: TVD 9 + GPU 2). cross-model flag 마지막 갭 해소 — ★**`Cd` 기본값 = 0.0(마찰 완전 off)**, io.F:2777-2783 미지정 시 0.0+경고, init.F:887 배포([[bottom-friction-cross-model]] §5 함정 계열, physics-sources 노트 반영). 문서 잔여는 전부 비코어 — 매뉴얼 2종·검증 케이스는 MN 3(tvd-manual·user-manual-full·validation-cases 카탈로그)이 커버, ~33 PDF 는 validation 출력물(examples 티어), Intro-CHL-TN 은 user-manual 과 중복 개요.

### 4.1 문서 (39 PDF — 대부분 validation 출력 caseA/B/C·sph_sol 등 → examples 티어)
| PDF | 종류 | 노트 | 상태 |
|---|---|---|---|
| funwave_tvd_2.1_manual / funwave_tvd_3.0 | 사용자 매뉴얼 | funwave-tvd-manual·funwave-user-manual-full | ✅ |
| Intro-to-FUNWAVE-CHL-TN | 기술노트 | — (user-manual 중복 개요 — 비코어 판정 2026-07-12) | ⬜ |
| funwave_code_analysis | 코드분석 | funwave-code-graph(자체) | 🟡 |
| caseA/B/C·comp_beach·sph_sol·monai 등 ~33 | 검증 출력 | funwave-validation-cases(카탈로그) | ✅ (examples 티어) |

### 4.2 코드 모듈
| 모듈 | 파일 | 티어 | 노트 | 상태 |
|---|--:|:--:|---|:--:|
| FUNWAVE-TVD/src | 38 | C | dispersion-solver·flux-tvd·physics-sources·feature-modules·infrastructure·source-map·code-graph·**wk-data2d-spectral-wavemaker(2026-07-07)** | ✅ |
| FUNWAVE-GPU/src | 41 | C | gpu-source + **gpu-cuda-port(kernel launch·MGPU halo exchange·cuSPARSE v2)** + build-and-blackwell-port | ✅ |

---

## 문서축 종결 기준 (I-6 명문화, 2026-07-17)

공식 문서(이론·기술 문서)의 각 장은 다음 중 하나가 성립해야 문서축 종결:
- **(a) 포섭**: 장 내용이 manual-notes 로 페이지 인용과 함께 노트화됨.
- **(b) 코드 대체 명시**: 동일 내용을 source-analysis 노트가 file:line 으로 커버함을 **명시 대조**(암묵 추정 금지).
- **(c) 비코어 disclosed**: 운용 절차·타 문서 중복·원문 미완성(placeholder) 등 사유를 명기.

**제약**: ①위키 자체 노트(overview 등)가 "핵심"으로 평가한 장은 (c) 단독 판정 불가 — (a)/(b) 또는 평가 철회(근거 필요). ②source-coverage 의 근거는 file:line 보유 노트만 유효 — 문서 기반 개관 노트는 불가(swan-foundation 사례). ③"driver/유틸 = S요약 충분" 판정은 해당 파일의 서브루틴 인벤토리 실측 후에만(swanmain 사례: 9.3k 줄 중 후반 2.3k 줄이 실질 로직).

## 5. ADCIRC 🟢 **종결 2026-07-11** (adcirc/src 56 +gahm +asgs / SA 38 verified — 구 "SA 60" 은 2026-06-18 정화 전 stale; 종결 후 보강: NFFR flux 경계 2026-07-12)

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
| adcirc/src | 56 | C | gwce·momentum·timestep·wetdry·boundary·met-forcing·tidal·hotstart·3d-mode·**3d-vssol-vertical-scheme(2026-07-11: θ³ Alp1/2/3·복소 tridiag·w adjoint — 마지막 코어 갭)**·baroclinic·dg-continuity·weir·output·**nffr-periodic-flux-boundary(2026-07-12 사용자 지목: fort.15 NFFR 레코드·IBTYPE=32 q=QN−c(η−EN)·QNAM 내향 양 규약 — Codex 표본 재검증 전 항목 일치 확인)** | ✅ |
| adcirc/prep | 18 | S | preprocessing-foundation·parallel | ✅ |
| adcirc/wind·util | 19 | S | met-forcing(포맷별 reader dispatch 커버)·utilities — S티어 요약으로 충분 판정(2026-07-11: 잔여는 포맷 변환 유틸, 물리 커널 아님) | ✅ (S요약) |
| gahm/src (GAHM 비대칭 Holland wind) | ~40 | C | **adcirc_gahm_vortex_model**(GahmSolver·radius solver·ATCF isotach·OWI 출력·Vortex 마찰/translation) | ✅ |
| asgs (자동운영) | ~599 | S | output-writers + **adcirc_asgs_operational_system**(구조·tide_fac·aswip·asgs_main.sh·FigureGen) | ✅ (S요약) |

---

## 6. EFDC 🟢 **종결 2026-07-11** (264 / SA 38 verified — 구 "SA 29" stale)

**소스**: EFDC-GVC(301, 구버전)·EFDCPlus_Stable/EFDC(48 코어). 코어+서브시스템(hydro·transport·turbulence·sediment·sedzlj·propwash·waves·ice·toxics·water_quality·**diagenesis·RPEM·surface_forcing·heat/ice**·mpi·linkages·drifters·vertical·external_mode·hydraulic_structures) 전반 ✅ + **efdc_internal_shear_caluvw(2026-07-11: 전단 완전 implicit tridiag+Sherman-Morrison — 마지막 코어 갭 해소)**. 문서 6 PDF 중 Theory(Ch2·5·6 cross-walk)/Manual/Implementation = manual-notes 9.
잔여 소진: ~~EFDC-GVC 별도 검수~~(**불요 판정 2026-07-04** — DSI 비권장·repo 동결 2021-11·12.4 SGZ 후속·efdc_gvc_legacy 기커버), ~~GOTM_Turbulence(32)~~(**T티어 판정 2026-07-11** — vendored 3rd-party GOTM 라이브러리(gotm.net)=범위 밖, 결합 인터페이스 mod_gotm.f90 은 efdc_internal_shear_caluvw §6 커버).

---

## 7. XBeach 🟢 **종결 2026-07-12** (118 / SA 33 — intrawave-sediment 2026-07-07 포함)

xbeachlibrary(66) 코어 광범위 커버(flow_solver·morphology·nonh·q3d·wave_*·boundary·avalanching·groundwater·vegetation·ship_waves·bed_friction·single_dir·infrastructure·output + intrawave-sediment). 문서 9 PDF 중 manual_master/kingsday·usersguide·non-hydrostatic_report·Parallellization_report — **manual-notes 4**(master-manual·local-stack·DELILAH·Holland ref).

> **종결 판정(2026-07-12)**: cross-model flag 마지막 갭 소스직독 해소 — `eps` 기본 **0.005 m**(params.F90:1398)·wet/dry 마스크 산정식 `compute_wetcells`(wetcells.F90:75-117 — wetz=`hh>eps+numeps`, wetu 는 hu·hum 이중조건, wete 는 파고 δ·H 가산)·형태학 갱신 후 재산정+dry 클램프(morphevolution.F90:3202-3208) — [[xbeach_flow_solver]] §5 반영. 잔여 매뉴얼 PDF 심화는 master-manual 노트(물리 정식화+params reference)가 코어 커버 — 비코어 판정. (kingsday=master 동계열 기판정.)

---

## 8. Celeris 🟢 **종결 2026-07-12** (WebGPU JS+CUDA / SA 9)

Celeris-WebGPU(JS + .wgsl/.cu compute shader). boussinesq-solver·breaking·fv-reconstruction·render·sediment·webgpu-infra·coulwave·pipeline-graph·source-map 커버. 문서 3 PDF(Tavakkol 2017/2020·Lynett 2026) = web-refs 2. 코어 솔버 ✅.

> **종결 판정(2026-07-12)**: cross-model flag 3갭 전부 소스직독 해소 — ①breaking 계수 기본값 dzdt_I 0.50/dzdt_F 0.15/T_star 5.0/δ_b 2.0(constants_load_calc.js:51-54) ②FrictionCalc 식 전개(Pass3_\*.wgsl:67-92 — Manning `g·n²/h^{1/3}` 또는 무차원 f, f≤0.5 클램프, ★h⁴ 단정밀도 스케일링=수심<5% base_depth 마찰 과소 disclosed, ★기본 friction=0.000 off) ③**dt 정적 확정**(constants_load_calc.js:404 `Courant_num 0.15·√(g·base_depth)` 기반 1회 산정, main.js:1614 재계산은 UI 변경 시만 — 기존 `[source-needed]` 미검증 → 소스 확정 전환). 잔여 없음 — CUDA 쌍둥이는 WebGPU 와 동형(coulwave·pipeline-graph 커버).

---

## 10. CADMAS-SURF 🟢 **종결 2026-07-12** (신규 모델 2026-06-23, 4 시뮬 / SA 17)

**소스**: CDIT/PARI 공식 GitHub org `CADMAS-SURF` 의 `Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami` clone (`raw/source_code/`, HEAD `da7668f` 2024-08-30). 멀티스케일·멀티피직스 통합: `STOC-ML/IC`(광역, PARI 별도) → **`CADMAS-SURF/3D`**(단상 VOF NS, 240 Fortran) → `CADMAS-2F`(기액 2상) → `STR3D`(FEM 구조) → `AGENT`(피난). 총 1263 Fortran + 매뉴얼 19 PDF.

### 10.1 문서 (26 PDF 전수 — manual-notes 5)
| PDF | 종류 | 노트 | 상태 |
|---|---|---|---|
| CADMAS-SURF3D_Manural_English (150p) | SURF/3D 영문 | **cadmas-surf3d-english-manual-governing-equations**(Table 0-1-1+§2 지배식) | ✅ |
| CADMAS-2F_Manural_English (160p) | 2상 영문 | **cadmas-2f-manual-compressibility**(기상 압축성 EOS/Poisson cross-confirm; /3D 95%중복+부록) | ✅ |
| CADMAS-STR Manual(18p)+Program Instructions(113p) 영문 | STR3D 영문 | **cadmas-str-manual-fem-theory-input**(Biot·Newmark·von Mises/DP·MPC·NASTRAN; MUMPS 플래그 stale 적발) | ✅ |
| CADMAS-AGENT_Manual_English (30p) | 피난 영문 | **cadmas-agent-manual**(potential-field·익사판정; Tobler 식 소스전용 적발) | ✅ |
| 나머지 21 PDF(튜토리얼6·일문중복5·STOC-CADMAS1·STR(CADMAS)2·Pre/post7) | 카탈로그 | **cadmas-manuals-catalogue**(전수 인벤토리) | ✅(🟡 일문상세·바이너리툴 내부 source-needed) |

### 10.2 코드 — CADMAS-SURF/3D (C티어, 240 Fortran, SA 7 — 2026-06-23 검수 + 심화)
> 메인 드라이버 + 핵심 물리 커널 전수. 각 노트 file:line 인용 + 영문 매뉴얼 식 cross-confirm (가상질량 2.5·저항 R·VOF 2.7·Sommerfeld 2.16·k-ε 상수 모두 일치).

| 서브시스템 | 노트 | 상태 |
|---|---|---|
| 아키텍처(SMAC+VOF 루프·명명규칙·데이터모델) | cadmas-surf3d-architecture-source-map | ✅ |
| SMAC 流速-압력(예측자·Poisson·MILU-BiCGSTAB·보정) | cadmas-surf3d-smac-velocity-pressure-solver | ✅ |
| VOF 자유수면(donor-acceptor·NF 머신·기포/물방울) | cadmas-surf3d-vof-free-surface | ✅ |
| k-ε 난류·porous Morison drag·파력적분 | cadmas-surf3d-turbulence-and-porous-resistance | ✅ |
| 조파(소스/파이론)·방사경계·대수칙벽 | cadmas-surf3d-wave-generation-and-boundaries | ✅ |
| 시간刻み(CFL)·親子 격자 nesting·STOC 결합(MPMD) | cadmas-surf3d-timestep-nesting-stoc-coupling | ✅ |
| 갇힌 공기(entrapped air) 압력 모델 | cadmas-surf3d-entrapped-air-pressure | ✅ |

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

> **종결 판정(2026-07-12)**: 코드 4 시뮬레이터 100% 포섭(C13+S4=SA 17) + 영문 매뉴얼 4종 cross-confirm + 26 PDF 전수 카탈로그. 위 잔여는 전부 **disclosed 비코어** — 일문 매뉴얼 상세는 영문판과 95% 중복(카탈로그 판정), 바이너리 3툴은 소스 부재로 코드 검수 대상 아님, LICENSE 부재는 repo 자체 상태. cross-model 대조노트(time-integration §5 CADMAS celerity 부재 등)가 flag 한 사항도 전부 원노트 disclosed 로 커버 — 추가 코어 갭 없음.

---

## 11. SWAN 🟢 **종결 2026-07-12** (src 77 / SA 29 + MN 29)

> 초기 검수(2026-06-01 이전)가 원장 섹션화 이전에 완료되어 전용 섹션이 없었음 — 종결 판정과 함께 신설.

**커버리지 근거**: [swan-source-coverage-audit](SWAN/source-analysis/swan-source-coverage-audit.md) 가 src 58 source files 전수 인벤토리 + 기존 노트 매핑을 verified 로 보유. 그 §4.1 이 flag 한 **신설 후보 8건 전원 기작성** — surfbeat-iem·bragg-scattering·gse-correction·quasi-coherent·xnl4-exact-quadruplet·unstructured-time-step·grid-readers·vtk-output. legacy 대형 파일 갭도 해소: swancom1(12k줄) 19 서브루틴 crosswalk + SETUPP/SETUP2D 심층(2026-07-04, [swan-setup-solver-swancom1-crosswalk](SWAN/source-analysis/swan-setup-solver-swancom1-crosswalk.md)).

**종결 판정(2026-07-12)**: 잔여 3건 비코어 판정 — 단 **당일 Codex ② 레이어 표본 재검증에서 2건 반박, ⚠재검토 open**:
| 잔여 | 판정 | ⚠재검증(2026-07-12) |
|---|---|---|
| swanmain.ftn(9.3k줄) 정밀 라인매핑 | ~~driver — S요약 충분~~ → **✅해소(2026-07-17 I-6)** | 반박 수용: RBFILE(7469-8086)·RESPEC(8089-8521)·FLFILE(8524-8860)·SWINCO(8864-9156) = **C 티어 재분류**, [swan-main-boundary-init-sourcemap](SWAN/source-analysis/swan-main-boundary-init-sourcemap.md) 신설(전체 18유닛 인벤토리 + 함정 9건: 경계/입력장 무음 동결·RESPEC IERR 미설정·비문서화 FAC 보정·SWINCO 셀1칸 fetch·무풍 시드 등). swan-foundation 은 frontmatter 자기모순 정정(문서 기반 개관 — source-coverage 증거 사용 금지 명시). 6708행 이전·SWCLME = S요약 유지 |
| fftpack51.ftn90(15k줄) | NCAR FFTPACK 5.1 vendor — **T티어** | 유지 |
| mod_xnl4v5.ftn90(9k줄) | ~~외부 라이브러리 T티어 준용~~ | **반박(중간)**: 외부 기원은 맞으나 swancom1:1479 `xnl_init`·swancom4:2835,2978 `XNL_MAIN` 직접 호출 — **선택형 core physics**. 후속: 확인 깊이 기준 결정 후 재분류 |

문서 축: 공식 4 docs(swantech·swanuse·swanimp·swanpgr) 全 deep-verify + MN 29 (INDEX 참조).

---

## 12. SFINCS 🟢 **종결 2026-07-12** (src 36 f90 / SA 9 + MN 5)

> 신규 모델(2026-06-18)로 원장 섹션 없이 대시보드 행만 있었음 — 종결 판정과 함께 신설.

**커버리지**: 코어 8노트(main BMI 루프·flow_solver·subgrid/quadtree·nonhydrostatic/wavemaker·boundaries/forcing·SnapWave·structures·IO/BMI) + infiltration(강우손실 6법, 2026-07-07) = **SA 9**. 문서 = readthedocs rst 실질 전부(MN 5: numerical·params-io·model-building·v2.4.0 testbed 77케이스·changelog).

**종결 판정(2026-07-12)**: cross-model 대조노트(시간적분·저면마찰·침수노출) flag **0건** — 전 셀 소급 기완료(alfa 0.50·huthresh 0.05·Bates 분모 등 anchor 직접 재확인 이력). 잔여는 전부 비코어 — singularity.rst(Deltares 사내문서)·numerical_implementation/validation.rst(skeleton, 문서 자체 부재로 disclosed). ★기록 보존 finding: Green-Ampt 인덱싱 버그(sfincs_infiltration.f90:856 np vs nm — 외부 미제출, 위키만 기록 2026-07-07 결정).

---

## 13. LISFLOOD-FP 🟢 **종결 2026-07-12** (classic+swe+cuda C++/CUDA / SA 8 + MN 1)

> 신규 모델(2026-06-18) — §12 와 동일하게 종결 시 섹션 신설.

**커버리지**: 전 솔버 8노트 — lisflood.cpp 다중솔버 dispatch·classic FP(ACC·diffusive·SGC·weir)·swe FV1/DG2(HLL·SSP-RK2)·cuda GPU·acc_nugrid 동적해상도·**mwdg2-adaptive-mra**(멀티웨이블릿 MRA, 2026-07-07)·IO/boundary·sgm_fast. MN 1(user manual).

**종결 판정(2026-07-12)**: 마지막 cross-model flag 해소 — cuda/adaptive `tol_h`=**1e-3 하드코딩**(SolverParams.h:15, parfile 미노출 — tol_q 데드 파라미터와 같은 계열, classic DepthThresh 와 별개 변수·동값). 침수노출 대조노트 미커버 잔여 0. ★기록 보존 finding: maxes.qy copy-paste 버그(get_max_scale_coeffs.cu:23, y-흐름 과소 refine — 외부 미제출, 위키만 기록 2026-07-07 결정). 잔여 매뉴얼 심화=user manual 노트가 코어 커버, 비코어 판정.

---

## 14. ShorelineS 🟡 **신설 2026-07-17** (functions 136 .m / SA 1 architecture-map)

- **정체**: free-form one-line 해안선 진화(Roelvink IHE Delft·Huisman Deltares, MATLAB/Octave, LGPL — LICENSE=v3 전문·소스헤더=2.1+ 병존 disclosed). 위키 유일 해안선 진화 클래스.
- **스냅샷(audited_ref)**: git `7bf4481ab84c635033ef475fa648a1b09cf9f36b`(2025-10-07), depth-1 clone 2026-07-17. 소스: `models/ShorelineS/raw/source_code/shorelines/`(gitignore) + 외부 드라이브 아카이브 사본(로컬 관리, G8b).
- **분모**: `functions/` **136 .m**(전수 ls). T티어 vendored = **0**(자체 구현만). C티어 후보 ≈ 40(transport 9·wave 12·coastline change·사구/스핏/양빈/조석/수로 모듈군), 잔여 S티어(prepare/get 유틸·plot·IO). 문서축 = repo `doc/` 3 PDF(기준논문 Roelvink 2020 Frontiers 7:535 — manual-notes 발췌 대상·ICEC2018·FAQ) + `ShorelineS-Publications.txt`(후속 문헌 리스트).
- **현황(코어 1차 검수 2026-07-17 동일 세션)**: SA 4 verified — [architecture-map](ShorelineS/source-analysis/shorelines-architecture-map.md)(골격·분모) / [transport-formulations](ShorelineS/source-analysis/shorelines-transport-formulations.md)(★문서화 5종 vs **실분기 7종**(+RAY·TIDEPROF) — CERC1 k=0.2 vs SPM 0.39 주석·VR14 vtide=0 하드·회절 dHS 2차항·Sphimax 포물선 반복·adt=ds²h0/(4QSmax) 확산기준) / [coastline-change](ShorelineS/source-analysis/shorelines-coastline-change.md)(staggered FTCS Eq.5 동형·Bruun −SLR/tanβ·★groyne 침식 시 구조물 자동 육측연장·mud dndt 대체 vs groyne점 가산 비대칭 관찰) / [wave-dune-spit-modules](ShorelineS/source-analysis/shorelines-wave-dune-spit-modules.md)(회절 Kd Roelvink 지수형/Kamphuis 구간식·방향분산 에너지 재결합·Stockdon runup verbatim·overwash 광선법=Ashton-Murray 벡터판). MN 1 — [roelvink2020-frontiers](ShorelineS/manual-notes/shorelines-roelvink2020-frontiers.md)(Eq.1/Eq.5·고각도·월류 코드 대조 완료). **잔여(disclosed)**: wave_diffraction.m 기하 본문(928줄 중 계수부만)·transport_mud.m 본문·merge_coastlines_mc(690)·prepare_grid_groyne(408)·make_sgrid_mc(302)·FAQ PDF 발췌 — 종결 판정은 잔여 소진 후.

## 9. 검수 진행 규약

1. 한 단위(모듈/문서) 검수 완료 시 → source-analysis(또는 manual-notes) 노트 작성 + **본 원장 상태 갱신** (⬜→🟡/✅).
2. T티어는 코드 검수 제외, 라이선스·버전·출처만 모델 README 에 기록.
3. 우선순위는 §0 대시보드 따름: SWASH → Delft3D(waq·dflowfm·fbc/rr/rtc) → ROMS(adjoint suite·Utility) → FUNWAVE → ADCIRC(gahm·asgs) → 매뉴얼 전수화.
4. 검수 깊이는 산출물 규모에 비례 (santa-method) — 커널 서브루틴은 deep, util/IO 는 요약 가능.
5. 본 원장은 [INDEX.md](../INDEX.md) 에서 진입.
