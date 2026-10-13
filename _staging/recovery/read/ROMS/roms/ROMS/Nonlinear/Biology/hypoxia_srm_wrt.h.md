---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/hypoxia_srm_wrt.h
lines: 26
sha256: e97658ed1eeff8c4c8ca4db2ac160870718b5042e961c852fd2a4b3000a652b7
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# hypoxia_srm_wrt.h — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 저작권·MIT/X 라이선스·Hypoxia Simple Respiration Model 입력 매개변수를 NetCDF에 쓰는 목적 주석(1–13). wrt_info.F에 포함된다는 주석이며, 이 파일에는 루틴 입구나 열린 전처리 조건이 없다(10). 출력 구분 주석과 빈 줄도 포함한다(14–17). |
| 18–26 | netcdf_put_ivar를 호출해 BioIter(ng)를 BioIter 변수에 쓰고 ncid를 넘긴다(18–20). netcdf_put_fvar로 ResRate(ng)를 ResRate 변수에 쓴다(23–25). 두 호출 모두 시작·개수 인수는 (/0/)이다. 각 호출 직후 FoundError(exit_flag, NoError, __LINE__, MyFile)가 참이면 RETURN한다(21·26). 원문 조건·루프·대입·전처리: `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (21) / `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
