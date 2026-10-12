---
file: models/ShorelineS/raw/source_code/shorelines/functions/update_props.m
lines: 53
sha256: 725661767d5d1fc811cd9366488c8b97669517cfa4907b142422da52a288b000
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# update_props.m — 판독 구간 기록

구간은 1행부터 53행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | 함수 시그니처(1), 격자 변경 뒤 사구(dune)와 점착성 퇴적물(mud) 속성 갱신 목적(4), 저작권·LGPL·무보증 주석(6–32). 입력 구조체 COAST·DUNE·MUD의 기본값 설정문은 없다. 원문: `function [COAST,DUNE,MUD] = update_props(COAST,DUNE,MUD)` (1). |
| 33–43 | 시작 시 1행 함수 안. DUNE.used 조건에서 x_mc가 NaN이 아닌 점을 고른다(33–34). 해당 해안 좌표·berm 폭·사구 전면/마루 고도(dune front/crest elevation)를 DUNE에 복사한다(35–39). COAST 사구 좌표는 berm 폭과 해안 법선으로 계산한다(40–41). get_disentangled 호출은 주석이다(42). 원문: `if DUNE.used` (33), `ok = ~isnan(COAST.x_mc);` (34), `DUNE.xdune = COAST.x_mc(ok); % - COAST.wberm_mc(ok).*sind(COAST.PHIcxy_mc(ok));` (35), `DUNE.ydune = COAST.y_mc(ok); % - COAST.wberm_mc(ok).*cosd(COAST.PHIcxy_mc(ok));` (36), `DUNE.wberm = COAST.wberm_mc(ok);` (37), `DUNE.dfelev = COAST.dfelev_mc(ok);` (38), `DUNE.dcelev = COAST.dcelev_mc(ok);` (39), `COAST.xdune_mc = COAST.x_mc - COAST.wberm_mc.*sind(COAST.PHIcxy_mc);` (40), `COAST.ydune_mc = COAST.y_mc - COAST.wberm_mc.*cosd(COAST.PHIcxy_mc);` (41). |
| 44–53 | 시작 시 1행 함수 안이며 DUNE 조건 밖. MUD.used 조건에서 x_mc가 NaN이 아닌 점의 좌표와 Bf·Bfm·Bm을 MUD에 복사한다(44–50). 조건·함수 끝과 빈 줄(51–53). 원문: `if MUD.used` (44), `ok = ~isnan(COAST.x_mc);` (45), `MUD.xmgv = COAST.x_mc(ok);` (46), `MUD.ymgv = COAST.y_mc(ok);` (47), `MUD.Bf = COAST.Bf_mc(ok);` (48), `MUD.Bfm = COAST.Bfm_mc(ok);` (49), `MUD.Bm = COAST.Bm_mc(ok);` (50). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 35–36·40–41: DUNE.xdune·ydune는 해안 좌표를 그대로 복사한다. COAST.xdune_mc·ydune_mc는 berm 폭을 뺀 좌표를 계산한다.
- 34·45: 두 속성 갱신 모두 x_mc의 NaN 여부로 ok를 정한다. y_mc의 NaN 여부에 대한 별도 조건은 없다.
