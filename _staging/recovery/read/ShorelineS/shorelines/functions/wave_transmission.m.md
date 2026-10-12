---
file: models/ShorelineS/raw/source_code/shorelines/functions/wave_transmission.m
lines: 100
sha256: c6021d1ac805363f8616dfa3ce9bcc8e435178b5fe85f646bb11ca4a614f7390
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# wave_transmission.m — 판독 구간 기록

구간은 1행부터 100행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–54 | 함수 시그니처(1), 파랑 전달(wave transmission) 목적(4), 구조물·수송점·해안 좌표, 수위·파고·주기와 구조물 높이·폭·경사·형식·입경 입력 설명(6–22), Kt_total 0–1 출력 설명(24–25), 저작권·LGPL·무보증·빈 줄(27–54). 구조체 입력과 인수 기본값 설정은 없다. 원문: `function [Kt_total]=wave_transmission(xhard,yhard,xq,yq,x,y,SWL,Hs,Tp,transmbwdepth,transmcrestheight,transmcrestwidth,transmslope,transmform,transmd50)` (1). |
| 55–74 | 시작 시 1행 함수 안. get_one_polygon으로 첫 구조물을 얻고 Kt·Kt_total을 0으로 초기화한다(56–58). Hs·Tp·SWL 행 수 최대값을 dtfractions로 정한다(62). 부분 시간조건 루프에서 SWL 행을 제한하여 취하고 weighted_distance 방법으로 get_interpolation_on_grid를 호출한다(65–71). 첫 구조물 두 점의 중점과 가장 가까운 수송점에서 SWLstruc를 선택한다(72–73). 원문: `[ x_struc,y_struc,nhard,~,~ ] = get_one_polygon(xhard,yhard,1);` (56), `Kt = zeros(length(Hs),length(nhard));` (57), `Kt_total = zeros(length(Hs),length(nhard));` (58), `dtfractions=max([size(Hs,1),size(Tp,1),size(SWL,1)]);` (62), `for tt=1:dtfractions` (65), `SWLi=SWL(min(tt,size(SWL,1)),:);` (68), `method='weighted_distance';` (70), `[SWLi2]=get_interpolation_on_grid(method,xq,yq,x,y,SWLi,[]);` (71), `[~,closest]=min(hypot((x_struc(1)+x_struc(2))/2-xq,(y_struc(1)+y_struc(2))/2-yq));` (72), `SWLstruc = SWLi2(closest);` (73). |
| 75–83 | 시작 시 1행 함수·65행 tt 루프 안. 구조물 수심에서 get_disper로 k를 얻고 Lwave·van Gent용 심해 파장(deep-water wavelength)을 계산한다(76–79). 구조물 여유고(freeboard) Rc는 crestheight−SWLstruc이고 CHIop는 구조물 경사를 파형 경사 Hs./Lwave의 제곱근으로 나눈 값이다(81). 원문: `h=transmbwdepth;` (76), `k=get_disper(h,Tp);` (77), `Lwave=2*pi./k;` (78), `Lwave_vGent=(9.81.*(Tp/1.2).^2)/(2*pi);` (79), `Rc=transmcrestheight-SWLstruc;  % Rc is positive when the crest is higher than the water level, meaning lower Kt for higher Rc. Typically it would be between -2m below water and +1m above water level` (80), `CHIop=transmslope./((Hs./Lwave).^0.5);` (81). [10-12 전수 검증 정정] |
| 84–100 | 시작 시 1행 함수·65행 tt 루프 안. transmform 부분문자열 angr·gent·seabrhall에 따라 d’Angremond·van Gent·Seabrook & Hall 전달식을 선택한다(84–95). Gent 계수는 c1=0.43·c2=3.1·c3=0.75·c4=−0.25·c5=0.5이다(87–91). Kt를 0–1로 제한하고 tt까지의 산술평균을 Kt_total로 갱신한다(96–98). 루프·함수가 끝난다(99–100). 원문: `if ~isempty(findstr(lower(transmform),'angr'))   % d'Angremond et al. (1996) formulation, rough / permeable structure` (84), `Kt=real(-0.4.*Rc/Hs+0.64.*((transmcrestwidth/Hs).^-0.31).*(1 - exp(-0.5.*CHIop)));` (85), `elseif ~isempty(findstr(lower(transmform),'gent')) % van Gent et al. (2023) formulation, rough / permeable structure` (86), `c1=0.43;` (87), `c2=3.1;` (88), `c3=0.75;` (89), `c4=-0.25;` (90), `c5=0.5;` (91), `Kt=c1*tanh(-(Rc/Hs+c2*((transmcrestwidth/Lwave_vGent)^c3)+c4))+c5;` (92), `elseif ~isempty(findstr(lower(transmform),'seabrhall')) % Seabrook & Hall (1998) formulation, rough / permeable structure` (93), `Kt=1-exp(-0.65*(-1*Rc/Hs)-1.09*(Hs/transmcrestwidth))+0.047*((transmcrestwidth*-1*Rc)/(Lwave*transmd50))-0.067*(-1*Rc*Hs)/(transmcrestwidth*transmd50);` (94), `Kt=min(Kt,1);   % Limitations are that Kt=0.8 and Kt=0.075 in d'Angremond et al. formula.` (96), `Kt=max(Kt,0);` (97), `Kt_total=(Kt_total*(tt-1)+Kt)/tt;   % compute average Kt over various waterlevels` (98). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15·1: 입력 설명에는 Dir가 있으나 함수 인수에는 Dir가 없다.
- 56–58: 첫 구조물만 get_one_polygon으로 추출한다. 배열 열 크기는 nhard 자체가 아니라 length(nhard)를 사용한다.
- 68·77·79·81·85·92·94: 부분 시간조건 인덱스 tt는 SWL 선택에 적용한다. 파장·전달 계산은 Hs·Tp 전체 인수를 사용한다.
- 84–95: 전달식 선택문에는 세 elseif/if 분기만 있고 else가 없다.
- 96–97: 주석은 d’Angremond 제한값 0.8·0.075를 언급한다. 실행 제한값은 상한 1·하한 0이다.
