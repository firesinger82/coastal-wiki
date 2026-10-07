---
file: models/SFINCS/raw/source_code/sfincs/source/sigrid/sge-loop.sh
lines: 26
sha256: c29d5f5c4eb7781fda385bb48f97c3e42ad14ae8f4669e6aa265b5aae64fe87c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# sge-loop.sh — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `/usr/bin/bash` shebang(1), 첫 번째 인수를 DIR에 받는 `DIR=$1` (3), 빈 줄(2·4·10). 조건 `if [ -z ${DIR} ]` (5), then(6). 참이면 `echo "Usage: $0 <model directory>"` (7), `exit 0` (8). fi(9). |
| 11–16 | Cleaning 주석(11)과 빈 줄(12·16). `find . -name "*.nc" -delete` (13), `find . -name "*.log" -delete` (14), `find . -name "SFINCStest-*" -delete` (15)로 현재 디렉터리 아래 이름이 일치하는 항목을 삭제한다. |
| 17–23 | 작업 제출 주석·빈 줄(17–18). ``for MODEL in `\ls $DIR` `` (19), do(20). 각 항목에 `echo "Running model in $MODEL"` (21), `qsub -N SFINCStest-${MODEL} test-job.sh ${DIR} ${MODEL}` (22)를 실행한다. done(23). |
| 24–26 | 빈 줄(24·26), 인수 없는 `exit` (25). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 3·13–15·19: 삭제 명령의 시작 경로는 DIR가 아니라 현재 디렉터리를 가리키는 점이다. DIR는 뒤의 ls와 qsub 인수에 쓰인다.
- 19–22: ls 출력 항목을 순회하며 항목이 디렉터리인지 검사하는 조건은 없다. DIR와 MODEL 확장에는 따옴표가 없다.
