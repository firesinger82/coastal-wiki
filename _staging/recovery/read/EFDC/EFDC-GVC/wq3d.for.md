---
file: models/EFDC/raw/source_code/EFDC-GVC/wq3d.for
lines: 318
sha256: 4ea5f8d576e66cf589a5b9b973ba67aaf47cf81fa783b2b3ae7f82401c1f799e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# wq3d.for — 판독 구간 기록

구간은 1행부터 318행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–50 | 수질 모델 시작·구분 주석(1–11), `SUBROUTINE WQ3D` (12). 제어 루틴 목적·작성자·수정 이력·버전 주석(13–35). EFDC.PAR·EFDC.CMN 포함(36–37), HHMMSS 선언은 주석이다(39). `DATA IWQTICI,IWQTAGR,IWQTSTL,IWQTSUN,IWQTBEN,IWQTPSL,IWQTNPL/7*0/` (41), `DATA ISMTICI/0/` (42). IWQTSUN·IWQTBEN·IWQTPSL·IWQTNPL은 자기 자신을 대입한다(46–49). 빈 주석(38·40·43–45·50). |
| 51–114 | 시작 시 12행 루틴 안. 초기 농도 조건·호출 `IF(IWQICI.EQ.1 .AND. ITNWQ.EQ.IWQTICI) CALL RWQICI(IWQTICI)` (53). 경계 시계열 RWQCSR 무조건 호출(57). 조류(algae) 매개변수 조건·호출 `IF(IWQAGR.EQ.1 .AND. ITNWQ.EQ.IWQTAGR) CALL RWQAGR(IWQTAGR)` (61). 침강 속도(settling velocity) 조건·호출 `IF(IWQSTL.EQ.1 .AND. ITNWQ.EQ.IWQTSTL) CALL RWQSTL(IWQTSTL)` (65). 이전 1·2·3일 일사(solar radiation) 설명 주석(67–71). `ISTPDAY = INT((86400.0/TIDALP)*REAL(NTSPTC))` (73), `IF(MOD(N, ISTPDAY) .EQ. 0)THEN` (74) 안 WQI3=WQI2·WQI2=WQI1·WQI1=WQI0 복사(75–77). 일사 입력 단위·변환 계수 설명 주석(80–87). `IF(IWQSUN.EQ.1)THEN` (89) 안 RWQSUN 호출(90), WQI0=SOLSRDT·WQFD=SOLFRDT 복사(91–92). 95–104행 공간 평균 경로는 전체 주석이다: `c      IF(IWQSUN.EQ.2)THEN` (95); `c        SOLARAVG=0.` (96); `c        DO L=2,LA` (97); `c          SOLARAVG=SOLARAVG+SOLSWRT(L)` (98); `c        ENDDO` (99); `c        SOLARAVG=SOLARAVG/FLOAT(LA-1)` (100); `c        WQI0 = PARADJ*2.065*SOLARAVG` (101); `c        WQI0OPT = MAX(WQI0OPT, WQI0)` (102); `c        WQFD=1.` (103); `c      ENDIF` (104). 활성 `IF(IWQSUN.EQ.2)THEN` (106) 안 107행 L=2..LA에서 WQIH3=WQIH2·WQIH2=WQIH1 복사(108–109), `WQIH1(L) = PARADJ*2.065*SOLSWRT(L)` (110). `WQFD=1.` (112), 조건 종료·주석(113–114). |
| 115–154 | 시작 시 12행 루틴 안. 저서 플럭스(benthic flux) 판독 주석과 이전 호출 주석 `C      IF(IWQBEN.EQ.2 .AND. ITNWQ.EQ.IWQTBEN) CALL RWQBEN(IWQTBEN)          !MRM` (117). `IF(IWQBEN .EQ. 2)THEN                                                !MRM` (121) 안 `IF(ISDYNSTP.EQ.0)THEN` (122) 참이면 `TIMTMP=(DT*FLOAT(N)+TCON*TBEGIN)/86400.` (123). `ELSE` (124) 분기는 `TIMTMP=TIMESEC/86400.` (125). `IF(TIMTMP .GE. BENDAY)THEN                                         !MRM` (127) 참이면 `CALL RWQBEN2(TIMTMP)                                               !MRM` (128). 조건 종료(129–130). 점오염원 부하(point source loading) 조건·호출 `IF(IWQPSL.GE.1) CALL RWQPSL` (134). 대기 습식 침적(atmospheric wet deposition) RWQATM 무조건 호출(138). 비점오염원(non point source) 판독 호출은 주석이다: `*     IF(IWQNPL.EQ.1 .AND. ITNWQ.EQ.IWQTNPL) CALL RWQNPL(IWQTNPL)` (142). `IF(IWQBEN.EQ.1)THEN` (146) 안 초기 퇴적물 조건·호출 `IF(ISMICI.EQ.1 .AND. ITNWQ.EQ.ISMTICI) CALL RSMICI(ISMTICI)` (147). `ITNWQ = ITNWQ + 2` (152), `TINDAY = TINDAY + DTWQ` (153)으로 시각을 갱신한다. 주석(154). |
| 155–208 | 시작 시 12행 루틴 안. 기존 농도 복사 루프는 전체 주석이다(157–163). 용존산소(dissolved oxygen, D.O.) 수송 성분 설명 주석(165–168). 169행 K=1..KC·170행 L=2..LA에서 `XMRM = WQV(L,K,19)*DTWQ*DZC(K)*HP(L)` (171), `XDOTRN(L,K) = XDOTRN(L,K) - XMRM` (172), `XDOALL(L,K) = XDOALL(L,K) - XMRM` (173). 물리 수송(physical transport)의 조건·호출 `IF(IGRIDV.EQ.0) CALL CALWQC(2)` (181), `IF(IGRIDV.EQ.1) CALL CALWQCGVC(2)` (182). 수송 뒤 188행 K·189행 L 루프에서 `XMRM = WQV(L,K,19)*DTWQ*DZC(K)*HP(L)` (190), `XDOTRN(L,K) = XDOTRN(L,K) + XMRM` (191), `XDOALL(L,K) = XDOALL(L,K) + XMRM` (192)로 새 농도를 더한다. 반응 계산용 이전 농도 복사 주석(196–199), NMALG=0(200), `IF(IDNOTRVA.GT.0) NMALG=1` (201). 202행 NW=1..NWQV+NMALG·203행 K·204행 L 루프에서 WQVO에 WQV를 복사한다(205). 세 루프 종료(206–208). |
| 209–243 | 시작 시 12행 루틴 안. 반응속도(kinetics)·퇴적물 모델을 더 긴 간격으로 갱신한다는 주석(210–212). `NWQKCNT=NWQKCNT+1` (214). `IF(NWQKCNT.EQ.NWQKDPT)THEN` (215) 참이면 NWQKCNT=0(216). `IF(ISCRAY.EQ.0)THEN` (220) 참이면 `TTMP=SECNDS(0.0)` (221)로 SECNDS 시작 시각을 얻는다. `ELSE` (222) 분기는 `T1TMP=SECOND( )` (223) 및 TIMEF(WT1TMP) 호출(224). 반응 루틴 조건·호출 `IF(ISWQLVL.EQ.0) CALL WQSKE0` (227), `IF(ISWQLVL.EQ.1) CALL WQSKE1` (228), `IF(ISWQLVL.EQ.2) CALL WQSKE2` (229). `IF(ISWQLVL.EQ.3) THEN` (230) 안 `IF(IGRIDV.EQ.0) CALL WQSKE3` (231), `IF(IGRIDV.EQ.1) CALL WQSKE3GVC` (232). 실행 뒤 `IF(ISCRAY.EQ.0)THEN` (235) 참이면 `TWQKIN=TWQKIN+SECNDS(TTMP)` (236). `ELSE` (237) 분기는 `T2TMP=SECOND( )` (238), TIMEF(WT2TMP) 호출(239), `TWQKIN=TWQKIN+T2TMP-T1TMP` (240), `WTWQKIN=WTWQKIN+(WT2TMP-WT1TMP)*0.001` (241). 주석(243); 215행 분기는 이어진다. |
| 244–255 | 시작 시 12행 루틴·215행 반응/퇴적물 갱신 분기 안. 음수 농도 진단 WWQNC 무조건 호출(246). `IF(ITNWQ.GE.IWQTSB .AND. ITNWQ.LE.IWQTSE)THEN` (250) 안 `IF(MOD(ITNWQ,IWQTSDT).EQ.0) CALL WWQTS` (252)이면 WWQTS를 호출한다. 인수 TINDAY를 넣는 이전 호출 `C           IF(MOD(ITNWQ,IWQTSDT).EQ.0) CALL WWQTS(TINDAY)` (251)과 WWQTSBIN 호출(253)은 주석이다. 조건 종료·주석(254–255). |
| 256–299 | 시작 시 12행 루틴·215행 반응/퇴적물 갱신 분기 안. `IF(IWQBEN.EQ.1)THEN` (258) 안 `IF(ISCRAY.EQ.0)THEN` (260) 참이면 `TTMP=SECNDS(0.0)` (261). `ELSE` (262) 분기는 `T1TMP=SECOND( )` (263) 및 TIMEF(WT1TMP) 호출(264). `CALL SMMBE` (267)로 퇴적물 모델을 계산한다. `IF(ISCRAY.EQ.0)THEN` (269) 참이면 `TWQSED=TWQSED+SECNDS(TTMP)` (270). `ELSE` (271) 분기는 `T2TMP=SECOND( )` (272), TIMEF(WT2TMP) 호출(273), `TWQSED=TWQSED+T2TMP-T1TMP` (274), `WTWQSED=WTWQSED+(WT2TMP-WT1TMP)*0.001` (275). `IF(ISMTS.GE.1)THEN` (278) 안 `IF(ITNWQ.GE.ISMTSB .AND. ITNWQ.LE.ISMTSE)THEN` (282) 안 `IF(MOD(ITNWQ,ISMTSDT).EQ.0) CALL WSMTS` (284)이면 WSMTS를 호출한다. 이전 TINDAY 인수 호출 `C              IF(MOD(ITNWQ,ISMTSDT).EQ.0) CALL WSMTS(TINDAY)` (283)은 주석이다. 별도 `IF(ITNWQ.GE.ISMTSB .AND. ITNWQ.LE.ISMTSE)THEN` (291) 안 `CALL WSMTSBIN` (292). IWQBEN 조건 종료(294), 반응/퇴적물 갱신 조건 종료(296), 설명 주석(298–299). |
| 300–318 | 시작 시 12행 루틴 안이며 215행 갱신 분기 밖. 시각 로그 호출·TFILE 추가 기록은 주석이다(302–305). 재시작 출력의 조건·호출도 주석이다: `C      IF(IWQRST.EQ.1) CALL WWQRST` (309), `C      IF(IWQBEN.EQ.1 .AND. ISMRST.EQ.1) CALL WSMRST` (310). IWQONC close는 주석이다(312). 사용 시각·진단 FORMAT(314–315), RETURN·END(317–318), 사이 주석(300–301·306–308·311·313·316). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41·46–49: IWQTSUN·IWQTBEN·IWQTPSL·IWQTNPL은 DATA로 0을 설정한 뒤 자기 대입한다. 이 파일의 활성 실행문에는 이 네 변수의 다른 참조가 없다.
- 73–74: 일 경계 판단은 INT((86400.0/TIDALP)*REAL(NTSPTC))와 MOD(N,ISTPDAY)를 사용한다. 이 두 문장 앞에는 ISTPDAY 양수 검사문이 없다.
- 89–113·95–104: IWQSUN=1 분기는 WQI0을 설정한다. 활성 IWQSUN=2 분기는 셀별 WQIH1을 설정한다. IWQSUN=2에서 WQI0을 설정하던 공간 평균 코드는 주석이다.
- 152–153: ITNWQ 증가량은 상수 2이다. TINDAY 증가량은 DTWQ이다.
- 171·181–182·190: 용존산소 수송 진단은 IGRIDV에 따른 두 수송 루틴 호출 전후에 DTWQ*DZC(K)*HP(L)를 곱한다. 이 진단식에는 GVCSCLP 참조가 없다.
- 214–216: 반응/퇴적물 갱신은 NWQKCNT.EQ.NWQKDPT일 때만 실행한다. 이 분기에 NWQKCNT>NWQKDPT 조건은 없다.
- 227–233·181–182: 반응 호출 분기는 ISWQLVL=0,1,2,3을 열거한다. 수송 호출과 ISWQLVL=3 내부 분기는 IGRIDV=0,1을 열거한다. 이 파일에는 그 밖의 값에 대한 대체 호출 분기가 없다.
- 278–293: WSMTS 호출에는 ISMTS.GE.1 및 MOD(ITNWQ,ISMTSDT).EQ.0 조건이 있다. WSMTSBIN 호출에는 이 두 조건이 없고 시간 구간 조건만 있다. 두 호출은 모두 IWQBEN=1 분기 안이다.
- 309–312: WWQRST·WSMRST 호출과 IWQONC close는 주석 처리되어 있다.
