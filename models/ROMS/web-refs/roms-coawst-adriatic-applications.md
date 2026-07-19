---
title: "ROMS·COAWST 운영적용 리뷰 — Adriatic Sea (Carniel et al. 2013)"
topic: roms-web-refs
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "arxiv:1309.7600v4 (Carniel·Russo·Benetazzo 2013) **full PDF 직접 read (2026-07-19, pdftotext 5쪽)** — 격자 해상도·운영 개시일·강제력·경계조건·서브모델 구성 전부 본문 §1~§5·Conclusions 에서 확인. ★단 이 논문은 review 논문이라 관측 대비 정량 skill metric 은 미수록 — 검증 수치는 인용 하위 논문(Benetazzo et al. 2013 Ocean Modelling 70:152-165·Carniel et al. 2011·Russo et al. 2009)에 존재(본 노트 미확보, disclosed §6). COAWST 시스템 정의(Warner et al. 2010)·CSTMS 명칭은 본 논문 미인용 — publicly-known/외부 귀속([[roms-official-resources]] §3)으로 별도 표기."
note_author: "Claude Opus 4.7 (1M context) — abstract 초안 2026-06-15"
note_date: 2026-06-15
verification_by: "Claude Fable 5 — full PDF read"
verification_date: 2026-07-19
related:
  - models/ROMS/README.md
  - models/ROMS/web-refs/roms-official-resources.md
  - models/ROMS/source-analysis/roms_wec.md
  - models/ROMS/source-analysis/roms_nesting.md
  - models/SWAN/web-refs/swan-official-resources.md
---

# ROMS·COAWST 운영적용 리뷰 — Adriatic Sea

> [`roms-official-resources.md`](roms-official-resources.md) 의 공식 큐레이션 보완 — ROMS/COAWST 가 실제 반폐쇄해(Adriatic)에서 **순수 hydrodynamic → 완전 결합(COAWST)** 으로 발전한 운영·연구 적용 사례 리뷰. 모델 메커닉 자체는 [`source-analysis/`](../source-analysis/) 가 canonical, 본 노트는 적용 맥락(application context) 참조.

## 1. 출처

| 항목 | 값 |
|---|---|
| 제목 | "A review of modeling applications using ROMS model and COAWST system in the Adriatic sea region" |
| 저자 | Sandro Carniel (ISMAR-CNR), Aniello Russo (Univ. Politecnica delle Marche), Alvise Benetazzo (ISMAR-CNR) |
| arxiv ID | **1309.7600v4** (2013-09-29) |
| URL | <https://arxiv.org/abs/1309.7600> |
| citation_status | **verified** (full PDF read 2026-07-19 — 정량·구성 본문 확인; 관측대비 skill 은 §6 disclosed) |

Adriatic 해역: 이탈리아·발칸 3면 둘러싸인 NW–SE 세장형 반폐쇄분지, **약 700 km 길이 × 200 km 폭**, Otranto Strait 로 지중해 연결. Bora(NE)·Sirocco(SE) 바람 → NW 천해에 고파랑·연안침식 (Intro). ROMS = community·3D·**hydrostatic**·finite-difference·RANS 해석 모델 (Intro).

## 2. COAWST 시스템 — 본 리뷰의 결합 축

COAWST (Coupled Ocean-Atmosphere-Wave-Sediment Transport) 는 ROMS 를 해양 코어로 atmosphere·wave·sediment 모듈을 **MCT (Model Coupling Toolkit)** 로 결합:

- **Ocean**: ROMS ([`source-analysis/roms_baroclinic_3d.md`](../source-analysis/roms_baroclinic_3d.md), [`roms_barotropic_2d.md`](../source-analysis/roms_barotropic_2d.md))
- **Wave**: SWAN ([[../../SWAN/web-refs/swan-official-resources]]) — 본 리뷰 Adriatic 구현(NA-COAWST §3)은 ROMS↔SWAN **two-way coupling**, MCT 경유 (본문 §3)
- **Sediment**: 본 논문은 결합 표사 모듈을 **Carniel et al. (2011)** 로 인용 (§5). ⚠ "CSTMS (Community Sediment Transport Modeling System, Warner et al. 2008)" 명칭·COAWST 원논문 "Warner et al. 2010" 은 **본 논문에 미인용** — publicly-known 외부 귀속([[roms-official-resources]] §3)으로 별도 표기.
- ROMS 내 wave effect on current 연계는 [`source-analysis/roms_wec.md`](../source-analysis/roms_wec.md) (WEC, vortex-force) 참조

→ 본 리뷰는 이 결합 스택이 단일 해역에서 **다목적 운영체계**로 성숙한 사례를 정리한 1차 출처.

## 3. Adriatic 적용 5계열 (full PDF §1~§5)

### 3.1 AdriaROMS 4.0 — 수력학 운영 예보 (§1)

- **격자 2 km 정규격자, 전 Adriatic**, 매일 수치예보 산출. **해수면 3일 예보 + 수력학**.
- 강제력: **COSMO-I7 시간별 출력**에서 air-sea heat·momentum·water flux 상호계산.
- 경계: 주 분조(main tidal components) open boundary 부과 / Po 강 실시간 유량 / 그 외 **48개 하천·카르스트 용천**은 문헌 유래 월별 climatology / Otranto Strait 경계 T·S·수위·유속 = 이탈리아 GNOO Mediterranean Forecasting System.
- ARPA-SIMC 운영 파생 서브모델:
  - **1D morphodynamic 모델** (Emilia Romagna Po 삼각주 남측 노출 단면) — total water level(AdriaROMS) + Hs(SWAN-EMR)로 강제, 침수 조기경보.
  - **Rimini 해수욕장 수질 예측** — Delft3D 기반(Previbalneazione, EU Directive 2006/7/CE), total water level + COSMO-I7 10 m 바람 + SWAN-EMR Hs 경계.
  - **oil-spill 확산 rapid response** (지역·Coast Guard 공조) + **Po 강 염수쐐기(saline wedge) 침입 예측** — 비엄격 운영.

### 3.2 EMMA — 저산소(hypoxia) 이벤트 예보 (§2)

- 목적: 북 Adriatic(특히 Rimini) 단기 hypoxic event 예보. LIFE-Environment, 이·슬로베니아 파트너.
- 코어: ROMS + **Fennel 생지화학 모듈** — 무기질소(질산·암모늄)·식물/동물플랑크톤 biomass·소(<10 mm)/대 detritus (질소·탄소 농도)·무기탄소·용존산소 dynamics. 수주 pelagic 질소순환 + 수-저 계면 remineralisation.
- 강제: **COSMO-I7 (수평 7 km, ECMWF 경계, 관측 동화)**. 수평 **~2 km**, 출력 **3시간 간격**, 적분기간 **2007 늦봄 이후**.
- 2012 "Operation Dense Water"(ODW) — 속도·밀도장 R/V Urania 에 실시간 제공 → adaptive sampling.
- 상세: Russo et al. (2009), Russo et al. (2013).

### 3.3 NA-COAWST — 결합 파랑-해류 시스템 (§3)

- **북 Adriatic 서브분지 0.5 km 수평해상, 천해(최대수심 100 m)**, 격자는 **AdriaROMS 4.0 격자에 정확히 내접**하도록 설계.
- **two-way wave-current interaction**, ROMS↔SWAN 결합은 **MCT** 경유.
- 경계: AdriaROMS 4.0 + SWAN ITALIA(Valentini et al. 2007)가 남동 open boundary 에 유속·수위·T·S·파랑특성 제공 + 분조 부과.
- **운영 개시 2011-11-25**. ocean → wave 로 유속·자유수면 제공(형식 Benetazzo et al. 2013).
- 검증: CNR-ISMAR "Acqua Alta" tower + Jesolo AWAC(2013 겨울 배치) 초기결과가 NA-COAWST 개선 예보를 **정성적으로 뒷받침**(§3 — "seem indeed to support"). ⚠ 정량 skill 은 본 논문 미수록(§6).

### 3.4 소형 부어류 알·유생 수송·확산 (§4)

- 멸치·정어리 알·유생 — **ROMS 출력 구동 IBM(Individual Based Model)**(Russo et al. 2013). 대기·해양특성(유속장·하천유량) 상이한 2개년 커버.

### 3.5 Bevano 하구 고해상 표사 dynamics (§5)

- ROMS **완전 3D · SWAN two-way 결합 · 표사모듈(Carniel et al. 2011)** 통합모델.
- Bevano 하구(북 Adriatic) = **microtidal·저에너지 파랑 환경**. 2006 하구 인공개조(목재공학, 사구침식·홍수 방지). 극한 hydro-meteo 이벤트 형태변화 모델.
- 결과: **30년 빈도 홍수** 시 2차 유입구(inlet) 개방 가능성 확인 / **낙조(ebb tide) 우세**로 소형 ebb delta·swash bar 생성 → "minimum maintenance option" 전략(목구조 정기보수)로 지역 MSP 채택.

## 4. 상태최신 역량 (Conclusions)

리뷰가 명시한 채용 state-of-the-art 역량: **최신 bottom boundary layer 기술 · wetting/drying · 고급 연직혼합 · wave-current interaction 스킴**(Kantha & Carniel 2003; Carniel et al. 2009) · 생지화학 모듈. 최근 기능 = **one-way·two-way successive nesting + full two-way coupling** → 이탈리아 연안 초고해상 도달, 하구 환경 정밀 재현. 출력 **NetCDF CF-compliant → THREDDS Data Server(TDS)** 배포, catalog brokering(OpenSearch·OGC CSW)·INSPIRE 지향.

## 5. 본 위키 접점

| 본 위키 자료 | 접점 |
|---|---|
| [`source-analysis/roms_baroclinic_3d.md`](../source-analysis/roms_baroclinic_3d.md) | Adriatic 운영 코어 = ROMS 3D baroclinic |
| [`source-analysis/roms_wec.md`](../source-analysis/roms_wec.md) | ROMS↔SWAN two-way coupling 의 wave-current 연계 메커닉(NA-COAWST §3.3) |
| [`source-analysis/roms_biology.md`](../source-analysis/roms_biology.md) | EMMA Fennel 생지화학(§3.2) |
| [`source-analysis/roms_nesting.md`](../source-analysis/roms_nesting.md) | successive nesting → 연안 초고해상 (§3.5·Conclusions) |
| [[../../SWAN/web-refs/swan-official-resources]] | COAWST wave 컴포넌트 |

→ 한국 적용 함의: ROMS+SWAN 결합 운영체계의 reference architecture — 반폐쇄해(Adriatic ≈ 일부 한국 연안 만) 다목적 운영 사례로 참조 가능. 단 **한국 직접 적용 사례 아님(미실증)**.

## 6. 정량 근거 소재 (gap 해소 현황)

이 논문은 **review/overview** 성격이라 본문에 관측 대비 정량 skill 이 없다. 소재는 아래와 같고, **핵심 1건은 2026-07-19 해소**:

- ✅ **파랑-해류 결합(WCI) 정량 검증 — 해소**: **Benetazzo et al. (2013) Ocean Modelling 70:152-165** 출판본 전문 확보 → [`roms-coawst-wci-benetazzo-2013.md`](roms-coawst-wci-benetazzo-2013.md) 신설. Acqua Alta·위성 대조 Table 1(Hs RMSD 0.20 m·CC 0.90 등) + 2WC/UNC 차 정량(Bora 0.2 m·계절최대 0.6 m·유속 CC 0.70→0.75). ★귀속 정정도 그 노트에서 확정 — **Warner et al. (2010)(COAWST 원전)·CSTMS 명칭 모두 Benetazzo 2013 에 실제 인용**되어 있음(본 리뷰만 미인용이었던 것).
- ⬜ **video 기반 통합 wave-current-sediment 모델 검증** = **Carniel et al. (2011)** *Oceanological and Hydrobiological Studies* 40(4):11-20 `[source-needed]` — 미확보(§3.5 Bevano 표사 정량).
- ⬜ **EMMA hypoxia 예보 검증** = **Russo et al. (2009)** *Geofizika* 26(2) `[source-needed]` — 미확보(§3.2 생지화학 skill).
- ⬜ THREDDS endpoint(`tds.ve.ismar.cnr.it`)·운영 forecast 현행 여부 = 2013 논문 기준, 현재 운영 상태 별도 확인 필요 `[source-needed]`.
