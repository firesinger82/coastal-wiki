---
file: models/ShorelineS/raw/source_code/shorelines/functions/interpolate_props.m
lines: 125
sha256: e7064e1c21ae21d06b2ec806bd76a903d9f18342cd444f43d871be39570ed38b
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# interpolate_props.m — 판독 구간 기록

구간은 1행부터 125행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | 함수 시그니처(1). 격자가 바뀔 때 매 시간 단계(time step)마다 해안 속성을 다시 보간한다는 설명(4–5). 입력은 COAST 좌표, DUNE 사구(dune) 위치·해빈 폭·사구 기부와 정상 높이, MUD 갯벌(mud flat)·맹그로브(mangrove) 폭이다(7–22). 출력 속성·단위 설명(24–35). 원문: `function [COAST]=interpolate_props(COAST,DUNE,MUD,TIME)` (1). |
| 37–63 | 시작 시 1행 interpolate_props 함수 안. 2020년 저작권·연락처, LGPL 2.1 이상·무보증 안내(37–63). |
| 64–77 | 시작 시 1행 interpolate_props 함수 안. MUD와 DUNE을 모두 사용하지 않으면 wberm을 빈 배열로 만들고 반환한다(64–67). i_mc를 가져온다(69). TIME.it가 0 이상이면 현재 COAST 좌표와 weighted_distance 방법을 사용한다(70–76). 원문: `if ~MUD.used && ~DUNE.used` (64), `COAST.wberm = [];` (65), `return;` (66), `i_mc=COAST.i_mc;` (69), `if TIME.it>=0 %` (70), `x            =   COAST.x;` (74), `y            =   COAST.y;` (75), `method       =   'weighted_distance';` (76). |
| 78–102 | 시작 시 1행 interpolate_props 함수·70행 TIME.it 분기 안. DUNE 사용 시 wberm·dfelev·dcelev를 현재 xdune·ydune에서 보간한다(78–84). cs는 xdune0·ydune0에서 보간한다(87–92). xtill이 비어 있지 않으면 cstill·xtill·perctill도 보간한다(88–96). xtill이 비었으면 cstill을 cs로, perctill을 0으로, xtill을 빈 배열로 둔다(97–101). get_interpolation_on_grid를 두 번 호출한다(81·91). 원문: `if DUNE.used` (78), `fieldnm1={'wberm','dfelev','dcelev'};` (80), `[var1i,idGRID,distw]=get_interpolation_on_grid(method,x,y,DUNE.xdune,DUNE.ydune,DUNE,fieldnm1,{});` (81), `COAST.wberm  = var1i.wberm(:)';` (82), `COAST.dfelev  = var1i.dfelev(:)';` (83), `COAST.dcelev  = var1i.dcelev(:)';` (84), `fieldnm1={'cs'};` (87), `if ~isempty(DUNE.xtill)` (88), `fieldnm1={'cs','cstill','xtill','perctill'};` (89), `[var1i,idGRID,distw]=get_interpolation_on_grid(method,x,y,DUNE.xdune0,DUNE.ydune0,DUNE,fieldnm1,{});` (91), `COAST.cs = var1i.cs(:)';` (92), `if ~isempty(DUNE.xtill)` (93), `COAST.cstill = var1i.cstill(:)';` (94), `COAST.perctill = var1i.perctill(:)';` (95), `COAST.xtill  = var1i.xtill(:)';` (96), `else` (97), `COAST.cstill=COAST.cs;` (98), `COAST.perctill = zeros(size(COAST.cs));` (99), `COAST.xtill  = [];` (100). |
| 103–115 | 시작 시 1행 interpolate_props 함수·70행 TIME.it 분기·78행 DUNE.used 분기 안. 0번째 단계가 아니고 DUNE.xtill이 비어 있지 않으면 이전 해안선 좌표를 가져온다(104–106). 첫 해안 구간에서 xtill_mc를 xtill_mc1로 보관한다(107–109). interpNANs로 NaN을 보간한 뒤 get_interpolation_on_grid로 현재 격자의 xtill을 다시 만든다(110–113). 104행 조건과 DUNE 분기를 종료한다(114–115). 원문: `if TIME.it~=0 && ~isempty(DUNE.xtill)` (104), `x1_mc=COAST.x1_mc;` (105), `y1_mc=COAST.y1_mc;` (106), `if COAST.i_mc==1` (107), `COAST.xtill_mc1=COAST.xtill_mc(:)'; % cross-shore position of till in dune [m w.r.t. dune front]` (108), `fieldnm1={'xtill_mc1'};` (110), `COAST.xtill_mc1=interpNANs(COAST.xtill_mc1);` (111), `[var1i]=get_interpolation_on_grid(method,x,y,x1_mc,y1_mc,COAST,fieldnm1,{});` (112), `COAST.xtill=var1i.xtill_mc1(:)';` (113). [10-12 전수 검증 정정] |
| 116–125 | 시작 시 1행 interpolate_props 함수·70행 TIME.it 분기 안. MUD를 사용하면 Bf·Bm·Bfm을 xmgv·ymgv에서 보간한다(116–119). 필드 루프로 결과를 행 배열로 넣는다(120–122). MUD 분기·TIME.it 분기·함수 종료(123–125). 원문: `if MUD.used` (116), `fieldnm1={'Bf','Bm','Bfm'};` (118), `[var1i,~,~]=get_interpolation_on_grid(method,x,y,MUD.xmgv,MUD.ymgv,MUD,fieldnm1,{});` (119), `for ff=1:length(fieldnm1)` (120), `COAST.(fieldnm1{ff})  = var1i.(fieldnm1{ff})(:)';` (121). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 35·89·95·99: 출력 주석은 tillperc를 적지만 실행 코드는 perctill 필드를 사용한다.
- 69·81·91: i_mc는 가져온 뒤 사용하지 않는다. 두 호출의 idGRID·distw 출력도 이후 참조하지 않는다.
- 64–67: MUD와 DUNE을 모두 사용하지 않는 반환 분기는 COAST.wberm만 빈 배열로 설정한다.
