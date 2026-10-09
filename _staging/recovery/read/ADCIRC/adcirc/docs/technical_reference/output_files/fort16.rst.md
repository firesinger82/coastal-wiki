---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort16.rst
lines: 61
sha256: 3a646f9a81c18b788d19ba2eab2db7992d30ca8e859f81dd41f729033ee65020
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort16.rst — 판독 구간 기록

구간은 1행부터 61행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | Fort.16: General Diagnostic Output — 격자·경계 정보 파일과 모델 매개변수·주기 경계조건(periodic boundary condition) 파일의 정보를 다시 출력한다(6–9). 처리된 일부 정보와 ADCIRC 오류 메시지도 출력한다(11–14). 원문: `Output file which echo prints information from:` (6); `* The Grid and Boundary Information File` (8); `* The Model Parameter and Periodic Boundary Condition File` (9); `Additionally, this file:` (11); `* Provides some processed information` (13); `* Prints out error messages from ADCIRC` (14). |
| 16–30 | Notes for fort.16 file / GFDL와 fort.22 — GFDL(Geophysical Fluid Dynamics Laboratory) 파일 형식이 대기 모델 출력을 지원하려고 개발되었다고 설명한다(19). ASCII 기상 파일의 중첩 격자(nested grid)는 시간에 따라 변할 수 있다(21). 더 세밀한 중첩 자료가 있는 곳에는 거친 격자 자료를 저장하지 않는다(22). 이어서 fort.22의 네 종류 줄을 제시한다(24–29). 원문: `The Geophysical Fluid Dynamics Laboratory (GFDL) file format was developed to support the output from atmospheric models. The files have the following characteristics:` (19); `* Each ASCII GFDL met file contains one or more nested grid data where the nested grids are allowed to change in time.` (21); `* Coarse grid data is not stored where finer nest data is given.` (22); `The file format of the ADCIRC fort.22 for GFDL is as follows:` (24); `Line 1 — ASCII Text Header` (26); `Line 2 — Windmultiplier Value (real number)` (27); `Line 3 — Maximum Extrapolation distance (m)` (28); `Lines 4-end — cycleTime rampValue filename` (29). |
| 31–46 | Notes for fort.16 file / 실제 GFDL 파일 형식 — 첫 줄은 NCELLS이며 다음 줄들은 10f10.4 형식의 열을 가진다(31–34). 속도, 온도(temperature), 혼합비(mixing ratio), 폭풍 누적 강수(storm accum precipitation), 해면 기압(sea level pressure), 경도와 위도, 허리케인 시간, 중첩 번호의 이름과 단위를 원문대로 제시한다(36–45). 중첩 번호는 항상 존재하지는 않는다(45). 원문: `The file format for each of the actual GFDL files is as follows:` (31); `Line 1: Number of grid cells (f10.4) NCELLS` (33); `Lines 2-NCELLS+1: Have ten columns of data formatted as 10f10.4` (34); `1. u (m/sec)` (36); `2. v (m/sec)` (37); `3. Temperature (K)` (38); `4. mixing ratio(kg/kg)` (39); `5. storm accum precipitation (cm)` (40); `6. sea level pressure (hPa)` (41); `7. longitude (decimal deg)` (42); `8. latitude (decimal deg)` (43); `9. hurricane hour` (44); `10. nest number (this is not always present)` (45). |
| 47–61 | Example — GFDL용 fort.22 예제를 제시한다(50–59). 주석 최대 길이, 속도 크기 배율, 미터 단위 최대 외삽 거리(maximum extrapolation distance), 시간·배율·파일명 줄을 그대로 옮긴다(54–59). 전체 경로에 슬래시가 있으면 파일명을 큰따옴표로 감싸야 한다(61). Fortran이 감싸지 않은 슬래시를 레코드 종료 문자(end-of-record character)로 처리하는 이유를 적는다(61). 원문: `To illustrate the definitions and descriptions provided, a concrete example of an ADCIRC fort.22 file for GFDL is provided as follows:` (50); `.. code-block:: none` (52); `   ! 1st line is a comment line, max length 1024 characters` (54); `   1.0     ! 2nd line is a velocity magnitude multiplier` (55); `   10000.0 ! 3rd line: maximum extrapolation distance (m)` (56); `   0.0 0.0 "/home/jason/isaac/gfdl/isaac_gfdl_file1" ! time (hours), ramp mult, filename` (57); `   6.0 0.5 "/home/jason/isaac/gfdl/isaac_gfdl_file2"` (58); `   12.0 1.0 "/home/jason/isaac/gfdl/isaac_gfdl_file3"` (59); `Note: When including the path to the data files, if the full path includes forward slashes (as it would if ADCIRC is executing on Unix or Linux), be sure to surround the full path file name with double quotes as shown in the example above. This is required because Fortran treats a bare forward slash in an input file as an end-of-record character. ` (61). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 3·6–14·24·50행: 제목과 첫 설명은 fort.16의 일반 진단 출력이다. 24행부터의 형식 설명과 50행의 예제 소개는 fort.22의 GFDL 입력 파일을 명시한다.
- 34·45행: 34행은 `ten columns of data formatted as 10f10.4`라고 적는다. 45행은 열 목록의 열 번째 항목인 `nest number`가 항상 존재하지는 않는다고 적는다.
