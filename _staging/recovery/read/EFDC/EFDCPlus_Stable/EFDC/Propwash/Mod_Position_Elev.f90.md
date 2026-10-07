---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Propwash/Mod_Position_Elev.f90
lines: 26
sha256: 8a24d4c78ded618cf268f6e6afae235aae047756bd110564f54c9f9a70e68742
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Mod_Position_Elev.f90 — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | EFDC+·GPLv2·저작권 머리말(1–8), Mod_Position_Elev 시작(9). GLOBAL의 RKD/RK4·Mod_Position 사용(11–12), implicit none(14). 기본 private, position_elev 공개·빈 줄(16–18). |
| 19–26 | 시작 시 9행 Mod_Position_Elev 안. position_elev는 position을 확장(19). 좌표 위치의 바닥고(bottom elevation) b_elev와 수심(water depth) w_depth는 RKD 실수이고 기본값은 0.0, 단위는 meters라는 주석(21–22). 형식 종료·모듈 종료·빈 줄(24–26). 조건 분기·계산 루틴·호출은 없다. 원문: `real (kind = RKD)   :: b_elev  = 0.0       !< bottom elevation for the positions x,y coordinate[meters]` (21); `real (kind = RKD)   :: w_depth = 0.0       !< water depths for the x,y coorinda [meters]` (22). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
