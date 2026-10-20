---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/stats.cpp
lines: 86
sha256: cb0d89492169d0fd6c3abf6dedfc6fa51f78a7f67199942b8279e8be8a7c1e34
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# stats.cpp — 판독 구간 기록

구간은 1행부터 86행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | 헤더 포함과 Stats 생성자(1–16). interval·next_save를 인수에서 복사한다(14–15). filename[800]에 .mass 이름을 만든다(17–18). `if (checkpoint == ON && time > 0) {` (21)이면 fopen_or_die의 "a" 모드(22), else(24)는 "w" 모드(25)를 사용한다. 조건부 전처리 지시는 없다. |
| 30–45 | write_header의 `if (time == 0) {` (32)은 시간·시간 간격·최소 시간 간격·횟수·면적·체적·유입·Hds·유출·유량 오차·체적 오차·Rain-(Inf+Evap) 헤더를 출력한다(35). else(37)는 재시작(checkpoint restart) 표시와 같은 헤더를 출력하고 fflush를 호출한다(39–42). |
| 46–53 | need_to_write는 `return t >= next_save;` (51)를 반환한다. |
| 54–82 | write는 StatsEntry의 t·dt·min_dt·iteration·area·volume·mass.in·mass.out·discharge_error·volume_error를 순서에 맞춰 fprintf에 넘긴다(59–75). Hds 자리는 `C(0.0) /*Solverptr->Hds*/,` (70), 마지막 강우 손실 자리는 `C(0.0) /*Parptr->RainTotalLoss - (Parptr->InfilTotalLoss + Parptr->EvapTotalLoss)*/` (74)이다. fflush(76) 뒤 `next_save += interval;` (78). 빈 줄을 포함한다(80–82). |
| 83–86 | 소멸자는 `fclose(file);` (85)를 호출한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 70·74: 출력 헤더에는 Hds와 Rain-(Inf+Evap)가 있지만 데이터 출력은 두 위치에 C(0.0)을 전달한다.
- 51·78: 저장 판단은 t>=next_save이다. write 한 번마다 next_save에 interval을 한 번 더한다. 경과한 간격을 반복해서 따라잡는 루프는 이 함수에 없다.
