---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/io.templates.cpp
lines: 160
sha256: 6174282f98504c24b0ee85e2fcfbe0b849829c9c7587794044ddb5a36aefcce4
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# io.templates.cpp — 판독 구간 기록

구간은 1행부터 160행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | `template<typename F>` (1)의 AsciiRaster::write. `if (outflag == 0) {` (15)이면 xsz·ysz·blx·bly·dx·nodata 헤더를 precision으로 출력한다(16–21). `for (int j = 0; j < geometry.ysz; j++)` (23), `for (int i = 0; i < geometry.xsz; i++)` (25)에서 `array[j * pitch + i + offset]` (28)를 출력하고 행마다 개행한다(30). 조건부 전처리 지시는 없다. |
| 33–50 | 시작 시 2행 AsciiRaster::write 안. `else if (outflag == 1) {` (33)은 x 셀 수 `geometry.xsz + 1` (34), 원점 `geometry.blx - (geometry.dx / C(2.0))` (36)을 출력한다. ysz·bly·dx·nodata는 해당 격자값을 사용한다(35·37–39). `for (int j = 0; j < geometry.ysz; j++)` (41), `for (int i = 0; i < geometry.xsz + 1; i++)` (43)에서 `array[j * (pitch + 1) + i + offset]` (46)를 출력한다. |
| 51–70 | 시작 시 2행 AsciiRaster::write 안. `else if (outflag == 2) {` (51)은 xsz와 y 셀 수 `geometry.ysz + 1` (53), 원점 `geometry.bly - (geometry.dx / C(2.0))` (55), cellsize=dx(56)를 출력한다. `for (int j = 0; j < geometry.ysz + 1; j++)` (59), `for (int i = 0; i < geometry.xsz; i++)` (61)에서 `array[j * (pitch + 1) + i + offset]` (64)를 출력한다. 조건·함수 종료(68–69). |
| 71–94 | `template<typename F>` (71)의 Snapshot::write_async는 `return std::async(std::launch::async, [=, &geometry]{` (88)로 비동기(asynchronous) 작업을 만들고 `Snapshot::write(array, geometry, pitch, offset, prefix, counter, suffix, verbose, outflag, call_gzip, precision, no_data_value);` (89–90)를 실행한다. 람다(lambda)는 geometry를 참조로 캡처한다(88). |
| 95–132 | `template<typename F>` (95)의 Snapshot::write는 filename[800]·tmp_sys_com[255]를 선언한다(113–114). snprintf는 크기 `800*sizeof(char)`와 형식 `"%s-%.4d%s"` (116)을 사용한다. fopen_or_die로 "wb" 파일을 열고 AsciiRaster::write·fclose를 호출한다(118–123). `if (call_gzip == ON)` (126)이면 `sprintf(tmp_sys_com, "%s%s", "gzip -9 -f ", filename);` (128), `system(tmp_sys_com);` (129)를 실행한다. |
| 133–160 | `template<typename F>` (133)의 write_max는 filename[800]에 `snprintf(filename, 800 * sizeof(char), "%s%s", prefix, suffix);` (150)로 이름을 만들고 "wb"로 연다(152). `AsciiRaster::write(file, array, geometry, pitch, offset, no_data_value, outflag, precision)` (154–155) 뒤 fclose(157). counter·gzip 처리문은 이 루틴에 없다. 마지막 빈 줄(160). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 113–129: filename 버퍼는 800바이트이고 gzip 명령 버퍼는 255바이트이다. 명령 구성에는 크기 제한 인수 없는 sprintf를 사용한다.
- 15–69: AsciiRaster::write는 outflag 0·1·2만 분기한다. 그 밖의 값을 처리하는 else는 없다.
- 51–64: y 방향 추가 행 출력에서도 y 원점 이동에 geometry.dx를 사용하고 배열 행 간격에는 pitch+1을 사용한다.
- 81·105·142: 세 Snapshot 출력 함수는 verbose 인수를 받는다. 각 함수의 직접 로그·조건식에는 verbose가 사용되지 않는다. write_async는 이를 write로 전달한다.
