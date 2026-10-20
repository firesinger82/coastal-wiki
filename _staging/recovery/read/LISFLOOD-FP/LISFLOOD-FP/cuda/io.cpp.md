---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/io.cpp
lines: 144
sha256: 139494ded7babc77828ca49338ebb67a574c71164c0e00c394c343da49d138d4
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# io.cpp — 판독 구간 기록

구간은 1행부터 144행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | 헤더 포함(1–2). AsciiRaster::read_header는 fscanf로 xsz·ysz·blx·bly·dx·no_data_value를 순서대로 읽는다(11–16). `geometry.dy = geometry.dx;` (18), `geometry.tly = geometry.bly + geometry.ysz*geometry.dy;` (19). 조건부 전처리 지시는 없다. |
| 22–39 | AsciiRaster::read는 `for (int j=0; j<geometry.ysz; j++)` (31), `for (int i=0; i<geometry.xsz; i++)` (33)에서 `fscanf(file, "%" NUM_FMT, &(array[j*pitch + i + offset]));` (35)를 호출한다. pitch·offset으로 고스트 래스터(ghost raster) 내부 영역을 읽는다. |
| 40–62 | replace_no_data는 `for (int j=0; j<geometry.ysz; j++)` (50), `for (int i=0; i<geometry.xsz; i++)` (52)에서 해당 셀을 참조한다(54). `if (FABS(value - original_no_data_value) < C(1e-6))` (55)이면 new_value를 대입한다(57). |
| 63–78 | match_cell_dimensions_or_die는 `if (expected.xsz != candidate.xsz \|\| expected.ysz != candidate.ysz)` (70)이면 예상·실제 셀 수를 stderr에 출력하고 exit(1)을 호출한다(72–75). |
| 79–100 | StartFile::load는 fopen_or_die로 "rb" 파일을 열고(89), read_header(92), match_cell_dimensions_or_die(93–94), read(95), fclose(96), zero_no_data_values(98)를 순서대로 호출한다. |
| 101–119 | zero_no_data_values는 `for (int j=0; j<geometry.ysz; j++)` (110), `for (int i=0; i<geometry.xsz; i++)` (112)에서 셀 참조를 얻고 `if (FABS(value - no_data_value) < C(1e-5)) value = C(0.0);` (115)를 적용한다. |
| 120–140 | subtract_dem은 `for (int j=0; j<geometry.ysz; j++)` (129), `for (int i=0; i<geometry.xsz; i++)` (131)에서 H와 DEM을 같은 pitch·offset으로 읽고 `H_value = H_value - DEM_value;` (136)를 적용한다. |
| 141–144 | Snapshot::initialise_async는 `return std::async(std::launch::async, []{});` (143)로 빈 비동기(asynchronous) 작업의 future를 반환한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–16·35: fscanf 반환값을 검사하는 조건이 이 두 판독 함수에 없다.
- 70–76: 격자 일치 검사는 xsz·ysz만 비교한다. 원점과 셀 간격 비교는 이 함수에 없다.
- 55·115: replace_no_data의 허용 오차는 C(1e-6)이고 zero_no_data_values의 허용 오차는 C(1e-5)이다.
- 136: subtract_dem은 차이를 그대로 H에 저장한다. 음수 수심을 제한하는 조건은 이 함수에 없다.
