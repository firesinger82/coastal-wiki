---
title: "조석 — 06 모델 적용 (EFDC / ADCIRC / XBeach / Delft3D)"
topic: tides
canonical_source: self
citation_status: source-needed
verification_method: "AI cross-reference. 본 문서는 **요약 + 링크 중심** (canonical source 분리 규칙 [CONVENTIONS.md §3]). 각 모델의 구현 디테일은 `models/<model>/source-analysis/`·`manual-notes/`가 진실의 원천이며 현재 stub 상태 — 본 문서의 모델별 §은 그 채워짐에 따라 source-needed → verified 승격."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: ""
verification_date: ""
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

> **Canonical source**: [`models/EFDC/`](../../models/EFDC/) (현재 stub)
>
> 본 §은 작성 우선순위 안내. 채워질 위치 명시.

### 2.1 입력 파일

EFDC의 조석 forcing 관련 입력 (정식 정의는 `models/EFDC/manual-notes/`에서):

- `efdc.inp` — 메인 input. 조석 관련 카드:
  - `BCHARM` (open boundary harmonic flag)
  - `NOBCS` (open boundary segment count)
- `pser.inp` — 시계열 forcing 파일 (시간-수위 pair)
- `aser.inp` / `qser.inp` — 풍·유량 강제 (조석과 별개지만 같은 boundary에 합성 가능)

→ 정확한 입력 카드·포맷은 [`models/EFDC/manual-notes/`](../../models/EFDC/manual-notes/) 작성 후 인용 (현재 미작성, **source-needed**).

### 2.2 분조 입력 형식 (개념)

EFDC는 통상 다음 정보를 외해 경계 각 셀에 입력:
- 분조 수 (예: M₂·S₂·K₁·O₁의 4개 또는 더 많음)
- 각 분조별 주파수 (cycles/hour, [Foreman 1977 appendix](../../textbook/notes/tides-foreman1977-appendix.md) 표준 값)
- 각 분조별 (진폭 m, 위상 °) — 각 경계 셀별

→ 구체 포맷은 [`models/EFDC/source-analysis/`](../../models/EFDC/source-analysis/) 의 boundary handling 서브루틴 분석 후 (현재 미작성, **source-needed**).

### 2.3 EFDC 관련 textbook 자료

- `textbook/sources.yml`에 두 출처 등록:
  - `efdc-general` — `692624517-EFDC.pdf` (48 KB, 요약·index 추정)
  - `efdc-sed-trans-2003` — `86899804-EFDC-Theory-Tech-Aspects-of-Sed-Trans-2003-05.pdf`

EFDC 조석 부분 노트는 `textbook/notes/efdc-tides-*.md`로 추출 (미작성).

## 3. ADCIRC

> **Canonical source**: [`models/ADCIRC/`](../../models/ADCIRC/) (현재 stub)

### 3.1 입력 파일

- `fort.15` — 메인 control file. 조석 관련:
  - `NTIP` (tidal potential flag — 평형 조석 potential 적용 여부, `02-theory.md` §2)
  - `NWS` (wind/atmospheric forcing flag)
  - `NBFR` (open boundary 분조 수)
  - 각 분조별 amplitude·equilibrium argument
- `fort.14` — mesh (unstructured triangular)

→ 정확한 사양은 [`models/ADCIRC/manual-notes/`](../../models/ADCIRC/manual-notes/) (현재 미작성, **source-needed**).

### 3.2 ADCIRC Tidal Database

ADCIRC 자체 tidal database (LeProvost·FES 류 기반) 제공 — `aetide` 도구 등으로 임의 mesh 경계에 분조 보간 가능.

→ 상세는 `models/ADCIRC/web-refs/adcirc-tidal-database.md` (미작성).

## 4. XBeach

> **Canonical source**: [`models/XBeach/`](../../models/XBeach/) (현재 stub)

XBeach는 **단기 폭풍 시뮬레이션** 위주 (수일~수주). 조석 forcing은:
- 짧은 시뮬 기간 내 수위 변화로 적용
- 분조 forcing보다 시계열 forcing이 일반적

입력 파일: `params.txt` (메인) + `tide.txt` (수위 시계열). 자세한 사양은 [`models/XBeach/manual-notes/`](../../models/XBeach/manual-notes/) (미작성).

## 5. Delft3D

> **Canonical source**: [`models/Delft3D/`](../../models/Delft3D/) (현재 stub)

### 5.1 D3D-4 FLOW

- 입력 파일: `.bnd`, `.bca` (boundary, harmonic constituents)
- 분조 forcing 직접 지원 — 각 경계점별 분조 진폭·위상

### 5.2 Delft3D FM (Flexible Mesh)

- D-Flow FM: unstructured mesh, ADCIRC와 유사한 mesh 기반
- 입력 파일: `.bnd`, `.ext`, `.bc` — 더 유연한 boundary 정의

→ D3D-4 vs FM 차이 + 정확한 파일 포맷은 [`models/Delft3D/manual-notes/`](../../models/Delft3D/manual-notes/) (미작성).

## 6. 모델 간 비교 — 조석 적용 관점

| 항목 | EFDC | ADCIRC | XBeach | Delft3D |
|---|---|---|---|---|
| 격자 | curvilinear orthogonal | unstructured triangular | 직교/곡선 | 구조 (D3D-4) 또는 비구조 (FM) |
| 조석 입력 형식 | 분조 + 시계열 양쪽 | 분조 (NBFR) + 평형 조석 (NTIP) | 시계열 위주 | 분조 + 시계열 양쪽 |
| 사용 typical 분조 수 | 4-8 (M₂·S₂·K₁·O₁ + 보조) | 6-37 (database 지원) | 1-4 (단기) | 4-37 |
| 비선형 천해 분조 | 자체 생성 (격자 잘 잡으면) | 자체 생성 | n/a (입력만 받음) | 자체 생성 |
| 한국 서해 적합도 | 양호 (사용자 주력) | 양호 | 폭풍 케이스만 | 양호 |

> 비교 표의 각 항목은 **공식 메뉴얼 기반만** — 현재는 일반론. 정확 사양은 각 `models/<model>/manual-notes/` 작성 후 정밀화. **개인 사용 경험은 `experience/`로** (CONVENTIONS.md §6).

## 7. 다른 토픽과의 교차

조석은 단독 적용이 드물고 다음과 결합:

- **폭풍해일** (`concepts/storm-surge/`, 미작성) — 조석 + 해일 superposition
- **표사이동** (`concepts/sediment-transport/`, 미작성) — 창조류·낙조류 비대칭이 표사이동 방향 결정
- **하구 염분** — 조석 mixing이 estuarine circulation 좌우
- **항만 자연 공명** — 조석 주기가 항만 resonance와 일치할 때 amplitude 증폭

각 결합은 해당 토픽 작성 시 본 06으로 cross-link.

## 8. 보강 필요

본 문서가 `verified`로 가려면:

- [ ] `models/EFDC/manual-notes/` 작성 → §2 정확한 입력 카드 인용
- [ ] `models/EFDC/source-analysis/` 작성 → boundary handling 서브루틴 분석
- [ ] `models/ADCIRC/manual-notes/` 작성 → `fort.15` NTIP·NBFR 정확한 사양
- [ ] `models/ADCIRC/web-refs/` — ADCIRC tidal database 사용법
- [ ] `models/XBeach/manual-notes/` — `tide.txt` 포맷
- [ ] `models/Delft3D/manual-notes/` — `.bnd`/`.bca` 정확 사양 (D3D-4 + FM 양쪽)
- [ ] §6 모델 간 비교 표의 각 항목 출처 인용 (공식 메뉴얼 페이지)
- [ ] `textbook/notes/efdc-tides-*.md` — EFDC 메뉴얼 조석 부분 발췌

## 9. 연결

- `01-concept.md` ~ `04-code-and-tools.md` — 도메인 지식 (verified)
- `05-examples.md` — 조화상수 산출 → 본 페이지의 forcing 입력에 활용
- 모델별 객관 자료 (canonical sources):
  - [`models/EFDC/`](../../models/EFDC/) (stub)
  - [`models/ADCIRC/`](../../models/ADCIRC/) (stub)
  - [`models/XBeach/`](../../models/XBeach/) (stub)
  - [`models/Delft3D/`](../../models/Delft3D/) (stub)
- 글로벌 조석 모델 (`04-code-and-tools.md` §6):
  - TPXO, FES, NAO, GOT — 본 페이지의 forcing 데이터 원천
- 사용자 경험 (검증 통과 시):
  - `experience/efdc-tidal-forcing-*.md` (미작성, 3조건 통과 시) — EFDC 실제 사용 패턴
