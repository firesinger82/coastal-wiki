---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_aggregatedtimeseries.m
lines: 109
sha256: 18e84ee802c1e9ef853f50fadba26df9bf81d09569fa429573d7ddf8455ef315
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_aggregatedtimeseries.m — 판독 구간 기록

구간은 1행부터 109행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | 함수 시그니처 `function [D]=get_aggregatedtimeseries(D,TIME)` (1). 조건 누락을 피하기 위한 파랑 시계열(time series) 집계 목적(4–5). 저작권·연락처·LGPL 2.1 이상·무보증 및 빈 줄(7–35). 시간 간격별 평균으로 속도를 높인다는 주석(36–37). |
| 38–50 | 집계 진입 조건 `if ~isempty(D(1).timenum) && TIME.tc==0` (38). 방향 필드 Dir·PHIequi·PHIf와 스칼라 Hs·Tp·c1·c2·h0·fshape·QSoffset 목록(39–40). 스칼라 지수·일 단위 시간 간격 `sfac = [2.0 1.0 1.0 1.0 1.0 1.0 1.0]; %scaling factors for scalars` (41); `timestep = TIME.dt*365;` (42). 자료 루프 `for kk=1:length(D)` (44), 간격·중앙값·집계 인자·집계 간격·출력 수 `DT=diff(D(kk).timenum);` (45); `DT0=median(DT);` (46); `factor=max(ceil(timestep/DT0),1);` (47); `DT1=factor*DT0;` (48); `ttend=min(ceil((D(kk).timenum(end)-D(kk).timenum(1))/DT1)+1,length(D(kk).timenum));` (49). |
| 51–75 | 시작 시 38행 진입 참 분기·44행 kk 루프 안. 집계 인자 조건 `if factor>2` (51), 빈 임시 구조체·이전 범위 초기값 1(52–53). 출력 시간 루프 `for tt=1:ttend` (54), 구간 시작·끝 `tstart=D(kk).timenum(1)+(tt-1)*DT1;` (55); `tend=D(kk).timenum(1)+tt*DT1;` (56). 마지막 출력 조건 `if tt==ttend` (57)의 tend=inf(58). 등간격 조건 `if max(DT)==min(DT)` (61), 중심 인덱스 범위 `ttrange=unique(min(max((tt-1)*factor+[-floor((factor-1)/2):ceil((factor-1)/2)],1),length(D(kk).timenum)));` (63). 비등간격 `else` (64) 경로의 시간 마스크 `ttrange=find(D(kk).timenum>=tstart & D(kk).timenum<tend);` (67). 빈 범위 조건 `if isempty(ttrange)` (69)은 이전 범위 마지막 값 복사(70), ttrange0 갱신(72), 출력 시각 `Dtmp.timenum(tt,1) = D(kk).timenum(1)+DT1*(tt-1);` (74). |
| 76–93 | 시작 시 38행 참 분기·44행 kk 루프·51행 factor>2 참 분기·54행 tt 루프 안. 스칼라 루프 `for jj=1:length(fldsc)` (77), 필드 조건 `if isfield(D(kk),fldsc{jj})` (78), 지수 평균 `Dtmp.(fldsc{jj})(tt,1) = (mean(D(kk).(fldsc{jj})(ttrange).^sfac(jj))).^(1./sfac(jj));` (79). 방향 루프 `for jj=1:length(fldvc)` (83), 필드 조건 `if isfield(D(kk),fldvc{jj})` (84), HSfac 복사(85), 방향 사인·코사인 열 벡터와 파고 제곱합으로 나눈 항의 산술평균·각도 `sdir0=sind(D(kk).(fldvc{jj})(ttrange)); sdir0 = sdir0(:);` (86); `cdir0=cosd(D(kk).(fldvc{jj})(ttrange)); cdir0 = cdir0(:);` (87); `sdir1=mean(sdir0.*D(kk).Hs(ttrange).^HSfac ./ sum(D(kk).Hs(ttrange).^HSfac) );` (88); `cdir1=mean(cdir0.*D(kk).Hs(ttrange).^HSfac ./ sum(D(kk).Hs(ttrange).^HSfac) );` (89); `Dtmp.(fldvc{jj})(tt,1) = mod(atan2d(sdir1,cdir1),360);` (90). tt 루프 종료(93). [10-12 전수 검증 정정] |
| 94–109 | 시작 시 38행 참 분기·44행 kk 루프·51행 factor>2 참 분기 안. 집계 시각 복사(95). 스칼라 루프 `for jj=1:length(fldsc)` (96)·필드 조건 `if isfield(D(kk),fldsc{jj})` (97)의 결과 복사(98). 방향 루프 `for jj=1:length(fldvc)` (101)·필드 조건 `if isfield(D(kk),fldvc{jj})` (102)의 결과 복사(103). 분기·루프·함수 종료(104–109). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 38: 전체 집계 진입 여부는 D(1).timenum과 TIME.tc만 검사한다.
- 51: factor가 1 또는 2이면 해당 자료는 집계하지 않는다.
- 84–90: 방향 필드 존재를 확인한 뒤 D(kk).Hs를 사용한다. 이 블록에는 Hs 존재 검사와 파고 제곱합의 양수 검사가 없다.
- 45–49: 시간 간격 중앙값을 분모로 사용하며 빈 DT 또는 DT0=0을 따로 처리하는 분기는 없다.
