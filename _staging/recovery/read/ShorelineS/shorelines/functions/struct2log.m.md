---
file: models/ShorelineS/raw/source_code/shorelines/functions/struct2log.m
lines: 157
sha256: 614cca9b3b04068ca3eaff2818190c444ce14686b524ed260285768d489b71ca
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# struct2log.m — 판독 구간 기록

구간은 1행부터 157행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | 함수 시그니처는 `function struct2log(P,structname,writeopt)` (1). 주석은 모델 입력을 logfile.txt에 기록한다고 설명한다(2–5). S 구조체 인수와 S 필드 기본값은 없다. 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(6–33). |
| 34–64 | fopen('logfile.txt',writeopt)를 호출한다(35). `if ischar(P)` (37)이면 `if ischar(structname)` (39)에서 `structname={structname};` (40). `for jj=1:length(structname)` (42)은 각 메시지를 파일에 출력한다(43). `if strcmpi(P,'print') \|\| strcmpi(P,'warning')` (44)이면 화면에도 출력한다(45). `else` (48)는 fieldnames(P)를 읽고 구조체 머리말을 출력한다(50–52). 머리말 길이 계산은 `repmat('%',[1,15-length(structname)])` (52). `for i=1:length(fieldname)` (53)에서 val·fieldnm을 복사하고 `printinputfield(fid,fieldnm,val,' ');` (56)를 호출한다. 마지막 빈 줄 출력 뒤 fclose(fid)를 호출하고 주 함수를 닫는다(59–64). |
| 65–80 | 지역 함수 시그니처는 `function printinputfield(fid,fieldnm,val,addstr,endline)` (65). 기본값은 `endofline='\n';` (67), `nrspaces=26;` (68). `if nargin==5` (69)이면 `endofline='';` (70), `nrspaces=1;` (71), `fieldnm=['',fieldnm,repmat(' ',[1 max(nrspaces-length(fieldnm),0)])];` (72). `else` (73)는 `fieldnm=['',fieldnm,repmat(' ',[1 max(nrspaces-length(fieldnm),0)]),' ='];` (74). 조건 종료와 공백·주석 줄을 포함한다. |
| 81–106 | `if isempty(val)` (82)이면 []를 출력한다(83). `elseif isnumeric(val)` (86) 안에서 `if length(val)==1` (87)이면 num2str(val(:)')를 출력한다(88). `else` (89)는 `sz=size(val);` (90) 뒤 `if sz(2)==1 && sz(1)>1` (91)에서 `val=val';` (92), `sz=size(val);` (93). 대괄호를 연 뒤 `for mm=1:sz(1)` (96), `for nn=1:sz(2)` (97)에서 숫자를 출력한다(98). `if mm<sz(1)` (100)이면 연속 줄 표시와 `repmat(' ',[1 nrspaces+5])` (101) 공백을 출력한다. mm 루프는 103행에서 끝난다. 104행에서 닫는 대괄호와 줄 끝을 출력한다. 87행의 길이 조건은 105행에서 끝난다. [10-12 전수 검증 정정] |
| 107–126 | 시작 시 82행 값 유형 선택 분기 안. `elseif iscell(val)` (108)은 `sz=size(val);` (109), `if sz(2)==1 && sz(1)>1` (110)이면 `val=val';` (111), `sz=size(val);` (112). 중괄호를 연 뒤 `for mm=1:sz(1)` (115), `for nn=1:sz(2)` (116)에서 fieldnm2를 비우고 `printinputfield(fid,fieldnm2,val{mm,nn}','',1);` (119)을 재귀(recursion) 호출한다. 숫자 직접 출력문은 주석이다(117). `if mm<sz(1)` (121)이면 연속 줄 표시와 `repmat(' ',[1 nrspaces+5])` (122) 공백을 출력한다. 루프 종료 후 중괄호·줄 끝을 출력한다(124–125). |
| 127–144 | 시작 시 82행 값 유형 선택 분기 안. `elseif isstruct(val)` (128)이면 `fieldnm=deblank(fieldnm);` (129), fields(val) 호출(130). `for mm=1:length(val)` (132), `for gg=1:length(fields2)` (133)에서 addstr을 공백으로 둔다(135). `if length(val)==1` (136)이면 `fieldnm2=['',[deblank(fieldnm(1:end-1)),'.',fields2{gg}],repmat(' ',[1 max(nrspaces-length([deblank(fieldnm(1:end-1)),'.',fields2{gg}]),0)])];` (137). `else` (138)는 `fieldnm2=['',[deblank(fieldnm(1:end-1)),'(',num2str(mm),').',fields2{gg}],repmat(' ',[1 max(nrspaces-length([deblank(fieldnm(1:end-1)),'(',num2str(mm),').',fields2{gg}]),0)])];` (139). `printinputfield(fid,fieldnm2,val(mm).(fields2{gg}),addstr);` (141)를 재귀 호출한다. 대체 출력 주석·루프 종료·공백 줄을 포함한다. |
| 145–157 | 시작 시 82행 값 유형 선택 분기 안. `elseif ischar(val)` (146)에서 `if isempty(addstr)` (147)이면 문자열을 작은따옴표로 감싸 출력한다(148). `else` (149)는 try로 문자열을 출력하고(151), catch에서 fieldnm을 작은따옴표로 감싸 출력한다(152–153). 문자열 구성은 `['''',val(:)','''']` (148·151), catch 구성은 `['''',fieldnm,'''']` (153). try·내부 조건·값 유형 선택·지역 함수 종료를 포함한다(154–157). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 35: 파일 이름은 logfile.txt로 고정되어 있다. 파일 열기 반환값을 검사하는 조건은 없다.
- 52: 머리말 공백 대신 퍼센트 반복 개수를 15-length(structname)로 정한다. 이 인수에는 max(...,0) 제한이 없다.
- 65·69–71: endline 인수 값은 본문에서 참조하지 않는다. 다섯 번째 인수 존재 여부 nargin==5가 줄 끝 제거와 공백 폭 변경을 결정한다.
- 91–94·110–113·119: 숫자·셀 열벡터는 출력 전에 전치한다. 셀 재귀 호출도 개별 값에 전치를 적용한다.
- 82–156: 값 유형 분기는 빈 값·numeric·cell·struct·char를 검사한다. 그 밖의 유형을 처리하는 마지막 else는 없다.
