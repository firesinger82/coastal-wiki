---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/input/read_keyword_bool.cpp
lines: 42
sha256: 4e40e27ff7673bc0651e16281d79657c602ec4a11e3f9f591c6018af8d74fee5
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# read_keyword_bool.cpp — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 자기 헤더를 포함한다(1). read_keyword_bool은 파일명·키워드(keyword)·비교 문자 수를 받는다(3–8). `if (num_char > 128)` (10)이면 오류 출력·exit(-1)(12–13). fopen으로 파일을 연다(16). `if (NULL == fp)` (18)이면 오류 출력·exit(-1)(20–21). 전처리 조건 분기는 없다. |
| 24–42 | 시작 시 3행 함수 안. 128자 키 버퍼와 255자 행 버퍼를 널 문자로 초기화한다(24–25). `while ( strncmp(keyword_buf, keyword, num_char) )` (27) 안의 `if ( NULL == fgets(line_buf, sizeof(line_buf), fp) )` (29)이면 키 부재를 stderr에 출력하고 fclose 후 false를 반환한다(31–33). 그 조건 밖에서 sscanf로 첫 토큰(token)만 읽는다(36). 키 비교가 일치하면 루프 뒤 fclose하고 true를 반환한다(39–41). 함수 종료(42). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10·24·36: 길이 검사는 num_char > 128만 검사한다. keyword_buf는 128자이며 sscanf의 %s에는 필드 폭이 없다.
- 27·36·41: 참/거짓 값 토큰은 읽지 않는다. 첫 토큰이 지정 길이 strncmp에서 일치하면 true를 반환한다.
- 36: sscanf의 반환값을 검사하지 않는다.
