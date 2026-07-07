---
title: "Delft3D WAQ 저층 산소요구(SOD) source-analysis — sedox.f90 (SODCH4 sech 반복해법 + 메탄 버블 flux + S1/S2 무기화 결합)"
topic: delft3d-waq-sediment-oxygen-demand
canonical_source: self
citation_status: verified
verification_method: "Delft3D raw source 직접 read: waq/waq_process/sedox.f90(533) — SODCH4 sech 반복해법(:469-482)·SOD flux(:247) file:line 직접 검증. 소스주석 provenance orpheus report/Nico sodcard.for(:404-413). [[delft3d_waq_process_library]]:192 의 source-needed(sedox/sedsod/botmin 식 미인용) 해소."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-07
verification_by: "Claude Opus 4.8 (1M context) — sedox.f90:466-485 직접 read 검증"
verification_date: 2026-07-07
related:
  - models/Delft3D/source-analysis/delft3d_waq_process_library.md
  - models/Delft3D/source-analysis/delft3d_waq_kernel_integration.md
  - models/EFDC/source-analysis/efdc_sediment_diagenesis.md
---

# Delft3D WAQ 저층 산소요구(SOD) — `sedox.f90` (SODCH4)

> 소스: [`waq/waq_process/sedox.f90`](../raw/source_code/Delft3D/src/engines_gpl/waq/waq_process/sedox.f90) (533) + cluster `botmin.f90`(190)·`sedsod.f90`(165)·`swoxy.f90`(122).
> **정체**: 저니 **산소요구(SOD)** + 메탄(CH4) 생성/버블. Di Toro 계열 sech 폐형 반복해법. [[delft3d_waq_process_library]]:192 가 "sedox/sedsod/botmin 식 미인용, source-needed" 로 미룬 것을 해소. EFDC diagenesis([[efdc_sediment_diagenesis]] Di Toro 동류)와 cross-model.

## 0. 구조
| 서브루틴 | 라인 | 역할 |
|---|---|---|
| `sedox` | 31-402 | WAQ process wrapper(33 I/O 포인터 IP1-33·strides·셀루프 DO ISEG) → flux `FL(1)=DSOD`·`FL(2)=DOXSOD`(:358-359) |
| `sodCH4` | 407-531 | ★자립 수치 core: 탄소성 SOD 반복해 + 메탄 버블/용존 diffusion(`implicit double precision`, 경계서 single 변환) |
| cluster | botmin/sedsod/swoxy | 저니 무기화·산소요구 침강·S1/S2 산소분배 스위치 |

provenance(:404-413): "orpheus report" + "Nico's `sodcard.for`, renamed SODCH4 (rs11dec96)".

## 1. SOD flux (wrapper)
```fortran
TFSOD = TCSOD**(TEMP-20.)                                  ! :167 온도계수
DSOD  = ZFL/DEPTH + SOD*RCSOD*TFSOD/DEPTH                  ! :247 0차 + 1차 decay, /수심
O2FUNC = (OXY-COXSOD)/(OOXSOD-COXSOD) [0,1 clamp]          ! :182-192 산소제한(piecewise-linear)
DMINER = 2.67*(S1+S2 DetC/OOC flux)                        ! :253 저니 무기화 수요(2.67=gO2/gC)
diagen = DOXSOD*DEPTH + DMINER*DEPTH                       ! :282
```

## 2. ★SODCH4 sech 반복해법 (:449-518)
```fortran
kappac = kapc20*thetak**(temp-20)                          ! :449 전달계수 온도보정
ch4ssd = 99.*(1.+(dep+hsed/2.)/10.)*0.9759**(temp-20)      ! :451 메탄 포화농도 (★0.9759^ = 감소)
csodmx = min(sqrt(2.*kappad*ch4ssd*diagen), diagen)        ! :461 최대 탄소성 SOD
! *** total SOD 고정점 반복:
110 xc = kappac*dowc/sodi                                  ! :469
    sechxc = 2./(exp(xc)+exp(-xc))                         ! :471 hyperbolic secant
    csod = csodmx*(1.-sechxc)                              ! :473
    delta = csod - sodi                                    ! :476
    if(|delta|<=delsod(=0.01)) → 수렴                       ! :479
    sodi = sodi + delta/2. ; go to 110                     ! :481 ★half-step damping(수렴증명·반복상한 無)
! 수렴 후:
lch4s = sqrt(2.*kappad*ch4ssd*hsed²/diagen)                ! :488 메탄 포화깊이
jch4d = sqrt(2.*kappad*ch4ssd*diagen)*sechxc               ! :491 메탄 용존 diffusive flux
if(lch4s<=hsed) jch4g = 0.3502*diagv*(hsed-lch4s)          ! :493 가스생성(0.3502=C→L 변환)
jbt = min(0.0961*jch4g*dep^0.6667/diamb, ...)              ! :499 버블 전달
laero = edwcsd*dowc/csod                                   ! :518 호기층 깊이
```

## 3. S1/S2 저니 무기화 결합 (botmin)
```fortran
TEMFAK = MINRC*MINTC**(TEMP-20)                            ! botmin.f90:158 온도계수
FL = ZEMIN/DEPTH + TEMFAK*ORG/DEPTH                        ! :140 0차 + 1차, CRTEMP 이하 1차항 0(:109-117)
! SWITCH: 산소역치로 S1 vs S2 층 라우팅(:159-166), swoxy.f90 = WC/S1/S2 산소기반 분배
```

## 4. 주요 findings (code≠manual, 개발자 주석)
- **★메탄 double-count guard**: 수렴 시 `DOXSOD` 를 CH4-보정값으로 덮되 `DMINER` 를 빼냄 — 주석 "anders dubbeltelling met BotMin!!!!"(:313-317). sedox↔botmin 결합 제약(단일 process 매뉴얼로는 안 보임).
- **★개발자 미결(Dutch "Te doen")**: 가스버블 블록에 "mag ik dsod gebruiken voor diagen?"·"temperatuurcorrectie niet dubbelop???"·"groot risico dubbeltellingen"(:265-281) — 온도보정·DetC 수요 이중적용 가능성을 코드가 자인. 매뉴얼 부재.
- **수치 guard(식에 없음)**: DOXSOD floor 1e-15(:252)·dowc floor 1e-3(:454)·**half-step damping(:481, 수렴증명·반복상한 없음, 매뉴얼의 direct solve 암시와 다름)**.
- **온도 base 2종 공존**: sedox/botmin `theta^(T-20)`(증가) vs SODCH4 메탄포화 `0.9759^(T-20)`(감소) — 한 process 내 반대 온도민감도.
- **swoxy 런타임 층 라우팅**: flux 가 도달하는 저니층(S1/S2)이 수관 산소의 계산된 함수(정적 config 아님) — 매뉴얼은 고정층으로 제시.

## 5. Primary sources
- **Deltares D-Water Quality Technical Reference(Processes Library Description)** — SOD·SwitchOxyDem·S1/S2 무기화(process명 SEDOX·BMS1/2·SEDOD·SWOXY).
- **Di Toro 2001** *Sediment Flux Modeling*(Wiley) — sech 탄소성 SOD `csod=csodmx(1-sech xc)`·메탄 포화·버블전달 구조.
- **provenance**: orpheus report + Nico `sodcard.for`(rs11dec96, 소스 in-code).

## 6. 관련
- [[delft3d_waq_process_library]] — 프로세스 라이브러리(★:192 source-needed 해소 대상)
- [[delft3d_waq_kernel_integration]] — DELWAQ 적분스킴(SOD flux 소비)
- [[efdc_sediment_diagenesis]] — ★cross-model: EFDC Di Toro diagenesis(SOD Brent vs WAQ sech, 동일 Di Toro 계열 다른 해법)
