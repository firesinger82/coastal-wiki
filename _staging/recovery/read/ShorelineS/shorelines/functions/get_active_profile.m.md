---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_active_profile.m
lines: 97
sha256: 7922c5f8142b097ace9ea2bef50180fed2783b3a6c2c6941de07291557589446
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_active_profile.m — 판독 구간 기록

구간은 1행부터 97행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–46 | 함수 시그니처 `function [COAST] = get_active_profile(COAST)` (1). 공간적으로 변하거나 고정된 활성 단면(active profile) 높이를 얻는 목적과 좌표·높이 입력 및 출력 필드(4–18). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(19–46). |
| 47–65 | 문자 입력 조건 `if ischar(COAST.h0input)   % INPUT: from file` (47). 높이 표 load 호출(51), COAST.h0input의 세 열을 전치하여 x·y·높이에 대입(52–54). 빈 구조체 var1·var2 생성, var2.h0_mc 복사(58–60). weighted_distance 보간 호출 `[~,var2i,~]=get_interpolation_on_grid('weighted_distance',COAST.x,COAST.y,h0_x,h0_y,var1,var2);` (61), 높이·좌표를 보간 결과와 현재 격자로 복사(62–64). 추가 원문: `h0input=load(COAST.h0input);` (51). `h0_x=COAST.h0input(:,1)';` (52). `h0_y=COAST.h0input(:,2)';` (53). `h0=COAST.h0input(:,3)';` (54). [10-12 전수 검증 보완] |
| 66–87 | 시작 시 47행 if/elseif 연쇄 안. 스칼라 분기 `elseif isscalar(COAST.h0input)` (66)는 현재 좌표 복사(69–70), 전체 격자 확장 `h0=repmat(COAST.h0input,[1,COAST.n]);` (71). 수치 배열 분기 `elseif isnumeric(COAST.h0input)  % array from input structure` (73)는 세 열 전치(74–76), 빈 구조체 생성·h0_mc 복사(80–82), weighted_distance 보간 `[~,var2i,~]=get_interpolation_on_grid('weighted_distance',COAST.x,COAST.y,h0_x,h0_y,var1,var2);` (83), 결과와 현재 좌표 복사(84–86). 추가 원문: `h0_x=COAST.h0input(:,1)';` (74). `h0_y=COAST.h0input(:,2)';` (75). `h0=COAST.h0input(:,3)';` (76). [10-12 전수 검증 보완] |
| 88–97 | 시작 시 47행 if/elseif 연쇄 안. 기타 분기 `else` (88)는 Invalid active profile input 오류(89). COAST.h0·h0_x·h0_y에 결과 복사(93–95). 함수 종료(97). [10-12 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 47·51–54: 문자 입력 경로는 load 결과를 지역 h0input에 저장한다. 이어지는 세 열 추출은 지역 h0input 대신 COAST.h0input을 참조한다.
- 68: 고정 높이 분기의 입력 예시 주석은 COAST.PHIf0=10을 적는다.
- 73–76: 수치 배열 분기에는 세 열 추출 앞 열 수 검사가 없다.
