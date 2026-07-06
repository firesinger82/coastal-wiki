---
title: "XBeach intra-wave 유사이동 formulations source-analysis — morphevolution.F90 (Nielsen2006·intra_sedtr·mccall_vanrijn)"
topic: xbeach-intrawave-sediment-transport
canonical_source: self
citation_status: verified
verification_method: "XBeach raw source 직접 read: xbeachlibrary/morphevolution.F90(3299) — transus dispatch 6형식(:173-190)·Nielsen MPM transport(:2079)·Van Rijn ref conc eq5(:2392) file:line 직접 검증. FORM 상수 paramsconst.F90:83-91. 소스주석 primary Nielsen2006·van Rijn·McCall. [[xbeach_morphology]] 는 equilibrium 3형식만 커버(코드는 6형식)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-07
verification_by: "Claude Opus 4.8 (1M context) — morphevolution.F90:173-190·2076-2081·2389-2397 직접 read 검증"
verification_date: 2026-07-07
related:
  - models/XBeach/source-analysis/xbeach_morphology.md
  - models/XBeach/source-analysis/xbeach_nonh.md
  - models/Delft3D/source-analysis/delft3d_sediment_transport_formulae.md
---

# XBeach intra-wave 유사이동 formulations — `morphevolution.F90`

> 소스: [`xbeachlibrary/morphevolution.F90`](../raw/source_code/trunk/src/xbeachlibrary/morphevolution.F90) (3299). FORM 상수 [`paramsconst.F90`](../raw/source_code/trunk/src/xbeachlibrary/paramsconst.F90).
> **정체**: `transus` 의 `par%form` 6형식 중 **intra-wave(위상해상) 3형식** — 위상평균 equilibrium([[xbeach_morphology]] sedtransform) 밖의 가속-skewness·비정수압·자갈 sheet-flow 유사이동. 코드 ~960줄, 위키 미커버.
> ★**기존 노트는 3형식만 명시**([[xbeach_morphology]]:44-49 soulsby/vanthiel/vanrijn1993→sedtransform), **코드는 6형식**.

## 0. transus dispatch (:173-190)
```fortran
select case(par%form)
 case(FORM_SOULSBY_VANRIJN,FORM_VANTHIEL_VANRIJN,FORM_VANRIJN1993) → call sedtransform   ! 위상평균(xbeach_morphology 소관)
 case(FORM_NIELSEN2006)   → call Nielsen2006 ; if(par%bulk==0) return   ! :177-181
 case(FORM_INTRASEDTR)    → call intra_sedtr                            ! :182-183
 case(FORM_MCCALL_VANRIJN)→ call mccall_vanrijn ; if(par%bulk==0) return ! :185-189
```
FORM 상수(paramsconst.F90): `NIELSEN2006=3`(:83)·`MCCALL_VANRIJN=4`(:84)·`INTRASEDTR=11`(:91). ★**Nielsen/McCall 은 `par%bulk==0` 시 early return** — sedtransform 의 equilibrium/advection-diffusion 기계를 우회.

## 1. Nielsen2006 (:1858-2116) — 가속-skewness bed-shear
```fortran
dstar = (g·(rhos/rho-1)/ν²)^(1/3)·D50                          ! :1936
shieldscrit = 0.3/(1+1.2·dstar) + 0.055·(1-exp(-0.02·dstar))   ! :1937 Soulsby 임계 Shields
factime = min(dt/Tsmooth,1) ; dudtsmooth=(ulocal-ulocalold)/dt  ! :1949-1955 가속 skewness 입력
Arms = sqrt(2)/omegap·sqrt(uvarupd)                            ! :1973 RMS 궤도진폭
if(par%phaselag==1) shields += sin(phi)/omegap·dudtsmooth 항    ! :2002-2006 Nielsen 위상지연 가속
shields = ustar²/(delta·g·D50)                                 ! :2028
! bed-slope 보정(reposedzdx=tan(reposerad) clip) :2037-2049
fe = exp(5.5·(170·√(shields-0.05)·D50/Arms)^0.2 - 6.3)         ! :2061 Nielsen 파 마찰 + streaming
! MPM 형 transport:
qsedu = par%Ctrans·(shields-shieldscrit)·√shields · √(delta·g·D50³)·sign(ustar)   ! :2079 (shields>shieldscrit)
```

## 2. intra_sedtr (:2116-2502) — 비정수압(XBeach-NH) intra-wave
헤더(:2118): "compute sediment transport for nonh (ceqsg, ceqbg, ca_nonh)". 부유+bedload, **bedload 를 농도로 재정식화**(`ceqbg`).
```fortran
ca_nonh = 0.015·(1-pclay)·fsilt·D50/za·taurel^1.5/dstar^0.3    ! :2392 Van Rijn eq5 near-bed 기준농도
where(ca_nonh>=0.05) ca_nonh=0.05                              ! :2395 상한 0.05
! Rouse 프로파일 수심평균:
ceqsg = (za·ca_nonh + (hh-za)·c1mean)/hh                       ! :2442,2472 (c1mean = Rouse number s%rouse)
```
> ★**`FORM_INTRASEDTR=11` 은 `form=` 키워드로 사용자 설정 불가**(params.F90:933-936 목록에 없음) — 비정수압 run 내부 자동선택. [[xbeach_nonh]](수력만 문서화)의 **유사 짝**.

## 3. mccall_vanrijn (:2502-2817) — XBeach-G 자갈 sheet-flow
```fortran
Sster = D50/(4ν)·√((rhos/rho-1)·g·D50)                         ! :2581 Soulsby
wster = 1.06·tanh(0.064·Sster·exp(-7.5/Sster²)) + 0.22·tanh(...)·Sster   ! :2581-2585 침강속도
! sheet-flow transport (Eq 10, /rhos → m²/s) :2753
```

## 4. 주요 findings
- **기존 노트 3형식 주장, 코드 6형식** — [[xbeach_morphology]]:44-49·Decision Guide 가 nielsen2006·mccall_vanrijn·intra_sedtr 누락(transus 는 6 전부 분기).
- **FORM_INTRASEDTR=11 사용자 미설정**(내부 비정수압 경로) — [[xbeach_nonh]] 유사 짝.
- **equilibrium 기계 우회**: Nielsen/mccall `par%bulk==0` early return(:179,187), bedload=농도 `ceqbg`(morphology §E 의 Sub/Svb flux 아님).
- **`par%phaselag`·`par%Ctrans`** 파라미터가 glossary 미등재.

## 5. Primary sources (소스 verbatim)
- **Nielsen 2006** *Coastal Engineering* — sheet flow, 가속-skewness + BL streaming(§1 anchors).
- **Van Rijn 1984/1993/2007** — 기준농도 eq5 + 부유프로파일(§2).
- **McCall et al. 2014/2015** — XBeach-G 자갈 sheet-flow(§3, [[xbeach_groundwater]]:189 에 XBeach-G 만 인용, transport McCall-Van Rijn 은 미인용이었음).
- **Soulsby 1997** *Dynamics of Marine Sands* — 임계 Shields·침강속도.
- **Roelvink et al. 2009** — XBeach 형태역학 프레임.

## 6. 관련
- [[xbeach_morphology]] — 위상평균 equilibrium sedtransform(본 노트가 intra-wave 3형식 보완, 3→6형식 정정)
- [[xbeach_nonh]] — 비정수압 수력(intra_sedtr 의 유사 짝)
- [[delft3d_sediment_transport_formulae]] — cross-model 유사이동 formulation gateway(van Rijn 계열 대조)
