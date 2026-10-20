---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/read_num_point_srcs.cpp
lines: 49
sha256: 66b7a82ebc2bc2b8440aa19892989047cd0be17121f77d5ba5e2b68dbdebca7b
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_num_point_srcs.cpp — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 대응 헤더 포함과 `lis::cuda::acc_nugrid::PointSources lis::cuda::acc_nugrid::read_num_point_srcs` (3) 반환형·함수 이름 및 파일명 인수(4–7). str[255]를 선언한다(8). `if (strlen(bcifilename) == 0)` (10)이면 로그는 주석 처리된 채 0을 반환한다(12–13). fopen으로 파일을 읽기 모드로 연다(16). `if (NULL == fp)` (18)이면 오류 출력 후 exit(-1)한다(20–21). 닫는 괄호와 빈 줄도 포함한다. 이 파일 전체에는 조건부 전처리 분기가 없다. |
| 25–49 | 시작 시 3–7행 read_num_point_srcs 함수 안. 기본값은 `char point = '\0';` (25); `int  num_srcs = 0;` (26) 및 `NUMERIC_TYPE x_stage = C(0.0); //TOREMOVE` (28); `NUMERIC_TYPE y_stage = C(0.0); //TOREMOVE` (29)이다. `while (!(NULL == fgets(str, sizeof(str), fp)))` (31)에서 sscanf로 줄의 첫 문자를 읽는다(33). `if (point == 'P') num_srcs++;` (35)로 P 줄을 센다. `if (num_srcs == 0)` (38)이면 점 유입원(point source)이 없다는 로그를 출력하고 파일을 닫은 뒤 0을 반환한다(40–43). 나머지는 파일을 닫고 num_srcs를 반환한다(46–48). 조건·함수 닫기와 빈 줄도 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28–29: x_stage·y_stage에는 TOREMOVE 주석이 있으며 이후 실행문에서 두 변수를 사용하지 않는다.
- 3·13·26·43·48: 함수 반환형은 PointSources이다. 실제 return 표현식은 정수 0 또는 int 변수 num_srcs이다. 이 파일에는 해당 형 변환이나 생성자의 정의가 없다.
