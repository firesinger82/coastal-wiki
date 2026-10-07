---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calbuoy.f90
lines: 248
sha256: 03daa5e4ab2fc93ba1b90c68771a6d9cbc0e2f82f0e792207b301d6b7ac89012
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calbuoy.f90 — 판독 구간 기록

구간은 1행부터 248행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | EFDC+ 주소·저장소·2021–2024 DSI 저작권·GPLv2 머리말(1–8). `SUBROUTINE CALBUOY(UPDATE)` 시작(9). 부력(buoyancy)을 UNESCO 상태방정식(equation of state)의 Mellor 근사로 계산한다는 설명과 문헌·변경 기록(11–23). GLOBAL·Allocate_Initialize·GSW 사용(25–27), implicit none(29). UPDATE는 입력 논리값(31), RHOO·ONED·RHO1은 save 실수(33). 압력 PSW의 단위 주석은 dbar 또는 m(35). 기준 압력 선언은 `real(RKD), parameter :: p_ref = 0. ! *** dbar` (37). 잠재수온(potential temperature) PTEM은 save·allocatable 2차원 실수이며 단위는 degC(39). 빈 줄도 포함한다. |
| 41–63 | 시작 시 9행 CALBUOY 루틴 안. `if( (ISGOTM > 0 .or. ISTRAN(2) > 0 ) .and. .not. allocated(PTEM) )then` (41)이면 `call AllocateDSI( PTEM,LCM, KCM, 0.0)` (42)로 PTEM을 할당·0 초기화. `if( IBSC == 1 )then` (46)은 진단용 염분(salinity) 선형 밀도 경로라는 주석(47). K=1..KC·L=2..LA 루프(48–49)의 식은 `B(L,K) = 0.00075_8*SAL(L,K)` (50)이며 return(53). 별도 `if( N <= 5 )then` (58)에서 ONED=1 초기화(59), `TEM0 = ABS(TEMO)` (60), `RHOO = 999.842594 + 6.793952D-2*TEM0 - 9.095290D-3*TEM0*TEM0 + 1.001685D-4*TEM0*TEM0*TEM0 - 1.120083D-6*TEM0*TEM0*TEM0*TEM0 + 6.536332D-9*TEM0*TEM0*TEM0*TEM0*TEM0` (61). 주석은 P=0·S=0·T=TEMO의 기준 밀도를 계산한다고 적는다(57). |
| 64–86 | 시작 시 9행 CALBUOY 루틴 안. OpenMP 병렬 영역 시작(64). `if( UPDATE )then` (68)일 때 ND=1..NDM·K=1..KC·LP=1..LLWET(K,ND) 루프(70–72)에서 L=LKWET로 젖은 셀(wet cell)을 찾고 B1에 현재 B를 복사(73–74). OpenMP DO와 UPDATE 분기 종료(78–79). 밀도 계산용 OpenMP DO는 ND·K·L·LP·NN·NS 및 계산 실수를 private로 지정(84). `do ND = 1,NDM` 시작(85), 빈 줄(86). |
| 87–109 | 시작 시 9행 CALBUOY 루틴·64행 OpenMP 병렬 영역·85행 ND 루프 안. `if( ISTRAN(2) > 0 )then` (88) 안의 `if( ISGOTM > 0 .or. IBSC == 2 )then` (89)은 K=1..KC·LP=1..LLWET(K,ND) 루프(91–92)에서 `PSW = (1. - ZZ(L,K))*HP(L)        ! *** Pressue at the mid point of the layer [m]` (94), TEM을 tm으로 복사(95), `sa  = max(SAL(L,K),0.)            ! *** Absolute Salinity [g/kg] (Prevent negative value)` (96), `PTEM(L,K) = gsw_pt_from_t (sa, tm, PSW, p_ref)` (97). 89행 불성립 else(100)는 같은 K·LP 범위(101–102)에서 PTEM에 TEM을 복사(104). 두 조건 종료(107–108). |
| 110–140 | 시작 시 9행 CALBUOY 루틴·64행 OpenMP 병렬 영역·85행 ND 루프 안. `if( ISTRAN(1) == 0 .and. ISTRAN(2) == 0 )then` (111)은 K·젖은 셀 루프(112–113)에서 무차원 B=0(116). 병렬 분기 `elseif( ISTRAN(1) >= 1 .and. ISTRAN(2) == 0 )then` (121)은 `TEM0 = ABS(TEMO)` (122), K·LP 루프(123–124), `SSTMP = max(SAL(L,K),0.)` (126). 밀도식 원문은 `RHO1 = RHOO + SSTMP*(0.824493 - 4.0899D-3*TEM0       &` (128); `+ 7.6438D-5*TEM0*TEM0                              &` (129); `- 8.2467D-7*TEM0*TEM0*TEM0                         &` (130); `+ 5.3875D-9*TEM0*TEM0*TEM0*TEM0)                   &` (131); `+ SQRT(SSTMP)*SSTMP*(-5.72466D-3 + 1.0227D-4*TEM0  &` (132); `- 1.6546D-6*TEM0*TEM0)                             &` (133); `+ 4.8314D-4*SSTMP*SSTMP` (134). RHOW에 RHO1을 복사하며 단위 주석은 kg/m³(136). `B(L,K) = (RHO1/RHOO)-1._8       ! *** Buoyancy [dimensionless]` (137). 두 루프 종료(138–139). |
| 141–157 | 시작 시 9행 CALBUOY 루틴·64행 OpenMP 병렬 영역·85행 ND 루프·111행 조건의 121행 elseif 분기 안. 다음 병렬 분기는 `elseif( ISTRAN(1) == 0 .and. ISTRAN(2) >= 1 )then` (142). K=1..KC·LP=1..LLWET(K,ND) 루프(143–144)에서 TTMP에 PTEM을 복사(146). `RHO1 = 999.842594 + 6.793952D-2*TTMP - 9.095290D-3*TTMP*TTMP  &` (148); `+ 1.001685D-4*TTMP*TTMP*TTMP                &` (149); `- 1.120083D-6*TTMP*TTMP*TTMP*TTMP           &` (150); `+ 6.536332D-9*TTMP*TTMP*TTMP*TTMP*TTMP` (151). RHOW에 RHO1을 복사(153), `B(L,K) = (RHO1/RHOO)-1._8       ! *** Buoyancy [dimensionless]` (154). 두 루프 종료(155–156). |
| 158–183 | 시작 시 9행 CALBUOY 루틴·64행 OpenMP 병렬 영역·85행 ND 루프·111행 조건의 142행 elseif 분기 안. `elseif( ISTRAN(1) >= 1 .and. ISTRAN(2) >= 1 )then` (159)은 염분·수온을 모두 사용하는 병렬 분기. K·LP 루프(160–161)에서 `SSTMP = max(SAL(L,K),0.)` (163), TTMP에 PTEM 복사(164). `RHTMP = 999.842594 + 6.793952D-2*TTMP - 9.095290D-3*TTMP*TTMP  &` (166); `+ 1.001685D-4*TTMP*TTMP*TTMP                &` (167); `- 1.120083D-6*TTMP*TTMP*TTMP*TTMP           &` (168); `+ 6.536332D-9*TTMP*TTMP*TTMP*TTMP*TTMP` (169). `RHO1 = RHTMP + SSTMP*(0.824493 - 4.0899D-3*TTMP + 7.6438D-5*TTMP*TTMP   &` (171); `- 8.2467D-7*TTMP*TTMP*TTMP                          &` (172); `+ 5.3875D-9*TTMP*TTMP*TTMP*TTMP)                    &` (173); `+ SQRT(SSTMP)*SSTMP*(-5.72466D-3 + 1.0227D-4*TTMP   &` (174); `- 1.6546D-6*TTMP*TTMP)          &` (175); `+ 4.8314D-4*SSTMP*SSTMP` (176). RHOW에 RHO1 복사(178), `B(L,K) = (RHO1/RHOO)-1._8       ! *** Buoyancy [dimensionless]` (179). 루프·밀도 조건 종료(180–182). |
| 184–207 | 시작 시 9행 CALBUOY 루틴·64행 OpenMP 병렬 영역·85행 ND 루프 안. 저농도 퇴적물(sediment) 부력 보정 주석(185). `if( ISTRAN(6) >= 1 .or. ISTRAN(7) >= 1 )then` (186) 안의 K·LP 루프(188–189)에서 TVAR1S·TVAR1W=0(191–192). 그 루프 종료 후 `if( ISTRAN(6) >= 1 )then` (196)은 NS=1..NSED2·K=1..KC·LP=1..LLWET(K,ND) 루프(197–199)에서 `TVAR1S(L,K) = TVAR1S(L,K) + SDEN(NS)*SED(L,K,NS)` (201), `TVAR1W(L,K) = TVAR1W(L,K) + (SSG(NS)-1.)*SDEN(NS)*SED(L,K,NS)` (202). 세 루프·196행 조건 종료(203–206), 186행 조건은 계속 열린다. |
| 208–230 | 시작 시 9행 CALBUOY 루틴·64행 OpenMP 병렬 영역·85행 ND 루프·186행 퇴적물 보정 참 분기 안. `if( ISTRAN(7) >= 1 )then` (208)은 NN=1..NSND 루프(209)에서 `NS = NN+NSED` (210), K·LP 루프(211–212), `TVAR1S(L,K) = TVAR1S(L,K) + SDEN(NS)*SND(L,K,NN)` (214), `TVAR1W(L,K) = TVAR1W(L,K) + (SSG(NS)-1.)*SDEN(NS)*SND(L,K,NN)` (215). 루프·조건 종료(216–219). 별도 `if( ISTRAN(1) == 0 .and. ISTRAN(2) == 0 )then` (221)은 K·LP 루프(223–224)에서 RHOW에 RHOO를 복사(226). 루프·조건 종료(227–229). |
| 231–248 | 시작 시 9행 CALBUOY 루틴·64행 OpenMP 병렬 영역·85행 ND 루프·186행 퇴적물 보정 참 분기 안. K=1..KC·LP=1..LLWET(K,ND) 루프(231–232)에서 `B(L,K) = B(L,K)*(1. - TVAR1S(L,K)) + TVAR1W(L,K)` (234), `RHOW(L,K) = RHOW(L,K)*( 1. - TVAR1S(L,K) + TVAR1W(L,K) )` (237). 두 루프·퇴적물 조건·ND 루프 종료(238–242), OpenMP DO·병렬 영역 종료(243–244), 구분 주석·return·루틴 END(246–248). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 46–54·68–79·136–179: IBSC=1 경로는 B만 계산한 뒤 return한다. 해당 경로는 뒤의 B1 저장과 RHOW 대입에 도달하지 않는다.
- 33·57–62: RHOO는 save 변수이다. 주석은 한 번 계산한다고 적지만 실행 조건은 N<=5이다. 이 파일에는 N>5일 때의 RHOO 초기화가 없다.
- 33·59: ONED는 선언과 1 대입 이후 이 파일에서 참조되지 않는다.
- 111–119·186·221–229: 염분·수온 수송이 모두 0인 분기는 B=0만 설정한다. 같은 조건의 RHOW=RHOO 대입은 퇴적물 보정 조건 안에 있다.
- 94–97: 층 중앙 압력은 `(1. - ZZ(L,K))*HP(L)`로 계산되며 주석 단위는 m이다. 기준 압력 p_ref의 선언 주석은 dbar이다(37). 두 값을 gsw_pt_from_t 인수로 전달하기 전에 별도의 단위 변환문은 이 블록에 없다.
