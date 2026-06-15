---
title: "조류 — 04 코드와 도구"
topic: currents
canonical_source: self
citation_status: verified
verification_method: "AI cross-reference: UTide README + _solve.py docstring + KHOA OpenAPI 가이드 (khoa-tide-model skill.md) + 수치조류도 CSV 단위·구조 검증 (tides-khoa-cross-verification §5)."
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

> 파일: `D:\Numerical_models\00_Common\Tide\tide_model\KHOA\해양수산부 국립해양조사원_수치조류도 기반 조화상수_20250814.csv`
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

- **단일 성분만**: 4 parameter (Lsmaj, Lsmin, θ, g) 중 (진폭, 위상) 2개만 — 회전·장축 방향 정보 없음
  - 추측: u 또는 v 한 방향, 또는 max speed magnitude만
  - 정확한 의미 → KHOA 원본 문서 별도 확인 필요 (source-needed)
- **위상 기준**: GMT 또는 KST 중 어느 것인지 명시 없음 — KHOA 자료라면 g (135°E KST) 가능성 높지만 별도 확인
- **격자 해상도**: 약 0.001° (≈ 100 m) → 좁은 수로·만 미해상 가능

### 2.4 격자에서 임의 정점 분조 추출 (template)

```python
import pandas as pd
import numpy as np

# Load (cp949)
df = pd.read_csv(
    "/mnt/d/Numerical_models/00_Common/Tide/tide_model/KHOA/해양수산부 국립해양조사원_수치조류도 기반 조화상수_20250814.csv",
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

## 3. KHOA OpenAPI (조류 관측)

> KHOA 바다누리 API 가이드는 [`khoa-tide-model` skill.md](../../textbook/notes/tides-khoa-cross-verification.md) 인용. **조류 관련 endpoint** 별도 조사 필요 (현재 noted endpoints는 조위 위주).

조위 endpoint (참고):
- `tideObsHar` — 조화상수 (조위)
- `tideObsReal` — 실시간 관측 조위
- `tideObsPre` — 예측 조위

조류 endpoint (추정):
- `tideObsTideCurrent` 또는 유사 — 조류 관측 데이터
- 정확한 endpoint 명은 KHOA OpenAPI 문서 직접 확인 (source-needed)

→ 조류 관측 데이터 자동 다운로드 코드는 KHOA OpenAPI 키 + 정확한 endpoint 확인 후 보강.

## 4. 도구 vs 모델 분리 (참고)

`concepts/tides/04-code-and-tools.md` §6 글로벌 조석 모델은 **조류도 동시 제공** — 사용 시:

| 모델 | 조류 제공 |
|---|---|
| **TPXO** | u, v 분조 ✓ |
| **FES2022** | u, v 분조 ✓ (`global_tide_fes`/eastward·northward) |
| **NAO.99Jb** | 일본 주변 조류 ✓ |
| GOT5 | elevation only (deep ocean, 조류 별도) |

→ pyTMD는 elevation·current 양쪽 지원. 외해 조류 forcing은 글로벌 모델, 연안은 KHOA 수치조류도 우선.

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

### 6.1 연구 문헌 (research/inbox promote, source-needed)

- **Eddy dipole wave-current (Violante-Carvalho et al. 2025)** — arxiv:[2511.12711](https://arxiv.org/abs/2511.12711). WW3 로 ocean eddy dipole 근방 wave field 에 대한 표층류 영향 평가 — dipole = surface wave **수렴렌즈**(중앙 jet 으로 refraction 채널링), H_s 공간변동. 남서대서양 강 dipole 2개월 hindcast(HYCOM/GlobCurrent/SSalto-Duacs 3 표층류 비교, 위성고도계 H_s 검증). 와류 wave-current 상호작용.
- **Wave-current 축소모델 — Craik-Leibovich 확장 (Onuki·Fujiwara 2026)** — arxiv:[2606.03231](https://arxiv.org/abs/2606.03231). 약비선형 표면중력파 ↔ 천천히 진화하는 current 양방향 상호작용 reduced asymptotic 모델. Craik-Leibovich wave-averaged momentum 기반이나 Stokes drift 를 외부규정 않고 동반 진폭식으로 결정. **공간 scale separation 미가정** → current-induced advection·refraction·scattering 표현. wave action 보존.
- **Nearshore 모델 Bayesian 보정 (Balci·Restrepo·Venkataramani 2013)** — arxiv:[1307.0584](https://arxiv.org/abs/1307.0584). **longshore current** nearshore 모델 파라미터(bottom drag·surface forcing)를 field data 로 tuning 하는 Bayesian MLE(다항근사 효율화, covariance 부재 문제 대응). 모델 보정 방법론.
- citation_status: 위 3건 source-needed (abstract 기반)

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
