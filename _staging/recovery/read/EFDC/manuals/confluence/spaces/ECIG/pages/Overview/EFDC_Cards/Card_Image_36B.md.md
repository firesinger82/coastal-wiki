---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36B.md
lines: 47
sha256: 1eea8cced6fd84abafb1b25345c98aeba829bc57554129da8089d01ab5285c13
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_36B.md — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | C36B — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 퇴적물(sediment) 초기화와 수주(water column)·하상(bed) 표현 옵션 제목을 제시한다(10). ISTRAN(6)과 ISTRAN(7)이 모두 0일 때도 자료가 필요하다고 적는다(12). 빈 줄과 주석 표식도 포함한다(11–15). 원문: ` C36B SEDIMENT INITIALIZATION AND WATER COLUMN/BED REPRESENTATION OPTIONS ` (10); ` \* DATA REQUIRED EVEN IF ISTRAN(6) AND ISTRAN(7) ARE 0 ` (12). |
| 16–27 | 표층 장갑화(armoring) — ISEDAL은 미사용이다(16). 비점착성 장갑화 활성화와 활성·모층(active-parent layer) 방식의 옵션을 제시한다(18–20). 장갑층(armoring layer)의 일정 두께 또는 일정 전체 질량 옵션, 시작 시 최상층에서 장갑층을 만드는 옵션을 정의한다(22–26). 원문: ` \* ISEDAL: NOT USED ` (16); ` \* ISNDAL: 1 TO ACTIVATE NON-COHESIVE ARMORING EFFECTS (GARCIA & PARKER) ` (18); ` \*               2 SAME AS 1 WITH ACTIVE-PARENT LAYER FORMULATION ` (20); ` \* IALTYP: 0 CONSTANT THICKNESS ARMORING LAYER ` (22); ` \*              1 CONSTANT TOTAL SEDIMENT MASS ARMORING LAYER ` (24); ` \* IALSTUP: 1 CREATE ARMORING LAYER FROM INITIAL TOP LAYER AT START UP ` (26). |
| 28–43 | 점착성 효과 보정 — 비점착성 재부유(resuspension)와 임계 응력(critical stress)을 점착성 효과에 맞게 수정하는 두 옵션과 각각의 승수 계산식을 제시한다(28–34). 활성 장갑층 두께와 점착성 효과 계수 두 항목을 정의한다(36–40). 원문: ` \* ISEDEFF: 1 MODIFY NON-COHESIVE RESUSPENSION TO ACCOUNT FOR COHESIVE EFFECTS ` (28); ` \*                    USING MULTIPLICATION FACTOR: EXP(-COEHEFF\*FRACTION COHESIVE) ` (30); ` \*                 2 MODIFY NON-COHESIVE CRITICAL STRESS TO ACCOUNT FOR COHESIVE EFFECTS ` (32); ` \* USING MULT FACTOR: 1+(COEHEFF2-1)\*(1-EXP(-COEHEFF\*FRACTION COHESIVE)) ` (34); ` \* HBEDAL: ACTIVE ARMORING LAYER THICKNESS ` (36); ` \* COEHEFF: COHESIVE EFFECTS COEFFICIENT ` (38); ` \* COEHEFF2: COHESIVE EFFECTS COEFFICIENT ` (40). |
| 44–47 | C36B 입력 예시 — Markdown의 빈 표 머리글과 구분선(44–45), 열 이름(46), 입력 값(47)을 제시한다. 원문: ` \| C36B \| ISEDAL \| ISNDAL \| IALTYP \| IALSTUP \| ISEDEFF \| HBEDAL \| COEHEFF \| COEHEFF2 \| ` (46); ` \|  \| 1 \| 2 \| 0 \| 1 \| 0 \| 0.03 \| 0 \| 0 \| ` (47). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
