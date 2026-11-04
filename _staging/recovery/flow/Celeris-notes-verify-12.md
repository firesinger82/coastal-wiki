# Celeris 노트 전수 대조 12

검증 기준일: 2026-11-04.
대상은 사용자 지정 두 노트의 작업 시작 시 `git diff -U0 HEAD` 추가 줄이다.
빈 줄과 frontmatter도 대상 줄 수에 포함한다.
원문 기준은 Celeris-WebGPU ebca435와 각 행이 지정한 이전 판이다.
정정 수와 보완 수는 수정한 대상 줄 수로 센다.

## 진행

- celeris-source-map.md: 완료.
- celeris-architecture-and-config.md: 완료.

## celeris-source-map.md — 완료

대상: [celeris-source-map.md](../../../models/Celeris/source-analysis/celeris-source-map.md).
시작 시 diff의 추가 줄은 116줄이다.
116줄을 모두 대조했다.
정정은 13줄이다.
보완은 1줄이다.
줄 번호는 작업 시작 시와 정정 후가 같다.

대조 범위는 5–6, 15, 27–35, 47–48, 51–57, 60, 62–63, 66–70, 73–79, 85, 123, 177–198, 230–285행이다.
빈 줄·제목·표 머리·frontmatter도 이 범위에 포함한다.
차이 표 47행의 분류는 최종 배정표와 같다.
47행의 결론 의미는 각 conclusion-verify의 노트용 결론과 같다.
CP2-052에서 조사 한계 문장을 옮기지 않은 것은 사용자 지시와 일치한다.
이 표에는 E 행이 없다.
각 A 행의 논문 판과 근거 커밋을 version-verify-AD1·AD2 및 지정 원문과 대조했다.
본문은 notes-apply-1·8, 각 비교 보고서 §4, callflow §6 및 Claude 렌더 확인 절과 대조했다.
파일 수는 현재 본판 js/*.js 37개와 shaders/*.wgsl 44개를 직접 세어 확인했다.
과거 35개·42개는 CD2-459와 version-verify-AD2의 판별 근거와 대조했다.
명시적 파일·줄 참조 537개를 열었다.
같은 참조의 반복도 이 수에 포함한다.
상대 노트명 celeris-coulwave.md의 참조는 위키의 해당 과거 판으로 별도 대조했다.
Tavakkol 2017 p.3–5, Tavakkol 2020 p.1–6·10, Lynett 2026 p.1·4–5의 쪽 이미지를 확인했다.
논문 식·날짜·그림 구조는 쪽 이미지로 판정했다.
두 번째 경계의 조건과 예측·보정 호출은 main.js의 해당 분기 전체에서 확인했다.
원문 없는 설명과 직접 인용을 구분했다.

### 정정·보완 목록

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| celeris-source-map.md:5 | 보완 | recovery 반영 이력만 기록 → 이번 116줄 원문·최종 결론·쪽 이미지 대조 범위를 추가 | 이 절의 대상 줄 집계와 대조 기록. |
| celeris-source-map.md:55 | 정정 | `NumericalFlux()` → `NumericalFlux` 함수 | `shaders/Pass2.wgsl:36`의 `fn NumericalFlux(aplus: f32, aminus: f32, Fplus: f32, Fminus: f32, Udifference: f32) -> f32 {`. 빈 인수 목록은 원문에 없다. |
| celeris-source-map.md:85 | 정정 | UI 재계산 1614행·초기화 404행·Courant 27행 및 단순화한 구면식 → 현행 2294–2333행·486행·31행과 셀 중심 최소 물리 간격 설명 | `js/main.js:2294`의 `if (calc_constants.html_update > 0) {`. `js/constants_load_calc.js:31`의 `Courant_num: 0.15,`. 472–484행은 간격·반지름·cos 위도의 하한과 셀 중심 위도를 적용한다. 486행은 직교 dt 식이다. RF-021 최종 근거가 설정·UI 재계산을 구분한다. |
| celeris-source-map.md:240 | 정정 | `BoundaryPass again` → 백틱을 포함한 원문 전체 문장 | `ARCHITECTURE.md:55`: ``11. `BoundaryPass` again: re-applies boundary cleanup after the implicit solve.`` |
| celeris-source-map.md:241 | 정정 | 과거 노트 인용 안의 `js/main.js` → 원문 `main.js`. 현재 pipeline 노트 줄 참조 → `d8157c80` 판 참조 | `d8157c80:models/Celeris/source-analysis/celeris-source-map.md:145`의 `main.js:1619-1651` 및 `main.js:2638-2924`. 같은 커밋 pipeline-graph 49·86·118행의 예전 줄 번호. |
| celeris-source-map.md:261 | 정정 | 과거 표 인용의 `js/Run_Tridiag_Solver.js:59` → `Run_Tridiag_Solver.js:59` | `d8157c80:models/Celeris/source-analysis/celeris-source-map.md:160`. |
| celeris-source-map.md:262 | 정정 | 과거 표 인용의 `js/Run_Tridiag_Solver.js:84` → `Run_Tridiag_Solver.js:84` | `d8157c80:models/Celeris/source-analysis/celeris-source-map.md:161`. |
| celeris-source-map.md:263 | 정정 | 문서에 없는 외란 설명을 백틱으로 표기 → 설명문으로 바꾸고 문장 부재를 명시 | CD1-1391 최종 근거는 대상 문서에 활성 함수 설명이 없다고 판정한다. `shaders/AddDisturbance.wgsl:172,182–227`이 코드 근거다. |
| celeris-source-map.md:264 | 정정 | 문서에 없는 선박 코드 언어 설명을 백틱으로 표기 → 설명문으로 바꾸고 문장 부재를 명시 | CD1-1397 최종 근거. `shaders/Ship_pressure.compute:1–18`의 HLSL 선언과 `js/main.js:1536–1594`의 fetch 목록. |
| celeris-source-map.md:266 | 정정 | 현재 COULWAVE 노트 149행 참조·인용 내부 `js/` 추가 → `d8157c80` 149행·원문 `constants_load_calc.js:36` | `d8157c80:models/Celeris/source-analysis/celeris-coulwave.md:149`의 비선형 차수 설명. 현재 149행은 모드 표이므로 해당 문장 인용 위치가 아니다. |
| celeris-source-map.md:272 | 정정 | 생략 부호가 섞인 원문 인용·판 없는 COULWAVE 노트 참조 → 연속 원문 발췌와 `caf75a25` 판 명시 | `d8157c80:models/Celeris/source-analysis/celeris-source-map.md:25`의 `다층 z-α 그룹핑 텍스처`. `caf75a25:models/Celeris/source-analysis/celeris-coulwave.md:12`의 `단일층 완전비선형(fully-nonlinear) 확장 Boussinesq`와 `2층/다층 아님`. |
| celeris-source-map.md:277 | 정정 | “Assets ... Celeris” → “Assets”와 “Celeris”의 분리 인용 | Tavakkol 2020 p.4 §4.1. 두 이름은 같은 연속 원문 구절이 아니다. |
| celeris-source-map.md:278 | 정정 | “.shader ... .cginc ... Material” → 세 원문 어휘의 분리 인용 | Tavakkol 2020 p.4 오른쪽 위의 렌더 파일 설명. |
| celeris-source-map.md:281 | 정정 | 상속 관계 요약을 백틱 원문처럼 표기·`logToFile` → 요약임을 명시·`logTofile` | Tavakkol 2020 p.6 Fig.3의 상속 화살표와 Solver의 `logTofile()` 표기. |

### 기계 확인 후보 판정

- celeris-source-map.md:240의 `ARCHITECTURE.md:55` 후보는 실제 인용 오류다. 원문은 BoundaryPass를 백틱으로 감싼다. 원문 전체를 이중 백틱 인용으로 복원했다. 결론 B와 분산 모델 조건은 유지했다.

상대 링크는 모두 실제 파일을 가리킨다.
Mermaid 블록은 없다.
금지 경로와 사용자 지정 한계 문장은 없다.
이 노트의 미해결 항목은 없다.

## celeris-architecture-and-config.md — 완료

대상: [celeris-architecture-and-config.md](../../../models/Celeris/manual-notes/celeris-architecture-and-config.md).
시작 시 diff의 추가 줄은 105줄이다.
105줄을 모두 대조했다.
정정은 7줄이다.
보완은 5줄이다.
줄 번호는 작업 시작 시와 정정 후가 같다.

대조 범위는 5–6, 12–14, 21–23, 32–36, 40–43, 51–53, 58, 60, 66, 71–72, 78, 83–86, 94, 99–101, 109, 113, 115–119, 123–128, 137, 154, 184–186, 194, 202–204, 213, 215–218, 229–232, 233–272행이다.
빈 줄·제목·표 머리·frontmatter도 이 범위에 포함한다.
차이 표 29행의 분류는 최종 배정표와 같다.
29행의 결론 의미는 각 conclusion-verify의 노트용 결론과 같다.
이 표에는 E 행이 없다.
본문의 고립파 높이와 침강속도 후보는 최종 CD1-1303·1300의 중간 강도와 같다.
퇴적물 보정 전달 후보는 CD1-1301의 호스트 uniform 쓰기와 보정 호출을 대조했다.
본문은 notes-apply-5·9, 각 비교 보고서 §4와 callflow §6의 수정안에 대응한다.
설정 병합·재실행·스키마 부재·미지 키 보존을 초기화 코드와 대조했다.
설정 이름·기본값·단위·파생식·입사파 선택값·단면판 파랑 배열을 해당 원문과 대조했다.
수정 전 검사에서 명시적 파일·줄 참조 473개를 열었다.
같은 참조의 반복도 이 수에 포함한다.
추가로 존재하지 않는 과거 노트 경로 두 개를 발견했다.
두 경로는 실제 과거 노트 경로로 정정한 뒤 열어 확인했다.
Tavakkol 2017 p.1–3·5–7, Tavakkol 2020 p.1–3·9·11–14, Lynett 2026 p.1의 쪽 이미지를 대조했다.
2017년 CR 그림과 현행 PCR의 마지막 패스 쓰기를 구분했다.
2019년 문헌의 저자와 식별자는 Tavakkol 2020 p.14 [29]로 확인했다.

### 정정·보완 목록

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| celeris-architecture-and-config.md:5 | 정정 | `PDF 원논문은 서지만` → 이번 105줄의 코드·문서·최종 결론·논문 쪽 이미지 대조 범위 | 이 절의 대조 기록. 현재 본문은 논문 식·그림과 직접 대조한 주장을 포함한다. |
| celeris-architecture-and-config.md:42 | 보완 | 경계 파일 검사 근거 395–441행 → 324–330·378–400·433–441행 | `js/File_Loader.js:326`의 `values.some(value => !Number.isFinite(value))`. 378행의 `const expectedColumns = 1 + 3 * numPoints;`. 383행의 `if (row.length != expectedColumns) {`. 399행은 시간 증가 검사다. 434–440행은 공통 시간벡터 검사다. |
| celeris-architecture-and-config.md:154 | 보완 | PCR 결과 복사 근거 66행 → 66·91행 | `js/Run_Tridiag_Solver.js:66`은 x 풀이 결과를 복사한다. 91행의 `runCopyTextures(device, calc_constants, txtemp2_PCRy, txNewState)`가 y 풀이 결과를 복사한다. |
| celeris-architecture-and-config.md:185 | 보완 | 오버레이 갱신 호출만 인용 → 초기 렌더 호출 1451행도 인용 | `js/main.js:1451,2437,2450`의 활성 `createRenderBindGroup` 인수 목록이 같다. |
| celeris-architecture-and-config.md:202 | 정정 | [29]에 없는 논문 제목을 서지 인용에 포함 → 저자·연도·arXiv 식별자로 한정 | Tavakkol 2020 p.14 [29]: `S. Tavakkol, S. Son, P. Lynett, ArXiv Prepr. ArXiv:1909.04153 (2019).` CP2-165 수정안도 이 서지 요소만 제시한다. |
| celeris-architecture-and-config.md:250 | 보완 | CD1-1313의 검사 근거 395–441행 → 수치·열 수·시간벡터 검사 위치 추가 | `js/File_Loader.js:324–330,378–400,433–441`. 42행과 같은 검사 근거다. 최종 결론은 유지했다. |
| celeris-architecture-and-config.md:260 | 보완 | CD1-1324의 현행 PCR 근거 66행 → 66·91행 | `js/Run_Tridiag_Solver.js:91`의 y 최종 결과 복사. 최종 결론은 유지했다. |
| celeris-architecture-and-config.md:264 | 정정 | `Tavakkol 2020 Tavakkol 2017 p.1; P26 Tavakkol 2017 p.1` → `Tavakkol 2020 p.1; Lynett 2026 p.1` | CP1-001 최종 근거의 `P20 p.1; P26 p.1`. 두 논문의 첫 쪽 이미지. |
| celeris-architecture-and-config.md:267 | 정정 | 단일 백틱 인용 안의 역슬래시·백틱 → 이중 백틱으로 원문 전체 인용 | `ARCHITECTURE.md:3`의 마지막 문장: ``The source files in `js/` and `shaders/` are the application.`` 원문에는 역슬래시가 없다. |
| celeris-architecture-and-config.md:268 | 정정 | `d8157c80:models/Celeris/source-analysis/celeris-architecture-and-config.md:183` → 같은 커밋의 `manual-notes/` 경로 | `git show d8157c80:models/Celeris/manual-notes/celeris-architecture-and-config.md`의 183행은 2017 논문을 PCR에 연결한 이전 문장이다. `source-analysis/` 경로는 해당 커밋에 없다. |
| celeris-architecture-and-config.md:269 | 정정 | 생략 부호가 섞인 인용·중복 저자/연도·잘못된 source-analysis 경로 → 연속 원문 두 구절·정상 논문 표기·manual-notes 경로 | `d8157c80:models/Celeris/manual-notes/celeris-architecture-and-config.md:185`의 `2019 arXiv 1909.04153`과 `§1.5의 적응형 3차 Adams-Bashforth predictor/corrector 시간적분의 학술적 출처`. Tavakkol 2017 p.3 식 (15)–(20). |
| celeris-architecture-and-config.md:272 | 정정 | `Tavakkol 2017 Tavakkol 2020 p.3`·정의 없는 N9 → `Tavakkol 2017 p.3`·실제 Pass3 식 위치 | CP2-174 최종 근거의 `P17 p.3 식 (15)–(20)`. `shaders/Pass3_Bous.wgsl:399–409`의 Euler·AB3·AM4 식. |

### 기계 확인 후보 판정

- celeris-architecture-and-config.md:267의 `ARCHITECTURE.md:3` 후보는 인용 경계 오류다. `Celeris-WebGPU is a static browser application that runs a coastal wave model al`이라는 시작 부분 자체는 원문과 같다. 뒤쪽 `js/`·`shaders/`의 내부 백틱을 역슬래시로 처리한 형식이 인용을 끊었다. 전체 원문을 이중 백틱으로 감싸서 정정했다. A 판 차이 결론은 유지했다.

상대 링크는 모두 실제 파일을 가리킨다.
Mermaid 블록은 없다.
금지 경로와 사용자 지정 한계 문장은 없다.
이 노트의 미해결 항목은 없다.

## 최종 확인

두 노트의 시작 시 대상 줄 합계는 221줄이다.
정정한 대상 줄 합계는 20줄이다.
보완한 대상 줄 합계는 6줄이다.
각 수정 줄 끝 또는 표의 결론 문장 칸 끝에 지정 표식을 붙였다.
두 frontmatter는 YAML 파싱을 통과했다.
Markdown 파서는 차이 표를 각각 47행과 29행으로 읽었다.
두 차이 표의 분류·근거 파일 연결을 최종 배정표와 다시 대조했다.
두 차이 표의 결론 의미를 최종 근거와 다시 대조했다.
정정 후 명시적 파일·줄 참조를 모두 열 수 있다.
직접 인용의 문자 대조에서 남은 불일치는 없다.
두 노트의 상대 링크 대상 파일은 모두 존재한다.
두 노트에는 Mermaid 블록이 없다.
두 노트에는 금지 경로와 사용자 지정 한계 문장이 없다.
대상 노트의 읽기 전용 `git diff --check`는 통과했다.
쓰기 대상은 두 노트와 이 DELIVERABLE뿐이다.
git 쓰기 명령·sudo·모델 실행은 사용하지 않았다.
미해결 항목은 없다.
