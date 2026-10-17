---
file: models/FUNWAVE/raw/source_code/FUNWAVE-TVD/src/statistics.F
lines: 215
sha256: 4c710663a17c77f9603a15fdfba8a79ae9785898745090a566fe4124c15b6d26
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# statistics.F — 판독 구간 기록

구간은 1행부터 215행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–51 | statistics.F·FUNWAVE-TVD 소속·2016년 저작권·Simplified BSD 재배포 조건·무보증 머리말(1–44). 통계량을 계산하는 루틴이라는 설명과 2010년 이력(45–51). 전처리 조건 밖이다. |
| 52–72 | `SUBROUTINE STATISTICS`는 GLOBAL·TIDE_MODULE을 사용한다(52–55). MassVolume·Energy·MaxEta·MinEta·MaxU·MaxV·Fr·UTotal·UTotalMax·MaxM을 ZERO로 선언 초기화하고 MassVolume0를 선언한다(57–60). `LOGICAL :: FirstCallStatistics = .TRUE.` (61)와 SAVE (62). `# if defined (PARALLEL)` (63)일 때만 myvar를 선언하고 `# endif` (65)로 닫는다. PARALLEL이 없으면 이 선언을 제외하며 `#else`는 없다. 매 호출 MassVolume·Energy·UTotalMax를 ZERO로 초기화한다(69–71). 선언 초기화 원문은 `REAL(SP)::MassVolume=ZERO,Energy=ZERO,MaxEta=ZERO,MinEta=ZERO, &` (57), `MaxU=ZERO,MaxV=ZERO,Fr=ZERO,UTotal=ZERO,UTotalMax=ZERO, &` (58), `MaxM=ZERO` (59)이다. 매 호출 초기화 원문은 `MassVolume=ZERO` (69), `Energy=ZERO` (70), `UTotalMax=ZERO` (71)이다. [10-17 전수 검증 보완] |
| 73–97 | 시작 시 52행 STATISTICS 안이다. `DO J=Jbeg,Jend`·`DO I=Ibeg,Iend` (73–74). 수위 기준면 z=0의 체적과 에너지 설명 주석(76–77). `# if defined (CARTESIAN)` (79) 참 구간은 `IF(MASK(I,J)>0)THEN` (80)일 때 `MassVolume=MassVolume+Eta(I,J)*DX*DY` (81)를 누적한다. 이 MASK 조건 밖에서 `Energy=Energy+0.5_SP*H(I,J)*H(I,J)*GRAV*DX*DY &` (84); `+0.5_SP*U(I,J)*U(I,J)*H(I,J)*DX*DY &` (85); `+0.5_SP*V(I,J)*V(I,J)*H(I,J)*DX*DY` (86)를 누적한다. `# else` (87)는 CARTESIAN 미정의 구간이다. 여기서는 `IF(MASK(I,J)>0)THEN` (88)일 때 `MassVolume=MassVolume+Eta(I,J)*DX(I,J)*DY(I,J)` (89). MASK 조건 밖에서 `Energy=Energy+0.5_SP*H(I,J)*H(I,J)*GRAV*DX(I,J)*DY(I,J) &` (91); `+0.5_SP*U(I,J)*U(I,J)*H(I,J)*DX(I,J)*DY(I,J) &` (92); `+0.5_SP*V(I,J)*V(I,J)*H(I,J)*DX(I,J)*DY(I,J)` (93). `# endif` (94), 두 격자 루프 종료(95–96). PARALLEL 여부는 이 구간 선택에 관여하지 않는다. 체적 주석의 원문은 `! Vol=SUM(Eta*dx*dy), reference is at z=0` (76)이다. 에너지 주석의 원문은 `! Energy=SUM(1/2*g*H^2*dx*dy+0.5*u^2*H*dx*dy)` (77)이다. 이 주석 식에는 v 항이 없다. 실행 에너지 식에는 U와 V 항이 모두 있다(84–86·91–93). [10-17 전수 검증 보완] |
| 98–116 | 시작 시 52행 STATISTICS 안이며 격자 합산 루프 밖이다. `MaxEta=MAXVAL(Eta(Ibeg:Iend,Jbeg:Jend))` (98), `MinEta=MINVAL(Eta(Ibeg:Iend,Jbeg:Jend))` (99), `MaxU=MAXVAL(ABS(U(Ibeg:Iend,Jbeg:Jend)))` (100), `MaxV=MAXVAL(ABS(V(Ibeg:Iend,Jbeg:Jend)))` (101). 두 내부 격자 루프(104–105)에서 `IF(MASK(I,J)>ZERO)THEN` (106)이면 `Utotal=SQRT(U(I,J)*U(I,J)+V(I,J)*V(I,J))` (107). 그 안 `IF(Utotal.gt.UtotalMax)THEN` (108)이면 `UtotalMax=Utotal` (109)을 대입하고 `Fr=SQRT(GRAV*Max(H(I,J),MinDepthfrc))` (110)를 계산한다. 조건·루프 종료(111–114). `IF(Fr==ZERO)Fr=SQRT(GRAV*MinDepthfrc)` (115)로 Fr가 0일 때 보정한다. 이 구간에 전처리 조건은 없다. [10-17 전수 검증 보완] |
| 117–136 | 시작 시 52행 STATISTICS 안이다. `# if defined (PARALLEL)` (117) 참 구간에서 MPI_ALLREDUCE로 MassVolume·Energy는 MPI_SUM, MaxEta·MaxU·MaxV·UTotalMax·Fr는 MPI_MAX, MinEta는 MPI_MIN을 구한다(118–133). 각 결과는 myvar에서 해당 변수로 복사한다. `# endif` (134)로 닫는다. PARALLEL이 없으면 이 집합 연산(collective operation)을 제외하고 앞 구간의 지역 값을 유지하며 `#else`는 없다. 집합 연산 결과 복사 원문은 `MassVolume = myvar` (119), `Energy = myvar` (121), `MaxEta = myvar` (123), `MinEta = myvar` (125), `MaxU = myvar` (127), `MaxV = myvar` (129), `UTotalMax = myvar` (131), `Fr = myvar` (133)이다. [10-17 전수 검증 보완] |
| 137–170 | 시작 시 52행 STATISTICS 안이다. `# if defined (PARALLEL)` (137)에서 `if (myid.eq.0) then` (138)을 열고 `# endif` (139)로 전처리만 닫는다. 따라서 PARALLEL 정의 시 순위 0만 통계량을 표준 출력과 장치 3에 쓰며(141–160), 미정의 시 순위 조건 없이 쓴다. 출력에는 Time·DT·MassVolume·Energy·수위 극값·방향별 최대 속도·UTotalMax·Fr·`UTotalMax/Fr`·Dmass가 들어간다(144–148·156–160). 표준 출력의 `IF(TideWest.OR.TideEast.OR.TideSouth.OR.TideNorth)THEN` (149)과 로그의 같은 조건 `IF(TideWest.OR.TideEast.OR.TideSouth.OR.TideNorth)THEN` (161)은 네 경계 조석 수위(tidal elevation)를 출력한다(150–152·162–164). `# if defined (PARALLEL)` (165) 안의 endif (166)로 138행 조건을 닫고 `# endif` (167). `101  FORMAT(6E12.4)` (169). |
| 171–191 | 시작 시 52행 STATISTICS 안이며 출력의 순위 조건 밖이다. `# if defined (PARALLEL)` (171)에서 `if (myid.eq.0) then` (172)을 열고 `# endif` (173). CHECK_STATISTICS를 MassVolume·Energy·MaxEta·MinEta·MaxU·MaxV·UTotalMax·Fr·`UTotalMax/Fr`·Dmass에 각각 호출한다(175–184). PARALLEL 정의 시 순위 0만 호출하고 미정의 시 순위 조건 없이 호출한다. `# if defined (PARALLEL)` (185) 안의 endif (186)로 순위 조건을 닫고 `# endif` (187). STATISTICS 종료·빈 줄(190–191). |
| 192–215 | `CHECK_STATISTICS( val )`는 GLOBAL을 사용한다(194). val 선언은 `REAL(SP), INTENT(IN) :: val` (196)이다. 이 파일만으로 SP의 정밀도를 단정하지 않는다. `IF (ISNAN(val)) THEN` (199)이면 비수치값(Not a Number, NaN) 메시지를 표준 출력과 장치 3에 쓴다(200–201). 이 실행 조건 안의 `#if defined (PARALLEL)` (203) 참 구간에서만 `CALL MPI_ABORT( MPI_COMM_WORLD , 9 , ier)` (204)를 호출하고 `#endif` (205). PARALLEL이 없으면 MPI_ABORT를 제외한다. 두 컴파일 경우 모두 NaN 조건 안에 `STOP` (206)이 남는다. 병렬 코드에서는 MPI_ABORT 호출 뒤에 STOP이 배치된다. MPI_ABORT가 반환하지 않으면 STOP에 도달하지 않는다. 조건·루틴 종료(208–210)와 마지막 빈 줄(211–215). 오류 메시지 원문은 `WRITE(*,*) 'NaN detected in statistics, stopping simulation!'` (200), `WRITE(3,*) 'NaN detected in statistics, stopping simulation!'` (201)이다. [10-17 전수 검증 정정] [10-17 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 60–62: MassVolume0와 FirstCallStatistics는 선언·SAVE 이후 이 파일에서 사용되지 않는다. MaxM도 59행 선언 이후 사용되지 않는다.
- 69–71·106–115: Fr는 58행에서 ZERO로 선언 초기화된다. 매 호출 초기화 블록에는 Fr 대입이 없고, 이후 Fr 대입은 최대 속력 갱신 조건과 Fr==ZERO 조건에 있다.
- 80–93·98–101: 체적 누적은 MASK>0 조건 안에 있다. 에너지 누적과 수위·방향별 속도 극값 계산에는 이 MASK 조건이 없다.
- 130–133: PARALLEL 구간은 UTotalMax와 Fr에 각각 독립적인 MPI_MAX를 적용한다. 두 값의 원래 격자점이나 순위를 함께 전달하는 연산은 이 구간에 없다.
