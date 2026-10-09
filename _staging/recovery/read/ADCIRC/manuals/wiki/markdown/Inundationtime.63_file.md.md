---
file: models/ADCIRC/raw/manuals/wiki/markdown/Inundationtime.63_file.md
lines: 13
sha256: 00c35a12b73546413fac562166d57fa30a21473307093da9d3450bfa87df3a31
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Inundationtime.63_file.md — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | Inundationtime.63 file — 처음 건조(dry)한 영역이 inunThresh 침수 임계 깊이(inundation threshold depth)를 넘는 총 시간을 기록한다(5). fort.15 네임리스트(namelist)의 출력 활성화 조건을 적는다(7). 첫 데이터 집합(dataset)은 임계 깊이를 넘은 시간을 초 단위로 누적하며 서로 이어지지 않은 침수 기간도 합산한다(9). 둘째 데이터 집합은 임계 깊이를 넘는 침수 시작 시각을 콜드스타트(cold start) 이후 초로 기록한다(9). 제목·판본·빈 줄을 포함한다(1–10). 원문: `The inundationtime.63 file records the total time that an initially dry area is inundated beyond a certain inundation threshold depth specified in the [fort.15 file](/Fort.15_file) in the [inundationOutputControl namelist](/index.php?title=InundationOutputControl_namelist&action=edit&redlink=1) by the parameter [inunThresh](/index.php?title=InunThresh&action=edit&redlink=1).` (5); `The writing of the inundationtime.63 output file is activated when the [inundationOutput](/index.php?title=InundationOutput&action=edit&redlink=1) parameter is set to .true. in the optional [inundationOutputContol namelist](/index.php?title=InundationOutputContol_namelist&action=edit&redlink=1) at the bottom of the [fort.15 file](/Fort.15_file).` (7); `The file contains two datasets. The first dataset records the total accumulated time in seconds that a node was inundated beyond the threshold. Periods of inundation are counted toward the total time, even if they are not contiguous. The second dataset records the time of onset of inundation beyond the threshold in seconds since cold start. The time of onset data are useful in the context of real time model guidance for decision making.` (9). |
| 11–13 | File Format — `inundationtime.63 file format` 문서로 연결한다(11–13). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5·7행: 네임리스트 표기는 각각 `inundationOutputControl`과 `inundationOutputContol`이다. 이 네임리스트 링크와 inunThresh, inundationOutput 링크에 `action=edit&redlink=1`이 있다.
