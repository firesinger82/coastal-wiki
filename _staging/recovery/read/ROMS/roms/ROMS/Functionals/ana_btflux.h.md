---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_btflux.h
lines: 115
sha256: 60b622a7f75724392379aa0e8cc7bb826814f19bc2d2b94a729a903e77155431
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_btflux.h — 판독 구간 기록

구간은 1행부터 115행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | ana_btflux 시작(2), 저작권·라이선스(4–9), 해저 추적자 플럭스(bottom tracer flux)를 분석식으로 설정한다는 주석(11–13). 단위는 TracerUnits m/s이다(12). 모듈·인수·MyFile 선언(17–28). `#include "tile.h"` (30)로 tile.h를 끼워 넣는다. ana_btflux_tile에 FORCES(ng)%btflux 전달(32–35). `#ifdef DISTRIBUTE` (39)의 `IF (Lanafile) THEN` (40), `#else` (41)의 `IF (Lanafile.and.(tile.eq.0)) THEN` (42), `#endif` (43) 뒤 ANANAME(3)=MyFile(44). 조건 종료·RETURN·루틴 종료·주석(45–49). |
| 50–77 | ana_btflux_tile 시작(51–54), mod_param·mod_scalars와 인수 선언(57–64). `#ifdef ASSUMED_SHAPE` (66)는 assumed-shape 배열(67), `#else` (68)는 (LBi:UBi,LBj:UBj,NT(ng)) 배열(69), `#endif` (70). i·j 선언(74), `#include "set_bounds.h"` (76)로 set_bounds.h를 끼워 넣는다. 주석·빈 줄 포함. |
| 78–93 | 시작 시 51행 ana_btflux_tile 안. 수평 RHO점(RHO-point)의 해저 열 플럭스(bottom heat flux) 단위는 degC m/s라는 주석(79). `IF (itrc.eq.itemp) THEN` (82)의 j=JstrT..JendT·i=IstrT..IendT 루프(83–84)에서 `btflux(i,j,itrc)=0.0_r8` (85). 루프 종료(86–87). 해저 염분(salinity) 플럭스는 m/s이며 set_vbc에서 해저 염분으로 척도화(scaling)한다는 주석(90–91). |
| 94–105 | 시작 시 51행 ana_btflux_tile·82행 추적자 종류 선택 안. `ELSE IF (itrc.eq.isalt) THEN` (94)의 j·i 루프(95–96)에서 `btflux(i,j,itrc)=0.0_r8` (97). 루프 종료(98–99). 수동 추적자(passive tracer)의 해저 플럭스 단위는 Tunits m/s라는 주석(102–104). |
| 106–115 | 시작 시 51행 ana_btflux_tile·82행 추적자 종류 선택 안. `ELSE` (106)의 j·i 루프(107–108)에서 `btflux(i,j,itrc)=0.0_r8` (109). 루프·조건 종료(110–112), RETURN·루틴 종료(114–115). 세 종류 모두 0 플럭스를 설정한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–13: 첫 설명은 bottom flux를 설정한다고 적는다. 다음 문장은 surface fluxes를 set_vbc에서 btflx에 넣는다고 적는다.
