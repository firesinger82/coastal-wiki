---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/tests.cpp
lines: 176
sha256: 63e64c9cab14c0b2bcbd71c07a65af176b3182bdaa9f2bd6264ba1f714e25225
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# tests.cpp — 판독 구간 기록

구간은 1행부터 176행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–53 | lisflood 헤더(1) 후 `#ifdef TESTING`(2)이 나머지 본문을 감싼다. TESTING이 정의된 경우에만 DataTypes 헤더(3), 부하 균형(load balance) 함수 원형(4–6), 시험 함수들을 컴파일한다. 미정의 경우에는 1행 포함만 남는다. 이 파일에는 TESTING 값 정의와 #else가 없다. `TestInterpolate`(9–115)는 값·시간 교대 배열 12개와 독립 배열 5개씩을 준비한다. 다섯 표본은 시간 0·10·20·30·40, 값 0·10·200·10·10이며 교대 배열 끝은 −1·−1이다(12–44). TimeSeries에 count=5와 두 배열 포인터를 설정한다(47–50). 원문: `#ifdef TESTING` (2); `#include "lisflood2\DataTypes.h"` (3). |
| 54–84 | 시작 시 2행 TESTING 정의 분기·9행 `TestInterpolate` 안이다. t=0·3·5·10·15·20에서 교대 배열형과 TimeSeries 포인터형 `InterpolateTimeSeries`를 각각 호출한다. 각 결과와 x−y를 printf로 출력한다(57·62·68·73·78·83). 원문: `t = C(0.0);` (54); `x = InterpolateTimeSeries(interpData, t);` (55); `y = InterpolateTimeSeries(&ts, t);` (56); `t = C(3.0);` (59); `x = InterpolateTimeSeries(interpData, t);` (60); `y = InterpolateTimeSeries(&ts, t);` (61); `t = C(5.0);` (65); `x = InterpolateTimeSeries(interpData, t);` (66); `y = InterpolateTimeSeries(&ts, t);` (67); `t = C(10.0);` (70); `x = InterpolateTimeSeries(interpData, t);` (71); `y = InterpolateTimeSeries(&ts, t);` (72); `t = C(15.0);` (75); `x = InterpolateTimeSeries(interpData, t);` (76); `y = InterpolateTimeSeries(&ts, t);` (77); `t = C(20.0);` (80); `x = InterpolateTimeSeries(interpData, t);` (81); `y = InterpolateTimeSeries(&ts, t);` (82). |
| 85–116 | 시작 시 2행 TESTING 정의 분기·9행 `TestInterpolate` 안이다. t=25·30·35·40·45·2 순서로 두 보간 함수(interpolation function)를 호출한다. 매번 두 결과와 차이를 출력한다(88·93·98·103·108·113). 함수는 115행에서 끝난다. 원문: `t = C(25.0);` (85); `x = InterpolateTimeSeries(interpData, t);` (86); `y = InterpolateTimeSeries(&ts, t);` (87); `t = C(30.0);` (90); `x = InterpolateTimeSeries(interpData, t);` (91); `y = InterpolateTimeSeries(&ts, t);` (92); `t = C(35.0);` (95); `x = InterpolateTimeSeries(interpData, t);` (96); `y = InterpolateTimeSeries(&ts, t);` (97); `t = C(40.0);` (100); `x = InterpolateTimeSeries(interpData, t);` (101); `y = InterpolateTimeSeries(&ts, t);` (102); `t = C(45.0);` (105); `x = InterpolateTimeSeries(interpData, t);` (106); `y = InterpolateTimeSeries(&ts, t);` (107); `t = C(2.0);` (110); `x = InterpolateTimeSeries(interpData, t);` (111); `y = InterpolateTimeSeries(&ts, t);` (112). |
| 117–132 | 시작 시 2행 TESTING 정의 분기 안이다. `TestBalance`는 row_count=100, block_count=32로 `AllocateWetDryRowBound`를 호출한다(119–122). `SGC2_UpdateLoadBalance`에 100·−1·NULL·wet_dry_bounds를 넘긴다(126). 그 사이와 뒤에는 빈 줄만 있다. 원문: `int row_count = 100;` (119); `int block_count = 32;` (120); `WetDryRowBound* wet_dry_bounds;` (121); `AllocateWetDryRowBound(row_count, block_count, wet_dry_bounds);` (122); `SGC2_UpdateLoadBalance(100, -1, NULL, wet_dry_bounds);` (126). |
| 133–142 | 시작 시 2행 TESTING 정의 분기 안이다. `RunTests`는 선언과 중괄호만 있고 함수 본문 135–140행은 모두 빈 줄이다. 다른 시험 함수를 호출하는 문장은 없다. |
| 143–176 | 시작 시 2행 TESTING 정의 분기 안이다. 교대 배열형 `InterpolateTimeSeries`는 i·res를 0으로 초기화한다(147–149). 첫 시간보다 이르면 첫 값을 즉시 반환한다. 다음 시간의 센티널(sentinel) 기준 −0.9까지 순회하며 포함된 시간 구간에서 dt·a1·a2·res를 계산한다. 마지막 시간 이상이면 마지막 값을 복사한다. 176행 `#endif`가 TESTING 조건을 닫는다. 원문: `if (t < varlist[1]) return(varlist[0]);` (152); `while (varlist[(i + 1) * 2 + 1] > C(-0.9))` (154); `{` (155); `if (varlist[i * 2 + 1] <= t && varlist[i * 2 + 3] > t)` (156); `{` (157); `dt = varlist[i * 2 + 3] - varlist[i * 2 + 1];` (158); `a1 = (t - varlist[i * 2 + 1]) / dt;` (159); `a2 = C(1.0) - a1;` (160); `res = a1*varlist[i * 2 + 2] + a2*varlist[i * 2 + 0];` (162); `}` (163); `i++;` (165); `}` (166); `// for values greater than the end of the array - use last value` (168); `if (t >= varlist[i * 2 + 1])` (169); `res = varlist[i * 2];` (170); `return(res);` (172); `#endif` (176). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 133–141: `RunTests` 본문에는 실행문이 없다.
- 57–113: `TestInterpolate`는 두 결과와 차이를 출력한다. 결과를 단언(assert)하거나 허용오차로 비교하여 실패를 처리하는 문장은 없다.
- 121–126: wet_dry_bounds 포인터의 선언에는 초기값이 없다. 다음 문장은 이 포인터를 `AllocateWetDryRowBound`에 전달한다. 해당 외부 함수의 구현은 이 파일에 없다.
- 154–165: 보간 루프에는 일치 구간 계산 뒤 break가 없으며 센티널에 도달할 때까지 i를 증가시킨다.
