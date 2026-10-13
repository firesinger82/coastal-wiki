---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/set_2dfld.F
lines: 207
sha256: db89cd704bd40262a439e964a7c08d0054ebbc840b73bfec04eb505574a35662
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# set_2dfld.F — 판독 구간 기록

구간은 1행부터 207행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–69 | 시작 시 열린 전처리 조건 없음. `#include "cppdefs.h"` (1)는 cppdefs.h를 끼워 넣는다. set_2dfld_mod 모듈·라이선스·2차원 입력 스냅숏(snapshot)의 시간 보간(time interpolation) 설명·implicit none·CONTAINS(2–18). set_2dfld_tile 시작(21–24), 매개변수·병렬·입출력·필드·스칼라 모듈과 exchange_2d_mod 사용(27–33). `#ifdef DISTRIBUTE` (34), `#endif` (36) 안에서 mp_exchange2d를 가져온다. SetBC는 선택 인수, update는 출력, 격자 하한·상한·필드 번호는 입력(40–45). `#ifdef ASSUMED_SHAPE` (47)은 Finp(LBi:,LBj:,:)·Fout(LBi:,LBj:), `#else` (50)는 Finp(LBi:UBi,LBj:UBj,2)·Fout(LBi:UBi,LBj:UBj), `#endif` (53). 지역 논리·인덱스·실수 선언(57–62). `#include "set_bounds.h"` (64)는 set_bounds.h를 끼워 넣는다. 구분·빈 줄·주석 포함(65–69). |
| 70–97 | 시작 시 열린 전처리 조건 없음. 21행 set_2dfld_tile 안. `IF (PRESENT(SetBC)) THEN` (72)은 LapplyBC=SetBC, ELSE(74)는 `LapplyBC=.TRUE.` (75). Lgrided=Linfo(1,ifield,ng)·Lonerec=Linfo(3,ifield,ng)·gtype=Iinfo(1,ifield,ng)·Tindex=Iinfo(8,ifield,ng) 복사 및 update=.TRUE.(80–84). 가중치 준비: `SecScale=1000.0_dp              ! seconds to milliseconds` (90), `it1=3-Tindex` (91), it2=Tindex(92), `fac1=ANINT((Tintrp(it2,ifield,ng)-time(ng))*SecScale,dp)` (93), `fac2=ANINT((time(ng)-Tintrp(it1,ifield,ng))*SecScale,dp)` (94). 주석은 밀리초 정수 반올림과 towards zero를 적는다(86–88). 시간 불변 자료 설명(96–97). |
| 98–138 | 시작 시 열린 전처리 조건 없음. 21행 루틴 안. `IF (Lonerec) THEN` (98) 안 `IF (Lgrided) THEN` (99)이면 j=JstrR..JendR·i=IstrR..IendR에서 Finp(i,j,Tindex)를 복사(100–104). ELSE(105)는 Fpoint(Tindex,ifield,ng)를 Fval에 복사한 뒤 같은 범위 전체에 설정(106–111). 병렬 분기 `ELSE IF (((fac1*fac2).ge.0.0_dp).and.                             &` (116), `&        ((fac1+fac2).gt.0.0_dp)) THEN` (117)은 `fac=1.0_dp/(fac1+fac2)` (118), `fac1=fac*fac1                             ! nondimensional` (119), `fac2=fac*fac2                             ! nondimensional` (120). 내부 `IF (Lgrided) THEN` (121)은 `Fout(i,j)=fac1*Finp(i,j,it1)+fac2*Finp(i,j,it2)` (124). ELSE(127)는 `Fval=fac1*Fpoint(it1,ifield,ng)+fac2*Fpoint(it2,ifield,ng)` (128), 같은 i/j 범위에 Fval 복사(129–133). 동기화(synchronization) 설명 주석(136–138). |
| 139–167 | 시작 시 열린 전처리 조건 없음. 21행 루틴·116–117행 시간 보간 ELSE IF 안. `IF ((time(ng)+dt(ng)).gt.Tintrp(it2,ifield,ng)) THEN` (139) 안의 `IF (DOMAIN(ng)%SouthWest_Test(tile)) synchro_flag(ng)=.TRUE.` (140). 98행 검사의 ELSE(145)는 보간 불가 경로. `IF (DOMAIN(ng)%SouthWest_Test(tile)) THEN` (146) 안 `IF (Master) THEN` (147)이면 변수명·현재 시각·입력 시간 범위·보간 시각·가중치 로그 출력(148–162). Southwest 조건 안에서 exit_flag=2·update=.FALSE.(163–164). 조건 종료·주석(165–167). |
| 168–186 | 시작 시 열린 전처리 조건 없음. 21행 루틴 안. 경계 자료 교환(boundary exchange) 설명(168–169). `IF (update) THEN` (170), 내부 `IF (LapplyBC.and.(EWperiodic(ng).or.NSperiodic(ng))) THEN` (171). `IF (gtype.eq.r2dvar) THEN` (172)은 exchange_r2d_tile 호출(173–175), `ELSE IF (gtype.eq.u2dvar) THEN` (176)은 exchange_u2d_tile 호출(177–179), `ELSE IF (gtype.eq.v2dvar) THEN` (180)은 exchange_v2d_tile 호출(181–183). 각 호출은 ng·tile·격자 경계·Fout를 받는다. gtype 검사·주기 경계(periodic boundary) 조건 종료(184–185), 빈 줄(186). |
| 187–207 | 시작 시 열린 전처리 조건 없음. 21행 루틴·170행 update 분기 안. `#ifdef DISTRIBUTE` (187) 안 `IF (.not.LapplyBC) THEN` (188)이면 mp_exchange2d에 필드 수 1·NghostPoints·두 .FALSE.·Fout를 전달(189–193). ELSE(194)는 같은 호출에 EWperiodic(ng)·NSperiodic(ng)를 전달(195–199). 내부 조건 종료(200), `#endif` (201), update 조건 종료(202). RETURN·루틴 종료·모듈 종료와 빈 줄(203–207). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 86–94: 주석은 nearest milliseconds integer와 towards zero를 함께 적는다. 두 시간 가중치의 실행 식은 ANINT를 호출한다.
- 84·145–165·170: update는 모든 타일(tile)에서 .TRUE.로 시작한다. 보간 불가 ELSE의 exit_flag=2·update=.FALSE.는 SouthWest_Test(tile) 참 분기에만 있다.
