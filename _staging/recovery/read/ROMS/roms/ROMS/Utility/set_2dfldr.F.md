---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/set_2dfldr.F
lines: 208
sha256: 41855aec08e2e383546e233d71771a47c5e4f5817f214c37ea2561afa3970a48
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# set_2dfldr.F — 판독 구간 기록

구간은 1행부터 208행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–70 | 시작 시 열린 전처리 조건 없음. `#include "cppdefs.h"` (1)는 cppdefs.h를 끼워 넣는다. set_2dfldr_mod 시작(2), `#ifdef ADJOINT` (3). 라이선스·역방향 시간 보간(backward time interpolation) 설명·implicit none·CONTAINS(4–19). set_2dfldr_tile 시작(22–25), 매개변수·병렬·입출력·필드·스칼라 모듈과 exchange_2d_mod 사용(28–34). `# ifdef DISTRIBUTE` (35), `# endif` (37) 안에서 mp_exchange2d를 가져온다. SetBC 선택 입력·update 출력·정수 입력(41–46). `# ifdef ASSUMED_SHAPE` (48)은 Finp(LBi:,LBj:,:)·Fout(LBi:,LBj:), `# else` (51)는 Finp(LBi:UBi,LBj:UBj,2)·Fout(LBi:UBi,LBj:UBj), `# endif` (54). 지역 선언(58–63), `# include "set_bounds.h"` (65)는 set_bounds.h를 끼워 넣는다. 주석·빈 줄(66–70). |
| 71–98 | 시작 시 3행 `#ifdef ADJOINT`·22행 set_2dfldr_tile 안. `IF (PRESENT(SetBC)) THEN` (73)은 LapplyBC=SetBC, ELSE(75)는 `LapplyBC=.TRUE.` (76). Lgrided=Linfo(1,ifield,ng)·Lonerec=Linfo(3,ifield,ng)·gtype=Iinfo(1,ifield,ng)·Tindex=Iinfo(8,ifield,ng) 복사·update=.TRUE.(81–85). 주석은 밀리초 정수 반올림과 towards zero를 적는다(87–89). `SecScale=1000.0_dp              ! seconds to milliseconds` (91), `it1=3-Tindex` (92), it2=Tindex(93), `fac1=ANINT((time(ng)-Tintrp(it2,ifield,ng))*SecScale,dp)` (94), `fac2=ANINT((Tintrp(it1,ifield,ng)-time(ng))*SecScale,dp)` (95). 시간 불변 자료 설명(97–98). |
| 99–139 | 시작 시 3행 `#ifdef ADJOINT`·22행 루틴 안. `IF (Lonerec) THEN` (99)의 `IF (Lgrided) THEN` (100)은 j=JstrR..JendR·i=IstrR..IendR에 Finp(i,j,Tindex)를 복사(101–105). ELSE(106)는 Fpoint(Tindex,ifield,ng)를 Fval에 복사 후 같은 범위를 설정(107–112). `ELSE IF (((fac1*fac2).ge.0.0_dp).and.                             &` (117), `&        ((fac1+fac2).gt.0.0_dp)) THEN` (118)은 `fac=1.0_dp/(fac1+fac2)` (119), `fac1=fac*fac1                             ! nondimensional` (120), `fac2=fac*fac2                             ! nondimensional` (121). 내부 `IF (Lgrided) THEN` (122)은 `Fout(i,j)=fac1*Finp(i,j,it1)+fac2*Finp(i,j,it2)` (125). ELSE(128)는 `Fval=fac1*Fpoint(it1,ifield,ng)+fac2*Fpoint(it2,ifield,ng)` (129), 같은 i/j 범위에 Fval 복사(130–134). 동기화(synchronization) 주석(137–139). |
| 140–168 | 시작 시 3행 `#ifdef ADJOINT`·22행 루틴·117–118행 시간 보간 ELSE IF 안. `IF ((time(ng)-dt(ng)).lt.Tintrp(it2,ifield,ng)) THEN` (140) 안의 `IF (DOMAIN(ng)%SouthWest_Test(tile)) synchro_flag(ng)=.TRUE.` (141). 99행 검사의 ELSE(146)는 보간 불가 경로. `IF (DOMAIN(ng)%SouthWest_Test(tile)) THEN` (147) 안 `IF (Master) THEN` (148)이면 변수명·현재 시각·입력 범위·보간 시각·가중치를 출력(149–163). Southwest 조건 안 exit_flag=2·update=.FALSE.(164–165). 조건 종료·주석(166–168). |
| 169–187 | 시작 시 3행 `#ifdef ADJOINT`·22행 루틴 안. `IF (update) THEN` (171), 내부 `IF (LapplyBC.and.(EWperiodic(ng).or.NSperiodic(ng))) THEN` (172). `IF (gtype.eq.r2dvar) THEN` (173)은 exchange_r2d_tile 호출(174–176), `ELSE IF (gtype.eq.u2dvar) THEN` (177)은 exchange_u2d_tile 호출(178–180), `ELSE IF (gtype.eq.v2dvar) THEN` (181)은 exchange_v2d_tile 호출(182–184). 각 호출은 ng·tile·격자 경계·Fout를 받는다. gtype 조건·주기 경계(periodic boundary) 조건 종료·빈 줄(185–187). |
| 188–208 | 시작 시 3행 `#ifdef ADJOINT`·22행 루틴·171행 update 분기 안. `# ifdef DISTRIBUTE` (188) 안 `IF (.not.LapplyBC) THEN` (189)이면 mp_exchange2d에 필드 수 1·NghostPoints·두 .FALSE.·Fout를 전달(190–194). ELSE(195)는 EWperiodic(ng)·NSperiodic(ng)를 전달(196–200). 조건 종료(201), `# endif` (202), update 종료(203), RETURN·루틴 종료(205–206), `#endif` (207), 모듈 종료(208). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 87–95: 주석은 nearest milliseconds integer와 towards zero를 함께 적는다. 두 시간 가중치의 실행 식은 ANINT를 호출한다.
- 85·146–166·171: update는 모든 타일(tile)에서 .TRUE.로 시작한다. 보간 불가 ELSE의 exit_flag=2·update=.FALSE.는 SouthWest_Test(tile) 참 분기에만 있다.
