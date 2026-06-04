---
title: "ROMS 자료동화 framework — NLM/TLM/ADM/RPM 4 모델(각 NL 커널의 exact tangent-linear+adjoint 수작업 transpose) + I4D-Var/R4D-Var/RBL4D-Var driver + observation sensitivity/array modes. 타 모델 DA 비교"
topic: roms
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/source_code/roms/ROMS/ Adjoint/(65 ad_*.F)·Tangent/(54 tl_*.F)·Representer/(39 rp_*.F) + Drivers/(i4dvar_roms.h/r4dvar/rbl4dvar/obs_sen_*/array_modes/picard.h) 직접 ls + ad_step3d_t.F(adjoint tracer transpose 헤더) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-04
verification_by: "Claude Opus 4.8 (1M context) — NLM/TLM/ADM/RPM + 4dvar driver 구조"
verification_date: 2026-06-04
related:
  - models/ROMS/source-analysis/roms_4dvar.md
  - models/ROMS/source-analysis/roms_support_modules.md
  - models/ROMS/source-analysis/roms_baroclinic_3d.md
---

# ROMS 자료동화(DA) framework

> ROMS `Adjoint/`(65) + `Tangent/`(54) + `Representer/`(39) + `Drivers/` 직접 ls/read. ROMS 의 **변분 자료동화(variational DA)** 의 모델 구조 — [[roms_4dvar]] 가 알고리즘(B-precond·CG·multiscale)을, 본 노트가 **4 모델(NLM/TLM/ADM/RPM)과 driver** 구조를 다룸. coastal/regional 해양 DA 의 gold standard(native 4D-Var).

## 1. 4 모델 (exact transpose 수작업 coding) ★

ROMS 의 모든 NL 커널은 **3종 대응물**을 가짐:
| 모델 | prefix | 역할 |
|---|---|---|
| **NLM** Nonlinear | (none) | 정방향 예보([[roms_baroclinic_3d]] step3d_t/step3d_uv 등) |
| **TLM** Tangent Linear | `tl_` | NLM 의 선형화(perturbation 전파). `Tangent/tl_step3d_t.F` 등 |
| **ADM** Adjoint | `ad_` | TLM 의 **exact transpose**(gradient 역전파). `Adjoint/ad_step3d_t.F` 등 |
| **RPM** Representer | `rp_` | dual-space(관측공간) finite-amplitude TLM. `Representer/` |

- **각 물리 커널마다** 대응: `ad_step2d`/`ad_step3d_t`/`ad_step3d_uv`/`ad_prsgrd`/`ad_rho_eos`/`ad_uv3dmix`… (NL의 prsgrd·rho_eos·advection 모두 손으로 adjoint coding). ad_main2d/3d = adjoint 시간역행 driver.
- **exact adjoint**: TLM 의 정확한 수치 transpose(자동미분 아닌 hand-coded) → gradient 가 cost function 과 정확히 일치(검증된 J↔∇J). ROMS DA 정확도의 핵심.

## 2. 변분 driver (Drivers/) — 3 방법

| driver | 방식 | space |
|---|---|---|
| **I4D-Var** (`i4dvar_roms.h`) | incremental 4D-Var(Courtier) | **primal**(model space, B-precond) |
| **R4D-Var** (`r4dvar_roms.h`) | **representer**(indirect) | **dual**(obs space) |
| **RBL4D-Var** (`rbl4dvar_roms.h`) | Restricted B-preconditioned Lanczos | **dual** |

- 모두 **inner loop**(TLM/ADM 으로 quadratic cost 최소화, CG/Lanczos) + **outer loop**(NLM 재선형화). [[roms_4dvar]] 의 multiscale B·Dirac·CG 가 이 inner loop.
- `split_i4dvar` = 단계 분리 실행. `picard_roms.h` = R4D-Var 의 Picard 반복.
- **observation sensitivity**(`obs_sen_*`): 관측이 예보/분석에 미치는 영향(adjoint of forecast, OSE/OSSE). `array_modes.h` = stabilized representer.

## 3. Control variables

DA 가 조정하는 control: 초기조건(IC) + **boundary**(`obc_adjust`)·**surface forcing**(`frc_adjust`)([[roms_support_modules]] §6) increment. weak-constraint(model error) 옵션.

## 4. ★ 모델별 DA framework 비교 (cross-model)

| 모델 | DA 방식 | 근거 |
|---|---|---|
| **ROMS** | **native 변분(I4D/R4D/RBL4D-Var)** + exact ADM/TLM/RPM | 본 노트 (Adjoint/Tangent/Representer 158 .F) |
| **Delft3D** | **OpenDA**(외부, black-box) — EnKF/DUD ensemble·calibration | `third_party_open/openda` ([[delft3d_dflowfm_kernel_scheme]] BMI) |
| **XBeach** | **OpenDA**(BMI interface, [[xbeach_infrastructure]] §7) + Beach Wizard(관측 동화 bathymetry [[xbeach_beachwizard]]) | black-box ensemble |
| **ADCIRC** | **외부 ensemble**(ASGS, no built-in adjoint) — Kalman/ensemble surge | wgrib2 Ensemble util 만 |
| **SWAN** | 외부(없음, native DA 부재) | — |
| **EFDC** | 외부(없음) | — |

→ **ROMS 만 native exact-adjoint 변분 DA**(가장 강력·검증). 나머지는 OpenDA black-box ensemble(adjoint 불필요, 모델 수정 없이 결합) 또는 외부. coastal surge(ADCIRC)·wave(SWAN)는 주로 ensemble/통계.

## 5. 연결

- [[roms_4dvar]] — 변분 알고리즘(B-precond·multiscale·CG)이 본 framework 의 inner loop
- [[roms_support_modules]] — obc_adjust/frc_adjust(control), exchange
- [[roms_baroclinic_3d]] — NLM 커널(TLM/ADM 의 선형화 대상)
- [[xbeach_beachwizard]] / [[delft3d_dflowfm_kernel_scheme]] — 타 모델 DA(OpenDA)
- Moore et al. 2011 (ROMS 4D-Var system) / Courtier 1997(incremental) / Bennett(representer)
