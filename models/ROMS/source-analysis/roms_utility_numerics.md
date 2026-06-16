---
title: "ROMS Utility 수치·격자 도구 — vorticity·s-coord·interpolate·shapiro·white_noise"
model: ROMS
component: ROMS/Utility
canonical_source: self
citation_status: verified
verification_method: "ROMS 소스 직접 read (roms/ROMS/Utility/). vorticity.F·uv_rotate.F·uv_var_change.F·set_scoord.F·set_weights.F·interpolate.F·shapiro.F·stiffness.F·round.F·white_noise.F·tadv.F·tile_indices.F·timers.F·zeta_balance.F·time_corr.F·sum_imp.F·set_masks.F·inp_par.F·inp_decode.F·yaml_parser.F·grid_coords.F 의 헤더 주석·핵심 알고리즘을 file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/ROMS/source-analysis/roms_main_driver_dispatch.md
  - models/ROMS/source-analysis/roms_grid_metrics.md
  - models/ROMS/source-analysis/roms_baroclinic_3d.md
  - models/ROMS/README.md
---

# ROMS Utility 수치·격자 도구

> ROMS/Utility/ 의 비-IO 수치·격자 헬퍼 모음 — 진단량(vorticity), C↔A 격자 회전, s-좌표/시간평균 가중치 설정, 범용 보간, Shapiro 필터, 격자 stiffness, 백색잡음, 입력 파싱(namelist/YAML). 경로: roms/ROMS/Utility/. (IO 계열 `def_/wrt_/get_/nf_*`는 별도 담당)

`Utility/` 에는 198개 파일이 있으나 절반 이상이 IO(`def_*`·`wrt_*`·`get_*`·`nf_fread*`·`nf_fwrite*`)·4D-Var 상태벡터 대수(`state_*`·`congrad`·`rpcg_lanczos` 등)이다. 본 노트는 **순수 수치·격자 도구**만 다룬다.

---

## 1. 진단 vorticity — `vorticity.F`

모듈 `vorticity_mod` 은 단열 Boussinesq 유체의 상대(relative) 및 잠재(potential) vorticity 를 계산한다. 헤더 주석(`Utility/vorticity.F:11-18`):

> `This routine computes relative (s-1) and potential (m-1 s-1) vorticity for an adiabatic Boussinesq fluid where the potential density is conserved: pvor = 1/rho0 dot_product(avor, grad(pden))`

곡선좌표 정의(`Utility/vorticity.F:26-34`):

$$\text{rvor} = mn\left[\frac{\partial (v/n)}{\partial \xi} - \frac{\partial (u/m)}{\partial \eta}\right]$$

수평 PSI-점·연직 RHO-점에 이산화 (`vorticity.F:39-40`: `The relative and potential vorticity is discretized at horizontal PSI-points and vertical RHO-points.`).

공개 루틴 (`vorticity.F:65-69`): `pvorticity2d`, `rvorticity2d`, `pvorticity3d`, `rvorticity3d` (3D는 `SOLVE3D` 가드).

| 루틴 | 핵심 식 | file:line |
|---|---|---|
| `rvorticity2d` | `rvor2d = cff*(dVdx_p - dUde_p)`, `cff=0.0625*(Σpm)(Σpn)` | `vorticity.F:246-259` |
| `pvorticity2d` | `pvor2d = cff*(fomn_p+dVdx_p-dUde_p)/(h+zeta)`, 천수 잠재 vorticity | `vorticity.F:147-163` |
| `pvorticity3d` | `pvor3d = orho0*(...)`, `f/mn + d(v/n)/dξ - d(u/m)/dη` 항에 `dRdz`·`dRdx·dUdz`·`dRde·dVdz` 결합 | `vorticity.F:471-472`, dRdx/dRde 계산 `vorticity.F:376-390` |

`dVdx_p`/`dUde_p` 은 `on_v·vbar` / `om_u·ubar` 의 차분이며 `MASKING` 시 `pmask` 곱(`vorticity.F:152-160`). 결과는 주기경계 시 `exchange_p2d_tile`, MPI 시 `mp_exchange2d` 로 교환(`vorticity.F:169-181`). `AVERAGES`/AD/TL/RP 평균용 `vorticity_avg`도 조건부 공개(`vorticity.F:71-77`).

---

## 2. 격자 회전·변환 — `uv_rotate.F`, `uv_var_change.F`

### 2.1 `uv_rotate.F` (모듈 `uv_rotate_mod`)
헤더(`uv_rotate.F:11-13`):
> `These routines average momentum component to RHO-points and then rotates from (XI,ETA) coordinates to geographical Eastward and Northward directions.`

`uv_rotate2d` 의 핵심 (`uv_rotate.F:91-98`): U/V 를 RHO-점으로 0.5 평균 후
- `Uout = Urho*CosAngler - Vrho*SinAngler`
- `Vout = Vrho*CosAngler + Urho*SinAngler`

`add=.TRUE.` 분기는 누적(`uv_rotate.F:88-104`), `.FALSE.` 는 대입(`uv_rotate.F:105-118`). `MASKING` 시 `rmask_full` 곱(`uv_rotate.F:99-102`). 출력 전용이며 `exchange_r2d_tile`로 교환.

### 2.2 `uv_var_change.F` (모듈 `uv_var_change_mod`, `SOLVE3D` 한정)
C-grid ↔ A-grid(Arakawa A, cell-center) 상호변환 — 출력·4D-Var 상태벡터(셀중심)용(`uv_var_change.F:11-15`). 두 방향:

C2A (`uv_var_change.F:20-26`):
$$U_r = 0.5[u(i,j)+u(i{+}1,j)], \quad u_a = U_r\cos\theta - V_r\sin\theta$$

A2C (`uv_var_change.F:34-38`): 역회전 후 다시 C-grid로 평균. 공개 루틴 `uv_C2A_grid`/`uv_A2C_grid` + adjoint(`ad_*`)·tangent(`tl_*`) 변종(`uv_var_change.F:60-69`). 측방경계는 gradient BC(`bc_r3d_tile`).

---

## 3. 연직 s-좌표 설정 — `set_scoord.F` (`SOLVE3D`)

지형추종(terrain-following) 연직좌표 변환 변수 초기화. 헤더(`set_scoord.F:11-12`). 저자: A. F. Shchepetkin (`set_scoord.F:9`). [[roms_grid_metrics]]·[[roms_baroclinic_3d]] 의 연직격자와 연계되나, **무차원 stretching 함수와 임계깊이 `hc` 설정**이 고유 영역.

비차원 좌표 정의(`set_scoord.F:38-39`):
$$\text{sc\_w}(k)=\frac{k-N}{N},\quad \text{sc\_r}(k)=\frac{k-N-0.5}{N}$$

**임계깊이 `hc`** — Vtransform 별 (`set_scoord.F:170-177`):
- Vtransform=1: `hc = MIN(MAX(hmin,0),Tcline)` (원 공식, `hc<=hmin` 제약)
- Vtransform=2: `hc = Tcline` (임의 값 허용)

**Vstretching=1** (`set_scoord.F:184` 분기) — theta_s/theta_b 기반 (`set_scoord.F:202-226`):
$$C_s = (1-\theta_b)\frac{\sinh(\theta_s\, s)}{\sinh\theta_s} + \theta_b\left[\frac{\tanh(\theta_s(s+0.5))}{2\tanh(0.5\theta_s)}-0.5\right]$$
(`cff1=1/SINH(theta_s)`, `cff2=0.5/TANH(0.5*theta_s)`). `theta_s=0` 시 `Cs=sc` (`set_scoord.F:230-231`).

**연직격자 진단 출력** — Vtransform=1/2 별 `z1/z2/z3` (hmin/평균/hmax 깊이) 계산(`set_scoord.F:543-553`). Vtransform=2 식(`set_scoord.F:547-553`):
$$z = h\cdot\frac{h_c\,\text{sc} + h\cdot C_s}{h_c + h}$$

---

## 4. 바로트로픽 시간평균 가중치 — `set_weights.F` (`SOLVE3D`)

빠른(2D) 시간스텝에 대한 평균 가중치 함수 설정. 헤더(`set_weights.F:11-12`):
> `This routine sets the weigth functions for the time averaging of 2D fields over all short time-steps.`

**POWER_LAW** shape (`set_weights.F:60`):
$$F(\xi)=\xi^{F\alpha}(1-\xi^{F\beta})-F\gamma\cdot\xi$$
주석(`set_weights.F:64-67`): scale·Falpha·Fbeta·Fgamma·정규화는 0/1/2차 모멘트를 맞춰 **시간평균 바로트로픽 운동에 대해 전체 2차 시간정확도**를 산출. `scale` 은 centroid 를 `ndtfast` 에 맞추도록 16회 반복 조정(`set_weights.F:78-94`). 대안 `COSINE2` 는 Hamming window `0.0882+(cos)^2` (`set_weights.F:108`).

후처리(`set_weights.F:117-...`): centroid 불일치를 가중치의 "upstream advection" 으로 반복 제거 후 정규화(`set_weights.F:124-131`). 정밀도는 `real(r16)` (quad) 사용(`set_weights.F:38`).

---

## 5. 범용 보간 — `interpolate.F` (모듈 `roms_interpolate_mod`)

헤더(`interpolate.F:14`): `This module contains several all-purpose generic interpolations`. 주요 루틴(`interpolate.F:19-21`):

| 루틴 | 역할 | file:line |
|---|---|---|
| `linterp2d` | 임의 2D 필드 쌍선형(bilinear) 보간 | `interpolate.F:167-279` |
| `cinterp2d` | 쌍삼차(bicubic) 보간 | `interpolate.F:281-720` |
| `hindices` | 임의 datum 의 모델 격자셀 (fractional I,J) 탐색 | `interpolate.F:722-935` |
| `try_range`/`inside` | 셀 포함 판정 (Reid 1969 변형) | `interpolate.F:937`, `1013-1177` |

**쌍선형 핵심**(`interpolate.F:255-262`): `p2=(Iout-i1)`, `q2=(Jout-j1)`, `p1=1-p2`, `q1=1-q2`,
$$F_{out}=p_1q_1F(i_1,j_1)+p_2q_1F(i_2,j_1)+p_2q_2F(i_2,j_2)+p_1q_2F(i_1,j_2)$$

**hindices** 곡선좌표 변환(`interpolate.F:912-928`): 셀을 평행사변형으로 보고 Law of Cosines 로 shear 각 `phi` 산출(`interpolate.F:910`), `angler` 회전 후 `dx/dy` 를 셀변 길이로 정규화해 fractional index 도출. 메서드 상수: `BilinearMethod=0`, `BicubicMethod=1` (`interpolate.F:131-132`). 고수준 OO 래퍼 `roms_datum_interp_2d/3d/column` (`interpolate.F:139-141`), `roms_horiz_interp_2d/3d` (`interpolate.F:145-146`). `CUBIC_MASKED` 는 미완(`interpolate.F:3`: `needs work`).

`grid_coords.F` (`FLOATS||STATIONS`) 는 float/station 초기 위치를 `roms_interpolate_mod` 의 `hindices` 로 fractional 격자좌표 변환(`grid_coords.F:11-12`, `:22`).

---

## 6. Shapiro 필터 — `shapiro.F` (모듈 `shapiro_mod`)

order 2 Shapiro 필터, 경계·마스크 가장자리에서 차수 축소(`shapiro.F:11-12`). 저자 Kate Hedstrom (`shapiro.F:6`).

2D 두 패스(`shapiro2d_tile`) — 1차는 **η(j)방향**, 2차는 **ξ(i)방향**:
- 1차 η(j)-방향(`shapiro.F:78-94`): `Awrk1=0.25*(A(i,j-1)+A(i,j+1)-2*A(i,j))`, `Awrk2=A+Awrk1`
- 2차 ξ(i)-방향(`shapiro.F:103-119`): `Awrk1=0.25*(Awrk2(i-1,j)+Awrk2(i+1,j)-2*Awrk2(i,j))`, `A=Awrk2+Awrk1`

`MASKING` 분기는 각 이웃에 `Amask` 곱(`shapiro.F:103-106`). 3D 변종 `shapiro3d_tile` 동일 스텐실을 k-루프(`shapiro.F:182-223`).

---

## 7. 격자 stiffness 진단 — `stiffness.F` (모듈 `stiffness_mod`)

3D 격자의 최대 stiffness 비 r_x (Haney number) 진단. 헤더(`stiffness.F:11-19`):
$$r_x = \frac{z(i,j,k)-z(i{-}1,j,k)+z(i,j,k{-}1)-z(i{-}1,j,k{-}1)}{z(i,j,k)+z(i{-}1,j,k)-z(i,j,k{-}1)-z(i{-}1,j,k{-}1)}$$

주석(`stiffness.F:17-18`): `This is done for diagnostic purposes and it does not affect the computations.` — 즉 계산엔 영향 없는 안정성 진단.

`my_rx0` (바닥 z_w(0) 기반)·`my_rx1` (전 층) 의 tile-local MAX 누적(`stiffness.F:152-181`), 전역 `rx0(ng)=MAX(rx0(ng),my_rx0)` (`stiffness.F:254`). ⚠ 미확인: 부피·면적 통계(`omn`·`h`) 등 추가 진단은 본 노트에서 라인 미인용(source-needed).

---

## 8. 백색잡음 생성 — `white_noise.F` (모듈 `white_noise_mod`)

4D-Var 등에서 평균 0·분산 1 근사 난수 배열 생성(`white_noise.F:11-13`). 두 scheme(`white_noise.F:17-20`):
- `Rscheme=0`: F90 intrinsic `random_number`, `0<=R<1` (`white_noise.F:94-95`)
- `Rscheme=1`: Gaussian deviate (`nrutil`의 `gasdev`), `-1<R<1`

스케일 상수 `fac=2*SQRT(3)=2*1.732...` (`white_noise.F:77`) — 균등분포 [0,1) 을 E(R)=0, E(R²)=1 로 보정(`white_noise.F:97-100`, 참조 Bennett 2002 p.72). 변종: `white_noise1d/2d/2d_bry/3d/3d_bry` (`white_noise.F:38-43`). (난수 엔진 `ran1.F`·`gasdev.F`·`ran_state.F`·`nrutil.F`·`gasdev` 은 Numerical Recipes 계열로 본 노트 미세분석.)

---

## 9. tracer advection 스위치 보고 — `tadv.F` (`SOLVE3D`)

tracer 이류 스위치 구조체 `TYPE(T_ADV)` 처리(`tadv.F:11-19`):
- `tadv_putatt` — 활성 키워드를 출력 NetCDF 전역속성에 기록
- `tadv_report` — stdout 보고

수평·연직 이류 타입을 `Hadv(MAXVAL(NT),Ngrids)`/`Vadv` 구조체로 받아(`tadv.F:80-81`) 줄단위 포맷 문자열 생성(`tadv.F:107-125`). nf90/PIO 인터페이스 분기(`tadv.F:25-30`). 실제 이류 연산은 [[roms_advection]] 담당, 본 파일은 메타데이터 보고만.

---

## 10. 타일 인덱스 설정 — `tile_indices.F` (모듈 `tile_indices_mod`)

응용 격자의 타일 분해 bounds·인덱스·스위치 설정(`tile_indices.F:11-12`). 입력 `my_Im/my_Jm` (전역 격자점), `my_Lm/my_Mm` (계산점), 출력 `T_BOUNDS`/`T_DOMAIN`/`T_IOBOUNDS` 구조체(`tile_indices.F:30-40`).

변수타입별 경계 edge 인덱스 (`tile_indices.F:91-109`): p2dvar 의 서쪽=1, r2dvar 서쪽=0 등 staggered C-grid 규칙. `get_bounds`·`get_domain`·`get_tile` 등 `get_bounds_mod` 위임(`tile_indices.F:48-53`). 공개: `tile_indices`, `tile_obs_bounds` (`tile_indices.F:56-57`).

---

## 11. wall-clock 타이머 — `timers.F`

`wclock_on`/`wclock_off` — 각 병렬 스레드가 특정 model region 에 쓴 경과시간(초) 측정(`timers.F:11-13`). `RECURSIVE` (`timers.F:2`). 인자: `ng, model, region, line, routine` (`timers.F:42-44`). `TRACING` 정의 시 진입 로그 `==> Entering` (`timers.F:67-72`). DISTRIBUTE 시 `mp_barrier`·서브분할(`timers.F:30-90`). 전체 소스의 프로파일 호출(`CALL wclock_on(ng,model,N,__LINE__,MyFile)`)이 여기로 수렴.

---

## 12. 4D-Var 보조 수치 도구 (조건부 컴파일)

| 파일 | cppdefs 가드 | 역할 | file:line |
|---|---|---|---|
| `zeta_balance.F` | `BALANCE_OPERATOR && ZETA_ELLIPTIC` | 균형연산자용 SSH 타원방정식 `div(h grad(zeta)) = -div(∫∫grad(rho)...)` 해법(`balance_ref`,`biconj`) | `zeta_balance.F:11-20`, 공개 `:37-39` |
| `time_corr.F` | `WEAK_CONSTRAINT && TIME_CONV` | adjoint 상태에 대한 시간 상관(time correlation) 적용 | `time_corr.F:12-14` |
| `sum_imp.F` | `WEAK_CONSTRAINT && RPCG` | impulse 합산 (RPCG) | `sum_imp.F:3`, `:14-19` |

저자 Andrew M. Moore (`zeta_balance.F:6`, `time_corr.F:8`). 참조: Fukumori et al. 1998, Weaver et al. 2005 (`zeta_balance.F:23-30`). 본 노트는 호출 인터페이스만 — 내부 elliptic solver 세부는 [[roms_4dvar]] 와 중복이므로 링크.

---

## 13. 출력 마스킹 — `set_masks.F` (`MASKING`)

출력 NetCDF 처리용 내부 Land/Sea 마스크 배열 설정 — 육지점을 `_FillValue` 로 치환(`set_masks.F:11-14`). `*_full` 마스크는 wetting/drying 시 시간독립+시간종속 부분 결합 로직 단순화용(`set_masks.F:16-20`). point source 위치는 강제 water 로 설정해 _FillValue 마스킹 방지(`set_masks.F:22-23`). `WET_DRY` 시 매 스텝 `wetdry` 가 변경, 평균창용 시간평균 마스크 필요(`set_masks.F:24-28`).

---

## 14. 입력 파싱 — `inp_par.F`, `inp_decode.F`, `yaml_parser.F`

순수 수치는 아니나 격자·수치 파라미터 적재의 진입점이므로 포함.

### 14.1 `inp_par.F` (모듈 `inp_par_mod`)
표준입력에서 모델 파라미터 읽고 stdout 에 재출력(`inp_par.F:11-12`). `dateclock_mod::get_date`, DISTRIBUTE 시 `mp_bcasti/mp_bcasts` 로 브로드캐스트(`inp_par.F:31-34`). `GRID_EXTRACT` 시 netcdf 모듈 의존(`inp_par.F:20-25`).

### 14.2 `inp_decode.F` (모듈 `inp_decode_mod`)
ROMS namelist KeyWord 파라미터 디코드(`inp_decode.F:11-12`). 루틴(`inp_decode.F:14-...`): `decode_line`(KeyWord별 텍스트 라인 디코드), `find_file`(파일 존재 확인), `load_i`(정수), `load_l`(논리), `load_r`(실수), `load_lbc`(`T_LBC` 측방경계 스위치 구조체), `load_s1d/s2d`(`T_IO` I/O 구조체). C-grid 변수타입·LBC·I/O 구조체 적재의 핵심 디코더.

### 14.3 `yaml_parser.F` (모듈 `yaml_parser_mod`)
YAML 입력파일 처리 — OOP·표준 혼합형 경량 파서(`yaml_parser.F:10-23`). 제약: 단순화를 위해 **파일을 2회 읽음**(1차: 들여쓰기 정책·collection 길이 결정)(`yaml_parser.F:24-27`). 지원: `#` 주석, 무제한 중첩 구조(들여쓰기로 구조 표현), 자유 스키마 들여쓰기(`yaml_parser.F:28-34`). FCKit·Fortran-YAML·yaFyaml 대안 언급(`yaml_parser.F:14-17`).

---

## 15. 부동소수 라운딩 — `round.F` (모듈 `round_mod`)

Fuzzy/Tolerant floor 함수(`round.F:9-10`). 저자 H. D. Knoble (`round.F:4`). 공개(`round.F:58`): `TFLOOR`(tolerant floor). 함수(`round.F:64-154`):
- `ROUND(X,CT) = TFLOOR(X+0.5, CT)` (`round.F:79`)
- `TCEIL(X,CT) = -TFLOOR(-X, CT)` (`round.F:100`)
- `UFLOOR` (untolerant floor) (`round.F:135-154`)

비교허용치 `CT` (`0<CT<=(3-√5)/2`) 내면 가장 가까운 정수 반환(`round.F:18-25`). 격자 fractional index·날짜 계산 등의 정수 경계 처리에 사용.

---

## 미확인 / source-needed

- `stiffness.F` 의 부피·면적 통계(`omn`·`h`·`Cu` 등) 추가 진단 라인: 미인용 (source-needed)
- `cinterp2d` (bicubic) 의 12개 계수 산출 본체(`interpolate.F:447-720`): 헤더만 인용, 계수식 세부 미전사 (분량 비례 생략)
- `set_scoord.F` Vstretching=2/3/4/5 (Shchepetkin·Geyer 등) 분기: Vstretching=1 만 식 인용, 나머지 분기는 라인 위치만 언급 (`set_scoord.F:449-506`)
- 난수 엔진 `ran1.F`·`gasdev.F`·`ran_state.F`·`nrutil.F`: Numerical Recipes 계열, 미세분석 안 함
