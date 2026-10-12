---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_timestep.m
lines: 80
sha256: 67440ebdbffdf5355a0ab7e5c09948ca47f4ffe4cac49b92e73cbcddc946f6aa
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_timestep.m — 판독 구간 기록

구간은 1행부터 80행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–50 | 함수 시그니처는 `function [TIME]=get_timestep(TIME,COAST,TRANSP,WAVE)` (1). 수송률(transport rate)·격자(grid) 속성에 따른 자동 시간 간격(automatic time step) 계산을 설명한다(2–6). TIME·COAST·TRANSP 입력 필드와 연 단위 출력을 설명한다(7–22). 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(23–50). |
| 51–65 | 시작 시 1행 get_timestep 함수 안. `if TIME.tc<0` (51)이면 adt에 TIME.dt를 복사한다(52). `else` (53)에서는 최소 점 간격·활성 높이(active height) 식은 `dsmin=min(diff(COAST.s));` (54), `h0min=min(COAST.h0);` (55). `if ~isnan(max(abs(TRANSP.QSmax)))` (56)이면 `if size(TRANSP.QSmax,1)>1` (57)에서 확률 가중치(weight) 확장과 수송 합산식 `wghtNR=repmat(WAVE.Prob,[1,size(TRANSP.QSmax,2)]);` (58), `TRANSP.QSmax=sum(TRANSP.QSmax.*wghtNR,1);` (59). 자동 간격식은 `adt=dsmin^2*h0min / (4*max(abs(TRANSP.QSmax)));` (61). 두 내부 분기를 닫는다(60·62). 실제 수송 QS를 쓰는 대체식은 주석이다(63–65). |
| 66–80 | 시작 시 1행 get_timestep 함수 안. 시작 시 53행 TIME.tc<0 불성립 else 안. 최소 1분 제한식은 `adt=max(adt,1/365/24/60);    % use at least a 1 minute time step` (66). `if COAST.i_mc>1` (67)이면 구간별 최솟값 식 `adt=min(adt,TIME.adt);   % make sure to use the minimum adt that is computed for all coastal segments` (68). `if TIME.it>1` (70)이면 adt0에 이전 TIME.dt를 복사하고(71), 최대 100배·최소 0.001배 제한식 `adt=min(adt,100*adt0);     % make sure adt is not more than 100 times larger than previous cycle timestep 'adt0'` (72); `adt=max(adt,0.001*adt0);   % make sure adt is not more than 1000 times smaller than previous cycle timestep 'adt0'` (73). `else` (74)에서는 최초 최대 1일 제한식 `adt=min(adt,1/365);       % use at most 1 day time step initially` (75). 두 분기를 닫고(76–77), TIME.adt에 adt를 복사한다(78). 함수 종료·마지막 빈 줄을 포함한다(79–80). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 53–62·66: TIME.tc>=0이고 max(abs(TRANSP.QSmax))가 NaN이면 61행 adt 대입을 건너뛴다. 이 경로 앞에 다른 adt 초기화는 없다.
- 58–59·1·78: 여러 파랑 조건이면 지역 TRANSP.QSmax를 확률 가중 합으로 덮어쓴다. 함수 출력은 TIME 하나이다.
- 61: 자동 간격식은 max(abs(TRANSP.QSmax))로 나눈다. 이 값이 0인지 확인하는 조건은 이 분기 안에 없다.
