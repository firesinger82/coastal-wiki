---
title: "KHOA 조위관측 → 폭풍해일 극치분석(EVA) 파이프라인 — 100년 설계 재현값 재현 절차"
canonical_source: self
citation_status: verified
verification_method: "본 위키 내 cross-reference 기반 절차 문서. 방법론 출처: concepts/storm-surge/03-analysis-methods.md (Pugh tide-surge separation §1·annual maxima ranking §4·joint probability §5)·concepts/tides/03-analysis-methods.md (조화분해)·concepts/storm-surge/04-code-and-tools.md (KHOA OpenAPI·residual). 정량 결과·정점별 판정은 experience/khoa-design-surge-eva-2026.md (verified, AI programmatic pipeline) + experience/khoa-49-station-16yr-utide-2026.md (49정점 utide 검증)에 귀속. 실제 스크립트(~/khoa_tide/utide_validation/*.py)는 위키 외부 로컬 한정 — 본 노트는 재현 절차·입출력·도구 사용 outline만 기술."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - examples/README.md
  - experience/khoa-design-surge-eva-2026.md
  - experience/khoa-49-station-16yr-utide-2026.md
  - concepts/storm-surge/03-analysis-methods.md
  - concepts/storm-surge/04-code-and-tools.md
  - concepts/tides/03-analysis-methods.md
---

# KHOA 조위관측 → 폭풍해일 극치분석(EVA) 파이프라인

> KHOA 조위 관측 시계열에서 출발해 **조화분석으로 천문조를 예측·제거**하여 폭풍해일 잔차를 얻고, 그 잔차에 **극치분석(EVA)** 을 적용해 **100년 재현 폭풍해일고(설계값)** 를 산정하는 **재현 가능한 워크플로**. 단일 토픽(tides 또는 storm-surge) 을 넘어 **조석 분석 → 폭풍해일 분리 → 극치통계** 를 결합한 통합 실습.

## 다루는 개념·모델·경험

- 개념:
  - [`concepts/tides/03-analysis-methods.md`](../../concepts/tides/03-analysis-methods.md) — 조화분해(harmonic analysis): $\eta(t)=Z_0+\sum_n H_n\cos(\sigma_n t-g_n)$ (Stewart §17.5)
  - [`concepts/storm-surge/03-analysis-methods.md`](../../concepts/storm-surge/03-analysis-methods.md) — tide-surge separation(§1)·annual maxima ranking(§4)·joint tide-surge probability(§5) (Pugh §6:1·§8:3:2·§8:3:3)
  - [`concepts/storm-surge/04-code-and-tools.md`](../../concepts/storm-surge/04-code-and-tools.md) §4 — KHOA OpenAPI·residual($\eta_{surge}=\eta_{obs}-\eta_{tide,pred}$)·archive 1년 retention 한계
- 도구: [utide](https://github.com/wesleybowman/UTide) (Python, robust IRLS·nodal correction) — `concepts/tides/03-analysis-methods.md` §1.3 알고리즘
- 경험(정량 결과 귀속):
  - [`experience/khoa-design-surge-eva-2026.md`](../../experience/khoa-design-surge-eva-2026.md) — 본 파이프라인의 **실현 사례**: 49정점 1956–2025, 극치 4법(Gumbel/GEV·POT/GPD·RFA·부트스트랩 CI), 해수부 2022 21항만 설계값 대조, 통영 joint MC, SSP 기후증폭
  - [`experience/khoa-49-station-16yr-utide-2026.md`](../../experience/khoa-49-station-16yr-utide-2026.md) — 전신: 49정점 16년 utide 검증(조화상수 cross-check·폭풍해일 residual·nodal cycle)

## 파이프라인 개요

```
KHOA 조위 관측 (1시간/10분 시계열)
        │  ① 다운로드 + QC
        ▼
   조화분석 (utide)  ──►  천문조 예측 η_tide(t)
        │  ② separation
        ▼
폭풍해일 잔차  S(t) = η_obs(t) − η_tide(t)        [Pugh §6:1 non-tidal residual]
        │  ③ 극값 표본 추출
        ├──► 연최대치 (AM, annual maxima)          [Pugh §8:3:2]
        └──► 임계초과 (POT, peaks-over-threshold) + 디클러스터
        │  ④ 극치분포 적합
        ├──► Gumbel / GEV  (L-moment, Hosking)
        ├──► GPD           (POT)
        └──► 지역빈도 RFA  (index-flood)
        │  ⑤ 재현주기 외삽 + 부트스트랩 CI
        ▼
   100년 재현 폭풍해일고 z₁₀₀ [± 95% CI]
        │  ⑥ (선택) 설계값 감사·joint tide-surge·기후증폭
        ▼
설계 폭풍해일고 비교 / 총수위 분해 / SSP 연례화
```

## 단계별 절차

각 단계의 **방법 출처**와 **재현 입출력**만 기술한다. 정점별 정량 수치는 위 experience 노트에 귀속한다.

### ① 데이터 다운로드 + QC

- **소스**: KHOA 조위 관측. 두 경로 — (a) OpenAPI `surveyTideLevel`(`tdlvHgt` 실측·`bscTdlvHgt` 예측), (b) `distribution.do` ZIP 일괄 다운로드(과거자료 확장).
- **archive 한계**: OpenAPI 는 **약 1년 rolling retention** — 1년 이전 storm event 는 OpenAPI 직접 fetch 불가, **ZIP 과거자료** 또는 Annual Report 필요. 출처 [`concepts/storm-surge/04-code-and-tools.md §4.1`](../../concepts/storm-surge/04-code-and-tools.md).
- **product 주의**: ZIP `1시간 조위` ≠ OpenAPI `tdlvHgt_cm` (정량 편차 존재; [`experience/khoa-49-station-16yr-utide-2026.md §2`](../../experience/khoa-49-station-16yr-utide-2026.md) 진단).
- **QC**: 무자료 마킹(HTTP500+html), 단발 스파이크 제거(양측 이웃 차 임계), 손상연도·datum 계단 제거(Pettitt 변화점). 메디안필터는 실제 태풍 피크를 훼손할 수 있어 부적합 — 출처 [`experience/khoa-design-surge-eva-2026.md §6·§11`](../../experience/khoa-design-surge-eva-2026.md).

### ② 조화분석 → 천문조 예측

- 정점·연도별 utide 적합(OLS/IRLS, `nodal=True`, `trend=True`). 추출된 조화상수 $(H_n, g_n)$ 로 동일 시각의 천문조 $\eta_{tide}(t)$ 재구성.
- 방법: [`concepts/tides/03-analysis-methods.md §1`](../../concepts/tides/03-analysis-methods.md) (조화분해 정의·기본 모델·알고리즘).
- 검증: KHOA 공시 조화상수와 cross-check(M₂/S₂/K₁/O₁ 등) — [`experience/khoa-49-station-16yr-utide-2026.md §4`](../../experience/khoa-49-station-16yr-utide-2026.md).

### ③ 폭풍해일 분리 (separation)

$$S(t) = \eta_{obs}(t) - \eta_{tide}(t)$$

- $S(t)$ = non-tidal residual = 폭풍해일 + 기타 비조석 성분. 출처 [`concepts/storm-surge/03-analysis-methods.md §1.1`](../../concepts/storm-surge/03-analysis-methods.md) (Pugh §6:1).
- KHOA OpenAPI 가 예측값을 제공할 경우 $\eta_{surge}=\eta_{obs}-\eta_{bscTdlvHgt}$ 로도 분리 가능 — [`concepts/storm-surge/04-code-and-tools.md §4.2`](../../concepts/storm-surge/04-code-and-tools.md).

### ④ 극값 표본 추출

| 표본법 | 정의 | 주의 |
|---|---|---|
| **연최대 (AM)** | 매년 $S(t)$ 의 최댓값 | $M\ge25$ 권장; 1년=1통계라 데이터 낭비 (Pugh §8:3:2) |
| **POT** | 임계 $\tau$ 초과 피크 | 동일 폭풍 중복 피크는 **디클러스터**(시간 간격 분리); 혼합모집단 제거 효과 |

- 출처: [`concepts/storm-surge/03-analysis-methods.md §3·§4`](../../concepts/storm-surge/03-analysis-methods.md).
- POT 임계 자동선정(z₁₀₀ plateau 탐색)·디클러스터·캐시는 [`experience/khoa-design-surge-eva-2026.md §11`](../../experience/khoa-design-surge-eva-2026.md).

### ⑤ 극치분포 적합 + 재현주기

- **Gumbel / GEV**: L-moment(Hosking) 적합. GEV shape 파라미터가 꼬리 무게를 결정(음수 shape → 유계).
- **GPD**: POT 표본에 일반화 파레토 적합.
- **RFA (지역빈도)**: index-flood 법 — 유사 정점을 권역으로 묶어 성장곡선 공유(단일 정점 단기록의 CI 과대 문제 완화). 권역 동질성은 Hosking-Wallis $H$ 통계로 진단.
- **재현주기**: 연최대 ranking 의 비초과확률 $P=\frac{2r-1}{2M}$ → probability paper 외삽으로 $z_{100}$ (Pugh §8:3:2). 또는 joint convolution $D_0(\eta)=\int D_T(\eta-y)D_S(y)\,dy$ → $T_R[\text{hours}]=1/P$ (Pugh §8:3:3). 출처 [`concepts/storm-surge/03-analysis-methods.md §4·§5`](../../concepts/storm-surge/03-analysis-methods.md).
- **trend 사전 보정**: ranking 전 Mann-Kendall trend 검출 후 SLR 제거·공통 기준연도 normalize (Pugh §8:3:2, [`concepts/storm-surge/03-analysis-methods.md §4.3`](../../concepts/storm-surge/03-analysis-methods.md)).
- **부트스트랩 CI**: 전 방법에 재표집으로 95% CI 산정(정점별 고정 시드로 재현성 확보) — [`experience/khoa-design-surge-eva-2026.md §11·§13`](../../experience/khoa-design-surge-eva-2026.md).

### ⑥ (선택) 설계값 감사·joint·기후증폭

- **설계값 감사**: 산정된 CI 가 공식 설계 폭풍해일고(해수부 2022 등)를 포함하는지 정점별 대조 → 지지/과대/과소 판정.
- **joint tide-surge**: 약최고고조위 + 최악해일 조합으로 총수위 분해(MC 권장; 단순 convolution 은 결정론적 조석을 난수로 취급해 과대추정).
- **기후증폭**: 현재 100년 총수위에 SSP SLR 평행이동 → 미래 재현주기 $T_{future}=1/(1-F(z_{100}-\Delta))$.
- 정량 결론은 모두 [`experience/khoa-design-surge-eva-2026.md §3·§7·§12`](../../experience/khoa-design-surge-eva-2026.md) 귀속.

## 재현 조건

- **실행 환경**: Python, `utide`(≥0.3.1)·`scipy`(≥1.17). 본 위키 공용 venv `~/coastal-wiki/.venv`(uv) 기준.
- **입력 데이터**: KHOA 조위 관측(OpenAPI 키 필요 또는 distribution.do ZIP). 환경변수 `KHOA_API_KEY`.
- **재현성 한계**: 실제 스크립트·원자료는 **위키 외부 로컬**(`~/khoa_tide/utide_validation/`) 한정. 본 예제는 **방법·단계·입출력 절차**만 제공하며 정점별 정량값은 experience 노트에 귀속한다(CLAUDE.md: examples = 객관 재현 절차, "내가 해보니" 화법 금지).

## 파일

| 파일 | 내용 |
|---|---|
| [`code/01_fetch_khoa.py`](code/01_fetch_khoa.py) | KHOA OpenAPI 조위 fetch outline (관측·예측·archive 한계 처리) |
| [`code/02_utide_separation.py`](code/02_utide_separation.py) | utide 조화분석 → 천문조 예측 → 폭풍해일 잔차 분리 outline |
| [`code/03_eva_return_level.py`](code/03_eva_return_level.py) | AM/POT 표본 → Gumbel/GEV/GPD 적합 → 100년 재현값 + 부트스트랩 CI outline |
| [`results/README.md`](results/README.md) | 기대 출력·검증 포인트·정량 결과 귀속(experience 링크) |
