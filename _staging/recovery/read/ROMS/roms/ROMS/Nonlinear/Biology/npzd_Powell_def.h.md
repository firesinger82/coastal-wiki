---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/npzd_Powell_def.h
lines: 148
sha256: 08762dd7fc95ea0927c7cec3ba1bb43832755dc3c657f84bb2af3507dd0ae654
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# npzd_Powell_def.h — 판독 구간 기록

구간은 1행부터 148행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 저작권·MIT/X 사용허가·License_ROMS.md 안내(1–7). Powell 등(2006)의 생태계(ecosystem) 입력 매개변수를 NetCDF에 정의하며 `def_info.F`에 삽입한다는 주석(9–10). C 주석 종료·빈 줄·NPZD 매개변수 정의 설명(13–17). 이 파일에는 루틴 선언과 전처리 분기가 없다. |
| 18–48 | BioIter의 이름·반복 횟수 설명을 Vinfo에 넣고 정수형 `nf90_int`로 정의(18–22). AttSW는 해수 광 감쇠(light attenuation), 단위 `meter-1`(25–30). AttPhy는 식물플랑크톤 광 감쇠, 단위 `meter2 millimole_N-1`(33–38). PhyIS는 광합성–광도(P-I) 곡선 초기 기울기(initial slope), 단위 `meter2 watt-1`(41–46). 실수 매개변수의 형은 `NF_TYPE`이다. `def_var`는 ncid·varid·차원 수 1·차원 벡터 `(/0/)`·Aval·Vinfo·ncname과 `SetParAccess = .FALSE.`를 받는다. 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (23·31·39·47)이다. |
| 49–87 | Vm_NO3는 질산염 흡수율(uptake rate), PhyMRD/PhyMRN는 식물플랑크톤 사망(mortality)의 쇄설물/질소 저장량(pool) 전환율이며 각각 단위 `day-1`(49–70). K_NO3 설명은 역 반포화(inverse half-saturation)이며 단위는 `meter3 millimole-1`(73–78). Ivlev는 동물플랑크톤 섭식(grazing) 상수이며 이 블록에는 Vinfo(3) 대입이 없다(81–85). 각 형은 `NF_TYPE`이다. `def_var`는 ncid·varid·차원 수 1·차원 벡터 `(/0/)`·Aval·Vinfo·ncname과 `SetParAccess = .FALSE.`를 받는다. 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (55·63·71·79·86)이다. |
| 88–109 | ZooGR는 동물플랑크톤 섭식률, 단위 `day-1`(88–93). ZooEED/ZooEEN는 쇄설물/질소 저장량으로의 배설 효율(excretion efficiency)로 설명하며 단위 Vinfo(3) 대입이 없다(96–100·103–107). 각 형은 `NF_TYPE`이다. `def_var`는 ncid·varid·차원 수 1·차원 벡터 `(/0/)`·Aval·Vinfo·ncname과 `SetParAccess = .FALSE.`를 받는다. 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (94·101·108)이다. |
| 110–148 | ZooMRD/ZooMRN는 동물플랑크톤 사망의 쇄설물/질소 전환율, DetRR는 쇄설물 재광물화율(remineralization rate)이며 단위 `day-1`(110–131). wPhy/wDet는 식물플랑크톤/쇄설물 침강률(sinking rate), 단위 `m day-1`(134–147). 각 형은 `NF_TYPE`이다. `def_var`는 ncid·varid·차원 수 1·차원 벡터 `(/0/)`·Aval·Vinfo·ncname과 `SetParAccess = .FALSE.`를 받는다. 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (116·124·132·140·148)이다. 마지막 행은 wDet 오류 검사이다(148). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 75·81–86: K_NO3 정의는 Vinfo(3)에 'meter3 millimole-1'을 대입한다. 이어지는 Ivlev 정의는 Vinfo(1)·Vinfo(2)만 대입하며 그 사이 Vinfo(3)을 비우는 문장은 없다. def_var 내부 처리는 이 파일 판독에 포함하지 않았다.
- 90·96–108: ZooGR 정의는 Vinfo(3)에 'day-1'을 대입한다. 이어지는 ZooEED·ZooEEN 정의는 Vinfo(1)·Vinfo(2)만 대입하며 그 사이 Vinfo(3)을 비우는 문장은 없다.
