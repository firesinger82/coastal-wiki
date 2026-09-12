---
title: "XBeach 정상 파랑 계산 — 활성 wave_stationary_directions와 구형 wave_stationary 구분"
topic: xbeach
canonical_source: self
citation_status: verified
verification_method: "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_stationary.F90 (448) + wave_stationary_directions.F90 (732) 직접 read — wave_stationary(7) iter/itermax + Herr/thetaerr 수렴(34/152) + roelvink/baldock/janssen_battjes + refraction slope limit(96) + wave_stationary_directions(33, ntheta_s callType) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — stationary 파 solver verbatim"
verification_date: 2026-06-03
related:
  - models/XBeach/source-analysis/xbeach_wave_action_balance.md
  - models/XBeach/source-analysis/xbeach_mode_dispatch.md
  - models/XBeach/source-analysis/xbeach_single_dir.md
source_correction_date: 2026-09-12
source_correction_by: "Codex"
source_correction_scope: "구형 wave_stationary의 역할을 한정하고 현재 정상 계산의 두 호출을 구분"
source_correction_human_approval: not-issued
---

> **2026-09-12 AI 출처 정정**: 구형 wave_stationary의 역할을 한정하고 현재 정상 계산의 두 호출을 구분. 위 `verification_*`는 이전 검증 이력이며 이번 정정의 새 사람 승인을 뜻하지 않는다. [원문 구간·SHA와 재사용 근거](../../../_staging/total-read/model-audit/XBeach/connectivity/corrections-20260912/evidence.json)에 결속했다.

# XBeach 정상 파랑 계산

현재 `wave_timestep`의 stationary 호출 대상은 `wave_stationary_directions(s,par,0)`이다. 같은 루틴을 surfbeat `single_dir`의 평균 방향 계산에도 다른 `callType`으로 사용한다. 이름이 유사한 `wave_stationary.F90`와 `wave_directions.F90`는 조사한 Autotools/Visual Fortran/IFX 모델 빌드 목록에 포함되지 않는다. (`wave_timestep.F90:75-114`; [[xbeach-build-mode-connectivity]])

## 1. `wave_stationary` — 구형·빌드 미포함 구현

기존 원문 판독은 `wave_stationary.F90`의 `wave_stationary`가 반복 cross-shore sweep과 `Herr/thetaerr` 수렴을 사용하는 구현임을 기록했다 (`wave_stationary.F90:7, 34, 152`). 이 설명은 해당 구형 파일의 내용이며, 현재 stationary 모드의 호출 대상을 뜻하지 않는다. 기존 `verification_*`의 두 파일 판독 이력도 이 구분을 따른다.

## 2. 활성 `wave_stationary_directions`

루틴은 `callTypeStationary=0`, `callTypeDirections=1`을 구분하고 사용할 방향 격자를 선택한다. 따라서 이 루틴 자체를 single_dir와 대비되는 전용 full-directional 경로로 설명하면 두 호출 역할을 놓친다. (`wave_stationary_directions.F90:33-49, 71-76`)

| 호출자 모드 | 호출 인수 | 방향 격자 | 계산 주기 |
|---|---|---|---|
| stationary | `callType=0` | `s%ntheta` | `abs(mod(t,wavint))<0.001*dt` 또는 `newstatbc==1` |
| surfbeat, `single_dir==1` | `callType=1` | `s%ntheta_s` | 평균장 갱신 뒤 `abs(mod(t,wavint))<0.001*dt`, `newstatbc==1` 또는 `t==dt` |

두 경로 모두 정상 계산 전에 해당 인수의 `wave_dispersion`을 호출한다. surfbeat의 시간에 따른 에너지 전파는 이 방향 계산 뒤 `wave_instationary`에서 별도로 진행한다. (`wave_timestep.F90:75-114`)

## 3. 연결

- [[xbeach_wave_action_balance]] — surfbeat 에너지·roller 전파
- [[xbeach_mode_dispatch]] — stationary/surfbeat/nonh 실행 분기
- [[xbeach_single_dir]] — surfbeat 평균 방향 계산
- [[xbeach-build-mode-connectivity]] — 현재 빌드 목록과 비활성 파일의 근거
