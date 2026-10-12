---
file: models/ShorelineS/raw/source_code/shorelines/functions/interpNANs.m
lines: 104
sha256: f1bddbd1fdd61eb68f6a74b38c5643b77795034b3312c6be009a6a29955da334
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# interpNANs.m — 판독 구간 기록

구간은 1행부터 104행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 함수 시그니처(1). 스칼라(scalar) 데이터의 NaN을 보간(interpolation)한다는 설명과 예시(2–12). 주석은 내부 보간을 linear로, 외삽(extrapolation)을 nearest 또는 linear로 지정한다(8–9). 원문: `function [data2]=interpNANs(data,useextrapolation)` (1). |
| 13–40 | 시작 시 1행 interpNANs 함수 안. 2020년 저작권·연락처, LGPL 2.1 이상·무보증 안내와 빈 줄(13–40). |
| 41–58 | 시작 시 1행 interpNANs 함수 안. 두 번째 입력이 없으면 외삽 기본값을 nearest로 둔다(41–43). 열 수가 행 수와 2보다 모두 크면 data를 전치(transpose)한다(46–49). 단일 열이면 1부터 length(data)까지를 x로 사용하고, 그렇지 않으면 첫 열을 x, 둘째 열을 y로 사용한다(51–57). 원문: `if nargin<2` (41), `useextrapolation='nearest';  %<- use extrapolation if it is set to 1` (42), `rotate=0;` (45), `if max(size(data,1),2)<size(data,2)` (46), `rotate=1;` (47), `data=data';` (48), `if size(data,2)==1` (51), `x = [1:length(data)]';` (52), `y = data;` (53), `else` (54), `x = data(:,1);` (55), `y = data(:,2);` (56). [10-12 전수 검증 정정] |
| 59–73 | 시작 시 1행 interpNANs 함수 안. x를 정렬하고 같은 순서로 y를 재배열한다(60–61). 간격 계수 eps는 1e-6이다(62). 인접 x가 같으면 다음 x에 eps를 더한다(63–67). y의 비-NaN 표본만 x2·y2로 추출한다(69–72). 원문: `[x,ids]  = sort(x);` (60), `y        = y(ids);` (61), `eps      = 1e-6;` (62), `for tt=1:length(x)-1` (63), `if x(tt)==x(tt+1)` (64), `x(tt+1)=x(tt+1)+eps;` (65), `id = find(~isnan(y));` (70), `x2 = x(id);` (71), `y2 = y(id);` (72). |
| 74–94 | 시작 시 1행 interpNANs 함수 안. NaN이 없으면 y2를 그대로 쓴다(74–75). 그렇지 않으면 유효 표본이 둘 이상일 때 linear 외삽을 선택하거나, linear 보간 후 nearest 외삽을 적용한다(77–86). 유효 표본이 하나이면 같은 값을 반복한다(87–88). 유효 표본이 없으면 전부 NaN으로 만든다(89–92). 원문: `if length(id)==length(x)` (74), `ynew = y2;` (75), `else` (76), `if length(x2)>1` (77), `if strcmpi(useextrapolation,'linear')` (78), `ynew = interp1(x2,y2,x,'linear','extrap');` (79), `else` (80), `y3 = interp1(x2,y2,x,'linear');` (81), `id = find(~isnan(y3));` (82), `x2 = x(id);` (83), `y2 = y3(id);` (84), `ynew = interp1(x2,y2,x,'nearest','extrap');` (85), `elseif length(x2)==1` (87), `ynew=repmat(y2,size(x));` (88), `else` (89), `ynew=nan(size(x));` (91). |
| 95–104 | 시작 시 1행 interpNANs 함수 안. 앞선 전치 처리 후 data가 두 열이면 정렬한 x와 ynew를 결합한다(95–96). 그 외 입력은 ynew만 반환한다(97–99). 앞서 전치한 경우 출력도 전치한다(101–103). 함수 종료(104). 원문: `if size(data,2)==2` (95), `data2 = [x,ynew];` (96), `else` (97), `data2 = [ynew];` (98), `if rotate==1` (101), `data2 = data2';` (102). [10-12 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 42: 기본값은 문자열 nearest이며, 같은 행 주석은 값이 1일 때 외삽한다고 적는다.
- 60–67·95–99: 출력은 정렬한 x 순서를 사용한다. 입력 순서로 되돌리는 인덱스 대입은 없다.
- 63–67: 중복 보정은 인접 두 x가 같은 경우에만 다음 값에 1e-6을 더한다. 보정 후 재정렬하는 문장은 없다.
- 78–85: linear와 일치하지 않는 useextrapolation 값은 모두 nearest 외삽 경로로 들어간다.
