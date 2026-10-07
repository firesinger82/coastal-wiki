---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-Original/csedress.f90
lines: 61
sha256: 876f1c093e67c586bae97c9aa2d94fc12509a970bbe94d53e147267aeeafe2d7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# csedress.f90 — 판독 구간 기록

구간은 1행부터 61행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | EFDC+·저작권·GPLv2 머리말(1–8). CSEDRESS 함수 입구와 변경 이력 주석(9–11). 점착성 퇴적물(cohesive sediment)의 표면 침식률(surface erosion rate)을 바닥 벌크밀도(bulk density)로 구한다는 주석(13–14). 옵션 1은 Hwang–Mehta 1989, 2는 Hamrick 수정 Sanford–Maa 2001, 4·5는 SEDFLUME 시험 자료의 매개변수화(parameterization)를 적는다(15–27). 인수·반환값·작업 실수를 선언한다(29–33). |
| 35–47 | 시작 시 9행 CSEDRESS 안. IOPT=1은 DENBULK 원본을 보존하기 위해 BULKDEN에 0.001을 곱한다(35–36). BULKDEN<=1.065이면 침식률은 0.62이다(37–38). else는 TMP를 계산하고 EXP를 적용한 뒤 10.**TMP 식을 사용한다(39–43). 병렬 elseif의 IOPT=2는 VDR, IOPT=3은 VDRC를 분모에 사용한다(44–47). 조건·계산·호출 원문: `if( IOPT == 1 )then` (35); `BULKDEN = 0.001*DENBULK    ! *** TO PREVENT CORRUPTING THE DENBULK VARIABLE` (36); `if( BULKDEN <= 1.065 )then` (37); `CSEDRESS = 0.62` (38); `else` (39); `TMP = 0.198/(BULKDEN-1.0023)` (40); `TMP = EXP(TMP)` (41); `CSEDRESS = 6.4E-4*(10.**TMP)` (42); `elseif( IOPT == 2 )then` (44); `CSEDRESS = WRSPO*(1.+VDRO)/(1.+VDR)` (45); `elseif( IOPT == 3 )then` (46); `CSEDRESS = WRSPO*(1.+VDRO)/(1.+VDRC)` (47). |
| 48–61 | 시작 시 9행 CSEDRESS·35행 옵션 선택 블록 안. IOPT=4·5의 병렬 elseif는 각각 VDR·VDRC로 TMPVAL을 구하고 EXP(-TMPVAL) 감쇠를 곱한다(48–55). IOPT>=99이면 WRSPO를 반환한다(56–57). 선택 블록 종료, END FUNCTION, 마지막 빈 줄을 포함한다(58–61). 조건·계산·호출 원문: `elseif( IOPT == 4 )then` (48); `TMPVAL = (1.+VDRO)/(1.+VDR)` (49); `FACTOR = EXP(-TMPVAL)` (50); `CSEDRESS = FACTOR*WRSPO*(1.+VDRO)/(1.+VDR)` (51); `elseif( IOPT == 5 )then` (52); `TMPVAL = (1.+VDRO)/(1.+VDRC)` (53); `FACTOR = EXP(-TMPVAL)` (54); `CSEDRESS = FACTOR*WRSPO*(1.+VDRO)/(1.+VDRC)` (55); `elseif( IOPT >= 99 )then` (56). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 35–58: 반환값 대입 분기는 IOPT=1·2·3·4·5 또는 IOPT>=99이다. 나머지 IOPT를 처리하는 else나 기본값 대입은 없다.
- 40–42: TMP는 0.198/(BULKDEN-1.0023)으로 계산된 뒤 EXP(TMP)로 갱신된다. 침식률 식은 갱신된 TMP를 10의 지수로 사용한다.
- 45·47·49·53: 공극비(void ratio) 분모는 1.+VDR 또는 1.+VDRC이다. 이 함수에는 해당 분모가 0인지 검사하는 조건이 없다.

