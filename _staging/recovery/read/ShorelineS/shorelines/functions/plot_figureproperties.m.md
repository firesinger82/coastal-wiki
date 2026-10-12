---
file: models/ShorelineS/raw/source_code/shorelines/functions/plot_figureproperties.m
lines: 54
sha256: 5569b0b02cdeb1554c656ff5164d026ac13da35c364f4e241565b36fb6a33bbe
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# plot_figureproperties.m — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | 함수 시그니처(1). 해안선 그림의 인쇄용 속성·종이 크기를 정한다는 설명(4–5). 2행은 함수 시그니처를 반복한 주석이다. 3·6행은 빈 주석이다. 원문: `function plot_figureproperties(fh,HOR,VER,SCALE,X0,Y0)` (1). [10-12 전수 검증 정정] |
| 7–34 | 시작 시 1행 plot_figureproperties 함수 안. 2020년 저작권·연락처, LGPL 2.1 이상·무보증 안내와 빈 줄(7–34). |
| 35–45 | 시작 시 1행 plot_figureproperties 함수 안. 부족한 인수의 기본값은 HOR=21*35, VER=29*35, SCALE=35, X0=70, Y0=70이다(35–39). isoctave를 호출하는 조건이 참이면 PaperType a4, 그 외에는 a4letter를 사용한다(41–45). 원문: `if nargin<2;HOR=21*35;end` (35), `if nargin<3;VER=29*35;end` (36), `if nargin<4;SCALE=35;end` (37), `if nargin<5;X0=70;end` (38), `if nargin<6;Y0=70;end` (39), `if (isoctave)` (41), `pptyp = 'a4';` (42), `else` (43), `pptyp = 'a4letter';` (44). |
| 46–54 | 시작 시 1행 plot_figureproperties 함수 안. 세로 용지 방향(portrait), HOR/SCALE·VER/SCALE의 종이 위치·크기, X0·Y0·HOR·VER의 화면 위치를 set으로 적용한다(47–50). 용지 단위는 centimeters, PaperPositionMode는 manual, PaperType은 선택한 pptyp이다(51–53). 함수 종료(54). 원문: `set(fh, 'PaperOrientation','portrait', ...` (47), `'PaperPosition',[0 0 HOR/SCALE VER/SCALE], ...` (48), `'PaperSize',[HOR/SCALE VER/SCALE], ...` (49), `'Position',[X0,Y0,HOR,VER], ...` (50), `'PaperUnits','centimeters', ...` (51), `'PaperPositionMode','manual', ...` (52), `'PaperType',pptyp);` (53). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
