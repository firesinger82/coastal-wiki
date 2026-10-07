---
file: models/EFDC/raw/source_code/EFDC-GVC/rvelpltv.for
lines: 592
sha256: 01d9e3186ed85046431aeb2014fd5b64c4b053fb0790db822115e1fb05ac2143
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# rvelpltv.for — 판독 구간 기록

구간은 1행부터 592행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–44 | 머리말과 `SUBROUTINE RVELPLTV` (6). 버전·수정일·변경 이력 주석(8–17). 목적 주석은 VELPLTV라는 이름으로 임의 (I,J) 열에 수직인 법선 속도(normal velocity) 및 단면 접선 속도(tangential velocity)·수직속도(vertical velocity) 벡터 출력을 적는다(19–21). EFDC.PAR·EFDC.CMN 포함(25–26). RVELN·RVELT·RW, PVELN·PVELT·PWX, RLVELN·RLVELT·RLW는 모두 REAL(KCM,100)(30–38). 80자 제목 9개 선언(39–41). 구분 주석 포함. 포함 파일 내부는 판독하지 않았다. |
| 45–62 | 시작 시 6행 RVELPLTV 안. `IF(JSRVPV.NE.1) GOTO 300` (45)은 초기화를 건너뛴다. 초기화 경로는 법선 등치선(contour)·접선 등치선·접선 벡터 각각의 ERT·VPT·MMT 제목 9개를 설정한다(51–59). 제목은 약어만 사용하며 이 선언부에는 약어 정의가 없다. LEVELS=KC 복사(61). 구분 주석 포함. |
| 63–120 | 시작 시 6행 RVELPLTV 안이며 초기화 경로. 독립 `IF(ISECVPV.GE.1)THEN` (63), `IF(ISECVPV.GE.2)THEN` (92). 각 참 분기는 법선 RVLCNV·PVLCNV·MVLCNV, 접선 RVLCVT·PVLCVT·MVLCVT, 벡터 RVLVCV·PVLVCV·MVLVCV의 해당 번호 1·2 `.OUT` 파일을 열고 삭제 후 재개방한다(64–90·93–119). 번호 1은 단위 11·21·31·41·51·61·71·81·91, 번호 2는 각 단위에 1을 더한 번호이다. OPEN에는 STATUS 지정이 없다. |
| 121–178 | 시작 시 6행 RVELPLTV 안이며 초기화 경로. 독립 `IF(ISECVPV.GE.3)THEN` (121), `IF(ISECVPV.GE.4)THEN` (150). 앞 구간의 9개 파일 종류를 번호 3·4로 열고 삭제 후 재개방한다(122–148·151–177). 단위는 번호 3에서 13·23·33·43·53·63·73·83·93, 번호 4에서 14·24·34·44·54·64·74·84·94이다. |
| 179–236 | 시작 시 6행 RVELPLTV 안이며 초기화 경로. 독립 `IF(ISECVPV.GE.5)THEN` (179), `IF(ISECVPV.GE.6)THEN` (208). 9개 파일 종류를 번호 5·6으로 열고 삭제 후 재개방한다(180–206·209–235). 단위는 번호 5에서 15·25·35·45·55·65·75·85·95, 번호 6에서 16·26·36·46·56·66·76·86·96이다. |
| 237–294 | 시작 시 6행 RVELPLTV 안이며 초기화 경로. 독립 `IF(ISECVPV.GE.7)THEN` (237), `IF(ISECVPV.GE.8)THEN` (266). 9개 파일 종류를 번호 7·8로 열고 삭제 후 재개방한다(238–264·267–293). 단위는 번호 7에서 17·27·37·47·57·67·77·87·97, 번호 8에서 18·28·38·48·58·68·78·88·98이다. |
| 295–324 | 시작 시 6행 RVELPLTV 안이며 초기화 경로. `IF(ISECVPV.GE.9)THEN` (295).9개 파일 종류를 번호 9로 열고 삭제 후 재개방한다(296–322). 단위는 19·29·39·49·59·69·79·89·99이다. 분기 종료·주석(323–324). |
| 325–377 | 시작 시 6행 RVELPLTV 안이며 초기화 경로. IS=1..ISECVPV에서 `LUN1=10+IS` (326), `LUN2=20+IS` (327), `LUN3=30+IS` (328), `LUN4=40+IS` (329), `LUN5=50+IS` (330), `LUN6=60+IS` (331), `LUN7=70+IS` (332), `LUN8=80+IS` (333), `LUN9=90+IS` (334). LINES=NIJVPV(IS)(335). 각 단위에 해당 TITLE·CVTITLE, LINES·LEVELS, ZZ(1..KC)를 기록한다(336–362). 9개 파일 CLOSE·IS 루프 종료(363–372), JSRVPV=0(374), 구분 주석(373·375–377). |
| 378–386 | 시작 시 6행 RVELPLTV 안. 라벨 300(378). `IF(ISDYNSTP.EQ.0)THEN` (380): `TIME=DT*FLOAT(N)+TCON*TBEGIN` (381), `TIME=TIME/TCON` (382). `ELSE` (383): `TIME=TIMESEC/TCON` (384). 분기 종료·주석(385–386). |
| 387–452 | 시작 시 6행 RVELPLTV 안. 독립 `IF(ISECVPV.GE.1)THEN` (387), `IF(ISECVPV.GE.2)THEN` (398), `IF(ISECVPV.GE.3)THEN` (409), `IF(ISECVPV.GE.4)THEN` (420), `IF(ISECVPV.GE.5)THEN` (431), `IF(ISECVPV.GE.6)THEN` (442). 각 번호 1–6의 9개 법선·접선·벡터 파일을 대응 단위에서 append로 연다(388–396·399–407·410–418·421–429·432–440·443–451). 각 분기 종료 포함. |
| 453–486 | 시작 시 6행 RVELPLTV 안. 독립 `IF(ISECVPV.GE.7)THEN` (453), `IF(ISECVPV.GE.8)THEN` (464), `IF(ISECVPV.GE.9)THEN` (475). 번호 7–9의 9개 법선·접선·벡터 파일을 대응 단위에서 append로 연다(454–462·465–473·476–484). 분기 종료·주석(463·474·485–486). |
| 487–529 | 시작 시 6행 RVELPLTV 안. `DO IS=1,ISECVPV` (487), `LUN1=10+IS` (488), `LUN2=20+IS` (489), `LUN3=30+IS` (490), `LUN4=40+IS` (491), `LUN5=50+IS` (492), `LUN6=60+IS` (493), `LUN7=70+IS` (494), `LUN8=80+IS` (495), `LUN9=90+IS` (496). 각 파일에 N·TIME(497–505). 단면 각도 변환은 `COSC=COS(PI*ANGVPV(IS)/180.)` (506), `SINC=SIN(PI*ANGVPV(IS)/180.)` (507). NN=1..NIJVPV(IS)에서 I·J·L·LN·LS 복사(508–513), K=1..KC(514). 오일러 성분 원문: `RVELN(K,NN)=50.*((UHLPF(L+1,K)+UHLPF(L,K))*COSC` (515); `     &            +(VHLPF(LN,K)+VHLPF(L,K))*SINC)/HLPF(L)` (516). `RVELT(K,NN)=-50.*((UHLPF(L+1,K)+UHLPF(L,K))*SINC` (517); `     &            -(VHLPF(LN,K)+VHLPF(L,K))*COSC)/HLPF(L)` (518). `RW(K,NN)=50.*(WLPF(L,K)+WLPF(L,K-1))` (519). 벡터 퍼텐셜 성분: `PVELN(K,NN)=50.*((UVPT(L+1,K)+UVPT(L,K))*COSC` (520); `     &            +(VVPT(LN,K)+VVPT(L,K))*SINC)/HLPF(L)` (521). `PVELT(K,NN)=-50.*((UVPT(L+1,K)+UVPT(L,K))*SINC` (522); `     &            -(VVPT(LN,K)+VVPT(L,K))*COSC)/HLPF(L)` (523). `PWX(K,NN)=50.*(WVPT(L,K)+WVPT(L,K-1))` (524). 합은 `RLVELN(K,NN)=RVELN(K,NN)+PVELN(K,NN)` (525), `RLVELT(K,NN)=RVELT(K,NN)+PVELT(K,NN)` (526), `RLW(K,NN)=RW(K,NN)+PWX(K,NN)` (527). K·NN 루프 종료(528–529). |
| 530–578 | 시작 시 6행 RVELPLTV·487행 IS 루프 안. 새 NN=1..NIJVPV(IS) 루프에서 I·J·L을 얻고(530–533), `ZETA=HLPF(L)-HMP(L)` (534), HBTMP=HMP(L)(535). HBTMP 대안과 이전 WRITE 9개는 주석(536–545). 모든 단위에 IL·JL·DLON·DLAT·ZETA·HBTMP를 기록한다(546–554). LUN1–3은 RVELN·PVELN·RLVELN, LUN4–6은 RVELT·PVELT·RLVELT, LUN7–9는 접선 성분에 이어 RW·PWX·RLW를 각각 K=1..KC 순으로 출력한다(555–566). NN 루프·9개 파일·IS 루프 종료(567–577), 주석(578). |
| 579–592 | 시작 시 6행 RVELPLTV 안이며 IS 루프 밖. 구분 주석(579–580). FORMAT 99=A40·2X·A20, 100=I10·F12.4, 101=2I10, 200=2I5·1X·6E14.6, 250=12E12.4(581–585). CMRM 대안 FORMAT은 주석(586–587). 구분 주석·RETURN·END(588–592). 이 파일에는 서브루틴 CALL이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30–38·508·515–527·530·555–566: 작업 배열의 두 번째 차원은 100으로 고정되어 있다. NN 루프 상한은 NIJVPV(IS)이며 이 파일에는 NIJVPV(IS)<=100 검사가 없다.
- 63–323·325·387–485·487: 이름을 명시한 파일 개방 분기는 단면 번호 1–9까지이다. 머리말·자료 루프의 상한은 ISECVPV이며 이 파일에는 ISECVPV<=9 검사가 없다.
- 513: LS=LSC(L)을 대입한다. 이 파일의 이후 실행식은 LS를 참조하지 않는다.
- 515–524: 성분 계산은 계수 50을 고정 사용한다. 법선·접선 성분은 HLPF로 나누며 이 파일에는 해당 계산 전에 HLPF=0을 검사하는 조건이 없다.
