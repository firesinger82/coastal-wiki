---
title: "EFDC+ 퇴적물 diagenesis source-analysis — mod_diagen.f90 (Cerco-Cole/Di Toro 2-layer sediment flux, SOD Brent 폐합)"
topic: efdc-sediment-diagenesis
canonical_source: self
citation_status: verified
verification_method: "EFDC+ Stable(12.4, sha 3ed76b6) raw source 직접 read: Eutrophication/mod_diagen.f90(1394) — SOD ZBRENT root(:969)·ammonium 벤딕 flux(:998)·s=SOD/O2 closure(:1177) file:line 직접 검증. 소스주석 primary Numerical Recipes(:1259). 범위=SMMBE 드라이버 + ammonia/nitrification 2-layer flux(H2S/CH4/PO4/Si 요약). [[efdc_water_quality]] 는 dispatch만·[[efdc_rpem_vegetation]] 은 pool 소비만."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-07
verification_by: "Claude Opus 4.8 (1M context) — mod_diagen.f90:967-975·996-1001·1174-1179 직접 read 검증"
verification_date: 2026-07-07
related:
  - models/EFDC/source-analysis/efdc_water_quality.md
  - models/EFDC/source-analysis/efdc_rpem_vegetation.md
  - models/EFDC/source-analysis/sediment/efdc_sedzlj.md
---

# EFDC+ 퇴적물 diagenesis — `mod_diagen.f90` (`WQ_DIAGENESIS`)

> 소스: [`Eutrophication/mod_diagen.f90`](../raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90) (1394). EFDC+ Stable = 12.4.
> **정체**: Cerco-Cole 1994(CE-QUAL-ICM) / Di Toro 2001 **2-layer 퇴적물 flux** 서브모델. **pore-water pool `SM2NH4/NO3/PO4` + 벤딕 flux `WQBFNH4/NO3/PO4D/O2(SOD)/COD` 생산** — [[efdc_rpem_vegetation]]·수질 F1 이 이 pool 을 소비. [[efdc_water_quality]]:98-104 은 dispatch(`IWQBEN==1`·`SMMBE`)만, flux 알고리즘 미문서.
> ★**line range 정정**: water_quality:21 은 `mod_diagen.f90:9-1031` 이라 했으나 module `END`는 :1107, **flux kernel(SEDFLUXNEW/ZBRENT/SOLVSMBE)은 :1121-1393** — stale 인용은 solver 전체를 놓침.

## 0. 구조

| 서브루틴 | 라인 | 역할 |
|---|---|---|
| `SMRIN1_JNP` | 95-580 | `wq_3dsd.jnp` 입력 + **온도의존 Arrhenius θ^(T-20) 테이블 구성**(:481-503) |
| `WQSDICI` | 591-662 | 초기조건(POM G-class·pore-water 농도) |
| `SMMBE` | 674-1105 | **master 드라이버**: deposition→POM 물질수지→diagenesis flux→benthic stress→mixing→셀별 NH4/NO3/H2S/CH4/PO4/Si flux |
| `SOLVSMBE` | 1121-1141 | 2×2 2-layer 선형계(Cramer) |
| `SEDFLUXNEW` | 1152-1237 | **flux kernel**: 시행 surface transfer coeff 로 NH4→NO3→H2S/CH4 순차해 → SOD residual |
| `ZBRENT` | 1263-1393 | Brent 근찾기(SOD/표면전달계수, Numerical Recipes p.253) |

## 1. POM G-class diagenesis (SMMBE)

```fortran
SMTDCD(IT,M) = SMKPOC(M)*SMTHKC(M)**TT20                          ! :484 3 G-class(G1 반응성/G2 난분해/G3 불활성) Arrhenius
! deposition(algae WQDFB + refractory + labile G1) :774-790
SMPOC(L,M) = (SMPOC + SMDFC*SMDTOH)/(SMW2DTOH + SMTDCD*DTWQ)      ! :816 POM 물질수지(burial+decay, 2-layer)
SMDGFN(L)  = SMHSED*(SMTDND(,1)*SMPON(,1) + SMTDND(,2)*SMPON(,2)) ! :824 G1+G2 → diagenesis flux(N/P/C, pore-water 공급)
```
particle mixing `SMW12=SMDP·SMTDDP·SMPOC(,1)·O2/(SMKMDP+O2)`(:887) + 확산 `SMKL12=SMDD·SMTDDD+SMRBIBT·SMW12`(:888) — layer1↔2.

## 2. Ammonia/nitrification 2-layer + ★SOD Brent 폐합

```fortran
SK1NH4SM = SMKNH4*SMTDNH4*O2/((SMKMO2N+O2)*(SMKMNH4+SM1NH4))     ! :936 nitrification 2-Monod(O2·NH4)
! ammonia 2-layer 계수 A1/A2NH4SM, source B2NH4SM = SMDGFN + SMHODT*SM2NH4  :937-941
SMSOD = ZBRENT(L, ..., SK1NH4SM,A1NH4SM,..., SM2NH4(L),...)      ! :969 ★SOD = flux balance 의 근(Brent)
RSMSS = SMSOD1/(XSMO20(L)+1.E-18)                                ! :1177 ★s=SOD/O2(0) Di Toro 폐합
RNSODSM = SMO2NH4*RJNITSM ; SMSOD = CSODSM + RNSODSM             ! :1232 SOD = 탄소성(H2S/CH4) + 질소성(nitrification)
WQBFO2(L) = -SMSOD*SODMULT(IZ)                                    ! :989 SOD 벤딕 flux
WQBFNH4(L) = SMSS(L)*(SMFD1NH4*SM1NH4(L) - WQV(L,KSZ(L),INHX))    ! :998 암모늄 flux(g NH4/m2/day)
WQBFNO3(L) = SMSS(L)*(SM1NO3(L) - WQV(L,KSZ(L),INOX))            ! :999
WQBFCOD(L) = SMJAQH2S(L) - SMSS(L)*WQV(L,KSZ(L),ICOD)            ! :1000
```
kernel 순차해(SEDFLUXNEW): NH4→NO3(layer1 source = nitrification 산물 `RJNITSM`:1192, 양층 denitrif)→H2S/CH4(:1179-1231), 2×2 판별식 solver(:1131).

## 3. 병렬 flux (요약)
- **염분 switch H2S vs CH4**(:954 `SAL>SMCSHSCH` 황화물 else 메탄): 메탄 `CSODMSM=min(√(SMCH4S·SMJ2H2S),SMJ2H2S)` + sech gas-escape(:1219-1229).
- **인산 DO의존 sorption power-law**(:1009 `SMP1PO4=SMP2PO4·SMDP1PO4**(O2/SMCO2PO4)`, O2<임계 시 호기층 P trapping) + 2-layer 해 → `WQBFPO4D`(:1025). silica 동형(:1042).

## 4. 주요 findings
- **★SOD 은 입력 아니라 implicit 해**(Brent root :969, bound RMIN 1e-4/RMAX 100 g O2/m²/d, `s=SOD/O2` 순환폐합 :1177) — 매뉴얼은 흔히 SOD 를 입력 파라미터로 제시. 미수렴 시 `ZBRENT.LOG` 기록(:1090).
- **solve order 강제** NH4→NO3→H2S(SEDFLUXNEW) — CE-QUAL-ICM 은 결합식이나 코드는 순차.
- **P sorption power-law**(step 아님, 연속 지수 ramp) — 단순설명의 binary on/off 와 대조.
- **퇴적물 온도 = 확산/relaxation 상태**(:744 `SMT=(SMT+SM1DIFT·TEM)·SM2DIFT`, 저수온 lag), 범위밖 시 `ERROR.LOG`+clamp(정지 아님).
- **메탄 sech gas-escape 를 단일 염분비교(SMCSHSCH)로 switch** — 기수/하구 보정 주의점.
- **line range stale**(water_quality:21 `9-1031` → kernel :1121-1393 누락).

## 5. Primary sources
- **Cerco & Cole 1994** *Three-Dimensional Eutrophication Model of Chesapeake Bay*(CE-QUAL-ICM, USACE TR EL-94-4) — 직접 부모(water_quality:223 은 1995 저널판 인용).
- **Di Toro 2001** *Sediment Flux Modeling*(Wiley) — 2-layer 호기/혐기 물질수지·`s=SOD/[O2(0)]` 폐합·G-class·SOD root의 정본.
- **Press et al. Numerical Recipes** p.253 — Brent `ZBRENT`(소스 in-code :1259).

## 6. 관련
- [[efdc_water_quality]] — WQSKE1 수관 eutrophication(diagenesis 는 저면 flux 공급, ★:21 line range 정정 대상)
- [[efdc_rpem_vegetation]] — SM2NH4/NO3/PO4 pool 소비처(본 노트가 생산 측)
- [[efdc_sedzlj]] — POM deposition source(diagenesis 입력)
