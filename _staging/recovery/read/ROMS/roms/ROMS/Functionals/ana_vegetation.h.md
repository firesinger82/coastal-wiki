---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_vegetation.h
lines: 135
sha256: 579a2af28e481194664f3eae844622a1f51570c0d7cc505df84fc570bcb6f889
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_vegetation.h — 판독 구간 기록

구간은 1행부터 135행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–60 | 시작 시 열린 전처리 조건 없음. `ana_vegetation` 진입부·저작권·식생 초기 조건 설명을 포함한다(1–13). 주석은 NVEG·NVEGP와 밀도(density), 평균 지름(diameter), 평균 높이(height), 평균 두께(thickness), marsh_mask의 0/1 의미를 정의한다(14–28). 모듈·인수 선언 뒤 `tile.h`를 포함한다(30–39). `ana_vegetation_tile`에 plant를 전달하며 MARSH_WAVE_THRUST일 때 marsh_mask 인수를 추가한다(41–47). DISTRIBUTE별 Lanafile 조건으로 ANANAME(48)에 __FILE__을 저장한다(51–57). 반환·종료를 포함한다(59–60). 원문: `#include "tile.h"` (39); `CALL ana_vegetation_tile (ng, tile, model,                        &` (41); `&                          LBi, UBi, LBj, UBj,                     &` (42); `&                          IminS, ImaxS, JminS, JmaxS,             &` (43); `#ifdef MARSH_WAVE_THRUST` (44); `&                          VEG(ng) % marsh_mask,                   &` (45); `#endif` (46); `&                          VEG(ng) % plant)` (47); `#ifdef DISTRIBUTE` (51); `IF (Lanafile) THEN` (52); `#else` (53); `IF (Lanafile.and.(tile.eq.0)) THEN` (54); `#endif` (55); `ANANAME(48)=__FILE__` (56). |
| 61–107 | 시작 시 열린 전처리 조건 없음. `ana_vegetation_tile` 선언의 선택 인수 marsh_mask는 WAVE_THRUST_MARSH 조건으로 추가한다(63–69). 모듈·인수 선언 뒤 ASSUMED_SHAPE별 plant 배열을 선언한다(72–93). 두 배열 형상 모두 marsh_mask 선언은 WAVE_THRUST_MARSH로 감싼다(85–87·90–92). i/j/k/iveg 및 DISTRIBUTE의 Tstr/Tend를 선언하고 `set_bounds.h`를 포함한다(97–102). 빈 줄·식생 속성 초기화 주석을 포함한다(103–107). 원문: `#ifdef WAVE_THRUST_MARSH` (66); `#endif` (68); `#ifdef ASSUMED_SHAPE` (83); `# ifdef WAVE_THRUST_MARSH` (85); `# endif` (87); `#else` (88); `# ifdef WAVE_THRUST_MARSH` (90); `# endif` (92); `#endif` (93); `#ifdef DISTRIBUTE` (98); `#endif` (100); `#include "set_bounds.h"` (102). |
| 108–120 | 시작 시 열린 전처리 조건 없음. 시작 시 63행 `ana_vegetation_tile` 안. VEG_DRAG일 때 iveg=1..NVEG 및 JstrT..JendT, IstrT..IendT 루프에서 밀도 800 individuals/m², 지름 0.01 m, 높이 2 m, 두께 0.0005 m를 모든 종류에 대입한다(108–119). 빈 줄을 포함한다(120). 원문: `#ifdef VEG_DRAG` (108); `DO iveg=1,NVEG` (109); `DO j=JstrT,JendT` (110); `DO i=IstrT,IendT` (111); `plant(i,j,iveg,isDens)=800.0_r8       ! Density` (112); `plant(i,j,iveg,isDiam)=0.01_r8        ! Diameter` (113); `plant(i,j,iveg,isHght)=2.0_r8         ! Height` (114); `plant(i,j,iveg,isThck)=0.0005_r8      ! Thickness` (115); `#endif` (119). |
| 121–135 | 시작 시 열린 전처리 조건 없음. 시작 시 63행 `ana_vegetation_tile` 안. WAVE_THRUST_MARSH일 때 Jstr..JendT와 IstrT..IendT 루프에서 marsh_mask를 1로 설정한다(121–132). 주석·반환·루틴 종료를 포함한다(133–135). 원문: `#ifdef WAVE_THRUST_MARSH` (121); `DO j=Jstr,JendT` (127); `DO i=IstrT,IendT` (128); `marsh_mask(i,j)=1.0_r8` (129); `#endif` (132). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 44·66·85·90·121: 호출부의 marsh_mask 선택 매크로는 `MARSH_WAVE_THRUST`이다. 루틴 인수·배열 선언·대입의 선택 매크로는 `WAVE_THRUST_MARSH`이다.
- 97–100: k·Tstr·Tend는 선언 뒤 이 파일에서 참조하지 않는다.
- 108–132: plant 값 대입은 VEG_DRAG 조건 안에만 있다. marsh_mask 값 대입은 WAVE_THRUST_MARSH 조건 안에만 있다. 이 파일에는 경계 교환 루틴 호출이 없다.
