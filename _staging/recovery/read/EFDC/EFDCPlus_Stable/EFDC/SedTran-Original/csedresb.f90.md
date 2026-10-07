---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-Original/csedresb.f90
lines: 40
sha256: a600608a1739007fcbdf8eea8805dc0875712d98b366f9c1e17755766d7f191f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# csedresb.f90 — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | EFDC+·저작권·GPLv2 머리말(1–8). CSEDRESB(DENBULK,WRSPO,VDRO,VDR,VDRC,IOPT) 입구(9). 점착성 퇴적물(cohesive sediment)의 벌크 침식률(bulk erosion rate)을 바닥 벌크밀도(bulk density) 등으로 구한다는 주석(11–12). 주석은 현재 옵션을 사용하지 말라고 적는다(13). IOPT=1의 Hwang–Mehta 1989와 IOPT=2의 Hamrick 수정 Sanford–Maa 2001을 출처로 적는다(14–22). implicit none·인수·반환값을 선언한다(25–28). |
| 30–38 | 시작 시 9행 CSEDRESB 안. 유일한 실행 조건은 IOPT>=1이며 CSEDRESB=0.0을 대입한다(30). 밀도 변환, 0.62 상수, TMP와 거듭제곱 침식률 식은 모두 주석 처리되어 실행되지 않는다(31–37). 조건·계산·호출 원문: `if( IOPT >= 1 ) CSEDRESB = 0.0` (30); `!          CSEDRESB = 0.62` (33); `!          TMP = 0.198/(DENBULK-1.0023)` (35); `!          CSEDRESB = 6.4E-4*(10.**TMP)` (36). |
| 39–40 | 시작 시 9행 CSEDRESB 안. END FUNCTION과 마지막 빈 줄을 포함한다(39–40). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–30: IOPT>=1일 때만 반환값에 대입한다. IOPT<1일 때 반환값을 설정하는 실행문은 없다.
- 28–37: DENBULK·WRSPO·VDRO·VDR·VDRC는 인수로 선언되어 있다. 이 인수들은 실행 식에 사용되지 않는다.
