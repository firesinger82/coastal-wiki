---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_14.md
lines: 49
sha256: 2509ede6e2b9fe1d7c029e878622719141b934ddd2050a0446b92c155c234b84
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_14.md — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(metadata) — 페이지 ID(2), 제목(3), space(4), 원문 URL(5), 버전(6), 갱신 시각(7), 문서 계층 경로(8)를 기록한다. `---` 구분자를 포함한다(1·9). |
| 10–25 | C14 TIDAL & ATMOSPHERIC FORCING, GROUND WATER AND SUBGRID CHANNEL PARAMETERS / 강제력 수·지하수·수로 — 주기 조석 강제력(tidal forcing) 성분 수, 바람·대기 조건 시계열(time series) 수와 0의 의미, 토양 수분 수지(soil moisture balance)·지하수 상호작용(groundwater interaction) 선택, 하위 격자 수로(subgrid channel) 활성화와 입력 파일 읽기 조건을 설명한다(14–24). 매개변수·조건 원문: `\* MTIDE: NUMBER OF PERIOD (TIDAL) FORCING CONSTITUENTS` (14); `\* NWSER: NUMBER OF WIND TIME SERIES (0 SETS WIND TO ZERO)` (16); `\* NASER: NUMBER OF ATMOSPHERIC CONDITION TIME SERIES (0 SETS ALL ZERO)` (18); `\* ISGWIT: 1 TO ACTIVATE SOIL MOISTURE BALANCE WITH DRYING AND WETTING` (20); `\* 2 TO ACTIVATE GROUNDWATER INTERACTION WITH BED AND WATER COL` (22); `\* ISCHAN: >0 ACTIVATE SUBGRID CHANNEL MODEL AND READ MODCHAN.INP` (24). 제목, 주석용 `\*` 줄과 빈 줄을 포함한다. |
| 26–44 | C14 / 파랑·자료 동화·침투·체적력 — `ISWAVE`의 1·2·3·4 옵션은 경계층(boundary layer), 흐름(current), 외부 입력 파일 또는 내부 계산 바람 파랑(wind wave)의 영향 범위를 나누어 적는다(26–32). 조석 수위 자료 동화(tidal elevation assimilation)는 비활성으로 적는다(34). 건조 셀 초과 물의 침투 또는 제거, 외부 모드(external mode) 체적력(body force)의 수심 균일·표면층 조건과 준비정수압(quasi-nonhydrostatic) 옵션을 설명한다(36–42). 매개변수·조건 원문: `\* ISWAVE: 1-FOR BOUNDARY LAYER IMPACTS ONLY (WAVEBL.INP),` (26); `\* 2-FOR BOUNDARY LAYER & CURRENT IMPACTS (WVnnn.INP)` (28); `\* 3-FOR INTERNALLY COMPUTED WIND WAVE BOUNDARY LAYER IMPACTS (DSI)` (30); `\* 4-FOR INTERNALLY COMPUTED WIND WAVE BOUNDARY LAYER AND CURRENT IMPACTS (DSI)` (32); `\* ITIDASM: 1 FOR TIDAL ELEVATION ASSIMILATION (NOT ACTIVE)` (34); `\* ISPERC: 1 TO PERCOLATE OR ELIMINATE EXCESS WATER IN DRY CELLS` (36); `\* ISBODYF: TO INCLUDE EXTERNAL MODE BODY FORCES FROM FBODY.INP` (38); `\* 1 FOR UNIFORM OVER DEPTH, 2 FOR SURFACE LAYER ONLY` (40); `\* ISPNHYDS: 1 FOR QUASI-NONHYDROSTATIC OPTION` (42). 주석용 `\*` 줄을 포함한다(44). |
| 45–49 | C14 / 입력 예시 표 — 빈 줄, 빈 표 첫 행, 구분 행, 열 개 매개변수 헤더와 입력 예시를 포함한다(45–49). 예시를 기본값으로 표시하지 않았다. 입력 표 원문: `\| C14 \| MTIDE \| NWSER \| NASER \| ISGWIT \| ISCHAN \| ISWAVE \| ITIDASM \| ISPERC \| ISBODYF \| ISPNHYDS \|` (48); `\|  \| 0 \| 1 \| 1 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \|` (49). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음

