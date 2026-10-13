---
file: models/ROMS/raw/manuals/wiki/wikitext/Subroutines.wiki
lines: 6
sha256: 6a5be95fb35bf036d707b81ba875c1ad5e9caf9b1ae80c6c6d102784467f3f0d
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# Subroutines.wiki — 판독 구간 기록

구간은 1행부터 6행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Subroutines — 정방향 모델(forward model)의 ROMS/Nonlinear·ROMS/Utility 서브루틴 목록을 예고한다(1–3). shapiro.F 모듈은 shapiro2d_tile·shapiro3d_tile을 포함하며 통신을 하지 않고 최신 halo 정보의 배열을 전달받는다고 적는다(5–6). 섹션 전재용 마크업을 포함한다(5–6). 원문: `<section begin=shapiro.F />;<span id="shapiro.F"></span>[[shapiro.F]]` (5); `:This is actually a module containing '''shapiro2d_tile''' and '''shapiro3d_tile'''. The routines do no communications and expect to be passed arrays with up-to-date halo information.<section end=shapiro.F />` (6). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 3행: 전체 목록을 소개하는 문구가 `(coming)`으로 남아 있으며 파일에는 shapiro.F 항목 하나만 있다.
