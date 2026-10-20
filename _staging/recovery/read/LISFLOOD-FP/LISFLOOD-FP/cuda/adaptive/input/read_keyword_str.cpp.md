---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_keyword_str.cpp
lines: 42
sha256: a389891b22bc0f4b41c87d90113727c89c2b5ef7fb6b19af4428dcf274ff52ac
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_keyword_str.cpp — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 자기 헤더를 포함한다(1). read_keyword_str는 파일명·키워드(keyword)·비교 문자 수·출력 버퍼를 받는다(3–9). `if (num_char > 128)` (11)이면 오류 출력·exit(-1)(13–14). fopen 뒤(17) `if (NULL == fp)` (19)이면 오류 출력·exit(-1)(21–22). 전처리 조건 분기는 없다. |
| 25–42 | 시작 시 3행 함수 안. 키 버퍼 128자·행 버퍼 255자를 널 문자로 초기화한다(25–26). `while ( strncmp(keyword_buf, keyword, num_char) )` (28) 안의 `if ( NULL == fgets(line_buf, sizeof(line_buf), fp) )` (30)이면 키 부재를 출력하고 fclose한 뒤 value_buf[0]을 널 문자로 설정하고 반환한다(32–35). 그 조건 밖 `sscanf(line_buf, "%s %s", keyword_buf, value_buf);` (38)로 키와 문자열 값을 읽는다. 키 일치 후 fclose하고 함수를 닫는다(41–42). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–8·11·25·38: num_char > 128 검사는 있으나 출력 value_buf의 크기를 받는 인수는 없다. 두 %s 모두 필드 폭이 없다.
- 28·38: 키는 지정 길이 strncmp로 비교한다. sscanf의 반환값을 검사하지 않으며 키 일치 전에 읽는 각 행에서도 value_buf를 출력 대상으로 사용한다.
