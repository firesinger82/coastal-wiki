---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_nexttimestep.m
lines: 71
sha256: 83e73f2307e66d97bfdd7bc3a2200e1b980a5fb3c42000a7fcf14b3913281b47
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_nexttimestep.m — 판독 구간 기록

구간은 1행부터 71행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–42 | 함수 시그니처는 `function [TIME]=get_nexttimestep(TIME,WAVE,DUNE,WIND)` (1). 시간 간격(time step) 갱신·현재 파랑 출력 목적과 TIME·WAVE·DUNE·WIND 입력 필드를 설명한다(2–14). 갱신된 TIME 설명에도 INPUT 표제를 붙인다(12–13). 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(15–42). |
| 43–64 | 시작 시 1행 get_nexttimestep 함수 안. TIME.tprev에 현재 시간을 복사한다(44). 날짜 증가식은 `TIME.tnow=TIME.tnow + TIME.dt*365;     %calculate the current time after each time step` (45). 유의파고(significant wave height) 중앙값(median) 식은 `HSavg=median(WAVE.HStdp_mc(~isnan(WAVE.HStdp_mc)));` (48). 방향 중앙값 복원식은 `PHIavg=mod(atan2d(median(sind(WAVE.PHItdp_mc(~isnan(WAVE.PHItdp_mc(:))))),median(cosd(WAVE.PHItdp_mc(~isnan(WAVE.PHItdp_mc(:)))))),360);` (49). `if ~DUNE.used` (50)이면 날짜·파고·방향을 출력한다(51). `else` (52)에서는 가중치(weight) 초기값 `wghtNR=1;` (53). `if isfield(WIND,'Prob')` (54)이면 확장식 `wghtNR=repmat(WIND.Prob,[1,size(WIND.uz,2)]);` (55). 풍속(wind speed) 가중치와 평균 식은 `wghtWS=(WIND.uz.^1)/mean(sum(WIND.uz.^1,1));` (57); `WSavg=sum(WIND.uz.*wghtWS.*wghtNR,1);` (58); `WSavg=median(WSavg(~isnan(WSavg(:))));` (59). 풍향(wind direction) 성분·복원식은 `sdr = sum(sind(WIND.phiwnd).*wghtNR.*wghtWS,1);` (60); `cdr = sum(cosd(WIND.phiwnd).*wghtNR.*wghtWS,1);` (61); `WDavg=mod(atan2d(median(sdr(~isnan(sdr))),median(cdr(~isnan(cdr)))),360);` (62). 날짜·파랑·풍속·풍향을 출력하고 분기를 닫는다(63–64). |
| 65–71 | 시작 시 1행 get_nexttimestep 함수 안. 빈 줄과 실행시간 출력 주석을 포함한다(65–66). 완료 문구 조건은 `if TIME.tnow>TIME.tend && ~(TIME.tnow==TIME.tend && TIME.tc==0)` (67). 출력과 시간 환산식은 `fprintf(['  Run completed successfully in ' num2str((now-TIME.trealstart)*86400) 's. \n']);` (68). 분기·함수 종료와 빈 줄을 포함한다(69–71). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 48–49: HSavg는 NaN을 제외한 파고의 중앙값이다. PHIavg는 방향 사인과 코사인의 중앙값으로 계산한다.
- 67: 완료 문구 조건은 TIME.tnow>TIME.tend를 먼저 요구한다. 같은 조건식의 TIME.tnow==TIME.tend 검사는 그 요구와 함께 적혀 있다.
