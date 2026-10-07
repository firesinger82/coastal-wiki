---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Appendices/Appendix_B_-_Data_Formats/Data_Format_B-11__External_Windwaves.md
lines: 38
sha256: 6b09d9d6f8c160b343388432b94362e494f558eed15bbe4ee2262d19cb175ee7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-11__External_Windwaves.md — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 문서 메타데이터 — 페이지 ID·제목·space·URL·판본·갱신 시각·문서 경로와 frontmatter 구분자를 포함한다(1–9). Data Format B-11 / WAVE.INP 헤더·정의 — Tra Khuc의 WAVE.INP와 EFDC_Explorer7.1.1 판본 예제를 제시한다(10–12). 파·흐름 경계층(wave-current boundary layer)과 파랑 유발 흐름(wave induced flow) 정보를 지정한다는 주석을 포함한다(13). 입력 파일·판본·용도 주석 원문: `C \*\* Tra Khuc, FILE: WAVE.INP  ` (11); `C \*\* Version: EFDC\_Explorer7.1.1 : Ver 140606  ` (12); `C \*\* Specify Information For Wave-Current Boundary Layer and Wave Induced Flow  ` (13). 입력 열 순서 원문: `C \*\* I   J    WVHEI    WANGLE    WVPER    WVLEN    WVDISP  ` (15). 셀 인덱스·파고(wave height)·동쪽 기준 파향(wave angle)·파주기(wave period)·파장(wave length)·파랑 에너지 소산(wave energy dissipation)의 정의·단위 원문: `C \*\* I,J Cell Indices  ` (17); `C \*\* WVHEI = Wave Height (m)  ` (19); `C \*\* WANGLE = Wave Angle (Degrees from East)  ` (20); `C \*\* WVPER = Wave Period (seconds)  ` (21); `C \*\* WVLEN = Wave Length (meters)  ` (22); `C \*\* WVDISP = Wave Energy Dissipation In (m/s)\*\*3  ` (23). 빈 주석을 포함한다(14·16·18·24). |
| 25–38 | Data Format B-11 / 셀별 예시 입력 — I 인덱스 52부터 65까지와 J 인덱스 3의 자료를 제시한다(25–38). 모든 예시 행의 WVHEI·WANGLE·WVPER·WVLEN은 0.0000이다(25–38). WVDISP에는 0.0000과 -0.0090이 있다(25–38). 행별 원문: `52 3 0.0000 0.0000 0.0000 0.0000 -0.0090  ` (25); `53 3 0.0000 0.0000 0.0000 0.0000 0.0000  ` (26); `54 3 0.0000 0.0000 0.0000 0.0000 0.0000  ` (27); `55 3 0.0000 0.0000 0.0000 0.0000 0.0000  ` (28); `56 3 0.0000 0.0000 0.0000 0.0000 -0.0090  ` (29); `57 3 0.0000 0.0000 0.0000 0.0000 -0.0090  ` (30); `58 3 0.0000 0.0000 0.0000 0.0000 -0.0090  ` (31); `59 3 0.0000 0.0000 0.0000 0.0000 -0.0090  ` (32); `60 3 0.0000 0.0000 0.0000 0.0000 -0.0090  ` (33); `61 3 0.0000 0.0000 0.0000 0.0000 -0.0090  ` (34); `62 3 0.0000 0.0000 0.0000 0.0000 0.0000  ` (35); `63 3 0.0000 0.0000 0.0000 0.0000 -0.0090  ` (36); `64 3 0.0000 0.0000 0.0000 0.0000 -0.0090  ` (37); `65 3 0.0000 0.0000 0.0000 0.0000 0.0000` (38). 표시된 수치를 기본값으로 해석하지 않았다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 8행의 문서 경로는 `EFDC+ Explorer 12 User Guide`를 포함한다. 12행의 예제 판본은 `EFDC_Explorer7.1.1 : Ver 140606`이다.
- 23행은 `WVDISP`를 Wave Energy Dissipation으로 정의한다. 예시에는 음수 `-0.0090`이 있고 부호 규약은 이 파일에 없다(25·29–34·36–37).
