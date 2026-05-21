---
title: "KHOA 비조화상수 — 한국 공식 정의·공식·부산항 검증"
source_id: dashboard-khoa-data
chapter: "docs/research-nonharmonic-tidal-constants.md (사용자 본인 작성 2026-03-24)"
pages: "전체 (300 lines)"
page_offset_applied: false
topic: tides
canonical_source: self
citation_status: verified
verification_method: "AI cross-reference against /mnt/d/Numerical_models/01_Models/DASHBOARD/docs/research-nonharmonic-tidal-constants.md (사용자 본인 자료). 부산항 KHOA 공식값과 일치 검증 완료된 공식만 인용. 국립해양조사원고시 제2021-7호를 1차 법적 근거로 명시."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref against user's verified research doc"
verification_date: 2026-05-21
---

# KHOA 비조화상수 — 한국 공식 정의

> **법적 근거**: 국립해양조사원고시 **제2021-7호** "해양조사와 관련된 좌표계, 평균해수면, 기본수준면 및 약최고고조면에 관한 사항" (2021.3.31 전부개정). [law.go.kr](https://law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000199750)
>
> 관련 법: **해양조사와 해양정보 활용에 관한 법률** (법률 제21065호).
> 표준: **KCS 64 15 40 해양물리조사** (표준시방서, 일부개정 2023.12.26), **항만 및 해안설계기준** (해양수산부).

## 1. 한국 4대 분조 (Major 4 Constituents)

각속도 정밀값 (`khoa-tide-model` skill.md 9자리, 국립해양조사원고시 제2021-7호 기준. 대시보드 연구의 7자리값과 0.0005°/hr 이하로 일치 — [tides-khoa-cross-verification.md](tides-khoa-cross-verification.md) §2):

| 분조 | 명칭 | 한자 | 유형 | 각속도 (°/hr) | 9·a (KST offset) |
|---|---|---|---|---|---|
| **M₂** | 주태음반일주조 | 主太陰半日週潮 | 반일주조 | **28.984104156** | 260.857° |
| **S₂** | 주태양반일주조 | 主太陽半日週潮 | 반일주조 | **30.000000000** | 270.000° |
| **K₁** | 일월합성일주조 | 日月合成日週潮 | 일주조 | **15.041068639** | 135.370° |
| **O₁** | 주태음일주조 | 主太陰日週潮 | 일주조 | **13.943035584** | 125.487° |

→ Stewart Table 17.2 ([tides-stewart-ch17.md](tides-stewart-ch17.md))의 주기 환산값과 정합:
- M₂: 360 / 28.984104156 = 12.4206 h ✓
- S₂: 360 / 30.000000000 = 12.0000 h ✓
- K₁: 360 / 15.041068639 = 23.9344 h ✓
- O₁: 360 / 13.943035584 = 25.8194 h ✓

**위상 기준** ([변도성 2007] *The Sea* 12(3):234-238): G (Greenwich) / g (135°E KST) / κ (local) 3종. 변환 `g = G + 9·a (mod 360)`. 통합 자료 사용 시 어느 기준인지 반드시 확인 ([tides-khoa-cross-verification.md](tides-khoa-cross-verification.md) §3).

## 2. 한국 기준면 공식 정의

### 2.1 Z₀ — 4대분조 반조차합

```
Z₀ = H_M2 + H_S2 + H_K1 + H_O1
```

여기서 H_n은 각 분조의 진폭(=반조차, amplitude).

### 2.2 약최고고조면 (Approx. HHWL)

```
약최고고조면 = MSL + Z₀
            = MSL + (H_M2 + H_S2 + H_K1 + H_O1)
```

영문: *Approximate Highest High Water Level*.

### 2.3 기본수준면 (DL, Chart Datum)

```
DL = MSL - Z₀
   = MSL - (H_M2 + H_S2 + H_K1 + H_O1)
```

영문: *Datum Level*, *Chart Datum*. 한국 해도 수심 표기 기준.
Darwin의 **Indian Spring Low Water (ISLW)** 방식과 동일.

DL을 0으로 설정하면 MSL = Z₀ (DL 기준).

## 3. 비조화상수 공식 (모두 DL 기준)

대시보드 연구가 **부산항 KHOA 공식값과 정확히 일치**시킨 공식들:

| 비조화상수 | 한국어 | 영문 | 공식 |
|---|---|---|---|
| Z₀ | 4대분조 반조차합 | — | H_M2 + H_S2 + H_K1 + H_O1 |
| MSL | 평균해면 | Mean Sea Level | Z₀ (= DL + Z₀ 즉 DL 기준 Z₀) |
| Approx. HHWL | 약최고고조면 | — | 2 × Z₀ |
| **대조승** | Spring Rise | — | **2·H_M2 + 2·H_S2 + H_K1 + H_O1** |
| **소조승** | Neap Rise | — | **2·H_M2 + H_K1 + H_O1** |
| 평균조차 | Mean Range | — | 2 × H_M2 |
| 대조차 | Spring Range | — | 2 × (H_M2 + H_S2) |
| 소조차 | Neap Range | — | 2 × (H_M2 - H_S2) |
| 평균고조간격(g) | Mean High Water Interval (Greenwich) | HWI(g) | g_M2 / 28.9841042 (시간) |
| 평균고조간격(κ) | Mean High Water Interval (local) | HWI(κ) | κ_M2 / 28.9841042 (시간) |

> **"조승" ≠ "조차" — Critical**
> - 대조승 = DL 기준 대조시 고조위 **높이** (m above DL)
> - 대조차 = 대조시 고조-저조 **차이** (m, range)

## 4. 부산항 검증 (대시보드 연구 §3)

> **출처 명시**: H_M2=40 cm는 **KHOA 부산항 조석표 공시값** (단일 정점, 정확 obs_code 미확인). DT_0005 (부산, 38.23 cm), 다대포항 (493-01, 42.6 cm), 가덕도 (467-01, 56.7 cm) 등 sub-station 값과는 정점 정의 차이 ([tides-khoa-cross-verification.md](tides-khoa-cross-verification.md) §4).

부산항 4대분조 조화상수 (KHOA 조석표 공시):

```
H_M2 = 40.0 cm
H_S2 = 18.9 cm
H_K1 =  4.4 cm
H_O1 =  1.6 cm
g_M2 = 235.6° (Greenwich epoch)
κ_M2 = 232.8° (local epoch)
```

공식 적용:

| 비조화상수 | 계산 | 결과 | KHOA 공식값 | 일치 |
|---|---|---|---|---|
| Z₀ | 40 + 18.9 + 4.4 + 1.6 | 64.9 cm | — | — |
| MSL | Z₀ | 64.9 cm | 64.9 cm | ✓ |
| 약최고고조면 | 2 × 64.9 | 129.8 cm | 129.8 cm | ✓ |
| 대조승 | 2·40 + 2·18.9 + 4.4 + 1.6 | 123.8 cm | 123.8 cm | ✓ |
| 소조승 | 2·40 + 4.4 + 1.6 | 86.0 cm | 86.0 cm | ✓ |
| 대조차 | 2·(40+18.9) | 117.8 cm | — | — |
| 소조차 | 2·(40-18.9) | 42.2 cm | — | — |
| HWI(g) | 235.6° / 28.984104156 = 8.129 h | **8h 07m** | 8h 07m | ✓ |
| HWI(κ) | 232.8° / 28.984104156 = 8.031 h | **8h 01m** | 8h 02m | ≈ (반올림) |

> KHOA는 분 계산 시 **floor(내림)** 적용으로 보임 — HWI(κ) 케이스에서 0.86분 차이 발생 (반올림 vs 내림).

### 4.1 조석 형태 계수 (Form Factor) — 부산

```
F = (H_K1 + H_O1) / (H_M2 + H_S2)
  = (4.4 + 1.6) / (40 + 18.9)
  = 6.0 / 58.9 = 0.102
```

F < 0.25 → **반일주조형**. 부산은 반일주조 우세.

분류 기준 (NOAA 등 일반 통용):
- F < 0.25: 반일주조 (semidiurnal)
- 0.25 ≤ F < 1.5: 혼합조 (mainly semidiurnal)
- 1.5 ≤ F < 3.0: 혼합조 (mainly diurnal)
- F ≥ 3.0: 일주조 (diurnal)

## 5. 데이터 소스

### 5.1 KHOA OpenAPI 엔드포인트 (대시보드 §5 인용)

| API | 엔드포인트 | 내용 |
|---|---|---|
| 조화상수 | `/api/oceangrid/tideObsHarmo/search.do` | 조위관측소별 조화상수 (반조차, 지각) |
| 실측조위 | `/api/oceangrid/tideObsReal/search.do` | 실시간 관측 조위 |
| 예측조위 | `/api/oceangrid/tideObsPre/search.do` | 조석 예측값 |
| 조석예보 | `/api/oceangrid/tideObsPreTab/search.do` | 고저조 시각/높이 |

**중요**: KHOA OpenAPI는 **조화상수만 제공**. 비조화상수는 **위 공식으로 계산 필요**.

### 5.2 API 키 체계 주의

- **khoa.go.kr** 키 (바다누리 전용)
- **data.go.kr** 키 (공공데이터포털)
- **두 키는 비호환** — 사용처에 맞게 선택

## 6. JavaScript 구현 (대시보드 §7.1 인용)

```javascript
function calculateNonHarmonicConstants(harmonics) {
    // harmonics: { M2: {H, kappa, g}, S2: {H, kappa, g}, K1: {H, kappa, g}, O1: {H, kappa, g} }
    const HM2 = harmonics.M2.H;
    const HS2 = harmonics.S2.H;
    const HK1 = harmonics.K1.H;
    const HO1 = harmonics.O1.H;

    const Z0 = HM2 + HS2 + HK1 + HO1;

    return {
        MSL: Z0,                           // 평균해면 (DL 기준)
        HHWL: 2 * Z0,                      // 약최고고조면 (DL 기준)
        DL: 0,                             // 기본수준면 (기준)
        springRise: Z0 + HM2 + HS2,        // 대조승 (DL 기준)
        neapRise: Z0 + HM2 - HS2,          // 소조승 (DL 기준)
        springRange: 2 * (HM2 + HS2),
        neapRange: 2 * (HM2 - HS2),
        meanRange: 2 * HM2,
        HWI_kappa: harmonics.M2.kappa / 28.9841042,  // 시간 (분은 floor)
        HWI_g: harmonics.M2.g / 28.9841042,
        formFactor: (HK1 + HO1) / (HM2 + HS2)
    };
}
```

## 7. 인천 (DT_0001) 조화상수 발췌 — 사용 예제용

대시보드 데이터 (data/조석/조위관측소_조화상수.csv):

| 분조 | 진폭 (cm) | 위상 GMT (°) | 위상 KST (°) |
|---|---|---|---|
| **M₂** | 284.525 | 228.79 | 129.79 |
| **S₂** | 114.625 | 276.91 | 186.91 |
| **K₁** | 38.914 | 168.05 | 303.05 |
| **O₁** | 28.712 | 138.69 | 263.69 |
| N₂ | 53.327 | 214.10 | 110.10 |
| K₂ | 30.863 | 269.97 | 180.97 |
| P₁ | 11.534 | 161.75 | 296.75 |
| **M₄** (천해) | 6.294 | 329.51 | 131.51 |
| **MS₄** (천해) | 6.093 | 23.63 | 194.63 |
| M₆ (천해) | 3.052 | 5.49 | 68.49 |
| 2Q₁ | 0.578 | 254.14 | 10.14 |
| 2MK₆ | 0.924 | 46.08 | 118.08 |

(CSV에 같은 row가 2번 중복 등장 — 추후 dedup 권장. wiki 인용 시 1회만.)

### 인천 비조화상수 계산 (위 데이터 적용)

```
H_M2 = 284.525 cm, H_S2 = 114.625 cm, H_K1 = 38.914 cm, H_O1 = 28.712 cm

Z₀ = 284.525 + 114.625 + 38.914 + 28.712 = 466.776 cm ≈ 4.67 m
MSL = Z₀ = 466.776 cm (DL 기준)
약최고고조면 = 2 × Z₀ = 933.552 cm ≈ 9.34 m (DL 기준)
대조승 = 2·H_M2 + 2·H_S2 + H_K1 + H_O1
       = 569.05 + 229.25 + 38.914 + 28.712
       = 865.926 cm ≈ 8.66 m
소조승 = 2·H_M2 + H_K1 + H_O1
       = 569.05 + 38.914 + 28.712
       = 636.676 cm ≈ 6.37 m
대조차 = 2·(H_M2 + H_S2) = 798.300 cm ≈ 7.98 m
소조차 = 2·(H_M2 - H_S2) = 339.800 cm ≈ 3.40 m
F (form) = (38.914 + 28.712) / (284.525 + 114.625)
        = 67.626 / 399.150 = 0.169 → 반일주조형
HWI(g) = 228.79° / 28.9841 = 7.894 h → 7h 53m
```

**인천 조차 약 8 m는 한국 서해 typical 값**과 정합 (`tides-lubbad2009-overview.md` §3에서 인용된 한국 서해 5-9 m 범위 ✓).

### 인천 비선형 조석 강도

천해 분조 비율 (vs M₂):
- M₄ / M₂ = 6.294 / 284.525 = 2.21 %
- MS₄ / M₂ = 6.093 / 284.525 = 2.14 %
- M₆ / M₂ = 3.052 / 284.525 = 1.07 %

→ 서해 천해 비선형 effect 명확히 관측. 모델링 시 천해 분조 입력 필수.

## 8. 외부 참고문헌 (대시보드 §8 인용)

1. 국립해양조사원고시 제2021-7호 (2021.3.31): [law.go.kr](https://law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000199750)
2. 해양조사와 해양정보 활용에 관한 법률 (법률 제21065호): [law.go.kr](https://law.go.kr/LSW/lsInfoP.do?lsiSeq=277099)
3. NOAA Tides and Currents Glossary: [tidesandcurrents.noaa.gov/glossary](https://tidesandcurrents.noaa.gov/glossary.html)
4. NOAA, "Computational Techniques for Tidal Datums Handbook": [tidesandcurrents.noaa.gov](https://tidesandcurrents.noaa.gov/publications/Computational_Techniques_for_Tidal_Datums_handbook.pdf)
5. KCS 64 15 40 해양물리조사 (표준시방서, 일부개정 2023.12.26)
6. 정민·박영기, 『기초해안공학』, 구미서관 — Schureman(1940) 기준
7. KHOA 바다누리 OpenAPI 문서: [khoa.go.kr](https://www.khoa.go.kr/oceangrid/khoa/takepart/openapi/openApiObsTideHarDataInfo.do)
8. 항만 및 해안설계기준 (해양수산부)

## 9. 연결

- `concepts/tides/02-theory.md` §7-8 — 비조화상수·기준면 (본 노트가 1차 근거)
- `concepts/tides/03-analysis-methods.md` §4 — 산출 공식 (본 노트 §3·§4 인용)
- `concepts/tides/05-examples.md` §3 — 한국 KHOA template (인천 §7 데이터 활용)
- `concepts/tides/06-model-application.md` — 모델 datum 설정 시 DL/Z₀ 일치 확인
