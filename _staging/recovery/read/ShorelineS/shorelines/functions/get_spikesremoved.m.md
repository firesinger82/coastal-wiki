---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_spikesremoved.m
lines: 102
sha256: b7c7439d966da649b8c638caecdd4c8c366881b09af739a8e200d036a0b748f6
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_spikesremoved.m — 판독 구간 기록

구간은 1행부터 102행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | 함수 시그니처는 `function [COAST,TRANSP,WAVE]=get_spikesremoved(COAST,TRANSP,WAVE)` (1). 해안 좌표(coastline coordinate)의 뾰족한 격자점(spike) 제거 목적을 적는다(2–5). 저작권·연락처·LGPL 2.1 이상·무보증 주석을 포함한다(6–32). `if ~isempty(COAST.wberm)` (33)이면 즉시 return한다(34). 분기를 닫는다(35). |
| 36–63 | 시작 시 1행 get_spikesremoved 함수 안. ds0에 COAST.ds0를 복사한다(37). `if ~isscalar(ds0)` (38)이면 격자 간격(grid spacing) 축약식 `ds0=min(ds0(:,3));` (39). 제거 계수는 `thr_fraction_of_gridsize=0.2;` (41). 구간 수 식은 `n_mc=length(find(isnan(COAST.x_mc)))+1;` (43). 역순 구간 반복은 `for i_mc=n_mc:-1:1` (44). get_one_polygon 호출은 `[ x,y,~,i1,i2 ] = get_one_polygon( COAST.x_mc,COAST.y_mc,i_mc );` (45). ar·s를 0으로 초기화한다(46–47). `if length(x)>1` (49)이면 점 반복 `for i=1:length(x)` (50). `if i>=2` (51)이면 누적 거리식 `s(i)=s(i-1)+hypot(x(i)-x(i-1),y(i)-y(i-1));` (52). `if i==1` (54)이면 s(1)=0과 양옆점 거리식 `ds=hypot(x(2)-x(end),y(2)-y(end));` (56). `elseif i>1 && i<length(x)` (57)이면 `ds(i)=hypot(x(i+1)-x(i-1),y(i+1)-y(i-1));` (58). `elseif i==length(x)` (59)이면 `ds(i)=hypot(x(1)-x(end-1),y(1)-y(end-1));` (60). 분기·점 반복 종료와 빈 줄을 포함한다(53·61–63). |
| 64–88 | 시작 시 1행 get_spikesremoved 함수 안. 시작 시 44행 i_mc 반복·49행 점 수 분기 안. 제거 판정식은 `IDspiky=(ds<thr_fraction_of_gridsize*ds0);` (64). 좌표 NaN 대체 방식은 주석이다(65–68). 유지점 선택식은 `xnew=x(~IDspiky);` (69), `ynew=y(~IDspiky);` (70). 좌표 insert_section 호출은 `[COAST.x_mc,COAST.y_mc,i1,i2]=insert_section(xnew,ynew,COAST.x_mc,COAST.y_mc,i_mc);` (71). `if isempty(xnew)` (73)이면 `try` (74)에서 빈 구간으로 dSds_mc·PHIc_mc·PHIf_mc·QS_mc와 파랑 필드를 교체한다. 호출 원문은 `[COAST.dSds_mc]=insert_section(xnew,COAST.dSds_mc,i_mc);` (75); `[COAST.PHIc_mc]=insert_section(xnew,COAST.PHIc_mc,i_mc);` (76); `[COAST.PHIf_mc]=insert_section(xnew,COAST.PHIf_mc,i_mc);` (77); `[TRANSP.QS_mc]=insert_section(xnew,TRANSP.QS_mc,i_mc);` (78); `[WAVE.HSo_mc]=insert_section(xnew,WAVE.HSo_mc,i_mc);` (79); `[WAVE.PHIo_mc]=insert_section(xnew,WAVE.PHIo_mc,i_mc);` (80); `[WAVE.TP_mc]=insert_section(xnew,WAVE.TP_mc,i_mc);` (81); `[WAVE.HStdp_mc]=insert_section(xnew,WAVE.HStdp_mc,i_mc);` (82); `[WAVE.PHItdp_mc]=insert_section(xnew,WAVE.PHItdp_mc,i_mc);` (83); `[WAVE.dPHItdp_mc]=insert_section(xnew,WAVE.dPHItdp_mc,i_mc);` (84); `[WAVE.HSbr_mc]=insert_section(xnew,WAVE.HSbr_mc,i_mc);` (85); `[WAVE.PHIbr_mc]=insert_section(xnew,WAVE.PHIbr_mc,i_mc);` (86); `[WAVE.dPHIbr_mc]=insert_section(xnew,WAVE.dPHIbr_mc,i_mc);` (87); `[WAVE.hbr_mc]=insert_section(xnew,WAVE.hbr_mc,i_mc);` (88). 빈 줄을 포함한다(72). |
| 89–102 | 시작 시 1행 get_spikesremoved 함수 안. 시작 시 44행 i_mc 반복·49행 점 수 분기·73행 빈 xnew 분기·74행 try 블록 안. `catch` (89)에서는 관련 수송·파랑 구간을 비우지 못했다는 경고를 출력한다(90). try·빈 구간 분기를 닫는다(91–92). 구간 수 감소식은 `COAST.n_mc=COAST.n_mc-1;` (93). 수송점(transport point) 재생성 호출은 `[COAST]=get_transportpoints(COAST);` (96). 점 수 분기·구간 반복을 닫는다(97–98). 반복 밖의 cleanup_nans 호출은 `[COAST,di]=cleanup_nans(COAST);` (100). 주석·빈 줄·함수 종료를 포함한다(94–95·99·101–102). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 46–52·100: ar는 0 대입 이후 참조하지 않는다. s는 거리 누적 후 참조하지 않는다. cleanup_nans의 di 출력은 이후 참조하지 않는다.
- 73–93: 빈 xnew 조건은 관련 자료의 빈 구간 교체만 감싼다. COAST.n_mc 감소식은 그 조건 밖에서 길이가 1보다 큰 각 원래 구간마다 실행한다.
- 73–90: 관련 필드 insert_section 호출은 하나의 try 블록에서 차례로 실행한다. catch는 경고만 출력하며 앞 호출의 결과를 되돌리는 문장은 없다.
