---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_27.md
lines: 47
sha256: 20e6673794a5e3b2fb0b439bf39761f2ea794d0faa48e3f3a693ca8170b9bb37
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_27.md — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | C27 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 제트·플룸(jet/plume) 공급원의 위치·기하(geometry)·연행(entrainment) 매개변수 제목을 제시한다(10). 빈 줄과 주석 표식도 포함한다(11–13). 원문: ` C27 JET/PLUME SOURCE LOCATIONS, GEOMETRY AND ENTRAINMENT PARAMETERS ` (10). |
| 14–25 | 식별자·활성화·셀 위치 — 제트·플룸 식별자와 우회·일반 활성·취수/환수(withdrawal/return) 옵션을 설명한다(14–16). 셀·층 인덱스(cell/layer index), 기본 K 인덱스를 사용하는 조건, 같은 셀에 있는 동일 포트(port)의 수를 정의한다(18–24). 원문: ` \* ID: ID COUNTER FOR JET/PLUME ` (14); ` \* ICAL: 0 BYPASS, 1 ACTIVE (NORMAL - TOTAL LAYER FLOW AT DIFFUSER), 2 - W/R (USE W/R SERIES) ` (16); ` \* IQJP: I CELL INDEX OF JET/PLUME ` (18); ` \* JQJP: J CELL INDEX OF JET/PLUME ` (20); ` \* KQJP: K CELL INDEX OF JET/PLUME (DEFAULT, QJET=0 OR JET COMP DIVERGES) ` (22); ` \* NPORT: NUMBER OF IDENTIAL PORTS IN THIS CELL ` (24). |
| 26–43 | 기하·보정·오차 기준 — 방류 셀 중심을 기준으로 한 동쪽·북쪽 위치는 m 단위이며 미사용이라고 적는다(26–28). 방류 표고(elevation), 수평 기준 수직 각도, 동쪽 기준 반시계 방향 수평 각도, 포트 지름의 단위를 제시한다(30–36). 프루드수(Froude number) 조정 계수와 연행 오차 기준을 설명한다(38–40). 원문: ` \* XJET: LOCAL EAST JET LOCATION RELATIVE TO DISCHARGE CELL CENTER (m) (NOT USED) ` (26); ` \* YJET: LOCAL NORTH JET LOCATION RELATIVE TO DISCHARGE CELL CENTER (m)(NOT USED) ` (28); ` \* ZJET: ELEVATION OF DISCHARGE (m) ` (30); ` \* PHJET: VERTICAL JET ANGLE POSITIVE FROM HORIZONTAL (DEGREES) ` (32); ` \* THJET: HORIZONTAL JET ANGLE POS COUNTER CLOCKWISE FROM EAST (DEGREES) ` (34); ` \* DJET: DIAMETER OF DISCHARGE PORT (m) ` (36); ` \* CFRD: ADJUSTMENT FACTOR FOR FROUDE NUMBER ` (38); ` \* DJPER: ENTRAINMENT ERROR CRITERIA ` (40). |
| 44–47 | C27 입력 예시 — Markdown의 빈 표 머리글과 구분선(44–45), 열 이름(46), Jet/Plume 주석이 붙은 입력 값(47)을 제시한다. 원문: ` \| C27 \| ID \| ICAL \| IQJP \| JQJP \| KQJP \| NPORT \| XJET \| YJET \| ZJET \| PHJET \| THJET \| DJET \| CFRD \| DJPER \| !ID \| ` (46); ` \|  \| 1 \| 1 \| 31 \| 7 \| 1 \| 1 \| 0 \| 0 \| 95.1 \| 45 \| 0 \| 0.1 \| 1 \| 1 \| ! Jet/Plume \| ` (47). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 22행: `KQJP` 설명의 기본값 적용 조건에는 `QJET=0`이 나오지만 이 파일은 `QJET`를 정의하지 않는다.
