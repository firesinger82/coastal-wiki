---
file: models/ADCIRC/raw/manuals/wiki/markdown/Everdried.63_file.md
lines: 13
sha256: 2813c5aceb617e266746f6054debdd431951b785ee7feb8c5d54fdf73f27c8fe
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Everdried.63_file.md — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | 제목·판본 표기·빈 줄을 포함한다(1–4). Everdried.63 file — 조화 분석(harmonic analysis)을 위해 실행 중 한 번이라도 건조해진 절점을 표시한다(5). 문서는 건조 시간 단계의 수위 결측값이 분석 해를 오염시킨다고 설명한다(5). 출력 활성화 조건, 첫 자료집합의 건조 경험·항상 습윤 플래그, 둘째 자료집합의 누적 건조 시간과 초 단위를 원문 그대로 옮긴다(7–9). 원문: `The dry node flagging file (everdried.63) file was created to support harmonic analysis by flagging all nodes that had ever become dry during the course of a simulation. These data are useful to harmonic analysis because a node that goes dry for a single time step has a -99999 recorded for its water surface elevation, which contaminates the harmonic analysis solution.` (5); `The writing of the everdried.63 output file is activated when the [inundationOutput](/index.php?title=InundationOutput&action=edit&redlink=1) parameter is set to .true. in the optional [inundationOutputContol namelist](/index.php?title=InundationOutputContol_namelist&action=edit&redlink=1) at the bottom of the [fort.15 file](/Fort.15_file).` (7); `The file contains two data sets. The first dataset provides information about the wet/dry state, where a node is given a value of -99999.0 if it ever went dry during the simulation, and a value of 1.0 if it was wet for the entire simulation. The second data set lists the total time in seconds that a node was dry during the simulation (0.0 if it was always wet).` (9). |
| 11–13 | File Format — 별도 `everdried.63 file format` 페이지를 연결한다(13). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 7: `inundationOutput`·`inundationOutputContol namelist` 링크에는 `action=edit&redlink=1`이 붙어 있다.
