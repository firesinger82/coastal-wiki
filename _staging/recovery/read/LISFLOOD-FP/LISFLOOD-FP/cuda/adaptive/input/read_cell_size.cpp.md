---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_cell_size.cpp
lines: 29
sha256: b9e95b66b5eba3ddf4f5d77a535242ef090759679f9a713a1069bb5c11629945
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_cell_size.cpp — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 자기 헤더 포함(1). read_cell_size는 입력 파일명을 받는다(3). DEMfile을 read_keyword_str로 읽는다(5–6). dummy 정수와 문자 버퍼를 0/널 문자로 초기화하며(8–9), `real cell_size      = C(0.0);` (10). 수치표고모형(digital elevation model, DEM) 파일을 연다(12). `if (NULL == fp)` (14)이면 오류 출력·exit(-1)(16–17). 전처리 조건 분기는 없다. |
| 19–29 | 시작 시 3행 함수 안. 첫 두 키/정수 쌍은 dummy_buf·dummy로 읽는다(20–21). `fscanf(fp, "%s %" NUM_FRMT, dummy_buf, &cell_size);` (22), `fscanf(fp, "%s %" NUM_FRMT, dummy_buf, &cell_size);` (23), `fscanf(fp, "%s %" NUM_FRMT, dummy_buf, &cell_size);` (24)의 세 판독이 같은 cell_size 변수에 순서대로 값을 쓴다. fclose 후 cell_size를 반환하고 함수를 닫는다(26–29). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20–24: 헤더 키 이름을 비교하지 않고 순서대로 읽는다. 실수형 헤더 값 세 개를 같은 cell_size에 덮어쓴다.
- 20–24: 다섯 fscanf의 반환값을 검사하는 문장은 없다. %s에 필드 폭을 지정하지 않는다.
