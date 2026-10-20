---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc/cuda_acc_snapshot.cu
lines: 72
sha256: 08bc448992db7fdbc97b9f13309ff6670889c3d5bd4b96a917379e7d4dfb78f6
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_acc_snapshot.cu — 판독 구간 기록

구간은 1행부터 72행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | ACC Snapshot·입출력 헤더 포함(1–2). 이 파일에는 조건부 전처리 블록이 없다. 동일 소스 루트의 CMakeLists.txt에서 `if (CMAKE_CUDA_COMPILER)` (73) 아래 `add_compile_definitions(CUDA THRUST_IGNORE_CUB_VERSION_CHECK)` (77)를 적용하며 cuda/acc 구현 파일은 114–118행에 열거한다. config.default.cmake:2의 수치 모드 정의는 `add_compile_definitions(_NUMERIC_MODE=1)`이다. 실제 구성·컴파일은 실행하지 않았다. Snapshot 생성자(constructor)는 파일명·저장 간격과 상태·DEM·Flow·기하·인덱스·verbose·정밀도를 받아 cuda::Snapshot<Flow> 기반 클래스(base class)를 초기화한다(4–20). DEM 포인터를 보관하고 빈 람다(lambda)를 std::launch::async로 실행한 future 여섯 개를 초기화한다(21–28). 원문(조건·식·호출·선언): `#include "cuda_acc_snapshot.cuh"` (1); `#include "io.h"` (2); `lis::cuda::acc::Snapshot::Snapshot` (4); `(` (5); `const char* resrootname,` (6); `NUMERIC_TYPE interval,` (7); `NUMERIC_TYPE next_save,` (8); `int counter,` (9); `NUMERIC_TYPE* DEM,` (10); `Flow& U,` (11); `Geometry& geometry,` (12); `int pitch,` (13); `int offset,` (14); `int verbose,` (15); `int precision` (16); `)` (17); `:` (18); `cuda::Snapshot<Flow>(resrootname, interval, next_save, counter, U, geometry,` (19); `pitch, offset, verbose, precision),` (20); `DEM(DEM),` (21); `writer_elev(std::async(std::launch::async, []{})),` (22); `writer_H(std::async(std::launch::async, []{})),` (23); `writer_HU(std::async(std::launch::async, []{})),` (24); `writer_HV(std::async(std::launch::async, []{})),` (25); `writer_U(std::async(std::launch::async, []{})),` (26); `writer_V(std::async(std::launch::async, []{}))` (27). |
| 30–51 | Snapshot::write는 수심 U.H를 .wd로 비동기(asynchronous) 출력한다(30–32). write_elevation이면 ElevationWriter(U.H,DEM)를 .elev로 쓴다(34–36). write_discharge이면 Qxold·Qyold를 .Qx·.Qy로, write_velocity이면 Vx·Vy를 같은 이름 확장자로 쓴다(39–48). 각 호출은 call_gzip과 위치 인수 0·1·2를 전달한다. 원문(조건·식·호출·선언): `void lis::cuda::acc::Snapshot::write(const int& call_gzip)` (30); `writer_H = write_async(U.H, ".wd", 0, call_gzip);` (32); `if (write_elevation)` (34); `writer_elev = write_async(ElevationWriter(U.H, DEM), ".elev", 0, call_gzip);` (36); `if (write_discharge)` (39); `writer_HU = write_async(U.Qxold, ".Qx", 1, call_gzip);` (41); `writer_HV = write_async(U.Qyold, ".Qy", 2, call_gzip);` (42); `if (write_velocity)` (45); `writer_U = write_async(U.Vx, ".Vx", 1, call_gzip);` (47); `writer_V = write_async(U.Vy, ".Vy", 2, call_gzip);` (48). |
| 52–63 | Snapshot::write_maxes는 최초 침수시각·총 침수시간·최대수심·최대수심 시각 배열을 .inittm·.totaltm·.max·.maxtm으로 write_max에 전달한다(52–57). ElevationWriter의 비동기 최대장 출력은 주석 처리되어 있다(60). 원문(조건·식·호출·선언): `void lis::cuda::acc::Snapshot::write_maxes()` (52); `write_max(U.initHtm, ".inittm", 0);` (54); `write_max(U.totalHtm, ".totaltm", 0);` (55); `write_max(U.maxH, ".max", 0);` (56); `write_max(U.maxHtm, ".maxtm", 0);` (57). |
| 64–72 | Snapshot::wait는 수위·수심·두 유량·두 속도의 future에 차례로 wait를 호출한다(64–72). 자체 조건·루프·직접 CUDA 커널 실행은 없다. 원문(조건·식·호출·선언): `void lis::cuda::acc::Snapshot::wait()` (64); `writer_elev.wait();` (66); `writer_H.wait();` (67); `writer_HU.wait();` (68); `writer_HV.wait();` (69); `writer_U.wait();` (70); `writer_V.wait();` (71). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32–48: .wd 출력은 무조건 호출한다. 수위·유량·속도 출력은 각각의 독립 조건에 따른다.
- 41–42: .Qx·.Qy 출력에 전달하는 배열은 U.Qxold·U.Qyold이다.
- 54–60: 활성 최대 출력은 .inittm·.totaltm·.max·.maxtm 네 종류이다. 수위 최대장용 비동기 출력 문장은 주석이다.
- 66–71: wait 메서드는 각 future의 wait만 호출한다. future::get 호출은 이 파일에 없다.
