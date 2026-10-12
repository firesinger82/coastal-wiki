---
file: models/ShorelineS/raw/source_code/shorelines/functions/collect_variables.m
lines: 151
sha256: b22aa6e0a198c825898b2b6c427c56eeca3cfe110e3136d3f4a0d5397f4e15a5
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# collect_variables.m — 판독 구간 기록

구간은 1행부터 151행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | 함수 시그니처 `function [COAST,WAVE,TRANSP]=collect_variables(COAST,WAVE,TRANSP,DUNE,MUD,GROYNE,TIME,i_mc)` (1). 구간별 자료를 _mc 접미사의 전체 배열로 모으는 목적과 입력·출력 필드 주석(2–21). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(22–49). |
| 50–65 | 해안·사구(dune)·진흙 필드 목록(51–53). 사구 조건 `if DUNE.used` (54), 빈 xtill 조건 `if isempty(DUNE.xtill)` (55)이면 마지막 필드를 `fieldsdune=fieldsdune(1:end-1);` (56)로 제거한다. 사구 필드 연결식은 `fields={fields{:},fieldsdune{:}};` (58). 진흙 조건 `if MUD.used` (60)이면 진흙 필드 연결(61). COAST·WAVE·TRANSP 수집 목록을 fieldnm{1..3}에 저장(63–65). 추가 원문: `fields={fields{:},fieldsmud{:}};` (61). [10-12 전수 검증 보완] |
| 66–98 | 첫 구간 조건 `if i_mc==1` (66). COAST 루프 `for kk=1:length(fieldnm{1})` (67)는 각 필드를 _mc에 복사(68). WAVE 루프 `for kk=1:length(fieldnm{2})` (71). 첫 세 PHI 조건 `if ~isempty(findstr(fieldnm{2}{kk},'PHI')) && kk<=3` (73)이면 regexprep으로 HS 이름 생성(75), 파고 하한·확률 가중·파고 제곱 가중·사인 및 코사인 평균·방향 계산 `HStdp0=max(WAVE.(fldnmHS),1e-6);` (76); `wghtNR=repmat(WAVE.Prob,[1,size(WAVE.(fieldnm{2}{kk}),2)]);` (77); `wghtHS=HStdp0.^2;` (78); `sdr = sum(sind(WAVE.(fieldnm{2}{kk})).*wghtNR.*wghtHS,1);` (79); `cdr = sum(cosd(WAVE.(fieldnm{2}{kk})).*wghtNR.*wghtHS,1);` (80); `WAVE.(fieldnm{2}{kk})=mod(atan2d(sdr,cdr),360);` (81). 다행 배열 분기 `elseif size(WAVE.(fieldnm{2}{kk}),1)~=1` (82)의 가중·평균 `wghtNR=repmat(WAVE.Prob,[1,size(WAVE.(fieldnm{2}{kk}),2)]);` (84); `WAVE.(fieldnm{2}{kk})=sum(WAVE.(fieldnm{2}{kk}).*wghtNR,1);` (85). WAVE 결과 _mc 복사(87). TRANSP 루프 `for kk=1:length(fieldnm{3})` (90), 다행 조건 `if size(TRANSP.(fieldnm{3}{kk}),1)~=1` (91), 가중 수송 평균 `TRANSP.(fieldnm{3}{kk})=sum(TRANSP.(fieldnm{3}{kk}).*repmat(WAVE.Prob,[1,size(TRANSP.(fieldnm{3}{kk}),2)]),1);` (93), _mc 복사(95). rmfield 호출들은 주석 처리(69·88·96). 추가 원문: `COAST.([(fieldnm{1}{kk}),'_mc'])=COAST.(fieldnm{1}{kk});` (68). `fldnmHS=regexprep(fieldnm{2}{kk},'PHI','HS');` (75). `WAVE.([(fieldnm{2}{kk}),'_mc'])=WAVE.(fieldnm{2}{kk});` (87). `TRANSP.([(fieldnm{3}{kk}),'_mc'])=TRANSP.(fieldnm{3}{kk});` (95). [10-12 전수 검증 보완] |
| 99–118 | 시작 시 66행 if의 대체 분기. `else` (99), COAST 루프 `for kk=1:length(fieldnm{1})` (100)에서 NaN을 사이에 넣어 연결(101). WAVE 루프 `for kk=1:length(fieldnm{2})` (104), 다행 조건 `if size(WAVE.(fieldnm{2}{kk}),1)~=1` (105), 가중 평균 `WAVE.(fieldnm{2}{kk})=sum(WAVE.(fieldnm{2}{kk}).*repmat(WAVE.Prob,[1,size(WAVE.(fieldnm{2}{kk}),2)]),1);` (106), _mc 연결(108). TRANSP 루프 `for kk=1:length(fieldnm{3})` (111), 다행 조건 `if size(TRANSP.(fieldnm{3}{kk}),1)~=1` (112), 가중 수송 평균 `TRANSP.(fieldnm{3}{kk})=sum(TRANSP.(fieldnm{3}{kk}).*repmat(WAVE.Prob,[1,size(TRANSP.(fieldnm{3}{kk}),2)]),1);` (113), _mc 연결(115). rmfield 호출은 주석 처리(102·109·116). 바깥 조건 종료(118). 추가 원문: `COAST.([(fieldnm{1}{kk}),'_mc'])=[COAST.([(fieldnm{1}{kk}),'_mc']),nan,COAST.(fieldnm{1}{kk})];` (101). `WAVE.([(fieldnm{2}{kk}),'_mc'])=[WAVE.([(fieldnm{2}{kk}),'_mc']),nan,WAVE.(fieldnm{2}{kk})];` (108). `TRANSP.([(fieldnm{3}{kk}),'_mc'])=[TRANSP.([(fieldnm{3}{kk}),'_mc']),nan,TRANSP.(fieldnm{3}{kk})];` (115). [10-12 전수 검증 보완] |
| 119–139 | dSds_mc를 비운다(119). diff_mc의 NaN을 0으로 바꾸고 logical로 변환(120–121). 마지막 구간·초기 반복 조건 `if i_mc==COAST.n_mc && TIME.it==0` (124), get_reconnectedgroynes 호출(125), x0_mc·y0_mc 복사(126–127), 구간 수 `COAST.n0_mc=length(find(isnan(COAST.x0_mc)))+1;` (128). 마지막 구간 조건 `if i_mc==COAST.n_mc` (130), 현재 좌표·수송점·방향을 x1_mc·y1_mc·xq1_mc·yq1_mc·PHIc1_mc·PHIcxy1_mc로 복사(131–132·134–137), 구간 수 `COAST.n1_mc=length(find(isnan(COAST.x1_mc)))+1;` (133). 자료 선택·계산·호출의 원문은 `[COAST0]=get_reconnectedgroynes(COAST,GROYNE);` (125). 추가 원문: `WAVE.diff_mc(isnan(WAVE.diff_mc))=0;` (120). `WAVE.diff_mc=logical(WAVE.diff_mc);` (121). [10-12 전수 검증 보완] |
| 140–151 | WAVE의 cbr·nbr·ctdp·ntdp·dPHItdp_sh·dPHIcritbr를 rmfield로 제거(141–146). 마지막 COAST.i_mc 조건 `if COAST.i_mc==COAST.n_mc` (148)이면 dPHIcrit_mc0에 dPHIcrit_mc 복사(149). 함수 종료(151). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 73–85·104–106: 첫 해안 구간의 첫 세 PHI 필드는 파고 제곱과 확률로 원형 평균을 계산한다. 뒤 구간의 다행 파향 배열은 다른 WAVE 필드와 같은 확률 가중 산술합을 사용한다.
- 119: 각 호출은 COAST.dSds_mc를 빈 배열로 대입한다.
- 141–146: rmfield 호출 앞에 해당 필드의 존재를 확인하는 조건은 없다.
- 124·130·148: 초기 좌표와 현재 좌표 저장 조건은 인수 i_mc를 사용한다. 마지막 dPHIcrit 저장 조건은 COAST.i_mc를 사용한다.
