---
title: "조류 — 04 코드와 도구"
topic: currents
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "AI cross-reference: UTide README + _solve.py docstring + KHOA OpenAPI 가이드 (khoa-tide-model skill.md) + 수치조류도 CSV 단위·구조 검증 (tides-khoa-cross-verification §5). §6.1 full PDF 격상 (2026-09-28): arXiv 2511.12711v1·2606.03231v1·1307.0584v1 전문 판독(서브에이전트 + 핵심 인용·Table 2 원문 대조). ★ 에디 논문 hindcast 에서 HYCOM 입력이 무해류보다 RMSE·bias 나쁨, 축소모델은 수치실험 0건, Bayesian 논문은 사실상 MLE·‘surface forcing’=경계 파진폭으로 요약 정정."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 조류 — 04 코드와 도구

## 1. UTide 2D 모드 (Python/MATLAB)

조위 분석 도구와 동일 ([`concepts/tides/04-code-and-tools.md` §3](../tides/04-code-and-tools.md)). 2D 입력 시 자동으로 조류타원 모드.

### 1.1 설치

```bash
pip install utide
# 또는
conda install utide --channel conda-forge
```

### 1.2 2D 호출 (UTide README sample 인용)

```python
from utide import solve, reconstruct

coef = solve(
    t,                      # datetime64 array
    u,                      # 동-서 성분 (m/s)
    v,                      # 북-남 성분
    lat=37.5,
    nodal=True,
    trend=True,
    method="ols",
    conf_int="linear",
    Rayleigh_min=1.0,
)

# Predict
u_pred, v_pred = reconstruct(t_pred, coef)["u"], reconstruct(t_pred, coef)["v"]
```

### 1.3 출력 변수 — 조류타원 parameter

| 변수 | 의미 | 단위 |
|---|---|---|
| `coef["name"]` | 분조 이름 list (예: 'M2','S2','K1','O1',…) | — |
| `coef["Lsmaj"]` | 반장축 (semi-major) | u·v와 동일 |
| `coef["Lsmin"]` | 반단축. **부호** = 회전 (CCW + / CW −) | u·v와 동일 |
| `coef["theta"]` | 장축 inclination | ° (0-180, x축 CCW) |
| `coef["g"]` | phase | ° |
| `coef["umean"]`, `coef["vmean"]` | u·v 평균 | u·v와 동일 |
| `coef["uslope"]`, `coef["vslope"]` | linear trend | u·v / 시간 |

(`utide/_solve.py` `solve()` returns block 인용 — [`concepts/tides/05-examples.md` §1.3](../tides/05-examples.md) 동일 source)

### 1.4 회전 분해 옵션

UTide 내부적으로 회전 성분 W⁺ (CCW)·W⁻ (CW) 계산 — `coef["aux"]` 등 접근 가능 (UTide internal documentation 참조).

## 2. 수치조류도 격자 데이터 (KHOA, `khoa-tide-model`)

> 파일: 국립해양조사원 수치조류도 기반 조화상수 CSV (`khoa-tide-model` source — [textbook/sources.yml](../../textbook/sources.yml))
>
> 인코딩: **cp949**
>
> 단위: **cm/s** (조류 속도, **elevation 아님** — [`tides-khoa-cross-verification.md` §5](../../textbook/notes/tides-khoa-cross-verification.md))

### 2.1 데이터 구조

| 항목 | 값 |
|---|---|
| 행 수 | 813,703 |
| 좌표 범위 | lon 117.591–129.972, lat 25.162–40.896 (한국 + 동중국해) |
| 한국 해역 (124-132°E, 32-42°N) | 234,738 rows |
| 분조 수 | 14 |
| 분조 list | j1, k1, k2, l2, m1, m2, mu2, n2, nu2, o1, oo1, p1, q1, s2 |

### 2.2 CSV 컬럼 (28 + 1)

```
j1_진폭, j1_지각, k1_진폭, k1_지각, k2_진폭, k2_지각, l2_진폭, l2_지각,
m1_진폭, m1_지각, m2_진폭, m2_지각, mu2_진폭, mu2_지각, n2_진폭, n2_지각,
nu2_진폭, nu2_지각, o1_진폭, o1_지각, oo1_진폭, oo1_지각, p1_진폭, p1_지각,
q1_진폭, q1_지각, s2_진폭, s2_지각, 좌표
```

`좌표` 컬럼은 `"lon lat"` 형식 (공백 구분).

### 2.3 한계

- **단일 성분만**: 4 parameter (Lsmaj, Lsmin, θ, g) 중 (진폭, 위상) 2개만 — 회전·장축 방향 정보 없음.
  CSV 헤더와 data.go.kr 컬럼 설명(*"조화상수의 진폭정보"*)은 어느 성분인지 밝히지 않는다(2026-09-28 확인).
  같은 격자의 KHOA 예측 유속·유향 아카이브(data.go.kr 15130143)와 대조하면 **남북(v) 성분**과 일치하고 동서 성분은 담기지 않는다 —
  [`experience/khoa-tidal-current-phase-reference-2026.md`](../../experience/khoa-tidal-current-phase-reference-2026.md) @ `5de93ff` §3b.
  따라서 이 CSV 만으로는 조류 벡터·타원을 재구성할 수 없다.
- **위상 기준**: CSV 헤더·data.go.kr 컬럼 설명 모두 명시 없음(2026-09-28 확인). KHOA 공식 표준(지각 g 는 동경 135° 기준, [03-analysis-methods.md](03-analysis-methods.md) §1.3)에 따라 **g(135°E KST)** 로 해석한다. 데이터 기반 교차 확인: [`experience/khoa-tidal-current-phase-reference-2026.md`](../../experience/khoa-tidal-current-phase-reference-2026.md) @ `636c1e6`
- **격자 해상도**: 약 0.001° (≈ 100 m) → 좁은 수로·만 미해상 가능

### 2.4 격자에서 임의 정점 분조 추출 (template)

```python
import pandas as pd
import numpy as np

# Load (cp949)
df = pd.read_csv(
    "<KHOA_수치조류도_조화상수.csv>",  # khoa-tide-model source (국립해양조사원 수치조류도 기반 조화상수)
    encoding='cp949'
)
df[['lon','lat']] = df['좌표'].str.split(' ', expand=True).astype(float)

# 한국 해역 필터
korea = df[(df.lon.between(124,132)) & (df.lat.between(32,42))].copy()

# 임의 정점 (예: 인천 인근)
target_lat, target_lon = 37.45, 126.55

# Nearest neighbor (단순)
korea['dist'] = np.sqrt((korea.lon - target_lon)**2 + (korea.lat - target_lat)**2)
nearest = korea.nsmallest(1, 'dist').iloc[0]

print(f"가장 가까운 격자점: lat={nearest.lat:.4f}, lon={nearest.lon:.4f}")
print(f"M2 진폭 = {nearest['m2_진폭']:.2f} cm/s, 지각 = {nearest['m2_지각']:.2f}°")
print(f"S2: {nearest['s2_진폭']:.2f} cm/s @ {nearest['s2_지각']:.2f}°")
print(f"K1: {nearest['k1_진폭']:.2f} cm/s @ {nearest['k1_지각']:.2f}°")
print(f"O1: {nearest['o1_진폭']:.2f} cm/s @ {nearest['o1_지각']:.2f}°")
```

## 3. KHOA OpenAPI (조류·조위)

> ✅ verified (2026-09-28): KHOA 바다누리 OpenAPI 공식 목록(`https://www.khoa.go.kr/oceandata/openapi/openApiList.do`, 목록 데이터
> `POST /oceandata/openapi/search.do`) + 키 없이 호출한 응답 실측. 기존 가이드(`khoa-tide-model` skill.md)의 `http://www.khoa.go.kr/api/oceangrid/<이름>/search.do`
> 경로는 **폐기됐다** — 모든 이름에 오류 페이지를 돌려준다.

현행 경로 형식: `https://khoa.go.kr/oceandata/api/<이름>/search.do` (공통 `ServiceKey`, `ResultType=json|xml`).

| 이름 | 공식 명칭 | 주요 요청 파라미터 | 응답 |
|---|---|---|---|
| `tidalCurrentArea` | 수치조류도 예측 유향 유속 | `Date`(YYYYMMDD)·`Hour`·`Minute`·`MaxX`·`MinX`·`MaxY`·`MinY` | `pre_lon`·`pre_lat`·`current_speed`(**cm/s**)·`current_dir`(deg) — 영역 폭에 따라 1–10 km 간격 자동 조절 |
| `tidalCurrentAreaGeoJson` | 면(지역)단위 수치조류도 예측 유향 유속 | 위와 같음 | GeoJSON |
| `tidalCurrentPoint` | 수치조류도 지점별 최강창낙조 | `SDate`·`SHour`·`SMinute`·`EDate`·`EHour`·`EMinute`·`lon`·`lat` | 최근접 지점(최대 1 km)의 `obs_date`·`type`(창조·낙조·전류)·`current_speed`(cm/s)·`current_dir`(deg) |
| `tideObsHar` | 조위관측소 조화상수 | 관측소 코드 | 진폭·지각 |
| `tbm` | 기본수준점 | — | 조화상수·메타정보 |

**공공데이터포털 게이트웨이 (data.go.kr 인증키 — 바다누리 키와 별개, 서비스별 활용신청 필요)**:

| 서비스 (data.go.kr 번호) | 호출 | 주요 요청 | 응답 |
|---|---|---|---|
| 국립해양조사원_조류예보(시계열) (15156024) | `https://apis.data.go.kr/1192136/crntFcstTime/GetCrntFcstTimeApiService` | `obsCode`(예보지점, 예 16LTC10)·`reqDate`·`min`(간격, 최대 60) | `obsvtrNm`·`lat`·`lot`·`predcDt`·`crdir`(**16방위 문자**)·`crsp`(cm/s) |
| 국립해양조사원_조류예보 최강창낙조 및 전류 (15156025) | 같은 게이트웨이 | `obsCode` | 최강 창·낙조 유향(deg)·유속, 전류 시각 |

`crdir` 16방위 → 도(진북 기준 시계방향, 22.5° 간격). API 가 돌려주는 이름 16개를 2개 지점 144건에서 모두 확인했다(동·서가 앞에 오는 한국식: `동북동`·`동남동`·`서남서`·`서북서`):

| 방위 | 도 | 방위 | 도 | 방위 | 도 | 방위 | 도 |
|---|---|---|---|---|---|---|---|
| 북 | 0 | 동 | 90 | 남 | 180 | 서 | 270 |
| 북북동 | 22.5 | 동남동 | 112.5 | 남남서 | 202.5 | 서북서 | 292.5 |
| 북동 | 45 | 남동 | 135 | 남서 | 225 | 북서 | 315 |
| 동북동 | 67.5 | 남남동 | 157.5 | 서남서 | 247.5 | 북북서 | 337.5 |

```python
DIR16 = ['북','북북동','북동','동북동','동','동남동','남동','남남동',
         '남','남남서','남서','서남서','서','서북서','북서','북북서']
deg = {n: i * 22.5 for i, n in enumerate(DIR16)}   # crdir → 도
```

- **정밀도는 ±11.25°** 다 — 모델 유향과 비교할 때 이보다 작은 차이는 판별할 수 없다. 유속과 함께 벡터로 바꾸면 방향 오차가 성분에 그대로 들어간다(최대 약 20% 성분 오차: sin 11.25° ≈ 0.195).
- 변환표와 "흐르는 방향" 규약은 데이터로 검증했다 — 숫자 유향을 주는 최강창낙조 API 와 같은 시각 비교, 규약이 확인된 수치조류도 API 와 비교: [`experience/khoa-tidal-current-phase-reference-2026.md`](../../experience/khoa-tidal-current-phase-reference-2026.md) @ `20bc544` §3d.

2026-09-28–29 확인: 15156024 는 활용신청 전 `SERVICE_KEY_IS_NOT_REGISTERED_ERROR`, 신청 후 `NORMAL_SERVICE` — 비진도남측 2026-09-29 1시간 간격 24건(예 00:00 동북동 44.40 cm/s). 이것은 수치조류도 격자가 아니라 **관측 기반 조류예보 지점**의 예측이다(명세: *"우리나라 관할해역 조류 예보지점의 시계열 조류 정보(유향, 유속, 시각)"*).

- 실측 판별: 존재하는 이름은 키 없이 호출하면 `{"result":{"error":"ServiceKey is null"}}`, 없는 이름은 "요청하신 페이지" 오류 HTML 을 준다.
  이 방식으로 위 5개는 존재, 구판에 적었던 `tideObsReal`·`tideObsPre` 는 현행 경로에 **없다**(2026-09-28).
- 명세는 유향을 "deg" 로만 적는다. 시각 지정 호출 대조로 **`Date`·`Hour` 는 KST**, **유향은 흐르는 방향(진북 기준 시계방향)** 임을 확인했다 — [`experience/khoa-tidal-current-phase-reference-2026.md`](../../experience/khoa-tidal-current-phase-reference-2026.md) @ `68ae7d7` §3c.
- `tidalCurrentArea` 는 §2 조화상수 CSV 와 같은 수치조류도의 예측값이며, 예측은 **회전성 조류 벡터**다 — CSV(남북 성분만)로는 재현되지 않는다.

## 4. 도구 vs 모델 분리 (참고)

글로벌 조석 모델의 조류 제공 여부는 모델마다 다르다 — 가용성 표와 근거는 [06-model-application §6](06-model-application.md) (2026-09-28 확인).
요약: TPXO10·FES2014 는 u, v 분조 제공, **FES2022 조류는 공개 배포 안 함**, **NAO.99 는 조류 미배포**, GOT 는 조위만.
KHOA 수치조류도 조화상수 CSV 는 v 성분만이라 연안 조류 forcing 자료로 쓸 수 없다(§2.3).

## 5. 도구·자료 선택 가이드

| 상황 | 권장 |
|---|---|
| 1년 정도 ADCP 관측 분석 | **UTide 2D** (Python) |
| 정밀 분석 + IRLS robust | UTide `method='robust'` |
| 한국 임의 지점 분조 추정 | KHOA 수치조류도 CSV 격자 보간 |
| EFDC/ADCIRC 경계 조류 forcing | KHOA 수치조류도 (한국) + TPXO/FES (외해) |
| 명량·진도 등 강조류 해역 | 자체 ADCP 관측 + UTide robust |

## 6. 보강·미해결

- 수치조류도 CSV `진폭` 정확한 정의 (u 단독 / v 단독 / |U| / max speed 중 어느 것인지)
- 수치조류도 CSV 위상 기준 (G/g/κ 어느 것인지)
- KHOA OpenAPI 조류 endpoint 정확 명·파라미터
- TPXO·FES의 조류 데이터 사용법 — pyTMD `currents` mode 인용 보강
- 라이선스 (UTide MIT 확인, KHOA 자료 사용 정책 확인)

### 6.1 연구 문헌 3편 ✅ verified (full PDF 판독 2026-09-28)

#### 6.1.1 에디 dipole 근방 파랑–해류 — Violante-Carvalho et al., arXiv:[2511.12711](https://arxiv.org/abs/2511.12711)v1 (2025-11-16)

WAVEWATCH III **v7.14 ST4**, 0.04° 격자, 남서대서양(São Paulo 대지 부근) 에디 dipole. 실험이 **둘로 나뉜다**:[^vc]

| 실험 | 강제 | 결과 |
|---|---|---|
| 이상화 | **바람 없음**, HYCOM 해류 한 장(2010-09-08) 고정, 남쪽 경계 swell Hs 1 m · 방향분산 15° · Tp 7 s / 15 s | 중앙 jet 에서 Hs 증가 **7 s 50% 초과 / 15 s 최대 33%** — 선형이론 단일 파(1 m/s 역류) 예측 25% / 10% 보다 크다 |
| hindcast | ERA5 바람·경계 스펙트럼, 2010-08~09, 해류 3종(SSalto/Duacs 1/4° 일별 · HYCOM 1/12° · GlobCurrent 1/4°) + 무해류, 24/72 방향 | 위성고도계(CCI L3) Hs 14 궤도 구간 대조 |

- **"수렴렌즈" 는 이상화 실험의 결론이다** — 바람 없음·정지 해류·좁은 방향분산(저자 스스로 *"expected to cause a pronounced increase in energy"*).
  hindcast 에서 해류가 만든 Hs 변화량은 따로 정량화되지 않는다. 기구는 굴절 채널링 단독이 아니라 **굴절 + 이류(Doppler)** 결합.
- ★ **hindcast 검증표(Table 2)를 다시 읽으면** (dipole 영역 971점 / 중앙 jet 476점):

  | 해류 입력 | CORR | RMSE (m) | bias (m) |
  |---|---|---|---|
  | SSalto (24 방향) | 0.68 / 0.65 | 0.23 / 0.22 | 0.040 / 0.022 |
  | GlobCurrent (24) | 0.67 / 0.61 | 0.24 / 0.23 | 0.041 / 0.023 |
  | HYCOM (24) | 0.64 / 0.57 | 0.26 / 0.26 | 0.062 / 0.043 |
  | **무해류** | 0.53 / **0.30** | 0.25 / 0.23 | 0.040 / **−0.008** |

  해류 효과는 **상관계수에서만 뚜렷하고 RMSE 개선은 0.01–0.02 m** 다. **HYCOM 입력은 RMSE·SI·bias 모두 무해류보다 나쁘다** —
  jet 위치를 20–30 km 어긋나게 놓았기 때문이다(저자 명시). 가장 거친 SSalto 가 가장 좋다. 24→72 방향은 *"marginal impact"*.
  저자 스스로 *"the differences in RMSE are not statistically significant"* 라 쓰며, 검정 방법은 기술하지 않는다.
- 결론부 "HYCOM 이 에너지 역학을 더 포괄적으로 표현" 은 **저자 주장**이며 자신들의 Table 2 순위와 반대다.
- 본문 불일치: 파형경사를 $\varepsilon=(H_s/2)k_p$ 로 정의하나 보고값 0.0822(7 s)·0.0179(15 s)는 $H_s k_p$ 값이다
  ($k_p=\omega^2/g$ 심해: 7 s → 0.0821, 15 s → 0.0179 m⁻¹, 본 노트 계산).
- 연안 모델러 교훈: **해류장 선택(위치 정확도)이 방향 해상도보다 중요**하고, 위치가 어긋난 재해석 해류는 해류를 안 넣은 것보다 나쁠 수 있다.
  SWAN/WW3 해류 입력의 Doppler·굴절 항 메커닉은 [`08-wave-current-interaction`](../waves/08-wave-current-interaction.md).

#### 6.1.2 공간 규모 분리 없는 파랑–해류 축소모델 — Onuki·Fujiwara, arXiv:[2606.03231](https://arxiv.org/abs/2606.03231)v1 (2026-06-02, 12p)

Craik-Leibovich(Suzuki & Fox-Kemper 2016 형) 평균류 + 복소 진폭 $A$ 의 Helmholtz 형 파동식을 결합하고, Stokes drift 를 외부에서 주지 않고 $A$ 로부터 계산한다.
주기 영역에서 파작용·에너지(교환분)·운동량($f=0$ 일 때) 보존을 해석적으로 보인다.[^of]
- ★ **수치 실험이 하나도 없다** — 그림·시뮬레이션·기준해 비교 없음. 수치 구현은 향후 과제(§7).
- ★ **"규모 분리 없음" 은 수평 공간에 한정** — 시간 규모 분리($\epsilon^{-2}$), 좁은 주파수대($|k|=\kappa$), 약한 해류($U\sim\epsilon^2 c$)는 그대로 가정.
  저자 요약: *"weak nonlinearity, constant depth and a narrow frequency band, but does not impose a spatial-scale separation"*.
- 보존 구조의 일부는 현상론적 치환(§5: $\nabla\cdot\mathbf U^L=0$ 강제, Stokes 보정항 도입)으로 만든 것이며, 후자는 심해에서만 타당하다고 저자가 적는다.
  평탄 지형·강체 뚜껑·쇄파 없음 — 대상은 외해 Langmuir 순환이다. 연안 적용성은 현재 낮다.
- 위치 짓기: 저자는 vortex-force 계열(McWilliams et al. 2004, Uchiyama et al. 2010)과 WKB/ray 계열을 "규모 분리형" 으로 묶고 대비한다.
  SWAN/WW3 작용평형이 바로 그 WKB 계열이라는 연결은 본 노트의 해석이다.

#### 6.1.3 연안류 모델의 자료 기반 모수 추정 — Balci·Restrepo·Venkataramani, arXiv:[1307.0584](https://arxiv.org/abs/1307.0584)v1 (2013, *Ocean Modeling* 투고)

vortex-force 수심평균 파랑–해류 모델(Duck 단면, 연안방향 균일)의 두 모수 — **외해 경계 파진폭 $a$** 와 **선형 저면마찰 계수 $d$**($\tau=du$) — 를
DUCK94 현장 연안류(바 부근 유속계 3개, 1994-09~11)로 추정한다.[^br]
- 결과: *"a = 0.8−1.1 m"*, *"d = 0.007 − 0.020"*. 최소 **3–5 시간** 자료가 필요하고, 3 시간 창에서는 $a$ 는 변하나 $d$ 는 안정적이다.
- ★ **이름은 Bayesian 이지만 실제는 격자 위 최대우도(MLE)** — 사전분포는 균일 상자, 저자 *"only interested in computing the maximal likelihood estimates"*.
  불확실성 구간·합성자료(twin) 검증은 없다. 우도는 크기 상대오차 $|1-|O|/|M||$ 이며 **해류 방향은 벌점에 들어가지 않는다**.
- "다항근사" = 모델 출력의 Legendre 대리모델(17 × 33 = 561 run) → 256² 격자 평가. *"117 times faster"* 는 run 수 비 65536/561 = 116.8 이다(본 노트 계산).
- 기존 요약의 "surface forcing" 은 **바람이 아니라 외해 경계 파진폭**이다(풍응력 항은 0).
- 실무 교훈(저자 Fig. 6 의 능선 + 본 노트 해석): 마찰과 경계 파고는 서로 보상하는 능선을 이룬다 — **마찰을 경계 파고와 따로 보정하면 편향된다**.
  $d$ 는 선형계수라 2차 $C_f$·Manning 으로 바로 옮길 수 없다.

[^vc]: Violante-Carvalho et al., arXiv:2511.12711v1 — WW3 *"7.14"*, *"ST4"*; §4.1 *"A maximum increase in Hs for the 7 s waves of over 50% is observed in the central jet"*, *"maximum of 33%"*, 선형이론 *"predicts an increase of approximately 25%"*; §4.1 *"the narrow σ = 15◦ employed in the simulations is expected to cause a pronounced increase in energy"*; §4.2 HYCOM *"misplaced the position of the maximum value by ∼20-30 km"*, *"ten points greater than HYCOM"*, *"twice as large"*, *"the differences in RMSE are not statistically significant"*, *"has a marginal impact on Hs"*; Table 2 (6 run × dipole 971점 / jet 476점) CORR·BIAS·RMSE·SI·VAR — 위 표는 그 중 24 방향 4행 발췌.
[^of]: Onuki & Fujiwara, arXiv:2606.03231v1 [physics.flu-dyn] — §7 *"The formulation assumes weak nonlinearity, constant depth and a narrow frequency band, but does not impose a spatial-scale separation between the waves and the current"*; §7 *"A complementary next step is to implement the reduced equations in a numerical model"*. 본문에 Figure 0 건(추출본 계수).
[^br]: Balci, Restrepo & Venkataramani, arXiv:1307.0584v1 — *"linear bottom drag formulation: τ = du"*; 사전 상자 *"[0.4, 1.2]"*·*"[0.002, 0.026]"*; §3.1 *"only interested in computing the maximal likelihood estimates for a and d"*; §3.3 *"117 times faster"*; §5 *"a = 0.8−1.1 m. The most likely bottom drag coefficient was in the range d = 0.007 − 0.020"*, *"3-5 hours"*; *"Submitted to Ocean Modeling"*.

## 7. 연결

- `02-theory.md` — 조류타원 (Lsmaj/Lsmin/θ/g 정의)
- `03-analysis-methods.md` — UTide 2D 호출법
- `05-examples.md` — 수치조류도 실제 정점 추출
- `concepts/tides/04-code-and-tools.md` — 동일 도구·전 지구 모델
- `concepts/tides/04-code-and-tools.md` §6 — TPXO·FES·NAO·GOT 글로벌 조석/조류 모델
- 외부 인용:
  - UTide README + _solve.py
  - `khoa-tide-model` skill.md (KHOA API 가이드)
  - 변도성 (2007) 위상 기준 — `concepts/tides/02-theory.md` §8.3.1
