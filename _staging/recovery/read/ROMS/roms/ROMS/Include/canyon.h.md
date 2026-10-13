---
file: models/ROMS/raw/source_code/roms/ROMS/Include/canyon.h
lines: 42
sha256: ba6c1633698fa0d1d9ba1d5463be986fa8edb1bfe126701446a9fbe3cdedba21
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# canyon.h — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스·이상화 협곡(idealized canyon) 설정 주석을 포함한다(1–10). CANYON과 2차원·3차원 입력 roms_canyon2d.in/roms_canyon3d.in을 적는다(11–12). 주석 종료·빈 줄을 포함한다(13–14). |
| 15–24 | 시작 시 열린 전처리 조건 없음. SOLVE3D가 없을 때 2차원 설정을 선택한다(15). 운동량 이류·이차 항력·2차 점성·코리올리·BODYFORCE·해석 진단/격자/초기 조건/표면 운동량 플럭스를 정의한다(16–24). 원문: `#ifndef SOLVE3D                   /* 2D set-up */` (15); `# define UV_ADV` (16); `# define UV_QDRAG` (17); `# define UV_VIS2` (18); `# define UV_COR` (19); `# define BODYFORCE` (20); `# define ANA_DIAG` (21); `# define ANA_GRID` (22); `# define ANA_INITIAL` (23); `# define ANA_SMFLUX` (24). |
| 25–42 | 시작 시 `#ifndef SOLVE3D                   /* 2D set-up */` (15) 안. SOLVE3D가 있는 ELSE의 3차원 설정으로 전환한다(25). 운동량·MIX_S_UV·DJ_GRADPS·SPLINES_VVISC·TS_DIF2·MIX_GEO_TS와 해석 진단/격자/초기 조건/표면 운동량 및 추적자 플럭스/바닥 추적자 플럭스/수직 혼합을 정의한다(26–41). 조건을 닫는다(42). 원문: `#else                             /* 3D set-up */` (25); `# define UV_ADV` (26); `# define UV_COR` (27); `# define UV_QDRAG` (28); `# define UV_VIS2` (29); `# define MIX_S_UV` (30); `# define DJ_GRADPS` (31); `# define SPLINES_VVISC` (32); `# define TS_DIF2` (33); `# define MIX_GEO_TS` (34); `# define ANA_DIAG` (35); `# define ANA_GRID` (36); `# define ANA_INITIAL` (37); `# define ANA_SMFLUX` (38); `# define ANA_STFLUX` (39); `# define ANA_BTFLUX` (40); `# define ANA_VMIX` (41); `#endif` (42). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–42: SOLVE3D 여부로 2차원·3차원 설정을 나눈다. 이 파일 자체에는 SOLVE3D를 정의하거나 해제하는 지시문이 없다.
