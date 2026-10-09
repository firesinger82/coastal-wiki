---
file: models/ADCIRC/raw/source_code/adcirc/src/driver.F
lines: 63
sha256: 3a2b23fb5fee08d5e157fd071cb70b13653271182f98d47c98b304a580762b93
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# driver.F — 판독 구간 기록

구간은 1행부터 63행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | ADCIRC 저작권(1994–2025)·LGPL v3 이상·무보증 고지(1–19). Non-ESMF ADCIRC DRIVER라는 구분 주석(20–24). |
| 25–37 | `PROGRAM ADCIRC` 시작(25). ADCIRC_Mod의 ADCIRC_Init·ADCIRC_Run·ADCIRC_Final과 성공 종료용 terminate·ADCIRC_EXIT_SUCCESS를 가져옴(27–28). `#ifdef CSWAN` (30)에서 비정형 격자(unstructured mesh) SWAN 결합(coupling)용 Couple2swan의 PADCSWAN_INIT·PADCSWAN_FINAL과 SIZES의 MNPROC·MYPROC를 가져옴(31–34). implicit none·빈 줄(35–37). |
| 38–49 | 시작 시 25행 ADCIRC 프로그램 안. `ADCIRC_Init()` (38) 호출. `#ifdef CSWAN` (40)에서 시간 단계(time step) 루프 전 SWAN 초기화 설명 주석(41–44). `IF(MYPROC.LT.MNPROC)THEN` (45)이면 `PADCSWAN_INIT()` (46) 호출. 조건·전처리 분기 종료·빈 줄(47–49). |
| 50–59 | 시작 시 25행 ADCIRC 프로그램 안. `ADCIRC_Run()` (50) 호출. `#ifdef CSWAN` (52)에서 SWAN 정리 주석(53–54). `IF(MYPROC.LT.MNPROC)THEN` (55)이면 `PADCSWAN_FINAL()` (56) 호출. 조건·전처리 분기 종료·빈 줄(57–59). |
| 60–63 | 시작 시 25행 ADCIRC 프로그램 안. `ADCIRC_Final()` (60) 호출. 빈 줄(61), `terminate(exit_code=ADCIRC_EXIT_SUCCESS)` (62) 호출. ADCIRC 프로그램 종료(63). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

