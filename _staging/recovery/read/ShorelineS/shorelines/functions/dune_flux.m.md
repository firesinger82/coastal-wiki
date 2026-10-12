---
file: models/ShorelineS/raw/source_code/shorelines/functions/dune_flux.m
lines: 203
sha256: cd7e9d133ee5a63a0f5fc751773c38d6383dcd46719514a4c922449d4c16b0e7
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# dune_flux.m — 판독 구간 기록

구간은 1행부터 203행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–84 | 함수 시그니처 `function [DUNE,COAST]=dune_flux(COAST,DUNE,WIND,RUNUP,TRANSP,TIME,CC)` (1). 사구(dune) 침식·성장 목적과 COAST·WIND·RUNUP·DUNE·TRANSP·TIME 필드·단위, 출력 설명(4–56). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(57–84). |
| 85–122 | 사구 사용 조건 `if DUNE.used` (86). dt=TIME.dt(87). 사구 시간 간격 조건 `if ~isempty(DUNE.dt)` (88)이면 DUNE.dt 복사(89), `else` (90)이면 TIME.dt 복사(91). 하위 간격 `dtnum    = min(dtdune,1/365/48);` (93). 해안 방향·활성 높이·점 수·바람·수위·파고·주기 복사(94–102). 상대 파향 `dPHI     = repmat(COAST.PHIcxy,[size(RUNUP.Dir,1),1])-RUNUP.Dir;` (103). 퇴적물·침식·바람·공극률·경사·처오름(runup) 계수를 입력 필드에서 복사한다(104–121). 추가 원문: `n        = length(phic);` (96). `cs       = COAST.cs(:)';` (106). `cstill   = COAST.cstill(:)';` (107). [10-12 전수 검증 보완] |
| 123–143 | 시작 시 86행 DUNE.used 참 분기 안. 버름(berm) 폭·원래 사구 기부 높이·정상 높이 복사(124–126). 바람의 스칼라 확장식은 주석 처리(129–130). qs·qss·qw·ql·R·SWL을 COAST.x 열 수의 0 배열로 초기화(133–138). 조건 자료의 최대 행 수 `dtfractions=max([size(HS,1),size(TP,1),size(dPHI,1),size(SWL,1),size(uwind,1),size(phiwnd,1)]);` (142). |
| 144–175 | 시작 시 86행 DUNE.used 참 분기 안. 하위 조건 루프 `for tt=1:dtfractions` (145). 각 자료는 min(tt,자료 행 수) 행 선택(146–151). 하위 시간 간격 `dtdune=dt/dtfractions;` (154). 원래 경사·최대 경사에 맞춘 기부 높이·경사 `slope0=dfelev0./wberm;` (158); `dfelev=dfelev0.*min(maxslope./slope0,1);` (159); `slope=dfelev./wberm;` (160). 162행 주석은 파랑 위치를 외해로 적으면서 동적 단면 하단인지 의문을 표시한다. 파고·파장·제곱근 `HSo1 = HSi.*sqrt(max(cosd(dPHIi),eps));` (163); `L0 = g/(2*pi)*TPi.^2;` (164); `sqrHsL0=sqrt(HSo1.*L0);` (165). 평활화는 주석 처리(168–170). 침식 호출 `[~,qs,qss,ql,R]=dune_erosion(runupform,runupfactor,wberm,dfelev0,dfelev,dcelev,h0,sqrHsL0,SWLi,TPi,cs,cstill,xtill,perctill,A,dtdune,dtnum);` (171), 바람 수송 성장 호출 `[qw,uc,us,mwe,qwe,Bdry,FL]=dune_growth(uwindi,duneaw,rhos,rhoa,por,g,d50,d50r,z,k,kw,R,SWLi,dfelev,wberm,phic,phiwndi,segmaw);` (174). 자료 선택·계산·호출의 원문은 `HSi=HS(min(tt,size(HS,1)),:);` (146); `TPi=TP(min(tt,size(TP,1)),:);` (147); `dPHIi=dPHI(min(tt,size(dPHI,1)),:);` (148); `SWLi=SWL(min(tt,size(SWL,1)),:);` (149); `uwindi=uwind(min(tt,size(uwind,1)),:);` (150); `phiwndi=phiwnd(min(tt,size(phiwnd,1)),:);` (151). [10-12 전수 검증 정정] |
| 176–193 | 시작 시 86행 DUNE.used 참 분기·145행 tt 루프 안. 균등 확률 `Prob=1/dtfractions; % in case of eqaul likelihood (e.g. time-series)` (177). WIND 확률 필드 조건 `if isfield(WIND,'Prob') && isfield(WIND,'iwc')` (178), 가중 확률 `Prob=WIND.Prob(WIND.iwc(tt))/sum(WIND.Prob(WIND.iwc)); % in case of varying probability (e.g. wave climate)` (179). 차폐(shadowing) 자료 행 선택 `tt2=min(tt,size(TRANSP.shadow,1));` (183). 해안·구조물·호안(revetment) 차폐점의 qs·qss·ql을 0으로 설정(184–192). 추가 원문: `qs(TRANSP.shadow(tt2,:))      = 0;      % Set dune transport to zero due to dune-dune shadowing` (184). `qs(TRANSP.shadow_h(tt2,:))    = 0;      % Set dune transport to zero due to being sheltered behind structures` (185). `qs(TRANSP.shadowS_hD(tt2,:))  = 0;      % Set dune transport to zero due to being sheltered behind revetment` (186). `qss(TRANSP.shadow(tt2,:))     = 0;      % Set dune transport to zero due to dune-dune shadowing` (187). `qss(TRANSP.shadow_h(tt2,:))   = 0;      % Set dune transport to zero due to being sheltered behind structures` (188). `qss(TRANSP.shadowS_hD(tt2,:)) = 0;      % Set dune transport to zero due to being sheltered behind revetment` (189). `ql(TRANSP.shadow(tt2,:))      = 0;      % Set dune transport to zero due to dune-dune shadowing` (190). `ql(TRANSP.shadow_h(tt2,:))    = 0;      % Set dune transport to zero due to being sheltered behind structures` (191). `ql(TRANSP.shadowS_hD(tt2,:))  = 0;      % Set dune transport to zero due to being sheltered behind revetment` (192). [10-12 전수 검증 보완] |
| 194–203 | 시작 시 86행 DUNE.used 참 분기·145행 tt 루프 안. 수송률의 확률 평균 누적 `COAST.qw=COAST.qw+qw*Prob;         % compute average qw, i.e. component due to wind transport` (195); `COAST.qs=COAST.qs+qs*Prob;         % compute average qs, i.e. dune erosion that is beneficial for the beach` (196); `COAST.qss=COAST.qss+qss*Prob;      % compute average qss, i.e. dune erosion that is beneficial for the beach (i.e. the sandy part, discarding the till part)` (197); `COAST.ql=COAST.ql+ql*Prob;         % compute average ql, i.e. dune erosion that is not beneficial for the beach` (198). 처오름과 수위는 최댓값 갱신 `COAST.R=max(COAST.R,R);            % use maximum instead of average for the runup` (199); `COAST.SWL=max(COAST.SWL,SWLi);     % use maximum instead of average for the still water level` (200). 루프·조건·함수 종료(201–203). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·64–203: CC는 함수 인수에 있으나 실행 계산에서 참조하지 않는다.
- 88–93·154: DUNE.dt가 비어 있지 않으면 dtdune에 DUNE.dt를 대입한다. 비어 있으면 dtdune에 TIME.dt를 대입한다. dtnum은 dtdune과 1/365/48 중 작은 값이다. tt 루프 안에서는 dtdune을 TIME.dt/dtfractions로 다시 대입한다. [10-12 전수 검증 보완]
- 160: slope는 계산 뒤 이 파일의 호출 인수나 실행 계산에서 사용되지 않는다.
- 171: dune_erosion의 첫 출력 wberm은 ~로 버린다.
- 174: uc·us·mwe·qwe·Bdry·FL은 호출 출력으로 받지만 이후 실행 계산에서 사용되지 않는다.
- 137–138·199–200: R과 SWL 누적 배열은 0으로 초기화되며 각 조건 값과 max를 취한다.
