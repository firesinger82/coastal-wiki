---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/fennel_def.h
lines: 316
sha256: 589e56ac1049b40ab3ad8b61a00f6fcf6606404127c8f4d14b0654cdddd166cc
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# fennel_def.h — 판독 구간 기록

구간은 1행부터 316행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 저작권·MIT/X 라이선스와 Fennel 생태계(ecosystem) 입력 매개변수를 출력 NetCDF에 정의한다는 주석(1–13). 주석은 def_info.F에서 이 파일을 포함한다고 적음(9–10). 빈 줄·Fortran 도입 주석(14–17). 이 파일 안에는 루틴·루프·전처리 조건의 시작이 없다. 수치 기본값을 설정하지 않고 Vinfo 메타데이터(metadata)와 변수 정의 호출을 구성함. |
| 18–78 | BioIter 반복 수(18–19)는 `status=def_var(ng, model, ncid, varid, nf90_int,                  &` (20); `&               1, (/0/), Aval, Vinfo, ncname,                     &` (21); `&               SetParAccess = .FALSE.)` (22)로 정의함. 실수 변수는 NF_TYPE으로 같은 def_var를 호출함(28–30·36–38·43–45·50–52·58–60·66–68·74–76). AttSW 해수 광 감쇠(light attenuation)는 meter-1(25–27), AttChl 엽록소(chlorophyll) 감쇠는 meter-2 milligram_Chl-1(33–35). PARfrac 광합성 유효 복사(Photosynthetically Available Radiation) 비율(41–42), Vp0 Eppley 온도 제한 성장 매개변수(48–49). I_thNH4 질산화(nitrification) 복사 임계값과 D_p5NH4 반포화(half-saturation) 복사는 watt meter-2(55–57·63–65), NitriR은 day-1(71–73). 각 호출 뒤 조건 원문은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (23·31·39·46·53·61·69·77). 빈 줄도 포함함(24·32·40·47·54·62·70·78). |
| 79–141 | K_NO3/K_NH4 흡수 반포화의 역수는 meter3 millimole_N-1(79–81·87–89). K_PO4는 meter3 millimole_P-1(95–97). K_Phy의 설명은 동물플랑크톤 섭취 반포화 상수이며 단위 문자열은 day-1(103–105). Chl2C_m 최대 엽록소/탄소 비는 milligram_chl milligram_carbon-1(111–113), ChlMin은 milligram_chl meter-3(119–121). PhyCN 탄소/질소 비는 mole_C mole_N-1(127–129), R_P2N 인산염/질소 비는 mole_P mole_N-1(135–137). 각 변수는 NF_TYPE·스칼라 차원 인수 1, (/0/)·SetParAccess=.FALSE.로 def_var를 호출함(82–84·90–92·98–100·106–108·114–116·122–124·130–132·138–140). 오류 조건 원문은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (85·93·101·109·117·125·133·141). |
| 142–196 | PhyIP NH4 억제(inhibition)는 millimole_N-1(143–145), PhyIS 광-광합성(P-I) 곡선 초기 기울기는 milligram_C milligram_Chl-1 watt-1 meter2 day-1(151–153). PhyMin은 millimole_N meter-3(159–161), PhyMR 사망률(mortality rate)은 day-1(167–169). ZooAE_N은 동물플랑크톤 질소 동화 효율(assimilation efficiency) 설명이며 원문 철자는 mitrogen(175–176). ZooBM 기초 대사(basal metabolism)는 day-1(182–184), ZooCN은 mole_C mole_N-1(190–192). def_var는 모두 NF_TYPE·1, (/0/)·SetParAccess=.FALSE.를 사용함(146–148·154–156·162–164·170–172·177–179·185–187·193–195). 오류 조건 원문은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (149·157·165·173·180·188·196). 빈 줄을 포함함. |
| 197–252 | ZooER 배설(excretion), ZooGR 최대 성장, ZooMR 사망률은 day-1(198–200·206–208·222–224). ZooMin 최소 농도는 millimole_N meter-3(214–216). LDeRRN/LDeRRC 큰 쇄설물(detritus)의 질소/탄소 재광물화(remineralization)는 day-1(230–232·238–240). CoagR 응집(coagulation)도 day-1(246–248). 각 def_var 호출은 NF_TYPE·1, (/0/)·SetParAccess=.FALSE.(201–203·209–211·217–219·225–227·233–235·241–243·249–251). 오류 조건 원문은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (204·212·220·228·236·244·252). 빈 줄을 포함함. |
| 253–316 | SDeRRN/SDeRRC 작은 쇄설물 질소/탄소 재광물화는 day-1(254–256·262–264). RDeRRN/RDeRRC 하천 쇄설물 질소/탄소 재광물화도 day-1(270–272·278–280). wPhy/wLDet/wSDet의 수직 침강 속도(vertical sinking velocity)는 meter day-1(286–288·294–296·302–304). pCO2air 대기 CO2 분압(partial pressure)의 단위 문자열은 parts per million by volume(310–312). def_var는 NF_TYPE·1, (/0/)·SetParAccess=.FALSE.(257–259·265–267·273–275·281–283·289–291·297–299·305–307·313–315). 오류 조건 원문은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (260·268·276·284·292·300·308·316). 마지막 문장은 이 오류 검사이며 빈 줄을 포함함. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 103–105: K_Phy 설명은 섭취 반포화 상수이고 Vinfo(3)의 단위 문자열은 day-1이다.
- 175–176: ZooAE_N 설명 문자열은 nitrogen 대신 mitrogen을 사용한다.
- 18–22·41–45·48–52·175–179: BioIter/PARfrac/Vp0/ZooAE_N 블록은 Vinfo(3)을 대입하지 않는다. def_var 내부의 메타데이터 초기화는 이 파일에 없다.
- 95–101·135–141·238–244·262–284·310–316: 인산염·탄소·하천 재광물화·대기 CO2 매개변수 정의를 감싸는 전처리 조건은 이 파일에 없다.
