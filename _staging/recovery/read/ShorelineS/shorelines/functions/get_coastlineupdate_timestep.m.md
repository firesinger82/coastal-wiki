---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_coastlineupdate_timestep.m
lines: 129
sha256: 08f9c072002e9a11b1c74551dcd9a353a8dd5f305ae7f3c07fa66213280502ea
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_coastlineupdate_timestep.m — 판독 구간 기록

구간은 1행부터 129행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | 함수 시그니처 `function [TIME, WAVE] = get_coastlineupdate_timestep(TIME, BATHY, WAVE, FORMAT)` (1). TIME·BATHY·WAVE·FORMAT 입력과 TIME·WAVE 출력 설명(4–9). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(10–37). |
| 38–46 | 다음 파랑 조건 시각의 기본 대체값 `WVCtime=1e9;` (39). 시계열(time series) 조건 `if (~isempty(WAVE.wvcfile) \|\| isfield(WAVE,'Wavematfile')) && ~isempty(WAVE.WVC(1).timenum)` (40), 현재보다 나중인 시각 검색 `indxw=find((WAVE.WVC(1).timenum-TIME.tnow)>0,1);` (41), 인덱스 존재 조건 `if ~isempty(indxw)` (42)에서 해당 시각 복사(43). |
| 47–69 | 최소 시간 간격 `eps=1e-5; % minimum time step` (48). 끝 시각 복사(49), 끝 시각 조건 `if TIME.tnow+eps>tend` (50)의 연장 `tend=TIME.tnow+eps;` (51). 그림 일정 조건 `if (isempty(FORMAT.slplot) \|\| FORMAT.tplot==0)` (55)의 기본 시각 `FORMAT.tplot=1e9;` (56). 수심 갱신 조건 `if (isempty(BATHY.bathyupdate) \|\| BATHY.tupdate==0)` (60)의 기본 시각 `BATHY.tupdate=1e9;` (61). tc 기본값 `tc=1;` (65), 유연 시간 비 조건 `if TIME.tc>0` (66)이면 TIME.tc 복사(67). |
| 70–95 | 적응 간격·다음 파랑·끝 시각·그림·수심 갱신 시각의 최솟값 연속 식 `dtnew=min([tc*TIME.adt,...` (71); `(WVCtime-TIME.tnow)/365,...` (72); `(tend-TIME.tnow)/365,...` (73); `(FORMAT.tplot-TIME.tnow)/365,...` (74); `(BATHY.tupdate-TIME.tnow)/365]);` (75). 기존 dt·dtsteps·adt를 store에 복사(77–79). 시간 가변 분기 `if TIME.tc>0` (82). 파랑 조건 인덱스 부재 `if isempty(WAVE.iwc)` (84)는 dtnew 복사·dtsteps=0(85–86). 새 기후 조건 `elseif TIME.dtsteps==0` (87)는 dtnew 복사(89), 분할 수·반복 횟수 `fac=ceil(TIME.dt0/(tc*TIME.adt));` (90); `TIME.dtsteps=max(fac-1,0);` (91). 기후 반복 `else` (92)의 횟수 감소 `TIME.dtsteps=max(TIME.dtsteps-1,0);` (93). |
| 96–121 | 시작 시 82행 if/elseif 연쇄 안. 임시 작은 간격 분기 `elseif TIME.dtsteps>0 && TIME.tc==0` (96), 남은 횟수 `TIME.dtsteps=max(TIME.dtsteps-1,0);` (98). 간격 축소 조건 `if TIME.dt>tc*TIME.adt` (99), 분할 수·dt·남은 횟수 `fac=ceil(TIME.dt/(tc*TIME.adt));` (101); `TIME.dt=TIME.dt/fac;` (102); `TIME.dtsteps=(TIME.dtsteps+1)*fac-1;` (103). 간격 확대 조건 `elseif 2*TIME.dt<tc*TIME.adt && mod(TIME.dtsteps,2)==0` (104), 남은 시간·분할 수·dt·횟수 `dt2=(TIME.dtsteps+1)*TIME.dt; % remaining time` (106); `fac=ceil(dt2/(tc*TIME.adt));` (107); `TIME.dt=dt2/fac;` (108); `TIME.dtsteps=fac-1;` (109). 새 임시 분할 조건 `elseif TIME.dt0>(tc*TIME.adt) && TIME.tc==0` (111), 분할 수·횟수·dt `fac=ceil(TIME.dt0/(tc*TIME.adt));` (114); `TIME.dtsteps=fac-1;` (115); `TIME.dt=TIME.dt0/fac;` (116). 고정 분기 `else` (117)는 dt0 복사(119). 조건 종료(120). |
| 122–129 | 비활성 디버그 조건 `if 0` (122). dts 필드 조건·초기화 `if ~isfield(TIME,'dts');TIME.dts=[];end` (124), 간격 배열 연결(125), 누적 시간과 기준 간격 그림·축 범위 계산을 포함한 문장 `figure(11);clf;plot([0,cumsum(TIME.dts)],zeros(1,length(TIME.dts)+1),'b*');hold on;plot([0,cumsum(repmat(TIME.dts(1),[1 length(TIME.dts)]))],zeros(1,length(TIME.dts)+1),'ro');xlim([0,sum(TIME.dts)*1.01]);` (126). 분기·함수 종료·빈 줄(127–129). 추가 원문: `TIME.dts=[TIME.dts,TIME.dt];` (125). [10-12 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 77–79: store.dt·dtsteps·adt에 복사한 값은 이후 참조하지 않는다.
- 71–75·82–119: dtnew는 여러 일정 시각으로 제한하여 계산한다. TIME.dt에 dtnew를 대입하는 문장은 TIME.tc>0 분기 안에만 있다. [10-12 전수 검증 정정]
- 55–62·1: FORMAT·BATHY 일정 값을 지역적으로 대입한다. 이 구조체들은 함수 출력 목록에 없다.
- 48·50–51·71–75: eps=1e-5는 tend를 늘리는 데 사용한다. dtnew 전체에 max(dtnew,eps)를 적용하는 문장은 없다.
