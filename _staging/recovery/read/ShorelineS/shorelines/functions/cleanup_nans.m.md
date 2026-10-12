---
file: models/ShorelineS/raw/source_code/shorelines/functions/cleanup_nans.m
lines: 122
sha256: b3fc5715effd84178b9aead90e492f40af44ea47db83a1777cb7ab008f1bd0f7
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# cleanup_nans.m — 판독 구간 기록

구간은 1행부터 122행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–45 | 함수 시그니처 `function [COAST,i_diff]=cleanup_nans(COAST)` (1). NaN을 포함한 해안선 좌표 정리 목적·입출력 필드와 i_diff 설명(2–17). 저작권·연락처·LGPL 2.1 이상·무보증 및 빈 줄(18–45). |
| 46–60 | i=1·i_diff=0 초기화(46·48). 좌표 중복 허용치 `eps=0.1;` (47). 루프 `while i<=length(COAST.x_mc)` (49). 시작 NaN·짧은 시작 구간 제거 조건 `if i<=3 && isnan(COAST.x_mc(i))` (53). x_mc·y_mc를 i+1:end로 자른다(54–55). 내부 조건 `if i~=1` (56), 변경 수 계산 `i_diff=i_diff-1;                            % administrate that 1 element is removed!` (57). i를 1로 되돌린다(59). 자료 선택·계산·호출의 원문은 `COAST.x_mc=COAST.x_mc(i+1:end);` (54); `COAST.y_mc=COAST.y_mc(i+1:end);` (55). |
| 61–78 | 시작 시 49행 while 루프·53행 if/elseif 연쇄 안. 끝 NaN 분기 `elseif i>=length(COAST.x_mc)-2 && isnan(COAST.x_mc(i))` (64). 좌표 선택식은 `COAST.x_mc=COAST.x_mc(1:i-1);` (65). y 좌표 선택식은 `COAST.y_mc=COAST.y_mc(1:i-1);` (66). 좌표를 자른 뒤 내부 조건 `if i~=length(COAST.x_mc)` (67), 변경 수 계산 `i_diff=i_diff-1;                            % administrate that 1 element is removed!` (68), i=1(70). 연속 NaN 분기 `elseif i>1 && i<=length(COAST.x_mc)-1 && isnan(COAST.x_mc(i)) && isnan(COAST.x_mc(i+1))` (74). 좌표에서 i번째 위치를 제거하고 i=1로 되돌린다(75–77). 자료 선택·계산·호출의 원문은 `COAST.x_mc=[COAST.x_mc(1:i-1),COAST.x_mc(i+1:end)];` (75); `COAST.y_mc=[COAST.y_mc(1:i-1),COAST.y_mc(i+1:end)];` (76). [10-12 전수 검증 보완] |
| 79–94 | 시작 시 49행 while 루프·53행 if/elseif 연쇄 안. 한 점 구간 제거 조건 `elseif i<=length(COAST.x_mc)-1 && isnan(COAST.x_mc(i)) && isnan(COAST.x_mc(i+2))` (81). 좌표의 i:i+1을 제거한다(82–83). 변경 수 계산 `i_diff=i_diff-1;                            % administrate that 1 element is removed!` (84), i=1(85). 두 점 구간 제거 조건 `elseif i<=length(COAST.x_mc)-1 && isnan(COAST.x_mc(i)) && isnan(COAST.x_mc(i+3))` (89). 좌표의 i:i+2를 제거한다(90–91). 변경 수 계산 `i_diff=i_diff-1;                            % administrate that 1 element is removed!` (92), i=1(93). 자료 선택·계산·호출의 원문은 `COAST.x_mc=[COAST.x_mc(1:i-1),COAST.x_mc(i+2:end)];` (82); `COAST.y_mc=[COAST.y_mc(1:i-1),COAST.y_mc(i+2:end)];` (83); `COAST.x_mc=[COAST.x_mc(1:i-1),COAST.x_mc(i+3:end)];` (90); `COAST.y_mc=[COAST.y_mc(1:i-1),COAST.y_mc(i+3:end)];` (91). |
| 95–114 | 시작 시 49행 while 루프·53행 if/elseif 연쇄 안. 인접 중복점 조건 `elseif i<=length(COAST.x_mc)-1 && hypot(COAST.x_mc(i+1)-COAST.x_mc(i),COAST.y_mc(i+1)-COAST.y_mc(i))<eps` (98). i+1 좌표를 제거하고 i=1(99–101). 한 점을 사이에 둔 중복점 조건 `elseif i<=length(COAST.x_mc)-2 && hypot(COAST.x_mc(i+2)-COAST.x_mc(i),COAST.y_mc(i+2)-COAST.y_mc(i))<eps && ~isnan(COAST.x_mc(i+1))` (106). i+2 좌표를 제거하고 i=1(107–109). 기본 분기 `else` (111), 인덱스 증가 `i=i+1;` (112). 조건 연쇄·while 종료(113–114). 자료 선택·계산·호출의 원문은 `COAST.x_mc=[COAST.x_mc(1:i),COAST.x_mc(i+2:end)];` (99); `COAST.y_mc=[COAST.y_mc(1:i),COAST.y_mc(i+2:end)];` (100); `COAST.x_mc=[COAST.x_mc(1:i+1),COAST.x_mc(i+3:end)];` (107); `COAST.y_mc=[COAST.y_mc(1:i+1),COAST.y_mc(i+3:end)];` (108). |
| 115–122 | 구간 수 계산 `COAST.n_mc=length(find(isnan(COAST.x_mc)))+1;` (116). try 블록(119) 안에서 `[COAST]=get_transportpoints(COAST);` (120)로 수송점(transport point)을 재구성한다. try·함수 종료(121–122). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 64–68: 끝 NaN 분기의 i~=length(COAST.x_mc) 검사는 좌표를 1:i-1로 자른 다음에 수행한다.
- 81·89: 조건은 i<=length(COAST.x_mc)-1을 검사하면서 각각 x_mc(i+2)와 x_mc(i+3)를 참조한다.
- 16·54–57·65–68·75–76·82–84·90–92·99–100·107–108: i_diff 설명은 좌표 점 수 변화를 적지만 실행문은 일부 분기에서만 1을 뺀다. 연속 NaN과 중복점 제거 분기에는 i_diff 대입이 없다.
- 119–121: try 블록에는 get_transportpoints 호출이 있고 catch 절은 없다.
