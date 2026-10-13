---
file: models/ROMS/raw/source_code/roms/ROMS/Include/test_chan.h
lines: 43
sha256: dd6dcce5fd695c81462c97dcfb79b516a3a6d4c5f1118575be4e11a8df88c0cc
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# test_chan.h — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·퇴적물 수로 시험 주석과 TEST_CHAN·ROMS/퇴적물 입력 파일을 포함한다(1–14). 빈 줄을 포함한다(15). |
| 16–33 | 시작 시 열린 전처리 조건 없음. WRITE_GRID/OUT_DOUBLE·ANA_GRID·UV_ADV·SOLVE3D·수직 스플라인·해석 초기 조건·표면/바닥 추적자·염분·수동 추적자 및 표면 운동량 플럭스·자유수면/2차원 운동량 경계를 정의한다(16–33). SALINITY를 해제한다(20). 원문: `#define WRITE_GRID` (16); `#define OUT_DOUBLE` (17); `#define ANA_GRID` (18); `#define UV_ADV` (19); `#undef  SALINITY` (20); `#define SOLVE3D` (21); `#define SPLINES_VDIFF` (22); `#define SPLINES_VVISC` (23); `#define ANA_INITIAL` (24); `#define ANA_SMFLUX` (25); `#define ANA_STFLUX` (26); `#define ANA_BTFLUX` (27); `#define ANA_SSFLUX` (28); `#define ANA_BSFLUX` (29); `#define ANA_SPFLUX` (30); `#define ANA_BPFLUX` (31); `#define ANA_FSOBC` (32); `#define ANA_M2OBC` (33). |
| 34–43 | 시작 시 열린 전처리 조건 없음. SEDIMENT·ANA_SEDIMENT·SUSPLOAD를 정의한다(34–36). ANA_VMIX를 해제하고 GLS_MIXING·KANTHA_CLAYSON·N2S2_HORAVG·RI_SPLINES·UV_LOGDRAG를 정의한다(37–42). PERFECT_RESTART를 해제하며 끝난다(43). 원문: `#define SEDIMENT` (34); `#define ANA_SEDIMENT` (35); `#define SUSPLOAD` (36); `#undef  ANA_VMIX` (37); `#define GLS_MIXING` (38); `#define KANTHA_CLAYSON` (39); `#define N2S2_HORAVG` (40); `#define RI_SPLINES` (41); `#define UV_LOGDRAG` (42); `#undef  PERFECT_RESTART` (43). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
