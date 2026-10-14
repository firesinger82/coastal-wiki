SWASH PDF 판독 기록의 10-15 전수 검증 결과다.

쪽 번호는 PDF 파일의 물리 쪽 번호다.
대상 기록의 모든 쪽 행을 지정된 300dpi 쪽 이미지와 대조했다.
집계 단위는 쪽 행이다.
한 쪽 행의 여러 수정은 해당 유형 한 건으로 셌다.

대조 이미지 경로는 다음과 같다.
`/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/swhpages/<PDF명>-<3자리 쪽번호>.png`

| 기록 | 대조한 쪽 | 대조 쪽 수 | 정정 | 보완 | 이상 없음 |
| --- | --- | ---: | ---: | ---: | ---: |
| [swashuse.pdf/p145-167.md](../swash/doc/swashuse.pdf/p145-167.md) | 145–167 | 23 | 6 | 0 | 17 |
| [swashtech.pdf/p001-018.md](../swash/doc/swashtech.pdf/p001-018.md) | 1–18 | 18 | 2 | 1 | 15 |
| 합계 | 대상 전체 | 41 | 8 | 1 | 32 |

swashuse 기록의 이상 없는 쪽은 145–146, 148–149, 152, 154–158, 160–161, 163–167쪽이다.
swashtech 기록의 이상 없는 쪽은 1–13, 15, 18쪽이다.

아래 표의 swashuse와 swashtech는 위 표의 각 기록을 가리킨다.
인쇄 원문 칸의 따옴표와 코드 표시는 쪽 이미지에서 확인한 발췌다.

| 기록:쪽 | 이전 요지 | 새 요지 | 인쇄 원문 |
| --- | --- | --- | --- |
| swashuse:p.147 (정정) | 표를 지수 m에 따른 한쪽 방향 퍼짐으로 설명했다. | 해당 쪽에 인쇄된 m과 방향 퍼짐만 기록했다. | “Table A.1: Directional distribution.”. 표 머리글은 “m”과 “directional spread (in °)”다. “one-sided”는 p.145에 인쇄되어 있다. |
| swashuse:p.150 (정정) | 소제목 앞의 B.2.1을 해당 쪽에 인쇄된 절 번호처럼 썼다. | p.149에서 시작한 B.2.1절의 계속임을 밝혔다. | “Spelling of keywords”. “Required and optional keywords”. 이 쪽에는 B.2.1이 인쇄되어 있지 않다. |
| swashuse:p.151 (정정) | 소제목 앞의 B.2.1을 해당 쪽에 인쇄된 절 번호처럼 썼다. | p.149에서 시작한 B.2.1절의 계속임을 밝혔다. | “Repetitions of keywords and/or other data”. 이 쪽에는 B.2.1이 인쇄되어 있지 않다. |
| swashuse:p.153 (정정) | 소제목 앞의 B.2.2를 해당 쪽에 인쇄된 절 번호처럼 썼다. | p.151에서 시작한 B.2.2절의 계속임을 밝혔다. | “Required data and optional data”. 이 쪽에는 B.2.2가 인쇄되어 있지 않다. |
| swashuse:p.159 (정정) | SMOOTH 줄과 MIXing 줄에서 세로 분기선 하나씩을 빠뜨렸다. | 두 줄의 세로 분기선을 각각 두 개로 옮겼다. | `! \| \| -> SMOOTH`. `! \| \| MIXing [lm]`. |
| swashuse:p.162 (정정) | QUANTity 매개변수를 예외값·기준값·평균 기간 등으로 풀이했다. | 문자열 이름과 수치 매개변수를 표시하는 명령 도식으로 기록했다. 이 쪽에는 각 매개변수의 뜻을 설명하는 본문이 없음을 밝혔다. | `QUANTity` 명령 도식에 `’short’’long’ [lexp] [hexp] [excv] [ref]`가 있다. 매개변수의 뜻을 설명하는 본문은 없다. |
| swashtech:p.14 (보완) | Arakawa의 C-격자 문헌 번호만 기록했다. 발산형·이류형의 운동에너지 비보존 설명에서 유한차분 계산이라는 범위를 생략했다. | C-격자가 비선형 수치 불안정성 제거에 효과적이라는 결과를 보완했다. 운동에너지 비보존 설명의 범위를 유한차분 계산으로 명시했다. | “the staggered C-grid approach has proven to be effective in eliminating the problem of nonlinear computational instability [2, 3].”. “neither the divergence form nor the advective form conserves kinetic energy in finite difference computations, even on a uniform grid, unless they comply with a discrete product rule of differentiation.”. |
| swashtech:p.16 (정정) | 마지막 문장을 C-격자의 정확도·안정성 비교로 기록했다. | 해당 쪽에 인쇄된 정확도 비교만 기록했다. | “The C-grid discretization is superior to both A-grid and B-grid regarding the accuracy” 뒤에서 다음 쪽으로 이어진다. “and stability”는 p.17에 인쇄되어 있다. |
| swashtech:p.17 (정정) | 쪽 끝의 미완성 문장에 discrete differential forms라는 완성된 용어를 썼다. | 해당 문장이 discrete differential 뒤에서 다음 쪽으로 이어짐을 밝혔다. | “Rather, they are driven by the topological interpretation of the physical fields as discrete differential” 뒤에서 다음 쪽으로 이어진다. “forms.”는 p.18에 인쇄되어 있다. |

두 대상 기록의 frontmatter를 유지했다.
쪽 행의 수와 순서를 유지했다.
정정·보완한 쪽 행 끝에 해당 검증 표지를 붙였다.
이상 없는 쪽 행은 변경하지 않았다.

정정 8, 보완 1, 이상 없음 32
