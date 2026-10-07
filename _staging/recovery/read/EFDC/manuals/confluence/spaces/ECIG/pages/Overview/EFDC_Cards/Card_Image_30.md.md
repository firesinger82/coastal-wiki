---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_30.md
lines: 33
sha256: c796e9433bfd57f6046656eae5be508114ca5e2ffa08973306c028dc9d7a9add
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_30.md — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | C30 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 시간에 대해 일정한 제트·플룸 공급원(time constant jet/plume source)의 일정 유입 농도(inflow concentration) 제목을 제시한다(10). 빈 줄과 주석 표식도 포함한다(11–13). 원문: ` C30 TIME CONSTANT INFLOW CONCENTRATIONS FOR TIME CONSTANT JET/PLUME SOURCES ` (10). |
| 14–29 | 일정 유입 농도 — 염분(salinity), 온도(temperature), 염료(dye), 패류 유생(shellfish larvae) 농도를 정의한다(14–20). 독성 오염물질(toxic contaminant) 농도 배열의 표기와 범위를 제시한다(22–24). 독성 물질 수송이 비활성일 때도 단일 기본값이 필요하다고 적는다(24–26). 원문: ` \* SAL: SALT CONCENTRATION CORRESPONDING TO INFLOW ABOVE ` (14); ` \* TEM: TEMPERATURE CORRESPONDING TO INFLOW ABOVE ` (16); ` \* DYE: DYE CONCENTRATION CORRESPONDING TO INFLOW ABOVE ` (18); ` \* SFL: SHELL FISH LARVAE CONCENTRATION CORRESPONDING TO INFLOW ABOVE ` (20); ` \* TOX: NTOX TOXIC CONTAMINANT CONCENTRATIONS CORRESPONDING TO ` (22); ` \*          INFLOW ABOVE WRITTEN AS TOXC(N), N=1,NTOX A SINGLE DEFAULT ` (24); ` \*          VALUE IS REQUIRED EVEN IF TOXIC TRANSPORT IS NOT ACTIVE ` (26). |
| 30–33 | C30 입력 예시 — Markdown의 빈 표 머리글과 구분선(30–31), 열 이름(32), Jet/Plume 주석이 붙은 입력 값(33)을 제시한다. 원문: ` \| C30 \| SAL \| TEM \| DYE \| SFL \| ! ID \| ` (32); ` \|  \| 0 \| 0 \| 0 \| 0 \| ! Jet/Plume \| ` (33). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 22–26·32–33행: 설명은 `TOX` 농도를 `TOXC(N), N=1,NTOX`로 쓰고 독성 물질 수송이 비활성일 때도 단일 기본값을 요구한다. 입력 표에는 `SAL`, `TEM`, `DYE`, `SFL`만 있고 독성 오염물질 농도 열과 값은 없다.
