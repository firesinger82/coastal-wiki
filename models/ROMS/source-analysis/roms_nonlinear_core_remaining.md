---
title: "ROMS Nonlinear 코어 잔여 — 압력경사·상태방정식·연직속도·진단·연직경계·깊이좌표"
model: ROMS
component: ROMS/Nonlinear
canonical_source: self
citation_status: verified
verification_method: "ROMS 소스 직접 read (roms/ROMS/Nonlinear/). prsgrd.F·prsgrd31.h·prsgrd32.h·prsgrd40/42/44.h(압력경사 옵션), rho_eos.F(Jackett-McDougall EOS), omega.F(S-좌표 연직속도+OMEGA_IMPLICIT), wvelocity.F(true w), diag.F(에너지·Courant), set_vbc.F(표면/바닥 응력), set_zeta.F, set_depth.F(Vtransform 1/2), set_massflux.F(Huon/Hvom), pre_step3d.F·ini_fields.F 헤더를 file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/ROMS/source-analysis/roms_main_driver_dispatch.md
  - models/ROMS/source-analysis/roms_baroclinic_3d.md
  - models/ROMS/source-analysis/roms_barotropic_2d.md
  - models/ROMS/source-analysis/roms_grid_metrics.md
  - models/ROMS/README.md
---

# ROMS Nonlinear 코어 잔여 — 압력경사·상태방정식·연직속도·진단·연직경계·깊이좌표

> Nonlinear 커널 root 파일 중 기존 노트 미커버 루틴. 경로: `roms/ROMS/Nonlinear/`. 3D 엔진 한 스텝의 보조·진단 루틴 — 압력경사(prsgrd), 상태방정식(rho_eos), 연직속도(omega·wvelocity), 진단(diag), 연직경계조건(set_vbc), 자유표면/깊이/질량플럭스 세팅(set_zeta·set_depth·set_massflux), 사전스텝(pre_step3d)·초기화(ini_fields).

기존 노트와의 경계: 평균이류·수평확산·연직혼합·2D/3D 시간적분 본체는 [[roms_advection]] · [[roms_horizontal_mixing]] · [[roms_vertical_mixing]] · [[roms_barotropic_2d]] · [[roms_baroclinic_3d]] 가 커버. 본 노트는 그 사이를 메우는 **상태·진단·세팅** 루틴에 집중. 깊이/메트릭 일반론은 [[roms_grid_metrics]] 참조(여기서는 시간진화 깊이만).

---

## 1. 압력경사항 prsgrd — 옵션 디스패치

`prsgrd.F` 자체는 cppdefs로 5개 헤더 중 하나를 include 하는 셀렉터다 (`prsgrd.F:16-26`):

| cppdef | include 헤더 | 스킴 | 참조 |
|---|---|---|---|
| `PJ_GRADPQ4` | prsgrd44.h | finite-volume Jacobian, quartic 재구성 + PPM+power-law 한정자 | Shchepetkin & McWilliams 2003 (`prsgrd44.h:11-30`) |
| `PJ_GRADPQ2` | prsgrd42.h | finite-volume Jacobian, quartic 재구성 + PPM 한정자 | SM2003 (`prsgrd42.h:11-25`) |
| `PJ_GRADP` | prsgrd40.h | finite-volume pressure Jacobian (Lin 1997) | Lin 1997 (`prsgrd40.h:10-21`) |
| `DJ_GRADPS` | prsgrd32.h | 비보존 Density-Jacobian, cubic 다항식 + harmonic-mean 단조화, anti-symmetry `J(rho,z_r)=-J(z_r,rho)` | SM2003 (`prsgrd32.h:10-30`) |
| (기본) | prsgrd31.h | STANDARD 또는 WEIGHTED density Jacobian (Song 1998) | Song 1998 (`prsgrd31.h:10-23`) |

공통 헤더 주석: "computes the baroclinic hydrostatic pressure gradient term" (`prsgrd.F:11-12`), 결과는 우변 배열 `ru`,`rv` (m4/s2) 로 적재.

### 1.1 기본 스킴 prsgrd31.h 의 식 (대표 인용)

표면 baroclinic 경사 (XI 방향, `prsgrd31.h:211-237`):

- 상수: `fac1=0.5*g/rho0`, `fac2=1000*g/rho0`, `fac3=0.25*g/rho0` (`prsgrd31.h:211-213`).
- 표면항:
$$\phi_x = \text{fac1}\,(\rho_i-\rho_{i-1})\,[(z_w-z_r)_i+(z_w-z_r)_{i-1}]$$
(`prsgrd31.h:221-224`).
- `RHO_SURF` 정의 시 자유표면 기여 추가 (`prsgrd31.h:231-235`), `ATM_PRESS` 시 대기압 항 `fac*(Pair_i-Pair_{i-1})`, `fac=100/rho0` (`prsgrd31.h:208-210, 228-230`), `WEC_VF` 시 `zetat` 차 (`prsgrd31.h:225-227`), `TIDE_GENERATING_FORCES` 시 `eq_tide` 보정 (`prsgrd31.h:217-219`).
- 우변 적재: `ru(i,j,N,nrhs) = -0.5*(Hz_i+Hz_{i-1})*phix*on_u` (`prsgrd31.h:236-237`).

내부(interior) 경사는 표면에서 바닥으로 차분 후 연직 적분 — 주석 "Differentiate and then vertically integrate" (`prsgrd31.h:246-247`); k-루프가 `N-1→1` 역방향으로 `phix` 누적 (`prsgrd31.h:249, 279-281`).

`WJ_GRADP` 정의 시(weighted Jacobian, Song 1998) `gamma` 가중 보정이 추가됨 (`prsgrd31.h:251-269`). ETA 방향(`rv`/`phie`)은 `j.ge.JstrV` 분기에서 대칭 처리 (`prsgrd31.h:299-376`).

`DIAGNOSTICS_UV` 정의 시 각 항이 `DiaRU(...,M3pgrd)`,`DiaRV(...,M3pgrd)` 진단 슬롯에 복사됨 (`prsgrd31.h:241-243, 287-289`).

---

## 2. 상태방정식 rho_eos — Jackett & McDougall (1995)

> **심층·승격**: 전용 노트 [[roms_equation_of_state]] (2026-07-04) — bvf 단열 산출·alpha/beta 조립·linear branch·EFDC EOS cross-model 대조 보강. 아래는 요약.

`rho_eos.F:11-19`: "computes 'in situ' density ... as a function of potential temperature, salinity, and pressure from a polynomial expression (Jackett and McDougall, 1992)". 248 oceanographic 값에 fitting, 지오포텐셜 면을 따라 압력 변화 무시 → 깊이(m, 음수)와 압력(dbar, 음수)을 호환적으로 사용 (`rho_eos.F:16-19`).

체크값 제공 (T=3°C, S=35.5 PSU, Z=-5000 m): `alpha=2.1014611551470e-04`, `beta=7.2575037309946e-04`, `den=1050.36...`, `sound=1548.88...` 등 (`rho_eos.F:21-29`).

### 2.1 비선형 EOS (NONLIN_EOS) 다항식

- 유효 범위: 잠재온도 −2~40°C, 염분 0~42 PSU (`rho_eos.F:247-249`).
- 입력 클램프: `Tt=MAX(-2, t(itemp))`, `Ts=MAX(0, t(isalt))`, `sqrtTs=SQRT(Ts)`, 압력 = `Tp=z_r` (`rho_eos.F:259-268`).
- 1기압 밀도: 계수 `C(0..2)` 가 Tt 의 Horner 다항식, `den1 = C(0)+Ts*(C(1)+sqrtTs*C(2)+Ts*W00)` (`rho_eos.F:274-285`). 계수 상수(Q00,U00,V00,W00...)는 `mod_eoscoef`/scalars에서 정의 (본 파일은 사용만).
- 할선 부피탄성률(secant bulk modulus): `C(3..9)` 다항식, `bulk = bulk0 - Tp*(bulk1 - Tp*bulk2)` (`rho_eos.F:301-322`).
- in-situ 밀도 이상: `cff=1/(bulk+0.1*Tp)`, `den = den1*bulk*cff`, 끝에서 −1000 (`rho_eos.F:342-355`).
- `SEDIMENT && SED_DENS` 시 부유사 농도로 밀도 보정 (`rho_eos.F:344-353`).
- `EOS_TDERIVATIVE` 시 `Dden1DS`,`Dden1DT`,`DbulkDS`,`DbulkDT` 도함수 → `alpha`(열팽창)·`beta`(염수축) 계수 산출 (`rho_eos.F:277-335`); 이 계수는 LMD KPP·BULK_FLUXES·BALANCE_OPERATOR 가 정의될 때만 필요 (`rho_eos.F:91-98, 324-325`).

### 2.2 연직평균 밀도(rhoA, rhoS)

`VAR_RHO_2D` 정의 시 barotropic 압력경사에 쓰일 연직평균 밀도 `rhoA` 와 밀도 섭동 `rhoS` 를 무차원으로 산출 (`rho_eos.F:362-379`). N→1 적분 누적.

선형 EOS 분기는 `NONLIN_EOS` 미정의 시 별도 `rho_eos_tile` 본체로 처리(`rho_eos.F:108` 의 `# ifdef NONLIN_EOS` 분기).

---

## 3. 연직속도 omega.F — S-좌표 omega

`omega.F:11-16`: "computes S-coordinate vertical velocity (m^3/s), W=[Hz/(m*n)]*omega, diagnostically at horizontal RHO-points and vertical W-points". 저자 Shchepetkin (`omega.F:10`).

알고리즘 (`omega_tile`, `omega.F:96-377`):
1. **바닥에서 0** 으로 시작 `W(i,j,0)=0` (`omega.F:217`), k=1→N 로 수평 질량플럭스 발산 `-(Huon_{i+1}-Huon_i + Hvom_{j+1}-Hvom_j)` 을 연직 적분 (`omega.F:223-230`). 주석 "barotropic mass flux divergence is not used directly" (`omega.F:204`).
2. **점 소스**(LwSrc) 처리: `Dsrc==2` 면 격자셀 w-면 횡단 유량으로 W 재계산 + `Qsrc(k)` 추가 (`omega.F:251-277`).
3. **표면 0 보정**: 자유표면 W = d(zeta)/dt; S-좌표 등면 이동분 `wrk(i)*(z_w_k - z_w_0)` 을 빼서 표면에서 0 보장 — 비례계수는 바닥 0, 표면 1 의 선형 (`omega.F:286-299`). `WEC_VF` 시 `W_stokes` 도 차감 (`omega.F:296-298`).
4. 표면 `W(i,j,N)=0` 강제 (`omega.F:346-348`).
5. `SEDIMENT && SED_MORPH` 시 해저 변화에 따른 수체 부피변화 항 추가 (LwSrc 유사 접근, `omega.F:207-230`).

### 3.1 OMEGA_IMPLICIT — Shchepetkin (2015) 적응적 암시 연직이류

W 를 **명시(We)·암시(Wi)** 로 분할, 국소 흐름의 Courant 수에 따라 자동 조정 → 큰 시간스텝 허용 (`omega.F:18-29`). 참조 Ocean Modelling 91, 38-69 (`omega.F:26-28`).

- Courant 파라미터: `amax=0.75`(최대), `amin=0.60`(최소) (`omega.F:189-193`).
- 수평 Courant 수 `Cu_adv` 누적 (`omega.F:236-239`), 2D Courant `Cu_adv(i,0)=dt*pm*pn` (`omega.F:282`).
- 분할 로직: 연직변위를 `dz*amax` 와 비교, 3구간(cw≤cw_min / ≤cutoff*cw_max / else)으로 `cff` 결정 후 `W=cw_max2*Wi/cff`, `Wi=Wi-W` (`omega.F:325-342`). 변위가 amax*dz 초과 시 전량 Wi 로 (`W=0`) (`omega.F:340-342`).

LBC: `bc_w3d_tile` + (DISTRIBUTE) `mp_exchange3d` 로 W·Wi 교환 (`omega.F:353-373`).

### 3.2 scale_omega — m/s 변환

`scale_omega`: `Wscl = W*pm*pn` 로 omega 를 m/s 로 스케일 (`omega.F:413-423`), 주기경계 시 `exchange_w3d_tile` (`omega.F:427-431`).

---

## 4. wvelocity.F — 출력용 "true" 연직속도

`wvelocity.F:12-15`: "computes vertical velocity (m/s) at W-points from the vertical mass flux ... **solely for output purposes**". 즉 진단·출력 변수 `wvel` 만 채운다(예측 미사용).

관계식 (`wvelocity.F:140-150`):
$$H_z\,\omega = w - \frac{\partial z}{\partial t} - \mathrm{div}(z),\quad \mathrm{div}(z)=pm\,u\,\partial_\xi z + pn\,v\,\partial_\eta z$$

- 준수평 기여 `(Ui+Vj)·GRADs(z)` 를 `vert(i,j,k)` 에 누적 (`wvelocity.F:171-195`).
- 자유표면 시간변화 기여: barotropic 질량플럭스 발산 `(DU_avg1 차 + DV_avg1 차)/총수심` 을 수심 따라 선형분포 (`wvelocity.F:197-216`).
- RHO→W 점 이동에 **cubic 보간** 사용, 계수 cff1=3/8, cff2=3/4, cff3=1/8, cff4=9/16, cff5=1/16 (`wvelocity.F:205-209, 218-269`); 바닥/표면은 외삽 slope 사용 (`wvelocity.F:221-223, 251-253`).
- `OMEGA_IMPLICIT` 시 `Wi` 도 더함 (`wvelocity.F:230-237` 등).
- 시간평균 `DU_avg1`,`DV_avg1` 을 먼저 exchange (`wvelocity.F:152-169`), 결과는 `bc_w3d_tile`+mp_exchange3d (`wvelocity.F:273-284`).

---

## 5. diag.F — 진단(에너지·Courant·blow-up 감지)

`diag.F:11`: "computes various diagnostic fields". `ninfo` 스텝마다만 수행 (`diag.F:211`).

- **운동/위치 에너지**: `ke2d += Hz*0.25*u2v2`, `pe2d = 0.5*g*z_w(N)^2 + Σ (g/rho0)*Hz*(rho+1000)*(z_r-z_w(0))` (`diag.F:227-242`). 2D 모드는 `ke2d=(zeta+h)*0.25*u2v2`, `pe2d=0.5*g*zeta^2` (`diag.F:264-271`).
- **Courant 수**: `Cu=0.5*|u_i+u_{i+1}|*dt*pm`, `Cv`, `Cw=0.5*|wvel_{k-1}+wvel_k|*dt/Hz`, 합 `C=Cu+Cv+Cw`; 최대값과 위치 (i,j,k) 추적 (`diag.F:243-258`).
- **최대 속도·밀도**: `maxspeed`, `maxrho` 추적 (`diag.F:259-260`).
- 타일별→전역 합산(라운드오프 저감 2단계 합 `diag.F:289-322`), DISTRIBUTE 시 `mp_reduce`(SUM/MAX) + `mp_reduce2`(MAXLOC) (`diag.F:405, 424`).
- **로그 출력**: Master 가 step·시각·KE·PE·총E·체적·Courant·MaxSpeed 출력 (`diag.F:471-508`).
- **blow-up 감지**: KE/PE 문자열에 'N'/'n'/'*'(NaN/Inf) 검출 시 `exit_flag=1` (`diag.F:512-521`); `maxspeed > max_speed` 또는 `maxrho > max_rho` 초과 시도 정지 (`diag.F:526-543`). 주석 "good way to screen for very bad values which indicates that the model is blowing-up" (`diag.F:535-536`).
- 임계영역 `!$OMP CRITICAL (NL_DIAGNOSTICS)` (`diag.F:340, 566`).

---

## 6. set_vbc.F — 연직(표면/바닥) 경계조건

`set_vbc.F:11-14`: "sets vertical boundary conditons for momentum and tracers". `NONLINEAR` 정의 시 활성, `SOLVE3D` 분기에 본체 (`set_vbc.F:3, 24`).

### 6.1 표면 트레이서 플럭스 (stflx)
- 온도: `stflx(itemp)=stflux(itemp)`(외부), `btflx(itemp)=btflux(itemp)` (`set_vbc.F:304-305`).
- 단파 침투(solar) 추가 (`set_vbc.F:323-326`).
- 결빙 억제: cooling 부호 규약상 결빙 시 추가냉각 차단 (`set_vbc.F:336-355`).
- 염분: E-P (증발-강수) 플럭스 `stflx(isalt)=EmP*t(isalt)` 또는 nudging (`set_vbc.F:378-399`); 바닥 `btflx(isalt)*t(...,1,...)` (`set_vbc.F:402`).

### 6.2 표면 운동량(빙붕 캐비티) 응력
`ICESHELF` 캐비티 시 바람응력을 캐비티 응력으로 대체 — 드래그 방식별 분기 (`set_vbc.F:449-556`):
- `UV_LOGDRAG`: 로그층 `Cd=vonKar^2/log^2((z_w-z_r)/ZoBot)`, `Cdb_min/max` 클램프 (`set_vbc.F:454-490`).
- `UV_QDRAG`: 2차 `rdrag2` (`set_vbc.F:491-520`).
- `UV_LDRAG`: 선형 `rdrag` (`set_vbc.F:521-540`).

### 6.3 바닥 응력 (bustr/bvstr)
표면과 동일한 3-드래그 패밀리 (`set_vbc.F:602-702`):
- 로그/2차: `bustr=0.5*(rdrag2_{i-1}+rdrag2_i)*u(1)*sqrt(u^2+v^2)` (`set_vbc.F:646-648`).
- 선형: `bustr=0.5*(rdrag_{i-1}+rdrag_i)*u(1)` (`set_vbc.F:680-681`).
- `LIMIT_BSTRESS` 시 응력 크기를 `|u|*cff3` (cff3∝Hz) 로 제한, 부호 보존 `SIGN(1, bustr)*MIN(...)` (`set_vbc.F:611-616, 649-654, 682-687`).
- LBC: `bc_u2d_tile`/`bc_v2d_tile` + mp_exchange2d (`set_vbc.F:706-718`).

> 참고: BBL 모델(SSW/MB) 사용 시 바닥응력은 `Nonlinear/BBL/`에서 계산 — [[roms_bottom_boundary_layer]] 참조. set_vbc 의 단순 드래그는 `!BBL_MODEL` 또는 ICESHELF 조건에서 활성 (`set_vbc.F:282`).

---

## 7. set_zeta.F — 자유표면 fast-time 평균

`set_zeta.F:13`: "sets free-surface to its fast-time averaged value". 2D 적분 준비로 `zeta(:,:,1)=zeta(:,:,2)=Zt_avg1` (시간스텝 "n" 에 해당) (`set_zeta.F:96-106`). `Zt_avg1` 은 barotropic 모드의 fast-time 평균(자유표면) — coupling 모듈에서 온다 (`set_zeta.F:49`). 주기경계 exchange (`set_zeta.F:108-124`).

---

## 8. set_depth.F — 시간진화 깊이좌표 (Vtransform 1/2)

`set_depth.F:12`: "computes the time evolving depths of the model grid". 자유표면 변동에 따라 매 스텝 z_w·z_r·Hz 갱신.

서브루틴 구성:
- `set_depth_tile` — 시간진화 깊이 (`set_depth.F:76-276`)
- `set_depth0_tile` — 정지(zeta=0) 기준 깊이 (`set_depth.F:318-481`)
- `set_depth_bry_tile` — 경계 깊이 (`set_depth.F:522-803`)

### 8.1 Vtransform=1 (원래 정식, `set_depth.F:136-179`)
$$z_w = Z_{o,w} + \zeta\,[1 + Z_{o,w}/h],\quad Z_{o,w}=h_c[s(k)-C(k)] + C(k)\,h$$
구현: `z_w0=cff_w+cff1_w*hwater`, `z_w=z_w0+Zt_avg1*(1+z_w0*hinv)` (`set_depth.F:168-169`), 여기서 `cff_w=hc*(sc_w-Cs_w)`, `hinv=1/hwater` (`set_depth.F:158-167`).

### 8.2 Vtransform=2 (새 정식, `set_depth.F:181-225`)
$$z_w = \zeta + (\zeta+h)\,Z_{o,w},\quad Z_{o,w}=\frac{h_c\,s(k)+C(k)\,h}{h_c+h}$$
구현: `hinv=1/(hc+hwater)`, `cff2_w=(cff_w+cff1_w*hwater)*hinv`, `z_w=Zt_avg1+(Zt_avg1+hwater)*cff2_w` (`set_depth.F:212-216`).

공통: `z_w(i,j,0)=-h(i,j)` (`set_depth.F:155, 200`), `Hz(i,j,k)=z_w(k)-z_w(k-1)` (`set_depth.F:176, 222`). `ICESHELF` 시 `hwater-=|zice|`, 깊이도 `-|zice|` 보정 (`set_depth.F:164-175, 209-221`). `WET_DRY` 시 h=0 → eps (`set_depth.F:150-154, 195-199`). 신축함수 `sc_r/sc_w/Cs_r/Cs_w` 는 SCALARS 구조체에 사전계산 (set_scoord 영역; 본 파일은 사용). exchange + mp_exchange (`set_depth.F:232-263`).

> S-좌표 정의·신축함수 일반론은 [[roms_grid_metrics]] 참조.

---

## 9. set_massflux.F — 수평 질량플럭스 Huon/Hvom

`set_massflux.F:13`: "computes horizontal mass fluxes, Hz*u/n and Hz*v/m". 구현 (`set_massflux.F:140-163`):
$$\text{Huon}=0.5(H_z^i+H_z^{i-1})\,u\,\text{on\_u},\quad \text{Hvom}=0.5(H_z^j+H_z^{j-1})\,v\,\text{om\_v}$$
`WEC` 정의 시 Stokes drift `u_stokes`/`v_stokes` 기여 추가 (`set_massflux.F:145-149, 156-160`) — [[roms_wec]] 참조. 결과는 omega·이류가 소비. exchange_u3d/v3d + mp_exchange3d (`set_massflux.F:167-182`).

`ADJOINT` 정의 시 `reset_massflux` 도 공개 (`set_massflux.F:21-23, 190`) — adjoint 재계산용, [[roms_adjoint_framework]] 참조.

---

## 10. pre_step3d.F — 새 3D 스텝 사전계산

`pre_step3d.F:13-27`: "initialize computations for new time step of the 3D primitive variables". 저자 Shchepetkin (`pre_step3d.F:11`). 모듈 시작에서 `# define NEUMANN` (`pre_step3d.F:4`).

역할 (헤더):
- **Adams-Bashforth** n-1·n-2 스텝 기여를 `nnew` 시간인덱스의 u,v 에 미리 추가 — 이후 3D 엔진에서 ru,rv(n-2)가 덮어쓰여지기 때문 (`pre_step3d.F:16-19`).
- **Crank-Nicholson** 암시 스킴의 시간 "n" 연직 점성·확산 기여 계산 — Hz 가 2D(barotropic) 엔진 끝에서 덮어쓰여지므로 미리 (`pre_step3d.F:21-24`).
- 실제 시간적분은 step3d_uv·step3d_t 에서 (`pre_step3d.F:26-27`) — [[roms_baroclinic_3d]].

본체 주요 블록 (`pre_step3d_tile`, `pre_step3d.F:126-1180`): 단파 침투분율 swdk (`326`), 중간 트레이서 n+1/2 (`348`), 수평·연직 이류에 의한 변화율 (`351, 627`), 인공 연속방정식(`811`), 연직 확산플럭스 FC (`858`), 새 트레이서 (`918`), U/V 점성 연직플럭스 + 새 운동량 (`939, 966, 1044, 1071`). (세부 알고리즘은 step3d 본체와 중복 — [[roms_baroclinic_3d]] · [[roms_vertical_mixing]] 참조.)

---

## 11. ini_fields.F — 시간레벨 초기화 + 2D/3D 결합

`ini_fields.F:12-14`: "initializes other time levels for 2D fields. It also couples 3D and 2D momentum equations: it initializes 2D momentum (ubar,vbar) to the vertical integral of initial 3D momentum (u,v)".

서브루틴:
- `ini_fields_tile` — 2D 필드 타임레벨 초기화 + ubar/vbar = ∫u,v (`ini_fields.F:137-715`); A-grid 출력용 RHO-점 운동량(ua,va) 계산 (`ini_fields.F:352`).
- `ini_zeta_tile` — 자유표면 초기화 (`ini_fields.F:764-990`); `SEDIMENT` 시 초기 bed 두께 합산 (`ini_fields.F:950`).
- `set_zeta_timeavg_tile` — zeta 시간평균 세팅 (`ini_fields.F:1028-1082`).

---

## 호출 맥락 요약

3D 엔진 한 스텝(`main3d.F`) 내 호출 순서 골격: `set_depth → set_massflux → omega → rho_eos → prsgrd → rhs3d → ... → pre_step3d → step3d_uv → step3d_t → set_zeta`, 그리고 진단은 `diag`, 출력 시 `wvelocity`. 정확한 디스패치 순서는 [[roms_main_driver_dispatch]] · [[roms_baroclinic_3d]] 참조.

⚠ 미커버(범위 외, 별도 노트 또는 source-needed): bc_2d/3d/4d·exchange_*·conv_*·get_data·set_data·output·set_avg·step_floats 등 I/O·교환·플로트 루틴은 본 노트 범위 밖.
