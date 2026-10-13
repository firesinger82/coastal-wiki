---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_stflux.h
lines: 153
sha256: 7a5bb26e9d18f4b0dd9a03cdc16b43c76fc76eb31ab49b2c0ab8831d44cc1ee6
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_stflux.h — 판독 구간 기록

구간은 1행부터 153행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–52 | ana_stflux의 머리말은 추적자 표면 플럭스(tracer surface flux) stflux(:,:,itrc)의 단위를 TracerUnits m/s로 적고 set_vbc에서 stflx 상태로 처리한다고 설명한다(2–15). param·forces·ncparam, 입력 ng·tile·model·itrc, MyFile을 선언한다(17–28). 30행은 tile.h를 끼워 넣는다. ana_stflux_tile에 stflux를 넘기고 SHORTWAVE에서 srflx도 넘긴다(32–38). DISTRIBUTE 조건에 따라 ANANAME(31)에 MyFile을 저장하고 끝낸다(42–52). 원문 조건·대입·전처리 행: `character (len=*), parameter :: MyFile =                          &` (27), `&  __FILE__` (28), `#include "tile.h"` (30), `#ifdef SHORTWAVE` (35), `#endif` (37), `#ifdef DISTRIBUTE` (42), `IF (Lanafile) THEN` (43), `#else` (44), `IF (Lanafile.and.(tile.eq.0)) THEN` (45), `#endif` (46), `ANANAME(31)=MyFile` (47), `END IF` (48). |
| 53–94 | ana_stflux_tile의 인수 목록은 SHORTWAVE에서 srflx를 추가한다(54–60). param·scalars·exchange_r2d_tile을 사용하고 DISTRIBUTE에서 mp_exchange2d를 가져온다(63–69). ASSUMED_SHAPE·SHORTWAVE에 따라 입력 srflx와 intent(inout) stflux의 경계를 선언하고 기본 stflux의 추적자 차원은 NT(ng)이다(77–87). 지역 i·j를 선언하고 93행에서 set_bounds.h를 끼워 넣는다. 원문 조건·대입·전처리 행: `#ifdef SHORTWAVE` (57), `#endif` (59), `#ifdef DISTRIBUTE` (67), `#endif` (69), `#ifdef ASSUMED_SHAPE` (77), `# ifdef SHORTWAVE` (78), `# endif` (80), `#else` (82), `# ifdef SHORTWAVE` (83), `# endif` (85), `#endif` (87), `#include "set_bounds.h"` (93). |
| 95–109 | 시작 시 54행 ana_stflux_tile 안. RHO 지점 순 열 플럭스(net heat flux)의 주석 단위는 degC m/s이다(96). itrc=itemp일 때 타일 j·i 루프를 순회한다(99–101). BL_TEST는 stflux=srflx이고 다른 응용은 stflux=0이다(102–106). 두 루프를 닫고 주석 줄을 포함한다(107–109). 99행 추적자 조건은 다음 구간까지 열린다. 원문 조건·대입·전처리 행: `IF (itrc.eq.itemp) THEN` (99), `DO j=JstrT,JendT` (100), `DO i=IstrT,IendT` (101), `#ifdef BL_TEST` (102), `stflux(i,j,itrc)=srflx(i,j)` (103), `#else` (104), `stflux(i,j,itrc)=0.0_r8` (105), `#endif` (106), `END DO` (107), `END DO` (108). |
| 110–121 | 시작 시 54행 ana_stflux_tile·99행 추적자 조건 안. 주석은 담수 플럭스(freshwater flux)의 단위를 m/s로 적고 표면 염분에 의한 척도 조정은 set_vbc에서 수행한다고 설명한다(111–112). 115행 ELSE IF는 itrc=isalt 분기이다. 모든 타일 지점의 stflux를 0으로 설정한다(116–120). 주석 줄을 포함한다(121). 원문 조건·대입·전처리 행: `ELSE IF (itrc.eq.isalt) THEN` (115), `DO j=JstrT,JendT` (116), `DO i=IstrT,IendT` (117), `stflux(i,j,itrc)=0.0_r8` (118), `END DO` (119), `END DO` (120). |
| 122–134 | 시작 시 54행 ana_stflux_tile·99행 추적자 조건 안. 수동 추적자(passive tracer) 표면 플럭스의 주석 단위는 Tunits m/s이다(123–124). 127행 ELSE는 앞 온도·염분 조건 이외의 분기이다. 타일 지점의 stflux를 0으로 설정하고 추적자 조건을 닫는다(128–133). 주석 줄을 포함한다(134). 원문 조건·대입·전처리 행: `ELSE` (127), `DO j=JstrT,JendT` (128), `DO i=IstrT,IendT` (129), `stflux(i,j,itrc)=0.0_r8` (130), `END DO` (131), `END DO` (132), `END IF` (133). |
| 135–153 | 시작 시 54행 ana_stflux_tile 안. 동서 또는 남북 주기경계(periodic boundary)가 있으면 exchange_r2d_tile을 현재 itrc의 stflux 슬라이스에 호출한다(137–141). DISTRIBUTE는 mp_exchange2d에 같은 슬라이스·NghostPoints·주기 플래그를 넘긴다(143–150). RETURN과 루틴 종료를 포함한다(152–153). 원문 조건·대입·전처리 행: `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (137), `END IF` (141), `#ifdef DISTRIBUTE` (143), `#endif` (150). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 35–37·57–59·78–85·102–106: srflx 인수 전달과 선언은 SHORTWAVE 조건 안에 있다. srflx를 참조하는 온도 대입은 BL_TEST 조건 안에 있으며 그 대입의 전처리 조건에는 SHORTWAVE가 없다.
- 105·118·130: BL_TEST 온도 분기 이외의 온도·염분·수동 추적자 표면 플럭스는 0.0_r8로 설정된다.
