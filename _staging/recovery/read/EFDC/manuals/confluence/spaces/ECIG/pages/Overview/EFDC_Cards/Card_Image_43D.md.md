---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_43D.md
lines: 51
sha256: 453824a619e8d2b778c06698b4da3943d79d745ef04a3514ccb67241c0a9efa9
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_43D.md — 판독 구간 기록

구간은 1행부터 51행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(frontmatter) — 페이지 ID 31490190(2), 제목 Card Image 43D(3), space ECIG(4), 원문 URL(5), 버전 1(6), 수정 시각 2018-01-11T07:32:11.144Z(7), 문서 경로(8)와 구분선(1·9)을 포함한다. |
| 10–26 | C43D TOXIC BULK DECAY AND BIODEGRADATION PARAMETERS — 독성물질 번호, 수주(water column)·퇴적층(sediment bed)의 전량 감쇠(bulk decay)·생분해(biodegradation) 속도와 퇴적층 내 최대 적용 깊이를 정의한다(14–26). 이름·단위 원문: `\* NTOXN: TOXIC CONTAMINANT NUMBER ID` (14); `\* TOX\_BLK\_KW: BULK DECAY RATE IN THE WATER COLUMN (1/SECOND)` (16); `\* TOX\_BLK\_KB: BULK DECAY RATE IN THE SEDIMENT BED (1/SECOND)` (18); `\* TOX\_BLK\_MXD: MAXIMUM DEPTH OF BULK DECAY IN THE SEDIMENT BED (METERS)` (20); `\* TOX\_BIO\_KW: BIODEGRADATION RATE IN THE WATER COLUMN (1/SECOND)` (22); `\* TOX\_BIO\_KB: BIODEGRADATION RATE IN THE SEDIMENT BED (1/SECOND)` (24); `\* TOX\_BIO\_MXD: MAXIMUM DEPTH OF BIODEGRADATION IN THE SEDIMENT BED (METERS)` (26). |
| 27–44 | 생분해 온도 보정 — 수주와 퇴적층의 Q10 온도 보정계수 및 기준 온도를 정의한다(28–40). 수주·퇴적층의 계수 계산식을 그대로 옮긴다(38·42). 원문: `\* TOX\_BIO\_Q10W: Q10 TEMPERATURE ADJUSTMENT COEFFICIENT FOR WATER COLUMN` (28); `\*                              BIODEGRADATION (dimensionless)` (30); `\* TOX\_BIO\_Q10B: Q10 TEMPERATURE ADJUSTMENT COEFFICIENT FOR SEDIMENT BED` (32); `\*                             BIODEGRADATION (dimensionless)` (34); `\* TOX\_BIO\_TW: REFERENCE TEMPERATURE FOR BIODEGRADATION IN WATER COLUMN (DEG C)` (36); `\*                         COEFF = TOX\_BIO\_KW(NT)\*TOX\_BIO\_Q10W(NT)^((TEM(L,K)-TOX\_BIO\_TB(NT))/10)` (38); `\* TOX\_BIO\_TB: REFERENCE TEMPERATURE FOR BIODEGRADATION IN SEDIMENT BED (DEG C)` (40); `\* COEFF = TOX\_BIO\_KB(NT)\*TOX\_BIO\_Q10B(NT)^((TEMB(L)-TOX\_BIO\_TB(NT))/10)` (42). |
| 45–51 | C43D 입력 표 — 빈 줄·표 마크업과 오염물질별 입력 행을 포함한다(45–51). 제시된 수치를 기본값으로 표시하지 않는다. 머리글·입력 행 원문: `\| C43D \| NTOXN \| BLK\_KW \| BLK\_KB \| BLK\_MXD \| BIO\_KW \| BIO\_KB \| BIO\_MXD \| Q10W \| Q10B \| BIO\_TW \| BIO\_TW \| COMMENTS \|` (48); `\|  \| 1 \| 0 \| 0 \| 100 \| 0 \| 0 \| 1 \| 1.5 \| 1.5 \| 20 \| 20 \| ! Pesticides \|` (49); `\|  \| 2 \| 0 \| 0 \| 100 \| 0 \| 0 \| 1 \| 1.5 \| 1.5 \| 20 \| 20 \| ! Polychrorinated Biphenyls 1336-36-3 \|` (50); `\|  \| 3 \| 0 \| 0 \| 100 \| 0 \| 0 \| 1 \| 1.5 \| 1.5 \| 20 \| 20 \| ! Zn \|` (51). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 36·38·40: 수주 기준 온도의 정의 이름은 `TOX\_BIO\_TW`이다(36). 수주 계수식은 온도 차에 `TOX\_BIO\_TB(NT)`를 사용한다(38). `TOX\_BIO\_TB`는 퇴적층 기준 온도로 정의된다(40).
- 40·48: 본문에는 퇴적층 기준 온도 `TOX\_BIO\_TB`가 있다(40). 표 머리글은 마지막 두 온도 열을 모두 `BIO\_TW`로 적는다(48).
- 38·42: 계수식에 사용된 `COEFF`, `NT`, `L`, `K`, `TEM(L,K)`, `TEMB(L)`의 별도 정의는 이 파일에 없다.

