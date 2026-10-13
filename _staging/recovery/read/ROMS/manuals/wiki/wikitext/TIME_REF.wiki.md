---
file: models/ROMS/raw/manuals/wiki/wikitext/TIME_REF.wiki
lines: 28
sha256: e90dcf7f354a2959433e01e11551efccd8ad5138e9a68cc78065e57d8c81d236
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# TIME_REF.wiki — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | time_ref / 달력 기준 시각 — 제목·전재 호출·구분선 뒤, 출력 NetCDF의 units 속성을 정의하는 기준 시각이라고 적는다(1–6). 실제 달력 적용에서는 0보다 큰 부동소수점(floating point) yyyymmdd.f 형식이며, TIME_REF=20020115.5 예제가 2002-01-15 12:00:00 기준의 초 속성을 만든다고 적는다(8–12). 원문: `{{#lst:Variables\|time_ref}}` (2); `For so-called realistic applications where the model time corresponds to a certain calendar date, '''time_ref''' will be a floating point number > 0 in the format (yyyymmdd.f)` (8); `For example, setting <span class="blue">TIME_REF</span>=20020115.5 in your [[roms.in]] will yield the following [http://www.cgd.ucar.edu/cms/eaton/cf-metadata/CF-1.0.html CF-Comliant] time units attribute:` (10); `    units = "seconds since 2002-01-15 12:00:00" ` (12). |
| 14–28 | time_ref / 특수값 — TIME_REF=-2이면 model time·DSTART가 modified Julian days, -1이면 매달 30일·매년 360일, 0이면 문서가 common year라고 부르는 365.25일 달력을 사용한다고 적는다(14–26). 각 units 문자열을 원문 그대로 옮기며 마지막 포럼 참조를 포함한다(28). 원문: `If <span class="blue">TIME_REF</span> = -2, model time and [[dstart\|DSTART]] are in modified Julian days units.  The "units" attribute becomes:` (16); `    units = "since 1968-05-23 00:00:00 GMT:` (18); `If <span class="blue">TIME_REF</span> = -1, model time and [[dstart\|DSTART]] are in a calendar with 360 days in every year (30 days each month).  The "units" attribute is:` (20); `   units = "seconds since 0000-01-01 00:00:00"` (22); `If <span class="blue">TIME_REF</span> = 0, model time and [[dstart\|DSTART]] are in a common year calendar with 365.25 days.  The "units" attribute is:` (24); `   units = "seconds since 0000-01-01 00:00:00"` (26). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 18행: units 문자열은 `units = "since 1968-05-23 00:00:00 GMT:`로 끝나며 닫는 큰따옴표와 시간 단위 접두어가 없다.
