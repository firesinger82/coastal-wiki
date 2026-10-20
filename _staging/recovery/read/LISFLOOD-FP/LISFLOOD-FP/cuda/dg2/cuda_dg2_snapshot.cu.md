---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/dg2/cuda_dg2_snapshot.cu
lines: 90
sha256: 30c0e31b64554cf0b692959d17504e7af742dfcd50e4d2d284da36aa570f3293
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_dg2_snapshot.cu — 판독 구간 기록

구간은 1행부터 90행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | DG2 Snapshot 헤더를 포함한다(1). 전처리 조건 분기는 없다. 생성자는 cuda::Snapshot<Flow>에 공통 설정을 전달하고 DEM·U 참조를 저장한다(3–21). writer_elev·H/H1x/H1y·HU/HU1x/HU1y·HV/HV1x/HV1y·U/V의 std::future<void> 12개를 각각 `std::async(std::launch::async, []{})`를 인수로 초기화한다(22–33). 빈 작업의 비동기 실행(asynchronous execution)이다. |
| 36–63 | write는 H·H1x·H1y를 .wd·.wd1x·.wd1y로 write_async한다(38–40). `if (write_elevation)` (42)은 ElevationWriter(U.H, DEM._0)를 .elev로 쓴다(44). `if (write_discharge)` (47)은 HU의 0차·1x·1y를 .Qx·.Qx1x·.Qx1y로, HV를 .Qy·.Qy1x·.Qy1y로 쓴다(49–54). `if (write_velocity)` (57)은 DepthThresh를 받는 VelocityWriter로 .Vx·.Vy를 쓴다(59–60). 각 write_async의 outflag는 0이고 call_gzip을 전달한다. |
| 64–75 | write_maxes는 write_max로 U.initHtm을 .inittm, U.totalHtm을 .totaltm, U.maxH를 .max, U.maxHtm을 .maxtm을 기록하며 outflag는 0이다(66–69). 수위 최대값 비동기 기록의 대체 호출은 주석이다(72). 빈 줄과 함수 끝을 포함한다. |
| 76–90 | wait는 생성자에서 준비한 12개 writer에 각각 .wait()를 호출한다(78–89). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 76–90: wait는 각 future의 wait만 호출한다. 이 함수 본문에는 get 호출이 없다.
