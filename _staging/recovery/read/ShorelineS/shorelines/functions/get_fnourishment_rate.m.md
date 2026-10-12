---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_fnourishment_rate.m
lines: 86
sha256: 631beb708457bb1be1a2197329407cccf5b2143d02389866598f135d3f92590a
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_fnourishment_rate.m — 판독 구간 기록

구간은 1행부터 86행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | 함수 시그니처 `function [Vend,Qend,Fac] = get_fnourishment_rate(dt,dtsteps,V0,labda0,w,mb,K,WAVE,idx_mc,x_fnour,y_fnour)` (1). 양빈(nourishment)이 모델 시작 전에 시작한 경우 남은 상대 체적을 구한다는 주석(4–6). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(8–35). |
| 36–48 | 한 간격 평가 조건 `if dtsteps==1` (37), 현재 영향 구간 파고·주기의 제곱평균 제곱근(root mean square) `H = sqrt( mean( WAVE.HSo(idx_mc).^2 ) );` (39); `T = sqrt( mean( WAVE.TP(idx_mc).^2 ) );` (40). dtsteps가 1이 아닌 분기 `else` (42) 안 균일 파랑 시계열(time series) 조건 `if isfield(WAVE.WVC,'Hs') && size(WAVE.WVC,2) == 1 && dtsteps>1` (44), 전체 시계열 파고·주기 평균 `H = sqrt( mean( WAVE.WVC.Hs.^2 ) );` (46); `T = sqrt( mean( WAVE.WVC.Tp.^2 ) );` (47). [10-12 전수 검증 정정] |
| 49–67 | 시작 시 37행 if의 42행 else 안. 이 분기는 dtsteps가 1이 아닌 경우다. 시작 시 44행 if/elseif 연쇄 안. 공간 가변 파랑 조건 `elseif isfield(WAVE.WVC,'Hs') && size(WAVE.WVC,2) > 1 && dtsteps>1` (49), 파랑 자료 지점 좌표 연결(51–52), 양빈 중심과 파랑 자료 지점 거리 `x_fnour = mean( x_fnour ); % middle of nourishment` (53); `y_fnour = mean( y_fnour );` (54); `dist = sqrt( ( x_wvc - x_fnour ).^2 + ( y_wvc - y_fnour ).^2 ); % Find closest point to nourishment` (55), 최근접 파랑 자료 지점(56), 해당 파고·주기 평균 `H = sqrt( mean( WAVE.WVC(id).Hs.^2 ) );` (57); `T = sqrt( mean( WAVE.WVC(id).Tp.^2 ) );` (58). 빈 WVC 조건 `elseif isempty(WAVE.WVC)` (60)은 현재 영향 구간 평균 `H = sqrt( mean( WAVE.HSo(idx_mc).^2 ) );` (62); `T = sqrt( mean( WAVE.TP(idx_mc).^2 ) );` (63). 조건 종료(65–66). 자료 선택·계산·호출의 원문은 `[~,id] = min(dist);` (56). 추가 원문: `x_wvc = [WAVE.WVC(:).x];` (51). `y_wvc = [WAVE.WVC(:).y];` (52). [10-12 전수 검증 정정] [10-12 전수 검증 보완] |
| 68–86 | 초기 체적 밀도 V(1)=V0·q(1)=0(69–70). 시간 루프 `for t = 1:max(dtsteps,1)` (71), 다음 인덱스 `t2=t+1;` (72), 응답 계수·지수 감소 공급률·체적 감소율·새 체적 `labda    = labda0 * ( H / (w*T ) ) ^ mb;            % response coefft2cient [-]` (73); `q(t2)    = ( V(t) * (1-exp(-1*K*labda*dt)) ) / dt;  % rate of supply of the nourishment to the beach [m3/m/s]` (74); `dVdt(t2) = -1*q(t2);                                % rate of erosion of the nourishment [m3/m/s]` (75); `V(t2)    = V(t) + dVdt(t2)*dt;                      % new volume density of the foreshore nourishment [m3/m]` (76). 마지막 q 복사(80), dtsteps+1의 체적 선택(81), 상대 체적 `Fac  = Vend / V(1);   % [-]` (82). 함수 종료·빈 줄(84–86). 자료 선택·계산·호출의 원문은 `Vend = V(dtsteps+1);  % [m3/m]` (81). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 44–65: dtsteps가 1이 아닌 경로에서 WVC가 비어 있지 않고 Hs 필드 조건을 만족하지 않으면 H·T에 값을 대입하는 else 경로가 없다. [10-12 전수 검증 보완]
- 46–47·57–58: 분기 조건은 Hs 존재만 검사하며 Tp 존재는 별도로 검사하지 않는다.
- 71·81: 반복은 max(dtsteps,1)을 상한으로 사용한다. Vend 인덱스는 dtsteps+1을 사용한다.
- 73–76: 시간 루프 안에서 H·T·w·mb·labda0를 바꾸지 않으면서 매 반복 labda를 다시 계산한다.
- 74·82: dt와 초기 V(1)을 분모로 쓰며 이 값들의 0 검사는 없다.
