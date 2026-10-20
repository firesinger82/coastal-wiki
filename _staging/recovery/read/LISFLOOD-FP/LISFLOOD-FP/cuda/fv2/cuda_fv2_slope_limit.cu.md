---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/fv2/cuda_fv2_slope_limit.cu
lines: 269
sha256: b779a806732de8cc597b660d2f71468d446d9ecfda436c59d0a238a293ea8848
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_fv2_slope_limit.cu — 판독 구간 기록

구간은 1행부터 269행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–46 | 헤더 포함(1–6). `__device__` (8) Stencil::limit는 mesh_delta와 stencil_minH를 받는다(9–13). `if (stencil_minH <= C(0.09)) return C(0.0);` (15). 네 이웃 값 함수를 호출하고(17–20), `NUMERIC_TYPE b_jump = l_pos - b_neg;` (22), `NUMERIC_TYPE f_jump = l_neg - f_pos;` (23). `if (FABS(b_jump) <= C(0.0))` (27)이면 r=0(29), else(31)는 `r = f_jump / b_jump;` (33). `NUMERIC_TYPE beta = C(1.25);` (36), `NUMERIC_TYPE phi = FMAX(C(0.0), FMAX(FMIN(beta * r, C(1.0)), FMIN(r, beta)));` (38), `NUMERIC_TYPE limiter = phi * b_jump;` (40)를 반환한다(42). 조건부 전처리 지시는 없다. |
| 47–96 | `__device__` (47)의 minH_x는 i−1·i·i+1의 수심을 읽고 `return FMIN(backward0, FMIN(local0, forward0));` (59). `__device__` (62)의 minH_y는 j+1·j·j−1의 수심으로 같은 식 `return FMIN(backward0, FMIN(local0, forward0));` (74). `__device__ NUMERIC_TYPE lis::cuda::fv2::Stencil::backward_neg()` (77)는 backward_const, `__device__ NUMERIC_TYPE lis::cuda::fv2::Stencil::local_pos()` (82)와 `__device__ NUMERIC_TYPE lis::cuda::fv2::Stencil::local_neg()` (87)는 local_const, `__device__ NUMERIC_TYPE lis::cuda::fv2::Stencil::forward_pos()` (92)는 forward_const를 반환한다(79·84·89·94). |
| 97–116 | `__device__` (97)의 ETA_stencil_x는 `return` (106), `{` (107), `DEM[j * cuda::pitch + i - 1] + H[j * cuda::pitch + i - 1],` (108), `0.0, //ETA1x[j * cuda::pitch + i - 1],` (109), `DEM[j * cuda::pitch + i] + H[j * cuda::pitch + i],` (110), `0.0, //ETA1x[j * cuda::pitch + i],` (111), `DEM[j * cuda::pitch + i + 1] + H[j * cuda::pitch + i + 1],` (112), `0.0 //ETA1x[j * cuda::pitch + i + 1]` (113), `};` (114). 이웃·현재 수위 세 값과 0 기울기 세 값을 교대로 반환한다. |
| 117–154 | `__device__` (117)의 HU_stencil_x는 i−1·i·i+1 HU를 세 상수 필드에 넣고 기울기 필드에는 각각 0.0을 반환한다(125–133). `__device__` (136)의 HV_stencil_x도 같은 위치의 HV와 세 0.0을 반환한다(144–152). 원래 HU1x·HV1x 참조는 각 0.0 뒤에 주석으로 남아 있다(128·130·132·147·149·151). |
| 155–174 | `__device__` (155)의 ETA_stencil_y는 `return` (164), `{` (165), `DEM[(j + 1) * cuda::pitch + i] + H[(j + 1) * cuda::pitch + i],` (166), `0.0, //ETA1y[(j + 1) * cuda::pitch + i],` (167), `DEM[j * cuda::pitch + i] + H[j * cuda::pitch + i],` (168), `0.0, //ETA1y[j * cuda::pitch + i],` (169), `DEM[(j - 1) * cuda::pitch + i] + H[(j - 1) * cuda::pitch + i],` (170), `0.0, //ETA1y[(j - 1) * cuda::pitch + i]` (171), `};` (172)를 반환한다. |
| 175–212 | `__device__` (175)의 HU_stencil_y는 j+1·j·j−1 HU와 세 0.0 기울기를 반환한다(183–191). `__device__` (194)의 HV_stencil_y도 j+1·j·j−1 HV와 세 0.0 기울기를 반환한다(202–210). HU1y·HV1y 참조는 주석이다(186·188·190·205·207·209). |
| 213–239 | Slopes::allocate_device는 ETA1x·ETA1y·HU1x·HU1y·HV1x·HV1y를 `cuda::GhostRaster::allocate_device(geometry)`로 각각 할당한다(219–224). Slopes::free_device는 여섯 필드에 `cuda::free_device`를 각각 호출한다(232–237). |
| 240–269 | MaxH 생성자는 `elements(lis::GhostRaster::elements(geometry))` (245)로 요소 수를 받고 temp·dummy_in·dummy_out을 nullptr로 초기화한다(247–249). `checkCudaErrors(cub::DeviceReduce::Max(temp, bytes, dummy_in, dummy_out, elements));` (251–252)로 임시 공간 크기를 받은 뒤 `malloc_device(bytes)` (254)를 호출한다. update는 `checkCudaErrors(cub::DeviceReduce::Max(temp, bytes, flow.H, &(cuda::fv2::maxH), elements));` (262–263)로 최대 수심을 환산 없이 저장한다. 소멸자는 `free_device(temp)` (268)를 호출한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11·15–42: limit는 mesh_delta를 인수로 받지만 실행식에서 참조하지 않는다.
- 15·36: 최소 수심 임계값 C(0.09)와 beta=C(1.25)를 함수 안에 직접 적는다.
- 77–94·108–113·127–132·146–151·166–171·185–190·204–209: Stencil의 네 평가 함수는 상수 필드만 반환한다. 여섯 스텐실(stencil) 생성 함수는 기울기 필드를 모두 0.0으로 채운다.
