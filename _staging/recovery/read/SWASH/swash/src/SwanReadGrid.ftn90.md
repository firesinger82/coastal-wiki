---
file: models/SWASH/raw/source_code/swash/src/SwanReadGrid.ftn90
lines: 95
sha256: f407dd9846c09b84e46492deaff25b18d2b46c1e68b8a90d336b8becf417b892
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwanReadGrid.ftn90 — 판독 구간 기록

구간은 1행부터 95행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–57 | SwanReadGrid 입구(1), 기관·작성자·GPL 3 이상·무보증 머리말(2–29), 2007년 신설 이력(30–36). ADCIRC·Triangle·Easymesh 생성기의 비구조 격자(unstructured grid)를 읽는다는 목적·방법(38–44). ocpcomm4·SwanGriddata 사용(48–49), implicit none(51). lenfnm·basenm은 intent(in)(55–56). |
| 58–69 | 시작 시 1행 SwanReadGrid 루틴 안. `integer, save :: ient = 0` 선언(60), 구조·실행부 표제(62–67), `if (ltrace) call strace (ient,'SwanReadGrid')` (68). [10-15 전수 검증 보완] |
| 70–95 | 시작 시 1행 SwanReadGrid 루틴 안. `if ( grid_generator == meth_adcirc ) then` (70)은 `call SwanReadADCGrid` (74)이다. `elseif ( grid_generator == meth_triangle ) then` (76)은 `call SwanReadTriangleGrid ( basenm, lenfnm )` (80), `elseif ( grid_generator == meth_easy ) then` (82)은 `call SwanReadEasymeshGrid ( basenm, lenfnm )` (86)이다. `else` (88)는 msgerr 등급 4로 알 수 없는 생성기를 보고하고 return한다(90–91). 분기 설명 주석과 루틴 종료(70–95). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
