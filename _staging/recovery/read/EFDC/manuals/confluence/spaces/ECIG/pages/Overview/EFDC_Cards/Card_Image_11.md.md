---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_11.md
lines: 45
sha256: aa99bc3aebb291373b4333ec201d41576139adf51f594669eb6a7b92db913011
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_11.md — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(metadata) — 페이지 ID(2), 제목(3), space(4), 원문 URL(5), 버전(6), 갱신 시각(7), 문서 계층 경로(8)를 기록한다. `---` 구분자를 포함한다(1·9). |
| 10–25 | C11 GRID, ROUGHNESS AND DEPTH PARAMETERS / 격자·거칠기 — X 또는 I 방향 셀 길이(cell length), Y 또는 J 방향 셀 길이, 두 길이를 미터로 바꾸는 배율, 별도 격자 파일 읽기 조건과 로그 경계층(log boundary layer)의 거칠기 높이 조정·환산을 설명한다(14–24). 이름·조건·단위 원문: `\* DX: CARTESIAN CELL LENGTH IN X OR I DIRECTION` (14); `\* DY: CARTESION CELL LENGTH IN Y OR J DIRECTION` (16); `\* DXYCVT: MULTIPLY DX AND DY BY TO OBTAIN METERS` (18); `\* IMDXDY: GREATER THAN 0 TO READ MODDXDY.INP FILE` (20); `\* ZBRADJ: LOG BDRY LAYER CONST OR VARIABLE ROUGH HEIGHT ADJ IN METERS` (22); `\* ZBRCVRT: LOG BDRY LAYER VARIABLE ROUGHNESS HEIGHT CONVERT TO METERS` (24). 제목, 주석용 `\*` 줄과 빈 줄을 포함한다(10–25). |
| 26–41 | C11 / 수심·하상고 — 입력 수심의 최소값(minimum depth), 수심장 조정·환산, 셀 또는 유동 면(flow face)의 건조 수심, 셀 취수 중단 수심과 하상고(bottom bed elevation) 조정·환산을 설명한다(26–38). `HWET` 설명은 취수 중단 조건으로 옮겼다(34). 매개변수·단위·조건 원문: `\* HMIN: MINIMUM DEPTH OF INPUTS DEPTHS IN METERS` (26); `\* HADJ: ADJUSTMENT TO DEPTH FIELD IN METERS` (28); `\* HCVRT: CONVERTS INPUT DEPTH FIELD TO METERS` (30); `\* HDRY: DEPTH AT WHICH CELL OR FLOW FACE BECOMES DRY` (32); `\* HWET: DEPTH AT WHICH WITHDRAWALS FROM CELL ARE TURNED OFF` (34); `\* BELADJ: ADJUSTMENT TO BOTTOM BED ELEVATION FIELD IN METERS` (36); `\* BELCVRT: CONVERTS INPUT BOTTOM BED ELEVATION FIELD TO METERS` (38). 주석용 `\*` 줄과 빈 줄을 포함한다(39–41). |
| 42–45 | C11 / 입력 예시 표 — 빈 표 첫 행, 구분 행, 헤더 및 입력 예시를 포함한다(42–45). 예시 값은 기본값으로 명시되지 않았다. 입력 표 원문: `\| C11 \| DX \| DY \| DXYCVT \| IMD \| ZBRADJ \| ZBRCVRT \| HMIN \| HADJ \| HCVRT \| HDRY \| HWET \| BELADJ \| BELCVRT \|` (44); `\|  \| 1 \| 1 \| 1 \| 0 \| 0 \| 0.005 \| 0.01 \| 0 \| 1 \| 0.025 \| 0.03 \| 0 \| 1 \|` (45). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 20·44행: 설명의 파일 읽기 매개변수 이름은 `IMDXDY`이다. 입력 표 헤더의 같은 위치에는 `IMD`가 적혀 있다.

