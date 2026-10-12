---
file: models/ShorelineS/raw/source_code/shorelines/functions/prepare_coastline.m
lines: 174
sha256: 4b195f5d821ad1c46127808f28ca9f9d14562d7b2782b567dc40db74ba252153
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# prepare_coastline.m — 판독 구간 기록

구간은 1행부터 174행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–64 | 함수 시그니처는 `function [COAST]=prepare_coastline(S)` (1). 입력·출력 주석은 해안선(coastline) 좌표, 활성 높이(active height), 격자 간격, 평활화(smoothing), 굴절(refraction), 경계조건(boundary condition)을 설명한다(2–36). 주석의 twopoints 기본값은 1(25), smoothfac의 합리적 값은 0부터 0.1(26), smoothrefrac 값은 0부터 1이다(27). 실행 코드에는 S 필드 기본값 대입이 없다. 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(37–64). |
| 65–97 | 로그 뒤 COAST를 만든다(65–66). ldbcoastline·ds0·xlimits·ylimits·xyoffset·twopoints·smoothfac·smoothrefrac·tanbeta·griddingmethod·maxangle·preserveorientation을 같은 이름의 S 필드에서 복사한다. h0는 비우고 h0input은 S.d, PHIf0는 S.phif에서 복사한다(67–81). 기본값은 `COAST.mergegrid=0;` (82), `COAST.PHIc0bnd=[nan,nan];` (86). `if ischar(S.boundaryconditionstart)` (87)이면 `COAST.boundaryconditionstart={S.boundaryconditionstart,nan};` (88), `else` (89)이면 입력을 그대로 복사한다. `if ischar(S.boundaryconditionend)` (92)이면 `COAST.boundaryconditionend={S.boundaryconditionend,nan};` (93), `else` (94)이면 그대로 복사한다. 경계조건 설명과 빈 줄을 포함한다. |
| 98–141 | `if ~isempty(S.ldbcoastline)` (98) 안에서 `if ischar(S.ldbcoastline)` (100)이면 load(101), `else` (102)이면 직접 입력을 복사한다. `if isempty(S.xyoffset)` (105)이면 `COAST.xyoffset = [floor(min(xy_mc(:,1))/1000)*1000 , floor(min(xy_mc(:,2))/1000)*1000];` (106). 좌표식은 `COAST.x_mc=xy_mc(:,1)' - S.xyoffset(1);` (108), `COAST.y_mc=xy_mc(:,2)' - S.xyoffset(2);` (109). 초기 좌표에 복사한다(110–111). `elseif ~isempty(S.xmc)` (113)는 S.xmc·S.ymc를 복사하고 try로 S.xmc0·S.ymc0를 읽는다. catch는 현재 입력 좌표를 초기 좌표로 복사한다(117–123). `else` (126)는 그림 11에 입력 범위를 그리고 안내문을 만든다. 안내문 위치는 `xl(1)+0.02*diff(xl)`과 `yl(2)-0.01*diff(yl)`이다(135). `[COAST.x_mc,COAST.y_mc]=select_multi_polygon('r');` (136)를 호출한 뒤 안내문을 숨기고 초기 좌표를 복사한다(137–139). 분기 종료와 빈 줄을 포함한다. [10-12 전수 검증 보완] |
| 142–161 | 좌표 배열 양 끝과 중복 NaN을 정리한다. `idnotnan=find(~isnan(COAST.x_mc));` (143), `COAST.x_mc=COAST.x_mc(idnotnan(1):idnotnan(end));` (144), `COAST.y_mc=COAST.y_mc(idnotnan(1):idnotnan(end));` (145), `idnan=find(isnan(COAST.x_mc));` (146), `iduse=setdiff([1:length(COAST.x_mc)],idnan(diff(idnan)==1));` (147), `COAST.x_mc=COAST.x_mc(iduse);` (148), `COAST.y_mc=COAST.y_mc(iduse);` (149). `if S.gisconvention` (152)이면 `COAST.x_mc = COAST.x_mc(end:-1:1);` (153), `COAST.y_mc = COAST.y_mc(end:-1:1);` (154). 요소 수는 `nans=find(isnan(COAST.x_mc));` (158), `COAST.n_mc=length(nans)+1;` (159)로 정하고 n_mc0에 복사한다(160). |
| 162–174 | 사구(dune) 표시용 초기 해안선 방향을 계산한다. `xq=(COAST.x_mc0(1:end-1)+COAST.x_mc0(2:end))/2;` (163), `yq=(COAST.y_mc0(1:end-1)+COAST.y_mc0(2:end))/2;` (164), `xq=[1.5*COAST.x_mc0(1)-0.5*COAST.x_mc0(2),xq];` (165), `yq=[1.5*COAST.y_mc0(1)-0.5*COAST.y_mc0(2),yq];` (166), `xq=[xq,COAST.x_mc0(end)];` (167), `yq=[yq,COAST.y_mc0(end)];` (168), `COAST.PHIcxy_mc0 = mod(360.0-atan2d(diff(yq),diff(xq)),360);` (169). struct2log 호출은 주석이다(172). 빈 줄과 함수 종료를 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–9·113–122: 머리말의 직접 입력 필드 이름은 x_mc·y_mc이다. 실행 코드의 입력 필드 이름은 xmc·ymc·xmc0·ymc0이다.
- 105–109: S.xyoffset이 비었을 때 자동 오프셋을 COAST.xyoffset에 대입한다. 바로 뒤 좌표식은 S.xyoffset을 참조한다.
- 110–139·142–155·163–169: 초기 좌표 x_mc0·y_mc0는 현재 좌표의 NaN 정리와 gisconvention 역순 처리를 수행하기 전에 저장한다. 방향 계산은 초기 좌표를 사용한다.
- 143–145·165–166: 정리 블록은 idnotnan의 첫 원소와 마지막 원소를 바로 참조한다. 방향 계산은 초기 좌표의 두 번째 원소를 바로 참조한다. 해당 참조 앞에 원소 수 검사는 없다.
