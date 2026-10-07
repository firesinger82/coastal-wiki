---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Appendices/Appendix_B_-_Data_Formats/Data_Format_B-17__ICE.md
lines: 28
sha256: eb8bbcd3278276d2d16d41861cfed0f7a7d717c74f3ad02c589e7cdde1adf44c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-17__ICE.md — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 식별자, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(2–8). |
| 10–14 | ICE.INP 적용 조건과 열 — 얼음 두께(ice thickness)의 초기 조건을 제시한다(12). 격자 좌표 필드와 두께 단위는 원문 열 제목에 있다(14). 빈 줄도 포함한다(11,13). 원문: `**Data Format B-17  ICE.INP for ISICE = 3 & 4**` (10); ` \* ICE THICKNESS INITIAL CONDITIONS` (12); ` \* I    J    THICKNESS[m]  ` (14). |
| 15–28 | ICE.INP 예시 — 좌표별 초기 두께 데이터 줄을 제시한다(15–28). 원문: `3 207 0.300  ` (15); `3 208 0.300  ` (16); `3 209 0.300  ` (17); `3 210 0.300  ` (18); `3 211 0.300  ` (19); `3 212 0.300  ` (20); `4 207 0.300  ` (21); `4 208 0.300  ` (22); `4 209 0.300  ` (23); `4 210 0.300  ` (24); `4 211 0.300  ` (25); `4 212 0.300  ` (26); `5 207 0.300  ` (27); `5 208 0.300` (28). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
