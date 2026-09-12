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
source_correction_date: 2026-09-12
source_correction_by: "Codex"
source_correction_scope: "`form`의 허용 입력 12개와 실제 공식 호출 네 루틴, `intrasedtr` 명시 입력을 구분"
source_correction_human_approval: not-issued
---

> **2026-09-12 AI 출처 정정**: `form`의 허용 입력 12개와 실제 공식 호출 네 루틴, `intrasedtr` 명시 입력을 구분. 위 `verification_*`는 이전 검증 이력이며 이번 정정의 새 사람 승인을 뜻하지 않는다. [원문 구간·SHA와 재사용 근거](../../../_staging/total-read/model-audit/XBeach/connectivity/corrections-20260912/evidence.json)에 결속했다.

# XBeach intra-wave 유사이동 formulations — `morphevolution.F90`

> 소스: [`xbeachlibrary/morphevolution.F90`](../raw/source_code/trunk/src/xbeachlibrary/morphevolution.F90) (3299). FORM 상수 [`paramsconst.F90`](../raw/source_code/trunk/src/xbeachlibrary/paramsconst.F90).
> `transus`에서 `sedtransform` 외에 직접 호출하는 `Nielsen2006`, `intra_sedtr`, `mccall_vanrijn`을 다룬다. 입력으로 허용하는 이름 수와 실제 공식 호출 분기는 다르다.

## 0. `form` 입력과 `transus` 호출

`sedtrans==1`일 때 `params.F90:928-949`는 `intrasedtr`를 포함한 **12개 이름**을 입력 목록에 등록한다. `parmapply`는 이름을 상수 값으로 바꾸며, 과거 숫자 문자열 `1`~`12`는 각각 상수 값 `0`~`11`에 대응한다. 일반 설정의 기본값은 두 번째 이름 `vanthiel_vanrijn`, `useXBeachGSettings!=0`이면 다섯 번째 이름 `mccall_vanrijn`이다. (`paramsconst.F90:80-91`; `readkey.F90:762-804, 806-824, 866-875`)

| 입력 이름 | 상수 값 | `transus`가 직접 호출하는 공식 루틴 |
|---|---|---|
| `soulsby_vanrijn`, `vanthiel_vanrijn`, `vanrijn1993` | 0, 1, 2 | `sedtransform` |
| `nielsen2006` | 3 | `Nielsen2006` |
| `mccall_vanrijn` | 4 | `mccall_vanrijn` |
| `intrasedtr` | 11 | `intra_sedtr` |
| `wilcock_crow`, `engelund_fredsoe`, `mpm`, `wong_parker`, `fl_vb`, `fredsoe_deigaard` | 5~10 (표기 순서) | 해당 SELECT에 공식 호출 분기 없음 |

이 SELECT에는 `DEFAULT`도 없다. 따라서 5~10은 위 네 공식 루틴을 호출하지 않은 채 뒤의 공통 수송 계산으로 진행한다. 이를 입력 오류 종료나 특정 수치 결과로 해석하지 않는다. `Nielsen2006`과 `mccall_vanrijn` 분기만 `bulk==0`이면 호출 직후 `transus`에서 복귀한다. (`morphevolution.F90:173-204`; `transus` 상위 호출 조건은 `libxbeach.F90:293-310`)

`mccall_vanrijn` 내부에 `FORM_WILCOCK_CROW`와 `FORM_ENGELUND_FREDSOE` 비교가 존재하지만, 그것만으로 해당 입력 값이 이 루틴에 도달한다고 볼 수 없다. 직접 호출자는 위 SELECT다. (`morphevolution.F90:2565-2576`)

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
> **`form=intrasedtr`는 사용자가 설정할 수 있다.** `params.F90:932-943`의 허용 이름과 `morphevolution.F90:182-183`의 호출이 직접 연결된다. nonh용이라는 루틴 헤더는 모드가 이 공식을 자동 선택한다는 근거가 아니다.

## 3. mccall_vanrijn (:2502-2817) — XBeach-G 자갈 sheet-flow
```fortran
Sster = D50/(4ν)·√((rhos/rho-1)·g·D50)                         ! :2581 Soulsby
wster = 1.06·tanh(0.064·Sster·exp(-7.5/Sster²)) + 0.22·tanh(...)·Sster   ! :2581-2585 침강속도
! sheet-flow transport (Eq 10, /rhos → m²/s) :2753
```

## 4. 적용 범위

[[xbeach_morphology]]의 평형농도 설명은 `sedtransform`의 세 입력 값에 해당한다. 전체 입력 목록은 12개이고, 현재 `transus`의 직접 공식 호출은 여섯 값에서 네 루틴으로 연결된다. `intrasedtr`의 명시 입력과 Nielsen/McCall의 `bulk==0` 조기 복귀를 구분해야 한다. (§0 원문 근거)

## 5. Primary sources (소스 verbatim)
- **Nielsen 2006** *Coastal Engineering* — sheet flow, 가속-skewness + BL streaming(§1 anchors).
- **Van Rijn 1984/1993/2007** — 기준농도 eq5 + 부유프로파일(§2).
- **McCall et al. 2014/2015** — XBeach-G 자갈 sheet-flow(§3, [[xbeach_groundwater]]:189 에 XBeach-G 만 인용, transport McCall-Van Rijn 은 미인용이었음).
- **Soulsby 1997** *Dynamics of Marine Sands* — 임계 Shields·침강속도.
- **Roelvink et al. 2009** — XBeach 형태역학 프레임.

## 6. 관련
- [[xbeach_morphology]] — 위상평균 equilibrium sedtransform(세 평형농도 입력의 계산 설명; 전체 입력·호출 대응은 본 노트 §0)
- [[xbeach_nonh]] — 비정수압 수력(intra_sedtr 의 유사 짝)
- [[delft3d_sediment_transport_formulae]] — cross-model 유사이동 formulation gateway(van Rijn 계열 대조)
