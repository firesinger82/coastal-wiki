---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_6.md
lines: 61
sha256: 568366cf4e47974cb28d6f1c0aae4e5dcb47d95d7c41cf46f84f7555fc2ed694
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_6.md — 판독 구간 기록

구간은 1행부터 61행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(frontmatter) — 페이지 ID 30507038(2), 제목 Card Image 6(3), space ECIG(4), 원문 URL(5), 버전 1(6), 수정 시각 2018-01-08T08:19:48.412Z(7), 문서 경로(8)와 구분선(1·9)을 포함한다. |
| 10–24 | C6 DISSOLVED AND SUSPENDED CONSTITUENT TRANSPORT SWITCHES / 성분·수송·이류 — 용존 및 부유 성분(dissolved and suspended constituents)의 수송(transport) 스위치를 다룬다(10). 성분 ID 대응을 열거한다(12). 수송 활성화 범위와 옵션, 3TL 전용 이류(advection) 방식 및 연구용 조건을 정의한다(16–24). ID·매개변수·범위·조건 원문: `\* TURB INTENSITY=0,SAL=1,TEM=2,DYE=3,SFL=4,TOX=5,SED=6,SND=7,CWQ=8` (12); `\* ISTRAN: 1 OR GREATER TO ACTIVATE TRANSPORT` (16); `\* ISTOPT: NONZERO FOR TRANSPORT OPTIONS, SEE USERS MANUAL` (18); `\* ISCDCA: 0 FOR STANDARD DONOR CELL UPWIND DIFFERENCE ADVECTION (3TL ONLY)` (20); `\*                1 FOR CENTRAL DIFFERENCE ADVECTION FOR THREE TIME LEVEL STEPS (3TL ONLY)` (22); `\*                2 FOR EXPERIMENTAL UPWIND DIFFERENCE ADVECTION (FOR RESEARCH) (3TL ONLY)` (24). |
| 25–42 | 수치 확산 보정·연산자 분할 — 표준 donor cell 방식의 반수치 확산 보정(anti-numerical diffusion correction), 플럭스 제한(flux limiting), 수평·수직 이류의 연산자 분할(operator splitting) 및 각 분할 방향의 보정 옵션을 제시한다(26–42). 연구용 조건을 그대로 포함한다. 원문: `\* ISADAC: 1 TO ACTIVATE ANTI-NUMERICAL DIFFUSION CORRECTION TO` (26); `\* STANDARD DONOR CELL SCHEME` (28); `\* ISFCT: 1 TO ADD FLUX LIMITING TO ANTI-NUMERICAL DIFFUSION CORRECTION` (30); `\* ISPLIT: 1 TO OPERATOR SPLIT HORIZONTAL AND VERTICAL ADVECTION` (32); `\* (FOR RESEARCH PURPOSES)` (34); `\* ISADAH: 1 TO ACTIVATE ANTI-NUM DIFFUSION CORRECTION TO HORIZONTAL` (36); `\* SPLIT ADVECTION STANDARD DONOR CELL SCHEME (FOR RESEARCH)` (38); `\* ISADAV: 1 TO ACTIVATE ANTI-NUM DIFFUSION CORRECTION TO VERTICAL` (40); `\* SPLIT ADVECTION STANDARD DONOR CELL SCHEME (FOR RESEARCH)` (42). |
| 43–48 | 농도 재시작 파일 — 농도를 restart.inp에서 읽는 옵션과 restart.out에 쓰는 옵션을 정의한다(44·46). 파일 이름과 적용 조건 원문: `\* ISCI: 1 TO READ CONCENTRATION FROM FILE restart.inp` (44); `\* ISCO: 1 TO WRITE CONCENTRATION TO FILE restart.out` (46). |
| 49–61 | C6 입력 표 — 빈 줄·표 마크업과 성분별 아홉 입력 행을 포함한다(49–61). 머리글 및 TURB·SAL·TEM·DYE·SFL·TOX·SED·SND·CWQ 행의 열별 값을 그대로 옮긴다(52–61). 제시된 수치를 기본값으로 표시하지 않는다. 원문: `\| C6 \| ISTRAN \| ISTOPT \| ISCDCA \| ISADAC \| ISFCT \| ISPLIT \| ISADAH \| ISADAV \| ISCI \| ISCO \|  \|` (52); `\|  \| 1 \| 1 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| 1 \| !TURB 0 \|` (53); `\|  \| 0 \| 0 \| 0 \| 1 \| 1 \| 0 \| 0 \| 0 \| 1 \| 0 \| !SAL  1 \|` (54); `\|  \| 1 \| 4 \| 0 \| 1 \| 1 \| 0 \| 0 \| 0 \| 1 \| 1 \| !TEM  2 \|` (55); `\|  \| 1 \| 0 \| 0 \| 1 \| 1 \| 0 \| 0 \| 0 \| 0 \| 1 \| !DYE  3 \|` (56); `\|  \| 0 \| 0 \| 0 \| 1 \| 1 \| 0 \| 0 \| 0 \| 0 \| 0 \| !SFL  4 \|` (57); `\|  \| 0 \| 0 \| 0 \| 1 \| 1 \| 0 \| 0 \| 0 \| 0 \| 0 \| !TOX  5 \|` (58); `\|  \| 0 \| 0 \| 0 \| 1 \| 1 \| 0 \| 0 \| 0 \| 1 \| 0 \| !SED  6 \|` (59); `\|  \| 0 \| 0 \| 0 \| 1 \| 1 \| 0 \| 0 \| 0 \| 0 \| 0 \| !SND  7 \|` (60); `\|  \| 0 \| 0 \| 0 \| 1 \| 1 \| 0 \| 0 \| 0 \| 0 \| 0 \| !CWQ  8 \|` (61). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 18: `ISTOPT` 설명은 `SEE USERS MANUAL`이라고 적는다. 이 파일에는 해당 참조의 절 번호·쪽 번호·링크가 없다.

