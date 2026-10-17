# FUNWAVE PDF 전수 검증 6

판정 기준은 지정된 300dpi 쪽 이미지다.
이미지 경로는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/fwpages/<PDF 이름>-<세 자리 쪽번호>.png`다.
대조 행 수는 판독 기록 표의 쪽 행을 센 값이다.
정정과 보완은 아래 목록의 항목 수를 센다.
하나의 쪽 행에 정정과 보완이 함께 있을 수 있다.
이상 없음은 대조한 쪽 행 중 변경이 없는 행을 센다.

| 기록 | 대조한 행 수 | 상태 |
|---|---:|---|
| [Intro-to-FUNWAVE-CHL-TN.pdf/p019-024.md](../FUNWAVE-TVD/doc/Intro-to-FUNWAVE-CHL-TN.pdf/p019-024.md) | 6/6 | p.19–24 완료 |
| [funwave_code_analysis.pdf/p001-015.md](../FUNWAVE-TVD/doc/funwave_code_analysis.pdf/p001-015.md) | 15/15 | p.1–15 완료 |

대상 기록의 전체 21행을 대조했다.
각 기록의 frontmatter는 유지했다.
각 기록의 쪽 행 구성은 유지했다.
원문 이미지에서 잘린 부분은 판독 불가 표시를 유지했다.
모델은 실행하지 않았다.
원문·노트·git은 변경하지 않았다.

아래 표의 기록명은 위 파일명의 PDF 이름을 줄여 쓴다.
원문 행은 쪽 이미지의 본문·그림·표에서 찾을 수 있는 위치로 적었다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| Intro-to-FUNWAVE-CHL-TN:p.21 (보완) | 그림 7의 지형 표기로 BEACH LOCATION만 기록했다. | 그림 7의 SUBMERGED BAR 표기를 추가했다. | p.21 Figure 7 음영 사주 안의 `SUBMERGED BAR`. |
| Intro-to-FUNWAVE-CHL-TN:p.22 (보완) | 월파를 동반한 처오름 성능의 서술 범위를 기록하지 않았다. | 성능 평가에 `In the identified statements of needs`라는 한정을 추가했다. | p.22 두 번째 글머리표 첫 문장 `In the identified statements of needs`. |
| Intro-to-FUNWAVE-CHL-TN:p.22 (보완) | Git 활용에 투자한 목적을 기록하지 않았다. | 적절한 소프트웨어 개발 실무를 따르려는 목적을 추가했다. | p.22 여덟 번째 글머리표 끝 `in order to adhere to proper software carpentry practices`. |
| Intro-to-FUNWAVE-CHL-TN:p.23 (보완) | Beji–Battjes, Briggs 등, Hansen–Svendsen, Kirby 등의 일부 발행 정보를 생략했다. | Amsterdam의 Elsevier Science Publishers B.V.를 추가했다. International Association for Hydraulic Research와 Delft를 추가했다. Denmark와 Newark, DE를 추가했다. | p.23 Beji–Battjes (1993), Briggs 등 (1994), Hansen–Svendsen (1979), Kirby 등 (1998) 항목의 발행 정보 행. |
| funwave_code_analysis:p.1 (보완) | 분석 결과의 가치와 향후 지침에 대한 저자 평가를 생략했다. 도구의 효과는 도움 가능성으로만 요약했다. | 매우 가치 있는 결과라는 평가를 추가했다. 향후 지침 제안을 추가했다. 디버깅 간소화와 개발 가속을 추가했다. 필수적인 도구 모음이라는 평가를 추가했다. | p.1 Abstract의 `the results are invaluable`. §1의 `suggest guidelines`, `greatly streamline debugging`, `accelerate development`, `an essential set of tools`. |
| funwave_code_analysis:p.1 (보완) | 하위 보고서의 맵과 역방향 맵 설명을 생략했다. | 맵과 역방향 맵을 제공한다는 설명을 추가했다. | p.1 §2 두 번째 문단 `a set of maps and inverse maps`. |
| funwave_code_analysis:p.2 (정정) | 해당 쪽에 없는 `§2 Summary Report`를 붙였다. | 보고서의 절 번호와 제목이 이 쪽에 없음을 명시했다. | p.2에는 Figure 1 화면과 캡션만 있다. |
| funwave_code_analysis:p.2 (보완) | Figure 1의 메뉴 일부만 기록했다. | 형·include 파일 상호 참조, 호출 트리, 복잡도, 프로젝트·파일 평균 지표, Fortran 확장, 암시적 선언, 미초기화, 미사용 항목 메뉴를 추가했다. | p.2 Figure 1 왼쪽 Table of Contents의 `Type Cross Reference`부터 `Unused Objects and Functions`까지 해당 메뉴 행. |
| funwave_code_analysis:p.3 (정정) | 해당 쪽에 없는 `§2 Summary Report`를 붙였다. | 보고서의 절 번호와 제목이 이 쪽에 없음을 명시했다. | p.3에는 Figure 2 화면과 캡션만 있다. |
| funwave_code_analysis:p.4 (정정) | 해당 쪽에 없는 `§2 Summary Report`를 붙였다. | 보고서의 절 번호와 제목이 이 쪽에 없음을 명시했다. | p.4에는 Figure 3 화면과 캡션만 있다. |
| funwave_code_analysis:p.4 (정정) | 화면이 서브루틴과 함수를 나열한다고 기록했다. | 완전히 보이는 프로그램 단위는 모두 Subroutine임을 명시했다. 캡션의 일반적인 설명은 유지했다. | p.4 Figure 3 각 프로그램 단위 오른쪽의 `Subroutine`. |
| funwave_code_analysis:p.4 (보완) | 하단 목록을 `CONSTRUCT_Y` 등으로 끝냈다. | 그 다음 행은 화면 하단에 일부만 표시된다는 사실을 추가했다. | p.4 Figure 3 화면 하단의 `CONSTRUCT_Y` 다음 행. |
| funwave_code_analysis:p.5 (정정) | 해당 쪽에 없는 `§2 Summary Report`를 붙였다. | 보고서의 절 번호와 제목이 이 쪽에 없음을 명시했다. | p.5에는 Figure 4 화면과 캡션만 있다. |
| funwave_code_analysis:p.5 (정정) | ESTIMATE_DT의 보이는 문자열이 `DX,`에서 끝난다고 기록했다. | 오른쪽에서 잘리기 전 `DX,REA`까지 보이는 것으로 정정했다. | p.5 Figure 4 `ESTIMATE_DT` 인수 선언의 오른쪽 끝 `DX,REA`. |
| funwave_code_analysis:p.6 (정정) | 해당 쪽에 없는 `§2 Summary Report`를 붙였다. | 보고서의 절 번호와 제목이 이 쪽에 없음을 명시했다. | p.6에는 Figure 5 화면과 캡션만 있다. |
| funwave_code_analysis:p.7 (정정) | 해당 쪽에 없는 `§2 Summary Report`를 붙였다. | 보고서의 절 번호와 제목이 이 쪽에 없음을 명시했다. | p.7에는 Figure 6 화면과 캡션만 있다. |
| funwave_code_analysis:p.7 (보완) | 두 gamma_spec 소속 루틴의 잘린 인수 선언에서 읽을 수 있는 부분을 생략했다. | 첫 루틴은 `mfreq,INTEGE`까지 기록했다. 둘째 루틴은 `mfre`까지 기록했다. 잘린 뒷부분은 판독 불가로 남겼다. | p.7 Figure 6 위쪽 CALCULATE_TMA_Cm_Sm과 WK_WAVEMAKER_IRREGULAR_WAVE 선언 행. |
| funwave_code_analysis:p.7 (보완) | A_sponge와 A_sponge_wavemaker의 사용 위치에 붙은 루틴 이름을 생략했다. | Use Argument의 INITIALIZATION을 추가했다. Set와 Use의 READ_INPUT을 추가했다. | p.7 Figure 6 `GLOBAL.A_sponge` 및 `GLOBAL.A_sponge_wavemaker` 각 참조 행의 오른쪽 루틴 이름. |
| funwave_code_analysis:p.8 (정정) | 해당 쪽에 없는 `§2 Summary Report`를 붙였다. | 보고서의 절 번호와 제목이 이 쪽에 없음을 명시했다. | p.8에는 Figure 7 화면과 캡션만 있다. |
| funwave_code_analysis:p.8 (보완) | 호출 인수 표시에 관한 캡션과 화면의 차이를 끝 절에만 적었다. 불일치라는 점은 명시하지 않았다. | 호출 인수를 나열한다는 캡션과 인수가 없는 화면의 불일치를 쪽 행과 끝 절에 명시했다. | p.8 Figure 7 캡션의 `listing the line number and the call arguments`. 같은 그림의 Call 행에는 파일·행 번호와 루틴 이름만 표시된다. |
| funwave_code_analysis:p.9 (정정) | 해당 쪽에 없는 `§2 Summary Report`를 붙였다. | 보고서의 절 번호와 제목이 이 쪽에 없음을 명시했다. | p.9에는 Figure 8 화면과 캡션만 있다. |
| funwave_code_analysis:p.10 (정정) | 해당 쪽에 없는 `§2 Summary Report`를 붙였다. | 보고서의 절 번호와 제목이 이 쪽에 없음을 명시했다. | p.10에는 Figure 9 화면과 캡션만 있다. |
| funwave_code_analysis:p.10 (보완) | HTML 보고서의 생성 시각을 기록하지 않았다. | October 18, 2016 5:32:56 PM CDT를 추가했다. | p.10 Figure 9 왼쪽 아래 `Generated on: October 18, 2016 5:32:56 PM CDT`. |
| funwave_code_analysis:p.11 (보완) | Figure 10의 왼쪽 파일 노드 일부를 생략했다. | nesting.F, samples.F, parallel.F, mod_vessel.F, Makefile, README.md, files.txt를 추가했다. | p.11 Figure 10 왼쪽에서 main.F 아래에 배치된 파일 노드. |
| funwave_code_analysis:p.12 (정정) | 해당 쪽에 없는 `§3 Diagrams`를 붙였다. | 보고서의 절 번호와 제목이 이 쪽에 없음을 명시했다. | p.12에는 Figure 11–13과 각 캡션만 있다. |
| funwave_code_analysis:p.12 (보완) | FLUXES의 function 및 Subroutine 표기를 끝 절에 병기했다. 종류 명칭의 불일치는 명시하지 않았다. | 종류 명칭의 불일치를 p.12 행과 끝 절에 명시했다. | p.12 Figure 13 캡션 `the function FLUXES`. p.8 Figure 7 `FLUXES (Subroutine)`. |
| funwave_code_analysis:p.13 (정정) | 해당 쪽에 없는 `§3 Diagrams`를 붙였다. | 보고서의 절 번호와 제목이 이 쪽에 없음을 명시했다. | p.13에는 Figure 14–15와 각 캡션만 있다. |
| funwave_code_analysis:p.14 (정정) | 해당 쪽에 없는 `§3 Diagrams`를 붙였다. | 보고서의 절 번호와 제목이 이 쪽에 없음을 명시했다. | p.14에는 Figure 16과 캡션만 있다. |
| funwave_code_analysis:p.14 (보완) | Figure 16에 대한 classic 및 enhanced 설명을 끝 절에 병기했다. 불일치는 명시하지 않았다. | 두 설명의 불일치를 p.14 행과 끝 절에 명시했다. | p.14 Figure 16 캡션 `enhanced flow chart`. p.11 목록 항목 6 `classic flow chart 16`. |
| funwave_code_analysis:p.15 (정정) | 해당 쪽에 없는 `§3 Diagrams`를 붙였다. | 보고서의 절 번호와 제목이 이 쪽에 없음을 명시했다. | p.15에는 Figure 17–18과 각 캡션만 있다. |

이상 없음: Intro-to-FUNWAVE-CHL-TN p.19, p.20, p.24.

정정 15, 보완 15, 이상 없음 3
