---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_save_interval.cpp
lines: 40
sha256: 62a6517e196f788a0b0de28c901d3f0da035816c17e46c9bd6cc84901deb7948
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_save_interval.cpp — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | SaveInterval을 반환하는 read_save_interval 정의와 헤더 포함이다(1–8). interval=C(0.0), 문자열 버퍼 두 개를 널 문자로 초기화하고 문자 수를 0으로 둔다(9–14). while로 interval_type의 길이를 세고 입력 파일을 연다(16–18). 조건부 전처리 분기는 없다. 원문: `while ( *(interval_type + num_char_interval_id) != '\0' ) num_char_interval_id++;` (16). |
| 19–25 | 시작 시 3행 read_save_interval 루틴 안. 입력 파일 열기 실패 조건에서 표준 오류에 파일·행 정보를 출력하고 exit(-1)을 호출한다(20–24). 원문: `if (NULL == fp)` (20). |
| 26–40 | 시작 시 3행 read_save_interval 루틴 안. 키의 지정 길이만큼 비교하는 while을 돈다(26). fgets가 NULL이면 로그·fclose 후 고정된 두 값 C(9999.0)과 9999를 반환한다(28–34). 루프 안 sscanf는 키와 interval을 읽는다(36). 키가 맞으면 interval과 0을 반환한다(39). 원문: `while ( strncmp(buf, interval_type, num_char_interval_id) )` (26); `if ( NULL == fgets(str, sizeof(str), fp) )` (28); `return { C(9999.0), 9999 };` (33); `sscanf(str, "%s %" NUM_FRMT, buf, &interval);` (36); `return { interval, 0 };` (39). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26·36: 키 비교 길이는 interval_type 길이이다. sscanf의 %s에는 필드 폭이 없고 반환값 검사도 없다.
- 31·39–40: 파일을 닫는 문장은 fgets 실패 경로에 있다. 정상 반환 직전에는 fclose가 없다.
- 33: 키 미발견 반환값은 { C(9999.0), 9999 }로 고정되어 있다.
