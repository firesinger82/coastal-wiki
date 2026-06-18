---
title: SFINCS flow solver — reduced-complexity SWE 코어 (momentum·continuity·advection-diffusion·time loop)
model: SFINCS
component: flow-solver
canonical_source: self
citation_status: verified
verification_method: >
  source/src/{sfincs_momentum.f90, sfincs_continuity.f90,
  sfincs_advection_diffusion.f90, sfincs_lib.f90, sfincs_timestep_analysis.f90}
  를 직접 Read. 인용한 모든 file:line 은 본문 작성 전 해당 라인을 직접 확인.
  기본값은 source/src/sfincs_input.f90 read_*_input 호출에서 확인.
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "[[sfincs-architecture-source-map]]"
---

# SFINCS flow solver

SFINCS 의 시간 적분 코어. **staggered grid + explicit** 으로 reduced-complexity 천수방정식(SWE)을 푼다. 한 time step 은 시간루프(`sfincs_lib.f90`)에서

1. `compute_fluxes` (운동량 → U/V 점의 flux `q`, 속도 `uv`)
2. `compute_water_levels` (연속방정식 → 수위 `zs` 또는 부피 `z_volume`)

순서로 실행된다 (`sfincs_lib.f90:584`, `sfincs_lib.f90:618`). [[sfincs-architecture-source-map]] §2 의 호출 순서를 본 노트가 알고리즘 레벨로 보완한다.

## 1. 자료구조 (staggered)

| 변수 | 위치 | 의미 | 인덱싱 |
|---|---|---|---|
| `zs` | z-point (cell center) | 수위 | `nm = 1..np` |
| `z_volume` | z-point | subgrid 모드 셀 부피 | `nm` |
| `q` | uv-point (cell edge) | 단위폭 flux | `ip = 1..npuv` |
| `uv` | uv-point | wet-averaged 속도 = `q / max(hu, huvmin)` | `ip` |
| `q0`, `uv0` | uv-point | 직전 time step 사본 | `ip` |
| `kcuv` | uv-point | 마스크: 1 정상, 6 연안측방경계 | `sfincs_momentum.f90:159` |
| `kfuv` | uv-point | wet 플래그 (0/1) | `sfincs_momentum.f90:726,747` |

이웃 인덱스는 미리 계산된 매핑 배열로 접근한다: U/V 점에서 좌우 수위점 `uv_index_z_nm`/`uv_index_z_nmu` (`sfincs_momentum.f90:165-166`), 수위점에서 사방 flux 점 `z_index_uv_md/mu/nd/nu` (`sfincs_continuity.f90:130-133`). 즉 격자 위상은 인덱스 배열에 인코딩되어 quadtree 비균일 격자도 동일 루프로 처리된다.

`compute_fluxes` 시작 시 직전 값을 복사한다: `q0(ip)=q(ip)`, `uv0(ip)=uv(ip)` (`sfincs_momentum.f90:132-133`). 이류·코리올리·점성 항은 이 `q0`/`uv0` (explicit, 직전 step 값) 으로 계산된다 (`sfincs_momentum.f90:317-335`).

## 2. 운동량 방정식 (`compute_fluxes`)

각 wet U/V 점에서 강제항 `frc` 를 누적한 뒤 Bates et al. (2010) 형식의 semi-implicit friction 갱신으로 새 flux 를 구한다.

### 2.1 wet 판정과 수심 `hu`

- 수위: `zsu = max(zs(nm), zs(nmu))` (`sfincs_momentum.f90:170`).
- subgrid: `zsu > zmin + huthresh` 면 wet (`sfincs_momentum.f90:177-178`). 비-subgrid: `zsu > zbuvmx(ip)` 이며 `zbuvmx = max(zb(nm),zb(nmu)) + huthresh` (`sfincs_momentum.f90:183`, 주석 동일 라인).
- subgrid wet 수심 `hu`: 셀 전체가 잠겼으면(`zsu>zmax`) 테이블 상한 + zsu (`sfincs_momentum.f90:351`), 아니면 subgrid 테이블 `subgrid_uv_havg` 의 선형보간 (`sfincs_momentum.f90:372-378`). 동시에 대표 마찰 `gnavg2`(=$gn^2$)와 wet fraction `phi` 도 같은 보간 (`sfincs_momentum.f90:377-378`).
- 비-subgrid: `hu = max(zsu - zbuvmx(ip), huthresh)`, `gnavg2 = gn2uv(ip)` (`sfincs_momentum.f90:384-385`).

`huthresh` 기본 0.05 m (`sfincs_input.f90:80`).

### 2.2 강제항 `frc`

압력(수면경사) 항이 베이스:

$$\text{frc} = -\,g\,h_u\,\frac{\partial z_s}{\partial x}$$

`sfincs_momentum.f90:409`, `dzdx = (zs(nmu)-zs(nm))*dxuvinv` (`:405`). `slopelim` (기본 9999.9, 사실상 off; `sfincs_input.f90:99`) 으로 경사 제한 가능 (`:401`).

이후 옵션 항을 `frc` 에 가산:

| 항 | 조건 | 코드 | file:line |
|---|---|---|---|
| 이류 | `advection` | `adv = -phi*(dqxudx+dqyudy)` 후 `frc+=adv` | `:500,:507` |
| 점성 | `viscosity` | `nuvisc*hu*(라플라시안 uu)` | `:519` (refinement 시 `:525`) |
| 코리올리 | `coriolis` | `frc ± fcoriouv*hu*vu` (U는 +, V는 −) | `:537,:541` |
| 바람 | `wind` | `frc += phi*tauwu(nm)` (얕으면 감쇠) | `:555,:570` |
| 대기압 | `patmos` | `hu*(patm(nm)-patm(nmu))*dxuvinv/rhow` | `:587` |
| 파랑 | `snapwave` | `phi*sign(min(|fwuv|,fwmax),fwuv)` | `:606` |

**이류**는 `mask_adv(ip)==1` (개경계 인근 off) 일 때만 (`:417`). 두 스킴:
- `advection_scheme==0` (original): 단순 upwind, $q>0$/$q<0$ 분기 (`:422-447`).
- `advection_scheme==1` (upw1, **기본** — `sfincs_input.f90:178` `'upw1'`, `:680`): 보존형 1차 upwind 으로 $\partial(qu)/\partial x = q\,\partial u/\partial x + u\,\partial q/\partial x$ 를 면적분값으로 전개 (`:448-498`, 식 주석 `:452-453`).

이류 가속도는 `advlim`(기본 1.0 m/s², `sfincs_input.f90:98`)로 클램프: `adv=min(max(adv,-advlim*hu),advlim*hu)` (`:505`).

코리올리·점성에 쓰는 V-속도는 인접 4점 평균 `vu=(...)/4` (`:335`).

### 2.3 마찰 + Bates 갱신

마찰에 쓰는 flux `qfr`:
- 막 wet 된 점(`kfuv(ip)==0`)은 평형 flux 추정 `qfr=sqrt(|dzdx|/(gnavg2/10))*hu^(5/3)` (`:616`).
- 그 외: `friction2d` 면 $\sqrt{q_x^2+(h_u v_u)^2}$ (`:624`), 아니면 원조 Bates `|q_x|` (`:630`).

새 flux (Bates et al. 2010 의 semi-implicit Manning friction):

$$q^{n+1} = \frac{q_{sm} + \text{frc}\cdot dt}{1 + \dfrac{g\,n^2\,dt\,|q_{fr}|}{h_u^{7/3}}}$$

`sfincs_momentum.f90:677`. 분자 `qsm` 은 보통 `qx_nm`(=`q0`)이며 `thetasmoothing` 시에만 이웃 평균과 혼합 (`:638,:653`, 기본 theta=1.0 → 비활성, `sfincs_input.f90:71`). $h_u^{7/3}$ 은 lookup table `power7over3` (`:667`, 함수 `:787-820`) 또는 직접 `hu**2*hu**(1/3)` (`:673`).

**후처리 한계들**:
- `wiggle_suppression` (subgrid, 기본 on `sfincs_input.f90:180`): 인접 셀 수위 가속 부호가 반대로 클 때 flux 감쇠 (`:683-687`).
- 음의 부피/수심 셀에서 유출 차단: `z_volume(nm)<0` 면 `q=min(q,0)` 등 (`:697-713`).
- flux limiter `uvlim` (기본 10 m/s, `sfincs_input.f90:184`): `q=min(max(q,-hu*uvlim),hu*uvlim)` (`:719`).
- 속도 `uv(ip)=q(ip)/max(hu,huvmin)` (`:724`); `huvmin` 기본 0.0 (`sfincs_input.f90:81`).

dry 점은 `q=uv=0`, `kfuv=0` (`:745-747`).

### 2.4 combined uv 점

quadtree 미세-조대 경계의 결합점 `ncuv` 개는 두 하위 uv 점 평균: `q(cuv)=(q1+q2)/2`, `uv` 동일 (`sfincs_momentum.f90:771-772`). 이 값이 연속방정식·출력에 쓰인다 (주석 `:759-761`).

## 3. 연속방정식 (`compute_water_levels`)

`subgrid` 여부로 분기 (`sfincs_continuity.f90:22-30`): subgrid → `compute_water_levels_subgrid`, 아니면 `compute_water_levels_regular`.

### 3.1 regular

점소스 먼저 (`:87-106`), 이후 각 `kcs(nm)==1` 셀:

$$z_s^{n+1} = z_s^n + \big[(q_{nmd}-q_{nmu})\,dx^{-1} + (q_{ndm}-q_{num})\,dy^{-1}\big]\,dt$$

`sfincs_continuity.f90:151` (projected). 강수 `netprcp*dt` (`:118`), 외부소스 `qext*dt` (`:126`) 선가산. geographic(`crsgeo`)은 위도별 셀폭 `dxm(nm)` 사용 (`:139`).

### 3.2 subgrid (부피 기반)

flux 발산으로 **부피 변화** `dvol` 누적 (`:355` geo / `:376` quadtree / `:380` regular), 강수·qext 를 `dvol += dzsdt*a*dt` 로 가산 (`:495`), storage volume 처리(`:499-531`) 후 `z_volume(nm) += dvol` (`:535`). 수위는 subgrid 테이블에서 역산:
- 완전 wet (`z_volume >= subgrid_z_volmax*0.999`): `zs=max(z_zmax,-20)+(vol-volmax)/a` (`:553`).
- 거의 dry (`<=1e-6`): `zs=max(z_zmin,-20)` (`:559`).
- 그 외: 부피→수위 테이블 `subgrid_z_dep` 선형보간 (`:565-568`).

`wiggle_suppression` 용 2차 도함수 `zsderv(nm)=zs - 2*zs11 + zs00` 저장 (`:575`) — 이를 §2.3 의 flux 감쇠가 사용.

### 3.3 부가 저장

`compute_store_variables` (`:626-720`): `vmax`(`:684`), `qmax`(`:691`), `twet`(`:700,707`) 누적. `zsmax`(최대수위)는 메인 루프 내에서 항상 갱신 (`:253`, subgrid `:614`).

## 4. 이류-확산 (tracer, 옵션)

`compute_tracer_fluxes` (`sfincs_advection_diffusion.f90:5`): wet uv 점마다 tracer flux. upwind 이류 + Fickian 확산:

$$\text{trflux} = q\cdot c_{up} + (c_{nm}-c_{nmu})\cdot \text{dico}$$

$q>0$ 면 상류농도 `trconc(nm)`, 아니면 `trconc(nmu)` (`:49-56`). `dico` 는 확산계수. 결합점 평균도 수행(`:77-85`).

> 주의: `:82` 의 `trflux(itracer, cuv_index_uv(icuv)) = (itracer, trflux(...)+...)/2` 는 인덱싱이 깨진 표현(컴파일 불가 형태)으로 보인다 — tracer 경로가 미완/비활성 가능성. 단언이 아니라 코드 그대로 관찰만 기록.

## 5. 시간 루프와 CFL (`sfincs_lib.f90`)

### 5.1 dt 결정

`compute_fluxes` 가 각 wet 점에서 CFL 후보를 계산:

$$\text{min\_dt\_ip} = \frac{1}{\max\!\big(\sqrt{g h_u},\,|uv|\big)\cdot dx^{-1}}$$

`sfincs_momentum.f90:731`, 전역 최소로 reduction `min_dt=min(min_dt,min_dt_ip)` (`:733`). 즉 dt 는 셀별 파속+이류속도의 CFL 로 매 step 적응.

루프에서 `alfa`(CFL 계수, 기본 0.5 — `sfincs_input.f90:70`)를 곱해 실제 dt:

```
dt = alfa * min_dt   ! min_dt 는 alfa 없이 momentum 에서 계산
dtchk = alfa * min_dt
```

`sfincs_lib.f90:391-392` (주석 `:391`). `min_dt` 상한은 `dtmax`(기본 60 s, `sfincs_input.f90:79`)로 momentum 진입 시 초기화 (`sfincs_momentum.f90:99`).

### 5.2 step 순서와 불안정 정지

한 step: `compute_fluxes(dt)` (`sfincs_lib.f90:584`) → (옵션 구조물·비정수압) → `compute_water_levels(t,dt)` (`:618`). `dtchk < dtmin`(불안정 시 dt 폭락) 이고 `nt>1` 이면 `error=1` 로 시뮬레이션 중단 후 마지막 출력 (`:634-646`). 메시지: `'Error! Minimum time step of ... reached ! Current velocity exceeded uvmax ...'` (`:638`).

## 6. timestep 진단 (`sfincs_timestep_analysis.f90`, 옵션)

`timestep_analysis` 활성 시 uv 점별 통계로 "어느 셀이 dt 를 제한하는가" 를 추적.

- `compute_fluxes` 진입 시 `timestep_analysis_required_timestep(ip)=dtmax` 로 리셋 (dry 셀은 dtmax 유지) (`sfincs_momentum.f90:112`), wet 점은 `min_dt_ip` 저장 (`:739`).
- `timestep_analysis_update(min_dt)` (`sfincs_lib.f90:588`): wet 점(`kfuv==1`)의 required dt 누적 평균, `times_wet++` (`sfincs_timestep_analysis.f90:51-55`), 전역 `min_dt` 와 거의 같으면(`<= min_dt+1e-6`) `times_limiting++` (`:59-61`).
- `timestep_analysis_finalize(nt)` (`sfincs_lib.f90:698`): 셀의 8개 이웃 U/V 점 평균 required dt 의 최소에 `alfa` 곱해 셀별 dt 맵, 유효 이웃 없으면 −1 (`sfincs_timestep_analysis.f90:178-188`), 제한 비율 `100*tmsl/nt` (`:192`).
- `timestep_analysis_write_log` (`sfincs_lib.f90:781`): 가장 자주 제한한 uv 점의 인덱스·좌표·제한 비율 로그 (`sfincs_timestep_analysis.f90:206-241`).

## 핵심 요약

- explicit, staggered, cell-center 수위 / cell-edge flux. 위상은 인덱스 배열에 인코딩 → quadtree 동일 처리.
- 운동량: 수면경사 압력항 + 옵션(이류 upw1 기본·점성·코리올리·바람·기압·파랑) → Bates(2010) semi-implicit Manning friction 갱신 (`sfincs_momentum.f90:677`).
- 연속: regular 는 수위 직접 갱신, subgrid 는 부피→테이블 역산 (`sfincs_continuity.f90:151` vs `:535,:553-568`).
- dt: 셀별 $1/(\max(\sqrt{gh},|u|)\,dx^{-1})$ 의 전역 최소 × `alfa`(0.5), 상한 `dtmax`(60 s); `dtmin` 미만 시 중단 (`sfincs_lib.f90:391,634`).
