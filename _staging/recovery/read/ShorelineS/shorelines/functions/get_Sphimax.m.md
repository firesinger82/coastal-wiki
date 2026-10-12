---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_Sphimax.m
lines: 162
sha256: 98333d205b0ba1c046c1c6cf6af1cf44f68dbfe4eb68a1f64daa53a375b7b555
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_Sphimax.m — 판독 구간 기록

구간은 1행부터 162행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–51 | 함수 시그니처 `function [WAVE,TRANSP]=get_Sphimax(WAVE,TIDE,TRANSP,STRUC)` (1). 고각 입사(high-angle wave incidence)에서 최대 수송과 폐쇄 수심(depth of closure)·쇄파점(breaking point) 임계각을 구한다는 주석·입출력(4–22). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(23–51). |
| 52–87 | 포물선(parabola) 근사 주석(52). 허용치 `eps=1d-4;` (53), 임계각·QSmax 비우기(54–55), 파랑 조건·격자 수(56–57), QSmax 0 배열·임계각 NaN 배열(58·61–62), 초기 각도 `waveangle1=35;` (59); `waveangle2=45;` (60). 첫 계산은 WAVE 복사(65), 방향 확장·파고 하한 `WAVE1.dPHItdp=repmat(waveangle1,[nw,nq]);` (66); `WAVE1.HStdp=max(WAVE1.HStdp,eps);` (67), wave_breakingheight 호출(68), 파고 상한 `WAVE1.HStdp=min(WAVE1.HStdp,WAVE1.ddeep*0.5);` (69), transport의 QSmax 호출(70), 방향·수송값 복사(71–72). 둘째 계산 `WAVE2.dPHItdp=repmat(waveangle2,[nw,nq]);` (76); `WAVE2.HStdp=max(WAVE2.HStdp,eps);` (77); `WAVE2.HStdp=min(WAVE2.HStdp,WAVE2.ddeep*0.5);` (79)과 같은 호출(78·80), 결과 복사(81–82). WAVEm 복사(85), 중간 각도 `dPHIm=.5*(dPHI1+dPHI2);       % at depth-of-closure` (86). 추가 원문: `nw=size(WAVE.HStdp,1); % nr of wave conditions` (56). `nq=size(WAVE.HStdp,2); % nr of grid cells of the coast` (57). [10-12 전수 검증 보완] |
| 88–115 | 초기 오차 `err=repmat(1d3,[nw,nq]);` (89), iter=0(90). 반복 조건 `while ( min(err(:))>eps \|\| iter<=2 ) && iter<10 %err0>err` (91), 반복 번호 `iter=iter+1;` (92), WAVEm 방향 복사(95), wave_breakingheight·transport 호출(96–97), QSm 복사(98), 이전 방향 복사(101), 갱신 마스크 `in=(err>eps);` (102), find(103), 점 루프 `for i=1:length(ivals)` (104). 행·열 인덱스 복사(105–106). 포물선 계수 행렬·우변 `A=[dPHI1(i1,j1)^2,dPHI1(i1,j1),1;dPHI2(i1,j1)^2,dPHI2(i1,j1),1;dPHIm(i1,j1)^2,dPHIm(i1,j1),1];              % at depth-of-closure` (108); `B=[QS1(i1,j1);QS2(i1,j1);QSm(i1,j1)];` (109), warning off/on(110·112) 사이의 계수 풀이 `a=A\B;` (111), 꼭짓점 각도 `dPHIm(i1,j1)=-a(2)/(2*a(1));     % at depth-of-closure` (113). 추가 원문: `[ivals,jvals]=find(in);` (103). [10-12 전수 검증 보완] |
| 116–136 | 시작 시 91행 while 루프 안. 각도 표본 교체식은 `dPHI2(QS1>QS2)=dPHImold(QS1>QS2);` (117). 다른 각도 표본 교체식은 `dPHI1(QS1<=QS2)=dPHImold(QS1<=QS2);` (118). QS2 교체식은 `QS2(QS1>QS2)=QSm(QS1>QS2);` (119). 그 뒤 QS1 교체식은 `QS1(QS1<=QS2)=QSm(QS1<=QS2);` (120). 각도 상한 `dPHIm(dPHIm>179.99)=179.99;` (123), 오차 `err=abs(dPHIm-dPHImold);` (126), 999인 각도를 NaN으로 설정(127). 오차 10 제한식은 주석 처리(128–129). 임계각·쇄파 임계각·QSmax에 현재 자료 복사(132–134). 반복 종료(135). 추가 원문: `dPHIm(dPHIm==999)=nan;` (127). [10-12 전수 검증 보완] |
| 137–162 | 파랑 조건 루프 `for i=1:nw` (138), interpNANs로 두 임계각과 수송의 NaN 보간 `WAVE.dPHIcrit(i,:)=interpNANs(WAVE.dPHIcrit(i,:));` (139); `WAVE.dPHIcritbr(i,:)=interpNANs(WAVE.dPHIcritbr(i,:));` (140); `TRANSP.QSmax(i,:)=interpNANs(QSmax(i,:));` (141). 남은 NaN의 기본값 `WAVE.dPHIcrit(isnan(WAVE.dPHIcrit))=45;` (145); `WAVE.dPHIcritbr(isnan(WAVE.dPHIcritbr))=45;` (146); `TRANSP.QSmax(isnan(TRANSP.QSmax))=0;` (147): 두 각도 45·수송 0. 복수 파랑 조건의 확률·파고 가중 재결합은 전체 주석 처리(149–161). 함수 종료(162). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 53·89: 숫자 리터럴을 eps=1d-4와 repmat(1d3,[nw,nq])로 적는다.
- 91: 반복 종료 검사는 err 전체의 min을 사용하며 최대 오차가 아니다. iter<=2와 iter<10도 같은 조건에 있다.
- 117–120: QS2를 갱신한 다음 QS1<=QS2 마스크를 다시 평가하여 QS1을 갱신한다.
- 123·127: 방향 상한은 179.99이며 999 표식의 NaN 치환은 이 상한 적용 뒤에 나온다.
- 95–98·113·132–134: 쇄파 임계각과 수송은 현재 WAVEm 계산에서 얻는다. dPHIcrit에는 그 계산 뒤 포물선으로 다시 구한 dPHIm을 저장한다.
- 110–112: 계수 풀이 주위에서 warning off/on을 호출하며 이전 설정을 저장하는 문장은 없다.
