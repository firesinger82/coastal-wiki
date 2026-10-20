---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/dg2/cuda_dg2_simulate.cu
lines: 248
sha256: 2ec5813375bf45a97f4fcae3171196fa0be22056ec9503e0e431bd0f39c8b0da
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_dg2_simulate.cu — 판독 구간 기록

구간은 1행부터 248행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | 공통 CUDA·DG2·최대장·강우·통계·통합 할당기와 rain·입출력·cstdio·ctime·Rainfall_uniform 헤더를 포함한다(1–19). 파일 내부 전처리 조건 분기는 없다. 뒤의 빈 줄도 포함한다(20–21). |
| 22–60 | Simulation::run의 `if (verbose) print_device_info();` (31)로 장치 정보를 출력한다. 커널 격자(kernel grid)는 `dim3 grid_size(128, 128);` (32), pitch·offset 초기값은 0이다(35–36). Topography를 읽고 update_geometry, cuda::copy_to_symbol의 geometry·pitch 복사, d_DEM.initialise, cuda::sync를 호출한다(38–48). `::DynamicRain<cuda::UnifiedAllocator<NUMERIC_TYPE>> rain(` (50), `filenames.dynamicrainfilename, verbose);` (51)으로 동적 강우(dynamic rain)를 만들고 rain_geometry를 복사한다(52). Flow::allocate_pinned 후 initialise_H·initialise_discharge를 호출한다(54–59). |
| 61–100 | 시작 시 22행 run 안이다. 두 Manning 포인터를 nullptr로 초기화한다(61–62). `if (strlen(filenames.nfilename) > 0)` (63) 안에서 호스트(host)·장치 배열을 할당하고 initialise_manning·GhostRaster::copy를 호출한다(65–69). 물리·수치 매개변수를 만들어 cuda::copy_to_symbol로 복사한다(72–78). 균일 강우(uniform rain) 초기값은 `Rainfall_uniform   rainfall_uniform(C(0.0));` (80)이다. load_boundaries·cuda::Boundary::initialise(82–85), Solver 생성(87–88), DynamicTimestep 생성과 MinTstep=InitTstep(90–92), StatsCollector·MaxField·Stats 생성과 통계 머리말 기록을 수행한다(94–99). |
| 101–136 | 시작 시 22행 run 안이다. Sampler 생성 뒤 `if (states.save_stages == ON)` (102) 안에서 표본점(sample point)을 읽고 수위 파일·머리말을 연다(104–107). 그 안의 `if (states.voutput_stage == ON)` (109)은 계측(gauge) 파일·머리말을 연다(111–112). Snapshot 생성(116–118) 후 독립 조건 `if (states.save_elev == ON)` (119), `if (states.voutput == ON)` (123), `if (states.save_Qs == ON)` (127)에 따라 수위·유속·유량 기록을 켠다(121·125·129). 장치 상태 참조를 받고 루프 시작 시간을 기록한다(132–135). |
| 137–163 | 시작 시 22행 run 안이다. `while (solver.t < solver.Sim_Time)` (137)의 반복에서 `if (rain.enabled())` (140)이면 강우 시각을 갱신하고 `lis::cuda::DynamicRain::update<<<grid_size, CUDA_BLOCK_SIZE>>>(` (143), `d_DEM._0, d_U.H, rain.data());` (144)를 실행한다. 독립 `if (states.rainfall == ON) {` (147)는 rainfall_uniform.update_rainfall과 solve->update_uniform_rain을 호출한다(149–151). 순간 통계를 0으로 만들고 경계 시계열(time series)·점 원천(point source)을 갱신한다(154–157). 통계 누적·순간 통계 초기화·가상 셀(ghost cell) 갱신·시간 간격 갱신을 호출한다(158–161). `solver.MinTstep = FMIN(solver.MinTstep, cuda::dt);` (162)이다. |
| 164–190 | 시작 시 22행 run·137행 while 안이다. `if (verbose) printf("t=%f\tdt=%f\n", solver.t, cuda::dt);` (164), `solver.t += cuda::dt;` (165), `solver.itCount++;` (166)를 수행한다. update_flow_variables의 반환 상태를 d_U에 대입한다(168–169). `if (pars.drain_nodata)` (170)이면 cuda::Boundary::drain_nodata_water를 호출한다(172–173). 통계 누적과 최대장(maximum field) 갱신을 수행한다(175–176). `if (stats.need_to_write(solver.t))` (178) 안에서 sampler.sample·zero_ghost_cells·cuda::sync·stats.write(create_entry(...))·write_if_buffer_full을 호출한다(180–185). 이 조건 밖에서 snapshot.write_if_needed를 호출한다(188). while이 끝난다(189). |
| 191–206 | 시작 시 22행 run 안이며 137행 while 밖이다. 종료 시간을 얻고 `NUMERIC_TYPE seconds = difftime(loop_end, loop_start);` (193)를 출력한다(194). sampler.write·snapshot.wait·max_field.write를 호출한다(196–198). d_DEM.free_device, delete[] manning, cuda::free_device(d_manning), Flow::free_pinned(U), cuda::Boundary::free_device(boundaries)를 호출하고 run을 닫는다(200–205). |
| 207–231 | initialise_H의 `if (states.startfile == ON)` (221) 안에서 cuda::Simulation::initialise_H로 평균 수심을 읽고(223–224), initialise_H_slope를 "1x"·"1y" 접미사로 각각 호출한다(225–228). 조건 밖의 추가 초기화 문장은 없다. |
| 232–248 | initialise_H_slope는 `char h_slope[256];` (243)에 strcpy·strcat으로 파일명과 접미사를 결합한다(244–245). StartFile::load로 array에 읽는다(247). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 154–161·175: 한 while 반복에서 stats_collector.accumulate_mass를 두 번 호출한다. 첫 호출은 dynamic_dt.update_dt보다 앞에 있다.
- 137·165: 반복 조건은 t<Sim_Time이다. 이 루프에는 dt를 Sim_Time-t로 제한하는 문장이 없다.
- 207–230: initialise_H에는 startfile==ON 분기만 있다. 이 함수는 startfile 조건이 거짓일 때 H·H1x·H1y에 대입하지 않는다.
- 243–245: h_slope의 크기는 256이다. strcpy·strcat 앞에 길이 검사 조건이 없다.
