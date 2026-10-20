---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_test_case.cpp
lines: 42
sha256: a51781f58a03008b97efc11112deee9408c28a901f3852c16082abdf2b0ec3f6
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_test_case.cpp — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 헤더를 포함하고 read_test_case를 정의한다(1–4). 파일 열기에 실패하면 오류 출력 후 exit(-1)을 호출한다(5–11). 조건부 전처리 분기는 없다. 원문: `if (NULL == fp)` (7). |
| 13–28 | 시작 시 3행 read_test_case 루틴 안. str[255]·buf[64]를 초기값 없이 선언하고 test_case를 0으로 둔다(13–15). test_case 키의 앞 9자를 비교하는 while에서 fgets가 NULL이면 파일을 닫고 0을 반환한다(17–24). sscanf로 buf와 test_case를 읽고 반환값을 num_read에 둔다(26). 원문: `while ( strncmp(buf, "test_case", 9) )` (17); `if (NULL == fgets(str, sizeof(str), fp))` (19); `int num_read = sscanf(str, "%s %d", buf, &test_case);` (26). |
| 29–42 | 시작 시 3행 read_test_case 루틴 안이며 17행 while 밖이다. fclose와 테스트 번호 로그를 실행한다(29–31). 최대 번호를 23으로 고정한다(33). 0..23 범위를 벗어나면 로그와 exit(-1)을 실행한다(35–39). 정수를 반환한다(41–42). 원문: `const int max_test_case = 23;` (33); `if (test_case > max_test_case \|\| test_case < 0)` (35). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13–17·26: buf는 초기화 없이 선언된다. while 조건은 첫 sscanf 실행 전에 buf를 strncmp에 전달한다.
- 26: num_read는 sscanf 반환값을 받은 뒤 이 파일에서 사용되지 않는다. %s에는 필드 폭이 없다.
- 17·33–35: 키 비교 길이는 9로 고정된다. 허용 테스트 번호는 0..23으로 고정된다.
