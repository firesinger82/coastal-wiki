---
file: models/ADCIRC/raw/manuals/wiki/markdown/NTIP.md
lines: 47
sha256: 0622bcba86f485b35ef588e24dc3cf47fb8b9a4d110a76d69cf28349fb2da78c
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# NTIP.md — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | NTIP / Parameter Summary — NTIP는 fort.15에서 천문 강제력(astronomical forcing) 입력 종류를 선택한다(5). 가능한 값·설명·세부사항·필수 추가 입력의 표 열 제목, 제목·판본·빈 줄을 포함한다(1–18). 원문: `NTIP is an input in the [fort.15 file](/Fort.15_file) that selects the astronomical forcing input type. ` (5). |
| 19–26 | Parameter Summary / 값 0 — 천문 강제력을 사용하지 않는다(19–23). 필수 입력으로 NTIF=0을 적는다(25). 원문: `0` (19); `No Astronomical Forcing` (21); `-` (23); `[NTIF](/NTIF) = 0` (25). |
| 27–34 | Parameter Summary / 값 1 — 평형 조석 포텐셜(equilibrium tidal potential)의 해석 구성(analytical formulation)으로 조석 수위를 재구성한다(27–31). 필수 입력은 NTIF>0이다(33). 원문: `1` (27); `Astronomical Tidal Potential` (29); `Reconstructs the tidal elevation using the analytical formulation for the equilibrium tidal potential[&#91;1&#93;](#cite_note-tp-1)` (31); `[NTIF](/NTIF) > 0` (33). |
| 35–42 | Parameter Summary / 값 2 — 평형 조석 포텐셜과 자체 인력과 하중(self-attraction and loading, SAL) 조석 기여를 더해 수위를 재구성한다(35–39). SAL 분조(constituent) 값은 fort.24에서 읽는다(39). 필수 입력은 NTIF>0과 fort.24이다(41). 원문: `2` (35); `Astronomical Tidal Potential plus Self-attraction and Loading (SAL) Tide[&#91;2&#93;](#cite_note-Ray-2)` (37); `Reconstructs the tidal elevation by summing the contribution from the analytical formulation for the equilibrium tidal potential[&#91;1&#93;](#cite_note-tp-1) with the contribution from the prescribed SAL constituent values found in the [fort.24 file](/Fort.24_file).` (39); `[NTIF](/NTIF) > 0, [fort.24 file](/Fort.24_file)` (41). |
| 43–47 | References — ADCIRC 이론 보고서의 27번 식·17쪽과 SAL 조석 수치모델 논문을 인용한다(43–47). 이 파일에는 인용한 27번 식의 본문이 없다(45). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
