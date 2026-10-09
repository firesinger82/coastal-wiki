---
file: models/ADCIRC/raw/manuals/wiki/markdown/Global_Minimum_and_Maximum_Files.md
lines: 15
sha256: 8fb96183c91f4a926ffa81ed11a9c8ecf191edfb1c2b5c1ae5728dac92ca1b01
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Global_Minimum_and_Maximum_Files.md — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | Global Minimum and Maximum Files — 제목과 판본 표기 `_revid=627_`(1–3)을 포함한다. 전 영역(domain) 시계열 출력의 파일 크기와 관측소(station) 출력의 공간 범위 때문에 각 절점(node)의 극값(extreme value)을 저장하는 파일을 도입했다고 설명한다(5). 짧게 지속되는 첨두(peak)를 잡으려면 높은 표본 해상도(sampling resolution)가 필요하다고 적는다(5). ADCIRC는 매 시간 단계(time step)에 수위·유속·풍속·가용한 경우의 파랑 복사응력(wave radiation stress)·기압 극값을 모으고 마지막 단계가 끝난 뒤 파일을 쓴다(7). 파일명과 수집·출력 조건 원문: `These input/output files (maxele.63, maxvel.63, maxwvel.63, maxrs.63, minpr.63) were developed to resolve issues where only the most extreme values at each node in the domain were required, e.g., peak water levels throughout the domain. The use of time varying full domain output for this purpose would produce files that are too large, while station files would not cover the entire domain. Furthermore, some peak values last for only a very short time, and therefore the sampling resolution must be very high to capture true peaks at each node.` (5); `As a result, ADCIRC collects extreme values at every time step for water surface elevation (maxele.63), water velocity (maxvel.63), wind velocity (maxwvel.63), wave radiation stress (maxrs.63, if available), and barometric pressure (minpr.63). The files are then written out after the last time step of the simulation is complete.` (7). |
| 9–12 | 재시작·판본별 자료 집합 — 재시작(hotstart) 이전 극값을 포함하기 위해 실행 시작 때 실행 디렉터리의 각 극값 파일을 읽으려고 시도한다고 설명한다(9). 파일을 찾으면 재시작 실행의 극값 기록에 사용한다(9). ADCIRC 51부터 첫 자료 집합(data set)은 절점별 극값이고 둘째는 콜드 시작(cold start) 이후 초 단위 발생 시각이라고 설명한다(11). 이전 판본은 첫 자료 집합만 포함한다(11). 적용 조건·판본·단위 원문: `One issue with recording extreme values in this way is the use of [hotstart files](/index.php?title=Fort.67/fort.68_files&action=edit&redlink=1) to restart a simulation. In order to capture the extreme values prior to the hotstart time, an ADCIRC simulation will attempt to load each of these extreme values files from the run directory at the start of the run. If it finds them, it will use them in its recording of extreme values throughout the hotstarted run; the extreme values files it writes out will then take into account the values that were recorder prior to the hotstart time.` (9); `In ADCIRC versions starting with version 51, these files contain two full domain data sets: the first contains the extreme value at each node, while the second contains time (in seconds since cold start) that the extreme value occurred at each node. In previous ADCIRC versions, only the first data set appears in the file.` (11). |
| 13–15 | File Format — Global minumum and maximum file format 참조로 연결한다(15). 원문의 `minumum` 표기를 그대로 유지한다. `See [Global minumum and maximum file format](/index.php?title=Global_minumum_and_maximum_file_format&action=edit&redlink=1) for details.` (15). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 9행: hotstart files 참조 URL에 `action=edit&redlink=1`이 들어 있다.
- 15행: 파일 형식 참조는 `Global_minumum_and_maximum_file_format`을 가리키며 `action=edit&redlink=1`이 들어 있다. 참조 이름은 `Minimum` 대신 `minumum`을 사용한다.
