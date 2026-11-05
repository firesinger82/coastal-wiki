# CADMAS-SURF3D 영문 매뉴얼 p.1–18 전수 대조

검증일은 2026-11-04다.
검증자는 `codex gpt-6-astra`다.
대상 기록은 [p001-018.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Manual/CADMAS-SURF3D_Manural_English.pdf/p001-018.md)다.
원본 PDF는 `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Manual/CADMAS-SURF3D_Manural_English.pdf`다.

사용자가 지정한 300 dpi PNG의 p.1–18을 모두 이미지 보기 도구로 열었다.
작은 글자·첨자·괄호·범례는 같은 PNG의 해당 부분을 메모리에서 잘라 원래 해상도로 확대 표시했다.
확대용 파일은 저장하지 않았다.
철자 확인에는 지정된 텍스트 추출본을 보조로 사용했다.
판독과 정정의 기준은 PNG 이미지다.

대조한 쪽 수는 18쪽이다.
고친 쪽 수는 12쪽이다.
정정 표식이 있는 쪽 수는 5쪽이다.
보완 표식이 있는 쪽 수는 9쪽이다.
일치 표식이 있는 쪽 수는 6쪽이다.
위 수치는 대상 기록의 쪽 행 끝에 붙인 표식에서 집계했다.
p.5와 p.15는 정정과 보완을 모두 포함한다.
따라서 정정과 보완의 쪽 수에는 이 두 쪽이 중복된다.

이미지 경로의 공통 디렉터리는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/`다.
아래 표의 파일명은 이 디렉터리를 기준으로 한다.

| 쪽 | 직접 연 이미지 | 판정 |
|---|---|---|
| p.1 | `cad-3d-manual-001.png` | 일치 |
| p.2 | `cad-3d-manual-002.png` | 일치 |
| p.3 | `cad-3d-manual-003.png` | 보완 |
| p.4 | `cad-3d-manual-004.png` | 보완 |
| p.5 | `cad-3d-manual-005.png` | 정정·보완 |
| p.6 | `cad-3d-manual-006.png` | 일치 |
| p.7 | `cad-3d-manual-007.png` | 일치 |
| p.8 | `cad-3d-manual-008.png` | 보완 |
| p.9 | `cad-3d-manual-009.png` | 일치 |
| p.10 | `cad-3d-manual-010.png` | 정정 |
| p.11 | `cad-3d-manual-011.png` | 보완 |
| p.12 | `cad-3d-manual-012.png` | 보완 |
| p.13 | `cad-3d-manual-013.png` | 보완 |
| p.14 | `cad-3d-manual-014.png` | 보완 |
| p.15 | `cad-3d-manual-015.png` | 정정·보완 |
| p.16 | `cad-3d-manual-016.png` | 정정 |
| p.17 | `cad-3d-manual-017.png` | 일치 |
| p.18 | `cad-3d-manual-018.png` | 정정 |

## 정정·보완 목록

같은 쪽에서 여러 부분을 바꾼 경우에는 변경 부분마다 행을 나누었다.
이 목록의 행 수를 수정한 쪽 수로 세지 않았다.
수식의 이전·새 표기는 LaTeX 원문이다.

| 쪽 | 이전 | 새 | 근거 |
|---|---|---|---|
| p.3 | 시스템 구성은 단일 프로세서와 다중 프로세서로 구분한다. | 독립 실행판의 원문 이름은 `CADMAS - SURF / 3D`다. 시스템 구성은 단일 프로세서와 다중 프로세서로 구분한다. 본문은 단일 프로세서 구성을 `Figure 0-1-1`로 참조한다. 본문은 다중 프로세서 구성을 `Figure 0-1-2`로 참조한다. 3차원 계산에서 데이터 규모가 커지기 때문에 그래픽 파일을 추가했다고 설명한다. | 보완. p.3 `(2) System configuration`의 첫째·둘째 문단. |
| p.4 | 후자는 `Folder(DataBmp)`의 비트맵 파일(bitmap file)을 만들고 `Viewer`로 이어진다. | 후자는 `Folder (DataBmp)`의 비트맵 파일을 만든다. 비트맵 파일의 그림 안 표기는 `BitMap file`이다. 비트맵 파일은 `Viewer`로 이어진다. | 보완. p.4 Figure 0-1-1 하단 확대 이미지의 `Folder (DataBmp)`와 `BitMap file`. |
| p.5 | `Detail file (data.res00000-XXXXX)` | `Detail file (data. res00000–XXXXX)` | 정정. p.5 Figure 0-1-2 오른쪽 위 상세 입력 파일명 확대 이미지. |
| p.5 | `List file (data.list00000-XXXXX)`, `Graphic file (data.grp00000-XXXXX)`, `Detail file (data.rsl00000-XXXXX)`, `History file (data.tran)` | `List file`(파일명은 `(data. list00000–`까지만 판독), `Graphic file (data. grp00000–XXXXX)`, `Detail file (data. rsl00000–XXXXX)`, `History file (data. tran)` | 정정. p.5 중앙 파일명 확대 이미지. 목록 파일은 `data. list00000–`까지만 식별된다. 다른 파일명은 점 뒤 공백과 범위 기호를 포함한다. |
| p.5 | 목록 파일 표기는 줄바꿈되어 있다. | 목록 파일명은 `data. list00000–` 뒤가 잘려 있다. 그 아래의 작은 글자 흔적은 확대해도 판독할 수 없다. 이 기록은 다른 파일명에서 뒷부분을 추정하여 채우지 않는다. | 정정. p.5 List file 바로 아래 확대 이미지. |
| p.5 | 다중 프로세서의 파일 흐름을 보여 준다. | 다중 프로세서의 파일 흐름을 보여 준다. 위쪽 `Word Processor`의 화살표는 `Matrix Data`, `Input`, `Prosity file`로 향한다. 입력 파일들의 화살표는 중앙 `CADMAS-SURF/3D Analysis`로 향한다. `List file`의 화살표는 아래쪽 `Word Processor`로 향한다. | 보완. p.5 위쪽 입력 작성 상자·중앙 해석 상자·왼쪽 목록 열람 상자. |
| p.5 | 단일 `Graphic file (data.grp)` | 단일 `Graphic file (data. grp)` | 정정. p.5 Graphic conversion 아래 파일명. |
| p.5 | `data0001.bmp, data0002.bmp, …, dataXXXX.bmp` | `data0001. bmp, data0002. bmp, …, dataXXXX. bmp` | 정정. p.5 하단 일본어 상자 확대 이미지의 파일명. |
| p.8 | `2.1. Coordinate system and difference grid method`. | `2.1. Coordinate system and difference grid method`. 장 도입 문단은 CADMAS-SURF/3D-MG의 해석 모델을 소개한다고 설명한다. 소개 대상으로 3차원 비압축성 유체의 기본 방정식, 자유수면 해석 모델, 조파 모델을 든다. | 보완. p.8 Chapter 2 제목 아래의 독립된 도입 문단. |
| p.8 | 원·삼각형으로 스칼라량과 유속의 배치를 표시한다. | 범례의 빈 사각형은 `Cell to target`이다. 범례의 회색 사각형은 `Virtual cell`이다. 범례의 빈 원은 `Scholar to target`이다. 범례의 검은 원은 `Scholar cell`이다. 범례의 빈 삼각형 두 개는 `Velocity to target`이다. 범례의 검은 삼각형 두 개는 `Virtual velocity`이다. 오른쪽을 향한 삼각형은 수평방향 유속 위치를 나타낸다. 위쪽을 향한 삼각형은 수직방향 유속 위치를 나타낸다. | 보완. p.8 Figure 0-2-1 하단 범례 확대 이미지. 원문 철자는 `Scholar`다. |
| p.8 | 오른쪽은 대응하는 `j`, `NJ`를 사용한다. | 오른쪽 가로 첨자는 `1`, `j−1`, `j`, `j+1`, `NJ−1`, `NJ`다. | 보완. p.8 오른쪽 격자 하단 첨자 확대 이미지. |
| p.10 | `\left(2\frac{\partial u}{\partial x}\right)` | `2\left(\frac{\partial u}{\partial x}\right)` | 정정. p.10 식 (2.2)의 점성항 확대 이미지. 계수 2는 소괄호 밖에 인쇄되어 있다. |
| p.10 | `\left(2\frac{\partial v}{\partial y}\right)` | `2\left(\frac{\partial v}{\partial y}\right)` | 정정. p.10 식 (2.3)의 점성항 확대 이미지. 계수 2는 소괄호 밖에 인쇄되어 있다. |
| p.10 | `\left(2\frac{\partial w}{\partial z}\right)` | `2\left(\frac{\partial w}{\partial z}\right)` | 정정. p.10 식 (2.4)의 점성항 확대 이미지. 계수 2는 소괄호 밖에 인쇄되어 있다. |
| p.11 | 2.2의 계속과 `2.3. Free surface analysis model`. | 앞 쪽에서 이어지는 절 `2.2. Basic equations of three-dimensional incompressible fluid`의 내용이다. 이 쪽에는 새 절 제목 `2.3. Free surface analysis model`도 있다. | 보완. p.11 첫 문단은 p.10 마지막 문장의 연속이다. 새 절 2.3의 제목은 이 쪽에 인쇄되어 있다. |
| p.11 | 자유수면 모델은 복잡한 표면 형상을 해석할 수 있는 VOF 방법을 채택한다. | 자유수면 모델은 범용성이 높고 복잡한 표면 형상을 해석할 수 있는 VOF 방법을 채택한다. 본문은 VOF 방법에 참고문헌 표시 `3)`과 `4)`를 붙인다. 본문은 자유수면 모델링 개념도를 `Figure 0-2-3`으로 참조한다. | 보완. p.11 절 2.3 첫 문단. |
| p.12 | 2.3의 계속. | 앞 쪽에서 이어지는 절 `2.3. Free surface analysis model`의 내용이다. 이 쪽에는 절 제목이 다시 인쇄되어 있지 않다. | 보완. p.12 상단은 절 제목 없이 `As shown in Figure 0-2-4`로 시작한다. |
| p.12 | 계면 기울기(inclination of interface)를 고려하는 방법도 선택할 수 있다. | 계면 기울기(inclination of interface)를 고려하는 방법도 선택할 수 있다. 도너·억셉터 방법, 계면 기울기를 고려하는 방법, 표면 방향 결정 방법은 뒤에서 설명한다고 안내한다. | 보완. p.12 본문 마지막 문장. |
| p.12 | 수치 축은 없다. | 두 분할 화살표 위의 글자는 각각 `Division`이다. 왼쪽 도해 아래의 글자는 `VOF method F`다. 오른쪽 도해 아래의 글자는 `Void fraction α`다. 수치 축은 없다. | 보완. p.12 Figure 0-2-4 확대 이미지. |
| p.13 | 마지막 문장은 다음 쪽으로 이어진다. | 마지막 문단은 이 조파 유속을 사용하는 CADMAS-SURF/3D-MG의 조파 모델을 소개하기 시작한다. 이 쪽에 인쇄된 문장은 `In the CADMAS-SURF/3D-MG, as the wave generation model using these wave-generating flow`까지다. 문장은 다음 쪽으로 이어진다. | 보완. p.13 맨 아래 문단. 조파 경계와 조파 소스의 채택이라는 나머지 내용은 p.14 첫 줄에 있다. |
| p.14 | 2.4의 계속. `(2) Wave boundary`, `(3) Wave source`. | 앞 쪽에서 이어지는 절 `2.4. Wave model`의 내용이다. 첫 문장은 앞 쪽에서 소개한 조파 유속 $U(z,t)$를 사용하는 두 모델로 조파 경계와 조파 소스를 채택한다고 설명한다. 이 쪽에는 소제목 `(2) Wave boundary`와 `(3) Wave source`가 인쇄되어 있다. | 보완. p.14 첫 문장 및 두 소제목. |
| p.14 | 원문은 무반사 모델과 결합하는 효과를 `Reflective wave generation` 및 `which can generats reflected waves`라고 표기한다. | 원문은 뒤에서 설명할 무반사 모델과 결합하는 효과를 `Reflective wave generation`(반사파 조파)이라고 표기한다. 같은 문장은 `which can generats reflected waves`(반사파를 생성할 수 있다는 뜻)라고 끝난다. 조파 경계와 조파 소스의 각 설명 문단은 `Figure 0-2-5`를 참조한다. | 보완. p.14 `(2)` 및 `(3)`의 본문. 인쇄된 반사파 표현을 무반사 조파로 바꾸지 않았다. |
| p.15 | 구조물의 반사파와 천수변형(shallow water deformation) 등을 안정적으로 해석할 때 영역 양 끝의 영향을 최소화하는 무반사 모델을 설명한다. | 규칙파뿐 아니라 불규칙파에서도 구조물의 반사파와 천수변형(shallow water deformation) 등을 안정적으로 해석하는 데 긴 시간이 걸린다고 설명한다. 무반사 모델은 해석 영역 양 끝의 영향을 최소화하는 모델로 설명된다. 같은 문장의 `so that it is not artificially set`는 문자 그대로 인위적으로 설정되지 않도록 한다는 뜻이다. 문장 끝의 `where it does not have to be obtained`는 문자 그대로 그것이 얻어질 필요가 없는 곳이라는 뜻이다. | 보완. p.15 절 2.5 첫 문단. 규칙파·불규칙파, 긴 해석 시간, 두 부정 표현. |
| p.15 | 추가 계산 영역이 필요하다. 여러 파형에 적용할 수 있다는 설명은 다음 쪽으로 이어진다. | 추가 계산 영역이 필요하다. 에너지 감쇠대는 여러 파형에 적용할 수 있다고 이 쪽에서 설명한다. 장점에 관한 마지막 문장은 다음 쪽으로 이어진다. Sommerfeld 방사 경계와 에너지 감쇠대의 설명은 각각 `Figure 0-2-6`을 참조한다. | 정정. p.15 마지막 문단. `applicable to various waveforms`는 p.15에 있고 `has an advantage` 뒤의 설명이 p.16으로 이어진다. |
| p.16 | 2.5 `(2) Energy damping zone`의 계속. | 앞 쪽에서 이어지는 절 `2.5. Nonreflective model`의 소절 `(2) Energy damping zone` 내용이다. 이 쪽에는 두 제목이 다시 인쇄되어 있지 않다. | 정정. p.16은 p.15의 마지막 문장에 이어지는 `that a stable calculation result ...`로 시작한다. |
| p.18 | 2.6의 계속, `2.7. Energy equation`, 마지막에 `2.8. Concentration transport equations` 제목이 있다. | 앞 쪽에서 이어지는 절 `2.6. Turbulent flow model`의 내용으로 시작한다. 이 쪽에는 새 절 제목 `2.7. Energy equation`이 있다. 마지막에는 `2.8. Concentration transport equations` 제목이 있다. | 정정. p.18 상단은 식 (2.28)로 시작한다. 절 2.6의 제목은 이 쪽에 다시 인쇄되어 있지 않다. |

## 유지한 내용과 판독 한계

p.1·p.2·p.6·p.7·p.9·p.17은 기존 행의 내용과 이미지가 일치했다.
이 여섯 행에는 일치 표식만 추가했다.
표의 쪽 행 수는 수정 전과 같은 18개다.
기존 frontmatter 항목은 유지했다.
frontmatter에는 `verified_by: codex gpt-6-astra (2026-11-04, 300dpi 이미지 전수 대조)` 한 줄만 추가했다.

번호식 (2.1)–(2.34)를 이미지와 대조했다.
번호식의 수는 식 번호별 묶음으로 세어 34개다.
p.16의 무번호 감쇠계수식 3개도 대조했다.
p.12의 그림 안 값과 p.18의 경험상수도 대조했다.
p.18의 경험상수를 입력 기본값으로 바꾸지 않았다.
p.5의 일본어 `フォルダ(DataBmp)`와 `ビットマップファイル`은 이미지와 일치했다.
기존 한국어 뜻인 폴더와 비트맵 파일을 유지했다.

p.4의 마지막 비트맵 파일명은 `dataXXXX.` 뒤를 판독할 수 없다.
p.5의 목록 파일명은 `data. list00000–` 뒤를 판독할 수 없다.
두 부분은 이미지 확대 후에도 완전한 파일명을 확인할 수 없었다.
원문에서 확인되지 않는 뒷부분은 보충하지 않았다.
원문의 특이한 철자와 문장은 대상 기록의 마지막 절인 “판독 중 확인된 사실”에 남겼다.

열지 못한 이미지는 없다.
이 검증은 지정된 p.1–18의 기록 대조로 한정했다.

정정 5, 보완 9, 일치 6
