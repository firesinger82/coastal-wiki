---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/Depths1D.h
lines: 62
sha256: 17c1991dc0fec0df5297aec8a3987b73883a8ae52e7d16ec59a303d6b3d884b4
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# Depths1D.h — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `#pragma once` (1), real.h 포함(3). 전처리 조건 분기는 없다. Depths1D 구조체는 real hl·hr를 선언하며 멤버 초기값은 없다(5–8). |
| 10–26 | 시작 시 5–6행 Depths1D 구조체 안. test_case 생성자의 `switch (test_case)` (12). 시험별 case·기본 수심 대입 전체 `case 1: case 2: // wet c property`<br>`this->hl = C(6.0);`<br>`this->hr = C(6.0);`<br>`break;`<br>`case 3: case 4: // wet/dry c property`<br>`this->hl = C(2.0);`<br>`this->hr = C(2.0);`<br>`break;`<br>`case 5: case 6:   // wet dam break`<br>`case 11: case 12: // wet overtopping`<br>`this->hl = C(6.0);`<br>`this->hr = C(2.0);`<br>`break;` (14–26). 1·2는 습윤 c-property(wet c-property)의 양쪽 6, 3·4는 습윤/건조 c-property(wet/dry c-property)의 양쪽 2라는 주석이다. 5·6 및 11·12는 왼쪽 6·오른쪽 2이다. |
| 27–43 | 시작 시 10–11행 생성자·12행 switch 안. 건조 댐 붕괴(dry dam break)·마찰·월류(overtopping) 시험 및 three humps의 case와 대입 전체 `case 7:  case 8:  // dry dam break`<br>`case 9:  case 10: // dry dam break with fric`<br>`case 13: case 14: // dry overtopping`<br>`this->hl = C(6.0);`<br>`this->hr = C(0.0);`<br>`break;`<br>`case 17: // three humps`<br>`this->hl = C(2.0);`<br>`this->hr = C(0.0);`<br>`break;`<br>`default:`<br>`break;` (27–38). switch·생성자·구조체 종료(39–42). default는 break만 실행한다. |
| 44–62 | 전체가 블록 주석이다(44–62). 지정 초기화(designated initialiser)와 /std:c++latest 설명(45–48), 주석 예제 전체 `Depths1D bcs = {`<br>`.hl = C(2.0),`<br>`.hr = C(0.0),`<br>`.ql = C(0.0),`<br>`.qr = C(0.0),`<br>`.reflectUp = C(0.0),`<br>`.reflectDown = C(0.0),`<br>`.hImposedUp = C(0.0),`<br>`.qxImposedUp = C(0.0),`<br>`.hImposedDown = C(0.0),`<br>`.qxImposedDown = C(0.0)`<br>`};` (50–61). 예제의 hl·hr 외 ql·qr·reflectUp·reflectDown·hImposedUp·qxImposedUp·hImposedDown·qxImposedDown은 실행되는 Depths1D 선언에는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–8·37–38: hl·hr 선언에는 기본값이 없다. 생성자의 default는 두 필드에 값을 대입하지 않는다.
- 50–60: 블록 주석의 지정 초기화 예제는 현재 구조체에 선언되지 않은 필드도 포함한다. 이 예제는 실행 코드가 아니다.
