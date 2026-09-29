---
title: "조류 — 06 모델 적용"
topic: currents
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "조류의 운동량·연속 방정식 흐름 해상(currents solver core) claim 은 검수완료 모델 source-analysis 노트로 verified — ROMS [[roms_baroclinic_3d]]·[[roms_barotropic_2d]] (3D 경압 step3d_uv / 2D 순압 step2d 모드분할, file:line), Delft3D [[delft3d_flow2d3d_dispatcher]] (구조격자 TRISULA ADI kernel) + [[delft3d_dflowfm_compute_core]] (비구조 FM furu/s1ini/u1q1 semi-implicit θ-method), EFDC [[efdc_hydro_core]] (external 2D / internal 3D 모드분할 + PCG 연속식). 여전히 source-needed: §1.1~1.3·§6~8 의 조류 forcing 입력 포맷·글로벌 datum(TPXO/FES/NAO.99Jb/KHOA)·한국 해역 권장·검증 임계치는 모델 manual / 외부 datum 문서 미수록분으로 잔존. ADCIRC·XBeach §3·§5 도 검수 노트 미연결로 잔존. **2026-09-28 토큰 재분류**: §2 PSER 포맷(efdc_boundary_conditions §A)·§4 .bca 포맷(delft3d-flow-boundary-forcing §3)·§3 ADCIRC 경계 분조(NBFR/NFFR)·§5 XBeach 흐름 경계(xbeach_flow_boundary_conditions·xbeach_tide_forcing)는 이미 검수완료 models/ 노트가 있어 연결로 해소. §3 의 구 서술 'ADCIRC tidal database 가 조위+u,v 분조를 함께 보간' 은 근거 없음 — 소스 노트상 경계 강제는 수위 분조(NBFR)와 법선 flux 분조(NFFR)이고 u,v 분조 입력 카드는 확인되지 않아 정정. 잔존: 글로벌 datum·한국 해역 권장·검증 임계치, ADCIRC tidal database 내용(코퍼스 밖). **2026-09-28 추가**: §6 조류 가용성 표를 pyTMD 모델 DB·AVISO FES2022 release·NAO 공식 페이지·adcirc.org 로 재작성 — FES2022 조류 비공개, NAO.99 조류 미배포, KHOA CSV 성분 판별은 이 verification_method의 검증 범위에서 제외(관련 경험 분석은 탐색용), 따라서 §7 구 권장표(서해 KHOA CSV·동해 NAO.99Jb) 폐기; §8 무출처 임계(±20%·±10°) 삭제."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.8 (1M context) — 모델 solver-core 노트 cross-link"
verification_date: 2026-06-18
related:
  - models/ROMS/source-analysis/roms_baroclinic_3d.md
  - models/ROMS/source-analysis/roms_barotropic_2d.md
  - models/Delft3D/source-analysis/delft3d_dflowfm_compute_core.md
  - models/EFDC/source-analysis/efdc_hydro_core.md
---

# 조류 — 06 모델 적용

> **Canonical source 규칙** ([CONVENTIONS.md §3](../../CONVENTIONS.md)): 모델 메커닉은 `models/<model>/`이 진실의 원천. 본 페이지는 요약 + 링크만.

조위 ([`concepts/tides/06-model-application.md`](../tides/06-model-application.md))와 동일한 모델군이 조류도 함께 출력·입력. 본 페이지는 조류 특화 항목.

## 0. 모델별 흐름(운동량·연속) 해상 — solver core

조류·해류는 결국 모델이 **운동량 방정식 + 깊이적분 연속 방정식**을 어떻게 이산화·시간적분하느냐로 결정된다. 아래는 검수완료 source-analysis 노트로 뒷받침되는 모델별 흐름 해상 메커닉 요약(상세는 각 노트가 canonical).

### 0.1 ROMS — split-explicit 경압3D + 순압2D

ROMS는 빠른 **순압(2D, 깊이적분) 모드**와 느린 **경압(3D) 모드**를 분리(mode-splitting)해 푼다.

- **3D 경압 흐름**: `step3d_uv` 가 운동량 신시간 update를 명시적으로 수행(`u(...,nnew) += DC*ru`), Coriolis(`UV_COR`)는 flux 형 `0.5*Hz*fomn` 으로 `ru/rv` 에 삽입, 압력경사는 `prsgrd` 변형 중 선택 — [[roms_baroclinic_3d]] §A·§F (`rhs3d.F:562-619`, `step3d_uv.F:359-360`). 수직좌표 `Hz`(s-coordinate)가 모든 흐름 연산의 기반(§C).
- **2D 순압 흐름**: `step2d` 가 fast substep `nfast` 반복으로 깊이적분 연속(`rhs_zeta=div(transport)`)·운동량(`rhs_ubar/vbar`, Coriolis `0.5*Drhs*fomn`)을 LF-AM3 / FB-AB3-AM4 로 적분, fast-time 평균 `DU_avg1/2` 를 3D로 되먹여 질량보존 복원 — [[roms_barotropic_2d]] §B·§C·§D (`step2d_LF_AM3.h:924-941, 2577-2693`). `NDTFAST` 가 모드분할 substep 수.
- 개경계 흐름 BC: `Flather`(조석 방사) / reduced-physics, free-surface `Chapman` — [[roms_barotropic_2d]] §F.

### 0.2 Delft3D — 구조격자 TRISULA(ADI) + 비구조 FM(θ-method)

- **구조격자 (D3D-4 FLOW / flow2d3d)**: `flow2d3d_kernel` 가 **Stelling-Leendertse ADI**(Alternating Direction Implicit) 분할로 연속+운동량을 푼다 — [[delft3d_flow2d3d_dispatcher]] §3 (Lesser et al. 2004 검증 source). 8 package 구조에서 kernel 이 수치 코어, manager 가 time-step 제어.
- **비구조격자 (D-Flow FM)**: link별 운동량을 `fu·ru` 계수로 환원(`furu`: $u^{n+1}_L = ru - fu\,(s_1(k_2)-s_1(k_1))$, 마찰 inner loop 4회), cell 연속식 행렬로 조립(`s1ini`→`s1nod`), 수위 `s1` 에 대한 대칭 양정부호 선형계를 **Gauss 소거 + CG** 로 풀고, link 속도·플럭스를 복원(`u1q1`) — [[delft3d_dflowfm_compute_core]] §2~§4·§6 (`furu.f90:200-204`, `s1ini.f90:328-344`, `u1q1.f90:80-82`). semi-implicit θ-method, 1D 가지망 + 2D 그물망 혼합.

### 0.3 EFDC — external 2D / internal 3D 모드분할 + PCG 연속식

EFDC도 **external(깊이적분 2D)** 과 **internal(3D shear)** 모드를 분리.

- **External 운동량**: `CALEXP`(3TL) / `CALEXP2T`(2TL) 가 이류·Coriolis·곡률(`CAC`)을 조립, 바람·바닥·압력·부력은 `CALPUV` 에서 합산 — [[efdc_hydro_core]] §A (`calexp.f90:571`, `calpuv9c.f90:256-257`).
- **External 연속**: `CALPUV9C`/`CALPUV2C` 가 자유표면 head `P` 에 대한 선형계를 **preconditioned conjugate gradient** 로 풀고 `HP=GI*P−BELV` 복원 — §B (`calpuv9c.f90:693-707, 804-807`).
- **Internal 3D 결합**: `CALUVW` 가 외부 단위유량에서 shear 재구성 → **barotropic correction**(3D 적분 transport를 2D 결과에 맞춤) → 개경계 mass-flux 보정 — §C (`caluvw.f90:601-624`). 이 보정 없으면 3D transport가 2D 솔버 결과에서 drift하여 질량보존 깨짐.
- 시간적분: 3TL(leapfrog+trapezoidal corrector, `IS2TIM=0`) vs 2TL(`IS2TIM>=1`) — §D.
- 조류 흐름의 개경계 forcing은 `CALPSER`/`SETOPENBC` 가 수위/압력 시계열을 `FP(L)` 에 기입(외부 솔버 전) — §G; §2.1 의 EFDC 조류 forcing 입력이 여기로 들어간다.

### 0.4 저면마찰 — 10모델 cross-model 대조

운동량 방정식의 저면마찰 항(법칙 선택지·조도 knob·implicit 처리·wave-current BBL)은 모델 간 편차가 캘리브레이션에 직결 — **[[bottom-friction-cross-model]]** 이 10모델(EFDC·Delft3D·ROMS·ADCIRC·SWASH·SFINCS·LISFLOOD-FP·FUNWAVE·Celeris·XBeach + SWAN 파랑소산 구분) 대조표의 canonical. 요지: z₀/log-law 3D 해양모델 계보(ZBR/z₀/Zob) vs Manning 계열 천수·범람 계보(`g n²/h^{1/3}`) vs 파랑 소산 별도 축(SWAN `FRICTION` 미지정 시 off 주의).

### 0.5 연직혼합·난류종결 — 5개 3D 모델 대조

연직 eddy viscosity 공급 메커니즘(MY2.5 계열 vs k-ε/GLS 계열 vs 진단 KPP)·안정함수 세대·배경 하한·파랑 TKE 주입 여부는 **[[vertical-mixing-cross-model]]** 이 canonical (ROMS·Delft3D·EFDC·SWASH·ADCIRC 3D). 요지: 파랑 표면 TKE 주입은 ROMS GLS(Craig-Banner)만 명시적, EFDC 는 저면응력 경유, SWASH breaking 은 수평 점성 경로 — 성층·상층 혼합 캘리브 시 최대 분기점.

### 0.6 시간적분 — 12모델 cross-model 대조

시간적분 스킴(LF-AM3·3TL/2TL·GWCE 3레벨·ADI·θ semi-implicit·SSP-RK·AB-AM·SMAC projection)·mode splitting·adaptive dt·implicit 성분은 **[[time-integration-cross-model]]** 이 canonical (ROMS·EFDC·ADCIRC·Delft3D-FLOW·FM·SWASH·FUNWAVE·Celeris·XBeach·SFINCS·LISFLOOD-FP·CADMAS). 요지: split-explicit(ROMS 단독) vs semi-implicit 중력파 격리(해양모델 다수) vs explicit CFL-adaptive(천수) vs 고차 RK/multistep(위상해상) 4계보 — dt 고정/적응 여부와 무조건 안정 성분이 모델 선택·런타임 예측의 1차 분기. 부수 적발: [[adcirc-timestep-orchestration]] §5 의 EFDC 파라미터 혼용 정정(2026-07-10).

> 위 §0 의 흐름 해상 claim 은 모두 검수완료 source-analysis 노트로 verified. §1·§6·§7 의 조류 자료 가용성은 2026-09-28 공식 배포처로 확인했다(§6 출처). **조류 검증의 수치 합격 임계**는 출처가 없어 제시하지 않는다(§8).

## 1. 모델별 조류 입출력

### 1.1 분조 forcing (Harmonic Current Boundary)

외해 개경계에서 조류 분조 forcing:
- 각 경계 셀에 분조별 (u_Lsmaj, u_Lsmin, u_θ, u_g) 4 parameter 또는 (u_진폭, u_위상, v_진폭, v_위상) 입력
- 데이터 출처: **TPXO10**·**FES2014** (u, v 분조 제공), 자체 ADCP 관측 조화분해. **KHOA 수치조류도 조화상수 CSV 는 남북(v) 성분만** 담아 u, v 분조 입력으로 쓸 수 없다([04 §2.3](04-code-and-tools.md)). FES2022 조류·NAO.99 조류는 공개 배포되지 않는다(§6)

### 1.2 시계열 forcing (Time-series Current Boundary)

외해 경계 점에 (u(t), v(t)) 시계열 직접 입력. 비조석 효과 (해류·바람 흐름) 포함 시 사용.

### 1.3 모델 출력 조류 분석

모델 결과의 조류 (u, v) 시계열을 UTide 2D로 후처리 → 검증·진단:
- 분조별 (Lsmaj, Lsmin, θ, g) 추출
- 관측 ADCP·수치조류도 격자와 비교
- 잔류 흐름·비선형 분조 평가

## 2. EFDC

> Canonical: [`models/EFDC/`](../../models/EFDC/) — 흐름 코어는 [[efdc_hydro_core]] 검수완료.
>
> EFDC 조류 흐름 해상(external 2D / internal 3D 모드분할, CALEXP·CALPUV·CALUVW)은 §0.3 참조. 본 절은 조류 forcing 입출력 운영 관점.

### 2.1 조류 forcing

- 분조 forcing 또는 시계열 forcing 둘 다 지원
- 입력: `efdc.inp` 경계 카드 + `pser.inp` (수위 시계열) + 자체 보조 파일
- 정확한 카드명·포맷은 [`efdc-implementation-guide`](../../models/EFDC/manual-notes/efdc-implementation-guide.md)(efdc.inp card 구조) 참조

### 2.2 조류 출력

- EFDC는 (u, v, w) 3D 흐름 출력 — 수직 평균 또는 층별
- 분석: snapshot 매 시간 / 시계열 추출 후 UTide 2D
- 검증: KHOA 수치조류도 격자 또는 ADCP 관측

→ EFDC 흐름 솔버(external 연속식 PCG, internal barotropic correction)가 (u, v, w) 출력을 생성하는 메커닉은 [[efdc_hydro_core]] §B·§C (`calpuv9c.f90:693-707`, `caluvw.f90:601-624`). 개경계 조류 forcing 의 솔버 진입 경로는 [[efdc_hydro_core]] §G (`calpser.f90`, `setopenbc.f90`). `PSER.INP` 포맷(헤더 `ITYPE, NREC, TMULT, TOFFSET, RMULADJ, ADDADJ, PSERZDF, INTPSER`, ITYPE 0/1 레코드, 압력수두 변환 `input.f90:5801-5836`)은 [[efdc_boundary_conditions]] §A, 조화 경계(C17 `PFAM`/`PFPH` — nodal factor·V0+u 를 사용자가 fold)는 [[efdc-tidal-forcing-conventions-v12]].

## 3. ADCIRC

> Canonical: [`models/ADCIRC/`](../../models/ADCIRC/) (source-analysis 38, verified)

- `fort.15` 수위 경계 분조 카드 `NBFR` (분조별 진폭·equilibrium argument) — [[adcirc-fort15-checklist-v1]], 개경계 조화 합성 `ETA2(NBDI) += EMO*FF*RampElev*cos(AMIG*timeh + FACE - EFA)` (`gwce.F:1638-1650`) 은 [[adcirc-gwce-implementation]]
- 주기 **법선 flux** 경계 분조 `NFFR` (flux 경계 IBTYPE 2/12/22/32/52 가 있을 때만) — [[adcirc-nffr-periodic-flux-boundary]] §1
- 출력 조류 조화분해: global velocity HA → `fort.54` — [[adcirc-tidal-forcing]]
- ★정정 (2026-09-28): 구판의 "ADCIRC tidal database 가 조위 + u, v 분조를 함께 보간" 은 근거가 없다. 위 소스 노트상
  경계 강제 입력은 수위 분조와 법선 flux 분조이며 u, v 분조 입력 카드는 확인되지 않는다.
  ADCIRC tidal database 는 판본마다 다르다 — ec_95d·ec2001_v2e·wc_2003 는 *"elevations and depth-averaged velocities"*, ec2001_v2d 는 조위만,
  ec2015·ENPAC15 는 두 판본(조위+유속 / 조위만). 영역은 서북대서양·동태평양 연안뿐이라 **한국 해역을 덮는 판본은 없다**
  ([adcirc.org/products/adcirc-tidal-databases](https://adcirc.org/products/adcirc-tidal-databases/), 2026-09-28 확인).

## 4. Delft3D

> Canonical: [`models/Delft3D/`](../../models/Delft3D/) — 흐름 커널 검수완료: 구조격자 [[delft3d_flow2d3d_dispatcher]], 비구조 FM [[delft3d_dflowfm_compute_core]].

- D3D-4 FLOW: `.bnd`, `.bca` (boundary, harmonic constituents) — 조위·조류 분조 직접 입력. 내부 흐름 해상은 `flow2d3d_kernel` 의 Stelling-Leendertse ADI (§0.2 / [[delft3d_flow2d3d_dispatcher]] §3).
- Delft3D FM: unstructured mesh, 동일 분조 지원. 흐름 솔버는 `furu`→`s1ini`→`s1nod`→Gauss+CG→`u1q1` semi-implicit θ-method 루프 (§0.2 / [[delft3d_dflowfm_compute_core]] §1·§8). 수위 경계(Dirichlet)·Riemann·velocity 경계의 행렬 처리는 [[delft3d_dflowfm_compute_core]] §3.2 (`s1nod.f90:181-277`).

> `.bnd`/`.bca` 조류 분조 카드 포맷은 [[delft3d-flow-boundary-forcing]] §3 (FLOW User Manual §4.5.6.1 p.50-53 + App A.2.11 p.455-456).

## 5. XBeach

> Canonical: [`models/XBeach/`](../../models/XBeach/) (source-analysis 32, verified)

XBeach는 단기 폭풍 모델. 조류는 보통 수위 시계열 forcing의 부산물 또는 별도 background 흐름.

흐름 해상은 [[xbeach_flow_solver]], 조위 경계 입력·보간은 [[xbeach_tide_forcing]] (`compute_tide_zs0.F90`), 흐름 경계의 tide 처리(instant/velocity/hybrid)·offshore front 는 [[xbeach_flow_boundary_conditions]].

## 6. 조류 (u, v) 자료 가용성 — 2026-09-28 확인

| 모델·자료 | 조류 (u, v) | 근거 |
|---|---|---|
| **TPXO10-atlas** | ✓ (z·u·v) | pyTMD 모델 DB `TPXO10-atlas-v2` 항목에 `z`·`u`·`v` |
| **FES2014** | ✓ (z·u·v) | pyTMD 모델 DB `FES2014` 항목에 `z`·`u`·`v` |
| **FES2022** | **✗ 공개 배포 안 함** | AVISO: *"The FES2022 currents are not disseminated yet, they will be delivered to scientific teams and for scientific studies on demand."* |
| **NAO.99b / NAO.99Jb** | **✗ 배포 목록에 없음** | NAO 공식 페이지 배포물 = 단주기·장주기 해양조석 + loading(radial displacement·potential) 뿐 |
| **GOT4.10 / GOT5.x** | ✗ (z 만) | pyTMD 모델 DB 에 `z` 만 |
| **KHOA 수치조류도 조화상수 CSV** | **v 성분만** | [04 §2.3](04-code-and-tools.md) — 벡터 재구성 불가 |
| **KHOA OpenAPI `tidalCurrentArea`** | ✓ 예측 유속·유향 (벡터) | [04 §3](04-code-and-tools.md) — 날짜·시각·영역 지정, 1–10 km 간격. 분조가 아닌 **시계열** 자료 |
| **ADCIRC tidal database** | 판본별(조위만 / 조위+유속) | §3 — 한국 해역 판본 없음 |

pyTMD 모델 DB: `pyTMD/data/database.json` (github.com/tsutterley/pyTMD, main, 2026-09-28). FES2022: [AVISO FES2022 release](https://www.aviso.altimetry.fr/en/data/products/auxiliary-products/global-tide-fes/release-fes22.html). NAO: [miz.nao.ac.jp/rise/s/nao99](https://www.miz.nao.ac.jp/rise/s/nao99/index_En.html).
조위(z) 쪽 모델 비교는 [`concepts/tides/04-code-and-tools.md` §6](../tides/04-code-and-tools.md).

## 7. 한국 해역 조류 경계 자료 — 선택지

★정정 (2026-09-28): 구판 권장표는 "서해 경계 = KHOA 수치조류도 분조", "동해 경계 = NAO.99Jb 조류" 였다. 둘 다 성립하지 않는다 —
수치조류도 CSV 는 v 성분만 있고, NAO.99 는 조류를 배포하지 않는다(§6).

| 필요 | 쓸 수 있는 자료 |
|---|---|
| 개경계 u, v **분조** (§1.1) | TPXO10-atlas · FES2014 (한국 해역 전역, 공개) |
| 개경계 u, v **시계열** (§1.2) | KHOA OpenAPI `tidalCurrentArea` 예측 벡터 (황해·남해 중심 — 동해 연안 격자 없음, [04 §2.3](04-code-and-tools.md)) |
| 조위 경계 (§1.1 대신 흔한 선택) | [`concepts/tides/06`](../tides/06-model-application.md) |

어느 자료가 한국 해역에서 더 정확한지는 이 위키에 비교 근거가 없다 — 권장 순위는 두지 않는다.

## 8. 모델 검증 — 조류 specific

| 항목 | 방법 |
|---|---|
| 분조별 진폭 정합 | 모델 출력의 **v 성분**을 UTide 로 분해해 KHOA 수치조류도 격자값(v 성분)과 비교 — 장축(Lsmaj)과 비교하면 안 된다 |
| 분조별 위상 정합 | 격자 지각은 g(135°E) — UTC 입력 UTide(G) 와 비교 시 G = g − 9a |
| 잔류 흐름 | 모델·관측 시계열 평균 비교 |
| 창·낙조류 비대칭 | 비선형 분조 (M₄·MS₄) 진폭 비교 |
| Hodograph (vector trace) | 시각적 패턴 정합 (왕복성/회전성) |

> 수치 합격 임계(구판의 ±20%·±10°)는 출처가 없어 뺐다 — 파랑 `waves/06` 의 검증 임계표와 같은 성격의 공백이다.

## 9. 보강 — `verified` 승격 체크리스트

- [x] `models/EFDC/source-analysis/` — 흐름 코어 [[efdc_hydro_core]] (external/internal 모드분할·PCG·barotropic correction·개경계 forcing 진입) **verified**
- [x] ROMS 흐름 코어 [[roms_baroclinic_3d]]·[[roms_barotropic_2d]] (경압3D step3d_uv / 순압2D split-explicit) **verified**
- [x] Delft3D 흐름 커널 [[delft3d_flow2d3d_dispatcher]] (구조격자 ADI) + [[delft3d_dflowfm_compute_core]] (비구조 FM θ-method) **verified**
- [x] EFDC `PSER.INP`·C17 조화 경계 포맷 — [[efdc_boundary_conditions]] §A · [[efdc-tidal-forcing-conventions-v12]] (2026-09-28 연결)
- [x] ADCIRC 경계 분조 NBFR/NFFR — §3 연결·정정 + tidal database 판본별 수록 변수(adcirc.org) (2026-09-28)
- [x] Delft3D `.bca` 조류 분조 포맷 — [[delft3d-flow-boundary-forcing]] §3 (2026-09-28 연결)
- [ ] 한국 적용 사례 1건 verified (`experience/` 경유 — 동해 조류 경계에 NAO.99Jb 는 쓸 수 없음, §6)

## 10. 연결

- `01`~`05` — 조류 도메인 지식
- [`concepts/tides/06-model-application.md`](../tides/06-model-application.md) — 조위 모델 적용 (동일 모델군)
- 흐름 솔버 코어 (검수완료): [[roms_baroclinic_3d]] · [[roms_barotropic_2d]] · [[delft3d_flow2d3d_dispatcher]] · [[delft3d_dflowfm_compute_core]] · [[efdc_hydro_core]]
- ADCIRC 흐름 코어: [[adcirc-momentum-implementation]] · [[adcirc-gwce-implementation]] / XBeach: [[xbeach_flow_solver]] · [[xbeach_flow_boundary_conditions]]
- `concepts/tides/04-code-and-tools.md` §6 — 글로벌 조석/조류 모델
