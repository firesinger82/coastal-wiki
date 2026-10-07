---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_39.md
lines: 57
sha256: 622f441750734a357ef9075b63d2725febf404f15781063371a56d9aedda4ca7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_39.md — 판독 구간 기록

구간은 1행부터 57행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | C39 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 점착성 퇴적물(cohesive sediment) 매개변수 집합 1과 자료 행을 NSED번 반복하라는 지시를 제시한다(10). NSED>0이면 ISTRAN(6)=0일 때도 자료가 필요하다고 적는다(12). 빈 줄과 주석 표식도 포함한다(11–15). 원문: ` C39 COHESIVE SEDIMENT PARAMETER SET 1 REPEAT DATA LINE NSED TIMES ` (10); ` \* DATA REQUIRED IF NSED>0, EVEN IF ISTRAN(6) = 0 ` (12). |
| 16–29 | 초기 농도와 물질 특성 — 수주(water column)의 일정 초기 농도와 단위, 단위 면적당 하상 퇴적물 질량과 단위 및 예시를 제시한다(16–24). 퇴적물 비체적(specific volume)의 단위·예시와 비중(specific gravity)을 정의한다(26–28). 원문: ` \* SEDO: CONSTANT INITIAL COHESIVE SEDIMENT CONC IN WATER COLUMN ` (16); ` \* (MG/LITER=GM/M^3) ` (18); ` \* SEDBO: CONSTANT INITIAL COHESIVE SEDIMENT IN BED PER UNIT AREA ` (20); ` \* (GM/SQ METER) IE 1CM THICKNESS BED WITH SSG=2.5 AND ` (22); ` \* N=.6,.5 GIVES SEDBO 1.E4, 1.25E4 ` (24); ` \* SDEN: SEDIMENT SPEC VOLUME (IE 1/2.25E6 M^3/GM) ` (26); ` \* SSG: SEDIMENT SPECIFIC GRAVITY ` (28). |
| 30–41 | 침강·퇴적 — 일정 또는 기준 침강 속도(settling velocity)와 계산식을 제시한다(30–32). SEDSN과 SEXP는 미사용이라고 적는다(34–36). 응력이 TAUD보다 작을 때 퇴적(deposition)이 일어나며 적용하는 비율식을 제시한다(38–40). 원문: ` \* WSEDO: CONSTANT OR REFERENCE SEDIMENT SETTLING VELOCITY ` (30); ` \* IN FORMULA WSED=WSEDO\*( (SED/SEDSN)\*\*SEXP ) ` (32); ` \* SEDSN: (NOT USED) ` (34); ` \* SEXP: (NOT USED) ` (36); ` \* TAUD: BOUNDARY STRESS BELOW WHICH DEPOSITION TAKES PLACE ACCORDING ` (38); ` \* TO (TAUD-TAU)/TAUD ` (40). |
| 42–53 | 농도 보정과 퇴적 확률(probability of deposition) — 최하층 농도를 하상 근처 농도(near bed concentration)로 보정하는 옵션을 제시한다(42). Krone·Partheniades 퇴적 확률과 점착성 입자 응력(cohesive grain stress)·전체 하상 응력(total bed stress)의 네 조합을 구분한다(44–50). 원문: ` \* ISEDSCOR: 1 TO CORRECT BOTTOM LAYER CONCENTRATION TO NEAR BED CONCENTRATION ` (42); ` \* ISPROBDEP: 0 KRONE PROBABILITY OF DEPOSITION USING COHESIVE GRAIN STRESS ` (44); ` \*                       1 KRONE PROBABILITY OF DEPOSITION USING TOTAL BED STRESS ` (46); ` \*                       2 PARTHENIADES PROBABILITY OF DEPOSITION USING COHESIVE GRAIN STRESS ` (48); ` \*                       3 PARTHENIADES PROBABILITY OF DEPOSITION USING TOTAL BED STRESS ` (50). |
| 54–57 | C39 입력 예시 — Markdown의 빈 표 머리글과 구분선(54–55), 열 이름(56), 입력 값(57)을 제시한다. 원문: ` \| C39 \| SEDO \| SEDBO \| SDEN \| SSG \| WSEDO \| SEDSN \| SEXP \| TAUD \| ISEDSCOR \| ISPROBDEP \| ` (56); ` \|  \| 10 \| 25000 \| 4.40E-07 \| 2.65 \| 0.0001 \| 0 \| 0 \| 0.001 \| 0 \| 0 \| ` (57). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 32·34·36행: 침강 속도 계산식은 `SEDSN`과 `SEXP`를 사용한다(32). 두 매개변수 설명은 각각 `(NOT USED)`라고 적는다(34·36).
- 24·32·40행: 초기 하상 예시의 `N`, 침강 계산식의 `SED`, 퇴적 비율식의 `TAU`는 이 파일에 기호 정의가 없다.
