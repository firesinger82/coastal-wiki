---
file: models/FUNWAVE/raw/source_code/FUNWAVE-GPU/src/statistics.F
lines: 163
sha256: 6861ee6c2315149fb954dc72ea2c49087c234c215e0bdd211d423f59bf964c79
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# statistics.F — 판독 구간 기록

구간은 1행부터 163행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–51 | statistics.F·FUNWAVE-TVD 소속·2016년 저작권·Simplified BSD 재배포 조건·무보증 머리말(1–44). 통계량을 계산하는 루틴이라는 설명과 2010년 이력(45–51). 전처리 조건 밖이다. |
| 52–71 | STATISTICS는 GLOBAL을 사용한다(52–54). MassVolume·Energy·MaxEta·MinEta·MaxU·MaxV·Fr·UTotal·UTotalMax·MaxM을 ZERO로 선언 초기화하고 MassVolume0를 선언한다(56–59). `LOGICAL :: FirstCallStatistics = .TRUE.` (60)와 SAVE (61). `# if defined (PARALLEL) \|\| defined (MGPU)` (62)일 때만 myvar를 선언하고 `# endif` (64)로 닫는다. PARALLEL과 MGPU가 모두 없으면 myvar를 제외하며 `#else`는 없다. 매 호출 MassVolume·Energy·UTotalMax를 ZERO로 초기화한다(68–70). 선언 초기화 원문은 `REAL(SP)::MassVolume=ZERO,Energy=ZERO,MaxEta=ZERO,MinEta=ZERO, &` (56), `MaxU=ZERO,MaxV=ZERO,Fr=ZERO,UTotal=ZERO,UTotalMax=ZERO, &` (57), `MaxM=ZERO` (58)이다. 매 호출 초기화는 `MassVolume=ZERO` (68), `Energy=ZERO` (69), `UTotalMax=ZERO` (70)이다. [10-17 전수 검증 보완] |
| 72–96 | 시작 시 52행 STATISTICS 안이다. 내부 격자 루프 `DO J=Jbeg,Jend`·`DO I=Ibeg,Iend` (72–73)와 z=0 기준 체적·에너지 설명 주석(75–76). `# if defined (CARTESIAN)` (78) 참 구간은 `IF(MASK(I,J)>0)THEN` (79)이면 `MassVolume=MassVolume+Eta(I,J)*DX*DY` (80). 이 MASK 조건 밖에서 `Energy=Energy+0.5_SP*H(I,J)*H(I,J)*GRAV*DX*DY &` (83); `+0.5_SP*U(I,J)*U(I,J)*H(I,J)*DX*DY &` (84); `+0.5_SP*V(I,J)*V(I,J)*H(I,J)*DX*DY` (85). `# else` (86)의 CARTESIAN 미정의 구간은 `IF(MASK(I,J)>0)THEN` (87)이면 `MassVolume=MassVolume+Eta(I,J)*DX(I,J)*DY(I,J)` (88). MASK 조건 밖에서 `Energy=Energy+0.5_SP*H(I,J)*H(I,J)*GRAV*DX(I,J)*DY(I,J) &` (90); `+0.5_SP*U(I,J)*U(I,J)*H(I,J)*DX(I,J)*DY(I,J) &` (91); `+0.5_SP*V(I,J)*V(I,J)*H(I,J)*DX(I,J)*DY(I,J)` (92). `# endif` (93), 두 루프 종료·빈 줄(94–96). PARALLEL·MGPU 여부는 이 구간 선택에 관여하지 않는다. 주석 속 체적·에너지 식은 `! Vol=SUM(Eta*dx*dy), reference is at z=0` (75), `! Energy=SUM(1/2*g*H^2*dx*dy+0.5*u^2*H*dx*dy)` (76)이다. 79·87행 MASK IF에는 ELSE가 없다. 이 IF들은 각각 `ENDIF` (81·89)에서 닫힌다. 83–85행 에너지 식은 MASK IF 밖이지만 CARTESIAN 참 분기 안이다. 90–92행 에너지 식은 MASK IF 밖이지만 CARTESIAN 미정의 분기 안이다. [10-17 전수 검증 보완] |
| 97–115 | 시작 시 52행 STATISTICS 안이며 앞 격자 루프 밖이다. `MaxEta=MAXVAL(Eta(Ibeg:Iend,Jbeg:Jend))` (97), `MinEta=MINVAL(Eta(Ibeg:Iend,Jbeg:Jend))` (98), `MaxU=MAXVAL(ABS(U(Ibeg:Iend,Jbeg:Jend)))` (99), `MaxV=MAXVAL(ABS(V(Ibeg:Iend,Jbeg:Jend)))` (100). 내부 격자 루프(103–104)의 `IF(MASK(I,J)>ZERO)THEN` (105) 안에서 `Utotal=SQRT(U(I,J)*U(I,J)+V(I,J)*V(I,J))` (106). `IF(Utotal.gt.UtotalMax)THEN` (107)이면 `UtotalMax=Utotal` (108)로 현재 속력을 복사하고 `Fr=SQRT(GRAV*Max(H(I,J),MinDepthfrc))` (109)를 계산한다. 조건·루프 종료(110–113). `IF(Fr==ZERO)Fr=SQRT(GRAV*MinDepthfrc)` (114)로 Fr가 0일 때 보정한다. 이 구간에는 전처리 조건이 없다. 107·105행 IF에는 ELSE가 없다. 이 IF들은 각각 `ENDIF` (110·111)에서 닫힌다. 114행 Fr 보정은 두 IF와 격자 루프 밖이다. [10-17 전수 검증 보완] |
| 116–135 | 시작 시 52행 STATISTICS 안이다. `# if defined (PARALLEL) \|\| defined (MGPU)` (116) 참 구간에서 MPI_ALLREDUCE를 호출한다. MassVolume·Energy는 MPI_SUM, MaxEta·MaxU·MaxV·UTotalMax·Fr는 MPI_MAX, MinEta는 MPI_MIN을 사용하고 결과 myvar를 각 변수에 복사한다(117–132). `# endif` (133). PARALLEL 또는 MGPU가 정의될 때 집합 연산(collective operation)을 컴파일한다. 두 플래그가 모두 없으면 지역 값을 유지하며 `#else`는 없다. 집합 연산 뒤 복사는 `MassVolume = myvar` (118), `Energy = myvar` (120), `MaxEta = myvar` (122), `MinEta = myvar` (124), `MaxU = myvar` (126), `MaxV = myvar` (128), `UTotalMax = myvar` (130), `Fr = myvar` (132)이다. [10-17 전수 검증 보완] |
| 136–163 | 시작 시 52행 STATISTICS 안이다. `# if defined (PARALLEL) \|\| defined (MGPU)` (136) 안에서 `if (myid.eq.0) then` (137)을 열고 `# endif` (138)로 전처리만 닫는다. PARALLEL 또는 MGPU 정의 시 순위(rank) 0만 표준 출력과 장치 3에 통계량을 쓴다(140–155). 두 플래그가 모두 없으면 순위 조건 없이 출력한다. 출력값은 Time·DT·MassVolume·Energy·수위 극값·방향별 최대 속도·UTotalMax·Fr·`UTotalMax/Fr`·Dmass이다(143–147·151–155). `UTotalMax/Fr`는 Froude 열에 출력한다(146–147·154–155). `# if defined (PARALLEL) \|\| defined (MGPU)` (156) 안의 endif (157)로 순위 조건을 닫고 `# endif` (158). `101  FORMAT(6E12.4)` (160), 빈 줄·루틴 종료(161–163). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 58–61: MaxM·MassVolume0·FirstCallStatistics는 선언 또는 SAVE 이후 이 파일에서 사용되지 않는다.
- 57·68–70·105–114: Fr는 ZERO로 선언 초기화된다. 매 호출 초기화 블록에는 Fr 대입이 없고, 이후 Fr 대입은 최대 속력 갱신 조건과 Fr==ZERO 조건에 있다.
- 79–92·97–100: 체적 누적은 MASK>0 조건 안에 있다. 에너지 누적과 수위·방향별 속도 극값 계산에는 이 MASK 조건이 없다.
- 129–132: UTotalMax와 Fr에는 각각 독립적인 MPI_MAX를 적용한다. 두 값의 원래 격자점이나 순위를 함께 전달하는 연산은 이 구간에 없다.
