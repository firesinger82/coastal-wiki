---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_foreshore_orientation.m
lines: 140
sha256: 322f7d4ed214ce027d7dd378999149c1acfd6ce661bd8c1ce6870912f993b642
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_foreshore_orientation.m — 판독 구간 기록

구간은 1행부터 140행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–45 | 함수 시그니처 `function [COAST]=get_foreshore_orientation(COAST)` (1). 전빈(foreshore)·하부 해안 전면(lower shoreface) 방향의 입력·출력 필드 주석(4–17). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(18–45). |
| 46–75 | 파일 입력 조건 `if ischar(COAST.PHIf0)   % INPUT: from file` (47), load로 COAST.PHIf0 교체(51). 빈 입력·네 열 임시표 조건 `if isempty(COAST.PHIf0) \|\| size(COAST.PHIf0,2)==4 % INPUT: at t=0` (54). nl·수송점 열 벡터 준비(60–62). 순환 조건 `if COAST.cyclic` (63), 3회 반복 방향의 get_smoothdata·360도 제한·인덱스 `PHIf=get_smoothdata(repmat(COAST.PHIc(2:end-1),[1 3]),'angle',1);` (65); `PHIfsmooth=mod(PHIf(nl-1:2*nl-4),360);` (66); `idx=[2:nl-1];` (67); `PHIfsmooth=mod(PHIf(nl-1:2*nl-3),360);` (68); `idx=[2:nl];` (69). 비순환 `else` (70)의 평활화·360도 제한·범위 `PHIf=get_smoothdata(COAST.PHIc,'angle',1);` (71); `PHIfsmooth=mod(PHIf,360);` (72); `idx=[1:nl];` (73). 추가 원문: `nl=length(COAST.PHIc);` (60). `xq=COAST.xq(:);` (61). `yq=COAST.yq(:);` (62). [10-12 전수 검증 보완] |
| 76–86 | 시작 시 54행 초기 방향 준비 참 분기 안. 첫 구간 조건 `if COAST.i_mc==1` (77), 수송점 좌표와 평활화 방향을 중복한 네 열 표 생성(78). 뒤 구간 `else` (79)은 네 열 표를 아래로 연결(80). 마지막 구간 조건 `if COAST.i_mc==COAST.n_mc` (82)이면 첫 세 열만 유지(83). 바깥 조건 종료(85). 추가 원문: `COAST.PHIf0=[xq(idx),yq(idx),PHIfsmooth(:),PHIfsmooth(:)];` (78). `COAST.PHIf0=[COAST.PHIf0;[xq(idx),yq(idx),PHIfsmooth(:),PHIfsmooth(:)]];` (80). `COAST.PHIf0=COAST.PHIf0(:,1:3);` (83). [10-12 전수 검증 보완] |
| 87–104 | 셀 입력·길이 조건 `if iscell(COAST.PHIf0) && length(COAST.PHIf0)>=2 % INPUT: at t=0` (87). 평활화 방법·범위 복사(90–91). 순환 조건 `if COAST.cyclic` (92), 반복 방향의 코사인·사인 평활화와 가운데 방향 `cPHIf=smoothdata(cosd(repmat(COAST.PHIc,[1 3])),smoothmethod,smoothrange);` (94); `sPHIf=smoothdata(sind(repmat(COAST.PHIc,[1 3])),smoothmethod,smoothrange);` (95); `PHIf=atan2d(sPHIf(nl+1:2*nl),cPHIf(nl+1:2*nl));` (96). 비순환 `else` (97)의 평활화·방향 `cPHIf=smoothdata(cosd(COAST.PHIc),smoothmethod,smoothrange);` (98); `sPHIf=smoothdata(sind(COAST.PHIc),smoothmethod,smoothrange);` (99); `PHIf=atan2d(sPHIf,cPHIf);` (100). 360도 제한 `PHIfsmooth=mod(PHIf,360);` (102), COAST.PHIf 복사(103). 추가 원문: `nl=length(COAST.PHIc);` (93). [10-12 전수 검증 보완] |
| 105–116 | 시작 시 87행 셀 입력 참 분기 안. 첫 구간 조건 `if COAST.i_mc==1` (105), 방법·범위·좌표·방향을 다섯 셀로 저장(106). 뒤 구간 `else` (107)의 좌표·방향 연결(108–110). 마지막 구간 조건 `if COAST.i_mc==COAST.n_mc` (112)에서 세 열 수치표로 바꾼다(113). 바깥 조건 종료(115). 추가 원문: `COAST.PHIf0={COAST.PHIf0{1},COAST.PHIf0{2},COAST.xq(:),COAST.yq(:),PHIfsmooth(:)};` (106). `COAST.PHIf0{3}=[COAST.PHIf0{3};COAST.xq(:)];` (108). `COAST.PHIf0{4}=[COAST.PHIf0{4};COAST.yq(:)];` (109). `COAST.PHIf0{5}=[COAST.PHIf0{5};PHIfsmooth(:)];` (110). `COAST.PHIf0=[COAST.PHIf0{3},COAST.PHIf0{4},COAST.PHIf0{5}];` (113). [10-12 전수 검증 보완] |
| 117–140 | 고정 스칼라 조건 `if isscalar(COAST.PHIf0)` (117), 수송점 수만큼 방향 확장 `COAST.PHIf=repmat(COAST.PHIf0,[1,length(COAST.xq)]);` (120). 표 입력 조건 `if ~isscalar(COAST.PHIf0) && ~iscell(COAST.PHIf0)` (125), 세 열 전치 추출(126–128). 순환 조건 `if COAST.cyclic` (132)의 weighted_distance 보간 `[~,PHIf1,~]=get_interpolation_on_grid('weighted_distance',COAST.xq,COAST.yq,PHIf_x,PHIf_y,[],PHIf0);` (133). 비순환 `else` (134)의 alongshore_mapping 보간 `[~,PHIf1,~]=get_interpolation_on_grid('alongshore_mapping',COAST.xq,COAST.yq,PHIf_x,PHIf_y,[],PHIf0);` (135). 결과 PHIf 복사(137). 조건·함수 종료(138–140). 추가 원문: `PHIf_x=COAST.PHIf0(:,1)';` (126). `PHIf_y=COAST.PHIf0(:,2)';` (127). `PHIf0=COAST.PHIf0(:,3)';` (128). [10-12 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·47–137: 입력 주석은 phif0 소문자를 적는다. 실행문은 PHIf0를 사용한다.
- 66–69: 순환 경로는 PHIfsmooth와 idx를 각각 두 번 대입한다. 첫 대입 결과는 다음 대입으로 덮어쓴다.
- 54·78–83: 네 열 표의 네 번째 열은 세 번째 열과 같은 평활화 방향이다. 마지막 구간에서 네 번째 열을 제거한다.
- 15–16·126–137: 출력 주석은 COAST.PHIf_x·PHIf_y를 적는다. 실행문은 지역 PHIf_x·PHIf_y만 만들며 해당 COAST 필드에 대입하지 않는다.
- 54·87·117·125: 입력 유형 처리 조건은 서로 독립된 if 문장이다.
