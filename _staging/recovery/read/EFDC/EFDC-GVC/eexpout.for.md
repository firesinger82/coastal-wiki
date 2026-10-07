---
file: models/EFDC/raw/source_code/EFDC-GVC/eexpout.for
lines: 205
sha256: 57b6bb74a2adbde20fa39777584cc4ab702898390b344d4aff73ea0b26560470
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# eexpout.for — 판독 구간 기록

구간은 1행부터 205행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 구분 주석과 `SUBROUTINE EEXPOUT(JSEXPLORER)` 입구(1–6). 머리말은 BEDTOP이 퇴적층(sediment bed) 최상층의 퇴적물·독성물질 변수를 출력한다고 적는다(10–13). `EFDC.PAR`·`EFDC.CMN` 포함(15–16), INTEGER*4 IVER 선언(18), 최초 호출 주석(20–23). 포함 파일 내부는 이 파일의 판독 범위에 포함하지 않았다. |
| 24–42 | 시작 시 6행 EEXPOUT 루틴 안. 원문 조건 `IF(JSEXPLORER.EQ.1)THEN` (24). 최초 호출 분기에서 장치 95의 BED_TOP.OUT을 순차 이진 파일로 열고 삭제한 뒤 다시 연다(28–32). 버전 기본값 `IVER=103` (33)을 쓴다(34). ISTRAN(1..7), NSED·NSND·KB·KC·NTOX 헤더를 출력한다(35–37). 클래스 수 계산 `NSXD=NSED+NSND` (38). `DO NS=1,NSXD` (39)에서 SEDDIA를 출력한다(40–41). |
| 43–80 | 시작 시 6행 EEXPOUT 루틴·24행 최초 호출 참 분기 안. 퇴적층 파일 조건은 `IF(ISBEXP.GE.1)THEN` (44), 그 안 `IF(ISTRAN(6).GE.1.OR.ISTRAN(7).GE.1)THEN` (45). IWRSP 선택에 따른 임계 전단응력(critical shear stress) 출력 변경 주석(48–51). 장치 1001의 TAU_CRIT_COH.OUT을 열고 삭제한 뒤 다시 연다(52–56). 장치 96의 BED_LAY.OUT도 같은 방식으로 연다(60–64). 버전·수송 플래그·종 수·층 수를 출력한다(65–68). `NSXD=NSED+NSND` (69), `DO NS=1,NSXD` (70)에서 입경을 출력한다(71–72). 두 내부 조건과 최초 호출 조건을 닫는다(73–75). 구분·후속 호출 주석(76–80). |
| 81–94 | 시작 시 6행 EEXPOUT 루틴 안. 시간 조건 `IF(ISDYNSTP.EQ.0)THEN` (81)이면 `TIME=DT*FLOAT(N)+TCON*TBEGIN` (82). `ELSE` (83)는 TIMESEC를 복사한다(84). 최초 호출 보정은 `IF(JSEXPLORER.EQ.1)TIME=TCON*TBEGIN` (86). 일 단위 변환 `TIME=TIME/86400.` (89). 별도 출력 조건 `IF(ISSPH(8).GE.1)THEN` (91) 안에서 TIME과 `LA-1`을 장치 95에 쓴다(93). |
| 95–119 | 시작 시 6행 EEXPOUT 루틴·91행 ISSPH(8) 참 분기 안. `DO L=2,LA` (95)에서 N1=KBT(L)을 복사한다(96). `IF(ISTRAN(6).GT.0.OR.ISTRAN(7).GT.0)THEN` (97) 안의 `IF(ISBEDSTR.GE.1)THEN` (98)은 TAUBSED를 출력한다(99). 그 안 `IF(ISBEDSTR.EQ.1)THEN` (100)은 TAUBSND도 출력한다(101). 98행 조건의 `ELSE` (103)는 TAUB를 출력한다(104). 97행 조건의 `ELSE` (106)는 `SHEAR=MAX(QQ(L,0),QQMIN)/CTURB2` (107)를 계산하고 출력한다(108). 개별 조건 `IF(ISTRAN(1).EQ.1) WRITE(95)(SAL(L,K),K=1,KC)` (110), `IF(ISTRAN(2).EQ.1) WRITE(95)(TEM(L,K),K=1,KC)` (111), `IF(ISTRAN(3).EQ.1) WRITE(95)(DYE(L,K),K=1,KC)` (112), `IF(ISTRAN(4).EQ.1) WRITE(95)(SFL(L,K),K=1,KC)` (113). 독성물질 조건 `IF(ISTRAN(5).EQ.1)THEN` (115)은 최상 퇴적층 TOXB와 수층(water column) 전체 TOX를 쓴다(116–117). |
| 120–139 | 시작 시 6행 EEXPOUT 루틴·91행 출력 참 분기·95행 L 루프 안. `IF(ISTRAN(6).EQ.1.OR.ISTRAN(7).GE.1)THEN` (120)은 최상층 번호·바닥 고도·층 두께·밀도·공극률(porosity)을 쓴다(121). `IF(ISTRAN(6).EQ.1)THEN` (122)은 SEDB·VFRBED와 수층 SED를 출력한다(123–124). 병렬 조건 `IF(ISTRAN(7).EQ.1)THEN` (126)은 SNDB·VFRBED의 NX+NSED 위치와 수층 SND를 출력한다(127–128). 그 안 `IF(ISBDLDBC.GT.0)THEN` (129)은 CQBEDLOADX/Y를 출력한다(130). 내부 조건·L 루프·91행 조건을 닫는다(131–136). 전체 퇴적층 출력 주석(137–139). |
| 140–174 | 시작 시 6행 EEXPOUT 루틴 안. 전체 퇴적층 출력 조건 `IF(ISBEXP.GE.1)THEN` (140), 내부 조건 `IF(ISTRAN(6).GE.1.OR.ISTRAN(7).GE.1.AND.KB.GT.1)THEN` (141). TIME·LA-1을 쓴다(144). `DO L=2,LA` (146)에서 각 KBT를 먼저 출력한다(147–148). 별도 `DO L=2,LA` (150), `DO K=1,KBT(L)` (152)에서 HBED·BDENBED·PORBED를 쓴다(153). `IF(ISTRAN(6).GE.1)THEN` (154) 안 `DO NS=1,NSED` (155)에서 SEDB·VFRBED를 쓴다(156). `IF(ISTRAN(7).GE.1)THEN` (159) 안 `DO NX=1,NSND` (160)에서 클래스 인덱스 `NS=NSED+NX` (161)를 계산하고 SNDB·VFRBED를 쓴다(162). `IF(ISTRAN(5).GE.1)THEN` (165) 안 `DO NT=1,NTOX` (166)에서 TOXB를 쓴다(167). 루프·조건을 모두 닫는다(168–173). |
| 175–205 | 시작 시 6행 EEXPOUT 루틴 안. 구분 주석(175–176). BEDARD.OUT 생성·추가 출력·FORMAT 문은 모두 `c moved to bedplth.for`로 주석 처리되어 있다(177–200). 주석 속 조건은 `IF(JSBPHA.EQ.1)THEN` (177), `IF(ISBARD.GE.1)THEN` (186)이며 실행 조건이 아니다. 원문은 퇴적 클래스별 SEDFDTAP/SEDFDTAN·SNDFDTAP/SNDFDTAN 출력 코드의 이동을 적는다(190–192). 마지막 구분 주석·RETURN·END(201–205). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·10–13: 실행 루틴 이름은 EEXPOUT이다. 머리말의 루틴 이름은 BEDTOP이다.
- 52–56·57–205: TAU_CRIT_COH.OUT을 장치 1001로 다시 연다. 이후 이 파일에는 장치 1001의 WRITE 또는 CLOSE 문이 없다.
- 45·141: BED_LAY.OUT 생성 조건에는 KB 조건이 없다. 후속 출력 조건은 `ISTRAN(6).GE.1.OR.ISTRAN(7).GE.1.AND.KB.GT.1`이며 OR 전체를 감싸는 괄호가 없다.
- 97·110–126: 전단응력 선택 조건은 ISTRAN(6/7)>0이다. 최상층 퇴적물 출력의 일부 조건은 ISTRAN=1이고, 120행의 ISTRAN(7) 조건은 >=1이다.
