---
title: SFINCS 비정수압·wavemaker·파-증강 조도 (단파해상 옵션)
model: SFINCS
component: nonhydrostatic / wavemaker / wave-enhanced-roughness
canonical_source: self
citation_status: verified
verification_method: >
  source/src/sfincs_nonhydrostatic.f90 (1-746), source/src/sfincs_wavemaker.f90
  (1-1763), source/src/sfincs_wave_enhanced_roughness.f90 (1-76) 전수 Read 후
  서브루틴별 file:line 직접 확인. 모든 식·자료구조·주석 verbatim 인용은 해당 라인 재확인.
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "[[sfincs-architecture-source-map]]"
---

# SFINCS 비정수압·wavemaker·파-증강 조도

SFINCS의 **단파해상(short-wave resolving)** 확장 3종을 다룬다. 기본 SFINCS는 정수압(hydrostatic) reduced-complexity 모델이지만, (1) 비정수압 압력 보정으로 단파 분산(dispersion)을 도입하고, (2) wavemaker 경계에서 IG/incident 파를 생성하며, (3) 파 궤도속도로 바닥 조도를 증강한다.

모듈 개관:

| 모듈 | 파일 | 핵심 역할 |
|---|---|---|
| `sfincs_nonhydrostatic` | `sfincs_nonhydrostatic.f90` | 비정수압 압력 $p_{nh}$를 sparse matrix로 풀어 flux/velocity 보정 → 분산 |
| `sfincs_wavemaker` | `sfincs_wavemaker.f90` | 파 생성 경계점 식별 + IG/incident 파 spectrum 생성 + weakly-reflective flux |
| `sfincs_wave_enhanced_roughness` | `sfincs_wave_enhanced_roughness.f90` | 파 궤도속도 $U_w$로 유효 마찰계수 증강 |

---

## 1. 비정수압 (`sfincs_nonhydrostatic.f90`)

### 1.1 적용 제약 (header)

파일 최상단 주석(`sfincs_nonhydrostatic.f90:1-3`)이 한계를 명시한다:

> `! Non-hydrostatic code now only works with regular grids (can still use quadtree netcdf file as long as there are no refinement levels).`
> `! Now uses bicgstab_ilu to solve matrix. Both should ideally utilize CPU and GPU parallelization. Currently, this solver cannot be fully parallelized.`

즉 **정칙 격자 전용**(quadtree refinement 불가), solver는 `bicgstab_ilu` (ILU 전처리 BiCGStab). solver 자체는 완전 병렬화 불가로 명기.

### 1.2 자료구조 (모듈 변수, `:7-28`)

| 변수 | 타입 | 의미 |
|---|---|---|
| `index_sparse_matrix(5,nrows)` | int | 셀당 5-스텐실(좌1·우2·하3·상4·중심5)의 sparse 배열 위치 (`:7`, 채움 `:236-330`) |
| `nh_uv_index(4,nrows)` | int | 각 행(셀)에 인접한 nh uv 점 인덱스 (`:8`) |
| `nm_index_of_row` / `row_index_of_nm` | int | 행↔nm 양방향 매핑 (`:9-10`, `:103-111`) |
| `uv_index_of_nhuv(nhuv)` | int | nh uv 점 → 전체 uv 배열 인덱스 (`:11`, `:141-157`) |
| `col_idx` / `row_ptr` | int | CSR 형식 (`:12-13`, `:335-337`) |
| `pnh(nrows)` | real4 | 비정수압 압력 (해 벡터) (`:15`) |
| `ws`, `wb`, `wb0` | real4 | 표면/바닥 연직속도 (현·이전 시각) (`:16-18`) |
| `Dnm` | real4 | 셀 수심 (`:20`) |
| `dzbdx`, `dzbdy` | real4 | 바닥 경사 (`:21-22`) |
| `huthresh_nh` | real4 | nh 최소 수심 임계 = `max(huthresh, 0.01)` (`:24`, `:80`) |

### 1.3 초기화 `initialize_nonhydrostatic` (`:32-388`)

- **행 카운트**: `mask_nonh(nm)==1`인 셀만 행으로 (`:56-64`, `:105-111`). nh 활성 영역만 풀이.
- **nh uv 점 식별**: uv 점이 인접 두 셀 중 하나라도 nh 마스크면 포함 (`:131-139` 카운트, `:148-221` 방향별 매핑). 스텐실 도식은 `:115-123` 주석 (1=좌,2=우,3=하,4=상,5=중심).
- **sparse 구조 결정** (`:225-332`): 행별로 이웃 존재 시에만 항목 추가, CSR `row_ptr`/`col_idx0` 채움. 최종 비영(非零) 개수 `nr_vals_in_matrix` (`:334`).
- **바닥 경사** (`:341-386`): 4방향 이웃 zb 차분으로 `dzbdx`/`dzbdy` 계산, 예: 좌측 `dzbdx(irow) = dzbdx(irow) + 0.5*(zb(nm)-zb(nmd))*dxrinv(1)` (`:355`).

### 1.4 압력 보정 `compute_nonhydrostatic(dt, tloop)` (`:391-744`)

핵심: sparse 선형계 $\mathbf{AA}\cdot\mathbf{p}_{nh} = \mathbf{QQ}$를 풀어(`:631`) flux 보정. 주석(`:496`):

> `! Compute non-hydrostatic pressure by solving matrix AA * PP = QQ, where AA is a sparse matrix, PP is the nonh pressure, and QQ is the forcing`

단계별:

1. **셀 수심** `Dnm(irow) = max(zs(nm)-zb(nm), huthresh_nh)` (`:458`).
2. **AB 계수** (`:467-492`): uv 점이 양쪽 모두 충분히 젖었을 때 (`:479`)
   $$\text{AB} = \frac{(z_{s,nmu}-h_{nmu}) - (z_{s,nm}-h_{nm})}{D_{nm}+D_{nmu}}$$
   (`:487`, 여기서 $h = -z_b$). 바닥 경사 기여를 압력 항으로 반영하는 계수.
3. **행렬 채움** (`:505-627`): 상수 `dtover2rhodx2 = dt*dxr2inv(1)/(2*rhow)` (`:501`).
   - 이웃 비대각 항: 예 좌측 `AA(j) = dtover2rhodx2*(-1.0 + AB(nmd))` (`:525`), 우측 `*(-1.0 - AB(nmu))` (`:539`).
   - 중심 대각 항: `AA(j) = 2*dt/(rhow*Dnm(irow)**2)` (`:579`), 추가로 각 이웃이 대각에 `dtover2rhodx2*(1.0 ± AB)` 누적 (`:593,601,609,617`).
   - 강제항 `QQ(irow) = -(ws(irow) + wb0(irow) - 2*wb(irow))/Dnm(irow)` (`:589`)에 flux 발산 기여를 더함 (`:595,603,611,619`).
4. **선형계 풀이**: `call bicgstab_solve(nrows, AA, col_idx, row_ptr, QQ, pnh, nh_tol, nh_itermax, iter, relres, .true.)` (`:631`). 허용오차 `nh_tol`, 최대 반복 `nh_itermax`.
5. **flux/velocity 보정** (`:640-671`): `dtover2rhodx = dt*dxrinv(1)/(2*rhow)` (`:635`).
   $$u_{nh} = -\,\text{dtover2rhodx}\,\big(\text{AB}\,(p_{nh,nmu}+p_{nh,nm}) + p_{nh,nmu}-p_{nh,nm}\big)$$
   (`:660`). **2dx 파 억제 nudging**(주석 `:662` `! Do some nudging to avoid 2dx waves`):
   ```
   q(ipuv)  = (1.0 - nh_fnudge)*q(ipuv)  + nh_fnudge*(q(ipuv)  + hu*unh)
   uv(ipuv) = (1.0 - nh_fnudge)*uv(ipuv) + nh_fnudge*(uv(ipuv) + unh)
   ```
   (`:664-665`). `nh_fnudge`가 nudging 강도.
6. **연직속도 갱신** (`:677-737`): `wb0 = wb`(이전 복사, `:684`) 후 4방향 flux로 바닥 연직속도 `wb` 재계산(예 `:702`), 표면속도
   $$w_s(irow) = w_s - (w_b - w_{b0}) + \frac{2\,dt}{\rho_w D_{nm}}p_{nh}$$
   (`:735`, 주석 `! this is ws m+1 in the next time step`). 주석 `:691` `! This will not yet work for quadtree !` — quadtree 미지원 재확인.

OpenMP 병렬 영역 다수(`:451,464,505,637,677`), 단 solver(`:631`)는 직렬.

---

## 2. Wavemaker (`sfincs_wavemaker.f90`)

파 생성 경계. 두 서브루틴: 셋업(`initialize_wavemakers`, `:8-1397`)과 시간갱신(`update_wavemaker_fluxes`, `:1400-1761`).

### 2.1 `initialize_wavemakers` (`:8-1397`)

기능 요약 (header `:9-13`): polyline 파일 읽기 → cross section 계산 → 보간 가중치 → 수심 보간.

- **polyline 읽기** (`:72-139`): `wavemaker_wvmfile` 파일에서 wavemaker 선 읽음. 선분별 격자 방향 대비 각도 `phip = atan2(dy,dx) + 0.5*pi` 후 `rotation` 보정·0~2π 정규화 (`:108-111`).
- **교차 셀 식별**: `find_cells_intersected_by_line(...)` (`:113`) → 임시 플래그 `indwm(ip)=1`, 각도 `phi(ip)=phip` 저장 (`:121-127`).
- **해안측 중복 제거** (`:141-457`): wavemaker 셀이 더 해안에 가까운 wavemaker 이웃을 가지면 제외. `phi`의 4사분면별로 검사 방향이 다름(`:153,226,299,372`). 유효하면 `kcs(ip)=4` 부여 (`:446-454`). 주석 `:141` `! Now get rid of cells that have neighbor closer to shore that is also a wavemaker point`.
- **uv wavemaker 점 설정** (`:476-1163`): `kcs==4` 셀의 비-wavemaker(`kcs==1`) 이웃 uv 점들을 wavemaker uv 점으로 등록. 각 점에 방향 `wavemaker_idir`(±1), 각도계수 `wavemaker_angfac` 부여. 예 우측 1차 이웃(`:784-790`): `idir=1`, `angfac=max(cos(phi(ip)-0.0),0.0)`. 위쪽은 `max(sin(phi),0)` (`:836`), 좌측은 `max(cos(pi-phi),0)` (`:886`), 아래쪽은 `max(-sin(phi),0)` (`:1032`).
- **quadtree refinement 경고**: 2차 이웃(`mu2/nu2/...`) 사용 시 `refinement_warning=.true.` (`:804,852,...`), 최종 경고 출력 (`:1167-1172`):
  > `' WARNING! Found wavemaker point along quadtree refinement boundary, this is not recommended! The simulation will continue.'`
- **kcuv 플래그**: wavemaker uv 점에 `kcuv(ip)=4` (`:1176-1181`).

#### 시계열 강제 (`wavemaker_wfpfile /= 'none'`, `:1193-1365`)

`wavemaker_timeseries=.true.` (`:1195`). IG 파만 지원(이후 `update`의 주석 `:1435` `! Only IG wave forcing supported at the moment !`).
- 강제점 좌표(`wfp`), 시각(`whi`), **IG 유의파고 `wavemaker_forcing_hm0_ig`**(`:1238-1241`), **IG 첨두주기 `wavemaker_forcing_tp_ig`**(wti, `:1249-1252`), **set-up**(wst, `:1257-1268`) 읽음.
- 시계열이 시뮬 기간 미포함 시 첫/끝 시각 조정 + 경고 (`:1271-1292`).
- 각 uv 점을 가장 가까운 두 강제점에 거리역가중 보간: `wavemaker_fac_wmfp(iwm) = dst2/(dst1+dst2)` (`:1316-1343`).

#### 주파수 성분 (`:1367-1395`)

- **IG 주파수** `wavemaker_nfreqs_ig`개, 균등 분할 `wavemaker_dfreq_ig = (freqmax_ig - freqmin_ig)/nfreqs_ig` (`:1373`), 중심주파수 (`:1375`), 위상 난수 초기화 `phi_ig = r*2π` (`:1376-1377`), 위상 표류 `dphi_ig = 1e-6*2π/freq` (`:1378`).
- **Incident 주파수** (`wavemaker_hinc`일 때만, `:1381-1395`) 동일 절차로 `wavemaker_nfreqs_inc`개.

### 2.2 `update_wavemaker_fluxes(t, dt, tloop)` (`:1400-1761`)

매 시간스텝 wavemaker uv flux 갱신.

#### 첨두주기 결정 (`:1433-1531`)

- **시계열 모드**: 시간 보간으로 `hs`, `tp_ig`, `setup` (`:1471-1473`), `tp_ig`는 강제점 평균 (`:1482`).
- **SnapWave 모드** (`:1485-1531`):
  - `wavemaker_Tinc2ig > 0`이면 `tp_ig = snapwave_tpmean * wavemaker_Tinc2ig` (`:1493`).
  - 아니면 `tp_ig = snapwave_tpigmean` (SnapWave가 Herbers spectrum 또는 사용자 비율로 계산, 주석 `:1514`). 10s 미만/250s 초과 시 DEBUG 경고 (`:1516-1523`).
  - `tp_inc = max(snapwave_tpmean, wavemaker_tpmin)` (`:1527`), `tp_ig = max(tp_ig, wavemaker_tpmin)` (`:1529`).
  - 주석 `:1495-1508`: Dean's a 기반 surfzone slope로 IG 주기 추정하는 옵션은 현재 branch에서 `snapwave_hsmean` 부재로 **주석처리**됨.

#### 파 신호 생성 (`:1533-1612`)

단위 Hm0=1.0m 기준 정규화 시계열 `zwav_ig`, `zwav_inc` 생성(`:1534-1535` 주석), 이후 실제 파고로 스케일.

- **Spectrum 모드** (`wavemaker_spectrum`, `:1540-1594`):
  - IG (`wavemaker_hig`): `fm_ig=1/tp_ig` (`:1546`), 위상 갱신(`:1554`), 성분 cos(`:1555`). 스펙트럼 형상 (`:1559`):
    $$a = 0.125\,f_m^{-2}\,f\,e^{-f/f_m}$$
    누적 `zwav_ig += cost_ig*sqrt(a*dfreq_ig)` (`:1561`).
  - Incident (`wavemaker_hinc`): ISSC(Bretschneider/수정 PM) 스펙트럼 (`:1576-1578`):
    $$a = 0.625\,f_m^{4}\,f^{-5}\,e^{-1.25 (f/f_m)^{-4}}$$
    `zwav_inc += cost_inc*sqrt(a*dfreq_inc)` (`:1580`).
- **Monochromatic 모드** (`:1596-1612`): `zwav_ig = 0.5*sin(2π t/tp_ig)` (`:1602`), `zwav_inc` 동일 (`:1608`).
- **Spin-up ramp**: `t < tspinup`이면 선형 `*(t-t0)/(tspinup-t0)` (`:1614-1619`).

#### Flux 계산 (GPU `!$acc parallel`, `:1631-1756`)

각 wavemaker uv 점 `ib`에 대해:
- 내측 수위 `zsnmi = zs(nmi)` (`:1643`).
- 경계측 수위: 시계열은 `zs0nmb = zs(nmb)+setup`, `zsnmb = zs0nmb + zwav_ig*hs` (`:1655-1656`). SnapWave는 IG/incident 각각 `zig = wavemaker_hm0_ig_factor*zwav_ig*hm0_ig(nmb)` (`:1664`), `zinc = wavemaker_hm0_inc_factor*zwav_inc*hm0(nmb)` (`:1665`).
- **파고 제한** (gammax): `zsnmb = zs0nmb + min(zinc+zig, wavemaker_gammax*dwvm)` (`:1677`), 초과 시 경고 (`:1679-1681`).
- 수심 `hnmb`: subgrid면 subgrid uv 테이블 보간 (`:1686-1714`), 아니면 `0.5*(zsnmb+zsnmi)-zbuv(ip)` (`:1717`).
- **Weakly-reflective 경계** (주석 `:1723`):
  $$u_i = \sqrt{g/h}\,(z_{s,nmb}-z_{s0,nmb}),\quad
  u_b = i_{dir}\big(2u_i - \sqrt{g/h}(z_{s,nmi}-z_{s0,nmb})\big)\cdot\text{angfac}$$
  (`:1734-1735`), flux `q(ip) = ub*hnmb + wavemaker_uvmean(ib)` (`:1737`). `hnmb < wavemaker_hmin`이면 `q=0` (`:1725-1731`).
- **이중지수 시간필터** (주석 `:1742`): `alpha=min(dt/filter_time,1)`, `beta=min(dt/(0.2*filter_time),1)` (`:1427-1428`). 평균/추세 갱신 (`:1746-1747`):
  ```
  wavemaker_uvmean(ib)  = alpha*q(ip) + wavemaker_filter_fred*(1.0-alpha)*(wavemaker_uvmean(ib)+wavemaker_uvtrend(ib))
  wavemaker_uvtrend(ib) = beta*(wavemaker_uvmean(ib)-uvm0) + (1.0-beta)*wavemaker_uvtrend(ib)
  ```
  `filter_time < 0`이면 평균 0 (`:1749-1753`).

---

## 3. 파-증강 조도 (`sfincs_wave_enhanced_roughness.f90`)

`update_wave_enhanced_roughness` (`:5-74`). 파 궤도속도가 바닥 마찰을 키우는 효과를 유효 Manning n으로 환산.

- **가드**: `wave_enhanced_roughness`가 꺼져 있으면 즉시 return (`:14`).
- uv 점 루프 (`kcuv==1` 또는 `==6`, `:21`). 기본값으로 `gnapp2(ip) = subgrid_uv_navg_w(ip)` 설정 — 이미 $g n^2$로 변환된 값 (주석 `:30`).
- **파 궤도속도** `Uw = 0.5*(uorb(nm)+uorb(nmu))` (`:32`). `Uw < 0.1`이면 skip (`:39`).
- **흐름속도** `Uc = max(sqrt(uu*2 + vu**2), 0.25)` (`:37`; `vu`는 4점 평균 `:35`).
  ※ 주의: `uu*2`는 통상 $u^2$가 아닌 `uu`의 2배 — 소스 그대로이며 잠재적 오타 의심. 인용: `sfincs_wave_enhanced_roughness.f90:37`.
- 수심 `hu = subgrid_uv_havg_zmax(ip) + zsu` (`:42`), `hu < 0.1` skip (`:44`).
- **기저 마찰**: `n_base = sqrt(subgrid_uv_navg_w(ip)/g)` (`:48`), `cd = g*n_base**2 / hu^(1/3)` (`:50`).
- **Ruessink (2001)** 유효 마찰 (주석 `:52`):
  $$c_{d,\text{eff}} = c_d\,\frac{\sqrt{(1.16\,U_w)^2 + U_c^2}}{U_c}$$
  (`:54`). 대안으로 Grant & Madsen (1979)/Soulsby (1997) `cdeff = cd*(1.4*Uw + Uc)/Uc`는 주석처리 (`:56-58`).
- **유효 Manning**: `n_app = sqrt(cdeff*hu^(1/3)/g)` (`:60`), `gnapp2(ip) = g*n_app**2` (`:62`).
- CPU에서만 계산되므로 마지막에 GPU 메모리 갱신 `!$acc update device(gnapp2)` (주석 `:70`, `:72`).

---

## 4. 검수 노트

- 비정수압: 정칙 격자 전용, BiCGStab-ILU solver 직렬, `nh_fnudge` nudging으로 2dx 파 억제 — 모두 소스 명기 (`:1-3, :631, :662-665`).
- wavemaker: 현재 시계열 강제는 **IG만 지원**(`:1435`), SnapWave 연계 시 IG+incident 모두 가능. Dean's a 기반 IG 주기 추정은 비활성(주석, `:1495-1508`).
- 파-증강 조도: `Uc` 계산의 `uu*2` (`:37`)는 $u^2$ 의도로 보이나 소스는 `uu`의 2배로 작성됨 — 잠재 버그로 기록(날조 아님, 라인 그대로).

상위 아키텍처·flux solver 등 일반 흐름은 [[sfincs-architecture-source-map]] 참조.
