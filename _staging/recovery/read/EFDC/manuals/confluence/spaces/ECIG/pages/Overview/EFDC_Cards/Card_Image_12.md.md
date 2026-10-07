---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_12.md
lines: 41
sha256: 491a6f169d6f8246ddc23fcb19fdfe37da5028a1bc9bf7118c4f0ebd54f7b90e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_12.md — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(metadata) — 페이지 ID(2), 제목(3), space(4), 원문 URL(5), 버전(6), 갱신 시각(7), 문서 계층 경로(8)를 기록한다. `---` 구분자를 포함한다(1·9). |
| 10–25 | C12 TURBULENT DIFFUSION PARAMETERS / 확산·점성 — 상수 수평 운동량·질량 확산계수(diffusivity), 무차원 수평 운동량 확산계수, 배경 점성(viscosity)·확산계수, 와점성(eddy viscosity)과 와확산계수(eddy diffusivity)의 최대값을 설명한다(14–24). 단위 표기 `m\*m/s`와 `AHD` 적용 조건을 그대로 옮겼다. 매개변수·단위·조건 원문: `\* AHO: CONSTANT HORIZONTAL MOMENTUM AND MASS DIFFUSIVITY m\*m/s` (14); `\* AHD: DIMESIONLESS HORIZONTAL MOMENTUM DIFFUSIVITY (ONLY FOR ISHDMF>0)` (16); `\* AVO: BACKGROUND, CONSTANT OR EDDY (KINEMATIC) VISCOSITY m\*m/s` (18); `\* ABO: BACKGROUND, CONSTANT OR MOLECULAR DIFFUSIVITY m\*m/s` (20); `\* AVMX: MAXIMUM KINEMATIC EDDY VISCOSITY m\*m/s (DS-INTL)` (22); `\* ABMX: MAXIMUM EDDY DIFFUSIVITY m\*m/s (DS-INTL)` (24). 제목, 주석용 `\*` 줄과 빈 줄을 포함한다(10–25). |
| 26–37 | C12 / 유동성 진흙·수직 설정·측벽 — 유동성 진흙(fluid mud)의 상수 점성, `AVCON`을 0으로 둘 때의 상수 수직 점성·확산계수와 그 외의 값, 측벽(side wall) 로그 법칙 거칠기 및 적용 조건을 설명한다(26–34). `AVCON=0`이면 AVO·ABO와 같게 정하며 그렇지 않으면 1.0으로 두는 설명이다(28–30). 매개변수·단위·조건 원문: `\* VISMUD: CONSTANT FLUID MUD VISCOSITY m\*m/s` (26); `\* AVCON: EQUALS ZERO FOR CONSTANT VERTICAL VISCOSITY AND DIFFUSIVITY` (28); `\* WHICH ARE SET EQUAL TO AVO AND ABO, OTHERWISE SET TO 1.0` (30); `\* ZBRWALL: SIDE WALL LOG LAW ROUGHNESS HEIGHT. USED WHEN HORIZONTAL` (32); `\* MOMENTUM DIFFUSION IS ACTIVE AND AHO OR AHD ARE NONZERO` (34). 주석용 `\*` 줄과 빈 줄을 포함한다(35–37). |
| 38–41 | C12 / 입력 예시 표 — 빈 표 첫 행, 구분 행, 매개변수 헤더 및 입력 예시를 포함한다(38–41). 예시를 기본값으로 표시하지 않았다. 입력 표 원문: `\| C12 \| AHO \| AHD \| AVO \| ABO \| AVMX \| ABMX \| VISMUD \| AVCON \| ZBRWALL \|` (40); `\|  \| 0 \| 0.025 \| 0.000001 \| 1.00E-07 \| 0.000001 \| 1.00E-07 \| 0 \| 1 \| 0.002 \|` (41). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 16행: AHD의 적용 조건은 `ISHDMF>0`이다. 이 파일에는 `ISHDMF`의 정의나 값이 없다.

