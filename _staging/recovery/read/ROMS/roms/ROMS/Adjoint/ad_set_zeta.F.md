---
file: models/ROMS/raw/source_code/roms/ROMS/Adjoint/ad_set_zeta.F
lines: 163
sha256: b51e4b75190c603fff802745c6310c15d27925c844f0828c095ddb89853706a2
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ad_set_zeta.F — 판독 구간 기록

구간은 1행부터 163행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | `#include "cppdefs.h"` (1)로 cppdefs.h를 포함한다. 모듈 ad_set_zeta_mod는 2행에서 시작한다. `#if defined ADJOINT && defined SOLVE3D` (4) 안에 저작권·MIT/X 라이선스 주석(6–11), 수반 자유수면(adjoint free-surface)을 빠른 시간(fast time) 평균값으로 설정한다는 설명(13–14), implicit none·PRIVATE·공개 ad_set_zeta·CONTAINS(18–23)를 둔다. |
| 25–59 | 시작 시 4행 `#if defined ADJOINT && defined SOLVE3D` 안. ad_set_zeta(ng,tile) 루틴(26)은 mod_param·mod_coupling·mod_ocean을 사용한다(29–31). ng·tile은 입력 정수(35)이며 `character (len=*), parameter :: MyFile =                          &` (39), `     &  __FILE__` (40)로 파일명을 설정한다. `# include "tile.h"` (42)는 tile.h를 포함한다. `# ifdef PROFILE` (44)·`# endif` (46) 사이 wclock_on(ng,iADM,12,__LINE__,MyFile)(45)을 호출한다. ad_set_zeta_tile에 격자 경계·작업 범위와 COUPLING의 ad_Zt_avg1, OCEAN의 ad_zeta·ad_zeta_sol을 넘긴다(47–52). `# ifdef PROFILE` (53)·`# endif` (55) 사이 같은 계측 번호 12로 wclock_off를 호출한다(54). RETURN·루틴 종료(57–58), 주석(59). |
| 60–98 | 시작 시 4행 `#if defined ADJOINT && defined SOLVE3D` 안. ad_set_zeta_tile 루틴과 인수 목록(61–64), mod_param·mod_scalars·ad_exchange_r2d_tile 사용(67–70). `# ifdef DISTRIBUTE` (71)·`# endif` (73) 안에서 ad_mp_exchange2d를 가져온다(72). 격자 경계·작업 범위는 입력 정수(77–79). `# ifdef ASSUMED_SHAPE` (81)에서는 ad_Zt_avg1·ad_zeta를 가정 형상(assumed shape)의 intent(inout), ad_zeta_sol을 intent(out)으로 선언한다(82–85). `# else` (86)에서는 명시 경계 LBi:UBi·LBj:UBj와 ad_zeta의 세 번째 차원 3을 선언한다(87–90). `# endif` (91). i·j 선언(95), `# include "set_bounds.h"` (97)로 set_bounds.h를 포함한다. |
| 99–137 | 시작 시 4행 `#if defined ADJOINT && defined SOLVE3D`·61행 ad_set_zeta_tile 안. 빠른 시간 평균값이 시간 단계 n에 해당한다는 주석(100–102). `# ifdef DISTRIBUTE` (105)에서는 접선 선형(tangent linear) mp_exchange2d 호출이 `!^` 주석이다(106–111). 실행 ad_mp_exchange2d는 iADM·배열 수 2·NghostPoints·주기 경계 플래그와 ad_zeta(:,:,1)·ad_zeta(:,:,2)를 받는다(113–118). `# endif` (120). `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (122) 안에서 ad_exchange_r2d_tile을 시간 인덱스 2, 이어서 1에 호출한다(127–129·134–136). 대응 접선 선형 호출은 주석이다(123–125·130–132). END IF(137). |
| 138–163 | 시작 시 4행 `#if defined ADJOINT && defined SOLVE3D`·61행 ad_set_zeta_tile 안. 자유수면 해 저장 주석(139–140). j=JstrR..JendR·i=IstrR..IendR 루프(142–146)에서 `ad_zeta_sol(i,j)=ad_zeta(i,j,1)+ad_zeta(i,j,2)` (144). 같은 범위의 두 번째 루프(148–158)에서 접선 선형 복사식은 주석이다(150–151). 수반 누적식은 `ad_Zt_avg1(i,j)=ad_Zt_avg1(i,j)+                              &` (153), `     &                    ad_zeta(i,j,1)+ad_zeta(i,j,2)` (154)이다. 두 자유수면 성분을 0으로 초기화한다(155–156). RETURN·루틴 종료(160–161), `#endif` (162)로 4행 조건을 닫고 모듈을 종료한다(163). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 88·113–118·144·153–156: 명시 형상의 ad_zeta 세 번째 차원은 3이다. 이 루틴의 교환·합산·0 대입은 시간 인덱스 1과 2만 대상으로 한다.
