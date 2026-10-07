---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_43C.md
lines: 26
sha256: dfd7d39f806427e4d7592766cd0ab62c0569d3d466d4e4007eb02ab4aa26f201
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_43C.md — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(frontmatter) — 페이지 ID 31686686(2), 제목 Card Image 43C(3), space ECIG(4), 원문 URL(5), 버전 1(6), 수정 시각 2018-01-11T03:41:39.954Z(7), 문서 경로(8)와 구분선(1·9)을 포함한다. |
| 10–22 | C43C TOXIC TIME STEPS AND VOLATILIZATION SWITCHES — 독성물질 반응 속도론(toxic kinetics)의 시간 간격과 퇴적층(sediment bed)의 확산(diffusion)·혼합(mixing) 시간 간격을 초 단위로 정의한다(14·16). 휘발(volatilization) 계산 방식의 유속·수심 전환 표기를 제시한다(18·20). 이름·단위·전환 조건 원문: `\* TOXSTEPW: TIME STEP IN SECONDS FOR TOXIC KINETICS IN WATER COLUMN AND BED` (14); `\* TOXSTEPB: TIME STEP IN SECONDS FOR TOXIC BED PROCESSES OF DIFFUSION AND MIXING` (16); `\* TOX\_VEL\_MAX: VELOCITY SWITCH FOR VOLATILIZATION APPROACH: LAKE < TOX\_VEL\_MAX > RIVER` (18); `\* TOX\_DEP\_MAX: DEPTH SWITCH FOR VOLATILIZATION APPROACH: LAKE > TOX\_DEP\_MAX < RIVER` (20). |
| 23–26 | C43C 입력 형식 — 빈 줄과 열 이름 및 값의 두 줄을 포함한다(23–26). 제시값의 기본값 표시는 없다. 원문: `C43C STEPW  STEPB  VEL\_MAX  DEP\_MAX` (24); `                 2          2             2              5` (26). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 18·20: 전환 조건은 `LAKE < TOX\_VEL\_MAX > RIVER`와 `LAKE > TOX\_DEP\_MAX < RIVER`로 적혀 있다. 본문에는 이 비교 표기의 별도 해설과 유속·수심 임계값의 단위가 없다.

