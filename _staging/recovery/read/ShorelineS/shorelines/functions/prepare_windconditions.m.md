---
file: models/ShorelineS/raw/source_code/shorelines/functions/prepare_windconditions.m
lines: 96
sha256: cb995d7d95c3a84996f0d49bcccf2b0829333c50f9baf43fd1e14fe4d84ad23c
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# prepare_windconditions.m — 판독 구간 기록

구간은 1행부터 96행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–62 | 함수 시그니처는 `function [WIND]=prepare_windconditions(S,TIME)` (1). 주석은 사구(dune)·이질 해안(mud coast) 스위치, 바람 시간 간격·공기 밀도·계수·속도·풍향 및 입력 시계열(time series) 파일을 설명한다(2–34). 이 파일에는 S 필드 기본값 대입이 없다. 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(35–62). |
| 63–79 | WIND를 만들고 dune·mud·mergeconditions를 같은 이름의 S 필드에서, dt를 S.dtdune에서 복사한다(63–67). WND를 비운다(69). `if S.dune \|\| S.mud` (70)이면 rhoa·uz·wndfile을 같은 이름의 S 필드에서, Cd·phiwnd를 S.cd·S.phiwnd0에서 복사한다(71–75). `if isfield(S,'Windclimfile') && isempty(WIND.wndfile)` (76)이면 이전 입력 S.Windclimfile을 wndfile에 복사한다(77). |
| 80–96 | 시작 시 70행 사구·이질 해안 조건 안. `if ~isempty(WIND.wndfile)` (80)에서 `if ischar(WIND.wndfile)` (81)이면 `WIND.wndfile={WIND.wndfile};` (82). `elseif size(WIND.wndfile,2)>3 && (size(WIND.wndfile,1)==1 \|\| size(WIND.wndfile,1)==3)` (83)이면 `WIND.wndfile=WIND.wndfile';` (84). 로그 뒤 `[WND]=get_inputfiledata(WIND.wndfile,TIME);` (89)를 호출한다. struct2log 호출은 주석이다(92). 바깥 분기를 닫은 뒤 WND를 WIND.WND에 복사한다(93–94). 빈 줄과 함수 종료를 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11·13·15·66·72·74: 입력 주석은 dt·Cd·phiwnd를 적는다. 실행 코드의 S 필드 이름은 dtdune·cd·phiwnd0이다.
- 32–33·89: 출력 주석은 바람 자료의 출처를 wvcfile이라고 적는다. 실행 호출은 WIND.wndfile을 전달한다.
- 63–94: 두 스위치가 모두 거짓이면 WIND에는 dune·mud·dt·mergeconditions·빈 WND만 대입한다. rhoa·Cd·uz·phiwnd·wndfile은 참 분기 안에서만 대입한다.
