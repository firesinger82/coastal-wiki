# SWAN PDF 대조 기록 6

검증일은 2026-10-13이다.
원문은 `models/SWAN/raw/manuals/pdfs/swantech.pdf`이다.
쪽 번호는 PDF 쪽 번호이다.
원문 근거는 지정된 300dpi 이미지 `swantech-NNN.png`에서 직접 읽었다.
이미지 디렉터리는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/swpages/`이다.
정정과 보완은 아래 목록의 유형별 항목 수로 센다.
같은 쪽의 같은 유형 수정은 한 항목으로 묶는다.
정정과 보완이 함께 있는 쪽은 두 유형에 각각 포함한다.
이상 없음은 수정하지 않은 쪽 행 수로 센다.

| 기록 | 대상 쪽 행 수 | 대조한 쪽 행 수 |
|---|---:|---:|
| `manuals/pdfs/swantech.pdf/p109-126.md` | 18 | 18 |
| `manuals/pdfs/swantech.pdf/p127-144.md` | 18 | 18 |

기록 경로는 `_staging/recovery/read/SWAN/`을 기준으로 적었다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| `manuals/pdfs/swantech.pdf/p109-126.md:p.110` · 정정 | §3.8.5 계속이라고 표기했다. 성긴 해상도의 식 (3.43)을 문장의 주어로 복원했다. | 인쇄되지 않은 §3.8.5를 삭제했다. 첫머리에 보이는 고해상도 식의 언급만 기록했다. | PDF p.110(인쇄 102), 첫 줄 “(3.43) or Eq. (3.42) with high resolution.”. 이 쪽의 절 표제는 “3.9 Implementation of QC approximation”이다. |
| `manuals/pdfs/swantech.pdf/p109-126.md:p.111` · 정정 | §3.9와 절 제목을 이 쪽의 계속 표제로 적었다. | 이 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다. | PDF p.111(인쇄 103), 머리말 “Numerical approaches”. 본문은 “one should stick to the k⃗-space”로 시작한다. §3.9 표제는 없다. |
| `manuals/pdfs/swantech.pdf/p109-126.md:p.112` · 정정 | §3.9 계속이라고 표기했다. 첫머리의 접근을 앞 쪽 내용으로 명명했다. 비정상 계산에 Stelling and Leendertse 방식을 반드시 선택한다고 적었다. | 인쇄되지 않은 절 표제를 삭제했다. 첫머리에 보이는 식 (2.16)의 항 참조를 기록했다. 구조 격자의 비정상 계산에서 선택할 수 있는 대안으로 고쳤다. | PDF p.112(인쇄 104), 첫 줄 “(viz. the third and fourth terms of Eq. (2.16))”. 공간 이산화 문단 “In case of structured grids the SORDUP scheme (or the Stelling and Leendertse scheme for non-stationary runs) should then be selected”. §3.9 표제는 없다. |
| `manuals/pdfs/swantech.pdf/p109-126.md:p.112` · 보완 | 협대역 파군 사례만 기록했다. | 간섭 패턴이 주로 매질 변화의 특성과 Wigner 분포의 스펙트럼 폭에 의존한다는 설명을 추가했다. | PDF p.112(인쇄 104), 마지막 문단 “depend mainly on the nature of the medium variations and the spectral width of the Wigner distribution”. |
| `manuals/pdfs/swantech.pdf/p109-126.md:p.113` · 정정 | §3.9 계속이라고 표기했다. 첫머리 문장의 주어와 표준편차의 대상을 앞 쪽 내용으로 복원했다. | 인쇄되지 않은 절 표제를 삭제했다. 첫머리의 구절만 기록했다. | PDF p.113(인쇄 105), 첫 구절 “to this standard deviation.”. §3.9 표제는 없다. |
| `manuals/pdfs/swantech.pdf/p109-126.md:p.114` · 정정 | 창 함수 설명을 §3.9로 표기했다. | 이 쪽에 인쇄되지 않은 §3.9를 삭제했다. | PDF p.114(인쇄 106), 첫 줄 “A standard Tukey window is utilized”. 이 쪽의 절 표제는 “3.10 Governing equations in curvilinear co-ordinates”이다. |
| `manuals/pdfs/swantech.pdf/p109-126.md:p.115` · 정정 | §3.10과 절 제목을 계속 표제로 적었다. | 이 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다. | PDF p.115(인쇄 107), 첫 줄 “It follows that the partial derivatives can be approximated by”. §3.10 표제는 없다. |
| `manuals/pdfs/swantech.pdf/p109-126.md:p.117` · 정정 | 이웃점 1의 기여를 K_t²로 줄인다고 적었다. | K_t²가 기여에 곱하는 계수임을 명시했다. | PDF p.117(인쇄 109), 그림 3.8 아래 “contribution of a neighbouring grid point ... is reduced by K_t²”. |
| `manuals/pdfs/swantech.pdf/p109-126.md:p.118` · 정정 | §3.12와 절 제목을 계속 표제로 적었다. | 이 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다. | PDF p.118(인쇄 110), 첫 줄 “A consequence of the above procedure”. §3.12 표제는 없다. |
| `manuals/pdfs/swantech.pdf/p109-126.md:p.118` · 보완 | 한국어 설명에는 수치 부정확성의 발생만 적었다. | 이런 부정확성이 수치 모델에서 드물지 않다는 한정 설명을 추가했다. | PDF p.118(인쇄 110), 식 (3.70) 아래 “This introduces numerical inaccuracies, but that is not uncommon in numerical models.” |
| `manuals/pdfs/swantech.pdf/p109-126.md:p.119` · 정정 | 반사 설명을 §3.12로 표기했다. 첫 항목의 대체 대상을 점 1의 기여로 복원했다. | 인쇄되지 않은 §3.12를 삭제했다. 첫 항목에 보이는 부분 대체 설명만 기록했다. | PDF p.119(인쇄 111), 첫 항목 “partially replaced by the reflection of an incoming component in point 0.”. 이 쪽의 절 표제는 3.13과 3.14이다. |
| `manuals/pdfs/swantech.pdf/p109-126.md:p.120` · 정정 | §3.14와 절 제목을 계속 표제로 적었다. 기호 k̄에 평균 파수라는 정의를 덧붙였다. 같은 쪽의 기록 하단에도 평균 파수라고 적었다. | 이 쪽에 인쇄되지 않은 계속 표제를 삭제했다. 정의 없이 제시된 기호 k̄를 그대로 기록했다. 기록 하단의 중복 문장도 바로잡았다. | PDF p.120(인쇄 112), 식 (3.82) 아래 “For instance, in the computation of k̄, P* = P − 2n − 1.”. 이 쪽의 절 표제는 3.15이다. |
| `manuals/pdfs/swantech.pdf/p109-126.md:p.121` · 정정 | §3.15와 절 제목을 계속 표제로 적었다. | 이 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다. | PDF p.121(인쇄 113), 첫 줄 “measurements were taken at fixed positions.”. 이 쪽의 절 표제는 “3.16 Interpolation of spectra”이다. |
| `manuals/pdfs/swantech.pdf/p109-126.md:p.122` · 정정 | §3.16과 절 제목을 계속 표제로 적었다. 첫머리에 식 (3.85)라는 번호를 덧붙였다. | 이 쪽에 인쇄되지 않은 절 표제와 식 번호를 삭제했다. | PDF p.122(인쇄 114), 첫 줄 “with i=1,2 ... and k=0,1”. 첫 인쇄 식 번호는 (3.86)이다. 절 표제는 “3.17 Computation of breaking source term”이다. |
| `manuals/pdfs/swantech.pdf/p109-126.md:p.123` · 정정 | §3.17과 절 제목을 계속 표제로 적었다. | 이 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다. | PDF p.123(인쇄 115), 본문은 “and”와 식 (3.96)으로 시작한다. §3.17 표제는 없다. |
| `manuals/pdfs/swantech.pdf/p109-126.md:p.126` · 정정 | Chapter 4의 제목을 계속 표제로 적었다. | 이 쪽에 인쇄된 머리말 Chapter 4만 기록했다. | PDF p.126(인쇄 118), 머리말 “Chapter 4”. “Wave boundary and initial conditions”라는 장 제목은 없다. |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.128` · 정정 | 중첩 모델 설명을 5.1절로 표기했다. | 이 쪽에 인쇄되지 않은 5.1을 삭제했다. | PDF p.128(인쇄 120), 첫 줄 “The setup computed in the larger model”. 절 표제는 5.2와 5.2.1이다. |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.129` · 정정 | 5.2.1과 절 제목을 계속 표제로 적었다. | 이 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다. | PDF p.129(인쇄 121), 머리말 “Implementation of 2D wave setup”. 본문은 반변 기저벡터의 성분 정의로 시작한다. 5.2.1 표제는 없다. |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.130` · 정정 | 5.2.1 계속이라고 표기했다. 식 (5.14)의 두 적분식에서 가장 바깥쪽 닫는 괄호를 누락했다. 같은 쪽 후속 메모에도 닫는 괄호가 인쇄되지 않았다고 적었다. | 인쇄되지 않은 절 번호를 삭제했다. 두 적분식의 닫는 괄호를 원문대로 복원했다. 같은 쪽 후속 메모도 바로잡았다. | PDF p.130(인쇄 122), 식 (5.14)의 첫째 적분 줄 끝은 $\vec{F}))d\Omega_x$이다. 둘째 적분 줄 끝은 $\vec{F}))d\Omega_\xi$이다. 두 닫는 괄호를 확대 이미지에서 확인했다. 5.2.1 표제는 없다. |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.131` · 정정 | 5.2.1 계속이라고 표기했다. 가상 셀 설명의 c⁽ᵅ⁾에 벡터 화살표를 붙였다. | 인쇄되지 않은 절 번호를 삭제했다. c⁽ᵅ⁾의 화살표를 원문 표기에 맞춰 삭제했다. | PDF p.131(인쇄 123), 식 (5.24) 아래 “because we need the c⁽ᵅ⁾ at the boundary”. 이 c에는 화살표가 없다. 5.2.1 표제는 없다. |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.132` · 정정 | 건조점 처리를 5.2.1절로 표기했다. | 이 쪽에 인쇄되지 않은 5.2.1을 삭제했다. | PDF p.132(인쇄 124), 소제목 “Building of the matrix and right hand side”. 5.2.1 표제는 없다. |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.133` · 정정 | 행렬 구성 설명을 5.2.1절로 표기했다. | 이 쪽에 인쇄되지 않은 5.2.1을 삭제했다. | PDF p.133(인쇄 125), 첫 문단은 분배를 설명한다. 절 표제는 “5.2.2 The iterative solver for the linear system”이다. |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.133` · 보완 | 비대칭 행렬의 사용과 전 경계 노이만 조건의 특이성만 기록했다. | 비대칭성은 작은 단점에 불과하다는 한정과 그 이유를 추가했다. 해법 구성 시 특이성을 고려해야 한다는 요구를 추가했다. | PDF p.133(인쇄 125), “This is only a small drawback, because recently good methods have been developed”. 다음 문단 “We have to keep this in mind during the construction of the solution procedure.” |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.134` · 정정 | 쪽에 인쇄되지 않은 절 번호 ‘5.2.2 계속’을 기재했다. | 절 번호를 삭제했다. 실제 소제목 ‘The iterative solver’는 유지했다. | PDF p.134(인쇄 p.126): 머리말 ‘Chapter 5’; 소제목 ‘The iterative solver’. 절 번호 5.2.2는 인쇄되어 있지 않다. |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.136` · 정정 | 인쇄되지 않은 6.1 절 제목을 기재했다. 첫 문장의 주어를 ‘반복행렬 M’으로 복원했다. | 6.1 절 제목을 삭제했다. 첫머리는 주어 없이 앞 쪽 문장을 마무리하는 구절로 기록했다. | PDF p.136(인쇄 p.128) 첫 행: ‘is close to A by relation (6.2).’ 실제 절 제목은 ‘6.2 Successive Over Relaxation (SOR) technique’이다. |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.137` · 보완 | 희소 선형계가 생기는 맥락을 생략했다. MPICH의 무료 배포 설명과 각주 주소를 생략했다. 추가 구현·알고리즘 문제가 남는다는 단서를 생략했다. | 전산유체역학의 유한차분법·유한체적법이라는 맥락을 보완했다. MPICH 설명과 각주를 보완했다. 다루어야 할 추가 문제가 남는다는 단서를 보완했다. | PDF p.137(인쇄 p.129): ‘arising from finite difference or finite volume methods in computational fluid dynamics’; ‘MPICH which is free software’; 각주 1 배포 주소; ‘There are, however, some other implementation and algorithmic issues that need to be addressed.’ |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.138` · 정정 | 인쇄되지 않은 7.1 절 제목을 기재했다. 사용자의 ‘대부분’이라는 한정을 생략했다. 습윤점당 계산량의 일정성이 시간에 관한 것임을 생략했다. | 7.1 절 제목을 삭제했다. ‘대부분의 최종 사용자’로 한정했다. ‘모의가 진행되는 동안 각 습윤점’으로 시간 조건을 명시했다. | PDF p.138(인쇄 p.130): ‘most end-users are not willing to determine the partitioning themselves’; ‘the amount of computations in each wet grid point remains more or less constant during the simulation’. 실제 절 제목은 7.2이다. |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.139` · 정정 | 인쇄되지 않은 7.2 절 제목을 기재했다. 블록 파면 접근의 명칭을 Bastian and Horton에게 직접 귀속했다. 쪽 끝에 없는 ‘다음 띠의 프로세서’를 통신 상대라고 적었다. | 7.2 절 제목을 삭제했다. 저자들의 아이디어에 기반한 전략에 본문이 붙인 명칭으로 구분했다. 쪽 끝의 통신 문장이 미완성임을 기록했다. | PDF p.139(인쇄 p.131): ‘based on the ideas proposed by Bastian and Horton (1991) and is referred here to as the block wavefront approach’; 마지막 행 ‘Thereafter, communication takes place between this processor and’. |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.139` · 보완 | 다색 순서 기법의 참조 문헌만 기재했다. | 다색 순서 기법이 이전에 제안되었다는 설명을 보완했다. | PDF p.139(인쇄 p.131), 그림 7.1 아래: ‘This multicolor ordering technique has been proposed earlier, e.g. in Meurant (1988) and Van der Vorst (1989).’ |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.140` · 정정 | 인쇄되지 않은 ‘7.2 계속’을 기재했다. 두 띠의 미지수를 병렬로 갱신한다고 단정했다. | 절 번호를 삭제했다. 원문의 can에 맞추어 병렬로 갱신할 수 있다고 기록했다. | PDF p.140(인쇄 p.132): 머리말 ‘Chapter 7’; ‘The unknowns N(i,2,l,m) along j = 2 in strip 1 and N(i,1,l,m) along j = 1 in strip 2 can be updated in parallel’. |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.140` · 보완 | 쪽 첫머리의 통신 상대 구절을 생략했다. 소스 코드 안내와 점별 표준 파면 기법과의 유사성을 생략했다. | ‘둘째 띠의 프로세서’라는 첫 구절을 보완했다. 상세는 소스 코드에 있다는 안내를 보완했다. 두 기법이 매우 비슷하다는 설명을 보완했다. | PDF p.140(인쇄 p.132): ‘processor for strip 2.’; ‘Details can be found in the source code of SWAN.’; ‘This technique resembles much to the standard wavefront technique applied in a pointwise manner’. |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.141` · 정정 | 인쇄되지 않은 ‘7.2 계속’을 기재했다. 앞 쪽의 버전 41.10과 블록 야코비 접근을 이 쪽의 문장으로 복원했다. | 절 번호와 앞 쪽에서 복원한 버전·기법명을 삭제했다. 첫머리의 미완성 구절과 이 쪽의 곡률 기반 종료 기준 권고를 기록했다. | PDF p.141(인쇄 p.133) 첫머리: ‘front technique as an alternative (see the Implementation Manual how to activate this approach).’ 이어지는 행: ‘The user is however advised to apply the curvature-based termination criterion, as described in Section 3.4.’ |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.143` · 정정 | 쪽 끝에 인쇄되지 않은 ‘곡선 격자’를 다음 쪽에서 가져와 문장을 복원했다. | 실제 마지막 구절 ‘These can be rectilinear or’에서 문장이 끊긴다고 기록했다. | PDF p.143(인쇄 p.135) 마지막 행: ‘two-dimensional structured grid may contain quadrilaterals. These can be rectilinear or’. |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.143` · 보완 | 국소 격자 세분화에 필요한 유연성만 기재했다. | 해안에서 떨어진 곳의 격자 조정에 따른 추가 비용을 유발하지 않아야 한다는 조건을 보완했다. | PDF p.143(인쇄 p.135) 첫 문단: ‘without incurring overhead associated with grid adaptation at some distance offshore’. |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.144` · 정정 | 인쇄되지 않은 8.1.1 절 제목을 기재했다. 첫 문장의 대상을 앞 쪽에서 가져와 ‘구조 격자’로 명시했다. | 8.1.1 절 제목을 삭제했다. 첫 단어 ‘curvilinear’와 이어지는 내부 꼭짓점의 셀 수 문장을 구분해 기록했다. | PDF p.144(인쇄 p.136) 첫머리: ‘curvilinear. The number of cells that meet each other in an internal vertex is always 4. In unstructured meshes this restriction is abandoned.’ 실제 절 제목은 8.1.2와 8.1.3이다. |
| `manuals/pdfs/swantech.pdf/p127-144.md:p.144` · 보완 | 식 (8.1) 앞에 기호 정의만 기재했다. | 셀·면 개수 관계의 대상이 2차원 삼각형 격자라는 조건을 보완했다. | PDF p.144(인쇄 p.136), 식 (8.1) 앞: ‘For a two-dimensional triangular mesh, the number of cells C, the number of boundary faces Eb and internal faces Ei are related according to:’ |

이상 없음: p.109, p.116, p.124, p.125, p.127, p.135, p.142.

정정 28, 보완 8, 이상 없음 7
