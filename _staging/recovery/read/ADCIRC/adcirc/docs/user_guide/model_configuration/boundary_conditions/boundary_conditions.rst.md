---
file: models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/boundary_conditions/boundary_conditions.rst
lines: 64
sha256: 8642bbe56c5f0350e3607e83cdaf1e89a39a65eff784678c2d3107682e67ce06
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# boundary_conditions.rst — 판독 구간 기록

구간은 1행부터 64행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | Boundary Conditions — 메타 지시문·앵커·제목을 포함한다(1–8). 측면 경계 조건(lateral boundary condition)은 경계의 물리량을 제약한다고 설명한다(10–15). ADCIRC는 수위와 유속·플럭스(flux)를 풀며 경계에서 보통 둘 중 하나, 때로 둘 모두를 제약한다고 적는다(16–18). 원문: `**Lateral boundary conditions** allow one to constrain the physics along` (10); ``boundaries in the model. They are similar to `initial`` (11); ``conditions <initial_conditions>`__, which specify the model state at start time.`` (12); `As an example, at the walls of a bathtub, the flow normal to the walls is zero` (13); `since they are impermeable. For general information on the topic, see the` (14); `` `Wikipedia article <https://en.wikipedia.org/wiki/Boundary_value_problem>`__. `` (15); `Since ADCIRC solves for water elevations and velocities (fluxes), typically one` (16); `(occasionally both) of these two quantities are constrained at the lateral` (17); `boundaries.` (18). |
| 20–24 | Open Boundaries — 개방 경계(open boundary)는 수면 고도 지정 경계이다(23). 위치는 fort.14, 주기 조건의 진폭·주파수·위상은 fort.15, 비주기 수위 시계열은 fort.19에 정의한다고 적는다(23). 원문: ``Open boundaries are boundaries where the water surface elevation is specified. Locations of the open boundaries are specified in :ref:`fort.14 <fort14>` file. For periodic conditions, the amplitudes, frequencies, and phases are defined in the :ref:`fort.15 <fort15>` file. For non-periodic conditions, time series of the water surface elevations are defined in the :ref:`fort.19 <fort19>` file.`` (23). |
| 25–34 | Flux Boundaries — 법선 플럭스(normal flux) 경계의 위치는 fort.14, 주기 조건은 fort.15, 비주기 법선 플럭스 시계열은 fort.20에 정의한다고 적는다(28). ADCIRC가 기본적으로 격자 경계의 무플럭스(no-flux) 조건을 약하게 만족한다고 적는다(30–33). 원문: ``Flux boundaries are boundaries where the normal flux is specified. Locations of the flux boundaries are specified in :ref:`fort.14 <fort14>` file. For periodic conditions, the amplitudes, frequencies, and phases are defined in the :ref:`fort.15 <fort15>` file. For non-periodic conditions, time series of the normal fluxes are defined in the :ref:`fort.20 <fort20>` file.`` (28); `By default ADCIRC weakly satisfies the no-flux boundary condition at mesh` (30); ``boundaries. See :ref:`flux specified boundaries <flux_specified_boundaries>` for`` (31); `details on fine-grained specification of the flux boundary conditions if` (32); `required.` (33). |
| 35–51 | Automatic Specific of Boundary Conditions — OceanMesh2D의 makens 함수 auto 옵션은 기본 무플럭스·개방 해양 수위 경계를 자동 지정할 수 있다고 적는다(40–44). 해양·해안선·육상 경계 구분에는 지리공간 해안선 자료가 필요하다(44–47). makens의 다른 옵션은 하천·보(weir) 등의 수동 지정에도 사용한다고 적는다(49–50). 원문: ``The OceanMesh2D [1]_\ `(GitHub`` (40); ``site) <https://github.com/CHLNDDEV/OceanMesh2D>`__ mesh generation toolbox has`` (41); `the ability to automatically apply the basic no-flux and open ocean elevation` (42); `boundary conditions for an ADCIRC mesh. See the **makens** (make node-string)` (43); `function using the 'auto' option. Geospatial shoreline data is required to` (44); `automatically detect whether a mesh boundary is located in the ocean (applies` (45); `open ocean elevation boundary condition) or is along the shoreline/on-land` (46); `(applies natural no-flux boundary condition).` (47); `The **makens** function also contains other options for manually specifying` (49); `other boundary condition types such as rivers and weirs.` (50). |
| 52–64 | References — raw HTML references 지시문과 OceanMesh2D 1.0의 비정형 격자(unstructured mesh) 생성 논문 및 DOI를 포함한다(55–63). 마지막 빈 행을 포함한다(64). 원문: `.. [1]` (59); `   Roberts, K. J., Pringle, W. J., & Westerink, J. J. (2019). OceanMesh2D 1.0:` (60); `   MATLAB-based software for two-dimensional unstructured mesh generation in` (61); `   coastal ocean modeling. Geoscientific Model Development, 12, 1847–1868.` (62); `   https://doi.org/10.5194/gmd-12-1847-2019` (63). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
