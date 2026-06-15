---
title: "표사이동 — 04 코드와 도구 (EFDC SED · Delft3D-SED · CSTMS · XBeach SED)"
topic: sediment-transport
canonical_source: self
citation_status: verified
verification_method: "AI cross-reference: textbook 자료 + WebSearch 공식 모델 페이지 + Soulsby 1997 implementation guidance."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 표사이동 — 04 코드와 도구

## 1. 모델 비교

| 모델 | 종류 | 라이선스 | 표사 모듈 | 사용자 익숙도 |
|---|---|---|---|---|
| **EFDC SED** | hydrodynamic + sediment (3D) | open source (DSI, USEPA 등) | 자체 모듈 | **사용자 주력** ([축산항] 등) |
| **Delft3D-SED** | hydrodynamic + sediment | GPL-3.0 | D3D-4 또는 FM | 표준 (Deltares) |
| **MIKE 21/3 ST** | 상용 | 상용 (DHI) | ST = Sediment Transport | 한국 항만 설계 |
| **XBeach sedtrans** | 폭풍 침식 | GPL-3.0 | non-cohesive · 비점착성 | 폭풍 시뮬 |
| **CSTMS / COAWST** | combined ocean·atm·wave·sed | open source | ROMS + SWAN + CSTMS | 학술 |
| **TELEMAC-SISYPHE** | unstructured | open source (EDF) | SISYPHE = sediment | 유럽 표준 |

## 2. EFDC SED (사용자 주력)

> **Canonical**: [`models/EFDC/`](../../models/EFDC/) (현재 stub) + `efdc-sed-trans-2003` source (`textbook/md/86899804-EFDC-Theory-Tech-Aspects-of-Sed-Trans-2003-05.md`).

### 2.1 EFDC 표사이동 이론 — Tech Aspects (2003)

본 PDF는 EFDC의 표사이동 구현 이론서. 핵심:
- **Multi-class** sediment (비점착성 + 점착성 동시)
- **Bedload + Suspended** 양쪽 추적
- 자체 **bed layer** 다층 추적 (수직 격자 + bed 다층)
- Rouse profile (`02-theory.md` §3) 기반 부유 농도 평형

### 2.2 입력 카드 (EFDC)

- `efdc.inp`:
  - `NSED` (cohesive 점착성 sediment class 수)
  - `NSND` (non-cohesive sand class 수)
  - `RSED1NS` (각 class의 초기 부유 농도)
  - `SDEN(NS)` (각 class 입경)
  - `TAUR`, `TAUC` (재부유 임계, 침전 임계)
  - `RKTR`, `RKAGG` (재부유 속도, aggregation 속도 점착성)
- `aser.inp` / `wser.inp`: 외력 시계열
- `bed_layer.inp`: 초기 bed 다층 구성

→ 정확한 카드는 [`models/EFDC/manual-notes/`](../../models/EFDC/manual-notes/) (작성 예정).

### 2.3 출력

- 각 sediment class 부유 농도 (mg/L) 3D 격자
- Bed 표고 변화 (m) 시계열
- Bed 입자 분포 변화 (multi-layer)
- 침전·재부유 flux

### 2.4 한국 EFDC 사용자 사례 (`축산항` 등)

사용자는 `D:\Projects\축산항\` 등에서 EFDC 운용. SED 모듈 적용 사례:
- 축산항 침퇴적 변화 (15년 누적, 약 -22 cm 침식 또는 +22 cm 퇴적, [memory 1215] 참조)
- 모델 → idealized 결과 → 보고서

→ 실제 운용 사례는 `experience/` 또는 [`models/EFDC/source-analysis/`](../../models/EFDC/source-analysis/) (작성 검토).

## 3. Delft3D-SED

### 3.1 D3D-4 SED

- FLOW + SED 모듈 연결
- 입력 파일: `.mor`, `.sed` (sediment fraction, bed composition)
- non-cohesive: van Rijn (1984·2007) + bedload 별도
- cohesive: Partheniades-Krone (재부유) + settling

### 3.2 Delft3D FM (Flexible Mesh)

- D-Morphology 모듈
- Sand + mud transport 통합

→ [`models/Delft3D/`](../../models/Delft3D/) (stub).

## 4. CSTMS / COAWST

- Community Sediment Transport Modeling System
- ROMS (ocean) + SWAN (wave) + CSTMS (sediment) coupling
- 공식 GitHub: [https://github.com/DOI-USGS/COAWST](https://github.com/DOI-USGS/COAWST) (확인 필요)

## 5. XBeach Sediment

### 5.1 모드

- `morphology = 1`: bed update 활성
- Bedload (Soulsby-van Rijn 식)
- Suspended (advection-diffusion + settling)
- Avalanching (사구 붕괴 dune front)

### 5.2 적용

- 폭풍 침식·붕괴 시뮬 (수일 단위)
- Beach-dune system: erosion·breaching
- 한국 적용 사례 (서해 폭풍 침식): 별도 보강

## 6. MIKE 21 ST (상용)

- DHI MIKE Powered 의 sediment 모듈
- 비점착성 + 점착성 통합
- 한국 항만 설계 (성남구·해양수산부) 사용 빈도 높음 — 상용 라이선스
- 별도 보강

## 7. Python 도구

| 도구 | 기능 | 출처 |
|---|---|---|
| **pyplosa** | sediment grain size analysis | GitHub (확인) |
| Soulsby formulae (NumPy) | `02-theory.md`·`03-analysis-methods.md` 식 직접 구현 | 자체 |
| scikit-image (수직 단면 분석) | side-scan image 처리 | open |

## 8. 도구 선택 가이드

| 상황 | 권장 |
|---|---|
| 한국 EFDC 시뮬 (사용자 주력) | **EFDC SED** + manual + `efdc-sed-trans-2003` |
| 단순 항만 (단기 설계) | **MIKE 21 ST** 또는 **Delft3D-SED** |
| 폭풍 침식 시뮬 | **XBeach** sediment + morphology |
| 학술 ocean-atm-wave-sed coupling | **CSTMS / COAWST** |
| 평형 단면 검토 (Dean profile) | 수동 (`02-theory.md` §5 식) |
| 정점별 d_{50} 분석 | scipy, scikit (sieve curve fit) |

## 9. 사용자 SWAN-EFDC coupling

`swan-library-firesinger` ↔ EFDC SED:
- SWAN 출력 (radiation stress, H_s, T_p) → EFDC SED 입력 (wave forcing)
- 한국 KHOA 수치조류도 (`tides-khoa-cross-verification.md` §5) → EFDC 외해 흐름 boundary
- 둘 조합 시 천해 비선형 모드 활성

## 10. 보강

- EFDC 표사이동 source-code (`models/EFDC/source-analysis/sediment.md`) 발췌
- Delft3D-SED 입력 카드 정리
- CSTMS Python interface
- 사용자 축산항 EFDC SED 실제 input·output 사례 → `experience/`

### 10.1 연구 문헌 (research/inbox promote, source-needed)

- **Green-Naghdi DG morphodynamics (Kazhyken·Videman·Dawson 2020)** — arxiv:[2005.00920](https://arxiv.org/abs/2005.00920). Green-Naghdi(분산파 hydrodynamic) + Exner(bed-load morphodynamic) 결합을 discontinuous Galerkin FEM 으로 해석. Strang operator splitting 으로 분산항 분리(surf zone 등 특정영역 무시 가능) + wetting-drying + 쇄파 감지. swash zone 까지 분산효과 해상. coupled/decoupled 두 접근.
- **Green-Naghdi DG hydro-sediment-morphodynamics (Kazhyken·Videman·Dawson 2020)** — arxiv:[2010.06167](https://arxiv.org/abs/2010.06167). 위 확장 — SHSM(shallow water hydro-sediment-morphodynamic) + Green-Naghdi 분산보정. suspended + bed load 경험식 보정 시 표사·bed morphodynamic 예측. (※ Dawson = ADCIRC 핵심 개발자 — [`models/ADCIRC/`](../../models/ADCIRC/))
- **Bedform DMD system ID (Mustavee·Singh·Agarwal 2026)** — arxiv:[2603.27604](https://arxiv.org/abs/2603.27604). **하천** bedform 이동 kinematics 로부터 sediment flux 간접추정 — Dynamic Mode Decomposition + Exner 식 결합 → scale-dependent flux surrogate. (하천 대상이나 bedform→flux 추론 기법 연안 전이가치)
- **Copula 민감도분석 — Delft3D-WAQ (Tene·Stuparu·Kurowicka·El Serafy 2018)** — arxiv:[1804.04541](https://arxiv.org/abs/1804.04541). Morris(1991) 민감도법을 **copula** 로 확장(파라미터 의존성 처리). **Delft3D-WAQ 북해 표사이동 모델**(Deltares)에 적용 — 강한 입력 상관 하 classic Morris 보다 물리 일관성 우수. [`models/Delft3D/`](../../models/Delft3D/) + §3 Delft3D-SED 접점.
- citation_status: 위 4건 모두 source-needed (abstract 기반 — full PDF read 시 정량·검증 보강)

## 11. 연결

- `01`-`03` — 도메인 지식
- `05-examples.md` — 한국 사례 (작성 예정)
- `06-model-application.md` — 모델 적용 워크플로
- 외부:
  - **EFDC**: [https://www.epa.gov/exposure-assessment-models/efdc](https://www.epa.gov/exposure-assessment-models/efdc)
  - **Delft3D**: [https://oss.deltares.nl/web/delft3d](https://oss.deltares.nl/web/delft3d)
  - **XBeach**: [https://xbeach.readthedocs.io/](https://xbeach.readthedocs.io/)
  - **COAWST**: NOAA/USGS open source
