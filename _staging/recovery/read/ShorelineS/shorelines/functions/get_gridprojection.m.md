---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_gridprojection.m
lines: 74
sha256: 6662181bd132b71389dbc25b9edd786b7697e54d7c131e0f3680b92dabcec7c3
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_gridprojection.m — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–46 | 함수 시그니처 `function [SCALARS,VECTORS,idgrid]=get_gridprojection(COAST,WAVE,TRANSP,xp,yp,xw,yw,scalarfields,vectorfields,method)` (1). 해안선(shoreline) 자료를 다른 격자로 보간(interpolation)하는 목적·필드 목록·방법·출력 설명(4–18). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(19–46). |
| 47–59 | var1 빈 구조체(48). 스칼라 필드 루프 `for ff=1:length(scalarfields)` (49). WAVE 필드 조건 `if isfield(WAVE,[scalarfields{ff},'_mc'])` (50)이면 WAVE _mc 복사(51). TRANSP 조건 `elseif isfield(TRANSP,[scalarfields{ff},'_mc'])` (52)이면 TRANSP _mc 복사(53). 나머지 `else` (54)는 COAST _mc 복사(55). get_convertgrid 호출은 주석 처리(58). 추가 원문: `var1.(scalarfields{ff})=WAVE.([scalarfields{ff},'_mc']);` (51). `var1.(scalarfields{ff})=TRANSP.([scalarfields{ff},'_mc']);` (53). `var1.(scalarfields{ff})=COAST.([scalarfields{ff},'_mc']);` (55). [10-12 전수 검증 보완] |
| 60–71 | var2 빈 구조체(61). 방향 필드 루프 `for ff=1:length(vectorfields)` (62). WAVE 조건 `if isfield(WAVE,[vectorfields{ff},'_mc'])` (63)이면 WAVE _mc 복사(64). TRANSP 조건 `elseif isfield(TRANSP,[vectorfields{ff},'_mc'])` (65)이면 TRANSP _mc 복사(66). 나머지 `else` (67)는 COAST _mc 복사(68). 추가 원문: `var2.(vectorfields{ff})=WAVE.([vectorfields{ff},'_mc']);` (64). `var2.(vectorfields{ff})=TRANSP.([vectorfields{ff},'_mc']);` (66). `var2.(vectorfields{ff})=COAST.([vectorfields{ff},'_mc']);` (68). [10-12 전수 검증 보완] |
| 72–74 | 선택 method·목표 좌표 xp·yp·원자료 좌표 xw·yw·두 구조체로 보간 호출 `[SCALARS,VECTORS,idgrid]=get_interpolation_on_grid(method,xp,yp,xw,yw,var1,var2);` (73). 함수 종료(74). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 50–55·63–68: 같은 이름이 여러 구조체에 있으면 WAVE 다음 TRANSP 순으로 선택한다. COAST 접근 앞에는 필드 존재 검사가 없다.
- 72–73: 주석은 가중 거리 보간을 적는다. 실제 호출에는 인수 method를 그대로 전달한다.
