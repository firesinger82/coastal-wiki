---
title: "ADCIRC 2D-baroclinic 결합 (couple2baroclinic3D.F) — 외부 3D 모델 fort.11.nc 의 depth-avg 경압압력경사(BPGX/BPGY)·부력진동수·MLD·internal tide dispersion 시공간 보간 → 2D 운동량"
topic: adcirc
canonical_source: self
citation_status: verified
last_source_check: 2026-10-11 (recovery 재판독 대조)
verification_method: "models/ADCIRC/raw/source_code/adcirc/src/couple2baroclinic3D.F (1168) 직접 read — Module Couple2BC3D + Read_BC3D_NetCDF(113, BPGX/BPGY/SigTS/NB/NM/MLD/CDisp/DispX/DispY) + Put_BC3D_on_ADCIRC_Grid(855 공간보간) + Update_BC3D_Info(714 시간보간) + FBPG_Disp_from_BC3D(1012) + 적용(momentum.F:473-477 VIDBCPDXOH) file:line 인용. WJP(Westerink-Pringle?) 개발."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — BC3D 결합 데이터·보간·적용 verbatim"
verification_date: 2026-06-03
related:
  - models/ADCIRC/source-analysis/adcirc-momentum-implementation.md
  - models/ADCIRC/source-analysis/adcirc-tidal-forcing.md
  - models/ADCIRC/source-analysis/adcirc-nodal-attributes.md
  - models/ADCIRC/source-analysis/adcirc-3d-mode.md
---

# ADCIRC 2D-baroclinic 결합 (couple2baroclinic3D.F)

> `src/couple2baroclinic3D.F`(1168, Module `Couple2BC3D`) 직접 read. **2D barotropic ADCIRC** 가 외부 **3D baroclinic ocean model**(예: HYCOM)의 경압 효과를 받는 결합 — full 3D([[adcirc-3d-mode]]) 없이 baroclinic pressure gradient + internal tide 를 포함. `CBaroclinic` 활성 시 [[adcirc-momentum-implementation]] §1 의 baroclinic pressure 항(momentum.F:473) 공급원.

## 1. 개념 (module 주석 :39-52)

- 외부 3D 모델이 산출한 **depth-averaged 경압 압력경사**(BPGX/BPGY)를 ADCIRC 2D 운동량에 더함 → 2D 모델이 밀도구배 효과(하구 염분쐐기·대양 경압류)를 흉내.
- **good oceanographic practice 주석**(WJP, :41-50): in-situ 밀도/온도 직접 보간은 부정확 → 본래는 Conservative T/S(SA, θ) 를 보간 후 N·ρ 재계산해야. 현 구현은 외부 모델이 미리 계산한 **BPG·N·dispersion 을 직접 read**(공간 절약 위해 2 timestep 만 보관·보간).

## 2. 입력 — fort.11.nc NetCDF (Read_BC3D_NetCDF :113)

`densityFileName`의 기본값은 `fort.11.nc`다 (`src/read_input.F:882` `densityFileName = 'fort.11.nc';`).
reader는 `time·strlen` 차원과 `time` 문자열 배열을 읽는다 (`src/couple2baroclinic3D.F:213` `call check_err(nf90_inq_dimid(nc_id,'time', Temp_ID))`; `src/couple2baroclinic3D.F:215` `call check_err(nf90_inq_dimid(nc_id,'strlen', Temp_ID))`; `src/couple2baroclinic3D.F:220` `call Check_err(NF90_INQ_VARID(NC_ID,'time',Temp_ID))`; `src/couple2baroclinic3D.F:226` `call check_err(nf90_get_var(nc_id, Temp_ID,`; `src/couple2baroclinic3D.F:227` `&                  TSS,start=[1, BC3D_IT],count=[SL, 1]))`). reader는 `%Y-%m-%d %H:%M` 날짜 문자열을 파싱한다 (`src/couple2baroclinic3D.F:228` `TNDT = strptime(trim(TSS),"%Y-%m-%d %H:%M")`).

| 변수 | 내용 |
|---|---|
| `BPGX`/`BPGY` | depth-averaged 동서/남북 **baroclinic pressure gradient** |
| `SigTS` | 자유표면 sigmat 밀도 |
| `NB`/`NM` | `NB`는 해저 부력진동수다 (`src/couple2baroclinic3D.F:145` `! Buoyancy frequency at the seabed`). `NM`은 수심 평균 부력진동수다 (`src/couple2baroclinic3D.F:147` `! Depth-averaged nuoyancy frequency`). `LoadIT_Fric`은 두 변수의 읽기를 제어한다 (`src/couple2baroclinic3D.F:144` `if (LoadIT_Fric) then`; `src/couple2baroclinic3D.F:146` `BC3D_NB = read_nc_var(NC_ID,'NB',BC3D_IT,XI,NX,YI,NY)`; `src/couple2baroclinic3D.F:148` `BC3D_NM = read_nc_var(NC_ID,'NM',BC3D_IT,XI,NX,YI,NY)`). |
| `MLD` | 직교·staggered 경로는 `NOLIBF=3`과 `HBREAK>0`에서 `MLD`를 읽는다 (`src/couple2baroclinic3D.F:151` `if (NOLIBF.eq.3) then`; `src/couple2baroclinic3D.F:152` `if (HBREAK.gt.0d0) then`; `src/couple2baroclinic3D.F:154` `BC3D_MLD = read_nc_var(NC_ID,'MLD',BC3D_IT,XI,NX,YI,NY)`). ADCIRC 격자 reader는 `NOLIBF=3`이면 `HBREAK`와 관계없이 `MLD`를 읽는다 (`src/couple2baroclinic3D.F:509` `IF (NOLIBF.EQ.3) THEN`; `src/couple2baroclinic3D.F:511` `mld_g = read_nc_var_adc(NC_ID,'MLD',BC3D_IT,np_g)`). |
| `CDisp`/`DispX`/`DispY` | 직교·staggered 경로는 `NOLIBF=3`과 `HBREAK<=0`에서 운동량 분산에 따른 마찰 계수 `CDisp`를 읽는다 (`src/couple2baroclinic3D.F:151` `if (NOLIBF.eq.3) then`; `src/couple2baroclinic3D.F:152` `if (HBREAK.gt.0d0) then`; `src/couple2baroclinic3D.F:157` `BC3D_CD = read_nc_var(NC_ID,'CDisp',BC3D_IT,XI,NX,YIs,NYs)`). `DispX·DispY`는 `abs(IDEN)=6`에서 읽는 운동량 분산 항이다 (`src/couple2baroclinic3D.F:161` `if (abs(iden).eq.6) then`; `src/couple2baroclinic3D.F:163` `BC3D_DX = read_nc_var(NC_ID,'DispX',BC3D_IT,XI,NX,YIs,NYs)`; `src/couple2baroclinic3D.F:165` `BC3D_DY = read_nc_var(NC_ID,'DispY',BC3D_IT,XI,NX,YIs,NYs)`). |

`ABS(IDEN)>=8`의 ADCIRC 격자 schema는 `node·nele` 길이를 전역 격자 수와 비교한다 (`src/couple2baroclinic3D.F:253` `IF (IDEN.GE.8) THEN`; `src/couple2baroclinic3D.F:255` `call Check_err(NF90_INQ_DIMID(NC_ID,'node',Temp_ID))`; `src/couple2baroclinic3D.F:257` `IF (NY.NE.NP_G) THEN`; `src/couple2baroclinic3D.F:267` `call Check_err(NF90_INQ_DIMID(NC_ID,'nele',Temp_ID))`; `src/couple2baroclinic3D.F:269` `IF (NY.NE.NE_G) THEN`). 이 reader는 `BPGX·BPGY·SigTS`를 읽는다 (`src/couple2baroclinic3D.F:501` `bpgx_g  = read_nc_var_adc(NC_ID,'BPGX',BC3D_IT,np_g)`; `src/couple2baroclinic3D.F:502` `bpgy_g  = read_nc_var_adc(NC_ID,'BPGY',BC3D_IT,np_g)`; `src/couple2baroclinic3D.F:503` `sigts_g = read_nc_var_adc(NC_ID,'SigTS',BC3D_IT,np_g)`). 이 reader도 `LoadIT_Fric`에서 `NB·NM`을 읽는다 (`src/couple2baroclinic3D.F:504` `IF (LoadIT_Fric) THEN`; `src/couple2baroclinic3D.F:506` `nb_g = read_nc_var_adc(NC_ID,'NB',BC3D_IT,np_g)`; `src/couple2baroclinic3D.F:507` `nm_g = read_nc_var_adc(NC_ID,'NM',BC3D_IT,np_g)`). 확인하지 않음: 외부 파일 생산자가 사용하는 변수별 입력 단위.

- staggered grid 보간계수(XI/YI vs XIc/YIc/YIs) — BPGX 는 u-point, BPGY 는 v-point 격자(:137-139).
- `LoadIT_Fric`(nodalattr, [[adcirc-nodal-attributes]]) + `HBREAK` 연계(:36, :144).

## 3. 보간 (공간 + 시간)

- **공간** `Put_BC3D_on_ADCIRC_Grid`(:855) / `Read_BC3D_NetCDF_on_ADCIRC_Grid`(:479): BC3D lon/lat 정규격자 → ADCIRC unstructured node 보간(`Get_LonLatDepthTime` :174 좌표·보간계수).
- **시간** `Update_BC3D_Info`(:714): **2 timestep 만 메모리 보관**, 그 사이 선형 보간(`densityTimeIterator` skip). `Initial_BC3D_NetCDF`(:627) cold-start 초기화.

## 4. 적용 — momentum (FBPG_Disp_from_BC3D :1012 → momentum.F:473)

```fortran
! momentum.F:474-477 (CBaroclinic)
DBCPDX1A = VIDBCPDXOH(NM1) * AreaIE     ! 정점별 수직적분 baroclinic pressure gradient / H × element 면적
```
- `VIDBCPDXOH`는 이미 수심 평균한 외부 `BPG`와 자유수면 추가 항을 합친다 (`src/couple2baroclinic3D.F:1134` `VIDBCPDXOH(J) = Ramp*(VIDBCPDXOH(J)/TotalArea(J) + BXE(J))`). 현재 자유수면 항은 `(g/RhoWat0)*grad[EtaN*SigTS]`의 면적 평균이다 (`src/couple2baroclinic3D.F:1107` `VIDBCPDXOHN1 = G/RhoWat0*(DARhoMRho0N1*EtaN1*FDX1O2A`; `src/couple2baroclinic3D.F:1108` `&                + DARhoMRho0N2*EtaN2*FDX2O2A`; `src/couple2baroclinic3D.F:1109` `&                + DARhoMRho0N3*EtaN3*FDX3O2A)`; `src/couple2baroclinic3D.F:1134` `VIDBCPDXOH(J) = Ramp*(VIDBCPDXOH(J)/TotalArea(J) + BXE(J))`). 해석: ADCIRC2D+ rst 두 식에서 도출되는 `eta/H` 계수와 이 경로가 다르다 (`docs/user_guide/special_features/adcirc2d_plus.rst:37` `\frac{\partial \mathbf{U}}{\partial t} + \mathbf{U} \cdot \nabla \mathbf{U} + f \mathbf{k} \times \mathbf{U} = - \nabla\left( \frac{p_s}{\rho_0} + g(\eta - \eta_{EQ} - \eta_{SAL}) \right) - \frac{\text{BPG}}{H} + \frac{\boldsymbol{\tau}_s - \boldsymbol{\tau}_b}{\rho_0 H} - \gamma_D \mathbf{C} \mathbf{U}`; `docs/user_guide/special_features/adcirc2d_plus.rst:48` `\text{BPG} = \frac{g}{\rho_0} \left[ \int_{-h}^{0} \nabla \left( \int_{0}^{z} (\rho - \rho_0) \, dz' \right) dz + \eta \nabla[\eta(\rho_s - \rho_0)] \right]`; `src/couple2baroclinic3D.F:1107` `VIDBCPDXOHN1 = G/RhoWat0*(DARhoMRho0N1*EtaN1*FDX1O2A`). 확인하지 않음: 외부 파일 생성 과정이 이 차이를 보상하는지.
- `DispX·DispY`는 별도 운동량 분산 항으로 전달한다 (`src/couple2baroclinic3D.F:161` `if (abs(iden).eq.6) then`; `src/couple2baroclinic3D.F:163` `BC3D_DX = read_nc_var(NC_ID,'DispX',BC3D_IT,XI,NX,YIs,NYs)`; `src/couple2baroclinic3D.F:165` `BC3D_DY = read_nc_var(NC_ID,'DispY',BC3D_IT,XI,NX,YIs,NYs)`; `src/couple2baroclinic3D.F:1136` `VIDISPDXOH(J) = Ramp*DXE(J)`; `src/couple2baroclinic3D.F:1137` `VIDISPDYOH(J) = Ramp*DYE(J)`). `NB·NM`은 내부 조석 변환 계수 계산에 쓴다 (`src/nodalattr.F:2656` `Baroc: IF (CBaroclinic.and.abs(IDEN).ge.5) THEN`; `src/nodalattr.F:2673` `Fit = IT_Fric(I,1)*NB(I)/DP(I)*`; `src/nodalattr.F:2694` `NBdiff = (NB(I)**2d0 - omega**2d0)`; `src/nodalattr.F:2695` `NMdiff = (NM(I)**2d0 - omega**2d0)`). `CDisp`의 읽기 조건은 이 두 경로와 다르다 (`src/couple2baroclinic3D.F:151` `if (NOLIBF.eq.3) then`; `src/couple2baroclinic3D.F:152` `if (HBREAK.gt.0d0) then`; `src/couple2baroclinic3D.F:157` `BC3D_CD = read_nc_var(NC_ID,'CDisp',BC3D_IT,XI,NX,YIs,NYs)`).

## 5. 위치 — 2D vs 3D

| 방식 | 경압 처리 |
|---|---|
| **2D + BC3D 결합**(본 노트) | 외부 3D 모델의 depth-avg BPG 를 read·보간 (경량, 대양 조석+경압) |
| `densityForcingType` 비교 문자열 | 현재 코드의 비교 문자열은 `BuoyancyFrequenciesonGrid`다 (`src/read_input.F:926` `elseif (trim(densityForcingType).eq.'BuoyancyFrequenciesonGrid') then`; `src/read_input.F:927` `IDEN = 9`). rst의 `BuoyancyFrequenciesOnGrid`는 `On`의 대소문자가 다르다 (`docs/user_guide/special_features/adcirc2d_plus.rst:94` ``` ``'BuoyancyFrequenciesOnGrid'`` ```). 해석: 문서 문자열을 그대로 쓰면 이 분기를 켜지 못한다 (`src/read_input.F:926` `elseif (trim(densityForcingType).eq.'BuoyancyFrequenciesonGrid') then`; `docs/user_guide/special_features/adcirc2d_plus.rst:94` ``` ``'BuoyancyFrequenciesOnGrid'`` ```). |
| **full 3D**([[adcirc-3d-mode]]) | ADCIRC 자체 연직 분해(vsmy.F) + 내부 밀도·baroclinic |

→ BC3D 결합 = global tide+surge 모델에 baroclinic/internal-tide 보정을 저비용으로 추가하는 경로(full 3D 비용 회피).

## 6. 연결

- [[adcirc-momentum-implementation]] — VIDBCPDXOH → baroclinic pressure 항(momentum.F:473)
- [[adcirc-tidal-forcing]]의 내부 조석 변환 경로는 `NB·NM`을 사용한다 (`src/nodalattr.F:2694` `NBdiff = (NB(I)**2d0 - omega**2d0)`; `src/nodalattr.F:2695` `NMdiff = (NM(I)**2d0 - omega**2d0)`). 외부 `DispX·DispY`는 별도 운동량 분산 항이다 (`src/couple2baroclinic3D.F:1136` `VIDISPDXOH(J) = Ramp*DXE(J)`; `src/couple2baroclinic3D.F:1137` `VIDISPDYOH(J) = Ramp*DYE(J)`).
- [[adcirc-nodal-attributes]] — LoadIT_Fric·HBREAK internal tide friction 연계
- [[adcirc-3d-mode]] — full 3D 경압(대안)
- 외부 3D ocean model(HYCOM 등) → fort.11.nc BPG/N/dispersion preprocessor
