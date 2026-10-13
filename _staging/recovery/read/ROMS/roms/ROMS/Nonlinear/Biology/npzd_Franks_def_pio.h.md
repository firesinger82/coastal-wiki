---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/npzd_Franks_def_pio.h
lines: 117
sha256: 1ce5cd34762df80fdb0284965e69e8f035f1fddf9d102a7309995b55a125cc52
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# npzd_Franks_def_pio.h — 판독 구간 기록

구간은 1행부터 117행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 저작권·MIT/X 사용허가·License_ROMS.md 안내(1–7). Franks 등(1986)의 생태계(ecosystem) 입력 매개변수를 NetCDF에 정의하며 `def_info.F`에 삽입한다는 주석(9–10). C 주석 종료·빈 줄·NPZD 매개변수 정의 설명(13–17). 이 파일에는 루틴 선언과 전처리 분기가 없다. |
| 18–48 | BioIter의 이름과 반복 횟수 설명을 Vinfo에 넣고 정수형 `PIO_int`로 정의(18–22). K_ext는 광 소산계수(light extinction coefficient), 단위 `meter-1`(25–30). K_NO3는 식물플랑크톤 질산염 흡수의 역 반포화(inverse half-saturation), 단위 `millimole-1 meter3`(33–38). K_Phy는 식물플랑크톤 포화계수(saturation coefficient), 단위 `millimole meter-3`(41–46). 이 실수 매개변수의 형은 `PIO_TYPE`이다. 각 정의는 `def_var`에 pioFile·pioVar·차원 수 1·차원 벡터 `(/0/)`·Aval·Vinfo·ncname과 `SetParAccess = .FALSE.`를 전달한다. 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (23·31·39·47)이다. |
| 49–88 | Vm_NO3는 질산염 흡수율(uptake rate)(49–54), PhyMR는 식물플랑크톤 노화·사망률(senescence/mortality rate)(57–62), ZooGR는 동물플랑크톤 최대 성장률(maximum growth rate)(65–70), ZooMR는 동물플랑크톤 사망률(73–78), ZooMD의 설명 문자열은 `zootoplankton death bits rate`(81–86)이다. 각 단위는 `day-1`이고 형은 `PIO_TYPE`이다. 각 정의는 `def_var`에 pioFile·pioVar·차원 수 1·차원 벡터 `(/0/)`·Aval·Vinfo·ncname과 `SetParAccess = .FALSE.`를 전달한다. 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (55·63·71·79·87)이다. |
| 89–117 | ZooGA는 동물플랑크톤 섭식 비효율(grazing inefficiency)(89–93), ZooEC는 배설 분율(excreted fraction)(96–100)로 정의하며 해당 블록에는 Vinfo(3) 단위 대입이 없다. DetRR는 쇄설물 재광물화율(remineralization rate), 단위 `day-1`(103–108). wDet는 쇄설물 침강률(sinking rate), 단위 `m day-1`(111–116). 네 변수의 형은 `PIO_TYPE`이다. 각 정의는 `def_var`에 pioFile·pioVar·차원 수 1·차원 벡터 `(/0/)`·Aval·Vinfo·ncname과 `SetParAccess = .FALSE.`를 전달한다. 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (94·101·109·117)이다. 마지막 행은 wDet 오류 검사이다(117). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 83·89–101: ZooMD 정의는 Vinfo(3)에 'day-1'을 대입한다. 뒤따르는 ZooGA·ZooEC 정의 블록은 Vinfo(1)·Vinfo(2)만 대입한다. 이 파일에는 그 사이 Vinfo(3)을 비우는 문장이 없다. def_var 내부 처리는 이 파일 판독에 포함하지 않았다.
