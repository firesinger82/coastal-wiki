---
file: models/ROMS/raw/source_code/roms/ROMS/Include/estuary_test.h
lines: 47
sha256: c57cab852bee40dfe8abf7c507153e01ccaedaba37e50eec1ca38de66958e0ce
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# estuary_test.h — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·퇴적물 수송 하구(estuary) 시험 주석과 ESTUARY_TEST·roms_estuary_test.in·sediment_estuary_test.in을 포함한다(1–14). 빈 줄을 포함한다(15). |
| 16–34 | 시작 시 열린 전처리 조건 없음. UV_ADV/UV_LOGDRAG·수직 스플라인·SALINITY·SOLVE3D·SEDIMENT를 정의한다(16–22). SEDIMENT이면 SUSPLOAD를 정의한다(23–25). AVERAGES·GLS_MIXING을 정의하고 MY25_MIXING을 해제한다(26–28). GLS 또는 MY25 조건에서 KANTHA_CLAYSON/N2S2_HORAVG/RI_SPLINES를 정의하고 CANUTO_A를 해제한다(29–34). 원문: `#define UV_ADV` (16); `#define UV_LOGDRAG` (17); `#define SPLINES_VDIFF` (18); `#define SPLINES_VVISC` (19); `#define SALINITY` (20); `#define SOLVE3D` (21); `#define SEDIMENT` (22); `#ifdef SEDIMENT` (23); `# define SUSPLOAD` (24); `#endif` (25); `#define AVERAGES` (26); `#define GLS_MIXING` (27); `#undef  MY25_MIXING` (28); `#if defined GLS_MIXING \|\| defined MY25_MIXING` (29); `# define KANTHA_CLAYSON` (30); `# undef  CANUTO_A` (31); `# define N2S2_HORAVG` (32); `# define RI_SPLINES` (33); `#endif` (34). |
| 35–47 | 시작 시 열린 전처리 조건 없음. 해석 격자·초기 조건·퇴적물·표면/바닥 운동량 및 추적자 플럭스·염분/수동 추적자 플럭스·자유수면/2차원 운동량/추적자 경계 옵션을 정의한다(35–47). 원문: `#define ANA_GRID` (35); `#define ANA_INITIAL` (36); `#define ANA_SEDIMENT` (37); `#define ANA_SMFLUX` (38); `#define ANA_STFLUX` (39); `#define ANA_BTFLUX` (40); `#define ANA_SSFLUX` (41); `#define ANA_BSFLUX` (42); `#define ANA_SPFLUX` (43); `#define ANA_BPFLUX` (44); `#define ANA_FSOBC` (45); `#define ANA_M2OBC` (46); `#define ANA_TOBC` (47). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
