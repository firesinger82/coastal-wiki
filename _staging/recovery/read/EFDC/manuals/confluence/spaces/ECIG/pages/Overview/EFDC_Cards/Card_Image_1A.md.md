---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_1A.md
lines: 38
sha256: b5fef4a62adfe91f230817d839ffa0a69c9e20ede7558e06831feff87d8e6997
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_1A.md — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(metadata) — 페이지 ID(2), 제목(3), space(4), 원문 URL(5), 버전(6), 갱신 시각(7), 문서 계층 경로(8)를 기록한다. `---` 구분자를 포함한다(1·9). |
| 10–23 | C1A GRID CONFIGURATION AND TIME INTEGRATION MODE SELECTION / 시간 적분·미사용 항목 — 격자 구성(grid configuration) 및 시간 적분(time integration) 방식 선택 제목을 적는다(10). `IS2TIM`의 0은 세 시간 레벨 적분(three-time level integration), 1은 두 시간 레벨 적분(two-time level integration)이다(14–16). `IGRIDH`는 사용하지 않는다고 적는다(20). 매개변수·옵션 원문: `\* IS2TIM: 0 THREE-TIME LEVEL INTEGRATION` (14); `\*              1 TWO-TIME LEVEL INTEGRATION` (16); `\* IGRIDH: NOT USED` (20). 주석용 `\*` 줄과 빈 줄을 포함한다. |
| 24–35 | C1A / 연직 격자·층 수·수위 상승 — `IGRIDV`의 0은 표준 시그마 연직 격자(standard sigma vertical grid) 또는 단일층 수심 평균(single layer depth average), 1은 셀마다 층 수가 달라질 수 있는 SIGMA-ZED 연직 층 배치(vertical layering), 2는 표면의 균일한 층 두께를 사용하는 SIGMA-ZED 연직 격자이다(24–28). `SGZMin`은 SIGMA-ZED의 최소 층 수이며, `SGZHPDelta`는 `IGRIDV>0` 조건에서 초기 상태 대비 전형적인 수위 상승량으로 단위는 M이다(30–32). 매개변수·조건·단위 원문: `\* IGRIDV: 0 STANDARD SIGMA VERTICAL GRID OR SINGLE LAYER DEPTH AVERAGE` (24); `\*              1 SIGMA-ZED (SGZ) VERTICAL LAYERING ALLOWING VARYING LAYERS FOR EACH CELL (DSI)` (26); `\*              2 SIGMA-ZED (SGZ) VERTICAL GRID USING UNIFORM LAYER THICKENSS AT SURFACE (DSI)` (28); `\* SGZMin: MINIMUM NUMBER OF LAYERS FOR SIGMA-ZED` (30); `\* SGZHPDelta: TYPICAL RISE OF WATER ABOVE THE INITIAL CONDITIONS WHEN IGRIDV>0 (M)` (32). 주석용 `\*` 줄과 빈 줄을 포함한다(33–35). |
| 36–38 | C1A / 입력 예시 — 다섯 필드의 입력 헤더와 수치 예시를 적는다(36·38). 예시를 기본값으로 표시하지 않았다. 입력 줄 원문: `C1A IS2TIM  IGRIDH  IGRIDV  SGZMin  SGZHPDelta` (36); `             1        0            0            5             0` (38). 빈 줄을 포함한다(37). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음

