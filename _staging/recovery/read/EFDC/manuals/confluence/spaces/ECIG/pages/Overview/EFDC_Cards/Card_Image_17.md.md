---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_17.md
lines: 46
sha256: ccdc0dfe20574cd50f3f2729cb65c73d3308a126e71f653c8afe0bebd7e1517e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_17.md — 판독 구간 기록

구간은 1행부터 46행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(metadata) — 페이지 ID(2), 제목(3), space(4), 원문 URL(5), 버전(6), 갱신 시각(7), 문서 계층 경로(8)를 기록한다. `---` 구분자를 포함한다(1·9). |
| 10–25 | C17 PERIODIC FORCING (TIDAL) SURF ELEV OR PRESSURE BOUNDARY COND. FORCINGS / 번호·기호·진폭·위상 — 주기 조석 강제력(periodic tidal forcing)의 경계 수면 높이(surface elevation) 또는 압력(pressure) 절 제목을 적는다(10). `NPFOR`는 강제력 번호이며 `SYMBOL`은 여기에서 참조용으로만 쓴다(14–16). `NPFORT=0`의 `AMPLITUDE`는 M 단위이며 압력은 `RHO\*G`로 나눈다(18). 같은 조건의 `PHASE`는 TBEGIN에 대한 초 단위 위상(forcing phase)이다(22). `NPFORT.GE.1`에서는 코사인 진폭(cosine amplitude)과 사인 진폭(sine amplitude)을 적는다(20·24). 매개변수·단위·조건 원문: `\* NPFOR: FORCING NUMBER` (14); `\* SYMBOL: FORCING SYMBOL (FOR REFERENCE HERE ONLY)` (16); `\* AMPLITUDE: AMPLITUDE IN M (PRESSURE DIVIDED BY RHO\*G), NPFORT=0` (18); `\* COSINE AMPLITUDE IN M, NPFORT.GE.1` (20); `\* PHASE: FORCING PHASE RELATIVE TO TBEGIN IN SECONDS, NPFORT=0` (22); `\* SINE AMPLITUDE IN M, NPFORT.GE.1` (24). 주석용 `\*` 줄과 빈 줄을 포함한다. |
| 26–35 | C17 / 강제력 형식별 입력 조건 — `NPFORT=0`은 단일 진폭과 위상을 읽는다(26). `NPFORT=1`은 각 강제력의 상수·선형 코사인 및 사인 진폭을 읽으며, `NPFORT=2`는 상수·선형·이차 코사인 및 사인 진폭을 읽는 것으로 적는다(26–32). 조건 원문: `\* NOTE: FOR NPFORT=0 SINGLE AMPLITUDE AND PHASE ARE READ, FOR NPFORT=1` (26); `\* CONST AND LINEAR COS AND SIN AMPS ARE READ FOR EACH FORCING, FOR` (28); `\* NPFORT=2, CONST, LINEAR, QUAD COS AND SIN AMPS ARE READ FOR EACH` (30); `\* FOR EACH FORCING` (32). 원문의 마지막 `FOR EACH FORCING` 반복을 유지했다(32). 주석용 `\*` 줄과 빈 줄을 포함한다(33–35). |
| 36–46 | C17 / 입력 예시 표 — 빈 표 첫 행, 구분 행, `NPFOR`, `SYMBOL`, `AMPLITUDE`, `PHASE` 헤더 및 여덟 조석 성분의 입력 예시를 포함한다(36–46). 위상 값을 다른 단위로 바꾸지 않았다. 예시를 기본값으로 표시하지 않았다. 입력 표 원문: `\| C17 \| NPFOR \| SYMBOL \| AMPLITUDE \| PHASE \|` (38); `\|  \| 1 \| 'Q1' \| 0.04 \| 126.073 \|` (39); `\|  \| 1 \| 'O1' \| 0.261 \| 146.432 \|` (40); `\|  \| 1 \| 'P1' \| 0.097 \| 182.577 \|` (41); `\|  \| 1 \| 'K1' \| 0.293 \| 185.991 \|` (42); `\|  \| 1 \| 'N2' \| 0.04 \| 59.376 \|` (43); `\|  \| 1 \| 'M2' \| 0.185 \| 75.861 \|` (44); `\|  \| 1 \| 'S2' \| 0.072 \| 114.865 \|` (45); `\|  \| 1 \| 'K2' \| 0.025 \| 95.187 \|` (46). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 18·20·22·24·26–32행: 이 파일에는 압력 환산의 `RHO`·`G`, 위상 기준 `TBEGIN`, 입력 형식 조건 `NPFORT`의 정의가 없다.

