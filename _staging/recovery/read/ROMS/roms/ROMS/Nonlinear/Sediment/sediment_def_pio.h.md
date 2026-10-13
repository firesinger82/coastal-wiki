---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Sediment/sediment_def_pio.h
lines: 110
sha256: f707ae787a62155d4c291eccbe178682ef6c667d09653de5bdc9fbfab6df61f9
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# sediment_def_pio.h — 판독 구간 기록

구간은 1행부터 110행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | C 형식 저작권·MIT/X 라이선스 주석(1–13), 빈 줄·Fortran 주석(14–17). 출력 NetCDF 파일에 퇴적물(sediment) 입력 매개변수를 정의하고 def_info.F에 포함된다는 설명(9–10). 이 파일 자체에는 루틴 선언이 없다. |
| 18–34 | minlayer_thick는 퇴적층 최소 두께, newlayer_thick는 새 층 생성 두께 기준이며 두 단위는 meter(18–20·26–29). 두 def_var는 pioFile/pioVar, PIO_TYPE, 차원 수 1, 목록 (/0/), Aval/Vinfo/ncname, SetParAccess=.FALSE.를 사용한다(21–23·30–32). 오류 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (24·33). 빈 줄 포함. |
| 35–43 | `#ifdef BEDLOAD` (35)·`#endif` (42) 안 bedload_coeff를 소류사(bed load) 수송률 계수로 정의한다(36–37). def_var는 pioFile/pioVar, PIO_TYPE, 1, (/0/), SetParAccess=.FALSE.(38–40). 오류 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (41). 빈 줄(43). |
| 44–62 | `#ifdef ANA_SEDIMENT` (44)에서 Sd50를 균일 초기조건의 중간 입경(median grain diameter), 단위 meter로 정의(45–48), Srho를 입자 밀도, 단위 kilogram meter-3로 정의(54–57). 두 def_var는 pioFile/pioVar, PIO_TYPE, 1, (/seddim/), SetParAccess=.FALSE.(49–51·58–60). 오류 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (52·61). 빈 줄 포함. |
| 63–72 | 시작 시 44행 `#ifdef ANA_SEDIMENT` 안. Csed를 균일 초기조건의 농도(concentration), 단위 kilogram meter-3로 설정한다(63–66). def_var는 pioFile/pioVar, PIO_TYPE, 1, (/seddim/), SetParAccess=.FALSE.(67–69). 오류 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (70). `#endif` (71), 빈 줄(72). |
| 73–88 | Wsed를 침강속도(settling velocity), 단위 meter second-1로 설정(73–75), Erate를 표면층 침식률(erosion rate), 단위 kilogram meter-2 second-1로 설정한다(81–83). def_var는 pioFile/pioVar, PIO_TYPE, 1, (/seddim/), SetParAccess=.FALSE.(76–78·84–86). 오류 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (79·87). 빈 줄 포함. |
| 89–104 | tau_ce/tau_cd는 침식(erosion)/퇴적(deposition) 임계 전단(critical shear)이다(89–90·97–98). 두 단위 문자열 원문 `Vinfo( 3)='meter-2 second-2'` (91·99). def_var는 pioFile/pioVar, PIO_TYPE, 1, (/seddim/), SetParAccess=.FALSE.(92–94·100–102). 오류 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (95·103). 빈 줄 포함. |
| 105–110 | poros를 퇴적물 공극률(porosity)로 정의한다(105–106). def_var는 pioFile/pioVar, PIO_TYPE, 1, (/seddim/), Aval/Vinfo/ncname 및 SetParAccess=.FALSE.(107–109). 오류 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (110). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 91·99: tau_ce와 tau_cd의 단위 문자열은 모두 meter-2 second-2이다.
- 36–41·105–110: bedload_coeff와 poros 정의 블록에는 Vinfo(3) 대입 또는 Vinfo 전체 초기화가 없다. def_var와 포함 루틴 내부의 처리는 이 판독에 포함하지 않았다.
