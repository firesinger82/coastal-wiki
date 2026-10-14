SWASH swashuse.pdf 1–36쪽 전수 검증 기록

검증일은 2026-10-15이다.
쪽 번호 `p.N`은 원문 PDF의 물리적 쪽 번호이다.
원문은 `models/SWASH/raw/source_code/swash/doc/swashuse.pdf`이다.
대조 이미지는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/swhpages/swashuse-NNN.png`이다.
대상 36쪽의 300dpi 이미지를 모두 열어 각 쪽 행과 의미를 대조했다.
수식의 기호와 수치, 기본값과 단위, 명령 문법, 조건, 부정과 불확실성 표현, 절 제목의 인쇄 위치를 확인했다.

| 기록 | 대조한 PDF 쪽 | 대조 쪽 수 | 정정 쪽 수 | 보완 쪽 수 | 정정·보완 중복 쪽 수 | 이상 없음 쪽 수 |
|---|---|---:|---:|---:|---:|---:|
| [p001-018.md](../swash/doc/swashuse.pdf/p001-018.md) | 1–18 전부 | 18 | 9 | 5 | 4 | 8 |
| [p019-036.md](../swash/doc/swashuse.pdf/p019-036.md) | 19–36 전부 | 18 | 16 | 9 | 8 | 1 |
| 합계 | 1–36 전부 | 36 | 25 | 14 | 12 | 9 |

정정과 보완은 각 유형별로 쪽마다 1건으로 센다.
한 쪽에 두 유형이 모두 있으면 각각 센다.
정정·보완 중복 쪽은 p.12, p.13, p.14, p.17, p.19, p.20, p.21, p.24, p.26, p.27, p.28, p.36이다.
수정한 고유 쪽 수는 27쪽이다.
이상 없음 쪽은 p.1, p.2, p.3, p.4, p.5, p.7, p.9, p.10, p.29이다.

아래 목록은 같은 쪽의 같은 유형 변경을 한 행으로 묶었다.
인쇄 원문 열의 따옴표와 백틱 안은 이미지에서 확인한 원문이다.
인쇄 원문 열에서 별도로 표시한 앞 쪽 번호는 절 제목이나 문장 앞부분의 출처이다.

| 기록:쪽 | 이전 요지 | 새 요지 | 인쇄 원문 |
|---|---|---|---|
| p001-018.md:p.6 (정정) | 4.4 Start-up의 명령 목차가 이어진다. | 4.4 Start-up은 앞 쪽(p.5)에 인쇄된 목차 제목임을 명시했다. | p.6의 첫 목차는 `SET ... 25`, `MODE ... 27`, `COORDINATES ... 27`이다. `4.4 Start-up ... 24`는 p.5에 인쇄되어 있다. |
| p001-018.md:p.8 (정정) | B.2.1의 마지막 항목이라고만 기록했다. | B.2.1은 앞 쪽(p.7)에 인쇄된 목차 번호임을 명시했다. | p.8의 첫 목차는 `Repetitions of keywords and/or other data ... 143`이다. `B.2.1 Keywords ... 141`은 p.7에 인쇄되어 있다. |
| p001-018.md:p.11 (보완) | SWAN과 입력 방식이 유사하다는 설명만 기록했다. | SWAN에 익숙한 사용자는 큰 노력 없이 SWASH를 사용할 수 있을 것이라는 원문의 전망을 보완했다. | `Hence, those users who are familiar with SWAN should be able to use SWASH without much effort.` |
| p001-018.md:p.12 (정정) | 2.2.1 제목의 인쇄 위치를 밝히지 않았다. 적용 현상을 급변류라고만 기록했다. | 2.2.1 제목의 출처를 p.11로 명시했다. 적용 현상을 급변류의 복잡한 변화로 고쳤다. | p.11: `2.2.1 Objective and context`. p.12의 적용 현상: `complex changes to rapidly varied flows typically found in coastal flooding`. |
| p001-018.md:p.12 (보완) | 전체 모델링 과정과 수치 안정성·결과 정확성·처리 시간의 설명을 생략했다. | 관심 영역에서 전체 모델링 과정을 수행한다는 설명을 추가했다. 수치 안정성과 견고성에 관한 주장을 추가했다. 합리적인 처리 시간 안에 정확한 결과를 제공한다는 주장을 추가했다. | `the entire modelling process to be carried out in any area of interest`; `it provides numerical stability and robustness`; `it gives accurate results in a reasonable turn-around time`. |
| p001-018.md:p.13 (정정) | 2.2.2 제목의 인쇄 위치를 밝히지 않았다. | 2.2.2 제목의 출처를 p.12로 명시했다. | p.13은 `For accuracy reason, the pressure is split-up ...` 항목으로 시작한다. `2.2.2 A bird’s-eye view of SWASH`는 p.12에 인쇄되어 있다. |
| p001-018.md:p.13 (보완) | leapfrog의 파랑 전파 이점과 비정형 격자의 격자점 분포 유연성 설명을 생략했다. | 파랑 전파에 유익할 것이라는 전망을 추가했다. 비정형 격자의 격자점 분포 유연성이 정형 격자보다 낫다는 설명을 추가했다. | `This will prove beneficial to wave propagation.`; `the level of flexibility with respect to the grid point distribution of unstructured grids is far more optimal compared to structured grids`. |
| p001-018.md:p.14 (정정) | 2.2.2 제목의 인쇄 위치를 밝히지 않았다. | 2.2.2 제목의 출처를 p.12로 명시했다. | p.14는 “respectively). The model improves its frequency dispersion”로 시작한다. “2.2.2 A bird’s-eye view of SWASH”는 p.12에 인쇄되어 있다. |
| p001-018.md:p.14 (보완) | 현업 운용에 관한 가능성 설명을 생략했다. | SWASH를 현업 운용에 사용할 수 있다는 설명을 추가했다. | `SWASH can be used operationally`. |
| p001-018.md:p.15 (정정) | 2.2.3 제목의 인쇄 위치를 밝히지 않았다. | 2.2.3 제목의 출처를 p.14로 명시했다. | p.15는 `as driven by e.g. waves, tides, buoyancy and wind forces`로 시작한다. `2.2.3 Model features and validity of SWASH`는 p.14에 인쇄되어 있다. |
| p001-018.md:p.16 (정정) | 2.2.3 제목의 출처를 생략했다. 3파 상호작용과 쇄파를 분리할 수 있다고만 기록했다. | 2.2.3 제목의 출처를 p.14로 명시했다. 원문이 3파 상호작용과 쇄파를 지배 과정으로 분리해 살피는 예를 든다는 뜻을 복원했다. | p.14: `2.2.3 Model features and validity of SWASH`. p.16: `a typical surf zone where the dominant processes of triad interaction and depth-induced breaking can be isolated`. |
| p001-018.md:p.17 (정정) | 2.2.4 제목의 출처를 생략했다. `wrong (not well-posed)`를 두 대안처럼 연결했다. | 2.2.4 제목의 출처를 p.16으로 명시했다. `not well-posed`가 `wrong`의 괄호 설명임을 보존했다. | p.16: `2.2.4 Relation to Boussinesq-type wave models`. p.17: `the boundary conditions are wrong (not well-posed)`. |
| p001-018.md:p.17 (보완) | Boussinesq형 모델의 대안이라는 결론을 생략했다. 환경 문제의 예측 필요성과 비교 모델의 개발 제약을 생략했다. | 대안으로 볼 수 있다는 표현을 추가했다. 소규모 연안 유동·오염물질 수송의 예측 필요성을 추가했다. 모델 한계·수치 기법·컴퓨터 성능에 관한 개발 제약을 추가했다. | `it can be seen as an attractive alternative to the Boussinesq-type wave models`; `The need to accurately predict small-scale coastal flows and transport of contaminants encountered in environmental issues is becoming more and more recognized.`; `The development of these models is often dictated by model limitations, numerical techniques and computer capabilities.` |
| p001-018.md:p.18 (정정) | 2.3 제목의 인쇄 위치를 밝히지 않았다. | 2.3 제목의 출처를 p.17로 명시했다. | p.18은 `the problem may be only very local, or`로 시작한다. `2.3 Internal scenarios, shortcomings and coding bugs`는 p.17에 인쇄되어 있다. |
| p019-036.md:p.19 (정정) | 입력장을 초기 흐름장과 초기 수위로만 적었다. | 원문의 `(initial)` 괄호를 보존해 (초기) 흐름장과 (초기) 수위로 고쳤다. | `(initial) current field, (initial) water level`. |
| p019-036.md:p.19 (보완) | 두 좌표계의 공통 명칭과 항해 관례의 복수성 설명을 생략했다. 성분 입력 격자 수를 생략했다. | p.18에서 이어지는 문제 좌표계 명칭을 보완했다. 항해 관례가 여럿이라는 괄호 설명을 추가했다. 성분의 초기조건·정상 경계조건용 격자가 하나 이상임을 보완했다. | `designated in this manual as the problem coordinate system.`; `a nautical convention (there are more such conventions)`; `one (or more) spatial input grid(s) for transport of constituents to define initial and stationary boundary conditions for constituents`. |
| p019-036.md:p.20 (정정) | §2.5.1 제목의 인쇄 위치를 밝히지 않았다. | §2.5.1 제목의 출처를 p.19로 명시했다. | p.20에는 §2.5.1 제목이 없다. `2.5.1 Introduction`은 p.19에 인쇄되어 있다. |
| p019-036.md:p.20 (보완) | 바람·압력 입력 시간 구간에서 자료가 존재하는 경우라는 조건을 생략했다. | 바람장과 압력장이 있는 경우라는 조건을 추가했다. | `one (or more) input time window(s) in which wind and pressure field (if present) are given by the user`. |
| p019-036.md:p.21 (정정) | §2.5.2 제목의 인쇄 위치를 밝히지 않았다. | §2.5.2 제목의 출처를 p.20으로 명시했다. | p.21은 `Alternatively, the user may apply a curvilinear, boundary-fitted grid.`로 시작한다. `2.5.2 Computational grid and time window`는 p.20에 인쇄되어 있다. |
| p019-036.md:p.21 (보완) | 조파 경계와 격자 선택에 관한 Chapter 5 참조를 생략했다. 시간 간격이 정확도에 미치는 영향을 생략했다. | Chapter 5 참조 두 곳을 복원했다. 시간 간격이 계산 결과의 정확도에 영향을 준다는 설명을 추가했다. | `see also Chapter 5 for details`; `For further suggestions regarding choice of the resolution and orientation of the computational grid ... Chapter 5.`; `the accuracy of the results of SWASH are obviously affected by the time step`. |
| p019-036.md:p.22 (보완) | 부유체와 능선의 예를 생략했다. 능선이 보간 과정에서 사라질 수 있다는 조건부 설명을 생략했다. | 계류 선박·WECs와 사주·천퇴·방파제 예를 추가했다. 입력 격자와 계산 격자가 같지 않으면 보간 과정에서 능선이 사라질 수 있음을 추가했다. | `floating objects (e.g. moored ships, WECs)`; `sharp and shallow ridges (sand bars, shoals, breakwaters)`; `choosing the computational grid to be identical to the input grid (otherwise the ridge may be ”lost” in the interpolation from the bottom input grid to the computational grid)`. |
| p019-036.md:p.23 (정정) | §2.5.3 제목과 입력 시간 구간의 시작 지시를 이 쪽의 설명으로만 기록했다. | 절 제목과 문장 앞부분이 p.22에서 이어짐을 명시했다. | p.23의 첫 문장은 `so that the initial state of SWASH has propagated through the computational area before reliable output of SWASH is expected.`이다. `The input windows should start early enough`는 p.22 끝에 인쇄되어 있다. |
| p019-036.md:p.24 (정정) | §2.5.4 제목의 인쇄 위치를 밝히지 않았다. | §2.5.4 제목의 출처를 p.23으로 명시했다. | p.24는 `It is advised to make an input grid so large ...`로 시작한다. `2.5.4 Input grid(s) for transport of constituents`는 p.23에 인쇄되어 있다. |
| p019-036.md:p.24 (보완) | 성분 경계값의 측방 이동 설명과 출력 해상도의 임의 선택을 생략했다. | 원문의 측방 이동 설명을 추가했다. 출력 해상도는 임의로 선택할 수 있음을 추가했다. | `the value at the nearest boundary of the input grid (lateral shift of that boundary)`; `An output grid has to be specified by the user with an arbitrary resolution`. |
| p019-036.md:p.25 (정정) | §2.6 제목의 인쇄 위치를 밝히지 않았다. | §2.6 제목의 출처를 p.24로 명시했다. | p.25는 `Irregular multidirectional waves by means of 2D spectrum.` 항목으로 시작한다. `2.6 Boundary conditions`는 p.24에 인쇄되어 있다. |
| p019-036.md:p.26 (정정) | 모델이 수렴해야 하는 상황이라고 기록했다. | `is supposed to converge`를 수렴할 것으로 예상되는 상황으로 고쳤다. | `If all input is correct and the model is supposed to converge`. |
| p019-036.md:p.26 (보완) | 시간 간격 축소를 먼저 시도하라는 권고와 그 이유를 생략했다. | 가장 쉬운 문제 해결 방법이므로 시간 간격 축소부터 시작하라는 권고를 추가했다. | `Since this is the easiest way to overcome problems, it is always a good practice to start with this measure.` |
| p019-036.md:p.27 (정정) | 흐름과 수위를 모두 초기값으로만 적었다. | 원문의 `(initial) current and water level`에서 초기의 괄호를 보존했다. | `file(s) containing: grid, bottom, (initial) current and water level, friction, porosity, and wind and pressure (if relevant)`. |
| p019-036.md:p.27 (보완) | 편집 파일을 이용하면 사용자 설명서를 매번 확인할 필요가 없다는 설명을 생략했다. | 키워드 철자와 자료 순서를 확인할 때마다 사용자 설명서를 참조할 필요는 없다는 설명을 추가했다. | `the user does not need to consult the User Manual every time to check the correct spelling of keywords, order of data, etc.` |
| p019-036.md:p.28 (정정) | §3.2 제목의 인쇄 위치를 밝히지 않았다. | §3.2 제목의 출처를 p.27로 명시했다. | p.28은 `at the user’s request.`로 시작한다. `3.2 Input / output facilities`는 p.27에 인쇄되어 있다. |
| p019-036.md:p.28 (보완) | 출력선의 등심선 예와 메시지의 일반적인 설명 특성을 생략했다. | 출력선의 예로 특정 수심의 등심선을 추가했다. 메시지는 보통 별도 설명 없이 이해할 수 있다는 표현을 추가했다. | `user specified lines (e.g., a given depth contour line)`; `These messages are usually self-explanatory.` |
| p019-036.md:p.30 (정정) | §4.1의 명령 목록이 이어진다고만 기록했다. | §4.1의 인쇄 위치를 앞 쪽(p.29)으로 명시했다. | p.29: “4.1 List of available commands”. p.30에는 §4.1 제목 없이 READTRA 행부터 목록이 이어진다. |
| p019-036.md:p.31 (정정) | §4.1의 명령 목록이 이어진다고만 기록했다. | §4.1의 인쇄 위치를 앞 쪽(p.29)으로 명시했다. | p.29: “4.1 List of available commands”. p.31에는 §4.1 제목 없이 RAY 행부터 목록이 이어진다. |
| p019-036.md:p.32 (정정) | §4.2의 블록 내부 순서 목록이 이어진다고만 기록했다. | §4.2의 인쇄 위치를 앞 쪽(p.31)으로 명시했다. | p.31: “4.2 Sequence of commands”. p.32에는 §4.2 제목 없이 “In block (e)”부터 목록이 이어진다. |
| p019-036.md:p.33 (정정) | §4.4의 PROJect 설명이 이어진다고만 기록했다. | §4.4 제목과 PROJect 명령 구문의 인쇄 위치를 앞 쪽(p.32)으로 명시했다. | p.32: “4.4 Start-up”, “PROJect ’name’ ’nr’”. p.33은 “With this required command”로 시작한다. |
| p019-036.md:p.34 (정정) | §4.4 SET 설명의 앞 쪽 출처를 생략했다. 배경 점성을 계산된 수직 점성보다 작은 값으로만 설명했다. | §4.4 제목은 p.32에 인쇄되었음을 명시했다. SET 설명은 p.33부터 이어짐을 명시했다. 배경 점성은 계산된 수직 점성에 비해 작은 값이어야 한다고 정정했다. | p.32: “4.4 Start-up”. p.33: “SET”. p.34: “The value must be small compared to the vertical viscosity calculated by the standard k − ε model.” |
| p019-036.md:p.35 (정정) | §4.4 SET 설명의 앞 쪽 출처를 생략했다. 이 쪽의 CCM·QC 선택 구문에 없는 ‘투영(projection)’을 덧붙였다. | §4.4 제목의 p.32 출처를 명시했다. SET 설명의 p.33 출처를 명시했다. CCM·QC는 구문에 인쇄된 선택 관계만 기록했다. | p.32: “4.4 Start-up”. p.33: “SET”. p.35 구문: “COORDINATES”, “-> CARTesian”, “SPHErical” 아래 “-> CCM”, “QC”. 이 쪽에는 “projection”이 인쇄되지 않았다. |
| p019-036.md:p.36 (정정) | §4.4 COORDINATES 설명의 앞 쪽 출처를 생략했다. | §4.4 제목은 p.32에 인쇄되었음을 명시했다. COORDINATES 설명은 p.35부터 이어짐을 명시했다. | p.32: “4.4 Start-up”. p.35: “COORDINATES”. p.36은 “CARTESIAN all locations and distances are in m.”으로 선택 설명을 이어간다. |
| p019-036.md:p.36 (보완) | CGRID 구문의 격자 선택 가지 뒤에 인쇄된 &를 기록하지 않았다. | 격자 선택 가지를 닫는 > 뒤에 &가 인쇄되었음을 추가했다. | CGRID 구문에서 세 선택 가지를 닫는 “>” 뒤에 “&”가 인쇄되어 있다. 다음 줄에는 “REPeating” 선택 구문이 있다. |

두 기록의 frontmatter는 변경하지 않았다.
두 기록의 쪽 행 순서와 열 구성은 보존했다.
쪽 행 밖의 기존 문장은 변경하지 않았다.
원문과 노트는 수정하지 않았다.
Git 명령은 실행하지 않았다.
모델은 실행하지 않았다.

정정 25, 보완 14, 이상 없음 9
