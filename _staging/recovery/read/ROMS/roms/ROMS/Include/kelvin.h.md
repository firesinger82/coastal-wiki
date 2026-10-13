---
file: models/ROMS/raw/source_code/roms/ROMS/Include/kelvin.h
lines: 32
sha256: c0fe9887b06030dc2ce79faad11468498df8e9e6b6f1e2dc36a47ecb6b12ab68
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# kelvin.h — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·Kelvin 파(Kelvin wave) 시험 주석과 KELVIN·roms_kelvin.in을 포함한다(1–13). 빈 줄을 포함한다(14). |
| 15–24 | 시작 시 열린 전처리 조건 없음. 운동량 이류·코리올리·이차 항력·2차 점성·S면 혼합·DJ_GRADPS·추적자 2차 확산/S면 혼합·SOLVE3D·RADIATION_2D를 정의한다(15–24). 원문: `#define UV_ADV` (15); `#define UV_COR` (16); `#define UV_QDRAG` (17); `#define UV_VIS2` (18); `#define MIX_S_UV` (19); `#define DJ_GRADPS` (20); `#define TS_DIF2` (21); `#define MIX_S_TS` (22); `#define SOLVE3D` (23); `#define RADIATION_2D` (24). |
| 25–32 | 시작 시 열린 전처리 조건 없음. 해석 격자·초기 조건·자유수면/2차원 운동량 경계·표면 운동량/추적자/복사·바닥 추적자 플럭스 옵션을 정의한다(25–32). 원문: `#define ANA_GRID` (25); `#define ANA_INITIAL` (26); `#define ANA_FSOBC` (27); `#define ANA_M2OBC` (28); `#define ANA_SMFLUX` (29); `#define ANA_STFLUX` (30); `#define ANA_SRFLUX` (31); `#define ANA_BTFLUX` (32). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
