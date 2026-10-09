---
file: models/ADCIRC/raw/source_code/adcirc/prep/diffmerge.F
lines: 606
sha256: 3611f267d92f80d9073b1016b89e03c5f2abebba16fcd87418c12ba32d7839e1
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# diffmerge.F — 판독 구간 기록

구간은 1행부터 606행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | ADCIRC 저작권·LGPL 3 이상·무보증 머리말(1–19). 버전 1.1 이력과 빈 줄(20–23). |
| 24–59 | `DIFFMERGE63(DIR1,DIR2,SCALEFAC)` 선언(24). 두 디렉터리의 전역 수위 자료 차이에 사용자가 준 배율(scale factor)을 적용한다는 주석(26–38). POST_GLOBAL 및 정수·실수·문자·논리 변수 선언(40–55). ETA1·ETA2는 REAL(8)이며 MNP 크기로 할당한다(57–58). |
| 60–86 | 시작 시 24행 DIFFMERGE63 안. 디렉터리 문자열 루프(62·68)의 `IF (DIR1(I:I).EQ.' ') THEN` (63), `IF (DIR2(I:I).EQ.' ') THEN` (69)이면 각각 `LEN1 = I-1` (64), `LEN2 = I-1` (70)로 첫 공백 앞에서 잘라 루프를 탈출한다. 입력 이름은 디렉터리 뒤 /fort.63, 출력은 diffmerge.63이다(75–77). `IF (ABS(NOUTGE).EQ.1) THEN` (81)이면 1000으로 이동한다. `ELSE` (83)는 2000으로 이동한다. |
| 87–134 | 시작 시 24행 DIFFMERGE63 안이며 1000 순차 서식(sequential formatted) 경로. `IF (FOUND1.AND.FOUND2) THEN` (93)이면 입력 53·63과 출력 73을 연다. `ELSE` (97)는 메시지 후 반환한다. 두 제목을 INLINE에 순서대로 읽고 마지막 INLINE을 출력한다(102–104). 헤더를 읽은 뒤 `IF (NDSETGE1.NE.NDSETGE2) THEN` (109), `IF (NP1.NE.NP2) THEN` (114), `IF (ABS(DTE1-DTE2).GT.1.0E-5) THEN` (119), `IF (NSTEMP1.NE.NSTEMP2) THEN` (124), `IF (ITEMPE1.NE.ITEMPE2) THEN` (128)은 각각 메시지 후 반환한다. 시간 간격 차이의 허용 검사값은 원문 1.0E-5이다. 첫 파일 헤더를 출력한다(133). |
| 135–160 | 시작 시 24행 DIFFMERGE63 안. 자료 집합 J 루프(135)에서 두 시간·단계 번호를 읽는다(137–138). `IF (ABS(TIMEOUTE1-TIMEOUTE2).GT.1.0E-5) THEN` (140), `IF (ITE1.NE.ITE2) THEN` (145)이면 메시지 후 반환한다. 시간·단계 번호를 출력하고 I=1..NNODG 루프에서 두 수위를 읽는다. 계산·출력 원문은 `WRITE(73,2453) I,SCALEFAC*(ETA1(I)-ETA2(I))` (155)이다. 자료 집합 루프 뒤 9999로 이동한다(159). |
| 161–213 | 시작 시 24행 DIFFMERGE63 안이며 2000 직접 접근 이진(direct access binary) 경로 주석(163). `IF (FOUND1.AND.FOUND2) THEN` (167)이면 ACCESS='DIRECT', RECL=NBYTE로 53·63·73을 연다. `ELSE` (171)는 메시지 후 반환한다. 첫 파일의 설명·실행 ID·격자 ID를 출력에 복사한다. `IF (NBYTE.EQ.4) THEN` (179)은 8·6·6개 문자 레코드를 처리하며 `IREC1=IREC1+8` (184), `IREC1=IREC1+6` (189·194)이다. `IF (NBYTE.EQ.8) THEN` (196)은 4·3·3개 레코드와 `IREC1=IREC1+4` (201), `IREC1=IREC1+3` (206·211)이다. |
| 214–246 | 시작 시 24행 DIFFMERGE63 안. 둘째 파일의 설명·실행 ID·격자 ID를 읽는다. `IF (NBYTE.EQ.4) THEN` (217)은 8·6·6개 레코드와 `IREC2=IREC2+8` (221), `IREC2=IREC2+6` (225·229)이다. `IF (NBYTE.EQ.8) THEN` (231)은 4·3·3개 레코드와 `IREC2=IREC2+4` (235), `IREC2=IREC2+3` (239·243)이다. |
| 247–276 | 시작 시 24행 DIFFMERGE63 안. 첫 파일의 자료 집합 수·노드 수·시간 간격·주기·자료형을 읽고 출력에 복사한다(251–260). `IREC1 = IREC1+5` (261), 둘째 파일 헤더 판독 후 `IREC2 = IREC2+5` (268)이다. 세 파일을 닫고 직접 접근으로 다시 연다(270–275). 출력 장치 재개 원문은 `OPEN(73,FILE=FNAME2,ACCESS='DIRECT',RECL=NBYTE)` (275)이다. |
| 277–313 | 시작 시 24행 DIFFMERGE63 안. J=1..NDSETGE1 루프(277)는 첫 파일 시간·단계 번호를 출력에 복사하고 `IREC1 = IREC1+2` (283), 둘째 파일을 읽고 `IREC2 = IREC2+2` (287)이다. 노드 루프의 계산·출력은 `WRITE(73,REC=IREC1+I)  I,SCALEFAC*(ETA1(I)-ETA2(I))` (292)이다. 다음 집합 위치는 `IREC1 = IREC1 + NNODG` (294), `IREC2 = IREC2 + NNODG` (295)이다. 9999에서 세 장치를 닫고(301–304) 서식 선언·RETURN·루틴 종료를 둔다(306–312). |
| 314–351 | `DIFFMERGE64` 선언(314), 두 디렉터리의 전역 속도 차이를 생성한다는 주석(316–328). POST_GLOBAL·변수 선언(330–345). UU1/VV1 및 UU2/VV2는 REAL(8)이며 각각 MNP 크기로 할당한다(347–350). |
| 352–378 | 시작 시 314행 DIFFMERGE64 안. `IF (DIR1(I:I).EQ.' ') THEN` (355), `IF (DIR2(I:I).EQ.' ') THEN` (361)이면 `LEN1 = I-1` (356), `LEN2 = I-1` (362)로 디렉터리 길이를 정한다. 입력은 /fort.64, 출력은 diffmerge.64이다(367–369). `IF (ABS(NOUTGV).EQ.1) THEN` (373)은 1000으로 이동한다. `ELSE` (375)는 2000으로 이동한다. |
| 379–426 | 시작 시 314행 DIFFMERGE64 안이며 1000 순차 서식(sequential formatted) 경로. `IF (FOUND1.AND.FOUND2) THEN` (385)이면 54·64·74를 연다. `ELSE` (389)는 메시지 후 반환한다. 두 제목 중 둘째를 출력하고 두 헤더를 읽는다(394–399). `IF (NDSETGV1.NE.NDSETGV2) THEN` (401), `IF (NP1.NE.NP2) THEN` (406), `IF (ABS(DTV1-DTV2).GT.1.0E-5) THEN` (411), `IF (NSTEMP1.NE.NSTEMP2) THEN` (416), `IF (ITEMPV1.NE.ITEMPV2) THEN` (420)은 각각 메시지 후 반환한다. 첫 파일 헤더를 출력한다(425). |
| 427–453 | 시작 시 314행 DIFFMERGE64 안. J=1..NDSETGV1 루프(427)는 시간·단계 번호를 읽는다. `IF (ABS(TIMEOUTV1-TIMEOUTV2).GT.1.0E-5) THEN` (432), `IF (ITV1.NE.ITV2) THEN` (437)은 메시지 후 반환한다. I=1..NNODG 루프에서 두 속도 성분을 읽는다(444–446). 출력 원문은 `WRITE(74,2454) I,SCALEFAC*(UU1(I)-UU2(I)),` (447), `&          SCALEFAC*(VV1(I)-VV2(I))` (448)이다. 루프 뒤 9999로 이동한다(452). |
| 454–506 | 시작 시 314행 DIFFMERGE64 안이며 2000 직접 접근 경로. `IF (FOUND1.AND.FOUND2) THEN` (460)이면 ACCESS='DIRECT', RECL=NBYTE로 세 파일을 연다. `ELSE` (464)는 메시지 후 반환한다. 첫 파일 문자 헤더를 출력에 복사한다. `IF (NBYTE.EQ.4) THEN` (472)은 8·6·6개 레코드와 `IREC1=IREC1+8` (477), `IREC1=IREC1+6` (482·487)이다. `IF (NBYTE.EQ.8) THEN` (489)은 4·3·3개 레코드와 `IREC1=IREC1+4` (494), `IREC1=IREC1+3` (499·504)이다. |
| 507–538 | 시작 시 314행 DIFFMERGE64 안. 둘째 파일 문자 헤더를 읽는다. `IF (NBYTE.EQ.4) THEN` (510)은 8·6·6개 레코드와 `IREC2=IREC2+8` (514), `IREC2=IREC2+6` (518·522)이다. `IF (NBYTE.EQ.8) THEN` (524)은 4·3·3개 레코드와 `IREC2=IREC2+4` (528), `IREC2=IREC2+3` (532·536)이다. |
| 539–567 | 시작 시 314행 DIFFMERGE64 안. 첫 파일 수치 헤더 5개를 읽어 출력하고 `IREC1 = IREC1+5` (552)이다. 둘째 파일 헤더 판독 후 `IREC2 = IREC2+5` (559)이다. 세 장치를 닫고 다시 연다(561–566). 출력 장치 74는 FNAME3로 재개한다(566). |
| 568–606 | 시작 시 314행 DIFFMERGE64 안. J 루프(568)는 첫 파일 시간·단계 번호를 출력하고 `IREC1 = IREC1+2` (574), 둘째 파일 판독 후 `IREC2 = IREC2+2` (578)이다. I 루프(580)는 홀수 레코드의 U, 짝수 레코드의 V를 읽는다(581–584). 계산·출력은 `WRITE(74,REC=IREC1+2*I-1) SCALEFAC*(UU1(I)-UU2(I))` (585), `WRITE(74,REC=IREC1+2*I)   SCALEFAC*(VV1(I)-VV2(I))` (586)이다. `IREC1 = IREC1 + 2*NNODG` (588), `IREC2 = IREC2 + 2*NNODG` (589)로 이동한다. 9999에서 파일을 닫고 서식 선언·RETURN·종료를 둔다(595–606). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 62–73 및 354–365: LEN1·LEN2 대입은 문자열에서 공백을 찾는 분기 안에만 있다. 공백을 찾지 못했을 때의 별도 길이 설정은 없다.
- 102–104·176–212 및 394–396·469–505: 순차 서식 출력 제목은 둘째 입력의 INLINE이다. 직접 접근 출력 문자 헤더는 첫째 입력에서 복사한다. 두 문자 헤더를 비교하는 조건은 없다.
- 114–117·152–155 및 406–409·444–448: NP1과 NP2의 일치는 검사한다. 노드 자료 루프의 상한은 NNODG이다. 읽은 노드 식별자 IDUM을 비교하거나 출력 번호로 사용하는 문장은 없다.
- 251–297 및 542–591: 직접 접근 경로에는 순차 서식 경로의 헤더 일치·시간 일치·단계 번호 일치 조건 검사가 없다.
- 170·275: DIFFMERGE63은 처음 출력 장치 73을 FNAME3로 연다. 재개할 때는 FNAME2로 연다.
- 290–292: 직접 접근 수위 입력은 각 레코드에서 ETA 하나를 읽는다. 출력은 같은 레코드에 정수 I와 배율을 곱한 수위 차이를 함께 쓴다.
- 168–170·273–275·461–463·564–566: 직접 접근 OPEN은 ACCESS와 RECL을 지정한다. 해당 OPEN 문장에는 FORM 지정이 없다.
- 109–131·140–147 및 401–423·432–439: 순차 서식 자료 불일치 분기는 RETURN으로 끝난다. 해당 분기는 파일 닫기 구간(301–304·595–598)을 실행하기 전에 반환한다.
