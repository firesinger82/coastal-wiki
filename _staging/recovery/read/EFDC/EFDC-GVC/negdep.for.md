---
file: models/EFDC/raw/source_code/EFDC-GVC/negdep.for
lines: 253
sha256: fd678ca11781c7229a7b8e036f81658d68b5c503592cd9c18b5f745b5aeb4ba1
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# negdep.for — 판독 구간 기록

구간은 1행부터 253행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | 구분 주석과 `SUBROUTINE NEGDEP(QCHANUT,QCHANVT,ISTL)` 입구(1–6). EFDC-FULL 1.0a·수정일·변경 이력 및 relax2t 추가 주석(8–18). 외부 해(external solution)의 음수 수심을 검사한다는 주석(22). EFDC.PAR·EFDC.CMN 포함(26–27), NCHANM 크기의 QCHANUT/QCHANVT 선언(29). 검사 머리말·구분 주석도 포함한다(30–36). 포함 파일 내부는 판독하지 않았다. |
| 37–58 | 시작 시 6행 NEGDEP 안. `IF(ISNEGH.GE.1)THEN` (37)에서 INEGFLG=0으로 초기화한다(38). L=2..LA 루프(40)의 `IF(HP(L).LT.0.)THEN` (41)이면 INEGFLG=1·LN=LNC(L)을 설정한다(42–43). 단위 6·8에 셀 중심(cell center) 경고와 I/J·HP/H1P/H2P·서/동측 HU/H1U·남/북측 HV/H1V를 출력한다(44–55). 셀 조건과 루프를 닫는다(56–57). |
| 59–78 | 시작 시 6행 NEGDEP·37행 ISNEGH>=1 분기 안. L=2..LA 루프(59)의 `IF(HU(L).LT.0.AND.SUBO(L).GT.0.5)THEN` (60)이면 INEGFLG=1·LN=LNC(L)을 설정한다(61–62). 단위 6·8에 서측 면(west face) 경고와 같은 주변 수심을 출력한다(63–74). 조건·루프 종료와 빈 주석을 포함한다(75–78). |
| 79–97 | 시작 시 6행 NEGDEP·37행 ISNEGH>=1 분기 안. L=2..LA 루프(79)의 `IF(HV(L).LT.0.AND.SVBO(L).GT.0.5)THEN` (80)이면 INEGFLG=1·LN=LNC(L)을 설정한다(81–82). 단위 6·8에 남측 면(south face) 경고와 주변 수심을 출력한다(83–94). 조건과 루프를 닫는다(95–96). |
| 98–136 | 시작 시 6행 NEGDEP·37행 ISNEGH>=1 분기 안. 건조 표시 ISCDRY와 주변 수심을 출력하는 대체 두 루프는 모두 주석이다(98–134). 주석 조건은 `C      IF(HU(L).LT.0.)THEN` (99), `C      IF(HV(L).LT.0.)THEN` (118). 주석 블록은 INEGFLG·LN·LS 설정과 단위 6·8 출력문을 포함한다(100–114·119–133). 실행 중인 37행 조건을 닫는다(135). |
| 137–162 | 시작 시 6행 NEGDEP 안. `IF(ISNEGH.EQ.2)THEN` (137), 그 안의 `IF(INEGFLG.EQ.1)THEN` (138)에서 후속 진단을 수행한다. `IF(MDCHH.GT.0)THEN` (141)의 NMD=1..MDCHH 루프(142)에서 호스트 셀(host cell)과 채널 셀(channel cell)을 찾는다(144–148). `IF(MDCHTYP(NMD).EQ.1)THEN` (150)의 X 방향 채널 식은 `SRFCHAN=HP(LCHNU)+BELV(LCHNU)` (153), `SRFHOST=HP(LHOST)+BELV(LHOST)` (154), `SRFCHAN1=H1P(LCHNU)+BELV(LCHNU)` (155), `SRFHOST1=H1P(LHOST)+BELV(LHOST)` (156). 단위 8에 단계·채널 유형·셀 위치·건조 표시·수심·P1과 QCHANU/QCHANUT·CCCCHU/CCCCHV를 출력한다(157–161). X 방향 조건을 닫는다(162). |
| 163–180 | 시작 시 6행 NEGDEP·137행 ISNEGH=2·138행 INEGFLG=1·141행 MDCHH>0 분기·142행 NMD 루프 안. `IF(MDCHTYP(NMD).EQ.2)THEN` (164)의 Y 방향 채널 식은 `SRFCHAN=HP(LCHNV)+BELV(LCHNV)` (167), `SRFHOST=HP(LHOST)+BELV(LHOST)` (168), `SRFCHAN1=H1P(LCHNV)+BELV(LCHNV)` (169), `SRFHOST1=H1P(LHOST)+BELV(LHOST)` (170). 단위 8에 채널·호스트 셀의 현재/이전 수면과 수심, QCHANV/QCHANVT·CCCCHU/CCCCHV를 출력한다(171–175). Y 조건을 닫고 8004 형식의 문자열을 쓴다(176–177). NMD 루프와 MDCHH 조건을 닫는다(178–179). |
| 181–203 | 시작 시 6행 NEGDEP·137행 ISNEGH=2·138행 INEGFLG=1 분기 안. `CALL RESTOUT(1)` (181). EQCOEF.OUT을 삭제 후 append로 다시 열고 N/ISTL을 쓴다(183–186). L=2..LA 루프(187)의 `SURFTMP=GI*P(L)` (188)을 계산하고 I/J·CCS/CCW/CCC/CCE/CCN·FPTMP/SURFTMP를 쓴다(189–190). 파일을 닫는다(192). EQTERM.OUT을 같은 방식으로 열고 N/ISTL, 셀별 SUB/SVB·HRUO/HRVO·HUTMP/HVTMP를 쓴 뒤 닫는다(194–202). |
| 204–228 | 시작 시 6행 NEGDEP·137행 ISNEGH=2·138행 INEGFLG=1 분기 안. CFLMAX.OUT을 삭제 후 다시 열어 L=2..LA, K=1..KC의 CFLUUU/CFLVVV/CFLWWW/CFLCAC를 쓴다(204–213). NEGDEPDIA.OUT을 삭제 후 다시 열어 셀별 IMASKDRY·BELV·HP/H1P·서/동 SUB·남/북 SVB를 쓴다(215–222). STOP을 실행한다(224). 두 바깥 조건을 닫는다(226–227). |
| 229–253 | 시작 시 6행 NEGDEP 안. 진단 자료·CFL 배열·중심/면 경고·수심·채널 표의 FORMAT을 정의한다(229–248). 채널 머리말은 N/NMD/MTYP/I/J/IDRY/P/H/P1/H1이고, 8004 문자열은 QCHANU/QCHANUT/CCCCHU/CCCCHV이다(245–248). 구분 주석·RETURN·END로 끝난다(249–253). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 37–96·137–138·224: 수심 검사는 ISNEGH>=1에서 수행한다. 진단 파일 작성과 STOP은 ISNEGH=2이면서 INEGFLG=1인 경우에만 실행한다.
- 153–161·167–175: X 방향 채널 분기는 SRFCHAN1/SRFHOST1을 계산하지만 같은 분기의 출력에는 P1(LCHNU)/P1(LHOST)를 쓴다. Y 방향 분기는 계산한 SRFCHAN1/SRFHOST1을 출력한다.
- 177·247–248: 8004의 QCHANU/QCHANUT 문자열은 X·Y 채널 조건 밖에서 출력한다. Y 방향 채널의 수치 출력은 QCHANV/QCHANVT이다(175).
- 230: 1002 FORMAT을 선언하지만 이 파일의 실행문에는 해당 형식 번호를 참조하는 출력문이 없다.
