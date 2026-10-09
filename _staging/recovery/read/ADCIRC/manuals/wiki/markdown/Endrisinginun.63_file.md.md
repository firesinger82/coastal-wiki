---
file: models/ADCIRC/raw/manuals/wiki/markdown/Endrisinginun.63_file.md
lines: 11
sha256: 070f4bf0d91b60b6e6b1a55b2a3d874c6635109f991c9bd61b3b73099c7a5a22
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Endrisinginun.63_file.md — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 제목·판본 표기·빈 줄을 포함한다(1–4). Endrisinginun.63 file — 최종 시간 단계와 바로 전 시간 단계의 자유수면 수위(water surface elevation)를 비교하여 침수 수심(inundation depth)이 상승하는 절점에 정수 1, 나머지에 정수 0을 부여한다고 설명한다(5). `fort.15`의 선택 namelist에서 출력을 활성화하는 조건을 원문 그대로 옮긴다(7). 원문: `The inundation rising at the end of the run flag (endrisinginun.63) file flags nodes whose inundation depth is rising at the end of the simulation by comparing the water surface elevation on the final time step with the water surface elevation on the previous time step. Nodes with rising inundation levels are flagged with an integer value of 1 and all others are given an integer value of 0.` (5); `The writing of the endrisinginun.63 output file is activated when the [inundationOutput](/index.php?title=InundationOutput&action=edit&redlink=1) parameter is set to .true. in the optional [inundationOutputContol namelist](/index.php?title=InundationOutputContol_namelist&action=edit&redlink=1) at the bottom of the [fort.15 file](/Fort.15_file).` (7). |
| 9–11 | File Format — 별도 `endrisinginun.63 file format` 페이지를 연결한다(11). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 7: `inundationOutput`·`inundationOutputContol namelist` 링크에는 `action=edit&redlink=1`이 붙어 있다.
