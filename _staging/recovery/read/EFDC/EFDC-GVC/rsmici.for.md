---
file: models/EFDC/raw/source_code/EFDC-GVC/rsmici.for
lines: 100
sha256: 38393cffa229f6d32d1a0d2094caa288cc722866c52ee498bd887cc7455cea9c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# rsmici.for — 판독 구간 기록

구간은 1행부터 100행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | 머리말과 `SUBROUTINE RSMICI(ISMTICI)` (6). 수정일·버전·변경 이력 주석(10–21). 주석은 공간 또는 시간에 따라 달라지는 초기조건(initial conditions)을 INSMICI 단위에서 읽는다고 적는다(26). EFDC.PAR·EFDC.CMN 포함(30–31). NSMGM 크기의 XSMPON·XSMPOP·XSMPOC와 79자 TITLE(3)·3자 ICICONT 선언(33–34). 포함 파일 내부는 판독하지 않았다. |
| 36–52 | 시작 시 6행 RSMICI 안. WQSDICI.INP를 단위 1·STATUS='OLD'로 열고 WQ3D.OUT을 단위 2·append로 연다(36·38). `IF(ISMTICI.EQ.0)THEN` (40)이면 3행 TITLE을 읽어 빈 형식 및 제목과 함께 로그에 쓴다(41–43). 분기 밖에서 ISMTICI와 모델 시작 이후 날짜 메시지를 기록한다(46–47). 한 입력 레코드를 넘긴 뒤 TITLE(1)을 읽고 로그에 쓴다(49–51). 주석·분기 종료 포함. |
| 53–80 | 시작 시 6행 RSMICI 안. `DO M=2,LA` (53)에서 I·J, NSMG개 XSMPON·XSMPOP·XSMPOC, XSM1NH4·XSM2NH4·XSM2NO3·XSM2PO4·XSM2H2S·XSMPSI·XSM2SI·XSMBST·XSMT를 읽고 같은 FORMAT 90으로 로그에 쓴다(55–60). INSMRST READ 대안은 주석(54). `IF(IJCT(I,J).LT.1 .OR. IJCT(I,J).GT.8)THEN` (61)이면 I·J·M-1 출력 후 `STOP 'ERROR!! INVALID (I,J) IN FILE WQSDICI.INP'` (63). 허용 IJCT 범위는 1..8이다. L=LIJ(I,J)(65), MM=1..NSMG에서 입력 임시 배열을 SMPON·SMPOP·SMPOC로 복사한다(66–70). 나머지 9개 입력값을 해당 L의 SM 배열로 복사한다(71–79). M 루프 종료(80). 이 블록은 값을 계산하지 않고 입력값을 복사한다. |
| 81–91 | 시작 시 6행 RSMICI 안이며 M 루프 밖. 다음 ISMTICI·ICICONT를 읽고 로그에 쓴다(82–83). `IF(ICICONT.EQ.'END')THEN` (85)이면 입력 단위 1을 닫고 ISMICI=0으로 설정한다(86–87). 분기 종료(88), 로그 단위 2는 무조건 닫는다(90). 주석 포함. |
| 92–100 | 시작 시 6행 RSMICI 안. FORMAT 999는 1X, 50은 A79, 52는 I7·1X·A3, 60은 날짜 메시지, 84는 3I5·22F8.4, 90은 2I5·22E16.4(92–97). 주석·RETURN·END(98–100). 이 파일에는 서브루틴 CALL이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26·36·55: 입력 단위에 관한 주석은 INSMICI를 적는다. 실제 OPEN·READ는 단위 1을 사용한다.
- 55–65: I·J는 파일에서 읽는다. 유효 셀 검사 자체가 IJCT(I,J)를 참조하며 이 참조 전에 I·J 배열 인덱스 범위를 따로 검사하는 조건은 없다.
- 40–43·82–87: 첫 3행 제목 판독 조건은 ISMTICI=0이다. 끝의 READ는 인수 ISMTICI를 다음 입력값으로 덮어쓴다. 종료 문자열 END는 ISMICI를 0으로 설정한다.
- 36·85–90: 입력 파일 OPEN은 매 호출 실행문이다. 입력 파일 CLOSE는 ICICONT='END' 분기 안에만 있다. 로그 파일 CLOSE는 해당 분기 밖에 있다.
- 96: FORMAT 84가 선언되어 있다. 이 파일의 READ·WRITE는 FORMAT 84를 사용하지 않는다.
