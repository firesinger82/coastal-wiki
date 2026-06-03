---
title: "XBeach wave boundary 생성 & SWAN 연동 — offshore 스펙트럼(JONSWAP/SWAN/vardens) → 랜덤위상 단파 train → bound long-wave(infragravity, Herbers 1994 + Van Dongeren 2003) 경계 forcing"
topic: xbeach
canonical_source: self
citation_status: verified
verification_method: "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_boundary_update.f90 (2768) + waveparamsnew.F90(spectral_wave_bc 98, read_swan_file 418) 직접 read — generate_wave_boundary_surfbeat(73), generate_qbcf bound long wave(2460: Herbers1994 eq.1 E=2D²Sf²df, Van Dongeren2003 eq.21 phase/eq.22 angle theta3=atan2(KKy,KKx)) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — bound long wave 생성·SWAN 연동 chain verbatim"
verification_date: 2026-06-03
related:
  - models/XBeach/source-analysis/xbeach_swan_handoff.md
  - models/XBeach/source-analysis/wave/xbeach_wave_boundary.md
  - models/XBeach/source-analysis/xbeach_wave_action_balance.md
  - models/SWAN/source-analysis/swan-output-formats.md
---

# XBeach wave boundary 생성 & SWAN 연동

> `wave_boundary_update.f90`(2768) + `waveparamsnew.F90`(spectral_wave_bc) 직접 read. offshore 스펙트럼을 surfbeat 경계 forcing 으로 변환하는 **생성 알고리즘** — 특히 **bound long-wave(infragravity) 생성**. [[xbeach_swan_handoff]]/[[xbeach_wave_boundary]] 이 스펙트럼 **읽기·파일구조**를 다뤘고, 본 노트는 그 스펙트럼이 **bound IG 경계파로 변환되는 물리**(SWAN↔XBeach 연동의 심부)와 그 결과가 [[xbeach_wave_action_balance]] 내부 solver 로 들어가는 chain.

## 1. 스펙트럼 입력 3 경로 (waveparamsnew.F90:415-421)

```fortran
spectral_wave_bc → wbctype:
  read_jonswap_file   ! 파라메트릭 JONSWAP (Hm0/Tp/mainang/gam/scoeff)
  read_swan_file      ! SWAN ASCII spectral output → [[xbeach_swan_handoff]]
  read_vardens_file   ! variance density 2D spectrum
```
→ 모두 `specin%S(f,θ)` (variance density 2D 스펙트럼)으로 통일. **SWAN 연동** = `read_swan_file`(SWAN VaDens/EnDens·FACTOR·freq×dir matrix → S(f,θ), 801 freq × 401 dir 보간). SWAN 출력측은 [[swan-output-formats]].

## 2. generate_wave_boundary_surfbeat 흐름 (wave_boundary_update.f90:73)

1. **스펙트럼 → XBeach 격자 보간**(naint=401 방향, nfint freq).
2. **랜덤위상 단파 train**: 스펙트럼을 Fourier component 로 분해 — `wp%fgen`(주파수)/`thetagen`(방향)/`phigen`(랜덤 위상)/`kgen`(파수)/`wgen`(각진동수). 각 성분 진폭 `√(2·S·df·dθ)`.
3. **에너지 envelope** 시계열: 단파 군(wave group)의 변동(variance) 포락선 계산(directional-spreading 의존, :2168).
4. **`generate_qbcf`** — bound long wave 생성(§3).
5. nonh 시계열(`generate_nhtimeseries_file`, nonhspectrum 시).

## 3. Bound long-wave (infragravity) 생성 — generate_qbcf (:2460) ★

단파 쌍(pair)의 **difference-interaction**(주파수차 Δf)이 만드는 2차 bound 장파(infragravity). 파군(wave group) 아래 묶인 IG 파:
- **Energy** (Herbers 1994 eq. 1, :2640):
  ```
  E_forc = 2·D²·S²·dθ²·df  =  2·D²·Sf²·df
  ```
  `D` = **difference-interaction coefficient**(상호작용 primary wave 쌍의 2차 강제 계수), `S`/`Sf` = primary wave 에너지밀도. 모든 freq-pair (m=1..K-1) 합산.
- **Phase** (Van Dongeren 2003 eq. 21, :2602): primary wave 강제와의 **국소평형** 가정 → bound wave 위상 = `π + imag(log(CompFn*)) 차`(Fourier 켤레곱의 편각).
- **Angle** (Van Dongeren 2003 eq. 22, :2612): `theta3 = atan2(KKy, KKx)` (상호작용 파수벡터 차의 방향).
- **shallow-water 보정**(`par%nmax`): 얕은 물에서 bound wave variance 과대 방지(:2568).
- longshore point(npb)별로 별도 계산(spatial phase: 참조점 거리 `distx/disty` × 파수).

→ 결과: 경계에서 단파(short wave) + **bound 장파(IG flux qbcf)** 시계열 → surfbeat 흐름 경계조건. surfzone 에서 bound IG 가 풀려(release) free IG 로 → swash/runup 의 주 에너지원.

## 4. SWAN ↔ XBeach 연동 chain (전체)

```
SWAN run → 2D spectral output(VaDens/EnDens, FACTOR)
  → read_swan_file (specin%S(f,θ))           [[xbeach_swan_handoff]] (읽기·보간)
  → generate_wave_boundary_surfbeat (Fourier train + envelope)
  → generate_qbcf (bound IG: Herbers/Van Dongeren)   [본 노트]
  → 경계 forcing(short + bound IG)
  → wave_instationary 파작용 전파 + flow      [[xbeach_wave_action_balance]]/[[xbeach_flow_solver]]
```
- **one-way nesting**: SWAN(regional 파랑) → XBeach(surfzone). EFDC 의 SWAN 결합([[efdc_waves]] GETSWAN)과 동일 철학(SWAN=offshore 파랑 공급).
- SWAN 방향 convention 변환: `dthetaS_XB`(SWAN nautical → XBeach x-axis 반시계, :916).

## 5. 연결

- [[xbeach_swan_handoff]] — read_swan_file SWAN 스펙트럼 읽기·보간(본 노트의 입력단)
- [[xbeach_wave_boundary]] — wbctype·JONSWAP·BCF 파일구조·directional spreading
- [[xbeach_wave_action_balance]] — 생성된 경계파가 들어가는 내부 파작용 solver
- [[xbeach_flow_solver]] — bound IG → surfbeat 흐름
- [[swan-output-formats]] / [[swan-spectral-file-format]] — SWAN 출력측 포맷
- Herbers et al. 1994 / Van Dongeren et al. 2003 / Hasselmann 1962 (bound long wave 2차 이론)
