---
file: models/ShorelineS/raw/source_code/shorelines/functions/prepare_nourishment.m
lines: 172
sha256: b2027ab68a94741fa68f18aa81f4eb19e59c79f4641f82f960223bbae606cbb3
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# prepare_nourishment.m — 판독 구간 기록

구간은 1행부터 172행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–67 | 함수 시그니처는 `function [NOUR] = prepare_nourishment(S,COAST,STRUC)` (1). 주석은 양빈(nourishment) 입력의 .NOR 파일, 다각형(polygon)·공급률·날짜 파일, 대화형 입력, COAST·STRUC 표시 좌표와 NOUR 출력을 설명한다(2–39). growth의 주석 범위는 0부터 1, 기본값은 1이다(9·32). 이 파일에는 S.growth의 기본값 대입이 없다. 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(40–67). |
| 68–90 | 로그 뒤 NOUR를 만들고 xnour·ynour·nnour·tstart·tend·rate를 비운다(68–75). nourish·growth를 같은 이름의 S 필드에서, method를 S.nourmethod에서 복사한다(76–78). `if ~isempty(findstr(lower(S.norfile),'.nor'))` (81)이면 S.norfile을 S.ldbnourish에 복사하고 `NOUR.nourish=1;` (83). `elseif isfield(S,'ldbnour') & isempty(S.ldbnourish)` (84)이면 S.ldbnour를 S.ldbnourish에 복사하고 `NOUR.nourish=1;` (86). `elseif ~isempty(findstr(lower(S.ldbnourish),'.nor'))` (87)이면 `NOUR.nourish=1;` (88). 숫자로 설정하는 S 필드 기본값은 없다. |
| 91–117 | `if ~isempty(NOUR.nourish) && NOUR.nourish ~= 0` (91) 안에서 `if ~isempty(findstr(lower(S.ldbnourish),'.nor'))` (93)이면 `NOUR.nourish=2;` (94), `readmatfile=1;` (95), load(97). `NOUR.nnour=size(nor,1);` (98), `NOUR.xnour=[nor(:,1),nor(:,3)];` (99), `NOUR.ynour=[nor(:,2),nor(:,4)];` (100), `NOUR.tstart=datenum(num2str(nor(:,5)),'yyyymmdd');` (101), `NOUR.tend=datenum(num2str(nor(:,6)),'yyyymmdd');` (102), `NOUR.rate=(nor(:,7)./(NOUR.tend-NOUR.tstart))*365;` (103). `elseif ~isempty(S.ldbnourish) && NOUR.nourish==3` (105)이면 `NOUR.nourish=2;` (106), `readmatfile=1;` (107), load와 nor.nor 추출(109–110), `NOUR.nnour=size(nor,1);` (111), `NOUR.xnour=[nor(:,1),nor(:,3)];` (112), `NOUR.ynour=[nor(:,2),nor(:,4)];` (113), `NOUR.tstart=datenum(num2str(nor(:,5)),'yyyymmdd');` (114), `NOUR.tend=datenum(num2str(nor(:,6)),'yyyymmdd');` (115), `NOUR.rate=(nor(:,7)./(NOUR.tend-NOUR.tstart))*365;` (116). |
| 118–154 | 시작 시 91행 활성화 분기·93행 입력 선택 분기 안. `elseif ~isempty(S.ldbnourish)` (118)이면 `NOUR.nourish=1;` (119), `readmatfile=0;` (120), load(121), `NOUR.xnour=xynour(:,1)'-S.xyoffset(1);` (122), `NOUR.ynour=xynour(:,2)'-S.xyoffset(2);` (123). 파일명을 복사한 뒤 `matname(end-2:end)='mat';` (125). `if exist(matname)==2` (126)이면 load(127), `NOUR.nnour=length(nourishments);` (128), `for inour=1:NOUR.nnour` (129)에서 구조체의 tstart·tend·rate를 복사한다(130–132). `readmatfile=1;` (134). 입력 선택의 `else` (137)는 `NOUR.nourish=1;` (138), `readmatfile=0;` (139). `if length(STRUC.xhard)>1` (141)이면 구조물과 해안선을 함께 그리고, `else` (145)이면 해안선만 그린다. 안내문 위치는 `xl(1)+0.02*diff(xl)`과 `yl(2)-0.01*diff(yl)`이다(151). 안내문 뒤 `[NOUR.xnour,NOUR.ynour]=select_multi_polygon('k');` (152)를 호출하고 안내문을 숨긴다(153). [10-12 전수 검증 보완] |
| 155–172 | 시작 시 91행 활성화 분기 안이며 입력 선택 분기 밖. `if readmatfile==0` (155)이면 get_one_polygon으로 nnour를 받는다(156). `if ~isempty(S.nourratefile)` (158)이면 `NOUR.tstart=datenum(importdata(S.nourstartfile));` (159), `NOUR.tend=datenum(importdata(S.nourendfile));` (160), load로 rate 판독(161). `else` (162)는 `NOUR.tstart(1:n)=datenum(S.reftime);` (163), `NOUR.tend(1:n)=datenum(S.endofsimulation);` (164), `NOUR.rate(1:NOUR.nnour)=S.nourrate;` (165). struct2log 호출은 주석이다(169). 빈 줄과 조건·함수 종료를 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8·31·105: 입력 스위치 설명은 0/1, 출력 설명은 0/1/2를 적는다. 실행 코드에는 NOUR.nourish==3 분기가 있다.
- 81–88: .nor 입력과 이전 필드 이름 입력을 감지하면 NOUR.nourish를 1로 다시 설정한다.
- 103·116: 공급률 계산은 종료일과 시작일 차이를 분모로 쓰고 365를 곱한다. 해당 블록에는 날짜 차이가 0인지 검사하는 조건이 없다.
- 99–100·112–113·122–123: 두 .nor 계열 분기는 원래 좌표를 구성한다. 다각형 파일 분기는 좌표에서 S.xyoffset을 뺀다.
- 163–164: 기본 날짜 분기는 n을 범위 끝 인덱스로 사용한다. 이 함수에는 n에 앞선 대입이 없다. 다각형 개수는 NOUR.nnour로 받는다(156).
