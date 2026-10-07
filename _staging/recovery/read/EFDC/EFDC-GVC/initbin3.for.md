---
file: models/EFDC/raw/source_code/EFDC-GVC/initbin3.for
lines: 304
sha256: 489f75d7b4b8ef5e0393fbf79a8c024d3faa685ddd3ee363459eb46462d5c201
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# initbin3.for — 판독 구간 기록

구간은 1행부터 304행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–62 | 구분 주석과 `SUBROUTINE INITBIN3` 입구(1–9). 작성자·수정일·EFDC-FULL 1.0a·변경 기록 주석(10–27). 용존산소(dissolved oxygen) 성분 분석의 WQDOCOMP.BIN 이진 파일(binary file)에 후처리기(post-processor) 제어 정보를 헤더(header)로 넣는다는 목적 주석(28–34). `INCLUDE 'EFDC.PAR'` (35), `INCLUDE 'EFDC.CMN'` (36). 포함 파일 내부는 이 판독 대상에 없다. `PARAMETER(MXPARM=33)` (38). 실수 TEND, LCM 크기의 XLON/YLAT, 정수 NPARM/NCELLS, 논리 FEXIST/IS1OPEN/IS2OPEN를 선언한다(39–42). WQNAME/WQUNITS/WQCODE는 각각 길이 20/10/3이며 배열 크기는 MXPARM이다(43–45). 구분 주석과 입력 매개변수 KC·IWQTSDT·DT·LA·TBEGAN의 설명(46–55). NPARM은 WWQTSBIN 출력과 맞춘다는 주석(56–59). NREC3의 전체 자료 출력 간격 주석은 IWQDIUDT를 적는다(60–62). 빈 줄(37). |
| 63–77 | 시작 시 6행 INITBIN3 루틴 안. `NPARM = 33` (63), `NCELLS = LA-1` (64), `NREC3 = 0` (65). TEND에 TBEGIN을 복사한다(66). `MAXRECL3 = 32` (67). 원문 `IF(NPARM .GE. 8)THEN` (68)이면 `MAXRECL3 = NPARM*4` (69); 조건 종료(70). 이름·단위·코드는 WWQTSBIN 출력과 일치시키고 고정 문자열 길이를 지켜야 한다는 주석(71–77). |
| 78–114 | 시작 시 6행 INITBIN3 루틴 안. 20자 이름 안내(78–80). WQNAME(1–4)는 NITROGEN_LIMIT_CYA·NITROGEN_LIMIT_DIA·NITROGEN_LIMIT_GRN·NITROGEN_LIMIT_MAC이다(81–84). WQNAME(5–8)는 PHOSPHORUS_LIMIT_CYA·PHOSPHORUS_LIMIT_DIA·PHOSPHORUS_LIMIT_GRN·PHOSPHORUS_LIMIT_MAC이다(85–88). WQNAME(9–12)는 LIGHT_LIMIT_CYA·LIGHT_LIMIT_DIA·LIGHT_LIMIT_GRN·LIGHT_LIMIT_MAC이다(89–92). WQNAME(13–16)는 TEMP_LIMIT_CYA·TEMP_LIMIT_DIA·TEMP_LIMIT_GRN·TEMP_LIMIT_MAC이다(93–96). WQNAME(17–18)는 VELOCITY_LIMIT_MAC·DENSITY_LIMIT_MAC이다(97–98). WQNAME(19–33)은 DO_SATURATION·DO_POINT_SOURCES·DO_SED_OXYGEN_DEMAND·DO_REAERATION·DO_DOC_DECAY·DO_NH4_NITRIFICATION·DO_COD_OXIDATION·DO_PHOTOSYNTH_CHL·DO_RESPIRATION_CHL·DO_PHOTOSYNTH_MAC·DO_RESPIRATION_MAC·DO_DEFICIT·DO_TRANSPORT·DO_ALL_COMPONENTS·LAYER_THICKNESS이다(99–113). 주석(114). |
| 115–151 | 시작 시 6행 INITBIN3 루틴 안. 10자 단위 안내(115–117). WQUNITS(1–18)은 UNITLESS이다(118–135). WQUNITS(19–32)는 MG/L/DAY이다(136–149). WQUNITS(33)은 METERS이다(150). 주석(151). |
| 152–190 | 시작 시 6행 INITBIN3 루틴 안. 3자 코드 안내(152–154). WQCODE(1–33)은 NLC·NLD·NLG·NLM·PLC·PLD·PLG·PLM·LLC·LLD·LLG·LLM·TLC·TLD·TLG·TLM·VLM·DLM·DCS·DPS·DSO·DKA·DCA·DNH·DCO·DPC·DRC·DPM·DRM·DEF·DTR·DAL·DZZ이다(155–187). 구분 주석(188–190). |
| 191–217 | 시작 시 6행 INITBIN3 루틴 안. 기존 WQDOCOMP.BIN 추가 기록(append) 안내(191–192). 원문 `IF(ISCOMP .EQ. 2)THEN` (193)이면 `IO = 1` (194), `5       IO = IO+1` (195)로 후보 장치를 늘린다. `IF(IO .GT. 99)THEN` (196)이면 로그 출력 후 `STOP ' EFDC HALTED IN SUBROUTINE INITBIN3'` (198); 조건 종료(199). 장치 사용 여부 조회(200), `IF(IS2OPEN) GOTO 5` (201). 파일 존재 여부 조회(202). 내부 `IF(FEXIST)THEN` (203)이면 장치 IO에 직접 접근(direct access)·비서식(unformatted)·STATUS='UNKNOWN'·RECL=MAXRECL3로 연다(204–205). 발견 로그 출력(206). `READ(IO, REC=1) NREC3, TBEGAN, TEND, DT, IWQTSDT, NPARM,` (207); `+      NCELLS, KC` (208)로 헤더를 읽는다. 다음 기록 위치는 `NR5 = 1 + NPARM*3 + NCELLS*4 + (NCELLS*KC+1)*NREC3 + 1` (209). 파일 닫기(210). `ELSE` (211)는 `ISCOMP=1` (212). 두 조건 종료(213–214), 구분 주석(215–217). |
| 218–239 | 시작 시 6행 INITBIN3 루틴 안. 기존 파일 삭제 안내(218–219). 원문 `IF(ISCOMP .EQ. 1)THEN` (220)이면 TBEGAN에 TBEGIN을 복사한다(221). `IO = 1` (222), `10      IO = IO+1` (223). `IF(IO .GT. 99)THEN` (224)이면 로그 출력 후 `STOP ' EFDC HALTED IN SUBROUTINE INITBIN3'` (226); 조건 종료(227). 장치 사용 여부 조회(228), `IF(IS2OPEN) GOTO 10` (229). 파일 존재 여부 조회(230). 내부 `IF(FEXIST)THEN` (231)이면 WQDOCOMP.BIN을 열고 STATUS='DELETE'로 닫으며 로그를 출력한다(232–234); 내부 조건 종료(235). 빈 줄(236). 장치 IO에 직접 접근·비서식·STATUS='UNKNOWN'·RECL=MAXRECL3로 새 파일을 연다(237–238). 구분 주석(239). 220행 생성 조건은 이어진다. |
| 240–262 | 시작 시 6행 INITBIN3 루틴·220행 ISCOMP=1 참 분기 안. 헤더 작성 안내(240–242). NREC3·TBEGAN·TEND·DT·IWQTSDT·NPARM·NCELLS·KC를 쓴다(243). `DO I=1,NPARM` (244·247·250)의 세 루프는 WQNAME·WQUNITS·WQCODE를 각각 쓴다(245·248·251); 루프 종료(246·249·252). 셀(cell) 인덱스 대응 안내(253–255). `DO L=2,LA` (256·259)의 두 루프는 IL(L)·JL(L)를 각각 쓴다(257·260); 루프 종료(258·261), 주석(262). |
| 263–288 | 시작 시 6행 INITBIN3 루틴·220행 ISCOMP=1 참 분기 안. 셀 중심 좌표 입력 안내(263–265). `IO1 = 0` (266), `20      IO1 = IO1+1` (267). `IF(IO1 .GT. 99)THEN` (268)이면 로그 출력 후 `STOP ' EFDC HALTED IN SUBROUTINE INITBIN3'` (270); 조건 종료(271). 장치 사용 여부 조회(272), `IF(IS1OPEN) GOTO 20` (273). 장치 IO1에 LXLY.INP를 STATUS='UNKNOWN'으로 연다(274). `DO NS=1,4` (276)에서 `READ(IO1,1111)` (277)로 앞 네 기록을 건너뛴다; 루프 종료(278), `1111   FORMAT(80X)` (279). `DO LL=1,LVC` (281)에서 I·J·XUTME·YUTMN을 읽는다(282). 대응 인덱스는 `L=LIJ(I,J)` (283). XLON(L)·YLAT(L)에 좌표를 복사한다(284–285). 루프 종료(286), 장치 IO1 닫기(287), 주석(275·280·288). |
| 289–304 | 시작 시 6행 INITBIN3 루틴·220행 ISCOMP=1 참 분기 안. 좌표 출력 안내(289–291). `DO L=2,LA` (292·295)의 두 루프에서 XLON(L)·YLAT(L)를 쓴다(293·296); 루프 종료(294·297). 빈 줄(298). NEXTREC를 NR5로 조회하고 장치 IO를 닫는다(299–300). 220행 조건 종료(301), 빈 줄(302), `RETURN` (303), `END` (304). 이 파일에는 CALL문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 51·60–61·207·243: 입력 설명 주석과 헤더 입출력은 출력 간격 변수로 IWQTSDT를 사용한다. NREC3 설명 주석은 IWQDIUDT를 적는다.
- 237–238·243–260·292–296: 새 출력 파일은 ACCESS='DIRECT'로 열린다. 헤더·이름·단위·코드·인덱스·좌표의 WRITE문에는 REC 지정이 없다. 기존 헤더 READ에는 REC=1이 있다(207).
- 63–69·207–208: MAXRECL3는 초기 NPARM=33을 이용해 계산한다. 기존 파일 헤더 READ는 NPARM을 다시 읽는다. 그 뒤 MAXRECL3를 다시 계산하는 문장은 이 파일에 없다.
- 38·43–45·81–187·207–208: 문자열 배열 크기는 33이다. 이 파일의 이름·단위·코드 대입 범위는 1–33이다. 기존 헤더에서 읽은 NPARM에 대해 배열 크기를 검사하는 조건은 이 파일에 없다.
- 40·281–286·292–297: 좌표 입력 루프는 LL=1..LVC이며 실제 배열 인덱스는 LIJ(I,J)이다. 좌표 출력 루프는 L=2..LA이다. 이 블록에는 XLON/YLAT 전체 초기화나 읽은 I/J의 범위 검사 문장이 없다.
