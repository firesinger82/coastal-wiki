---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_coastline_orientation.m
lines: 112
sha256: c798003fc3d3de9ff7450a4db860eb0c050f81726e7d390a30dc144d99a248e2
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_coastline_orientation.m — 판독 구간 기록

구간은 1행부터 112행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | 함수 시그니처 `function [COAST]=get_coastline_orientation(COAST)` (1). 해안선(shoreline)·수송점 좌표와 순환 여부 입력, 방향·경계 방향·초기 방향 출력 설명(4–20). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(21–48). |
| 49–64 | 수송점 및 해안선점 방향 `COAST.PHIc=mod(360.0-atan2d(diff(COAST.y),diff(COAST.x)),360);` (51); `COAST.PHIcxy=mod(360.0-atan2d(diff(COAST.yq),diff(COAST.xq)),360);` (54). 순환 조건 `if COAST.cyclic` (57)이면 양끝에 마지막·첫 내부 방향 연결(59). 비순환 `else` (61)이면 PHIcxy의 양끝 방향 연결(63). 추가 원문: `COAST.PHIc=[COAST.PHIc(end),COAST.PHIc,COAST.PHIc(1)];` (59). `COAST.PHIc=[COAST.PHIcxy(1),COAST.PHIc,COAST.PHIcxy(end)];` (63). [10-12 전수 검증 보완] |
| 65–85 | 시작 시 57행 if의 61행 비순환 else 안. 시작 경계 Angleconstant·Gradient 조건 연속 행 `if strcmpi(COAST.boundaryconditionstart{1},'Angleconstant') \|\| ...` (68); `strcmpi(COAST.boundaryconditionstart{1},'Gradient')` (69). 미정 경계 조건 `if isnan(COAST.boundaryconditionstart{2})` (70)는 현재 방향 저장(71), `else` (72)는 저장 방향 적용(73). 끝 경계 조건 연속 행 `if strcmpi(COAST.boundaryconditionend{1},'Angleconstant') \|\| ...` (76); `strcmpi(COAST.boundaryconditionend{1},'Gradient')` (77), 미정 조건 `if isnan(COAST.boundaryconditionend{2})` (78)는 현재 끝 방향 저장(79), `else` (80)는 저장 방향 적용(81). 경계·비순환 조건 종료(82–84). |
| 86–104 | 초기 시작 방향 조건 `if isnan(COAST.PHIc0bnd(1))` (87)은 PHIc0bnd(1) 복사(88). 초기 끝 방향 조건 `if isnan(COAST.PHIc0bnd(2))` (90)은 PHIc0bnd(2) 복사(91). 격자 변화·병합 조건 `if COAST.gridchange==1 \|\| COAST.mergegrid==1` (93)은 PHIcxy0에 현재 방향 복사(94), 이전 방향 필드 조건 `if isfield(COAST,'PHIcxy1_mc')` (95), method 설정(96), try 안 보간 호출 `[~,COAST.PHIcxy0]=get_interpolation_on_grid(method,COAST.x,COAST.y,COAST.x1_mc,COAST.y1_mc,'',COAST.PHIcxy1_mc);` (98). try·필드 조건 종료(99–100). 격자 고정 `else` (101)은 get_one_polygon으로 이전 방향 구간 추출(102). 자료 선택·계산·호출의 원문은 `COAST.PHIcxy0=get_one_polygon(COAST.PHIcxy1_mc,COAST.i_mc);` (102). |
| 105–112 | 평활화 방향은 근해 굴절(refraction)에만 쓴다는 주석(105–107). PHIcs=PHIc 복사(108). 평활화 조건 `if COAST.smoothrefrac>0` (109), 상한 1을 둔 get_smoothdata 호출 `COAST.PHIcs=get_smoothdata(COAST.PHIc,'Angle',min(COAST.smoothrefrac,1));` (110). 함수 종료(112). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 68–83: 경계 방향을 고정·재사용하는 처리는 비순환 경로 안에서만 수행한다.
- 95–99·101–102: 격자 변화 경로는 PHIcxy1_mc 존재를 검사하고 try 안에서 보간한다. 격자 고정 경로는 이 필드를 조건 없이 get_one_polygon에 전달한다.
- 97–99: 보간 try 블록에는 catch 절이 없다.
