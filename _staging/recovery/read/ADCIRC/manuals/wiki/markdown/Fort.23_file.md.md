---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.23_file.md
lines: 9
sha256: ad81b7ad08ae5db9fffe0119a124a908d69cd665e149645a14ad4af88c527849
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.23_file.md — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Fort.23 file / 역할·적용 조건 — 제목·판본·빈 줄을 포함한다(1–4). 파랑 복사응력(wave radiation stress)을 단독 또는 바람을 포함한 다른 강제력과 함께 ADCIRC에 입력한다고 적는다(5). 이 파일을 읽는 NWS 조건과 hot-start 뒤 PBL 허리케인 형식과의 유사성을 명시한다(5). 원문: `The fort.23 file contains wave radiation stresses that can be used by themselves or in concert with other forcing (including winds) to drive ADCIRC. The wave radiation stress input file is read when ABS([NWS](/NWS))>=100 in the [fort.15 file](/Fort.15_file). The format is similar to the meteorological input file used when [NWS](/NWS) =-4 (i.e. the PBL hurricane model input format following a hot start).` (5). |
| 7–9 | File Format — 별도 `fort.23 file format` 문서로 연결한다(7–9). 이 구간은 입력행을 제시하지 않는다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
