---
file: models/EFDC/raw/source_code/EFDC-GVC/initbin0.for
lines: 229
sha256: 73a4e04b427eceab9b08393742363b399f859c6e9fe5727d32fbcb2a167d0788
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# initbin0.for — 판독 구간 기록

구간은 1행부터 229행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–60 | 구분 주석과 `SUBROUTINE INITBIN0` 입구(1–9). 작성자·수정일·EFDC-FULL 1.0a·변경 기록 주석(10–27). 유체동역학(hydrodynamics) 변수의 HYDTS.BIN 이진 파일(binary file)에 후처리기(post-processor) 제어 정보를 헤더(header)로 넣는다는 목적 주석(28–33). `INCLUDE 'EFDC.PAR'` (34), `INCLUDE 'EFDC.CMN'` (35). 포함 파일 내부는 이 판독 대상에 없다. `PARAMETER(MXPARM=30)` (37). 실수 TEND, LCM 크기의 XLON/YLAT, 정수 NPARM/NCELLS, 논리 FEXIST/IS1OPEN/IS2OPEN를 선언한다(38–41). HYNAME/HYUNITS/HYCODE는 각각 길이 20/10/3이며 배열 크기는 MXPARM이다(42–44). 입력 매개변수 KCHYD·NWTMSR·DT·LA·TBEGAN을 설명하는 주석(46–53). KCHYD를 여기서 1로 강제한다는 주석이 있다(48). NPARM은 TMSRBIN 출력과 맞추고 NREC0은 전체 자료 출력 횟수로 사용한다는 주석(54–60). |
| 61–76 | 시작 시 6행 INITBIN0 루틴 안. `NPARM = 8` (61), `NCELLS = LA-1` (62), `NREC0 = 0` (63). TEND에 TBEGIN을 복사한다(64). `KCHYD = 1` (65), `MAXRECL0 = 32` (66). 원문 `IF(NPARM .GE. 8)THEN` (67)이면 `MAXRECL0 = NPARM*4` (68); 조건 종료(69). 이름·단위·코드는 TMSRBIN 출력과 맞추고 문자열 길이를 지켜야 한다는 주석(70–76). 주석은 이 항목들을 WATER QUALITY라고 부른다(71). |
| 77–114 | 시작 시 6행 INITBIN0 루틴 안. 20자 이름 안내(77–79). HYNAME(1–8)은 SURFACE_ELEVATION·WATER_DEPTH·VELOCITY-X·VELOCITY-Y·FLOW-X·FLOW-Y·BOTTOM_ELEVATION·BOTTOM_ROUGHNESS이다(80–87). 10자 단위 안내(88–91). HYUNITS는 1·2·7·8번 METERS, 3·4번 CM/SEC, 5·6번 M3/SEC이다(92–99). 3자 코드 안내(100–103). HYCODE(1–8)은 SEL·DEP·VXX·VYY·QXX·QYY·BEL·ZBR이다(104–111). 끝 구분 주석(112–114). |
| 115–139 | 시작 시 6행 INITBIN0 루틴 안. 기존 HYDTS.BIN 추가 기록(append) 안내(115–116). 원문 `IF(ISTMSR .EQ. 2)THEN` (117)이면 `IO = 1` (118), `5       IO = IO+1` (119)로 후보 장치를 늘린다. `IF(IO .GT. 99)THEN` (120)이면 로그 출력 후 `STOP ' EFDC HALTED IN SUBROUTINE INITBIN0'` (122); 조건 종료(123). 장치 사용 여부 조회(124), `IF(IS2OPEN) GOTO 5` (125)로 사용 중인 장치를 건너뛴다. 파일 존재 여부 조회(126). 내부 `IF(FEXIST)THEN` (127)이면 장치 IO에 직접 접근(direct access)·비서식(unformatted)·STATUS='UNKNOWN'·RECL=MAXRECL4로 연다(128–129). 발견 로그 출력(130). `READ(IO, REC=1) NREC0, TBEGAN, TEND, DT, NWTMSR, NPARM,` (131); `+      NCELLS, KCHYD` (132)로 헤더를 읽는다. 다음 기록 위치는 `NR0 = 1 + NPARM*3 + NCELLS*4 + (NCELLS*KCHYD+1)*NREC0 + 1` (133). 파일 닫기(134). `ELSE` (135)는 `ISTMSR=1` (136). 두 조건 종료(137–138), 주석(139). |
| 140–163 | 시작 시 6행 INITBIN0 루틴 안. 기존 파일 삭제 안내(140–143). 원문 `IF(ISTMSR .EQ. 1)THEN` (144)이면 TBEGAN에 TBEGIN을 복사한다(145). `IO = 1` (146), `10      IO = IO+1` (147). `IF(IO .GT. 99)THEN` (148)이면 로그 출력 후 `STOP ' EFDC HALTED IN SUBROUTINE INITBIN0'` (150); 조건 종료(151). 장치 사용 여부 조회(152), `IF(IS2OPEN) GOTO 10` (153). 파일 존재 여부 조회(154). 내부 `IF(FEXIST)THEN` (155)이면 HYDTS.BIN을 열고 STATUS='DELETE'로 닫으며 로그를 출력한다(156–158); 내부 조건 종료(159). 빈 줄(160). 장치 IO에 직접 접근·비서식·STATUS='UNKNOWN'·RECL=MAXRECL0로 새 파일을 연다(161–162). 주석(163). 144행 생성 조건은 이어진다. |
| 164–187 | 시작 시 6행 INITBIN0 루틴·144행 ISTMSR=1 참 분기 안. 헤더 작성 안내(164–167). NREC0·TBEGAN·TEND·DT·NWTMSR·NPARM·NCELLS·KCHYD를 쓴다(168). `DO I=1,NPARM` (169·172·175)의 세 루프는 HYNAME·HYUNITS·HYCODE를 각각 쓴다(170·173·176); 루프 종료(171·174·177). 셀(cell) 인덱스 대응 안내(178–180). `DO L=2,LA` (181·184)의 두 루프는 IL(L)·JL(L)를 각각 쓴다(182·185); 루프 종료(183·186), 주석(187). |
| 188–213 | 시작 시 6행 INITBIN0 루틴·144행 ISTMSR=1 참 분기 안. 셀 중심 좌표 입력 안내(188–190). `IO1 = 0` (191), `20      IO1 = IO1+1` (192). `IF(IO1 .GT. 99)THEN` (193)이면 로그 출력 후 `STOP ' EFDC HALTED IN SUBROUTINE INITBIN0'` (195); 조건 종료(196). 장치 사용 여부 조회(197), `IF(IS1OPEN) GOTO 20` (198). 장치 IO1에 LXLY.INP를 STATUS='UNKNOWN'으로 연다(199). `DO NS=1,4` (201)에서 `READ(IO1,1111)` (202)로 앞 네 기록을 건너뛴다; 루프 종료(203), `1111   FORMAT(80X)` (204). `DO LL=2,LA` (206)에서 I·J·XUTME·YUTMN을 읽는다(207). 대응 인덱스는 `L=LIJ(I,J)` (208). XLON(L)·YLAT(L)에 좌표를 복사한다(209–210). 루프 종료(211), 장치 IO1 닫기(212), 주석(200·205·213). |
| 214–229 | 시작 시 6행 INITBIN0 루틴·144행 ISTMSR=1 참 분기 안. 좌표 출력 안내(214–216). `DO L=2,LA` (217·220)의 두 루프에서 XLON(L)·YLAT(L)를 쓴다(218·221); 루프 종료(219·222). 빈 줄(223). NEXTREC를 NR0으로 조회하고 장치 IO를 닫는다(224–225). 144행 조건 종료(226), 주석(227), `RETURN` (228), `END` (229). 이 파일에는 CALL문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 66–68·128–129·161–162: 이 루틴은 MAXRECL0을 계산한다. 기존 HYDTS.BIN을 여는 분기는 RECL=MAXRECL4를 사용한다. 새 HYDTS.BIN을 여는 분기는 RECL=MAXRECL0을 사용한다. 이 파일에는 MAXRECL4 대입문이 없다.
- 161–162·168–185·217–221: 새 출력 파일은 ACCESS='DIRECT'로 열린다. 헤더·이름·단위·코드·인덱스·좌표의 WRITE문에는 REC 지정이 없다. 기존 헤더 READ에는 REC=1이 있다(131).
- 37·42–44·61·65·80–111·131–132: NPARM은 8, KCHYD는 1로 초기화한다. 기존 파일 헤더 READ는 NPARM/KCHYD를 다시 읽는다. 문자열 배열 크기는 30이며 이 파일의 문자열 대입 범위는 1–8이다. 헤더에서 읽은 NPARM/KCHYD의 범위를 검사하는 조건은 이 파일에 없다.
- 39·206–211·217–222: 좌표 입력 루프의 제어 변수는 LL이지만 실제 배열 인덱스는 읽은 I/J의 LIJ(I,J) 값이다. 이 블록에는 I/J 범위 검사나 XLON/YLAT 전체 초기화가 없다. 이후 좌표 출력 루프는 L=2..LA를 사용한다.
