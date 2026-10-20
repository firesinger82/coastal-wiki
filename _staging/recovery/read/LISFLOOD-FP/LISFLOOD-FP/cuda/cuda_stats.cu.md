---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_stats.cu
lines: 166
sha256: 8a81a03eee9cdc0aeeb8558efd269a1da2eb199780a2200cbd46d21e73a6a910
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_stats.cu — 판독 구간 기록

구간은 1행부터 166행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | stats·solver·util·CUB·limits 헤더와 lis::cuda 이름공간(namespace)이다(1–10). 전처리 조건 분기는 없다. 질량 누적 커널(kernel)은 `__global__ void accumulate_mass` (12)이다. `cumulative->in += instantaneous->in * cuda::dt;` (18), `cumulative->out += instantaneous->out * cuda::dt;` (19)로 시간 적분한다. 이름공간 끝과 빈 줄을 포함한다(22–24). |
| 25–66 | StatsCollector 생성자의 격자 원소 수는 `elements((acceleration == 0) ? lis::GhostRaster::elements(geometry) : lis::GhostRaster::elements_H(geometry))` (33)이다. 작업 포인터를 nullptr로 초기화한다(35–39). 히스토그램(histogram) 경계 메모리는 `histogram_levels = static_cast<NUMERIC_TYPE*>(` (41), `malloc_unified(3*sizeof(NUMERIC_TYPE)));` (42)이다. 경계값은 `histogram_levels[0] = C(0.0);` (44), `histogram_levels[1] = DepthThresh;` (45), `histogram_levels[2] = std::numeric_limits<NUMERIC_TYPE>::max();` (46)이다. 개수 메모리는 `histogram_counts = static_cast<int*>(malloc_unified(2*sizeof(int)));` (48)이다. cub::DeviceHistogram::HistogramRange와 cub::DeviceReduce::Sum을 nullptr 입력으로 호출해 메모리 크기를 얻고 각 작업 영역을 malloc_device로 할당한다(50–56). 단일 d_volume·두 MassStats 장치 메모리를 할당하고 zero_cumulative_mass를 호출한다(58–64). |
| 67–85 | zero_instantaneous_mass는 값 초기화(value initialization)된 MassStats를 cuda::copy로 장치에 복사한다(67–71). instantaneous_mass는 해당 장치 포인터를 반환한다(73–76). accumulate_mass는 `lis::cuda::accumulate_mass<<<1, 1>>>(d_cumulative_mass,` (80), `d_instantaneous_mass);` (81)로 한 스레드 커널을 실행하고 cuda::sync를 호출한다(82). 누적 시간은 `cumulative_time += cuda::dt;` (83)이다. |
| 86–121 | create_entry는 `NUMERIC_TYPE current_volume = volume(H);` (92), `NUMERIC_TYPE volume_change = current_volume - previous_volume;` (93)로 체적(volume) 변화를 계산하고 previous_volume을 갱신한다(94). 순간·누적 MassStats를 호스트(host)로 복사한다(96–100). 누적 시간을 보존하고 `NUMERIC_TYPE net_source_flux =` (104), `h_cumulative_mass.in - h_cumulative_mass.out;` (105)를 계산한다. zero_cumulative_mass 호출 후 StatsEntry를 반환한다(107–119). 반환 항목은 t·dt·itCount·MinTstep·area(H)·current_volume·순간 통계이며, 질량 오차는 `net_source_flux - volume_change,` (117), 오차율은 `(net_source_flux - volume_change)/time` (118)이다. |
| 122–143 | 소멸자(destructor)는 히스토그램 경계·개수를 free_unified로, 두 작업 영역·d_volume·두 MassStats를 free_device로 해제한다(122–131). area는 cub::DeviceHistogram::HistogramRange에 H·3개 경계·elements를 전달하고 동기화한다(138–140). 젖은 면적은 `return histogram_counts[1] * geometry.dx * geometry.dy;` (141)이다. |
| 144–166 | volume은 cub::DeviceReduce::Sum으로 H의 합을 d_volume에 저장하고 cuda::copy로 h_volume을 받는다(150–155). `return h_volume * geometry.dx * geometry.dy;` (157)로 체적을 반환한다. zero_cumulative_mass는 값 초기화된 MassStats를 누적 메모리에 복사하고(162–163), `cumulative_time = C(0.0);` (165)으로 시간을 초기화한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 58–64·67–71: 생성자는 d_instantaneous_mass를 할당한다. 생성자 본문에는 zero_instantaneous_mass 호출이 없다.
- 102–118: create_entry는 누적 시간으로 나눈 값을 반환한다. 이 함수 본문에는 time이 0인지 검사하는 조건이 없다.
