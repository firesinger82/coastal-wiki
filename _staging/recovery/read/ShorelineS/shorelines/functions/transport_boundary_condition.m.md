---
file: models/ShorelineS/raw/source_code/shorelines/functions/transport_boundary_condition.m
lines: 122
sha256: 138c027fc5ce983691b9e073ed7249c66663aab23e14a7868a3c262405702bc7
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# transport_boundary_condition.m — 판독 구간 기록

구간은 1행부터 122행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–58 | 함수 시그니처(1), 비주기 해안 경계조건(boundary condition)의 목적과 Fixed/Neumann·Periodic·Closed·Angleconstant/Gradient 설명(4–11), TRANSP·COAST·GROYNE 입력과 QS 출력 설명(13–29), 저작권·LGPL·무보증 주석 및 빈 줄(31–58). 입력 필드 기본값 설정문은 없다. 원문: `function [TRANSP]=transport_boundary_condition(TRANSP,COAST,GROYNE)` (1). |
| 59–91 | 시작 시 1행 함수 안. 기존 QS를 보관하고 비주기 해안만 처리한다(60–61). 시작점에 돌제(groyne)가 있으면 side=2로 찾고, idgroyne 검사 내부의 수송 대입은 주석 처리되어 있다(62–68). 돌제가 없는 else에서 Periodic은 양쪽 내부 수송 평균, Closed는 지정 수송 또는 NaN일 때 0, Neumann/Fixed는 두 번째 점 복사로 처리한다(69–85). Angleconstant/Gradient 분기는 각도를 다른 루틴에서 정한다는 주석만 있다(86–89). 원문: `QS0=TRANSP.QS;` (60), `if ~COAST.cyclic` (61), `if COAST.BNDgroyne(COAST.i_mc,1)~=0` (62), `side=2;` (64), `idgroyne=find(GROYNE.idcoast(:,side)==COAST.i_mc);` (65), `if (~isempty(idgroyne))` (66), `else` (69), `if strcmpi(TRANSP.boundaryconditionstart{1},'Periodic') && ~COAST.cyclic` (70), `TRANSP.QS(:,1)=(QS0(:,end-1)+QS0(:,2))/2;` (72), `if strcmpi(TRANSP.boundaryconditionstart{1},'Closed') && ~COAST.cyclic` (74), `if isnan(TRANSP.boundaryconditionstart{2})` (76), `TRANSP.QS(:,1)=0;` (77), `else` (78), `TRANSP.QS(:,1)=TRANSP.boundaryconditionstart{2};` (79), `if (strcmpi(TRANSP.boundaryconditionstart{1},'Neumann') \|\| strcmpi(TRANSP.boundaryconditionstart{1},'Fixed')) && ~COAST.cyclic` (82), `TRANSP.QS(:,1)=TRANSP.QS(:,2);` (84), `if (strcmpi(TRANSP.boundaryconditionstart{1},'Angleconstant') \|\| strcmpi(TRANSP.boundaryconditionstart{1},'Gradient')) && ~COAST.cyclic` (86). |
| 92–122 | 시작 시 1행 함수·61행 비주기 참 분기 안. 끝점 돌제가 있으면 side=1로 검색하지만 내부 수송 대입은 주석 처리되어 있다(92–98). 돌제가 없는 else에서 Periodic·Closed·Neumann/Fixed를 시작점과 대응되게 처리한다(99–115). Angleconstant/Gradient 분기는 get_coastline_orientation에 관한 주석만 포함한다(116–119). 바깥 조건과 함수가 끝난다(120–122). 원문: `if COAST.BNDgroyne(COAST.i_mc,2)~=0` (92), `side=1;` (94), `idgroyne=find(GROYNE.idcoast(:,side)==COAST.i_mc);` (95), `if (~isempty(idgroyne))` (96), `else` (99), `if strcmpi(TRANSP.boundaryconditionend{1},'Periodic') && ~COAST.cyclic` (100), `TRANSP.QS(:,end)=(QS0(:,end-1)+QS0(:,2))/2;` (102), `if strcmpi(TRANSP.boundaryconditionend{1},'Closed') && ~COAST.cyclic` (104), `if isnan(TRANSP.boundaryconditionend{2})` (106), `TRANSP.QS(:,end)=0;` (107), `else` (108), `TRANSP.QS(:,end)=TRANSP.boundaryconditionend{2};` (109), `if (strcmpi(TRANSP.boundaryconditionend{1},'Neumann') \|\| strcmpi(TRANSP.boundaryconditionend{1},'Fixed')) && ~COAST.cyclic` (112), `TRANSP.QS(:,end)=TRANSP.QS(:,end-1);` (114), `if (strcmpi(TRANSP.boundaryconditionend{1},'Angleconstant') \|\| strcmpi(TRANSP.boundaryconditionend{1},'Gradient')) && ~COAST.cyclic` (116). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–19: 입력 설명에 WAVE.HStdp가 있으나 함수 시그니처에는 WAVE 인수가 없다(1).
- 66–68·96–98: idgroyne가 비어 있지 않은 분기의 수송 대입은 모두 주석이다.
- 86–89·116–119: Angleconstant/Gradient 조건 내부에는 실행문이 없다. get_coastline_orientation는 주석에서만 언급된다.
