---
file: models/ADCIRC/raw/manuals/wiki/markdown/NTIF.md
lines: 9
sha256: a8f4970abb99e6d228f2ee8255824c4ccfd655932104e14f46e175cb36a0937e
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# NTIF.md — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | NTIF — fort.15의 NTIF는 천문 강제력(astronomical forcing)의 조석 분조(tidal constituents) 수를 지정한다(5). 천문 강제력에는 평형 조석 포텐셜(equilibrium tidal potential)과 선택적으로 자체 인력과 하중(self-attraction and loading) 조석이 포함된다(5). 제목·판본·빈 줄을 포함한다(1–6). 원문: `` `NTIF` is an input in the [fort.15 file](/Fort.15_file) that indicates the number of tidal constituents that make up the astronomical forcing (the equilibrium tidal potential and, if used, the self-attraction and loading tide). `` (5). |
| 7–9 | Usage Notes — fort.15의 NTIP를 1 또는 2로 설정해야 한다고 적는다(9). 원문: ``The other [fort.15 file](/Fort.15_file) parameter, `[NTIP](/NTIP)`, must be set to 1 or 2.`` (9). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 9행: `[NTIP](/NTIP)` 링크 표기가 백틱 내부에 있다.
