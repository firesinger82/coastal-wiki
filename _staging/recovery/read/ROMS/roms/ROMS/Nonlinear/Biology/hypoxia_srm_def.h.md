---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/hypoxia_srm_def.h
lines: 31
sha256: 06829b4ac3815d764536d35732807cb91c6d89d28c3bab99be77e442408bbd04
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# hypoxia_srm_def.h — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 저작권·MIT/X 라이선스 머리말(1–13). 단순 저산소 호흡 모형(Hypoxia Simple Respiration Model)의 입력 매개변수를 출력 NetCDF에 정의한다는 주석(9–10). 포함 위치는 def_info.F라고 적음(10). 빈 줄·Fortran 도입 주석(14–17). 이 파일에는 루틴·루프·전처리 조건의 시작이 없다. |
| 18–24 | BioIter 이름·반복 수 설명을 Vinfo(1:2)에 설정(18–19). 정수 스칼라 정의 호출은 `status=def_var(ng, model, ncid, varid, nf90_int,                  &` (20); `&               1, (/0/), Aval, Vinfo, ncname,                     &` (21); `&               SetParAccess = .FALSE.)` (22). 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (23). 빈 줄(24). 반복 수의 수치 기본값·범위 대입은 없다. |
| 25–31 | ResRate 이름·total biological respiration rate 설명과 단위 day-1을 Vinfo(1:3)에 설정(25–27). 실수 정의 호출은 `status=def_var(ng, model, ncid, varid, NF_TYPE,                   &` (28); `&               1, (/0/), Aval, Vinfo, ncname,                     &` (29); `&               SetParAccess = .FALSE.)` (30). 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (31). 기본값·범위·호흡률(respiration rate) 계산식은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 25–31 및 대상 hypoxia_srm.h:329–336: 이 파일은 ResRate를 스칼라 NetCDF 변수로 정의하며 단위 문자열은 day-1이다. 대상 hypoxia_srm.h는 3차원 respiration 입력장을 사용하며 해당 주석의 단위는 millimole/m3/day이다. 두 이름과 단위 표기의 관계는 이 두 파일 안에서 설명하지 않는다.
