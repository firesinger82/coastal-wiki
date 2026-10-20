---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/fv2/cuda_fv2_simulate.cu
lines: 192
sha256: 831a1297ced9c3eca3a1fbb323d91fb5bc9e0bcfab198571df6e11470edcee1f
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_fv2_simulate.cu — 판독 구간 기록

구간은 1행부터 192행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–47 | 헤더 포함과 run 선언(1–28). `if (verbose) print_device_info();` (29). 실행 격자는 `dim3 grid_size(128, 128);` (30), pitch·offset은 0(33–34). Topography에 nodata_elevation·states.acceleration을 전달한다(36–37). update_geometry 후 geometry·pitch를 `cuda::copy_to_symbol`로 복사한다(39–41). DeviceTopography를 initialise하고 `cuda::sync();` (46)를 호출한다. 조건부 전처리 지시는 없다. |
| 48–88 | 시작 시 20행 Simulation::run 안. `::DynamicRain<cuda::UnifiedAllocator<NUMERIC_TYPE>>` (48–49)을 구성하고 rain_geometry를 심벌에 복사한다(50). Flow를 고정 메모리(pinned memory)에 할당하고 initialise_H·initialise_discharge로 H/HU/HV를 초기화한다(52–57). manning·d_manning은 nullptr(59–60). `if (strlen(filenames.nfilename) > 0)` (61)이면 호스트·장치 고스트 래스터(ghost raster)를 할당하고 initialise_manning·GhostRaster::copy를 호출한다(63–67). PhysicalParams·SolverParams를 구성해 장치 심벌에 복사한다(70–76). load_boundaries·Boundary::initialise(79–80), `new Solver(U, d_DEM, d_manning, geometry, physical_params, pars.limit_slopes, grid_size)` (82–83), DynamicTimestep 구성(85–86), MinTstep=InitTstep 복사(87). |
| 89–110 | 시작 시 20행 run 안. StatsCollector는 DepthThresh·acceleration을 받는다(89). MaxField는 경로·격자·pitch·offset·grid_size·출력 정밀도를 받는다(90–91). Stats 구성·헤더 출력(93–94), Sampler 구성(96). `if (states.save_stages == ON)` (97)이면 표본 지점 적재·수심 파일 열기·DEM._0를 받는 헤더 쓰기를 실행한다(99–102). 그 안 `if (states.voutput_stage == ON)` (104)이면 유속 관측 파일과 헤더를 연다(106–107). |
| 111–131 | 시작 시 20행 run 안이며 97행 조건 밖. Snapshot 구성(111–113). `if (states.save_elev == ON)` (114)은 enable_elevation_writer(116), `if (states.voutput == ON)` (118)은 DepthThresh를 받는 enable_velocity_writer(120), `if (states.save_Qs == ON)` (122)는 enable_discharge_writer(124)를 호출한다. solve->d_U()의 Flow 참조를 받고(127), loop_start를 time으로 채운다(129–130). |
| 132–153 | 시작 시 20행 run 안. `while (solver.t < solver.Sim_Time)` (132). `if (rain.enabled())` (134)이면 rain.update_time(136) 뒤 `lis::cuda::DynamicRain::update<<<grid_size, CUDA_BLOCK_SIZE>>>(` (137), `d_DEM._0, d_U.H, rain.data());` (138)를 실행한다. 이후 순간 질량을 0으로 만들고 경계 시계열·점 유입원을 갱신하고 질량을 누적한다(140–145). solve->update_ghost_cells·dynamic_dt.update_dt(146–147), `solver.MinTstep = FMIN(solver.MinTstep, cuda::dt);` (148). `if (verbose)` (150)의 로그 뒤 `solver.t += cuda::dt;` (151), `solver.itCount++;` (152). |
| 154–176 | 시작 시 20행 run·132행 while 안. solve->update_flow_variables에 순간 질량을 넘기고 d_U를 갱신한다(154–155). `if (pars.drain_nodata)` (156)이면 `cuda::Boundary::drain_nodata_water(d_U.H, d_DEM._0, stats_collector.instantaneous_mass(), grid_size)` (158–159). 질량 누적·최대 수심 갱신(161–162). `if (stats.need_to_write(solver.t))` (164)이면 sampler.sample·solve->zero_ghost_cells·`cuda::sync();` (166–168), 통계 항목 작성·버퍼 출력(170–171). 이 조건 밖에서 snapshot.write_if_needed(d_U, solver.t, states.call_gzip)(174), while 종료(175). |
| 177–192 | 시작 시 20행 run 안이며 132행 while 밖. time으로 loop_end를 받고 `NUMERIC_TYPE seconds = difftime(loop_end, loop_start);` (179)를 출력한다(180). sampler.write·snapshot.wait·max_field.write(182–184). d_DEM.free_device, delete[] manning, cuda::free_device(d_manning), Flow::free_pinned(U), cuda::Boundary::free_device(boundaries)를 호출한다(186–190). run 종료와 빈 줄(191–192). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30: grid_size는 128×128로 고정한다.
- 52–57: 초기 Flow의 할당 뒤 이 파일에서 명시적으로 초기화하는 흐름 성분은 H·HU·HV이다. H1x·H1y·HU1x·HU1y·HV1x·HV1y 초기화 호출은 이 구간에 없다.
- 132–151: 동적 강우 커널 호출은 dynamic_dt.update_dt보다 앞에 있다. 이 호출 순서는 원문에서 확인되며 사용 시간 간격의 적합성은 판단하지 않았다.
