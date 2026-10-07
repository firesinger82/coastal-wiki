---
file: models/EFDC/raw/source_code/EFDC-GVC/initbin4.for
lines: 229
sha256: 1a3a51cbfca13caabf48a2ca84f85a6801685846e9e7bb5a678e7acbfe16207c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# initbin4.for — 판독 구간 기록

구간은 1행부터 229행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–61 | 구분 주석과 `SUBROUTINE INITBIN4` 입구(1–9). 작성자·수정일·EFDC-FULL 1.0a·변경 기록 주석(10–27). 저서 플럭스(benthic flux) 출력의 WQSDTS.BIN 이진 파일(binary file)에 후처리기(post-processor) 제어 정보를 헤더(header)로 넣는다는 목적 주석(28–33). `INCLUDE 'EFDC.PAR'` (34), `INCLUDE 'EFDC.CMN'` (35). 포함 파일 내부는 이 판독 대상에 없다. `PARAMETER(MXPARM=30)` (37). 실수 TEND, LCM 크기의 XLON/YLAT, 정수 NPARM/NCELLS, 논리 FEXIST/IS1OPEN/IS2OPEN를 선언한다(38–41). WQNAME/WQUNITS/WQCODE는 각각 길이 20/10/3이며 배열 크기는 MXPARM이다(42–44). 구분 주석과 입력 매개변수 KCSD·ISMTSDT·DT·LA·TBEGAN의 설명(45–54). KCSD를 저서 플럭스 파일에서 1로 강제한다는 주석이 있다(49). NPARM은 WSMTSBIN 출력과 맞춘다는 주석(55–58). NREC4의 전체 자료 출력 간격 주석은 IWQDIUDT를 적는다(59–61). 빈 줄(36). |
| 62–77 | 시작 시 6행 INITBIN4 루틴 안. `NPARM = 8` (62), `NCELLS = LA-1` (63), `NREC4 = 0` (64). TEND에 TBEGIN을 복사한다(65). `KCSD = 1` (66), `MAXRECL4 = 32` (67). 원문 `IF(NPARM .GE. 8)THEN` (68)이면 `MAXRECL4 = NPARM*4` (69); 조건 종료(70). 이름·단위·코드는 WSMTSBIN 출력과 일치시키고 고정 문자열 길이를 지켜야 한다는 주석(71–77). |
| 78–115 | 시작 시 6행 INITBIN4 루틴 안. 20자 이름 안내(78–80). WQNAME(1–8)은 SOD_BENTHIC_FLUX·NH4_BENTHIC_FLUX·NO3_BENTHIC_FLUX·PO4D_BENTHIC_FLUX·SAD_BENTHIC_FLUX·COD_BENTHIC_FLUX·SEDIMENT_TEMPERATURE·BENTHIC_STRESS이다(81–88). 10자 단위 안내(89–92). WQUNITS(1–6)은 G/M2/DAY, 7번은 DEGC, 8번은 DAYS이다(93–100). 3자 코드 안내(101–104). WQCODE(1–8)은 SOD·FNH·FNO·FP4·FSA·FCO·SMT·BST이다(105–112). 구분 주석(113–115). |
| 116–142 | 시작 시 6행 INITBIN4 루틴 안. 기존 WQSDTS.BIN 추가 기록(append) 안내(116–117). 원문 `IF(ISSDBIN .EQ. 2)THEN` (118)이면 `IO = 1` (119), `5       IO = IO+1` (120)로 후보 장치를 늘린다. `IF(IO .GT. 99)THEN` (121)이면 로그 출력 후 `STOP ' EFDC HALTED IN SUBROUTINE INITBIN4'` (123); 조건 종료(124). 장치 사용 여부 조회(125), `IF(IS2OPEN) GOTO 5` (126). 파일 존재 여부 조회(127). 내부 `IF(FEXIST)THEN` (128)이면 장치 IO에 직접 접근(direct access)·비서식(unformatted)·STATUS='UNKNOWN'·RECL=MAXRECL4로 연다(129–130). 발견 로그 출력(131). `READ(IO, REC=1) NREC4, TBEGAN, TEND, DT, ISMTSDT, NPARM,` (132); `+      NCELLS, KCSD` (133)로 헤더를 읽는다. 다음 기록 위치는 `NR6 = 1 + NPARM*3 + NCELLS*4 + (NCELLS*KCSD+1)*NREC4 + 1` (134). 파일 닫기(135). `ELSE` (136)는 `ISSDBIN=1` (137). 두 조건 종료(138–139), 구분 주석(140–142). |
| 143–164 | 시작 시 6행 INITBIN4 루틴 안. 기존 파일 삭제 안내(143–144). 원문 `IF(ISSDBIN .EQ. 1)THEN` (145)이면 TBEGAN에 TBEGIN을 복사한다(146). `IO = 1` (147), `10      IO = IO+1` (148). `IF(IO .GT. 99)THEN` (149)이면 로그 출력 후 `STOP ' EFDC HALTED IN SUBROUTINE INITBIN4'` (151); 조건 종료(152). 장치 사용 여부 조회(153), `IF(IS2OPEN) GOTO 10` (154). 파일 존재 여부 조회(155). 내부 `IF(FEXIST)THEN` (156)이면 WQSDTS.BIN을 열고 STATUS='DELETE'로 닫으며 로그를 출력한다(157–159); 내부 조건 종료(160). 빈 줄(161). 장치 IO에 직접 접근·비서식·STATUS='UNKNOWN'·RECL=MAXRECL4로 새 파일을 연다(162–163). 구분 주석(164). 145행 생성 조건은 이어진다. |
| 165–187 | 시작 시 6행 INITBIN4 루틴·145행 ISSDBIN=1 참 분기 안. 헤더 작성 안내(165–167). NREC4·TBEGAN·TEND·DT·ISMTSDT·NPARM·NCELLS·KCSD를 쓴다(168). `DO I=1,NPARM` (169·172·175)의 세 루프는 WQNAME·WQUNITS·WQCODE를 각각 쓴다(170·173·176); 루프 종료(171·174·177). 셀(cell) 인덱스 대응 안내(178–180). `DO L=2,LA` (181·184)의 두 루프는 IL(L)·JL(L)를 각각 쓴다(182·185); 루프 종료(183·186), 주석(187). |
| 188–213 | 시작 시 6행 INITBIN4 루틴·145행 ISSDBIN=1 참 분기 안. 셀 중심 좌표 입력 안내(188–190). `IO1 = 0` (191), `20      IO1 = IO1+1` (192). `IF(IO1 .GT. 99)THEN` (193)이면 로그 출력 후 `STOP ' EFDC HALTED IN SUBROUTINE INITBIN4'` (195); 조건 종료(196). 장치 사용 여부 조회(197), `IF(IS1OPEN) GOTO 20` (198). 장치 IO1에 LXLY.INP를 STATUS='UNKNOWN'으로 연다(199). `DO NS=1,4` (201)에서 `READ(IO1,1111)` (202)로 앞 네 기록을 건너뛴다; 루프 종료(203), `1111   FORMAT(80X)` (204). `DO LL=1,LVC` (206)에서 I·J·XUTME·YUTMN을 읽는다(207). 대응 인덱스는 `L=LIJ(I,J)` (208). XLON(L)·YLAT(L)에 좌표를 복사한다(209–210). 루프 종료(211), 장치 IO1 닫기(212), 주석(200·205·213). |
| 214–229 | 시작 시 6행 INITBIN4 루틴·145행 ISSDBIN=1 참 분기 안. 좌표 출력 안내(214–216). `DO L=2,LA` (217·220)의 두 루프에서 XLON(L)·YLAT(L)를 쓴다(218·221); 루프 종료(219·222). 빈 줄(223). NEXTREC를 NR6으로 조회하고 장치 IO를 닫는다(224–225). 145행 조건 종료(226), 빈 줄(227), `RETURN` (228), `END` (229). 이 파일에는 CALL문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 50·59–60·132·168: 입력 설명 주석과 헤더 입출력은 출력 간격 변수로 ISMTSDT를 사용한다. NREC4 설명 주석은 IWQDIUDT를 적는다.
- 162–163·168–185·217–221: 새 출력 파일은 ACCESS='DIRECT'로 열린다. 헤더·이름·단위·코드·인덱스·좌표의 WRITE문에는 REC 지정이 없다. 기존 헤더 READ에는 REC=1이 있다(132).
- 62–69·132–133: MAXRECL4는 초기 NPARM=8을 이용해 계산한다. 기존 파일 헤더 READ는 NPARM을 다시 읽는다. 그 뒤 MAXRECL4를 다시 계산하는 문장은 이 파일에 없다.
- 37·42–44·62·66·81–112·132–133: NPARM은 8, KCSD는 1로 초기화한다. 기존 파일 헤더 READ는 NPARM/KCSD를 다시 읽는다. 문자열 배열 크기는 30이며 이 파일의 문자열 대입 범위는 1–8이다. 헤더에서 읽은 NPARM/KCSD의 범위를 검사하는 조건은 이 파일에 없다.
- 39·206–211·217–222: 좌표 입력 루프는 LL=1..LVC이며 실제 배열 인덱스는 LIJ(I,J)이다. 좌표 출력 루프는 L=2..LA이다. 이 블록에는 XLON/YLAT 전체 초기화나 읽은 I/J의 범위 검사 문장이 없다.
