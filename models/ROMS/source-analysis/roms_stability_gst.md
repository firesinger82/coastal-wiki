---
title: "ROMS 일반화 안정성이론(GST) & 관측 영향 — FTE/AFTE eigenmodes·OP/FSV singular vectors·SO/SO_SEMI stochastic optimals·HOP/HSO Hessian + obs_sen observation sensitivity·optobs. propagator(ARPACK Arnoldi) 기반"
topic: roms
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/source_code/roms/ROMS/Drivers/ 직접 read — fte_roms.h(Finite Time Eigenmodes)/afte_roms(Adjoint FTE)/op_roms(Optimal Pertubations Singular Vectors)/fsv_roms(Forcing Singular Vectors)/so_roms(Stochastic Optimal)/so_semi_roms(Seminorm)/propagator_*(fte/fsv/op/so/hop/hso ARPACK Arnoldi)/obs_sen_i4dvar_analysis(I4D-Var Observation Sensitivity)/optobs_roms(Optimal Observation) 헤더 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-09
verification_by: "Claude Opus 4.8 (1M context) — GST 드라이버·obs sensitivity 헤더 verbatim"
verification_date: 2026-06-09
related:
  - models/ROMS/source-analysis/roms_adjoint_framework.md
  - models/ROMS/source-analysis/roms_4dvar.md
---

# ROMS 일반화 안정성이론(GST) & 관측 영향

> ROMS `Drivers/` 직접 read. [[roms_adjoint_framework]](TLM/ADM 모델 구조)·[[roms_4dvar]](변분 DA) 가 안 다룬 **TLM/ADM 기반 분석 driver 군** — Generalized Stability Theory(GST, Moore-Farrell-Ioannou)로 **예측가능성·오차성장·최적교란**을 진단 + **관측 영향/설계**. 자료동화의 자매 capability(adjoint/tangent 모델을 DA 가 아닌 stability 분석에 사용).

## 1. GST — propagator 고유값/특이값 분석 ★

TLM(전파연산자 R)·ADM(R*)의 spectrum 을 **ARPACK Arnoldi**(`propagator_*.h`)로 계산:

| driver | 분석 | 의미 |
|---|---|---|
| **FTE** `fte_roms` | Finite Time **Eigenmodes** of R | 유한시간 정상모드(가장 빨리 성장) |
| **AFTE** `afte_roms` | **Adjoint** FTE (R*) | adjoint eigenmode(수용성, biorthogonal) |
| **OP** `op_roms` | **Optimal Perturbations**(=Singular Vectors of R) | 최대 오차성장 초기교란(predictability·ensemble seed) |
| **FSV** `fsv_roms` | **Forcing** Singular Vectors | forcing 에 대한 최적 반응(stochastic forcing) |
| **SO** `so_roms` | **Stochastic Optimals** | 시변 random forcing 의 최적 분산 구조 |
| **SO_SEMI** `so_semi_roms` | SO seminorm 추정 | 부분공간 norm |
| **HOP/HSO** `propagator_hop/hso` | **Hessian** optimal pert/stochastic | 4D-Var 분석오차 공분산의 Hessian eigenstructure |

- **OP(singular vector)** = `R*·R` 의 최대 고유벡터 → 주어진 norm 에서 최대 성장 초기교란. **ensemble forecast seed·target observation** 의 이론적 기반.
- `propagator_*.h` = 각 분석의 matrix-vector(R 또는 R*R 적용) — TLM/ADM 정방향/역방향 적분([[roms_adjoint_framework]] tl_/ad_)을 ARPACK 가 반복 호출.

## 2. Observation 영향·설계

- **obs_sen_{i4dvar/r4dvar/rbl4dvar}_analysis.h**: **Observation Sensitivity** — 관측이 분석/예보(cost·forecast metric)에 미치는 영향(adjoint of forecast aspect). OSE/OSSE, 관측 영향 진단(FSO, Forecast Sensitivity to Observations).
- **obs_sen_rbl4dvar_forecast.h**: 예보 민감도(forecast error → 관측 기여).
- **optobs_roms.h**(Optimal Observation): 최적 **관측 배열 설계**(어디서 관측하면 분석 개선 최대 — OP/SV 기반 adaptive observation).

## 3. 보조 driver

- **pert_roms.h**: perturbation 적분(TLM forward 교란 전파). **tlcheck_roms.h**: TLM-ADM **inner-product test**(⟨R x, y⟩=⟨x, R*y⟩ 검증, [[roms_4dvar]] §working rules 의 정확성 체크). **split_*_roms.h**: GST/4D-Var 단계 분리 실행.

## 4. ★ ad_/tl_/rp_ 커널 파일 — class 커버 명시

`Adjoint/`(81)·`Tangent/`(70)·`Representer/`(55) 의 개별 `ad_*`/`tl_*`/`rp_*` 파일(예: ad_step3d_t·tl_prsgrd·rp_uv3dmix…)은 **각 NL 커널의 exact transpose/linearization** — [[roms_adjoint_framework]] §1 이 **class 로 특성화**(NL 커널 1:1 대응). 개별 file 노트는 반복적이라 미작성(NL 물리는 [[roms_baroclinic_3d]] 등 covered). GST/obs-sensitivity(본 노트)와 4D-Var([[roms_4dvar]])가 이 커널들을 **사용하는 driver**.

## 5. 연결

- [[roms_adjoint_framework]] — TLM/ADM/RPM 모델 구조(GST 가 사용하는 R/R*)
- [[roms_4dvar]] — 변분 DA(GST 의 자매, 같은 TLM/ADM 사용)
- Moore et al. 2004 (ROMS GST) / Farrell-Ioannou 1996(generalized stability) / ARPACK(Arnoldi) / Lehoucq-Sorensen
