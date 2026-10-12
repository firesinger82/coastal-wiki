# SWAN swanuse.pdf p.1–36 전수 검증

검증일은 2026-10-13이다.
원문은 두 기록의 frontmatter `file:`이 지정한 `models/SWAN/raw/manuals/pdfs/swanuse.pdf`이다.
대조 단위는 기록의 쪽 행이다.
대상 쪽 행마다 지정된 300 dpi 쪽 이미지를 열어 대조했다.
이미지 경로는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/swpages/swanuse-NNN.png`이다.
대조한 이미지 번호는 `001`부터 `036`까지다.

수식·숫자·단위·기본값·명령 구문을 이미지와 대조했다.
조건·부정·불확실성 표현의 의미를 대조했다.
절 번호·제목·귀속 표현의 해당 쪽 근거를 확인했다.
확인한 오류와 누락은 해당 쪽 행에서 고쳤다.
두 기록의 frontmatter와 쪽 행 순서는 유지했다.
쪽 행 밖의 내용은 유지했다.

정정과 보완은 해당 종류의 수정이 있는 쪽 행을 각각 1회 집계했다.
두 종류가 모두 있는 행은 정정과 보완에 각각 포함했다.
이상 없음은 수정하지 않은 쪽 행이다.

| 기록 | 대조 구간 | 대조한 쪽 행 수 | 정정 행 | 보완 행 | 정정·보완 동시 행 | 이상 없음 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| [p001-018.md](../manuals/pdfs/swanuse.pdf/p001-018.md) | p.1–18 | 18 | 7 | 6 | 5 | 10 |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md) | p.19–36 | 18 | 14 | 10 | 9 | 3 |
| 합계 | p.1–36 | 36 | 21 | 16 | 14 | 13 |

`p001-018.md`에서 이상 없음으로 확인한 행은 p.1–10이다.
`p019-036.md`에서 이상 없음으로 확인한 행은 p.27·p.28·p.31이다.

`원문 행` 열에는 해당 쪽 이미지의 근거 문구를 인용했다.
PDF 쪽 번호와 인쇄 쪽 번호를 병기했다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
| --- | --- | --- | --- |
| [p001-018.md](../manuals/pdfs/swanuse.pdf/p001-018.md):p.11 (보완) | 비구조 격자의 격자점 분포 유연성을 생략했다. 국부 격자 세분화의 설명만 기록했다. | 구조 격자보다 높은 격자점 분포 유연성을 보충했다. 공간 규모가 흔히 다양하다는 한정을 보충했다. 먼바다의 격자 조정 부담 없이 연안을 세분화한다는 조건을 보충했다. | PDF p.11, 인쇄 p.3: “the level of flexibility with respect to the grid point distribution”; “Often, the characteristic spatial scales”; “without incurring overhead associated with grid adaptation at some distance offshore.” |
| [p001-018.md](../manuals/pdfs/swanuse.pdf/p001-018.md):p.12 (정정) | 쪽 첫머리를 ‘2.1 Introduction의 계속’으로 표기했다. | 쪽에 인쇄되지 않은 절 번호·제목을 삭제했다. 첫 문장이 앞쪽에서 이어진다고 명시했다. | PDF p.12, 인쇄 p.4: 첫 행은 “repeated on ever decreasing scales”로 시작한다. 이 쪽의 절 제목은 “2.2 Limitations”이다. |
| [p001-018.md](../manuals/pdfs/swanuse.pdf/p001-018.md):p.12 (보완) | 비구조 격자의 생성 노력과 격자점 수 비교를 생략했다. 2D 근사의 적용 범위는 다음 쪽에 이어진다고만 기록했다. | 비구조 격자의 해상도 조정이 쉽다는 설명을 보충했다. 격자 생성 노력과 적은 격자점으로 얻는 상대적 정확도를 보충했다. 이 쪽에 인쇄된 열린 해안만의 적용 조건을 보충했다. | PDF p.12, 인쇄 p.4: “the modest effort needed to generate grids”; “with a much fewer grid points than with regular grids”; “can only be applied to open coast (unlimited supply” |
| [p001-018.md](../manuals/pdfs/swanuse.pdf/p001-018.md):p.13 (정정) | 인쇄되지 않은 ‘2.2 Limitations’를 표기했다. p.12의 ‘2D’, ‘open coast’, ‘only’, ‘unlimited supply’를 p.13의 완결된 주장으로 기록했다. | 인쇄되지 않은 절 표기를 삭제했다. 첫 문장에 남아 있는 물 공급과 예시를 기록했다. 흐름 효과를 항상 무시한다는 문구의 위치를 첫 문단으로 한정했다. | PDF p.13, 인쇄 p.5: “of water from outside the domain, e.g. nearshore coasts and estuaries)”; “The effects of wave-induced currents are always ignored.” |
| [p001-018.md](../manuals/pdfs/swanuse.pdf/p001-018.md):p.13 (보완) | 규모의 유연성을 제공한 이유만 기록했다. | 풍파 표면 중력파에 해당하는 모든 규모라는 적용 한정을 보충했다. 연안 적용을 위한 설계라는 설명을 보충했다. | PDF p.13, 인쇄 p.5: “any scale relevant for wind generated surface gravity waves”; “specifically designed for coastal applications that should actually not require such flexibility in scale.” |
| [p001-018.md](../manuals/pdfs/swanuse.pdf/p001-018.md):p.14 (정정) | 인쇄되지 않은 2.3 절 표기를 붙였다. 굴절 오차 허용 조건의 ‘only’와 스펙트럼 전파 수렴 설명의 ‘only’를 드러내지 않았다. | 첫머리의 실제 문구를 기록했다. 무시 가능한 국부 효과에만 그칠 때라는 조건을 복원했다. 수렴 실패 가능성 설명을 흐름 유발 굴절과 주파수 이동으로 한정했다. | PDF p.14, 인쇄 p.6: “Examples are:”; “may be acceptable when refraction has only local effects that can be ignored”; “but only current-induced refraction and frequency shift” |
| [p001-018.md](../manuals/pdfs/swanuse.pdf/p001-018.md):p.14 (보완) | 공간 전파 반복의 문제가 다른 제3세대 파랑 모델에도 공통된다는 설명을 생략했다. | 원문이 WAM·WAVEWATCH III·SWAN 등 모든 제3세대 파랑 모델의 공통 문제로 설명한다는 사실을 보충했다. | PDF p.14, 인쇄 p.6, ad 1: “This is a common problem for all third-generation wave models (such as WAM, WAVEWATCH III and also SWAN).” |
| [p001-018.md](../manuals/pdfs/swanuse.pdf/p001-018.md):p.15 (정정) | 인쇄되지 않은 ‘2.3’을 붙였다. 이 쪽의 Watt에 다음 쪽의 ‘(W)’를 붙였다. 해상도 조건을 ‘two or three의 배수’로 기록했다. | 실제 첫머리인 ‘ad 3’을 기록했다. Watt의 기호가 이 쪽에는 없음을 명시했다. 해상도 조건을 두 배 또는 세 배보다 크게 달라지지 않아야 한다는 뜻으로 고쳤다. | PDF p.15, 인쇄 p.7: “ad 3”; “should not differ more than a factor two or three”; 마지막 행은 “such as Newton (N) and Watt”로 끝난다. |
| [p001-018.md](../manuals/pdfs/swanuse.pdf/p001-018.md):p.15 (보완) | 근본적 한계의 전형성에 대한 불확실성을 생략했다. 심해 경계 위치 조건의 목적을 생략했다. | 제3세대 파랑 모델에 전형적일 수도 있고 아닐 수도 있다는 표현을 보충했다. 모델 사이의 지나친 불연속을 피한다는 목적을 보충했다. | PDF p.15, 인쇄 p.7: “which may or may not be typical for third-generation wave models”; “to avoid too large discontinuities between the two models” |
| [p001-018.md](../manuals/pdfs/swanuse.pdf/p001-018.md):p.16 (정정) | 인쇄되지 않은 ‘2.5 Units and coordinate systems’를 쪽 첫머리에 붙였다. | 절 표기를 삭제했다. 실제 첫머리인 ‘(W).’가 앞쪽에서 이어진다고 기록했다. | PDF p.16, 인쇄 p.8: 첫 행은 “(W). Consequently, the wave height and water depth are in m”으로 시작한다. 절 제목은 없다. |
| [p001-018.md](../manuals/pdfs/swanuse.pdf/p001-018.md):p.16 (보완) | 항해 방식의 정의만 기록했다. | 그 밖의 항해 방식 관례도 있다는 원문의 한정을 보충했다. | PDF p.16, 인쇄 p.8: “a nautical convention (there are more such conventions)” |
| [p001-018.md](../manuals/pdfs/swanuse.pdf/p001-018.md):p.17 (정정) | 마지막 문장을 구면좌표 사용 권고로 설명했다. | 이 쪽에 보이는 마지막 문장 조각을 그대로 기록했다. | PDF p.17, 인쇄 p.9: 마지막 문장은 “Since, the computational grids of WAM and WAVEWATCH”에서 끝난다. 구면좌표와 권고는 이 쪽에 인쇄되지 않았다. |
| [p001-018.md](../manuals/pdfs/swanuse.pdf/p001-018.md):p.18 (정정) | 인쇄되지 않은 ‘2.6.1 Introduction’을 붙였다. 첫 문장의 주어를 앞쪽에서 가져와 완결된 이유로 기록했다. | 인쇄되지 않은 절 표기를 삭제했다. 첫 문장의 실제 시작 부분을 명시했다. 이 쪽에 보이는 중첩 계산의 구면좌표 권고는 유지했다. | PDF p.18, 인쇄 p.10: “III are in spherical coordinates, it is recommended to use spherical coordinates in a nested SWAN when nesting in WAM or WAVEWATCH III.” |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.19 (정정) | 쪽에 없는 장 번호를 붙였다. 앞쪽의 ‘It is best to’를 이 쪽의 완결된 권고로 기록했다. 능선의 중요성을 조건 없이 서술했다. | 장 번호를 삭제했다. 첫 문장이 앞쪽에서 이어지는 내용임을 명시했다. 능선 설명의 ‘이러한 경우’ 조건을 복원했다. | PDF p.19, 인쇄 p.11: “make an input grid so large that it completely covers the computational grid.”; “In such cases the ridges are vitally important” |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.19 (보완) | 공간 해상도 설명의 대상 목록을 생략했다. 결과가 불안정해 보일 수 있다는 표현을 생략했다. | 해상해야 하는 입력 대상 목록을 보충했다. 결과의 겉보기 불안정 가능성을 보충했다. | PDF p.19, 인쇄 p.11: “bathymetry, currents, bottom friction, vegetation, mud, ice and wind”; “the results may appear to be unstable” |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.20 (정정) | 마지막 문장에 유의파고 차이와 경고를 귀속했다. | 해당 쪽에 인쇄된 마지막 문장 조각만 기록했다. | PDF p.20, 인쇄 p.12: 마지막 문장은 “The user is informed by means of”에서 끝난다. 유의파고와 경고는 이 쪽에 인쇄되지 않았다. |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.20 (보완) | 다른 모델의 경계 결과를 쓰면 오차가 더 허용 가능할 수도 있다고만 기록했다. | 그 경우 경계를 관심 영역에 더 가까이 둘 수도 있다는 대안을 보충했다. | PDF p.20, 인쇄 p.12: “or the boundaries are permitted to be closer to the area of interest” |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.21 (정정) | 인쇄되지 않은 ‘§2.6.3’을 붙였다. ‘wave field’를 파장으로 기록했다. | 절 번호가 이 쪽에는 없음을 명시했다. ‘wave field’를 파랑장으로 고쳤다. | PDF p.21, 인쇄 p.13: “resolve relevant details of the wave field.” 이 쪽에 2.6.3 절 표기는 없다. |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.22 (정정) | 인쇄되지 않은 ‘§2.6.3’을 붙였다. 쪽 첫 문장의 대상을 앞쪽에서 가져왔다. 시간 변화 대상인 ‘wave field’를 두 곳에서 파장으로 기록했다. | 절 표기를 삭제했다. 첫 문장의 실제 조각을 기록했다. 두 ‘wave field’를 모두 파랑장으로 고쳤다. | PDF p.22, 인쇄 p.14: “it is so defined by the user.”; “time variations of computed wave field itself”; “large variations in the wave field.” |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.23 (정정) | 인쇄되지 않은 ‘§2.6.3’을 붙였다. 첫 문장 조각에 앞쪽의 초기조건 설명을 붙였다. | 절 표기를 삭제했다. 첫 문장의 실제 조각만 기록했다. | PDF p.23, 인쇄 p.15: “the local wind direction.” 이 쪽에는 절 제목이 없다. |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.23 (보완) | 최고 예측 주파수의 의미를 생략했다. | SWAN이 명시적으로 계산하는 최고 주파수라는 정의를 보충했다. | PDF p.23, 인쇄 p.15: “a highest prognostic frequency (that is explicitly computed by SWAN)” |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.24 (정정) | 인쇄되지 않은 ‘§2.6.3’을 붙였다. 앞쪽 조건과 이 쪽 결과의 경계가 드러나지 않았다. ‘may often’의 가능성을 생략했다. 각도 단위를 Δθ의 위 첨자로 설명했다. | 절 표기를 삭제했다. 이 쪽의 조건 조각과 결과를 구분했다. ‘흔히 해당할 수 있다’로 가능성을 복원했다. 위 첨자 o가 해상도 값에 붙는다고 고쳤다. | PDF p.24, 인쇄 p.16: “of energy), then”; “This may often be the case”; 표의 “Δθ = 15ᵒ − 10ᵒ”, “Δθ = 5ᵒ − 2ᵒ”. |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.24 (보완) | 해상도 선택과 안정성의 관계를 생략했다. 제한기의 국부적 목적과 다른 영역의 해 개선을 생략했다. | 해상도와 무관한 안정성이라는 원문 설명을 보충했다. 제한기의 국부 적용 목적 문구와 다른 영역의 해 개선을 보충했다. | PDF p.24, 인쇄 p.16: “SWAN will be stable, whatever resolution you choose”; “locally in geographic space for cosmetic reasons”; “thus improve the solution there.” |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.25 (정정) | 인쇄되지 않은 ‘§2.6.3’을 첫 문단에 붙였다. ‘wave field’를 파장으로 기록했다. | 해당 절 번호를 삭제했다. 에너지 가감 대상을 파랑장으로 고쳤다. | PDF p.25, 인쇄 p.17: “add or withdraw wave energy to or from the wave field.” 실제 절 제목은 2.6.4와 2.7이다. |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.25 (보완) | 1·2·3세대 실행 모드가 구분하는 수준을 생략했다. | 이 모드들이 매개변수화 수준을 나타낸다는 설명을 보충했다. | PDF p.25, 인쇄 p.17: “SWAN can run in several modes, indicating the level of parameterization.” |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.26 (정정) | 쪽 첫머리에 ‘§2.7 계속’을 붙였다. | 절 번호와 절 제목이 인쇄되지 않았음을 명시했다. | PDF p.26, 인쇄 p.18: 첫 목록은 “Wind input is activated by commands GEN1, GEN2 or GEN3”이다. 2.7 절 표기는 없다. |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.29 (보완) | 편집 파일의 부록 참조와 출력 처리의 유연성 설명이 빠져 있었다. | 편집 파일의 부록 C 참조를 추가했다. 출력 처리가 상당히 유연하다는 설명을 추가했다. | PDF p.29, 인쇄 p.21: “an edit file is available to the user (see Appendix C)”; “SWAN is fairly flexible with respect to output processing.” |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.30 (정정) | 쪽 첫머리를 인쇄되지 않은 §3.2로 표시했다. | 절 번호 없이 출력 제어 목록이 이어지는 것으로 고쳤다. | PDF p.30, 인쇄 p.22 첫 항목: “Definitions of the geographic location(s) of the output.” 이 쪽에 인쇄된 절 제목은 “3.3 Print file and error messages”이다. |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.30 (보완) | 경고·오류 메시지의 통상적인 이해 가능성 설명이 빠져 있었다. | 메시지는 보통 별도 설명 없이 이해할 수 있다는 설명을 추가했다. | PDF p.30, 인쇄 p.22: “These messages are usually self-explanatory.” |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.32 (정정) | 인쇄되지 않은 §4.1을 표시했다. BOUNDNEST1·2·3을 해당 모델 실행의 경계조건을 정의하는 명령으로 적었다. | 절 번호 없는 명령 목록의 계속으로 고쳤다. 세 명령은 각각 거친 SWAN·WAM·WAVEWATCH III 실행에서 얻은 경계조건을 정의한다고 고쳤다. | PDF p.32, 인쇄 p.24 첫 제목: “(d) Commands for boundary and initial conditions:”. BOUNDNEST1: “defines boundary conditions obtained from (coarse) SWAN run”. BOUNDNEST2·3에도 “obtained from”이 인쇄되어 있다. |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.33 (정정) | 쪽 첫 목록에 인쇄되지 않은 §4.1과 블록 (g) 라벨을 붙였다. ISOLINE의 출력 경로를 앞선 RAY의 선으로 읽힐 수 있게 적었다. | 첫 목록의 절 번호와 블록 라벨을 제거했다. ISOLINE의 출력 경로는 정의한 등고선이라고 명시했다. | PDF p.33, 인쇄 p.25 첫 목록은 “FRAME defines an output frame (a regular grid)”에서 시작한다. ISOLINE: “defines a depth- or bottom contour (for output along that contour)”. 첫 절 제목은 “4.2 Sequence of commands”이다. |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.34 (정정) | 쪽 첫머리를 인쇄되지 않은 §4.2로 표시했다. | 절 번호 없이 블록별 명령 순서 설명이 이어지는 것으로 고쳤다. | PDF p.34, 인쇄 p.26 첫 행: “In block (a) : no prescribed sequence in block”. 이 쪽의 절 제목은 “4.3 Command syntax and input/output limitations”와 “4.4 Start-up”이다. |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.34 (보완) | 사용자가 지정할 수 있는 계수의 예가 빠져 있었다. | 해저 마찰계수의 예를 추가했다. | PDF p.34, 인쇄 p.26: “assign values to coefficients of SWAN (e.g. the bottom friction coefficient)” |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.35 (정정) | 인쇄되지 않은 §4.4와 PROJECT 명령명을 쪽 첫머리에 붙였다. 쪽 끝을 다음 쪽의 메시지·기본값 설명으로 미리 요약했다. | 절 번호 없는 구문의 계속으로 고쳤다. 끝부분은 실제 문장 조각 “During the”로 한정했다. | PDF p.35, 인쇄 p.27 첫 구문: “’title2’”, “’title3’”. 설명 첫머리: “With this required command”. 마지막 행은 “During the”로 끝난다. |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.35 (보완) | 프로젝트 이름과 실행 식별자의 예가 빠져 있었다. | 엔지니어링 프로젝트의 예를 추가했다. 실행 번호의 예를 추가했다. | PDF p.35, 인쇄 p.27: “project name e.g., an engineering project”; “to be provided as a character string; e.g. the run number” |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.36 (정정) | 인쇄되지 않은 §4.4와 SET 명령명을 쪽 제목처럼 표시했다. | 절 번호나 명령 제목 없이 매개변수 설명이 이어지는 것으로 고쳤다. | PDF p.36, 인쇄 p.28 첫 행: “computational process messages are written to the print file.” 본문은 “[maxmes] = 200” 기본값과 “[maxerr]” 이하 항목으로 이어진다. |
| [p019-036.md](../manuals/pdfs/swanuse.pdf/p019-036.md):p.36 (보완) | 전처리의 입력 자료 검사 설명이 빠져 있었다. [hsrerr] 경고의 엄격한 초과 조건이 명시되지 않았다. | 전처리에서 입력 자료를 검사한다는 설명을 추가했다. 상대 차이가 [hsrerr]를 초과할 때 경고한다는 조건을 추가했다. | PDF p.36, 인쇄 p.28 [maxerr]: “during pre-processing SWAN checks input data.” [hsrerr]: “above which a warning will be given.” |

정정 21, 보완 16, 이상 없음 13

