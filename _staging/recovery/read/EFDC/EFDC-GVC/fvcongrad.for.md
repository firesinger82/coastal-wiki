---
file: models/EFDC/raw/source_code/EFDC-GVC/fvcongrad.for
lines: 456
sha256: 0c7af3ce151bc9458bbd12b9380426d408db67345be1dacaab821dbdddcc16f2
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# fvcongrad.for — 판독 구간 기록

구간은 1행부터 456행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–55 | 구분 주석과 `SUBROUTINE FVCONGRAD(ISTL)` 선언(1–6). EFDC-FULL 1.0a·수정자·날짜·변경 이력 틀(8–18). 외부 모드(external mode) 선형계를 전처리 공액기울기법(preconditioned conjugate gradient scheme)과 FVMULAD2로 푼다는 주석(19–22). 5점 스텐실(stencil) 원문 `CCC(L)*P(L)+CCS(L)*P(LS)+CCW(L)*P(L-1)+CCE(L)*P(L+1)+CCN(L)*P(LN)` (26), `=FPTMP(L)` (27). LN/LS 조회표(29–30), 실제 미지수 2..LC-1 및 더미(dummy) 위치 1·LC, 저장 크기 LCM>=LC·4의 배수라는 주석(32–39). `EFDC.PAR`·`EFDC.CMN` 포함(43–44). 연결할 벡터 루틴은 `[A]=[B]+[C]*[D]` (50), 1D REAL*4 배열이라는 주석(52). |
| 56–95 | 시작 시 6행 FVCONGRAD 루틴 안. 타이머(timer) 조건 `IF(ISCRAY.EQ.0)THEN` (58)은 `TTMP=SECNDS(0.0)` (59). `ELSE` (60)는 `T1TMP=SECOND( )` (61), `CALL TIMEF(WT1TMP)` (62). 고정 진단 설정 `IVECDIG=0` (69), `LCM4=LCM/4` (70). 위치 1의 P·이웃 P·RCG·PCG·APCG·RA4·RTMP/RTMP1·RNULL·FPTMP·이웃 PCG·스텐실 계수·CCCI를 0으로 초기화한다(72–94). 구분·빈 주석도 포함한다. |
| 96–141 | 시작 시 6행 FVCONGRAD 루틴 안. `DO L=LC,LCM` (96)에서 97–119행의 P·잔차(residual)·탐색 벡터·작업 배열·우변·계수를 0으로 설정한다. `DO L=2,LA` (122)에서 LN=LNC(L)·LS=LSC(L)(123–124), `PW(L)=P(L-1)` (125), `PE(L)=P(L+1)` (126), PS=P(LS)·PN=P(LN) 복사(127–128). LA=LC-1 주석(133). 직접 스텐실 잔차 루프·식은 주석 처리되어 있다(135–140). |
| 142–179 | 시작 시 6행 FVCONGRAD 루틴 안. 진단 로그 조건 `IF(IVECDIG.EQ.1)` (142·156·165). 진단 배열 출력의 원문 조건 `IF(IVECDIG.EQ.1)THEN` (143·157·166)은 각각 L=1..LC에서 스텐실 계수와 P(144–146), RCG(158–160), RTMP(167–169)를 출력한다. 실행 초기 잔차 루프 `DO L=2,LA` (149)에서 `RCG(L)=-FPTMP(L)` (150), RNULL·RTMP·RTMP1=0(151–153). 중앙 계수 더하기 `CALL FVMULAD2(LCM,LC,RTMP,RCG,CCC,P)` (163). 남쪽 계수 더하기 `CALL FVMULAD2(LCM,LC,RCG,RTMP,CCS,PS)` (172). 진단 로그 조건 `IF(IVECDIG.EQ.1)` (174), 배열 출력 조건 `IF(IVECDIG.EQ.1)THEN` (175)은 RCG를 출력한다(176–178). |
| 180–225 | 시작 시 6행 FVCONGRAD 루틴 안. 서쪽 항 `CALL FVMULAD2(LCM,LC,RTMP,RCG,CCW,PW)` (181), 동쪽 항 `CALL FVMULAD2(LCM,LC,RCG,RTMP,CCE,PE)` (190), 북쪽 항 `CALL FVMULAD2(LCM,LC,RTMP,RCG,CCN,PN)` (199). 진단 로그 조건 `IF(IVECDIG.EQ.1)` (183·192·210·219), 배열 출력 조건 `IF(IVECDIG.EQ.1)THEN` (184·193·211·220)은 RTMP·RCG·RCG·PCG를 각각 L=1..LC에서 출력한다(185–187·194–196·212–214·221–223). 주석 처리된 잔차 부호 반전·전처리식(201–204). 실행 `DO L=2,LA` (206)의 `RCG(L)=-RTMP(L)` (207). 전처리된 탐색 벡터 생성 `CALL FVMULAD2(LCM,LC,PCG,RNULL,RCG,CCCI)` (217). |
| 226–246 | 시작 시 6행 FVCONGRAD 루틴 안. 직접 내적(dot product) RPCG 루프는 주석 처리(226–229). 실행 `CALL FVMULAD2(LCM,LC,RTMP,RNULL,RCG,CCCI)` (231), `CALL FVMULAD2(LCM,LC,RTMP1,RNULL,RCG,RTMP)` (232). 진단 조건 `IF(IVECDIG.EQ.1)` (234·241). RPCG=0 초기화(236), `DO L=2,LA` (237)의 `RPCG=RPCG+RTMP1(L)` (238). ITER=0 초기화(243), 구분 주석(245–246). |
| 247–291 | 시작 시 6행 FVCONGRAD 루틴 안. 반복 점프 목적지 `100 CONTINUE` (247), `ITER=ITER+1` (249). L 루프(251)에서 LN/LS 조회(252–253), PCGS에 남쪽 PCG 복사(254), `PCGW(L)=PCG(L-1)` (255), `PCGE(L)=PCG(L+1)` (256), PCGN에 북쪽 PCG 복사(257). 직접 행렬·벡터 곱(matrix-vector product)은 주석 처리(260–265). 실행 호출 `CALL FVMULAD2(LCM,LC,APCG,RNULL,CCC,PCG)` (267), `CALL FVMULAD2(LCM,LC,RTMP,APCG,CCS,PCGS)` (271), `CALL FVMULAD2(LCM,LC,APCG,RTMP,CCW,PCGW)` (275), `CALL FVMULAD2(LCM,LC,RTMP,APCG,CCE,PCGE)` (279), `CALL FVMULAD2(LCM,LC,APCG,RTMP,CCN,PCGN)` (283). 각 진단 로그 조건 `IF(IVECDIG.EQ.1)` (269·273·277·281·285). APCG 배열 출력 조건 `IF(IVECDIG.EQ.1)THEN` (286), L=1..LC 출력(287–289), 조건 종료(290). |
| 292–327 | 시작 시 6행 FVCONGRAD 루틴 안. 직접 PAPCG 내적 주석(292–295). 실행 곱 `CALL FVMULAD2(LCM,LC,RTMP,RNULL,APCG,PCG)` (297), 진단 조건 `IF(IVECDIG.EQ.1)` (299·307). PAPCG=0(301), L 루프(302)의 `PAPCG=PAPCG+RTMP(L)` (303), 이전 P를 RTMP1에 복사(304). 이동 계수 `ALPHA=RPCG/PAPCG` (309). 직접 P 갱신 루프는 주석 처리(311–313). L 루프(315)에서 ALPHA를 RA4에 복사(316). 갱신 `CALL FVMULAD2(LCM,LC,P,RTMP1,RA4,PCG)` (319). 진단 조건 `IF(IVECDIG.EQ.1)` (321), 배열 출력 조건 `IF(IVECDIG.EQ.1)THEN` (322)은 L=1..LC에서 P를 출력한다(323–325). |
| 328–368 | 시작 시 6행 FVCONGRAD 루틴 안. 직접 잔차 갱신식은 주석 처리(330–332). `DO L=1,LCM` (334)의 `RA4(L)=-ALPHA` (335), RTMP=RCG 복사(336). `CALL FVMULAD2(LCM,LC,RCG,RTMP,RA4,APCG)` (339). 진단 로그 조건 `IF(IVECDIG.EQ.1)` (341), 배열 조건 `IF(IVECDIG.EQ.1)THEN` (342)은 RCG를 출력한다(343–345). 직접 RPCGN 내적은 주석 처리(348–351). 실행 곱 `CALL FVMULAD2(LCM,LC,RTMP,RNULL,RCG,CCCI)` (353), `CALL FVMULAD2(LCM,LC,RTMP1,RNULL,RTMP,RCG)` (357). 진단 조건 `IF(IVECDIG.EQ.1)` (355·359·367). RPCGN=0(361), L 루프(362)의 `RPCGN=RPCGN+RTMP1(L)` (363), RTMP=RCG 복사(364). |
| 369–419 | 시작 시 6행 FVCONGRAD 루틴 안. 직접 RSQ 계산 주석(369–372). 곱 `CALL FVMULAD2(LCM,LC,RTMP1,RNULL,RTMP,RCG)` (374). 진단 조건 `IF(IVECDIG.EQ.1)` (376·383). RSQ=0(378), L 루프(379)의 `RSQ=RSQ+RTMP1(L)` (380). 수렴 조건 `IF(RSQ.LE.RSQM)GOTO 200` (385). 반복 상한 조건 `IF(ITER.GE.ITERM)THEN` (387)은 최대 반복 초과 메시지를 쓰고 STOP한다(388–389). 수렴·상한 조건을 통과하면 `BETA=RPCGN/RPCG` (392), RPCG=RPCGN 복사(393). 직접 PCG 갱신 주석(395–397). L 루프(399)는 BETA를 RA4에 복사(400). 호출 `CALL FVMULAD2(LCM,LC,RTMP,RNULL,PCG,RA4)` (403), `CALL FVMULAD2(LCM,LC,PCG,RTMP,CCCI,RCG)` (407). 진단 조건 `IF(IVECDIG.EQ.1)` (405·409), `IF(IVECDIG.EQ.1)THEN` (410)은 PCG 배열을 출력한다(411–413). GOTO 100(416), FORMAT 600 메시지(418). |
| 420–456 | 시작 시 6행 FVCONGRAD 루틴 안. 최종 잔차 주석과 `200 CONTINUE` (424). RSQ=0(426). L 루프(428)에서 LN/LS 조회(429–430), `RSD=CCC(L)*P(L)+CCS(L)*P(LS)+CCW(L)*P(L-1)+CCE(L)*P(L+1)` (431); `$        +CCN(L)*P(LN)-FPTMP(L)` (432), `RSD=RSD*CCCI(L)` (433), `RSQ=RSQ+RSD*RSD` (434). 진단 조건 `IF(IVECDIG.EQ.1)` (437–438). 시간 누적 조건 `IF(ISCRAY.EQ.0)THEN` (442)은 `TCONG=TCONG+SECNDS(TTMP)` (443). `ELSE` (444)는 `T2TMP=SECOND( )` (445), `CALL TIMEF(WT2TMP)` (446), `TCONG=TCONG+T2TMP-T1TMP` (447), `WTCONG=WTCONG+(WT2TMP-WT1TMP)*0.001` (448). FORMAT 800·구분 주석·RETURN·END(451–456). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6: ISTL은 인수로 선언된다. 이후 이 파일에는 ISTL 참조가 없다.
- 70: LCM4=LCM/4를 대입한다. 이후 이 파일에는 LCM4 참조가 없다.
- 69·142–438: IVECDIG를 0으로 고정한다. 모든 벡터 진단 출력 조건은 IVECDIG=1이다.
- 243–309·385·392: 최초 수렴 검사는 ALPHA=RPCG/PAPCG 계산 뒤에 있다. PAPCG와 RPCG를 분모로 쓰는 대입 앞에는 각각의 0 여부 검사가 없다.
- 374–385·431–434: 반복 중 수렴 판정용 RSQ는 RCG 제곱합이다. 종료 후 다시 계산하는 RSQ는 스텐실 잔차에 CCCI를 곱한 값의 제곱합이다.
