---
file: models/ShorelineS/raw/source_code/shorelines/functions/prepare_tide.m
lines: 83
sha256: 4370078aa7bd62411936c433fe845fb2e6112619c272cc3a6980d9e64d109617
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# prepare_tide.m — 판독 구간 기록

구간은 1행부터 83행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–54 | 함수 시그니처는 `function [TIDE]=prepare_tide(S)` (1). 주석은 조석(tide) 지원점 좌표, M2·M4 수위 진폭·연안방향 기울기·위상·파수, 잔류 흐름(residual current)을 구동하는 평균 수면 경사, 조도(roughness), 최소 수심·한계 수심(depth of closure), 횡단면(cross-shore profile), Ttide·nT 출력을 설명한다(2–26). 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(27–54). |
| 55–70 | 로그 뒤 `if isfield(S,'tidefile') & ~isempty(S.tidefile)` (56)이면 load(57)를 호출한다. td의 1·2열을 x_stat·y_stat, 3:4열을 eta_stat, 5:6열을 detads_stat, 7:8열을 phi_stat, 9:10열을 k_stat, 11열을 ss_stat에 복사한다(58–64). cf·hmin·hclosure는 같은 이름의 S 필드에서 복사한다(65–67). `if isfield(S,'profile')` (68)이면 S.profile을 S.tideprofile에 복사한다(69). S 필드의 숫자 기본값 대입은 없다. |
| 71–83 | 시작 시 56행 조석 파일 분기 안. load(S.tideprofile)를 호출한다(71). `TIDE.x  = [xz(1,1):S.tidedx:xz(end,1)];` (72), `TIDE.zb = interp1(xz(:,1),xz(:,2),TIDE.x);` (73)로 횡단면을 만든다. 고정값은 `TIDE.Ttide              = 745*60;` (74), `TIDE.nT                 = 24;` (75). n은 S.tiden에서 복사한다(76). struct2log 호출은 주석이다(78). 56행의 `else` (79)는 TIDE를 빈 배열로 만든다(80). 빈 줄과 조건·함수 종료를 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 56: 필드 존재 검사와 비어 있음 검사는 &로 결합한다.
- 24·74–75: 머리말은 Ttide를 spring-neap cycle의 길이라고 설명한다. 실행문은 745*60을 고정 대입하며 nT에는 24를 고정 대입한다.
- 58–59·72: 지원점 좌표를 복사하고 횡단면 축을 구성하는 블록에는 xyoffset 보정식이 없다.
