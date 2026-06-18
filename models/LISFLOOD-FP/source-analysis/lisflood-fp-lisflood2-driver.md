---
title: "LISFLOOD-FP lisflood2/ 신규 driver 계층 — SGC 고성능 솔버 orchestration"
model: LISFLOOD-FP
component: lisflood2-driver
canonical_source: self
citation_status: verified
verification_method: "lisflood2/{lisflood_processing,DataTypes,sgm_fast,lis2_output,file_tool}.cpp 및 lisflood.cpp:772 직접 Read; 인용 file:line 모두 본문 라인 확인"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "[[lisflood-fp-architecture-source-map]]"
---

# lisflood2/ — SGC 전용 고성능 driver 계층

## 1. 정체와 classic lisflood.cpp 와의 관계

`lisflood2/`는 **SGC(Sub-Grid Channel) 모드 전용**의 재작성된 고성능 2D 솔버 계층이다. classic 코드(`lisflood.cpp` 등)의 `Arrptr`/`Solverptr`/`Statesptr` 구조체 기반 초기화는 그대로 재사용하되, 시간적분 직전에 데이터를 **padding 정렬·SoA·블록/행 분할** 자료구조로 변환하고, classic 의 `IterateQ`/`UpdateH` 대신 자체 루프를 돈다.

진입 분기 — `lisflood.cpp:770-773`: `Statesptr->SGC == ON` 일 때만 `Fast_MainStart(...)` 호출 (주석에 옛 `IterateQ(...)` 호출이 comment-out 됨). 즉 비-SGC 경로(fv1/dg2/acceleration/Roe)는 별도 솔버로 분기되고, lisflood2 는 SGC 일 때만 활성.

호출 체인:
```
lisflood.cpp:772  Fast_MainStart
  └ lisflood_processing.cpp:2173 Fast_MainStart  (Tstep 초기화 + CalcT)
      └ :2248 Fast_MainInit          (메모리 변환·구조 생성)
          └ :2123 Fast_IterateLoop   (sgm_fast.cpp:3986, 시간적분 메인 루프)
              └ sgm_fast.cpp:3479 Do_Update  (한 timestep: Q→BC→Vol/H)
```

| 계층 파일 | 책임 |
|---|---|
| `lisflood_processing.cpp` | classic→fast 메모리 변환, 모든 보조구조(sub-grid·weir·BC·point source·routing·dam·superlink) 초기화 (`Fast_MainInit`) |
| `DataTypes.cpp` | fast 자료구조 allocate/zero 헬퍼 |
| `sgm_fast.cpp` | 핵심 수치 커널(inertial Q, SGC 단면, weir/bridge/dam) + `Do_Update` + `Fast_IterateLoop` |
| `lis2_output.cpp` | 정규/최종 raster 출력 (padded→unpadded, sub-grid Q/V 재구성) |
| `file_tool.cpp` | asc/bin/netCDF I/O 저수준 + grid 비교 디버그 |

classic 솔버의 세부 SGC 수치(`sgc.cpp` 의 `SGC_FloodplainQ`, `SGC_UpdateH`)는 [[lisflood-fp-architecture-source-map]] 참조. 본 노트는 lisflood2 의 driver/orchestration 측면에 집중한다.

## 2. 핵심 자료구조 (DataTypes.cpp, header DataTypes.h)

`Arrptr` 의 AoS·grid-per-field 표현을 **flow/cell 리스트(SoA)** 로 변환한다. 핵심: 채널이 있는 셀과 셀-쌍(flow)만 압축 저장하여 vectorize.

- `SubGridCellInfo` — sub-grid 채널 셀 SoA. `AllocateSubGridCellInfo` (`DataTypes.cpp:21-39`)가 좌표·`sg_cell_grid_index_lookup`·`sg_cell_cell_area`·`sg_cell_dem`·`sg_cell_SGC_width`/`_c`/`_BankFullHeight`/`_BankFullVolume`/`_group`/`_is_large` 배열을 alloc. `ZeroSubGridCellInfo`(`:41-57`)는 -1/-1.0 sentinel 로 초기화.
- `SubGridFlowInfo` — 셀-쌍 flow 정보. `sg_flow_ChannelRatio`·`sg_flow_effective_distance`·`sg_flow_g_friction_sq`·`sg_pair_cell_index_lookup`·`flow_pair`(쌍 끝 셀)·`sg_cell_flow_lookup`(셀별 add/subtract flow index).
- `WetDryRowBound` — `AllocateWetDryRowBound`(`:3-19`). 행마다 `fp_h`/`fp_h_prev`/`fp_vol`/`dem_data` `IndexRange`(start,end), 블록 경계 `block_row_bounds`. **wet/dry 압축의 핵심**: 매 step 젖은 컬럼 범위만 순회.
- `WaterSource`(`:59-72`) — point source/BC 공용. `Ident`(`ESourceType`)·`Val`·`timeSeries`·`Q_FP_old`/`Q_SG_old`·friction²(FP/SG) + 내장 `ws_cell`.
- `WeirLayout`(`AllocateWeir :75-88`) — qx/qy index, `Weir_Q_old_SG`, `Weir_grid_index`, `Weir_pair_stream_flow_index`, `cell_pair`.
- `RouteDynamicList`(`:91-97`) — 고경사 셀 routing 동적 리스트.

## 3. 메모리/구조 변환 — Fast_MainInit (lisflood_processing.cpp:1524)

핵심 설계 결정:

- **Padding**: `grid_cols_padded = grid_cols + 1 + 64/sizeof(NUMERIC_TYPE)`, `GRID_ALIGN_WIDTH` 정렬(`:1531-1532`). qx 가 한 컬럼 더 필요하고 매 행 우측에 최소 64B 빈 패딩 → SIMD 정렬 보장.
- **classic 배열 대량 free**: Trent/Roe 솔버 잔재(`HU,HV,RSHU,...,FHVy`), `maxH/maxHtm/initHtm/...`, `LimQx/Vx/...` 를 변환 후 즉시 해제(`:1539-1619`). `Fast_MainInit` 말미(`:2092-2122`)에서 `Weir_Identx/y`·`FlowDir`·`H`·`DEM`·`Manningsn`·`SGCwidth`·`SGCz`·`dx/dy/dA` 등 변환 끝난 grid 도 free.
- **컬럼 벡터화**: 위경도 모드에서 셀 dx/dy/area 가 위도에 따라 변하므로 `dx_col`/`dy_col`/`cell_area_col` 를 행당 1값(`grid_rows+1`)으로 저장(`:1643-1651`).
- 마지막에 `Fast_IterateLoop` 호출(`:2123`)로 제어 이양.

### 3.1 sub-grid 구조 빌드 — 두 전략

`InitSubGridStructureByRows`(`:519`)와 `InitSubGridStructureByBlocks`(`:186`) 두 버전. 헤더 주석(`:181-185`, `:514-518`): "sub grid divided into rows/blocks — 행을 floodplain 과 같은 OpenMP 루프에서 처리; 행당 sub-grid 셀이 적어 vectorization 을 완전히 활용 못함". `_SGM_BY_BLOCKS` 매크로로 선택(sgm_fast.cpp 의 `#if _SGM_BY_BLOCKS`).

3-pass 알고리즘(rows 버전):
1. `CheckSubGrid`(`:76`)로 행별 flow/cell count 선계산 (메모리 크기 결정, `:548-593`).
2. 셀 정보 채우기 + `sub_cell_lookup_grid_tmp` 채움 (first-touch NUMA, `#pragma omp parallel for` `:619`).
3. flow 쌍 연결 — 우/하(+D8 대각) 이웃과 link, `sg_cell_flow_lookup.flow_add/subtract` 채움, **floodplain 폭에서 채널비율 차감**(`Fp_xwidth`/`Fp_ywidth -= ChannelRatio`, omp critical, `:744-747`,`:800-803`).

`CheckSubGrid`(`:76-179`): TauDEM 방향코드(1:E,2:NE,...,8:SE, 주석 `:91`)를 `SGCdirn` 로 검사. weir 있는 곳·DEM_NO_DATA(단 ChanMask 있으면 예외, `:98`)는 link 제외. D8 대각(`SGCd8`)은 `belowright`/`belowleft` 추가(`:136-176`).

`CopyToSubSubGridFlowInfo`(`:24-51`): meander 계수 `0.5*(SGCm[g0]+SGCm[g1])` 로 effective distance 보정(`:31-32`); friction²= `g*0.5*n0*n1`(셀별 n) 또는 `g*SGCn[group]`(`:35-42`); ChannelRatio = `min(width0,width1)/cell_width`(`:47-49`).

## 4. 수치 커널 (sgm_fast.cpp)

### 4.1 관성파 Q (CalculateQ, :47-111)

inertial wave 이산화. `_CALCULATE_Q_MODE` 매크로로 변형. mode 0(주석 `:57-71`):

$$Q = \dfrac{Q_{old} - g\,A\,\Delta t\,S_f}{1 + \Delta t\, g n^2\, |Q_{old}| / (R^{4/3} A)}$$

여기서 `R^{4/3}` 는 `CBRT(R*R*R*R)` 로 계산 — 주석 "4 multiplies and 1 cube root profiled faster than POW(R,4/3)"(`:64`). mode 1 은 Froude 상한(`max_Froude*A*sqrt(gR)`) 적용(`:87-92`).

### 4.2 SGC 단면 — SGC2_CalcR / SGC2_CalcA / SGC2_CalcUpH / SGC2_CalcUpV

`SGCchantype`(group별) switch 로 7종 단면: 1 직사각(기본)·2 지수(power)·3 선형·4 삼각·5 포물·6 직사각(무제방)·7 사다리꼴 (`:149-209`). `_ONLY_RECT==1` 컴파일 시 직사각만(`:142-144`). `SGC2_CalcUpV/UpH`(`:365-454`)는 V↔h 역변환. `SGC2_CalcPointFREE`(`:301-360`)는 한 면에서 채널 Q(SG)와 floodplain Q(FP) 를 동시 계산하고, FP 에서 채널이 차지한 비율을 차감(`Q_FP_corrected`, Neal 2012 Fig.1(C) 주석 `:298`).

### 4.3 weir/bridge/dam

- `CalcWeirQ`(`:498-582`): broad-crested weir, free/drowned flow (`Weir_m` 비율 임계), `maxQ=0.5*vol/dt` 상한, 일방향(culvert) `Weir_Fixdir` 지원.
- `CalcBridgeQ`(`:587-702`): 개수로(Qoc)·오리피스/압력류(Qp)·천이대(Tz) 블렌딩, 상류 속도수두 `heg` 보정(`:663-665`).
- `DamOpQ`(`:867-957`): 7종 댐 운영 규칙 (constant·proportional·Döll 2003·Wada 2014·Wisser 2010·Hanasaki 2005 등, 각 주석에 출처). `SGC2_UpdateDamFlowVolume`(`:959`)가 동적 edge 별 FP+SG 유입 계산 후 volume 이동.

## 5. 한 timestep — Do_Update (sgm_fast.cpp:3479)

`#pragma omp parallel` 안에서 호출됨(루프 `:4160`). 단계 순서:

1. **Q 갱신** (`#pragma omp for ... nowait`, 블록별, `:3528-3655`):
   `SGC2_UpdateQx_row`(`:3550`)→ routing 또는 diffusive 분기 → 선택적 velocity → `SGC2_UpdateQy_row`(`:3599`) 동일 → `ProcessSubGridQBlock`(sub-grid 채널 Q) → `SGC2_UpdateWeirsFlow_row`. wet/dry bound 로 순회 범위 축소(`fp_h[j].start-1` 등, `:3544`).
2. **overlapped single** (`#pragma omp single nowait`, `:3678`): reduction 변수 0화, point source TimeSeries 선보간, `SGC2_BCs`(경계 Q+sub-grid vol, `:3714`), evap/rain deltaH 계산.
3. **barrier**(`:3754`) — Q·single 완료 보장. 이후 dam(`:3756`)·superlink(`:3766`)·stage velocity 출력(`:3774`)을 single 로.
4. **bridge/routing-correct/hazard**(`:3812-3861`, omp for) — Q 전부 갱신 후, Vol/H 읽기 전에 수행(주석 `:3814-3815`).
5. **Vol/H 갱신**(`#pragma omp for reduction`, `:3866-3903`): `SGC2_UpdateVolumeHeight_block`(`:3877`)가 floodplain(`SGC2_UpdateVol_floodplain_row :2469`)+sub-grid(`SGC2_UpdateVol_sub_grid_row :2549`) 볼륨→높이 변환, blockHmax/evap/rain/Qpoint reduction.
6. **inundation/면적·볼륨**(`:3933-3960`): `time_next>=MassTotal || mint_hk==OFF` 일 때만 침수시간·domain volume/flood area reduction.

`Do_Update` 자체는 Tstep 을 바꾸지 않음 — Hmax reduction 만 산출하고, 호출부가 다음 CFL 을 계산.

## 6. 시간적분 메인 루프 — Fast_IterateLoop (sgm_fast.cpp:3986)

`curr_time = Solverptr->t`(`:4113`)에서 시작, `#pragma omp parallel` 진입(`:4160`) 후:

```
while (curr_time < Sim_Time && stop_loop == OFF)   // :4163
    delta_time = Solverptr->SGCtmpTstep            // :4194  (이전 step 에서 계산된 CFL)
    Do_Update(... delta_time ...)                   // :4197
    #pragma omp single {                            // :4216
        Tstep=delta_time; wet/dry fp_vol←fp_h 복사;
        Evap/Rain/Qpoint/Qin/Qout/VolIn/Out 누적;
        SGCtmpTstep = min(cfl*min_dx_dy*SGC_m / sqrt(g*max(Hmax,DamMaxH)), InitTstep)  // :4499
        curr_time += delta_time; Solverptr->t=curr_time; itCount++;                     // :4503-4506
        if curr_time>=MassTotal { mass balance error → mass_fp ; MassTotal+=MassInt }   // :4510,4564
        if curr_time>=SaveTotal { write_regular_output ; SaveTotal+=SaveInt }            // :4655,4705
    }
```

**CFL 시간스텝**(`:4499`):
$$\Delta t = \min\!\left(\dfrac{\mathrm{cfl}\cdot \min(dx,dy)\cdot m_{SGC}}{\sqrt{g\,\max(H_{max},H_{dam})}},\ \Delta t_{init}\right)$$

루프 진입 전 초기 `SGCtmpTstep` 은 `Fast_MainStart`(`:2227-2229`)에서 `CalcT` 로 설정. classic 과 달리 SGC 는 UpdateH 가 아니라 여기서 timestep 을 계산한다는 주석(`:2225-2226`).

## 7. 출력 (lis2_output.cpp, file_tool.cpp)

### 7.1 write_regular_output (lis2_output.cpp:117)

저장 간격마다 호출. 핵심:
- **padded→unpadded + 채널 깊이 합산**: `.wd` = `h + SGC_BankFullHeight`(채널/제방 위 깊이), `.wdfp` = `h`(floodplain 만), depth_thresh 이하는 0 truncate(`:164-204`). `.elev`(`:250-277`), `saveint_max` 시 `.wd_max`/`.wdfp_max`(`:207-247`).
- **sub-grid Q 재구성**: `get_sub_grid_values`(`:66-114`)가 flow-list SoA 를 qx/qy grid 로 산란(쌍 셀 grid_index 인접 여부로 qx/qy 판별, `:101-110`); `add_boundary_sub_flow`(`:8-55`)로 경계 채널 flux 가산 → `.Qcx`/`.Qcy`(`:330-341`). 채널 폭 `.Fwidth`(`:296-327`).
- **velocity**: `.Vx`/`.Vy`(large sub-grid 셀은 FP flow 없어 0, `:357-371`), `.SGCVx`/`.SGCVy`/`.SGCVc`(셀중심 최대속도, `:401-447`).
- 첫 호출 시 `StartNetCDF`(`:154-160`).

`WriteOutput`(`:468`)는 시뮬 종료 시 `.inittm`/`.totaltm`/`.max`/`.mxe`/`.maxtm`/`.maxV*`/`.maxVc*`/`.maxHaz` 최종 raster. `maxdepthonly` 모드 분기(`:478`).

### 7.2 file_tool.cpp — I/O 저수준

- `read_file`(`:597-638`): 헤더 첫 4byte `"ncol"` 검사로 asc(`read_file_asc :456`) vs bin(`read_file_bin :506`) 자동 판별. bin 은 길이 검증으로 precision(float/double) 불일치 감지(`:540-543`).
- `write_grid` 오버로드(`:755`,`:802`,`:815`): netCDF/binary/ascii 동시 지원. netCDF 는 padding 제거 후 기록(`grid_cols==grid_cols_padded` 일 때만 직접, 아니면 tmp_grid 복사 `:824-834`); `call_gzip` 시 `system("gzip -9 -f ...")`(`:781-785`).
- `make_filename`(`:728`): `root-NNNN.ext` (SaveNumber 4자리 zero-pad, >9999 면 자유폭).
- `compare_grids`(`:866`,`:926`): RESULT_CHECK 디버그용 — 두 디렉토리 raster 를 16개 임계로 diff.

### 7.3 netCDF (lis2_output.cpp 의 NetCDF 부)

`StartNetCDF_impl`(`:134`): NC_NETCDF4/HDF5, time(unlimited)·y·x·y_edge·x_edge 차원, `LATLONGMODE` 시 lat/lon(`:191-225`). 모든 var deflate(level 1)+shuffle. `_NETCDF != 1` 빌드면 `StartNetCDF`(`:418-433`)가 경고만 출력하고 ascii fallback.

## 8. 정리: classic 대비 신규 워크플로 차이

| 측면 | classic (lisflood.cpp/sgc.cpp) | lisflood2/ |
|---|---|---|
| 자료배치 | `Arrptr` grid-per-field, 패딩 없음 | padded SoA flow/cell 리스트 |
| sub-grid | grid mask 전수 순회 | 압축 flow-pair 리스트 + wet/dry bound |
| 병렬 | per-field omp | 블록 분할 + first-touch NUMA + nowait/single 오버랩 |
| timestep | UpdateH 내부에서 CFL | `Fast_IterateLoop` single 절에서 CFL(`:4499`) |
| 출력 | `Arrptr` 직접 | padded→unpadded 변환, 채널깊이 합산, netCDF |
| 진입 | — | `Statesptr->SGC==ON` 에서만 (`lisflood.cpp:772`) |

> 주의: `Do_Update` 의 `_SGM_BY_BLOCKS` 분기에서 blocks 경로(`:3663-3667`)는 `j` 변수 미정의 등 빌드 조건부 코드 — 기본 rows 경로(`:3639-3646`)가 주 사용 경로로 보임 (단언 아님, `#if` 가드 관찰 기반).
