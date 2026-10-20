---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/fv1/cuda_fv1_simulate.cu
lines: 209
sha256: bf1e75589e3748b85974786a8b397e2c85aa1f1a237b1ecdde43faffebcb0afa
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_fv1_simulate.cu — 판독 구간 기록

구간은 1행부터 209행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 공통 CUDA·FV1 흐름/실행/스냅샷/solver·강우·최대장·통계·통합 할당기·rain·입출력·cstdio·ctime·Rainfall_uniform 헤더를 포함한다(1–16). 전처리 조건 분기는 없다. 빈 줄을 포함한다(17). |
| 18–56 | Simulation::run은 `if (verbose) print_device_info();` (27)와 `dim3 grid_size(128, 128);` (28)로 시작한다. pitch·offset은 0이다(31–32). Topography::load·clamp_boundary_values와 update_geometry를 호출한 뒤 cuda::copy_to_symbol로 geometry·pitch를 복사한다(34–40). GhostRaster::allocate_device·copy로 장치 지형을 만들고 Zstar_x/y도 할당·초기화한다(42–49). 동기화 후 `::DynamicRain<cuda::UnifiedAllocator<NUMERIC_TYPE>> rain(` (53), `filenames.dynamicrainfilename, verbose);` (54)으로 동적 강우(dynamic rain)를 만들고 rain_geometry를 복사한다(55). |
| 57–103 | 시작 시 18행 run 안이다. Flow::allocate_pinned 후 initialise_H·initialise_discharge를 호출한다(57–62). Manning 포인터는 nullptr이며 `if (strlen(filenames.nfilename) > 0)` (66)일 때 호스트(host)·장치 배열을 할당하고 initialise_manning·GhostRaster::copy를 호출한다(68–72). PhysicalParams·SolverParams를 만들어 cuda::copy_to_symbol로 복사한다(75–81). 균일 강우(uniform rain)는 `Rainfall_uniform   rainfall_uniform(C(0.0));` (83)이다. load_boundaries·Boundary::initialise(85–87), Solver·DynamicTimestep 생성과 MinTstep=InitTstep(89–95), StatsCollector·MaxField·Stats 생성과 머리말 기록을 수행한다(97–102). |
| 104–139 | 시작 시 18행 run 안이다. Sampler를 만든 뒤 `if (states.save_stages == ON)` (105) 안에서 표본점(sample point)과 수위 파일·머리말을 준비한다(107–110). 내부 `if (states.voutput_stage == ON)` (112)은 계측(gauge) 파일·머리말을 준비한다(114–115). Snapshot 생성(119–121) 후 독립 `if (states.save_elev == ON)` (122), `if (states.voutput == ON)` (126), `if (states.save_Qs == ON)` (130)에 따라 수위·유속·유량 기록을 켠다(124·128·132). 장치 상태 참조와 시작 시각을 얻는다(135–138). |
| 140–164 | 시작 시 18행 run 안이다. `while (solver.t < solver.Sim_Time)` (140)의 `if (rain.enabled())` (142)은 강우 시각을 갱신하고 `lis::cuda::DynamicRain::update<<<grid_size, CUDA_BLOCK_SIZE>>>(` (145), `d_DEM, d_U.H, rain.data());` (146)를 실행한다. `if (states.rainfall == ON) {` (149)은 rainfall_uniform.update_rainfall·solve->update_uniform_rain을 호출한다(151–152). 순간 통계 초기화·경계 시계열(time series)·점 원천(point source) 갱신 뒤 질량을 누적한다(155–159). 순간 통계를 다시 초기화하고 가상 셀(ghost cell)·시간 간격을 갱신한다(160–162). `solver.MinTstep = FMIN(solver.MinTstep, cuda::dt);` (163)이다. |
| 165–191 | 시작 시 18행 run·140행 while 안이다. `if (verbose) printf("t=%f\tdt=%f\n", solver.t, cuda::dt);` (165), `solver.t += cuda::dt;` (166), `solver.itCount++;` (167)를 수행한다. update_flow_variables의 반환 상태를 d_U에 저장한다(169–170). `if (pars.drain_nodata)` (171)이면 Boundary::drain_nodata_water를 호출한다(173–174). 질량 누적과 최대장(maximum field) 갱신을 한다(176–177). `if (stats.need_to_write(solver.t))` (179) 안에서 sampler.sample·zero_ghost_cells·cuda::sync·stats.write(create_entry(...))·write_if_buffer_full을 호출한다(181–186). 이 조건 밖 snapshot.write_if_needed를 호출하고 while을 닫는다(189–190). |
| 192–209 | 시작 시 18행 run 안이며 140행 while 밖이다. 종료 시간을 얻고 `NUMERIC_TYPE seconds = difftime(loop_end, loop_start);` (194)를 출력한다(195). sampler.write·snapshot.wait·max_field.write를 호출한다(197–199). 호스트 DEM·manning을 delete[]로, 장치 DEM·manning·Zstar_x·Zstar_y를 cuda::free_device로 해제한다(201–206). Flow::free_pinned와 Boundary::free_device 호출 후 함수를 닫는다(207–209). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 155–162·176: 한 while 반복에서 accumulate_mass를 두 번 호출한다. 첫 호출은 dynamic_dt.update_dt보다 앞에 있다.
- 140·166: 반복 조건은 t<Sim_Time이다. 이 루프에는 dt를 Sim_Time-t로 제한하는 문장이 없다.
