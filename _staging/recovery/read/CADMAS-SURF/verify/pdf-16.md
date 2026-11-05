# CADMAS-SURF PDF 73–90쪽 전수 대조

검증일은 2026-11-04이다.
검증자는 `codex gpt-6-astra`이다.
대상 기록은 [p073-090.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Manual/CADMAS-2F_Manural_English.pdf/p073-090.md)이다.
원본 PDF는 `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Manual/CADMAS-2F_Manural_English.pdf`이다.
쪽 번호는 PDF 쪽 번호다.
대조한 쪽은 p.73–90의 18쪽이다.
내용을 고친 쪽은 검증 표지만 추가한 쪽을 제외한 15쪽이다.
정정한 쪽은 7쪽이다.
보완한 쪽은 11쪽이다.
기존 내용과 일치한 쪽은 3쪽이다.
p.81, p.86, p.89는 정정과 보완에 모두 포함된다.
마지막 줄의 정정·보완 수는 각 표지가 붙은 쪽 수다.
이 수는 변경 항목 수가 아니다.
기록 표의 쪽 행은 기존과 같은 18행이다.
기존 frontmatter는 유지했다.
frontmatter에는 요청한 `verified_by` 한 줄만 추가했다.

이미지는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/`의 `cad-2f-manual-073.png`부터 `cad-2f-manual-090.png`까지 모두 직접 열었다.
이미지 해상도는 사용자가 지정한 300 dpi이다.
p.74와 p.76의 작은 코드 글자는 영역을 확대해서 확인했다.
p.83의 `SCMVP` 수치 표기는 영역을 확대해서 확인했다.
p.89–90의 격자·셀 번호 표기는 영역을 확대해서 확인했다.
확대 이미지는 메모리에서 만들었다.
확대 이미지 파일은 저장하지 않았다.
텍스트 추출본의 p.74–78은 철자 확인에 참고했다.
최종 판독은 PNG를 기준으로 했다.

## 쪽별 결과

| 쪽 | 이미지 대조 | 결과 |
|---|---|---|
| p.73 | 직접 열어 대조함. | 일치 |
| p.74 | 직접 열어 대조함. | 보완 |
| p.75 | 직접 열어 대조함. | 보완 |
| p.76 | 직접 열어 대조함. | 보완 |
| p.77 | 직접 열어 대조함. | 보완 |
| p.78 | 직접 열어 대조함. | 보완 |
| p.79 | 직접 열어 대조함. | 보완 |
| p.80 | 직접 열어 대조함. | 보완 |
| p.81 | 직접 열어 대조함. | 정정·보완 |
| p.82 | 직접 열어 대조함. | 정정 |
| p.83 | 직접 열어 대조함. | 정정 |
| p.84 | 직접 열어 대조함. | 정정 |
| p.85 | 직접 열어 대조함. | 정정 |
| p.86 | 직접 열어 대조함. | 정정·보완 |
| p.87 | 직접 열어 대조함. | 보완 |
| p.88 | 직접 열어 대조함. | 일치 |
| p.89 | 직접 열어 대조함. | 정정·보완 |
| p.90 | 직접 열어 대조함. | 일치 |

## 정정·보완 목록

| p.N | 이전 | 새 | 근거 |
|---|---|---|---|
| p.74 | 기록 없음. | 보완: 본문 첫 문장은 포함 파일의 코딩 형식을 `Table 0-4-2`에서 제시한다고 설명한다. 표의 `VF_A0PRM. h` 설명은 `Files collecting PARAMETER statements`이다. 이 설명은 `PARAMETER` 문을 모은 파일이라는 뜻이다. 표의 정수 공통문 설명은 `Common statement (Integer)`이다. | p.74 PNG 본문 첫 문장과 표의 파일 개요·오른쪽 설명 열. |
| p.75 | 기록 없음. | 보완: 위쪽 정수 공통문 예시에도 `CD (1)`과 `CD (2)`의 설명 자리표시자가 있다. 그 아래 구역 이름은 `C==== Contents`이다. `CNS`는 전처리 후 변경하지 않는다는 뜻이다. `TRN`은 전처리 후 변경한다는 뜻이다. 실수 공통문에 대응하는 설명은 `Common statement (Real)`이다. | p.75 PNG 위쪽 정수 예시의 첫 두 행과 Contents 구역 및 오른쪽 설명 열. |
| p.76 | 기록 없음. | 보완: 본문 첫 문장은 소스 파일의 코딩 형식을 `Table 0-4-3`에서 제시한다고 설명한다. 표의 열 이름은 `Coding style`과 `Description`이다. 개요 주석에는 `CDT VF_XXXXXX:`와 번호 `(1)`, `(2)`의 설명 자리표시자가 있다. 전역 형식 구역 이름은 `C - Global type -`이다. 전역 변수 구역 이름은 `C - global variable -`이다. 포함문 예시는 `INCLUDE 'VF_A @@@@@.. H'`로 인쇄되어 있다. | p.76 PNG 본문 첫 문장과 표 전체 및 표 왼쪽 확대 이미지. |
| p.77 | 기록 없음. | 보완: 인수 구역 이름은 `CD - Argument -`이다. 지역 변수 구역 이름은 `CD - Local variable -`이다. 실행 구역 이름은 `C ==== Execution`이다. 실행 시작에 대응하는 설명은 `Start of execution statement`이다. 실행문 자리에는 `CD - @@@@ @@ -` 주석이 두 번 있다. 실행 종료 구역 이름은 `C - End of executable statement -`이다. 오류 처리 구역 이름은 `C ==== File related error handling`이다. 형식문 구역 이름은 `C ==== Format Statement`이다. 종료 구역 이름은 `C ==== Termination`이다. 종료 처리에 대응하는 설명은 `End processing`이다. | p.77 PNG 표 왼쪽의 구역 이름·실행문 자리표시자와 오른쪽 설명 열. |
| p.78 | 그림 왼쪽의 `VF_A1MAIN` 흐름은 `START`, 처리 상자들, `End` 판단, 반복 경로, `File close`, `STOP`, `END`를 보여 준다. | 보완: 그림 왼쪽의 `VF_A1MAIN` 흐름은 `START`, `Process` 상자들, `End` 판단, 반복 경로, `File close`, `STOP`, `END`를 보여 준다. | p.78 PNG Figure 0-4-5의 왼쪽 처리 상자에 인쇄된 이름. |
| p.78 | 기록 없음. | 보완: 본문은 정상 종료와 비정상 종료를 구분한다. 비정상 종료의 예시는 `such as an input error which can be detected by the program`이다. 이 예시는 프로그램이 감지할 수 있는 입력 오류를 뜻한다. 왼쪽 흐름에는 `Process` 상자가 세 개 있다. 첫 번째 `Process`는 `START` 다음에 있다. 두 번째 `Process`는 `End` 판단 앞에 있다. 세 번째 `Process`는 `End` 판단 아래에 있다. 세 번째 `Process`에서 두 번째 `Process` 앞으로 돌아가는 경로가 있다. `End` 판단의 오른쪽 경로는 `File close`로 이어진다. 각 `Process` 상자에서 오른쪽 `VF_A2ERR`로 점선 화살표가 하나씩 향한다. 두 흐름의 `STOP` 상자는 회색이다. | p.78 PNG 본문 후반의 괄호 안 예시와 Figure 0-4-5의 상자·화살표·음영. |
| p.79 | 기록 없음. | 보완: 본문이 이 전역 데이터 분류의 대상으로 명시한 모델 이름은 `CADMAS-SURF/3D-2F`이다. | p.79 PNG 4.4.1 본문 첫 문장. |
| p.80 | 기록 없음. | 보완: 절 4.4.2의 본문 첫 문장은 `Table 0-4-5`가 공통문에 의한 전역 변수의 상세 설명을 제시한다고 설명한다. | p.80 PNG 절 4.4.2의 본문 첫 문장. |
| p.81 | 절 4.4.2의 표다. | 정정: 앞 쪽에서 이어지는 절 `4.4.2. Detailed explanation of global variables by common`의 표다. 이 쪽에는 절 제목이 다시 인쇄되어 있지 않다. | p.81 PNG 상단에는 표 캡션이 있다. 절 제목은 p.80 PNG 하단에 있다. |
| p.81 | 기록 없음. | 보완: 파일 개요는 `File contains PARAMETER statement`이다. 이 개요는 파일에 `PARAMETER` 문이 들어 있다는 뜻이다. | p.81 PNG 표 첫 행의 파일 개요. |
| p.82 | 절 4.4.2의 표다. | 정정: 앞 쪽에서 이어지는 절 `4.4.2. Detailed explanation of global variables by common`의 표다. 이 쪽에는 절 제목이 다시 인쇄되어 있지 않다. | p.82 PNG 상단에는 표 캡션이 있다. 절 제목은 p.80 PNG 하단에 있다. |
| p.83 | 절 4.4.2의 표다. | 정정: 앞 쪽에서 이어지는 절 `4.4.2. Detailed explanation of global variables by common`의 표다. 이 쪽에는 절 제목이 다시 인쇄되어 있지 않다. | p.83 PNG 상단에는 표 캡션이 있다. 절 제목은 p.80 PNG 하단에 있다. |
| p.84 | 절 4.4.2의 표 두 개가 있다. | 정정: 앞 쪽에서 이어지는 절 `4.4.2. Detailed explanation of global variables by common`의 표 두 개가 있다. 이 쪽에는 절 제목이 다시 인쇄되어 있지 않다. | p.84 PNG 상단에는 표 캡션이 있다. 절 제목은 p.80 PNG 하단에 있다. |
| p.85 | 절 4.4.2의 표다. | 정정: 앞 쪽에서 이어지는 절 `4.4.2. Detailed explanation of global variables by common`의 표다. 이 쪽에는 절 제목이 다시 인쇄되어 있지 않다. | p.85 PNG 상단에는 표 캡션이 있다. 절 제목은 p.80 PNG 하단에 있다. |
| p.86 | 절 4.4.2의 표다. | 정정: 앞 쪽에서 이어지는 절 `4.4.2. Detailed explanation of global variables by common`의 표다. 이 쪽에는 절 제목이 다시 인쇄되어 있지 않다. | p.86 PNG 상단에는 표 캡션이 있다. 절 제목은 p.80 PNG 하단에 있다. |
| p.86 | 기록 없음. | 보완: `ILPARA(3)`의 성분 `(1)` 설명은 `Output section`이다. 이 성분은 출력 단면을 지정한다. | p.86 PNG ILPARA(3) 행의 성분 (1) 설명. |
| p.87 | 기록 없음. | 보완: 아래쪽 표의 파일 개요는 `File related to file number and output control(Integer)`이다. 이 개요는 파일 번호와 출력 제어에 관한 정수 자료를 뜻한다. | p.87 PNG Table 0-4-12의 첫 행. |
| p.89 | 절 4.4.2의 표다. | 정정: 앞 쪽에서 이어지는 절 `4.4.2. Detailed explanation of global variables by common`의 표다. 이 쪽에는 절 제목이 다시 인쇄되어 있지 않다. | p.89 PNG 상단에는 표 캡션이 있다. 절 제목은 p.80 PNG 하단에 있다. |
| p.89 | 기록 없음. | 보완: 표의 파일 개요는 `File related to file number and output control(Integer)`이다. 이 개요는 파일 번호와 출력 제어에 관한 정수 자료를 뜻한다. 이 쪽의 `Variable name`, `Type`, `Variable type` 열은 비어 있다. 이어지는 `ITRPRM`의 이름과 형식은 앞 쪽 p.88에 인쇄되어 있다. | p.89 PNG Table 0-4-13의 첫 행과 비어 있는 왼쪽 세 열. p.88 PNG ITRPRM 행. |

## 원문 표기 확인

- p.77의 `CALL A2ERR`와 p.78의 `VF_A2ERR`를 각각 인쇄대로 유지했다.
- p.78의 정상·비정상 종료 설명에 있는 어색한 연결을 임의로 고치지 않았다.
- p.81의 `ZERO`, `ZEROG`, `PI` 설명은 이미지의 각 행과 일치한다.
- p.83의 `SCMVP` 범위 `0 0 - 1 0`에는 소수점을 보충하지 않았다.
- p.85의 `Debug (Real)` 표에서 두 변수의 형식은 모두 `I*4`이다.
- p.86–89의 표 캡션 분할 번호와 파일 이름 옆 분할 번호는 서로 다르게 인쇄되어 있다.
- p.87의 `IGRARA(6)` 설명에 있는 `list file`을 유지했다.
- p.88의 `ITRTRN(3)` 설명과 선택값은 `ITRTYP`의 설명과 선택값을 반복한다.
- p.88의 `Wave power to obstacles`와 p.89의 `wave force`를 각각 유지했다.
- p.89의 곱셈 표현은 기존 LaTeX와 일치한다.
- p.89–90의 `I 1`, `J 1`, `K 1`, `I 2`, `J 2`, `K 2`에는 아래첨자가 없다.
- p.73–90에는 번호가 붙은 독립된 수학식이 없다.
- p.73–90에는 일본어 문장이 없다.
- p.73–90에는 기본값이나 권장값을 지정하는 문장이 없다.

열지 못한 이미지는 없다.
판독하지 못한 항목은 없다.

정정 7, 보완 11, 일치 3
