---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/Neighbours.h
lines: 20
sha256: f36d7ec1d4e21f4100983da5be30db22bc6e3bd77fb689f794c921b53d88bf68
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# Neighbours.h — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | `#pragma once` (1), AssembledSolution.h 포함(3). 전처리 조건 분기는 없다. Neighbours 구조체는 AssembledSolution north·east·south·west를 보유한다(5–10). |
| 12–20 | 시작 시 5–6행 Neighbours 구조체 안. 생성자는 num_finest_elems와 solver_type을 받아 같은 두 인수로 네 방향의 AssembledSolution을 각각 생성한다(12–17). 생성자 본문은 비어 있다(18). 구조체 종료(20). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
