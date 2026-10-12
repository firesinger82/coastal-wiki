SWAN `swanpgr.pdf` 판독 기록 전수 검증 (2026-10-13).

원문은 `models/SWAN/raw/manuals/pdfs/swanpgr.pdf`이다.
PDF 1–36쪽의 지정된 300dpi 이미지를 모두 열어 기록의 쪽 행과 의미를 대조했다.
이미지 경로는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/swpages/`이다.
실제 파일명은 `swanpgr-01.png`부터 `swanpgr-36.png`까지이다.

대조한 행 수는 각 기록의 `| p.N |` 쪽 행을 센 값이다.
정정과 보완은 각 표식이 있는 쪽 행을 각각 센 값이다.
`p001-018.md:p.11`은 정정과 보완 집계에 모두 포함된다.
이상 없음은 수정하지 않은 쪽 행을 센 값이다.

| 기록 | 대조 구간 | 대조한 행 수 | 정정 행 | 보완 행 | 이상 없음 행 |
|---|---|---:|---:|---:|---:|
| [p001-018.md](../manuals/pdfs/swanpgr.pdf/p001-018.md) | p.1–18 | 18 | 7 | 3 | 9 |
| [p019-036.md](../manuals/pdfs/swanpgr.pdf/p019-036.md) | p.19–36 | 18 | 4 | 1 | 13 |
| 합계 | p.1–36 | 36 | 11 | 4 | 22 |

첫 기록에서 이상 없음으로 분류한 쪽은 p.1–6, p.8, p.14, p.18이다.
둘째 기록에서 이상 없음으로 분류한 쪽은 p.19–21, p.23–27, p.30–33, p.36이다.

아래 원문 행은 이미지에서 확인한 구절이다.
원문 행의 위치는 PDF 쪽과 인쇄 쪽으로 표시했다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [p001-018.md:p.7](../manuals/pdfs/swanpgr.pdf/p001-018.md) (정정) | 제9장 안내를 성능 개선으로 좁혀 적었다. | 이 쪽의 표현대로 코드 개선으로 고쳤다. | PDF p.7(인쇄 p.1), 둘째 문단: `Chapter 9 gives some advices on the improvement of the code`. |
| [p001-018.md:p.9](../manuals/pdfs/swanpgr.pdf/p001-018.md) (보완) | 규칙이 코드 인계를 돕는다는 설명만 적었다. | 규칙이 소스 코드의 개발과 유지보수도 돕는다는 설명을 추가했다. | PDF p.9(인쇄 p.3), 도입 문단 끝: `Rules will help the programmer to develop and maintain the source code.` |
| [p001-018.md:p.10](../manuals/pdfs/swanpgr.pdf/p001-018.md) (정정) | 이 쪽의 도입 표기에 `FORTRAN 90 standards`를 넣었다. | 인쇄된 머리말 `Chapter 2`만 적었다. | PDF p.10(인쇄 p.4), 위쪽 머리말: `Chapter 2`. 이 쪽에는 장 제목이 없다. |
| [p001-018.md:p.11](../manuals/pdfs/swanpgr.pdf/p001-018.md) (정정) | 이 쪽의 도입 표기에 `Chapter 2`를 넣었다. | 인쇄된 머리말 `FORTRAN 90 standards`만 적었다. | PDF p.11(인쇄 p.5), 위쪽 머리말: `FORTRAN 90 standards`. 이 쪽에는 장 번호가 없다. |
| [p001-018.md:p.11](../manuals/pdfs/swanpgr.pdf/p001-018.md) (보완) | 상수를 한 곳에서 정의하는 이유를 생략했다. | 상수 값을 한 번만 변경하면 된다는 이유를 추가했다. | PDF p.11(인쇄 p.5), PARAMETER 설명: `so that changing the value can be done once`. |
| [p001-018.md:p.12](../manuals/pdfs/swanpgr.pdf/p001-018.md) (정정) | 이 쪽의 도입 표기에 `FORTRAN 90 standards`를 넣었다. | 인쇄된 머리말 `Chapter 2`만 적었다. | PDF p.12(인쇄 p.6), 위쪽 머리말: `Chapter 2`. 이 쪽에는 장 제목이 없다. |
| [p001-018.md:p.13](../manuals/pdfs/swanpgr.pdf/p001-018.md) (정정) | 이 쪽의 도입 표기에 `Chapter 2`를 넣었다. | 인쇄된 머리말 `FORTRAN 90 standards`만 적었다. | PDF p.13(인쇄 p.7), 위쪽 머리말: `FORTRAN 90 standards`. 이 쪽에는 장 번호가 없다. |
| [p001-018.md:p.15](../manuals/pdfs/swanpgr.pdf/p001-018.md) (보완) | 제어 구조를 세 가지로 제시하는 문장에서 한정 표현을 생략했다. | 원문의 `In principle`을 원칙적으로로 보완했다. | PDF p.15(인쇄 p.9), 본문 첫 행: `In principle, a net program contains three control structure:`. |
| [p001-018.md:p.16](../manuals/pdfs/swanpgr.pdf/p001-018.md) (정정) | 이 쪽의 도입 표기에 `Control statements`를 넣었다. | 인쇄된 머리말 `Chapter 3`만 적었다. | PDF p.16(인쇄 p.10), 위쪽 머리말: `Chapter 3`. 이 쪽에는 장 제목이 없다. |
| [p001-018.md:p.17](../manuals/pdfs/swanpgr.pdf/p001-018.md) (정정) | 이 쪽의 도입 표기에 `Chapter 3`를 넣었다. | 인쇄된 머리말 `Control statements`만 적었다. | PDF p.17(인쇄 p.11), 위쪽 머리말: `Control statements`. 이 쪽에는 장 번호가 없다. |
| [p019-036.md:p.22](../manuals/pdfs/swanpgr.pdf/p019-036.md) (정정) | 이 쪽의 도입 표기에 `Program layout`을 넣었다. | 인쇄된 머리말 `Chapter 5`만 적었다. | PDF p.22(인쇄 p.16), 위쪽 머리말: `Chapter 5`. 이 쪽에는 장 제목이 없다. |
| [p019-036.md:p.28](../manuals/pdfs/swanpgr.pdf/p019-036.md) (정정) | 이 쪽에 없는 장 제목 `Pseudo code`와 절 번호 `§8.1`을 도입 표기에 넣었다. | 인쇄된 머리말 `Chapter 8`만 남겼다. 기호 정의의 확인 범위를 이 쪽의 반복 예제로 적었다. | PDF p.28(인쇄 p.22), 위쪽 머리말: `Chapter 8`. 이 쪽의 절 표기는 `8.2 Input and output`과 `8.3 Further operations`이다. |
| [p019-036.md:p.29](../manuals/pdfs/swanpgr.pdf/p019-036.md) (정정) | 이 쪽의 도입 표기에 `Chapter 8`과 `§8.3`을 넣었다. | 인쇄된 머리말 `Pseudo code`만 적었다. | PDF p.29(인쇄 p.23), 위쪽 머리말: `Pseudo code`. 본문에는 `Notes:`가 보인다. 이 쪽에는 장 번호와 절 번호가 없다. |
| [p019-036.md:p.34](../manuals/pdfs/swanpgr.pdf/p019-036.md) (정정) | 이 쪽의 도입 표기에 `Machine dependency`를 넣었다. | 인쇄된 머리말 `Chapter 10`만 적었다. | PDF p.34(인쇄 p.28), 위쪽 머리말: `Chapter 10`. 이 쪽에는 장 제목이 없다. |
| [p019-036.md:p.35](../manuals/pdfs/swanpgr.pdf/p019-036.md) (보완) | 배열 차원 선호의 구조적 관점을 생략했다. 행렬 구조와 선형 해법기가 예시라는 한정을 생략했다. | 구조적 관점에서 배열 차원을 선호한다는 설명을 보완했다. 행렬 구조와 선형 해법기를 각각 예시로 표시했다. | PDF p.35(인쇄 p.29), 첫 번째 글머리표: `from a structural point of view`; `an n-dimensional array (e.g. for the matrix structure)`; `an m-dimensional array is preferred (e.g. for the linear solver)`. |

두 기록의 frontmatter는 변경하지 않았다.
두 기록의 쪽 행 구성은 유지했다.
두 기록의 쪽 행 밖 내용은 변경하지 않았다.
모델은 실행하지 않았다.
원문·노트·git은 변경하지 않았다.

정정 11, 보완 4, 이상 없음 22

