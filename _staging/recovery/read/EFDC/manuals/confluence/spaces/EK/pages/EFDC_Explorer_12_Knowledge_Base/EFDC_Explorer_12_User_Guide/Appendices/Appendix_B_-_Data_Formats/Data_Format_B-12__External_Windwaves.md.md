---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Appendices/Appendix_B_-_Data_Formats/Data_Format_B-12__External_Windwaves.md
lines: 25
sha256: 12254890d4252facdf00729d7fccacdcb447c6f05690ea05feb58bd9aaacd740
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-12__External_Windwaves.md — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 문서 메타데이터 — 페이지 ID·제목·space·URL·판본·갱신 시각·문서 경로와 frontmatter 구분자를 포함한다(1–9). Data Format B-12 / 외부 풍파 시각 — 외부 바람 파일에 대응하는 율리우스일(JULIAN DAYS)과 비정상 파랑(unsteady waves)의 SWAN 실행 조건을 주석으로 적는다(10–12). 용도·적용 조건 원문: `C \*\* JULIAN DAYS CORRESPONDING TO EXTR. WIND FILES  ` (11); `C \*\* FOR SWAN MODEL RUN IN CASE OF UNSTEADY WAVES  ` (12). |
| 13–25 | Data Format B-12 / 시각 예시 입력 — 각 줄에 시각 값 하나를 적는다(13–25). 예시 입력 원문: `225.0000  ` (13); `225.0417  ` (14); `225.0833  ` (15); `225.1250  ` (16); `225.1667  ` (17); `225.2083  ` (18); `225.2500  ` (19); `225.2917  ` (20); `225.3333  ` (21); `225.3750  ` (22); `225.4167  ` (23); `225.4583  ` (24); `225.5000` (25). 수치를 다른 시각 단위로 변환하지 않았다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 11–25행의 JULIAN DAYS 값에는 기준 연도나 기준일 설명이 없다.
