---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Working_with_Models/Running_a_Model/Guiding_Principles_for_Running_MPI.md
lines: 33
sha256: a6b9b9e09e5083c7ed84afc79f25dfaf24d19b7fe87b304bacc68071bc1e23f9
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Guiding_Principles_for_Running_MPI.md — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 앞부분 메타데이터. `title: "Guiding Principles for Running MPI"` (3) 및 페이지 ID, space, URL, 버전, 갱신 시각과 문서 계층을 포함한다(1–9). |
| 10–16 | 효율을 결정하는 네 요인. 모델 실행에는 격자 셀(grid cell) 수, 계산할 성분(constituent) 수, 사용 가능한 물리 코어(physical core) 수, 매 시간 단계에서 하위 영역(sub-domain) 사이에 교환되는 데이터 양의 균형이 필요하다고 서술한다(10–15). 요인 이름 원문: `1. Number of grid cells` (12) `2. Number of constituents to be simulated` (13) `3. Number of physical cores available for processing` (14) `4. The amount of data exchanged between sub-domains in each time step` (15) |
| 17–20 | 1. Number of grid cells. 코어당 셀 수에 대한 경험적 지침(rule of thumb)과 초기 영역 분할 예시를 제공한다. 약 1,000개를 최소로 언급하는 문장, 예상 할당 범위 500–10,000개, 최대여야 한다고 서술한 20,000개, 60,000개 셀과 6개 코어의 초기 분할 예시를 모두 원문으로 보존한다. `A general rule of thumb is that the number of cells assigned to a given core should be in the order of some thousands. A minimum of approximately 1,000 cells is needed to make an MPI computation worthwhile.  An individual core would be expected to be assigned from 500 to 10,000 cells.  20,000 cells should be the maximum number of cells on any one core. For example, if we have a hydrodynamic model with 60,000 cells and 6 cores, then the model could initially be divided into six subdomains, each with 10,000 cells.  The user should then adjust the run configuration by increasing or decreasing subdomains.` (19) |
| 21–24 | 2. Number of constituents. 유체역학(hydrodynamics) 외에 염분, 수온, 염료, 퇴적물, 독성물질과 수질 항목의 이송은 풀어야 하는 방정식 수를 늘린다. 각 하위 영역 내부에서는 OMP로 병렬화할 수 있다. 성분이 늘면 더 많은 영역을 권고하는 조건은 `Besides hydrodynamics, each transport process added to the simulation such as salinity, temperature, dye, sediment, toxic, or water quality parameters, requires more equations to be solved. Although the processing of the constituents in each sub-domain can be parallelized using OMP, if more constituents need to be considered, then it is recommended that more domains be used.` (23)이다. |
| 25–28 | 3. Number of physical cores. 프로세서(processor)마다 동일한 계산 부하를 배치하는 목표를 설명한다. 영역마다 층 수가 다른 Sigma-Zed 모델의 예에서 층이 적은 하위 영역에 더 많은 수평 셀을 배치하여 수직·수평 셀 총수가 대략 같도록 분할한다고 적는다. 적용 조건과 'roughly'를 포함한 원문: `The goal of the modeler should be to ensure that an equal computational load is placed on each processor.  This means that if some models have different numbers of layers in different parts of the grid, thought should be given to how to divide the domain.  For example, a Sigma-Zed model could fewer layers in some parts of the domain.  The domain should then be divided in such a way that more horizontal cells are in that one sub-domain so that the total number of vertical and horizontal cells are roughly equal for each sub-domain.` (27) |
| 29–33 | 4. The amount of data exchanged between sub-domains in each time step. 매 시간 단계마다 영역 접면(interface)의 정보를 교환한다. 특히 수질 성분이 많으면 교환량이 매우 커질 수 있다고 적는다. 접면 셀 연결 수를 최적화하여 교환량을 최소화해야 한다는 원문: `The information at the interfaces of the subdomain is exchanged between the subdomains at each time step. If more constituents are simulated, especially for water quality problems, the amount of data exchanged between the subdomain could be very significant. This should be minimized by optimization of the number of cell connections between the subdomains at the interfaces.` (31) 마지막 빈 줄과 구분선도 포함한다(32–33). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 같은 셀 수 지침에서 `A minimum of approximately 1,000 cells is needed to make an MPI computation worthwhile.` (19)와 `An individual core would be expected to be assigned from 500 to 10,000 cells.` (19)를 함께 적는다. 두 수치 지침의 관계를 별도로 설명하지 않는다(19).

