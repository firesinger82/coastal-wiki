---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Sediment/sediment_def.h
lines: 161
sha256: ddb1fd5ca79cba111397d1f49fc000007592b1690c78ef761da5ffa13d0dbcbe
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# sediment_def.h — 판독 구간 기록

구간은 1행부터 161행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | C 형식 저작권·MIT/X 라이선스 주석(1–13), 빈 줄·Fortran 주석(14–17). 출력 NetCDF 파일에 퇴적물(sediment) 입력 매개변수를 정의하고 def_info.F에 포함된다는 설명(9–10). 이 파일 자체에는 루틴 선언이 없다. |
| 18–41 | minlayer_thick는 퇴적층 최소 두께(meter), newlayer_thick는 새 층 생성 두께 기준(meter), sg_zwbl는 바닥 부근 유속을 구할 입력 고도로 Vinfo에 설정한다(18–20·26–29·35–36). 각 def_var 호출은 NF_TYPE, 차원 수 1, 차원 목록 (/0/), Aval/Vinfo/ncname, `SetParAccess = .FALSE.`를 사용한다(21–23·30–32·37–39). 각 호출 뒤 오류 조건 원문은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (24·33·40). 주석·빈 줄 포함. |
| 42–64 | `#ifdef BEDLOAD` (42)에서 소류사(bed load) 수송 계수 bedload_coeff, 습윤(wet)/건조(dry) 바닥 붕괴(slumping) 임계 경사 sedslope_crit_wet/sedslope_crit_dry를 정의한다(43–63). 각 def_var는 NF_TYPE, 1, (/0/), SetParAccess=.FALSE.(45–47·53–55·60–62). 첫 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__,                      &` (48), `&               __FILE__)) RETURN` (49). 나머지는 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (56·63). 주석(50·57·64) 포함. |
| 65–94 | 시작 시 42행 `#ifdef BEDLOAD` 안. slopefac_wet/slopefac_dry는 습윤/건조 바닥 붕괴 계수, bedload_vandera_alphac/bedload_vandera_alphaw는 흐름/파랑 기여 배율로 정의한다(65–91). 각 def_var의 형식은 NF_TYPE, 1, (/0/), SetParAccess=.FALSE.(67–69·74–76·81–83·88–90). 오류 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (70·77·84·91). `#endif` (93), 주석(92·94). |
| 95–123 | `!#ifdef ANA_SEDIMENT` (95)와 `!#endif` (122)는 Fortran 주석이며 열린 전처리 조건이 아니다. Sd50는 균일 초기조건의 중간 입경(median grain diameter), 단위 meter(96–99). Srho는 입자 밀도, Csed는 농도(concentration), 단위 kilogram meter-3(105–108·114–117). 세 def_var 호출의 차원 목록은 (/seddim/), 형식 NF_TYPE, 차원 수 1, SetParAccess=.FALSE.(100–102·109–111·118–120). 오류 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (103·112·121). 빈 줄 포함. |
| 124–139 | Wsed를 입자 침강속도(settling velocity), 단위 meter second-1로 설정한다(124–126). Erate는 표면층 침식률(erosion rate), 단위 kilogram meter-2 second-1(132–134). def_var는 NF_TYPE, 1, (/seddim/), SetParAccess=.FALSE.(127–129·135–137). 오류 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (130·138). 빈 줄 포함. |
| 140–155 | tau_ce는 침식 임계 전단(critical shear), tau_cd는 퇴적 임계 전단이다(140–141·148–149). 두 단위 문자열 원문 `Vinfo( 3)='meter-2 second-2'` (142·150). def_var는 NF_TYPE, 1, (/seddim/), SetParAccess=.FALSE.(143–145·151–153). 오류 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (146·154). 빈 줄 포함. |
| 156–161 | poros를 퇴적물 공극률(porosity)로 설정한다(156–157). def_var는 NF_TYPE, 1, (/seddim/), Aval/Vinfo/ncname 및 SetParAccess=.FALSE.를 사용한다(158–160). 오류 조건 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (161). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 95·122: ANA_SEDIMENT의 조건 시작·끝처럼 보이는 두 행은 앞에 !가 붙은 주석이다. Sd50/Srho/Csed 정의를 감싸는 활성 전처리 조건은 이 파일에 없다.
- 142·150: tau_ce와 tau_cd의 NetCDF 단위 문자열은 모두 meter-2 second-2이다. 이 기록은 원문 문자열만 확인했다.
- 35–40·43–91·156–161: sg_zwbl, BEDLOAD 매개변수, poros 정의 블록에는 Vinfo(3)에 값을 대입하거나 Vinfo를 비우는 문장이 없다. def_var와 포함 루틴 내부의 Vinfo 처리는 이 판독에 포함하지 않았다.
