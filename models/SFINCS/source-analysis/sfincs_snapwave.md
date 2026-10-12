---
title: "SFINCS SnapWave 연안 파솔버 — 정상상태 wave/action 전파 + IG·wind·radiation stress 결합"
model: SFINCS
component: snapwave (coastal phase-averaged wave solver, coupled)
canonical_source: self
citation_status: verified
verification_method: "직접 Read — sfincs_snapwave.f90 (전 739줄), snapwave/snapwave_solver.f90 (2005줄), snapwave_domain.f90 (2097줄), snapwave_boundaries.f90 (972줄), snapwave_infragravity.f90 (699줄), snapwave_windsource.f90 (232줄), snapwave_RFtable.f90 (3990줄). 인용 라인 모두 직접 확인."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "[[sfincs-architecture-source-map]]"
last_source_check: 2026-10-12 (recovery 차이 결론 반영)
---

# SFINCS SnapWave 연안 파솔버

SnapWave는 Deltares가 SFINCS와 한 바이너리로 통합한 **정상상태(stationary) 방향분해(directional) 파에너지 평형** 솔버다. 비정상 분광모델(SWAN 등)과 달리 시간미분을 가성(pseudo) under-relaxation 으로만 쓰고 sweep 반복으로 정상해를 찾는 reduced-complexity 모델이다. 입사파(incident)와 인프라그래비티(IG) 파를 동시에 풀고, 파 라디에이션 응력으로 SFINCS 흐름에 setup/wave force 를 되돌려준다. 결합·매핑은 `sfincs_snapwave.f90`, 물리 솔버는 `snapwave/` 서브모듈 군.

본체 시간루프와의 위치는 [[sfincs-architecture-source-map]] §3 (파/처오름 행) 참조.

## 1. 자료구조 & 결합 진입점 (`sfincs_snapwave.f90`)

모듈은 SnapWave 격자(`snapwave_no_nodes` 노드)와 SFINCS 격자(`np` 점) 사이 양방향 인덱스를 들고, 노드별 파라미터 배열을 보유한다 (`sfincs_snapwave.f90:8-40`). 대표 배열: `snapwave_H`(입사 Hrms), `snapwave_H_ig`(IG), `snapwave_Tp`/`snapwave_Tp_ig`, `snapwave_Fx`/`snapwave_Fy`(파 force), `snapwave_Dw`/`snapwave_Df`(breaking/friction 소산), `snapwave_srcig`/`snapwave_alphaig`/`snapwave_beta`(IG source 진단).

### 결합 초기화 `couple_snapwave` (`:44`)
순서: `read_snapwave_input`(inp 읽기) → `initialize_snapwave_domain`(메쉬·upwind) → `read_boundary_data` → 배열 할당 → `find_matching_cells`. spherical/cartesian 은 SFINCS `crsgeo` 로 `sferic` 결정 (`:97-101`).

### 격자 매핑 `find_matching_cells` (`:173`)
`find_matching_cells`는 대응 셀이 없고 `snapwave_use_nearest`가 참이면 좌표 차이의 최소 거리를 찾는다. `sfincs_snapwave.f90:220` `if (snapwave_use_nearest) then`; `sfincs_snapwave.f90:225` `dstmin = 1.0e6`; `sfincs_snapwave.f90:233` `dst = sqrt((z_xz(ip) - xsw)**2 + (z_yz(ip) - ysw)**2)`; `sfincs_snapwave.f90:244` `if (min_distance < dstmin) then`
거리 상한은 `dstmin=1.0e6`이다. `sfincs_snapwave.f90:220` `if (snapwave_use_nearest) then`; `sfincs_snapwave.f90:225` `dstmin = 1.0e6`; `sfincs_snapwave.f90:233` `dst = sqrt((z_xz(ip) - xsw)**2 + (z_yz(ip) - ysw)**2)`; `sfincs_snapwave.f90:244` `if (min_distance < dstmin) then`
이 비교는 좌표 차이를 미터로 바꾸지 않는다. `sfincs_snapwave.f90:220` `if (snapwave_use_nearest) then`; `sfincs_snapwave.f90:225` `dstmin = 1.0e6`; `sfincs_snapwave.f90:233` `dst = sqrt((z_xz(ip) - xsw)**2 + (z_yz(ip) - ysw)**2)`; `sfincs_snapwave.f90:244` `if (min_distance < dstmin) then`

### `update_wave_field(t, tloop)`

`update_wave_field`는 SnapWave 갱신 시각에 도달한 시간 단계에서만 실행한다. `sfincs_lib.f90:552` `if (snapwave .and. update_waves) then`; `sfincs_lib.f90:509` `if (t >= twaveupd) then`; `sfincs_input.f90:68` `call read_real_input(500,'dtwave',dtwave,3600.0)`
`dtwave`의 기본값은 3600초다. `sfincs_lib.f90:552` `if (snapwave .and. update_waves) then`; `sfincs_lib.f90:509` `if (t >= twaveupd) then`; `sfincs_input.f90:68` `call read_real_input(500,'dtwave',dtwave,3600.0)`
1. SnapWave 수심을 SFINCS 수위에서 산정: `snapwave_depth = max(zs(ip) - snapwave_z, 1e-5)` (wavemaker 면 `zsm`) (`:354-368`).

   SnapWave는 현재 단계의 연속식보다 먼저 내부 수위를 읽는다. `sfincs_lib.f90:546` `call update_boundaries(t, dt, tloopbnd)`; `sfincs_lib.f90:556` `call update_wave_field(t, tloopsnapwave)`; `sfincs_lib.f90:618` `call compute_water_levels(t, dt, tloopcont)`; `sfincs_snapwave.f90:356` `snapwave_depth(nm) = max(zsm(ip) - snapwave_z(nm), 0.00001)`; `sfincs_snapwave.f90:360` `snapwave_depth(nm) = max(zs(ip) - snapwave_z(nm), 0.00001)`
   SFINCS 대응 셀이 있는 `if (ip > 0) then` 안에서 `if (wavemaker) then`은 `sfincs_snapwave.f90:356` `snapwave_depth(nm) = max(zsm(ip) - snapwave_z(nm), 0.00001)`으로 필터 수위 `zsm`을 읽는다(`sfincs_snapwave.f90:349` `if (ip > 0) then`; `sfincs_snapwave.f90:354` `if (wavemaker) then`). [10-12 전수 검증 보완]
   대응 셀이 있고 `wavemaker`가 거짓이면 `sfincs_snapwave.f90:360` `snapwave_depth(nm) = max(zs(ip) - snapwave_z(nm), 0.00001)`으로 `zs`를 읽는다. [10-12 전수 검증 정정] 대응 셀이 없는 ELSE는 `sfincs_snapwave.f90:368` `snapwave_depth(nm) = max(0.0 - snapwave_z(nm), 0.00001)`으로 수위 0.0을 사용한다. [10-12 전수 검증 보완]
   경계 갱신은 이 읽기보다 먼저 실행한다. `sfincs_lib.f90:546` `call update_boundaries(t, dt, tloopbnd)`; `sfincs_lib.f90:556` `call update_wave_field(t, tloopsnapwave)`; `sfincs_lib.f90:618` `call compute_water_levels(t, dt, tloopcont)`; `sfincs_snapwave.f90:356` `snapwave_depth(nm) = max(zsm(ip) - snapwave_z(nm), 0.00001)`; `sfincs_snapwave.f90:360` `snapwave_depth(nm) = max(zs(ip) - snapwave_z(nm), 0.00001)`

2. `update_wave_field`는 `windu/windv`로 풍속 크기를 계산한다. `sfincs_snapwave.f90:390` `u10 = sqrt(windu(ip)**2 + windv(ip)**2)`; `sfincs_snapwave.f90:392` `u10dir = atan2(windv(ip), windu(ip))*180/pi`; `sfincs_snapwave.f90:398` `snapwave_u10dir(nm) = u10dir / 180.0 * pi ! from nautical coming from in degrees to cartesian going to in radians` 이 변환은 `if (wind) then`, `if (snapwavewind) then`, `if (ip>0) then` 안에서 수행한다(`sfincs_snapwave.f90:376` `if (wind) then ! =We have wind inputs given to SFINCS`; `sfincs_snapwave.f90:378` `if (snapwavewind) then ! =We have windgrowth in SnapWave turned on`; `sfincs_snapwave.f90:384` `if (ip>0) then`). [10-12 전수 검증 보완]
   이 루틴은 `atan2(windv,windu)`의 방향을 도 단위로 만든다. `sfincs_snapwave.f90:390` `u10 = sqrt(windu(ip)**2 + windv(ip)**2)`; `sfincs_snapwave.f90:392` `u10dir = atan2(windv(ip), windu(ip))*180/pi`; `sfincs_snapwave.f90:398` `snapwave_u10dir(nm) = u10dir / 180.0 * pi ! from nautical coming from in degrees to cartesian going to in radians` 저장 전에 `sfincs_snapwave.f90:394` `if (u10dir<0.0) u10dir = u10dir + 360.0`와 `sfincs_snapwave.f90:395` `if (u10dir>360.0) u10dir = u10dir - 360.0`로 음수·360도 초과를 처리한다. [10-12 전수 검증 보완]
   이 루틴은 그 방향을 라디안으로 저장한다. `sfincs_snapwave.f90:390` `u10 = sqrt(windu(ip)**2 + windv(ip)**2)`; `sfincs_snapwave.f90:392` `u10dir = atan2(windv(ip), windu(ip))*180/pi`; `sfincs_snapwave.f90:398` `snapwave_u10dir(nm) = u10dir / 180.0 * pi ! from nautical coming from in degrees to cartesian going to in radians`
3. `compute_snapwave(t)` 호출 (실제 솔버).
4. 결과를 SFINCS 배열로 역매핑 (`:417-485`): `hm0`, `hm0_ig`, `sw_tp`, force 등.
5. **Hrms→Hm0 변환**: `hm0 = hm0 * sqrt(2.0)` (`:487-488`).
<a id="cv-s-wave-force"></a>6. 파 force 를 UV 점으로 보간·회전, `rhow`로 나눠 단위폭 유량 변화율 항(m²/s²)으로 전달: U점 `fwuv = waveforces_ratio*(... cosrot*fwx + sinrot*fwy ...)/rhow` (`:502`), V점은 회전 부호 반전 (`:508`). `waveforces_ratio` 기본 1.0, wavemaker_hinc 시 incident setup 이중계산 방지용 0 설정 가능 (`:503` 주석). 근거: `docs/developments.rst:32` `Official open source version 2026.01: v2.4.0 Galibier release release`<br>`docs/developments.rst:54` `* Added input variable 'snapwave_waveforces_factor' which you can set to 0 to turn off wave forces and thus incident wave setup.`<br>`sfincs_lib.f90:97` `build_revision = "$Rev: v2.4.0 Galibier Release"`<br>`sfincs_input.f90:308` `call read_real_input(500,'snapwave_waveforces_ratio',waveforces_ratio,1.0)`<br>`sfincs_snapwave.f90:502` `fwuv(ip) = waveforces_ratio * (0.5 * (cosrot * fwx0(nm) + sinrot * fwy0(nm)) + 0.5 * ( cosrot * fwx0(nmu) + sinrot * fwy0(nmu))) / rhow` [대조 보고서 §5 E014·B044·K140·C018](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:965) 결론: 문서 오기. 이 판은 snapwave_waveforces_ratio를 0으로 설정하면 SnapWave의 직접 파력 전달을 끈다. `sfincs_snapwave.f90:563–564`는 solver 가속도에 rho와 depth를 곱한다. `sfincs_momentum.f90:606,677`은 rhow로 나눈 fwuv를 frc에 더한 뒤 dt를 곱하여 단위폭 유량 q를 갱신한다. 따라서 fwuv 자체를 가속도(m/s²)라고 부르면 수심 인자가 빠진다. [10-12 결론 검증 정정]

<a id="cv-s-sf-01"></a>**CV-S-SF-01 — E 코드 결함 후보.** SnapWave 파력 출력 fwx·fwy의 NetCDF 단위 속성이 계산값과 다르다. 쇄파 소산 경로의 `snapwave/snapwave_solver.f90:1092`는 `F(k) = Dw(k) * kwav(k) / sig(k) / rho / depth(k)`이다. `sfincs_snapwave.f90:563–564`는 Fx·Fy에 rho와 depth를 곱한다. 해석: 이 출력 파력의 차원은 N/m²이다. `:427–428,471–472`는 이 값을 fwx·fwy에 전달한다. `sfincs_ncoutput.F90:2638,2651,3007–3008`은 단위 변환 없이 출력 배열에 복사한다. 그러나 정규격자의 `:600,608`과 quadtree의 `:1404,1411`은 단위를 모두 m으로 기록한다. 계산·전달식과 출력 속성의 차원이 서로 모순된다. 반대 경로를 검색했지만 출력 전에 길이로 바꾸는 변환은 찾지 못했다. `sfincs_snapwave.f90:502,508`의 rhow 나눗셈은 운동량용 fwuv에 적용된다. fwx·fwy 출력에는 적용되지 않는다. 후보는 SnapWave와 store_wave_forces가 활성인 출력에 한정한다. 모델 계산값의 오류까지 뜻하지 않는다. [대조 보고서 §5 CV-S-SF-01](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md#cv-s-sf-01) [10-12 결론 검증 정정]

### `compute_snapwave(t)` (`:525`)
SnapWave 작업배열에 depth/zb/u10 복사 → `update_boundary_conditions(t)` → `compute_wave_field()` → 결과를 모듈 배열로 복사. 핵심 단위변환:
- 평균방향: `snapwave_mean_direction = modulo(270 - thetam*180/pi + 360, 360)` (cartesian rad → nautical deg) (`:551`).
- **파 force 단위변환**: `snapwave_Fx = Fx * rho * depth` (솔버 `F`=Dw·k/σ/ρ/h 를 SFINCS 기대 단위로 환산) (`:563-564`).
- force limiter: `snapwave_fwmaxfac = 0.25*sqrt(g)*rho*gammax**2/tpmean_bwv` (`:567`).
- H≤0 셀은 Tp·방향·cg 를 0 으로 청소(초기 Tpini 잔존 방지) (`:573-584`).

waves.rst의 WIP 상태: 근거: `docs/waves.rst:7` `The input of waves as boundary conditions is still work in progress. Right now the following files should not be used:`<br>`sfincs_snapwave.f90:543` `call update_boundary_conditions(t) ! SnapWave boundary conditions`<br>`sfincs_snapwave.f90:545` `call compute_wave_field()`<br>`sfincs_snapwave.f90:671` `call read_char_input(500, 'snapwave_jonswapfile', snapwave_jonswapfile, 'none')`<br>`sfincs_snapwave.f90:672` `call read_char_input(500, 'snapwave_bndfile', snapwave_bndfile, 'none')`<br>`sfincs_snapwave.f90:674` `call read_char_input(500, 'snapwave_bhsfile', snapwave_bhsfile, 'none')`<br>`sfincs_snapwave.f90:675` `call read_char_input(500, 'snapwave_btpfile', snapwave_btpfile, 'none')`<br>`sfincs_snapwave.f90:682` `call read_char_input(500, 'netsnapwavefile', netsnapwavefile, 'none')` [대조 보고서 §5 B136](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1055) 결론: 문서 누락. 이 판은 미완성 waves.rst의 안내와 별개로 통합 SnapWave를 실행하는 호출 경로를 제공한다.


### 입력 파라미터 `read_snapwave_input` (`:602`)
`sfincs.inp` 에서 `snapwave_*` 키를 읽는다. 주요 기본값 (모두 `read_*_input` 호출 라인):
`snapwave_gamma`=0.7, `snapwave_gammax`=999, `snapwave_alpha`=1.0, `snapwave_fw`=0.01, `snapwave_fwig`=0.015, `snapwave_niter`=10, `snapwave_dtheta`=10°, `snapwave_sector`=180°, `snapwave_baldock_ratio`=0.2, `snapwave_baldock_exponent`=2, `relax_factor_DoverA/DoverE`=0.25 (`:615-641`). IG: `snapwave_igwaves`=1, `snapwave_gammaig`=0.7, `snapwave_gamma_fac_br`=0.45, `snapwave_shinc2ig`=1.0, `snapwave_ig_opt`=1, `snapwave_iterative_srcig`=0 (`:644-652`). IG bc: `snapwave_use_herbers`=1, `snapwave_tpig_opt`=1(Tm01), `snapwave_jonswapgamma`=3.3 (`:655-657`). 플래그 후처리: `igwaves`/`igherbers`/`iterative_srcig`/`wind`/`vegetation` 설정 (`:688-724`), `nr_sweeps` 는 1 또는 4 만 허용(아니면 4) (`:726-731`), `coupled_to_sfincs=.true.` (`:734`).

#### 문서에 빠진 통합 SnapWave 입력

| 보고서 행 ID | 항목 | 근거 | 결론 |
|---|---|---|---|
| K001·K002·K003·K004·K005·K006·K007·K008·K009·K010·K011·K012 | 통합 SnapWave 수치 입력 | K001: `sfincs_snapwave.f90:615` `call read_real_input(500,'snapwave_gamma',gamma,0.7)`<br>K002: `sfincs_snapwave.f90:616` `call read_real_input(500,'snapwave_gammax',gammax,999.0)`<br>K003: `sfincs_snapwave.f90:617` `call read_real_input(500,'snapwave_alpha',alpha,1.0)`<br>K004: `sfincs_snapwave.f90:618` `call read_real_input(500,'snapwave_hmin',hmin,0.1)`<br>K005: `sfincs_snapwave.f90:619` `call read_real_input(500,'snapwave_fw',fw0,0.01)`<br>K006: `sfincs_snapwave.f90:620` `call read_real_input(500,'snapwave_fwig',fw0_ig,0.015)`<br>K007: `sfincs_snapwave.f90:621` `call read_real_input(500,'snapwave_dt',dt,36000.0)`<br>K008: `sfincs_snapwave.f90:622` `call read_real_input(500,'snapwave_tol',tol,1000.0)`<br>K009: `sfincs_snapwave.f90:623` `call read_real_input(500,'snapwave_dtheta',dtheta,10.0)`<br>K010: `sfincs_snapwave.f90:624` `call read_real_input(500,'snapwave_crit',crit,0.001)`<br>K011: `sfincs_snapwave.f90:625` `call read_int_input(500,'snapwave_nrsweeps',nr_sweeps,4)`<br>K012: `sfincs_snapwave.f90:626` `call read_int_input(500,'snapwave_niter',niter, 10) !TL: Old default was 40`<br>검색: docs/*.rst·docs/*.txt에서 위 호출의 정확한 입력 이름을 검색했다.<br>확인: 해당 문서는 이 이름들을 입력 필드로 설명하지 않는다.<br>해석: 코드에 존재하는 입력 읽기의 문서 누락이다. | C 문서 누락. 이 판의 통합 SnapWave는 열거한 수치 입력을 생략하면 각 리더에 적힌 기본값을 사용한다. [대조 보고서 §5 K001·K002·K003·K004·K005·K006·K007·K008·K009·K010·K011·K012](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:981) |
| K013·K014·K015·K016·K017·K018·K019·K020·K021·K022·K023·K024·K025 | 통합 SnapWave 쇄파·마찰·바람·분산 계수 | K013: `sfincs_snapwave.f90:628` `call read_real_input(500,'snapwave_baldock_ratio',baldock_ratio,0.2)`<br>K014: `sfincs_snapwave.f90:629` `call read_int_input(500,'snapwave_baldock_exponent',baldock_exponent,2)   ! Exponent for multiplying the Baldock dissipation with a factor 'f = (Hloc / Hmax)**iexp' to enhance breaking when H > Hmax, with iexp = 0 (means unused), 1 or 2 (default). Generally, only active for steep coastlines, where Baldock dissipation can be too low in the surf zone.`<br>K015: `sfincs_snapwave.f90:631` `call read_real_input(500,'snapwave_fw_ratio',fwratio,1.0)`<br>K016: `sfincs_snapwave.f90:632` `call read_real_input(500,'snapwave_fwig_ratio',fwigratio,1.0)`<br>K017: `sfincs_snapwave.f90:633` `call read_real_input(500,'snapwave_Tpini',Tpini,1.0)`<br>K018: `sfincs_snapwave.f90:634` `call read_int_input (500,'snapwave_mwind',mwind,2)`<br>K019: `sfincs_snapwave.f90:635` `call read_real_input(500,'snapwave_sigmin',sigmin,8.0 * atan(1.0) / 25.0)`<br>K020: `sfincs_snapwave.f90:636` `call read_real_input(500,'snapwave_sigmax',sigmax,8.0 * atan(1.0) / 1.0)`<br>K021: `sfincs_snapwave.f90:637` `call read_int_input (500,'snapwave_jadcgdx',jadcgdx,1)`<br>K022: `sfincs_snapwave.f90:638` `call read_real_input(500,'snapwave_c_dispT',c_dispT,1.0)`<br>K023: `sfincs_snapwave.f90:639` `call read_real_input(500,'snapwave_sector',sector,180.0)`<br>K024: `sfincs_snapwave.f90:640` `call read_real_input(500,'snapwave_relax_factor_DoverA',relax_factor_DoverA,0.25) ! underrelaxation factor for DoverA (set to 1.0 to disable)`<br>K025: `sfincs_snapwave.f90:641` `call read_real_input(500,'snapwave_relax_factor_DoverE',relax_factor_DoverE,0.25) ! underrelaxation factor for DoverE (set to 1.0 to disable)`<br>검색: docs/*.rst·docs/*.txt에서 위 호출의 정확한 입력 이름을 검색했다.<br>확인: 해당 문서는 이 이름들을 입력 필드로 설명하지 않는다.<br>해석: 코드에 존재하는 입력 읽기의 문서 누락이다. | C 문서 누락. 이 판의 통합 SnapWave 리더는 열거한 쇄파·마찰·바람·분산 계수 입력을 받는다. [대조 보고서 §5 K013·K014·K015·K016·K017·K018·K019·K020·K021·K022·K023·K024·K025](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:982) |
| K026·K027·K028·K029·K030·K031·K032·K033·K034·K035·K036·K037·K038·K039 | 통합 SnapWave IG·스펙트럼 입력 | K026: `sfincs_snapwave.f90:644` `call read_int_input(500,'snapwave_igwaves',igwaves_opt,1)`<br>K027: `sfincs_snapwave.f90:645` `call read_real_input(500,'snapwave_alpha_ig',alpha_ig,1.0) !TODO choose whether snapwave_alphaig or snapwave_gamma_ig`<br>K028: `sfincs_snapwave.f90:646` `call read_real_input(500,'snapwave_gammaig', gamma_ig, 0.7)                  ! Wave breaking parameter for IG waves, default=0.7`<br>K029: `sfincs_snapwave.f90:647` `call read_real_input(500,'snapwave_gamma_fac_br',gamma_fac_br,0.45) ! factor times gamma that is used to determine the maximum incident wave breaking point in the surf zone using local incident wave height over water depth ratio, among others used to set the IG source term to 0 shallower than this point`<br>K030: `sfincs_snapwave.f90:648` `call read_real_input(500,'snapwave_shinc2ig',shinc2ig,1.0)                   ! Ratio of how much of the calculated IG wave source term, is subtracted from the incident wave energy (0-1, 1=default=all energy as sink)`<br>K031: `sfincs_snapwave.f90:649` `call read_real_input(500,'snapwave_alphaigfac',alphaigfac,1.0)               ! Multiplication factor for IG shoaling source/sink term`<br>K032: `sfincs_snapwave.f90:650` `call read_real_input(500,'snapwave_baldock_ratio_ig',baldock_ratio_ig,0.2)`<br>K033: `sfincs_snapwave.f90:651` `call read_int_input(500,'snapwave_ig_opt',ig_opt,1)`<br>K034: `sfincs_snapwave.f90:652` `call read_int_input(500,'snapwave_iterative_srcig',iterative_srcig_opt,0)        ! Option whether to calculate IG source/sink term in iterative lower (better, but potentially slower, 1=default), or effectively based on previous timestep (faster, potential mismatch, =0)`<br>K035: `sfincs_snapwave.f90:655` `call read_int_input(500,'snapwave_use_herbers',herbers_opt,1)    ! Choice whether you want IG Hm0&Tp be calculated by herbers (=1, default), or want to specify user defined values (0> then snapwave_eeinc2ig & snapwave_Tinc2ig are used)`<br>K036: `sfincs_snapwave.f90:656` `call read_int_input(500,'snapwave_tpig_opt',tpig_opt,1) ! IG wave period option based on Herbers calculated spectrum, only used if snapwave_use_herbers = 1. Options are: 1=Tm01 (default), 2=Tpsmooth, 3=Tp, 4=Tm-1,0`<br>K037: `sfincs_snapwave.f90:657` `call read_real_input(500,'snapwave_jonswapgamma',jonswapgam,3.3)  ! JONSWAP gamma value for determination offshore spectrum and IG wave conditions using Herbers, default=3.3, only used if snapwave_use_herbers = 1`<br>K038: `sfincs_snapwave.f90:658` `call read_real_input(500,'snapwave_eeinc2ig',eeinc2ig,0.01)  ! Only used if snapwave_use_herbers = 0`<br>K039: `sfincs_snapwave.f90:659` `call read_real_input(500,'snapwave_Tinc2ig',Tinc2ig,7.0)  ! Only used if snapwave_use_herbers = 0`<br>검색: docs/*.rst·docs/*.txt에서 위 호출의 정확한 입력 이름을 검색했다.<br>확인: 해당 문서는 이 이름들을 입력 필드로 설명하지 않는다.<br>해석: 코드에 존재하는 입력 읽기의 문서 누락이다. | C 문서 누락. 이 판의 통합 SnapWave 리더는 열거한 IG 및 스펙트럼 입력을 받는다. [대조 보고서 §5 K026·K027·K028·K029·K030·K031·K032·K033·K034·K035·K036·K037·K038·K039](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:983) |
| K040·K041 | 통합 SnapWave 바람·식생 플래그 | K040: `sfincs_snapwave.f90:663` `call read_int_input(500,'snapwave_wind',wind_opt,0)   ! Flag whether to include windgrowth in SnapWave (1) or not (0, default)`<br>`sfincs_input.f90:306` `call read_int_input(500,'snapwave_wind',iwind,0)`<br>K041: `sfincs_snapwave.f90:667` `call read_int_input(500, 'snapwave_vegetation', vegetation_opt, 0)`<br>`sfincs_input.f90:307` `call read_logical_input(500,'snapwave_vegetation',snapwave_vegetation,.false.)`<br>검색: docs/*.rst·docs/*.txt에서 위 호출의 정확한 입력 이름을 검색했다.<br>확인: 해당 문서는 이 이름들을 입력 필드로 설명하지 않는다.<br>해석: 코드에 존재하는 입력 읽기의 문서 누락이다. | C 문서 누락. 이 판은 snapwave_wind와 snapwave_vegetation을 통합 리더와 주 입력 리더에서 각각 읽는다. [대조 보고서 §5 K040·K041](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:984) |
| K042·K043·K044·K045·K046·K047·K048·K049·K050·K051·K052·K053·K054 | 통합 SnapWave 파일·격자 출력 입력 | K042: `sfincs_snapwave.f90:671` `call read_char_input(500, 'snapwave_jonswapfile', snapwave_jonswapfile, 'none')`<br>K043: `sfincs_snapwave.f90:672` `call read_char_input(500, 'snapwave_bndfile', snapwave_bndfile, 'none')`<br>K044: `sfincs_snapwave.f90:673` `call read_char_input(500, 'snapwave_encfile', snapwave_encfile, 'none')`<br>K045: `sfincs_snapwave.f90:674` `call read_char_input(500, 'snapwave_bhsfile', snapwave_bhsfile, 'none')`<br>K046: `sfincs_snapwave.f90:675` `call read_char_input(500, 'snapwave_btpfile', snapwave_btpfile, 'none')`<br>K047: `sfincs_snapwave.f90:676` `call read_char_input(500, 'snapwave_bwdfile', snapwave_bwdfile, 'none')`<br>K048: `sfincs_snapwave.f90:677` `call read_char_input(500, 'snapwave_bdsfile', snapwave_bdsfile,'none')`<br>K049: `sfincs_snapwave.f90:678` `call read_char_input(500, 'snapwave_upwfile', upwfile, 'snapwave.upw')`<br>K050: `sfincs_snapwave.f90:679` `call read_char_input(500, 'snapwave_mskfile', mskfile, 'none')`<br>K051: `sfincs_snapwave.f90:680` `call read_char_input(500, 'snapwave_depfile', depfile, 'none')`<br>K052: `sfincs_snapwave.f90:681` `call read_char_input(500, 'snapwave_ncfile',  gridfile, 'snapwave_net.nc')`<br>K053: `sfincs_snapwave.f90:682` `call read_char_input(500, 'netsnapwavefile', netsnapwavefile, 'none')`<br>K054: `sfincs_snapwave.f90:683` `call read_logical_input(500,'storesnapwavegrid',storesnapwavegrid,.false.)`<br>검색: docs/*.rst·docs/*.txt에서 위 호출의 정확한 입력 이름을 검색했다.<br>확인: 해당 문서는 이 이름들을 입력 필드로 설명하지 않는다.<br>해석: 코드에 존재하는 입력 읽기의 문서 누락이다. | C 문서 누락. 이 판은 통합 SnapWave의 파일명과 격자 저장 여부를 열거한 입력으로 읽는다. [대조 보고서 §5 K042·K043·K044·K045·K046·K047·K048·K049·K050·K051·K052·K053·K054](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:985) |

#### 문서에 빠진 독립 snapwave.inp 입력

| 보고서 행 ID | 항목 | 근거 | 결론 |
|---|---|---|---|
| K142·K143·K144·K145·K146·K147·K148·K149·K150·K151·K152·K153·K154·K155·K156·K157·K158·K159·K160 | 독립 SnapWave 전용 이름 | K142: `snapwave/snapwave_input.f90:33` `call read_real_input(500,'timestep',timestep,3600.0)`<br>K143: `snapwave/snapwave_input.f90:34` `call read_real_input(500,'gamma',gamma,0.7)`<br>K144: `snapwave/snapwave_input.f90:36` `call read_real_input(500,'hmin',hmin,0.1)`<br>K145: `snapwave/snapwave_input.f90:37` `call read_char_input(500,'gridfile',gridfile,'.txt')`<br>K146: `snapwave/snapwave_input.f90:38` `call read_int_input(500,'sferic',sferic,0)`<br>K147: `snapwave/snapwave_input.f90:39` `call read_real_input(500,'fw',fw0,0.01)`<br>K148: `snapwave/snapwave_input.f90:40` `call read_real_input(500,'fwig',fw0_ig,0.015)`<br>K149: `snapwave/snapwave_input.f90:41` `call read_real_input(500,'dt',dt,36000.0)`<br>K150: `snapwave/snapwave_input.f90:42` `call read_real_input(500,'tol',tol,10.0)`<br>K151: `snapwave/snapwave_input.f90:43` `call read_real_input(500,'dtheta',dtheta,10.0)`<br>K152: `snapwave/snapwave_input.f90:53` `call read_char_input(500,'jonswapfile',jonswapfile,'')`<br>K153: `snapwave/snapwave_input.f90:55` `call read_char_input(500,'encfile',encfile,'')`<br>K154: `snapwave/snapwave_input.f90:58` `call read_char_input(500,'bwdfile',bwdfile,'')`<br>K155: `snapwave/snapwave_input.f90:59` `call read_char_input(500,'bdsfile',bdsfile,'')`<br>K156: `snapwave/snapwave_input.f90:61` `call read_char_input(500,'upwfile',upwfile,'')`<br>K157: `snapwave/snapwave_input.f90:63` `call read_char_input(500,'indfile',indfile,'')`<br>K158: `snapwave/snapwave_input.f90:67` `call read_char_input(500,'map_file',map_filename,'')`<br>K159: `snapwave/snapwave_input.f90:68` `call read_char_input(500,'his_file',his_filename,'')`<br>K160: `snapwave/snapwave_input.f90:69` `call read_int_input(500,'restart',irestart,1)`<br>검색: docs/*.rst·docs/*.txt에서 위 호출의 정확한 입력 이름을 검색했다.<br>확인: 해당 문서는 이 이름들을 입력 필드로 설명하지 않는다.<br>확인: global·vegetation·timestep·restart의 일반 명사 용례는 동명 입력 필드의 설명이 아니다.<br>해석: 코드에 존재하는 입력 읽기의 문서 누락이다. | C 문서 누락. 이 판의 독립 snapwave.inp 리더는 열거한 수치·파일·재시작 입력을 받는다. [대조 보고서 §5 K142·K143·K144·K145·K146·K147·K148·K149·K150·K151·K152·K153·K154·K155·K156·K157·K158·K159·K160](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:997) |
| 보고서 606행·보고서 607행·보고서 608행·보고서 609행·보고서 610행·보고서 611행·보고서 612행·보고서 613행·보고서 614행·보고서 615행·보고서 616행·보고서 617행·보고서 618행·보고서 619행·보고서 620행·보고서 621행·보고서 622행·보고서 623행·보고서 624행 | 독립 snapwave.inp의 동명 입력 19개 | 보고서 606행 nmax: `snapwave/snapwave_input.f90:23` `call read_int_input(500,'nmax',nmax,0)`<br>보고서 607행 mmax: `snapwave/snapwave_input.f90:24` `call read_int_input(500,'mmax',mmax,0)`<br>보고서 608행 dx: `snapwave/snapwave_input.f90:25` `call read_real_input(500,'dx',dx,0.0)`<br>보고서 609행 dy: `snapwave/snapwave_input.f90:26` `call read_real_input(500,'dy',dy,0.0)`<br>보고서 610행 x0: `snapwave/snapwave_input.f90:27` `call read_real_input(500,'x0',x0,0.0)`<br>보고서 611행 y0: `snapwave/snapwave_input.f90:28` `call read_real_input(500,'y0',y0,0.0)`<br>보고서 612행 rotation: `snapwave/snapwave_input.f90:29` `call read_real_input(500,'rotation',rotation,0.0)`<br>보고서 613행 tref: `snapwave/snapwave_input.f90:30` `call read_char_input(500,'tref',trefstr,'20000101 000000')`<br>보고서 614행 tstart: `snapwave/snapwave_input.f90:31` `call read_char_input(500,'tstart',tstartstr,'20000101 000000')`<br>보고서 615행 tstop: `snapwave/snapwave_input.f90:32` `call read_char_input(500,'tstop',tstopstr,'20000101 000000')`<br>보고서 616행 alpha: `snapwave/snapwave_input.f90:35` `call read_real_input(500,'alpha',snapwave_alpha,1.0)`<br>보고서 617행 bndfile: `snapwave/snapwave_input.f90:54` `call read_char_input(500,'bndfile',bndfile,'')`<br>보고서 618행 bhsfile: `snapwave/snapwave_input.f90:56` `call read_char_input(500,'bhsfile',bhsfile,'')`<br>보고서 619행 btpfile: `snapwave/snapwave_input.f90:57` `call read_char_input(500,'btpfile',btpfile,'')`<br>보고서 620행 bzsfile: `snapwave/snapwave_input.f90:60` `call read_char_input(500,'bzsfile',bzsfile,'')`<br>보고서 621행 mskfile: `snapwave/snapwave_input.f90:62` `call read_char_input(500,'mskfile',mskfile,'')`<br>보고서 622행 depfile: `snapwave/snapwave_input.f90:64` `call read_char_input(500,'depfile',depfile,'')`<br>보고서 623행 obsfile: `snapwave/snapwave_input.f90:65` `call read_char_input(500,'obsfile',obsfile,'')`<br>보고서 624행 outputformat: `snapwave/snapwave_input.f90:66` `call read_char_input(500,'outputformat',outputformat,'bin')`<br>`docs/waves.rst:7` `The input of waves as boundary conditions is still work in progress. Right now the following files should not be used:`<br>검색: docs/*.rst·docs/*.txt에서 snapwave.inp와 위 입력명의 독립판 기본값 설명을 검색했다.<br>확인: 대상 문서는 SFINCS 주 입력 설명을 제공하지만 이 독립 리더의 전체 기본값은 설명하지 않는다.<br>확인: 독립 리더의 alpha 기본값은 1.0이다.<br>확인: 독립 리더의 outputformat 기본값은 bin이다.<br>해석: 동일 철자의 SFINCS 입력 기본값을 독립 SnapWave에 옮길 수 없다. | C 문서 누락. 이 판의 독립 SnapWave는 동명 입력에도 snapwave.inp 리더에 적힌 별도 기본값을 적용한다. [대조 보고서 §5 보고서 606행·보고서 607행·보고서 608행·보고서 609행·보고서 610행·보고서 611행·보고서 612행·보고서 613행·보고서 614행·보고서 615행·보고서 616행·보고서 617행·보고서 618행·보고서 619행·보고서 620행·보고서 621행·보고서 622행·보고서 623행·보고서 624행](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:998) |



## 2. 핵심 솔버 (`snapwave/snapwave_solver.f90`)

### `compute_wave_field()` (`:9`)
celerity·refraction 사전계산 후 `solve_energy_balance2Dstat` 호출. 분산관계는 근사식:
$$ k = \frac{\sigma^2}{g}\,(1 - e^{-(\sigma\sqrt{h/g})^{2.5}})^{-0.4},\quad C=\sigma/k,\quad n=0.5+\frac{kh}{\sinh(2kh)},\quad C_g=nC $$
(`solver:74-78`). IG 파수 `kwav_ig` 는 동일 형태로 `sigm_ig` 사용, `cg_ig = Cg` 동기화 (`:80-90`). Hmax: 입사파는 `Hmx = gamma*depth`(`:100`), IG 는 `Hmx_ig = 0.88/k_ig*tanh(gamma_ig*k_ig*h/0.88)` (`:106`). 굴절속도:
$$ c_\theta(\theta,k)=\frac{\sigma}{\sinh(2kh)}\,(\partial_x h\,\sin\theta-\partial_y h\,\cos\theta) $$
파주기당 1/4 라디안으로 제한 `min(|cθ|, σ/4)` (`:116-137`). 솔버 후 `Fx=F*cos(thetam)`, `Fy=F*sin(thetam)` (`:176-177`).

방향 퍼짐과 분산의 문서 공백: 근거: `docs/waves.rst:7` `The input of waves as boundary conditions is still work in progress. Right now the following files should not be used:`<br>`docs/numerical_implementation.rst:55` `Wave generation`<br>`docs/numerical_implementation.rst:57` `(Work in progress)`<br>`snapwave/snapwave_boundaries.f90:85` `wd_bwv = (270.0 - wd_bwv)*pi/180`<br>`snapwave/snapwave_boundaries.f90:87` `! Convert directional spreading input to radians - independent of input type`<br>`snapwave/snapwave_boundaries.f90:88` `ds_bwv = ds_bwv * pi / 180`<br>`snapwave/snapwave_solver.f90:74` `expon   = - (sig * sqrt(depth / g))**2.5`<br>`snapwave/snapwave_solver.f90:75` `kwav    = sig**2 / g * (1.0 - exp(expon))**-0.4`<br>`snapwave/snapwave_solver.f90:76` `C       = sig / kwav`<br>`snapwave/snapwave_solver.f90:77` `nwav    = 0.5 + kwav * depth / sinh(min(2 * kwav * depth, 50.0))`<br>`snapwave/snapwave_solver.f90:78` `Cg      = nwav * C` [대조 보고서 §5 B140](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1056) 결론: 문서 누락. 이 판의 SnapWave solver는 주파수와 수심으로 파수 및 군속도를 계산한다.


### `solve_energy_balance2Dstat` (`:183`) — 메인 반복
비정형 격자에서 방향분해 에너지평형을 풀이. 노드별 ee(θ), IG 면 ee_ig(θ), 바람 면 action aa(θ).

**Sweep & 정렬**: 4 sweep 방향으로 좌표를 회전투영(`ra = x cos(θm+kπ/2)+y sin(...)`) 후 heapsort 로 정렬 (`:490-497`). 반복은 `niter*4` 회, sweep=mod(iter,4) (`:526-532`). grid edge·upwind 없는 점은 `inner=.false.` 처리 (`:501-522`).

**upwind 보간**: 두 upwind 점 `prev(1:2,θ,k)` 와 weight `w` 로 에너지·cg 보간 (`:666-685`). 풍파는 action `aa` 도 보간하며 `[ee/sigmax, ee/sigmin]` 으로 clip.

**source/sink (Step 3)**:
- 바닥마찰: `uorbi = 0.5*σ*Hk/sinh(kh)`, `Dfk = 0.28*rho*fw*uorbi^3` (`:710-711`).
- breaking: `Hk > baldock_ratio*Hmx` 일 때만 `baldock(...)` 호출 (`:716-726`).
- 식생: `vegatt` (`:730-733`).
- 소산비 under-relax: `DoverE = (1-r)*DoverE + r*(Dwk+Dfk+Dvegk)/Ek` (`:743-744`).

**에너지 평형 행렬 (Step 4)**: θ에 대한 삼중대각계. 우변 `R = ee/dt + cgprev*eeprev/ds - srcig_local*shinc2ig`(IG sink) (`:778`), 대각 `B = 1/dt + cg/ds + DoverE`, 비대각은 굴절항 `±cθ/(2dθ)` (cyclic θ경계) (`:783-797`). 바람 source `WsorE` 가산 후 `solve_tridiag` (`:799-801`).

**action 평형 (Step 5, 풍파)**: A·C 동일, `B_aa` 에 DoverA, θ 끝단은 upwind BC (`:809-838`).

**depth-limit (Step 6)**: `depthlimfac = max(1, (sqrt(Ek/rhog8)/(gammax*h))^2)`, `ee /= depthlimfac` (`:842-844`).

**IG 평형 (Step 7)**: IG 마찰 `Dfk_ig = fw_ig*0.0361*(g/h)^1.5*Hk*Ek_ig` (`:866`), IG breaking 도 Baldock(gamma_ig). 우변에 IG source `+srcig_local` (`:885-889`), θ경계는 cθ_ig 부호별 한쪽 차분 (`:893-917`).

**수렴**: sweep=4 마다 `diff/eemax < crit` 로 노드별 `ok` 마킹, `error<crit .or. %ok>99` 시 종료. IG 수렴은 로그만 출력하고 종료조건엔 입사파만 사용(주석처리됨, `:986`).

**후처리**: H, thetam(`atan2(Σee·sinθ, Σee·cosθ)`), IG H, 방향평균 beta/alphaig/srcig (`:1026-1063`). 식생 시 `swvegnonlin`(비선형 궤도속도) 후 `F = Dw*k/σ/ρ/h (+ Dveg항 + Fvw)` (`:1078-1116`).

### `solve_tridiag` (`:1123`) — Thomas 알고리즘 (전방소거·후방대입).

### `baldock` (`:1166`) — 파 breaking 소산
$$ D_w = 0.28\,\alpha\,\frac{\rho g}{T}\,e^{-(H_{max}/H_{loc})^2}\,(H_{max}^2+H_{loc}^2)\cdot f $$
여기서 `f=(Hloc/Hmax)^iexp` (Hloc>Hmax 일 때만, 가파른 해안 보강용) (`:1183-1200`).

### 문서와 코드 차이 (외부 원문 판정)

| 보고서 행 ID | 항목 | 근거 | 결론 |
|---|---|---|---|
| <a id="cv-s-b069"></a>B069 | SnapWave IG와 inner 셀 정의 버그 | Deltares/SFINCS, `v2.2.0_col_dEze_release`, [`source/src/snapwave/snapwave_solver.f90`](https://raw.githubusercontent.com/Deltares/SFINCS/v2.2.0_col_dEze_release/source/src/snapwave/snapwave_solver.f90), `snapwave/snapwave_solver.f90:412–416`<br>Deltares/SFINCS, `v2.3.0_mt_Faber_release`, [`source/src/snapwave/snapwave_solver.f90`](https://raw.githubusercontent.com/Deltares/SFINCS/v2.3.0_mt_Faber_release/source/src/snapwave/snapwave_solver.f90), `snapwave/snapwave_solver.f90:415–428`<br>Deltares/SFINCS, `v2.4.0_Galibier_release`, [`source/src/snapwave/snapwave_solver.f90`](https://raw.githubusercontent.com/Deltares/SFINCS/v2.4.0_Galibier_release/source/src/snapwave/snapwave_solver.f90), `snapwave/snapwave_solver.f90:508–516`<br>[Deltares/SFINCS 커밋 `2c55d22`](https://github.com/Deltares/SFINCS/commit/2c55d22) 및 [Deltares/SFINCS 커밋 `ed41f5d`](https://github.com/Deltares/SFINCS/commit/ed41f5d)<br>`docs/developments.rst:124`의 수정 이력을 깊이 조건 제거와 대조했다. 로컬 `snapwave/snapwave_solver.f90:508–516`에도 `if (k1 * k2 == 0) then`과 `elseif (k1==1 .and. k2==1) then ! TL: for now still needed for a working IG solver`가 남아 있다. | A 판 차이. v2.3.0은 SnapWave의 `inner`를 깊이 조건으로 바꾸던 분기를 주석 처리했다. 이 변경은 `inner`를 정적으로 유지한다. `(k1==1 .and. k2==1)`일 때 `inner`를 .false.로 바꾸는 조건은 IG 수지를 위해 남았다. [대조 보고서 §5 B069](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1034) [10-12 외부 원문 판정] [10-12 결론 검증 보완] |
| <a id="cv-s-b070"></a>B070 | SnapWave 논문과 통합 solver의 식 대조 | [Roelvink et al. (2025) preprint](https://egusphere.copernicus.org/preprints/2025/egusphere-2025-492/egusphere-2025-492.pdf), PDF 3–4쪽 식 (2.2), (2.6)–(2.7)과 계수표.<br>`snapwave/snapwave_solver.f90:778–779`의 R에는 `- srcig_local(itheta, k) * shinc2ig`가 있다. `:799`는 `if (wind) R(:) = R(:) + WsorE(:, k)`를 적용한다. `:785–787`의 A·B·C는 식 (2.6)의 중심 차분에 대응한다. `:1200`의 소산 계수는 0.28이다. `:1192–1196`은 추가 인자 f의 분기이다.<br>[외부 판독 B070](../../../_staging/recovery/compare/external-results-sf.md#b070-snapwave-통합-solver와-roelvink-et-al-2025-일관성)의 이전 SFINCS 판과 독립판도 0.28을 사용한다. 이 사실만으로 preprint와 코드 사이의 변경 시점은 정할 수 없다. | B 문서 오기·G 판단 근거 부족. Preprint의 계수 B에 있는 `c_ϑ/Δϑ`는 식 (2.6)에 없는 대각항이다. 이를 단순 표기 차이로 분류한 결론을 철회한다. R의 공통 시간·공간 전달항만 대응한다. IG 전이항과 바람 항까지 동일하다는 결론은 성립하지 않는다. 0.25와 0.28의 차이는 확인했다. 그 차이의 원인과 판별 시점은 미확인이다. [대조 보고서 §5 B070](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1035) [10-12 결론 검증 정정] |

## 3. Infragravity (IG) source/sink (`snapwave_solver.f90:1209` + `snapwave_infragravity.f90`)

### `determine_infragravity_source_sink_term` (`solver:1209`)
Leijnse et al. 2024 기반 IG source. node별 라디에이션 응력 `Sxx = (2·n - 0.5)·E` 사전계산(n은 [0,1] clip) (`:1305`). 각 방향 upwind:
- 국부 slope `beta_local = max((Σw·(zb(k)-zb(prev)))/ds, 0)` (`:1336`).
- 상대수심 `gam = 0.5*(Hprev/depthprev + H/depth)` (`:1358`).
- 쇼올링 파라미터 `alphaig` 추정 (`estimate_shoaling_parameter_alphaig`, `:1366`).
- ig_opt=1: 보존 쇼올링 `Sxx_cons = Eprev·cgprev/cg_ig·(2n-0.5)`, `dSxx = Sxx_cons - Sxxprev` (`:1383-1387`); ig_opt=2 는 실제 차분 (`:1391`). `dSxx = max(dSxx,0)`.
- IG source:
$$ \text{srcig} = \alpha_{igfac}\cdot\alpha_{ig}\cdot\sqrt{E^{ig}_{prev}}\cdot\frac{cg_{prev}}{h_{prev}}\cdot\frac{dS_{xx}}{ds}\cdot\frac{ee(\theta,k)}{E_{local}} $$
(`:1399`).
- breaking 후(gam > gamma_fac_br·gamma) Fermi-Dirac 형 transition_factor 로 srcig 를 0 으로 부드럽게 소거 (`:1407-1411`).

#### 문서와 코드 차이 (외부 원문 판정)

| 보고서 행 ID | 항목 | 근거 | 결론 |
|---|---|---|---|
| <a id="cv-s-b051"></a>B051 | SnapWave IG 생성항 버그 | Deltares/SFINCS, `v2.3.0_mt_Faber_release`, [`source/src/snapwave/snapwave_solver.f90`](https://raw.githubusercontent.com/Deltares/SFINCS/v2.3.0_mt_Faber_release/source/src/snapwave/snapwave_solver.f90), `snapwave/snapwave_solver.f90:1142`<br>Deltares/SFINCS, `v2.4.0_Galibier_release`, [`source/src/snapwave/snapwave_solver.f90`](https://raw.githubusercontent.com/Deltares/SFINCS/v2.4.0_Galibier_release/source/src/snapwave/snapwave_solver.f90), `snapwave/snapwave_solver.f90:1396–1399`<br>Deltares/SFINCS, [PR #283](https://github.com/Deltares/SFINCS/pull/283) 설명. [Deltares/SFINCS 커밋 `1f1d828`](https://github.com/Deltares/SFINCS/commit/1f1d828) 메시지.<br>로컬 생성항은 `snapwave/snapwave_solver.f90:1399`이다. `docs/developments.rst:67`의 수정 이력은 위 태그의 생성항 차이와 릴리스 커밋 메시지에 대응한다.<br>PR #283의 `Yasmine`과 문서의 `Elmessary`가 같은 사람인지는 확인하지 못했다. `k1·k2` 검사 조건은 이번 수정과 무관하다. 수정의 수치 결과는 검증하지 않았다. | A 판 차이. v2.4.0의 SnapWave IG 생성항은 방향 bin별 에너지 `eeprev_ig` 대신 총 에너지 `Eprev_ig`에 기초한다. 생성항은 `/E * ee`로 방향에 재분배된다. 릴리스 커밋 메시지는 이 변경을 PR #283의 수정으로 적는다. [대조 보고서 §5 B051](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1029) [10-12 외부 원문 판정] [10-12 결론 검증 보완] |

### `estimate_shoaling_parameter_alphaig` (`solver:1434`)
Leijnse 2024 피팅상수(beta1=0.016993 … beta7=0.34037). beta≤0 면 alphaig=0, 아니면 gam 영역별 지수식, 최종 [0,1] clip (`:1446-1479`).

### IG 경계조건 — Herbers 1994 (`snapwave_infragravity.f90`)
오프쇼어 입력점에서 IG Hm0·Tp 를 입사 스펙트럼으로부터 산정. XBeach `waveparams.f90` 3단계(build_jonswap/build_etdir/build_boundw)를 한 서브루틴 `compute_herbers` 로 포팅 (`:119`).
- Part1: JONSWAP 1D→2D 방향분포 스펙트럼 빌드 (`jonswapgk`, `:160-239`).
- Part2: 피크 주변 K=400 성분 선택, 랜덤위상/방향 할당 (`:242-388`).
- Part3: Herbers eq.1/A5 difference-interaction 계수 D 로 bound long wave 에너지 `Ebnd` 계산 (`:390-478`).
- 최종 `hsig = 4*sqrt(Σ Ebnd·df)` (`:483`), 주기 `tpDcalc` 로 Tm01/Tm-1,0/Tp/Tpsmooth (`:495`).
진입점 `determine_ig_bc` (`:11`): Hs/depth>0.5 면 depth 를 `2*hsinc` 로 강제, depth>200m 면 200 으로 제한(NaN 방지) (`:48-65`). tpig_opt 로 주기 선택(1=Tm01 기본) (`:88-104`). 분산관계는 Klopman 근사 `bc_disper` (`:582`).

## 4. 도메인 & upwind (`snapwave_domain.f90`)

현재 `initialize_snapwave_domain`은 `ext='qt'`를 설정한다. `snapwave/snapwave_domain.f90:45` `ext = 'qt'`; `snapwave/snapwave_domain.f90:52`; `sfincs_snapwave.f90:734` `coupled_to_sfincs = .true.`
현재 결합 경로는 이미 보유한 quadtree 자료를 사용하는 `read_snapwave_quadtree_mesh(.false.)`를 선택한다. `snapwave/snapwave_domain.f90:45` `ext = 'qt'`; `snapwave/snapwave_domain.f90:52`; `sfincs_snapwave.f90:734` `coupled_to_sfincs = .true.`

**upwind 이웃**: `snapwave.upw` 캐시가 있으면 읽고(prev360/w360/ds360/dhdx/dhdy), 없으면 `fm_surrounding_points`(주변점·bed slope 최소제곱) + `find_upwind_neighbours` 로 생성 후 저장 (`:223-279`).
- `find_upwind_neighbours` (`:356`): 각 노드·방향마다 주변 edge 와 광선(θ+π)의 교차점을 `intersect_angle` 로 찾아 2개 upwind 점·weight·거리 ds 산정. 교차 실패 시 prev=1, w=0 (`:405-410`).
- `fm_surrounding_points` (`:457`): face_nodes 로 cell-노드 연결관계 구성, 정렬된 surr_pts 로 bed slope `dhdx=-Σ(dx·dz)/Σdx²` 최소제곱 추정 (sferic 보정 포함) (`:566-594`).

**경계 마스크**: msk=2(파 경계), msk=3(Neumann). msk=2 없으면 구버전 encfile polygon 으로 보충 (`:286-304`). Neumann 은 `neuboundaries_light` 로 각 msk=3 점의 최근접 msk=1 점을 `neumannconnected` 에 저장 (`:308-321`, `:791`). msk=1 이 inner (`:340-348`).

**quadtree 메쉬** `read_snapwave_quadtree_mesh` (`:1039`): quadtree 점에서 refinement 레벨별(mu/nu/mnu) 10여 종 cell 타입(Type 1~10+)을 분기 생성 — fine↔coarse 전이 처리 (`:1331` 이하 장대 분기).

## 5. 경계 데이터 & 스펙트럼 (`snapwave_boundaries.f90`)

`read_boundary_data` (`:8`): jonswap(단일점)/netcdf/timeseries 분기 → `find_boundary_indices`.

read_boundary_data는 입력 파향을 Cartesian 진행 방향 라디안으로 바꾼다. `snapwave/snapwave_boundaries.f90:85` `wd_bwv = (270.0 - wd_bwv)*pi/180`
같은 루틴은 방향 퍼짐을 도에서 라디안으로 바꾼다. `snapwave/snapwave_boundaries.f90:87` `! Convert directional spreading input to radians - independent of input type`; `snapwave/snapwave_boundaries.f90:88` `ds_bwv = ds_bwv * pi / 180` 근거: `snapwave/snapwave_boundaries.f90:85` `wd_bwv = (270.0 - wd_bwv)*pi/180`<br>`snapwave/snapwave_boundaries.f90:87` `! Convert directional spreading input to radians - independent of input type`<br>`snapwave/snapwave_boundaries.f90:88` `ds_bwv = ds_bwv * pi / 180`<br>`snapwave/snapwave_solver.f90:74` `expon   = - (sig * sqrt(depth / g))**2.5`<br>`snapwave/snapwave_solver.f90:75` `kwav    = sig**2 / g * (1.0 - exp(expon))**-0.4`<br>`snapwave/snapwave_solver.f90:76` `C       = sig / kwav`<br>`snapwave/snapwave_solver.f90:78` `Cg      = nwav * C` [대조 보고서 §5 C031](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1060) 결론: 문서 오기. 이 판의 경계 리더는 방향 퍼짐을 도에서 라디안으로 변환한다.
방향 퍼짐과 파수·주파수의 분산 관계를 구분한다. `snapwave/snapwave_boundaries.f90:87` `! Convert directional spreading input to radians - independent of input type`; `snapwave/snapwave_boundaries.f90:88` `ds_bwv = ds_bwv * pi / 180`; `snapwave/snapwave_solver.f90:74` `expon   = - (sig * sqrt(depth / g))**2.5`; `snapwave/snapwave_solver.f90:75` `kwav    = sig**2 / g * (1.0 - exp(expon))**-0.4`; `snapwave/snapwave_solver.f90:76` `C       = sig / kwav`; `snapwave/snapwave_solver.f90:77` `nwav    = 0.5 + kwav * depth / sinh(min(2 * kwav * depth, 50.0))`; `snapwave/snapwave_solver.f90:78` `Cg      = nwav * C`

`update_boundary_conditions(t)` (`:471`): 경계점 갱신 → 바람장 → theta grid 를 평균 파/바람 방향 중심으로 회전 → `update_boundaries`.

`update_boundary_points` (`:521`): 시계열을 시간보간(`tbfac`). 입력 클램프 — Hs∈[0,25]m, ds∈[3,90]°, Tp∈[0.1,25]s (`:586-609`). IG bc 는 igherbers 면 `find_nearest_depth_for_boundary_points` 후 `determine_ig_bc` 호출(`:671-692`), 아니면 `tpmean_bwv_ig = tpmean_bwv * Tinc2ig` (`:696`).

**경계 스펙트럼 빌드** (`:716-725`): cos^ms 방향분포로 JONSWAP 에너지를 분배.
$$ E_0 = 0.0625\,\rho g\,H_{s}^2,\quad ms = 1/ds^2 - 1,\quad ee_{bwv}(\theta)=\frac{\text{dist}(\theta)}{\Sigma\text{dist}}\cdot\frac{E_0}{d\theta} $$
±π/2 밖은 0. IG 스펙트럼도 동일형, `E0_ig = 0.0625 rho g Hs_ig^2` (`:732`).

`make_theta_grid` (`:778`): 360° 테이블에서 중심방향 주변 ntheta 빈을 인덱스 `i360` 로 슬라이스해 w/prev/ds/windspreadfac 채움. 바람 시 `windspreadfac = cos(θ-u10dir)^mwind` 정규화 (`:818-826`).

`update_boundaries` (`:854`): 격자 경계점(nmindbnd)에 두 가장 가까운 입력점의 ee 를 가중보간 (`:870-880`). IG 는 herbers 면 eet_bwv_ig 보간, 아니면 `ee_ig = eeinc2ig*ee` (`:897-905`).

## 6. 풍파 성장 (`snapwave_windsource.f90`)

`windinput` (`:96`): 무차원 wave state 기반 wind source (Kahma & Calkoen 성장곡선, Breugem-Holthuijsen 완전발달 상한). 깊이제한 완전발달치 `Emaxddmlss=min(aa3²/16·d^(2bb3), Eful)`, `Eful=0.0036`, `Tful=7.69`(Pierson-Moskowitz) (`:125-158`). source 항 `dE = cgdmlss/fE`, `dT = cgdmlss/fT`, dcg/dx 보정 후 방향분포 `windspreadfac` 적용, 차원화 `wsorE = max(u10³·rho·..., 0)`, `wsorA = max(u10⁴·rho/g·..., 0)` (`:168-207`).

`compute_celerities` (`:67`): 노드별 분산관계(`disper_approx_1`)·refraction(`:67-94`). `disper_approx_1` (`:213`): 위 §2 동일 근사식의 단일노드판.

## 7. 식생 & RF table (`snapwave_solver.f90` + `snapwave_RFtable.f90`)

`vegatt` (`solver:1631`) → `swvegatt` (`:1687`): Suzuki et al. 2012 식 단파 식생소산.
$$ D_{vg} = \frac{1}{2\sqrt\pi}\rho\,C_d\,b\,N\,\Big(\tfrac12 k\,g/\sigma\Big)^3\,(h_{term}-h_{term,old})\,H^3 $$
(`:1738`). Cd 미지정 시 에러(M.Bendoni bulkdrag 는 주석처리) (`:1663-1670`).

`swvegnonlin` (`:1879`): Rienecker & Fenton (1981) 비선형 파형으로 skewness 유발 net drag 산정 (XBeach SurfBeat 포팅). `load_RFtable` 로 (11,18,20) RF 테이블 적재 (`:1925`), Ursell 수 기반 Ruessink 위상 `phi=π/2·(1-tanh(0.815/Urs^0.672))` 로 cos/sin 가중 w1/w2 (`:1960-1966`), h0/t0 격자에서 4점 양선형보간 (`:1972-1985`), 50점 시계열 `unl = urf2·sqrt(g·h)` 출력 (`:1999-2000`).

`snapwave_RFtable.f90`: 단일 서브루틴 `load_RFtable` (`:7`). 본문 99% 가 하드코딩 RF 계수 1D 배열(`RFvegtmp`, `:20-3981`)이며 마지막에 `RFveg = reshape(RFvegtmp, (/11,18,20/))` (`:3983`). XBeach `RFveg.inc` 를 컴파일 불필요하게 인라인한 것 (`:16-19` 주석). 차원: 11(=3 메타+8 Fourier 성분)×18(H/depth)×20(T√(g/h)).

## 8. 결합 데이터 흐름 요약

별도 host·device 메모리를 사용하는 빌드는 결합 입력의 최신성 확인이 필요하다. `sfincs_snapwave.f90:289` `subroutine update_wave_field(t, tloop)`; `sfincs_snapwave.f90:514` `!$acc update device(fwuv)`; `sfincs_output.f90:113` `if (write_map .or. write_his .or. write_rst) then`; `sfincs_output.f90:115` `!$acc update host(zs)`
`update_wave_field`는 입력 수위·바람을 host로 가져오는 지시문을 포함하지 않는다. `sfincs_snapwave.f90:289` `subroutine update_wave_field(t, tloop)`; `sfincs_snapwave.f90:514` `!$acc update device(fwuv)`; `sfincs_output.f90:113` `if (write_map .or. write_his .or. write_rst) then`; `sfincs_output.f90:115` `!$acc update host(zs)`
이 분석은 해당 빌드의 실행을 확인하지 않았다. `sfincs_snapwave.f90:289` `subroutine update_wave_field(t, tloop)`; `sfincs_snapwave.f90:514` `!$acc update device(fwuv)`; `sfincs_output.f90:113` `if (write_map .or. write_his .or. write_rst) then`; `sfincs_output.f90:115` `!$acc update host(zs)`


| 단계 | 함수 | 결과 |
|---|---|---|
| 초기화 | `couple_snapwave` → `initialize_snapwave_domain` | 메쉬·upwind·경계 |
| 갱신 시각의 입력 | `update_wave_field` | 갱신 시각의 입력은 SFINCS 수위와 선택한 바람 속도다. `sfincs_lib.f90:552` `if (snapwave .and. update_waves) then`; `sfincs_snapwave.f90:356` `snapwave_depth(nm) = max(zsm(ip) - snapwave_z(nm), 0.00001)`; `sfincs_snapwave.f90:360` `snapwave_depth(nm) = max(zs(ip) - snapwave_z(nm), 0.00001)`; `sfincs_snapwave.f90:390` `u10 = sqrt(windu(ip)**2 + windv(ip)**2)`<br>비갱신 단계는 마지막 파랑 결과를 유지한다. `sfincs_lib.f90:552` `if (snapwave .and. update_waves) then`; `sfincs_snapwave.f90:356` `snapwave_depth(nm) = max(zsm(ip) - snapwave_z(nm), 0.00001)`; `sfincs_snapwave.f90:360` `snapwave_depth(nm) = max(zs(ip) - snapwave_z(nm), 0.00001)`; `sfincs_snapwave.f90:390` `u10 = sqrt(windu(ip)**2 + windv(ip)**2)`<br>수위는 대응 셀이 없으면 0.0을 사용한다(`sfincs_snapwave.f90:349` `if (ip > 0) then`; `sfincs_snapwave.f90:368` `snapwave_depth(nm) = max(0.0 - snapwave_z(nm), 0.00001)`). [10-12 전수 검증 보완] 바람 전달은 `wind`·`snapwavewind`가 참이고 대응 셀이 있을 때 수행한다(`sfincs_snapwave.f90:376` `if (wind) then ! =We have wind inputs given to SFINCS`; `sfincs_snapwave.f90:378` `if (snapwavewind) then ! =We have windgrowth in SnapWave turned on`; `sfincs_snapwave.f90:384` `if (ip>0) then`). [10-12 전수 검증 보완] |
| 경계 | `update_boundary_conditions` | ee/ee_ig 경계 스펙트럼, theta grid |
| 솔버 | `compute_wave_field` → `solve_energy_balance2Dstat` | H, H_ig, Tp, Dw, F, thetam |
| IG | `determine_infragravity_source_sink_term` + Herbers bc | srcig, alphaig, H_ig |
| 출력 매핑 | `update_wave_field` 후반 | hm0(×√2), hm0_ig, fwuv(force/rhow) |

SnapWave→SFINCS 의 물리적 되먹임은 **UV 점 파 force `fwuv`** (radiation stress divergence/ρ → 운동량 가속도, `sfincs_snapwave.f90:502-508`)로, 이것이 SFINCS 흐름에 wave setup·wave-driven current 를 만든다.

SnapWave 갱신 단계는 새 `fwuv`를 같은 단계의 운동량에 사용한다. `sfincs_lib.f90:556` `call update_wave_field(t, tloopsnapwave)`; `sfincs_lib.f90:584` `call compute_fluxes(dt, tloopflux)`; `sfincs_snapwave.f90:502` `fwuv(ip) = waveforces_ratio * (0.5 * (cosrot * fwx0(nm) + sinrot * fwy0(nm)) + 0.5 * ( cosrot * fwx0(nmu) + sinrot * fwy0(nmu))) / rhow`; `sfincs_momentum.f90:606` `frc = frc + phi * sign(min(abs(fwuv(ip)), fwmax), fwuv(ip))` 운동량 소비 경로는 `if (bathtub) then`의 ELSE이다(`sfincs_lib.f90:572` `if (bathtub) then`; `sfincs_lib.f90:578` `else`; `sfincs_lib.f90:584` `call compute_fluxes(dt, tloopflux)`). [10-12 전수 검증 보완]
비갱신 단계는 마지막 `fwuv`를 사용한다. `sfincs_lib.f90:556` `call update_wave_field(t, tloopsnapwave)`; `sfincs_lib.f90:584` `call compute_fluxes(dt, tloopflux)`; `sfincs_snapwave.f90:502` `fwuv(ip) = waveforces_ratio * (0.5 * (cosrot * fwx0(nm) + sinrot * fwy0(nm)) + 0.5 * ( cosrot * fwx0(nmu) + sinrot * fwy0(nmu))) / rhow`; `sfincs_momentum.f90:606` `frc = frc + phi * sign(min(abs(fwuv(ip)), fwmax), fwuv(ip))`

## 문서 참고 링크 오류

v2.0.2 릴리스 링크의 정정은 [변경 이력 노트의 정본](../manual-notes/sfincs-v2.4.0-galibier-changelog-known-issues.md#문서-참고-링크-오류)을 따른다. [10-12 결론 검증 보완]
