---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_10.md
lines: 31
sha256: 0dd1979fde5b04e082cffb3c4dfda3dac60d4b75670532ac216695558fa4bc72
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_10.md — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(metadata) — 페이지 ID(2), 제목(3), space(4), 원문 URL(5), 버전(6), 갱신 시각(7), 문서 계층 경로(8)를 기록한다. `---` 구분자를 포함한다(1·9). |
| 10–23 | C10 LAYER THICKNESS IN VERTICAL — 층 번호(layer number)와 무차원 층 두께(dimensionless layer thickness)를 설명한다(10–16). 층 두께의 합은 1.0이어야 한다(16). 매개변수·범위·조건 원문: `\* K: LAYER NUMBER, K=1,KC` (14); `\* DZC: DIMENSIONLESS LAYER THICKNESS (THICKNESSES MUST SUM TO 1.0)` (16). 제목, 주석용 `\*` 줄과 빈 줄을 포함한다(10–23). |
| 24–31 | C10 / 입력 예시 표 — 비어 있는 표 첫 행과 구분 행을 포함한다(24–25). `K`와 `DZC` 헤더 및 K=1부터 K=5까지 각각 두께 0.2000인 예시를 적는다(26–31). 예시를 기본값으로 표시하지 않았다. 입력 표 원문: `\| C10 \| K \| DZC \|` (26); `\|  \| 1 \| 0.2000 \|` (27); `\|  \| 2 \| 0.2000 \|` (28); `\|  \| 3 \| 0.2000 \|` (29); `\|  \| 4 \| 0.2000 \|` (30); `\|  \| 5 \| 0.2000 \|` (31). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14행: 층 번호 범위는 `K=1,KC`이다. 이 파일에는 `KC`의 정의나 값이 없다.

