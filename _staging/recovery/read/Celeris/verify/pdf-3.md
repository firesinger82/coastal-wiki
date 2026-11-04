# PDF 3 — 2026-11-04 전수 이미지 대조

원본: `models/Celeris/raw/source_code/Celeris-WebGPU/docs/lynett-et-al-2026-an-interactive-nearshore-wave-simulator-for-rapid-design-prototyping-and-natural-hazard-education.pdf`.

판독 기록: [p001-013.md](../Celeris-WebGPU/docs/lynett-et-al-2026-an-interactive-nearshore-wave-simulator-for-rapid-design-prototyping-and-natural-hazard-education.pdf/p001-013.md).

대조자는 codex gpt-6-astra이다.
대조 범위는 PDF p.1–13이다.
직접 연 이미지는 사용자가 지정한 300 dpi PNG 13개이다.
이미지 파일명은 `cel-lynett2026-001.png`부터 `cel-lynett2026-013.png`까지이다.
이미지 디렉터리는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/celpages/`이다.
작은 첨자와 글자는 원본 크기 또는 부분 확대 이미지에서 확인했다.
확대 이미지는 메모리에서만 만들었다.
텍스트 추출본은 철자 확인에만 사용했다.
본문 문단의 쪽 배치는 이미지에 따랐다.

대조한 쪽 수는 13쪽이다.
내용을 고친 쪽 수는 13쪽이다.
기존 오기를 정정한 쪽은 p.9와 p.10의 2쪽이다.
이 두 쪽에는 누락 보완도 있다.
누락 보완만 한 쪽은 p.1–8과 p.11–13의 11쪽이다.
수정 없이 일치한 쪽은 0쪽이다.
마지막 줄은 정정이 있는 쪽을 정정으로 우선 집계한다.
따라서 마지막 줄의 보완 수에는 정정과 보완을 함께 한 2쪽을 중복 산입하지 않는다.
쪽 행에는 실제 수행한 정정·보완 표식을 모두 붙였다.

표의 쪽 행 수는 수정 전후 모두 13개이다.
기존 frontmatter 값은 유지했다.
frontmatter에는 `verified_by: codex gpt-6-astra (2026-11-04, 300dpi 이미지 전수 대조)` 한 줄을 추가했다.
표시 수식 6개는 p.2–4의 이미지와 일치했다.
인쇄 식 번호는 없었다.
번호가 붙은 표는 없었다.
Fig. 1–7의 번호와 캡션은 기존 기록과 일치했다.
p.3의 “neither model relies on numerical dissipation through limiters to mimic breaking”에 해당하는 부정 설명은 유지했다.
표본 오류 예시에 나온 `C++ and HLSL`, `GNU GPL`, `solveTriDiagonal`, `solverTriDiagonal()`, `time_integration.compute`, `tools.compute`, `GPGPU`는 이 PDF의 쪽 이미지에서 확인되지 않았다.
해당 이름은 다른 자료에서 가져와 삽입하지 않았다.

## 정정·보완 목록

아래의 p.N은 PDF 쪽 번호이다.
각 보완의 전체 문장은 판독 기록의 해당 쪽 행에 있다.

| 쪽 | 이전 | 새 | 근거 |
|---|---|---|---|
| p.1 | 초록의 자료 일치도 평가와 실행 성능이 없었다. | 보완: 실험·현장 자료와의 좋은 일치도를 추가했다. 일반 데스크톱에서 실시간보다 빠른 성능이라는 조건을 추가했다. | p.1 Abstract 문단. |
| p.1 | Practical Applications와 서론을 포괄적으로만 요약했다. keywords와 저자·발행 주석을 옮기지 않았다. | 보완: 기존 도구의 설정·공유 문제, 무설치 실행, 수 분 단위 설계 비교, 해빈 경사·주기 교육 예를 추가했다. 약비선형·장파·완경사 조건과 각 정식화의 개선점을 추가했다. keywords, 저자 소속, 교신저자, 제출·승인·발행·토론 날짜, 게재지와 ISSN을 추가했다. | p.1 Practical Applications, Author keywords, Introduction 및 하단 주석. |
| p.2 | 이전 구현에서 웹으로 옮긴 배경과 모드 선택을 짧게 적었다. | 보완: 2017 Celeris와 2020 Celeris Base의 저자·구현 배경을 추가했다. 전용 앱의 제약, URL 공유, 성능 유지, 두 모드의 비선형·분산 대응, 쇄파·마찰·스칼라 기능을 추가했다. | p.2 왼쪽 첫째·둘째 문단. |
| p.2 | 논문 구성 안내 문단이 없었다. 표준 식의 적용 조건과 고차 식의 출처 설명이 일부 없었다. | 보완: 수학 모델부터 결론까지의 논문 구성과 세 검증 사례를 추가했다. 선두 차수 비선형항 유지, 정확한 연속식, 유한 주파수 분산 보정, storm surge·tsunami inundation 조건을 추가했다. Kim et al. (2009)의 원래 3차원 와도 포함 설명을 추가했다. | p.2 왼쪽 마지막 문단과 오른쪽 지배방정식 설명. |
| p.3 | 완전비선형항의 효과와 기존 모델 대비 쇄파 정확도 평가가 없었다. | 보완: 운동량식 일반형의 동일성, 파봉·파곡 형태와 진폭 분산의 예측 개선, 기존 Boussinesq 모델과 비슷한 쇄파 정확도를 추가했다. | p.3 왼쪽 상단 두 문단과 Dissipation Models. |
| p.3 | 스칼라 예시와 재구성의 역할이 일부 없었다. | 보완: 이차 항력 법칙, Hwang et al. (2025), 오염물질 초기 패치, 불연속에서의 국소 보존, 재구성의 안정성·소산 역할, 두 재구성·두 플럭스 선택지를 추가했다. 선두 차수 플럭스의 절단오차 미분 차수 조건을 추가했다. | p.3 Bottom Friction, Passive Scalar Transport, Spatial Discretization 및 번호 목록. |
| p.4 | 일부 수치법 설명과 FUNWAVE-TVD 비교가 없었다. | 보완: minmod의 TVD 역할, HLL의 중간 상태와 접촉 불연속 예, HLLC의 적용 이유, 고차 모드의 미분항 증가, 두 삼중대각계의 발생 이유를 추가했다. 결합 시간적분 대상과 FUNWAVE-TVD·COULWAVE 비교를 추가했다. | p.4 왼쪽 Spatial Discretization 및 Time Integration. |
| p.4 | UI 기능과 입력 동기화의 이유가 일부 없었다. | 보완: WebGL 후속 표준 설명, 무설치·운영체제 독립성, Google Maps 겹침, 표시층·구조물 예를 추가했다. JavaScript 단일 스레드 제약과 단계 사이 갱신의 목적을 추가했다. 자유수면·유속 2D 텍스처를 추가했다. | p.4 Implementation in WebGPU의 각 문단. |
| p.5 | Fig. 1의 제어 블록과 내부 루프가 빠졌다. 계산·렌더링 블록은 한글 요약만 있었다. | 보완: User Interface (UI) Web Page [html], Simulation Control [js], Render and Compute Loop와 모든 내부 단계의 원문 표기를 추가했다. PREDICTOR STEP [wgsl], CORRECTOR STEP [wgsl], RENDER PIPELINE [wgsl]의 각 단계·위첨자·조건을 추가했다. 입출력 화살표의 연결을 추가했다. | p.5 Fig. 1 전체. 300 dpi 원본 크기에서 첨자를 확인했다. |
| p.5 | 쪽 첫 문단의 텍스처 설명과 TriDiag 이름이 없었다. | 보완: 수심·마찰계수의 WebGPU 텍스처 저장을 추가했다. Pass1, …, TriDiag 및 단계별 WGSL 구현을 추가했다. Explorer 카메라 제어와 이 쪽의 거품 생성 설명을 추가했다. | p.5 그림 아래 양단 본문. |
| p.6 | Fig. 2의 UI 패널을 한글로만 열거했다. | 보완: Start Here: Load Simulation Datafiles부터 Modify Simulation Parameters까지의 패널 이름을 원문대로 추가했다. Simulation Window를 추가했다. | p.6 Fig. 2. |
| p.6 | 거품 활용 예, 구현 절 마지막 요약 문단, 검증 목적이 일부 빠졌다. | 보완: 거품 이류·혼합·교육 예, 보안 컴퓨터의 설치 장벽, Unity 렌더링 기능, 일괄 실행·스크립트·대형 터치스크린 활용을 추가했다. 설치·비용 장벽을 줄인다는 요약 문단을 추가했다. 물리·수치 정확도 비교와 기존 모델 대비 정확도 검증 목적을 추가했다. | p.6 Fig. 2 아래 모든 본문 문단 및 Benchmark Tests. |
| p.7 | 쪽 첫 이어쓰기와 기존 모델의 정확도 비교가 없었다. 범례를 번역·요약했다. | 보완: 지난 20년간의 모델과 비교한다는 문장을 추가했다. 비교 구간과 Kennedy et al. (2000)·Løvholt et al. (2013)·Shi et al. (2012)의 동등 정확도 평가를 추가했다. 표준 모드의 외측 쇄파대 오차와 격자 수렴 해석을 추가했다. 여섯 범례 원문과 축 눈금을 추가했다. | p.7 상단 모든 본문 문단과 Fig. 3. 캡션 067071과 도표 061071의 차이는 유지했다. |
| p.8 | Fig. 4의 색·선 대응과 일부 결론이 없었다. 원추형 섬의 일치도 평가와 Duck 현장 소개가 일부 빠졌다. | 보완: Fig. 4 범례의 선·색과 nd·th 위첨자 및 축 눈금을 추가했다. 규칙파 비교의 첫째·둘째 결론을 추가했다. 섬 검증 목적, 배후 파면 충돌, 시계열·처오름의 매우 좋은 일치도, 2D 예측 평가를 추가했다. US Army Field Research Facility, DUCK85, DUCK94를 추가했다. | p.8 Fig. 4, 규칙파 결론 목록, Solitary Wave Run-Up 및 Spectral Wave Transformation 문단. |
| p.9 | 반경 눈금 1과 2가 보인다고 적었다. | 정정: 직접 보이는 숫자는 1이다. 중앙 범례에 가린 숫자는 확정하지 않는다. | p.9 Fig. 5(d). |
| p.9 | Fig. 5의 축 표기 위치와 (d) 범례가 명확하지 않았다. 관측 일치도와 Kazolea and Ricchiuto (2024)의 논지가 빠졌다. | 보완: 축 제목이 실제 인쇄된 패널과 (d) 범례를 추가했다. 스펙트럼 평균주기·왜도·비대칭도의 좋은 관측 일치도를 추가했다. 약분산 현장 조건에서 완전비선형항의 개선 효과가 작을 수 있다는 문단을 추가했다. NOAA 인용과 격자 선정 근거를 추가했다. | p.9 Fig. 5와 아래 현장 비교·설계 예제 문단. |
| p.10 | Crossshore Distance (m, FRF) | 정정: Crosshore Distance (m, FRF) | p.10 Fig. 6(e) 아래 공통 가로축. 해당 부분을 확대하여 철자를 확인했다. |
| p.10 | Fig. 6의 범례를 축약했다. 기존 모델의 작업시간 설명이 일부 빠졌다. | 보완: Beach Elevation, 각 파고·주기·Skew·Asym 범례, Beach Profile을 원문대로 추가했다. 패널별 High-Order와 High-Order mode의 차이를 보존했다. 축 눈금, V자 이안제, 출력 전송·후처리 시간 설명을 추가했다. | p.10 Fig. 6 전체와 본문. 주기 기호의 첨자를 확대 확인했다. |
| p.11 | Fig. 7 내부 제목과 일부 UI 이름이 빠졌다. 대규모 모의를 대체하지 않는다는 부정이 명시되지 않았다. | 보완: 네 패널의 내부 제목, Boussinesq Simulation, 추가 UI 이름과 Update 버튼을 추가했다. 대규모 모의를 대체하지 않고 기존 HPC 모델을 보완한다는 설명을 추가했다. | p.11 Fig. 7 및 하단 첫 문단. 작은 UI 글자를 확대 확인했다. stil과 입력값 0·2·30은 유지했다. |
| p.12 | 오래된 브라우저 조건, f32 사용 이유, 배정밀도 전망, 최종 설계 도구가 아니라는 설명이 일부 빠졌다. | 보완: 최신 WebGPU 브라우저 사용 조건을 추가했다. 소비자 GPU의 수치 형식 제약과 낮은 정밀도 성능 중심의 하드웨어 방향을 추가했다. 최종 설계 확정 도구가 아니며 포괄적 모델링을 대체해서는 안 된다는 용도 제한을 추가했다. | p.12 Performance and Usability Considerations의 둘째·셋째 문단. |
| p.12 | 결론 네 문단을 짧게 통합했다. Fellowship 기관명과 자금 출처가 빠졌다. | 보완: 쇄파대부터 오염물질 확산까지의 적용, 기존 모델과 동등한 정확도, 접근성·협업, 수 분 설계와 기존 수 시간·수 일 비교, 교육 조작 예를 추가했다. 실무자·학생·시민 참여와 다른 환경 모델의 웹 배포에 관한 마지막 문단을 추가했다. Oak Ridge Institute for Science and Education과 USACE 자금을 추가했다. | p.12 Conclusions의 네 문단과 Acknowledgments. |
| p.13 | 참고문헌을 주제와 일부 DOI만으로 요약했다. | 보완: 참고문헌 27개 항목의 저자·제목·연도·권호·쪽·DOI를 추가했다. Gobbi 제목의 $O(kh)^4$를 보존했다. Bak and Lynett의 2025 및 January 14, 2026을 모두 보존했다. | p.13 References 전체. Gobbi 제목의 지수 4를 확대 확인했다. |

## 판독 중 확인된 사실

- p.7 Fig. 3(d)의 제목은 `061071`이다. 캡션은 `067071`이다. 원문의 차이를 유지했다.
- p.9 Fig. 5(d)의 반경 숫자 `1`은 보인다. 중앙 범례 뒤의 눈금은 확정하지 않았다. 기존의 “이미지로 판독할 수 없었던 항목은 없다” 문장도 이 제한에 맞게 고쳤다.
- p.10 Fig. 6의 가로축은 `Crosshore Distance (m, FRF)`이다. 원문 철자를 유지했다.
- p.11 Fig. 7(b)의 UI는 `Change in stil water level`로 인쇄되어 있다. 원문 철자를 유지했다.
- p.12 브라우저 지원과 GPU 사양은 논문에 적힌 주장으로 유지했다. 현재 제품 상태를 외부 검증하지 않았다.
- p.13 Bak and Lynett 항목의 연도는 2025이다. 같은 항목의 제출일은 January 14, 2026이다. 원문의 차이를 유지했다.

## 열지 못한 이미지

없음.
지정한 13개 PNG를 모두 직접 열었다.

정정 2, 보완 11, 일치 0
