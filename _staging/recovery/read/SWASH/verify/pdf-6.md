SWASH `swashtech.pdf` 19–54쪽의 판독 기록을 전수 검증했다.

원문은 `models/SWASH/raw/source_code/swash/doc/swashtech.pdf`이다.
대조 근거는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/swhpages/`의 `swashtech-019.png`부터 `swashtech-054.png`까지이다.
지정된 300 dpi 이미지를 쪽 행마다 직접 열어 대조했다.
쪽 번호는 PDF 파일의 쪽 번호이다.

| 기록 | 대조한 PDF 쪽 | 대조한 쪽 수 | 정정 | 보완 | 이상 없음 |
|---|---|---:|---:|---:|---:|
| [p019-036.md](../swash/doc/swashtech.pdf/p019-036.md) | 19–36 | 18 | 17 | 10 | 0 |
| [p037-054.md](../swash/doc/swashtech.pdf/p037-054.md) | 37–54 | 18 | 17 | 7 | 0 |
| 합계 | 19–54 | 36 | 34 | 17 | 0 |

정정과 보완의 집계 단위는 해당 표식이 붙은 쪽 행이다.
같은 쪽 행에 두 표식이 있으면 각 항목에 한 번씩 집계했다.
두 표식이 함께 붙은 쪽 행은 15개이다.
이상 없음은 정정과 보완이 모두 필요하지 않은 쪽 행의 수이다.
두 기록의 frontmatter를 유지했다.
각 기록의 쪽 행 구성과 순서를 유지했다.

아래 목록의 인쇄 원문은 변경 근거가 되는 구절과 수식을 발췌한 것이다.
이어지는 절의 제목을 고친 항목에는 그 제목이 실제로 인쇄된 쪽을 함께 적었다.

| 기록:쪽 | 이전 요지 | 새 요지 | 인쇄 원문 |
|---|---|---|---|
| `p019-036.md:p.19` (보완) | 비압축성·유계 영역 조건과 플럭스형 명칭을 빠뜨렸다. 압력 기울기의 구동력 설명을 빠뜨렸다. | 비압축성 순압류와 2차원 유계 영역을 명시했다. 식 (2.1)–(2.2)를 플럭스형으로 명시했다. 수면 경사에 의한 구동력을 보완했다. | p.19: `barotropic flow of an incompressible fluid in a two-dimensional bounded domain`<br>`The inviscid shallow water equations in the flux-form`<br>`the pressure gradient is a driving force due to the surface slope along the flow line` |
| `p019-036.md:p.20` (정정·보완) | 2.2절의 앞 쪽 출처가 없었다. 보존형의 식 참조와 식 (2.4)의 유도 절차를 빠뜨렸다. | 2.2절의 출처를 p.19로 밝혔다. 보존형의 식 (2.1)–(2.2)를 명시했다. 식 (2.3)과 식 (2.1)의 결합 및 식 (2.2)에 대한 대입을 보완했다. 시간 미분항에 곱의 미분법을 적용함을 보완했다. | p.19: `2.2 Inviscid shallow water equations`<br>p.20: `Eqs. (2.1)–(2.2) are written in the conservation form`<br>`combining Eq. (2.3) and Eq. (2.1), next substituting into Eq. (2.2) while applying the product rule to the term ∂hu/∂t` |
| `p019-036.md:p.21` (정정·보완) | 2.3절의 앞 쪽 출처가 없었다. 내적이 0인 성질의 전제를 대칭 내적만으로 적었다. | 절 제목의 출처를 p.20으로 밝혔다. 연산자 A가 식 (2.9)를 만족한다는 전제를 명시했다. | p.20: `2.3 Hamiltonian formulation`<br>p.21: `As the inner product is symmetric, this implies ⟨u, Au⟩ = 0 for any u ∈ V` |
| `p019-036.md:p.22` (정정·보완) | 절 제목과 범함수 예제의 앞 쪽 출처가 없었다. 특정 성질의 대상을 H와 J로 묶었다. 무한차원 계와 동등한 정식화 및 식 참조를 빠뜨렸다. | 절 제목은 p.20에서 이어짐을 밝혔다. 범함수 예제의 출처를 p.21로 밝혔다. 특정 성질을 갖는 대상은 Poisson 텐서 J로 고쳤다. 무한차원 계와 여러 동등한 정의를 보완했다. 식 (2.1)–(2.2)의 Cartesian 텐서 표현임을 명시했다. | p.20: `2.3 Hamiltonian formulation`<br>p.22: `a functional H(p) and a Poisson tensor J with certain properties`<br>`just one of the many equivalent ways of defining Hamiltonian both for canonical and non-canonical systems`<br>`the Hamiltonian description of Eqs. (2.1)–(2.2)` |
| `p019-036.md:p.23` (정정·보완) | 2.3절의 앞 쪽 출처가 없었다. 시간 변화식에 대한 식 (2.10)과 식 (2.11)의 참조를 빠뜨렸다. | 절 제목의 출처를 p.20으로 밝혔다. 두 시간 변화식의 근거 식 번호를 보완했다. | p.20: `2.3 Hamiltonian formulation`<br>p.23: `Recall Eq. (2.10), then one has`<br>`Owing to Eq. (2.11) we observe that` |
| `p019-036.md:p.24` (정정) | 2.3절의 앞 쪽 출처가 없었다. | 절 제목의 출처를 p.20으로 밝혔다. | p.20: `2.3 Hamiltonian formulation`<br>p.24: `implying the conservation of the Hamiltonian` |
| `p019-036.md:p.25` (정정·보완) | 2.3절의 앞 쪽 출처가 없었다. 이 쪽에 없는 직교 격자 천수방정식 해법을 도입 문장의 내용으로 적었다. 발산 항의 식 참조를 생략했다. | 2.3절의 출처를 p.20으로 밝혔다. 도입 문장의 실제 끝을 적었다. 발산 항의 식 (2.2) 참조와 인쇄 수식을 보완했다. | p.20: `2.3 Hamiltonian formulation`<br>p.25: `the divergence term ∇·(q⊗u) in the momentum equation (2.2), as indicated by Eq. (2.13)`<br>`to demonstrate their utility for the development of a numerical` |
| `p019-036.md:p.26` (정정·보완) | 2.4.1절의 앞 쪽 출처가 없었다. 이 쪽 첫 구절을 p.25 내용으로 적었다. 질량 플럭스의 단면 크기·형상 조건을 빠뜨렸다. | 2.4.1절의 출처를 p.25로 밝혔다. 직교 격자 천수방정식 해법이라는 첫 구절을 이 쪽에 기록했다. 단면 크기·형상에 관계없이 물리적으로 정의된다는 설명을 보완했다. | p.25: `2.4.1 Introduction`<br>p.26: `method for the solution of the shallow water equations on orthogonal meshes`<br>`is physically defined for any size and shape of section S` |
| `p019-036.md:p.27` (정정) | 2.4.2절의 앞 쪽 출처가 없었다. | 2.4.2절의 출처를 p.26으로 밝혔다. | p.26: `2.4.2 Differential forms`<br>p.27: `which provides a geometric interpretation of the divergence operator ∇·` |
| `p019-036.md:p.28` (정정) | 2.4.3절의 앞 쪽 출처가 없었다. | 절 제목의 출처를 p.27로 밝혔다. | p.27: `2.4.3 Generalized Stokes’ theorem`<br>p.28: `that is written as dα^(k), for k = 0, 1, …, n − 1` |
| `p019-036.md:p.29` (정정) | 2.4.3절의 앞 쪽 출처가 없었다. 첫 구절이 앞 쪽의 1-형식 설명에서 이어짐을 밝히지 않았다. | 절 제목의 출처를 p.27로 밝혔다. 첫 구절의 1-형식 설명은 p.28에서 이어짐을 밝혔다. | p.27: `2.4.3 Generalized Stokes’ theorem`<br>p.29: `integrals over a set of edges, 2-forms by their surface integrals over a set of faces` |
| `p019-036.md:p.30` (정정·보완) | 2.4.3절과 첫 문장의 앞 쪽 출처가 없었다. 공변벡터값 3-형식의 체적 조건을 빠뜨렸다. | 절 제목의 출처를 p.27로 밝혔다. 첫 문장은 p.29에서 이어짐을 밝혔다. 임의의 체적 V에서 일관되게 정의된다는 설명을 보완했다. | p.27: `2.4.3 Generalized Stokes’ theorem`<br>p.30: `differential operators, grad, curl and div can then be mimicked at the discrete level`<br>`quantity m dV is consistently defined for any volume V` |
| `p019-036.md:p.31` (정정·보완) | 2.4.4절의 앞 쪽 출처가 없었다. 이 쪽에 없는 비보존형 명칭을 넣었다. 천수방정식 참조 중 (2.1)–(2.2) 또는 (2.4)를 빠뜨렸다. 기저 변화 설명의 보통이라는 한정이 없었다. | 2.4.4절의 출처를 p.30으로 밝혔다. 비보존형을 바로 위 방정식으로 고쳤다. 식 (2.1)–(2.2) 또는 식 (2.4)를 보완했다. 공변·반변 기저 벡터와 보통이라는 한정을 복원했다. | p.30: `2.4.4 Vector-valued differential forms`<br>p.31: `the covariant (and contravariant) base vectors change spatially which is commonly encoded in the covariant derivative and Christoffel symbols`<br>`We revisit the inviscid shallow water equations (2.1)–(2.2) or (2.4)`<br>`we are not considering Eq. (2.2) but rather the equation above` |
| `p019-036.md:p.32` (정정·보완) | 2.4.5절의 앞 쪽 출처가 없었다. 비보존형 명칭은 p.31에만 적혀 있었다. 식 (2.2)의 해석에서 부정 대상을 생략했다. DEC 이산화의 대상을 넓게 적었다. | 절 제목의 출처를 p.31로 밝혔다. 이 쪽에 인쇄된 식 (2.4)의 비보존형 설명을 보완했다. 식 (2.2)를 운동량 방정식이 아니라 유동방정식으로 해석한다는 설명을 복원했다. DEC 비교의 대상을 미분형식의 Lie 이류로 명시했다. | p.31: `2.4.5 Revisiting shallow water equations`<br>p.32: `the non-conservation form of Eq. (2.4) is utilized to reveal the association between the flow variables and geometry`<br>`Eq. (2.2) is interpreted as a flow equation rather than a momentum equation`<br>`the DEC discretizations of the Lie advection of a differential form` |
| `p019-036.md:p.33` (정정) | 2.4.5절의 앞 쪽 출처가 없었다. | 2.4.5절의 출처를 p.31로 밝혔다. | p.31: `2.4.5 Revisiting shallow water equations`<br>p.33: `the term ∇·(q⊗u) separately while adhering to the principles of mimetic discretizations as much as possible` |
| `p019-036.md:p.34` (정정) | 2.5.2절의 앞 쪽 출처가 없었다. 마지막 문장을 이 쪽에 없는 경계의 내부 방향에 대한 문장으로 설명했다. | 절 제목의 출처를 p.33으로 밝혔다. 마지막 문장의 인쇄된 끝 구절만 적었다. | p.33: `2.5.2 Cell complex and orientation`<br>p.34: `Additionally, the inner` |
| `p019-036.md:p.35` (정정) | 2.5.2절의 앞 쪽 출처가 없었다. | 2.5.2절의 출처를 p.33으로 밝혔다. | p.33: `2.5.2 Cell complex and orientation`<br>p.35: `orientation on ∂σ_(k) is induced by σ_(k)` |
| `p019-036.md:p.36` (정정) | 2.5.3절의 앞 쪽 출처가 없었다. | 절 제목의 출처를 p.35로 밝혔다. | p.35: `2.5.3 The computational mesh and its dual`<br>p.36: `polygon. A polygon is well centered if its circumcenter is contained in its interior` |
| `p037-054.md:p.37` (정정·보완) | 첫 설명을 앞 절이라고만 표시했다. 경계 연산자의 반환 대상을 셀 경계로만 적었다. 체인 공간의 생성 기저와 차원의 원소 수 관계를 빠뜨렸다. | 첫 설명이 p.36에서 이어짐을 밝혔다. 경계 연산자를 k-체인에서 (k−1)-체인으로 가는 선형 연산자로 고쳤다. C_k(K)의 생성 기저와 기본 k-체인 명칭 및 차원의 원소 수 관계를 보완했다. | p.37: `Let C_k(K) be a group generated by a basis consisting of all the k-cells of cell complex K`<br>`The dimension of C_k(K) equals the number of elements of M_k`<br>`a k-cell is also named as an elementary k-chain`<br>`a linear operator ∂_k : C_k(K) → C_(k−1)(K)` |
| `p037-054.md:p.38` (정정·보완) | 2.5.4절의 앞 쪽 출처가 없었다. 행렬 성분의 식 (2.15) 참조를 빠뜨렸다. | 2.5.4절의 출처를 p.37로 밝혔다. 행렬 성분의 근거 식 (2.15)를 보완했다. | p.37: `2.5.4 Chains and boundary operator`<br>p.38: `Owing to Eq. (2.15), the entries of the matrix are given by` |
| `p037-054.md:p.39` (정정·보완) | 2.5.5절의 앞 쪽 출처가 없었다. 이산 외미분이 계량에 무관하다는 성질을 빠뜨렸다. | 절 제목의 출처를 p.38로 밝혔다. 쌍대 쌍짓기에서 얻는 이산 외미분의 계량 독립성을 보완했다. | p.38: `2.5.5 Cochains and coboundary operator`<br>p.39: `By virtue of the duality pairing between the boundary operator and coboundary operator, the discrete exterior derivative is a metric independent operator` |
| `p037-054.md:p.40` (정정·보완) | 2.5.5절의 앞 쪽 출처가 없었다. 내부 방향을 선택하는 대상과 Stokes 정리의 성립 대상을 생략했다. 방향 계수의 식 (2.15) 참조를 빠뜨렸다. | 2.5.5절의 출처를 p.38로 밝혔다. 셀 복합체 K의 내부 방향 선택과 대응 k-셀에서의 Stokes 정리 성립을 명시했다. 원시 방향 계수의 식 (2.15) 참조를 보완했다. | p.38: `2.5.5 Cochains and coboundary operator`<br>p.40: `an inner orientation for cell complex K in R²`<br>`the Stokes’ theorem holds for the associated inner-oriented k-cells`<br>`This orientation coefficient is related to that on the primal mesh, viz. Eq. (2.15)` |
| `p037-054.md:p.41` (정정) | 2.5.6절의 앞 쪽 출처가 없었다. | 절 제목의 출처를 p.40으로 밝혔다. | p.40: `2.5.6 The dual mesh: discrete k-forms and exterior derivative`<br>p.41: `between the primal and dual boundary operators as follows` |
| `p037-054.md:p.42` (정정·보완) | 2.5.7절의 앞 쪽 출처가 없었다. 원시 격자의 영역과 안정성 조건의 절 참조가 빠졌다. | 절 제목의 출처를 p.41로 밝혔다. 영역 Ω⊂ℝ²와 2.5.8절 참조를 넣었다. | p.41: `2.5.7 Discrete Hodge star operators`<br>p.42: `primal mesh K on Ω ⊂ ℝ²`<br>`As will be explained in Section 2.5.8, a required condition for numerical stability` |
| `p037-054.md:p.43` (정정) | 2.5.7절의 앞 쪽 출처가 없었다. | 절 제목의 출처를 p.41로 밝혔다. | p.41: `2.5.7 Discrete Hodge star operators`<br>p.43: `employed, provided that the primal mesh is well centered` |
| `p037-054.md:p.44` (정정) | 2.5.7절의 앞 쪽 출처가 없었다. 무게중심 선택을 둔각삼각형 설명 뒤의 ‘이 경우’로만 표시했다. | 2.5.7절 시작 쪽을 p.41로 밝혔다. 무게중심 선택의 대상에 직각삼각형과 둔각삼각형의 문제를 모두 명시했다. | p.41: `2.5.7 Discrete Hodge star operators`<br>p.44: `for a right-angled triangle, matrix ℍ¹ is singular`<br>`ℍ¹ is negative definite`<br>`To overcome these unwanted cases` |
| `p037-054.md:p.45` (정정) | 2.5.8절의 앞 쪽 출처가 없었다. | 절 제목의 출처를 p.44로 밝혔다. | p.44: `2.5.8 Discrete inner products`<br>p.45: `and similarly,` |
| `p037-054.md:p.46` (정정) | 2.5.9절의 앞 쪽 출처가 없었다. | 절 제목의 출처를 p.45로 밝혔다. | p.45: `2.5.9 Discrete de Rham complexes`<br>p.46: `upper part of the diagram constitutes a cochain complex of outer-oriented discrete forms` |
| `p037-054.md:p.47` (정정) | 2.5.9절의 앞 쪽 출처가 없었다. | 2.5.9절 시작 쪽을 p.45로 밝혔다. | p.45: `2.5.9 Discrete de Rham complexes`<br>p.47: `bottom center of the diagram. We can walk through the diagram in two ways` |
| `p037-054.md:p.48` (정정·보완) | 2.5.10절의 앞 쪽 출처가 없었다. 기저가 속한 체인 공간과 식 (2.16)·(2.17) 참조가 빠졌다. | 절 제목의 출처를 p.47로 밝혔다. 0-체인 선형 공간과 C₁(K_sq)를 명시했다. 계수와 경계 행렬의 식 참조를 복원했다. | p.47: `2.5.10 Examples`<br>p.48: `the basis of the linear space of 0-chains`<br>`the basis of C₁(K_sq)`<br>`Referring to Eq. (2.16)`<br>`By virtue of Eq. (2.17)` |
| `p037-054.md:p.49` (정정) | 2.5.10절의 앞 쪽 출처가 없었다. | 절 제목의 출처를 p.47로 밝혔다. | p.47: `2.5.10 Examples`<br>p.49: `the boundary of the second 1-chain from the above example` |
| `p037-054.md:p.50` (정정) | 2.5.10절의 앞 쪽 출처가 없었다. Figure 2.7에 이 쪽에서 쓰지 않은 ‘외심’을 덧붙였다. 쌍대 꼭짓점의 위치를 ‘각 원시 셀 안’으로 한정했다. | 절 제목의 출처를 p.47로 밝혔다. 그림 설명을 ‘쌍대 셀’로 고쳤다. 꼭짓점과 면의 수를 원문처럼 각 격자 셀에 대응하여 설명했다. | p.47: `2.5.10 Examples`<br>p.50: `Dual computational cells with oriented (2−k)-cells`<br>`only have one vertex and multiple faces for each mesh cell` |
| `p037-054.md:p.51` (정정) | 2.5.10절의 앞 쪽 출처가 없었다. 연속 항등식 ∇·∇×의 우변을 보통체 0으로 적었다. | 절 제목의 출처를 p.47로 밝혔다. 연속 항등식의 우변을 인쇄된 굵은 영기호로 고쳤다. | p.47: `2.5.10 Examples`<br>p.51: `Subsequently, the coboundary operators can be found as follows`<br>`∇·∇× = 𝟎` |
| `p037-054.md:p.52` (정정) | 2.5.10절의 앞 쪽 출처가 없었다. 이 쪽에 없는 Figure 2.7a와 단위 정사각형 설명의 출처가 없었다. | 절 제목의 출처를 p.47로 밝혔다. 첫 행렬의 예제 설명은 p.51에서 이어진다고 명시했다. | p.47: `2.5.10 Examples`<br>p.52: `The Hodge star matrix that acts on 0-, 1- and 2-forms is then given by, respectively,` |
| `p037-054.md:p.53` (보완) | 모방 방법이 유용한 조건에서 물리적 정확도를 희생하지 않는다는 한정과 ‘이러한 성질을 가진’이라는 범위가 빠졌다. | 물리적 정확도를 희생하지 않고서는 비선형 운동의 모든 규모를 해상할 수 없는 조건을 넣었다. 앞서 제시한 성질을 가진 모방 방법이라는 범위를 복원했다. | p.53: `mimetic methods possessing these properties are useful when not all scales of nonlinear motion can be resolved without sacrificing physical accuracy, especially when grid refinement or high order discretizations are insufficient` |
| `p037-054.md:p.54` (정정) | 캡션이 ‘형식의 물리적 정의’를 제공한다고 요약했다. | 캡션의 대상은 ‘이산 형식과 격자 요소의 정의’라고 고쳤다. | p.54: `Definitions of discrete forms and mesh elements are provided in the text` |

p.54의 Figure 2.8에서 왼쪽 쌍대 끝점 첨자는 원본 픽셀을 확대해도 숫자 `1`과 소문자 `l`을 확정하지 못했다.
해당 쪽 행의 `[원문 인쇄 판독 불가]` 표기를 유지했다.

정정 34, 보완 17, 이상 없음 0

