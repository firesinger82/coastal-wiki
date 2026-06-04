---
title: "XBeach 인프라·유틸 맵 — spaceparams(spacepars 상태 derived type) + math_tools(Singleton FFT/Hilbert/random) + varianceupdate(on-the-fly 분산) + wetcells(wet/dry mask) + wave_timestep(wave 갱신 dispatcher) + drifters + BMI(C 결합 interface)"
topic: xbeach
canonical_source: self
citation_status: verified
verification_method: "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/ 직접 read — spaceparamsdef.F90(type spacepars 5-55, index imin_ee 등) + math_tools.F90(Singleton FFT/Hilbert/random 3-31) + varianceupdate.F90(variance2d/3d/4d pointer) + wetcells.F90(compute_wetcells 7) + wave_timestep.F90(wave 34, wavint mod 78) + xbeach_bmi.f90(initialize/update C bind 43-62) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — 인프라·유틸 모듈 인벤토리 verbatim"
verification_date: 2026-06-03
related:
  - models/XBeach/source-analysis/xbeach_flow_solver.md
  - models/XBeach/source-analysis/xbeach_wave_action_balance.md
  - models/XBeach/source-analysis/xbeach_output.md
---

# XBeach 인프라·유틸 맵

> XBeach 의 **지원(infrastructure) 모듈** 종합 — 물리 solver 가 아닌 자료구조·수치도구·결합 interface. 전 소스 커버 완결용(개별 deep 대신 역할 map).

## 1. spaceparams / spaceparamsdef — 상태 자료구조 ★

- `spaceparamsdef.F90`(61): **`type spacepars`**(5-55) = XBeach 전 상태배열의 derived type `s%*`(zb·zs·uu·vv·hh·ee·rr·H·theta·cf·Fx … 수백 필드). 모든 solver 가 `s` 로 상태 공유.
- `spaceparams.F90`(1534): spacepars 할당/관리(`gridprops`) + **index 범위**(`imin_ee/imax_ee`, `imin_uu`… = 계산영역 인덱스 한계, MPI subdomain). 배열 할당·복사·MPI 분배.

## 2. math_tools.F90 — 수치 도구

- **Singleton FFT**(complex transform, fftn.c 이식) — 스펙트럼·파 boundary 생성([[xbeach_wave_boundary_generation]]) Fourier.
- **Hilbert transform** — 파 envelope(analytic signal, bound wave variance).
- **random function** — 랜덤위상 단파 train 생성.
- interp1 등 보간.

## 3. varianceupdate.F90 — on-the-fly 분산

- 출력용 **분산(variance) 누적**(variance2d/3d/4d pointer): 시간변동(wave/IG envelope·통계)을 매 step 누적해 평균·표준편차 출력([[xbeach_output]]). H_rms·long-wave variance 등.

## 4. wetcells.F90 — wet/dry mask

- `compute_wetcells`(:7): `wete`(cell wet/dry) + `wetu/wetv`(u/v-point) mask 산출(hh > 임계). [[xbeach_flow_solver]] 의 dry-cell skip·boundary 처리에 사용. weteb(이전 step) 비교.

## 5. wave_timestep.F90 — wave 갱신 dispatcher

- `wave(s,par)`(:34): wave 모델 갱신을 **`wavint` 간격**으로 호출(`mod(t,wavint)<…`, :78) — flow 보다 큰 간격으로 wave 갱신(파는 천천히 변, 계산 절감). [[xbeach_mode_dispatch]] 가 surfbeat/stationary/nonh 중 어느 wave solver 를 부를지 결정, 이 dispatcher 가 timing.

## 6. drifters.F90 — Lagrangian

- `drifters.F90`(69): Lagrangian drifter 추적(입자 위치를 흐름으로 advect). 출력 진단([[xbeach_output]]).

## 7. BMI — xbeach_bmi.f90 / libxbeach / iso_c_utils

- **BMI(Basic Model Interface)**: `initialize(configfile)`/`update(dt)`/`get_var`/`set_var`/`finalize` C-bindable(`bind(C)`) interface(:43-62) — XBeach 를 외부(Python BMI·coupling framework·BMI-OpenEarth)에서 제어. `libxbeach`(dynamic library) + `iso_c_utils`(C interop 문자열). 모델 결합·실시간 제어용.
- **자료동화(DA)**: 이 BMI(`get_var`/`set_var`)가 **OpenDA**(EnKF/DUD black-box) 결합점 — XBeach 는 native adjoint 없이 BMI 로 DA. 관측 동화 bathymetry 는 [[xbeach_beachwizard]]. ★ 모델별 DA framework 비교는 [[roms_adjoint_framework]] §4(ROMS=native 변분 / XBeach·Delft3D=OpenDA / ADCIRC=외부 ensemble).

## 8. 연결

- [[xbeach_flow_solver]] / [[xbeach_wave_action_balance]] — spacepars `s` 상태 공유, wetcells mask
- [[xbeach_wave_boundary_generation]] — math_tools FFT/Hilbert/random
- [[xbeach_output]] — varianceupdate·drifters 출력
- [[xbeach_mode_dispatch]] — wave_timestep wave() dispatcher
