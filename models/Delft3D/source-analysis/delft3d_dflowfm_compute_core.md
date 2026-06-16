---
title: "Delft3D D-Flow FM 계산 커널 — 연속·운동량 이산화·암시 solver (furu/s1ini/s1nod/u1q1/step_reduce_hydro)"
model: Delft3D
component: dflowfm/dflowfm_kernel-compute
canonical_source: self
citation_status: verified
verification_method: "Delft3D 소스 직접 read (src/engines_gpl/dflowfm/packages/dflowfm_kernel/src). furu.f90(운동량 fu/ru 계산)·s1ini.f90(연속식 행렬 조립)·s1nod.f90(대각/RHS 및 경계)·u1q1.f90(속도/플럭스 update)·step_reduce_hydro.f90(암시 시간적분 outer loop)·setau.f90(습윤 단면적)·iterfurufm.f90(구조물 운동량) 의 알고리즘을 file:line 인용. solver 호출/Gauss+CG 구조는 dflowfm_utils/solve_guus.F90 인용."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/source-analysis/delft3d_dflowfm_kernel_scheme.md
  - models/Delft3D/source-analysis/delft3d_fm_compute_aux.md
  - models/Delft3D/source-analysis/delft3d_drying_flooding.md
  - models/Delft3D/source-analysis/delft3d_sigma_z.md
  - models/Delft3D/README.md
---

# Delft3D D-Flow FM 계산 커널 — 연속·운동량 이산화·암시 solver

> 한줄 요약(경로: src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/dflowfm_kernel/compute/): D-Flow FM 비구조격자 flow solver의 핵심. 운동량을 link별 `fu·ru` 계수로 환원(`furu`)하고, 이를 cell의 연속방정식 행렬로 조립(`s1ini`→`s1nod`)하여 수위 `s1`에 대한 대칭 양정부호 선형계를 Gauss 소거+CG로 풀고(`solve_matrix`), 다시 link 속도/플럭스를 복원(`u1q1`)하는 semi-implicit ADI-free θ-method 루프. 전체 outer loop는 `step_reduce_hydro`가 비선형(Nested Newton)·건습·time-step setback과 함께 지휘.

기존 [[delft3d_dflowfm_kernel_scheme]] (스킴 개요)·[[delft3d_fm_compute_aux]] (보조 루틴)·[[delft3d_drying_flooding]] (건습)·[[delft3d_sigma_z]] (수직 layering) 과 중복을 피하고, **compute/ 의 코어 solver 루틴 본체**(fu/ru 계산식·행렬 조립·암시 outer loop·선형계 solver 구조)에 집중한다.

---

## 1. 큰 그림 — 한 timestep의 암시 연속식 루프 (`step_reduce_hydro`)

`step_reduce_hydro(key)` 헤더 주석: `do a flow timestep dts guus, reduce once, then elimin conjugate grad substi` (`compute/step_reduce_hydro.f90:44`). 진입 시 `s1=s0, u1=u0` (`step_reduce_hydro.f90:50`).

핵심 호출 순서 (모두 `step_reduce_hydro.f90`):

| 단계 | 호출 | 라인 | 역할 |
|---|---|---|---|
| 1 | `call furu()` | `:111` | link별 운동량 → `fu(L), ru(L)` (s0 기준) |
| 2 | `call s1ini()` | `:124` | link 기여를 cell 연속식 행렬 `bb/ccr/dd` 에 조립 |
| 3 | `call pack_matrix()` | `:125` | 행렬 packed(CRS) 형식으로 변환 |
| 4 | `call s1nod()` | `:130` | cell 대각 `bbr`·RHS `ddr` 완성 + 경계조건 |
| 5 | `call solve_matrix(s1, ndx, itsol)` | `:140` | `s1` 에 대한 선형계 해 (Gauss+CG) |
| 6 | `call poshcheck(key)` | `:167` | 음수 수심 검사 → 필요시 setback |

`dti = 1/dts` 로 역시간간격 설정(`step_reduce_hydro.f90:96`), `time1 = time0 + dts` 도달 시도(`:95`).

세 겹 루프 구조:
- `setback:` (`:93`) — 음수수심·비수렴 시 `dts`를 절반으로 줄여 재시도. `dts = 0.5_dp*dts` 후 `cycle setback` (`:243`, `:253`).
- `wetdry:` (`:115`) — 건습 행렬 갱신(hu=0 처리) 재진입점.
- `nonlincont:` (`:129`) — 비선형 연속식 반복 진입점.

`itstep == 4` 면 명시적 timestep으로 분기하여 `s1 = s0` 만 두고 행렬 풀이 생략(`step_reduce_hydro.f90:113`, `:313-314`).

---

## 2. 운동량 방정식 → `fu`, `ru` 계수 (`furu`)

`subroutine furu() ! set fu, ru and kfs` (`compute/furu.f90:44`). link별 이산 운동량식을 풀어, 수위에 대한 1차 형태로 환원한다:

$$u^{n+1}_L = ru(L) - fu(L)\,\big(s_1(k_2) - s_1(k_1)\big)$$

(이 관계가 실제로 `u1q1.f90:80` 에서 사용됨 — §4 참조.)

### 2.1 2D(`kmx==0`) 코어 루프 (`furu.f90:89-214`)

link `L`에 대해 `hu(L)>0` (습윤)일 때만 계산(`furu.f90:97`):

- 중력·경사 항: `gdxi = agp * dxi(L)` (`furu.f90:144`), 여기서 `agp`는 위도보정 중력(Helmert, `furu.f90:140-143`), `dxi(L)=1/dx`.
- θ-implicit 계수: `cu = gdxi * teta(L)` (`furu.f90:149`) — θ-method의 암시 압력경사 기여.
- 명시 RHS: `du = dti*u0(L) - adve(L) + gdxi*slopec` (`furu.f90:150`) — 시간미분 `dti*u0`, 이류 `adve` (외부에서 set), drop-loss 경사 보정 `slopec`.
- θ≠1 이면 명시 압력경사 추가: `du = du - (1-teta)*gdxi*ds`, `ds = s0(k2)-s0(k1)` (`furu.f90:151-154`).
- 밀도가 운동량에 들어가면(`jarhoxu>=2`) `gdxi`에 `rhomean/rhou(L)` 곱(`furu.f90:145-147`).

**마찰 inner loop** `do itu1 = 1, 4 ! furu_loop` (`furu.f90:169`): 바닥마찰 항 `frL`을 속도의 함수로 갱신하며 최대 4회 반복.
- 표준: `frL = cfuhi(L) * sqrt(u1L*u1L + v2)` — 주석 `g / (H.C.C) = (g.K.K) / (A.A) travels in cfu` (`furu.f90:197`). 즉 `cfuhi`에 $g/(H C^2)$ 가 담겨 있고 여기에 속도 크기를 곱해 선형화된 마찰계수를 얻는다.
- 핵심 계수 산출(`furu.f90:200-204`):
  ```
  bui = 1/(dti + advi(L) + frL)
  fu(L) = cu * bui
  ru(L) = du * bui
  u1L   = ru(L) - fu(L)*ds
  ```
  즉 $fu = \dfrac{g\,\theta/\Delta x}{1/\Delta t + advi + fr}$, $ru = \dfrac{u^0/\Delta t - adve + \dots}{1/\Delta t + advi + fr}$ — 분모는 암시 시간·이류·마찰의 합.
- 수렴 조기탈출: 수심 <1 m 이거나 속도변화 <1e-2 면 `exit furu_loop` (`furu.f90:206-208`).

파동 연동 시 Stokes-drift 보정: `frL` 을 Eulerian 속도 `u1L - ustokes(L)` 기준으로 계산하고 `du = du0 + frL*ustokes(L)` 보정(`furu.f90:170-181`). 식생 항력은 `alfav(L)` 추가(`furu.f90:184-186`, `:194-195`).

### 2.2 펌프·구조물·3D

- 펌프 link: `fu/ru` 0으로 두고 `ru(L) = ±qp/ap` 로 규정 토출(`furu.f90:216-267`).
- 구조물: `call furu_structures()` (`furu.f90:269`), `call furusobekstructures()` (`furu.f90:369`).
- 3D(`kmx>0`)는 본 루프 대신 `call update_verticalprofiles()` 로 위임(`furu.f90:273-281`), 필터 predictor 옵션(`:275-277`).
- u-점 경계: `nbndu` 루프에서 `fu(L)=0`, `ru(L)=zbndun` 으로 규정속도/Riemann/critical-outflow 등 처리(`furu.f90:283-367`); 3D는 log-profile 적분으로 layer별 `ru` 분배(`furu.f90:340-362`).

### 2.3 구조물 운동량 (`iterfurufm`, SOBEK 계열)

`logical function iterfurufm(...)` — 헤더 주석 `coefficients for momentum equation in wet weir point`, programmer Guus Stelling (`compute/iterfurufm.f90:40,49,53`). 구조물(위어) link의 `fu/ru` 산출:
```
bu = dxdt + (1+relax+dxfrL)*ustru
du = (strucalfa*q1/au + (1-strucalfa)*u0)*dxdt + relax*ustru*u1 + rhsc
fu(m) = cu/bu ; ru(m) = du/bu ; u1(m) = ru(m) + fu(m)*(su-sd)
```
(`iterfurufm.f90:104-109`). `relax==0`이면 반복 없이 즉시 `.false.` 반환(`iterfurufm.f90:110-111`).

---

## 3. 연속방정식 행렬 조립 (`s1ini` → `s1nod`)

### 3.1 link 기여 조립 — `s1ini`

`subroutine s1ini() !> links in continuity eq.` (`compute/s1ini.f90:47-48`). 먼저 행렬 초기화 `bb=0; ccr=0; dd=0` (`s1ini.f90:70-72`).

전반부(`s1ini.f90:84-326`)는 소스/싱크(강우 `rain`, 증발 `evap`, 외부유량 `qext`, lateral `qqlat`, 지하수 `setgrwflowexpl`, source/sink `setsorsin`)를 `qin`/`dd`에 누적 — 질량보존 영역(`mba`) 추적 포함.

**핵심 행렬 조립** (2D, `s1ini.f90:328-344`): 습윤 link `L`마다
```
tetau = teta(L)*au(L)
aufu  = tetau*fu(L)
bb(k1) += aufu ; bb(k2) += aufu      ! 대각 (양 끝 cell)
ccr(Lv2(L)) -= aufu                  ! 비대각 (link L의 off-diagonal entry)
auru  = tetau*ru(L) + (1-teta)*au(L)*u0(L)   ! ≈ θ-가중 link flux q1(L)
dd(k1) -= auru ; dd(k2) += auru       ! RHS (유출/유입 부호)
```
여기서 `au(L)`=습윤 단면적, `Lv2(L)`=link `L`의 packed off-diagonal 인덱스. 즉 cell 연속식
$$A_n\frac{s_1^{n+1}-s_1^n}{\Delta t} + \sum_{L \in n} \pm q_1(L) = Q_{in}$$
에서 `q1(L) = au(L)[θ u^{n+1} + (1-θ)u^0]` 를 `u^{n+1}=ru-fu·Δs` 로 치환해, `s1`의 대각·비대각·RHS 항으로 전개한 것이다. 3D는 동일 로직을 layer `Lbot..Ltop`에 대해 누적(`s1ini.f90:346-372`).

비선형이면 `ccrsav = ccr` 저장(`s1ini.f90:374-376`) — outer 반복에서 solve가 `ccr`를 덮어쓰므로 복원용([[step_reduce_hydro]]의 `ccr = ccrsav` `:274`).

### 3.2 cell 대각·RHS 완성 + 경계 — `s1nod`

`subroutine s1nod() !> nodes in continuity eq` (`compute/s1nod.f90:44-45`). 헤더 주석으로 의도를 명시:
```
!bbr = bb + dti*a1     !m2/s
!ddr = dd + dti*a1*s1  !m3/s
```
(`s1nod.f90:78-79`). 구현(`s1nod.f90:107-177`):
```
dtiba = dti * a1(n)            ! a1(n)=cell 자유표면적
bbr(n) = bb(n) + dtiba         ! 대각 (시간미분 항 추가)
if (nonlin>=2) bbr(n) -= dti*a1m(n)   ! pressurised(Nested Newton) 보정
...
ddr(n) = dd(n) + dtiba*s1(n)
ddr(n) = ddr(n) + dti*(vol0(n)-vol1(n))   ! 비선형 체적 잔차
```
(`s1nod.f90:108-167`). `kfs(n)==1` (암시 점)에만 RHS 계산(`s1nod.f90:164`). 선형(`nonlin==0`)이면 `ddr(n)=dd(n)+dtiba*s0(n)` — 반복 커플링 대비 `s0` 사용(`s1nod.f90:171-173`).

대각이 0이면 SAAD solver crash 경고를 위치(`xz,yz`)·branch chainage와 함께 출력(`s1nod.f90:120-162`).

**경계조건 행렬 수정** (`s1nod.f90:181-277`):
- waterlevel(Dirichlet): `ddr(kb)=bbr(kb)*water_level_boundary`, 이웃 cell RHS 보정 후 `ccr(Lv2(L))=0` (link 절단) (`s1nod.f90:253-262`).
- Neumann: `ccr=-bbr(kb)`, 지정 경사를 RHS로(`s1nod.f90:215-224`).
- Riemann: `bbr(kb) = -cffu*(fuL + sqrtgfh)`, `sqrtgfh=sqrt(ag/hh)` (`s1nod.f90:225-252`).
- velocity 경계: 수위에 Neumann 적용 — `ccr(Lv2(L))=-bbr(k2)`, `bbr(kb)=-ccr` (`s1nod.f90:266-277`).

병렬(MPI)에서 overlap 영역 행렬 동기화: `call update_matrix(ierr)` (`s1nod.f90:298-299`).

---

## 4. 속도·플럭스 복원 (`u1q1`)

`subroutine u1q1()` (`compute/u1q1.f90:43`). solve로 `s1`이 갱신된 뒤 link 속도와 flux를 재계산.

2D 코어(`u1q1.f90:76-88`):
```
u1(L) = ru(L) - fu(L)*(s1(k2)-s1(k1))           ! 운동량 복원
q1(L) = au(L)*(teta(L)*u1(L) + (1-teta)*u0(L))  ! θ-가중 flux
qa(L) = au(L)*u1(L)                              ! 이류용 flux
```
이것이 §2의 `fu/ru` 정의를 닫는 관계다. MPI에서는 `u1` 계산 → `update_ghosts(ITYPE_U,...)` → `q1/qa` 계산 순으로 분리(`u1q1.f90:90-130`).

cell별 유입·유출 flux 합산 `squ`(유출), `sqi`(유입) 누적(`u1q1.f90:137-149`); 경계 총량 `qinbnd/qoutbnd` (`u1q1.f90:201-215`). `iadvec==40` 면 이류용 가중체적 `voldhu` 계산(`u1q1.f90:157-178`).

**3D 분기**(`u1q1.f90:217-441`): layer `Lb..Lt`에서 `u1(L)=ru(L)-fu(L)*dsL` (`:231`), flux를 depth-적분(`q1(LL)+=q1(L)`, `u1q1.f90:288-294`), 깊이평균 속도 `u1(LL)=q1(LL)/au(LL)` (`:335-336`). **수직 flux 폐합**: cell별 아래에서 위로 `qw(k)=qwb+sqiuh`, `ww1(k)=wb+sqiuh/a1` (연속식으로 수직속도 산출, `u1q1.f90:368-439`), σ-격자 격자운동 보정 `qsigma = a1*(zws(k)-zws0k)/dts` (`:417-419`).

마지막에 `sq = sqi - squ` (cell 순 발산, `u1q1.f90:443`) — drying/flooding·timestep 제어에 사용.

---

## 5. 습윤 단면적 `au` 설정 (`setau`)

`subroutine setau() ! get wet cross-sections at u points` (`compute/setau.f90:43`). §3의 행렬 조립이 쓰는 `au(L)`을 제공.

- 2D: `nonlin==0` 이면 `vol1_f(n)=ba(n)*hh`, `a1(n)=ba(n)` (선형 체적, `setau.f90:80-88`); 그 후 `call vol12D(1)` 로 `au` 계산(`setau.f90:90`). 댐브레이크·long-culvert 단면 축소 적용(`setau.f90:95-97`).
- 구조물: gate(`setau.f90:101-150`)·general structure(`:152-187`)에서 개방고 `zgaten` 위쪽 단면 차단 — `au(LL)=hu(LL)*wu(LL)`, 추가이류 `advi(LL)+= afac*0.5*|u1|*dxi` (`setau.f90:114-115`). check-valve(`:189-200`)·valve smoothing(`:202-215`).
- 유량경계 Manning 정규화: `at += au(L)*huqbnd(n)**FAC23`, `FAC23=2/3` (`setau.f90:308`, `:76`), `zbndq(n) = zbndq(n)*huqbnd**(2/3)/at` 로 단면별 토출 배분(`setau.f90:331-340`).

(상류 수심 `hu` 자체의 upwind 설정은 [[delft3d_drying_flooding]] 관련 `sethu` — `calculate_hu_au_and_advection_for_dams_weirs` `compute/sethu.f90:69` — 가 담당하며, 본 노트 범위 밖.)

---

## 6. 선형계 solver — Gauss 소거 + CG (`solve_matrix`)

행렬은 `dflowfm_utils/` 의 `m_solve_guus` 모듈이 푼다(compute/가 `use m_solve_guus` `step_reduce_hydro.f90:34`).

행렬 자료구조(packed/CRS) 주석 (`dflowfm_utils/solve_guus.F90:394-404`, verbatim 발췌):
```
!>  make the matrix and packed matrix array administration
!>    ia(i)%l : number of non-zero lower-diagonal entries for row i (Matrix is assumed symmetrical)
!>    ia(i)%j : array with the non-zero lower-diagonal column indices
...
!>    lv2(L)  : pointer to the lower-diagonal off-diagonal entry of link L in the packed matrix array
```
즉 **대칭** 행렬을 하삼각만 저장; `lv2(L)`이 §3의 `ccr(Lv2(L))` 인덱싱과 일치. 변수 의미는 주석으로 명시: `ddr (rechterlid), bbr (diag) , ccr (off diag)` (`solve_guus.F90:709`).

`subroutine solve_matrix(s1, ndx, itsol)` (`solve_guus.F90:544`) 의 3단 구조:

1. **Gauss 소거** — `call gauss_elimination()` (또는 derivedtypes용 `gauss_eliminationjipjan`) (`solve_guus.F90:577-581`). 망(network)의 가지(branch)-말단 노드를 minimum-degree 순서로 제거. `reducept`: `this subroutine finds an elimination order for Gaussian elimination based upon minimum degree algorithm` (`solve_guus.F90:1758-1759`).
2. **CG 반복** — `icgsolver` 분기(`solve_guus.F90:591-641`):
   - `1`: `conjugategradient_omp` (OMP, thread 순서 의존)
   - `2`: `conjugategradient_omp_threadsafe`
   - `3`: `conjugategradient` (no OMP)
   - `4/44`: `conjugategradientSAAD` (Saad, OMP + ILUD 전처리, `:600-602`)
   - `6`: `conjugategradientPETSC` (PETSc, `:615`)
   - `7`: `conjugategradient_MPI` (병렬 CG, block 전처리, `:624`)
   - `8`: pARMS, `10`: Jacobi (`:631`, `:638`)
   `ipre`=전처리 레벨(`solve_guus.F90:546`). 반복수 `nocgiter` 누적(`:650`).
3. **역대입** — `call gauss_substitution(s1, ndx)` (또는 jipjan, `solve_guus.F90:657-661`) — 제거된 노드의 `s1` 복원.

이 "Gauss로 트리 부분 제거 → 줄어든 시스템에 CG → 역대입" 구조가 D-Flow FM의 1D 가지망(branch) + 2D 그물망 혼합 격자에서 효율적인 이유다(가지·말단은 직접 소거, 강결합 코어만 반복법).

---

## 7. 비선형(Nested Newton)·수렴·setback (`step_reduce_hydro`)

`step_reduce_hydro`의 `nonlincont` 루프가 비선형 연속식을 반복:

- 매 반복 후 `call volsur()` 로 체적·표면적 재계산(`step_reduce_hydro.f90:213`), 수위변화 최대값 `difmaxlev` 산출(`:217-228`).
- 수렴판정: `difmaxlev > epsmaxlev` 면 `ccr = ccrsav` 복원 후 `cycle nonlincont` (`step_reduce_hydro.f90:273-275`).
- **Nested Newton** (`nonlin>=2`, pressurised/1D 정수압): 내부 수렴 후 `s1m`(보조 수위) 대 `s1` 차이 `difmaxlevm > epsmaxlevm` 검사 → outer 반복(`step_reduce_hydro.f90:286-303`). 시작 시 `s1m = bl` (bed level, `:118`).
- 비수렴(반복수 > `maxNonlinearIterations`): `dts = 0.5*dts`, `s1 = s0`, `dsetb++`, `cycle setback` (`step_reduce_hydro.f90:232-255`). `dts < dtmin` 이면 포기(`:246-251`).
- `poshcheck`가 음수수심 검출(`key==2`)하면 Nested Newton 재시작(`firstnniteration=.false.`, `cycle wetdry` `:177-180`) 또는 hu=0 재조립(`cycle wetdry` `:194`) 또는 timestep 감축(`cycle setback` `:200`).

---

## 8. 모듈 간 데이터 흐름 요약

```
setau ──au──┐
sethu ──hu──┤
            ▼
furu: u-momentum → fu(L), ru(L)         [compute/furu.f90:200-204]
            │
            ▼
s1ini: link → bb(diag)/ccr(offdiag)/dd  [compute/s1ini.f90:328-344]
            │  (+ pack_matrix CRS)
            ▼
s1nod: + dti*a1 대각, RHS ddr, 경계      [compute/s1nod.f90:108-167,181-277]
            │
            ▼
solve_matrix: Gauss elim → CG → subst   [dflowfm_utils/solve_guus.F90:577-661]
            │  → s1 (new water level)
            ▼
u1q1: u1=ru-fu·Δs, q1=au·(θu1+(1-θ)u0)  [compute/u1q1.f90:80-82]
            │
            ▼
poshcheck / volsur → 수렴·setback 판정   [compute/step_reduce_hydro.f90:167,213,273]
```

θ-method 변수: `teta(L)` (link별 implicitness), `dti=1/dts`. 대칭 양정부호 행렬 → CG. 비선형 체적(테이블 기반 `vol12d`)과 Nested Newton이 비선형 연속식·압력화(pressurised 1D)를 처리.

---

## 9. 미확인 / source-needed

- `gauss_elimination`/`conjugategradient_omp` **본체** 수치 디테일(전처리 ILUD 구성, 수렴 tolerance 값)은 본 검수에서 헤더·분기까지만 확인. 세부는 `dflowfm_utils/solve_guus.F90` (해당 subroutine 본체) 및 `solve_petsc.F90`/`solve_parms.F90` 추가 read 필요 — **source-needed**.
- `adve(L)`/`advi(L)` (이류 항·암시 이류계수)의 **계산 위치**는 본 노트 범위(compute/ solver 코어) 밖. `furu`는 이미 set된 값을 소비만 함(`furu.f90:150,200`). 이류 이산화 본체(예: `advec.f90`, `setumod.f90`)는 별도 검수 대상 — 본 노트에서 미확인.
- `vol12d`/`a1`/`a1m` 비선형 체적테이블의 구성은 [[delft3d_drying_flooding]]·[[delft3d_fm_compute_aux]] 영역으로, 여기선 소비 관계만 인용.
