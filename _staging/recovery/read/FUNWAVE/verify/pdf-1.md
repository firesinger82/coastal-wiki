# FUNWAVE 3.0 PDF 1–36쪽 전수 검증

검증일은 2026-10-17이다. 대상 원문은 `models/FUNWAVE/raw/source_code/FUNWAVE-TVD/doc/funwave_tvd_3.0.pdf`이다.
판정 근거는 지정된 `fwpages/funwave_tvd_3.0-NNN.png`의 300dpi 인쇄 이미지이다.
대상 기록의 경로는 `_staging/recovery/read/FUNWAVE/FUNWAVE-TVD/doc/funwave_tvd_3.0.pdf/`이다.
아래의 원문 행은 PDF 쪽 번호와 인쇄된 문단·목록 항목·식 번호로 식별한다.
정정과 보완은 각각 해당 변경이 있는 쪽 행 수로 센다. 두 변경이 있는 쪽은 두 수에 각각 포함한다. 이상 없음은 변경하지 않은 쪽 행 수이다.

| 기록 | 대조한 행 수 | 대조한 쪽 | 상태 |
|---|---:|---|---|
| p001-018.md | 18/18 | p.1, p.2, p.3, p.4, p.5, p.6, p.7, p.8, p.9, p.10, p.11, p.12, p.13, p.14, p.15, p.16, p.17, p.18 | 완료 |
| p019-036.md | 18/18 | p.19, p.20, p.21, p.22, p.23, p.24, p.25, p.26, p.27, p.28, p.29, p.30, p.31, p.32, p.33, p.34, p.35, p.36 | 완료 |

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| p001-018.md:p.3 (보완) | 이전 보고서의 출처가 빠졌다. 문서가 제공하는 내용 중 수치 기법·사용자 매뉴얼·예제의 열거가 빠졌다. | 이전 보고서를 Shi et al. (2011)로 명시했다. 수치 기법·사용자 매뉴얼·예제를 추가했다. | p.3 Abstract의 ‘detailed numerical schemes, users’ manual and examples’ 행. 다음 문단의 ‘previous report (Shi et al., 2011)’ 행. |
| p001-018.md:p.5 (정정) | 이 쪽을 Contents의 계속으로 식별했으나 제목의 실제 인쇄 여부를 구분하지 않았다. | 목차 항목은 이어지지만 Contents 제목은 이 쪽에 없음을 명시했다. | p.5 맨 위 “5 Examples”부터 Appendix A까지의 목차 항목. Contents 제목은 없다. |
| p001-018.md:p.7 (정정) | 이 쪽을 List of Figures의 계속으로 식별했으나 제목의 실제 인쇄 여부를 구분하지 않았다. | 그림 목록 항목은 이어지지만 List of Figures 제목은 이 쪽에 없음을 명시했다. | p.7 그림 목록 항목 24와 25. List of Figures 제목은 없다. |
| p001-018.md:p.9 (보완) | 구면 모드 조파기의 목적만 적었다. 해당 항목의 벤치마크 출처 표기가 빠졌다. | Version 1.1 변경 목록 4의 출처 Shi et al. (2012b)를 추가했다. | p.9 Version 1.1 변경 목록 4의 ‘benchmark tests (Shi et al., 2012b)’ 행. |
| p001-018.md:p.10 (정정) | 쪽 첫 두 항목을 앞쪽 Version 2.0 제목에 귀속했다. | 제목 없이 이어지는 목록 항목 3·4와 이 쪽의 Version 2.1·2.2 제목을 구분했다. | p.10 상단 목록 항목 3·4와 그 아래 두 Differences 제목. |
| p001-018.md:p.10 (보완) | Larsen–Dancy형 스펀지층의 인용 출처가 빠졌다. slope layer와 sponge layer를 병기했으나 명칭 불일치를 명시하지 않았다. | Larsen and Dancy (1983)와 Chen et al. (1999)를 추가했다. 같은 문장 안의 명칭 불일치를 쪽 행과 끝 절에 명시했다. | p.10 Version 2.2 변경 설명 첫 문장의 ‘Larsen-Dancy-type (Larsen and Dancy, 1983, Chen et al., 1999)’ 행. 같은 문단의 “two additional slope layer methods”와 두 “sponge layer” 명칭. |
| p001-018.md:p.12 (보완) | 분산·비선형성 개선과 쇄파·난류 및 기존 FUNWAVE 기법의 인용 출처 대부분이 빠졌다. 수면 변동의 크기와 ‘usually’ 한정이 빠졌다. | 각 주장에 Madsen·Nwogu·Gobbi·Agnon·Lynett와 Liu·Wei·Chen·Feddersen·Geiman·Kim·Kirby의 인쇄된 출처를 연결했다. 쇄파대·포말대의 수면 변동 범위와 통상적인 와점성 접근이라는 한정을 추가했다. 기존 수치 구현의 범주와 FUNWAVE의 공개 코드 설명을 추가했다. | p.12 첫 문단의 ‘Madsen et al (1991) and Nwogu (1993)’부터 ‘vertical flow structure’까지. 둘째 문단의 ‘finite difference, finite volume, or finite element’부터 ‘Wei et al (1995)’까지. |
| p001-018.md:p.13 (정정) | 쪽 첫머리를 1 Introduction으로 식별했다. | 앞쪽에서 이어지는 본문과 이 쪽의 인쇄 제목을 구분했다. 이 쪽에는 절 번호·제목이 없음을 명시했다. | p.13 첫 줄은 Kennedy·Chen 인용 문장이다. 쪽 전체에 절 제목이 없다. |
| p001-018.md:p.13 (보완) | 초기 쇄파대 확장과 다른 와점성 접근의 출처가 빠졌다. 슬롯의 깊이 조건과 연구 판본의 적용 범위가 빠졌다. Kennedy의 연도·부분 완화 한정이 빠졌다. | Kennedy et al. (2000), Chen et al. (2000), Nwogu and Demirbilek (2001), Kirby et al. (1998)를 추가했다. 예상 최저 수면보다 깊은 슬롯 조건을 추가했다. 이동 준위의 목적과 비교적 곧은 해안선 적용을 추가했다. Kennedy (2001, personal communications)의 HPF 개발 맥락과 부분 완화를 추가했다. 복잡한 지형의 슬롯 성능에 대한 의문을 추가했다. | p.13 첫 문단의 Kennedy·Chen·Nwogu 인용 행과 ‘lower than the minimum expected excursion’ 행. 둘째 문단의 ‘Kennedy (2001, personal communications)’부터 ‘alleviated to an extent’까지. 마지막 문단의 ‘called in to question’ 행. |
| p001-018.md:p.14 (정정) | 쪽 첫머리를 1 Introduction으로 식별했다. | 이 쪽에는 절 번호·제목이 인쇄되어 있지 않음을 명시했다. | p.14 첫 줄은 앞쪽 문장의 “great deal of numerical noise...”부터 이어진다. 쪽 전체에 절 제목이 없다. |
| p001-018.md:p.14 (보완) | TVD 혼합 기법과 쇄파 처리의 인용 출처가 빠졌다. 이동 기준 준위의 이유와 이전 시간 기법의 ‘usually’ 한정이 빠졌다. NLSWE·NSWE를 병기했으나 약어 불일치를 명시하지 않았다. | Toro (2009)와 혼합 기법의 사례 출처를 추가했다. Tonelli and Petti (2009)의 이동 도수 접근을 추가했다. 리만 해법의 해안선 처리와 이동 기준 준위의 이유를 추가했다. 이전 고차 기법이 보통 균일 시간 간격을 요구한다는 한정을 추가했다. 같은 방정식의 약어 불일치를 쪽 행과 끝 절에 명시했다. | p.14 둘째 문단의 ‘(Toro, 2009)’ 및 ‘Tonelli and Petti, 2009, 2010, Roeber et al., 2010, Shiach and Mingham, 2009, Erduran et al., 2005’ 행. 셋째 문단의 이동 기준 고도 설명과 ‘usually require uniform time-stepping’ 및 ‘follows the approach of Tonelli and Petti (2009)’ 행. 같은 문단의 NLSWE·NSWE 표기. |
| p001-018.md:p.15 (정정) | 쪽 첫머리 문장에 앞쪽의 1 Introduction이라는 절 번호·제목을 붙였다. | 제목 없이 이어지는 첫머리 문장과 이 쪽의 2 Theory·2.1 Governing equations 제목을 구분했다. | p.15 첫머리 두 행과 그 아래 “2 Theory”, 하단 “2.1 Governing equations”. |
| p001-018.md:p.15 (보완) | 유속 분해의 선행 출처와 이동 기준 고도의 출처가 빠졌다. 차수 표기의 사용 목적과 기준 고도의 이동 가능성 표현이 빠졌다. | Nwogu (1993)와 Kennedy et al. (2001)을 추가했다. 비정수압 효과를 식별하기 위한 차수 언급을 추가했다. §2.1의 ‘possible moving reference elevation’을 추가했다. | p.15 §2 첫 문단의 ‘deviations from hydrostatic behavior’와 ‘earlier works starting with Nwogu (1993)’ 행. 식 (4) 다음의 ‘as in Kennedy et al (2001)’ 행. §2.1 첫 행. |
| p001-018.md:p.16 (정정) | 쪽 첫머리를 2.1 Governing equations로 식별했다. | 이 쪽에는 절 번호·제목이 인쇄되어 있지 않음을 명시했다. | p.16 첫 줄은 “is the horizontal volume flux.”로 이어진다. 쪽 전체에 절 제목이 없다. |
| p001-018.md:p.16 (보완) | 식 (8)의 방정식 이름과 식 (9)·(10), 기준 고도 최적화 및 datum invariant 형태의 직접 출처가 빠졌다. | 식 (8)을 수심 평균 수평 운동량 방정식으로 명시했다. Kennedy et al. (2001), Wei et al. (1995), Nwogu (1993)를 해당 설명에 연결했다. | p.16 식 (8) 앞의 ‘depth-averaged horizontal momentum equation’ 행. 식 (10) 다음 문단의 Kennedy·Wei 인용 행. 식 (13) 다음 문단의 ‘Following Nwogu (1993)’ 및 식 (14) 앞의 Kennedy 귀속 행. |
| p001-018.md:p.17 (정정) | 첫 문단을 2.1의 마지막 설명으로 식별했다. | 첫 문단에는 2.1이 인쇄되지 않았음을 명시했다. 그 아래 실제 제목 2.2와 구분했다. | p.17 첫 문단의 “with ζ = −0.53...”과 그 아래 “2.2 Treatment of the surface gradient term”. |
| p001-018.md:p.17 (보완) | 기준 고도, 4차 MUSCL-TVD 및 평형 상태 편차 방식의 인용 출처가 빠졌다. 수정 SGM의 일반 2차원 적용에 관한 서술이 빠졌다. | Nwogu (1993), Yamamoto and Daiguji (1993), Yamamoto et al. (1998), Rogers et al. (2003), Liang and Marche (2009)를 추가했다. Kim et al.의 설명이 일반 2차원 적용 유효성을 시사한다는 원문의 표현을 추가했다. | p.17 맨 위 ‘as in Nwogu (1993)’ 행. §2.2의 ‘implying that their revised SGM is valid for general 2D applications’ 행. 4차 MUSCL-TVD의 괄호 인용 및 식 (15) 앞의 Rogers·Liang 인용 행. |
| p001-018.md:p.18 (보완) | 보존변수 선택 및 기존 코드 설명의 출처·한정이 빠졌다. 식 (22)의 기호 차이를 옮겼지만 같은 쪽 식 (17), (21)과의 불일치를 쪽 행에 명시하지 않았다. | Chen (2006), Shiach and Mingham (2009), Roeber et al. (2010), Wei et al. (1995), Shi et al. (2001)을 해당 설명에 연결했다. ‘보통’이라는 한정과 식 (6)·(8)·(16)·(17)의 유도 관계를 추가했다. 식 (22)의 대응 항에만 ∇가 없는 불일치를 쪽 행과 끝 절에 명시했다. | p.18 §2.3 첫 문단 및 식 (16) 앞뒤 문장. 식 (21) 다음의 ‘usually calculated’와 Wei·Shi 인용 행. 식 (17), (21), (22)의 H 안 첫 이류 항. |
| p019-036.md:p.19 (보완) | ‘as in Roeber et al. (2010)’이 빠졌다. η_t를 식 (23)에 귀속한 원문과 실제 식의 불일치를 적지 않았다. 유속 복원의 선행 조건과 구성 식 번호가 빠졌다. | Roeber et al. (2010)을 추가했다. 본문이 참조한 식 (23)에 η_t가 없는 불일치를 쪽 행과 끝 절에 명시했다. V를 얻은 뒤 식 (23)의 삼중대각 연립방정식으로 유속을 구한다는 조건을 추가했다. | p.19 식 (23). 그 아래 ‘In (23) η_t can be calculated explicitly using (5) as in Roeber et al. (2010)’ 행과 ‘As V is obtained’부터 ‘formed by (23)’까지. |
| p019-036.md:p.20 (정정) | 쪽 첫머리에 앞쪽 절 번호 2.4를 붙였다. | 문맥상 이어지는 본문과 실제 인쇄 제목을 구분했다. 이 쪽에는 절 제목이 없음을 명시했다. | p.20 첫 줄 “are”와 식 (28)–(44). 이 쪽에는 절 제목이 없다. |
| p019-036.md:p.21 (정정) | 쪽 첫머리에 앞쪽 절 번호 2.4를 붙였다. | 문맥상 이어지는 본문과 실제 인쇄 제목을 구분했다. 이 쪽에는 절 제목이 없음을 명시했다. | p.21 첫 줄 “where S_p is...”와 식 (45)–(56). 이 쪽에는 절 제목이 없다. |
| p019-036.md:p.24 (정정) | 쪽 첫머리에 앞쪽 절 번호 3.2를 붙였다. | 문맥상 이어지는 본문과 실제 인쇄 제목을 구분했다. 이 쪽에는 절 제목이 없음을 명시했다. | p.24 첫 문단 “For the low-order scheme...”과 식 (68)–(77). 이 쪽에는 절 제목이 없다. |
| p019-036.md:p.24 (보완) | 파속 기호와 추정식의 역할 설명이 빠졌다. 고차 미분 이산화와 Surface Gradient Method의 직접 출처가 빠졌다. | s_L·s_R를 리만 해법의 파속으로 명시했다. u_s·φ_s의 추정 관계를 명시했다. Wei et al. (1995)와 Zhou et al. (2001)을 각각 연결했다. | p.24 식 (74) 앞의 ‘The wave speeds of the Riemann solver’ 행. 식 (76) 앞의 ‘estimated as’ 행. 마지막 문단의 Wei·Zhou 인용 행. |
| p019-036.md:p.25 (정정) | 끝 절은 §3.4 첫 문장이 PDF에서 ‘The are’로 시작한다고 적었다. | 인쇄 이미지의 첫 문장은 ‘There are two breaking algorithms implemented in the model.’이다. 잘못 기록한 PDF·원고 철자 차이를 제거했다. | p.25 §3.4 첫 행의 ‘There are two breaking algorithms implemented in the model.’. |
| p019-036.md:p.25 (보완) | 중간 단계 유속 계산의 Ψ 획득 조건이 빠졌다. Froude 수와 파고비를 각각 기록했지만 같은 문단의 기준 설명 불일치를 명시하지 않았다. | Ψ를 얻은 뒤 유속을 구한다는 조건을 추가했다. 같은 전환 기준의 설명이 Froude 수와 파고 대 총수심 비로 불일치함을 쪽 행과 끝 절에 명시했다. | p.25 식 (78) 아래 ‘As Ψ is obtained at each intermediate step’ 행. §3.4 첫 문단의 ‘Froude number exceeds’와 ‘ratio of wave height to total water depth’ 행. |
| p019-036.md:p.26 (정정) | 쪽 첫머리에 앞쪽 절 번호 3.4를 붙였다. | 제목 없이 이어지는 쇄파 설명과 실제 인쇄된 3.5·3.6·3.6.1 제목을 구분했다. | p.26 첫 줄 “where δ_b = 1.2.”. 다음 인쇄 제목은 “3.5 Wetting-drying schemes for shallow water”이다. |
| p019-036.md:p.26 (보완) | 이전 판본과 같은 기본값이라는 설명과 다음 절 예제 참조가 빠졌다. 초기 임계값의 0.65×2와 Cbrk1=0.65를 병기했지만 수치 표기 차이와 환산 설명의 부재를 명시하지 않았다. | 이전 판본과의 관계 및 예제 참조를 추가했다. 계수 표기가 일치하지 않으며 해당 쪽에 추가 계수 2의 환산 설명이 없음을 쪽 행과 끝 절에 명시했다. | p.26 식 (83) 다음 문단의 ‘0.65 × 2√gh’ 행과 ‘i.e., Cbrk1 = 0.65 and Cbrk2=0.15’ 행. |
| p019-036.md:p.27 (정정) | 쪽 첫머리에 앞쪽 절 번호 3.6.1을 붙였다. | 제목 없이 이어지는 스펀지층 설명과 하단의 실제 제목 3.6.2를 구분했다. | p.27 상단 식 (86)과 하단 “3.6.2 Periodic boundary condition”. |
| p019-036.md:p.27 (보완) | γ_x와 γ_s를 각각 옮겼지만 식과 본문의 첨자 불일치를 명시하지 않았다. 감쇠계수의 사례 민감성에 대한 직접 귀속이 빠졌다. | 같은 쪽의 식과 본문에서 첨자가 불일치하며 γ_x의 별도 정의가 없음을 쪽 행과 끝 절에 명시했다. 감쇠계수의 사례 민감성을 Chen et al.의 지적으로 연결했다. | p.27 식 (87). 그 아래 ‘α_s and γ_s’ 행과 ‘Chen et al. also pointed out’ 행. |
| p019-036.md:p.28 (보완) | Larsen and Dancy (1983)의 선행 기법 출처가 빠졌다. 단일 격자 블록의 물 출입 설명과 발견·개선의 주체가 빠졌다. | Wei and Kirby가 따른 Larsen and Dancy (1983)를 추가했다. 엇갈림 격자의 단일 블록 설명을 추가했다. 잡음 발견과 분포 질량원 사용을 Wei and Kirby에 귀속했다. | p.28 둘째 문단의 ‘followed the approach of Larsen and Dancy (1983)’부터 ‘They then used a partially distributed mass source’까지. |
| p019-036.md:p.29 (정정) | 쪽 첫머리에 앞쪽 절 번호 3.7.1를 붙였다. | 문맥상 이어지는 설명과 이 쪽의 실제 인쇄 제목을 구분했다. | p.29 첫 줄 “coordinates x_1 and x_2...”와 Figure 1. 이 쪽에는 절 제목이 없다. |
| p019-036.md:p.30 (정정) | 쪽 첫머리에 앞쪽 절 번호 3.7.1를 붙였다. | 문맥상 이어지는 설명과 이 쪽의 실제 인쇄 제목을 구분했다. | p.30 첫 줄 “exactly follows the strategy in Chen et al. (2003)...”. 첫 인쇄 절 제목은 3.7.2이다. |
| p019-036.md:p.31 (정정) | 쪽 첫머리에 앞쪽 절 번호 3.7.4를 붙였다. | 문맥상 이어지는 설명과 이 쪽의 실제 인쇄 제목을 구분했다. | p.31 첫 줄 “G(θ) is the wrapped normal...”. 인쇄 절 제목은 하단 3.8과 3.8.1이다. |
| p019-036.md:p.32 (보완) | Fortran 90과 cpp 문장을 사용했다고만 기록했다. | cpp 문장의 목적이 소스코드 분리라는 설명을 보완했다. | p.32 §4.1 첫 문단 첫 문장: “for separation of the source code”. |
| p019-036.md:p.33 (정정) | 이 쪽의 그림에 4.1이라는 절 번호를 붙였다. | 이 쪽에는 Figure 2만 인쇄되어 있음을 구분했다. | p.33 흐름도 전체와 Figure 2 캡션. 절 번호 4.1은 인쇄되어 있지 않다. |
| p019-036.md:p.33 (보완) | ITERATION 분기와 옵션 미사용 캡션을 각각 기록했으나 불일치를 명시하지 않았다. | 그림의 분기 표기와 캡션의 이용 여부 설명이 일치하지 않음을 쪽 행과 끝 절에 명시했다. | p.33 흐름도 오른쪽 “RK & ITERATION” 분기와 하단 Figure 2 캡션. |
| p019-036.md:p.34 (정정) | 쪽 첫머리에 4.2라는 절 번호를 붙였다. | 이 쪽에 인쇄된 절 제목 4.3 Input과 앞쪽에서 이어지는 무제 본문을 구분했다. | p.34 상단은 “to extract files...”로 이어진다. 하단에 “4.3 Input”이 인쇄되어 있다. |
| p019-036.md:p.35 (정정) | 쪽 첫머리 제목으로 4.3과 SPECIFICATION OF HOT START를 적었다. | HOT_START 매개변수 설명부터 시작한다는 점을 명시했다. 앞쪽의 절 번호와 소제목을 이 쪽의 인쇄 제목에서 제외했다. | p.35 첫 줄 “HOT_START: logical parameter...”. 첫 인쇄 소제목은 “SPECIFICATION OF MULTI-PROCESSORS”이다. |
| p019-036.md:p.36 (정정) | 쪽 첫머리 제목으로 4.3과 SPECIFICATION OF DIMENSION을 적었다. | Nglob 설명부터 시작한다는 점을 명시했다. 앞쪽의 절 번호와 소제목을 이 쪽의 인쇄 제목에서 제외했다. | p.36 첫 줄 “Nglob: global dimension in y direction.”. 첫 인쇄 소제목은 “SPECIFICATION OF TIME”이다. |

이상 없음: p001-018.md:p.1, p001-018.md:p.2, p001-018.md:p.4, p001-018.md:p.6, p001-018.md:p.8, p001-018.md:p.11, p019-036.md:p.22, p019-036.md:p.23.

정정 21, 보완 18, 이상 없음 8
