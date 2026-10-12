---
file: models/ShorelineS/raw/source_code/shorelines/functions/prepare_dunes.m
lines: 147
sha256: 39e1d6e1e7066801f9ee3c4b90b40d154927ff15a6041f3d1baba81cc8c2d395
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# prepare_dunes.m — 판독 구간 기록

구간은 1행부터 147행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–72 | 함수 시그니처는 `function [DUNE]=prepare_dunes(S,COAST)` (1). 출력 주석은 사구(dune)의 버름(berm) 폭, 사구 기슭(dune foot)·마루(dune crest) 고도, 침식 계수, 월파 퇴적(overwash) 계수, 퇴적물·공기 밀도, 입경, 공극률(porosity), 취송거리(fetch length) 계수, 최대 경사, 시간 간격을 설명한다(2–29). 점착성 층(cohesive layer)·틸(till)의 cstill·xtill·perctill 및 바람·수위·처오름(runup) 필드 설명을 포함한다(30–44). perctill의 주석 범위는 0부터 100이다(33). 같은 주석의 모래 백분율 식은 `100-perctill`이다(33). 이 파일에는 S 필드 기본값 대입이 없다. 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(45–72). [10-12 전수 검증 보완] |
| 73–113 | 로그 뒤 DUNE 구조체를 만든다(73–74). used는 S.dune, A는 S.aoverwash, dt는 S.dtdune에서 복사한다(75·87·110). ldbdune·wndfile·uz·z·phiwnd0·watfile·swl0·cs·cstill·xtill·perctill·ds0·duneaw·rhos·rhoa·g·d50·d50r·k·kw·porosity·segmaw·xdune·ydune·wberm·dfelev·dcelev·runupform·runupfactor·maxslope·csmodel·temp를 같은 이름의 S 필드에서 복사한다(76–112). xdune0·ydune0는 S.xdune·S.ydune에서 복사한다(101–102). `DUNE.wberm_mc0=[];` (104)로 초기 버름 폭 배열을 비운다. |
| 114–147 | `if DUNE.used` (115) 안에서 `if ~isempty(findstr(lower(S.ldbdune),'.dun'))` (116)이면 load(118)로 읽은 1부터 5열을 xdune·ydune·wberm·dfelev·dcelev에 복사한다(119–123). `if size(dune,2)>5` (124)이면 6열을 cs로 복사한다. `else` (126)이면 `DUNE.cs = repmat(DUNE.cs,size(DUNE.xdune));` (127). `if size(dune,2)>6` (129)이면 7·8·9열을 cstill·xtill·perctill에 복사한다(130–132). `else` (133)이면 `DUNE.cstill = repmat(DUNE.cstill,size(DUNE.xdune));` (134), `DUNE.xtill = repmat(DUNE.xtill,size(DUNE.xdune));` (135), `DUNE.perctill = repmat(DUNE.perctill,size(DUNE.xdune));` (136). wberm_mc0·xdune0·ydune0에 읽은 값을 복사한다(138–140). struct2log 호출은 주석이다(144). 빈 줄과 두 분기·함수 종료를 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1: 입력 인수 COAST는 함수 본문에서 참조하지 않는다.
- 117–123: 파일 형식 주석은 네 값 [x,y,Bf0,Bm0]을 적는다. 실행 코드는 다섯 번째 열까지 읽는다.
- 129–132: 열 수 검사는 size(dune,2)>6이다. 참 분기는 아홉 번째 열까지 읽는다.
- 116–141: .dun 입력 분기는 좌표에 xyoffset을 적용하는 식을 포함하지 않는다.
