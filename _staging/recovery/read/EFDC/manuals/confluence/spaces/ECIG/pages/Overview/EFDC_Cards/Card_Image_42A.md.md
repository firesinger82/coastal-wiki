---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_42A.md
lines: 50
sha256: 5ceec27eec40d1439328f95e29ee6a2d7051ae7ddc34b70204c7ded80dfee1fa
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_42A.md — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | C42A — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 비점착성 퇴적물(non-cohesive sediment) 매개변수 집합 3의 소류(bed load) 공식 매개변수 제목을 제시한다(10). NSND>0이면 ISTRAN(7)=0일 때도 자료가 필요하다고 적는다(12). 빈 줄과 주석 표식도 포함한다(11–15). 원문: ` C42A NON-COHESIVE SEDIMENT PARAMETER SET 3 (BED LOAD FORMULA PARAMETERS) ` (10); ` \* DATA REQUIRED IF NSND>0, EVEN IF ISTRAN(7) = 0 ` (12). |
| 16–33 | 소류 활성화와 공식 계수 — 소류 비활성·활성 옵션과 셀을 지정하는 SEDBLBC.INP 파일을 제시한다(16–18). ALPHA·BETA 지수, GAMMA1–4 상수, 일정 PHI를 정의한다(20–32). 원문: ` \* ISBDLDBC: 0 DISABLE BEDLOAD ` (16); ` \*                    1 ACTIVATE BEDLOAD OPTION. USES SEDBLBC.INP TO SPECIFY CELLS ` (18); ` \* SBDLDA: ALPHA EXPONENTIAL FOR BED LOAD FORMULA ` (20); ` \* SBDLDB: BETA EXPONENTIAL FOR BED LOAD FORMULA ` (22); ` \* SBDLDG1: GAMMA1 CONSTANT FOR BED LOAD FORMULA ` (24); ` \* SBDLDG2: GAMMA2 CONSTANT FOR BED LOAD FORMULA ` (26); ` \* SBDLDG3: GAMMA3 CONSTANT FOR BED LOAD FORMULA ` (28); ` \* SBDLDG4: GAMMA4 CONSTANT FOR BED LOAD FORMULA ` (30); ` \* SBDLDP: CONSTANT PHI FOR BED LOAD FORMULA ` (32). |
| 34–43 | 셀 면 플럭스와 하상 경사 — 소류 면 플럭스(face flux)의 풍하 방향 투영(down wind projection), 모서리 보정(corner correction)을 포함한 투영, 중앙 평균(centered averaging) 옵션을 제시한다(34–36). 역방향 하상 경사(adverse bed slope)가 양의 BLBSNT 값보다 크면 소류 수송이 일어날 수 없다고 적는다(38–40). BLBSNT=0.0이면 이 제한은 비활성이다(40). 원문: ` \* ISBLFUC: BED LOAD FACE FLUX , 0 FOR DOWN WIND PROJECTION,1 FOR DOWN WIND ` (34); ` \* WITH CORNER CORRECTION,2 FOR CENTERED AVERAGING ` (36); ` \* BLBSNT: ADVERSE BED SLOPE (POSITIVE VALUE) ACROSS A CELL FACE ABOVE ` (38); ` \* WHICH NO BED LOAD TRANSPORT CAN OCCUR. NOT ACTIVE FOR BLBSNT=0.0 ` (40). |
| 44–50 | C42a 입력 예시 — Markdown의 빈 표 머리글과 구분선(44–45), 원문의 소문자 a를 포함한 카드 및 열 이름(46), 네 자료 행의 입력 값(47–50)을 제시한다. 각 자료 행을 그대로 옮긴다. 원문: ` \| C42a \| IBEDLD \| SBDLDA \| SBDLDB \| SBDLDG1 \| SBDLDG2 \| SBDLDG3 \| SBDLDG4 \| SBDLDP \| ISBLFUC \| BLBSNT \| ` (46); ` \|  \| 1 \| 2.5 \| 0 \| 1 \| 0 \| 1 \| 0 \| 0 \| 0 \| 0.1 \| ` (47); ` \|  \| 1 \| 2.5 \| 0 \| 1 \| 0 \| 1 \| 0 \| 0 \| 0 \| 0.1 \| ` (48); ` \|  \| 1 \| 2.5 \| 0 \| 1 \| 0 \| 1 \| 0 \| 0 \| 0 \| 0.1 \| ` (49); ` \|  \| 1 \| 2.5 \| 0 \| 1 \| 0 \| 1 \| 0 \| 0 \| 0 \| 0.1 \| ` (50). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 16·46행: 소류 스위치 설명의 이름은 `ISBDLDBC`다(16). 입력 표의 이름은 `IBEDLD`다(46). 이 파일은 두 이름의 대응을 명시하지 않는다.
