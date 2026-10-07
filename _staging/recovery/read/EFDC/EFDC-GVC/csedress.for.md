---
file: models/EFDC/raw/source_code/EFDC-GVC/csedress.for
lines: 79
sha256: e0dfa34d762d31a8e2cc13bad9a9cba3338f47a8057231291902044d39a08010
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# csedress.for — 판독 구간 기록

구간은 1행부터 79행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | 구분 주석과 `REAL FUNCTION CSEDRESS(DENBULK,WRSPO,VDRO,VDR,VDRC,IOPT)` (6) 선언. EFDC-FULL 1.0a·2001-11-01 수정 표기, 빈 변경 이력 양식(8–17), EFDC.PAR 포함(19). 바닥 체적 밀도(bed bulk density)에 따른 응집성 퇴적물(cohesive sediment)의 표면 침식률(surface erosion rate) 계산 주석(21–22). IOPT=1은 Hwang·Mehta 1989, IOPT=2/3은 Hamrick 수정·Sanford·Maa 2001, IOPT=4/5는 SEDFLUME 시험자료 매개변수화라는 주석(24–36). 빈 줄(38). |
| 39–61 | 시작 시 6행 CSEDRESS 함수 안. `IF(IOPT.EQ.1)THEN` (39)에서 `DENBULK=0.001*DENBULK` (40), 내부 `IF(DENBULK.LE.1.065)THEN` (41)이면 `CSEDRESS=0.62` (42), ELSE(43)는 `TMP=0.198/(DENBULK-1.0023)` (44); `TMP=EXP(TMP)` (45); `CSEDRESS=6.4E-4*(10.**TMP)` (46). 독립 `IF(IOPT.EQ.2)THEN` (50)의 식 `CSEDRESS=WRSPO*(1.+VDRO)/(1.+VDR)` (51). 독립 `IF(IOPT.EQ.3)THEN` (54)의 식 `CSEDRESS=WRSPO*(1.+VDRO)/(1.+VDRC)` (55). IOPT=3의 다른 식 `c      IF(IOPT.EQ.3)THEN` (58); `c        CSEDRESS=WRSPO*(1.+VDRO)/(1.+VDR)` (59)는 주석이며 실행되지 않는다. 각 ENDIF·구분 주석(47–49·52–53·56–61). |
| 62–79 | 시작 시 6행 CSEDRESS 함수 안. `IF(IOPT.EQ.4)THEN` (62)에서 `TMPVAL=(1.+VDRO)/(1.+VDR)` (63); `FACTOR=EXP(-TMPVAL)` (64); `CSEDRESS=FACTOR*WRSPO*(1.+VDRO)/(1.+VDR)` (65). `IF(IOPT.EQ.5)THEN` (68)에서 `TMPVAL=(1.+VDRO)/(1.+VDRC)` (69); `FACTOR=EXP(-TMPVAL)` (70); `CSEDRESS=FACTOR*WRSPO*(1.+VDRO)/(1.+VDRC)` (71). 두 옵션은 VDRO와 VDR/VDRC로 계산한 비율에 지수 감쇠 계수를 곱한다. `IF(IOPT.GE.99)THEN` (74)에서 CSEDRESS=WRSPO 복사(75). 각 분기 종료·주석과 RETURN·END(66–67·72–73·76–79). 호출문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 39–40: IOPT=1 경로는 입력 인수 DENBULK 자체에 0.001*DENBULK를 대입한다.
- 39–76: 반환값 대입은 IOPT=1..5 또는 IOPT>=99 경로에만 있다. 그 밖의 IOPT에 대한 기본 반환값 대입은 없다.
- 54–60: 실행 IOPT=3 식의 분모는 1.+VDRC이다. 바로 뒤 주석 처리된 IOPT=3 식의 분모는 1.+VDR이다.
