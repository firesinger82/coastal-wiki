---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/lisflood2/lisflood2.h
lines: 12
sha256: 675643505a86cc59ea74c18b753db3edc63a5b90c3c554dab9077a5f238620cf
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# lisflood2.h — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `#pragma once` (1), time.h 포함(3). `#if defined(_MSC_VER)` (5)에서는 windows_ext.h 포함(6), `#else` (7)는 sys/time.h 포함(8), `#endif` (9)로 닫는다. _MSC_VER는 이 파일에서 정의하지 않는 컴파일러 매크로이다. |
| 11–12 | 전처리 조건 밖. 격자 정렬 폭(alignment width)은 `#define GRID_ALIGN_WIDTH 8` (11), 스레드(thread)의 하위 격자 수로(subgrid channel) 셀 블록 크기는 `#define	THREAD_SG_CELL_BLOCK 64` (12)로 정의한다. 이 두 값의 정의는 이 헤더 자체에 있다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–12: GRID_ALIGN_WIDTH와 THREAD_SG_CELL_BLOCK는 각각 8과 64로 고정되어 있다. 이 정의 앞에는 기존 매크로 정의 여부를 검사하는 조건이 없다.
