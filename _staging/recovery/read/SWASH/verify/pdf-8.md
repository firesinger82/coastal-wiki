SWASH swashtech.pdf 전수 검증 기록 — 2026-10-15

원문은 `models/SWASH/raw/source_code/swash/doc/swashtech.pdf`이다.
아래 쪽 번호는 PDF 쪽 번호다.
지정된 300 dpi 쪽 이미지 38개를 각각 열어 두 기록의 모든 쪽 행과 대조했다.
이미지 경로는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/swhpages/swashtech-<3자리 쪽번호>.png`이다.
추출 텍스트와 Marker 출력은 보조로만 사용했다.

| 기록 | 대조 범위 | 대조한 쪽 수 | 정정 | 보완 | 이상 없음 |
|---|---|---:|---:|---:|---:|
| [p091-108.md](../swash/doc/swashtech.pdf/p091-108.md) | 91–108 | 18 | 3 | 4 | 13 |
| [p109-128.md](../swash/doc/swashtech.pdf/p109-128.md) | 109–128 | 20 | 0 | 0 | 20 |

정정과 보완은 해당 표식이 붙은 쪽 행을 유형별로 센 값이다.
91쪽과 95쪽은 두 유형에 각각 포함했다.
이상 없음은 수정하지 않은 쪽 행을 센 값이다.
수정한 쪽 행은 91, 93, 95, 105, 107쪽이다.
첫 기록의 이상 없음 쪽은 92, 94, 96–104, 106, 108쪽이다.
두 번째 기록의 이상 없음 쪽은 109–128쪽이다.

| 기록:쪽 | 이전 요지 | 새 요지 | 인쇄 원문 |
|---|---|---|---|
| [p091-108.md:p.91](../swash/doc/swashtech.pdf/p091-108.md) (정정) | A_c를 셀 면적이라고 별도로 정의했다. | 이 쪽에 별도로 인쇄되지 않은 A_c 정의를 삭제했다. | 인쇄식 d_c=(1/A_c)∫_c∇·(ν_h h∇u)dA만 있다. A_c의 별도 정의 문장은 없다. |
| [p091-108.md:p.91](../swash/doc/swashtech.pdf/p091-108.md) (보완) | 질량 플럭스와 운동량 방정식의 식 참조를 생략했다. | 산술 평균 (5.30), 질량 플럭스 (5.29), 운동량 방정식 (3.2), 힘을 제외한 이산화 (5.31)를 추가했다. | “water depths (5.30)”; “This definition is expressed by Eq. (5.29).”; “momentum equation (3.2)”; “without forces that is given by Eq. (5.31)” |
| [p091-108.md:p.93](../swash/doc/swashtech.pdf/p091-108.md) (보완) | 운동량 방정식과 힘 항 적분의 식 참조를 생략했다. | 식 (3.2), (5.31), (5.16), (5.22)와 식 (5.33)에 따른 분배 이유를 추가했다. | “momentum equation (3.2)”; “without forces is given by Eq. (5.31)”; “(cf. Eq. (5.16))”; “Referring to Eq. (5.33) and for consistency with the terms on the left-hand side”; “Like Eq. (5.22)” |
| [p091-108.md:p.95](../swash/doc/swashtech.pdf/p091-108.md) (정정) | 직교성 식의 내적 순서를 u_c·c_c=0으로 옮겼다. | 인쇄 순서인 c_c·u_c=0으로 고쳤다. | “we have c_c · u_c = 0” |
| [p091-108.md:p.95](../swash/doc/swashtech.pdf/p091-108.md) (보완) | 에너지 보존 유도의 식 (5.34)와 확장 대상 식 (5.32)를 생략했다. | 코리올리 힘을 더하는 식 (5.34)와 확장하는 유동 방정식 (5.32)를 추가했다. | “Recall Eq. (5.34). By adding the contribution of the Coriolis force”; “extension of the mimetic discretization of the flow equation (5.32)” |
| [p091-108.md:p.105](../swash/doc/swashtech.pdf/p091-108.md) (정정) | 식 (7.7)의 우변을 설명하면서 식의 위치를 밝히지 않았다. | 식 (7.7)은 앞 쪽인 p.104에 있다고 명시했다. | p.105: “the second term on the right-hand side represents the aliasing error”. 식 번호 (7.7)은 p.104에 인쇄되어 있다. |
| [p091-108.md:p.107](../swash/doc/swashtech.pdf/p091-108.md) (보완) | 발산형과 이류형의 합성곱 합 설명에서 식 참조를 생략했다. | 발산형에 식 (7.8)을 연결했다. 이류형에 식 (7.9)를 연결했다. | “this sum is multiplied by ik′_n (see Eq. (7.8))”; “when the advection term z_m = q_m du_m/dx is discretized (viz. Eq. (7.9))” |

수식의 부호·첨자·지수·분모와 식 참조를 대조했다.
조건·부정·불확실성 표현의 의미를 대조했다.
절 번호·제목·쪽 위치를 대조했다.
숫자·단위·그림 축·범례와 참고문헌의 서지 정보를 대조했다.
대상 쪽에는 입력 명령 문법이나 입력 기본값을 정하는 문장이 없었다.
쪽 행 구성과 frontmatter는 변경하지 않았다.
모델은 실행하지 않았다.
원문·노트·git은 변경하지 않았다.

정정 3, 보완 4, 이상 없음 33
