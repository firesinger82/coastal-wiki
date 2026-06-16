---
title: "SWASH 식생·다공성 구조물 — Morison 항력(SwashVeget) + Van Gent 다공성 마찰(SwashPorousStruc/PorFricDep/PorFricLay)"
model: SWASH
component: src (vegetation / porous structure friction)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashVeget.ftn90 (Morison 항력·관성 항 적분 cvegu/cvegv 산출, porosity 보정 식생 식 645·684), SwashPorousStruc.ftn90 (Van Gent 마찰계수 aporu/bporu/cporu 식 338-340·354-356), SwashPorFricDep.ftn90 (수심평균 잠수 보정 100-102 + KC 보정 169-170), SwashPorFricLay.ftn90 (다층 layer-resolved 보정 137-143 + w-point bpoks) 의 file:line 직접 인용."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/SWASH/source-analysis/swash-architecture-source-map.md
  - models/SWASH/README.md
---

# SWASH 식생·다공성 구조물 마찰 모델

> 식생 항력(Morison)과 다공성 구조물(porous structure) 마찰을 산출하는 4개 서브루틴 — 식생은 `SwashVeget`, 다공성은 setup `SwashPorousStruc` + 수심평균 `SwashPorFricDep` / 다층 `SwashPorFricLay`. (경로: raw/source_code/swash/src/)

두 메커니즘은 서로 다른 물리 모델이지만 코드상 연결점이 하나 있다 — `iveg==1 .and. iporos/=0` 일 때 식생 항력에 porosity 보정을 적용한다 (`SwashVeget.ftn90:635`). 아래에서 식생 → 다공성 순으로 분석한다.

---

## 1. 식생 항력·관성 — SwashVeget

### 1.1 물리 모델 (Purpose/Method verbatim)

`SwashVeget.ftn90:42-74` 의 헤더 주석 (verbatim 발췌):

- `Calculates vegetation coefficients` (`:42`)
- `The wave damping induced by aquatic vegetation is described by the Morison type equation, modelling the plants as vertical, noncompliant cylinders, neclecting swaying motions induced by waves` (`:46-49`)
- `The drag force consists of viscous effect and form drag around the cylinders which is modelled as one process and is proportional to the square of the characteristic velocity V ... The inertia force due to local acceleration (the time derivative of V) is optionally included` (`:51-55`)
- 조밀 실린더(맹그로브·다공성 브러시우드 groin)는 porosity 효과 포함: `the characteristic velocity is the pore velocity defined as V/n, with n the porosity` (`:57-61`)
- 총력은 `Eq. (61) of Burcharth and Andersen (1995)` 로 주어진다 (`:71-74`).

입력 식생 특성: drag coefficient, vegetation height, plant density, stem diameter (`:65-68`). 코드 내 배열은 `cdveg(l)` (항력계수), `bveg(l)` (줄기 직경 b), `nveg(l)` (식생 밀도 N), `hlayv(l)` (식생 layer 두께) — `:149-150` 에서 사용.

### 1.2 산출 계수 — cvegu / cvegv 구조

식생 효과는 `cvegu(nm,k,1:2)` (u-점) / `cvegv(nm,k,1:2)` (v-점) 두 성분으로 저장:
- 인덱스 `,1` = **항력(drag)** 계수, 인덱스 `,2` = **관성(inertia/added mass)** 계수.

단층(`kmax==1`) u-점 산출 (`:187-188`):
```
cvegu(nm,1,1) = 0.5 * tdragf / hum(nm)         ! drag
cvegu(nm,1,2) = cvm  * work(nm,1)              ! inertia
```
여기서 `work(nm,1) = 0.25 * pi * tinerf / hum(nm)` (`:185`), `cvm` = added mass(관성) 계수.

- **drag 누적** `tdragf += cdveg(l)*bveg(l)*nveg(l)*hlayv(l)` (`:149`) → 차원상 $C_D \, b \, N \, \Delta z$. 0.5 계수가 곱해져 $\tfrac12 C_D b N$ (수심평균) 형태.
- **inertia 누적** `tinerf += nveg(l)*bveg(l)*bveg(l)*hlayv(l)` (`:150`) → $N b^2 \Delta z$. $0.25\pi$ 가 곱해져 실린더 단면적 $\tfrac{\pi}{4}b^2$ 에 대응 (`:185`).

따라서 관성 계수는 $\tfrac{\pi}{4} C_m N b^2$ (단위 부피당 실린더 체적 × added mass), drag 계수는 $\tfrac12 C_D N b$ 형태로 Morison 식의 표준 구조다.

### 1.3 잠수 / 노출(submerged vs emerged) 처리

식생 캐노피가 수심보다 낮으면 전체 적분, 높으면 수면까지만 적분:
- `if ( hum(nm) > hvtot )` → `canopy is submerged` : 전 layer 합산 (`:144-152`). `hvtot = sum(hlayv)` (`:129`).
- else → `canopy is emerged` : `zv` 누적 높이로 수면(`hum(nm)`) 아래 부분만 부분 적분 (`:157-183`). 상부/중부 layer 분기: `upper part of layer or whole layer is vegetated` (`:165`), `lower or middle part of layer is vegetated` (`:170`).

### 1.4 다층(multi-layer) 모드 — layer별 계수

`kmax > 1` 일 때 (`:324` 이후) 각 계산층 k에 대해 별도 산출 (`:387-388`):
```
cvegu(nm,k,1) = 0.5      * tdragf / hkum(nm,k)
cvegu(nm,k,2) = 0.25*pi  * cvm * tinerf / hkum(nm,k)
```
식생 layer(l)와 계산 layer(k)의 교차를 4-way 분기로 처리: `upper part`(`:353`), `lower part`(`:360`), `middle part`(`:367`), `layer is completely vegetated`(`:374`). 층 간 인터페이스 `zkum(nm,k)` (z-level, 위쪽 양수)와 식생 누적 높이 `zvh` 비교.

`fsum` 으로 전 층 inertia 합산 후 `work(nm,1) = 0.25*pi*fsum/hum(nm)` (`:394`) — 이후 porosity 보정에 쓰임.

### 1.5 수평 밀도 변화 — varnpl

`varnpl` 가 참이면 공간변화 식생밀도 `nplaf` 를 곱함 (`:566-630`). u-점은 인접 두 점 평균 `fac = 0.5*(nplaf(nm)+nplaf(ndm))` (`:596`), drag·inertia 양쪽 모두에 적용 (`:598-600`). 영구건조 이웃은 자기값으로 mirror (`:594`).

### 1.6 Porosity 보정 — Burcharth & Andersen Eq.(61) vs (54)

주석: `adapt vegetation coefficients to include porosity effect ... (compare Eq. (61) with Eq. (54) of Burcharth and Andersen, 1995)` (`:632-633`).

두 경로:

| 조건 | porosity np 정의 | drag 보정 | inertia 보정 |
|---|---|---|---|
| `iveg==1 .and. iporos/=0` (`:635`) | `np = nporu(nm)` (외부 porosity 필드, `:643`) | `/np/np/np` (`:645`) | `/np/np` (`:646`) |
| `iveg==2` (`:684`) | `np = 1. - work(nm,1)` (식생 자체 체적분율, `:692`) | `/np/np/np` (`:694`) | `/np/np` (`:695`) |

즉 drag은 $1/n^3$, inertia는 $1/n^2$ 로 나눠 pore velocity $V/n$ 효과를 반영한다. `iveg==2` 의 경우 porosity가 식생 부피로부터 직접 계산됨($n = 1 - $ 단위부피당 식생체적, `:692`) — Method 주석의 "vegetation volume in the unit volume equals 1-n" (`:62-63`)과 일치.

### 1.7 병렬·주기 동기화

`SWEXCHG` 로 subdomain 교환 (`:737-742`), `periodic` 로 repeating grid 동기화 (`:747-752`). 2D에서만 v-성분 추가 교환.

---

## 2. 다공성 구조물 setup — SwashPorousStruc

### 2.1 물리 모델 (Method verbatim)

`SwashPorousStruc.ftn90:44-55` (verbatim):
- `Both laminar and turbulent frictional forces inside porous medium are calculated based on the Darcy and Forchheimer formulation` (`:44-45`)
- `The empirical formula's of Van Gent (1995) are applied` (`:46`)
- `Added mass effect for accelerating fluid in porous medium is included` (`:47`)
- `Note: the intrinsic volume-averaged variables are employed (not the Darcy's averaged variables!) the frictional forces are then multiplied by the volumetric porosity` (`:49-51`)
- 출처: `M.R.A. van Gent (1995) Wave interaction with permeable coastal structures, PhD thesis, Delft` (`:53-55`).

### 2.2 입력 상수

`ppor` 배열에서 추출 (`:97-99`):
- `dsiz = ppor(1)` — grain size $d_{50}$
- `alpha0 = ppor(3)` — 층류(laminar) 마찰 무차원 상수 $\alpha$
- `beta0 = ppor(4)` — 난류(turbulent) 마찰 무차원 상수 $\beta$
- 추가: `ppor(2)` = default 구조물 높이 (`:300-302`), `ppor(5)` = wave period (PorFricDep/Lay 에서 사용, `:80`/`:83`).
- added mass 경험계수 `gamma = 0.34` (parameter, `:69`).

### 2.3 Van Gent 마찰·added mass 식

핵심 식 (1D variable grainsize 경로, `:338-340`; u-점 `:354-356`):
```
apors(nm) = alpha0 * kinvis * (1.-npors(nm))**2. / ( npors(nm)*npors(nm)*dsiz*dsiz )
bpors(nm) = beta0  * (1.-npors(nm))             / ( npors(nm)*npors(nm)*dsiz )
cpors(nm) = gamma  * (1.-npors(nm))             /   npors(nm)
```
LaTeX (n = porosity, $\nu$ = `kinvis` 동점성, d = grain size):

- **층류(Darcy)**: $a = \alpha \dfrac{\nu (1-n)^2}{n^2 d^2}$
- **난류(Forchheimer)**: $b = \beta \dfrac{(1-n)}{n^2 d}$
- **added mass**: $c = \gamma \dfrac{(1-n)}{n}$, $\gamma = 0.34$

이는 Van Gent(1995)의 표준 Darcy-Forchheimer 다공질 마찰식. `kinvis` = 동점성계수(외부 모듈 변수, ⚠ 정의는 SwashCommdata 측 — 본 파일엔 사용만 등장 `:338`).

배열 분포:
- `apors/bpors/cpors` = water-level(s) 점, `aporu/bporu/cporu` = u-점, `aporv/bporv/cporv` = v-점.

### 2.4 Porosity·구조높이 점 보간

`nporf` (셀별 입력 porosity)로부터 점별 보간:
- s-점 2D: 4-점 평균 `npors(nm) = 0.25*(nporf(nm)+nporf(nmd)+nporf(ndm)+nporf(ndmd))` (`:145`)
- u-점: 2-점 평균 `nporu(nm)=0.5*(nporf(nm)+nporf(ndm))` (`:164`)
- v-점: `nporv(nm)=0.5*(nporf(nm)+nporf(nmd))` (`:183`)
- 영구건조 점은 1.0 (`:190-192`, 즉 완전 유체).

구조높이 `hporf` 도 `varsh` 면 동일 방식 보간 (`:211-306`), 단 porosity가 `0.1 < n < 0.99` 인 점만 (`:222` 등). 영구건조 점은 default `ppor(2)` (`:300-302`).

### 2.5 grain size 변화 — vargs

`vargs` 면 셀별 grain size `gsizf` 를 점별 평균하여 dsiz 산출 (s-점 4평균 `:417`, u-점 2평균 `:444`). 아니면 균일 `dsiz=ppor(1)`. `dsiz /= 0.` 가드로 0 나눗셈 방지 (`:336` 등).

`SWEXCHG`/`periodic` 로 porosity·구조높이·마찰계수 동기화 (`:198-207`, `:310-319`, `:544-552`).

---

## 3. 잠수 보정 (수심평균) — SwashPorFricDep

### 3.1 목적

`Adapts frictional forces and added mass inside porous structures in depth-averaged mode` (`SwashPorFricDep.ftn90:40`).

기본값으로 setup 값 복사 후 (`:84-86`), 구조물이 **잠수(submerged)** 상태일 때만 보정:
- 조건 `nporu(nm) > 0.1 .and. nporu(nm) < 0.99` (다공성 셀, `:88`) AND `.not. hporu(nm) > hum(nm)` (구조 높이가 수심보다 낮음 = breakwater is submerged, `:90-92`).

### 3.2 mean porosity 와 보정계수

수심평균 등가 porosity (`:96`):
$$n_{pom} = \frac{(n-1)h_{por} + h_u}{h_u}$$
(`npom = ( (nporu(nm)-1.)*hporu(nm) + hum(nm) ) / hum(nm)`). 구조물 위 청수층을 섞은 유효 porosity.

보정 multiplier (`:100-102`), 이후 `apomu/bpomu/cpomu = fac*apor*` (`:104-106`):
```
faca = (1.-npom)**2 * n^2 / ( (1.-n)**2 * npom^2 )    ! laminar
facb = (1.-npom)    * n^2 / ( (1.-n)    * npom^2 )    ! turbulent
facc = (1.-npom)    * n   / ( (1.-n)    * npom   )    ! added mass
```
즉 setup 식의 $n \to n_{pom}$ 치환 비율. 결과 `apomu` 등은 수심평균 유효 마찰.

### 3.3 KC 수 보정 (난류항)

`wper > 0.` 이면 Keulegan-Carpenter 수로 난류 마찰 추가 보정 (`:150-153`). 주석: `note: flow velocity here is the pore velocity` (`:151`).
```
kcn         = max(abs(u0(nm,1)),0.01) * max(1.,wper) / dsiz   (:169)
bpomu(nm,1) = bpomu(nm,1) * ( 1. + 7.5/kcn )                  (:170)
```
$KC = \dfrac{|u_0|\,T}{d}$, 난류 마찰을 $b(1 + 7.5/KC)$ 배. 작은 KC(짧은 진동)에서 마찰 증대. `max(abs(u0),0.01)`·`max(1.,wper)` 로 하한 가드. drag(`b`)에만 적용, laminar(`a`)·added mass(`c`)는 미적용.

`vargs` 면 dsiz를 점별 `gsizf` 평균으로 (`:165`/`:219`), 아니면 균일 `ppor(1)`. v-점은 `v0` 사용 (`:253`).

---

## 4. 다층 보정 (layer-resolved) — SwashPorFricLay

### 4.1 목적

`Adapts frictional forces and added mass inside porous structures in multi-layered mode` (`SwashPorFricLay.ftn90:40`).

수심평균과 달리 **각 계산층 k**에 대해 fluid/porous/partial 분류:
- 구조높이 level `zkh = zkum(nm,kmax) + hporu(nm)` (바닥+구조높이, 위쪽 양수, `:95`).
- `zkh > zkum(nm,0)` → `breakwater is emerged` : 전 층 setup 값 (`:97-104`).
- else submerged → 층별 분기 (`:109-147`):
  - `zkh < zkum(nm,k)` → `layer is fluid` : `apomu/bpomu/cpomu = 0` (`:111-118`)
  - `zkh > zkum(nm,k-1)` → `layer is completely porous` : setup 값 (`:119-126`)
  - else → `layer is partly porous` : 층내 mean porosity + 보정 (`:127-145`).

### 4.2 층내 mean porosity (부분 다공질 층)

`:133`:
$$n_{pok} = \frac{n(z_{kh} - z_k) + (z_{k-1} - z_{kh})}{z_{k-1} - z_k}$$
(`npok = ( nporu(nm)*(zkh-zkum(nm,k)) + (zkum(nm,k-1)-zkh) ) / (zkum(nm,k-1)-zkum(nm,k))`) — 층 두께 중 다공질 부분(아래)은 n, 청수 부분(위)은 1로 가중평균. 보정계수 faca/facb/facc는 PorFricDep와 동일 형태, $n_{pom}\to n_{pok}$ (`:137-139`), 결과 `apomu(nm,k)=faca*aporu(nm)` 등 (`:141-143`).

### 4.3 w-점(수직속도) 마찰 — bpoks / npoks

비정수압(`ihydro==1 .or. ihydro==2`)일 때 layer interface(w-점)용 마찰도 산출 (`:229-263`):
- 기본 `apoks/bpoks/cpoks/npoks = apors/bpors/cpors/npors` (`:233-236`).
- interface가 유체면(`zkh < zks(nm,k)`)이면 `apoks=bpoks=cpoks=0, npoks=1` (`:246-253`) — 수직운동방정식 마찰 제거.

### 4.4 KC 보정 (수평 + 수직)

`wper > 0.` 이면 (`:268`):
- 수평 u/v 마찰: 전 층 loop `bpomu(nm,k) *= (1.+7.5/kcn)` (`:284-287`), `kcn = max(abs(u0(nm,k)),0.01)*max(1.,wper)/dsiz` (`:285`).
- 수직 w 마찰(비정수압): `bpoks(nm,k) *= (1.+7.5/kcn)` with `w0` (`:312-315`, k=0..kmax-1). w-점은 인접 셀 grain size 평균 (1D 2평균 `:308`, 2D 4평균 `:464`).

수심평균과 동일한 $b(1+7.5/KC)$ 보정식이나, 다층은 층별 $u_0(k)$·$w_0(k)$ 로 층별 KC를 계산하는 점이 다르다.

---

## 5. 식생 ↔ 다공성 메커니즘 비교 요약

| 항목 | 식생 (SwashVeget) | 다공성 구조물 (SwashPorousStruc 계열) |
|---|---|---|
| 물리 모델 | Morison drag + inertia (Burcharth & Andersen 1995) | Darcy-Forchheimer (Van Gent 1995) |
| 출력 배열 | `cvegu/cvegv(nm,k,1:2)` (drag, inertia) | `apor*`(층류) `bpor*`(난류) `cpor*`(added mass) |
| 핵심 입력 | $C_D$(cdveg), $b$(bveg), $N$(nveg) | porosity $n$(nporf), grain $d$(gsizf), $\alpha,\beta$(ppor) |
| 단층/다층 | `kmax==1` vs `>1` 분기 (한 파일 내) | Dep(수심평균) / Lay(다층) 별도 파일 |
| 잠수 처리 | canopy submerged/emerged 적분한계 (`:144`/`:208`) | submerged 시 mean porosity 보정 (Dep `:96` / Lay `:133`) |
| KC 보정 | 없음 | $b(1+7.5/KC)$ (Dep `:170` / Lay `:286`) |
| 연결점 | `iveg==1 & iporos/=0` 시 porosity로 $1/n^3$(drag)·$1/n^2$(inertia) 보정 (`SwashVeget:645-646`) | — |

⚠ 미확인: `ppor(2)` 가 default 구조높이임은 `:300-302` 의 사용처에서 추정. `kinvis`·`cvm`·`iporos`·`ihydro` 등 외부 모듈 변수의 정의 본체는 본 4개 파일에 없음(SwashCommdata*/m_genarr 측) — 본 노트는 사용처 의미만 기술. 정확한 선언/단위는 해당 모듈 분석 노트 필요 (source-needed: SwashCommdata2/3 의 ppor·kinvis·cvm 선언).
