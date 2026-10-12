---
file: models/ShorelineS/raw/source_code/shorelines/functions/dune_erosion.m
lines: 152
sha256: 67dcf09a14e781d7b880e1d3b0a27f53f9ac5911476b2f78afefc3565da98a8a
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# dune_erosion.m — 판독 구간 기록

구간은 1행부터 152행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–64 | 함수 시그니처 `function [wberm,qs_avg,qss_avg,ql_avg,R]=dune_erosion(runupform,runupfactor,wberm_old,dfelev0,dfelev,dcelev,h0,sqrHsL0,SWL,TPc,cs,cstill,xtill,perctill,A,dt,dtnum)` (1). Larson 방식의 사구(dune) 침식과 버름(berm) 폭·모래 공급량을 계산한다는 주석(4–9). 입력·출력·단위(11–35), perctill의 주석 범위 0..100(25). 저작권·연락처·LGPL 2.1 이상·무보증과 빈 줄(37–64). |
| 65–79 | wberm_old 복사(65). 연간 초 수·반복 수·최소 반복 수 `spyr=365*24*3600;` (66); `nt=round(dt/dtnum,0);` (67); `nt=max(nt,1);` (68). qd·qs·qss·ql·alfa·세 평균 배열 0 초기화(69–76). 사구 정상 높이 하한·활성 사구 높이·버름 기준 폭 `dcelev=max(dcelev,dfelev0+0.2);` (77); `DH=dcelev-dfelev0;` (78); `wbermmin=5;` (79). |
| 80–104 | 반복 `for step=1:nt` (80). 경사 하한 0.001·상한 0.5 `slope=max(min(dfelev./(wberm-wbermmin),0.5),0.001);` (81). Stockdon 선택 `if ~isempty(findstr(lower(runupform),'sto'))` (82), 처오름(runup) 식 `R = runupfactor*1.1*sqrHsL0.*(0.35*slope + sqrt(0.563*(slope.^2) + 0.004)/2);` (84). Ghonim 선택 `elseif ~isempty(findstr(lower(runupform),'gho'))` (85), 식 `R = runupfactor*slope.*sqrHsL0;` (87). 기본 경로 `else` (88)는 Larson 주석(89)과 `R = runupfactor*0.158*sqrHsL0;` (92). 대체 감쇠식·조건은 주석 처리(90–96). 침식 마스크·초과 수위 `ero=SWL+R>dfelev;` (99); `wldf=SWL+R-dfelev;` (100). 침식점 부재 조건 `if sum(ero)==0` (101)이면 break(102). |
| 105–124 | 시작 시 80행 step 루프 안. 모래 사구 공급 상한 `qdmax=5.0*DH/dtnum;` (108). xtill 조건 `if ~isempty(xtill)` (109)의 상한 `qdmax=xtill.*DH/dtnum;` (110). 침식률·상한 적용 `qd(ero)=spyr * 4.*cs(ero).*(wldf(ero)).* min(wldf(ero),DH(ero))./ TPc(ero);` (115); `qd(ero)=min(qd(ero),qdmax(ero));  % To limit erosion/overwash per dtnum` (116), qds=qd 복사(117). 점착성 빙력토(cohesive till) 비율·침식률·총량 및 모래 성분 `tillfrac=max(1-qdmax(ero)./qd(ero),0); % fraction of erosion that is not anymore available as sand in the dune, but should come from the cohesive till layer behind the sand` (120); `qd2=spyr * tillfrac.*4.*cstill(ero).*(wldf(ero)).* min(wldf(ero),DH(ero))./ TPc(ero);` (121); `qd(ero)=qd(ero)+qd2;` (122); `qds(ero)=qd(ero)+min(1,max(1-perctill(ero)/100,0)).*qd2;` (123). 107행 주석은 till 미정의 시 무제한 폭 1e6을 적는다. |
| 125–147 | 시작 시 80행 step 루프 안. 월파(overwash) 성분 분리 `alfa(ero)=max(((wldf(ero))./DH(ero)-1),0)/A;` (126); `qs(ero)=qd(ero)./(1+alfa(ero));` (127); `qss(ero)=qds(ero)./(1+alfa(ero));` (128); `ql(ero)=qd(ero).*alfa(ero)./(1+alfa(ero));` (129). 침식이 없는 점의 qs·qd·qds·qss·ql=0(130–134). 해안선 이동·사구 전면 이동·버름 폭 하한 0.1 `dn=qds./h0*dtnum;` (139); `dndune=(qs+ql)./DH*dtnum;` (140); `wberm=max(wberm+dn+dndune,0.1);` (141). 평균용 누적 `qs_avg=qs_avg+qs;` (144); `qss_avg=qss_avg+qss;` (145); `ql_avg=ql_avg+ql;` (146). 반복 종료(147). 추가 원문: `qs(~ero)=0;` (130). `qd(~ero)=0;` (131). `qds(~ero)=0;` (132). `qss(~ero)=0;` (133). `ql(~ero)=0;` (134). [10-12 전수 검증 보완] |
| 148–152 | 반복 밖. nt로 평균 계산 `qs_avg=qs_avg/nt;` (148); `qss_avg=qss_avg/nt;` (149); `ql_avg=ql_avg/nt;` (150). 함수 종료·빈 줄(151–152). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1–2: 실행 시그니처에는 dfelev0가 있다. 바로 아래 시그니처 주석에는 dfelev0가 없다.
- 67·101–102·148–150: nt는 dt/dtnum에서 정한다. 침식점이 없으면 반복을 조기 종료하지만 평균 분모는 nt를 유지한다.
- 107–110: 주석은 till 미정의 시 폭 1e6을 적는다. 실행 기본 상한은 5.0*DH/dtnum이다.
- 115–123: qd를 qdmax로 제한한 다음 tillfrac를 계산한다. qd2를 qd에 더한 뒤 qds 식은 갱신된 qd와 모래 비율을 곱한 qd2를 함께 사용한다.
