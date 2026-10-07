---
file: models/EFDC/raw/source_code/EFDC-GVC/initbin2.for
lines: 240
sha256: e1bc5a08d12ab9d06067095609114c638b0bed33a49c3d8dc7f48b4822d82f9b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# initbin2.for — 판독 구간 기록

구간은 1행부터 240행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–61 | 구분 주석과 `SUBROUTINE INITBIN2` 입구(1–9). 작성자·수정일·EFDC-FULL 1.0a·변경 기록 주석(10–27). 일주기 용존산소(diurnal dissolved oxygen) 계산의 WQDIURDO.BIN 이진 파일(binary file)에 후처리기(post-processor) 제어 정보를 헤더(header)로 넣는다는 목적 주석(28–34). `INCLUDE 'EFDC.PAR'` (35), `INCLUDE 'EFDC.CMN'` (36). 포함 파일 내부는 이 판독 대상에 없다. `PARAMETER(MXPARM=30)` (38). 실수 TEND, LCM 크기의 XLON/YLAT, 정수 NPARM/NCELLS, 논리 FEXIST를 선언한다(39–42). WQNAME/WQUNITS/WQCODE는 각각 길이 20/10/3이며 배열 크기는 MXPARM이다(43–45). 입력 매개변수 KC·IWQDIUDT·DT·LA·TBEGAN을 설명한다(48–54). NPARM은 WWQTSBIN 출력과 맞추고 NREC2는 전체 자료 출력 횟수로 사용한다는 주석(55–61). 빈 줄·주석을 포함한다(37·46–47). |
| 62–76 | 시작 시 6행 INITBIN2 루틴 안. `NPARM = 20` (62), `NCELLS = LA-1` (63), `NREC2 = 0` (64). TEND에 TBEGIN을 복사한다(65). `MAXRECL2 = 32` (66). 원문 `IF(NPARM .GE. 8)THEN` (67)이면 `MAXRECL2 = NPARM*4` (68); 조건 종료(69). 이름·단위·코드는 WWQTSBIN 출력과 일치시키고 고정 문자열 길이를 지켜야 한다는 주석(70–76). |
| 77–124 | 시작 시 6행 INITBIN2 루틴 안. 20자 이름 안내(77–79). WQNAME(1–20)은 SALINITY·TEMPERATURE·DO_SATURATION·DISSOLVED_OXYGEN·SED_OXYGEN_DEMAND·KA_REAERATION·LAYER_THICKNESS·PRIM_PRODUCTION_CYA·RESPIRATION_CYA·PRIM_PRODUCTION_DIA·RESPIRATION_DIA·PRIM_PRODUCTION_GRN·RESPIRATION_GRN·PRIM_PRODUCTION_MAC·RESPIRATION_MAC·ALGAE_CYANOBACTERIA·ALGAE_DIATOMS·ALGAE_GREENS·TOTAL_CHLOROPHYLLA·MACROALGAE이다(80–99). 10자 단위 안내(100–103). WQUNITS는 1번 G/L, 2번 DEGC, 3·4번 MG/L, 5번 G/M2/DAY, 6번 PER_DAY, 7번 METERS, 8–15번 MGO2/L/DAY, 16–20번 UG/L이다(104–123). 주석(124). |
| 125–150 | 시작 시 6행 INITBIN2 루틴 안. 3자 코드 안내(125–127). WQCODE(1–20)은 SAL·TEM·DOS·DOO·SOD·RKA·DEP·PPC·RRC·PPD·RRD·PPG·RRG·PPM·RRM·CYA·DIA·GRN·CHL·MAC이다(128–147). 구분 주석(148–150). |
| 151–169 | 시작 시 6행 INITBIN2 루틴 안. 기존 WQDIURDO.BIN 추가 기록(append) 안내(151–152). 원문 `IF(ISDIURDO .EQ. 2)THEN` (153) 안에서 파일 존재 여부를 조회한다(154). 내부 `IF(FEXIST)THEN` (155)이면 장치 2에 직접 접근(direct access)·비서식(unformatted)·STATUS='UNKNOWN'·RECL=MAXRECL2로 연다(156–157). 발견 로그 출력(158). `READ(2, REC=1) NREC2, TBEGAN, TEND, DT, IWQDIUDT, NPARM,` (159); `+      NCELLS, KC` (160)로 기존 헤더를 읽는다. 다음 기록 위치는 `NR4 = 1 + NPARM*3 + NCELLS*4 + (NCELLS*KC+1)*NREC2 + 1` (161). 파일 닫기(162). `ELSE` (163)는 `ISDIURDO=1` (164). 두 조건 종료(165–166), 구분 주석(167–169). |
| 170–197 | 시작 시 6행 INITBIN2 루틴 안. 기존 파일 삭제 안내(170–171). 원문 `IF(ISDIURDO .EQ. 1)THEN` (172)이면 TBEGAN에 TBEGIN을 복사하고 파일 존재 여부를 조회한다(173–174). 내부 `IF(FEXIST)THEN` (175)이면 기존 WQDIURDO.BIN을 열고 STATUS='DELETE'로 닫으며 로그를 출력한다(176–178); 내부 조건 종료(179). 빈 줄(180). 장치 2에 직접 접근·비서식·STATUS='UNKNOWN'·RECL=MAXRECL2로 연다(181–182). 헤더 안내 주석은 WQWCAVG.BIN이라고 적는다(183–186). NREC2·TBEGAN·TEND·DT·IWQDIUDT·NPARM·NCELLS·KC를 쓴다(187). `DO I=1,NPARM` (188·191·194)의 세 루프는 WQNAME·WQUNITS·WQCODE를 각각 쓴다(189·192·195); 루프 종료(190·193·196), 주석(197). 172행 생성 조건은 이어진다. |
| 198–224 | 시작 시 6행 INITBIN2 루틴·172행 ISDIURDO=1 참 분기 안. 셀(cell) 인덱스 대응 안내(198–199). `DO L=2,LA` (200·203)의 두 루프는 IL(L)·JL(L)를 각각 쓴다(201·204); 루프 종료(202·205). 셀 중심 좌표 입력 안내(206–209). 장치 1에 LXLY.INP를 STATUS='UNKNOWN'으로 연다(210). `DO NS=1,4` (212)에서 `READ(1,1111)` (213)로 앞 네 기록을 건너뛴다; 루프 종료(214), `1111   FORMAT(80X)` (215). `DO LL=1,LVC` (217)에서 I·J·XUTME·YUTMN을 읽는다(218). 대응 인덱스는 `L=LIJ(I,J)` (219). XLON(L)·YLAT(L)에 좌표를 복사한다(220–221). 루프 종료(222), 장치 1 닫기(223), 주석(211·216·224). |
| 225–240 | 시작 시 6행 INITBIN2 루틴·172행 ISDIURDO=1 참 분기 안. 좌표 출력 안내(225–227). `DO L=2,LA` (228·231)의 두 루프에서 XLON(L)·YLAT(L)를 쓴다(229·232); 루프 종료(230·233). 빈 줄(234). NEXTREC를 NR4로 조회하고 장치 2를 닫는다(235–236). 172행 조건 종료(237), 빈 줄(238), `RETURN` (239), `END` (240). 이 파일에는 CALL문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 181–185: OPEN의 실제 파일명은 WQDIURDO.BIN이다. 그 뒤 헤더 작성 주석의 파일명은 WQWCAVG.BIN이다.
- 181–182·187–204·228–232: 새 출력 파일은 ACCESS='DIRECT'로 열린다. 헤더·이름·단위·코드·인덱스·좌표의 WRITE문에는 REC 지정이 없다. 기존 헤더 READ에는 REC=1이 있다(159).
- 62–68·159–160: MAXRECL2는 초기 NPARM=20을 이용해 계산한다. 기존 파일 헤더 READ는 NPARM을 다시 읽는다. 그 뒤 MAXRECL2를 다시 계산하는 문장은 이 파일에 없다.
- 38·43–45·80–147·159–160: 문자열 배열 크기는 30이다. 이 파일의 이름·단위·코드 대입 범위는 1–20이다. 기존 헤더에서 읽은 NPARM에 대해 배열 크기 또는 대입 범위를 검사하는 조건은 이 파일에 없다.
- 40·217–222·228–233: 좌표 입력 루프는 LL=1..LVC이며 실제 배열 인덱스는 LIJ(I,J)이다. 좌표 출력 루프는 L=2..LA이다. 이 블록에는 XLON/YLAT 전체 초기화나 읽은 I/J의 범위 검사 문장이 없다.
