# CADMAS-SURF PDF 55–72쪽 전수 대조

검증일은 2026-11-04이다. 검증자는 codex gpt-6-astra이다.

원본은 `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Manual/CADMAS-SURF3D_Manural_English.pdf`이다.

대상 기록은 [p055-072.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Manual/CADMAS-SURF3D_Manural_English.pdf/p055-072.md)이다.

대조한 쪽 수는 PDF p.55–p.72의 18쪽이다. 지정된 300 dpi PNG 18개를 이미지 보기 도구로 모두 열었다. 수식의 작은 첨자와 코드 예시는 원본 픽셀 영역을 메모리에서 잘라 확대했다. 추출본은 일부 문구의 철자를 확인하는 데 참고했다. 판독 결과는 이미지를 기준으로 정했다.

고친 쪽 수는 아래 목록에 있는 서로 다른 쪽 번호 15개이다. 정정은 2쪽이다. 보완은 15쪽이다. 정정과 보완을 함께 한 쪽은 p.61과 p.66이다. 일치는 p.56, p.59, p.70의 3쪽이다. 정정·보완 수는 유형별 쪽 수이므로 서로 중복된다. 절 제목과 표 캡션의 앞 쪽 출처를 명시한 변경은 보완으로 셌다.

기록의 쪽 행은 p.55–p.72의 18행을 유지했다. 기존 frontmatter 항목은 유지했다. frontmatter에는 요청된 `verified_by` 한 줄만 추가했다.

## 정정·보완 목록

유형은 근거 열의 첫 부분에 표시했다.

| 쪽 | 이전 | 새 | 근거 |
|---|---|---|---|
| p.55 | 해당 내용이 빠져 있었다. | 본문은 전처리를 적용한 BCGSTAB 방법의 수렴성과 안정성이 우수하다고 설명한다. 이 채택 설명에는 참고문헌 표지 `15)`가 붙어 있다. | 보완. p.55 본문 둘째 문단의 `excellent convergence and stability`와 위첨자 `15)`. |
| p.57 | `3.6` 계속. | 앞 쪽에서 이어지는 절 `3.6. Air pressure calculation model`이다. 이 쪽에는 절 제목이 다시 인쇄되어 있지 않다. | 보완. p.57은 `where, γ is the specific heat ratio`로 시작한다. 절 제목은 p.56에 있다. |
| p.58 | `3.6` 계속. | 앞 쪽에서 이어지는 절 `3.6. Air pressure calculation model`이다. 이 쪽에는 절 제목이 다시 인쇄되어 있지 않다. | 보완. p.58은 `implicit solution as follows.`로 시작한다. 절 제목은 p.56에 있다. |
| p.58 | 그림 안 설명은 한국어 요지만 있었다. | 그림의 내부 영역은 흰색이다. 그 주위 영역은 회색 무늬로 채워져 있다. 그림 안 설명의 원문은 `The flow velocity at the position of → is the boundary flow velocity determined by the divergence condition of the surface cell.`이다. 이 문장은 화살표 위치의 유속이 표면 셀의 발산조건으로 정한 경계유속이라는 뜻이다. | 보완. p.58 Figure 0-3-13의 격자와 설명 상자. |
| p.60 | `4.1`의 흐름도. | 앞 쪽에서 이어지는 절 `4.1. Processing flow`의 흐름도이다. 이 쪽에는 절 제목이 다시 인쇄되어 있지 않다. | 보완. p.60에는 Figure 0-4-1과 캡션만 있다. 절 제목은 p.59에 있다. |
| p.60 | 오른쪽 구간 이름의 원문과 내부 반복의 복귀 경로가 빠져 있었다. | 그림 오른쪽의 구간 이름은 `Preprocessing`, `Calculation loop`, `Post processing`이다. 각 구간의 양 끝은 세로 양방향 화살표로 표시되어 있다. `Velocity /Pressure calculation` 뒤의 선은 `L=1, NLOOP` 판정 앞으로 돌아간다. | 보완. p.60 Figure 0-4-1 오른쪽 구간 이름과 내부 반복선. |
| p.61 | 본문의 `CADMAS-SURF/3D-MG`와 그림의 끝 글자가 다르다. | 이 쪽 본문의 모델 이름은 `CADMAS - SURF / 3D`이다. 그림의 모델 이름에는 `-MP`가 붙어 있다. | 정정. p.61 둘째 문단 첫 문장과 Figure 0-4-2 오른쪽 이름. |
| p.61 | 파랑 계산 특화 설명과 그림의 점선 구분이 빠져 있었다. | 본문은 `CADMAS - SURF / 3D`가 파랑 계산에 특화되어 있다고 설명한다. 그림의 점선은 `MPI`와 `MPI mask` 사이에 있다. 오른쪽의 `CADMAS-SURF/3D-MP` 구간 표시는 `MPI mask`부터 `Calculation routine etc.`까지를 묶는다. | 보완. p.61 둘째 문단 첫 문장과 Figure 0-4-2의 점선·구간 화살표. |
| p.62 | Figure 0-4-4에 대한 본문 참조가 빠져 있었다. | 본문은 두 층 통신의 참조 그림으로 `Figure 0-4-3`과 `Figure 0-4-4`를 함께 적는다. | 보완. p.62 본문 마지막 괄호. |
| p.63 | `4.2.2`의 그림이 이어진다. | 앞 쪽에서 이어지는 절 `4.2.2. Coverage area and communication area of each processor`의 그림이다. 이 쪽에는 해당 절 제목이 다시 인쇄되어 있지 않다. | 보완. p.63 상단에는 Figure 0-4-4가 있다. 해당 절 제목은 p.62에 있다. |
| p.64 | `4.3.1`의 표. | 앞 쪽에서 이어지는 절 `4.3.1. File classification`의 표이다. 이 쪽에는 절 제목이 다시 인쇄되어 있지 않다. | 보완. p.64에는 Table 0-4-1과 캡션만 있다. 절 제목은 p.63에 있다. |
| p.65 | 표의 일부 설명 이름과 주석 접두어가 빠져 있었다. | 표의 오른쪽 설명은 첫 코드 구간을 `Parameter statement`로 표시한다. 정수 공통문 구간은 `Common statement (Integer)`로 표시한다. 개요 주석의 시작은 `CD=== Overview`이다. 파일 설명 주석의 시작은 `CDT`이다. 내용 주석의 시작은 `C==== Contents`이다. 변수 설명 주석의 시작은 `CD`이다. 매개변수 예시의 두 변수명 자리에는 각각 `@@@@@@`가 있다. 각 값 자리에는 `@@@`가 있다. | 보완. p.65 Table 0-4-2의 양쪽 열과 확대 확인한 PARAMETER 행. |
| p.66 | `Table 0-4-2 Include file coding style`의 계속이다. | 앞 쪽에서 이어지는 절 `4.3.2. Include file`의 표이다. p.65의 `Table 0-4-2 Include file coding style`이 이어진다. 이 쪽에는 절 제목과 표 캡션이 다시 인쇄되어 있지 않다. | 보완. p.66에는 p.65 표의 계속 부분만 있다. |
| p.66 | 서로 다른 두 설명을 단일 백틱 인용으로 합쳤다. | CNS와 TRN을 별도 인용으로 구분했다. 콜론 표기를 이미지와 맞췄다. | 정정. p.66 오른쪽 열에는 CNS와 TRN 설명이 별도로 인쇄되어 있다. |
| p.66 | 정수 공통문의 (1)·(2) 주석과 주석 접두어가 빠져 있었다. | 정수 공통문 예시의 첫 부분에도 `CD (1)`과 `CD (2)`로 시작하는 설명 주석이 있다. 실수 공통문 예시의 개요 주석은 `CD=== Overview`로 시작한다. 파일 설명 주석은 `CDT`로 시작한다. 두 공통문 예시의 내용 주석은 `C==== Contents`로 시작한다. 각 변수 설명은 `CD`로 시작한다. | 보완. p.66 표 왼쪽 열의 위쪽 두 줄과 실수 공통문 구간. |
| p.67 | 표의 열 제목과 코드 예시의 일부 주석 이름이 빠져 있었다. | 표의 열 제목은 `Coding style`과 `Description`이다. 루틴 설명 주석은 `CDT VF_XXXXXX:`로 시작한다. 그 아래에는 `CD (1)`과 `CD (2)`로 시작하는 설명 주석이 있다. 전역형 주석은 `C - Global type -`이다. 전역변수 주석은 `C - global variable -`이다. | 보완. p.67 Table 0-4-3의 열 제목과 확대 확인한 왼쪽 코드 예시. |
| p.68 | `Table 0-4-3 Source file coding policy`의 계속이다. | 앞 쪽에서 이어지는 절 `4.3.3. Source file coding policy`의 표이다. p.67의 `Table 0-4-3 Source file coding policy`가 이어진다. 이 쪽에는 절 제목과 표 캡션이 다시 인쇄되어 있지 않다. | 보완. p.68에는 p.67 표의 계속 부분만 있다. |
| p.68 | 배열 선언 예시는 `DIMENSION`이다. | 배열 선언 예시는 `DIMENSION @@@@@@ @`이다. 이 선언 예시는 인수 설명 뒤와 지역변수 설명 뒤에 각각 있다. | 보완. p.68 왼쪽 열의 두 DIMENSION 행. |
| p.68 | 9510 FORMAT만 기록했다. | FORMAT 예시의 인수와 닫는 작은따옴표가 없는 인쇄 상태를 기록했다. | 보완. p.68 확대 이미지의 9510 FORMAT 행. |
| p.68 | 인수·지역변수·실행문 구간의 주석 이름과 오른쪽 설명 일부가 빠져 있었다. | 인수 구간의 주석은 `CD - Argument -`이다. 지역변수 구간의 주석은 `CD - Local variable -`이다. 실행문 구간에는 `CD - @@@@ @@ -` 주석이 두 번 있다. 실행문 끝의 주석은 `C - End of executable statement -`이다. 오른쪽 설명에는 `Start of execution statement`와 `End of executable statement`가 있다. | 보완. p.68 양쪽 열의 주석과 실행문 시작·끝 설명. |
| p.69 | 비정상 종료의 입력 오류 예시와 주 루틴 반복 경로의 세부가 빠져 있었다. | 본문은 비정상 종료의 예시를 `such as an input error which can be detected by the program`으로 적는다. 이 구절은 프로그램이 검출할 수 있는 입력 오류 등을 뜻한다. 그림의 `VF_A1MAIN`에는 `Process` 상자가 세 개 있다. 첫 `Process` 다음에는 둘째 `Process`와 `End` 판정이 있다. `End` 판정의 아래 경로는 셋째 `Process`를 거쳐 둘째 `Process` 앞으로 돌아간다. `End` 판정의 오른쪽 경로는 `File close`로 이어진다. 각 `Process`의 점선 화살표는 `VF_A2ERR`를 향한다. 두 루틴의 `STOP` 상자는 회색이다. | 보완. p.69 본문의 괄호 구절과 Figure 0-4-5. |
| p.71 | `Table 0-4-4 Data structure list` 계속. | 앞 쪽에서 이어지는 절 `4.4.1. Data structure list`의 표이다. p.70의 `Table 0-4-4 Data structure list`가 이어진다. 이 쪽 상단에는 해당 절 제목과 표 캡션이 다시 인쇄되어 있지 않다. | 보완. p.71 상단은 p.70 표의 계속 부분이다. 새 절 4.4.2는 표 아래에 있다. |
| p.72 | `4.4.2`의 첫 상세표. | 앞 쪽에서 이어지는 절 `4.4.2. Detailed explanation of global variables by common`의 첫 상세표이다. 이 쪽에는 절 제목이 다시 인쇄되어 있지 않다. | 보완. p.72에는 Table 0-4-5 (1/15)와 캡션만 있다. 절 제목은 p.71에 있다. |

## 대조 결과와 판독 한계

- p.55의 초기화와 ①–⑩ 절차를 대조했다. 수식의 부호와 첨자는 기존 기록과 일치했다.
- p.56–p.58의 식 (3. 127)–(3. 137)을 대조했다. 식의 부호·첨자·식 번호는 기존 기록과 일치했다.
- p.58과 p.60–p.63 및 p.69의 그림을 대조했다. 그림 번호와 캡션은 기존 기록과 일치했다.
- p.64–p.68 및 p.70–p.72의 표를 대조했다. 파일 이름·변수 이름·형·분류·설명과 코드 예시를 확인했다.
- p.72의 매개변수 표는 26개 변수 행이다. 모든 행의 `Type`은 `PRM`이다. `ZERO`, `ZEROG`, `PI`의 `Variable type`은 `R*8`이다. 나머지 23개 행은 `I*4`이다. 이 표에는 매개변수의 수치나 기본값이 없다.
- p.55–p.72의 18개 이미지에서 일본어 문장은 확인되지 않았다.
- p.60의 `Initial conditions etc.` 아래에는 잘린 글자 흔적만 보인다. 확대 후에도 판독하지 못했다. 추출본의 `setting`을 이미지 판독 결과로 채택하지 않았다.
- p.62의 `anaylsys`와 p.63의 `Transfering`은 이미지의 철자를 유지했다.
- p.67의 `VF_A @@@@@.. H`는 두 점을 유지했다.
- p.68의 `A2ERR`와 p.69의 `VF_A2ERR`는 각 쪽의 표기를 유지했다.
- p.68의 `9510 FORMAT` 예시는 마지막 `@` 뒤의 닫는 작은따옴표가 보이지 않는다. 이 인쇄 상태를 기록 끝의 “판독 중 확인된 사실”에 적었다.
- p.69의 정상·비정상 종료 설명은 문장 연결이 어색한 인쇄 상태를 유지했다. 입력 오류 예시와 그림의 경로를 별도로 보완했다.
- p.72의 `Dupuit-Forheimer`는 인쇄된 철자를 유지했다.

열지 못한 이미지는 없다. 이미지 안에서 판독하지 못한 부분은 p.60의 잘린 글자 1곳이다.

정정 2, 보완 15, 일치 3
