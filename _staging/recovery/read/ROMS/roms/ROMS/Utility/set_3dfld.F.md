---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/set_3dfld.F
lines: 225
sha256: 28f134bba8c6acdfd370d8e2955d75cde80a06ac767cc0b10879b2ecdee04feb
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# set_3dfld.F — 판독 구간 기록

구간은 1행부터 225행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–73 | 시작 시 열린 전처리 조건 없음. `#include "cppdefs.h"` (1)는 cppdefs.h를 끼워 넣는다. set_3dfld_mod 모듈(2), `#ifdef SOLVE3D` (3). 라이선스·3차원 스냅숏(snapshot)의 시간 보간(time interpolation) 설명·implicit none·CONTAINS(4–19). set_3dfld_tile 시작(22–25). 매개변수·병렬·입출력·필드·스칼라·exchange_3d 모듈 사용(28–34). `# ifdef DISTRIBUTE` (35), `# endif` (37) 안에서 mp_exchange3d를 가져온다. time_string 사용 선언(38). 선택 입력 SetBC·출력 update·격자 및 수직 범위 인수(42–47). `# ifdef ASSUMED_SHAPE` (49)은 Finp(LBi:,LBj:,LBk:,:)·Fout(LBi:,LBj:,LBk:), `# else` (52)는 Finp(LBi:UBi,LBj:UBj,LBk:UBk,2)·Fout(LBi:UBi,LBj:UBj,LBk:UBk), `# endif` (55). 지역 선언·길이 22 날짜 문자열(59–66). `# include "set_bounds.h"` (68)는 set_bounds.h를 끼워 넣는다. 주석(69–73). |
| 74–103 | 시작 시 3행 `#ifdef SOLVE3D`·22행 set_3dfld_tile 안. `IF (PRESENT(SetBC)) THEN` (76)은 LapplyBC=SetBC, ELSE(78)는 `LapplyBC=.TRUE.` (79). Lgrided=Linfo(1,ifield,ng)·Lonerec=Linfo(3,ifield,ng)·gtype=Iinfo(1,ifield,ng)·Tindex=Iinfo(8,ifield,ng) 복사 및 update=.TRUE.(84–88). 밀리초 반올림 설명(90–92). `SecScale=1000.0_dp              ! seconds to milliseconds` (94), `it1=3-Tindex` (95), it2=Tindex(96), `fac1=ANINT((Tintrp(it2,ifield,ng)-time(ng))*SecScale,dp)` (97), `fac2=ANINT((time(ng)-Tintrp(it1,ifield,ng))*SecScale,dp)` (98). 두 time_string 호출은 주석(99–100). 시간 불변 자료 설명(102–103). |
| 104–152 | 시작 시 3행 `#ifdef SOLVE3D`·22행 루틴 안. `IF (Lonerec) THEN` (104) 안 `IF (Lgrided) THEN` (105)이면 k=LBk..UBk·j=JstrR..JendR·i=IstrR..IendR에서 Finp(i,j,k,Tindex)를 복사(106–112). ELSE(113)는 Fpoint(Tindex,ifield,ng)를 Fval로 복사하고 전체 k/j/i 범위에 설정(114–121). `ELSE IF (((fac1*fac2).ge.0.0_dp).and.                             &` (126), `&        ((fac1+fac2).gt.0.0_dp)) THEN` (127)은 `fac=1.0_dp/(fac1+fac2)` (128), `fac1=fac*fac1                             ! nondimensional` (129), `fac2=fac*fac2                             ! nondimensional` (130). 내부 `IF (Lgrided) THEN` (131)은 `Fout(i,j,k)=fac1*Finp(i,j,k,it1)+fac2*Finp(i,j,k,it2)` (135). ELSE(139)는 `Fval=fac1*Fpoint(it1,ifield,ng)+fac2*Fpoint(it2,ifield,ng)` (140), 전체 k/j/i 범위에 복사(141–147). 동기화(synchronization) 주석(150–152). |
| 153–181 | 시작 시 3행 `#ifdef SOLVE3D`·22행 루틴·126–127행 시간 보간 ELSE IF 안. `IF ((time(ng)+dt(ng)).gt.Tintrp(it2,ifield,ng)) THEN` (153) 안의 `IF (DOMAIN(ng)%SouthWest_Test(tile)) synchro_flag(ng)=.TRUE.` (154). 104행 검사의 ELSE(159)는 보간 불가 경로. `IF (DOMAIN(ng)%SouthWest_Test(tile)) THEN` (160) 안 `IF (Master) THEN` (161)이면 변수명·현재 시각·입력 범위·보간 시각·가중치를 출력(162–176). Southwest 조건 안 exit_flag=2·update=.FALSE.(177–178), 조건 종료(179–180)·주석(181). |
| 182–204 | 시작 시 3행 `#ifdef SOLVE3D`·22행 루틴 안. `IF (update) THEN` (184), 내부 `IF (LapplyBC.and.(EWperiodic(ng).or.NSperiodic(ng))) THEN` (185). `IF (gtype.eq.r3dvar) THEN` (186)은 exchange_r3d_tile 호출(187–189), `ELSE IF (gtype.eq.u3dvar) THEN` (190)은 exchange_u3d_tile 호출(191–193), `ELSE IF (gtype.eq.v3dvar) THEN` (194)은 exchange_v3d_tile 호출(195–197), `ELSE IF (gtype.eq.w3dvar) THEN` (198)은 exchange_w3d_tile 호출(199–201). 각 호출은 ng·tile·수평/수직 격자 경계·Fout를 받는다. gtype 검사·주기 경계(periodic boundary) 조건 종료(202–203)·빈 줄(204). |
| 205–225 | 시작 시 3행 `#ifdef SOLVE3D`·22행 루틴·184행 update 분기 안. `# ifdef DISTRIBUTE` (205) 안 `IF (.not.LapplyBC) THEN` (206)이면 mp_exchange3d에 필드 수 1·수평/수직 범위·NghostPoints·두 .FALSE.·Fout를 전달(207–211). ELSE(212)는 EWperiodic(ng)·NSperiodic(ng)를 전달(213–217). 조건 종료(218), `# endif` (219), update 종료(220), RETURN·루틴 종료(222–223), `#endif` (224), 모듈 종료(225). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 90–98: 주석은 nearest milliseconds integer와 towards zero를 함께 적는다. 두 시간 가중치의 실행 식은 ANINT를 호출한다.
- 88·159–179·184: update는 모든 타일(tile)에서 .TRUE.로 시작한다. 보간 불가 ELSE의 exit_flag=2·update=.FALSE.는 SouthWest_Test(tile) 참 분기에만 있다.
- 38·66·99–100: time_string 사용 선언과 DateString1·DateString2 선언은 남아 있다. 이 파일의 두 time_string 호출은 주석이며 두 문자열을 참조하는 실행문은 없다.
