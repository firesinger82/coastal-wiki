---
file: models/EFDC/raw/source_code/EFDC-GVC/calqq2.for
lines: 271
sha256: 115426d195f5446a1fd77b7d691b7c15d88d3eb6a8246a9e263dd4a14a4193ba
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calqq2.for — 판독 구간 기록

구간은 1행부터 271행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | 구분 주석과 `SUBROUTINE CALQQ2 (ISTL)` 입구(1–6). EFDC-FULL 1.0a·2001년 11월 1일 수정 머리말(8–10). 난류 강도 제곱(turbulent intensity squared)을 N+1 시각에 계산하고 ISTL이 시간 층 수를 나타낸다는 주석(19–21). 이류 수송(advective transport)을 별도 CALTRANQ로 처리한다는 주석(21–22). `INCLUDE 'EFDC.PAR'` (26), `INCLUDE 'EFDC.CMN'` (27). 포함 파일 내부는 이 판독 대상에 포함하지 않았다. |
| 31–61 | 시작 시 6행 CALQQ2 루틴 안. 기본값 `DELT=DT2` (31), `S3TL=1.0` (32), `S2TL=0.0` (33). `IF(ISTL.EQ.2)THEN` (34)이면 `DELT=DT` (35), `S3TL=0.0` (36), `S2TL=1.0` (37). `BSMALL=1.E-12` (39). 수송량을 QQ 위치로 옮긴다는 주석(43). K=1..KS·L=2..LA(47–48)에 `U2(L,K)=0.5*(U2(L,K)+U2(L,K+1))` (49), `V2(L,K)=0.5*(V2(L,K)+V2(L,K+1))` (50), `UHDY2(L,K)=0.5*(UHDY2(L,K)+UHDY2(L,K+1))` (51), `VHDX2(L,K)=0.5*(VHDX2(L,K)+VHDX2(L,K+1))` (52). K=0..KS·L=2..LA(56–57)에 `W2(L,K)=0.5*(W2(L,K)+W2(L,K+1))` (58). 루프 종료(59–60). |
| 62–97 | 시작 시 6행 CALQQ2 루틴 안. 개방 경계(open boundary) 유입 제거 주석(64). K=1..KS·각 경계 목록 루프에서 남쪽 `IF(VHDX2(LN,K).GT.0.) VHDX2(LN,K)=0.` (72), 서쪽 `IF(UHDY2(L+1,K).GT.0.) UHDY2(L+1,K)=0.` (79), 동쪽 `IF(UHDY2(L,K).LT.0.) UHDY2(L,K)=0.` (86), 북쪽 `IF(VHDX2(L,K).LT.0.) VHDX2(L,K)=0.` (94). 남쪽은 LN=LNC(L)(71), 북쪽은 LS=LSC(L)(93)를 대입한다. |
| 98–135 | 시작 시 6행 CALQQ2 루틴 안. `CALL CALTRANQ (ISTL,0,QQ,QQ1)` (104), `CALL CALTRANQ (ISTL,0,QQL,QQL1)` (106). L=2..LA에 W2(L,0)·W2(L,KC)=0(108–111). 생성·경계조건·수송 해법 및 배열 별명 주석(115–118). K=1..KS·L=2..LA(122–123)의 부력(buoyancy)·전단(shear) 생성 식 `PQQ=DELT*(AB(L,K)*GP*HP(L)*DZIG(K)*(B(L,K+1)-B(L,K))` (126), `&    +AV(L,K)*DZIGSD4(K)*(U(L+1,K+1)-U(L+1,K)+U(L,K+1)-U(L,K))**2` (127), `&    +AV(L,K)*DZIGSD4(K)*(V(LN,K+1)-V(LN,K)+V(L,K+1)-V(L,K))**2)` (128). `UUU(L,K)=QQ(L,K)*HP(L)+2.*PQQ` (129), `VVV(L,K)=QQL1(L,K)*HP(L)+CTE1*DML(L,K)*PQQ` (130). 루프 종료(131–132). |
| 136–153 | 시작 시 6행 CALQQ2 루틴 안. L=2..LA(136)의 삼중대각(tridiagonal) 첫 층 계수. `CLQTMP=-DELT*CDZKK(1)*AQ(L,1)*HPI(L)` (137), `CUQTMP=-DELT*CDZKKP(1)*AQ(L,2)*HPI(L)` (138), `CMQTMP=1.-CLQTMP-CUQTMP` (139), `&       +2.*DELT*SQRT(QQ(L,1))/(CTURB*DML(L,1)*HP(L))` (140), `CMQLTMP=1.-CLQTMP-CUQTMP` (141), `&       +DELT*(SQRT(QQ(L,1))/(CTURB*DML(L,1)*HP(L)))*(1.` (142), `&       +CTE4*DML(L,1)*DML(L,1)*FPROX(1))` (143). `EQ=1./CMQTMP` (144), `EQL=1./CMQLTMP` (145), `CU1(L,1)=CUQTMP*EQ` (146), `CU2(L,1)=CUQTMP*EQL` (147), `UUU(L,1)=(UUU(L,1)-CLQTMP*HP(L)*QQ(L,0))*EQ` (148), `VVV(L,1)=VVV(L,1)*EQL` (149). 표면 경계는 `CUQTMP=-DELT*CDZKKP(KS)*AQ(L,KC)*HPI(L)` (150), `UUU(L,KS)=UUU(L,KS)-CUQTMP*HP(L)*QQ(L,KC)` (151). 루프 종료(152). |
| 154–180 | 시작 시 6행 CALQQ2 루틴 안. K=2..KS·L=2..LA(154–155)의 전진 소거(forward elimination). `CLQTMP=-DELT*CDZKK(K)*AQ(L,K)*HPI(L)` (156), `CUQTMP=-DELT*CDZKKP(K)*AQ(L,K+1)*HPI(L)` (157), `CMQTMP=1.-CLQTMP-CUQTMP` (158), `&       +2.*DELT*SQRT(QQ(L,K))/(CTURB*DML(L,K)*HP(L))` (159), `CMQLTMP=1.-CLQTMP-CUQTMP` (160), `&       +DELT*(SQRT(QQ(L,K))/(CTURB*DML(L,K)*HP(L)))*(1.` (161), `&       +CTE4*DML(L,K)*DML(L,K)*FPROX(K))` (162). `EQ=1./(CMQTMP-CLQTMP*CU1(L,K-1))` (163), `EQL=1./(CMQLTMP-CLQTMP*CU2(L,K-1))` (164), `CU1(L,K)=CUQTMP*EQ` (165), `CU2(L,K)=CUQTMP*EQL` (166), `UUU(L,K)=(UUU(L,K)-CLQTMP*UUU(L,K-1))*EQ` (167), `VVV(L,K)=(VVV(L,K)-CLQTMP*VVV(L,K-1))*EQL` (168). 루프 종료(169–170). K=KS−1..1 간격 −1·L=2..LA(172–173)의 후진 대입(back substitution): `UUU(L,K)=UUU(L,K)-CU1(L,K)*UUU(L,K+1)` (174), `VVV(L,K)=VVV(L,K)-CU2(L,K)*VVV(L,K+1)` (175). 루프 종료(176–177). |
| 181–213 | 시작 시 6행 CALQQ2 루틴 안. K=1..KS·L=2..LA(181–182)에 `QQ1(L,K)=S2TL*QQ1(L,K)+S3TL*QQ(L,K)` (183), `QQHDH=UUU(L,K)*HPI(L)` (184), `QQ(L,K)=MAX(QQHDH,QQMIN)` (185), `QQ(L,K)=SPB(L)*QQ(L,K)+(1.-SPB(L))*QQMIN` (186). 다음 같은 범위(192–193)에 `QQL1(L,K)=S2TL*QQL1(L,K)+S3TL*QQL(L,K)` (194), `QQHDH=VVV(L,K)*HPI(L)` (195), `QQL(L,K)=MAX(QQHDH,QQLMIN)` (196), `QQL(L,K)=SPB(L)*QQL(L,K)+(1.-SPB(L))*QQLMIN` (197), `DMLTMP=QQL(L,K)/QQ(L,K)` (198), `DMLTMP=MAX(DMLTMP,DMLMIN)` (199), `DELB=B(L,K)-B(L,K+1)` (200). 길이 척도(length scale) 제한 `IF(DELB.GT.0.0.AND.ISLLIM.EQ.2)THEN` (201)이면 `DMLMAX=SQRT(RIQMAX)*SQRT(QQ(L,K)/(G*HP(L)*DZIG(K)*DELB))` (202), `DML(L,K)=MIN(DMLMAX,DMLTMP)` (203), `QQL(L,K)=QQ(L,K)*DML(L,K)` (204). 205행 ELSE는 DMLTMP를 DML에 복사(206). 조건 밖에서 `DML(L,K)=SPB(L)*DML(L,K)+(1.-SPB(L))*DMLMIN` (208). 루프 종료(209–210). |
| 214–224 | 시작 시 6행 CALQQ2 루틴 안. `IF(ISTOPT(0).GE.2)THEN` (214), K=1..KS·L=2..LA(215–216). `DELBSQ=( DZIG(K)*(B(L,K+1)-B(L,K)) )**2` (217), `BBT(L,K)=CTURBB2(L,K)*DML(L,K)*AB(L,K)*DELBSQ/SQRT(QQ(L,K))` (218). 루프·조건 종료(219–221). |
| 225–271 | 시작 시 6행 CALQQ2 루틴 안. 남쪽 QQ/QQL/DML 경계 복사(225–232), 서쪽 복사(236–243), 동쪽 복사(247–254), 북쪽 복사(258–266)는 모두 C 주석. 주석 처리된 남쪽 블록은 LN=LNC(L)를 사용하며 L=LCBS(LL) 대입은 적혀 있지 않다(225–232). 구분 주석, `RETURN` (270), `END` (271). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 39: BSMALL은 1.E-12 대입 뒤 이 파일의 조건이나 계산식에서 참조되지 않는다.
- 49–58·72–94·109–110: U2/V2/UHDY2/VHDX2/W2 평균은 같은 배열을 덮어쓴다. 경계 유입 제거도 UHDY2/VHDX2를 덮어쓴다. 이후 W2의 바닥·표면은 0 설정하며 이 파일에는 평균 전 값 복원문이 없다.
- 104–106·129–130: QQ와 QQL에 CALTRANQ를 각각 호출한다. 그 뒤 UUU 초기 항은 QQ를 사용하고 VVV 초기 항은 QQL1을 사용한다. CALTRANQ 내부의 시간 층 처리는 이 파일 판독 범위 밖이다.
- 136–170: 해법은 AQ(L,2) 및 K=1 계수를 사용한다. 이 블록에는 KC≤2를 별도로 처리하는 조건이 없다.
- 144–145·163–164: 대각 계수 및 전진 소거 분모의 역수 계산 앞에 분모 크기를 검사하는 실행 조건은 없다.
- 197–208: QQL에 SPB 혼합을 적용한 뒤 부력 제한 참 분기는 QQL=QQ*DML을 다시 계산한다. 마지막 SPB 혼합은 DML에만 적용한다. 마지막 DML 혼합 뒤에 QQL을 다시 계산하는 문장은 없다.
- 214–221: BBT 갱신은 ISTOPT(0)≥2 조건 안에 있다. 해당 조건의 ELSE에서 BBT를 설정하는 문장은 없다.
- 225–266: 네 방향 QQ/QQL/DML 경계 복사 루프는 모두 주석 처리되어 있다. 남쪽 주석 루프에는 경계 목록에서 L을 가져오는 대입이 없다(225–232).
