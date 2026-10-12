---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_fnourishment.m
lines: 143
sha256: 743c7038aa0f9c417c54f6b57a9258d9f6d659134145a289e233f93f811a5d7b
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_fnourishment.m — 판독 구간 기록

구간은 1행부터 143행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–45 | 함수 시그니처 `function [FNOUR] = get_fnourishment(TIME,COAST,FNOUR,WAVE,i_mc)` (1). 해안 전면 양빈(shoreface nourishment)의 순간 공급항(source term)과 남은 체적을 계산하는 목적·입출력 주석(4–17). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(18–45). |
| 46–66 | 최소 체적 기준 `eps=1e-6;  % default minimum volume for shoreface nourishment` (46), q_tot를 COAST.x 크기 0 배열로 초기화(47). 양빈 활성 조건 `if FNOUR.fnourish == 1 % if shoreface nourishments are activated` (49), 저장 시간 인덱스 `t = TIME.it+1;` (50), 양빈 루프 `for n = 1:FNOUR.n % for each shoreface nourishment` (52). 위치·폭·응답 계수·확산 계수(diffusion coefficient)·초기 체적 복사(55–61). get_fnourishment_fraction 호출 `[fraction,i_mc_rel,idx,dxnour]   = get_fnourishment_fraction(xn,yn,COAST.x_mc,COAST.y_mc,COAST.n_mc,COAST.ds_mc,COAST.shadow_mc);` (62), 관련 구간·그림 인덱스 저장(63–64), 해당 양빈 q를 0 배열로 초기화(65). 자료 선택·계산·호출의 원문은 `FNOUR.q_tot = zeros(size(COAST.x)); % default initialization value of 0 for the rate at which shoreface nourishments nourish the coast` (47). |
| 67–94 | 시작 시 49행 활성 참 분기·52행 n 루프 안. 관련 구간 조건 `if ismember(i_mc,i_mc_rel) % only for relevant segments, otherwise q stays zero as initiated above` (67). 양빈 시작 시각이 모델 시작 시각 이하인 초기화 조건 `if TIME.tnow >= FNOUR.tstart(n) && FNOUR.tstart(n) <= TIME.timenum0 && TIME.nt == 0` (69), 체적 밀도 `V0dens    = V0 / dxnour(i_mc);` (72), idx 복사(73), 하루 간격·모델 시작 전 경과 시간·반복 수 `dt        = 1 * 24 * 3600; % timestep used for the foreshore nourishment evolution [s]` (74); `delta_t   = (TIME.timenum0 - FNOUR.tstart(n)) * 24 * 3600; % time between nourishment start and start of modeltime [in s]` (75); `dtsteps   = ceil(delta_t/dt); % number of steps` (76), get_fnourishment_rate 호출(77), 총 체적·구간 체적 `FNOUR.Vt(n,t) = V0 * Fac;` (79); `FNOUR.Vt_mc{i_mc}(n,t) = V0 * Fac * fraction(i_mc);` (80). 69행 분기가 선택되지 않은 경우의 총 체적 0 초기화 `elseif TIME.tnow >= FNOUR.tstart(n) && FNOUR.Vt(n,t) == 0` (82)는 총량 V0 복사(85), 구간 체적 `FNOUR.Vt_mc{i_mc}(n,t) = V0 * fraction(i_mc);` (86). 시작 전 `elseif TIME.tnow < FNOUR.tstart(n)` (88)은 두 체적 0(90–91). 자료 선택·계산·호출의 원문은 `[~,~,Fac] = get_fnourishment_rate(dt, dtsteps, V0dens, labda0, w, mb, K, WAVE, idx_mc, xn, yn);` (77). [10-12 전수 검증 정정] |
| 95–122 | 시작 시 49행 활성 참 분기·52행 n 루프·67행 관련 구간 참 분기 안. 남은 체적 및 시작 시각 조건 `if TIME.tnow > FNOUR.tstart(n) && FNOUR.Vt(n,t) > 10*eps` (96). 구간 체적·밀도 `V1          = FNOUR.Vt(n,t) * fraction(i_mc);` (98); `V1dens      = V1 / dxnour(i_mc); % [m3/m]` (99), idx 복사(100), 연 단위를 초로 변환 `dt          = TIME.dt * 365 * 24 * 60 * 60; % yrs -> [s]` (101), dtsteps=1(102), get_fnourishment_rate 호출(103). 공급률·새 구간 체적·체적 하한 `FNOUR.q{t,i_mc}(n,idx{i_mc}) = Qend * 60 * 60 * 24 * 365; % set the rate of supply by the shoreface nourishment to the coast [m3/m/yr]` (105); `FNOUR.Vt_mc{i_mc}(n,t+1) = V2dens * dxnour(i_mc);         % the new volume of the shoreface nourishment after supply to the coast [m3]` (106); `FNOUR.Vt_mc{i_mc}(n,t+1) = max(FNOUR.Vt_mc{i_mc}(n,t+1),eps);` (110). 무침식 `else` (112)은 이전 체적 복사(114). 관련 구간 조건 종료(117). 모든 양빈 공급 합 `FNOUR.q_tot = sum(FNOUR.q{t,i_mc},1);` (120), n 루프 종료(121). 자료 선택·계산·호출의 원문은 `[V2dens,Qend] = get_fnourishment_rate(dt, dtsteps, V1dens, labda0, w, mb, K, WAVE, idx_mc, xn, yn);` (103). 추가 원문: `FNOUR.Vt_mc{i_mc}(n,t+1) = FNOUR.Vt_mc{i_mc}(n,t);` (114). [10-12 전수 검증 보완] |
| 123–134 | 시작 시 49행 활성 참 분기 안. 마지막 해안 구간 조건 `if i_mc==COAST.n_mc` (125), 양빈 루프 `for n = 1 : FNOUR.n % nr of nourishments` (126), 관련 구간 번호 최댓값 크기의 temp 0 배열(127), 관련 구간 루프 `for j = FNOUR.i_mc_rel{n}(end,:) % nr of relevant segments` (128), 각 구간 다음 체적 복사(129), 총 남은 체적 `FNOUR.Vt(n,t+1) = sum( temp );` (131). 루프·조건 종료(130·132–133). 자료 선택·계산·호출의 원문은 `temp=zeros(1,max(FNOUR.i_mc_rel{n}(end,:)));` (127); `temp(j)  =  FNOUR.Vt_mc{j}(n,t+1);` (129). |
| 135–143 | 시작 시 49행 활성 참 분기 안. 첫 구간 조건 `if i_mc==1` (136)은 q_tot_mc에 q_tot 복사(137). 뒤 구간 `else` (138)은 NaN 구분자 연결(139). 조건·활성 조건 종료와 빈 줄(140–143). 추가 원문: `FNOUR.q_tot_mc=[FNOUR.q_tot_mc,nan,FNOUR.q_tot];` (139). [10-12 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16·47·120: 출력 주석의 필드 이름은 q_grid_tot이며 실행 대입 필드는 q_tot이다.
- 69·82·96: 체적 초기화는 tnow>=tstart를 사용한다. 침식 계산은 tnow>tstart를 사용한다.
- 82·85·110: 69행 분기가 선택되지 않은 경우에 82행은 TIME.tnow >= FNOUR.tstart(n)과 해당 시각 총 체적 FNOUR.Vt(n,t) == 0을 검사하여 V0를 대입한다. 침식 계산 뒤 구간 체적에는 eps 하한을 적용한다. [10-12 전수 검증 정정]
- 49·136–142: q_tot_mc 저장은 fnourish==1 분기 안에 있다. 비활성 경로는 q_tot만 0으로 초기화한다.
- 1·142–143: 마지막 end는 49행 if를 닫으며 별도의 함수 end는 없다.
