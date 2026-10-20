---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/PointSources.h
lines: 211
sha256: 879b698fc576d684c6ae616ef1b44f4fe18bf4e9958468642dbd28aec5ebab38
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# PointSources.h — 판독 구간 기록

구간은 1행부터 211행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | `#pragma once` (1), cuda_utils·표준 입출력·메모리·문자열·MortonCode·InletTypes·lisflood 헤더 포함(3–9), `lis::cuda::acc_nugrid` 이름공간(namespace)(11–16). SourceAndRow 구조체(struct)는 NUMERIC_TYPE src·int row를 갖는다(18–23). 점 유입원(point source) 구조체 PointSources(25–26)는 호스트(host)·장치(device)의 Morton 코드(Morton code) 포인터 h_codes·d_codes(27–28), 유입값 포인터 h_srcs·d_srcs(29–30), num_srcs와 유형 포인터 h_src_types·d_src_types(31–33), timeseries·rows 포인터(34–35), `bool        is_copy = false;` (36)를 보유한다. 이 파일의 모든 구간에는 `#if` 계열 전처리 조건 분기가 없다. |
| 38–57 | 시작 시 25행 PointSources 구조체 안. 생성자(constructor)는 num_srcs를 받는다(38–39). `size_t bytes_codes = sizeof(MortonCode) * num_srcs;` (40), `size_t bytes_srcs = sizeof(NUMERIC_TYPE) * num_srcs;` (41), `size_t bytes_src_types = sizeof(int) * num_srcs;` (42). `h_codes = (num_srcs > 0) ? new MortonCode[num_srcs] : nullptr;` (44), `d_codes = (num_srcs > 0) ? (MortonCode*)malloc_device(bytes_codes) : nullptr;` (45), `h_srcs = (num_srcs > 0) ? new NUMERIC_TYPE[num_srcs]() : nullptr;` (46), `d_srcs = (num_srcs > 0) ? (NUMERIC_TYPE*)malloc_device(bytes_srcs) : nullptr;` (47), `h_src_types = (num_srcs > 0) ? new int[num_srcs] : nullptr;` (48), `d_src_types = (num_srcs > 0) ? (int*)malloc_device(bytes_src_types) : nullptr;` (49), `timeseries = (num_srcs > 0) ? new char[num_srcs * 32]() : nullptr;` (50), `rows = (num_srcs > 0) ? new int[num_srcs]() : nullptr;` (51). this->num_srcs에 인수 복사(53). 복사 생성자(copy constructor) `PointSources(const PointSources& original) { *this = original; is_copy = true; }` (56). |
| 58–71 | 시작 시 25행 구조체 안. 소멸자(destructor)(58–59)의 `if (!is_copy)` (60) 안에서 `if (h_codes != nullptr) delete[] h_codes;` (62), `if (h_srcs != nullptr) delete[] h_srcs;` (63), `if (h_src_types != nullptr) delete[] h_src_types;` (64), `if (h_codes != nullptr) free_device(d_codes);` (66), `if (d_srcs != nullptr) free_device(d_srcs);` (67), `if (d_src_types != nullptr) free_device(d_src_types);` (68). 블록 종료와 빈 줄(69–71). |
| 72–109 | 시작 시 25행 구조체 안. update_source의 선언에는 TOREMOVE 주석이 있다(72). 인수는 srcfilename·time_now·row_in·src_type·timeseries(73–80). `if (src_type != HVAR && src_type != QVAR) return { C(0.0), 0 };` (81). str[255]·널 초기화한 buf[32](83–84), fopen(srcfilename, "r")(86). `if (NULL == fp)` (88)는 오류 출력·exit(-1)(90–91). num_char_timeseries=0(94), `while ( *(timeseries + num_char_timeseries) != '\0' ) num_char_timeseries++;` (96). `while ( strncmp(buf, timeseries, num_char_timeseries) )` (98)의 `if ( NULL == fgets(str, sizeof(str), fp) )` (100)는 오류 출력·fclose·exit(-1)(102–104), `sscanf(str, "%s", buf);` (107)로 이름을 읽는다. 루프 종료와 빈 줄(108–109). |
| 110–134 | 시작 시 25행 구조체·72행 update_source 안. src·src_1·src_2·t_1·t_2는 C(0.0)(110–115), row=row_in(117), num_rows_timeseries=0·time_multiplier=1(118–119). fgets(121), `sscanf(str, "%d %s", &num_rows_timeseries, buf);` (123). `time_multiplier = ( !strncmp(buf, "seconds", 7) ) ? 1 : ( strncmp(buf, "minutes", 7) ) ? 60 : 3600;` (125). `for (int i = 0; i < row + 1; i++) fgets(str, sizeof(str), fp);` (127). `sscanf(str, "%" NUM_FMT " %" NUM_FMT, &src_1, &t_1);` (129), fgets(131), `sscanf(str, "%" NUM_FMT " %" NUM_FMT, &src_2, &t_2);` (133). NUM_FMT의 정의값은 이 파일에 없다. |
| 135–166 | 시작 시 25행 구조체·72행 update_source 안. `if (time_now > t_2)` (135)에서 `row++;` (137). `if (row + 1 == num_rows_timeseries)` (139)는 시뮬레이션 시각 초과 오류 출력(141–146), fclose·exit(-1)(148–149). 내부 조건 밖에서 t_1=t_2·src_1=src_2(152–153), fgets(155), `sscanf(str, "%" NUM_FMT " %" NUM_FMT, &src_2, &t_2);` (157). 바깥 조건 종료·fclose(158–160). `src = src_1 + (src_2 - src_1) / ( (t_2 - t_1) * time_multiplier ) * (time_now - t_1);` (162), src·row 집합 반환(164). 루틴 종료와 빈 줄(165–166). |
| 167–203 | 시작 시 25행 구조체 안. update_all_sources는 input_filename·time_now·BoundCs& h_src를 받는다(167–173). `for (int i = 0; i < this->num_srcs; i++)` (174)에서 src_type=h_src_types[i](177). row_in·timeseries 취득과 update_source 호출은 주석(176·178·180–187). `if (src_type == HVAR \|\| src_type == QVAR)` (189)에서 `this->h_srcs[i] = InterpolateTimeSeries(h_src.PS_TimeSeries[i], time_now);` (193). src_and_row의 값·행 복사는 주석(191–192). 배열 크기 계산과 copy_cuda도 주석(198·200). 실제 복사는 `cudaError_t error = cudaMemcpy(d_srcs, h_srcs, sizeof(NUMERIC_TYPE) * this->num_srcs, cudaMemcpyDefault);` (201). 루틴 종료와 빈 줄(202–203). |
| 204–211 | 시작 시 25행 구조체 안. `__device__ __forceinline__` (204)의 `NUMERIC_TYPE q_src(const NUMERIC_TYPE& dt, const NUMERIC_TYPE& dx, const int idx) { return this->d_srcs[idx] * dt / dx; }` (205)는 장치 유입값에 dt/dx를 곱해 반환한다. 구조체·이름공간 종료와 빈 줄(206–211). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 50–51·58–70: 생성자는 timeseries·rows에 new[]를 사용한다. 소멸자에는 두 배열의 delete[]가 없다.
- 62·66: d_codes의 free_device 호출 조건은 d_codes가 아닌 h_codes의 nullptr 비교다. 이 비교는 h_codes의 delete[] 뒤에 있다.
- 125: seconds 비교에는 부정 연산자 !가 있고 minutes 비교에는 없다. 따라서 seconds가 아니고 minutes가 일치하면 배수는 3600이며, 두 문자열 모두 일치하지 않으면 배수는 60이다.
- 96–107·121–133·155–157: 이름 비교 길이는 요청 문자열 길이다. %s에는 폭 지정이 없다. 해당 sscanf의 반환 개수와 121·127·131·155행 fgets의 반환값 검사는 없다.
- 135–162: 시각 비교는 time_now와 배수 적용 전 t_2 사이에서 수행한다. 보간식은 분모의 시간 차에 time_multiplier를 곱하며, 마지막 차는 time_now−t_1이다. row 증가는 단일 if에서 한 번 수행한다.
- 167–201: update_all_sources의 input_filename은 활성 본문에서 사용되지 않는다. update_source 호출은 주석이고 실제 값 갱신은 InterpolateTimeSeries를 호출한다. cudaMemcpy 반환값 error는 이후 검사하지 않는다.
