---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_keyword_real.cpp
lines: 44
sha256: 262efe9812d2791a8785aadd1ecbddfe7a0d7ddc04e22a905346fb35c73fd0b0
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_keyword_real.cpp — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 자기 헤더를 포함한다(1). read_keyword_real은 파일명·키워드(keyword)·비교 문자 수를 받는다(3–8). `if (num_char > 128)` (10)이면 오류 출력·exit(-1)(12–13). fopen 뒤(16) `if (NULL == fp)` (18)이면 오류 출력·exit(-1)(20–21). 전처리 조건 분기는 없다. |
| 24–44 | 시작 시 3행 함수 안. `real value = C(0.0);` (24). 키 버퍼 128자·행 버퍼 255자를 널 문자로 초기화한다(26–27). `while ( strncmp(keyword_buf, keyword, num_char) )` (29) 안의 `if ( NULL == fgets(line_buf, 255, fp) )` (31)이면 키 부재를 출력하고 fclose 후 `return C(0.0);` (35). 그 조건 밖 `sscanf(line_buf, "%s %" NUM_FRMT, keyword_buf, &value);` (38)로 키와 실수 값을 읽는다. 키 일치 후 fclose하고 value를 반환하며 함수를 닫는다(41–44). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10·26·38: 길이 검사는 num_char > 128만 검사한다. 키 버퍼는 128자이며 sscanf의 %s에는 필드 폭이 없다.
- 24·38: value는 루프 전에 한 번 C(0.0)으로 초기화된다. 각 행 sscanf의 반환값을 검사하거나 value를 재초기화하는 문장은 없다.
- 29·35: 키는 지정 길이 strncmp로 비교한다. 키 부재 시 반환값 C(0.0)은 초기 기본값과 같다.
