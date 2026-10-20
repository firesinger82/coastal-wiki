---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/input.cpp
lines: 34
sha256: e5a211afe5cb41d2a26430782b952bff58f476976c7133d483d0815168fc23d3
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# input.cpp — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | 헤더 포함(1) 뒤 ASCII 격자(ASCII raster) 판독 함수 `read_ascfile`(3–34)를 시작한다. 문자 작업 배열 길이는 800(13), nodata 초기값은 −9999(14)다. `fopen_or_die`로 읽기 모드 파일을 열고 첫 다섯 헤더 줄을 문자열 두 개씩 읽어 버린다. 다음 줄에서 nodata 값을 NUM_FMT 형식으로 읽는다. 조건부 전처리 분기는 없다. 원문: `NUMERIC_TYPE no_data_value = -9999;` (14); `fp = fopen_or_die(filename, "r", message, verbose);` (16); `for (int i=0; i<5; i++)` (17); `{` (18); `fscanf(fp, "%s %s", dummy, dummy);` (19); `}` (20); `fscanf(fp, "%s %" NUM_FMT"", dummy, &no_data_value);` (21). |
| 22–34 | 시작 시 3행 `read_ascfile` 안이다. ysz·xsz 이중 루프로 셀값을 읽는다. nodata 값과의 절댓값 차가 1e−12보다 작으면 0으로 치환한다. 두 루프 뒤 fclose로 닫는다(33). 원문: `for (int j=0; j<Parptr->ysz; j++)` (22); `{` (23); `for (int i=0; i<Parptr->xsz; i++)` (24); `{` (25); `fscanf(fp, "%" NUM_FMT"", field + j*Parptr->xsz + i);` (26); `if (FABS(field[i + j*Parptr->xsz] - no_data_value) < C(1e-12))` (27); `{` (28); `field[j*Parptr->xsz + i] = C(0.0);` (29); `}` (30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19·21·26: fscanf 호출의 반환값을 검사하는 문장은 없다.
- 17–21: 처음 다섯 헤더 항목의 이름·값은 버린다. 격자 반복 크기는 파일 헤더 대신 Parptr의 xsz·ysz를 사용한다(22–24).
- 13·19·21: dummy 배열 길이는 800이며 문자열 판독 형식은 폭 지정이 없는 `%s`다.
