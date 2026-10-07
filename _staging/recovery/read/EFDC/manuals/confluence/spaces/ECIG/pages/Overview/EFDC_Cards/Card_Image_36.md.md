---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md
lines: 95
sha256: 78961f9566d787e277384f3733a79253557e23b6c02d3c8c69dd92336fb081fe
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_36.md — 판독 구간 기록

구간은 1행부터 95행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | C36 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 퇴적물(sediment) 초기화와 수주(water column)·하상(bed) 표현 옵션 제목을 제시한다(10). ISTRAN(6) 또는 ISTRAN(7)이 0이 아닐 때 자료가 필요하다고 적는다(12). 빈 줄과 주석 표식도 포함한다(11–15). 원문: ` C36 SEDIMENT INITIALIZATION AND WATER COLUMN/BED REPRESENTATION OPTIONS ` (10); ` \* DATA REQUIRED IF ISTRAN(6) OR ISTRAN(7) <> 0 ` (12). |
| 16–27 | 초기조건(initial conditions) 공간 분포 — 일정 초기조건, 외부 파일에서 읽는 공간 가변 수주 초기조건, 외부 파일에서 읽는 공간 가변 하상 초기조건, 수주와 하상 모두 공간 가변인 초기조건을 구분한다(16–26). 파일명을 그대로 옮긴다(20·24). 원문: ` \* ISEDINT: 0 FOR CONSTANT INITIAL CONDITIONS ` (16); ` \*               1 FOR SPATIALLY VARIABLE WATER COLUMN INITIAL CONDITIONS ` (18); ` \*                  FROM SEDW.INP AND SNDW.INP ` (20); ` \*              2 FOR SPATIALLY VARIABLE BED INITIAL CONDITIONS ` (22); ` \*                 FROM SEDB.INP AND SNDB.INP ` (24); ` \*             3 FOR SPATIALLY VARIABLE WATER COL AND BED INITIAL CONDITIONS ` (26). |
| 28–43 | 하상 초기조건과 수송 하위 모델(sub-model) — 공간 가변 하상 자료를 면적당 질량(mass/area) 또는 전체 퇴적물 질량의 질량 분율(mass fraction)로 입력하는 옵션을 제시한다(28–34). 질량 분율 옵션은 BEDLAY.INP를 요구한다(32–34). EFDC 본체, SEDZLJ, 독성 오염물질(toxics)을 포함한 SEDZLJ 수송 함수를 구분한다(36–40). 원문: ` \* ISEDBINT: 0 FOR SPATIALLY VARYING BED INITIAL CONDITIONS IN MASS/AREA ` (28); ` \*                 1 FOR SPATIALLY VARYING BED INITIAL CONDITIONS IN MASS FRACTION ` (30); ` \*                    OF TOTAL SEDIMENT MASS (REQUIRES BED LAYER THICKNESS ` (32); ` \*                    FILE BEDLAY.INP) ` (34); ` \* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE ` (36); ` \*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL ` (38); ` \*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS ` (40). |
| 44–53 | 유동성 이토(fluid mud) — 점착성 유동성 이토의 점성 효과(viscous effects)를 포함하는 조건과 함수를 제시한다(44–46). ISNDWC는 미사용이라고 적는다(48). 빈 줄과 반복 주석 표식도 포함한다. 원문: ` \* ISMUD: 1 INCLUDE COHESIVE FLUID MUD VISCOUS EFFECTS USING EFDC ` (44); ` \*                FUNCTION CSEDVIS(SEDT) ` (46); ` \* ISNDWC: NOT USED ` (48). |
| 54–73 | 점착성 퇴적물 침강 속도(cohesive sediment settling velocity) — 일정 또는 단순 농도 의존 속도와 농도·전단(shear)·난류(turbulence) 의존 속도 옵션을 설명한다(54–62). 함수 인수와 옵션 이름, Lick 응집(flocculation), 응집체 지름 이류(floc diameter advection)를 원문대로 제시한다(62–72). 원문: ` \* ISEDVW: 0 FOR CONSTANT OR SIMPLE CONCENTRATION DEPENDENT ` (54); ` \*                   COHESIVE SEDIMENT SETTLING VELOCITY ` (56); ` \*               >1 CONCENTRATION AND/OR SHEAR/TURBULENCE DEPENDENT COHESIVE ` (58); ` \*                  SEDIMENT SETTLING VELOCITY. VALUE INDICATES OPTION TO BE USED ` (60); ` \*                  IN EFDC FUNCTION CSEDSET(SED,SHEAR,ISEDVWC) ` (62); ` \*               1 HUANG AND MEHTA - LAKE OKEECHOBEE ` (64); ` \*               2 SHRESTA AND ORLOB - FOR KRONES SAN FRANCISCO BAY DATA ` (66); ` \*               3 ZIEGLER AND NESBIT - FRESH WATER ` (68); ` \*             98 LICK FLOCCULATION ` (70); ` \*             99 LICK FLOCCULATION WITH FLOC DIAMETER ADVECTION ` (72). |
| 74–91 | 비점착성 퇴적물 침강 및 하상 층 — 일정 속도 또는 지정 속도가 음수일 때 입경으로 계산하는 옵션을 제시한다(74–76). >1 옵션의 방해 침강(hindered settling) 보정과 원문 계산식을 제시한다(78–84). 활성 층(active layer)을 제외한 최대 하상 층 수와 퇴적물·독성 오염물질 진단 활성화 조건을 정의한다(86–88). 원문: ` \* ISNDVW: 0 USE CONSTANT SPECIFIED NON-COHESIVE SED SETTLING VELOCITIES ` (74); ` \*                  OR CALCULATE FOR CLASS DIAMETER IF SPECIFIED VALUE IS NEG ` (76); ` \*              >1 FOLLOW OPTION 0 PROCEDURE BUT APPLY HINDERED SETTLING ` (78); ` \*                  CORRECTION. VALUE INDICATES OPTION TO BE USED WITH EFDC ` (80); ` \*                  FUNCTION CSNDSET(SND,SDEN,ISNDVW) VALUE OF ISNDVW INDICATES ` (82); ` \*                  EXPONENTIAL IN CORRECT (1-SDEN(NS)\*SND(NS)\*\*ISNDVW ` (84); ` \* KB: MAXIMUM NUMBER OF BED LAYERS (EXCLUDING ACTIVE LAYER) ` (86); ` \* ISDTXBUG: 1 TO ACTIVATE SEDIMENT AND TOXICS DIAGNOSTICS ` (88). |
| 92–95 | C36 입력 예시 — Markdown의 빈 표 머리글과 구분선(92–93), 열 이름(94), 입력 값(95)을 제시한다. 원문: ` \| C36 \| ISEDINT \| ISEDBINT \| NSEDFLUME \| ISMUD \| ISNDWC \| ISEDVW \| ISNDVW \| KB \| ISDTXBUG \| ` (94); ` \|  \| 2 \| 1 \| 0 \| 0 \| 0 \| 0 \| 0 \| 8 \| 0 \| ` (95). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 58·64행: 농도·전단·난류 의존 침강 속도 설명은 `>1`을 적는다(58). 같은 옵션 목록은 `1 HUANG AND MEHTA - LAKE OKEECHOBEE`도 적는다(64).
- 54·62행: 매개변수 이름은 `ISEDVW`라고 적는다(54). 함수 인수에는 `ISEDVWC`라고 적으며 이 파일은 두 이름의 관계를 정의하지 않는다(62).
- 84행: 보정 계산식은 `(1-SDEN(NS)\*SND(NS)\*\*ISNDVW`로 끝난다. 여는 괄호에 대응하는 최종 닫는 괄호가 없다.
