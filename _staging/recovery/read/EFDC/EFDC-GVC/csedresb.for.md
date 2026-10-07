---
file: models/EFDC/raw/source_code/EFDC-GVC/csedresb.for
lines: 62
sha256: 66820bf568da2e70f6ba664ee9c88e4524a412c74f7eef0bc60969ba272d1cf4
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# csedresb.for — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | 구분 주석과 `REAL FUNCTION CSEDRESB(DENBULK,WRSPO,VDRO,VDR,VDRC,IOPT)` (6) 선언. EFDC-FULL 1.0a와 2001-11-01 수정 표기, 빈 변경 이력 양식(8–17). EFDC.PAR 포함(19). 바닥 체적 밀도(bed bulk density)와 다른 변수에 따른 응집성 퇴적물(cohesive sediment)의 전체 침식률(bulk erosion rate)을 계산한다는 주석(21–22). 현재 옵션을 사용하지 말라는 문구가 주석에 있다(23). IOPT=1의 Hwang·Mehta 1989와 IOPT=2의 Hamrick 수정·Sanford·Maa 2001 문헌 표기(25–34). |
| 36–62 | 시작 시 6행 CSEDRESB 함수 안. 유일한 실행 대입은 `IF(IOPT.GE.1)CSEDRESB=0.0` (36)이며 IOPT>=1에서 반환값 0. 주석 처리된 IOPT=1 블록은 `C      IF(IOPT.EQ.1)THEN` (38); `C        DENBULK=0.001*DENBULK` (39); `C        IF(DENBULK.LE.1.065)THEN` (40); `C          CSEDRESB=0.62` (41); `C        ELSE` (42); `C          TMP=0.198/(DENBULK-1.0023)` (43); `C          TMP=EXP(TMP)` (44); `C          CSEDRESB=6.4E-4*(10.**TMP)` (45), 종료 주석(46–47). 주석 처리된 IOPT=2는 `C      IF(IOPT.EQ.2)THEN` (49); `C        CSEDRESB=WRSPO*(1.+VDRO)/(1.+VDR)` (50), IOPT=3은 `C      IF(IOPT.EQ.3)THEN` (53); `C        CSEDRESB=WRSPO*(1.+VDRO)/(1.+VDRC)` (54), IOPT=99는 `C      IF(IOPT.EQ.99)THEN` (57); `C        CSEDRESB=WRSPO` (58). 이 식들은 실행되지 않는다. 주석·RETURN·END(59–62). 호출문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 36·61: 반환값을 대입하는 실행문은 IOPT>=1 조건의 CSEDRESB=0.0뿐이다. IOPT<1 경로에서 반환값을 대입하는 문장은 없다.
- 6·38–59: DENBULK/WRSPO/VDRO/VDR/VDRC는 인수 목록에 있다. 해당 인수를 참조하는 계산식은 모두 주석이다.

