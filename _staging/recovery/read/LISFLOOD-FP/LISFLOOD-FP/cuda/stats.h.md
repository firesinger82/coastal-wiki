---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/stats.h
lines: 61
sha256: b32b1cb90cee0e30cb7550d617b47f8edf4d64bef3429966537c502aa2c24634
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# stats.h — 판독 구간 기록

구간은 1행부터 61행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | `#pragma once` (1), LISFLOOD·cstdio 헤더 포함(2–3), lis 이름 공간(namespace)(5–6). MassStats는 NUMERIC_TYPE in·out을 선언한다(8–12). 조건부 전처리 지시는 없다. |
| 14–26 | StatsEntry는 NUMERIC_TYPE t·dt·min_dt·area·volume·volume_error·discharge_error, long iteration, MassStats mass를 선언한다(14–25). 멤버 기본값은 없다. |
| 27–54 | Stats 클래스 public 구역에서 resroot·interval·next_save·checkpoint·time을 받는 생성자를 선언한다(27–37). write_header, need_to_write, StatsEntry를 받는 write, 공개 next_save, 소멸자를 선언한다(39–53). |
| 55–61 | 시작 시 5행 이름 공간·27행 Stats 클래스 안. private에는 FILE* file과 NUMERIC_TYPE interval을 둔다(55–57). 클래스·이름 공간 종료와 빈 줄(58–61). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
