---
file: models/EFDC/raw/source_code/EFDC-GVC/vcongrad.for
lines: 457
sha256: 072c8dcff7a60b92d27910b888e5169a0ac5268888724c336eaf10f63c229154
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# vcongrad.for — 판독 구간 기록

구간은 1행부터 457행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–56 | 머리말과 `SUBROUTINE VCONGRAD(ISTL)` 입구(1–6). EFDC-FULL 1.0a·수정 이력(8–17). 외부 모드(external mode) 선형계(linear system)를 전처리 공액경사법(preconditioned conjugate gradient)과 AltiVec 벡터 처리로 푼다는 주석(19–21). 5점 스텐실(stencil) 식은 주석의 `CCC(L)*P(L)+CCS(L)*P(LS)+CCW(L)*P(L-1)+CCE(L)*P(L+1)+CCN(L)*P(LN)` (25), `=FPTMP(L)` (26). LN/LS 조회표와 실제 변수 2:LC-1, 더미 1/LC, LCM의 4배수 제약을 설명(28–38). `INCLUDE 'EFDC.PAR'` (42), `INCLUDE 'EFDC.CMN'` (43). Mac G4 C 루틴 연결 및 PC용 CVMULAD2 설명, 주석의 `[A]=[B]+[C]*[D]` (51), REAL*4 배열 설명(47–53). 포함 파일 내부는 이 기록의 판독 대상이 아니다. |
| 57–96 | 시작 시 6행 VCONGRAD 안. 타이머(timer) 주석(57). `IF(ISCRAY.EQ.0)THEN` (59)은 `TTMP=SECNDS(0.0)` (60). `ELSE` (61)는 `T1TMP=SECOND( )` (62), `CALL TIMEF(WT1TMP)` (63). `IVECDIG=0` (70), `LCM4=LCM/4` (71). P·네 방향 P·RCG·PCG·APCG·RA4·RTMP/RTMP1/RNULL·FPTMP·네 방향 PCG·CCC/CCW/CCE/CCS/CCN/CCCI의 인덱스 1을 모두 0 초기화(73–95). |
| 97–142 | 시작 시 6행 VCONGRAD 안. L=LC..LCM 루프(97)에서 앞 구간의 같은 배열을 0 초기화(98–120), 루프 종료(121). L=2..LA 루프(123)는 LN/LS를 조회하고 `PW(L)=P(L-1)` (126), `PE(L)=P(L+1)` (127), `PS(L)=P(LS)` (128), `PN(L)=P(LN)` (129)으로 이웃 값을 복사한다. LA=LC-1 주석(134). 초기 잔차(residual) RCG를 스텐실로 계산하는 대체 루프는 주석(136–141). |
| 143–180 | 시작 시 6행 VCONGRAD 안. 로그 조건 `IF(IVECDIG.EQ.1)` (143·157·166·175)과 배열 출력 조건 `IF(IVECDIG.EQ.1)THEN` (144·158·167·176)은 단위 8에 단계명 및 L=1..LC의 계수/RCG/RTMP/RCG를 쓴다(145–148·159–162·168–171·177–180). L=2..LA(150)에서 `RCG(L)=-FPTMP(L)` (151), RNULL/RTMP/RTMP1=0(152–154). `CALL CVMULAD2(VAL(LCM),RTMP,RCG,CCC,P)` (164), `CALL CVMULAD2(VAL(LCM),RCG,RTMP,CCS,PS)` (173)은 cval 주석이며 실행 호출이 아니다. |
| 181–245 | 시작 시 6행 VCONGRAD 안. cval 주석 호출은 `CALL CVMULAD2(VAL(LCM),RTMP,RCG,CCW,PW)` (182), `CALL CVMULAD2(VAL(LCM),RCG,RTMP,CCE,PE)` (191), `CALL CVMULAD2(VAL(LCM),RTMP,RCG,CCN,PN)` (200). 로그 조건 `IF(IVECDIG.EQ.1)` (184·193·211·220·235·242), 배열 출력 조건 `IF(IVECDIG.EQ.1)THEN` (185·194·212·221)은 단계명 및 RTMP/RCG/RCG/PCG·RPCG를 출력한다. 옛 RCG 부호 반전·PCG 계산은 주석(202–205). 실행 L=2..LA 루프(207)의 식은 `RCG(L)=-RTMP(L)` (208). PCG 생성 및 두 내적(dot product) 작업 호출 `CALL CVMULAD2(VAL(LCM),PCG,RNULL,RCG,CCCI)` (218), `CALL CVMULAD2(VAL(LCM),RTMP,RNULL,RCG,CCCI)` (232), `CALL CVMULAD2(VAL(LCM),RTMP1,RNULL,RCG,RTMP)` (233)은 주석이다. 직접 RPCG 누적 대체식도 주석(227–230). RPCG=0(237), L=2..LA(238)에서 `RPCG=RPCG+RTMP1(L)` (239). ITER=0(244). |
| 246–291 | 시작 시 6행 VCONGRAD 안. 구분 주석과 반복 이동 대상 `100 CONTINUE` (248), `ITER=ITER+1` (250). L=2..LA(252)에서 LN/LS 조회, `PCGS(L)=PCG(LS)` (255), `PCGW(L)=PCG(L-1)` (256), `PCGE(L)=PCG(L+1)` (257), `PCGN(L)=PCG(LN)` (258). 직접 행렬 곱(matrix product) 루프는 주석(261–266). 다섯 cval 주석 호출은 `CALL CVMULAD2(VAL(LCM),APCG,RNULL,CCC,PCG)` (268), `CALL CVMULAD2(VAL(LCM),RTMP,APCG,CCS,PCGS)` (272), `CALL CVMULAD2(VAL(LCM),APCG,RTMP,CCW,PCGW)` (276), `CALL CVMULAD2(VAL(LCM),RTMP,APCG,CCE,PCGE)` (280), `CALL CVMULAD2(VAL(LCM),APCG,RTMP,CCN,PCGN)` (284). 단계 로그 조건 `IF(IVECDIG.EQ.1)` (270·274·278·282·286). `IF(IVECDIG.EQ.1)THEN` (287)은 L=1..LC의 APCG 출력(288–291). |
| 292–330 | 시작 시 6행 VCONGRAD 안. PAPCG 직접 누적 루프는 주석(293–296), `CALL CVMULAD2(VAL(LCM),RTMP,RNULL,APCG,PCG)` (298)도 cval 주석. 로그 조건 `IF(IVECDIG.EQ.1)` (300·308·322). PAPCG=0(302), L=2..LA(303)에서 `PAPCG=PAPCG+RTMP(L)` (304), RTMP1=P 복사(305). `ALPHA=RPCG/PAPCG` (310). 직접 P 갱신은 주석(312–314). RA4에 ALPHA를 L=2..LA에서 복사(316–318). `CALL CVMULAD2(VAL(LCM),P,RTMP1,RA4,PCG)` (320)은 주석. `IF(IVECDIG.EQ.1)THEN` (323)은 L=1..LC의 P를 출력(324–327), 구분 주석(328–330). |
| 331–369 | 시작 시 6행 VCONGRAD 안. 직접 RCG 갱신 루프는 주석(331–333). L=2..LA(335)에서 `RA4(L)=-ALPHA` (336), RTMP=RCG 복사(337). `CALL CVMULAD2(VAL(LCM),RCG,RTMP,RA4,APCG)` (340)은 주석. 로그 조건 `IF(IVECDIG.EQ.1)` (342·356·360·368), 배열 출력 조건 `IF(IVECDIG.EQ.1)THEN` (343)은 RCG 출력(344–347). 직접 RPCGN 누적 루프는 주석(349–352), `CALL CVMULAD2(VAL(LCM),RTMP,RNULL,RCG,CCCI)` (354), `CALL CVMULAD2(VAL(LCM),RTMP1,RNULL,RTMP,RCG)` (358)도 주석. RPCGN=0(362), L=2..LA(363)에서 `RPCGN=RPCGN+RTMP1(L)` (364), RTMP=RCG 복사(365). |
| 370–419 | 시작 시 6행 VCONGRAD 안. 직접 RSQ 누적 루프(370–373) 및 `CALL CVMULAD2(VAL(LCM),RTMP1,RNULL,RTMP,RCG)` (375)은 주석. 로그 조건 `IF(IVECDIG.EQ.1)` (377·384·406·410). RSQ=0(379), L=2..LA(380)에서 `RSQ=RSQ+RTMP1(L)` (381). `IF(RSQ.LE.RSQM)GOTO 200` (386)은 종료 경로로 이동. `IF(ITER.GE.ITERM)THEN` (388)은 메시지 출력·STOP(389–390). `BETA=RPCGN/RPCG` (393), RPCG=RPCGN 복사(394). 직접 PCG 갱신식은 주석(396–398). L=2..LA에 RA4=BETA 복사(400–402). `CALL CVMULAD2(VAL(LCM),RTMP,RNULL,PCG,RA4)` (404), `CALL CVMULAD2(VAL(LCM),PCG,RTMP,CCCI,RCG)` (408)은 주석. `IF(IVECDIG.EQ.1)THEN` (411)은 L=1..LC의 PCG 출력(412–415). `GOTO 100` (417), 최대 반복 오류 FORMAT(419). |
| 420–440 | 시작 시 6행 VCONGRAD 안. 최종 잔차 주석(423), `200 CONTINUE` (425), RSQ=0(427). L=2..LA 루프(429)는 LN/LS를 조회(430–431), `RSD=CCC(L)*P(L)+CCS(L)*P(LS)+CCW(L)*P(L-1)+CCE(L)*P(L+1)` (432); `$        +CCN(L)*P(LN)-FPTMP(L)` (433), `RSD=RSD*CCCI(L)` (434), `RSQ=RSQ+RSD*RSD` (435)로 전처리 잔차 제곱합을 계산한다. 루프 종료(436). 로그 조건 `IF(IVECDIG.EQ.1)` (438·439)은 단계명과 RSQ 출력. |
| 441–457 | 시작 시 6행 VCONGRAD 안. `IF(ISCRAY.EQ.0)THEN` (443)은 `TCONG=TCONG+SECNDS(TTMP)` (444). `ELSE` (445)는 `T2TMP=SECOND( )` (446), `CALL TIMEF(WT2TMP)` (447), `TCONG=TCONG+T2TMP-T1TMP` (448), `WTCONG=WTCONG+(WT2TMP-WT1TMP)*0.001` (449). 조건 종료(450), 출력 FORMAT(452), 구분 주석·RETURN·END(453–457). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 164–408: CVMULAD2 호출은 모두 cval로 시작하는 주석이다. 직접 계산 대체 루프도 주석으로 남아 있다. 실행 CALL은 TIMEF 두 번이다(63·447).
- 150–155·164–200·207–209·237–240: RTMP/RTMP1을 0 초기화한다. 초기 행렬 곱 호출들은 주석이다. 이어지는 실행문은 RCG=-RTMP와 RPCG에 RTMP1을 합산하는 식이다.
- 70·143–439: IVECDIG는 매 진입에서 0으로 대입한다. 모든 단계/배열 디버깅 출력은 IVECDIG.EQ.1 조건을 갖는다. 이 파일에는 IVECDIG를 1로 바꾸는 실행문이 없다.
- 71: LCM4는 대입 뒤 이 파일에서 사용하지 않는다. ISTL 인수도 입구 선언(6) 외의 실행문에서 참조하지 않는다.
- 310·386–394: ALPHA=RPCG/PAPCG는 수렴 조건보다 앞에 있다. BETA=RPCGN/RPCG는 수렴 및 반복 한도 조건 뒤에 있다. 두 나눗셈 직전의 분모 0 검사문은 없다.
- 379–386·427–435: 반복 중 수렴 판정 RSQ는 RTMP1 합산이다. 종료 뒤 RSQ는 스텐실 잔차에 CCCI를 곱한 값의 제곱합으로 다시 계산한다.
- 73–121·218·404–408: PCG의 0 초기화는 더미 인덱스 1과 LC..LCM에 있다. 2..LA의 초기 PCG 계산 및 갱신 호출은 주석이다.
