---
file: models/ADCIRC/raw/manuals/wiki/markdown/Boundary_Conditions.md
lines: 31
sha256: 157d56fbf1cf2c050ea389929732b6f93485536e4fd3671e8ee0a752f3ed56ab
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Boundary_Conditions.md — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 제목·판본 표기·빈 줄·목차를 포함한다(1–16). Boundary conditions — 측면 경계조건(lateral boundary condition)은 경계의 물리를 제약하고 초기조건(initial condition)은 시작 상태를 지정한다고 설명한다(5). 불투수 벽의 법선 흐름을 예로 들며 ADCIRC에서는 보통 수위 또는 속도·유량 중 하나를, 때로 둘을 제약한다고 적는다(5). |
| 17–20 | Flux Boundaries — ADCIRC가 기본적으로 격자 경계에서 무유량(no-flux) 조건을 약하게(weakly) 만족한다고 설명한다(19). 세부 조건을 지정할 문서 링크를 제공한다(19). 원문: `By default ADCIRC weakly satisfies the no-flux boundary condition at mesh boundaries. See [flux specified boundaries](/Flux_specified_boundaries) for details on fine-grained specification of the flux boundary conditions if required.` (19). |
| 21–22 | Elevation Boundaries — 절 제목과 빈 줄만 있으며 설명은 없다(21–22). |
| 23–28 | Automatic Specific of Boundary Conditions — OceanMesh2D의 `makens`에서 `'auto'` 옵션을 사용하는 조건과 지리공간 해안선 자료의 필요성을 설명한다(25). 바다와 해안·육지 경계를 판별하여 기본 수위·자연 무유량 경계조건(natural no-flux boundary condition)을 적용한다(25). 강·보(weir)의 수동 지정 옵션도 있다고 적는다(27). 원문: `The OceanMesh2D[&#91;1&#93;](#cite_note-1)[(GitHub site)](https://github.com/CHLNDDEV/OceanMesh2D) mesh generation toolbox has the ability to automatically apply the basic no-flux and open ocean elevation boundary conditions for an ADCIRC mesh. See the makens (make node-string) function using the 'auto' option. Geospatial shoreline data is required to automatically detect whether a mesh boundary is located in the ocean (applies open ocean elevation boundary condition) or is along the shoreline/on-land (applies natural no-flux boundary condition). ` (25). |
| 29–31 | References — Roberts·Pringle·Westerink(2019)의 OceanMesh2D 논문과 DOI를 제공한다(31). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 21–22: `Elevation Boundaries`는 제목과 빈 줄만 있으며 본문이 없다.
