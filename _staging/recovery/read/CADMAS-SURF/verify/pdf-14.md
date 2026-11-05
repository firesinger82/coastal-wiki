# CADMAS-2F_Manural_English.pdf p.37–54 전수 대조

검증일은 2026-11-04다.
검증자는 codex gpt-6-astra다.
대상 기록은 [p037-054.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Manual/CADMAS-2F_Manural_English.pdf/p037-054.md)다.
원본은 `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Manual/CADMAS-2F_Manural_English.pdf`다.

사용자가 지정한 300 dpi PNG를 p.37부터 p.54까지 각각 직접 열었다.
대조한 쪽 수는 범위의 쪽 행에서 센 18쪽이다.
내용을 고친 쪽 수는 정정·보완 표시가 있는 쪽 행의 합집합에서 센 11쪽이다.
정정 표시는 p.44와 p.45의 2쪽에 붙였다.
보완 표시는 p.37, p.40, p.41, p.42, p.43, p.44, p.46, p.48, p.50, p.51의 10쪽에 붙였다.
p.44는 정정과 보완에 모두 포함된다.
일치 표시는 p.38, p.39, p.47, p.49, p.52, p.53, p.54의 7쪽에 붙였다.
마지막 줄의 수치는 각 표시가 붙은 쪽 행 수다.

본문의 문단, 식의 첨자·부호·번호, 그림 캡션과 내부 표기, 도표의 조건과 음영을 대조했다.
p.37–40, p.44–47, p.49, p.51–54의 작은 수식·문구는 원본 PNG의 해당 영역을 확대해서 확인했다.
확대 영역은 메모리에서만 만들었다.
철자 확인에는 지정된 텍스트 추출본을 참고했다.
이미지와 추출본을 구별해서 판단했다.
이 범위에는 입력 키워드·파일명·기본값을 나열하는 입력 설정 표가 없다.
이 범위의 수치 조건은 NF, ISW, 패턴 분류, H 값 등의 본문·수식·도표에 있다.

## 정정·보완 목록

근거의 p.N은 PDF 쪽 번호다.
각 행의 새 내용 앞에 변경 유형을 표시했다.

| p.N | 이전 | 새 | 근거 |
|---|---|---|---|
| p.37 | §3.3.6 `Poisson equation of the potential function`은 포텐셜 함수(potential function)의 푸아송 방정식(Poisson equation)을 이산화한다. | 보완. §3.3.6 `Poisson equation of the potential function`은 식 (3.18)에 제시된 포텐셜 함수(potential function)의 푸아송 방정식(Poisson equation)에서 바깥쪽 미분을 이산화한다. | p.37 §3.3.6 첫 문단의 `outside derivative`와 식 (3.18) 참조. |
| p.40 | 누락. | 보완. 원문은 표면 방향 결정 방법을 먼저 설명한다고 안내한다. 이후 도너·억셉터 방법과 경계면 기울기를 고려하는 방법으로 이류방정식을 이산화한다고 안내한다. 마지막 문단은 이 쪽에서 x축과 y축에 수직인 표면 방향까지 열거한다. z축에 수직인 방향은 다음 쪽 첫 문장에서 이어진다. | p.40 §3.3.8 둘째 문단의 마지막 문장과 쪽 끝의 미완 문장. |
| p.41 | 누락. | 보완. 첫 문장의 `or perpendicular to the z axis). The flag NF is defined as`는 앞 쪽의 표면 방향 설명을 마무리한다. 이어지는 본문은 표시자 `NF`에 따른 셀 분류를 그림으로 제시한다고 설명한다. 왼쪽 격자 그림의 표기는 `Gas cell`이다. 오른쪽 격자 그림의 표기는 `Fluid cell`이다. | p.41 첫 문장, NF 목록 뒤 문장, 두 격자 그림 안의 표기. |
| p.42 | 누락. | 보완. 셀을 유체 셀·기체 셀·표면 셀로 분류할 때 자유수면의 경계조건을 처리해야 한다. 왼쪽 격자 그림의 표기는 `Gas cell`이다. 오른쪽 격자 그림의 표기는 `Fluid cell`이다. 마지막 문장은 `However, in the example shown in`에서 끊긴다. 그 문장의 나머지는 다음 쪽으로 이어진다. | p.42 첫 본문 문단의 첫 문장, 두 격자 그림, 마지막 두 줄. |
| p.43 | 누락. | 보완. 왼쪽 격자 그림의 표기는 `Gas cell`이다. 오른쪽 격자 그림의 표기는 `Fluid cell`이다. 두 번째 ① 뒤에는 `② If Fluid Cell - Surface Cell - Gas Cell is satisfied, assume that there is a fluid in the direction where the value of the surrounding F is large.`가 인쇄되어 있다. 이 항목은 해당 셀 배열을 만족할 때 주변 F 값이 큰 방향에 유체가 있다고 가정하라는 뜻이다. | p.43 격자 그림의 표기와 입체 셀 그림 바로 위의 ② 문장. |
| p.44 | \gamma_{v i,j,k} | 정정. \gamma_{v.i,j,k} | p.44 식 (3.95) 분모의 아래첨자를 300 dpi 원본 크기로 확대하면 v 뒤에 점이 보인다. |
| p.44 | 누락. | 보완. 왼쪽 격자 그림의 표기는 `Gas cell`이다. 오른쪽 격자 그림의 표기는 `Fluid cell`이다. 본문은 도너·억셉터 방법의 개념을 `Figure 0-3-4`에 제시한다고 설명한다. 식 (3.95)의 분모 아래첨자에는 v 뒤에 점이 인쇄되어 있다. | p.44 위쪽 격자 그림, `(2) Donor acceptor method` 첫 문단, 식 (3.95). |
| p.45 | \(F_{AD}\)의 두 조건을 \(\begin{cases}\cdots\end{cases}\)로 묶었다. | 정정. 두 조건을 \(\left(\begin{aligned}\cdots\end{aligned}\right.\)로 묶었다. 원문은 왼쪽 소괄호를 사용한다. | p.45 F_AD 정의의 왼쪽 구분 기호는 중괄호가 아니라 소괄호다. |
| p.46 | 누락. | 보완. 위 그림의 경계면 표기는 `Interface considering advection`이다. 반대 방향의 두 화살표 사이에는 `Flow direction`이 있다. 아래 도표의 왼쪽 열 제목은 `The surface is perpendicular to the interface`다. 오른쪽 두 열의 공통 제목은 `The surface is horizontal to the interface`다. `Surface shape` 행의 세 그림은 모두 왼쪽 셀을 `D`로 표시한다. 세 그림은 모두 오른쪽 셀을 `A`로 표시한다. 세 그림의 유동 화살표는 모두 오른쪽을 향한다. 왼쪽 열의 유체 영역은 D 셀의 아래쪽을 차지한다. 가운데 열의 유체 영역은 D 셀의 오른쪽 일부와 A 셀 전체를 차지한다. 오른쪽 열의 유체 영역은 D 셀의 왼쪽 일부를 차지한다. `Transfer flow rate` 행의 세 사각형은 왼쪽부터 아래쪽 일부만 회색인 경우, 전체가 회색인 경우, 전체가 흰색인 경우를 보여 준다. | p.46 위 그림의 두 설명 표기와 아래 도표의 열 제목·셀 이름·화살표·음영. |
| p.48 | 누락. | 보완. 기존 도너·억셉터 방법에 대한 본문 참조는 `Figure 0-3-5(b)`다. 경계면 기울기를 고려하는 방법에 대한 본문 참조는 `Figure 0-3-5(c)`다. 계산 절차의 원문 항목 이름은 차례로 `① Calculation of normal vector`, `② Classification of interface pattern`, `③ Determination of interface`, `④ Calculation of advection amount`다. | p.48 첫 설명 문단의 두 그림 참조와 계산 절차의 네 항목 이름. |
| p.50 | 누락. | 보완. `Figure 0-3-6`의 왼쪽 그림은 중심의 위·아래·왼쪽·오른쪽 검은 점에서 중심 흰 점으로 향하는 회색 화살표를 보여 준다. 오른쪽 그림은 주변 검은 점에서 네 격자점으로 향하는 회색 화살표를 보여 준다. 오른쪽 그림은 네 격자점에서 중심 흰 점으로 향하는 검은 화살표를 보여 준다. 두 그림의 굵은 법선 화살표는 오른쪽 위를 향한다. `Figure 0-3-8`의 음영 영역은 왼쪽 위 그림에서는 왼쪽 아래에 놓인다. 오른쪽 위 그림의 음영 영역은 오른쪽 아래에 놓인다. 왼쪽 아래 그림의 음영 영역은 왼쪽 위에 놓인다. 오른쪽 아래 그림의 음영 영역은 오른쪽 위에 놓인다. | p.50 Figure 0-3-6의 점·화살표와 Figure 0-3-8의 네 음영 영역. |
| p.51 | 누락. | 보완. 본문의 격자 간격은 소문자 \(c\)를 사용한다. `Figure 0-3-9` 안의 격자 간격 표기는 대문자 \(C\)를 사용한 \(\Delta C_1\), \(\Delta C_2\)다. `Figure 0-3-10(a)`의 셀 내부는 전체가 빗금으로 채워져 있다. `(b)`의 빗금 영역은 수직 경계면의 왼쪽이다. `(c)`의 빗금 영역은 수평 경계면의 아래쪽이다. 세 그림에는 좌우로 향하는 이류 화살표가 있다. | p.51 Figure 0-3-9의 대문자 C 표기와 Figure 0-3-10의 세 도해. |

## 이어지는 절의 표시

p.38–39, p.41–43, p.45–48, p.51–54의 절 번호 앞에 `앞 쪽에서 이어지는 절`을 명시했다.
p.48의 실제 새 항목 제목은 `(3) Method considering inclination of interface`로 구분했다.
기존 기록이 이미 이어지는 내용으로 설명한 부분의 문구 정리는 내용 정정·보완 수에 추가하지 않았다.
일치 표시가 있는 행에도 이 문구 정리가 포함될 수 있다.

## 원문 인쇄를 유지한 항목

p.37 식 (3.69)의 제곱근 앞 속도는 기존 기록의 \(v_{i,j,k}\)와 일치한다.
p.38 식 (3.79)의 \(A^D\) 아래첨자에는 추가 점이 있다.
p.38 식 (3.81)–(3.84)는 \(\Delta z_z\)를 쓴다.
p.39 식 (3.90)의 두 번째 분모는 \(\Delta y_k\)다.
p.43은 첫 번째 방향 결정 항목 ①을 반복한다.
p.45의 첫 문장에는 `B`가 추가로 인쇄되어 있다.
p.46의 세 열은 모두 `Let suffix AD be D`를 쓴다.
p.47의 두 번째 항 설명은 `Maximum amount of water that can be`에서 끝난다.
p.49 본문은 `Figure III-3-6`을 참조한다.
p.50의 해당 그림 번호는 `Figure 0-3-6`이다.
p.50의 부분 캡션은 `(a)Cell centererd`다.
p.51 본문의 상수 설명은 `Figure 0-3-8`을 참조한다.
p.51의 해당 직선 그림 번호는 `Figure 0-3-9`다.
p.52는 `P1-1` 제목을 두 번 쓴다.
p.52의 두 번째 `P1-1` 항목은 `P1-3` 조건을 설명한다.
p.52의 일본어 `P1-2` 문장과 한국어 뜻은 기존 기록과 일치한다.
p.52의 `エラー! 参照元が見つかりません。`와 한국어 뜻은 기존 기록과 일치한다.
p.53 식 (3.101)의 첫 통분 행은 \(2n_1\eta_2\)를 분모로 쓴다.
p.54의 계수식은 가로 분수선 대신 `/2n₁n₂`를 쓴다.
p.54의 일본어 문장과 한국어 뜻은 기존 기록과 일치한다.
새로 확인한 p.44의 아래첨자 점과 p.45의 왼쪽 소괄호는 기록 끝의 “판독 중 확인된 사실”에도 추가했다.
p.51의 본문과 그림 사이의 c/C 표기 차이도 같은 절에 추가했다.

## 형식 및 이미지 확인

쪽 표의 데이터 행은 수정 전후 모두 18행이다.
p.37부터 p.54까지 각 쪽은 한 행을 유지한다.
기존 frontmatter의 값은 유지했다.
frontmatter에는 `verified_by: codex gpt-6-astra (2026-11-04, 300dpi 이미지 전수 대조)` 한 줄만 추가했다.
열지 못한 이미지는 없다.
이미지에서 끝내 판독하지 못한 항목은 없다.
수정 대상은 지정된 판독 기록과 이 검증 보고서다.

정정 2, 보완 10, 일치 7
