---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_sample.cu
lines: 333
sha256: 0611a51c9d7b72a74efbea07f8ccd36ef12bec4f36ae67822d59660ed2998a69
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_sample.cu — 판독 구간 기록

구간은 1행부터 333행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–47 | sample·util·fv1/acc의 flow·solver 헤더(1–6), lis::cuda 이름 공간(namespace)(8–11). `__global__ void sample` (13)는 시간 복사(22), `for (int i=0; i<cuda::sample_points.count; i++)` (24), `int buf_offset = cuda::sample_buf_idx*cuda::sample_points.count;` (26). `if (cuda::sample_points.inside_domain[i])` (28)는 Hval 복사·표본 버퍼(sample buffer)에 수심 저장(30–31), 내부 `if (Hval > cuda::solver_params.DepthThresh)` (33)에서 HUval·HVval 복사(35–36). 속력식은 `NUMERIC_TYPE speed = SQRT(HUval/Hval * HUval/Hval` (38), `+ HVval/Hval * HVval/Hval);` (39). 속력 저장(40), 반복 종료 후 cuda::sample_buf_idx 증가(45). 전처리 조건 분기는 없다. |
| 48–88 | 시작 시 8–11행 lis::cuda 이름 공간 안. `__global__ void sample_ACC` (48)는 시간 저장(57), `for (int i = 0; i < cuda::sample_points.count; i++)` (59), `int buf_offset = cuda::sample_buf_idx * cuda::sample_points.count;` (61). `if (cuda::sample_points.inside_domain[i])` (63)에서 수심 저장(65–66), `if (Hval > cuda::solver_params.DepthThresh)` (68)에서 idx_Qx1·idx_Qx2·idx_Qy1·idx_Qy2의 네 속도 복사(70–73). 속력식은 `NUMERIC_TYPE speed = SQRT(getmax(FABS(Vxval1), FABS(Vxval2)) * getmax(FABS(Vxval1), FABS(Vxval2))` (75), `+ getmax(FABS(Vyval1), FABS(Vyval2)) * getmax(FABS(Vyval1), FABS(Vyval2)));` (76). 속력 저장(77), cuda::sample_buf_idx 증가(82), 함수·이름 공간 종료와 빈 줄(83–88). |
| 89–120 | Sampler 생성자(constructor)는 d_sample_points·sample_buf_idx·verbose를 받는다(89–94). 두 참조·verbose를 저장하고 stage_file·gauge_file에 sample_points를 전달한다(95–101). load_sample_points(103–109)는 lis::Sample::initialise에 파일명·geometry·pitch·offset·verbose 전달(111–112), initialise_sample_points(113), 호스트 고정 메모리(pinned memory)와 장치 버퍼 할당(115–116), active=true(118). |
| 121–163 | open_stage_file(121–129)는 stage_file.open(filename, checkpoint, t)(128). open_gauge_file(131–141)는 gauge_file.open(138), write_speed=true(140). write_stage_header(143–152)는 stage_file.write_header(DEM, sample_points_filename, checkpoint, t)(151). write_gauge_header(154–162)는 gauge_file.write_header(DEM, sample_points_filename, t)(161). 각 선언·빈 줄 포함. |
| 164–197 | Sampler::sample(164–173)의 호출 조건과 커널(kernel) 호출은 `if (active) lis::cuda::sample<<<1, 1>>>(H, HU, HV, d_sample_buf, t);` (172). Sampler::sample_ACC(175–184)는 `if (active) lis::cuda::sample_ACC << <1, 1 >> > (H, Vx, Vy, d_sample_buf, t);` (183). write_if_buffer_full(186)의 `if (active && buffer_full())` (188)에서 `if (verbose == ON) printf("SampleBuffer full: flushing to disk\n");` (190), copy_buffer(191), stage_file.write(192), `if (write_speed) gauge_file.write(sample_buf, sample_buf_idx);` (193), sample_buf_idx=0(194). |
| 198–225 | Sampler::write(198)는 `if (active)` (200)에서 `if (verbose == ON) printf("Flushing SampleBuffer to disk\n");` (202), copy_buffer(203), stage_file.write(204), `if (write_speed) gauge_file.write(sample_buf, sample_buf_idx);` (205). buffer_full(209)는 `return sample_buf_idx == sample_buf.size;` (211). copy_buffer(214)는 dst=sample_buf·src=d_sample_buf 참조(216–217), time은 sample_buf_idx*sizeof(NUMERIC_TYPE)(219), H·speed는 sample_buf_idx*sample_points.count*sizeof(NUMERIC_TYPE) 바이트를 cuda::copy한다(220–223). |
| 226–256 | initialise_sample_points는 d_sample_points·sample_points를 d_dst·h_src로 참조(228–229), temp와 count 설정(231–232). x·y·idx·idx_Qx1·idx_Qx2·idx_Qy1·idx_Qy2·inside_domain 장치 배열 할당(234–243), 대응 호스트 배열을 cuda::copy(245–252), copy_to_symbol(d_dst, &temp, sizeof(SamplePoints))(254). |
| 257–303 | Sampler::free(SamplePoints&)는 x·y·idx·네 면 인덱스·inside_domain을 cuda::free_device로 해제(262–269). allocate_pinned(272–277)는 buf.size=size(279), NUMERIC_TYPE time을 size개(280–281), H·speed를 size*points개씩 malloc_pinned로 할당(282–285). allocate_device(288–293)는 buf.size=size(295), 같은 크기 배열을 malloc_device로 할당(296–301). |
| 304–333 | free_pinned(SampleBuffer&)(304–312)는 time·H·speed의 고정 호스트 메모리 해제(309–311). free_device(SampleBuffer&)(314–322)는 같은 장치 배열 해제(319–321). 소멸자(destructor)(324)의 `if (active)` (326)에서 lis::Sample::free(sample_points)(328), free(d_sample_points)(329), free_pinned(sample_buf)(330), free_device(d_sample_buf)(331). 함수 종료(333). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28–40·63–77: 영역 밖 표본의 H·speed는 두 커널에서 대입하지 않는다. 영역 안이더라도 Hval<=DepthThresh이면 speed 대입은 없다.
- 280–301: 버퍼 할당 함수에는 time·H·speed 배열의 값 초기화 문장이 없다.
- 188–211: write_if_buffer_full은 출력 후 sample_buf_idx를 0으로 설정한다. write는 출력 후 인덱스를 변경하지 않는다. buffer_full은 크기와의 동등 비교만 반환한다.
