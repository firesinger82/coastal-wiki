---
file: models/ShorelineS/raw/source_code/shorelines/functions/prepare_delta.m
lines: 88
sha256: 655f69d748d9b4c6d26ed772c90fb134ada0533c969834f9dd7a1e54b718a8e3
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# prepare_delta.m — 판독 구간 기록

구간은 1행부터 88행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–52 | 함수 시그니처는 `function [DELTA]=prepare_delta(S)` (1). 주석은 창조 삼각주(flood delta)와 사취(spit)의 다각형(polygon), S.flooddelta 스위치, S.dxf 해상도, S.overdepth 초기 추가 수심을 설명한다(2–24). 이 파일에는 S 필드 기본값 대입이 없다. 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(25–52). |
| 53–74 | 로그 뒤 DELTA를 만들고 xflood·yflood·flooddeficit·fcellarea를 빈 배열로 초기화한다(53–60). `if S.flooddelta & S.channel` (62) 안에서 `if ~isempty(S.xfloodpol)` (63)이면 xfloodpol·yfloodpol·xspitpol·yspitpol을 S에서 복사한다. `elseif ~isempty(S.ldbflood)` (68)이면 두 파일을 load(69·72)하고 `xfloodpol=xyflood(:,1)'-S.xyoffset(1);` (70), `yfloodpol=xyflood(:,2)'-S.xyoffset(2);` (71), `xspitpol=xyspit(:,1)'-S.xyoffset(1);` (73), `yspitpol=xyspit(:,2)'-S.xyoffset(2);` (74)를 계산한다. |
| 75–88 | 시작 시 62행 두 스위치 분기와 63행 입력 선택 분기 안. `else` (75)는 `figure;plot(x_mc,y_mc,xrmc,yrmc,'--');axis equal;hold on;` (76)으로 그림을 만들고 select_multi_polygon('k')를 창조 삼각주와 사취에 각각 호출한다(78·80). flooddelta.mat에 네 좌표를 저장한다(81). 입력 선택 분기를 닫은 뒤 `[DELTA.xflood,DELTA.yflood,DELTA.flooddeficit,DELTA.fcellarea] = prepare_flooddelta(xfloodpol,yfloodpol,S.dxf,S.dxf,S.overdepth);` (83)를 호출한다. struct2log 호출은 주석이다(86). 바깥 분기와 함수를 닫는다(87–88). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9·12·68–74: 주석은 ldbflood·ldbspit에 직접 행렬을 제공할 수 있다고 적는다. 실행 분기는 두 입력을 load 인수로 전달한다.
- 1·76: 대화형 그림은 x_mc·y_mc·xrmc·yrmc를 참조한다. 이 함수의 인수는 S뿐이며 이 파일에서 네 변수에 앞선 대입은 없다.
- 66–67·73–74·80·83: xspitpol·yspitpol을 읽거나 선택하지만 prepare_flooddelta 호출에는 두 변수를 전달하지 않는다.
