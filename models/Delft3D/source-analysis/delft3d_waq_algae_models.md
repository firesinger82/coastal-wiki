---
title: "Delft3D WAQ 조류 모델 — BLOOM(LP 다종 경쟁 최적화)·protist(기능군 광합성/성장)"
model: Delft3D
component: waq/waq_process(bloom·protist)
canonical_source: self
citation_status: verified
verification_method: "Delft3D 소스 직접 read (src/engines_gpl/waq/waq_process/). BLOOM: bloom.f90(LP 셋업·구간해법)·setabc.f90(A/B/C 행렬)·maxgro.f90(성장제약)·maxprd.f90(Pmax 온도함수)·natmor.f90(사망률)·constr.f90(소광근)·qslp.f90(simplex)·bloom_data.f90(자료구조) file:line 인용. protist: protistPhotosynthesisFunctions.f90·protistCellFunctions.f90·protistUptakeFunctions.f90·protistMathFunctions.f90·protistGreen.f90(PROGRE)·protistCM.f90(혼합영양) file:line 인용. DYNAMO 는 본 디렉토리에 없음(source-needed)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/source-analysis/delft3d_delwaq.md
  - models/Delft3D/README.md
---

# Delft3D WAQ 조류 모델 — BLOOM·protist

> 식물플랑크톤 동역학 두 패러다임의 소스 분석 (경로: `src/engines_gpl/waq/waq_process/bloom/` · `.../protist/`). BLOOM = 선형계획(LP) 기반 다종 경쟁 평형, protist = Q10·기능군별 quota 동역학. 두 모델 모두 [[delft3d_delwaq]] 프로세스 라이브러리에서 D-Water Quality 의 1차생산 키네틱으로 호출됨.

WAQ 조류 패키지는 두 가지 독립 식물플랑크톤 엔진을 담는다.

| 모델 | 패러다임 | 핵심 알고리즘 | 디렉토리 |
|---|---|---|---|
| **BLOOM II** | 종 경쟁 → 선형계획 평형 | extinction 구간별 LP 최대화 (simplex) | `bloom/` |
| **protist** | 기능군 quota 동역학 | Q10 성장 · Liebig 제한 · sigmoid uptake | `protist/` |
| DYNAMO | (단순 단일종 Monod) | ⚠ 미확인 — 본 디렉토리에 없음 (source-needed) |

---

## 1. BLOOM II — 선형계획 다종 경쟁

### 1.1 핵심 아이디어

BLOOM 은 각 종(type)의 바이오매스를 매 시간스텝마다 **선형계획(LP)** 으로 푼다. 목적함수 = 총 바이오매스(또는 순성장) 최대화, 제약 = 영양염·에너지(광) 제약. 메인 루틴 `bloom` 헤더 주석:

> `!  *    SUBROUTINE FOR SETTING UP AND SOLVING BLOOM MODEL PROBLEM      *` — `bloom/bloom.f90:42`

핵심 통찰: 광 가용성은 총 소광계수 `exttot` 에 의존하는데, 바이오매스 자체가 소광에 기여하므로 비선형이다. BLOOM 은 이를 **소광계수 구간(extinction intervals)** 으로 분할해 각 구간 내에서 LP 가 선형이 되도록 만든 뒤(`spcsd`), 구간별로 LP 를 풀고 최대 바이오매스 해를 선택한다.

- 구간 분할: `200 call spcsd(aroot, oroot, aco, extlim, extb, ni)` — `bloom/bloom.f90:205`
- 구간별 LP 루프: `do j = 1, ni ... call solvlp(...)` — `bloom/bloom.f90:228`,`bloom/bloom.f90:251`

### 1.2 자료구조 (A·B·C 행렬과 차원)

LP 의 표준형 `max C·x s.t. A·x ≤ B` 를 명시적 모듈 변수로 보유 (`bloom_data_matrix`):

- `a(ia,mt)` = A 행렬, `b(ia)` = B 벡터, `c(mt)` = 목적함수 C 벡터 — `bloom/bloom_data.f90:132`–`:134`

차원 파라미터 (`bloom_data_dim`):

- `mt = 30` 최대 type 수, `ms = 15` 최대 species(group) 수, `mn = 8` 최대 영양염 — `bloom/bloom_data.f90:44`–`:46`
- A 행렬 행수 `ia = mn + 2 + 1 + 2*ms` — `bloom/bloom_data.f90:48`; 주석: 영양염 `mn` + 에너지 제약 2 + exclusion row 1 + 종별 사망·성장 제약 `2*ms`

용어 구분(중요): **type** = 한 종의 한 표현형(빛 적응 변종), **species/group** = 생태군. `it2(ms,2)` 가 group→type 범위를 관리 — `bloom/bloom_data.f90:151`. `nuspec` = type 수, `nuecog` = group 수 — `bloom/bloom_data.f90:153`–`:154`. stoichiometry 행렬 `aa(mn,mt)` — `bloom/bloom_data.f90:142`.

### 1.3 LP 행렬 셋업 (setabc)

`setabc` 가 A/B/C 를 채운다. 헤더: `!  *    SUBROUTINE TO SET MATRIX A AND B` — `bloom/setabc.f90:31`.

- 목적함수 초기화 (바이오매스 최대화): `c(j) = 1.0` for all type — `bloom/setabc.f90:84` (주석 `! Initialize "C" values for all species to 1.0: maximize.` `bloom/setabc.f90:82`)
- 광량 변환 (J/cm²/week → J/m²/day): `dsol = 1428.57 * csol` — `bloom/setabc.f90:101`
- 종별 수면 가용광 (윗물층 소광 보정 포함):
  `surf(k) = tcorr(k) * dsol * dexp(- exttot * sdmixn(k) * dep)` — `bloom/setabc.f90:108`
- 영양염 제약 우변 B = 가용 영양염: `b(k) = concen(k)` — `bloom/setabc.f90:114`

### 1.4 최대 1차생산·호흡 (온도함수, maxprd)

`maxprd` 가 온도 의존 Pmax·호흡률을 계산. 헤더 `!  *    SUBROUTINE TO CALCULATE MAXIMAL PRIMARY PRODUCTION AND ... RESPIRATION RATES` — `bloom/maxprd.f90:31`. 주석:

> `!  Calculate the maximum gross growth rate per day as a linear or exponential function of the temperature T.` — `bloom/maxprd.f90:48`–`:49`

온도가 임계값 `temlim` 미만이면 Pmax 를 작은 값 `basmor` 로 설정 (저온 성장 억제), 단 첫 스텝(`nrep==1`)에는 무시 — `bloom/maxprd.f90:54`–`:58`.

### 1.5 광 효율과 소광근 (constr / maxgro)

각 종은 최소 광효율 요구량 `emin` 을 가진다:

`emin(k) = (resp(k) + rmort(k)) / (pmax(k) * daym)` — `bloom/bloom.f90:123`

즉 (호흡+사망)을 (일조보정 Pmax)로 나눈 값 — 종이 양의 순성장을 내려면 광효율이 이 값을 넘어야 한다. `daym` 은 일장(daylength) 보정 계수의 시간 보간 — `bloom/bloom.f90:121`.

`constr` 이 종이 살아남을 수 있는 소광계수 범위(roots)를 계산. 헤더 `!  *    SUBROUTINE TO DETERMINE LIMITS ON THE EXTINCTION COEFFICIENT` — `bloom/constr.f90:4`. `root(2)` (UKmax, num_layers_grid root) 가 그 종이 견딜 수 있는 최대 소광: `root(2) = phi / dmix` — `bloom/constr.f90:77`; `bloom.f90` 에서 `call constr(surf(k), dep, emin(k), root, j)` 로 호출 — `bloom/bloom.f90:142`.

`maxgro` 가 성장 제약의 우변을 계산. 헤더 `!  *  SUBROUTINE TO CALCULATE MAXIMUM ATTAINABLE EQUILIBRIUM VALUES BASED UPON THE INITIAL GROWTH RATE` — `bloom/maxgro.f90:31`–`:33`. 핵심 성장 제약식 (지수 성장):

`bt = dexp(((pmax(iskmax) - lpmort*rmort(iskmax))*effi - resp(iskmax)) * tstep)` 이어서 `bt = bt * xinit(j)` — `bloom/maxgro.f90:106`–`:108`

즉 다음 평형 바이오매스 상한 = `초기 바이오매스 × exp((효율보정 Pmax − 호흡)·Δt)`. `effi` 는 광효율(`aveffi` 또는 3D-light 효율). 만약 `root(2) ≤ exttot`(종이 현 소광을 못 견딤)이면 목적함수에 작은 값 0.01 부여(빨리 소멸) — `bloom/maxgro.f90:80`–`:82`. 순성장 최대화 옵션(`lobfun==1`)이면 C 벡터에 순성장률 저장: `c(k) = dmax1((effi*pmax(k) - resp(k)), 1.0d-6)` — `bloom/maxgro.f90:124`.

### 1.6 자연 사망 (natmor)

헤더 `!  *  SUBROUTINE TO SET,CALCULATE OR CALIBRATE NATURAL MORTALITY RATE CONSTANT` — `bloom/natmor.f90:3`–`:5`. 저온(`temp < temlim`)이면 기저 사망률 `basmor`, 그 외엔 온도 지수함수:

`rmort(i) = rmort1(i) * tmpcor ** temp2` — `bloom/natmor.f90:62`

`rmort2(i) < 0` 인 종은 선형 온도 보정으로 전환 — `bloom/natmor.f90:63`–`:65`.

### 1.7 LP 솔버 (solvlp → qslp)

`solvlp` 은 구간별로 불필요한 변수·제약(redundant)을 제거해 LP 크기를 줄여 속도를 높인다. 주석:

> `! A considerable increase in speed is obtained by dropping all variables and constraints from consideration which are redundant for a particular extinction interval. These are: 1. All types not considered in an interval. 2. All constraints with a zero value... 3. All constraints with only zero A coefficients...` — `bloom/solvlp.f90:52`–`:58`

실제 simplex 는 `qslp`: `! QSLP Quick Simplex algorithm to solve a Linear Program. The technique used here is a variant of the primal - dual algorithm.` — `bloom/qslp.f90:32`–`:33`. 차원 초과 시 에러 1000 반환 — `bloom/qslp.f90:53`.

### 1.8 BLOOM 흐름 요약

```
bloom (bloom.f90)
  ├─ maxprd        Pmax(T), resp(T)               bloom.f90:94
  ├─ setabc        A·B·C 행렬, surf(k) 가용광        bloom.f90:101
  ├─ constr/maxgro 종별 소광근·성장제약 우변         bloom.f90:142,:183
  ├─ spcsd         소광계수 구간 분할               bloom.f90:205
  └─ 구간 루프: exclud → solvlp → qslp → print6   bloom.f90:228–255
```

---

## 2. protist — 기능군 quota 동역학

### 2.1 패러다임과 프로세스 루틴

protist 는 종을 **기능군(functional group)** 으로 모델링: green(독립영양 PROGRE), diatom(PRODIA, Si 추가), CM(constitutive mixotroph, PROCM), NCM(non-constitutive mixotroph), zoo(순포식). 각 루틴은 WAQ 프로세스(`process_space_real`/`fl`/`ipoint` 인터페이스)로 구현 — 예: `subroutine PROGRE(process_space_real, fl, ipoint, ...)` — `protist/protistGreen.f90:11`.

함수 라이브러리는 도메인별로 분리:
- `protist_photosynthesis_functions` — `protist/protistPhotosynthesisFunctions.f90:35`
- `protist_cell_functions` — quota·status·respiration·growth·mortality — `protist/protistCellFunctions.f90:37`
- `protist_uptake_functions` — 영양염 흡수 — `protist/protistUptakeFunctions.f90`
- `protist_math_functions` — normalize·monod·sigmoid — `protist/protistMathFunctions.f90`

### 2.2 온도 의존 성장 (Q10)

protist 는 BLOOM 의 지수 온도식과 달리 **Q10 접근**:

`rate = referenceRate * Q10**((Temp - referenceTemp) / 10.0)` — `protist/protistCellFunctions.f90:84` (함수 `Q10rate`)

PROGRE 에서 최대 성장률·기저호흡·사망률 모두 Q10 으로:
- `UmT = Q10rate(UmRT, Q10, Temp, RT)` — `protist/protistGreen.f90:220`
- `BR = basal_respiration(UmT, CR)` = `maxUmT * CR` — `protist/protistGreen.f90:221`, `protist/protistCellFunctions.f90:62`
- `mrt = Q10rate(MrtRT, Q10, Temp, RT)` — `protist/protistGreen.f90:271` (사망 블록)

### 2.3 영양염 quota 와 Liebig 제한

세포 내 quota = `protNut/protC` (`quota`) — `protist/protistCellFunctions.f90:46`. 영양염 상태(0~1)는 각 원소별:

- N: `statusNC` = normalize(NC, NCmin, NCopt) 를 [0,1] clamp — `protist/protistCellFunctions.f90:73`–`:81`
- P: `statusPC` = Gompertz sigmoid `L*exp(-b*exp(-k*x))` — `protist/protistCellFunctions.f90:86`–`:94`, `protist/protistMathFunctions.f90:48`
- Si: `statusSC` = `min(monod(resource)*NCopt/NCmin, 1.0)` — `protist/protistCellFunctions.f90:99`–`:103`

성장 제한은 **Liebig 최소법칙** (가장 부족한 영양소가 율속):

`NPCu = min(NCu, PCu)` — `protist/protistGreen.f90:228` (주석 `! Determine minimum of N-P-Si limitation; Liebig-style limitation of growth (NPCu)` `protist/protistGreen.f90:224`)

### 2.4 영양염 흡수 (sigmoid uptake)

흡수는 단순 Monod 가 아니라 **이중 sigmoid acquisition potential**: quota < opt 이면 흡수 가속, quota > max 이면 감속. P 흡수(`uptakeP`):

`up = optUptake*APincrease*yFactor + optUptake*APdecrease` — `protist/protistUptakeFunctions.f90:91`

여기서 `optUptake = monod(resource, halfSat)*maxUmT*NutCopt` — `protist/protistUptakeFunctions.f90:88`, APincrease/APdecrease 는 `sigmoidLogistic` — `protist/protistUptakeFunctions.f90:78`,`:82`. NH4 흡수(`uptakeNH4`)는 추가로 **P 상태가 N 상태보다 나쁘면 N 흡수를 억제**하는 상호작용(`interactionP`) — `protist/protistUptakeFunctions.f90:48`–`:53` (주석 `! only if P status worse then N status then NutCvalue changed` `:48`).

### 2.5 광합성 (Smith 식 깊이적분)

핵심 PE 곡선은 **Smith 방정식의 깊이적분 형태**. 최대 광합성 plateau:

`plateau = ((1.0+PSDOC)*maxUmT*maxPSreq*relPS*(1.0 + NCopt*(redco+anaResp))*NPSiCu) + BR + 1e-6` — `protist/protistPhotosynthesisFunctions.f90:51`

총 광합성(`grossPS`)은 Smith 곡선의 깊이적분 (intermediateVal 의 arcsinh 차):

`grossPhotoRate = plateau * (log(iv + sqrt(1+iv²)) - log(iv*exat + sqrt(1+(iv*exat)²))) / (atten + tiny)` — `protist/protistPhotosynthesisFunctions.f90:71`–`:72`, where `intermediateVal = (alpha*ChlC*PFD*numSecPerDay)/plateau` — `:69` (주석 `! ... according to the Smith equation` `:68`).

순광합성 = `grossPhotoRate*(1.0 - PSDOC)` (`netPS`) — `protist/protistPhotosynthesisFunctions.f90:80`. PROGRE 에서:
`Cfix = netPS(PS, PSDOC)` — `protist/protistGreen.f90:246`.

엽록소 합성(`synthesisChl`)은 광순응(photoacclimation): 광합성이 plateau 대비 부족하면 Chl 증가, sigmoid logistic 으로 quota 정규화 — `protist/protistPhotosynthesisFunctions.f90:96`.

### 2.6 호흡·C 성장·사망

총 호흡은 질산환원(`redco*upNO3`)·동화비용(anaResp)·기저호흡을 합산:

`totR = (redco*upNO3) + anaResp*(upNH4+upNO3+assN*propLostIngC) + (assC*propLostIngC) + BR` — `protist/protistCellFunctions.f90:106`

순 C 성장률 `Cu = Cfix + assC - totR` (`CgrowthRate`) — `protist/protistCellFunctions.f90:120`. PROGRE(독립영양)는 포식 없으므로 `Cu = Cfix - totR` — `protist/protistGreen.f90:262`, 순1차생산 `NPP = Cu * protC` — `protist/protistGreen.f90:266`. 사망률 = `mortQ10 * frac`(autolysis/detritus 분배) — `protist/protistCellFunctions.f90:127`.

### 2.7 혼합영양 (constitutive mixotroph, PROCM)

`PROCM`(protistCM.f90)은 광합성 + 포식을 동시에. prey 입력은 종당 `nrPreyInp = 8` 필드 — `protist/protistCM.f90:77`, `nrPrey` = proc_def 에서 읽은 총 먹이종 수 — `protist/protistCM.f90:95`,`:168`. `protist_phagotrophy_functions` 사용 — `protist/protistCM.f90:45`. 포식 동화량 `assC, assN, assP` 가 `totalRespiration`/`CgrowthRate` 에 들어가 광합성과 함께 성장에 기여 — `protist/protistCM.f90:139`. 운동성(motility)은 먹이 포획용 유영속도 (Flynn & Mitra 2016 인용):

`velProt = C_velProt*(a*ESD**k) + small`, a=38.542, k=0.5424 — `protist/protistCellFunctions.f90:140`–`:143` (주석에 citation `protist/protistCellFunctions.f90:133`–`:135`).

---

## 3. BLOOM vs protist 비교

| 항목 | BLOOM II | protist |
|---|---|---|
| 종 경쟁 해법 | LP simplex 평형 (전역 최적) | quota ODE (개별 군 동역학) |
| 온도 성장 | 지수/선형 (`maxprd`) | Q10 (`Q10rate`) |
| 영양염 제한 | LP 부등제약(질량보존) | Liebig min (`NPCu = min`) |
| 광합성 | 효율-소광근 LP 제약 | Smith 식 깊이적분 PE 곡선 |
| 광적응 | type=빛적응 변종 (다 type/group) | Chl:C quota 동역학(photoacclimation) |
| 혼합영양 | 없음(독립영양만) | CM/NCM 기능군 (포식+광합성) |

BLOOM 은 "어느 종 조합이 주어진 자원에서 최대 바이오매스를 내는가"를 LP 로 직접 푸는 **경쟁-평형** 모델인 반면, protist 는 각 기능군의 세포 quota·생리를 시간적분하는 **mechanistic** 모델이다.

---

## 4. 미확인 / source-needed

- **DYNAMO**: 검수 초점에 언급되었으나 `bloom/`·`protist/` 디렉토리에 없음. WAQ 프로세스 라이브러리 다른 위치(단순 Monod 단일종)로 추정되나 본 분석 범위에서 미확인 — source-needed.
- 3D-light(`active_3dl`) 효율 계산 `effi_3dl`/`effic_3dl` 내부(`bloom_data_3dl`)는 헤더만 확인, 본체 미독 — source-needed.
- protist NCM/PFD/Zoo/Diat 루틴의 그룹별 차이(Si·prey·plastid)는 헤더만 확인 — 상세 source-needed.
- WAQ 프로세스 매니저가 BLOOM/protist 를 호출하는 디스패치 경로는 [[delft3d_delwaq]] 참조.
