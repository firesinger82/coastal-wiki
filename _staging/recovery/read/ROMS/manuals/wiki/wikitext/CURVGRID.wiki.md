---
file: models/ROMS/raw/manuals/wiki/wikitext/CURVGRID.wiki
lines: 3
sha256: 8ca18d9bcc474ca9aa8ee2b113d1f7d814e043f07c8272c8c874ac3e76cdb4ef
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# CURVGRID.wiki — 판독 구간 기록

구간은 1행부터 3행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–3 | CURVGRID — Options 절 포함 지시문과 dmde·dndx·angle 중 하나가 0이 아니면 옵션을 활성화해야 한다는 조건이다(1–2). 격자 곡률(curvature)은 운동량식의 추가 계량항(metric terms)을 요구한다(3). 격자 회전(grid rotation)에 필요한 비영 각도와 바람 성분 회전 용도를 설명한다(3). 원문: ` {{#lst:Options\|CURVGRID}} ` (1); ` IF dmde or dndx or angle is non-zero, then you should activate this option. ` (2); ` The curvature of the grid requires additional metric terms in the momentum equations. The rotation of a grid requires the grid angle to be non-zero. The grid angle is needed for such features as to rotate Uwind and Vwind to the grid (for example). ` (3). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
