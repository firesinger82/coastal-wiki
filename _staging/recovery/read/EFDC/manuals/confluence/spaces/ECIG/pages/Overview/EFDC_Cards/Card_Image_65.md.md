---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_65.md
lines: 28
sha256: 33c38641f41574d794c913b3f170bd1d2faae2815b52c317e4c0ad4cede7cb39
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_65.md — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 원문 메타데이터(frontmatter) — 문서 ID·제목·space·URL·버전·갱신 시각·계층 경로를 적는다(1–9). |
| 10–26 | C65 TIME CONSTANT SURFACE CONC ON NORTH CONC BOUNDARIES — 북측 농도 경계(concentration boundary)의 시간 불변 표층(surface layer) 유입 염분(salinity)·수온(temperature)·염료(dye)·패류 유생(shellfish larvae)·독성 오염물질(toxic contaminant) 농도를 설명한다(10–24). 독성 오염물질은 `NTOX`개 값을 나열한다(22–24). 원문은 표층을 `SURFAC`으로 적는다(14–22). 주석 표식과 빈 줄을 포함한다(11–26). 원문: `C65 TIME CONSTANT SURFACE CONC ON NORTH CONC BOUNDARIES` (10); `\* SAL: ULTIMATE INFLOWING SURFAC LAYER SALINITY` (14); `\* TEM: ULTIMATE INFLOWING SURFAC LAYER TEMPERATURE` (16); `\* DYE: ULTIMATE INFLOWING SURFAC LAYER DYE CONCENTRATION` (18); `\* SFL: ULTIMATE INFLOWING SURFAC LAYER SHELLFISH LARVAE CONCENTRAION` (20); `\* TOX: NTOX ULTIMATE INFLOWING SURFAC LAYER TOXIC CONTAMINANT` (22); `\*          CONCENTRATIONS NTOX VALUES TOX(N), N=1,NTOX` (24). |
| 27–28 | C65 입력 열 제목 — 염분·수온·염료·패류 유생 열을 제시한다(28). 앞 빈 줄을 포함한다(27). 원문: `C65 SAL TEM DYE SFL` (28). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 22–24·28행: `TOX` 설명은 있으나 마지막 입력 열 제목 `C65 SAL TEM DYE SFL`에는 `TOX`가 없다.

