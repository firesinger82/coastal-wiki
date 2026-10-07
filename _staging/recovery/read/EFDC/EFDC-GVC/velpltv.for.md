---
file: models/EFDC/raw/source_code/EFDC-GVC/velpltv.for
lines: 250
sha256: c5b4758ba97f3e0c4c94d0840efd378eb07e6e1489238416bb91568760230c4c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# velpltv.for — 판독 구간 기록

구간은 1행부터 250행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | 머리말과 `SUBROUTINE VELPLTV` 입구(1–6). EFDC-FULL 1.0a·수정 이력 주석(8–17). 임의 격자점 순서에 대한 수직 단면(vertical plane)의 법선 유속(normal velocity) 등고선(contour) 및 접선 유속(tangential velocity)·연직 유속(vertical velocity) 벡터 출력 설명(19–21). `INCLUDE 'EFDC.PAR'` (25), `INCLUDE 'EFDC.CMN'` (26). VELN/VELT/WZCORD는 REAL(KCM,100), 제목 두 개는 CHARACTER*80(30–33). 포함 파일 내부는 이 기록의 판독 대상이 아니다. |
| 37–78 | 시작 시 6행 VELPLTV 안. `IF(JSVPV.NE.1) GOTO 300` (37)은 헤더 부분을 건너뛴다. LEVELS=KC와 법선/접선 유속 제목 대입(43–45). `IF(ISECVPV.GE.1)THEN` (47), `IF(ISECVPV.GE.2)THEN` (55), `IF(ISECVPV.GE.3)THEN` (63), `IF(ISECVPV.GE.4)THEN` (71)은 각각 VELCNV1..4.OUT와 VELVCV1..4.OUT를 단위 11..14 및 21..24에 열고 DELETE로 닫은 뒤 재개방한다(48–78). 각 조건은 독립적이다. |
| 79–119 | 시작 시 6행 VELPLTV 안. `IF(ISECVPV.GE.5)THEN` (79), `IF(ISECVPV.GE.6)THEN` (87), `IF(ISECVPV.GE.7)THEN` (95), `IF(ISECVPV.GE.8)THEN` (103), `IF(ISECVPV.GE.9)THEN` (111)은 각각 VELCNV5..9.OUT와 VELVCV5..9.OUT를 단위 15..19 및 25..29로 삭제·재개방한다(80–118). 빈 주석(119). |
| 120–139 | 시작 시 6행 VELPLTV 안. IS=1..ISECVPV 루프(120)에서 `LUN1=10+IS` (121), `LUN2=20+IS` (122), LINES=NIJVPV(IS) 복사(123). 두 파일에 TITLE1/TITLE2와 CVTITLE(LUN1/LUN2), LINES/LEVELS, K=1..KC의 ZZ를 쓴다(124–129). 단위 두 개 CLOSE·루프 종료(130–132). JSVPV=0(134), 구분 주석과 이동 대상 `300 CONTINUE` (138). |
| 140–183 | 시작 시 6행 VELPLTV 안. `IF(ISDYNSTP.EQ.0)THEN` (140)은 `TIME=DT*FLOAT(N)+TCON*TBEGIN` (141), `TIME=TIME/TCON` (142). `ELSE` (143)는 `TIME=TIMESEC/TCON` (144). `IF(ISECVPV.GE.1)THEN` (147), `IF(ISECVPV.GE.2)THEN` (151), `IF(ISECVPV.GE.3)THEN` (155), `IF(ISECVPV.GE.4)THEN` (159), `IF(ISECVPV.GE.5)THEN` (163), `IF(ISECVPV.GE.6)THEN` (167), `IF(ISECVPV.GE.7)THEN` (171), `IF(ISECVPV.GE.8)THEN` (175), `IF(ISECVPV.GE.9)THEN` (179)은 각 단면 법선/접선 파일을 POSITION='APPEND'로 연다(148–182). |
| 184–201 | 시작 시 6행 VELPLTV 안. IS=1..ISECVPV 루프(184), `LUN1=10+IS` (185), `LUN2=20+IS` (186), N/TIME 출력(187–188). `COSC=COS(PI*ANGVPV(IS)/180.)` (189), `SINC=SIN(PI*ANGVPV(IS)/180.)` (190)으로 각도를 변환. NN=1..NIJVPV(IS)(191)에서 I/J/L/LN/LS 조회(192–196), K=1..KC 루프(197). `VELN(K,NN)=50.*((U(L+1,K)+U(L,K))*COSC+(V(LN,K)` (198); `&                                         +V(L,K))*SINC)` (199). `VELT(K,NN)=-50.*((U(L+1,K)+U(L,K))*SINC-(V(LN,K)` (200); `&                                          +V(L,K))*COSC)` (201). |
| 202–217 | 시작 시 6행 VELPLTV·184행 IS 루프·191행 NN 루프·197행 K 루프 안. 연직 좌표 유속 식은 `WZCORD(K,NN)=50.*(W(L,K)+W(L,K-1))+GI*ZZ(K)*(DTI*(P(L)-P1(L))` (202); `&         +50.*(U(L+1,K)*(P(L+1)-P(L))*DXIU(L+1)` (203); `&              +U(L,K)*(P(L)-P(L-1))*DXIU(L)` (204); `&              +V(LN,K)*(P(LN)-P(L))*DYIV(LN)` (205); `&              +V(L,K)*(P(L)-P(LS))*DYIV(L)))` (206); `&         +50.*(1.-ZZ(K))*(U(L+1,K)*(BELV(L+1)-BELV(L))*DXIU(L+1)` (207); `&                         +U(L,K)*(BELV(L)-BELV(L-1))*DXIU(L)` (208); `&                         +V(LN,K)*(BELV(LN)-BELV(L))*DYIV(LN)` (209); `&                         +V(L,K)*(BELV(L)-BELV(LS))*DYIV(L))` (210). W 평균·수면 변화·수평 압력(pressure) 차·바닥 표고(bottom elevation) 차의 항을 포함한다. HMP 차를 빼는 대체 연속행은 주석(211–214). K/NN 루프 종료(216–217). |
| 218–235 | 시작 시 6행 VELPLTV·184행 IS 루프 안. 두 번째 NN=1..NIJVPV(IS) 루프(218)는 I/J/L 조회(219–221), `ZETA=P(L)*GI-SBPLTV(1)*(HMP(L)+BELV(L))` (222), HBTMP=HMP 복사(223). 대체 HBTMP 및 WRITE는 주석(224–226). 두 파일에 IL/JL·DLON/DLAT·ZETA·HBTMP 출력(227–228). 법선 파일에는 K=1..KC의 VELN(229), 접선 파일에는 VELT와 WZCORD(230–231). NN 루프·두 단위 CLOSE·IS 루프 종료(232–235). |
| 236–250 | 시작 시 6행 VELPLTV 안. 구분 주석(236–238). 제목·시간·행/수준 수·셀 메타데이터·수직 값 FORMAT 정의(239–243). 다른 FORMAT 두 개는 CMRM 주석(244–245). 구분 주석·RETURN·END(246–250). 이 루틴에는 CALL 문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 47–118·120–132·147–182·184–188: 명시적 파일 OPEN은 단면 1..9까지만 있다. 헤더 및 값 출력 루프 상한은 ISECVPV이며 이 파일에는 ISECVPV<=9 검사문이 없다.
- 30–32·191–210·218–231: 세 작업 배열의 두 번째 크기는 100이다. NN 루프 상한은 NIJVPV(IS)이다. 이 파일에는 NIJVPV(IS)<=100 검사문이 없다.
- 184·222: ZETA 식은 모든 IS에 SBPLTV(1)을 사용한다. 이 식에는 SBPLTV(IS)가 없다.
