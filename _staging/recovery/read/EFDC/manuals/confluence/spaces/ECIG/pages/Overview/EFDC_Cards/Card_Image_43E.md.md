---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_43E.md
lines: 35
sha256: cec487f541f72cde185cbf6bec609619dc9767b5f09fbbe92aea7d02a99873af
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_43E.md — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(frontmatter) — 페이지 ID 31784987(2), 제목 Card Image 43E(3), space ECIG(4), 원문 URL(5), 버전 1(6), 수정 시각 2018-01-11T07:39:56.766Z(7), 문서 경로(8)와 구분선(1·9)을 포함한다. |
| 10–28 | C43E TOXIC VOLATILIZATION PARAMETERS — 독성물질의 휘발(volatilization)에 사용하는 번호, 분자량(molecular weight), Henry 법칙 계수(Henry's law coefficient), 물질 전달 온도 계수(mass transfer temperature coefficient), 대기 농도와 조정 인자를 정의한다(14–26). 온도 보정의 거듭제곱식도 제시한다(22). 이름·단위·식 원문: `\* NTOXN: TOXIC CONTAMINANT NUMBER ID` (14); `\* TOX\_MW: MOLECULAR WEIGHT (G/MOLE)` (16); `\* TOX\_HE: HENRY'S LAW COEFFICIENT FOR THE TOXIC (ATM-M3/MOLE)` (18); `\* TOX\_KV\_TCOEFF: MASS TRANSFER TEMPERATURE COEFFICIENT (DIMENSIONLESS)` (20); `\*                                 TOX\_KV\_TCOEFF\*\*(TEM(L,KC)-20)` (22); `\* TOX\_ATM: ATMOSPHERIC CONCENTRATION OF TOXIC (micro G/L)` (24); `\* TOX\_VOL\_ADJ: ADJUSTMENT FACTOR (DIMENSIONLESS)` (26). |
| 29–35 | C43E 입력 표 — 빈 줄·표 마크업과 오염물질별 입력 행을 포함한다(29–35). 제시된 수치를 기본값으로 표시하지 않는다. 머리글·입력 행 원문: `\| C43E \| NTOXN \| TOX\_MW \| TOX\_HE \| TCOEFF \| ATM \| VOL\_ADJ \| COMMENTS \|` (32); `\|  \| 1 \| 0 \| 0 \| 1.069 \| 0 \| 1 \| ! Pesticides \|` (33); `\|  \| 2 \| 0 \| 0 \| 1.069 \| 0 \| 1 \| ! Polychrorinated Biphenyls 1336-36-3 \|` (34); `\|  \| 3 \| 0 \| 0 \| 1.069 \| 0 \| 1 \| ! Zn \|` (35). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 22: 온도 보정식은 `TEM(L,KC)`를 사용한다. 이 파일에는 `TEM`, `L`, `KC`의 별도 정의가 없다.

