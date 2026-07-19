---
title: "ROMS+Fennel 저산소 예보 운영검증 — EMMA 시스템 (Russo et al. 2009)"
topic: roms-web-refs
canonical_source: self
citation_status: verified
has_source_needed: false
verification_method: "Russo A., Coluccelli A., Iermano I., Falcieri F., Ravaioli M., Bortoluzzi G., Focaccia P., Stanghellini C.R., Ferrari J., Chiggiato J., Deserti M. (2009) 'An operational system for forecasting hypoxic events in the northern Adriatic Sea', Geofizika 26(2):191-213 — **출판본 PDF 전문 직접 read (2026-07-19, pdftotext -layout)**. 관측계 §2.1(p.196-197)·수치설정 §2.2(p.197-199)·검증 §3(p.199-205)·MSE 분해식(p.204)·한계 §4(p.205-207) 페이지 단위 인용. RMSE/CC 수치는 본문 서술값 직접 전사."
note_author: "Claude Fable 5"
note_date: 2026-07-19
verification_by: "Claude Fable 5 — 출판본 PDF 직독"
verification_date: 2026-07-19
related:
  - models/ROMS/web-refs/roms-coawst-adriatic-applications.md
  - models/ROMS/source-analysis/roms_biology.md
  - models/ROMS/web-refs/roms-official-resources.md
---

# ROMS+Fennel 저산소 예보 운영검증 — EMMA 시스템

> [`roms-coawst-adriatic-applications.md`](roms-coawst-adriatic-applications.md) §3.2 가 언급한 EMMA 운영 구현의 **검증 원전**. ROMS 생지화학 모듈 메커닉은 [`source-analysis/roms_biology.md`](../source-analysis/roms_biology.md) 가 canonical, 본 노트는 운영 skill 맥락.

## 1. 출처

| 항목 | 값 |
|---|---|
| 제목 | "An operational system for forecasting hypoxic events in the northern Adriatic Sea" |
| 저자 | A. Russo 외 10인 (Univ. Politecnica delle Marche · ISMAR-CNR · ARPA-EMR) |
| 게재 | *Geofizika* **26**(2), 191–213 (2009) |

★**희소 가치**: 연안 생지화학 모델의 **운영 예보 skill 을 2년 연속 부이 관측과 대조한 공개 문헌** — surrogate·데이터동화 이전 세대의 정직한 baseline.

## 2. 수치 구성 (§2.2, p.197-199)

| 항목 | 값 |
|---|---|
| 코어 | ROMS — primitive equation·유한차분·**정수압**·자유수면·지형추종 s-좌표·Arakawa C·split-explicit predictor/corrector |
| 격자 | 직교곡선, **전 도메인 등간격 2 km**, **연직 20 s-level**(표층·저층 경계층 해상 위해 stretch) |
| 이류 | 재귀 **MPDATA**(Margolin & Smolarkiewicz 1998). 수평확산=격자의존 약한 Laplacian, **수평점성 미부가** |
| 압력경사 | density Jacobian + 3차 다항식 적합(Shchepetkin & McWilliams 2003) |
| 연직혼합 | ★**Mellor-Yamada level 2.5**(MY2.5) — 같은 Adriatic 계열이라도 Benetazzo 2013(GLS k-ε)과 **다른 closure** 채택 |
| 조석 | 남측 개방경계(Otranto) **4 분조 M2·S2·K1·O1**, 지중해 FEM 모델(Cushman-Roisin & Naimie 2002). Flather(2D 운동량)+Chapman(조위), baroclinic=radiation(Marchesiello 2001) |
| 하천 | **48 하천·카르스트 용천**(Po 일자료, 그 외 Raicich 1994 월 climatology) + ★**Emilia Romagna 연안 13 추가 소스**(하계 관광객 도시배출 영양염 모사) |
| 대기 | COARE 3.0 bulk flux(Fairall 2003), SST 는 ROMS 자체 산출. **COSMO-I7 7 km**, 시간별, 72 h 예보, 1일 2회(00·12 UTC) |
| 생지화학 | **Fennel 모듈**(Fennel et al. 2006, Fasham 1990 변형; ROMS v3.2 부터 명칭) — 질산·암모늄 분리 상태변수, 클로로필 예측변수, 식·동물플랑크톤, **detritus 2 크기군**(Sdet<10 mm, Ldet=Sdet+Phyt), 무기탄소·용존산소, 탈질·퇴적물 재광물화 |
| ★저층 산소 보정 | Fennel 저층 과정 단순화 한계 보완 위해 **음의 상수 플럭스 0.115 mmol m⁻² s⁻¹** 인위 부가(문헌 Moodley 1998 + 민감도 실험 유래) — 즉 **모델 단독으로 저층 산소소비를 못 맞춰 튜닝항을 넣은 구성** |
| 운영 | Ancona 소재 Marche 공대 운영. 매일 COSMO-I7·Po 유량 자동 수신 → 72 h 예보. 전일 run 의 restart 로 초기화. ★**Po 유량 예보는 비운영** — run 중 현재값 고정 |

관측계(§2.1, p.196): **E1 부이** — Rimini 외해 약 6 km, 수심 10.5 m, 2006-08-09 설치. 1.6 m(표층)·8.4~8.8 m(저층) 2단 센서, 저층에 **SBE 43 용존산소** + Aanderaa DCS-3900 단일점 유속계. 15~30분 기록. 보조 = 2007-05 CTD 123 정점 항해(초기장), ARPA-Daphne 정기 monitoring(독립 검증셋).

## 3. ★운영 예보 검증 (§3, p.199-205) — E1 부이 2년(2007-06 ~ 2009-05)

| 변수 | 층 | RMSE (평균) | 계절 범위 | CC |
|---|---|---:|---|---:|
| **수온** | 표층 1.6 m | **0.90 °C** | 여름 0.65 ~ 겨울 1.02 | **0.993** |
| **수온** | 저층 8.8 m | **1.77 °C** | 가을 0.98 ~ 봄 2.10 | **0.976** |
| **염분** | 표층 | **2.21** | 여름 1.34 ~ 가을 2.55 | 0.733 |
| **염분** | 저층 | **1.55** | 봄 1.22 ~ 겨울 1.79 | **0.554** |
| **연안방향 유속** | 저층 | **≈0.1 m/s** | 2008-07 만 2배 | (bias ≈ −0.05 m/s 상시) |
| **용존산소** | 저층 | **1.67 mL/L** | 봄 1.34 ~ 가을 1.92 | 0.730 |

★**성능 서열이 뚜렷**: 수온(CC 0.99) ≫ 염분·용존산소(CC 0.73) > 저층염분(CC 0.55). 저자 판정(§4 p.206) — "수온은 good, **염분·용존산소는 그만큼 강하지 않다(not as strong)**".

### 3.1 ★MSE 분해 — 오차의 정체는 편차(bias) (p.204, Fig.6)

Murphy(1992)·Oke et al.(2002) 방식(ROMS skill 평가 관례, Wilkin et al. 2006):

```
MSE = ⟨(m_i − o_i)²⟩
MB  = ⟨m⟩ − ⟨o⟩                        (평균편차)
SDE = S_m − S_o                        (표준편차 오차 = 진폭오차)
CC  = S_m⁻¹ S_o⁻¹ ⟨(m_i−⟨m⟩)(o_i−⟨o⟩)⟩
RMSE² = MB² + SDE² + 2 S_m⁻¹ S_o⁻¹ (1−CC)
```

용존산소 월별 RMSE 는 **MB(평균편차)가 지배**. SDE(진phase 진폭오차)는 작아 — **변동성 자체는 옳게 재현**되었고, 늦겨울~초봄만 모델 변동폭이 관측보다 작음. 월별 CC 는 낮고 **2007-08·09·12 는 음수**.

→ 저자 결론(§4 p.207): "용존산소 RMSE 대부분이 MB 에서 왔다 = **과정의 변동은 옳게 모사됐고, 편차는 보정으로 줄일 수 있다**". 실제로 초록(p.191)이 **10일 평균 편차 제거만으로 예보가 개선**됨을 명시.

### 3.2 독립 검증 — ARPA-Daphne 전선 (p.205, Fig.7)

E1 부이 남북 2개 전선, 연안에서 **3·6·10 km** 정점(314/319·614/619·1014/1019), 2007-06~09. 관측·모델 모두 **연안→외해로 갈수록 변동성 감소**하는 동일 거동. ★**예보 정확도는 외해 정점에서 더 좋음** — 천해 연안일수록 어려움.

## 4. 알려진 한계 (저자 명시)

- **생지화학 모듈 단순화**가 용존산소 약세의 주원인(§4 p.206). 저층 산소소비는 상수 플럭스로 대체(§2.2).
- **2 km 격자 vs 연안 6 km 부이**(p.207): E1 은 Po·지역 하천 runoff 영향권 — 2 km 해상도로 연안 담수 구조를 못 잡는 한계 지적.
- **부이 오염(biofouling)** 2건이 관측 자체를 훼손: 2008-07 유속(모델엔 이상 없음 — ★관측 쪽 오류로 판정)·2008-07 용존산소 센서.
- Po 유량 예보 부재 → run 중 상수 고정(§2.2).

## 5. 본 위키 접점

| 본 위키 자료 | 접점 |
|---|---|
| [`roms-coawst-adriatic-applications.md`](roms-coawst-adriatic-applications.md) | 리뷰 §3.2 EMMA 운영구현의 정량 근거 |
| [`source-analysis/roms_biology.md`](../source-analysis/roms_biology.md) | Fennel 모듈 코드 메커닉 ↔ 본 노트 운영 skill |
| [`roms-coawst-wci-benetazzo-2013.md`](roms-coawst-wci-benetazzo-2013.md) | 동일 해역·동일 2 km 부모격자 계열, ★연직혼합 closure 는 상이(MY2.5 vs GLS) |

→ **한국 적용 함의**: 연안 생지화학 운영예보의 현실적 기대치 — 수온은 CC 0.99 로 신뢰 가능하나 **용존산소는 CC 0.7 대·RMSE 1.7 mL/L 수준이 2009년 시점 최선**이며, 오차 대부분이 편차이므로 **사후 bias 보정이 실효적 개선수단**. 저층 산소소비를 상수 플럭스로 대체해야 했다는 점은 국내 적용 시에도 동일 제약으로 예상(미실증).
