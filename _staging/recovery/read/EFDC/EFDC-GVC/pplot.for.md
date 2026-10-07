---
file: models/EFDC/raw/source_code/EFDC-GVC/pplot.for
lines: 125
sha256: 56ac0ee5b8eaeb6fd72868b4d252b4a9c5f8460f4b275765bef29e2b603f4438
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# pplot.for — 판독 구간 기록

구간은 1행부터 125행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | 구분 주석과 `SUBROUTINE PPLOT (IPT)` 입구(1–6). EFDC-FULL 1.0a·수정일·변경 이력 주석(8–17). `INCLUDE 'EFDC.PAR'`·`INCLUDE 'EFDC.CMN'` (21–22)과 구분 주석(23–25). 포함 파일 내부는 판독하지 않았다. |
| 26–44 | 시작 시 6행 PPLOT 안. BNDU/BNDL은 각각 크기 51이다(26). 문자 BLANK/ASTER·LET1(51)/LET2(51)·CHARY(ICM,JCM)을 선언한다(28). BLANK는 공백, ASTER는 별표로 DATA 초기화한다(30–31). LET1은 A..Y 사이에 공백을 번갈아 넣고 Z로 끝난다(33–37). LET2는 A..Y를 두 번씩 반복하고 Z로 끝난다(39–43). |
| 45–66 | 시작 시 6행 PPLOT 안. 극값 초기값은 `PMAX=-99999.` (45), `PMIN= 99999.` (46). L=2..LA 루프(48)의 `IF(PAM(L) .GT. PMAX) PMAX=PAM(L)` (49), `IF(PAM(L) .LT. PMIN) PMIN=PAM(L)` (50)로 극값을 찾는다. 구간 수의 실수값은 `RNBAN=FLOAT(NBAN)` (53), 구간 폭은 `PINV=(PMAX-PMIN)/RNBAN` (54). BNDU(1)에 PMAX를 복사하고 `BNDL(1)=PMAX-PINV` (59)를 계산한다. M=2..NBAN 루프(61)의 `MM=M-1` (62) 뒤 BNDU(M)에 이전 하한을 복사한다(63). `BNDL(M)=BNDU(M)-PINV` (64)로 연속 구간을 만든다. |
| 67–85 | 시작 시 6행 PPLOT 안. `IF(IPT.EQ.1)THEN` (67)의 M=1..NBAN 루프는 단위 7에 BNDU/LET1/BNDL 범례를 쓴다(68–70). `ELSE` (71)의 루프는 LET2를 쓴다(72–74). 조건 종료·FORMAT 10과 구분 주석을 포함한다(75–78). WRITE(7,11)은 주석이고 FORMAT 11은 남아 있다(79–80). FORMAT 12로 페이지 제어 문자를 출력한다(81–82). 문자 배열 적재 머리말도 포함한다(83–85). |
| 86–95 | 시작 시 6행 PPLOT 안. J=1..JC·I=1..IC 루프(86–87)의 `IF(IJCT(I,J) .NE. 9) CHARY(I,J)=BLANK` (88), `IF(IJCT(I,J) .EQ. 9) CHARY(I,J)=ASTER` (89)로 격자 문자를 초기화한다. 두 루프 종료 뒤 `BNDU(1)=BNDU(1)+1.` (93), `BNDL(NBAN)=BNDL(NBAN)-1.` (94)로 양끝 범위를 1씩 넓힌다. |
| 96–109 | 시작 시 6행 PPLOT 안. L=2..LA 루프에서 I=IL(L)·J=JL(L)을 찾는다(96–98). `IF(IPT.EQ.1)THEN` (99)의 M 루프 조건은 `IF(PAM(L).LT.BNDU(M).AND.PAM(L).GE.BNDL(M)) CHARY(I,J)=LET1(M)` (101). `ELSE` (103)의 조건은 `IF(PAM(L).LT.BNDU(M).AND.PAM(L).GE.BNDL(M)) CHARY(I,J)=LET2(M)` (105). 각 구간은 상한 제외·하한 포함이다. M 루프·IPT 조건·L 루프를 닫는다(102·106–108). |
| 110–125 | 시작 시 6행 PPLOT 안. `DO JJ=1,JC,120` (110)에서 JS=JJ를 복사하고 `JE=JJ+119` (112)를 계산한다. `IF(JE.GT.JC) JE=JC` (113)로 마지막 J를 제한한다. 단위 7에 JS/JE 제목과 I=1..IC별 CHARY의 J=JS..JE 문자를 쓴다(114–118). 80A1의 대체 FORMAT은 주석이고 실제 FORMAT 20은 1X/I3/2X/120A1이다(120–121). FORMAT 22·주석·RETURN·END로 끝난다(122–125). 외부 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26·28·53–54·61·68·72·100·104: 경계값·문자 배열의 크기는 51이다. 구간 수는 NBAN을 사용한다. 이 파일에는 NBAN<=51이나 NBAN>0을 검사하는 조건이 없다.
- 69·73·93–94·101·105: 범례 출력 후 첫 상한과 마지막 하한을 1씩 넓힌다. 문자 선택은 넓힌 경계값을 사용한다.
- 110–122: 문자 출력은 J 방향 120개씩 나눈다. 실제 문자 FORMAT도 120A1로 고정한다.
