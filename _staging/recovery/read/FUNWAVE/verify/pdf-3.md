# FUNWAVE PDF 전수 검증 3

검증일: 2026-10-17.

대조 기준은 지정된 300dpi 쪽 이미지다.
텍스트 추출본은 보조 자료로 사용한다.
정정·보완 수는 아래 목록의 항목 수다.
한 쪽에 정정과 보완이 함께 있으면 각각 한 항목으로 집계한다.
이상 없음 수는 수정이 필요하지 않은 쪽 행 수다.
같은 쪽의 같은 변경을 끝 절에 반복한 것은 중복 집계하지 않는다.

| 기록 | 대상 행 수 | 대조한 행 수 | 상태 |
|---|---:|---:|---|
| `FUNWAVE-TVD/doc/funwave_tvd_3.0.pdf/p073-089.md` | 17 | 17 | p.73–89 전체 완료. |
| `FUNWAVE-TVD/doc/funwave_tvd_2.1_manual.pdf/p001-018.md` | 18 | 18 | p.1–18 전체 완료. |

기록 경로는 `_staging/recovery/read/FUNWAVE/` 기준이다.
원문 행은 PDF 쪽 이미지 안의 문장·수식·캡션 위치로 표시한다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| 3.0:p.73 (보완) | 캡션과 범례를 각각 옮겼으나 모순을 명시하지 않았다. | 그림 23의 캡션과 그림 내부 범례는 실선의 의미가 서로 모순된다. 캡션은 자료를 별표로 설명하지만 그림에는 별표가 없다. | 그림 23 범례: 실선 data, 파선 model. 캡션: `Solid line: model, stars: data.` 그림에 별표가 없다. |
| 3.0:p.74 (보완) | 캡션과 범례를 각각 옮겼으나 모순을 명시하지 않았다. | 그림 24의 캡션과 그림 내부 범례는 실선과 파선의 의미가 서로 반대이므로 모순된다. | 그림 24 범례: 실선 data, 파선 model. 캡션: `Solid line: model, dashed line: data.` |
| 3.0:p.75 (정정) | 첫 문구를 전쪽의 연속으로 설명했다. 유속 예측 설명에서 `at both locations`를 빠뜨렸다. 위치 수의 차이는 p.74와 비교했다. | 첫 문구 자체를 기록했다. 유속 예측의 두 위치 한정을 복원했다. 같은 문단의 ADV 세 위치 열거와 맞지 않는 점을 명시했다. | 쪽 첫 행 `and its reflection from the shore.` 둘째 문단: `ADV 1 ... ADV 2 ... ADV 3 ... at both locations`. |
| 3.0:p.76 (정정) | 첫 입력에 앞쪽의 SPONGE LAYER 라벨을 붙였다. 다음 쪽으로 넘어가는 i의 정의를 격자 번호로 채웠다. | 쪽 맨 위의 입력으로 기록했다. 괄호의 i=500과 정의가 다음 쪽으로 이어지는 상태를 기록했다. | p.76 첫 행 `DIFFUSION_SPONGE = F` 앞에는 SPONGE LAYER 라벨이 없다. 마지막 문구는 `(i = 500, where i is`이다. |
| 3.0:p.76 (보완) | 고립파의 형태 유지 특성과 Grid_B가 Grid_A 내부에 놓인다는 설명을 명시하지 않았다. | `of permanent form`을 복원했다. Grid_B가 Grid_A 내부에 중첩됨을 기록했다. | 5.8절 첫 문단: `a solitary wave of permanent form`; `Grid_B ... is nested inside Grid_A`. |
| 3.0:p.77 (정정) | 이 쪽에 인쇄되지 않은 5.8 절 제목과 첫 문구의 주어 i를 앞쪽에서 가져왔다. | 절 번호·제목이 인쇄되지 않았음을 명시했다. 주어를 채우지 않고 실제 첫 문구를 기록했다. | p.77 첫 행: `grid number in x direction in Grid_A).` 이 쪽에는 5.8 절 제목이 없다. |
| 3.0:p.78 (정정) | 5.8 절 제목을 반복했다. 앞쪽에서 가져온 Grid_A·WAVEMAKER 라벨을 쪽 위 입력에 붙였다. | 절 제목이 없음을 명시했다. 첫 입력들은 이 쪽에 보이는 PHYSICS·NUMERICS·OUTPUT 구분만 사용했다. 실제 인쇄된 아래쪽 Grid_B 안내는 유지했다. | p.78 첫 행 `DEP = 10.0`. 뒤의 PHYSICS·NUMERICS·OUTPUT 구분. 아래쪽 `The input parameters for Grid_B are listed below.` |
| 3.0:p.79 (정정) | 이 쪽에 없는 5.8 절 제목과 Grid_B·GRID 라벨을 앞쪽에서 가져왔다. | 앞쪽에서 가져온 라벨을 제거했다. 실제 인쇄된 아래쪽 6절 제목은 유지했다. | p.79 첫 행 `Dtheta = 0.0001`. 이 행 앞에는 GRID나 Grid_B가 없다. 아래쪽 제목은 `6 Dealing with numerical instability`이다. |
| 3.0:p.79 (보완) | 마지막 문장이 균형 보존형에 관한 내용이라는 점만 기록했다. | 수면 기울기 항이 균형 보존형임에도 불구하고라는 `Although`의 양보 관계를 복원했다. | 마지막 두 행: `Although the surface gradient term is in a well-balanced form as described in the`. |
| 3.0:p.81 (정정) | 쪽 상단에 인쇄되지 않은 6절 제목과 항목 번호 1을 붙였다. | 제목·항목 번호 없이 이어지는 바닥 경사 설명으로 기록했다. 실제 인쇄된 항목 2–5와 7절 제목을 유지했다. | p.81 첫 행 `theory section, an unreasonably large bottom slope may cause numerical instability.` 다음 항목 번호는 2이다. 아래쪽 제목은 `7 References`이다. |
| 3.0:p.82 (정정) | 이 쪽에 없는 `7 References` 절 제목을 반복했다. | 절 번호·제목 없이 이어지는 서지 목록으로 기록했다. | p.82 첫 행은 Briggs et al. (1994)의 서지 항목이다. 절 제목은 인쇄되어 있지 않다. |
| 3.0:p.82 (보완) | Briggs et al. (1994)의 학회명과 국가를 빠뜨렸다. | International Association for Hydraulic Research와 The Netherlands를 복원했다. | 첫 서지 항목 둘째·셋째 행: `International Association for Hydraulic Research, Delft, The Netherlands, 446-455`. |
| 3.0:p.83 (정정) | 이 쪽에 없는 `7 References` 절 제목을 반복했다. | 절 번호·제목 없이 이어지는 서지 목록으로 기록했다. | p.83 첫 행은 Kim, Cho and Kim (2008)의 서지 항목이다. 절 제목은 인쇄되어 있지 않다. |
| 3.0:p.83 (보완) | Kirby et al. (1998)과 Long and Kirby (2006)의 발행 연구소·학과를 빠뜨렸다. | 두 보고서의 Center for Applied Coastal Research와 Civil and Environmental Engineering 학과를 복원했다. | Kirby (1998) 항목 셋째·넷째 행. Long and Kirby (2006) 항목 둘째·셋째 행. |
| 3.0:p.84 (정정) | 이 쪽에 없는 `7 References` 절 제목을 반복했다. | 절 번호·제목 없이 이어지는 서지 목록으로 기록했다. | p.84 첫 행은 Nwogu (1993)의 서지 항목이다. 절 제목은 인쇄되어 있지 않다. |
| 3.0:p.84 (보완) | Nwogu and Demirbilek (2001)의 연구소명을 빠뜨렸다. | Coastal and Hydraulics Laboratory를 복원했다. | 둘째 서지 항목 둘째 행: `ERDC/CHL TR-01-25, Coastal and Hydraulics Laboratory, USACOE`. |
| 3.0:p.85 (정정) | 이 쪽에 없는 `7 References` 절 제목을 반복했다. | 절 번호·제목 없이 실린 서지 목록으로 기록했다. | p.85 첫 행은 Tehranirad et al. (2011)의 서지 항목이다. 절 제목은 인쇄되어 있지 않다. |
| 3.0:p.85 (보완) | Tehranirad et al. (2011)의 발행 연구소를 빠뜨렸다. | Center for Applied Coastal Research를 복원했다. | 첫 서지 항목 셋째 행: `No. CACR-11-02, Center for Applied Coastal Research, University of Delaware`. |
| 3.0:p.87 (정정) | 수식만 있는 쪽에 8절의 Appendix A 전체 제목을 반복했다. | 절 번호·제목이 이 쪽에 인쇄되지 않았음을 명시했다. | p.87은 U₃의 식 (113)으로 시작하며 식 (113)–(118)과 쪽 번호만 있다. |
| 3.0:p.88 (정정) | 이 쪽에 없는 8절의 Appendix A 전체 제목을 반복했다. | 절 번호·제목이 이 쪽에 인쇄되지 않았음을 명시했다. | p.88 첫 문구는 `In detail,`이다. 뒤에는 식 (119)과 쪽 번호가 있다. 절 제목은 없다. |
| 3.0:p.89 (정정) | 수식만 있는 쪽에 8절의 Appendix A 전체 제목을 반복했다. | 절 번호·제목이 이 쪽에 인쇄되지 않았음을 명시했다. | p.89에는 V₂의 식 (120)과 쪽 번호만 있다. |
| 2.1:p.3 (보완) | 침수 모의의 지역·연안 규모를 명시하지 않았다. 문서가 제공하는 상세 수치 기법·사용자 설명서·예제를 빠뜨렸다. | 모의 규모를 복원했다. 문서 제공 내용 세 항목을 보완했다. | 초록 첫 문단: `a regional/coastal scale for prediction of coastal inundation`; `detailed numerical schemes, users’ manual and examples`. |
| 2.1:p.5 (정정) | 그림 목록의 비교 대상에 처오름(runup)을 포함했다. | 이 쪽 캡션에 없는 처오름 귀속을 삭제했다. | List of Figures 항목 1–20. 어느 항목도 `runup`을 비교 대상으로 쓰지 않는다. |
| 2.1:p.6 (정정) | 그림 22의 원문 캡션과 설명을 `Grid A`, `Grid B`로 기록했다. 이 쪽에 인쇄되지 않은 목록 제목을 붙였다. | 이미지의 `Grid_A`, `Grid_B`를 복원했다. 목록 항목만 실려 있고 제목은 인쇄되지 않았음을 명시했다. | List of Figures 항목 22: `larger domain Grid_A (upper)`; `domain Grid_B (lower)`. 쪽 첫 행은 그림 21의 목록 항목이다. |
| 2.1:p.7 (정정) | `each gauge`를 각 파고계로 특정했다. | 장비 종류를 특정하지 않는 각 관측점(gauge)으로 기록했다. | 표 1 목록 캡션: `calculated for each gauge in conical island test`. |
| 2.1:p.8 (보완) | 시간평균 특성값 계산을 별도로 기록하지 않았다. 조파기 추가에 붙은 Shi et al. (2012b) 인용을 빠뜨렸다. Kirby 방정식 집합의 비교 표현을 빠뜨렸다. | 시간평균 계산을 복원했다. 조파기 벤치마크의 출처를 붙였다. 더 완전한 구면좌표계 방정식 집합이라는 서술을 복원했다. | 첫 문단 `calculation of time-averaged properties`. 1.1 변경 사항 4의 `(Shi et al., 2012b)`. 2.0 첫 문단 `a more complete set of Boussinesq equations in spherical coordinates`. |
| 2.1:p.9 (정정) | `gauges`의 입력을 파고계 입력으로 특정했다. 첫 두 항목에 이 쪽에 인쇄되지 않은 목록 제목을 붙였다. | 장비 종류를 특정하지 않는 관측점(gauges)으로 기록했다. 첫 두 항목의 번호는 3과 4로 기록했다. 이 두 항목의 목록 제목이 이 쪽에 없음을 명시했다. | 변경 사항 3: `Input format for gauges was changed to geographic coordinates (Lat/Lon) in the spherical mode`. 쪽 첫 두 항목은 3과 4이다. 아래쪽 제목은 `Differences between Version 2.1 and Version 2.0`이다. |
| 2.1:p.10 (정정) | 분산 근사 차수를 높였다고 단정했다. 상대적 천해 제한은 완화했다고 요약했다. 완전 비선형식에서는 전개 매개변수만 제거했다고 기록했다. | 차수를 높일 수 있음을 보였다는 표현을 복원했다. 천해 제한을 사실상 없앴다는 강도를 복원했다. 척도 또는 전개 매개변수를 모두 기록했다. | 첫 문단 `could be increased`; `have effectively eliminated the restriction`; `a scaling or expansion parameter`. |
| 2.1:p.10 (보완) | 고차·다층·완전 비선형·기존 FUNWAVE 수치 기법의 출처 일부를 빠뜨렸다. 수면 변동 규모, 적용 범위, 성능 설명, 기존 수치 구현 종류를 생략했다. | Gobbi (2000), Agnon (1999), Lynett and Liu (2004), Wei (1995), Kirby (1998), Wei and Kirby (1995)를 해당 설명에 복원했다. 천수변형대 이상 적용, 쇄파대·포말대 수면 변동, 파고 감쇠, 단순·복잡 지형, 수직 난류 구조, 유한차분·유한체적·유한요소 구현, 공개 소스 이력을 보완했다. | 첫 문단 전체. 둘째 문단의 `finite difference, finite volume, or finite element`, `public domain open-source code`, `(Wei and Kirby, 1995)`, `Wei et al (1995)`. |
| 2.1:p.11 (정정) | 기존 모형이 약하게 불안정했다고만 기록했다. 경계조건 수정과 엇갈림 격자의 효과를 합쳐 설명했다. 인쇄되지 않은 절 번호·제목을 붙였다. 새 형식 개발의 동기를 잡음 하나로 좁혔다. | 잡음이 있거나 적어도 약하게 불안정했다는 표현을 복원했다. Kennedy의 일부 원인·일부 완화와 Shi의 잡음 민감도 감소를 구분했다. 절 번호·제목이 인쇄되지 않았음을 명시했다. 일반화 목적과 여러 중대한 문제라는 설명을 복원했다. | 둘째 문단 `“noisy”, or at least weakly unstable`; `partially due to implementation of boundary conditions`; `could be alleviated to an extent`; `less susceptible`. 이 쪽에는 절 제목이 없다. 첫 문장 `aimed at generalizing`. 둘째 문단 첫 문장 `several crucial problems`. |
| 2.1:p.11 (보완) | Kennedy (2000), Chen (2000), Kirby (1998), Kennedy (2001, personal communications), Zhen (2004)의 연결을 빠뜨렸다. 슬롯망·연구 확장·복잡 지형 침수의 설명을 줄였다. | 해당 출처를 복원했다. 슬롯망의 격자 해상도, 적응 기준 높이의 목적, 비교적 곧은 해안선 한정, 고차 이류항 수정, 보존 차수의 일치, 복잡 지형 침수 사례의 의문을 보완했다. 마지막 문구의 `tend to induce a`와 목적어가 다음 쪽으로 이어짐을 보완했다. | 첫 문단의 Kennedy·Chen·Kirby 인용과 연구 판본 확장 설명. 둘째 문단의 Kennedy 개인 교신·HPF 개발·Zhen 비교 안내. 마지막 문단의 `several cases involving inundation over complex bathymetry`. 마지막 문장 `At the other extreme, slots which are too narrow tend to induce a`. |
| 2.1:p.12 (정정) | 쪽 첫 문장의 원인 주어를 앞쪽에서 가져왔다. 결정적 요인의 강도를 줄였다. 삼중대각 구조를 만드는 목적을 달성한 사실처럼 썼다. 인쇄되지 않은 절 번호·제목을 붙였다. | 쪽 첫 문구와 이 쪽에 보이는 결과를 기록했다. 결정적 요인이라는 표현을 복원했다. 삼중대각 구조를 목표로 한다는 표현을 복원했다. 절 번호·제목이 인쇄되지 않았음을 명시했다. | 첫 행 `great deal of numerical noise`. 첫 문단 `the determining factor`. 셋째 문단 `with the aim of constructing a tridiagonal structure`. 이 쪽에는 절 제목이 없다. |
| 2.1:p.12 (보완) | 혼합 기법 선행연구 출처·견고성 설명, 이동 기준 높이의 이유, 보통 일정한 시간 간격을 쓰던 기법과의 비교 등을 빠뜨렸다. 서로 다른 약어와 철자를 모순으로 명시하지 않았다. | Toro, Tonelli and Petti, Roeber, Shiac and Mingham, Erduran 인용을 복원했다. 이동 기준 높이·보존형·공간 이산화·TVD 도수 처리와 마지막 Kirby 문구를 보완했다. 같은 방정식과 해법의 표기 불일치를 쪽 행과 끝 절에 명시했다. 비선형 천수방정식의 기본 항이 부시네스크 방정식의 바탕이라는 괄호 설명을 복원했다. | 둘째 문단의 인용 목록과 견고성 설명. 셋째 문단 `more consistent`, `usually require uniform time-stepping`, `NLSWE`, `NSWE`, `Riemann solver`. 둘째 문단의 `Reiman solver`. 마지막 행의 Kirby 문구. 둘째 문단 괄호 `which form the basis of the Boussinesq model equations`. |
| 2.1:p.13 (보완) | 구면 코드의 서론 끝부분, 차수 설명과 식의 선행연구 인용 일부가 빠졌다. | 첫 문구의 et al. (2004, 2012), 같은 모델 체계의 구현, 정수압 거동에서 벗어나는 항의 차수 설명, Nwogu (1993)와 Kennedy et al. (2001), 움직일 수 있는 기준 높이를 보완했다. | p.13 첫 두 행, Theory 첫 문단, 식 (1) 앞 문장, 식 (4) 뒤 문장, 2.1 첫 문장. |
| 2.1:p.14 (정정) | 이 쪽에 인쇄되지 않은 절 번호·제목을 계속 표기로 넣었다. 첫 문구의 생략된 주어를 M으로 채웠다. | 이 쪽에는 절 번호·제목이 없음을 명시했다. 수평 체적 플럭스에 관한 첫 문구와 주어가 없는 상태를 기록했다. | p.14 첫 행은 `is the horizontal volume flux.`로 시작한다. 이 쪽에는 절 제목이 없다. |
| 2.1:p.14 (보완) | 본문과 식 (7)의 상선 차이를 나열했으나 불일치를 명시하지 않았다. 선행연구 인용과 기준 높이 선택의 설명 일부가 빠졌다. | 본문·식 (7)의 기호 불일치를 쪽 행과 끝 절에 명시했다. 식 (9)의 짝 없는 괄호를 쪽 행에 명시했다. Kennedy (2001)·Wei (1995)·Nwogu (1993)의 귀속과 기준 높이의 비선형 거동 최적화 설명을 보완했다. | p.14 첫 문장과 식 (7). 식 (9). 식 (10) 뒤 문단. 식 (13) 뒤 마지막 문단과 식 (14). |
| 2.1:p.15 (정정) | 첫 문단에 이 쪽에 인쇄되지 않은 2.1 절 번호를 붙였다. σ 좌표에 대한 `in essence`를 빠뜨렸다. | 첫 문단으로 지칭했다. 본질적으로 σ 좌표 접근에 해당한다는 한정을 복원했다. 통상 조건의 2차 기법은 괄호 설명으로 기록했다. | p.15 첫 문단: `This corresponds in essence to a σ coordinate approach`. 이 쪽에 인쇄된 절 번호는 2.2이다. Roeber 문장의 괄호: `second-order for normal conditions`. |
| 2.1:p.15 (보완) | 선도 차수 압력항의 수정 필요, 2차원 확장의 바닥 구성 한정과 수정 SGM의 의미, 고차 기법과 평형 재정식화의 출처를 빠뜨렸다. | 누락된 설명을 보완했다. Yamamoto and Daiguji (1993), Yamamoto et al. (1998), Rogers et al. (2003), Liang and Marche (2009)를 각각 해당 설명에 연결했다. | p.15 2.2 첫 문단의 첫 문장·2차원 확장 및 Kim 문장. 둘째 문단 첫 문장. 식 (15) 앞 문단. |
| 2.1:p.16 (정정) | 보존 변수 선택에 관한 Chen 방정식·작은 확장이라는 범위를 빠뜨렸다. 저장값 계산의 `usually`를 빠뜨렸다. | 보존 변수 선택의 적용 범위를 복원했다. 기존 코드가 보통 여러 시간 단계의 저장값으로 계산했다는 한정을 복원했다. | p.16 첫 문장: `For Chen’s (2006) equations or the minor extension considered here`. 식 (21) 뒤: `was usually calculated using values stored in several time levels`. |
| 2.1:p.16 (보완) | 질량 소스항과 기존 시간 미분 계산의 인용 일부가 빠졌다. 식 (21)·(22)의 ∇ 차이를 나열했으나 불일치를 명시하지 않았다. | Shiach and Mingham (2009), Roeber et al. (2010), Wei et al. (1995), Shi et al. (2001)를 해당 설명에 연결했다. 식 (21)의 중복 등호를 쪽 행에 명시했다. 식 (21)·(22)의 ∇ 불일치를 쪽 행과 끝 절에 명시했다. | p.16 첫 문단. 식 (21)과 그 뒤 문단. 식 (22)의 H 괄호 첫 항. |
| 2.1:p.17 (정정) | 첫 식에 이 쪽에 인쇄되지 않은 2.3 절 번호를 붙였다. | 이 쪽의 첫 식으로 지칭했다. | p.17 첫 줄 `where`와 식 (23). 인쇄된 절 제목은 3 및 3.1이다. |
| 2.1:p.17 (보완) | η의 시간 미분 계산에서 Roeber 인용이 빠졌다. 본문의 식 참조와 식 (23)의 불일치가 쪽 행에 드러나지 않았다. | `as in Roeber et al. (2010)`을 복원했다. 본문이 식 (23)의 η 시간 미분을 설명하지만 식 (23)에 그 기호가 없다는 불일치를 쪽 행과 끝 절에 명시했다. | p.17 식 (23) 바로 다음 문장: `In (23) η_t can be calculated explicitly using (5) as in Roeber et al. (2010).` |
| 2.1:p.18 (정정) | 첫 식에 이 쪽에 인쇄되지 않은 3.1 절 번호를 붙였다. | 이 쪽의 첫 식으로 지칭했다. | p.18 첫 식 (28). 이 쪽에 인쇄된 절 제목은 3.2이다. |
| 2.1:p.18 (보완) | 같은 4차 기법에 대한 Yamamoto 인용 연도를 각각 적었으나 불일치를 명시하지 않았다. | 1998과 1995의 인용 연도 불일치를 쪽 행과 끝 절에 명시했다. 식 (28)의 소거항 -U''₁이 인쇄된 표기임을 쪽 행에 명시했다. x 방향 재구성이 예시임을 명시했다. | p.18 식 (28). 3.2 첫 문단: `Yamamoto et al.’s (1998) fourth-order approach`. 마지막 문단: `the fourth-order scheme given by Yamamoto et al. (1995)`. |

3.0에서 수정이 필요하지 않은 행은 p.80과 p.86의 2행이다.
2.1에서 수정이 필요하지 않은 행은 p.1, p.2, p.4의 3행이다.
3.0의 식 (107)–(120)은 첨자·부호·지수·계수·괄호·식 번호를 이미지와 대조했다.
2.1의 식 (1)–(32)과 p.17의 번호 없는 성분 정의식 7개를 이미지와 대조했다.
원문에 인쇄된 수식의 불일치와 비정상 괄호·등호·첨자는 원문대로 보존했다.
같은 쪽의 모순과 표기 불일치는 해당 쪽 행과 끝 절에 함께 적었다.
두 기록의 frontmatter와 쪽 행 구성은 유지했다.
모델은 실행하지 않았다.

정정 25, 보완 19, 이상 없음 5
