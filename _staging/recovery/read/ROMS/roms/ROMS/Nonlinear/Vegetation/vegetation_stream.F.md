---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Vegetation/vegetation_stream.F
lines: 163
sha256: 9c96866017963ce8e577b2955bf46303ae243846570f04133d601e7bb748055b
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# vegetation_stream.F — 판독 구간 기록

구간은 1행부터 163행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | cppdefs.h를 포함하고 vegetation_stream_mod를 시작한다(1–2). VEGETATION과 VEG_STREAMING을 모두 정의할 때 구현을 넣는다(4). 식생으로 인한 흐름 변화가 파랑에 미치는 효과라는 주석과 라이선스 머리말이다(6–16). mod_param·mod_forces·mod_grid·mod_scalars·mod_vegetation을 가져오고 vegetation_stream_cal을 공개한다(18–29). 조건·전처리 원문: `#include "cppdefs.h"` (1). `#if defined VEGETATION && defined VEG_STREAMING` (4). |
| 31–68 | 시작 시 전처리 `#if defined VEGETATION && defined VEG_STREAMING` (4) 안. vegetation_stream_cal(ng,tile)을 열고 tile.h를 포함한다(32–44). PROFILE에서 wclock_on/off를 호출한다(46–48·62–64). vegetation_stream_tile에 angler·Dwave·Lwave·dissip_veg·Lveg·BWDXL_veg·BWDYL_veg를 전달한다(49–61). SOLVE3D에서 z_w도 전달한다(53–55). RETURN·루틴 종료·빈 줄을 포함한다(66–68). 조건·전처리 원문: `# include "tile.h"` (44). `# ifdef PROFILE` (46). `# endif` (48). `# ifdef SOLVE3D` (53). `# endif` (55). `# ifdef PROFILE` (62). `# endif` (64). |
| 69–111 | 시작 시 전처리 `#if defined VEGETATION && defined VEG_STREAMING` (4) 안. vegetation_stream_tile의 인수 목록과 배열 선언이다(70–110). SOLVE3D에서 z_w를 넣는다(74–76). ASSUMED_SHAPE에서는 z_w의 수직 하한을 0으로 지정한다(91–93). 명시 크기 분기는 z_w의 마지막 차원을 UBk로 선언한다(102–104). Lveg와 두 파랑 유도 흐름(streaming) 배열의 수직 크기는 N(ng)이다(108–110). 두 출력 배열은 intent(inout)이다. 조건·전처리 원문: `# ifdef SOLVE3D` (74). `# endif` (76). `# ifdef ASSUMED_SHAPE` (89). `#  ifdef SOLVE3D` (91). `#  endif` (93). `# else` (100). `#  ifdef SOLVE3D` (102). `#  endif` (104). `# endif` (111). |
| 112–129 | 시작 시 전처리 `#if defined VEGETATION && defined VEG_STREAMING` (4) 안. 시작 시 70행 vegetation_stream_tile 안. i·j·k·iveg, 작업 계수·파랑 소산(wave dissipation)·수심(depth)·파수(wavenumber) 성분·고유 각주파수(intrinsic angular frequency)와 역수를 선언한다(115–122). 파장(wavelength) 하한은 `real(r8), parameter :: Lwave_min = 1.0_r8` (118). set_bounds.h를 포함하고 실행 구간 주석·빈 줄을 포함한다(124–129). 조건·전처리 원문: `# include "set_bounds.h"` (124). |
| 130–163 | 시작 시 전처리 `#if defined VEGETATION && defined VEG_STREAMING` (4) 안. 시작 시 70행 타일 루틴 안. k=1..N(ng)·j=Jstr..Jend·i=Istr..Iend 루프를 연다(130–132). 수심은 `Dstp=z_w(i,j,N(ng))-z_w(i,j,0)` (133). 파수와 회전된 방향 성분은 `waven=2.0_r8*pi/MAX(Lwave(i,j),Lwave_min)` (139); `cff1=1.5_r8*pi-Dwave(i,j)-angler(i,j)` (140); `wavenx=waven*COS(cff1)` (141); `waveny=waven*SIN(cff1)` (142). 주파수와 역수는 `sigma=MIN(SQRT(g*waven*TANH(waven*Dstp)),2.0_r8)` (143); `osigma=1.0_r8/sigma` (144). 파랑 진폭 계산이라는 주석(136)과 국소 소산·Lveg의 종 수에 대한 확인 주석(147–148)을 포함한다. 소산의 복사 및 힘 계산은 `EWD_veg=dissip_veg(i,j)` (151); `cff2=EWD_veg*osigma*Lveg(i,j,k)` (152); `BWDXL_veg(i,j,k)=cff2*wavenx` (153); `BWDYL_veg(i,j,k)=cff2*waveny` (154). 루프·RETURN·타일 루틴·cpp 조건·모듈 종료까지 포함한다(156–163). 조건·전처리 원문: `#endif` (162). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 92·103·133: ASSUMED_SHAPE의 z_w는 수직 하한 0이다. 명시 크기 선언은 UBk만 지정하여 기본 하한을 사용한다. 수심 식은 두 분기 모두 z_w(i,j,0)을 참조한다.
- 53–55·74–76·91–93·102–104·133: z_w 인수와 선언은 SOLVE3D 조건 안에 있다. z_w를 사용하는 수심 계산은 SOLVE3D 조건 밖에 있다.
- 139·143–144: Lwave에는 하한 1.0_r8을 적용하고 sigma에는 상한 2.0_r8을 적용한다. sigma의 역수 계산 앞에 양의 하한을 적용하거나 0을 검사하는 문장은 없다.
- 115·130–158: iveg는 선언 이후 활성 실행문에서 사용되지 않는다. 실행 루프에는 식생 종 인덱스가 없다.
- 136·139–144: 주석은 파랑 진폭·파수·고유 주파수를 계산한다고 적는다. 해당 활성 블록에는 파랑 진폭 대입이 없다.
