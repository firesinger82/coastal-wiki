---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-Original/csndset.f90
lines: 24
sha256: 9ed7abc9374a70620822df01b722b433922584a1d77f7e00eb8bf9ebf11add27
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# csndset.f90 — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | EFDC+·저작권·GPLv2 머리말(1–8). CSNDSET(SND,SDEN,IOPT) 입구(9). 변경 이력과 비점착성 퇴적물(noncohesive sediment)의 간섭침강(hindered settling) 보정 주석(10–13). implicit none·정수 IOPT·실수 인수·반환값·ROPT 선언과 빈 줄을 포함한다(15–19). |
| 20–24 | 시작 시 9행 CSNDSET 안. IOPT를 FLOAT로 실수 ROPT에 변환한다(20). 1.-SDEN*SND의 ROPT승을 보정값으로 반환한다(21). 조건 분기나 다른 루틴 호출은 없다. END FUNCTION·마지막 빈 줄을 포함한다(23–24). 조건·계산·호출 원문: `ROPT = FLOAT(IOPT)` (20); `CSNDSET = (1.-SDEN*SND)**ROPT` (21). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20–21: 반환값 계산 전 SND·SDEN·IOPT의 범위를 검사하거나 거듭제곱의 밑을 제한하는 실행문은 없다.

