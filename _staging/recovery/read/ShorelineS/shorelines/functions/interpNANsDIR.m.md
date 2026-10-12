---
file: models/ShorelineS/raw/source_code/shorelines/functions/interpNANsDIR.m
lines: 68
sha256: 903f20b2bf3c00c10370703c24060dd63b74ace034b30bf5442e7e9a3286102f
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# interpNANsDIR.m — 판독 구간 기록

구간은 1행부터 68행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | 함수 시그니처(1). 방향(direction) 데이터의 NaN 보간과 nearest 외삽을 설명하는 주석·예시(2–11). 원문: `function [data2]=interpNANsDIR(data)` (1). |
| 12–39 | 시작 시 1행 interpNANsDIR 함수 안. 2020년 저작권·연락처, LGPL 2.1 이상·무보증 안내와 빈 줄(12–39). |
| 40–47 | 시작 시 1행 interpNANsDIR 함수 안. 열 수가 행 수와 2보다 모두 크면 data를 전치한다(41–44). data1에 입력을 복사하고, 첫 비-NaN 값으로 dir0를 정한다(46–47). 원문: `rotate=0;` (40), `if max(size(data,1),2)<size(data,2)` (41), `rotate=1;` (42), `data=data';` (43), `data1 = data;` (46), `dir0 = data(find(~isnan(data),1));` (47). [10-12 전수 검증 정정] |
| 48–62 | 시작 시 1행 interpNANsDIR 함수 안. 각 데이터 값에 대한 루프에서 비-NaN 값만 처리한다(48–49). 이전 방향의 360도 배수와 반대 방향을 구한다(51–52). 차이가 180도를 넘을 때 조건에 따라 오프셋(offset)에 360을 더하거나 뺀다(53–57). 보정값을 data1에 넣고 dir0를 갱신한다(58–59). 루프·조건 종료와 빈 줄(60–62). 원문: `for ii=1:length(data)` (48), `if ~isnan(data(ii));` (49), `dir = data(ii);` (50), `diroffset = dir0-mod(dir0,360);` (51), `dir0B = mod(dir0+180,360);` (52), `if dir<dir0B && abs(dir+diroffset-dir0)>180` (53), `diroffset = diroffset+360;` (54), `elseif dir>dir0B && abs(dir+diroffset-dir0)>180` (55), `diroffset = diroffset-360;` (56), `data1(ii) = dir+diroffset;` (58), `dir0 = data1(ii);` (59). |
| 63–68 | 시작 시 1행 interpNANsDIR 함수 안. interpNANs를 nearest로 호출한 결과를 mod 360으로 되돌린다(63). 전치했던 배열이면 출력도 전치한다(65–67). 함수 종료(68). 원문: `data2 = mod(interpNANs(data1,'nearest'),360);` (63), `if rotate==1` (65), `data2 = data2';` (66). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 47: 첫 비-NaN 값을 찾기 전에 전부 NaN인 입력을 따로 처리하는 분기는 없다.
- 53–56·63: 방향의 오프셋 조정 기준은 180이며, 조정 크기와 반환의 나머지 연산 기준은 360으로 고정되어 있다.
