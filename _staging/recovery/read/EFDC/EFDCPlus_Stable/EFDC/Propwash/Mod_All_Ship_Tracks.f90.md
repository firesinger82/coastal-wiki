---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Propwash/Mod_All_Ship_Tracks.f90
lines: 23
sha256: 8624574966857f907a76ca62e9f14e3333842605137dfdb8e79683fda94d3108
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Mod_All_Ship_Tracks.f90 — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | EFDC+·GPLv2·저작권 머리말(1–8). Mod_All_Ship_Tracks 시작(9), Mod_All_Tracks 사용(11), implicit none·빈 줄(13–14). |
| 15–23 | 시작 시 9행 Mod_All_Ship_Tracks 안. All_Ship_Tracks 형식(15)은 all_tracks의 allocatable 1차원 구성 요소 All_Ship_Tracks와 한 선박의 항적(track) 수 num_tracks를 가진다(17–18). num_tracks 기본값은 0(18). 형식 종료·빈 줄·모듈 종료(20–23). 조건 분기·계산 루틴 호출은 없다. 원문: `integer :: num_tracks = 0      !< total tracks for a given ship` (18). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
