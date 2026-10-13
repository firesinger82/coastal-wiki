---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/set_zeta.F
lines: 129
sha256: cd00fa5f51d6fb7db906170446b89245a6e1f67c99c49f9ea89077c671041f83
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# set_zeta.F — 판독 구간 기록

구간은 1행부터 129행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 시작 시 열린 전처리 조건 없음; 2행 set_zeta_mod 모듈은 이 구간에서 시작한다. cppdefs.h를 포함한다(1). SOLVE3D에서 자유수면(free surface)을 빠른 시간 단계 평균(fast-time average)으로 설정하는 모듈이다(2–17). 기본 PRIVATE이며 set_zeta를 공개하고 CONTAINS를 연다(19–23). 원문 전처리·조건·반복·대입: `#include "cppdefs.h"` (1); `#ifdef SOLVE3D` (4). |
| 24–57 | 시작 시 전처리 조건 `#ifdef SOLVE3D` (4) 안; 2행 set_zeta_mod 모듈 안. set_zeta는 ng·tile을 받아 mod_param/coupling/ocean을 사용한다(25–39). tile.h를 끼워 넣는다(41). PROFILE에서 wclock_on/off를 호출한다(43–45,51–53). set_zeta_tile에 타일 범위, COUPLING%Zt_avg1 입력과 OCEAN%zeta 출력을 전달한다(46–50). RETURN과 루틴 종료를 포함한다(55–57). 원문 전처리·조건·반복·대입: `character (len=*), parameter :: MyFile =                          &` (38); `&  __FILE__` (39); `# include "tile.h"` (41); `# ifdef PROFILE` (43); `# endif` (45); `# ifdef PROFILE` (51); `# endif` (53). |
| 58–94 | 시작 시 전처리 조건 `#ifdef SOLVE3D` (4) 안; 2행 set_zeta_mod 모듈 안; 59행 set_zeta_tile 루틴은 이 구간에서 시작한다. set_zeta_tile의 인수·모듈과 DISTRIBUTE의 mp_exchange2d를 선언한다(59–71). ASSUMED_SHAPE와 명시 크기를 나누고 Zt_avg1을 입력, zeta를 출력으로 정한다(79–87). 명시 zeta의 마지막 크기는 3이다(86). i/j를 선언하고 set_bounds.h를 끼워 넣는다(91–93). 원문 전처리·조건·반복·대입: `# ifdef DISTRIBUTE` (69); `# endif` (71); `# ifdef ASSUMED_SHAPE` (79); `# else` (83); `# endif` (87); `# include "set_bounds.h"` (93). |
| 95–107 | 시작 시 전처리 조건 `#ifdef SOLVE3D` (4) 안; 2행 set_zeta_mod 모듈·59행 set_zeta_tile 루틴 안. 주석은 2차원 방정식의 다음 시간 적분(time stepping)을 위해 시간 단계 n의 자유수면을 빠른 시간 단계 평균으로 준비한다고 적는다(95–99). j=JstrR..JendR·i=IstrR..IendR에서 zeta의 1·2 슬롯에 모두 같은 Zt_avg1을 대입한다(101–106). 원문 전처리·조건·반복·대입: `DO j=JstrR,JendR` (101); `DO i=IstrR,IendR` (102); `zeta(i,j,1)=Zt_avg1(i,j)` (103); `zeta(i,j,2)=Zt_avg1(i,j)` (104). |
| 108–129 | 시작 시 전처리 조건 `#ifdef SOLVE3D` (4) 안; 2행 set_zeta_mod 모듈·59행 set_zeta_tile 루틴 안. 주기 조건이면 exchange_r2d_tile를 zeta(:,:,1)과 zeta(:,:,2)에 각각 호출한다(108–115). DISTRIBUTE이면 mp_exchange2d에서 두 슬롯을 함께 교환하고 NghostPoints·두 주기 논리를 전달한다(117–124). RETURN·루틴 종료·SOLVE3D 닫힘·모듈 종료를 포함한다(126–129). 원문 전처리·조건·반복·대입: `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (108); `# ifdef DISTRIBUTE` (117); `# endif` (124); `#endif` (128). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 82·86·103–104·108–123: zeta는 intent(out)이고 명시 마지막 차원은 3이다. 이 루틴은 슬롯 1·2만 대입하고 교환한다. 슬롯 3에 대한 대입이나 교환은 이 파일에 없다.
