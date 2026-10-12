---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_landboundary.m
lines: 112
sha256: 256cbaafc2d3f7c105d495eeea88258aa91193c83ab52ed6b72e7f94daef7226
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_landboundary.m — 판독 구간 기록

구간은 1행부터 112행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–45 | 함수 시그니처는 `function [LDB]=get_landboundary(LDBfilename,closepoly)` (1). 육상 경계(land boundary) 파일과 여러 다각형(polygon) 판독을 설명한다(2–17). closepoly 주석은 기본 0, 열린 선을 만드는 -1, 닫힌 다각형을 만드는 1을 설명한다(9–12). 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(18–45). |
| 46–76 | 시작 시 1행 get_landboundary 함수 안. LDB를 비우고 jj·linenr를 0으로 초기화한다(46·48–49). 결측값 표식 기본값은 `defaultNAN   = 999.999;` (47). `if nargin==1` (50)이면 `closepoly    = 0;` (51). fopen 호출은 `fid = fopen(LDBfilename,'r');` (55). `if fid==-1` (56)이면 파일 부재 문구만 출력한다(57). `else` (58)에서는 `while ~feof(fid)` (60)으로 파일 끝까지 반복한다. 행 판독·공백 추가식은 `line = fgetl(fid); line=[line,' '];` (61). `if isempty(findstr(line(1),'*'));` (62)이면 머리말을 linehdr에 보관하고 다음 행을 읽는다(64–65). `if ~isempty(deblank(line)) && ~feof(fid)` (66)이면 `[nrpoints,nrcolumns]=strread([line,'  '],'%f %f','delimiter',' ');` (67)로 점 수·열 수를 읽는다. `if jj>0` (68)이면 `jj=jj+1;` (69)로 인덱스를 늘리고 두 좌표에 NaN 구분자를 넣는다(70–71). `if nrcolumns>2` (72)이면 세 번째 열에도 NaN을 넣는다(73). |
| 77–89 | 시작 시 1행 get_landboundary 함수 안. 시작 시 58행 파일 열기 성공 else·60행 while·62행 비주석 행 분기·66행 비어 있지 않은 크기 행 분기 안. jj0에 시작 인덱스(index)를 보관한다(78). 점 판독 반복은 `for ii=1:nrpoints` (79). fgetl로 행을 읽고(80), `[a,b,c]=strread([line,'  '],'%f %f %f','delimiter',' ');` (81)로 a·b·c를 판독한다. 인덱스 증가식은 `jj=jj+1;` (82). a·b를 LDB 두 열에 복사한다(83–84). `if nrcolumns>2` (85)이면 c를 세 번째 열에 복사한다(86). 분기·반복 종료와 빈 줄을 포함한다(87–89). |
| 90–112 | 시작 시 1행 get_landboundary 함수 안. 시작 시 58행 else·60행 while·62행 비주석 행 분기·66행 크기 행 분기 안. `if closepoly==-1 && jj>jj0+1` (91)에서 `if LDB(jj,1)==LDB(jj0+1,1) && LDB(jj,2)==LDB(jj0+1,2)` (92)이면 마지막 중복점을 제거하는 식 `LDB=LDB(1:jj-1,:);` (93)과 감소식 `jj=jj-1;` (94). 대체 분기는 `elseif closepoly==1 && jj>jj0+1` (97). 그 안에서 `if LDB(jj,1)~=LDB(jj0+1,1) \|\| LDB(jj,2)~=LDB(jj0+1,2)` (98)이면 첫 점을 붙이는 식 `LDB=[LDB;LDB(jj0+1,:)];` (99)와 증가식 `jj=jj+1;` (100). 분기를 닫고(101–102), LDB의 defaultNAN 값을 전체 열에서 NaN으로 대체한다(105). 크기 행·비주석 행·while을 닫고(106–108), fclose를 호출한다(109). 파일 분기·함수 종료와 주석·빈 줄을 포함한다(110–112). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 49·64: linenr는 0 대입 이후 사용하지 않는다. linehdr는 행 복사 이후 사용하지 않는다.
- 55–58: fopen 결과가 -1이면 fprintf만 실행한다. 해당 분기에 error 호출은 없으며 LDB의 초기값은 빈 배열이다.
- 67·79–86: nrcolumns의 값과 관계없이 데이터 행은 세 실수 형식으로 strread를 호출한다. 세 번째 열 저장만 nrcolumns>2 조건 안에 있다.
