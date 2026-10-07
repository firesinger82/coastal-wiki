---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_33.md
lines: 60
sha256: f69ec89a0200e420059c40c44e08b4c3626527195e2945f78c333bb7d336bfaf
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_33.md — 판독 구간 기록

구간은 1행부터 60행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | C33 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 유량 취수(flow withdrawal), 열 또는 물질 추가(heat or material addition), 환수(return) 자료 제목을 제시한다(10). 빈 줄과 주석 표식도 포함한다(11–13). 원문: ` C33 FLOW WITHDRAWAL, HEAT OR MATERIAL ADDITION, AND RETURN DATA ` (10). |
| 14–31 | 취수·환수 위치와 유량 — 상류·취수 셀 및 층, 하류·환수 셀 및 층의 인덱스(index)를 설명한다(14–24). 일정 체적 유량(constant volume flow rate)과 연결 취수·환수 유량 및 농도 증가 시계열(concentration rise time series)의 식별자를 정의한다(26–30). 원문: ` \* IWRU: I INDEX OF UPSTREAM OR WITHDRAWAL CELL ` (14); ` \* JWRU: J INDEX OF UPSTREAM OR WITHDRAWAL CELL ` (16); ` \* KWRU: K INDEX OF UPSTREAM OR WITHDRAWAL LAYER ` (18); ` \* IWRD: I INDEX OF DOWNSTREAM OR RETURN CELL ` (20); ` \* JWRD: J INDEX OF DOWNSTREAM OR RETURN CELL ` (22); ` \* KWRD: J INDEX OF DOWNSTREAM OR RETURN LAYER ` (24); ` \* QWRE: CONSTANT VOLUME FLOW RATE FROM WITHDRAWAL TO RETURN ` (26); ` \* NQWRSERQ: ID NUMBER OF ASSOCIATED VOLUMN WITHDRAWAL-RETURN FLOW AND ` (28); ` \* CONCENTRATION RISE TIME SERIES ` (30). |
| 32–51 | 운동량 플럭스(momentum flux) — 취수와 환수 각각의 스위치가 0이 아니면 운동량 플럭스를 고려한다(32·42). 두 스위치의 1–4 옵션은 음·양의 U면과 V면을 구분한다(34–40·44–50). 원문: ` \* NQWRMFU: IF NON ZERO ACCOUNT FOR WITHDRAWAL FLOW MOMENTUM FLUX ` (32); ` \*                  = 1 MOMENTUM FLUX ON NEG U FACE ` (34); ` \*                  = 2 MOMENTUM FLUX ON NEG V FACE ` (36); ` \*                  = 3 MOMENTUM FLUX ON POS U FACE ` (38); ` \*                  = 4 MOMENTUM FLUX ON POS V FACE ` (40); ` \* NQWRMFD: IF NON ZERO ACCOUNT FOR RETURN FLOW MOMENTUM FLUX ` (42); ` \*                 = 1 MOMENTUM FLUX ON NEG U FACE ` (44); ` \*                 = 2 MOMENTUM FLUX ON NEG V FACE ` (46); ` \*                 = 3 MOMENTUM FLUX ON POS U FACE ` (48); ` \*                 = 4 MOMENTUM FLUX ON POS V FACE ` (50). |
| 52–59 | 폭과 각도 — 상류 및 하류 운동량 플럭스 폭(width)은 m 단위다(52·54). 환수 운동량 플럭스의 수평 각도(horizontal angle)를 설명한다(56). 원문: ` \* BQWRMFU: UPSTREAM MOMENTUM FLUX WIDTH (m) ` (52); ` \* BQWRMFD: DOWNSTREAM MOMENTUM FLUX WIDTH (m) ` (54); ` \* ANGWRMFD: ANGLE FOR HORIZONTAL FOR RETURN FLOW MOMENTUM FLUX ` (56). |
| 60–60 | C33 입력 형식 — 입력 열 이름만 제시한다(60). 파일은 이 줄에서 끝난다. 원문: ` C33 IWRU  JWRU  KWRU  IWRD  JWRD  KWRD  QWRE  NQW\_RQ  NQWR\_U  NQWR\_D  BQWR\_U  BQWR\_D  ANG\_D ` (60). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 18·24행: 상류 층 항목 `KWRU`는 `K INDEX`라고 적는다. 하류 층 항목 `KWRD`는 `J INDEX`라고 적는다.
- 28·32·42·52·54·56·60행: 설명은 `NQWRSERQ`, `NQWRMFU`, `NQWRMFD`, `BQWRMFU`, `BQWRMFD`, `ANGWRMFD`를 사용한다. 입력 열 이름은 `NQW\_RQ`, `NQWR\_U`, `NQWR\_D`, `BQWR\_U`, `BQWR\_D`, `ANG\_D`를 사용한다. 이 파일은 두 표기의 대응을 명시하지 않는다.
