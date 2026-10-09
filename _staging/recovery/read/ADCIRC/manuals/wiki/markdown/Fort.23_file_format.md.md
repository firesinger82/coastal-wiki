---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.23_file_format.md
lines: 21
sha256: c2113169b6c741d07788e27c1e24e07604b71230f5449c4120acd50c7268e066
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.23_file_format.md — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | Fort.23 file format / 입력 구조 — 제목·판본·빈 줄을 포함한다(1–4). 입력 변수 행 및 가독성 설명과 절점 번호·두 복사응력(radiation stress) 성분의 입력행을 제시한다(5–7). 원문: `The basic file structure is shown below. Each line of input data is represented by a line containing the input variable name(s) in bold face type. Blank lines are only to enhance readability. ` (5); `[JN](/index.php?title=JN&action=edit&redlink=1), [RSX(JN)](/index.php?title=RSX(JN)&action=edit&redlink=1), [RSY(JN)](/index.php?title=RSY(JN)&action=edit&redlink=1)` (7). |
| 9–18 | Notes / 자료 수·시각·행 형식 — 시간 보간(temporal interpolation)을 위해 최소 두 자료 묶음이 필요하며 하나뿐이면 예기치 않은 파일 끝 오류(end-of-file error)로 종료한다고 명시한다(11). 일부 절점에 직접 입력하며 초기화별 첫 자료 시각·후속 자료 간격과 시간 보간을 적는다(13–15). 행 형식·시간 증가분 종료 표식과 새 시각에 생략한 절점의 0 응력을 명시한다(17). 원문: `At least two datasets must be present in the file to allow for time interpolation. If only one dataset is present, the run will terminate with an unexpected end-of-file error` (11); `Radiation stresses are input directly to a subset of nodes in the ADCIRC grid (as specified by the node number [JN](/index.php?title=JN&action=edit&redlink=1)).` (13); `If ADCIRC is cold started, the first set of radiation stress data corresponds to [TIME](/index.php?title=TIME&action=edit&redlink=1)=[STATIM](/index.php?title=STATIM&action=edit&redlink=1). If ADCIRC is hot started, the first set of radiation stress data corresponds to [TIME](/index.php?title=TIME&action=edit&redlink=1)=HOT START TIME. Additional sets of radiation stress data must be provided every [RSTIMINC](/index.php?title=RSTIMINC&action=edit&redlink=1), where [RSTIMINC](/index.php?title=RSTIMINC&action=edit&redlink=1) is the radiation stress time interval and is specified in the Model Parameter and Periodic Boundary Condition File. Radiation stresses are interpolated in time to the ADCIRC time step.` (15); `Each data line must have the format I8, 2E13.5.Data input lines are repeated for as many nodes as desired. A line containing the # symbol in column 2 indicates radiation stress data at the next time increment begins on the following line. At each new time, any node that is not specified in the input file is assumed to have zero wave radiation stress.` (17). |
| 19–21 | Notes / 단위·기간 — 중력의 단위와 일치하는 속도 제곱으로 입력하고 힘/면적 응력을 물의 기준 밀도(reference density)로 나눠 해당 단위를 얻는다고 적는다(19). 전체 실행 기간의 자료가 필요하며 부족하면 실행이 중단된다고 명시한다(21). 원문: `Wave radiation stress must be input in units of velocity squared (consistent with the units of gravity). Stress in these units is obtained by dividing stress in units of force/area by the reference density of water.` (19); `Data must be provided for the entire model run, otherwise the run will crash.` (21). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 7·13·15: 변수 참조 URL에 `action=edit&redlink=1`이 들어 있다.
