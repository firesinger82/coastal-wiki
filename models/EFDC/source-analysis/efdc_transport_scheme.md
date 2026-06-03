---
title: "EFDC+ scalar transport 수치 스킴 — CALTRAN donor-cell upwind + CALTRAN_AD Smolarkiewicz MPDATA anti-diffusion (ISADAC/ISFCT) + CALCONC dispatch"
topic: efdc
canonical_source: self
citation_status: verified
verification_method: "models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Transport/caltran.f90 (373) + caltran_ad.f90 (347) + calconc.f90 (528) 직접 read. upwind flux FUHUD=UHDY2·CON1(LUPU) + LUPU/LUPV flow-sign upwind index + anti-diffusive pseudo-velocity UHU + cross-derivative MPDATA 항 + ISADAC/ISFCT 입력(input.f90:306/mod_scaninp.f90:117) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — upwind+MPDATA 스킴 + dispatch 구조 verbatim"
verification_date: 2026-06-03
related:
  - models/EFDC/source-analysis/efdc_hydro_core.md
  - models/EFDC/source-analysis/efdc_vertical.md
  - models/EFDC/source-analysis/efdc_water_quality.md
  - models/EFDC/source-analysis/sediment/efdc_sediment.md
---

# EFDC+ scalar transport 수치 스킴 — CALTRAN / CALTRAN_AD

> `Transport/caltran.f90`(373) + `caltran_ad.f90`(347) + `calconc.f90`(528) 직접 read. **모든 scalar(염분·수온·dye·SFL·toxic·SED·SND·WQ)의 advection 수치 알고리즘** = **1차 donor-cell upwind + Smolarkiewicz MPDATA anti-diffusive corrector**. 여러 노트가 CALTRAN 호출 맥락(dry mask·open-BC·vertical)을 다뤘으나, 본 노트는 **advection 스킴 자체**의 canonical. [[efdc_hydro_core]](운동량)·[[efdc_vertical]](연직 advection)·[[efdc_water_quality]]·[[efdc_sediment]]·[[efdc_toxics]] 가 공유.

## 1. CALCONC dispatch (calconc.f90)

scalar transport driver. `ISTRAN(NN)>0` constituent 마다 active water-column(IW) 으로 묶어 transport:
```fortran
ISTRAN: 1 염분 / 2 수온 / 3 dye / 4 SFL(shellfish larvae) / 5 toxic / 6 SED(cohesive) / 7 SND(noncohesive) / 8 WQ
```
1. **upwind cell 사전지정** (`calconc.f90:115-127`):
```fortran
LUPU(L,K) = UHDY2(L,K) >= 0 ? LWC(L) : L     ! x-flux donor cell (서/현)
LUPV(L,K) = VHDX2(L,K) >= 0 ? LSC(L) : L     ! y-flux donor cell (남/현)
```
2. `CALTRAN`(IW) — donor-cell upwind 1차 update (모든 active WC).
3. `ISADAC>0` constituent → `CALTRAN_AD`(IW) — anti-diffusive 보정 (MPI: 그 사이 `Communicate_CON2` 로 FUHUD/FVHUD/FWUU 교환).
4. 그 후 SED/SND(CALSND/bedload, ISTRAN6/7), dye(CALDYE), toxic 등 module-specific.

## 2. CALTRAN — donor-cell upwind (caltran.f90)

### 2.1 upwind flux
```fortran
FUHUD(L,K,IW) = UHDY2(L,K)*CON1(LUPU(L,K),K)   ! line 148 - x-방향 upwind 질량 flux
! (FVHUD = VHDX2·CON1(LUPV), FWUU = 연직 W2·CON1(upwind layer))
```
- `UHDY2/VHDX2` = face 통과 부피수송(u·H·Δy), `CON1` = 이전 시각 농도, `LUPU/LUPV` = 흐름방향 상류 셀.
- **새 농도** (line 170): `CON = CON1 + DDELT·(ΣFUHUD 발산)·DXYIP·HPKI` (DXYIP=1/면적, HPKI=1/층두께).
- → **1차 풍상차분**(donor-cell): monotone·positive 보장하나 **수치확산 큼**.

### 2.2 시간 스텝 DDELT (line 62-77)
- 3TL: `ISTL==3 → DT2`(leapfrog full), `ISTL==2 → DT`(corrector, ISUD=0). 2TL/dynamic: `DT`/`DTDYN`.

## 3. CALTRAN_AD — Smolarkiewicz MPDATA anti-diffusive corrector (caltran_ad.f90) ★

donor-cell 의 수치확산을 상쇄하는 **2차 보정 pass** (2020-01 MPI 분리 split):
```fortran
AUHU  = ABS(UHDY2(L,K))                                    ! line 105
UTERM = AUHU*( POS(L,K) - POS(LW,K) )                      ! 1차 anti-diffusive (확산 = |u|Δx 상쇄)
UTERM = UTERM - 0.5*DDELTA*UHDY2*( VVVV+VVVV + WWWW+WWWW + UUUU+UUUU )  ! line 109-112 cross-derivative (다차원 MPDATA)
UHU   = UTERM/( POS(L,K) + POS(LW,K) + BSMALL )            ! line 114 - anti-diffusive pseudo-velocity
FUHUD(L,K,IW) = max(UHU,0.)*POS(LW,K) + min(UHU,0.)*POS(L,K)  ! line 115 - pseudo-velocity 로 재-upwind
```
- **POS** = 양정치(positive-definite) 농도장, `UUUU/VVVV/WWWW` = 정규화 흐름성분.
- **원리** (Smolarkiewicz 1984 MPDATA): donor-cell 의 implicit 확산을 "anti-diffusive velocity" `UHU = |u|(C_L−C_LW)/(C_L+C_LW)` 로 추정해 반대로 다시 upwind → 수치확산 차수 1→2 향상, **양정치 유지**.
- **cross-derivative 항**(line 109-143)이 다차원 MPDATA 의 핵심(1D 분리오차 보정).

## 4. ISADAC / ISFCT — constituent별 토글 (input.f90:306)

입력 카드(constituent별, C14 염분 ~ ):
```fortran
read ISTRAN(NS), ISTOPT(NS), -, ISADAC(NS), ISFCT(NS), -, -, -, ISCI(NS), ISCO(NS)
```
| flag | 의미 |
|---|---|
| **ISADAC(NS)** | 0 = donor-cell upwind 만(수치확산 큼) / **1 = anti-diffusion(MPDATA) 적용** |
| **ISFCT(NS)** | flux corrector(FCT) — anti-diffusion 후 **monotonicity 보장**(local min/max clamp, caltran_ad CWMAX/CWMIN 등) |
| ISCI/ISCO | concentration input/output series 토글 |

→ **ISADAC=1 + ISFCT=1** = MPDATA + flux-corrected transport (실무 표준: 염분·수온 front 보존). ISADAC=0 = 순수 upwind(안정하나 smearing). `NANTIDIFF` = anti-diffusion 적용 constituent 수 카운트(calconc:93-99).

## 5. 비교·맥락

- **vs 운동량 advection**([[efdc_hydro_core]]): 운동량은 별도(CALUVW 등), 본 스킴은 **scalar 전용**.
- **연직 advection**([[efdc_vertical]] caltran.f90:152-228): 동일 스킴의 연직(FWUU) 성분 + SGZ inactive-layer skip.
- **SED/SND**: CALTRAN 으로 부유사 이송 후 [[efdc_sediment]]/[[efdc_sedzlj]] 가 bed exchange. **toxic**([[efdc_toxics]])도 CALTRAN passenger.
- dry-cell/open-BC 처리: [[efdc_wetdry]]·[[efdc_boundary_conditions]] (LMASKDRY/LKSZ skip).

## 6. 연결

- [[efdc_hydro_core]] — UHDY2/VHDX2 face transport(이 스킴의 입력 flux), 운동량 측
- [[efdc_vertical]] — 연직 advection(FWUU) + SGZ
- [[efdc_water_quality]] / [[efdc_sediment]] / [[efdc_sedzlj]] / [[efdc_toxics]] — CALTRAN 으로 이송되는 scalar
- [[efdc_wetdry]] / [[efdc_boundary_conditions]] — dry mask·open-BC 처리
- Smolarkiewicz P.K. 1984 (MPDATA) — anti-diffusion 알고리즘 lineage(코드 주석 미명시, 구조 기반 식별)
