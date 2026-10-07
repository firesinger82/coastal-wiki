---
file: models/EFDC/raw/source_code/EFDC-GVC/negdepHOUS.for
lines: 269
sha256: 56591beab6695ac78f76fe2bf14d283d29d8812302217eab7ffeaea08f79e48c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# negdepHOUS.for — 판독 구간 기록

구간은 1행부터 269행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | 구분 주석과 `SUBROUTINE NEGDEPHOUS(QCHANUT,QCHANVT,ISTL)` 입구(1–6). EFDC-FULL 1.0a·수정일·변경 이력·relax2t 추가 주석(8–18). 외부 해(external solution)의 음수 수심 검사 주석은 NEGDEP이라는 이름을 쓴다(22). EFDC.PAR·EFDC.CMN 포함(26–27), NCHANM 크기의 QCHANUT/QCHANVT 선언(29). 검사 머리말·구분 주석을 포함한다(30–36). 포함 파일 내부는 판독하지 않았다. |
| 37–66 | 시작 시 6행 NEGDEPHOUS 안. `IF(ISNEGH.GE.1)THEN` (37)에서 INEGFLG=0을 설정한다(38). L=2..LA 루프(40)의 `IF(HP(L).LT.0.)THEN` (41)에서 `cjah  INEGFLG=1` (42)은 주석이다. LN을 찾고 단위 6·8에 셀 중심(cell center) 경고와 중심·주변 면 수심을 출력한다(43–55). 보정 대입은 `HP(L)=HDRY` (57), `IMASKDRY(L)=2` (58), `LMASKDRY(L)=.FALSE.` (61). 정수 마스크 대입 `C      LMASKDRY(L)=0` (60)은 주석이다. 조건과 루프를 닫는다(64–65). |
| 67–89 | 시작 시 6행 NEGDEPHOUS·37행 ISNEGH>=1 분기 안. L=2..LA 루프(67)의 `IF(HU(L).LT.0.AND.SUBO(L).GT.0.5)THEN` (68)에서 `cjah  INEGFLG=1` (69)은 주석이다. LN을 찾고 단위 6·8에 서측 면(west face) 경고와 중심·주변 면 수심을 출력한다(70–82). `HU(L)=HDRY` (84)로 보정한다. 조건·루프 종료와 주석도 포함한다(83–89). |
| 90–111 | 시작 시 6행 NEGDEPHOUS·37행 ISNEGH>=1 분기 안. L=2..LA 루프(90)의 `IF(HV(L).LT.0.AND.SVBO(L).GT.0.5)THEN` (91)에서 `cjah  INEGFLG=1` (92)은 주석이다. LN을 찾고 단위 6·8에 남측 면(south face) 경고와 중심·주변 면 수심을 출력한다(93–105). `HV(L)=HDRY` (107)로 보정한다. 조건과 루프를 닫는다(109–110). |
| 112–150 | 시작 시 6행 NEGDEPHOUS·37행 ISNEGH>=1 분기 안. ISCDRY를 함께 출력하는 대체 HU·HV 루프는 전체가 주석이다(112–148). 주석 조건은 `C      IF(HU(L).LT.0.)THEN` (113), `C      IF(HV(L).LT.0.)THEN` (132). 각 주석 블록에는 INEGFLG=1·LN/LS 설정과 단위 6·8 출력이 있다(114–128·133–147). 실행 중인 37행 조건을 닫는다(149). |
| 151–176 | 시작 시 6행 NEGDEPHOUS 안. `IF(ISNEGH.EQ.2)THEN` (151), `IF(INEGFLG.EQ.1)THEN` (152), `IF(MDCHH.GT.0)THEN` (155), NMD=1..MDCHH 루프(156)에서 채널 셀(channel cell)과 호스트 셀(host cell)을 찾는다(158–162). `IF(MDCHTYP(NMD).EQ.1)THEN` (164) 안의 X 방향 식은 `SRFCHAN=HP(LCHNU)+BELV(LCHNU)` (167), `SRFHOST=HP(LHOST)+BELV(LHOST)` (168), `SRFCHAN1=H1P(LCHNU)+BELV(LCHNU)` (169), `SRFHOST1=H1P(LHOST)+BELV(LHOST)` (170). 단위 8에 채널·호스트 위치·건조 표시·현재 수면·수심·P1·이전 수심 및 QCHANU/QCHANUT·CCCCHU/CCCCHV를 출력한다(171–175). X 조건을 닫는다(176). |
| 177–194 | 시작 시 6행 NEGDEPHOUS·151행 ISNEGH=2·152행 INEGFLG=1·155행 MDCHH>0 분기·156행 NMD 루프 안. `IF(MDCHTYP(NMD).EQ.2)THEN` (178) 안의 Y 방향 식은 `SRFCHAN=HP(LCHNV)+BELV(LCHNV)` (181), `SRFHOST=HP(LHOST)+BELV(LHOST)` (182), `SRFCHAN1=H1P(LCHNV)+BELV(LCHNV)` (183), `SRFHOST1=H1P(LHOST)+BELV(LHOST)` (184). 단위 8에 채널·호스트 셀의 현재/이전 수면과 수심, QCHANV/QCHANVT·CCCCHU/CCCCHV를 출력한다(185–189). Y 조건 종료·8004 문자열 출력·NMD 루프와 MDCHH 조건 종료를 포함한다(190–193). |
| 195–217 | 시작 시 6행 NEGDEPHOUS·151행 ISNEGH=2·152행 INEGFLG=1 분기 안. `CALL RESTOUT(1)` (195). EQCOEF.OUT을 삭제 후 append로 열어 N/ISTL을 쓴다(197–200). L=2..LA 루프(201)의 `SURFTMP=GI*P(L)` (202)를 계산한다. I/J·CCS/CCW/CCC/CCE/CCN·FPTMP/SURFTMP를 쓰고 닫는다(203–206). EQTERM.OUT을 같은 방식으로 열어 N/ISTL과 셀별 SUB/SVB·HRUO/HRVO·HUTMP/HVTMP를 쓰고 닫는다(208–216). |
| 218–244 | 시작 시 6행 NEGDEPHOUS·151행 ISNEGH=2·152행 INEGFLG=1 분기 안. CFLMAX.OUT을 삭제 후 다시 열어 L=2..LA·K=1..KC의 CFLUUU/CFLVVV/CFLWWW/CFLCAC를 쓴다(218–227). NEGDEPDIA.OUT을 삭제 후 다시 열어 IMASKDRY·BELV·HP/H1P·서/동 SUB·남/북 SVB를 쓰고 닫는다(229–236). `CALL EE_LINKAGE(0)` (238), `CALL SURFPLT` (239) 뒤 STOP을 실행한다(240). 두 바깥 조건을 닫는다(242–243). |
| 245–269 | 시작 시 6행 NEGDEPHOUS 안. 자료·CFL 배열·중심/면 경고·수심·채널 표의 FORMAT을 정의한다(245–264). 채널 표 머리말은 N/NMD/MTYP/I/J/IDRY/P/H/P1/H1이며, 8004 문자열은 QCHANU/QCHANUT/CCCCHU/CCCCHV이다(261–264). 구분 주석·RETURN·END로 끝난다(265–269). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 38·42·69·92·114·133·151–152: 실행문은 INEGFLG를 0으로 설정한다. INEGFLG=1인 모든 대입문은 주석이다. 후속 진단의 INEGFLG=1 조건은 실행문으로 남아 있다.
- 57–61·84·107: 음수 HP는 HDRY로 바꾸면서 IMASKDRY와 LMASKDRY를 바꾼다. 음수 HU·HV 보정 블록은 해당 면 수심만 HDRY로 바꾼다.
- 167–175·181–189: X 방향은 SRFCHAN1/SRFHOST1을 계산하지만 같은 분기 출력에는 P1을 사용한다. Y 방향은 계산한 SRFCHAN1/SRFHOST1을 출력한다.
- 191·263–264: 8004의 QCHANU/QCHANUT 문자열은 X·Y 조건 밖에서 출력한다. Y 방향 수치 기록은 QCHANV/QCHANVT를 사용한다(189).
- 246: 1002 FORMAT을 선언하지만 이 파일의 실행문에는 해당 형식 번호를 참조하는 출력문이 없다.
