---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_41.md
lines: 52
sha256: 82e2a692cffd4756fdcd78d53d86f3e875fd3def952df8ff54af3428d8aca76b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_41.md — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | C41 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 비점착성 퇴적물(non-cohesive sediment) 매개변수 집합 1과 자료 행을 NSND번 반복하라는 지시를 제시한다(10). NSND>0이면 ISTRAN(7)=0일 때도 자료가 필요하다고 적는다(12). 빈 줄과 주석 표식도 포함한다(11–15). 원문: ` C41 NON-COHESIVE SEDIMENT PARAMETER SET 1 REPEAT DATA LINE NSND TIMES ` (10); ` \* DATA REQUIRED IF NSND>0, EVEN IF ISTRAN(7) = 0 ` (12). |
| 16–29 | 초기 농도와 물질 특성 — 수주(water column)의 일정 초기 농도와 단위, 단위 면적당 하상(bed) 퇴적물 질량과 단위 및 예시를 제시한다(16–24). 퇴적물 비체적(specific volume)의 단위·예시와 비중(specific gravity)을 정의한다(26–28). 원문: ` \* SNDO: CONSTANT INITIAL NON-COHESIVE SEDIMENT CONC IN WATER COLUMN ` (16); ` \* (MG/LITER=GM/M^3) ` (18); ` \* SNDBO: CONSTANT INITIAL NON-COHESIVE SEDIMENT IN BED PER UNIT AREA ` (20); ` \* (GM/SQ METER) IE 1CM THICKNESS BED WITH SSG=2.5 AND ` (22); ` \* N=.6,.5 GIVES SNDBO 1.E4, 1.25E4 ` (24); ` \* SDEN: SEDIMENT SPEC VOLUME (IE 1/2.65E6 M^3/GM) ` (26); ` \* SSG: SEDIMENT SPECIFIC GRAVITY ` (28). |
| 30–35 | 입경과 침강 속도(settling velocity) — 입경 등급(sediment class)의 대표 지름은 m 단위다(30). 일정 또는 기준 침강 속도를 정의하며 WSNDO<0이면 내부에서 계산한다고 적는다(32–34). 원문: ` \* SNDDIA: REPRESENTATIVE DIAMETER OF SEDIMENT CLASS (m) ` (30); ` \* WSNDO: CONSTANT OR REFERENCE SEDIMENT SETTLING VELOCITY ` (32); ` \* WSNDO < 0, SETTLING VELOCITY INTERNALLY COMPUTED ` (34). |
| 36–45 | 미사용 항목 — SNDN, SEXP, TAUD, ISNDSCOR는 미사용이라고 적는다(36–42). 빈 줄과 주석 표식도 포함한다. 원문: ` \* SNDN: (NOT USED) ` (36); ` \* SEXP: (NOT USED) ` (38); ` \* TAUD: (NOT USED) ` (40); ` \* ISNDSCOR: (NOT USED) ` (42). |
| 46–52 | C41 입력 예시 — Markdown의 빈 표 머리글과 구분선(46–47), 열 이름(48), 네 자료 행의 농도·하상 질량·비체적·비중·입경·침강 속도와 나머지 입력 값(49–52)을 제시한다. 각 자료 행을 그대로 옮긴다. 원문: ` \| C41 \| SNDO \| SNDBO \| SDEN \| SSG \| SNDDIA \| WSNDO \| SNDN \| SEXP \| TAUD \| ISNDSCOR \| ` (48); ` \|  \| 5 \| 10070 \| 3.77E-07 \| 2.65 \| 0.000135 \| 0.01351 \| 0 \| 0 \| 0 \| 0 \| ` (49); ` \|  \| 0 \| 10070 \| 3.77E-07 \| 2.65 \| 0.0004 \| 0.05925 \| 0 \| 0 \| 0 \| 0 \| ` (50); ` \|  \| 0 \| 10070 \| 3.77E-07 \| 2.65 \| 0.0008 \| 0.102 \| 0 \| 0 \| 0 \| 0 \| ` (51); ` \|  \| 0 \| 10070 \| 3.77E-07 \| 2.65 \| 0.002 \| 0.1979 \| 0 \| 0 \| 0 \| 0 \| ` (52). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 24행: 초기 하상 질량 예시에 `N=.6,.5`가 나오지만 이 파일은 `N`의 뜻을 정의하지 않는다.
