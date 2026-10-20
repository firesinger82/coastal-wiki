---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/read_bdy_conds.cu
lines: 166
sha256: 9874b119b81e996e655c41a14039377d45754b5e8f6667d93d26478268b72aee
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_bdy_conds.cu — 판독 구간 기록

구간은 1행부터 166행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 대응 헤더 포함과 read_bdy_conds 정의(1–10). 경계 조건(boundary condition) 파일명·방향 값·Boundary 참조·Pars 상수 참조를 받는다(5–8). 초기값은 `NUMERIC_TYPE upper = C(0.0);` (11); `NUMERIC_TYPE lower = C(0.0);` (12)·`char bcidir  = '0';` (14); `char filedir = '0';` (15) 및 `NUMERIC_TYPE origin = C(0.0);` (20)이다. str[255]와 bdytype_buf[8]를 선언한다(17–18). BCi 선언은 주석이다(22). 이 파일 전체에는 조건부 전처리 분기가 없다. |
| 24–45 | 시작 시 3–10행 read_bdy_conds 함수 안. `switch (direction)` (24)에서 `case NORTH:` (26)는 origin=pars.blx 및 bcidir='N'(27–28), `case EAST:` (30)는 origin=pars.bly 및 bcidir='E'(31–32), `case SOUTH:` (34)는 origin=pars.blx 및 bcidir='S'(35–36), `case WEST:` (38)는 origin=pars.bly 및 bcidir='W'(39–40)를 설정한다. 각 case는 break로 끝난다(29·33·37·41). `default:` (42)는 break만 수행한다(43). switch 닫기와 빈 줄을 포함한다(44–45). |
| 46–68 | 시작 시 3–10행 read_bdy_conds 함수 안. fopen으로 읽기 모드 파일을 연다(46). `if (NULL == fp)` (48)이면 오류를 출력하고 exit(-1)한다(50–51). `while (filedir != bcidir)` (54)에서 `if ( NULL == fgets(str, sizeof(str), fp) )` (56)이면 닫힌 경계로 진행한다는 로그를 출력하고 fclose 후 반환한다(58–61). 반복 안의 판독문은 `sscanf(str, "%c %" NUM_FMT " %" NUM_FMT " %s", &filedir, &lower, &upper, bdytype_buf);` (64)이다. 방향이 일치하면 반복을 끝내고 파일을 닫는다(65–67). 빈 줄을 포함한다. |
| 69–95 | 시작 시 3–10행 read_bdy_conds 함수 안. `if (bcidir == 'N') {` (69)에서 북쪽 범위 제한 원문은 `if (lower < pars.blx) lower = pars.blx;` (72); `if (lower > pars.blx + pars.xsz * pars.dx) lower = pars.blx + pars.xsz * pars.dx;` (73); `if (upper < pars.blx) upper = pars.blx;` (74); `if (upper > pars.blx + pars.xsz * pars.dx) upper = pars.blx + pars.xsz * pars.dx;` (75)이다. BCi1·BCi 선언·대입 및 `//		BCi1 = (int)((lower - pars.blx) / pars.dy);` (77)은 주석이다(70·77·79). 북쪽 조건 종료(80) 뒤 독립된 `if (bcidir == 'W') {` (82)에서 서쪽 범위 제한 원문은 `if (lower < pars.bly) lower = pars.bly;` (86); `if (lower > pars.tly) lower = pars.tly;` (87); `if (upper < pars.bly) upper = pars.bly;` (88); `if (upper > pars.tly) upper = pars.tly;` (89)이다. `//		BCi1 = (int)(2 * pars.xsz + 2 * pars.ysz - (pars.tly - lower) / pars.dy);` (91)과 BCi 관련 선언·대입은 주석이다(84·91·93). 조건 닫기와 빈 줄도 포함한다(94–95). |
| 96–124 | 시작 시 3–10행 read_bdy_conds 함수 안. `if (bcidir == 'S')` (96)에서 남쪽 범위 제한 원문은 `if (lower < pars.blx) lower = pars.blx;` (100); `if (lower > pars.blx + pars.xsz * pars.dx) lower = pars.blx + pars.xsz * pars.dx;` (101); `if (upper < pars.blx) upper = pars.blx;` (102); `if (upper > pars.blx + pars.xsz * pars.dx) upper = pars.blx + pars.xsz * pars.dx;` (103)이다. BCi 관련 문장과 `//		BCi1 = (int)(2 * pars.xsz + pars.ysz - (lower - pars.blx) / pars.dy);` (105)은 주석이다(98·105·107). 조건 종료(108) 뒤 독립된 `if (bcidir == 'E')` (110)에서 동쪽 범위 제한 원문은 `if (lower < pars.bly) lower = pars.bly;` (114); `if (lower > pars.tly) lower = pars.tly;` (115); `if (upper < pars.bly) upper = pars.bly;` (116); `if (upper > pars.tly) upper = pars.tly;` (117)이다. `//		BCi1 = (int)(pars.xsz + (pars.tly - lower) / pars.dy);` (119)과 BCi 관련 문장은 주석이다(112·119·121). 조건 닫기와 빈 줄도 포함한다(122–124). |
| 125–158 | 시작 시 3–10행 read_bdy_conds 함수 안. 기본값은 `int  bdytype        = CLOSED;` (125); `NUMERIC_TYPE inlet          = C(0.0);` (126) 및 `char timeseries[32] = {'\0'};` (128)이다. `if ( !strncmp(bdytype_buf, "CLOSED", 6) )` (130)이면 CLOSED(132), `else if ( !strncmp(bdytype_buf, "FREE", 4) )` (134)이면 FREE(136)로 정한다. `else if ( !strncmp(bdytype_buf, "HFIX", 4) )` (138)이면 HFIX(140)를 정하고 `sscanf(str, "%c %" NUM_FMT " %" NUM_FMT " %s %" NUM_FMT, &filedir, &lower, &upper, bdytype_buf, &inlet);` (141)로 inlet을 읽는다. `else if ( !strncmp(bdytype_buf, "HVAR", 4) )` (143)이면 HVAR(145)를 정하고 `sscanf(str, "%c %" NUM_FMT " %" NUM_FMT " %s %s", &filedir, &lower, &upper, bdytype_buf, timeseries);` (146)로 시계열(time series) 이름을 읽는다. `else if ( !strncmp(bdytype_buf, "QFIX", 4) )` (148)이면 QFIX(150)를 정하고 `sscanf(str, "%c %" NUM_FMT " %" NUM_FMT " %s %" NUM_FMT, &filedir, &lower, &upper, bdytype_buf, &inlet);` (151)로 inlet을 읽는다. `else if ( !strncmp(bdytype_buf, "QVAR", 4) )` (153)이면 QVAR(155)를 정하고 `sscanf(str, "%c %" NUM_FMT " %" NUM_FMT " %s %s", &filedir, &lower, &upper, bdytype_buf, timeseries);` (156)으로 시계열 이름을 읽는다. 각 else if는 이전 조건이 모두 거짓일 때 평가한다. 마지막 기본 else는 없으며 닫기와 빈 줄도 포함한다. |
| 159–166 | 시작 시 3–10행 read_bdy_conds 함수 안. `boundary.start = (lower - origin) / pars.dx;` (159); `boundary.end = (upper - origin) / pars.dx - 1;` (160)으로 경계 시작·끝 인덱스를 구한다. gen_bdy_morton_codes(boundary, pars, direction)를 호출한다(161). 경계 형식과 inlet을 복사한다(162–163). BCi 복사는 주석이고(164), sprintf로 timeseries를 복사한 뒤 함수를 닫는다(165–166). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 54–65·67: 파일에서 방향이 처음 일치하면 탐색을 끝내고 파일을 닫는다. 같은 방향의 뒤쪽 기록을 추가로 읽는 반복은 없다.
- 72–117·141·146·151·156: lower·upper를 영역 범위로 제한한 뒤 HFIX·HVAR·QFIX·QVAR 분기에서는 같은 원문 줄의 좌표를 sscanf로 lower·upper에 다시 읽는다.
- 159–160: 북·남·동·서 방향 모두 시작·끝 인덱스 계산의 분모에 pars.dx를 사용한다. 서·동 방향의 origin은 pars.bly이다(31·39).
- 17–18·64·128·141–156: bdytype_buf의 크기는 8이고 timeseries의 크기는 32이다. 이를 읽는 %s 지정에는 필드 폭이 없다. 이 함수는 sscanf 반환값을 검사하지 않는다.
- 14–15·24–44·54·130: switch의 default는 방향 문자를 바꾸지 않는다. direction이 네 case에 해당하지 않으면 bcidir와 filedir의 초기값이 같아 파일 탐색 반복을 건너뛴다. bdytype_buf 선언에는 초기값이 없다(18).
