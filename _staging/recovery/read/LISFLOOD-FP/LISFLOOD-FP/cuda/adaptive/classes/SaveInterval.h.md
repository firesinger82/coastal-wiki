---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/SaveInterval.h
lines: 63
sha256: 113267a6b6b90b15aee0ac002aaa95091636e750737aadfeda2b5194b0c24cb5
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# SaveInterval.h — 판독 구간 기록

구간은 1행부터 63행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | `#pragma once` (1), real.h 포함(3). 전처리 조건 분기는 없다. SaveInterval은 real interval·int count를 보유한다(5–8). 생성자는 input_filename·interval_type을 받는다(10–15). 지역 기본값 `real interval = C(0.0);` (16), 255·64자 버퍼 초기화(18–19), 문자 수 0 초기화(21). `while ( *(interval_type + num_char_interval_id) != '\0' ) num_char_interval_id++;` (23)로 키 이름 길이를 센다. |
| 25–46 | 시작 시 10–15행 SaveInterval 생성자 안. 입력 파일 fopen(25), `if (NULL == fp)` (27)이면 오류·exit(-1)(29–30). `while ( strncmp(buf, interval_type, num_char_interval_id) )` (33)의 키 탐색에서 `if ( NULL == fgets(str, sizeof(str), fp) )` (35)이면 안내·fclose(37–38), 대체 기본값 `this->interval = C(9999.0);`<br>`this->count    = 9999;` (40–41)을 저장하고 반환한다(42). 정상 행은 sscanf로 키와 interval을 읽는다(45). |
| 47–51 | 시작 시 10–15행 SaveInterval 생성자 안이며 33행 while 밖. 찾은 간격과 시작 횟수 설정 `this->interval = interval;`<br>`this->count    = 0;` (48–49). 생성자 종료(50). |
| 52–63 | 시작 시 5–6행 SaveInterval 구조체 안. save(current_time)(52–53)의 판정 `if (current_time >= interval * count)` (54)이 참이면 count를 한 번 증가시키고 true를 반환한다(56–57). 분기 밖에서는 false를 반환한다(60). 메서드·구조체 종료(61–63). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 25–50: 입력 파일은 fopen으로 열린다. EOF 처리 분기에는 fclose가 있지만 키를 찾은 정상 경로에는 fclose가 없다.
- 37·40–41·54: 키가 없을 때 안내 문구는 associated data를 저장하지 않는다고 적는다. 실제 상태는 interval=C(9999.0)·count=9999이며 save는 여전히 current_time >= interval * count로 판정한다.
- 23·33: 키 비교는 interval_type 길이의 strncmp이다. 읽은 토큰 전체 길이가 같은지 확인하는 조건은 없다.
- 45·48–49·54: 읽은 간격의 부호·0 여부와 sscanf 반환값을 검사하는 조건은 없다. 정상 판독 경로의 count 초기값은 0이다.
