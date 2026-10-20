---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/fv2/cuda_fv2_snapshot.cu
lines: 72
sha256: b82e828aeabb0582adbdf7a920d3b7e9109c5e10c7104c6206be755365d3952e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_fv2_snapshot.cu — 판독 구간 기록

구간은 1행부터 72행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | 헤더 포함(1)과 스냅숏(snapshot) 생성자(3–28). `cuda::Snapshot<Flow>(resrootname, interval, next_save, counter, U, geometry, pitch, offset, verbose, precision)` (18–19)에 공통 인수를 넘기고 DEM·U 참조를 보관한다(20–21). 여섯 future를 각각 `std::async(std::launch::async, []{})` (22–27)로 초기화한다. 조건부 전처리 지시는 없다. |
| 30–51 | write는 `write_async(U.H, ".wd", 0, call_gzip)` (32)를 호출한다. `if (write_elevation)` (34)이면 `write_async(ElevationWriter(U.H, DEM._0), ".elev", 0, call_gzip)` (36). `if (write_discharge)` (39)이면 HU/HV를 .Qx/.Qy로 저장한다(41–42). `if (write_velocity)` (45)이면 `write_async(VelocityWriter(U.H, U.HU, DepthThresh), ".Vx", 0, call_gzip)` (47), `write_async(VelocityWriter(U.H, U.HV, DepthThresh), ".Vy", 0, call_gzip)` (48). |
| 52–63 | write_maxes는 initHtm·totalHtm·maxH·maxHtm을 각각 .inittm·.totaltm·.max·.maxtm에 write_max로 저장하며 세 번째 인수는 모두 0이다(54–57). 최대 수위 출력문은 주석이다(60). |
| 64–72 | wait는 writer_elev·writer_H·writer_HU·writer_HV·writer_U·writer_V에 대해 `wait()`를 차례로 호출한다(66–71). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 54–60: 최대값 출력은 네 필드만 호출한다. 최대 수위 출력문은 주석 처리되어 있다.
