---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_gridsize.m
lines: 60
sha256: cec8a554829232c8e8d58a8a12d6d3501a5f5a9c178621f375039326007cfee6
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_gridsize.m — 판독 구간 기록

구간은 1행부터 60행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | 함수 시그니처 `function [ds0i,ds0i_center]=get_gridsize(x,y,ds0)` (1). 스칼라 또는 xg·yg·ds0 세 열 표의 격자 크기(grid size) 설명과 출력 크기 예시(4–13). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(14–41). |
| 42–51 | 스칼라 조건 `if isscalar(ds0)` (42), x 길이만큼 확장 `ds0i=repmat(ds0,[1,length(x)]);` (43). 표 입력 `else` (44)는 세 열 추출(45–47), weighted_distance 보간 호출 `ds0i=get_interpolation_on_grid('weighted_distance',x,y,xg,yg,ds1);` (48). 인접 격자 크기 평균 `ds0i_center=0.5*(ds0i(1:end-1)+ds0i(2:end));` (50). |
| 52–60 | NaN 위치 검색(53). 연속 NaN의 앞 위치를 제외한 인덱스 `idnotnan=setdiff([1:length(ds0i_center)],idnan(diff(idnan)==1));` (54), 중심 배열에서 해당 위치만 유지(55). 두 출력을 행 벡터로 전환(58–59). 함수 종료(60). 추가 원문: `idnan=find(isnan(ds0i_center));` (53). `ds0i_center=ds0i_center(idnotnan);` (55). `ds0i=ds0i(:)';` (58). `ds0i_center=ds0i_center(:)';` (59). [10-12 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1–2·5–12: 함수 주석의 출력 이름과 좌표 설명은 실행 시그니처의 ds0i·ds0i_center 및 입력 x·y와 다르다.
- 50·54–55: ds0i_center는 인접 평균으로 만든 뒤 연속 NaN의 앞 위치를 제거한다. 같은 위치 제거를 ds0i에 적용하는 문장은 없다.
