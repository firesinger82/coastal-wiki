---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/boundary.cpp
lines: 68
sha256: 925c58a0d089048b9d4bd762f2603f893763f8f25e77b5df93dc57285cbaa595
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# boundary.cpp — 판독 구간 기록

구간은 1행부터 68행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | boundary.h를 포함한다(1). linear_interpolate는 시간열(time series)의 시각·값 배열을 참조한다(3–10). `if (t < times[0]) return values[0];` (12)이면 첫 값을 반환한다. `for (int i=1; i < timeSeries->count; i++)` (14)에서 `if (times[i - 1] <= t && times[i] > t)` (16)인 구간을 찾으면 `dt = times[i] - times[i - 1];` (19), `a1 = (t - times[i - 1]) / dt;` (20), `a2 = C(1.0) - a1;` (21)로 선형 보간(linear interpolation) 가중치를 구하고 `return a1*values[i] + a2*values[i - 1];` (23)을 반환한다. 구간을 찾지 못하면 `return values[timeSeries->count - 1];` (27)로 마지막 값을 반환한다. 이 파일에는 전처리 분기가 없다. |
| 30–49 | 서쪽·동쪽 경계 인덱스(boundary index) 함수는 모두 Pars와 const int i·j를 받는다(30–35·40–45). 서쪽 반환식은 `return 2*Parptr->xsz + 2*Parptr->ysz - j - 1;` (37), 동쪽 반환식은 `return Parptr->xsz + j;` (47)이다. 두 함수는 i를 사용하지 않는다. |
| 50–68 | 북쪽·남쪽 경계 인덱스 함수도 Pars와 const int i·j를 받는다(50–55·60–65). 북쪽은 i를 반환하고(57), 남쪽은 `return 2*Parptr->xsz + Parptr->ysz - i - 1;` (67)이다. 두 함수는 j를 사용하지 않는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–12·27: linear_interpolate는 times[0]과 values[count-1]에 접근한다. 이 함수에 count>0 또는 포인터 NULL 검사는 없다.
- 30–68: 서·동 함수의 i, 북·남 함수의 j, 북 함수의 Parptr는 본문에서 사용되지 않는다.
