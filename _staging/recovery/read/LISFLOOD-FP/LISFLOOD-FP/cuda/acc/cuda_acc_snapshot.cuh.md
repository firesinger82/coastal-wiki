---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc/cuda_acc_snapshot.cuh
lines: 48
sha256: ce0a9f92c2d38cdb85dec3e7452ecdcbaadc2d79c788ef7fbd8b79cd305d112c
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_acc_snapshot.cuh — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | 중복 포함 방지·CUDA Snapshot·ACC Flow 헤더와 lis::cuda::acc 이름공간(namespace) 선언(1–10). 조건부 전처리 블록이 없다. 헤더 전체는 포함 번역 단위(translation unit)의 매크로 조합을 따르며 자체 #if 제한이 없다. CMakeLists.txt:73·77의 CUDA 구성 정의와 config.default.cmake:2의 _NUMERIC_MODE=1 정의가 관련 빌드 설정이다. 원문(조건·식·호출·선언): `#pragma once` (1); `#include "cuda_snapshot.cuh"` (2); `#include "cuda_acc_flow.cuh"` (3); `namespace lis` (5); `namespace cuda` (7); `namespace acc` (9). |
| 12–31 | 시작 시 5·7·9행 이름공간 안. Snapshot은 lis::cuda::Snapshot<Flow>를 public 상속(inheritance)한다(12). 생성자 인수는 출력명·간격·다음 시각·번호·DEM·Flow·Geometry·pitch·offset·verbose·precision이며 precision의 기본값은 DEFAULT_PRECISION이라는 매크로 기호다(15–28). 이 헤더는 그 기호의 숫자 값을 정의하지 않는다. 확인한 CMakeLists.txt·config.default.cmake·makefile·루트 *.mk에도 그 기호의 숫자 정의는 없다. public wait를 선언한다(30). 원문(조건·식·호출·선언): `class Snapshot : public lis::cuda::Snapshot<Flow>` (12); `public:` (14); `Snapshot` (15); `(` (16); `const char* resrootname,` (17); `NUMERIC_TYPE interval,` (18); `NUMERIC_TYPE next_save,` (19); `int counter,` (20); `NUMERIC_TYPE* DEM,` (21); `Flow& U,` (22); `Geometry& geometry,` (23); `int pitch,` (24); `int offset,` (25); `int verbose,` (26); `int precision = DEFAULT_PRECISION` (27); `);` (28); `void wait();` (30). |
| 32–48 | 시작 시 5·7·9행 이름공간·12행 Snapshot 클래스 안. protected write·write_maxes 메서드를 선언한다(32–34). private에는 const NUMERIC_TYPE* DEM 및 수위·수심·두 유량·두 속도용 std::future<void> 멤버를 둔다(36–43). 클래스와 이름공간을 닫는다(44–48). 직접 실행 조건·루프·커널 지시는 없다. 원문(조건·식·호출·선언): `protected:` (32); `void write(const int& call_gzip);` (33); `void write_maxes();` (34); `private:` (36); `const NUMERIC_TYPE* DEM;` (37); `std::future<void> writer_elev;` (38); `std::future<void> writer_H;` (39); `std::future<void> writer_HU;` (40); `std::future<void> writer_HV;` (41); `std::future<void> writer_U;` (42); `std::future<void> writer_V;` (43). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
