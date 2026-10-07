---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_25.md
lines: 42
sha256: dbdc7b022029ff9a5976fc6ff985224811c09958cdcc0eb95c76fb921abec3f1
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_25.md — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | C25 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 시간에 대해 일정한 체적 공급원(time constant volumetric source)의 일정 유입 농도(inflow concentration) 제목을 제시한다(10). 빈 줄과 주석 표식도 포함한다(11–13). 원문: ` C25 TIME CONSTANT INFLOW CONCENTRATIONS FOR TIME CONSTANT VOLUMETRIC SOURCES ` (10). |
| 14–29 | 일정 유입 농도 — 염분(salinity), 온도(temperature), 염료(dye), 패류 유생(shellfish larvae) 농도를 정의한다(14–20). 독성 오염물질(toxic contaminant) 농도 배열의 표기와 범위를 제시한다(22–24). 독성 물질 수송이 비활성일 때도 단일 기본값이 필요하다고 적는다(24–26). 원문: ` \* SAL: SALT CONCENTRATION CORRESPONDING TO INFLOW ABOVE ` (14); ` \* TEM: TEMPERATURE CORRESPONDING TO INFLOW ABOVE ` (16); ` \* DYE: DYE CONCENTRATION CORRESPONDING TO INFLOW ABOVE ` (18); ` \* SFL: SHELL FISH LARVAE CONCENTRATION CORRESPONDING TO INFLOW ABOVE ` (20); ` \* TOX: NTOX TOXIC CONTAMINANT CONCENTRATIONS CORRESPONDING TO ` (22); ` \* INFLOW ABOVE WRITTEN AS TOXC(N), N=1,NTOX A SINGLE DEFAULT ` (24); ` \* VALUE IS REQUIRED EVEN IF TOXIC TRANSPORT IS NOT ACTIVE ` (26). |
| 30–42 | C25 입력 예시 — Markdown의 빈 표 머리글과 구분선(30–31), 열 이름(32), 지점 주석이 붙은 농도 값(33–42)을 제시한다. 모든 자료 행을 그대로 옮긴다. 원문: ` \| C25 \| SAL \| TEM \| DYE \| SFL \| ! ID \| ` (32); ` \|  \| 0 \| 0 \| 0 \| 0 \| ! Sammamish River \| ` (33); ` \|  \| 0 \| 0 \| 0 \| 0 \| ! Sammamish River \| ` (34); ` \|  \| 0 \| 0 \| 0 \| 0 \| ! KingCo34a \| ` (35); ` \|  \| 0 \| 0 \| 0 \| 0 \| ! KingCo35C \| ` (36); ` \|  \| 0 \| 0 \| 0 \| 0 \| ! 12120000 \| ` (37); ` \|  \| 0 \| 0 \| 0 \| 0 \| ! KingCo37A \| ` (38); ` \|  \| 0 \| 0 \| 0 \| 0 \| ! Cedar River \| ` (39); ` \|  \| 0 \| 0 \| 0 \| 0 \| ! Cedar River \| ` (40); ` \|  \| 0 \| 0 \| 0 \| 0 \| ! Cedar River \| ` (41); ` \|  \| 0 \| 0 \| 0 \| 0 \| ! Clock \| ` (42). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 22–26·32–42행: 설명은 `TOX` 농도를 `TOXC(N), N=1,NTOX`로 쓰고 독성 물질 수송이 비활성일 때도 단일 기본값을 요구한다. 입력 표에는 `SAL`, `TEM`, `DYE`, `SFL`만 있고 독성 오염물질 농도 열과 값은 없다.
