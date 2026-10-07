---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/Input_Files/Initial_Condition_Files.md
lines: 30
sha256: e6e930fdc6fb9893d55bcdac9958f3f25816c1bf9e6889abad3b7928398046b5
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Initial_Condition_Files.md — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 머리말 — 페이지 제목은 Initial Condition Files이다(3). 페이지 ID, space, URL, 버전, 갱신 시각과 문서 경로를 기록한다(2–8). |
| 10–30 | Initial Condition Files / 초기 조건(initial condition) 파일 표 — 염분(salinity), 온도(temperature), 염료(dye), 수층(water column)과 하상(bed)의 점착성 퇴적물(cohesive sediment)·비점착성 퇴적물(non-cohesive sediment)·독성물질(toxic) 파일을 나열한다(12–20). POC·DOC·FPOC 수층·하상 파일, 수질(water quality), SOD와 뿌리 식물(rooted plant) 파일을 나열한다(21–30). 각 행의 파일 이름과 설명을 그대로 옮긴다. 표는 기본값·범위·단위를 제시하지 않는다. 원문: `\| salt.inp \| Salinity \|` (12); `\| temp.inp \| Temp \|` (13); `\| dye.inp \| Dye \|` (14); `\| sedw.inp \| Cohesive Sediment water column \|` (15); `\| sndw.inp \| Non-Cohesive Sediment water column \|` (16); `\| toxw.inp \| Toxic water column \|` (17); `\| sedb.inp \| Cohesive Sediment bed \|` (18); `\| sndb.inp \| Non-Cohesive Sediment bed \|` (19); `\| toxb.inp \| Toxic bed \|` (20); `\| pocw.inp \| POC water column \|` (21); `\| pocb.inp \| POC bed \|` (22); `\| docw.inp \| DOC water column \|` (23); `\| docb.inp \| DOC bed \|` (24); `\| fpocb.inp \| FPOC bed \|` (25); `\| fpocw.inp \| FPOCwater column \|` (26); `\| wqwcrst.inp \| Water quality \|` (27); `\| wqsdici.inp \|  \|` (28); `\| wqsdrst.inp \| SOD \|` (29); `\| wqrpemsic.inp \| Rooted Plant \|` (30). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 28행: `wqsdici.inp`의 설명 칸이 비어 있다.
- 21–29행: POC, DOC, FPOC와 SOD의 약어 풀이는 이 파일에 없다.

