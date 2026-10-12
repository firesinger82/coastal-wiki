---
file: models/ShorelineS/raw/source_code/shorelines/functions/wave_angles.m
lines: 146
sha256: 1c978601c736e1aa436a65d955a71be928037f3308e97d7afa4b60c9fece3686
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# wave_angles.m — 판독 구간 기록

구간은 1행부터 146행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–69 | 함수 시그니처(1), 파향 임계각(critical wave angle)과 최대 수송 QSmax 목적(4–5), COAST·WAVE·TRANSP 입력과 출력 설명(7–40), 저작권·LGPL·무보증·빈 줄(42–69). pswell의 주석 범위는 0–100이다(28). 입력 필드 기본값 대입은 이 구간에 없다. 원문: `function [WAVE,TRANSP]=wave_angles(COAST,WAVE,TIDE,TRANSP,STRUC)` (1). |
| 70–94 | 시작 시 1행 함수 안. RAY가 아니면 파향·파고를 복사하고 dnearshore를 COAST.nq만큼 복제하여 분산(dispersion) 관계 get_disper를 호출한다(70–74). TP 길이가 1이면 복제한다(75–77). RAY else에서는 c1·c2·QSoffset를 가져온다(78–82). CERC1 임계각 45와 CERC2 42.39에 관한 주석이 있고 dPHIcrit·dPHIcritbr를 45로, QSmax를 0으로 초기화한다(84–93). 원문: `if ~strcmpi(TRANSP.trform,'RAY')` (70), `PHIlocal = WAVE.PHItdp;` (71), `HSlocal  = WAVE.HStdp;` (72), `DEPlocal = repmat(WAVE.dnearshore,[1,COAST.nq]);` (73), `[~,WAVE.ctdp,~,WAVE.ntdp]=get_disper(DEPlocal,WAVE.TP);` (74), `if length(WAVE.TP)==1` (75), `WAVE.TP=repmat(WAVE.TP,[1,COAST.nq]);` (76), `else` (78), `c1 = WAVE.c1;` (79), `c2 = WAVE.c2;` (80), `QSoffset = WAVE.QSoffset;` (81), `WAVE.dPHIcrit=repmat(45,[1,COAST.nq]);` (90), `WAVE.dPHIcritbr=repmat(45,[1,COAST.nq]);` (91), `WAVE0=WAVE;` (92), `TRANSP.QSmax=zeros(1,COAST.nq);` (93). [10-12 전수 검증 정정] |
| 95–128 | 시작 시 1행 함수 안. CERC·CERC2·RAY 분기는 각각 45·42.39·abs(1/(sqrt(2)*c2))로 임계각을 설정한 뒤 transport를 QSmax 모드로 호출한다(95–108). sphimax가 비어 있지 않고 숫자이면 sphimax·sphibrmax를 복제하고 transport를 호출한다(110–117). 숫자가 아닌 else는 get_Sphimax 결과의 중앙값(median)에서 표준편차(standard deviation)를 빼 저장한다(118–123). sphimax가 빈 else는 get_Sphimax만 호출한다(124–126). 원문: `if strcmpi(TRANSP.trform,'CERC')` (95), `WAVE.dPHIcrit=repmat(45,[1,COAST.nq]);` (96), `WAVE0.dPHItdp=WAVE.dPHIcrit;` (97), `TRANSP=transport(TRANSP,WAVE0,TIDE,STRUC,'QSmax');` (98), `elseif strcmpi(TRANSP.trform,'CERC2')` (100), `WAVE.dPHIcrit=repmat(42.39,[1,COAST.nq]);` (101), `WAVE0.dPHItdp=WAVE.dPHIcrit;` (102), `TRANSP=transport(TRANSP,WAVE0,TIDE,STRUC,'QSmax');` (103), `elseif strcmpi(TRANSP.trform,'RAY')` (105), `WAVE.dPHIcrit=abs(1./(sqrt(2).*c2));` (106), `WAVE0.dPHItdp=WAVE.dPHIcrit;` (107), `TRANSP=transport(TRANSP,WAVE0,TIDE,STRUC,'QSmax');` (108), `elseif ~isempty(WAVE.sphimax)` (110), `if isnumeric(WAVE.sphimax)` (111), `WAVE.dPHIcrit=repmat(WAVE.sphimax,[1,COAST.nq]);` (113), `WAVE.dPHIcritbr=repmat(WAVE.sphibrmax,[1,COAST.nq]);` (114), `WAVE0.dPHItdp=WAVE.dPHIcrit;` (115), `WAVE0.dPHIbr=WAVE.dPHIcritbr;` (116), `TRANSP=transport(TRANSP,WAVE0,TIDE,STRUC,'QSmax');` (117), `else % if strcmpi(WAVE.sphimax,'estimate')` (118), `[WAVE,TRANSP]=get_Sphimax(WAVE,TIDE,TRANSP,STRUC);` (120), `WAVE.sphimax=median(WAVE.dPHIcrit)-std(WAVE.dPHIcrit);` (121), `WAVE.sphibrmax=median(WAVE.dPHIcritbr)-std(WAVE.dPHIcritbr);` (122), `else` (124), `[WAVE,TRANSP]=get_Sphimax(WAVE,TIDE,TRANSP,STRUC);` (126). |
| 129–146 | 시작 시 1행 함수 안. suppresshighangle=1이면 파랑 조건 루프에서 근해 각도를 부호 유지 임계각으로 제한하고 임계각 초과 인덱스의 쇄파각도 제한한다(130–135). refraclimit=180.0으로 외해각과의 차이를 검사하여 근해·쇄파각을 ±180으로 대입한다(139–144). 함수 끝과 빈 줄(145–146). 원문: `if TRANSP.suppresshighangle==1` (130), `for kk=1:size(WAVE.dPHItdp,1)` (131), `id=abs(WAVE.dPHItdp(kk,:))>WAVE.dPHIcrit;` (132), `WAVE.dPHItdp(kk,:)=sign(WAVE.dPHItdp(kk,:)).*min([abs(WAVE.dPHItdp(kk,:));WAVE.dPHIcrit],[],1);` (133), `WAVE.dPHIbr(kk,id)=sign(WAVE.dPHIbr(kk,id)).*min([abs(WAVE.dPHIbr(kk,id));WAVE.dPHIcritbr(id)],[],1);` (134), `refraclimit=180.0;` (139), `WAVE.dPHItdp((WAVE.dPHItdp-WAVE.dPHIo)<-refraclimit)=-refraclimit;` (140), `WAVE.dPHItdp((WAVE.dPHItdp-WAVE.dPHIo)>refraclimit)=refraclimit;` (141), `refraclimit=180.0;` (142), `WAVE.dPHIbr((WAVE.dPHIbr-WAVE.dPHIo)<-refraclimit)=-refraclimit;` (143), `WAVE.dPHIbr((WAVE.dPHIbr-WAVE.dPHIo)>refraclimit)=refraclimit;` (144). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 71–72·79·81: PHIlocal·HSlocal·c1·QSoffset는 지역 대입 이후 이 파일에서 참조되지 않는다.
- 74–77: get_disper 호출은 TP를 COAST.nq 크기로 복제하는 조건보다 먼저 실행된다.
- 85·95–100: 주석은 CERC1의 임계각을 45라고 적는다. 명시적인 수송식 분기는 CERC·CERC2·RAY이며 CERC1 조건은 없다.
- 139–144: 외해각과의 차이로 제한 조건을 검사하지만 대입값은 외해각에 한계를 더한 값이 아니라 ±refraclimit 자체이다.
