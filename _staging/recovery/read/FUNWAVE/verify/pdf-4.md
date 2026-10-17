# FUNWAVE 2.1 매뉴얼 19–54쪽 전수 검증

검증일은 2026-10-17이다.
대상 두 기록의 모든 쪽 행을 대조했다.
판정 근거는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/fwpages/funwave_tvd_2.1_manual-NNN.png`의 300dpi 쪽 이미지이다.
`NNN`은 019–054의 쪽 번호이다.
작은 기호는 같은 이미지의 확대 영역으로 확인했다.
원문은 두 기록의 `file:`에 지정된 `models/FUNWAVE/raw/source_code/FUNWAVE-TVD/doc/funwave_tvd_2.1_manual.pdf`이다.

| 기록 | 대상 행 수 | 대조한 행 수 | 대조 구간 | 상태 |
|---|---|---|---|---|
| [p019-036.md](../FUNWAVE-TVD/doc/funwave_tvd_2.1_manual.pdf/p019-036.md) | 18 | 18 | p.19–36 | 완료 |
| [p037-054.md](../FUNWAVE-TVD/doc/funwave_tvd_2.1_manual.pdf/p037-054.md) | 18 | 18 | p.37–54 | 완료 |
| 합계 | 36 | 36 | p.19–54 | 완료 |

행 수는 각 기록의 `| p.N |` 쪽 행을 세었다.
정정·보완 수는 아래 목록의 항목 수이다.
같은 쪽의 같은 유형 변경은 한 항목으로 묶었다.
같은 쪽에 정정과 보완이 있으면 각각 센다.
이상 없음 수는 수정할 차이를 찾지 못해 그대로 둔 쪽 행 수이다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| p019-036.md:p.19 (정정) | 식 (37)·(38)·(40)의 s를 근호 밖에 표기했다. | 세 식을 모두 $\sqrt{\varphi_s}$로 고쳤다. | p.19 식 (37)·(38)의 $u_s\mp\sqrt{\varphi_s}$와 식 (40)의 좌변 $\sqrt{\varphi_s}$. |
| p019-036.md:p.19 (보완) | 제한 함수·처오름 검증·중앙차분·수면경사법의 출처를 일부 생략했다. | Yamamoto et al. (1998), Erduran et al. (2005), Tehranirad et al. (2011), Wei et al. (1995), Zhou et al. (2001)을 해당 설명에 넣었다. | p.19 첫 문단: “Yamamoto et al. (1998)”, “Erduran et al. (2005)”, “Tehranirad et al. (2011)”. 마지막 문단: “as in Wei et al. (1995)”, “The Surface Gradient Method (Zhou et al, 2001)”. |
| p019-036.md:p.20 (보완) | SSP 방법의 출처와 전환 기준의 출처·명칭 불일치를 생략했다. 마른 셀 파속의 원래 식 번호를 생략했다. | Gottlieb et al. (2001)과 Tonelli and Petti (2009)를 넣었다. 임계값 0.8의 제안자를 적었다. Froude 수와 파고 대 총수심 비의 명칭 불일치를 쪽 행과 끝 절에 적었다. 원래 파속 식 (37), (38)을 넣었다. | p.20 §3.3: “(Gottlieb et al., 2001)”. §3.4: “Tonelli and Petti (2009)”, “Froude number”, “the ratio of wave height to total water depth”, “0.8, as suggested by Tonelli and Petti”. 마지막 문단: “the Riemann solver (37) and (38)”. |
| p019-036.md:p.21 (보완) | 경계조건·조파기·바람응력·병렬 해법의 출처 연도와 연안방향 주기성 도입 목적을 생략했다. | Kirby et al. (1998), Chen et al. (2003, 2004), Wei and Kirby (1999), Naik et al. (1993)을 해당 설명에 넣었다. 경계 효과 제거 목적과 Chen et al. (2003)의 전략을 그대로 따른다는 한정을 넣었다. | p.21 §3.5: “following Kirby et al. (1998)”, “following Chen et al. (2003)”, “Wei and Kirby’s (1999)”, “in order to eliminate a boundary effect”, “exactly follows the strategy in Chen et al. (2003)”, “Chen et al. (2004)”. §3.6: “Naik et al. (1993)”. |
| p019-036.md:p.23 (정정) | 이 쪽에 없는 §3.7을 붙였다. | 절 번호와 제목이 인쇄되지 않았다고 고쳤다. | p.23 쪽 전체. 식 (46)으로 시작한다. |
| p019-036.md:p.23 (보완) | 좌표변환의 목적과 식 (46)·(51)의 첨자 불일치를 쪽 행에서 생략했다. | 같은 모델 틀에서 풀기 위한 동등한 Cartesian 방정식으로의 변환임을 넣었다. φ의 인쇄 위치 불일치를 쪽 행과 끝 절에 명시했다. | p.23: “an equivalent set of equations in Cartesian coordinates”. 식 (46)의 $(Hu)_\phi$와 식 (51)의 $(Hu)\phi$. |
| p019-036.md:p.24 (정정) | 이 쪽에 없는 §3.7을 붙였다. | 절 번호와 제목이 인쇄되지 않았다고 고쳤다. | p.24 쪽 전체. 식 (53)으로 시작한다. |
| p019-036.md:p.25 (정정) | 이 쪽에 없는 §3.7을 붙였다. | 절 번호와 제목이 인쇄되지 않았다고 고쳤다. | p.25 쪽 전체. 식 (70)으로 시작한다. |
| p019-036.md:p.26 (정정) | CONSTRUCT HO X에 공백을 썼다. 평균 η까지 Smagorinsky 혼합에 필요하다고 묶었다. | CONSTRUCT_HO_X의 밑줄을 복원했다. Smagorinsky 혼합에 필요한 평균 u v와 별도로 계산하는 평균 η를 구분했다. | p.26 마지막 항목명 “CONSTRUCT_HO_X”. CALCULATE_MEAN: “calculate mean u v required by the smagorinsky mixing. Mean η is also calculated.” |
| p019-036.md:p.26 (보완) | cpp 문장의 목적을 생략했다. | 소스코드를 분리하는 목적을 넣었다. | p.26 §4.1 첫 문장: “for separation of the source code”. |
| p019-036.md:p.28 (정정) | 이 쪽에 없는 §4.2를 붙였다. | 절 번호와 제목이 인쇄되지 않았다고 고쳤다. | p.28 쪽 전체. CONSTRUCT_HO_Y 항목으로 시작한다. |
| p019-036.md:p.29 (정정) | 이 쪽에 없는 §4.2를 붙였다. | 절 번호와 제목이 인쇄되지 않았다고 고쳤다. | p.29 쪽 전체. FLUX_AT_INTERFACE_HLLC 항목으로 시작한다. |
| p019-036.md:p.29 (보완) | HLLC와 HLL을 각각 적었지만 명칭 불일치를 명시하지 않았다. | 같은 서브루틴의 해법 명칭 불일치를 쪽 행과 끝 절에 적었다. | p.29 FLUX_AT_INTERFACE_HLLC 항목: “using HLLC scheme”. FLUXES 항목: “FLUX_AT_INTERFACE_HLLC for HLL scheme”. |
| p019-036.md:p.30 (정정) | 이 쪽에 없는 §4.2를 붙였다. | 절 번호와 제목이 인쇄되지 않았다고 고쳤다. | p.30 쪽 전체. INITIAL_RECTANGULAR 항목으로 시작한다. |
| p019-036.md:p.31 (정정) | 쪽 앞부분에 없는 §4.2를 붙였다. | 서브루틴 설명이 절 제목 없이 이어진다고 고쳤다. 실제로 인쇄된 §4.3은 유지했다. | p.31 앞부분의 서브루틴 목록. 하단 §4.3 Permanent variables. |
| p019-036.md:p.32 (정정) | 이 쪽에 없는 §4.3을 붙였다. | 절 번호와 제목이 인쇄되지 않았다고 고쳤다. | p.32 쪽 전체. DepthY()항목으로 시작한다. |
| p019-036.md:p.33 (정정) | 이 쪽에 없는 §4.3을 붙였다. | 절 번호와 제목이 인쇄되지 않았다고 고쳤다. | p.33 쪽 전체. EtaRyL() 항목으로 시작한다. |
| p019-036.md:p.34 (정정) | 정밀도 플래그를 -DDOUBLE PRECISION으로 적었다. 구분 문자를 공백이라고 명시했다. | -DDOUBLE_PRECISION으로 고쳤다. 쪽 행과 끝 절에서 밑줄임을 명시했다. | p.34 §4.4 첫 번째 플래그: -DDOUBLE_PRECISION. |
| p019-036.md:p.35 (정정) | 이 쪽에 없는 §4.5를 붙였다. | 입력 매개변수 설명이 절 번호 없이 이어진다고 고쳤다. | p.35 쪽 전체. HOT_START 항목으로 시작한다. |
| p019-036.md:p.36 (정정) | 이 쪽에 없는 §4.5를 붙였다. | 입력 매개변수 설명이 절 번호 없이 이어진다고 고쳤다. | p.36 쪽 전체. SPECIFICATION OF TIME으로 시작한다. |
| p037-054.md:p.37 (보완) | Time_ramp의 두 단위와 GAUSIAN/INI_GAU를 각각 적었지만 모순·불일치를 명시하지 않았다. | 주기의 배수와 s의 단위 모순을 쪽 행과 끝 절에 적었다. GAUSIAN/INI_GAU 이름 불일치를 명시했다. GAUSIAN 필요 입력의 개별 조건에 GAUSIAN이 없는 점을 넣었다. | p.37 WK_REG: “Time_ramp (factor of period)”. Time_ramp: “time ramp (s)”. WAVEMAKER = GAUSIAN 행과 AMP·Xc·Yc·WID 항목. |
| p037-054.md:p.38 (정정) | 이 쪽에 없는 SPECIFICATION OF WAVEMAKER 소제목을 붙였다. | 조파기 입력 설명의 계속이라고 고쳤다. 인쇄된 두 소제목은 유지했다. | p.38 첫 행 “Xc_WK: x coordinate (m) ...”. 하단의 PERIODIC BOUNDARY CONDITION·SPONGE LAYER 소제목. |
| p037-054.md:p.38 (보완) | 불규칙파 매개변수 묶음에서 조파기 출처를 생략했다. | Wei and Kirby (1999)를 불규칙파 조파기 설명에 넣었다. | p.38 FreqPeak부터 Sigma_Theta까지 각 항목의 “for Wei and Kirby (1999) irregular wavemaker”. |
| p037-054.md:p.40 (정정) | 이 쪽에 없는 SPECIFICATION OF NUMERICS 소제목을 붙였다. | 수치기법 입력 설명의 계속이라고 고쳤다. 인쇄된 OUTPUT VARIABLES 소제목은 유지했다. | p.40 첫 행 “HIGH_ORDER: spatial scheme option ...”. 중간 소제목 SPECIFICATION OF OUTPUT VARIABLES. |
| p037-054.md:p.43 (정정) | 이 쪽에 없는 4.7 Model nesting을 붙였다. | 모델 중첩 설명의 계속이라고 고쳤다. 실제 인쇄된 4.8·5·5.1 제목은 유지했다. | p.43 첫 행 ENDDO. 이후 4.8 Output, 5 Examples, 5.1 Breaking waves on a beach. |
| p037-054.md:p.43 (보완) | 기존 검토에도 격자 민감도 우려가 있다는 문장과 두 출처를 생략했다. 검증 범위·벤치마크 협력 기관을 생략했다. | Tonelli and Petti (2009), Shiach and Mingham (2009)과 격자 민감도 우려를 넣었다. 광범위한 실험 검증이라는 원문 주장과 National Tsunami Hazard Mitigation Program을 넣었다. | p.43 §5 첫 문단. §5.1 마지막 문단: “Although ... examined by previous researchers ... there is a concern about its sensitivity to grid spacing.” |
| p037-054.md:p.44 (정정) | 이 쪽에 없는 5.1 절 번호·제목을 붙였다. | 해빈 쇄파의 결과 설명이라고 고쳤다. 절 번호와 제목이 인쇄되지 않았다고 적었다. | p.44 첫 문장 “Results from the dx=0.25 m and 0.0125 m grids ...”. 절 제목은 없다. |
| p037-054.md:p.44 (보완) | Kennedy et al. (2000)의 두 비교를 생략했다. 붕파형의 격자별 파고 차이와 같은 문단의 0.25/0.025 표기 불일치를 생략했다. | Figure 2의 예측 경향 및 약 10% 과소예측 비교를 넣었다. 붕파형의 격자별 첨두 차이를 넣었다. 0.25/0.025 불일치를 쪽 행과 끝 절에 적었다. | p.44 첫 문단의 “Kennedy et al. (2000, Figure 2)”와 “similar to Kennedy et al. (2000)”. 세 번째 문단 첫 문장. 첫 문단의 dx 두 표기. |
| p037-054.md:p.45 (정정) | 이 쪽에 사례명이 없는 입력 블록을 권파형 쇄파 입력으로 단정했다. | 앞쪽 입력 예시의 계속이라고 고쳤다. | p.45 입력 블록은 “Delta_WK = 0.3”으로 시작한다. 권파형이라는 표기는 없다. |
| p037-054.md:p.46 (정정) | 이 쪽에 없는 5.1 절 번호를 붙였다. | 그림 3만 있다고 고쳤다. 절 번호와 제목이 인쇄되지 않았다고 적었다. | p.46 그림 3과 “Figure 3: Comparisons of wave height ... Case: plunging breaker.” 캡션. |
| p037-054.md:p.47 (정정) | 이 쪽에 없는 5.1 절 번호를 붙였다. | 그림 4만 있다고 고쳤다. 절 번호와 제목이 인쇄되지 않았다고 적었다. | p.47 그림 4와 “Figure 4: Snapshots of surface elevation ...” 캡션. |
| p037-054.md:p.48 (정정) | 이 쪽에 없는 5.1 절 번호를 붙였다. | 그림 5만 있다고 고쳤다. 절 번호와 제목이 인쇄되지 않았다고 적었다. | p.48 그림 5와 “Figure 5: Model/data comparisons ... Case: spilling breaker.” 캡션. |
| p037-054.md:p.49 (정정) | 이 쪽에 없는 5.2 절 번호·제목을 붙였다. 3차 모멘트로 정규화한다고 적었다. | 절 번호·제목이 없다고 고쳤다. 3차 모멘트 계산과 관측·모델 시계열 각각의 정규화된 왜도·비대칭도 계산을 구분했다. | p.49 “we performed third moment computations ... Normalized wave skewness and asymmetry were calculated for both measured and model time series ...”. 두 수식의 분모는 $<\eta^2>^{3/2}$이다. |
| p037-054.md:p.50 (정정) | 이 쪽에 없는 5.2 절 번호를 붙였다. | 그림 6·7이 있다고 고쳤다. 절 번호와 제목이 인쇄되지 않았다고 적었다. | p.50 Figure 6·7 캡션. 절 번호는 없다. |
| p037-054.md:p.50 (보완) | 그림 7의 세로축 눈금을 생략했다. | 표시 눈금 0, 20, 40, 60, 80, 100을 넣었다. | p.50 그림 7의 Surface elevation (cm) 세로축 눈금. |
| p037-054.md:p.51 (정정) | 이 쪽에 없는 5.2 절 번호를 붙였다. | 그림 8만 있다고 고쳤다. 절 번호와 제목이 인쇄되지 않았다고 적었다. | p.51 그림 8과 “Figure 8: Comparison of skewness ...” 캡션. |
| p037-054.md:p.52 (정정) | 이 쪽에 없는 5.2 절 번호를 붙였다. 앞쪽 파일명·수심 항목 구분을 가져왔다. | 입력 예시가 이어진다고 고쳤다. SLP와 Xslp를 쪽 첫 입력 항목으로 적었다. | p.52 첫 두 행 “SLP = 0.05”, “Xslp = 10.0”. 이 쪽에는 5.2·input.txt·DEPTH 표제가 없다. |
| p037-054.md:p.53 (정정) | 이 쪽에 없는 5.2 절 번호와 PHYSICS 표제를 붙였다. | 앞쪽 입력·출력 설명의 끝이라고 고쳤다. 첫 입력 항목들을 절 번호·표제 없이 적었다. | p.53 첫 행 “Gamma2 = 1.0”. 이 쪽의 절 제목은 5.3이다. |
| p037-054.md:p.53 (보완) | 이전 FUNWAVE의 관측 파고 재현과 지형 생성 프로그램의 출처를 생략했다. | Kirby et al. (1998)의 이전 버전 재현 결과를 넣었다. 같은 프로그램으로 지형을 생성했다는 설명을 넣었다. | p.53 §5.3 첫 문단 “Kirby et al. (1998) showed ... reproduces measured wave heights ...”. 두 번째 문단 “generated using the same program in Kirby et al., (1998)”. |
| p037-054.md:p.54 (정정) | 이 쪽에 없는 5.3 절 번호·제목을 붙였다. 측선을 점선으로 적었다. | 절 번호·제목이 없다고 고쳤다. 그림 9의 측선을 파선으로 고쳤다. | p.54 첫 문장 “Thirty waves are simulated ...”. 그림 9의 (1)–(8) 측선은 긴 선분으로 끊어진 파선이다. |
| p037-054.md:p.54 (보완) | 세로축의 중복 양수 5를 각각 기록했지만 눈금 불일치를 명시하지 않았다. | 양수 5가 0 위와 아래에 반복되는 불일치를 쪽 행과 끝 절에 명시했다. | p.54 그림 9의 y(m) 축 눈금: 위에서 10, 5, 0, 5, −10. |

이상 없음: `p019-036.md`의 p.22, p.27.
이상 없음: `p037-054.md`의 p.39, p.41, p.42.

원문의 오표기와 내부 불일치는 기록에 명시했다.
원문은 수정하지 않았다.
두 기록의 frontmatter와 쪽 행 구성을 유지했다.
모델은 실행하지 않았다.
Git 작업은 하지 않았다.

정정 28, 보완 13, 이상 없음 5
