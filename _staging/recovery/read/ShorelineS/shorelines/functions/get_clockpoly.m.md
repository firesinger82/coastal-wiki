---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_clockpoly.m
lines: 97
sha256: c22f52841cc234c702171ec57dc2d5c360861ffd2037f2ae471de4a64e656e3d
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_clockpoly.m — 판독 구간 기록

구간은 1행부터 97행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–45 | 함수 시그니처 `function rot=get_clockpoly(x,y)` (1). 단순 다각형(simple polygon)의 점 순서를 판별한다는 주석(4–6). 반환값 주석은 시계 방향 1·반시계 방향 -1·미정 0이며 자기 교차 형상에 대한 설명도 있다(7–16). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(18–45). |
| 46–58 | x·y를 열 벡터로 변환(46–47). 중심 x `xc=mean(x);` (48), Rot=0(49). 비어 있지 않은 좌표 조건 `if ~isempty(x) && ~isempty(y)` (50). 끝과 처음을 이은 차분 `xd=diff([x;x(1)]);` (52); `yd=diff([y;y(1)]);` (53). 닫힌 끝점 허용치 조건 `if abs(x(end)-x(1))<1e-8 && abs(y(end)-y(1))<1e-8` (54)에서 마지막 차분을 첫 차분으로 복사(55–56). 추가 원문: `x=x(:);` (46). `y=y(:);` (47). [10-12 전수 검증 보완] |
| 59–72 | 시작 시 50행 비어 있지 않은 좌표 참 분기 안. 수직 변 마스크 `mark=(xd==0);` (59), 해당 xd를 NaN으로 설정(60). 중심선 교차 매개변수·범위 마스크·y좌표 `a=(xc-x)./xd;` (61); `mark2=a<0 \| a>1;` (62); `yc=y+a.*yd;` (63). 교차하지 않는 평행 변·범위 밖 변은 -inf(64–65). 중심선 위 변 마스크·최고 y `mark = (mark & xc==x);` (66); `yc(mark)=y(mark)+max(0,yd(mark)); % on the line x=xc -> take maximum` (67), 전체 최고 교차·인덱스 `ycm=max(yc); % highest crossing of x=xc somewhere between i and i+1` (69); `i=find(yc==ycm);` (70). 대체 검색은 주석 처리(71). 자료 선택·계산·호출의 원문은 `yc(mark & xc~=x)=-inf; % parallel to x=xc -> not crossing -> remove` (64); `yc(mark2)=-inf; % crossing outside range -> remove` (65). 추가 원문: `xd(mark)=NaN;` (60). [10-12 전수 검증 보완] |
| 73–84 | 시작 시 50행 좌표 참 분기 안. Rot=0(73). 오른쪽 진행 조건 `if all(xd(i)>=0) && any(xd(i)>0) % going right` (74)은 Rot=1(75). 왼쪽 조건 `elseif all(xd(i)<=0) && any(xd(i)<0) % going left` (76)은 Rot=-1(77). 양방향 `elseif any(xd(i)>0) && any(xd(i)<0) % going both left and right` (78)과 수직 `else, % xd=0 % going straight up or down` (80) 경로는 미정 주석만 있다(79·81). 조건 종료(82–83). |
| 85–97 | 출력 없는 호출 조건 `if nargout==0` (85), `switch Rot` (86) 선택의 `case -1` (87); `case 0` (89); `case 1` (91)에 따라 방향 이름 로그(88·90·92). 출력 있는 `else` (94)는 rot=Rot(95). 조건·함수 종료(96–97). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 54: 닫힌 다각형 판정의 x·y 허용치는 각각 1e-8로 고정되어 있다.
- 59–61·74–80: 수직 변의 xd를 NaN으로 바꾼다. 최종 방향 판정은 이 xd의 부등식 조건을 사용한다.
