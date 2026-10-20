---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/lisflood2/windows_ext.cpp
lines: 48
sha256: ae4a084bde9fb302591d4d219c18adc1cb7c9f666df3258524d41718fd5c1fa4
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# windows_ext.cpp — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 전체 파일의 외곽 전처리 조건은 _MSC_VER 또는 _MSC_EXTENSIONS 정의 여부다(1·48). 4행에서 같은 조건을 중첩 검사하여 참 쪽은 Ui64 접미사, 6행 else 쪽은 ULL 접미사의 epoch 상수를 정의한다(4–8). windows_ext.h를 포함한다(10). 이 구간의 include도 외곽 참 조건에서만 컴파일한다. 원문 조건·식·지시: `#if defined(_MSC_VER) \|\| defined(_MSC_EXTENSIONS)` (1), `#if defined(_MSC_VER) \|\| defined(_MSC_EXTENSIONS)` (4), `#define DELTA_EPOCH_IN_MICROSECS  11644473600000000Ui64` (5), `#else` (6), `#define DELTA_EPOCH_IN_MICROSECS  11644473600000000ULL` (7), `#endif` (8). |
| 13–33 | 시작 시 1행 외곽 전처리 참 분기 안. gettimeofday는 FILETIME·64비트 정수·정적 tzflag를 선언한다(13–17). tv가 NULL이 아니면 GetSystemTimeAsFileTime을 호출하고 상하위 32비트를 합쳐 epoch 상수를 뺀다(19–28). 10으로 나눈 뒤 초와 마이크로초(microsecond)를 몫/나머지로 계산하여 long으로 변환한다(29–31). 원문 조건·식·지시: `if (NULL != tv)` (19), `tmpres \|= ft.dwHighDateTime;` (23), `tmpres <<= 32;` (24), `tmpres \|= ft.dwLowDateTime;` (25), `tmpres -= DELTA_EPOCH_IN_MICROSECS;` (28), `tmpres /= 10;  /*convert into microseconds*/` (29), `tv->tv_sec = (long)(tmpres / 1000000UL);` (30), `tv->tv_usec = (long)(tmpres % 1000000UL);` (31). |
| 34–48 | 시작 시 1행 외곽 전처리 참 분기·13행 gettimeofday 안. tz가 NULL이 아닌 분기의 본문은 전부 블록 주석이다(34–43). 그 안의 tzflag 검사·_tzset·시간대 설정은 실행되지 않는다(36–42). 함수는 항상 0을 반환하고 외곽 전처리 조건을 닫는다(45–48). 원문 조건·식·지시: `if (NULL != tz)` (34), `/*	if (!tzflag)` (36), `{` (37), `_tzset();` (38), `tzflag++;` (39), `}` (40), `tz->tz_minuteswest = _timezone / 60;` (41), `tz->tz_dsttime = _daylight;*/` (42), `#endif` (48). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·4–8: 외곽과 내부 전처리 조건이 동일하다. 이 파일 안에는 두 검사 사이에서 해당 매크로를 바꾸는 지시가 없다. 6–7행에는 동일 조건의 else용 ULL 정의가 남아 있다.
- 5·28–31: 상수 이름은 DELTA_EPOCH_IN_MICROSECS이다. 코드는 이 상수를 먼저 뺀 다음 10으로 나누고 1000000UL로 초/마이크로초를 나눈다.
- 17·34–43: tzflag는 선언되지만 참조문은 블록 주석 안에만 있다. tz가 NULL이 아니어도 tz 필드에 실행되는 대입문은 없다.
