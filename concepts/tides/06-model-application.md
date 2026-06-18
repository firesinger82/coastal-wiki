---
title: "조석 — 06 모델 적용 (EFDC / ADCIRC / ROMS / XBeach / Delft3D)"
topic: tides
canonical_source: self
citation_status: verified
verification_method: "본 문서는 **요약 + 링크 중심** (canonical source 분리 규칙 [CONVENTIONS.md §3]). 각 모델의 조석 구현은 다음 검수완료(verified) 모델 노트로 cross-link·검증됨: ADCIRC tidal forcing(NTIP/fort.15 NBFR/fort.24 SAL — source-code file:line) = `models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md` + harmonic prep = `.../adcirc-tide-harmonic-prep.md`; ROMS 경계 조석(SSH_TIDES/UV_TIDES, set_tides.F) = `models/ROMS/source-analysis/roms_tidal_forcing.md`; EFDC 경계 조석(PSER + MTIDE harmonic synthesis, C14-C21 cards) = `models/EFDC/source-analysis/efdc_boundary_conditions.md` §A,§G,§H; Delft3D-TIDE 조화분석/예측(Ch 8 + App A/B) = `models/Delft3D/manual-notes/delft3d-tide-user-manual.md`; XBeach 조석(`tideloc`/`zs0file`) = `models/XBeach/manual-notes/xbeach-master-manual.md` §3.2.3; EFDC 카드(C14 MTIDE/C15) = `models/EFDC/manual-notes/efdc-implementation-guide.md`. **여전히 source-needed**: Delft3D-FLOW의 모델 내 조석 경계 forcing(`.bnd`/`.bca` 정확 사양 — Delft3D-TIDE 노트는 분석/예측 도구이지 FLOW 경계 forcing 매뉴얼이 아님), §6 비교표의 일부 일반론 항목, 글로벌 DB(TPXO/FES/NAO) 자체 사양(외부)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.8 (1M context) — 모델 노트 cross-reference"
verification_date: 2026-06-18
related:
  - models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md
  - models/ROMS/source-analysis/roms_tidal_forcing.md
  - models/EFDC/source-analysis/efdc_boundary_conditions.md
  - models/Delft3D/manual-notes/delft3d-tide-user-manual.md
---

# 조석 — 06 모델 적용

> **Canonical source 규칙** ([CONVENTIONS.md §3](../../CONVENTIONS.md)): 모델 메커닉(구현·서브루틴·알고리즘)은 `models/<model>/`이 진실의 원천. 본 페이지는 **요약 + 링크만**. 구현 디테일 복제 금지 (drift 방지).

이 토픽이 4개 주요 수치모델에서 어떻게 구현·적용되는지 정리. 각 모델의 객관 자료는 별도 `models/<model>/` 서브트리.

## 1. 공통 패턴

모든 연안·해양 hydrodynamic 모델은 조석을 **외해 개경계 (open boundary) forcing**으로 입력. 두 방식:

### 1.1 분조 forcing (Harmonic Boundary)

외해 경계점에서 시간 t의 수위 η(t):

```
η(t) = Z₀ + Σ_n H_n cos(σ_n t - g_n + φ_n)
```

(`02-theory.md` §4 모델과 동일, with adjustment of phase reference)

각 경계점에서 분조별 (진폭, 위상)을 입력. 데이터 출처:
- **현지 관측**: KHOA tide gauge 조화분해 결과 (`03-analysis-methods.md`, `05-examples.md` §3)
- **전 지구 조석 모델**: TPXO·FES·NAO·GOT (`04-code-and-tools.md` §6)
- **다중 모델 + tide gauge 검증** (권장)

### 1.2 시계열 forcing (Time-series Boundary)

외해 경계점에서 직접 η(t) 시계열 입력 (이미 조화 + 비조화 합쳐진 형태). 출처:
- 분조 forcing 결과를 시간 적분
- 실측 시계열 (인근 정점 + 보간)
- 광역 모델 (글로벌 ocean model) 출력의 경계 추출

비조석 효과 (storm surge, IB 효과 등)를 포함하려면 시계열 forcing 필요.

### 1.3 한국 적용 권장

| 영역 | forcing 권장 |
|---|---|
| 한국 서해 | FES2022 분조 4개 (M₂·S₂·K₁·O₁) + 인천·군산·목포 KHOA gauge 검증 |
| 한국 남해 | FES2022 또는 TPXO10 + 부산·여수 검증 |
| 한국 동해 | NAO.99Jb + 묵호·속초 검증 (일주조 우세 시 K₁·O₁ 비중 ↑) |
| 폭풍해일 동반 시뮬 | 분조 forcing + storm surge 별도 합산 |

`02-theory.md` §8 약최저저조위 ↔ 모델 datum 일치 확인 필수 — KHOA 기본수준면 사용 시 모델 zero datum도 동일하게 맞춰야.

## 2. EFDC

> **Canonical source**: [`models/EFDC/source-analysis/efdc_boundary_conditions.md`](../../models/EFDC/source-analysis/efdc_boundary_conditions.md) (verified, source-code file:line)

EFDC에서 조석은 **개경계 수위(pressure BC)**로 진입한다. source-code 분석(위 노트)에 따르면 두 경로가 공존하며 합산 가능:

### 2.1 PSER 시계열 + MTIDE 분조 합성 (verified)

검수완료 노트 [`efdc_boundary_conditions.md`](../../models/EFDC/source-analysis/efdc_boundary_conditions.md) §A·§G 가 확인하는 실제 구현:

- **PSER (수위 시계열)**: `NPSER >= 1`일 때 `PSER.INP` 읽음. 헤더 `ITYPE,NREC,TMULT,...`. 수위 η를 pressure-head `G·η`로 변환해 S/W/E/N 압력셀에 적용 (`input.f90:5650-5685`, `calpser.f90:25-66`, `setopenbc.f90`). `ITYPE=1`은 cross-channel slope용 2-side. → §1.2 시계열 forcing 패턴에 해당.
- **MTIDE 조화 합성**: `NWTSER` 심볼은 없고 `MTIDE` + periodic pressure forcing `NPFOR`로 분조 강제 (`input.f90:732-754`). C15가 `SYMBOL(M),TCP(M)`(분조명·주기)을, C17이 각 분조 진폭/위상→cos/sin 계수를 읽어 경계별 `PCB*/PSB*`(× G)로 변환. 런타임 `SETOPENBC`가 `TIMESEC`·`TCP`로 `cos/sin`을 계산해 각 경계 압력에 `PCB·cos + PSB·sin` 가산 (`setopenbc.f90:231-260`). → §1.1 분조 forcing 패턴에 해당.
- **총 경계 수위 = PSER 시계열 + 조화 합성** (둘 중 하나만 또는 합산 — `efdc_boundary_conditions.md` §G 결론). 조석+기상 surge 결합 시 PSER(관측) + 조화 block(잔차 처리).
- 위상은 **degrees**, 진폭 cm 입력 시 `RMULADJ=0.01` 필요 (노트 §G working rule).

> 정조 간조에 BC셀이 마르면 `LOPENBCDRY` 플래그로 해당 셀 비활성화 (`efdc_boundary_conditions.md` §H) — 간석지 조간대 경계 처리 시 주의.

분조 주파수(cycles/hour) 표준값은 [Foreman 1977 appendix](../../textbook/notes/tides-foreman1977-appendix.md) 참조; EFDC 메뉴얼 카드 정식 포맷은 [`efdc-implementation-guide`](../../models/EFDC/manual-notes/efdc-implementation-guide.md) — **C14 `MTIDE`**(조석 forcing, p.22)·**C15** 분조 constituent 기호·주기(p.23)·`PSER.INP`(수위 BC, p.69) verified.

### 2.3 EFDC 관련 textbook 자료

- `textbook/sources.yml`에 두 출처 등록:
  - `efdc-general` — `692624517-EFDC.pdf` (48 KB, 요약·index 추정)
  - `efdc-sed-trans-2003` — `86899804-EFDC-Theory-Tech-Aspects-of-Sed-Trans-2003-05.pdf`

EFDC 조석 카드(C14 MTIDE·C15 constituent·PSER)는 [`efdc-implementation-guide`](../../models/EFDC/manual-notes/efdc-implementation-guide.md) + source-analysis [`efdc_boundary_conditions`](../../models/EFDC/source-analysis/efdc_boundary_conditions.md)로 verified.

## 3. ADCIRC

> **Canonical source**: [`adcirc-tide-forcing-implementation.md`](../../models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md) + [`adcirc-tide-harmonic-prep.md`](../../models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md) (verified, source-code file:line)

ADCIRC는 다른 모델과 달리 조석을 **두 경로로 동시에** 다룬다 — (a) 전영역 **평형 조석 potential**(body force)과 (b) 외해 개경계 **조화 forcing**. 두 노트가 source-code로 확인.

### 3.1 fort.15 제어 — NTIP, NBFR (verified)

검수완료 노트 [`adcirc-tide-forcing-implementation.md`](../../models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md)가 확인:

- **`NTIP` (tidal potential flag)**: `0`=off, `1`=평형 조석 potential, `2`=+self-attraction & loading(SAL) (`read_input.F:1705-1731`). `02-theory.md` §2 평형 조석을 ADCIRC가 body force `TIP2`로 구현 — 분조별 `TIPOTAG`(TPK 계수·ETRF earth-tide reduction·FFT nodal factor·FACET eq.arg), 위도 의존 종(species) 계수 `L_N`(`adcirc.F:301-307`)로 합성 (`timestep.F:1507-1562`). 하드코딩 분조 없음, 사용자 지정.
- **`NBFR` (개경계 분조 수)** + per-node 진폭 `EMO`/위상 `EFA` (`read_input.F:3410-3456`). 매 timestep 경계 수위 합성: `Eta2 += EMO·FF·RampElev·cos(AMIG·timeh + FACE − EFA)` (`gwce.F:1638-1650`). → §1.1 분조 forcing 패턴. (이 코드베이스는 `EMO/EFA` 사용, 일부 fork의 `BCRFA/BCRFP` 아님.)
- **`fort.24` SAL**: `NTIP=2`에서만 읽음(`read_input.F:6282-6463`); `TIP2 += SALTMUL·SALTAMP·cos(ARGT − SALTPHA)`. 천해 M2 진폭을 5-10% 낮춤(노트 working rule).
- **`REFTIM`**: 조화 시간기준 epoch. `FACE/FACET`의 천문기준과 불일치가 가장 흔한 위상 오차 원인 (`adcirc-tide-harmonic-prep.md` §F).

### 3.2 분조 prep — 외부 DB → fort.15 변환 (verified)

[`adcirc-tide-harmonic-prep.md`](../../models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md) 핵심 사실: **ADCIRC는 FES/NAO/TPXO 내장 파서가 없다**. 외부 전처리로 DB→경계노드 보간 후 fort.15 NBFR block(per-node `EMO`(m)·`EFA`(deg, lag convention))과 fort.24 SAL을 직접 작성해야 한다. `FF`/`FACE` nodal factor·eq.arg는 T_TIDE/UTIDE/pyTMD로 epoch별 계산. 한국 연안은 NAO99jb가 M2/S2/K1/O1 양호, FES2022b가 N2/K2/P1 추가 정확도(노트 working rule). → §1.3 한국 적용 권장과 일치.

`02-theory.md` §8 datum 일치 + 위 EFA의 lag(`cos(arg−phase)`) 규약, cm↔m 단위 확인이 ADCIRC 조석 검증 핵심 pitfall.

## 3b. ROMS

> **Canonical source**: [`roms_tidal_forcing.md`](../../models/ROMS/source-analysis/roms_tidal_forcing.md) (verified, `set_tides.F` source-code)

ROMS는 regional 모델로, ADCIRC의 전영역 tidal potential과 달리 조석을 **주로 외해 개경계**에 넣는다. 검수완료 노트 [`roms_tidal_forcing.md`](../../models/ROMS/source-analysis/roms_tidal_forcing.md)가 `set_tides.F`(645줄)로 확인:

- **SSH_TIDES**: 조위 조화상수(`SSH_Tamp`·`SSH_Tphase`) × `cos(ω·t − φ)` 합 → 경계 자유표면(Chapman/Flather BC 입력). → §1.1 분조 forcing.
- **UV_TIDES**: 조류 타원(`UV_Tamp`/`UV_Tphase`/`UV_Tangle`) → 경계 barotropic 유속. ADCIRC가 수위만 합성하는 것과 달리 ROMS는 조류(수평조)도 직접 경계에 강제.
- `Tperiod`=분조 주기(M2/S2/K1/O1 등), `mod_tides`가 조화상수 보관. nodal correction(18.6년 교점)·equilibrium argument로 `tide_start` 기준 보정 + ramp.
- **AVERAGES_DETIDE** (`set_tides.F:32-48`): 출력 시 조석 성분 제거 → 잔차(subtidal) 순환만 출력 (ADCIRC harmonic analysis와 반대 방향=제거).
- 조화상수는 외부(TPXO/FES/OTPS)→ROMS forcing NetCDF. ADCIRC와 마찬가지로 DB 선택은 모델 상류 단계.

## 4. XBeach

> **Canonical source**: [`models/XBeach/`](../../models/XBeach/) (source-analysis 32 + manual-notes 4, verified)

XBeach는 **단기 폭풍 시뮬레이션** 위주 (수일~수주). 조석 forcing은:
- 짧은 시뮬 기간 내 수위 변화로 적용
- 분조 forcing보다 시계열 forcing이 일반적

입력: `params.txt` 의 **`tideloc`** (= 0 uniform `zs0` / 1·2·4 시계열 corner 수) + **`zs0file`** (수위 시계열 파일)로 적용 — [`xbeach-master-manual`](../../models/XBeach/manual-notes/xbeach-master-manual.md) §3.2.3(p.46), params.txt 예시 `tideloc=2`/`zs0file`(p.49). (※ `tide.txt` 라는 고정 파일명은 없음 — 사용자가 `zs0file` 로 지정.)

## 5. Delft3D

> **Canonical source (조화분석·예측 도구)**: [`delft3d-tide-user-manual.md`](../../models/Delft3D/manual-notes/delft3d-tide-user-manual.md) (verified, manual Ch 8 + App A/B)

### 5.1 Delft3D-TIDE — 분조 산출(ANALYSIS/PREDICT) (verified)

검수완료 매뉴얼 노트 [`delft3d-tide-user-manual.md`](../../models/Delft3D/manual-notes/delft3d-tide-user-manual.md)가 확인하는 것은 Deltares **Delft3D-TIDE** 도구 — 관측 수위/유속에서 조화상수 $A_0,A_i,G_i$를 **최소제곱(LU분해)**으로 추정(ANALYSIS)하고 임의 기간 예측(PREDICT)·고저조표(HILOW)·천문인자(ASCON)·Fourier(FOURIER). 이는 `03-analysis-methods.md`의 조화분해를 Delft3D 생태계에서 수행하는 도구이며, **그 출력 분조가 아래 FLOW 경계 forcing의 입력**이 된다.

- 지배식 (Ch 8, Eq.8.1): $H(t)=A_0+\sum_i A_i F_i\cos(\omega_i t+(V_0+u)_i-G_i)$ — $F_i$ nodal factor, $(V_0+u)_i$ astronomical argument, $G_i$ improved kappa(국지 위상지연). `02-theory.md` §4 합성식과 동형.
- **Rayleigh 기준** $\Delta\omega=360°/T$ (관측기간 T로 분해 가능한 최소 주파수차) + **Nyquist** $\Delta t \le T_{min}/2$가 분조 선택을 제약 (Ch 8.3.2-3).
- **Astronomical coupling**: 단기 계열에서 분해 불가한 sub-component를 main에 묶어 lumped로 풀고 천문관계로 복원 — 잘 알려진 결합 (K1,P1)·(N2,NU2)·(S2,K2) (Ch 8.3.4, App B에 진폭비 정량화: P1=0.328·K1, N2=0.191·M2, K2=0.284·S2 등). `03-analysis-methods.md`의 inference 개념과 대응.
- App B 내부 component base **234개** + 주파수(degr/hour) — M2=28.9841042, S2=30.0, K1=15.0410686 등 표준값(Foreman과 대조 가능).

### 5.2 D3D-4 FLOW / D-Flow FM — 모델 내 조석 경계 forcing (source-needed)

- D3D-4 FLOW: `.bnd`(경계 정의) + `.bca`(분조 진폭·위상) — §5.1 Delft3D-TIDE 산출 분조를 각 경계점별로 입력.
- D-Flow FM: unstructured mesh(ADCIRC 유사), `.bnd`/`.ext`/`.bc`로 더 유연한 boundary.

→ FLOW/FM의 `.bnd`/`.bca`/`.bc` **정확한 파일 포맷 및 경계 forcing 적용 메커닉**은 Delft3D-TIDE 노트(분석/예측 전용)가 다루지 **않음** — [`delft3d-flow-user-manual`](../../models/Delft3D/manual-notes/) 발췌 필요 (현재 미작성, **source-needed**).

## 6. 모델 간 비교 — 조석 적용 관점

| 항목 | EFDC | ADCIRC | ROMS | XBeach | Delft3D |
|---|---|---|---|---|---|
| 격자 | curvilinear orthogonal | unstructured triangular | curvilinear (ROMS-grid) | 직교/곡선 | 구조 (D3D-4) 또는 비구조 (FM) |
| 조석 진입 경로 (검수 노트) | 경계 압력셀: PSER 시계열 + MTIDE 조화 합성 | 경계 조화(NBFR `EMO/EFA`) + 전영역 평형 조석 potential(NTIP) | 경계 SSH_TIDES(조위)+UV_TIDES(조류) | 시계열 위주 (미검수) | TIDE 도구 산출 분조 → FLOW `.bca` (FLOW 경계 미검수) |
| 조류(수평조) 직접 강제 | (경계 유속 합성) | 수위 위주 | **SSH+UV 둘 다** | n/a | 분조 경계 |
| 외부 DB 파서 내장 | 무 (전처리) | **무** (fort.15 전처리 필수) | 무 (forcing NetCDF 전처리) | n/a | TIDE는 분석/예측 자체 도구 |
| 한국 서해 적합도 | 양호 (사용자 주력) | 양호 | 양호 | 폭풍 케이스만 | 양호 |

> "조석 진입 경로" 행은 각 모델의 **검수완료 source-analysis/manual 노트**로 verified (EFDC `efdc_boundary_conditions.md`+`efdc-implementation-guide.md`, ADCIRC `adcirc-tide-*.md`, ROMS `roms_tidal_forcing.md`, Delft3D `delft3d-tide-user-manual.md`, XBeach `xbeach-master-manual.md` `tideloc`/`zs0file`). Delft3D-FLOW의 모델 내 경계 forcing(`.bnd`/`.bca`) 행만 **미검수(source-needed)**. 분조 수·비선형 천해 분조 등 정량 비교는 각 모델 manual 추가 발췌 후 정밀화. **개인 사용 경험은 `experience/`로** (CONVENTIONS.md §6).

## 7. 다른 토픽과의 교차

조석은 단독 적용이 드물고 다음과 결합:

- **폭풍해일** ([`concepts/storm-surge/`](../storm-surge/), STABLE) — 조석 + 해일 superposition
- **표사이동** ([`concepts/sediment-transport/`](../sediment-transport/), STABLE) — 창조류·낙조류 비대칭이 표사이동 방향 결정
- **하구 염분** — 조석 mixing이 estuarine circulation 좌우
- **항만 자연 공명** — 조석 주기가 항만 resonance와 일치할 때 amplitude 증폭

각 결합은 해당 토픽 작성 시 본 06으로 cross-link.

## 8. 보강 상태

**검수완료(verified)로 cross-link됨:**

- [x] EFDC 경계 조석 — [`efdc_boundary_conditions.md`](../../models/EFDC/source-analysis/efdc_boundary_conditions.md) §A(PSER)·§G(MTIDE 조화)·§H(LOPENBCDRY)
- [x] ADCIRC 조석 — [`adcirc-tide-forcing-implementation.md`](../../models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md)(NTIP/NBFR/SAL) + [`adcirc-tide-harmonic-prep.md`](../../models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md)(DB→fort.15 prep)
- [x] ROMS 경계 조석 — [`roms_tidal_forcing.md`](../../models/ROMS/source-analysis/roms_tidal_forcing.md)(SSH_TIDES/UV_TIDES, set_tides.F)
- [x] Delft3D-TIDE 조화분석/예측 — [`delft3d-tide-user-manual.md`](../../models/Delft3D/manual-notes/delft3d-tide-user-manual.md)(Ch 8 + App A/B)
- [x] EFDC 매뉴얼 카드 — [`efdc-implementation-guide.md`](../../models/EFDC/manual-notes/efdc-implementation-guide.md)(C14 MTIDE p.22·C15 constituent p.23·PSER.INP p.69)
- [x] XBeach 조석 — [`xbeach-master-manual.md`](../../models/XBeach/manual-notes/xbeach-master-manual.md)(`tideloc`/`zs0file` §3.2.3 p.46)

**여전히 source-needed (외부):**

- [ ] `models/Delft3D/manual-notes/delft3d-flow-user-manual` — D3D-4/FM의 `.bnd`/`.bca`/`.bc` 경계 forcing 정확 사양 (TIDE 도구 노트는 분석/예측 전용)
- [ ] §6 비교 표의 분조 수·비선형 천해 분조 등 정량 항목 출처
- [ ] 글로벌 DB(TPXO/FES/NAO) 자체 사양(외부)
- [ ] 글로벌 DB(TPXO/FES/NAO/GOT) 자체 사양 — 외부, `04-code-and-tools.md` §6

## 9. 연결

- `01-concept.md` ~ `04-code-and-tools.md` — 도메인 지식 (verified)
- `05-examples.md` — 조화상수 산출 → 본 페이지의 forcing 입력에 활용
- 모델별 객관 자료 (canonical sources, 조석 부분):
  - EFDC 경계 조석 — [`efdc_boundary_conditions.md`](../../models/EFDC/source-analysis/efdc_boundary_conditions.md) (verified)
  - ADCIRC 조석 — [`adcirc-tide-forcing-implementation.md`](../../models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md), [`adcirc-tide-harmonic-prep.md`](../../models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md) (verified)
  - ROMS 조석 — [`roms_tidal_forcing.md`](../../models/ROMS/source-analysis/roms_tidal_forcing.md) (verified)
  - Delft3D-TIDE — [`delft3d-tide-user-manual.md`](../../models/Delft3D/manual-notes/delft3d-tide-user-manual.md) (verified)
  - [`models/XBeach/`](../../models/XBeach/) (source-analysis 32 + manual-notes 4, verified)
- 글로벌 조석 모델 (`04-code-and-tools.md` §6):
  - TPXO, FES, NAO, GOT — 본 페이지의 forcing 데이터 원천
- 사용자 경험 (검증 통과 시):
  - `experience/efdc-tidal-forcing-*.md` (미작성, 3조건 통과 시) — EFDC 실제 사용 패턴
