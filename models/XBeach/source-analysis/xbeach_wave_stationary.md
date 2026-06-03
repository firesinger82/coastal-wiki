---
title: "XBeach stationary wave 모드(wave_stationary.F90 + wave_stationary_directions.F90) — 정상상태 파작용 반복 cross-shore sweep(Herr/thetaerr 수렴) + Baldock 쇄파 + 방향분해"
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
---

# XBeach stationary wave 모드 (wave_stationary)

> `wave_stationary.F90`(448) + `wave_stationary_directions.F90`(732) 직접 read. XBeach **stationary 모드**의 파동 solver — 시간전진 없이 **정상상태(steady) 파작용**을 반복(iteration)으로 해. surfbeat(시간전진, [[xbeach_wave_action_balance]] wave_instationary)의 자매. 평균 wave forcing 만 필요한 case(긴 simulation·기후·정적 setup)에 경제적.

## 1. wave_stationary — 정상 파작용 (wave_stationary.F90:7)

- **반복 cross-shore sweep**: offshore→해안 방향으로 파작용 평형을 iteration(`iter`/`itermax`)으로 수렴. `Herr`(파고 오차)·`thetaerr`(방향 오차) < tol 까지(`stopiterate`).
- 쇄파: `roelvink`/`baldock`/`janssen_battjes`([[xbeach_wave_breaking]]) — stationary 는 주로 **Baldock**(확률적, 정상상태 적합).
- refraction: slope limit(:96, 비현실 refraction 속도 억제). y-advection 은 수렴 위해 upwind_1 강제(:68).
- roller energy balance 도 정상상태로 동시 해 → radiation stress.

## 2. wave_stationary_directions — 방향분해 (wave_stationary_directions.F90:33)

- `callType` 으로 `ntheta`(주 방향격자) vs `ntheta_s`(stationary 세분 방향) 선택.
- 방향(θ) 분해 파작용을 advection(xadvec/yadvec/thetaadvec, [[xbeach_wave_functions]])으로 반복 해. 방향분포(spreading) 정밀.
- [[xbeach_single_dir]](single-directional 근사)와 대비 — 이쪽은 full directional.

## 3. instationary vs stationary

| | surfbeat(wave_instationary) | stationary(wave_stationary) |
|---|---|---|
| 시간 | 시간전진(IG 변조) | 정상상태 반복 |
| IG | bound long wave 직접 | 없음(평균 forcing) |
| 비용 | 큼 | 작음 |
| 용도 | swash/runup/storm | 평균 wave-driven current·setup·긴 run |

## 4. 연결

- [[xbeach_wave_action_balance]] — instationary 자매(공유 advection/breaking/roller)
- [[xbeach_mode_dispatch]] — stationary/surfbeat/nonh 모드 선택
- [[xbeach_wave_functions]] — advection·refraction velocity 공유
- [[xbeach_single_dir]] — single-directional 근사
