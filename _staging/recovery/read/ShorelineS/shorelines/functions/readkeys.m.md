---
file: models/ShorelineS/raw/source_code/shorelines/functions/readkeys.m
lines: 75
sha256: ccbffbb2ab1a3d16e8a39b012a6abdb269f4a8975fb8a353f359b083d37feb09
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# readkeys.m — 판독 구간 기록

구간은 1행부터 75행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | 함수 시그니처는 `function [data] = readkeys(filename)` (1). 주석은 입력 파일 이름과 입력 필드를 담는 반환 구조체를 설명한다(2–9). S 입력 구조체 인수와 S 필드 기본값 설정은 없다. 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(10–37). |
| 38–50 | number를 0으로 초기화하고 fopen(filename)을 호출한다(38–39). `while 1` (40)에서 fgetl로 한 줄을 읽는다(41). `if ~isempty(s)` (42) 안의 원문 종료 조건은 `if ~ischar(s), break, end` (43). `s = strip(s);` (44), `cont=strfind(s,'...');` (45). `while ~isempty(cont)` (46)에서 다음 줄을 읽고 `s=[s(1:cont-1),strip(nxt)];` (48), `cont=strfind(s,'...');` (49)로 연속 줄을 합친다. 내부 루프 종료를 포함한다(50). |
| 51–69 | 시작 시 40행 무한 루프·42행 비어 있지 않은 줄 분기 안. `if s(1)~='%'` (51)이면 `k=find(s=='=',1);` (52). `if ~isempty(k)` (53)에서 `number=number+1;` (54), `keywords{number}=strip(s(1:k-1));` (55), `val=strip(s(k+1:end));` (56). 대체 구분자 검색문 두 줄은 주석이다(57–58). `m=find(val==';'\|val=='%');` (59). `if isempty(m)` (60)이면 val 전체를 values에 복사한다(61). `else` (62)는 `values{number}=val(1:m-1);` (63). 내부 조건·바깥 조건·루프를 닫고 fclose(fid)를 호출한다(64–69). |
| 70–75 | `for i=1:length(keywords);` (70)에서 keyword·value를 각 셀에서 복사한다(71–72). `eval(['data.',keyword,'=',value,';']);` (73)로 구조체 필드 대입문을 구성하고 실행한다. 루프와 함수 종료를 포함한다(74–75). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 39–41: fopen 반환값 fid를 바로 fgetl에 전달한다. 파일 열기 실패를 검사하는 조건은 없다.
- 42–51: 비어 있음 검사는 strip 호출 전이다. strip 뒤 첫 글자 s(1)를 바로 참조한다.
- 45–49: strfind는 모든 '...' 위치를 cont에 넣는다. 이어지는 범위식은 cont 전체를 사용한다.
- 59–63: 세미콜론·퍼센트 검색 find에는 첫 일치만 선택하는 인수가 없다. 값 자르기 범위식은 m 전체를 사용한다.
- 38–75: keywords·values·data에 별도 초기화는 없다. 대입문이 하나도 없는 입력에서도 length(keywords)를 참조한다.
