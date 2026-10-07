---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_87.md
lines: 40
sha256: 3b4d378e32d2dfc9a60eb2e2be0d53e370a6a981e3e4393e1e1ae6e45732d1e2
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_87.md — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 원문 메타데이터(frontmatter) — 문서 ID·제목·space·URL·버전·갱신 시각·계층 경로를 적는다(1–9). |
| 10–24 | C87 CONTROLS FOR WRITING TO TIME SERIES FILES / 위치·스칼라·혼합 — 시계열(time series) 출력 위치의 I·J 셀 첨자(cell index)와 위치별 출력 시나리오를 정의한다(14–18). 수면 표고(surface elevation)·수송 농도 변수(transported concentration variable)·와점성(eddy viscosity) 및 확산계수(diffusivity) 시계열의 활성화 조건을 적는다(20–24). 주석 표식과 빈 줄을 포함한다(11–24). 원문: `C87 CONTROLS FOR WRITING TO TIME SERIES FILES` (10); `\* ILTS: I CELL INDEX` (14); `\* JLTS: J CELL INDEX` (16); `\* NTSSSS: WRITE SCENARIO FOR THIS LOCATION` (18); `\* MTSP: 1 FOR TIME SERIES OF SURFACE ELEVATION` (20); `\* MTSC: 1 FOR TIME SERIES OF TRANSPORTED CONCENTRATION VARIABLES` (22); `\* MTSA: 1 FOR TIME SERIES OF EDDY VISCOSITY AND DIFFUSIVITY` (24). |
| 25–38 | C87 CONTROLS FOR WRITING TO TIME SERIES FILES / 속도·수송·체적·문자 위치 — 외부 모드(external mode) 수평 속도(horizontal velocity)·수평 수송(horizontal transport)·모든 층의 수평 속도 시계열 옵션을 적는다(26–30). 두 매개변수 모두 순 외부 모드 체적 생성·소멸(net external mode volume source/sink) 시계열이라고 적는다(32–34). 위치를 문자 변수(character variable)로 지정한다고 적는다(36). 주석 표식과 빈 줄을 포함한다(25–38). 원문: `\* MTSUE: 1 FOR TIME SERIES OF EXTERNAL MODE HORIZONTAL VELOCITY` (26); `\* MTSUT: 1 FOR TIME SERIES OF EXTERNAL MODE HORIZONTAL TRANSPORT` (28); `\* MTSU: 1 FOR TIME SERIES OF HORIZONTAL VELOCITY IN EVERY LAYER` (30); `\* MTSQE: 1 FOR TIME SERIES OF NET EXTERNAL MODE VOLUME SOURCE/SINK` (32); `\* MTSQ: 1 FOR TIME SERIES OF NET EXTERNAL MODE VOLUME SOURCE/SINK` (34); `\* CLTS: LOCATION AS A CHARACTER VARIALBLE` (36). |
| 39–40 | C87 입력 열 제목 — 위치·시나리오·각 출력 활성화·문자 위치의 열 제목을 제시한다(40). 앞 빈 줄을 포함한다(39). 원문: `C87 ILTS JLTS NTSSSS MTSP MTSC MTSA MTSUE MTSUT MTSU MTSQE MTSQ CLTS` (40). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 32–34행: `MTSQE`와 `MTSQ`의 설명은 모두 `1 FOR TIME SERIES OF NET EXTERNAL MODE VOLUME SOURCE/SINK`로 적혀 있다. 두 설정의 차이를 이 파일에서 설명하지 않는다.

