---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_bound_conds.cpp
lines: 37
sha256: 7408f26a897a7cc7c47d22fe0e9614e109911e8848fdec54144cbd37fcb1b38c
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_bound_conds.cpp — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 자기 헤더를 포함한다(1). read_bound_conds는 시험 번호의 const 참조를 받는다(3). Depths1D(test_case)로 경계 수심(boundary depth) 객체를 생성한다(5). `switch (test_case)` (7)로 시험 번호를 분기한다. 전처리 조건 분기는 없다. |
| 9–21 | 시작 시 3행 함수·7행 switch 안. `case 1: case 2: // wet c property` (9)에서는 `bcs.hl = C(6.0);` (10), `bcs.hr = C(6.0);` (11), break(12). `case 3: case 4: // wet/dry c property` (13)에서는 `bcs.hl = C(2.0);` (14), `bcs.hr = C(2.0);` (15), break(16). `case 5: case 6:   // wet dam break` (17) 및 `case 11: case 12: // wet overtopping` (18)에서는 `bcs.hl = C(6.0);` (19), `bcs.hr = C(2.0);` (20), break(21). |
| 22–37 | 시작 시 3행 함수·7행 switch 안. `case 7:  case 8:  // dry dam break` (22), `case 9:  case 10: // dry dam break with fric` (23), `case 13: case 14: // dry overtopping` (24)는 같은 대입 `bcs.hl = C(6.0);` (25), `bcs.hr = C(0.0);` (26) 뒤 break(27). `case 17: // three humps` (28)에서는 `bcs.hl = C(2.0);` (29), `bcs.hr = C(0.0);` (30), break(31). `default:` (32)는 break만 한다(33). switch를 닫고 bcs를 반환하며 함수를 닫는다(34–37). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28 및 classes/SimulationParams.h:139: 이 파일의 case 17 주석은 three humps다. 함께 판독한 SimulationParams의 case 17 주석은 parabolic bowl이다.
- 5·32–36: 이 switch에 명시되지 않은 시험 번호는 Depths1D(test_case) 생성 결과를 이 함수에서 추가 변경하지 않고 반환한다.
