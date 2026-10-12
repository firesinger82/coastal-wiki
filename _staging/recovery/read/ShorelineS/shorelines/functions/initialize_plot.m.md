---
file: models/ShorelineS/raw/source_code/shorelines/functions/initialize_plot.m
lines: 150
sha256: 4553ea97b0c4042fd589d019c9a382f760cef74e307075542d089e9988e7b898
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# initialize_plot.m — 판독 구간 기록

구간은 1행부터 150행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | 함수 시그니처는 `function [FORMAT] = initialize_plot(S,COAST)` (1). FORMAT 그림 설정(plot parameter) 초기화 목적을 설명한다(2–5). 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(6–33). |
| 34–55 | 시작 시 1행 initialize_plot 함수 안. 초기화 문구를 출력한다(34). `if isempty(S.xlimits)` (37)이면 해안 x 범위식 `xlims=[min(COAST.x_mc),max(COAST.x_mc)];` (38), 5% 확장과 좌표 이동(offset) 식 `S.xlimits = [min(xlims)-0.05*diff(xlims),max(xlims)+0.05*diff(xlims)] - S.xyoffset(1);` (39). `else` (40)이면 지정 x 범위 이동식 `S.xlimits = S.xlimits - S.xyoffset(1);` (41). `if isempty(S.ylimits)` (43)이면 해안 y 범위식 `ylims=[min(COAST.y_mc),max(COAST.y_mc)];` (44), 확장·이동식 `S.ylimits = [min(ylims)-0.05*diff(ylims),max(ylims)+0.05*diff(ylims)] - S.xyoffset(2);` (45). `else` (46)이면 지정 y 범위 이동식 `S.ylimits = S.ylimits - S.xyoffset(2);` (47). 최소 표시 폭·정렬 식은 `S.xlimits(2)=max(S.xlimits(1)+500,S.xlimits(2));` (49); `S.ylimits(2)=max(S.ylimits(1)+500,S.ylimits(2));` (50); `S.xlimits=sort(S.xlimits);` (51); `S.ylimits=sort(S.ylimits);` (52). 최종 xlimits·ylimits·xyoffset을 FORMAT에 복사한다(53–55). 빈 줄·주석·분기 종료를 포함한다(35–36·42·48). |
| 56–82 | 시작 시 1행 initialize_plot 함수 안. `if S.plotvisible==0` (58)이면 FORMAT.plotvisible='off', `else` (60)이면 'on'으로 설정한다(59·61). figure(11)·clf 호출은 `FORMAT.mainfighandle = figure(11);clf;` (64). Visible 속성을 설정한다(65). 초기화식은 `FORMAT.xmax=0;FORMAT.ymax=0;FORMAT.xmin=0;FORMAT.ymin=0;FORMAT.nmax=0;` (66). 창 가로세로 조건은 `if diff(S.xlimits)/diff(S.ylimits) > 1850/850` (68). 참이면 가로 크기 `sx=1850;` (69), 세로 계산식 `sy=1850*diff(S.ylimits)/diff(S.xlimits);` (70). `else` (71)이면 가로 계산식 `sx=850*diff(S.xlimits)/diff(S.ylimits);` (72), 세로 크기 `sy=850;` (73). plot_figureproperties·xlim·ylim 호출은 `plot_figureproperties(FORMAT.mainfighandle,sx,sy,32);` (75); `xlim(S.xlimits);ylim(S.ylimits);` (76). `try` (78)에서는 S.imgfilename·S.worldfilename을 FORMAT에 복사한다(79–80). try를 닫는다(81). 주석·빈 줄을 포함한다(56–57·62–63·67·74·77·82). [10-12 전수 검증 정정] |
| 83–118 | 시작 시 1행 initialize_plot 함수 안. `if S.yesplot` (83)이면 figure(11)·clf로 그림을 초기화한다(84). 사각형 범위 plot 호출은 `plot([S.xlimits(1) S.xlimits(2) S.xlimits(2) S.xlimits(1) S.xlimits(1)], ...` (85); `[S.ylimits(1) S.ylimits(1) S.ylimits(2) S.ylimits(2) S.ylimits(1)],'k:');` (86). axis equal·hold on·xlabel·ylabel과 COAST.x_mc0·y_mc0 plot을 호출한다(87–92). `if ~isempty(S.xlimits)` (93)이면 xlim, `if ~isempty(S.ylimits)` (96)이면 ylim을 설정한다(94·97). 그림 분기를 닫는다(95·98–99). xp_mc·yp_mc와 육지 다각형(land polygon) xb·yb를 빈 cell 배열로 초기화한다(101–106). `if ~isempty(S.slplot)  % For extracting specific shorelines` (109)이면 지정 해안선 추출 날짜식 `FORMAT.plot_time(:)=datenum(S.slplot(:,1),'yyyy-mm-dd');` (110), 첫 날짜 번호 `FORMAT.tsl=1;` (111), 날짜 선택식 `FORMAT.tplot=FORMAT.plot_time(FORMAT.tsl);` (112), 끝 날짜 표식 `FORMAT.plot_time(end+1)=0;` (113). `else` (114)이면 tplot·tsl·plot_time을 빈 배열로 만든다(115–117). 주석·빈 줄·분기 종료를 포함한다(100·103–104·107–108·118). |
| 119–150 | 시작 시 1행 initialize_plot 함수 안. `if ~exist(fullfile(pwd,S.outputdir),'dir')` (121)이면 출력 디렉터리(directory) mkdir를 호출한다(122). S의 plotinterval·usefill·usefillpoints·ldbplot·llocation·slplot·video·outputdir·fignryear·figplotfreq·ld·xywave·plotqs·ploths·plotdir·plotupw·printfig·fastplot을 FORMAT에 복사한다(125–142). 이 구간에는 해당 S 필드 기본값 대입이 없다. FORMAT.plotprofiles를 비우고 S.xyprofiles를 복사한다(143–144). plotcoast 초기값은 `FORMAT.plotcoast=0;` (145). struct2log는 주석이다(146–147). 분기 종료·빈 줄·함수 종료를 포함한다(119–120·123–124·148–150). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 49–50·68–75: 최소 표시 폭은 각 방향에서 500으로 고정한다. 창 크기 계산은 1850·850과 plot_figureproperties의 인수 32를 사용한다.
- 58–65: plotvisible==0이면 Visible을 off로 설정한다. figure(11)·clf 호출은 plotvisible 분기 밖에 있다.
- 78–81: S.imgfilename·S.worldfilename 접근은 try 안에 있다. 이 try 블록에는 catch 절이 없다.
