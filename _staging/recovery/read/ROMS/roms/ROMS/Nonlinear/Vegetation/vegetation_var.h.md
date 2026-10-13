---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Vegetation/vegetation_var.h
lines: 72
sha256: a5967dd776ba1e6dac22859e9a8be21fbae1f36cff1796d4dc014873da1ee56e
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# vegetation_var.h — 판독 구간 기록

구간은 1행부터 72행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | C 형식 주석의 라이선스·저작자 머리말이다(1–17). 입력·출력 NetCDF 변수의 메타데이터(metadata) 인덱스를 varinfo.dat에서 읽어 지정하고, mod_ncparam.F의 initialize_ncparm에 이 파일을 포함한다는 주석이다(9–14). 수중 식생(submerged aquatic vegetation) 변수 설명 주석과 빈 줄을 포함한다(18–22). |
| 23–38 | VEG_DRAG 또는 VEG_BIOMASS에서 밀도(density)·직경(diameter)·높이(height)·두께(thickness)의 문자열 CASE를 처리한다(23–31). 대응 idvprp 원소에 varid를 복사한다(25·27·29·31). pabbm과 pbgbm의 CASE·대입·VEG_BIOMASS 전처리 예시는 모두 !로 주석 처리되어 있다(32–37). 활성 전처리 조건을 닫는다(38). 조건·전처리 원문: `#if defined VEG_DRAG \|\| defined VEG_BIOMASS` (23). `CASE ('idvprp(isDens)')` (24). `CASE ('idvprp(isDiam)')` (26). `CASE ('idvprp(isHght)')` (28). `CASE ('idvprp(isThck)')` (30). `#endif` (38). |
| 39–44 | VEG_STREAMING에서 idWdvg·idCdvg 문자열 CASE를 처리한다(39–43). 파랑 소산(wave dissipation)과 스펙트럼 항력 계수(spectral drag coefficient)의 식별자에 varid를 복사한다(41·43). cpp 조건을 닫는다(44). 조건·전처리 원문: `#if defined VEG_STREAMING` (39). `CASE ('idWdvg')` (40). `CASE ('idCdvg')` (42). `#endif` (44). |
| 45–59 | MARSH_DYNAMICS에서 염습지(marsh) 마스크(mask)의 idTims에 varid를 복사한다(45–47). MARSH_WAVE_THRUST에서 idTtot, MARSH_RETREAT에서 idTmmr, MARSH_TIDAL_RANGE에서 idTmtr의 CASE를 처리하고 같은 값을 복사한다(48–59). 세 조건은 MARSH_DYNAMICS 안의 독립된 조건이다. 조건·전처리 원문: `#if defined MARSH_DYNAMICS` (45). `CASE ('idTims')` (46). `# if defined MARSH_WAVE_THRUST` (48). `CASE ('idTtot')` (49). `# endif` (51). `# if defined MARSH_RETREAT` (52). `CASE ('idTmmr')` (53). `# endif` (55). `# if defined MARSH_TIDAL_RANGE` (56). `CASE('idTmtr')` (57). `# endif` (59). |
| 60–72 | 시작 시 전처리 `#if defined MARSH_DYNAMICS` (45) 안. MARSH_VERT_GROWTH에서 최고 수위·최저 수위·최대 생물량(biomass)·수직 성장률(vertical growth rate)·누적 퇴적(accretion)에 대응하는 idTmhw·idTmlw·idTmbp·idTmvg·idTmvt 문자열 CASE를 처리한다(60–70). 각 식별자에 varid를 복사한다(62·64·66·68·70). 성장 조건과 바깥 MARSH_DYNAMICS를 닫는다(71–72). 조건·전처리 원문: `# if defined MARSH_VERT_GROWTH` (60). `CASE('idTmhw')` (61). `CASE('idTmlw')` (63). `CASE('idTmbp')` (65). `CASE('idTmvg')` (67). `CASE('idTmvt')` (69). `# endif` (71). `#endif` (72). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32–37: pabbm·pbgbm의 메타데이터 CASE와 대입은 주석이다. VEG_BIOMASS를 정의해도 이 두 CASE는 이 파일의 활성 코드에 포함되지 않는다.
