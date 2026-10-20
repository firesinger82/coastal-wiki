---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/read_num_stage_points.cpp
lines: 20
sha256: 25f0f570f46dd9637054a82990e731306d0ae5c71d2ac2ae19c01e15e2b4c881
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_num_stage_points.cpp — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 대응 헤더 포함(1).int 반환 read_num_stage_points는 stagefilename을 받는다(3–4). `int num_stage_points = 0;` (5)로 수위 관측점(stage point) 수 기본값을 정한다. 파일을 읽기 모드로 연다(7). `if (NULL == fp)` (9)이면 오류 출력 후 exit(-1)한다(11–12). fscanf의 %d로 개수를 읽고(15), 파일을 닫은 뒤 num_stage_points를 반환한다(17–20). 빈 줄도 포함한다. 조건부 전처리 분기는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5·15·19: fscanf의 반환값이나 읽은 개수의 부호·상한을 검사하지 않고 num_stage_points를 반환한다.
