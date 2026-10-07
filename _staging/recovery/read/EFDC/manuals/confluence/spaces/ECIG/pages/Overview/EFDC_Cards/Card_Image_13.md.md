---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_13.md
lines: 43
sha256: 20c2797542cddf4e5f3332d3e794708d300e1c3c17d94b40118380d849d469e1
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_13.md — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(metadata) — 페이지 ID(2), 제목(3), space(4), 원문 URL(5), 버전(6), 갱신 시각(7), 문서 계층 경로(8)를 기록한다. `---` 구분자를 포함한다(1·9). |
| 10–29 | C13 TURBULENCE CLOSURE PARAMETERS / 폐쇄 상수 — 난류 폐쇄(turbulence closure) 매개변수 제목, von Karman 상수, 보편 난류 상수들과 `Q\*Q\*L EQUATION`의 벽 함수(wall function) 상수를 설명한다(10–28). CTE4를 E4라고 부르며 때로 E3라고도 부른다는 표현을 유지했다(26). 매개변수 원문: `\* VKC: VON KARMAN CONSTANT` (14); `\* CTURB1: TURBULENT CONSTANT (UNIVERSAL)` (16); `\* CTURB2: TURBULENT CONSTANT (UNIVERSAL)` (18); `\* CTE1: TURBULENT CONSTANT (UNIVERSAL)` (20); `\* CTE2: TURBULENT CONSTANT (UNIVERSAL)` (22); `\* CTE3: TURBULENT CONSTANT (UNIVERSAL)` (24); `\* CTE4: TURBULENCE CONSTANT E4 (SOMETIMES CALL E3) WALL FUNCTION IN Q\*Q\*L EQUATION` (26); `\* CTE5: TURBULENCE CONSTANT E5 - 2ND OPEN CHANNEL WALL FUNCTION IN Q\*Q\*L EQUATION` (28). 주석용 `\*` 줄과 빈 줄을 포함한다. |
| 30–39 | C13 / 상한·하한 — 안정 조건(stable conditions)의 최대 난류 강도 Richardson 수(turbulent intensity Richardson number), 최소 난류 강도 제곱, 그 값과 길이 규모의 곱의 최소값, 최소 무차원 길이 규모를 설명한다(30–36). 상한·하한을 서로 바꾸지 않았다. 매개변수·조건 원문: `\* RIQMAX: MAXIMUM TURBULENT INTENSITY RICHARDSON NUMBER FOR STABLE CONDITIONS` (30); `\* QQMIN: MINIMUM TURBULENT INTENSITY SQUARED` (32); `\* QQLMIN: MINIMUM TURBULENT INTENSITY SQUARED \* LENGTH-SCALE` (34); `\* DMLMIN: MINIMUM DIMENSIONLESS LENGTH SCALE` (36). 주석용 `\*` 줄과 빈 줄을 포함한다(37–39). |
| 40–43 | C13 / 입력 예시 표 — 빈 표 첫 행, 구분 행, 열두 매개변수 헤더와 입력 예시를 포함한다(40–43). 예시를 기본값으로 표시하지 않았다. 입력 표 원문: `\| C13 \| VKC \| CTURB1 \| CTURB2 \| CTE1 \| CTE2 \| CTE3 \| CTE4 \| CTE5 \| RIQMAX \| QQMIN \| QQLMIN \| DMLMIN \|` (42); `\|  \| 0.4 \| 16.6 \| 10.1 \| 1.8 \| 1 \| 1.8 \| 1.33 \| 0.25 \| 0.28 \| 1.00E-08 \| 1.00E-12 \| 0.0001 \|` (43). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 26·28행: `Q\*Q\*L EQUATION`을 언급한다. 이 파일에는 기호 `Q`와 `L`의 정의가 없다.

