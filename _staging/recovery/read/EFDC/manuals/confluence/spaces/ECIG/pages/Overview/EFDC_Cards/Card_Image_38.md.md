---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_38.md
lines: 41
sha256: be22eec1c74789a98f705abd98e576a451d2eadfc21722acb0235410336bcf6e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_38.md — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | C38 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 하상 역학 특성(bed mechanical properties) 매개변수 집합 2 제목을 제시한다(10). NSED>0이면 ISTRAN(6)=0일 때도 자료가 필요하다고 적는다(12). 빈 줄과 주석 표식도 포함한다(11–15). 원문: ` C38 BED MECHANICAL PROPERTIES PARAMETER SET 2 ` (10); ` \* DATA REQUIRED IF NSED>0, EVEN IF ISTRAN(6) = 0 ` (12). |
| 16–19 | 투수계수(hydraulic conductivity) 함수 — IBMECHK=0의 K 함수와 IBMECHK=1의 투수계수를 1+간극비(void ratio)로 나눈 K' 함수를 제시한다(16·18). 두 함수식을 원문 그대로 옮긴다. 원문: ` \* IBMECHK: 0 FOR HYDRAULIC CONDUCTIVITY, K, FUNCTION K=KO\*EXP((E-EO)/EK) ` (16); ` \*                  1 FOR HYD COND/(1+VOID RATIO),K', FUNCTION K'=KO'\*EXP((E-EO)/EK) ` (18). |
| 20–37 | 역학 계수와 적용 조건 — 기준 유효 응력(effective stress)을 물의 비중량(water specific weight)으로 나눈 값의 m 단위, 기준 간극비, 유효 응력 함수를 정의한다(20–26). 기준 투수계수의 m/s 단위, 기준 간극비, 투수계수 함수를 정의한다(28–34). BMECH1<0과 BMECH4<0일 때 내부 함수를 쓰는 조건 및 미사용 항목 목록을 그대로 옮긴다(22·30). 원문: ` \* BMECH1: REFERENCE EFFECTIVE STRESS/WATER SPECIFIC WEIGHT, SEO (m) ` (20); ` \* IF BMECH1<0 USE INTERNAL FUNCTION, BMECH1,BMECH2,BMECH3 NOT USED ` (22); ` \* BMECH2: REFERENCE VOID RATIO FOR EFFECTIVE STRESS FUNCTION, EO ` (24); ` \* BMECH3: VOID RATIO RATE TERM ES IN SE=SEO\*EXP(-(E-EO)/ES) ` (26); ` \* BMECH4: REFERENCE HYDRAULIC CONDUCTIVITY, KO (m/s) ` (28); ` \* IF BMECH4<0 USE INTERNAL FUNCTION, BMECH1,BMECH2,BMECH3 NOT USED ` (30); ` \* BMECH5: REFERENCE VOID RATIO FOR HYDRAULIC CONDUCTIVITY, EO ` (32); ` \* BMECH6: VOID RATIO RATE TERM EK IN (K OR K')=(KO OR KO')\*EXP((E-EO)/EK) ` (34). |
| 38–41 | C38 입력 예시 — Markdown의 빈 표 머리글과 구분선(38–39), 열 이름(40), 입력 값(41)을 제시한다. 원문: ` \| C38 \| IBMECHK \| BMECH1 \| BMECH2 \| BMECH3 \| BMECH4 \| BMECH5 \| BMECH6 \| ` (40); ` \|  \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| ` (41). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 22·30행: `BMECH1<0` 조건의 미사용 목록은 `BMECH1,BMECH2,BMECH3`다(22). `BMECH4<0` 조건의 미사용 목록도 `BMECH1,BMECH2,BMECH3`라고 적는다(30).
- 16·18·26·34행: 함수식의 `E`, `KO'`, `SE`는 이 파일에 명시적인 기호 정의가 없다.
