---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Propwash/mod_Variables_Ship.f90
lines: 26
sha256: 619b7293579a590c1993e17ebc4f0ee577c0773626070b3155c397f870bc824d
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_Variables_Ship.f90 — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | EFDC+ 출처·GPLv2·저작권 머리말(1–8). Variables_Ship은 Mod_all_tracks·Mod_Active_Ship·Mod_all_ship_tracks를 가져오고 implicit none을 사용한다(9–15). 빈 줄을 포함한다(10·14·16). |
| 17–26 | 시작 시 9행 Variables_Ship 모듈 안. track_ids는 이전·다음 항적(track) 위치 인덱스를 모두 1로 선언 초기화한다(17–20). 입력 선박·활성 선박·읽은 항적을 ship_type·active_ship·all_ship_tracks의 1차원 allocatable 배열로 선언한다(22–24). 실행 루틴 없이 모듈을 닫는다(26). 계산·설정 원문: `integer :: prev = 1` (18), `integer :: next = 1` (19). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–19: prev와 next의 선언 초기값은 모두 1이다. 이 파일에는 다음 위치를 2로 바꾸는 실행문이 없다.
