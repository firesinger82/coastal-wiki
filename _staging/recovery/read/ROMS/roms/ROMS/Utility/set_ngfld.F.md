---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/set_ngfld.F
lines: 136
sha256: 2154b79d89a2a6c168384954dce8eb38df894494e8e2c07427c45bbf8202bfef
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# set_ngfld.F — 판독 구간 기록

구간은 1행부터 136행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | 시작 시 열린 전처리 조건 없음. `cppdefs.h`를 끼워 넣고 `set_ngfld` 루틴을 연다(1–4). 저작권과 비격자 자료(non-gridded data)의 시간 보간(time interpolation) 설명을 포함한다(6–36). ng·model·ifield, 배열 경계, Istr/Iend, Jrec, 두 시점 Finp와 Fout·update 인수의 뜻을 주석으로 적는다. UBj 또는 Jrec에 해당 차원이 없으면 1을 기대한다는 주석이다(23–28). 원문 조건·대입·전처리: `#include "cppdefs.h"` (1). |
| 38–68 | 시작 시 열린 전처리 조건 없음. 시작 시 2행 `set_ngfld` 안. 파라미터·병렬·입출력·NetCDF 메타자료(metadata)·스칼라 모듈을 사용한다(38–42). update는 intent(out), Finp(LBi:UBi,UBj,2)는 intent(in), Fout(LBi:UBi,UBj)는 intent(out)이다(48–55). Lonerec, Tindex·i·it1·it2·j와 배정밀도(double precision) 보간 계수를 선언한다(59–63). |
| 69–95 | 시작 시 열린 전처리 조건 없음. 시작 시 2행 `set_ngfld` 안. 전역 Linfo(3)에서 단일 레코드(record) 여부, Iinfo(8)에서 시점 인덱스를 얻고 update를 참으로 둔다(71–73). 초를 밀리초로 바꾸는 SecScale=1000.0_dp와 it1=3-Tindex·it2=Tindex를 설정한다(79–81). fac1은 미래 자료 시점에서 현재 시간을 뺀 값, fac2는 현재 시간에서 이전 자료 시점을 뺀 값을 SecScale과 ANINT로 처리한다(82–83). Lonerec이면 j=1:Jrec·i=Istr:Iend에서 Tindex 자료를 직접 복사한다(87–92). 원문 조건·대입·전처리: `Lonerec=Linfo(3,ifield,ng)` (71); `Tindex=Iinfo(8,ifield,ng)` (72); `update=.TRUE.` (73); `SecScale=1000.0_dp              ! seconds to milliseconds` (79); `it1=3-Tindex` (80); `it2=Tindex` (81); `fac1=ANINT((Tintrp(it2,ifield,ng)-time(ng))*SecScale,dp)` (82); `fac2=ANINT((time(ng)-Tintrp(it1,ifield,ng))*SecScale,dp)` (83); `IF (Lonerec) THEN` (87); `Fout(i,j)=Finp(i,j,Tindex)` (90). |
| 96–114 | 시작 시 열린 전처리 조건 없음. 시작 시 2행 루틴·87행 Lonerec IF 안에서 보간 ELSE IF로 전환한다(96). fac1*fac2가 0 이상이며 합이 양수이면 역합으로 두 계수를 무차원화(nondimensionalization)하고 Fout을 두 시점의 선형 결합(linear combination)으로 계산한다(97–104). 다음 단계 time+dt가 it2 자료 시점을 넘으면 synchro_flag를 참으로 둔다(109–111). 오류 경로 설명 주석까지 포함한다(113–114). 원문 조건·대입·전처리: `ELSE IF (((fac1*fac2).ge.0.0_dp).and.(fac1+fac2).gt.0.0_dp) THEN` (96); `fac=1.0_dp/(fac1+fac2)` (97); `fac1=fac*fac1                             ! nondimensional` (98); `fac2=fac*fac2                             ! nondimensional` (99); `Fout(i,j)=fac1*Finp(i,j,it1)+fac2*Finp(i,j,it2)` (102); `IF ((time(ng)+dt(ng)).gt.Tintrp(it2,ifield,ng)) THEN` (109); `synchro_flag(ng)=.TRUE.` (110). |
| 115–136 | 시작 시 열린 전처리 조건 없음. 시작 시 2행 루틴·87행 IF 안에서 보간 불가 ELSE로 전환한다(115). Master만 변수명·현재 날짜·자료 범위·보간 시점·계수를 stdout으로 출력한다(116–131). 모든 실행자는 exit_flag=2와 update=.FALSE.를 설정한다(132–133). IF·반환·루틴 종료까지 포함한다(134–136). 원문 조건·대입·전처리: `ELSE` (115); `IF (Master) THEN` (116); `exit_flag=2` (132); `update=.FALSE.` (133). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 75–83: 주석은 분수 초를 가장 가까운 밀리초 정수로 0 방향 반올림한다고 적는다. 두 가중치 식은 ANINT(...,dp)를 호출한다.
- 71–83·87–90: Lonerec 분기 전에 두 시점의 가중치를 계산한다. 이 루틴에는 Tindex가 1 또는 2인지 검사하는 문장이 없다.
- 50·69–136: model 인수는 선언 이후 실행문에서 참조하지 않는다.
