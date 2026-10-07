---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_43B.md
lines: 49
sha256: aa3d5c31bf487e7860647fcb5c86ce6e56da2fc956d98f02487ba3ffc7d52c9c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_43B.md — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(frontmatter) — 페이지 ID 31686682(2), 제목 Card Image 43B(3), space ECIG(4), 원문 URL(5), 버전 1(6), 수정 시각 2018-01-11T03:38:37.169Z(7), 문서 경로(8)와 구분선(1·9)을 포함한다. |
| 10–14 | C43B TOXIC KINETIC OPTION FLAGS — 독성물질 반응 속도론(toxic kinetics)의 옵션과 오염물질 번호를 소개한다(10·14). 번호 정의 원문: `\* NTOXN: TOXIC CONTAMINANT NUMBER ID` (14). |
| 15–28 | 전량 감쇠(bulk decay)·생분해(biodegradation)·휘발(volatilization) 옵션 — 수주(water column)와 퇴적물(sediment)의 전량 감쇠·생분해 사용 여부를 지정한다(16–22). 휘발 옵션은 사용하지 않거나 하천·호소 조건에서 사용하며 호소 계산법 두 가지를 구별한다(24–28). 옵션 원문: `\* ITOXKIN(1): 0 DO NOT USE BULK DECAY` (16); `\*                  : 1 USE BULK DECAY FOR WATER COLUMN AND SEDIMENT` (18); `\* ITOXKIN(2): 0 DO NOT USE BIODEGRADATION` (20); `\*                  : 1 USE BIODEGRADATION FOR WATER COLUMN AND SEDIMENT` (22); `\* ITOXKIN(3): 0 DO NOT USE VOLATILIZATION` (24); `\*                  : 1 USE VOLATILIZATION FOR RIVER AND LAKE CONDITIONS. LAKE USES O'CONNOR` (26); `\*                  : 2 USE VOLATILIZATION FOR RIVER AND LAKE CONDITIONS. LAKE USES MACKAY & YEUN` (28). |
| 29–42 | 미구현 옵션 — 광분해(photolysis), 가수분해(hydrolysis), 생성물(daughter products)의 사용 여부를 열거하며 모든 해당 선택에 NOT IMPLEMENTED를 표시한다(30–40). 원문: `\* ITOXKIN(4): 0 DO NOT USE PHOTOLYSIS (NOT IMPLEMENTED)` (30); `\*                  : 1 USE PHOTOLYSIS FOR WATER COLUMN (NOT IMPLEMENTED)` (32); `\* ITOXKIN(5): 0 DO NOT USE HYDROLYSIS (NOT IMPLEMENTED)` (34); `\*                  : 1 USE HYDROLYSIS FOR WATER COLUMN (NOT IMPLEMENTED)` (36); `\* ITOXKIN(6): 0 DO NOT USE DAUGHTER PRODUCTS (NOT IMPLEMENTED)` (38); `\*                  : 1 USE DAUGHTER PRODUCTS (NOT IMPLEMENTED)` (40). |
| 43–49 | C43B 입력 표 — 표 마크업과 오염물질별 입력 행을 포함한다(43–49). 여섯 반응 옵션의 제시값은 각 행에서 모두 0이다(47–49). 기본값 표시는 없다. 머리글·입력 행 원문: `\| C43B \| NTOXN \| KIN(1) \| KIN(2) \| KIN(3) \| KIN(4) \| KIN(5) \| KIN(6) \| COMMENTS \|` (46); `\|  \| 1 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| ! Pesticides \|` (47); `\|  \| 2 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| ! Polychrorinated Biphenyls 1336-36-3 \|` (48); `\|  \| 3 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| ! Zn \|` (49). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 16–40·46: 본문 매개변수 이름은 `ITOXKIN(1)`부터 `ITOXKIN(6)`까지이다. 표 머리글은 `KIN(1)`부터 `KIN(6)`까지이다. 이 파일에는 두 표기의 대응 설명이 없다.

