---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/set_ngfldr.F
lines: 142
sha256: 1eed24a0b1d5336b5759889cd21bc815d88b4c2477699ef71388c88e3a011a55
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# set_ngfldr.F — 판독 구간 기록

구간은 1행부터 142행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | 시작 시 열린 전처리 조건 없음. `cppdefs.h`를 끼워 넣고 ADJOINT 조건에서 `set_ngfldr` 루틴을 연다(1–5). 저작권과 비격자 자료(non-gridded data)의 역방향 시간 보간(backward time interpolation) 설명을 포함한다(7–37). 배열 경계·Istr/Iend·Jrec·두 시점 Finp·Fout·update 인수 뜻을 주석으로 적는다. UBj 또는 Jrec에 해당 차원이 없으면 1을 기대한다(24–29). 원문 조건·대입·전처리: `#include "cppdefs.h"` (1); `#ifdef ADJOINT` (2). |
| 39–69 | 시작 시 전처리 조건 `#ifdef ADJOINT` (2) 안. 시작 시 3행 `set_ngfldr` 안. 파라미터·병렬·입출력·NetCDF 메타자료(metadata)·스칼라 모듈을 사용한다(39–43). update와 Fout은 intent(out), Finp(LBi:UBi,UBj,2)는 intent(in)이다(49–56). Lonerec·Tindex·루프 인덱스와 배정밀도(double precision) 계수를 선언한다(60–64). |
| 70–96 | 시작 시 전처리 조건 `#ifdef ADJOINT` (2) 안. 시작 시 3행 `set_ngfldr` 안. Linfo(3)에서 단일 레코드(record) 여부와 Iinfo(8)에서 시점 인덱스를 얻고 update를 참으로 둔다(72–74). SecScale=1000.0_dp, it1=3-Tindex·it2=Tindex이다(80–82). fac1은 현재 시간에서 it2 자료 시점을 뺀 값, fac2는 it1 자료 시점에서 현재 시간을 뺀 값을 ANINT와 SecScale로 처리한다(83–84). Lonerec이면 j=1:Jrec·i=Istr:Iend의 Tindex 자료를 복사한다(88–93). 원문 조건·대입·전처리: `Lonerec=Linfo(3,ifield,ng)` (72); `Tindex=Iinfo(8,ifield,ng)` (73); `update=.TRUE.` (74); `SecScale=1000.0_dp              ! seconds to milliseconds` (80); `it1=3-Tindex` (81); `it2=Tindex` (82); `fac1=ANINT((time(ng)-Tintrp(it2,ifield,ng))*SecScale,dp)` (83); `fac2=ANINT((Tintrp(it1,ifield,ng)-time(ng))*SecScale,dp)` (84); `IF (Lonerec) THEN` (88); `Fout(i,j)=Finp(i,j,Tindex)` (91). |
| 97–115 | 시작 시 전처리 조건 `#ifdef ADJOINT` (2) 안. 시작 시 3행 루틴·88행 IF 안에서 보간 ELSE IF로 전환한다(97). 계수 곱이 0 이상이고 합이 양수이면 두 계수를 합으로 나누고 Fout을 두 시점의 선형 결합(linear combination)으로 계산한다(98–105). time-dt가 it2 자료 시점보다 작으면 synchro_flag를 참으로 둔다(110–112). 오류 경로 주석까지 포함한다(114–115). 원문 조건·대입·전처리: `ELSE IF (((fac1*fac2).ge.0.0_dp).and.(fac1+fac2).gt.0.0_dp) THEN` (97); `fac=1.0_dp/(fac1+fac2)` (98); `fac1=fac*fac1                             ! nondimensional` (99); `fac2=fac*fac2                             ! nondimensional` (100); `Fout(i,j)=fac1*Finp(i,j,it1)+fac2*Finp(i,j,it2)` (103); `IF ((time(ng)-dt(ng)).lt.Tintrp(it2,ifield,ng)) THEN` (110); `synchro_flag(ng)=.TRUE.` (111). |
| 116–142 | 시작 시 전처리 조건 `#ifdef ADJOINT` (2) 안. 시작 시 3행 루틴·88행 IF 안에서 오류 ELSE로 전환한다(116). Master는 변수명·현재 날짜·자료 범위·보간 시점·계수를 stdout으로 출력한다(117–132). exit_flag=2·update=.FALSE.를 설정하고 IF와 루틴을 닫는다(133–137). ADJOINT 불성립 cpp 분기는 인수 없는 `set_ngfldr` 빈 루틴을 정의하고 최종 #endif로 닫는다(138–142). 원문 조건·대입·전처리: `ELSE` (116); `IF (Master) THEN` (117); `exit_flag=2` (133); `update=.FALSE.` (134); `#else` (138); `#endif` (142). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 76–84: 주석은 분수 초를 가장 가까운 밀리초 정수로 0 방향 반올림한다고 적는다. 두 가중치 식은 ANINT(...,dp)를 호출한다.
- 72–84·88–91: Lonerec 분기 전에 두 시점의 가중치를 계산한다. 이 루틴에는 Tindex가 1 또는 2인지 검사하는 문장이 없다.
- 3–5·139–141: ADJOINT 참 분기의 set_ngfldr는 인수를 받는다. 불성립 분기의 같은 이름 루틴에는 인수가 없다.
