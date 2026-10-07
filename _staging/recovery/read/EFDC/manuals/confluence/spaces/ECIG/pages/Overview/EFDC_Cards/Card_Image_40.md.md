---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_40.md
lines: 67
sha256: a9d251c4be145ca74d35cd207198fea0f8b619b4df11402c37bb15326256099c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_40.md — 판독 구간 기록

구간은 1행부터 67행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | C40 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 점착성 퇴적물(cohesive sediment) 매개변수 집합 2와 자료 행을 NSED번 반복하라는 지시를 제시한다(10). NSED>0이면 ISTRAN(6)=0일 때도 자료가 필요하다고 적는다(12). 빈 줄과 주석 표식도 포함한다(11–15). 원문: ` C40 COHESIVE SEDIMENT PARAMETER SET 2 REPEAT DATA LINE NSED TIMES ` (10); ` \* DATA REQUIRED IF NSED>0, EVEN IF ISTRAN(6) = 0 ` (12). |
| 16–43 | 재부유·침식 유형 — IWRSP=0은 이 자료 행의 매개변수에 따른 재부유율(resuspension rate)과 임계 응력(critical stress)을 사용한다(16–18). 양의 값은 하상 특성에 의존하는 함수를 사용하며 함수 이름·인수 및 1–5·>=99 옵션을 제시한다(20–36). 벌크 침식(bulk erosion) 비활성 또는 함수 기반 활성 옵션을 구분한다(38–42). 원문: ` \* IWRSP: 0 USE RESUSPENSION RATE AND CRITICAL STRESS BASED ON PARAMETERS ` (16); ` \*                 ON THIS DATA LINE ` (18); ` \*            >0 USE BED PROPERTIES DEPENDEDNT RESUSPENSION RATE AND CRITICAL ` (20); ` \*                 STRESS GIVEN BY EFDC FUNCTIONS CSEDRESS,CSEDTAUS,CSEDTAUB ` (22); ` \*                 FUNCTION ARGUMENSTS ARE (BDENBED,IWRSP) ` (24); ` \*             1 HWANG AND MEHTA - LAKE OKEECHOBEE ` (26); ` \*             2 HAMRICK'S MODIFICATION OF SANFORD AND MAA ` (28); ` \*             3 SAME AS 2 EXCEPT VOID RATIO OF COHESIVE SEDIMENT FRACTION IS USED ` (30); ` \*             4 SEDFLUME WITHOUT CRITICAL STRESS ` (32); ` \*             5 SEDFLUME WITH CRITICAL STRESS ` (34); ` \*      >= 99 SITE SPECIFIC ` (36); ` \* IWRSPB:0 NO BULK EROSION ` (38); ` \*               1 USE BULK EROSION CRITICAL STRESS AND RATE IN FUNCTIONS ` (40); ` \*                  CSEDTAUB AND CSEDRESSB ` (42). |
| 44–57 | 표면 침식(surface erosion) 계산 — 기준 침식률과 계산식의 단위, 표면 침식이 발생하는 응력 조건과 단위, 코드에서 설정하는 TAUN 관계, 지수를 정의한다(44–52). 기준 간극비(reference void ratio)는 IWRSP=2·3에 적용한다(54–56). 계산식을 반복하는 52행도 그대로 옮긴다. 원문: ` \* WRSPO: REF SURFACE EROSION RATE IN FORMULA ` (44); ` \* WRSP=WRSP0\*( ((TAU-TAUR)/TAUN)\*\*TEXP ) (gm/m^2/sec) ` (46); ` \* TAUR: BOUNDARY STRESS ABOVE WHICH SURFACE EROSION OCCURS (m/s)\*\*2 ` (48); ` \* TAUN: (NOT USED, TAUN=TAUR SET IN CODE) ` (50); ` \* TEXP: EXPONENT OF WRSP=WRSP0\*( ((TAU-TAUR)/TAUN)\*\*TEXP ) ` (52); ` \* VDRRSPO: REFERENCE VOID RATIO FOR CRITICAL STRESS AND RESUSPENSION RATE ` (54); ` \* IWRSP=2,3 ` (56). |
| 58–63 | 차폐 계수(hiding factor) — 점착성 퇴적물 재부유를 줄이는 차폐 계수와 점착성 분율(cohesive fraction)을 사용하는 승수 계산식을 제시한다(58–60). 원문: ` \* COSEDHID: COHESIVE SEDIMENT RESUSPENSION HIDING FACTOR TO REDUCE COHESIVE ` (58); ` \* RESUSPENSION BY FACTOR = (COHESIVE FRACTION OF SEDIMENT)\*\*COSEDHID ` (60). |
| 64–67 | C40 입력 예시 — Markdown의 빈 표 머리글과 구분선(64–65), 열 이름(66), 입력 값(67)을 제시한다. 원문: ` \| C40 \| IWRSP \| IWRSPB \| WRSPO \| TAUR \| TAUN \| TEXP \| VDRRSPO \| COSEDHID \| ` (66); ` \|  \| 0 \| 0 \| 0.001 \| 0.002 \| 0 \| 1 \| 0 \| 0 \| ` (67). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 44·46·52·66행: 기준 표면 침식률의 설명 및 입력 이름은 마지막 문자가 영문 O인 `WRSPO`다(44·66). 계산식은 마지막 문자가 숫자 0인 `WRSP0`를 사용한다(46·52). 이 파일은 두 이름의 관계를 명시하지 않는다.
- 24·46·52행: 함수 인수의 `BDENBED`와 침식 계산식의 `TAU`는 이 파일에 기호 정의가 없다.
