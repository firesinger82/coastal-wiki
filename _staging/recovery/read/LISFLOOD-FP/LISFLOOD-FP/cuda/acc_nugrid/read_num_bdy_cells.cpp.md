---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/read_num_bdy_cells.cpp
lines: 70
sha256: 6ac8e590f68a0ddbad17e82ec7753092e70810dde7a0b19dbff201de3c3f716a
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_num_bdy_cells.cpp — 판독 구간 기록

구간은 1행부터 70행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 대응 헤더 포함과 int 반환 read_num_bdy_cells 정의(1–9). 경계 조건(boundary condition) 파일명·Pars 상수 참조·방향 값을 받는다(5–7). 좌표와 방향 문자 기본값은 `NUMERIC_TYPE upper = C(0.0);` (10); `NUMERIC_TYPE lower = C(0.0);` (11)·`char bcidir = '0';` (13); `char filedir = '0';` (14)이다. str[255]·bdytype_buf[8] 선언(16–17), `NUMERIC_TYPE origin = C(0.0);` (19)로 원점 기본값을 둔다. 이 파일 전체에는 조건부 전처리 분기가 없다. |
| 21–42 | 시작 시 3–9행 read_num_bdy_cells 함수 안. `switch (direction)` (21)의 `case NORTH:` (23)는 origin=pars.blx·bcidir='N'(24–25), `case EAST:` (27)는 origin=pars.bly·bcidir='E'(28–29), `case SOUTH:` (31)는 origin=pars.blx·bcidir='S'(32–33), `case WEST:` (35)는 origin=pars.bly·bcidir='W'(36–37)를 정한다. 각 case 뒤 break가 있다(26·30·34·38). `default:` (39)는 break만 수행한다(40). switch 닫기와 빈 줄도 포함한다(41–42). |
| 43–65 | 시작 시 3–9행 read_num_bdy_cells 함수 안. fopen으로 파일을 읽기 모드로 연다(43). `if (NULL == fp)` (45)이면 오류 출력 후 exit(-1)한다(47–48). `while (filedir != bcidir)` (51)에서 `if (NULL == fgets(str, sizeof(str), fp))` (53)이면 해당 방향의 강제 경계 셀이 없다는 로그를 출력하고 fclose 후 0을 반환한다(55–58). 판독문은 `sscanf(str, "%c %" NUM_FMT " %" NUM_FMT " %s", &filedir, &lower, &upper, bdytype_buf);` (61)이다. 방향 일치로 반복이 끝나면 fclose를 호출한다(64). 반복·조건 닫기와 빈 줄도 포함한다. |
| 66–70 | 시작 시 3–9행 read_num_bdy_cells 함수 안. 경계 인덱스는 `int start = (lower - origin) / pars.dx;` (66); `int end = (upper - origin) / pars.dx - 1;` (67)로 계산한다. 개수 반환식은 `return end - start + 1;` (69)이다. 함수 닫기와 빈 줄도 포함한다(68–70). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 51–64: 방향이 처음 일치하면 탐색을 끝내며 같은 방향의 뒤쪽 기록을 합산하는 반복은 없다. 읽은 bdytype_buf 값은 이후 사용하지 않는다.
- 66–69: 모든 방향에서 pars.dx로 나누어 개수를 구한다. lower·upper를 영역 범위로 제한하거나 start·end의 순서를 검사하는 분기는 없다.
- 16–17·61: bdytype_buf는 크기 8이며 이를 읽는 %s에는 필드 폭이 없다. sscanf 반환값을 검사하지 않는다.
- 13–14·19·21–41·51·66–69: default는 방향 문자와 원점을 바꾸지 않는다. 네 case 외의 direction은 초기 방향 문자가 같아 탐색 반복을 건너뛰며 초기 좌표로 개수를 계산한다.
