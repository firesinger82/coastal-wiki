# CADMAS-SURF3D 영문 매뉴얼 p.109–126 전수 대조

- 검증일: 2026-11-04.
- 검증자: codex gpt-6-astra.
- 원본: `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Manual/CADMAS-SURF3D_Manural_English.pdf`.
- 판독 기록: [p109-126.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Manual/CADMAS-SURF3D_Manural_English.pdf/p109-126.md).
- 대조한 쪽 수: PDF p.109–126의 18쪽이다.
- 고친 쪽 수: 아래 목록의 중복을 제외한 14쪽이다.
- 내용이 일치한 쪽 수: p.109, p.114, p.118, p.119의 4쪽이다.
- 열지 못한 이미지: 없다.

지정된 경로의 `cad-3d-manual-109.png`부터 `cad-3d-manual-126.png`까지 모든 300 dpi PNG를 이미지 보기 도구로 직접 열었다.
본문 문단, 입력문, 변수 설명, 자료형, 기본값, 제한조건, 수식과 인쇄 쪽 번호를 쪽별 기록과 대조했다.
p.115의 계수 문자와 p.119의 기본값은 메모리에서 확대해 다시 보았다.
p.114, p.120, p.125의 작은 기호와 변수명도 메모리에서 확대해 다시 보았다.
확대 과정에서 별도 이미지 파일은 쓰지 않았다.
텍스트 추출본은 p.114, p.120, p.122, p.125의 철자 확인에 사용했다.
이 범위에는 그림이 없다.
이 범위의 표에는 번호와 캡션이 없다.
이 범위의 수식에는 식 번호가 없다.
일본어 `OFF または ON`과 한국어 뜻 “OFF 또는 ON”은 p.122의 기존 기록과 일치했다.

## 정정·보완 목록

아래 근거의 쪽 번호는 지정된 PNG의 PDF 쪽 번호이다.
절의 이어짐만 명확히 한 항목은 보완으로 분류했다.
기존 기록에서 이미 “계속”으로 설명한 항목도 사용자가 지정한 “앞 쪽에서 이어지는 절” 표현으로 명시했다.

| 쪽 | 이전 | 새 | 근거 |
|---|---|---|---|
| p.110 | 「Physical property」 계속이다. | 앞 쪽에서 이어지는 절 「Physical property」의 입력문과 변수 표이다. | p.110은 `MATE I. C. V` 입력문으로 시작한다. 절 제목은 p.109에 있다. 보완. |
| p.111 | 물성 표 계속이며 모든 행의 자료형은 `R*8`이다. | 앞 쪽에서 이어지는 절 「Physical property」의 변수 표임을 명시했다. 자료형 설명은 별도 문장으로 유지했다. | p.111은 `DRDT` 행으로 시작한다. 「Model」과 「■Wave maker」는 이 쪽 중간에서 시작한다. 보완. |
| p.112 | 「Wave maker」 변수 표 계속이다. | 앞 쪽에서 이어지는 절 「Wave maker」의 변수 표이다. | p.112는 `Specified character only`와 방향별 허용 문자열로 시작한다. 절 제목은 p.111에 있다. 보완. |
| p.113 | 「Wave maker」 표의 `Y0` 설명으로 시작했다. | 앞 쪽에서 이어지는 절 「Wave maker」의 변수 표와 주석임을 명시했다. | p.113 상단에는 `Y0` 행과 주석이 있다. 「■ Open boundary condition」은 그 아래에서 시작한다. 보완. |
| p.113 | 개방경계 `{TYPE}`의 자료형·기본값·허용값만 적었다. | 변수 설명 “개방경계의 종류”와 원문 `Type of open boundary`를 추가했다. | p.113 개방경계 표의 `{TYPE}` 설명란. 보완. |
| p.115 | 「Turbulent model」 표 계속이다. | 앞 쪽에서 이어지는 절 「Turbulent model」의 변수 표이다. | p.115는 `AEMIN` 행으로 시작한다. 「Numerical solution」은 이 쪽 중간에서 시작한다. 보완. |
| p.116 | 「Numerical solution」 표 계속이다. | 앞 쪽에서 이어지는 절 「Numerical solution」의 변수 표와 주석이다. | p.116은 `SCMT` 행으로 시작한다. 「Grid coordinate」는 그 아래에서 시작한다. 보완. |
| p.116 | `{COORD}`의 자료형·기본값·허용 문자열만 적었다. | 좌표의 종류라는 설명을 추가했다. `'X'`, `'Y'`, `'Z'`와 x, y, z 좌표의 대응을 추가했다. | p.116 격자좌표 표의 `Type of coordinates`와 각 허용 문자열 설명. 보완. |
| p.117 | 「Grid coordinate」 주석은 `Input must be 1 degree`라고 인쇄되어 있다. | 앞 쪽에서 이어지는 절 「Grid coordinate (Required)」의 주석임을 명시했다. 원문 인용은 유지했다. | p.117은 `Note) Input must be 1 degree`로 시작한다. 절 제목은 p.116에 있다. 보완. |
| p.120 | 「Boundary condition (Required)」 계속이다. | 앞 쪽에서 이어지는 절 「Boundary condition (Required)」의 입력문과 변수 표이다. | p.120은 `B. C. Z` 입력문으로 시작한다. 절 제목은 p.119에 있다. 보완. |
| p.121 | 경계조건 종류와 경계값 표 계속이다. | 앞 쪽에서 이어지는 절 「Boundary condition (Required)」의 경계조건 종류와 경계값 표이다. | p.121 상단의 `Rough surface : VP LOG-KS [KS]`는 p.120의 유속·압력 경계조건 목록에서 이어진다. 보완. |
| p.122 | 경계값 표 계속이다. | 앞 쪽에서 이어지는 절 「Boundary condition (Required)」의 경계값 표와 주석이다. | p.122는 `BF` 행으로 시작한다. 「File control」은 그 아래에서 시작한다. 보완. |
| p.122 | 유속에 대수법칙 “또는” 완전 거친 면을 지정한 면이라고 적었다. | 원문의 `and`를 “과”로 보존했다. 실제 입력 처리 의미를 확인하지 않았음을 끝 절에 적었다. | p.122 본문: `the logarithmic law and the complete rough surface`. 정정. |
| p.122 | `inflow other than the specified flux etc.`를 원문으로만 인용했다. | “지정된 플럭스 등 이외의 유입”이라는 한국어 뜻을 추가했다. | p.122의 `[+ A]` 설명 괄호. 보완. |
| p.122 | `FLAG`의 자료형·기본값·제한만 적었다. | 재시작 시 지형자료를 사용할지 선택하는 변수라는 설명을 추가했다. | p.122 표의 `Selection to use topographical data at restart`. 보완. |
| p.123 | 재시작 지형자료 설정의 주석 계속이다. | 앞 쪽에서 이어지는 절 「Setting of reading topographical data at restart」의 주석이다. | p.123 상단의 외부 파일 지정 및 헤더 읽기 횟수 설명은 p.122의 해당 절에서 이어진다. 보완. |
| p.124 | 「List file output control data」 표 계속이다. | 앞 쪽에서 이어지는 절 「List file output control data」의 변수 표와 주석이다. | p.124는 `TEND` 행으로 시작한다. 절 제목은 p.123에 있다. 보완. |
| p.125 | 목록 파일 주석 계속이다. | 앞 쪽에서 이어지는 절 「List file output control data」의 주석이다. | p.125 상단에는 `IJKC`, `IJKG` 및 기본 미출력 설명이 있다. 「■Graphic file output control data」는 그 아래에서 시작한다. 보완. |
| p.126 | 그래픽 파일 주석 계속이다. | 앞 쪽에서 이어지는 절 「Graphic file output control data」의 주석이다. | p.126 상단에는 최소 셀 영역, 인덱스 해석, 와도 출력 주석이 있다. 「■Detailed file output control data」는 그 아래에서 시작한다. 보완. |

## 일치한 쪽

| 쪽 | 대조 결과 |
|---|---|
| p.109 | 시간 제어 입력문, 변수 표, 주석 세 문장과 물성 입력문이 일치했다. `DTMAX` 기본값 `1. 0D0/ZERO`를 유지했다. |
| p.114 | 감쇠 영역 입력문, 변수 표, 주석 세 문장과 난류모형 입력문이 일치했다. `AKMIN` 행도 일치했다. |
| p.118 | 공극률 외부 파일 설명의 두 문장과 모든 입력문이 일치했다. 소제목과 입력 인수 순서도 일치했다. |
| p.119 | 저항계수 입력문, 공극률 변수 표, 주석, 물 비율식과 경계조건 입력문이 일치했다. `PL` 기본값 `1 0 D - 4`에는 소수점이 없다. |

p.120의 `IG2`는 확대 이미지에서 정상적으로 확인했다.
p.114의 `[PZ]` 뒤에는 별도 기호가 없었다.
p.114의 `PXY` 기본값 뒤에도 추가 `-`는 없었다.
진행 보고에서 이 부분을 누락 또는 추가 기호로 판단했던 내용은 확대 확인으로 철회했다.
해당 판단은 판독 기록에 반영하지 않았다.

기존 쪽별 표의 행 수 18개를 유지했다.
기존 frontmatter에는 요청된 `verified_by` 한 줄만 추가했다.
쓰기 대상은 판독 기록과 이 검증 기록이다.
Git 명령은 실행하지 않았다.
모델 실행과 코드 동작은 검증하지 않았다.

아래 총계는 쪽 행에 붙인 표지의 개수이다.
p.122는 정정과 보완 양쪽에 포함된다.
보완 14쪽 중 p.122를 제외한 13쪽은 보완만 수행했다.

정정 1, 보완 14, 일치 4
