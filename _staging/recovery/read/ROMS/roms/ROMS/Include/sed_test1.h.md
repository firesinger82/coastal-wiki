---
file: models/ROMS/raw/source_code/roms/ROMS/Include/sed_test1.h
lines: 49
sha256: 1879642435908feb8c0d0bf77742ec61d212c1ffa17989fd6fa69fee241a39bf
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# sed_test1.h — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·수로의 부유 퇴적물(suspended sediment) 시험 주석과 SED_TEST1·ROMS/퇴적물 입력 파일을 포함한다(1–14). 빈 줄을 포함한다(15). |
| 16–29 | 시작 시 열린 전처리 조건 없음. UV_ADV/UV_LOGDRAG/UV_VIS4/MIX_S_UV·수직 스플라인·TS_DIF4/MIX_S_TS·SALINITY·SOLVE3D·SEDIMENT를 정의한다(16–26). SEDIMENT 조건에서 SUSPLOAD를 정의한다(27–29). 원문: `#define UV_ADV` (16); `#define UV_LOGDRAG` (17); `#define UV_VIS4` (18); `#define MIX_S_UV` (19); `#define SPLINES_VDIFF` (20); `#define SPLINES_VVISC` (21); `#define TS_DIF4` (22); `#define MIX_S_TS` (23); `#define SALINITY` (24); `#define SOLVE3D` (25); `#define SEDIMENT` (26); `#ifdef SEDIMENT` (27); `# define SUSPLOAD` (28); `#endif` (29). |
| 30–35 | 시작 시 열린 전처리 조건 없음. MY25_MIXING을 정의하고 해당 조건에서 KANTHA_CLAYSON/N2S2_HORAVG/RI_SPLINES를 정의한다(30–35). 원문: `#define MY25_MIXING` (30); `#ifdef MY25_MIXING` (31); `# define KANTHA_CLAYSON` (32); `# define N2S2_HORAVG` (33); `# define RI_SPLINES` (34); `#endif` (35). |
| 36–49 | 시작 시 열린 전처리 조건 없음. 해석 바닥 수동 추적자/염분/추적자 플럭스·격자·초기장·퇴적물·표면 운동량/수동 추적자/복사/염분/추적자 플럭스·점원·추적자/자유수면 경계 옵션을 정의한다(36–49). 원문: `#define ANA_BPFLUX` (36); `#define ANA_BSFLUX` (37); `#define ANA_BTFLUX` (38); `#define ANA_GRID` (39); `#define ANA_INITIAL` (40); `#define ANA_SEDIMENT` (41); `#define ANA_SMFLUX` (42); `#define ANA_SPFLUX` (43); `#define ANA_SRFLUX` (44); `#define ANA_SSFLUX` (45); `#define ANA_STFLUX` (46); `#define ANA_PSOURCE` (47); `#define ANA_TOBC` (48); `#define ANA_FSOBC` (49). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
