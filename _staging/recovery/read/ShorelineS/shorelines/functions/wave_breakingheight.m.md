---
file: models/ShorelineS/raw/source_code/shorelines/functions/wave_breakingheight.m
lines: 130
sha256: 406a8cf0c319d280c49bd185bd6ea15fe43ddb251ab89e518e5337e558c51dae
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# wave_breakingheight.m — 판독 구간 기록

구간은 1행부터 130행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–54 | 함수 시그니처(1), 근해점에서 쇄파점까지 굴절(refraction)·천수(shoaling) 계산 목적(4), WAVE·TRANSP 입력과 6개 WAVE 출력 설명(6–25), 저작권·LGPL·무보증·빈 줄(27–54). 입력 필드 기본값 대입은 이 구간에 없다. 원문: `function [WAVE]=wave_breakingheight(WAVE,TRANSP)` (1). |
| 55–79 | 시작 시 1행 함수 안. eps=1d-5·hmin=0.1·hbrmin=0.05와 5개 WAVE 출력 배열의 0 초기화가 있다(55–62). suppresshighangle=1이면 dPHIcrit_mc0 필드 존재 여부를 검사한다(65–66). get_one_polygon 결과의 유효 길이가 파향 길이와 같으면 점별 임계각, 1 이상이면 중앙값, else 또는 필드 없음이면 45도로 부호 유지 제한한다(67–77). 원문: `eps=1d-5;` (55), `hmin=0.1;` (56), `hbrmin=0.05; % minimum depthg of breaking` (57), `WAVE.HSbr=zeros(size(WAVE.dPHItdp));` (58), `WAVE.dPHIbr=zeros(size(WAVE.dPHItdp));` (59), `WAVE.hbr=zeros(size(WAVE.dPHItdp));` (60), `WAVE.cbr=zeros(size(WAVE.dPHItdp));` (61), `WAVE.nbr=zeros(size(WAVE.dPHItdp));` (62), `if TRANSP.suppresshighangle==1` (65), `if isfield(WAVE,'dPHIcrit_mc0')` (66), `dPHIcrit = get_one_polygon( WAVE.dPHIcrit_mc0,WAVE.i_mc);` (67), `if length(dPHIcrit(~isnan(dPHIcrit)))==length(WAVE.dPHItdp)` (68), `WAVE.dPHItdp=sign(WAVE.dPHItdp).*min([abs(WAVE.dPHItdp);dPHIcrit],[],1);` (69), `elseif length(dPHIcrit(~isnan(dPHIcrit)))>=1` (70), `WAVE.dPHItdp=sign(WAVE.dPHItdp).*min(abs(WAVE.dPHItdp),median(dPHIcrit));` (71), `else` (72), `WAVE.dPHItdp=sign(WAVE.dPHItdp).*min(abs(WAVE.dPHItdp),45);` (73), `else` (75), `WAVE.dPHItdp=sign(WAVE.dPHItdp).*min(abs(WAVE.dPHItdp),45);` (76). |
| 80–108 | 시작 시 1행 함수 안. RAY·CERC·CERC2가 아닐 때 파랑 조건·수송점 두 루프를 돈다(80–82). get_disper로 근해 파속(celerity)과 n을 구하고 cosPHI·hbr1에 eps 하한을 적용한다(83–87). wave_shoalref를 두 번 호출해 err1·err2를 얻는다(88–91). abs(err2)<eps이면 두 번째 결과를 채택한다(93–95). else의 3:10 반복은 이전 두 수심·오차로 보간/외삽(interpolation/extrapolation)한 hbrnew를 만들고 wave_shoalref를 다시 호출한다(97–99). abs(errnew)>eps이면 두 수심·오차 쌍을 갱신한다(100–102). 그 밖에는 break한다(103–105). 원문: `if ~strcmpi(TRANSP.trform,'RAY') && ~strcmpi(TRANSP.trform,'CERC') && ~strcmpi(TRANSP.trform,'CERC2')` (80), `for i=1:size(WAVE.HStdp,1)` (81), `for j=1:size(WAVE.HStdp,2)` (82), `[~,ctdp,~,ntdp]=get_disper(WAVE.dnearshore,WAVE.TP(i,j));` (83), `cosPHI=max(cosd(WAVE.dPHItdp(i,j)),eps);` (84), `sinPHI=sind(WAVE.dPHItdp(i,j));` (85), `iter=1; % First estimate: Hbr=WAVE.HStdp` (86), `hbr1=max(WAVE.HStdp(i,j)./WAVE.gamma,eps);` (87), `[hbr2,dPHIbr0,err1,cbr0,nbr0]=wave_shoalref(hbr1,WAVE.TP(i,j),WAVE.gamma,WAVE.HStdp(i,j),ctdp,ntdp,sinPHI,cosPHI);` (88), `hbr2b=max(hbr2,eps);` (89), `iter=2; % Second estimate: fill in hbr2` (90), `[hbr3,dPHIbr0,err2,cbr0,nbr0]=wave_shoalref(hbr2b,WAVE.TP(i,j),WAVE.gamma,WAVE.HStdp(i,j),ctdp,ntdp,sinPHI,cosPHI);` (91), `if abs(err2)<eps` (93), `hbrnew=hbr3;` (94), `errnew=err2;` (95), `else` (96), `for iter=3:10 % Following estimates: inter/extrapolate from last two WAVE.hbr/err pairs` (97), `hbrnew=max(hbr1-err1*(hbr2-hbr1)/(err2-err1),eps);` (98), `[hbrest,dPHIbr0,errnew,cbr0,nbr0]=wave_shoalref(hbrnew,WAVE.TP(i,j),WAVE.gamma,WAVE.HStdp(i,j),ctdp,ntdp,sinPHI,cosPHI);` (99), `if abs(errnew)>eps` (100), `hbr1=hbr2;err1=err2;` (101), `hbr2=hbrnew;err2=errnew;` (102), `else` (103), `break` (104). [10-12 전수 검증 정정] |
| 109–130 | 시작 시 1행 함수·80행 수송식 조건 참 분기·81·82행 i/j 루프 안. NaN 수심을 0으로 바꾸고 파고·각도·수심·파속·n을 WAVE에 저장한다(110–116). 루프를 끝낸 뒤 80행 else의 RAY/CERC/CERC2는 근해 파고·각도를 복사하고 최소 수심을 0.1*hbrmin으로 제한하며 get_disper를 호출한다(120–127). 조건·함수가 끝난다(128–130). 원문: `hbrnew(isnan(hbrnew))=0;` (110), `WAVE.HSbr(i,j)=hbrnew*WAVE.gamma;` (111), `WAVE.dPHIbr(i,j)=dPHIbr0;` (112), `WAVE.dPHIbr(isnan(WAVE.dPHIbr))=0;` (113), `WAVE.hbr(i,j)=hbrnew;` (114), `WAVE.cbr(i,j)=cbr0;` (115), `WAVE.nbr(i,j)=nbr0;` (116), `else` (120), `WAVE.HSbr=WAVE.HStdp;` (122), `WAVE.dPHIbr=WAVE.dPHItdp;` (123), `WAVE.hbr=max(WAVE.HStdp./WAVE.gamma,0.1*hbrmin);` (124), `[~,cbr,~,nbr]=get_disper(WAVE.hbr,WAVE.TP);` (125), `WAVE.cbr=cbr;` (126), `WAVE.nbr=nbr;` (127). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 56: hmin=0.1은 대입 이후 이 파일에서 참조되지 않는다.
- 98: 수심 보간 식은 err2−err1을 분모로 쓴다. 해당 차이가 0인지 검사하는 조건은 이 블록에 없다.
- 99: hbrest는 wave_shoalref 출력으로 받은 뒤 이 파일에서 참조되지 않는다.
- 111–116: 최종 hbrnew로 HSbr·hbr를 저장한다. dPHIbr0·cbr0·nbr0는 마지막 wave_shoalref 호출의 출력이며 최종 저장 앞에 별도 재계산 호출은 없다.
- 97–106: 반복 범위는 3:10이다. 반복을 모두 소진한 경우 별도 경고 분기는 없다.
