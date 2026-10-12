---
file: models/ShorelineS/raw/source_code/shorelines/functions/introduce_wind.m
lines: 171
sha256: e6630b71faa26b790225ba620af72c24af3837c2b3d38b2f2191a1f19a850d2d
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# introduce_wind.m — 판독 구간 기록

구간은 1행부터 171행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–39 | 함수 시그니처(1). 사구 또는 진흙 해안(mud coast)에서 바람을 해안 위치·사구 시간 단계에 보간한다는 설명(4–11). 입력 주석은 위치·자료·시간 정보와 파랑 기후 인덱스를 열거한다(13–33). 출력 uz는 m/s, phiwnd는 방향이며 사구 단계 수와 해안 격자 수의 M×N 배열로 설명한다(35–38). 원문: `function [WIND]=introduce_wind(WIND,TIME,WAVE,COAST)` (1). |
| 40–67 | 시작 시 1행 introduce_wind 함수 안. 2020년 저작권·연락처, LGPL 2.1 이상·무보증 안내와 빈 줄(40–67). |
| 68–94 | 시작 시 1행 introduce_wind 함수 안. WIND.WND·WAVE.WVC를 가져오고 위치 배열을 비운다(68–71). dune 또는 mud가 참이면 처리한다(72). WND가 비면 정적 경로로 nloc=0을 설정한다(73–75). 첫 자료의 timenum이 비어 있지 않으면 시간 보간 경로로 출력 배열을 비우고 모든 위치를 순회한다(76–81). eps는 1e-6이며 dtrewind(1)을 적용한 구간의 표본을 찾는다(82–86). WIND.dt가 있고 초기 단계가 아니면 min(WIND.dt*365,tnow-tprev) 간격의 시각 배열을 만든다(90–93). 원문: `WND=WIND.WND;` (68), `WVC=WAVE.WVC;` (69), `xw=[];` (70), `yw=[];` (71), `if WIND.dune \|\| WIND.mud` (72), `if isempty(WND)` (73), `WIND.nloc=0;` (75), `elseif ~isempty(WND(1).timenum)` (76), `WIND.uz=[];` (78), `WIND.phiwnd=[];` (79), `WIND.nloc=length(WND);` (80), `for kk=1:WIND.nloc` (81), `eps=1e-6;` (82), `tnow=TIME.tnow+WAVE.dtrewind(1);` (84), `tprev=TIME.tprev+WAVE.dtrewind(1);` (85), `idt=find(WND(kk).timenum>tprev & WND(kk).timenum<=tnow);` (86), `timenow=tnow;` (89), `if ~isempty(WIND.dt) && TIME.it~=0` (90), `dt=min(WIND.dt*365,tnow-tprev);` (91), `timenow=[tprev+dt:dt:tnow]';` (92). |
| 95–114 | 시작 시 1행 introduce_wind 함수·72행 dune/mud 분기·76행 시계열 분기·81행 kk 루프 안. 표본이 둘 이상이고 양 끝 시각과의 최소 차이가 각각 eps 미만이며 WIND.dt가 비었을 때 uz·Dir 표본을 직접 사용한다(96–99). 시각이 둘 이상이거나 초기 단계이면 uz를 interp1로 보간하고 방향은 sine·cosine 보간 뒤 atan2d와 mod 360으로 복원한다(100–103). 그 외에는 단일 값을 사용한다(104–108). x 필드가 있으면 위치를 저장한다(109–112). kk 루프 종료(113). 원문: `if length(idt)>1 && min(abs(WND(kk).timenum-tnow))<eps && min(abs(WND(kk).timenum-tprev))<eps && isempty(WIND.dt)` (96), `WIND.uz(:,kk) = WND(kk).uz(idt);` (98), `WIND.phiwnd(:,kk) = WND(kk).Dir(idt);` (99), `elseif length(WND(kk).timenum)>1 \|\| TIME.it==0` (100), `WIND.uz(:,kk) = interp1(WND(kk).timenum,WND(kk).uz,timenow);` (102), `WIND.phiwnd(:,kk) = mod(atan2d(interp1(WND(kk).timenum,sind(WND(kk).Dir),timenow),interp1(WND(kk).timenum,cosd(WND(kk).Dir),timenow)),360);` (103), `else` (104), `WIND.uz(1,kk) = WND(kk).uz;` (106), `WIND.phiwnd(1,kk) = WND(kk).Dir;` (107), `if isfield(WND,'x')` (109), `xw(1,kk)=WND(kk).x;` (110), `yw(1,kk)=WND(kk).y;` (111). [10-12 전수 검증 정정] |
| 115–136 | 시작 시 1행 introduce_wind 함수·72행 dune/mud 분기·73행 정적/시계열/기후 분기 안. 115행 elseif는 WND에 uz 필드가 있는 기후 경로이다. WVC.Hs와 WND.uz 길이가 같고 WAVE.iwc가 있으면 파랑 선택과 확률을 사용한다(117–120). 그렇지 않으면 첫 해안 구간·dtsteps==0에서 mergeconditions, get_randsample 확률 추출, 균등 임의 추출을 선택한다(121–135). 확률을 정규화하거나 균등값으로 설정한다(125·129·134). 원문: `elseif isfield(WND,'uz')` (115), `if length(WVC(1).Hs)==length(WND(1).uz) && ~isempty(WAVE.iwc)` (117), `WIND.iwc=WAVE.iwc(:);` (119), `WIND.Prob=WAVE.Prob;` (120), `elseif COAST.i_mc==1 && TIME.dtsteps==0` (121), `if WIND.mergeconditions==1` (122), `WIND.iwc=[1:length(WVD(1).Hs)]';` (124), `WIND.Prob=WND(1).Prob(:)./sum(WND(1).Prob);` (125), `elseif COAST.i_mc==1 && isfield(WND,'Prob')` (126), `WIND.iwc=get_randsample(length(WND(1).uz),1,WND(1).Prob);` (128), `WIND.Prob=WND(1).Prob(:)./sum(WND(1).Prob);` (129), `else` (130), `WIND.rnd=rand;` (132), `WIND.iwc=round((WIND.rnd*length(WND(1).uz)+0.5));` (133), `WIND.Prob=ones(length(WND(1).uz),1)/length(WND(1).uz);` (134). |
| 137–151 | 시작 시 1행 introduce_wind 함수·72행 dune/mud 분기·115행 기후 elseif 안. 바람 출력 배열을 비우고 nloc를 설정한다(138–140). 각 위치 루프에서 선택한 uz·Dir을 꺼내 행 배열로 바꾼다(141–145). x 필드가 있으면 위치를 저장한다(146–149). 루프·자료 유형 분기 종료(150–151). 원문: `WIND.uz=[];` (138), `WIND.phiwnd=[];` (139), `WIND.nloc=length(WND);` (140), `for kk=1:WIND.nloc` (141), `WIND.uz=WND(kk).uz(WIND.iwc);` (142), `WIND.phiwnd=WND(kk).Dir(WIND.iwc);` (143), `WIND.uz=WIND.uz(:)';` (144), `WIND.phiwnd=WIND.phiwnd(:)';` (145), `if isfield(WND,'x')` (146), `xw(1,kk)=WND(kk).x;` (147), `yw(1,kk)=WND(kk).y;` (148). |
| 152–171 | 시작 시 1행 introduce_wind 함수·72행 dune/mud 분기 안. 위치가 0이면 정적 값을 해안 전체에 곱한다(152–155). 1이면 열로 만든 시간 배열을 해안 전체에 반복한다(156–159). 여러 위치이면 weighted_distance로 get_interpolation_on_grid를 호출한다(160–166). 168행 else는 dune·mud 모두 사용하지 않는 경우이며 phiwnd만 비운다(169). 함수 종료(171). 원문: `if WIND.nloc==0` (152), `WIND.uz=WIND.uz(1)*ones(size(COAST.x));` (154), `WIND.phiwnd=WIND.phiwnd(1)*ones(size(COAST.x));` (155), `elseif WIND.nloc==1` (156), `WIND.uz=repmat(WIND.uz(:),[1,length(COAST.x)]);` (158), `WIND.phiwnd=repmat(WIND.phiwnd(:),[1,length(COAST.x)]);` (159), `else` (160), `xc=COAST.x;` (162), `yc=COAST.y;` (163), `method='weighted_distance';` (164), `[WIND.uz,WIND.phiwnd]=get_interpolation_on_grid(method,xc,yc,xw,yw,WIND.uz,WIND.phiwnd);` (166), `else` (168), `WIND.phiwnd=[];` (169). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 21·68: 입력 주석은 바람 자료 구조체를 SWL이라고 적는다. 실행 코드는 WIND.WND를 가져온다.
- 124: mergeconditions 분기는 WVD(1).Hs를 참조한다. 이 함수의 인수·앞선 대입에는 WVD가 없다.
- 141–145: 기후 위치 루프는 WIND.uz·WIND.phiwnd를 열 인덱스 없이 매번 덮어쓴다. xw·yw는 위치별 kk 인덱스를 사용한다(147–148).
- 84–85: 모든 바람 자료 위치의 시각 이동에는 WAVE.dtrewind(1)을 사용한다.
- 168–170: dune·mud가 모두 거짓인 분기는 phiwnd만 빈 배열로 만든다. uz를 설정하는 문장은 없다.
