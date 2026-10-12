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
last_source_check: 2026-10-12 (recovery 차이 결론 반영)
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

#### 문서에 빠진 wavemaker 입력

| 보고서 행 ID | 항목 | 근거 | 결론 |
|---|---|---|---|
| K072·K073·K074·K075·K076·K077·K078·K079·K080 | wavemaker 파일명 구 키워드와 새 키워드 | K072: `sfincs_input.f90:122` `if (wavemaker_wvmfile(1:4) == 'none') call read_char_input(500, 'wvmfile',    wavemaker_wvmfile,        'none') ! old keyword`<br>K073: `sfincs_input.f90:124` `call read_char_input(500, 'wavemaker_wfpfile',        wavemaker_wfpfile,        'none')     ! wavemaker forcing points file`<br>K074: `sfincs_input.f90:125` `if (wavemaker_wfpfile(1:4) == 'none') call read_char_input(500, 'wfpfile',    wavemaker_wfpfile,        'none')`<br>K075: `sfincs_input.f90:127` `call read_char_input(500, 'wavemaker_whifile',        wavemaker_whifile,        'none')     ! wavemaker wave height time series file`<br>K076: `sfincs_input.f90:128` `if (wavemaker_whifile(1:4) == 'none') call read_char_input(500, 'whifile',    wavemaker_whifile,        'none')`<br>K077: `sfincs_input.f90:130` `call read_char_input(500, 'wavemaker_wtifile',        wavemaker_wtifile,        'none')     ! wavemaker wave period time series file`<br>K078: `sfincs_input.f90:131` `if (wavemaker_wtifile(1:4) == 'none') call read_char_input(500, 'wtifile',    wavemaker_wtifile,        'none')`<br>K079: `sfincs_input.f90:133` `call read_char_input(500, 'wavemaker_wstfile',        wavemaker_wstfile,        'none')     ! wavemaker wave set-up time series file`<br>K080: `sfincs_input.f90:134` `if (wavemaker_wstfile(1:4) == 'none') call read_char_input(500, 'wstfile',    wavemaker_wstfile,        'none')`<br>검색: docs/*.rst·docs/*.txt에서 위 호출의 정확한 입력 이름을 검색했다.<br>확인: 해당 문서는 이 이름들을 입력 필드로 설명하지 않는다.<br>`docs/developments.rst:56` `* Renaming of wavemaker related input variables (e.g. wavemaker_wvmfile), contains legacy variables for backward compatibility.`<br>해석: 변경 기록은 이름 변경을 알리지만 이 구체적인 별칭과 읽기 우선순위는 생략했다.<br>해석: 코드에 존재하는 입력 읽기의 문서 누락이다. | C 문서 누락. 이 판은 새 wavemaker 파일명의 앞 네 글자가 none일 때 대응하는 구 키워드를 읽는다. [대조 보고서 §5 K072·K073·K074·K075·K076·K077·K078·K079·K080](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:990) |
| K081·K082·K083·K084·K085·K086·K087·K088·K089·K090·K091·K092·K093·K094·K095·K096·K097·K098·K099·K100 | wavemaker 설정 입력의 구 이름과 새 이름 | K081: `sfincs_input.f90:137` `call read_real_input(500, 'wmtfilter',                wavemaker_filter_time,    600.0)      ! time scale for wavemaker filter (in seconds)`<br>K082: `sfincs_input.f90:138` `call read_real_input(500, 'wavemaker_filter_time',    wavemaker_filter_time,    wavemaker_filter_time)`<br>K083: `sfincs_input.f90:140` `call read_real_input(500, 'wmfred',                   wavemaker_filter_fred,    0.99)       ! fred for wavemaker filter (reduces chance of jets)`<br>K084: `sfincs_input.f90:141` `call read_real_input(500, 'wavemaker_filter_fred',    wavemaker_filter_fred,    wavemaker_filter_fred)`<br>K085: `sfincs_input.f90:143` `call read_char_input(500, 'wmsignal',                 wmsigstr,                 'spectrum') ! wavemaker signal type (spectrum or monochromatic)`<br>K086: `sfincs_input.f90:144` `call read_char_input(500, 'wavemaker_signal',         wmsigstr,                 trim(wmsigstr))`<br>K087: `sfincs_input.f90:146` `call read_real_input(500, 'wmhmin',                   wavemaker_hmin,           0.1)        ! minimum water depth for wave generation (in m)`<br>K088: `sfincs_input.f90:147` `call read_real_input(500, 'wavemaker_hmin',           wavemaker_hmin,           wavemaker_hmin)`<br>K089: `sfincs_input.f90:149` `call read_int_input(500,  'nfreqsinc',                wavemaker_nfreqs_inc,     100)        ! wavemaker number of frequencies for incident wave spectrum`<br>K090: `sfincs_input.f90:150` `call read_int_input(500,  'wavemaker_nfreqs_inc',     wavemaker_nfreqs_inc,     wavemaker_nfreqs_inc)`<br>K091: `sfincs_input.f90:152` `call read_real_input(500, 'freqmininc',               wavemaker_freqmin_inc,    0.04)       ! wavemaker minimum frequency for incident wave spectrum (in Hz)`<br>K092: `sfincs_input.f90:153` `call read_real_input(500, 'wavemaker_freqmin_inc',    wavemaker_freqmin_inc,    wavemaker_freqmin_inc)`<br>K093: `sfincs_input.f90:155` `call read_real_input(500, 'freqmaxinc',               wavemaker_freqmax_inc,    1.0)        ! wavemaker maximum frequency for incident wave spectrum (in Hz)`<br>K094: `sfincs_input.f90:156` `call read_real_input(500, 'wavemaker_freqmax_inc',    wavemaker_freqmax_inc,    wavemaker_freqmax_inc)`<br>K095: `sfincs_input.f90:158` `call read_int_input(500,  'nfreqsig',                 wavemaker_nfreqs_ig,      100)        ! wavemaker number of frequencies for IG wave spectrum`<br>K096: `sfincs_input.f90:159` `call read_int_input(500,  'wavemaker_nfreqs_ig',      wavemaker_nfreqs_ig,      wavemaker_nfreqs_ig)`<br>K097: `sfincs_input.f90:161` `call read_real_input(500, 'freqminig',                wavemaker_freqmin_ig,     0.0)        ! wavemaker minimum frequency for IG wave spectrum (in Hz)`<br>K098: `sfincs_input.f90:162` `call read_real_input(500, 'wavemaker_freqmin_ig',     wavemaker_freqmin_ig,     wavemaker_freqmin_ig)`<br>K099: `sfincs_input.f90:164` `call read_real_input(500, 'freqmaxig',                wavemaker_freqmax_ig,     0.1)        ! wavemaker maximum frequency for IG wave spectrum (in Hz)`<br>K100: `sfincs_input.f90:165` `call read_real_input(500, 'wavemaker_freqmax_ig',     wavemaker_freqmax_ig,     wavemaker_freqmax_ig)`<br>검색: docs/*.rst·docs/*.txt에서 위 호출의 정확한 입력 이름을 검색했다.<br>확인: 해당 문서는 이 이름들을 입력 필드로 설명하지 않는다.<br>`docs/developments.rst:56` `* Renaming of wavemaker related input variables (e.g. wavemaker_wvmfile), contains legacy variables for backward compatibility.`<br>해석: 변경 기록은 이름 변경을 알리지만 이 구체적인 별칭과 읽기 우선순위는 생략했다.<br>해석: 코드에 존재하는 입력 읽기의 문서 누락이다. | C 문서 누락. 이 판은 새 wavemaker 설정 입력을 생략하면 구 이름으로 읽은 값을 유지한다. [대조 보고서 §5 K081·K082·K083·K084·K085·K086·K087·K088·K089·K090·K091·K092·K093·K094·K095·K096·K097·K098·K099·K100](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:991) |
| K101·K102·K103·K104·K105·K106·K107·K108 | wavemaker 파랑 성분과 계수 | K101: `sfincs_input.f90:168` `call read_real_input(500, 'wavemaker_tinc2ig',        wavemaker_tinc2ig,        -1.0)       ! wavemaker ig/inc wave period ratio (set <= 0.0 to use Herbers)`<br>K102: `sfincs_input.f90:169` `call read_real_input(500, 'wavemaker_surfslope',      wavemaker_surfslope,      -1.0)       ! wavemaker surf zone slope to compute Tp_ig with empirical run-up equation (van Ormondt et al., 2021))`<br>K103: `sfincs_input.f90:170` `call read_real_input(500, 'wavemaker_hm0_ig_factor',  wavemaker_hm0_ig_factor,  1.0)        ! wavemaker Hm0 IG wave factor`<br>K104: `sfincs_input.f90:171` `call read_real_input(500, 'wavemaker_hm0_inc_factor', wavemaker_hm0_inc_factor, 1.0)        ! wavemaker Hm0 inc wave factor`<br>K105: `sfincs_input.f90:172` `call read_real_input(500, 'wavemaker_gammax',         wavemaker_gammax,         1.0)        ! wavemaker gammax`<br>K106: `sfincs_input.f90:173` `call read_real_input(500, 'wavemaker_tpmin',          wavemaker_tpmin,          1.0)        ! wavemaker tpmin`<br>K107: `sfincs_input.f90:174` `call read_logical_input(500, 'wavemaker_hig',         wavemaker_hig,            .true.)     ! wavemaker include IG waves`<br>K108: `sfincs_input.f90:175` `call read_logical_input(500, 'wavemaker_hinc',        wavemaker_hinc,           .false.)    ! wavemaker include incident waves`<br>검색: docs/*.rst·docs/*.txt에서 위 호출의 정확한 입력 이름을 검색했다.<br>확인: 해당 문서는 이 이름들을 입력 필드로 설명하지 않는다.<br>해석: 코드에 존재하는 입력 읽기의 문서 누락이다. | C 문서 누락. 이 판은 열거한 wavemaker 주기·파고 계수와 파랑 성분 플래그를 읽는다. [대조 보고서 §5 K101·K102·K103·K104·K105·K106·K107·K108](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:992) |



#### 시계열 강제 (`wavemaker_wfpfile /= 'none'`, `:1193-1365`)

`wavemaker_timeseries=.true.` (`:1195`). IG 파만 지원(이후 `update`의 주석 `:1435` `! Only IG wave forcing supported at the moment !`).
- 강제점 좌표(`wfp`), 시각(`whi`), **IG 유의파고 `wavemaker_forcing_hm0_ig`**(`:1238-1241`), **IG 첨두주기 `wavemaker_forcing_tp_ig`**(wti, `:1249-1252`), **set-up**(wst, `:1257-1268`) 읽음.
- 시계열이 시뮬 기간 미포함 시 첫/끝 시각 조정 + 경고 (`:1271-1292`).
- 각 uv 점을 가장 가까운 두 강제점에 거리역가중 보간: `wavemaker_fac_wmfp(iwm) = dst2/(dst1+dst2)` (`:1316-1343`).

#### 주파수 성분 (`:1367-1395`)

- **IG 주파수** `wavemaker_nfreqs_ig`개, 균등 분할 `wavemaker_dfreq_ig = (freqmax_ig - freqmin_ig)/nfreqs_ig` (`:1373`), 중심주파수 (`:1375`), 위상 난수 초기화 `phi_ig = r*2π` (`:1376-1377`), 위상 표류 `dphi_ig = 1e-6*2π/freq` (`:1378`).
- **Incident 주파수** (`wavemaker_hinc`일 때만, `:1381-1395`) 동일 절차로 `wavemaker_nfreqs_inc`개.

#### 문서와 코드 차이 (외부 원문 판정)

| 보고서 행 ID | 항목 | 근거 | 결론 |
|---|---|---|---|
| <a id="cv-s-b048"></a>B048 | 북쪽에서 파를 가하는 wavemaker 버그 | Deltares/SFINCS, `v2.3.0_mt_Faber_release`, [`source/src/sfincs_wavemaker.f90`](https://raw.githubusercontent.com/Deltares/SFINCS/v2.3.0_mt_Faber_release/source/src/sfincs_wavemaker.f90), `sfincs_wavemaker.f90:304, 1007, 1029, 1096, 1118`<br>Deltares/SFINCS, `v2.4.0_Galibier_release`, [`source/src/sfincs_wavemaker.f90`](https://raw.githubusercontent.com/Deltares/SFINCS/v2.4.0_Galibier_release/source/src/sfincs_wavemaker.f90), `sfincs_wavemaker.f90:307, 1032, 1056, 1129, 1153`<br>[Deltares/SFINCS 커밋 `dce1e52`](https://github.com/Deltares/SFINCS/commit/dce1e52) 및 [Deltares/SFINCS 커밋 `1f1d828`](https://github.com/Deltares/SFINCS/commit/1f1d828)<br>`docs/developments.rst:64`의 수정 이력을 이전·이후 태그의 각도 계수와 대조했다. 로컬 위치는 `sfincs_wavemaker.f90:1032, 1056, 1129, 1153`이다.<br>문서의 `waves forced from the north`와 커밋의 `south-facing wavemakers`를 같은 사건으로 직접 연결하는 문구는 확인하지 못했다. | A 판 차이. v2.4.0은 wavemaker 아래쪽 면의 각도 계수 `angfac`를 `max(sin(pi - phi), 0)`에서 `max(-sin(phi), 0)`로 바꾸었다. 이 변경은 phi가 π~2π인 wavemaker 면의 각도 계수가 항상 0이 되던 문제를 수정했다. 현재 로컬 코드는 이 수정판이다. [대조 보고서 §5 B048](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1026) [10-12 외부 원문 판정] [10-12 결론 검증 보완] |

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

## 문서 참고 링크 오류

v2.0.2 릴리스 링크의 정정은 [변경 이력 노트의 정본](../manual-notes/sfincs-v2.4.0-galibier-changelog-known-issues.md#문서-참고-링크-오류)을 따른다. [10-12 결론 검증 보완]
