---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_23.md
lines: 45
sha256: a1622225ed3133ba07699b1f3dcce21e59e4bb2073ada004da583856205c44a1
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_23.md — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | C23 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 속도(velocity), 체적 공급원·흡수원(volume source/sink), 유량 제어(flow control), 취수·환수(withdrawal/return) 자료 제목을 제시한다(10). 빈 줄과 주석 표식도 포함한다(11–13). 원문: ` C23 VELOCITY, VOLUMN SOURCE/SINK, FLOW CONTROL, AND WITHDRAWAL/RETURN DATA ` (10). |
| 14–29 | 공급원·흡수원과 제어 자료 수 — 상수 또는 시계열로 지정한 위치 수, 제트·플룸(jet/plume)으로 처리할 공급원 위치 수, 체적 시계열 수를 정의한다(14–22). 압력 제어(pressure controlled) 취수·환수 쌍과 표, 수리 구조물(hydraulic structure) 정의의 수를 제시한다(24–28). 원문: ` \* NQSIJ: NUMBER OF CONSTANT AND/OR TIME SERIES SPECIFIED SOURCE/SINK ` (14); ` \* LOCATIONS (RIVER INFLOWS,ETC) . ` (16); ` \* NQJPIJ: NUMBER OF CONSTANT AND/OR TIME SERIES SPECIFIED SOURCE ` (18); ` \* LOCATIONS TREATED AS JETS/PLUMES . ` (20); ` \* NQSER: NUMBER OF VOLUME SOURCE/SINK TIME SERIES ` (22); ` \* NQCTL: NUMBER OF PRESSURE CONTROLED WITHDRAWAL/RETURN PAIRS ` (24); ` \* NQCTLT: NUMBER OF PRESSURE CONTROLED WITHDRAWAL/RETURN TABLES ` (26); ` \* NHYDST: NUMBER OF HYDRAULIC STRUCTURE DEFINITIONS ` (28). |
| 30–41 | 취수·환수 및 진단 — 상수 또는 시계열 취수·환수 쌍 수와 취수·환수·농도 증가(concentration rise) 시계열 수를 설명한다(30–36). 진단 파일을 쓰는 조건과 파일명을 제시한다(38). 원문: ` \* NQWR: NUMBER OF CONSTANT OR TIME SERIES SPECIFIED WITHDRAWL/RETURN ` (30); ` \* PAIRS ` (32); ` \* NQWRSR: NUMBER OF TIME SERIES SPECIFYING WITHDRAWL,RETURN AND ` (34); ` \* CONCENTRATION RISE SERIES ` (36); ` \* ISDIQ: SET TO 1 TO WRITE DIAGNOSTIC FILE, DIAQ.OUT ` (38). |
| 42–45 | C23 입력 예시 — Markdown의 빈 표 머리글과 구분선(42–43), 열 이름(44), 입력 값(45)을 제시한다. 원문: ` \| C23 \| NQSIJ \| NQJPIJ \| NQSER \| NQCTL \| NQCTLT \| NHYDST \| NQWR \| NQWRSR \| ISDIQ \| ` (44); ` \|  \| 3 \| 0 \| 1 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| ` (45). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
