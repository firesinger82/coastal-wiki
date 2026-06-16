---
title: "Delft3D flow2d3d 특수물리 — near-field 방류(DESA)·surf roller·비정수압 압력 projection"
model: Delft3D
component: flow2d3d/kernel(compute_nearfar·compute_roller·non_hydro)
canonical_source: self
citation_status: verified
verification_method: "Delft3D 소스 직접 read (src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src/). near_field.f90 dispatch(L392-655)·desa.f90 entrainment/sink/source(L361-654)·radstr.f90 radiation stress tensor(L212-373)·rollu.f90 roller energy(L85-116)·massfl.f90 mass flux(L96-117)·z_hydpres.f90 Poisson 행렬(L208-291,L474-485)·z_momcor.f90 velocity correction(L179-321) file:line 인용. 일부 솔버 내부(BiCGSTAB/ILU 세부)는 description 헤더만 인용."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/README.md
---

# Delft3D flow2d3d 특수물리 — near-field 방류(DESA)·surf roller·비정수압 압력 projection

> flow2d3d 커널의 3대 특수물리 모듈. 경로: `src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src/` (`compute_nearfar/`, `compute_roller/`, `non_hydro/`)

본 노트는 flow2d3d 구조격자 커널의 세 특수물리 영역을 다룬다. 일반 흐름·이송·난류는 기존 노트(`[[delft3d_flow_compute_aux]]`, `[[delft3d_turbulence]]`, `[[delft3d_adi_solver]]`, `[[delft3d_sigma_z]]`)와 파랑결합 전반은 `[[wave/delft3d_flow_wave_coupling]]` 참조. 여기서는 **near-field 방류 결합(COSUMO/CORMIX↔DESA)**, **surf roller 모델**, **비정수압(non-hydrostatic) 압력 projection** 의 지배식과 결합 방식에 집중한다.

---

## 1. Near-field 방류 결합 — `compute_nearfar/`

### 1.1 역할과 결합 구조

음·열 방류 플룸의 near-field(초기 희석/궤적)는 flow2d3d 격자보다 훨씬 작은 스케일이므로, 외부 적분 모델(CORMIX / CORJET / JET3D / COSUMO 일반 인터페이스)에 위임하고 그 결과를 flow 격자의 **source/sink 항**으로 되돌리는 양방향(FF↔NF) 결합이다.

`near_field.f90` 헤더 verbatim (compute_nearfar/near_field.f90:40-56):

```
!    Function: Converts flow results to cormix input
...
!    The master partition gathers all input arrays on the full global domain,
!    handles the communication with Cosumo/Cormix,
!    and calculates the arrays glb_disnf and glb_sournf (both on the full global
!    domain in n,m).
!    glb_disnf and glb_sournf are distributed to all partitions (call dfbroadc).
!    Each partition copies his part of these arrays to the local disnf/sournf in
!    nm.
```

병렬(MPI) 처리: master partition만 외부 모델과 통신·계산 → `dfgather`로 전역 입력 수집, `dfbroadc`로 `glb_disnf`/`glb_sournf`/`glb_nf_src_momu`/`glb_nf_src_momv` 전 partition 배포 (near_field.f90:386, 679-684), 각 partition이 자기 영역을 local `disnf(nm,:,:)`/`sournf(nm,:,:,:)`로 복사 (near_field.f90:692-710).

### 1.2 모델 dispatch — `nflmod`

`select case (nflmod)` 로 near-field 모델 분기 (near_field.f90:392). 현 소스에서 **`corjet`/`cortime`/`jet3d` 분기는 전부 주석 처리된 레거시**이며 (near_field.f90:393-450, 625-650), 실제 활성 경로는 `generic`(COSUMO XML 결합)이다 (near_field.f90:452). `nrfield` 분기는 빈 stub (near_field.f90:651-654).

| `nflmod` | 상태 | 변환 루틴(file) |
|---|---|---|
| `corjet`/`cortime` | 주석 레거시 | corjet2flow.f90 / cortim2flow.f90 |
| `jet3d` | 주석 레거시 | jet3d2flow.f90 (DESA of Joseph Lee, jet3d2flow.f90:490-491) |
| `generic` | **활성** | wri_FF2NF.f90 → nf_2_flow.f90 → desa.f90 |
| `nrfield` | stub | — |

`generic` 활성 흐름 (near_field.f90:452-624):
1. `corinp_gen2`로 settings.xml 읽기 (near_field.f90:466)
2. `findnmk`로 diffuser·ambient·intake의 (x,y,z)→(n,m,k) 변환 (near_field.f90:470-485)
3. `wri_FF2NF`로 각 방류구별 FF2NF XML 작성 (near_field.f90:540-547)
4. `wait_until_finished`로 외부 near-field 모델의 NF2FF 결과 대기 (near_field.f90:564)
5. `nf_2_flow`로 NF2FF XML 파싱 → `nf_intake`/`nf_sink`/`nf_sour` 채움 (near_field.f90:581)
6. `desa`로 Prof. Lee의 **DESA 방법**에 따라 source/sink 채움 (near_field.f90:589-595)

### 1.3 DESA(Distributed Entrainment Sink Approach) — `desa.f90`

헤더 verbatim (compute_nearfar/desa.f90:38-39): `! Converts Cosumo output to delft3d sources / following the DESA methodology of Joseph Lee`.

NF2FF 결과 테이블의 컬럼 인덱스 상수 (desa.f90:79-86):
`IX=1, IY=2, IZ=3, IS=4(dilution), IH=5(diffuser height), IW=6(width), IUMAG=7, IUDIR=8`.

**(a) Intake(취수) 처리** (desa.f90:224-294): intake 먼저 처리 — 취수농도 `conc_intake`가 source 처리에 쓰이기 때문. `disnf_intake`에 `dis_per_intake = nf_q_intake / wght_tot`를 음(-)으로 분배 (desa.f90:277, 282).

**(b) Sink(entrainment) 처리** (desa.f90:309-373): sink 점들을 순회하며 dilution 컬럼 IS 증분에 비례하는 entrainment 흡입량을:
$$ \text{dis\_dil} = (S_i - S_{i-1})\, Q_\text{source} $$
(desa.f90:367) — 이를 `disnf`(diffuser 방류 + entrainment 통합)와 `disnf_entr`(entrainment만)에서 빼낸다 (desa.f90:369-370). 이것이 DESA의 핵심: near-field에서 플룸이 빨아들인 주변수를 격자에 분산된 **sink**로 표현.

**(c) Source(희석 방류) 분배** (desa.f90:375-657): 두 경우로 분기 —
- `centre_and_width`(=TRUE): sink 존재 + source 1점. diffuser 중심·폭으로부터 sink-source 연결선에 수직한 선분을 정의, 1000-step 보행으로 분배 셀·가중치 결정 (desa.f90:376-454). 연결선 각도 `ang_end = atan2(ΔY, ΔX)`, 폭 투영 `dx=-W·cos(π/2-ang)`, `dy=W·sin(π/2-ang)` (desa.f90:405-407).
- 다중 source 또는 sink 없음(=FALSE): 각 source 점을 셀별로 누적, 마지막 컬럼이 weight면 그 값으로 가중 (desa.f90:455-537).

희석 방류량의 수직·수평 분배 (sigma-model, desa.f90:549-619):
$$ \text{disnf}(n,m,k) \mathrel{+}= \frac{Q_\text{source} + \text{dis\_tot}}{\text{thick\_tot}/(w\cdot\Delta\sigma_k)} $$
(desa.f90:591), entrainment 부분만 `disnf_entr`에 동일 형식으로 (desa.f90:592). 스칼라 농도 source는 `sournf(n,m,k,lcon)`에 — 배경온도(`flbcktemp`)면 마지막 step의 `r0`로, 아니면 절대(`NFLCONSTOPERATOR_ABS`)/상대 operator에 따라 `nf_const(lcon)` 사용 (desa.f90:593-619).

**(d) 운동량(momentum) source** (desa.f90:620-654): `nf_src_mom=.true.`일 때 방류 속도 크기/방향(IUMAG/IUDIR)을 `magdir_to_uv`로 u/v 성분으로 변환 (desa.f90:633-634). 주석 verbatim (desa.f90:639-641): `! Since momentum sources are located at edges instead of cells, we need to decide where to put them. / We add the momentum source to the downstream edge ... / This should avoid the occurrence of large vertical velocities as a reaction to large discharges in small cells.` 부호에 따라 downstream edge(`nf_src_momu(n,m-1,...)` 등)에 배치 (desa.f90:643-653).

### 1.4 flow 방정식으로의 환류(coupling back)

near_field가 채운 배열들이 메인 흐름 솔버에서 소비됨 (직접 확인, grep `src/`):
- `disnf`(질량 source/sink) → 연속방정식: `compute/sud.f90`, `compute/z_sud.f90`.
- `nf_src_momu`/`nf_src_momv`(운동량 source) → 운동량방정식: `compute/cucnp.f90`, `compute/uzd.f90`, `compute/z_cucnp.f90`, `compute/z_uzd.f90`.

near_field.f90:664-668 주석 verbatim: `! Fix by Wilbert: set nf_src_mom to True. Even when all NF2FF files only have 6 columns it doesn't hurt to put nf_src_mom to True, / as only zeros will be present in the glb_nf_src_momu and glb_nf_src_momv arrays, which means that it will not be taken into / account in the cucnp and z_cucnp routines`.

> NF2FF/FF2NF XML 파서 세부(read_xml_discharges/, xmlparse.f90 등)와 wait 로직(wait_until_finished.f90)은 IO 보일러플레이트라 본 노트 범위 밖. ⚠ DESA 이론 근거(Choi & Lee 논문)는 source-needed — 소스 주석은 "DESA methodology of Joseph Lee"만 명시(desa.f90:39).

---

## 2. Surf roller 모델 — `compute_roller/`

### 2.1 역할

쇄파대(surf zone)에서 파랑 에너지 → roller 에너지 전이, roller에 의한 추가 radiation stress·질량플럭스·운동량을 계산해 흐름에 결합한다. 파랑/roller 에너지 두 변수 `ewave`(유기파 에너지 밀도)·`eroll`(roller 에너지 밀도)를 이송·생성·소산한다.

### 2.2 파랑 에너지 이송·소산 — `difuwe.f90`, `waveu.f90`

`difuwe.f90` 헤더 verbatim (compute_roller/difuwe.f90:40-54): `! Computes transport of wave energy in u- and v-direction. / Implicit in the u-direction, and explicit in v-direction. / ... Sources are treated implicitly and sources explicitly.` — U방향 음해(higher-order upwind), V방향 양해(central), sink 음해/source 양해 (difuwe.f90:47-54).

`waveu.f90` 헤더 verbatim (compute_roller/waveu.f90:34): `! Computes wave energy dissipation terms due to breaking and bottom friction`. 출력 `df`(소산), `sinkw`(sink 계수).

### 2.3 Roller 에너지 balance — `rollu.f90`

헤더 verbatim (compute_roller/rollu.f90:34): `! Computes roller energy source and sink terms, as well as roller energy dissipation`.

roller sink 계수 (rollu.f90:97):
$$ \text{sinkr} = \frac{2\,g\,\beta_\text{roll}}{c} $$
여기서 $\beta_\text{roll}$는 roller slope 계수 `betarol`. `betarol<0`이면 동적으로 (rollu.f90:89-93):
$$ \beta_\text{tr} = 0.025\,\frac{1}{k\,h}\left(\frac{h-H_\text{rms}}{H_\text{rms}}\right)^2,\quad k=\frac{2\pi}{c\,T_p},\ H_\text{rms}=\sqrt{\frac{8E_w}{\rho g}} $$
roller 소산 `dis(nm,2) = sinkr·eroll0` (rollu.f90:99), roller source는 파랑 소산에서 바닥마찰분(df)을 뺀 것 (rollu.f90:104):
$$ \text{sourr} = \max\!\big(0,\ \text{sinkw}\cdot E_w - df\big) $$
총 소산 누적 `dis(nm,1)=dis2+dis3+dis4` (rollu.f90:115).

### 2.4 Radiation stress → 파랑력 — `radstr.f90`

헤더 verbatim (compute_roller/radstr.f90:38-41): `! calculation of wave forces from the divergence of / the stress tensor. The components of the stress / tensor can be obtained from the energy density / See "Extension of SURFBEAT model to two dimensions" by H. Petit`.

**stress tensor 성분** (radstr.f90:212-222), $n=c_g/c$ 비(=`cgc`), $\theta$=파향:
파랑부 ($E_w$):
$$ S^w_{xx}=(n-\tfrac12+n\cos^2\theta)E_w,\quad S^w_{xy}=n\,E_w\cos\theta\sin\theta,\quad S^w_{yy}=(n-\tfrac12+n\sin^2\theta)E_w $$
roller부 ($E_r$):
$$ S^r_{xx}=2\cos^2\theta\,E_r,\quad S^r_{xy}=2\,E_r\cos\theta\sin\theta,\quad S^r_{yy}=2\sin^2\theta\,E_r $$
(코드: 대각 `sw(1)=(en-0.5+en*costet*costet)*ewave1`(:213-214), `sr(1)=2*costet*costet*eroll1`(:215), `sw(3)`/`sr(3)` 대칭(:220-222). 비대각은 `sw(2)=en*ewave1`(:216)·`sr(2)=2*eroll1`(:217)에 이어 **`sw(2)=sw(2)*costet*sintet`(:218)·`sr(2)=sr(2)*costet*sintet`(:219)**로 $\cos\theta\sin\theta$ 가 곱해짐 — 비대각 응력에 방향 인자 필수).

파랑력 `fxw`/`fyw`는 stress tensor의 발산으로 계산 (radstr.f90:277-373). roller sink 기여를 wave-induced shear stress `wsu`/`wsv`로 추가 (radstr.f90:299-304, 354-359):
$$ \text{wsu} = \tfrac12\big(\text{sinkr}\cdot E_r\big|_{nm} + \text{sinkr}\cdot E_r\big|_{nm+1}\big),\quad f_{xw}\mathrel{-}=\text{wsu} $$
`wavfrc=.false.`면 파랑력 0 (radstr.f90:313, 368). `wsu`/`fxw`는 uzd/cucnp에서 gammax로 제한 (radstr.f90:315 주석).

### 2.5 질량플럭스(Stokes drift) — `massfl.f90`

gammax로 파랑·roller 에너지 제한 후 (massfl.f90:96-100, `emax=0.125·ρg·γmax²·h²`):
3D에서 roller 질량플럭스 (massfl.f90:107-109):
$$ \text{mass}_r = \frac{2E_r}{\rho\,c},\quad \text{rmasur}=\text{mass}_r\cos(\text{dir}),\ \text{rmasvr}=\text{mass}_r\sin(\text{dir}) $$
파랑+roller 총 질량플럭스 (massfl.f90:115-117):
$$ \text{mass} = \frac{E_w + 2E_r}{\rho\,c} $$
헤더 주석(massfl.f90:104-105): `! 3D: massflux resulting from roller is stored in rmasur/rmasvr / Waves massflux is obtained from stokes drift distribution`.

### 2.6 보조 루틴

| 파일 | 역할(file:line 헤더) |
|---|---|
| `rolcor.f90` | difu에서 쓰는 roller mass flux return flow·breaker delay 보정 (rolcor.f90:37-40); 기본설정(`eulerisoglm=false`)에선 euler.f90에서 처리 |
| `rbsig.f90` | 경계 wave component(Fourier) 입력 `wavcmp` 파일 읽기 — free/forced wave 분리, 자유표면 신호 (rbsig.f90:33-73) |
| `snel.f90` | Snel 굴절·파수(`wnr.f90`)·궤도속도 `uorb` 계산 (snel.f90 출력 uorb, L75) |
| `waveu.f90`/`rollu.f90` | 위 §2.2-2.3 |
| `orbvel.f90`,`turwav.f90`,`tapf.f90`,`le.f90`,`constwave.f90`,`varcon.f90`,`qkwbn.f90`,`qkwcg.f90`,`hds.f90`,`hds_wf.f90`,`wnr.f90` | 궤도속도·파-난류 상호작용·taper·선형보간(`le`)·상수파장·파수/군속도 등 보조 ⚠ 세부 source-needed |

> roller 모델 이론 근거는 코드가 명시한 H. Petit "Extension of SURFBEAT model to two dimensions"(radstr.f90:41) — 원문 검증은 source-needed.

---

## 3. 비정수압(non-hydrostatic) 압력 — `non_hydro/`

### 3.1 방식: pressure-correction projection

정수압 흐름을 예측자(predictor)로 풀고, 비정수압 압력 $p$를 **이산 비압축조건(incompressibility)**으로부터 Poisson 형 방정식으로 풀어 속도를 보정하는 projection(pressure-correction)법. z-layer 모델 전용(파일 접두 `z_`).

`z_hydpres.f90` 헤더 verbatim (non_hydro/z_hydpres.f90:44-50): `! The difference equations for the non-hydrostatic / pressure are derived from the discretized / incompressibility condition. / The non-hydrostatic pressure is computed for / a restricted horizontal area. / At the open boundaries the discretization / is such that it leads to a symmetric matrix.` — 비정수압은 제한된 수평영역(`m1_nhy..m2_nhy`, `n1_nhy..n2_nhy`)에서만 계산.

### 3.2 압력 Poisson 행렬 조립 — `z_hydpres.f90`

7-점 stencil 계수 (z_hydpres.f90:222-226 주석 도식):
```
!   horizontal:        cck2(m,n+1)            vertical:  bbkc(k+1)
!         aak(m-1,n) - bbk(m,n) - cck(m+1,n)            bbk(k)
!                      aak2(m,n-1)                       bbka(k-1)
```
계수 (dt=2·hdt, z_hydpres.f90:200, 247-254):
$$ \text{aak}=-\frac{\Delta z_u\,\Delta t}{\Delta x\,\Delta x_d\,\rho},\ \text{cck}=-\frac{\Delta z_u\,\Delta t}{\Delta x\,\Delta x_u\,\rho},\ \text{bbka}=-\frac{\Delta t}{\Delta z_d\,\rho},\ \text{bbkc}=-\frac{\Delta t}{\Delta z_\text{up}\,\rho} $$
대각 `bbk = -(aak+cck+aak2+cck2+bbka+bbkc)` (z_hydpres.f90:253-254).

RHS `ddk` = 예측자 속도장의 발산(=비압축 잔차) (z_hydpres.f90:255-257):
$$ \text{ddk} = -\frac{u_1\Delta z_u - u_1^{d}\Delta z_u^{d}}{\Delta x} - \frac{v_1\Delta z_v - v_1^{d}\Delta z_v^{d}}{\Delta y} - w_1^{(k)} + w_1^{(k-1)} $$
자유표면 셀에선 $-s_1/\Delta t + s_{00}/\Delta t$ 항과 대각에 $+1/(\Delta t\, g\,\rho)$ 추가 (z_hydpres.f90:288-291). 방류(discharge)는 NH 영역 내부일 때만 연속식에 추가 (z_hydpres.f90:296 주석).

### 3.3 선형 솔버 — CG / BiCGSTAB

`z_hydpres`가 `z_initcg`로 전처리 준비 후 `z_solcg` 호출 (z_hydpres.f90:474-485). 솔버 종류:
- `z_solcg.f90` — Conjugate Gradient (z_solcg.f90:37-38: `! Solves system of equations. / CG-method.`)
- `z_solbicgstab.f90` — BiCGSTAB (z_solbicgstab.f90:37-38: `! Solves system of equations. / BiCGSTAB-method.`)
- `z_precon.f90`(`! Computes the preconditioning`, z_precon.f90:34), `z_precon_ilu.f90`, `z_ilu_nhfull.f90`(ILU 전처리), `z_lu.f90`(LU)
- 수렴: `nhiter` 최대반복·`epsnh` 허용오차·`l2norm` 노름선택 (z_solcg.f90:56-58 pointer)

### 3.4 속도·자유표면 보정(projection 보정) — `z_momcor.f90`

압력 gradient로 예측자 속도를 보정 (dt=2·hdt, z_momcor.f90:169):
$$ u_1 \mathrel{-}= \Delta t\,\frac{p_1^{(nmu)}-p_1^{(nm)}}{\text{gvu}\,\rho},\qquad v_1 \mathrel{-}= \Delta t\,\frac{p_1^{(num)}-p_1^{(nm)}}{\text{guv}\,\rho} $$
(z_momcor.f90:185, 191), 수직속도 (z_momcor.f90:303):
$$ w_1 \mathrel{-}= \Delta t\,\frac{p_1^{(k+1)}-p_1^{(k)}}{\Delta z\,\rho} $$
자유표면 보정 (z_momcor.f90:179): $s_1 \mathrel{+}= p_1^{(kfsmax)}/(\rho g)$. 보정 후 유속 → 유량 `qxk=Δz_u·u_1·guu` 등 갱신 (z_momcor.f90:186, 192, 304). 누적압력 `p1+=p0`/`p1+=ag·ρ·(s00-s1)`, `w0=w1` 다음 step 준비 (z_momcor.f90:312, 320-321). s00은 momcor.f90에서 직전 step 수위로 설정됨 (z_hydpres.f90:264 주석).

### 3.5 수직 운동량방정식 — `z_vermom.f90`

헤더 verbatim (non_hydro/z_vermom.f90:38-40): `! Vertical momentum equation. Integration for / full timestep. w0 is vertical velocity at / end of previous non-hydrostatic timestep.` w-운동량을 삼중대각계 `aak/bbk/cck/ddk`(0:kmax)로 조립 (z_vermom.f90:80-83, 172-175). 수평이송 `u dw/dx + v dw/dy`(z_vermom.f90:213 주석, upwind 분기 L242-314), 수평확산 `rxz/ryz`(z_vermom.f90:202-206).

### 3.6 변형(variant) 파일

`*_nhfull` 접미 파일은 fully non-hydrostatic 변형: `z_hydpres_nhfull.f90`, `z_momcor_nhfull.f90`, `z_vermom_nhfull.f90`, `z_solcg_nhfull.f90`, `z_initcg_nhfull.f90`, `z_ilu_nhfull.f90`. 수평이송 이산화 변형 `z_vermom_horadv_iupw.f90`(1차 upwind)·`z_vermom_horadv_mdue.f90`(MDUE) (파일명 기준). ⚠ nhfull/horadv 변형 내부 세부는 source-needed.

| 파일 | 역할 |
|---|---|
| `z_hydpres.f90` | 압력 Poisson 조립 + CG 호출 (§3.2-3.3) |
| `z_momcor.f90` | 속도·수위 projection 보정 (§3.4) |
| `z_vermom.f90` | 수직 운동량(w) 방정식 (§3.5) |
| `z_solcg.f90`/`z_solbicgstab.f90` | CG / BiCGSTAB 선형솔버 |
| `z_initcg.f90`/`z_precon.f90`/`z_precon_ilu.f90`/`z_lu.f90`/`z_matpro.f90` | 솔버 초기화·전처리·LU·matrix-product |

---

## 4. 요약: 세 모듈의 결합 지점

| 모듈 | 입력 | 산출(배열) | 흐름 솔버 결합점(파일) |
|---|---|---|---|
| near-field(DESA) | COSUMO NF2FF XML | `disnf`(질량 sink/source), `sournf`(스칼라), `nf_src_momu/v`(운동량) | 연속: sud/z_sud; 운동량: cucnp/uzd/z_cucnp/z_uzd |
| surf roller | `ewave`,`eroll`,`c`,`cgc`,`dir` | `fxw`/`fyw`(파랑력), `wsu`/`wsv`(전단), `rmasu/v`,`rmasur/vr`(질량플럭스) | uzd/cucnp(파랑력,gammax 제한), difu(rolcor) |
| non-hydrostatic | 예측자 `u1,v1,w1,s1` | `p1`(비정수압), 보정 `u1,v1,w1,s1` | z_sud predictor → z_hydpres/z_momcor projection |

검증 한계: 외부 모델(CORMIX/COSUMO/JET3D) 자체·XML 스키마, roller/DESA 이론 원문, nhfull/horadv 변형 솔버 내부 세부는 본 노트에서 미인용(source-needed).
