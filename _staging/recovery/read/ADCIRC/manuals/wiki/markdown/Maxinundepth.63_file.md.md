---
file: models/ADCIRC/raw/manuals/wiki/markdown/Maxinundepth.63_file.md
lines: 13
sha256: 209a9cc765a86c1b33a4397a4ee3e2bcf7765075013797a9845cfb032e456d42
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Maxinundepth.63_file.md — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | Maxinundepth.63 file — initiallydry.63 기준으로 처음 건조(dry)한 영역의 지면 위 최대 침수 깊이(maximum inundation depth)를 m 단위로 기록한다(5). 모의 중 한 번도 습윤(wet)하지 않은 영역의 값도 지정한다(5). fort.15 네임리스트(namelist)의 출력 활성화 조건을 적는다(7). 첫 데이터 집합(dataset)은 최대 침수 값이고 둘째 집합은 최대값 발생 시각을 콜드스타트(cold start) 이후 초로 기록한다(9). 제목·판본·빈 줄을 포함한다(1–10). 원문: `The maximum inundation depth (maxinundepth.63) file records the peak inundation depth (in meters) above ground that occurred during the simulation. The data are only recorded in areas that are initially dry according to the [initiallydry.63 file](/Initiallydry.63_file). The values are -99999.0 if the area was never wet during the simulation.` (5); `The writing of the maxinundepth.63 output file is activated when the [inundationOutput](/index.php?title=InundationOutput&action=edit&redlink=1) parameter is set to .true. in the optional [inundationOutputContol namelist](/index.php?title=InundationOutputContol_namelist&action=edit&redlink=1) at the bottom of the [fort.15 file](/Fort.15_file).` (7); `The file contains two data sets. The first dataset contains the peak inundation value, and the second data set contains the time of occurrence of the peak inundation value in seconds since cold start.` (9). |
| 11–13 | File Format — `maxinundepth.63 file format` 문서로 연결한다(11–13). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 7행: 네임리스트 이름은 `inundationOutputContol`이다. 해당 네임리스트와 inundationOutput 링크에 `action=edit&redlink=1`이 있다.
