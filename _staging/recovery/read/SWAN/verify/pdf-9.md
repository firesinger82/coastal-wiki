# SWAN swanuse.pdf 전수 검증 기록

검증일은 2026-10-13이다.
원문은 `models/SWAN/raw/manuals/pdfs/swanuse.pdf`이다.
쪽 번호는 PDF의 물리 쪽 번호이다.
각 쪽 행의 모든 문장을 지정된 300dpi 쪽 이미지와 대조했다.
이미지는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/swpages/swanuse-NNN.png`에서 열었다.
수식의 첨자·부호·지수·분모를 확인했다.
숫자·단위·기본값과 명령 문법을 확인했다.
조건·부정·불확실성·한정 표현을 확인했다.
각 쪽에 없는 귀속·절 번호·제목·라벨을 확인했다.

다음 수치는 대상 기록의 쪽 행에서 센 값이다.
정정과 보완은 각각 해당 표식이 붙은 쪽 행 수이다.
두 표식이 함께 붙은 행은 p.73과 p.79이다.
이상 없음은 두 표식이 모두 없는 쪽 행 수이다.

| 기록 | 대조한 쪽 행 수 | 정정 행 수 | 보완 행 수 | 이상 없음 행 수 |
|---|---:|---:|---:|---:|
| [p037-054.md](../manuals/pdfs/swanuse.pdf/p037-054.md) | 18 | 15 | 0 | 3 |
| [p073-090.md](../manuals/pdfs/swanuse.pdf/p073-090.md) | 18 | 16 | 2 | 2 |
| 합계 | 36 | 31 | 2 | 5 |

`기록:구간`의 기록 경로는 `_staging/recovery/read/SWAN/manuals/pdfs/swanuse.pdf/`를 기준으로 썼다.
원문 행은 쪽 이미지에서 확인한 인쇄 내용이다.
한 쪽 행의 같은 유형 정정은 아래 표의 한 행에 모았다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| p037-054.md:p.38 (정정) | 쪽 첫머리의 기본 옵션을 이 쪽에 없는 `MODE` 명령명에 귀속했다. | 명령명 귀속을 삭제했다. | p.38 첫 행: `The default option is STATIONARY TWODIMENSIONAL.`. `MODE` 명령명은 없다. |
| p037-054.md:p.40 (정정) | 이 쪽의 도입에 §4.5.1 `Computational grid`를 표시했다. | 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다. | p.40 상단은 `(see command INPGRID).`와 `Default: [alpc] = 0.0.`으로 시작한다. 절 제목은 없다. |
| p037-054.md:p.41 (정정) | 도입에 §4.5.1 `Computational grid`를 표시했다. | 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다. | p.41 상단은 `[dir2] the direction of the left-hand boundary`로 시작한다. 절 제목은 없다. |
| p037-054.md:p.42 (정정) | 도입에 §4.5.1 `Computational grid`를 표시했다. | 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다. | p.42에는 Figure 4.1과 `READgrid COORdinates` 상자가 있다. 절 제목은 없다. |
| p037-054.md:p.43 (정정) | 도입에 §4.5.1 `Computational grid`를 표시했다. | 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다. | p.43 첫 명령 상자는 `READgrid UNSTRUCtured`이다. 절 제목은 없다. |
| p037-054.md:p.45 (정정) | 도입에 §4.5.2 `Input grids and data`를 표시했다. | 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다. | p.45 상단은 `(NONSTATionary [tbeginp] [deltinp] ...)` 문법의 연속이다. 절 제목은 없다. |
| p037-054.md:p.46 (정정) | 도입에 §4.5.2 `Input grids and data`를 표시했다. | 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다. | p.46 첫 문장은 `in case of option BOTTOM only stationary input field is allowed`이다. 절 제목은 없다. |
| p037-054.md:p.47 (정정) | 도입에 §4.5.2 `Input grids and data`를 표시했다. | 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다. | p.47 첫 항목은 `AICE`이다. 절 제목은 없다. |
| p037-054.md:p.48 (정정) | 도입에 §4.5.2 `Input grids and data`를 표시했다.<br>쪽 첫머리에 `REGULAR`와 ‘격자점 수보다 하나 작다’를 귀속했다. | 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다.<br>이 쪽에 없는 `REGULAR`와 ‘하나 작다’를 삭제했다. | p.48 상단은 앞 쪽 문장의 끝부분이다. 절 제목은 없다.<br>p.48 첫 행은 `than the number of grid points in this direction!).`이다. 다음 행은 `In 1D-mode, [myinp] should be 0.`이다. |
| p037-054.md:p.49 (정정) | 도입에 §4.5.2 `Input grids and data`를 표시했다.<br>쪽 첫머리의 `This format`을 `[tbeginp]`에 귀속했다. | 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다.<br>이 쪽에 없는 `[tbeginp]` 귀속을 삭제했다. | p.49 상단은 `This format is installation dependent.`로 시작한다. 절 제목은 없다.<br>p.49 첫 행은 `This format is installation dependent.`이다. `[tbeginp]`는 이 쪽에 없다. |
| p037-054.md:p.50 (정정) | 도입에 §4.5.2 `Input grids and data`를 표시했다. | 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다. | p.50 상단은 `DSS`와 `[nhedf] ([nhedt]) ([nhedvec])` 문법의 연속이다. 절 제목은 없다. |
| p037-054.md:p.51 (정정) | 도입에 §4.5.2 `Input grids and data`를 표시했다.<br>첫 문장을 `WIND`의 직선·곡선 입력 격자 설명으로 확정했다. | 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다.<br>이 쪽에서 보이는 성분·단위·파일 조건만 남겼다. | p.51 상단은 속도 성분 설명의 연속이다. 절 제목은 없다.<br>p.51 첫 행은 `the x- and y-component (ξ- and η-component) (in m/s) are to be read from`이다. 첫머리에 `WIND`와 격자 종류 표제는 없다. |
| p037-054.md:p.52 (정정) | 도입에 §4.5.2 `Input grids and data`를 표시했다.<br>이 쪽에 없는 `[fac]=0.1` 예시를 넣었다. | 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다.<br>이 쪽에서 보이는 문장 끝부분만 기록했다. | p.52 상단은 앞 쪽 문장의 끝부분이다. 절 제목은 없다.<br>p.52 첫 행은 `obtain levels in m.`으로 시작한다. `0.1`은 이 쪽에 없다. |
| p037-054.md:p.53 (정정) | 도입에 §4.5.2 제목과 앞 쪽에서 시작한 lay-out의 귀속을 붙였다. | 절 번호와 제목을 삭제했다. 쪽 첫머리의 lay-out을 그대로 제시했다. | p.53 첫머리에는 lay-out 마지막 두 행이 있다. 절 제목과 lay-out 자체의 표제는 없다. |
| p037-054.md:p.54 (정정) | 도입에 §4.5.2 `Input grids and data`를 표시했다.<br>첫 두 형식 번호에 이 쪽에 없는 `[idfm]` 라벨을 붙였다. | 쪽에 인쇄되지 않은 절 번호와 제목을 삭제했다.<br>이 쪽에 인쇄된 `=6`과 `=8`로 기록했다. | p.54 상단은 `=6: Format (12F6.0)`으로 시작한다. 절 제목은 없다.<br>p.54 첫 두 행은 `=6: Format (12F6.0)`과 `=8: Format (10F8.0)`이다. `[idfm]`는 이 쪽에 없다. |
| p073-090.md:p.73 (정정) | 이 쪽에 없는 장 번호 ‘제4장’을 붙였다. | 인쇄된 머리말 「Description of commands」만 남겼다. | p.73 머리말은 `Description of commands`이다. 장 번호는 인쇄되어 있지 않다. |
| p073-090.md:p.73 (보완) | `CONstant`의 기본 분기 표시와 천수 적용 설명이 빠졌다. | `CONstant` 기본 선택과 천수의 수심 유도 쇄파 조절을 추가했다. | p.73 명령 상자는 `-> CONstant [alpha] [gamma]`를 표시한다. 본문은 `influence depth-induced wave breaking in shallow water`라고 쓴다. |
| p073-090.md:p.75 (정정) | 도입에 이 쪽에 없는 ‘제4장’과 `FRICtion` 귀속을 붙였다.<br>`[D]`를 `RIPPLES`의 퇴적물 지름으로 설명하고 앞 쪽의 단위 m를 가져왔다. | 쪽 첫머리를 앞 명령의 기본값 설명 끝부분으로 기록했다.<br>이 쪽의 기본값만 남겼다. 정의와 단위의 부재를 명시했다. | p.75 머리말은 `Description of commands`이다. 첫 본문 행은 `Default: [D] = 0.0001.`이다.<br>p.75 첫 행 `Default: [D] = 0.0001.` 뒤에 바로 `TRIad` 명령 상자가 나온다. |
| p073-090.md:p.76 (정정) | 쪽 첫머리 관계식을 앞 쪽의 SPB 보정 매개변수 설명에 귀속했다.<br>쪽 끝 문장을 ‘명령 생략 조건’으로 기록했다.<br>도입에 이 쪽에 없는 `TRIad` 명령 라벨을 붙였다. | 이 쪽에 인쇄된 관계식으로만 소개했다.<br>원문의 `is used` 조건과 `will not` 부정을 그대로 기록했다.<br>쪽에 보이는 이중위상·전달계수 설명으로 소개했다. | p.76 첫 행은 `is a function of the local wave number: K = a · k_loc.`이다. 첫머리에 SPB 귀속은 없다.<br>p.76 마지막 행: `If this command is used, SWAN will not`.<br>p.76에는 `BIPHASE`, `TRANSFER`와 `VEGEtation` 표기가 있다. `TRIad` 명령명은 없다. |
| p073-090.md:p.77 (정정) | 도입에 이 쪽에 없는 ‘제4장’을 붙였다.<br>앞 문장을 ‘명령을 사용하지 않으면 식생 효과를 고려하지 않는다’고 완성했다. | 쪽에 인쇄된 식생 설명과 `MUD` 명령으로 소개했다.<br>이 쪽에 보이는 문장 끝부분만 기록했다. | p.77 머리말은 `Description of commands`이다. 장 번호는 없다.<br>p.77 첫 행: `account for vegetation effects.`. 조건절은 이 쪽에 없다. p.76의 실제 조건은 `If this command is used`이다. |
| p073-090.md:p.78 (정정) | 이 쪽에 없는 다음 쪽의 `ignored).`를 인용했다. | 현재 쪽에 보이는 ‘필요하지 않다’와 문장 연속만 기록했다. | p.78 마지막 행은 `The value of [aice] in this command is then not required (it will be`이다. |
| p073-090.md:p.79 (정정) | 도입에 이 쪽에 없는 ‘제4장’과 `SICE` 라벨을 붙였다.<br>쪽 첫머리에 `[aice]`와 공간 변화 자료의 조건을 앞 쪽에서 가져왔다. | 쪽에 보이는 해빙 소산 매개변수와 명령으로 소개했다.<br>현재 쪽의 문장 끝부분만 기록했다. | p.79 머리말은 `Description of commands`이다. 장 번호와 `SICE` 명령명은 없다.<br>p.79 첫 행: `ignored).`. `[aice]`와 그 조건절은 이 쪽에 없다. |
| p073-090.md:p.79 (보완) | 이 쪽에 보이는 저자명 Ardhuin을 기록하지 않았다. | 이 쪽에 인쇄된 저자 표기의 범위를 추가했다. | p.79 마지막 행: `based on the theory of Ardhuin and`. |
| p073-090.md:p.80 (정정) | 쪽 첫머리의 출처를 앞 쪽의 Ardhuin까지 합쳐 완성했다.<br>저면 스펙트럼 계산 조건을 ‘필요한 경우’로 썼다.<br>도입에 이 쪽에 없는 `BRAGg` 명령 라벨을 붙였다. | 이 쪽에 인쇄된 `Herbers (2002).`만 기록했다.<br>원문의 사용자 선택 조건 ‘원하는 경우’를 복원했다.<br>쪽에 보이는 Bragg 산란 설명으로 소개했다. | p.80 첫 행: `Herbers (2002). If this command is not used, SWAN will not account for Bragg scattering.`<br>p.80 `[nreg]`: `for computing the mean depth and, if desired, the bed elevation spectrum`.<br>p.80 본문은 `Bragg scattering`과 `[ibrag]`를 설명한다. `BRAGg` 명령명은 없다. |
| p073-090.md:p.81 (정정) | 도입에 이 쪽에 없는 ‘제4장’과 `BRAGg` 라벨을 붙였다. | 이 쪽에서 확인한 저면 스펙트럼 설명으로 소개했다. | p.81 머리말은 `Description of commands`이다. 첫머리에는 수심 평균과 `FILE` 저면 스펙트럼 설명이 있다. |
| p073-090.md:p.82 (정정) | 이 쪽에서 끝나지 않은 문장을 ‘프로그램의 경계 처리’로 완성했다.<br>도입에 이 쪽에 없는 `OBSTacle` 명령 라벨을 붙였다.<br>1차원 모드 금지문에 이 쪽에 없는 `OBSTacle` 명령명을 붙였다. | 현재 쪽에 보이는 경계 처리 조건만 기록했다.<br>쪽에 보이는 장애물 명령의 구문과 조건으로 소개했다.<br>금지 조건을 현재 쪽의 장애물 명령에 연결했다. | p.82 마지막 문장: `This can only be resolved by a different treatment of the boundaries in the`.<br>p.82 상자는 `REFL`, `FREEboard`, `LINe`의 연속 구문이다. `OBSTacle` 명령명은 없다.<br>p.82 명령 상자 아래: `CANNOT BE USED IN 1D-MODE.` |
| p073-090.md:p.83 (정정) | 도입에 이 쪽에 없는 ‘제4장’과 `OBSTacle` 라벨을 붙였다.<br>이 쪽에 없는 ‘주의 3’ 라벨을 붙였다. 권고의 시간 한정을 빠뜨렸다. | 쪽에 보이는 장애물 조건과 투과 옵션으로 소개했다.<br>라벨을 삭제했다. `Until this time`의 한정을 복원했다. | p.83 머리말은 `Description of commands`이다. 장 번호와 `OBSTacle` 명령 표제는 없다.<br>p.83 첫 문단: `program. Until this time, it is recommended to place obstacles at the inner area of the computational grid, not at or through the boundaries.` |
| p073-090.md:p.84 (정정) | 쪽 첫머리의 `this command`와 `this value`를 `GODA`와 `[hgt]`로 완성했다.<br>도입에 이 쪽에 없는 `OBSTacle` 명령 라벨을 붙였다. | 현재 쪽에 인쇄된 조건문만 기록했다.<br>쪽에 보이는 장애물 옵션 설명으로 소개했다. | p.84 첫 행: `level. If this command is used, this value is required.`. 다음 항목은 `[alpha]`이다.<br>p.84에는 `DANGREMOND`, `REFL`, `FREEBOARD`, `DAM` 표기가 있다. `OBSTacle` 명령명은 없다. |
| p073-090.md:p.85 (정정) | 도입에 이 쪽에 없는 ‘제4장’을 붙였다.<br>앞 쪽의 ‘투과 형상 매개변수’ 정의를 가져왔다. | 인쇄되지 않은 장 번호를 삭제했다.<br>현재 쪽에 보이는 `[gammat]` 기본값만 기록했다. | p.85 머리말은 `Description of commands`이다. 장 번호는 없다.<br>p.85 상단은 `for background information.`과 `Default: [gammat] = 1.`이다. |
| p073-090.md:p.87 (정정) | 이 쪽에 없는 ‘제4장’과 `SETUP` 명령명을 붙였다. | 현재 쪽의 선택 명령 조건문으로 기록했다. | p.87 머리말은 `Description of commands`이다. 첫 문장은 `If this optional command is given, the wave-induced set-up is computed and accounted for in the wave computations`이다. |
| p073-090.md:p.88 (정정) | 도입에 이 쪽에 없는 `DIFFRACtion` 명령 라벨을 붙였다. | 쪽에 보이는 회절 매개변수 설명으로 소개했다. | p.88 첫 항목은 `[idiffr]`이다. `SURFBeat` 상자는 있으나 `DIFFRACtion` 명령명은 없다. |
| p073-090.md:p.89 (정정) | 도입에 이 쪽에 없는 ‘제4장’과 `SURFBeat` 라벨을 붙였다.<br>쪽 첫머리의 평형식에 앞 쪽의 ‘장주기파’ 귀속을 붙였다.<br>이 쪽에 없는 굴절과 회절을 마지막 문장에 넣었다. | 현재 쪽에 보이는 장주기파 계산 설명으로 소개했다.<br>이 쪽의 `energy balance` 표기로만 소개했다.<br>이 쪽에 보이는 위상 결맞음 산란과 간섭까지 기록했다. | p.89 머리말은 `Description of commands`이다. 장 번호와 `SURFBeat` 명령 표제는 없다.<br>p.89 첫 행: `energy balance is solved. This equation is forced by bichromatic wave groups related to all`.<br>p.89 마지막 행은 `In turn, the immediate spatial effects of coherent scattering, interference,`로 끝난다. |
| p073-090.md:p.90 (정정) | 도입에 이 쪽에 없는 `SCAT` 명령 라벨을 붙였다.<br>앞 쪽의 위상 결맞음 산란과 간섭을 이 쪽 첫 문장에 합쳤다. | 쪽에 보이는 준결맞음 모델과 매개변수 설명으로 소개했다.<br>현재 쪽에 보이는 굴절과 회절 및 ‘일으킬 수 있다’의 가능성 표현을 기록했다. | p.90에는 `Chapter 4`, QC 모델 본문과 `[iqcm]` 항목이 있다. `SCAT` 명령명은 없다.<br>p.90 첫 행: `refraction and diffraction can cause large-scale changes in the wave parameters.` |

p037-054.md의 이상 없음 행은 p.37, p.39, p.44이다.
p073-090.md의 이상 없음 행은 p.74, p.86이다.

두 대상 기록의 frontmatter는 변경하지 않았다.
쪽 행의 개수와 순서는 유지했다.
쪽 행 밖의 기존 내용은 변경하지 않았다.
모델은 실행하지 않았다.

정정 31, 보완 2, 이상 없음 5
