---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_9.md
lines: 65
sha256: 6840746d0361c29f14da87c53ed6ec908cac39eb58270c8eda672a0b208d4c8e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_9.md — 판독 구간 기록

구간은 1행부터 65행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 머리말 — 페이지 제목은 Card Image 9이다(3). 페이지 ID, space, URL, 버전, 갱신 시각과 문서 경로를 기록한다(2–8). |
| 10–36 | C9 SPACE-RELATED AND SMOOTHING PARAMETERS / 격자·영역 분할 — I·J 방향 셀 수, 수평 활성 셀 수에 2를 더한 값, 가변 크기 수평 셀 수와 곡선 직교 격자(curvilinear-orthogonal grid) 옵션을 정의한다(14–22). 수평 영역 분할(horizontal domain decomposition)의 영역 수와 영역당 물 셀 수를 설명한다(24–36). 단일 프로세서 조건, 병렬 프로세서 조건, 벡터 길이 또는 stride의 정수배 제약을 원문 그대로 옮긴다. 원문: `\* IC: NUMBER OF CELLS IN I DIRECTION` (14); `\* JC: NUMBER OF CELLS IN J DIRECTION` (16); `\* LC: NUMBER OF ACTIVE CELLS IN HORIZONTAL + 2` (18); `\* LVC: NUMBER OF VARIABLE SIZE HORIZONTAL CELLS` (20); `\* ISCO: 1 FOR CURVILINEAR-ORTHOGONAL GRID (LVC=LC-2)` (22); `\* NDM: NUMBER OF DOMAINS FOR HORIZONTAL DOMAIN DECOMPOSITION` (24); `\*           ( NDM=1, FOR MODEL EXECUTION ON A SINGLE PROCESSOR SYSTEM OR` (26); `\*           NDM=MM\*NCPUS, WHERE MM IS AN INTEGER AND NCPUS IS THE NUMBER` (28); `\*           OF AVAILABLE CPU'S FOR MODEL EXECUTION ON A PARALLEL MULTIPLE PROCESSOR SYSTEM )` (30); `\* LDM: NUMBER OF WATER CELLS PER DOMAIN (LDM=(LC-2)/NDM, FOR MULTIPE VECTOR PROCESSORS,` (32); `\*           LDM MUST BE AN INTEGER MULTIPLE OF THE VECTOR LENGTH OR` (34); `\*           STRIDE NVEC THUS CONSTRAINING LC-2 TO BE AN INTEGER MULTIPLE OF NVEC )` (36). |
| 37–61 | C9 / 셀 마스킹·연결·평활화 — 물 셀의 육지 마스킹(masking) 또는 얇은 장벽 추가, 사용자 지정 남북·동서 연결, 수심·초기 염분장 평활화(smoothing) 횟수와 가중치를 설명한다(38–54). 옵션별 입력 파일 이름과 값을 보존한다. 빈 줄과 별표 마크업을 포함한다(37·39–61). 원문: `\* ISMASK: 1 FOR MASKING WATER CELL TO LAND OR ADDING THIN BARRIERS` (38); `\* USING INFORMATION IN FILE MASK.INP` (40); `\* ISCONNECT: 1 FOR USER DEFINED N-S CONNECTION OF CELLS USING INFO IN FILE MAPPGNS.INP` (42); `\*                      2 FOR USER DEFINED E-W CONNECTION OF CELLS USING INFO IN FILE MAPPGEW.INP` (44); `\*                      3 FOR BOTH E-W AND N-S CONNECTIONS` (46); `\* NSHMAX: NUMBER OF DEPTH SMOOTHING PASSES` (48); `\* NSBMAX: NUMBER OF INITIAL SALINITY FIELD SMOOTHING PASSES` (50); `\* WSMH: DEPTH SMOOTHING WEIGHT` (52); `\* WSMB: SALINITY SMOOTHING WEIGHT` (54). |
| 62–65 | C9 / 입력 예시 표 — 표 머리말과 데이터 행의 열 순서를 그대로 옮긴다(62–65). IC부터 WSMB까지의 수치는 입력 예시이며 이 파일은 이를 기본값으로 정의하지 않는다. 원문: `\| C9 \| IC \| JC \| LC \| LVC \| ISCO \| NDM \| LDM \| ISMASK \| CONNECT \| NSHMAX \| NSBMAX \| WSMH \| WSMB \|` (64); `\|  \| 58 \| 66 \| 2123 \| 2121 \| 1 \| 1 \| 2121 \| 1 \| 0 \| 0 \| 0 \| 0.125 \| 0 \|` (65). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 42·64행: 설명은 연결 옵션 이름을 `ISCONNECT`로 적고 입력 예시 표는 `CONNECT`로 적는다.

