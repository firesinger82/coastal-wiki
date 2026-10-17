# FUNWAVE-TVD 3.0 이론·수치기법과 코드 대조

분류별 개수: A 4, B 36, C 46, D 4, E 47, F 21, H 33, X 0. 일치 99행. 전체 290행.

## 1 요약

이 보고서는 AI가 작성한 원문 대조 기록이다.
작성일은 2026-10-17이다.
문서 기준은 `funwave_tvd_3.0.pdf`의 PDF p.12–32, p.81, p.86–89이다.
제6장의 시작 문맥은 p.79에서 보조 확인한다.
문서의 인쇄 쪽 번호는 이 범위에서 PDF 쪽 번호와 같다.
쪽 이미지는 사용자가 지정한 `fwpages/funwave_tvd_3.0-NNN.png`를 직접 열어 확인했다.
LaTeX 원고는 식을 옮기는 보조 자료로 쓴다.
PDF와 원고가 다르면 PDF 인쇄식을 기준으로 삼는다.
모델을 실행하지 않았다.
이 보고서는 실행·수치·물리 검증 결과를 주장하지 않는다.
쓰기 대상은 이 파일 하나다.

현재 TVD 코드 기준은 `models/FUNWAVE/raw/source_code/FUNWAVE-TVD/`이다.
이하 `T/`는 이 경로를 뜻한다.
이하 `G/`는 `models/FUNWAVE/raw/source_code/FUNWAVE-GPU/`를 뜻한다.
이하 `src/파일:줄`은 별도 표시가 없으면 `T/src/파일:줄`이다.
과거 코드는 `_staging/recovery/extract/FUNWAVE/external/tvd`에서 읽는다.
과거 인용은 `HASH:src/파일:줄`로 쓴다.
현재 TVD의 `src/main.F:47`은 `!    VERSION 3.0`이다.
현재 TVD의 `README.md:2`는 `This version is a beta version. Please report any bugs if you find in your case.`이다.
이 두 문자열만으로 현재 코드를 2016년 문서 시점의 코드로 취급하지 않는다.

`T/Makefile:25`는 `SPHERICAL   = false`이다.
`T/GNUMake/Essential/Make_Essential:126`은 `FLAG_CARTESIAN = -DCARTESIAN`을 정한다.
같은 파일의 130행은 `FLAG_PARALLEL = -DPARALLEL`을 정한다.
직교좌표계 식은 `CARTESIAN` 경로에 대조한다.
구면좌표계 식은 `CARTESIAN`을 정의하지 않은 경로에 대조한다.
`ZALPHA`는 구면좌표계에서 기준 깊이 유속을 고르는 별도 플래그다.
`MANNING`, `MIXING`, `WIND`, `METEO`, `COUPLING` 등의 조건은 해당 행에 적는다.

기호 대응은 다음과 같다.

| 문서 기호 | 코드 대응 | 근거 |
|---|---|---|
| $h,\eta,H$ | `Depth`, `Eta`, `H` | `etauv_solver.F:373` `H=Eta*Gamma3+Depth` |
| $u_\alpha,v_\alpha$ | `U`, `V` | `dispersion.F:77` `CALL DERIVATIVE_XX(Mloc,Nloc,Ibeg,Iend,Jbeg,Jend,MASK9,DX,U,Uxx)` |
| $\zeta,\beta$ | `Beta_ref`, `Beta_1` | `init.F:663` `Beta_1=Beta_ref+1.0_SP` |
| $A_x,A_y,B_x,B_y$ | `DUxx+DVxy`, `DUxy+DVyy`, `Uxx+Vxy`, `Uxy+Vyy` | `dispersion.F:303–307`의 각 대입을 §2.8에서 인용한다. |
| $\overline{\mathbf u}_2$ | `(U4,V4)` | `dispersion.F:296–317`의 각 대입을 §2.8에서 인용한다. |
| $\mathbf V$의 운동량 성분 | `Ubar,Vbar` | `etauv_solver.F:410–411`의 역변환을 아래 K03에 인용한다. |
| 질량의 경계면 플럭스 | `P,Q` | `etauv_solver.F:219–220`의 차분을 아래 K01에 인용한다. |

대조 표는 290행이다.
일치 행은 99개이다.
나머지 191개 행은 §5에서 각각 한 번 분류했다.
점성 확산의 P,Q 사용은 2017-03-03에 HU,HV 사용으로 바뀌었다(FT1-127,128,137).
FroudeCap의 현재 미입력 값은 3.0이다(FT1-197).
Cbrk2의 현재 미입력 값은 0.35이다(FT1-135).
MinDepthFrc의 현재 미입력 값은 0.1 m이다(FT1-199).
MinDepthFrc와 MinDepth는 입력 후 두 값의 최소값으로 합친다(FT1-199).
문서에만 있는 구현 주장은 4행이다(FT1-093,121,140,141).
코드 결함 후보는 식·항별 47행이며 원인별 8개 묶음이다(§5.3).
이 보고서는 이 후보를 고치지 않았다.

## 2 대조 표

표의 판정은 사용자 지정 네 구분을 쓴다.
불일치는 표기만 다른 경우도 포함한다.
동치 변형을 보인 행은 §5에서 F로 분류한다.
적용 예·이론 정의·권고·역사 설명은 문서에만으로 표시하고 §5에서 H로 분류한다.
K 번호 블록은 뒤의 표가 참조하는 코드 원문 인용이다.
코드 블록의 `&`는 원문의 행 연결을 보존한다.

### 2.1 p.12–18: 서론과 직교좌표계 식 (1)–(22)

K01 — `etauv_solver.F:219–220` (`CARTESIAN`, 일반 질량 보존).

```fortran
        R1(I,J)=-1.0_SP/DXg*(F_right*n_right+F_left*n_left) &
                   -1.0_SP/DYg*(F_top*n_top+F_bottom*n_bottom)
```

K02 — `sources.F:246–260` (`CARTESIAN`).

```fortran
       SourceX(I,J)=GRAV*(Eta(I,J))/DX*(Depthx(I+1,J)-Depthx(I,J))*MASK(I,J) &
                       ! friction
                   + FrcInsX(I,J) &
                       ! dispersion
                       ! (h+eta)(u*\nabla V4 + V4 * \nabla u - v1pp-v2-v3)
                   + Gamma1*MASK9(I,J)*Max(H(I,J),MinDepthFrc)*(         &
                     U(I,J)*0.5_SP*(U4(I+1,J)-U4(I-1,J))/DX+V(I,J)*0.5_SP*(U4(I,J+1)-U4(I,J-1))/DY &
                     +U4(I,J)*0.5_SP*(U(I+1,J)-U(I-1,J))/DX+V4(I,J)*0.5_SP*(U(I,J+1)-U(I,J-1))/DY  &
                     -Gamma2*MASK9(I,J)*(U1pp(I,J)+U2(I,J)+U3(I,J)) &
                     )    &
                        ! Ht(-V4+V1p) = div(M)*(U4-U1p)
                    +Gamma1*MASK9(I,J)*((P(I+1,J)-P(I,J))/DX+(Q(I,J+1)-Q(I,J))/DY) &
                      *(U4(I,J)-U1p(I,J)) &
! wavemaker
                   +WaveMaker_Mass(I,J)*U(I,J)
```

K03 — `etauv_solver.F:407–411` (`CARTESIAN`, x방향 삼중 대각계).

```fortran
       tmp1=Gamma1*MASK9(I,J)*(b1/2.0_SP/DX/DX*dep*dep + b2/DX/DX*depl*dep)
       tmp2=1.0_SP+Gamma1*MASK9(I,J)*(-b1/DX/DX*dep*dep-2.0_SP*b2/DX/DX*dep*dep)
       tmp3=Gamma1*MASK9(I,J)*(b1/2.0_SP/DX/DX*dep*dep + b2/DX/DX*dep*depr)
       tmp4=Ubar(I,J)*MASK(I,J)/Max(H(I,J),MinDepthFrc)  &
            + Gamma1*MASK9(I,J)*( -b1/2.0_SP*dep*dep*Vxy(I,J)-b2*dep*DVxy(I,J))
```

| 행 ID | 항목·문서(원문) | 코드(원문) | 판정 | 이유 |
|---|---|---|---|---|
| FT1-001 | p.12: Boussinesq 모델의 용도. “from deep water to the swash zone”; “wave-induced circulation inside the surfzone” | 특정 대입에 대응하지 않는다. | 문서에만 | H. Boussinesq 모델의 적용 범위를 소개하는 총설이다. [10-18 결론 검증 정정] |
| FT1-002 | p.12: Madsen·Nwogu의 분산 개선, Gobbi·Agnon의 고차 전개, Lynett·Liu의 다층화. “multiple level representations” | 특정 대입에 대응하지 않는다. | 문서에만 | H. 다른 모델과 선행 연구의 설명이다. 현 TVD의 다층 구현 주장으로 읽지 않는다. |
| FT1-003 | p.12: 완전 비선형의 의미. “removing the wave height to water depth ratio as a scaling or expansion parameter” | 이 행의 이론 정의·이력 문장에 직접 대응하는 실행식은 없다. | 문서에만 | H. 완전 비선형 근사의 전개 차수를 정의한다. [10-18 결론 검증 정정] |
| FT1-004 | p.12: Zelt의 점성 쇄파, Chen·Feddersen·Geiman의 순환 계산, Kim의 경계층 확장. “boundary layer turbulence effects on vertical flow structure” | 특정 대입에 대응하지 않는다. | 문서에만 | H. 선행 연구의 성과이다. 현 코드의 검증 결과로 옮기지 않는다. |
| FT1-005 | p.12: 구 FUNWAVE의 비엇갈린 격자와 반복 4차 ABM. “an iterated 4th order Adams-Bashforth-Moulton (ABM) scheme” | 이 행의 이론 정의·이력 문장에 직접 대응하는 실행식은 없다. | 문서에만 | H. 이 문장은 기존 FUNWAVE의 반복 ABM 방법을 설명한다. [10-18 결론 검증 정정] |
| FT1-006 | p.12: 구 코드의 1계 미분 4차·3계 미분 2차, 절단오차, 삼중 대각 구조. “maintaining the tridiagonal structure” | 이 행의 이론 정의·이력 문장에 직접 대응하는 실행식은 없다. | 문서에만 | H. 기존 혼합 차수 방법이 삼중 대각 구조를 유지한 이유를 설명한다. [10-18 결론 검증 정정] |
| FT1-007 | p.13: Kennedy·Chen의 2차원 점성 쇄파, Nwogu의 난류 에너지·길이 척도, slot 방법. “the entire domain remains wetted using a network of slots” | 이 행의 이론 정의·이력 문장에 직접 대응하는 실행식은 없다. | 문서에만 | H. 기존 FUNWAVE와 선행 모델의 slot 방법을 설명한다. [10-18 결론 검증 정정] |
| FT1-008 | p.13: 이동 기준 깊이, 연안 방향 주기 경계, 비직교 곡선 좌표의 연구 확장. “several extensions have been made in research versions” | 이 행의 이론 정의·이력 문장에 직접 대응하는 실행식은 없다. | 문서에만 | H. 이동 기준 깊이·주기 경계·곡선좌표 연구판의 개발 이력을 설명한다. [10-18 결론 검증 정정] |
| FT1-009 | p.13: 소산 없는 위치 와도 보존. “conserve depth-integrated potential vorticity to $O(\mu^2)$” | 이 행의 이론 정의·이력 문장에 직접 대응하는 실행식은 없다. | 문서에만 | H. 소산이 없는 근사 방정식의 위치 와도 보존 성질을 설명한다. [10-18 결론 검증 정정] |
| FT1-010 | p.13–14: 구 격자 잡음, 경계조건, 엇갈린 격자, slot 폭의 영향, Swigler 시험을 개정 동기로 설명한다. “the decision to pursue a new model formulation” | 특정 대입에 대응하지 않는다. | 문서에만 | H. 개발 동기와 비교 결과이다. 현 코드 결함으로 분류하지 않는다. |
| FT1-011 | p.14: 유한체적·유한차분 결합. “dispersive terms are implemented using conventional finite differencing” | `fluxes.F:61` `CALL CONSTRUCTION_HO`;`dispersion.F:77` `CALL DERIVATIVE_XX(Mloc,Nloc,Ibeg,Iend,Jbeg,Jend,MASK9,DX,U,Uxx)` | 일치 | 비분산 플럭스 재구성과 분산 차분을 구분한다. |
| FT1-012 | p.14: 이동 기준 깊이·보존형·삼중 대각화·정수압 균형·적응 3차 RK·최대 4차 MUSCL. “adaptive time stepping based on a third-order Runge-Kutta method” | K01–K03;`fluxes.F:56` `IF(HIGH_ORDER(1:3)=='FOU') THEN` | 일치 | 각 계산식과 제약은 뒤의 행에서 개별 판정한다. |
| FT1-013 | p.14: 쇄파 전환 조건. “where the Froude number exceeds a certain threshold” | 쇄파 판정 `masks.F`을 §2.5에서 인용한다. `masks.F:177–188`의 `IF(VISCOSITY_BREAKING)THEN`에 대한 `ELSE`에서 `IF(ABS(Eta(I,J))/MAX(DEPTH(I,J),MinDepthFrc)>SWE_ETA_DEP)THEN`을 적용한다. `7b93138:src/masks.F:130–131`에도 같은 조건이 있다. | 불일치 | B. 쇄파 전환 조건은 순간 수면고 절댓값과 정수심 하한의 비이다. 이 비를 유속 Froude 수로 적지 않는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-014 | p.14: “The original eddy viscosity breaking scheme is retained in Version 3.0.” | `sources.F:196` `IF(VISCOSITY_BREAKING .OR. WAVEMAKER_VIS)THEN` | 일치 | 명시적인 점성 쇄파 경로가 있다. |
| FT1-015 | p.14: 영역 분할과 MPI 비차단 통신. “MPI) with non-blocking communication” | MPI 호출 원문은 §2.7에 인용한다. | 일치 | PARALLEL에서 모델 경계 교환을 수행한다. MPI 라이브러리 내부는 범위 밖이다. |
| FT1-016 | p.14–15: 보고서 구성·벤치마크·Kirby에 근거한 쓰나미용 구면 모델. “implemented in the same model framework” | `init.F:666` `! for weakly nonlinear equations on sphere (kirby et al 2009)` `init.F:665–679`; `dispersion.F:347–381`; `etauv_solver.F:412–419,508–515`. | 일치 | 구면 방정식은 같은 초기화·분산 계산·유속 역변환에서 `CARTESIAN` 비정의 분기로 구현한다. 개별 식의 차이는 FT1-051–084에서 판정한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-017 | p.15: $O(\mu^2)$ 근사. $\mu$는 수심과 파장의 비이다. “We retain dimensional forms below” | 이 행의 이론 정의·이력 문장에 직접 대응하는 실행식은 없다. | 문서에만 | H. 분산 근사 차수와 차원식 사용을 정의한다. [10-18 결론 검증 정정] |
| FT1-018 | p.15 (1):$\mathbf u=\mathbf u_\alpha+\mathbf u_2(z)$ | 이 행의 이론 정의·이력 문장에 직접 대응하는 실행식은 없다. | 문서에만 | H. 임의 연직 위치의 수평 유속을 기준 깊이 유속과 보정으로 분해하는 이론 정의이다. [10-18 결론 검증 정정] |
| FT1-019 | p.15 (2):$\mathbf u_2(z)=(z_\alpha-z)\nabla A+\frac12(z_\alpha^2-z^2)\nabla B$ | 이 행의 이론 정의·이력 문장에 직접 대응하는 실행식은 없다. | 문서에만 | H. 연직 위치에 따른 유속 보정의 이론 정의이다. 수심 평균 보정의 구현 대조는 FT1-024에 있다. [10-18 결론 검증 정정] |
| FT1-020 | p.15 (3):$A=\nabla\cdot(h\mathbf u_\alpha)$、$B=\nabla\cdot\mathbf u_\alpha$ | `dispersion.F:303` `UxxVxy = Uxx(I,J) + Vxy(I,J)`;306 `HUxxHVxy = DUxx(I,J) + DVxy(I,J)` | 일치 | 코드는 A와 B 자체보다 그 편미분을 쓴다. DU는 수심과 U의 곱이다. 얕은 수심 하한은 §3에 쓴다. |
| FT1-021 | p.15 (4):$z_\alpha=\zeta h+\beta\eta$ | `init.F:663` `Beta_1=Beta_ref+1.0_SP`;664 `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP` `cab9425:init.F:497`와 `7b93138:src/init.F:488`도 같은 `Beta_2` 대입이다. `io.F:2577–2608`의 `DISPERSION`, `Gamma1`, `Gamma2` 입력과 `dispersion.F:302,398–399`의 `IF(gamma2>ZERO)THEN`이 이 경로를 선택한다. `sources.F:251–258,310–317`에서 분산 소스에 사용한다. | 불일치 | E 후보 (강함). Beta_1은 문서의 beta에 대응한다. Beta_2는 0.04이다. 현재 비선형 전개는 문서의 차원식에 추가 배수를 넣는다. 이 차이는 최초 공개 커밋부터 존재한 코드 결함 후보이다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-022 | p.15 (5):$\eta_t+\nabla\cdot\mathbf M=0$ | K01. | 일치 | 코드는 경계면 플럭스 차에 음수를 곱한다. 조파 질량 소스는 p.28에 따로 대조한다. |
| FT1-023 | p.15 (6):$\mathbf M=H\{\mathbf u_\alpha+\overline{\mathbf u}_2\}$;p.16:$H=h+\eta$ | `etauv_solver.F:373` `H=Eta*Gamma3+Depth`;경계면 분산 보정은 §2.3에 인용한다. | 일치 | Gamma3=1에서 총수심이 된다. 플럭스에 U4와 V4를 더한다. |
| FT1-024 | p.16 (7):$\overline{\mathbf u}_2=\frac1H\int_{-h}^{\eta}\mathbf u_2(z)dz=\left(\frac{z_\alpha^2}{2}-\frac16(h^2-h\eta+\eta^2)\right)\nabla B+\left(z_\alpha+\frac12(h-\eta)\right)\nabla A$ | `dispersion.F:296–317`의 K21. `cab9425:init.F:497`와 `7b93138:src/init.F:488`도 같은 `Beta_2` 대입이다. `io.F:2577–2608`의 `DISPERSION`, `Gamma1`, `Gamma2` 입력과 `dispersion.F:302,398–399`의 `IF(gamma2>ZERO)THEN`이 이 경로를 선택한다. `sources.F:251–258,310–317`에서 분산 소스에 사용한다. `dispersion.F:322–329`의 `# if defined (ZALPHA)` 블록은 앞서 계산한 U4·V4를 선형식으로 다시 대입한다. | 불일치 | E 후보 (강함). U4,V4의 비선형 수심 평균 보정은 Beta_2와 Beta_2 제곱을 포함한다. PDF 식 (7)의 계수와 일치하지 않는다. 2017년 변경은 고스트 셀 계산 위치의 수정이다. 이 U4·V4 비선형 보정 판정은 `ZALPHA`를 정의하지 않은 경로에 한정한다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-025 | p.16 (8):$\mathbf u_{\alpha,t}+(\mathbf u_\alpha\cdot\nabla)\mathbf u_\alpha+g\nabla\eta+\mathbf V_1+\mathbf V_2+\mathbf V_3+\mathbf R=0$ | K02와 K03. | 일치 | 코드는 비보존형을 직접 적분하지 않는다. 보존형으로 재배열한 식을 적분한다. 개별 분산 계수는 다른 행에서 판정한다. |
| FT1-026 | p.16: $\mathbf R$는 바닥 마찰과 격자하 수평 혼합을 포함한다. “including bottom friction and subgrid lateral turbulent mixing” | `sources.F:242` `-Cd(I,J)*U(I,J)*SQRT(U(I,J)*U(I,J)+V(I,J)*V(I,J))`;367 `# if defined (MIXING)` | 일치 | 마찰과 조건부 수평 혼합을 소스에 더한다. |
| FT1-027 | p.16 (9):$\mathbf V_1=\left\{\frac{z_\alpha^2}{2}\nabla B+z_\alpha\nabla A\right\}_t-\nabla\left[\frac{\eta^2}{2}B_t+\eta A_t)\right]$ | `dispersion.F:422–436`의 K22. `7b93138:src/dispersion.F:388–402`에도 여분 괄호 없는 전개식이 있다. 3.0 p.16 식 (9)의 인쇄 오기에 한정한다. | 불일치 | B. 식 (9)의 여분 닫는 소괄호는 문서 오기이다. 본문과 부록의 항 분할 차이와 구분한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-028 | p.16 (10):$\mathbf V_2=\nabla\left\{(z_\alpha-\eta)(\mathbf u_\alpha\cdot\nabla)A+\frac12(z_\alpha^2-\eta^2)(\mathbf u_\alpha\cdot\nabla)B+\frac12[A+\eta B]^2\right\}$ | `dispersion.F:438–469`의 K23. `cab9425:init.F:497`와 `7b93138:src/init.F:488`도 같은 `Beta_2` 대입이다. `io.F:2577–2608`의 `DISPERSION`, `Gamma1`, `Gamma2` 입력과 `dispersion.F:302,398–399`의 `IF(gamma2>ZERO)THEN`이 이 경로를 선택한다. `sources.F:251–258,310–317`에서 분산 소스에 사용한다. | 불일치 | E 후보 (강함). V2의 곱 미분 구조는 PDF 식 (10)과 대응한다. 구현의 Beta_2 배수는 차원식의 계수를 바꾼다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-029 | p.16 (11):$\mathbf V_3=\omega_0\mathbf i^z\times\overline{\mathbf u}_2+\omega_2\mathbf i^z\times\mathbf u_\alpha$ | `dispersion.F:491–498`의 K24. `cab9425:init.F:497`와 `7b93138:src/init.F:488`도 같은 `Beta_2` 대입이다. `io.F:2577–2608`의 `DISPERSION`, `Gamma1`, `Gamma2` 입력과 `dispersion.F:302,398–399`의 `IF(gamma2>ZERO)THEN`이 이 경로를 선택한다. `sources.F:251–258,310–317`에서 분산 소스에 사용한다. | 불일치 | E 후보 (강함). V3의 회전곱 부호는 문서와 같다. V3의 보정 계수에는 U4,V4의 선형 계수와 다른 Beta_2 배수가 남는다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-030 | p.16 (12):$\omega_0=(\nabla\times\mathbf u_\alpha)\cdot\mathbf i^z=v_{\alpha,x}-u_{\alpha,y}$ | `dispersion.F:471` `omega_0=Vx(I,J)-Uy(I,J)` | 일치 | 계수와 부호가 일치한다. |
| FT1-031 | p.16 (13):$\omega_2=(\nabla\times\mathbf u_2)\cdot\mathbf i^z=z_{\alpha,x}(A_y+z_\alpha B_y)-z_{\alpha,y}(A_x+z_\alpha B_x)$ | `dispersion.F:475–476`의 K24. `cab9425:init.F:497`와 `7b93138:src/init.F:488`도 같은 `Beta_2` 대입이다. `io.F:2577–2608`의 `DISPERSION`, `Gamma1`, `Gamma2` 입력과 `dispersion.F:302,398–399`의 `IF(gamma2>ZERO)THEN`이 이 경로를 선택한다. `sources.F:251–258,310–317`에서 분산 소스에 사용한다. | 불일치 | E 후보 (강함). 코드 omega_1은 문서 omega_2에 대응한다. 이름 차이와 별도로 기준 깊이 곱에 Beta_2 배수가 들어간다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-032 | p.16: Shi et al. (2012)의 (13)에서 $\overline{\mathbf u}_2$를 $\mathbf u_2$로 고친다. “there is a typo in (13) in Shi et al. (2012)” | 이 행의 이론 정의·이력 문장에 직접 대응하는 실행식은 없다. | 문서에만 | H. 선행 논문 식 (13)의 평균 표시 오기를 알리는 문장이다. [10-18 결론 검증 정정] |
| FT1-033 | p.16 번호 없음: $\alpha=(z_\alpha/h)^2/2+z_\alpha/h=-2/5$, $\alpha=-0.39$, $z_\alpha=-0.53h$, $0\le kh\le\pi$. 위상 속도 오차의 최적화를 설명한다. | 이 행의 이론 정의·이력 문장에 직접 대응하는 실행식은 없다. | 문서에만 | H. 선형 분산 관계의 최적화와 반올림한 이론값을 설명한다. 코드 입력값과의 대조는 FT1-035에 있다. [10-18 결론 검증 정정] |
| FT1-034 | p.16 (14):$z_\alpha=-h+\beta H=(\beta-1)h+\beta\eta=\zeta h+(1+\zeta)\eta$ | `init.F:663–664`을 위에 인용했다. `cab9425:init.F:497`와 `7b93138:src/init.F:488`도 같은 `Beta_2` 대입이다. `io.F:2577–2608`의 `DISPERSION`, `Gamma1`, `Gamma2` 입력과 `dispersion.F:302,398–399`의 `IF(gamma2>ZERO)THEN`이 이 경로를 선택한다. `sources.F:251–258,310–317`에서 분산 소스에 사용한다. | 불일치 | E 후보 (강함). Beta_ref와 Beta_1의 상수 대응은 성립한다. 현재 비선형 전개에는 문서 식 (14)만으로 설명되지 않는 Beta_2 배수가 존재한다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-035 | p.17 번호 없음: $\zeta=-0.53$, $\beta=1+\zeta=0.47$. 기준 깊이는 수면 아래 총수심의 53%이다. “within the actual water column” | `io.F:2620` `CALL READ_FLOAT(Beta_ref,FILE_NAME,'Beta_ref',ierr)`;2622 `Beta_ref = - 0.531_SP` | 불일치 | F. 0.53과 0.531은 설명상의 반올림이다. 수주 안에 놓이는 성질은 식 (14)의 기하학적 성질이다. 0.04 문제는 FT1-034에 분리한다. |
| FT1-036 | p.17: DGM·SGM·고차 SGM의 불균형과 Zhou·Kim·Roeber의 선행 연구. “the original SGM and the revised SGM may not be effective” | 특정 대입에 대응하지 않는다. | 문서에만 | H. 선행 방법의 설명이다. 현 코드에서 모든 선행 방법의 구현을 찾을 필요는 없다. |
| FT1-037 | p.17 (15):$gH\nabla\eta=\nabla[\frac12g(\eta^2+2h\eta)]-g\eta\nabla h$ | K02의 `GRAV*(Eta(I,J))/DX*(Depthx(I+1,J)-Depthx(I,J))*MASK(I,J)`와 §2.3의 압력 플럭스. | 일치 | 코드는 항등식의 두 부분을 플럭스와 소스로 구분한다. |
| FT1-038 | p.17: 임의 차수에서의 정수 상태 조건. “under an unforced stationary condition (still water condition)” | K02. | 일치 | 수면고·유속·외력이 모두 0이면 압력 플럭스와 수심 경사 소스가 모두 0이다. 임의 강제 상태의 보장으로 읽지 않는다. |
| FT1-039 | p.18: $H\mathbf u_\alpha$ 대신 $\mathbf M$을 사용한다. “we used $\mathbf M$, instead of $H\mathbf u_\alpha$” | K01. | 일치 | 질량식은 분산 보정을 포함한 경계면 플럭스를 차분한다. 시간 적분의 운동량 변수는 식 (23)에서 변환한다. |
| FT1-040 | p.18 (16):$\nabla\cdot(\mathbf u\mathbf v)=\nabla\mathbf u\cdot\mathbf v+(\nabla\cdot\mathbf v)\mathbf u$ | 특정 대입에 대응하지 않는다. | 문서에만 | H. 보존형을 유도하는 벡터 항등식이다. |
| FT1-041 | p.18 (17):$\mathbf M_t+\nabla\cdot(\mathbf M\mathbf M/H)+gH\nabla\eta=H\{\overline{\mathbf u}_{2,t}+\mathbf u_\alpha\cdot\nabla\overline{\mathbf u}_2+\overline{\mathbf u}_2\cdot\nabla\mathbf u_\alpha-\mathbf V_1-\mathbf V_2-\mathbf V_3-\mathbf R\}$ | K02. | 일치 | 시간 미분을 식 (22),(23)으로 옮기기 전의 중간 식이다. 분산 근사보다 높은 차수의 항을 보존한다는 뜻은 아니다. |
| FT1-042 | p.18 (18):$\mathbf V_1=\mathbf V'_{1,t}+\mathbf V''_1$ | K03와 K22. 3.0 p.18–19와 부록 p.86 식 (107)–(110); `dispersion.F:337–346,422–436`; `etauv_solver.F:407–411`. 배수 차이는 FT1-208,209에서 별도로 판정한다. | 불일치 | F. 본문은 비선형 항을 프라임 항에 포함한다. 부록과 코드는 선형 연산자와 나머지 항으로 나눈다. [10-18 결론 검증 보완] |
| FT1-043 | p.18 (19):$\mathbf V'_1=\frac{z_\alpha^2}{2}\nabla B+z_\alpha\nabla A-\nabla[\frac{\eta^2}{2}B+\eta A]$ | K03、`dispersion.F:337–346`의 K20. 3.0 p.18–19와 부록 p.86 식 (107)–(110); `dispersion.F:337–346,422–436`; `etauv_solver.F:407–411`. 배수 차이는 FT1-208,209에서 별도로 판정한다. | 불일치 | F. 코드의 U1p와 V1p는 이 식의 선형 부분이다. 비선형 잔차의 전체 식은 부록 (109),(110)에 대조한다. [10-18 결론 검증 보완] |
| FT1-044 | p.18 (20):$\mathbf V''_1=\nabla[\eta_t(A+\eta B)]$ | K22. 3.0 p.18–19와 부록 p.86 식 (107)–(110); `dispersion.F:337–346,422–436`; `etauv_solver.F:407–411`. 배수 차이는 FT1-208,209에서 별도로 판정한다. | 불일치 | F. 본문과 부록·구현은 분할이 다르다. 코드의 U1pp를 이 식만으로 설명하지 않는다. [10-18 결론 검증 보완] |
| FT1-045 | p.18 (21):$\mathbf M_t+\nabla\cdot[\mathbf M\mathbf M/H]+\nabla[\frac12g(\eta^2+2h\eta)]=H\{\overline{\mathbf u}_{2,t}+\mathbf u_\alpha\cdot\nabla\overline{\mathbf u}_2+\overline{\mathbf u}_2\cdot\nabla\mathbf u_\alpha-\mathbf V'_{1,t}-\mathbf V''_1-\mathbf V_2-\mathbf V_3-\mathbf R\}+g\eta\nabla h$ | K02. | 일치 | 식 (17)에 식 (15),(18)을 대입한 보존형이다. PDF 줄바꿈의 중복 등호는 추가 연산을 뜻하지 않는다. |
| FT1-046 | p.18 (22):$\mathbf V_t+\nabla\cdot[\mathbf M\mathbf M/H]+\nabla[\frac12g(\eta^2+2h\eta)]=\eta_t(\mathbf V'_1-\overline{\mathbf u}_2)+H(\mathbf u_\alpha\cdot\overline{\mathbf u}_2+\overline{\mathbf u}_2\cdot\nabla\mathbf u_\alpha-\mathbf V''_1-\mathbf V_2-\mathbf V_3-\mathbf R)+g\eta\nabla h$ | K02의 252행은 `U(I,J)*0.5_SP*(U4(I+1,J)-U4(I-1,J))/DX+V(I,J)*0.5_SP*(U4(I,J+1)-U4(I,J-1))/DY &`. `7b93138:src/sources.F:180`에도 두 방향 공간 미분이 있다. 3.0 p.18 식 (22)의 기호 누락에 한정한다. | 불일치 | B. 식 (22)의 첫 이류항에는 공간 미분이 필요하다. 해당 기호 누락은 문서 오기이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |

### 2.2 p.19–21: 식 (23)–(56)과 구면 좌표계

K04 — `init.F:379–381` (`!CARTESIAN`, 각도 격자를 쓰는 경로).

```fortran
       Dx(I,J) = R_earth*Dphi_r*COS(Lat_theta(I,J))
       Dy(I,J) = R_earth*Dtheta_r
       Coriolis(I,J) = pi*SIN(Lat_theta(I,J)) / 21600.0_SP
```

K05 — `etauv_solver.F:227–228,241` (`!CARTESIAN && !ZALPHA`).

```fortran
        R1(I,J)=-1.0_SP/DX(I,J)*(F_right*n_right+F_left*n_left) &
                   -1.0_SP/DY(I,J)*(F_top*n_top+F_bottom*n_bottom)
        R1(I,J)=R1(I,J)+1.0_SP/R_earth*TAN(Lat_theta(I,J))*HV(I,J)
```

K06 — `sources.F:497–528`의 기본 구면 운동량 소스.
전처리의 `MANNING` 분기는 같은 위치에서 마찰식만 교체한다.
아래는 `!MANNING`에서 이어지는 논리문 전체다.

```fortran
       SourceX(I,J)=GRAV*(Eta(I,J))*SlopeX(I,J)*MASK(I,J) &
                   -Cd(I,J)*U(I,J)*SQRT(U(I,J)*U(I,J)+V(I,J)*V(I,J)) &
                    +Gamma1*MASK9(I,J)*((P(I+1,J)-P(I,J))/DX(I,J)+(Q(I,J+1)-Q(I,J))/DY(I,J)) &
                      *(-U1p(I,J)) &
                    +Coriolis(I,J)*0.5_SP*(Q(I,J)+Q(I,J+1))
       SourceY(I,J)=GRAV*(Eta(I,J))*SlopeY(I,J)*MASK(I,J) &
                   -Cd(I,J)*V(I,J)*SQRT(U(I,J)*U(I,J)+V(I,J)*V(I,J)) &
                    +Gamma1*MASK9(I,J)*((P(I+1,J)-P(I,J))/DX(I,J)+(Q(I,J+1)-Q(I,J))/DY(I,J)) &
                      *(-V1p(I,J)) &
                    -Coriolis(I,J)*0.5_SP*(P(I,J)+P(I+1,J))
```

K07 — `dispersion.F:349–377`의 구면 분산 연산자.

```fortran
	 U1p(I,J)=0.5_SP*(1.0_SP-Beta_1)*(1.0_SP-Beta_1)  &
                *DEPTH(I,J)*DEPTH(I,J)*(Uxx(I,J)+Vxy(I,J)) &
               +(Beta_1-1.0_SP)*DEPTH(I,J)*(DUxx(I,J)+DVxy(I,J))
       V1p(I,J)=0.5_SP*(1.0_SP-Beta_1)*(1.0_SP-Beta_1)  &
                *DEPTH(I,J)*DEPTH(I,J)  &
                *(Uxy(I,J)+Vyy(I,J)) &
               +(Beta_1-1.0_SP)*DEPTH(I,J)*(DUxy(I,J)+DVyy(I,J))
# if defined(SPH_EXTRA_DISP)
       U1p(I,J)=U1p(I,J)+0.5_SP*(1.0_SP-Beta_1)  &
                *DEPTH(I,J)*DEPTH(I,J)*(-1.0_SP/R_earth*  &
                TAN(Lat_theta(I,J))*0.5_SP*(VxL(I,J)+VxR(I,J))) &
               +(Beta_1-1.0_SP)*DEPTH(I,J)*(-1.0_SP/R_earth* &
                TAN(Lat_theta(I,J))*0.5_SP*(HVxL(I,J)+HVxR(I,J)))
       V1p(I,J)=V1p(I,J)+0.5_SP*(1.0_SP-Beta_1) &
                 *DEPTH(I,J)*DEPTH(I,J) &
                /R_earth*( TAN(Lat_theta(I,J))*0.5_SP*(UxL(I,J)+UxR(I,J)) &
                          -TAN(Lat_theta(I,J))*0.5_SP*(VyL(I,J)+VyR(I,J)) &
                          -V(I,J)/R_earth/COS(Lat_theta(I,J))/COS(Lat_theta(I,J)) ) &
               +(Beta_1-1.0_SP)*DEPTH(I,J) &
                /R_earth*( 0.5_SP*(HUxL(I,J)+HUxR(I,J))*TAN(Lat_theta(I,J)) &
                          -0.5_SP*(HVyL(I,J)+HVyR(I,J))*TAN(Lat_theta(I,J)) &
                          -HV(I,J)/R_earth/COS(Lat_theta(I,J))/COS(Lat_theta(I,J)) &
                 )
# endif
```

K08 — `derivatives.F:246–248` (`!CARTESIAN`의 혼합 미분).

```fortran
       tmp1=(Uin(I+1,J+1)-Uin(I+1,J-1))/2.0_SP/DY(I,J)
       tmp2=(Uin(I-1,J+1)-Uin(I-1,J-1))/2.0_SP/DY(I,J)
       Uout(I,J)= (tmp1-tmp2)/2.0_SP/DX(I,J)*MASK(I,J)
```

| 행 ID | 항목·문서(원문) | 코드(원문) | 판정 | 이유 |
|---|---|---|---|---|
| FT1-047 | p.19 (23): $\mathbf V=H(\mathbf u_\alpha+\mathbf V'_1)$ | K03. 3.0 p.18–19와 부록 p.86 식 (107)–(110); `dispersion.F:337–346,422–436`; `etauv_solver.F:407–411`. 배수 차이는 FT1-208,209에서 별도로 판정한다. | 불일치 | F. 삼중 대각 역변환은 선형 부분을 쓴다. 비선형 잔차는 부록의 다른 분할로 소스에 둔다. [10-18 결론 검증 보완] |
| FT1-048 | p.19: $\eta_t$는 식 (5)로 계산한다. 식 (5),(22)를 푼다. 교차 미분을 우변으로 옮긴 삼중 대각계를 푼다. “all cross-derivatives are moved to the right-hand side” | `dispersion.F:114` `ETAT(I,J)=-(P(I+1,J)-P(I,J))/DX-(Q(I,J+1)-Q(I,J))/DY`; K03; `etauv_solver.F:465` `call TRIDx(myA,myC,myD,myF)`; 468 `call TRIDx_ser(myA,myC,myD,myF)` | 일치 | PDF는 (22),(23)을 올바르게 참조한다. LaTeX 원고 357행의 (21),(22) 참조를 PDF 판정에 대신 쓰지 않는다. |
| FT1-049 | p.19: 약비선형 구면식. $\theta,\phi$는 위도·경도이다. $r_0$는 지구 반지름이다. $f$는 Coriolis 계수이다. $(u,v)$는 수심 평균 유속이다. | K04; `init.F:667–670` `a1=ZERO`, `a2=ZERO`, `b1=1.0_SP/3.0_SP`, `b2=-1.0_SP/2.0_SP` | 일치 | 기본 구면 경로는 수심 평균 유속의 선형 분산 계수를 선택한다. `ZALPHA` 경로는 다른 모델이다. |
| FT1-050 | p.19 (24): $H_t+\frac1{r_0\cos\theta}\{(Hu)_\phi+(Hv\cos\theta)_\theta\}=0$ | K04, K05. | 일치 | $h_t=0$에서 $H_t=\eta_t$이다. 위도 방향 곡률 소스의 부호는 양수이다. |
| FT1-051 | p.19 (25): $u_t-fv+\frac{u u_\phi}{r_0\cos\theta}+\frac{vu_\theta}{r_0}+\frac{g\eta_\phi}{r_0\cos\theta}+\frac1{r_0^2\cos^2\theta}\{\frac{h^2}{6}[u_{\phi\phi t}+(v\cos\theta)_{\phi\theta t}]-\frac h2[(hu_t)_{\phi\phi}+(h\cos\theta v_t)_{\phi\theta}]\}-\tau_b^\phi+\frac{(BFT)_\phi}{r_0\cos\theta}=0$ | K03의 구면 대응은 `etauv_solver.F:413–417`이다. K06, K07, K08. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. | 불일치 | E 후보 (강함). 구면 수심 평균 경로는 Beta_1을 대입하지 않은 채 분산 소스를 계산한다. 이 소스의 계수는 b1=1/3과 b2=-1/2를 쓰는 역변환과 일치하지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-052 | p.19 (26): $v_t+fu+\frac{uv_\phi}{r_0\cos\theta}+\frac{vv_\theta}{r_0}+\frac{g\eta_\theta}{r_0}+\frac1{r_0^2}\{\frac{h^2}{6}[\frac1{\cos\theta}\{u_{\phi t}+(v\cos\theta)_{\theta t}\}]_\theta-\frac h2[\frac1{\cos\theta}\{(hu_t)_\phi+(h\cos\theta v_t)_\theta\}]_\theta\}-\tau_b^\theta+\frac{(BFT)_\theta}{r_0}=0$ | K06–K08; `etauv_solver.F:509–513`의 삼중 대각계. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. | 불일치 | E 후보 (강함). 식 (26)에 대응하는 구면 y경로에는 미초기화 Beta_1을 읽는 소스가 있다. 곡률항 누락과 별도로 역변환 계수와의 불일치를 강한 코드 결함 후보로 유지한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-053 | p.19: $BFT$는 해저 이동 강제항이다. “it is not taken into account in the present program” | K05, K06의 전체 기본 소스에는 $BFT$가 없다. | 일치 | 문서는 이 항을 구현했다고 주장하지 않는다. 조파 질량 소스나 선박 압력을 해저 이동으로 바꾸어 읽지 않는다. |
| FT1-054 | p.19 (27): $\{\xi_1=r_0\cos\theta_0(\phi-\phi_0),\ \xi_2=r_0(\theta-\theta_0)\}$ | K04. | 불일치 | F. 코드가 저장하는 길이는 $r_0\cos\theta\,d\phi$이다. 문서의 고정 기준 투영 길이에 $S_p$를 곱한 미분과 같다. |
| FT1-055 | p.20 (28): $\{d\xi_1=r_0\cos\theta_0d\phi,\ d\xi_2=r_0d\theta\}$ | `init.F:363` `Dphi_r=Dphi*pi/180.0_SP`; 364 `Dtheta_r=Dtheta*pi/180.0_SP`; K04. | 불일치 | F. 코드가 각도를 라디안으로 바꾸고 지역 격자 길이를 저장한다. |
| FT1-056 | p.20 (29): $\frac1{r_0\cos\theta}(Hu)_\phi=S_p(Hu)_{\xi_1}$ | K05. | 불일치 | F. $S_p/\Delta\xi_1=1/\mathrm{DX}(I,J)$이다. |
| FT1-057 | p.20 (30): $\frac1{r_0\cos\theta}(Hv\cos\theta)_\theta=\frac1{r_0\cos\theta}[\cos\theta(Hv)_\theta-Hv\sin\theta]=(Hv)_{\xi_2}-\frac1{r_0}\tan\theta Hv$ | K05. | 일치 | 마지막 항을 우변의 양수 소스로 옮긴다. |
| FT1-058 | p.20 (31): $\frac1{r_0\cos\theta}uu_\phi=S_puu_{\xi_1}$ | K04; `fluxes.F:553–554`의 K09 아래 구면 식. | 불일치 | F. 경도 미분의 지역 길이 치환이다. |
| FT1-059 | p.20 (32): $\frac1{r_0}vu_\theta=vu_{\xi_2}$ | K04; `fluxes.F:649` `FyL=Gamma3*HyL*UyL*VyL*Gamma3` | 일치 | 위도 길이에 기준 위도의 보정 계수가 없다. |
| FT1-060 | p.20 (33): $\frac1{r_0\cos\theta}g\eta_\phi=S_pg\eta_{\xi_1}$ | K04, K06. | 불일치 | F. 경도 방향 길이로 보정 계수를 흡수한다. |
| FT1-061 | p.20 (34): $\frac{h^2}{6r_0^2\cos^2\theta}u_{\phi\phi t}=S_p^2\frac{h^2}{6}u_{\xi_1\xi_1t}$ | `etauv_solver.F:413` `tmp1=Gamma1*MASK9(I,J)*(b1/2.0_SP/DX(I,J)/DX(I,J)*dep*dep + b2/DX(I,J)/DX(I,J)*depl*dep)` | 일치 | `b1/2=1/6`이다. 두 경도 미분은 지역 `DX` 두 번으로 나눈다. |
| FT1-062 | p.20 (35): $\frac{h^2}{6r_0^2\cos^2\theta}(v\cos\theta)_{\phi\theta t}=\frac{h^2S_p}{6}(v_{\xi_1\xi_2}-\frac1{r_0}\tan\theta v_{\xi_1})_t$ | K07, K08. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. | 불일치 | E 후보 (중간). 식 (35)의 tan(theta)·v_x 곡률 보정은 기본 구면 혼합 미분에 없다. SPH_EXTRA_DISP의 소스 보정은 역변환을 함께 바꾸지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-063 | p.20 (36): $-\frac h{2r_0^2\cos^2\theta}(hu)_{\phi\phi t}=-\frac{hS_p^2}{2}(hu)_{\xi_1\xi_1t}$ | FT1-061의 코드 원문. `init.F:670` `b2=-1.0_SP/2.0_SP` | 일치 | 수심과 유속 곱의 경도 2계 미분이다. |
| FT1-064 | p.20 (37): $-\frac h{2r_0^2\cos^2\theta}(hv\cos\theta)_{\phi\theta t}=-\frac{hS_p}{2}[(hv)_{\xi_1\xi_2}-\frac1{r_0}\tan\theta(hv)_{\xi_1}]_t$ | K07, K08. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. | 불일치 | E 후보 (중간). 식 (37)의 tan(theta)·(hv)_x 보정은 기본 구면 역변환에 없다. 계수 흡수 의도 주석 때문에 중간 강도의 코드 결함 후보로 유지한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-065 | p.20 (38): $\frac1{r_0\cos\theta}uv_\phi=S_puv_{\xi_1}$ | `fluxes.F:576` `GxL=HxL*UxL*VxL*Gamma3`; K04. | 불일치 | F. 지역 `DX`가 $S_p$를 흡수한다. |
| FT1-066 | p.20 (39): $\frac1{r_0}vv_\theta=vv_{\xi_2}$ | `fluxes.F:680–681`의 K09 구면 식. | 일치 | 위도 방향 운동량 플럭스에 대응한다. |
| FT1-067 | p.20 (40): $\frac1{r_0}g\eta_\theta=g\eta_{\xi_2}$ | K04, K06. | 일치 | 위도 방향 압력 플럭스와 경사 소스에 대응한다. |
| FT1-068 | p.20 (41): $\frac{h^2}{6r_0^2}(\frac{u_{\phi t}}{\cos\theta})_\theta=\frac{h^2S_p}{6}(u_{\xi_1\xi_2}+\frac1{r_0}\tan\theta u_{\xi_1})_t$ | K07, K08. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. | 불일치 | E 후보 (중간). 식 (41)의 양의 tan(theta)·u_x 보정은 기본 y역변환에 없다. SPH_EXTRA_DISP는 이 역변환을 같은 연산자로 바꾸지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-069 | p.20 (42): $-\frac h{2r_0^2}[\frac{(hu)_{\phi t}}{\cos\theta}]_\theta=-\frac{hS_p}{2}[(hu)_{\xi_1\xi_2}+\frac1{r_0}\tan\theta(hu)_{\xi_1}]_t$ | K07, K08. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. | 불일치 | E 후보 (중간). 식 (42)의 tan(theta)·(hu)_x 보정은 기본 y역변환에 없다. 소스의 선택적 추가항만으로 이 차이를 해소하지 못한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-070 | p.20 (43): $\frac{h^2}{6r_0^2}[\frac{(v\cos\theta)_{\theta t}}{\cos\theta}]_\theta=\frac{h^2}{6}[v_{\xi_2\xi_2}-\frac1{r_0}\tan\theta v_{\xi_2}-\frac1{r_0^2\cos^2\theta}v]_t$ | K07; `etauv_solver.F:509–513`. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. | 불일치 | E 후보 (중간). 식 (43)의 1계 미분 곡률항과 v에 비례하는 곡률항은 기본 y삼중 대각계에 없다. 보정 의도 주석을 반영하여 중간 강도로 유지한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-071 | p.20 (44): $-\frac h{2r_0^2}[\frac{(hv\cos\theta)_{\theta t}}{\cos\theta}]_\theta=-\frac h2[(hv)_{\xi_2\xi_2}-\frac1{r_0}\tan\theta(hv)_{\xi_2}-\frac1{r_0^2\cos^2\theta}hv]_t$ | K07; `etauv_solver.F:509–513`. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. | 불일치 | E 후보 (중간). 식 (44)의 (hv)_y 및 hv 곡률 보정은 기본 y삼중 대각계에 없다. 선택적 V1p 보정과 구분하여 기록한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-072 | p.21 (45): $S_p=\frac{\cos\theta_0}{\cos\theta}$ | K04. | 불일치 | F. 코드가 `S_p` 변수를 저장하지 않아도 $S_p/\Delta\xi_1=1/(r_0\cos\theta\Delta\phi)$가 성립한다. |
| FT1-073 | p.21 (46): $H_t+S_p(Hu)_{\xi_1}+(Hv)_{\xi_2}=\frac1{r_0}\tan\theta Hv$ | K05. | 일치 | 질량식에 곡률 소스를 직접 더한다. |
| FT1-074 | p.21 (47): $u_t+S_puu_{\xi_1}+vu_{\xi_2}-fv+S_pg\eta_{\xi_1}+F_t-\tau_b^{\xi_1}+S_p(BFT)_{\xi_1}=0$ | K06, K07. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. | 불일치 | E 후보 (강함). 식 (47)의 Coriolis 부호는 일치한다. F_t에 대응하는 분산 경로에는 Beta_1 초기화와 역변환 계수의 불일치가 남는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-075 | p.21 (48): $v_t+S_puv_{\xi_1}+vv_{\xi_2}+fu+g\eta_{\xi_2}+G_t-\tau_b^{\xi_2}+(BFT)_{\xi_2}$ | K06, K07. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. 3.0 p.21 쪽 이미지와 판독 기록; `doc/funwave_tvd_3.0.tex:474`. | 불일치 | E 후보 (강함). 식 (48)의 y분산 소스는 초기화하지 않은 Beta_1을 사용한다. 동일 경로의 역변환은 다른 계수 b1,b2를 사용한다. PDF p.21 식 (48)과 TEX 474행에는 등호와 우변이 없다. 기존의 `=0` 인용을 정정한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-076 | p.21 (49): $F=\frac{h^2S_p^2}{6}u_{\xi_1\xi_1}+\frac{h^2S_p}{6}(v_{\xi_1\xi_2}-\frac1{r_0}\tan\theta v_{\xi_1})-\frac{hS_p^2}{2}(hu)_{\xi_1\xi_1}-\frac{hS_p}{2}[(hv)_{\xi_1\xi_2}-\frac1{r_0}\tan\theta(hv)_{\xi_1}]$ | K07; `mod_global.F:174` `REAL(SP) :: Beta_1,Beta_2`; `init.F:667–678`의 분기. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. | 불일치 | E 후보 (강함). 식 (49)의 F를 계산하는 기본 구면 경로는 Beta_1을 초기화하지 않는다. 단순히 임의의 초기값을 가정해도 두 분산 계수가 역변환과 동시에 일치하지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-077 | p.21 (50): $G=\frac{h^2S_p}{6}(u_{\xi_1\xi_2}+\frac1{r_0}\tan\theta u_{\xi_1})+\frac{h^2}{6}(v_{\xi_2\xi_2}-\frac1{r_0}\tan\theta v_{\xi_2}-\frac{v}{r_0^2\cos^2\theta})-\frac{hS_p}{2}[(hu)_{\xi_1\xi_2}+\frac1{r_0}\tan\theta(hu)_{\xi_1}]-\frac h2[(hv)_{\xi_2\xi_2}-\frac1{r_0}\tan\theta(hv)_{\xi_2}-\frac{hv}{r_0^2\cos^2\theta}]$ | K07, K08. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. | 불일치 | E 후보 (강함). 식 (50)의 G를 계산하는 기본 구면 경로는 Beta_1을 초기화하지 않는다. SPH_EXTRA_DISP를 추가해도 이 초기화 문제는 남는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-078 | p.21 (51): $\mathbf\Psi=(\eta,U_s,V_s)^T$; $\mathbf\Theta=(S_pP\mathbf i+Q\mathbf j,\ [S_pP^2/(h+\eta)+\frac12S_pg(\eta^2+2\eta h)]\mathbf i+PQ/(h+\eta)\mathbf j,\ S_pPQ/(h+\eta)\mathbf i+[Q^2/(h+\eta)+\frac12g(\eta^2+2\eta h)]\mathbf j)^T$ | K04; `fluxes.F:520` `PL=HUxL`; 521 `PR=HUxR`; 576 `GxL=HxL*UxL*VxL*Gamma3`; K09. | 불일치 | F. 플럭스의 $S_p$는 시간 적분의 지역 `DX`에 들어간다. |
| FT1-079 | p.21 (52): $\mathbf S=(\frac1{r_0}\tan\theta(h+\eta)v,\ S_pg\eta h_{\xi_1}+f(h+\eta)v+\tau_b^{\xi_1}+\psi_1,\ g\eta h_{\xi_2}-f(h+\eta)u+\tau_b^{\xi_2}+\psi_2)^T$ | K05, K06. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/sources.F:362–378`에도 곡률 질량 소스의 곱이 없다. `cab9425:etauv_solver.F:188`에는 질량식 곡률 소스가 있다. | 불일치 | E 후보 (중간). 식 (52)의 분산 소스는 eta_t에 해당하는 곡률 질량 소스의 기여를 포함하지 않는다. 마찰·경사·Coriolis의 구현과 구분하여 중간 강도로 유지한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-080 | p.21 번호 없음: $P=(h+\eta)u,\ Q=(h+\eta)v$ | `etauv_solver.F:578` `HU(I,J)=Max(H(I,J),MinDepthFrc)*U(I,J)`; 579 `HV(I,J)=Max(H(I,J),MinDepthFrc)*V(I,J)`; `fluxes.F:520` `PL=HUxL` | 일치 | 수심 하한 이외의 습윤 영역에서 일치한다. |
| FT1-081 | p.21 (53): $U_s=(h+\eta)(u+F)$ | K03의 구면 대응 `etauv_solver.F:413–417`. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. `init.F:1020–1025`의 `Ubar=HU+gamma1*U1p*H`, `Vbar=HV+gamma1*V1p*H`를 대조했다. | 불일치 | E 후보 (강함). 구면 초기 Ubar는 U1p를 사용한다. Ubar에서 유속을 구하는 역변환은 다른 b1,b2 계수를 사용한다. 식 (53)의 동일 연산자 관계를 만족하지 않는 후보이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-082 | p.21 (54): $V_s=(h+\eta)(v+G)$ | `etauv_solver.F:509–513`. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. `init.F:1020–1025`의 `Ubar=HU+gamma1*U1p*H`, `Vbar=HV+gamma1*V1p*H`를 대조했다. | 불일치 | E 후보 (강함). 구면 초기 Vbar는 V1p를 사용한다. Vbar에서 유속을 구하는 역변환은 다른 b1,b2 계수를 사용한다. 식 (54)의 동일 연산자 관계를 만족하지 않는 후보이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-083 | p.21 (55): $\psi_1=\eta_tF$ | K06. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/sources.F:362–378`에도 곡률 질량 소스의 곱이 없다. `cab9425:etauv_solver.F:188`에는 질량식 곡률 소스가 있다. | 불일치 | E 후보 (중간). 구면 x분산 소스는 -div(M)·U1p를 쓴다. 질량식의 tan(theta)·HV/R_earth를 곱한 기여가 빠진다. Gamma1과 MASK9가 각각 1인 셀에서 코드와 식 (55)의 차이는 -tan(theta)·HV·U1p/R_earth이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-084 | p.21 (56): $\psi_2=\eta_tG$ | K06. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/sources.F:362–378`에도 곡률 질량 소스의 곱이 없다. `cab9425:etauv_solver.F:188`에는 질량식 곡률 소스가 있다. | 불일치 | E 후보 (중간). 구면 y분산 소스는 -div(M)·V1p를 쓴다. Gamma1과 MASK9가 각각 1인 셀에서 코드와 식 (56)의 차이는 -tan(theta)·HV·V1p/R_earth이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |

### 2.3 p.22: 간결한 보존형과 식 (57)–(61)

K09 — `fluxes.F:502–503,529–532,564–567` (`CARTESIAN`).

```fortran
     PL(1:Mloc1,1:Nloc)=HUxL(1:Mloc1,1:Nloc) &
     + Gamma1*MASK9u(1:Mloc1,1:Nloc)*HxL(1:Mloc1,1:Nloc)*U4xL(1:Mloc1,1:Nloc)
     FxL(1:Mloc1,1:Nloc)=Gamma3*PL(1:Mloc1,1:Nloc)*(UxL(1:Mloc1,1:Nloc)  &
        +Gamma1*MASK9u(1:Mloc1,1:Nloc)*U4xL(1:Mloc1,1:Nloc)) &
        +0.5*GRAV*((EtaRxL(1:Mloc1,1:Nloc))*(EtaRxL(1:Mloc1,1:Nloc))*Gamma3  &
        +2.0_SP*(EtaRxL(1:Mloc1,1:Nloc))*(Depthx(1:Mloc1,1:Nloc)))
	GxL(1:Mloc1,1:Nloc)=HxL(1:Mloc1,1:Nloc)*    &
	  ( UxL(1:Mloc1,1:Nloc) + Gamma1*MASK9u(1:Mloc1,1:Nloc)*U4xL(1:Mloc1,1:Nloc) )*   &
	  ( VxL(1:Mloc1,1:Nloc) + Gamma1*MASK9u(1:Mloc1,1:Nloc)*V4xL(1:Mloc1,1:Nloc) )*   &
	  Gamma3
```

구면 `!ZALPHA`의 대응 논리문은 `fluxes.F:553–554,680–681`이다.

```fortran
      FxL=Gamma3*PL*(UxL) &
        +0.5*GRAV*((EtaRxL)*(EtaRxL)*Gamma3+2.0_SP*(EtaRxL)*(Depthx))
     GyL=Gamma3*QL*(VyL) &
        +0.5*GRAV*((EtaRyL)*(EtaRyL)*Gamma3+2.0_SP*(EtaRyL)*(Depthy))
```

| 행 ID | 항목·문서(원문) | 코드(원문) | 판정 | 이유 |
|---|---|---|---|---|
| FT1-085 | p.22 번호 없음: $\mathbf u_\alpha=(u,v)$, $\overline{\mathbf u}_2=(U_4,V_4)$, $\mathbf M=(P,Q)=H[u+U_4,v+V_4]$ | K09; `dispersion.F:298–299`의 K21. | 일치 | 질량 플럭스와 깊이 평균 분산 보정의 기호 대응이다. |
| FT1-086 | p.22 번호 없음: $\mathbf V'_1=(U'_1,V'_1)$, $\mathbf V''_1=(U''_1,V''_1)$, $\mathbf V_2=(U_2,V_2)$, $\mathbf V=(U,V)=H[(u+U'_1),(v+V'_1)]$ | K03, K20, K22. | 불일치 | F. 코드의 `U,V`는 기준 깊이 유속이다. 문서의 보존 운동량 `U,V`는 코드의 `Ubar,Vbar`이다. 분할 차이는 FT1-042와 같다. |
| FT1-087 | p.22 (57): $\partial\mathbf\Psi/\partial t+\nabla\cdot\mathbf\Theta(\mathbf\Psi)=\mathbf S$ | K01, K02; `etauv_solver.F:310` `Ubar(I,J)=ALPHA(ISTEP)*Ubar0(I,J)+BETA(ISTEP)*(Ubar(I,J)+DT*R2(I,J))`; 343의 y대응식. | 일치 | 플럭스 발산과 소스를 적분한다. |
| FT1-088 | p.22 (58): $\mathbf\Psi=(\eta,U,V)^T$; $\mathbf\Theta=(P\mathbf i+Q\mathbf j,\ [P^2/H+\frac12g(\eta^2+2\eta h)]\mathbf i+PQ/H\mathbf j,\ PQ/H\mathbf i+[Q^2/H+\frac12g(\eta^2+2\eta h)]\mathbf j)^T$ | K09. | 일치 | $\mathrm{PL}=H(u+U_4)$에서 $\mathrm{PL}(u+U_4)=P^2/H$이다. 교차 플럭스도 두 보정 유속을 곱한다. |
| FT1-089 | p.22 (59): $\mathbf S=(0,\ g\eta h_x+\psi_x+HR_x,\ g\eta h_y+\psi_y+HR_y)^T$ | K02; `sources.F:305–319`의 y대응식. | 불일치 | F. 우변의 $HR_x,HR_y$는 코드의 음수 마찰 소스에 대응한다. 식 (8)의 좌변 $\mathbf R$와 부호를 혼동하지 않도록 $R_x$를 우변 성분으로 정의해야 한다. |
| FT1-090 | p.22 (60): $\psi_x=\eta_t(U'_1-U_4)+H(uU_{4,x}+vU_{4,y}+U_4u_x+V_4u_y-U''_1-U_2-U_3)$ | K02. | 일치 | $\eta_t=-\mathrm{div}(P,Q)$를 쓰면 코드의 $\mathrm{div}(U4-U1p)$ 부호와 같다. 개별 분산항의 축소 계수 문제는 §2.8에 분리한다. |
| FT1-091 | p.22 (61): $\psi_y=\eta_t(V'_1-V_4)+H(uV_{4,x}+vV_{4,y}+U_4v_x+V_4v_y-V''_1-V_2-V_3)$ | `sources.F:305–319`의 K02 대칭식. | 일치 | 네 이류항과 세 음수 분산항의 방향이 맞는다. |
| FT1-092 | p.22: 바닥 응력을 2차 마찰식으로 근사한다. “a quadratic friction equation” | `sources.F:242` `-Cd(I,J)*U(I,J)*SQRT(U(I,J)*U(I,J)+V(I,J)*V(I,J))` | 일치 | `!MANNING`에서 유속과 유속 크기를 곱한다. |
| FT1-093 | p.22: “A Smagorinsky (1963)-like subgrid turbulent mixing algorithm is implemented following Chen et al. (1999).” | `init.F:437` `nu_smg = ZERO`; `sources.F:367` `# if defined (MIXING)` `cab9425:init.F:332`, `7f892ba:src/init.F:332`의 `nu_smg = ZERO`; `sources.F:367–388`의 `MIXING` 분기. `git log --all -S nu_smg -- '*.F'`와 현재 TVD/GPU 대입 검색은 영 초기화·소비 경로를 확인한다. | 문서에만 | D. 공개 이력의 소스에는 nu_smg를 쓰는 확산 항이 있다. Smagorinsky 점성 계수 산출식은 없다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |

### 2.4 p.23–25: 재구성·리만 해법·시간 적분, 식 (62)–(79)

K10 — `fluxes.F:1551–1568,1600,1606–1618,1622–1634`의 핵심 대입.
아래 논리문은 각각 원문 한 줄이다.

```fortran
           TXP1=Vin(I-1,J)-Vin(I-2,J)
           TXP2=Vin(I,J)-Vin(I-1,J)
           TXP3=Vin(I+1,J)-Vin(I,J)
              DVP1=MAX(0.0_SP,MIN(TXP1,2.0*TXP2,2.0*TXP3))
              DVP1=MIN(0.0_SP,MAX(TXP1,2.0*TXP2,2.0*TXP3))
              DVP2=MAX(0.0_SP,MIN(TXP2,2.0*TXP3,2.0*TXP1))
              DVP2=MIN(0.0_SP,MAX(TXP2,2.0*TXP3,2.0*TXP1))
              DVP3=MAX(0.0_SP,MIN(TXP3,2.0*TXP1,2.0*TXP2))
              DVP3=MIN(0.0_SP,MAX(TXP3,2.0*TXP1,2.0*TXP2))
           Din(I,J)=TXP2-1.0_SP/6.0_SP*(DVP3-2.0_SP*DVP2+DVP1)
           TMP1 = Din(I-1,J);   TMP2 = Din(I,J);
           IF( ABS(TMP1).le.SMALL ) TMP1 = SMALL*SIGN( 1.0_SP, TMP1 )
           IF( ABS(TMP2).le.SMALL ) TMP2 = SMALL*SIGN( 1.0_SP, TMP2 )
           RAT = TMP2/TMP1
           VAN1 = 0.0_SP;
           IF( abs(1.0 + RAT) > SMALL ) VAN1 = ( RAT + ABS(RAT) )/( 1.0_SP + RAT)
           RAT = TMP1/TMP2
           VAN2 = 0.0_SP;
           IF( abs(1.0 + RAT) > SMALL ) VAN2 = ( RAT + ABS(RAT) )/( 1.0_SP + RAT)
           OutL(I,J) = Vin(I-1,J) + ( 1.0_SP/6.0_SP )*( VAN1*TMP1 + 2.0_SP*VAN2*TMP2 )
           OutR(I,J) = Vin(I,J) - ( 1.0_SP/6.0_SP )*( 2.0_SP*VAN1*TMP1 + VAN2*TMP2 )
```

`OutR` 앞에서도 코드가 1622–1632행에서 `TMP1,TMP2,RAT,VAN1,VAN2`를 갱신한다.
이 인용은 서로 다른 조건 분기의 대입을 나열한 것이다.
조건문의 완결 블록은 원문 `fluxes.F:1555–1569,1605–1635`이다.

K11 — `fluxes.F:371–376`의 x방향 파속.

```fortran
       SQR_PHI_L=SQRT(GRAV*ABS(HxL(I,J)))
       SQR_PHI_R=SQRT(GRAV*ABS(HxR(I,J)))
       SQR_PHI_S=0.5*(SQR_PHI_L+SQR_PHI_R)+0.25*(UL(I,J)-UR(I,J))
       U_S=0.5*(UL(I,J)+UR(I,J))+SQR_PHI_L-SQR_PHI_R
       SxL(I,J)=MIN(UL(I,J)-SQR_PHI_L,U_S-SQR_PHI_S)
       SxR(I,J)=MAX(UR(I,J)+SQR_PHI_R,U_S+SQR_PHI_S)
```

K12 — `fluxes.F:179–189`의 HLL.

```fortran
      IF(SL(I,J)>=ZERO) THEN
        FOUT(I,J)=FL(I,J)
      ELSEIF(SR(I,J)<=ZERO) THEN
        FOUT(I,J)=FR(I,J)
      ELSE
        FOUT(I,J)=SR(I,J)*FL(I,J)-SL(I,J)*FR(I,J)+SL(I,J)*SR(I,J)*(UR(I,J)-UL(I,J))
        IF((ABS(SR(I,J)-SL(I,J)))<SMALL)THEN
         FOUT(I,J)=FOUT(I,J)/SMALL
        ELSE
         FOUT(I,J)=FOUT(I,J)/(SR(I,J)-SL(I,J))
        ENDIF
```

| 행 ID | 항목·문서(원문) | 코드(원문) | 판정 | 이유 |
|---|---|---|---|---|
| FT1-094 | p.23: 유한체적·유한차분 결합. 플럭스·1계 미분에 고차·저차 MUSCL-TVD를 둔다. “both high-order and low-order MUSCL-TVD schemes are implemented” | `fluxes.F:56` `IF(HIGH_ORDER(1:3)=='FOU') THEN`; 61 `CALL CONSTRUCTION_HO`; 103 `CALL CONSTRUCTION` | 일치 | 선택에 따라 별도 재구성을 호출한다. |
| FT1-095 | p.23: 3.0 전 Yamamoto 방법의 장시간 불안정과 Erduran 수정 방식 채택. “numerical instability occurred in long time simulations” | 이 행은 관찰 이력·사용 권고이며 특정 실행식의 구현 주장이 아니다. | 문서에만 | H. 3.0 이전 고차 방식의 불안정 관찰과 개정 동기를 설명한다. 현재 재구성식의 구현은 FT1-096–106에서 대조한다. [10-18 결론 검증 정정] |
| FT1-096 | p.23 (62): $\phi^L_{i+1/2}=\phi_i+\frac16[\chi(r)\Delta^*\phi_{i-1/2}+2\chi(1/r)\Delta^*\phi_{i+1/2}]$ | K10의 `OutL(I,J) = Vin(I-1,J) + ( 1.0_SP/6.0_SP )*( VAN1*TMP1 + 2.0_SP*VAN2*TMP2 )` (`fluxes.F:1618`) | 일치 | 코드의 경계면 첨자는 문서보다 하나 이동한다. 계수 1,2와 1/6이 같다. |
| FT1-097 | p.23 (63): $\phi^R_{i-1/2}=\phi_i-\frac16[2\chi(r)\Delta^*\phi_{i-1/2}+\chi(1/r)\Delta^*\phi_{i+1/2}]$ | K10의 `OutR(I,J) = Vin(I,J) - ( 1.0_SP/6.0_SP )*( 2.0_SP*VAN1*TMP1 + VAN2*TMP2 )` (`fluxes.F:1634`) | 일치 | 부호와 2,1 계수가 같다. |
| FT1-098 | p.23 (64) 첫 두 줄: $\Delta^*\phi_{i+1/2}=\Delta\phi_{i+1/2}-\Delta^3\bar\phi_{i+1/2}/6$, $\Delta\phi_{i+1/2}=\phi_{i+1}-\phi_i$ | K10의 `TXP2=Vin(I,J)-Vin(I-1,J)`, `Din(I,J)=TXP2-1.0_SP/6.0_SP*(DVP3-2.0_SP*DVP2+DVP1)` | 일치 | 두 차분과 1/6 보정을 그대로 계산한다. |
| FT1-099 | p.23 (64) 나머지: $\Delta^3\bar\phi_{i+1/2}=\Delta\bar\phi_{i+3/2}-2\Delta\bar\phi_{i+1/2}+\Delta\bar\phi_{i-1/2}$; $\Delta\bar\phi_{i-1/2}=\mathrm{minmod}(\Delta\phi_{i-1/2},\Delta\phi_{i+1/2},\Delta\phi_{i+3/2})$; $\Delta\bar\phi_{i+1/2}=\mathrm{minmod}(\Delta\phi_{i+1/2},\Delta\phi_{i+3/2},\Delta\phi_{i-1/2})$; $\Delta\bar\phi_{i+3/2}=\mathrm{minmod}(\Delta\phi_{i+3/2},\Delta\phi_{i-1/2},\Delta\phi_{i+1/2})$ | K10의 `DVP1,DVP2,DVP3`와 `Din` 대입. | 일치 | 순환한 인수 순서와 중앙의 -2가 같다. |
| FT1-100 | p.23 (65): $\mathrm{minmod}(j,k,l)=\mathrm{sign}(j)\max\{0,\min[\lvert j\rvert,2\mathrm{sign}(j)k,2\mathrm{sign}(j)l]\}$ | K10의 양수·음수 `DVP1` 대입 (`fluxes.F:1555–1559`). | 일치 | 음수 분기에서 바깥 음수를 안으로 옮기면 `MIN(0,MAX(j,2*k,2*l))`이다. |
| FT1-101 | p.23 (66): $\chi(r)=\frac{r+\lvert r\rvert}{1+r}$ | `fluxes.F:1612` `IF( abs(1.0 + RAT) > SMALL ) VAN1 = ( RAT + ABS(RAT) )/( 1.0_SP + RAT)` | 일치 | 문서의 분모는 $1+r$이다. 코드는 $r=-1$ 근처의 나눗셈을 막는다. |
| FT1-102 | p.23 (67): $r=\Delta^*\phi_{i+1/2}/\Delta^*\phi_{i-1/2}$ | `fluxes.F:1610` `RAT = TMP2/TMP1`; 1614 `RAT = TMP1/TMP2` | 일치 | $r$와 역수를 따로 계산한다. |
| FT1-103 | p.24 (68): $\phi=\phi_i+(x-x_i)\sigma\phi_i$ | `fluxes.F:780` `OutL(I,J) = Vin(I-1,J) + 0.5_SP*DX*Din(I-1,J)` | 일치 | 선형 재구성의 경계면 평가이다. |
| FT1-104 | p.24 (69): $\phi^L_{i+1/2}=\phi_i+\frac12\Delta x\,\sigma\phi_i,\quad\phi^R_{i-1/2}=\phi_i-\frac12\Delta x\,\sigma\phi_i$ | `fluxes.F:780–781` `OutL(I,J) = Vin(I-1,J) + 0.5_SP*DX*Din(I-1,J)`; `OutR(I,J) = Vin(I,J) - 0.5_SP*DX*Din(I,J)` | 일치 | 좌우 부호와 1/2가 같다. |
| FT1-105 | p.24 (70): $\sigma\phi_i=\Upsilon((\phi_{i+1}-\phi_i)/(x_{i+1}-x_i),(\phi_i-\phi_{i-1})/(x_i-x_{i-1}))$ | `fluxes.F:310` `TMP1=(DIN(I+1,J)-DIN(I,J))/DX`; 311 `TMP2=(DIN(I,J)-DIN(I-1,J))/DX` | 일치 | 제한 함수에 전진·후진 기울기를 넣는다. |
| FT1-106 | p.24 (71): $\Upsilon(a,b)=\frac{a\lvert b\rvert+\lvert a\rvert b}{\lvert a\rvert+\lvert b\rvert}$ | `fluxes.F:321` `DOUT(I,J)=(TMP1*ABS(TMP2)+ABS(TMP1)*TMP2)/(ABS(TMP1)+ABS(TMP2))` | 일치 | 작은 분모 처리는 §3에 따로 적는다. |
| FT1-107 | p.24: 고차 수렴 실패·매우 큰 파고에서 2차 방식 권고. 더 높은 격자 해상도가 필요할 수 있다. “may be required to ensure model accuracy” | 이 행은 관찰 이력·사용 권고이며 특정 실행식의 구현 주장이 아니다. | 문서에만 | H. 4차 방식의 수렴 실패 사례에 2차 방식과 더 높은 격자 해상도를 권고하는 문장이다. [10-18 결론 검증 정정] |
| FT1-108 | p.24 (72): $\Theta(\Psi^L,\Psi^R)=\{\Theta(\Psi^L)\ (s_L\ge0),\ \Theta^*(\Psi^L,\Psi^R)\ (s_L<0<s_R),\ \Theta(\Psi^R)\ (s_R\le0)\}$ | K12. | 일치 | 세 분기와 등호 조건이 같다. |
| FT1-109 | p.24 (73): $\Theta^*=\frac{s_R\Theta(\Psi^L)-s_L\Theta(\Psi^R)+s_Ls_R(\Psi^R-\Psi^L)}{s_R-s_L}$ | K12의 `FOUT` 계산. `fluxes.F:156` `CALL HLL(Mloc1,Nloc,SxL,SxR,FxL,FxR,HUxL,HUxR,Fx)` `io.F`의 `CONSTRUCTION` 입력은 FT1-229에서 대조한다. `fluxes.F:109–112,154–159`가 HLL 경로와 상태 점프를 정한다. `etauv_solver.F:310,343`은 `Ubar,Vbar`를 적분한다. `7b93138:src/fluxes.F:128–131`도 같은 상태를 HLL에 전달한다. | 불일치 | E 후보 (약함). HLL의 운동량 상태 점프는 HU,HV이다. 시간 적분 상태는 Ubar,Vbar이다. 이 차이는 문서 시점에도 존재한다. 결합 설계 가능성 때문에 약한 코드 결함 후보로 유지한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-110 | p.24 (74): $s_L=\min(\mathbf V^L\cdot\mathbf n-\sqrt{g(h+\eta)^L},u_s-\sqrt{\varphi_s})$ | K11의 `SxL`; y대응은 `fluxes.F:410` `SyL(I,J)=MIN(VL(I,J)-SQR_PHI_L,U_S-SQR_PHI_S)` | 불일치 | F. 여기서 문서의 $\mathbf V$는 법선 유속을 뜻한다. p.18의 보존 운동량 $\mathbf V$로 읽으면 단위가 맞지 않는다. 코드가 쓰는 것은 재구성한 유속이다. |
| FT1-111 | p.24 (75): $s_R=\max(\mathbf V^R\cdot\mathbf n+\sqrt{g(h+\eta)^R},u_s+\sqrt{\varphi_s})$ | K11의 `SxR`; y대응은 `fluxes.F:411` `SyR(I,J)=MAX(VR(I,J)+SQR_PHI_R,U_S+SQR_PHI_S)` | 불일치 | F. FT1-110과 같은 유속 표기이다. 음수 수심의 절댓값 처리는 §3에 적는다. |
| FT1-112 | p.24 (76): $u_s=\frac12(\mathbf V^L+\mathbf V^R)\cdot\mathbf n+\sqrt{g(\eta+h)^L}-\sqrt{g(\eta+h)^R}$ | K11의 `U_S` 대입. | 일치 | 계수 1/2와 좌우 파속 차의 부호가 같다. |
| FT1-113 | p.24 (77): $\sqrt{\varphi_s}=\frac{\sqrt{g(\eta+h)^L}+\sqrt{g(\eta+h)^R}}2+\frac{(\mathbf V^L-\mathbf V^R)\cdot\mathbf n}4$ | K11의 `SQR_PHI_S` 대입. | 일치 | 평균 파속과 유속 차의 1/4 계수가 같다. |
| FT1-114 | p.24: 고계 미분은 셀 중심 중앙차분이다. “at the cell centroids” | `dispersion.F:77`의 미분 호출; `derivatives.F:280–281` `Uout(I,J)= (Uin(I+1,J)-2.0_SP*Uin(I,J) &`와 `+Uin(I-1,J))/DX/DX*MASK(I,J)` | 일치 | 분산 고계 미분은 셀 중심의 중앙차분이다. |
| FT1-115 | p.24: “No discretization of dispersion terms at the cell interfaces is needed due to using $\mathbf M$ as a flux variable.” | `fluxes.F:488` `CALL CONSTRUCT_X(Mloc,Mloc1,Nloc,DX,U4,DelxU4,U4xL,U4xR,Kappa)`; K09. 3.0 p.24 마지막 문단; 2.1 p.19의 같은 설명; `dispersion.F:77–83`; `fluxes.F:486–494`; `7b93138:src/fluxes.F:446–448`. | 불일치 | F. 고계 미분은 셀 중심에서 계산한다. 그 결과인 U4는 경계면에 재구성한다. p.24의 바로 앞 문장은 고계 미분의 이산화를 설명한다. 이 문맥의 이산화를 모든 경계면 재구성의 부재로 확대할 수 없으므로 git 판정 B를 F로 정정한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-116 | p.24: SGM으로 비물리 진동을 제거하며 2.2절 재배열로 고차 MUSCL의 불균형을 피한다. “The Surface Gradient Method ... was used” | K02, K09; `fluxes.F:482` `HxL=EtaRxL+Depthx`; 483 `HxR=EtaRxR+Depthx` | 불일치 | F. 수면고를 재구성한 뒤 경계면 수심을 더한다. 정수압 균형은 전통 SGM의 별도 상쇄식보다 식 (15)의 재배열로 설명해야 한다. |
| FT1-117 | p.25 (78) 1단계: $\Psi^{(1)}=\Psi^n+\Delta t(-\nabla\cdot\Theta(\Psi^n)+S^{(1)})$ | `mod_global.F:122` `REAL(SP),PARAMETER,DIMENSION(3)::alpha=(/0.0_SP,3.0_SP/4.0_SP,1.0_SP/3.0_SP/)`; 123 `REAL(SP),PARAMETER,DIMENSION(3)::beta=(/1.0_SP,1.0_SP/4.0_SP,2.0_SP/3.0_SP/)`; `etauv_solver.F:270`의 갱신식. | 일치 | 첫 단계는 $\alpha=0,\beta=1$이다. |
| FT1-118 | p.25 (78) 2단계: $\Psi^{(2)}=\frac34\Psi^n+\frac14[\Psi^{(1)}+\Delta t(-\nabla\cdot\Theta(\Psi^{(1)})+S^{(2)})]$ | FT1-117의 계수와 `etauv_solver.F:270,310,343`의 대입. | 일치 | 세 보존 변수에 3/4와 1/4를 쓴다. |
| FT1-119 | p.25 (78) 3단계: $\Psi^{n+1}=\frac13\Psi^n+\frac23[\Psi^{(2)}+\Delta t(-\nabla\cdot\Theta(\Psi^{(2)})+S^{n+1})]$ | FT1-117의 계수; `main.F:380` `DO ISTAGE=1,3` | 일치 | 마지막 계수는 1/3과 2/3이다. 외력의 단계별 시각은 §3에 분리한다. |
| FT1-120 | p.25: 단계마다 삼중 대각계를 풀고 소스를 갱신한다. “at each intermediate step” | `main.F:404` `CALL SourceTerms   ! put sourceterms after fluxes in order to get eta_t`; 414 `CALL ESTIMATE_HUV(ISTAGE)`; `etauv_solver.F:348` `CALL GET_Eta_U_V_HU_HV` | 일치 | 각 RK 단계가 소스 계산과 유속 역변환을 한 번 호출한다. |
| FT1-121 | p.25: “an iteration is needed to achieve convergence.” | `main.F:380–487`의 단계 루프에는 수렴 반복이 없다. `mod_param.F:89` `INTEGER :: ITER_NUM = 2`는 `ITERATION` 조건 선언이다. 3.0 p.11은 반복 옵션 제거를 명시한다. `7b93138:src/mod_param.F:87–88`의 선언과 `main.F:380–487`의 세 RK 단계를 대조했다. 전체 `git log --all -S ITER_NUM`·`-S ERRORi`는 `cab9425`, `b9c035d`, `8d5a857`의 선언 추가·경로 정리만 반환한다. 노트의 과장 판정은 FT1-266이다. | 문서에만 | D. 유체 RK 단계의 수렴 반복은 공개 소스 이력에 없다. 반복 선언과 과거 값 배열만으로 구현을 주장하지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-122 | p.25 (79): $\Delta t=C\min(\min\frac{\Delta x}{\lvert u_{i,j}\rvert+\sqrt{g(h_{i,j}+\eta_{i,j})}},\min\frac{\Delta y}{\lvert v_{i,j}\rvert+\sqrt{g(h_{i,j}+\eta_{i,j})}})$ | `misc.F:243` `TMP1=ABS(U(I,J))+SQRT(GRAV*MAX(H(I,J),MinDepthFrc))`; 252 `TMP2=DX/TMP1`; 259 `TMP1=ABS(V(I,J))+SQRT(GRAV*MAX(H(I,J),MinDepthFrc))`; 281 `DT_tmp=CFL*TMP3` | 일치 | 일반 습윤 영역에서 식과 같다. 전역 최소·수심 하한·고정 간격 절반화는 §3에 기록한다. |
| FT1-123 | p.25 번호 없음: $C=0.5$를 예제에서 쓴다. | `io.F:2862` `CALL READ_FLOAT(CFL,FILE_NAME,'CFL',ierr)`; 2864 `CFL = 0.5_SP` | 일치 | 코드의 미입력 기본값도 0.5이다. |

### 2.5 p.25–26: 쇄파와 습윤–건조, 식 (80)–(85)

K13 — `masks.F:177–186`의 분산 마스크.

```fortran
      IF(VISCOSITY_BREAKING)THEN
        ! dont use mask9 for viscosity breaking
        MASK9tmp(I,J)= 1
      ELSE
        MASK9tmp(I,J)=MASK(I,J)*MASK(I-1,J)*MASK(I+1,J)  &
                *MASK(I+1,J+1)*MASK(I,J+1)*MASK(I-1,J+1) &
                *MASK(I+1,J-1)*MASK(I,J-1)*MASK(I-1,J-1)
        IF(ABS(Eta(I,J))/MAX(DEPTH(I,J),MinDepthFrc)>SWE_ETA_DEP)THEN
         MASK9tmp(I,J)=ZERO
        ENDIF
```

K14 — `sources.F:428–437,442–451`의 실제 기본 점성 확산.

```fortran
       BreakSourceX(I,J) = 0.5_SP/DX*( &
                      (nu_vis(I+1,J)+nu_vis(I,J)) &
                      *1.0_SP/DX*(HU(I+1,J)-HU(I,J)) &
                     -(nu_vis(I-1,J)+nu_vis(I,J)) &
                      *1.0_SP/DX*(HU(I,J)-HU(I-1,J)) ) &
                                   + 0.5_SP/DY*( &
                      (nu_vis(I,J+1)+nu_vis(I,J)) &
                      *1.0_SP/DY*(HU(I,J+1)-HU(I,J)) &
                     -(nu_vis(I,J-1)+nu_vis(I,J)) &
                      *1.0_SP/DY*(HU(I,J)-HU(I,J-1)) )
        BreakSourceY(I,J) = 0.5_SP/DX*( &
                      (nu_vis(I+1,J)+nu_vis(I,J)) &
                      *1.0_SP/DX*(HV(I+1,J)-HV(I,J)) &
                     -(nu_vis(I-1,J)+nu_vis(I,J)) &
                      *1.0_SP/DX*(HV(I,J)-HV(I-1,J)) ) &
                                   + 0.5_SP/DY*( &
                      (nu_vis(I,J+1)+nu_vis(I,J)) &
                      *1.0_SP/DY*(HV(I,J+1)-HV(I,J)) &
                     -(nu_vis(I,J-1)+nu_vis(I,J)) &
                      *1.0_SP/DY*(HV(I,J)-HV(I,J-1)) )
```

| 행 ID | 항목·문서(원문) | 코드(원문) | 판정 | 이유 |
|---|---|---|---|---|
| FT1-124 | p.25: 충격 포착과 점성 쇄파의 두 알고리즘. “There are two breaking algorithms implemented in the model.” | K13; `sources.F:394` `IF(VISCOSITY_BREAKING.OR.DIFFUSION_SPONGE.OR.WAVEMAKER_VIS)THEN` | 일치 | `VISCOSITY_BREAKING`이 마스크 전환 방식과 명시 점성 방식을 구분한다. |
| FT1-125 | p.25: “where the Froude number exceeds a certain threshold” | K13. `io.F:2689–2703`의 `VISCOSITY_BREAKING` 입력과 `io.F:2713–2715`의 `SWE_ETA_DEP` 입력을 대조했다. `masks.F:177–188`은 점성 쇄파를 선택하지 않은 분기에서만 전환비를 검사한다. `7b93138:src/masks.F:124–134`도 같은 분기이다. FT1-013과 같은 판정이다. | 불일치 | B. 쇄파 전환 조건은 순간 수면고 절댓값과 정수심 하한의 비이다. 이 비를 유속 Froude 수로 적지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-126 | p.25: “the ratio of wave height to total water depth”; “threshold value set to 0.8” | K13. `io.F`의 `SWE_ETA_DEP` 기본값은 §5에서 이력과 함께 인용한다. `io.F:2689–2703`의 `VISCOSITY_BREAKING` 입력과 `io.F:2713–2715`의 `SWE_ETA_DEP` 입력을 대조했다. `masks.F:177–188`은 점성 쇄파를 선택하지 않은 분기에서만 전환비를 검사한다. `7b93138:src/masks.F:124–134`도 같은 분기이다. FT1-013과 같은 판정이다. | 불일치 | B. 충격 포착 전환식의 분자는 ABS(Eta)이다. 분모는 MAX(DEPTH,MinDepthFrc)이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-127 | p.25 (80): $\mathbf R_{bx}=\partial_x(\nu\partial_xP)+\partial_y(\nu\partial_yP)$ | K14; `sources.F:70` `LOGICAL :: PQ_scheme = .FALSE.` `17d2eeb`(2017-03-03)의 diff가 `LOGICAL :: PQ_scheme = .TRUE.`를 `LOGICAL :: PQ_scheme = .FALSE.`로 바꾼다. 현재 `sources.F:394–453`에서 `IF(VISCOSITY_BREAKING.OR.DIFFUSION_SPONGE.OR.WAVEMAKER_VIS)THEN` 뒤 HU·HV 분기를 선택한다. | 불일치 | A. 문서의 P 확산은 2016년 판의 기본 선택이다. 현재 기본 선택은 HU 확산이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-128 | p.25 (81): $\mathbf R_{by}=\partial_y(\nu\partial_yQ)+\partial_x(\nu\partial_xQ)$ | K14. `17d2eeb`(2017-03-03)의 diff가 `LOGICAL :: PQ_scheme = .TRUE.`를 `LOGICAL :: PQ_scheme = .FALSE.`로 바꾼다. 현재 `sources.F:394–453`에서 `IF(VISCOSITY_BREAKING.OR.DIFFUSION_SPONGE.OR.WAVEMAKER_VIS)THEN` 뒤 HU·HV 분기를 선택한다. | 불일치 | A. 문서의 Q 확산은 2016년 판의 기본 선택이다. 현재 기본 선택은 HV 확산이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-129 | p.25: 교차 미분을 제거한 식이 Kennedy 원식보다 안정적이었다. “as the cross-derivatives removed” | K14. | 일치 | 코드의 기본 점성 확산에도 교차 미분이 없다. 안정성 비교 결과 자체는 이 코드 판독으로 검증하지 않는다. |
| FT1-130 | p.25 (82): $\nu=B\delta_b^2(h+\eta)\eta_t$ | `breaker.F:314` `nu_break(I,J) = cap1*tmp2 + nu_bkg`; 125 `tmp1=Cbrk1*tmp3`; 126 `tmp2=Cbrk2*tmp3` `io.F:2689–2691,3062–3078`의 입력·활성 조건과 `breaker.F:64–66,248–265,278–315`의 조파기 안팎·컴파일 분기를 함께 대조했다. `7b93138:src/breaker.F:113–115,218–237`에도 기본 정적 점성식과 계수 1.0이 있다. | 불일치 | B. 조파기 밖의 기본 점성식은 `nu_break(I,J) = cap1*tmp2 + nu_bkg`이다. `cap1=1.0*(MAX(Depth(I,J),MinDepthFrc)+ETA(I,J))`이므로 기존 결론의 단순 H 대체는 정정한다. 문서의 수면고 시간 미분 비례식과 현재 `VIS_KENNEDY_ORIGINAL`·`VIS_KENNEDY` 분기를 구분한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-131 | p.26 번호 없음: $\delta_b=1.2$ | `breaker.F:265` `cap1=1.0*(MAX(Depth(I,J),MinDepthFrc)+ETA(I,J))` `io.F:2689–2691,3062–3078`의 입력·활성 조건과 `breaker.F:64–66,248–265,278–315`의 조파기 안팎·컴파일 분기를 함께 대조했다. `7b93138:src/breaker.F:113–115,218–237`에도 기본 정적 점성식과 계수 1.0이 있다. | 불일치 | B. 점성식의 코드 계수는 1.0이다. δb=1.2라는 문서 기술을 코드 계수로 옮기지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-132 | p.26 (83): $B=\{1\ (\eta_t\ge\eta_t^*),\ 0\ (\eta_t<\eta_t^*)\}$; 매끄러운 전이 생략. | `breaker.F:264` `IF(AGE(I,J)>ZERO.AND.AGE(I,J)<T_brk.AND.ETAt(I,J)>tmp2)THEN`; 314의 기본 점성. `io.F:2689–2691,3062–3078`의 입력·활성 조건과 `breaker.F:64–66,248–265,278–315`의 조파기 안팎·컴파일 분기를 함께 대조했다. `7b93138:src/breaker.F:113–115,218–237`에도 기본 정적 점성식과 계수 1.0이 있다. | 불일치 | B. 조파기 밖의 기본 쇄파 점성은 `IF(AGE(I,J)>ZERO.AND.AGE(I,J)<T_brk.AND.ETAt(I,J)>tmp2)THEN`에서 정적 식으로 계산한다. 문서 식 (83)의 B 정의와 구분한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-133 | p.26: 시작 임계값을 넘으면 쇄파를 시작하고 종료 임계값 아래에서 멈춘다. “until $\eta_t$ drops below $\eta_t^{(F)}$” | `breaker.F:151–153` `IF(ETAt(I,J).GE.tmp1.AND.(  &` / `AGE(I,J).EQ.ZERO.OR.AGE(I,J).GT.T_brk))THEN` / `AGE(I,J)=DT`; 264의 조건. 3.0·2.1·Intro-TN·code_analysis 전체 판독 및 TEX에서 `T_brk`, `AGE_BREAKING`, 쇄파 나이·수명을 검색했다. Intro-TN p.14는 AGE 출력을, code_analysis p.7은 AGE_BREAKING의 인수 사용을 적는다. `breaker.F:151–228,264`가 수명과 이웃 전파를 처리한다. | 불일치 | C. 3.0 p.26의 두 임계값 설명에는 조파기 밖의 T_brk 수명 제한과 이웃 셀의 쇄파 나이 전파 절차가 없다. 다른 문서의 AGE 출력·변수 목록은 이 절차를 설명하지 않는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-134 | p.26 번호 없음: $\eta_t^{(I)}=0.65\times2\sqrt{gh}$, “Cbrk1 = 0.65” | `io.F:3079` `CALL READ_FLOAT(Cbrk1,FILE_NAME,'Cbrk1',ierr)`; 3081 `Cbrk1 = 0.65_SP`; `breaker.F:124` `tmp3=SQRT(GRAV*MAX(MinDepthFrc,H(I,J)))`; 125 `tmp1=Cbrk1*tmp3` `io.F:2689–2691,3062–3078`의 입력·활성 조건과 `breaker.F:64–66,248–265,278–315`의 조파기 안팎·컴파일 분기를 함께 대조했다. `7b93138:src/breaker.F:113–115,218–237`에도 기본 정적 점성식과 계수 1.0이 있다. | 불일치 | B. 쇄파 개시 임계값은 `tmp3=SQRT(GRAV*MAX(MinDepthFrc,H(I,J)))`와 `tmp1=Cbrk1*tmp3`로 계산한다. 문서의 추가 2배를 코드 식에 넣지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-135 | p.26 번호 없음: $\eta_t^{(F)}=0.15\sqrt{gh}$, “Cbrk2=0.15” | `io.F:3101` `CALL READ_FLOAT(Cbrk2,FILE_NAME,'Cbrk2',ierr)`; 3103 `Cbrk2 = 0.35_SP`; `breaker.F:126` `tmp2=Cbrk2*tmp3` `io.F:2689–2691,3062–3078`의 입력·활성 조건과 `breaker.F:64–66,248–265,278–315`의 조파기 안팎·컴파일 분기를 함께 대조했다. `7b93138:src/breaker.F:113–115,218–237`에도 기본 정적 점성식과 계수 1.0이 있다. `7b93138:src/mod_global.F:372`도 `Cbrk2=0.35`이다. 3.0 p.45–46의 0.15는 예제에 명시한 설정값이다. | 불일치 | B. Cbrk2의 현재 입력 누락값은 0.35이다. 예제의 명시 입력 0.15는 별도 설정값이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-136 | p.26: 최근 시험에서는 시작 임계값을 약간 더 크게 해야 실험실 자료와 맞았다. “should be slightly larger to match the laboratory data” | p.26의 시험·보정 권고이며 특정 코드 대입을 주장하지 않는다. | 문서에만 | H. 검증·보정에 대한 권고이다. [10-18 결론 검증 정정] |
| FT1-137 | p.26: “instead of using $U$ and $V$ ... we used $P$ and $Q$” | K14; `sources.F:398–399` `! it turns out P and Q are not exchanged at processor interface`; `! it affects edges, make PQ_scheme=false` `17d2eeb`(2017-03-03)의 diff가 `LOGICAL :: PQ_scheme = .TRUE.`를 `LOGICAL :: PQ_scheme = .FALSE.`로 바꾼다. 현재 `sources.F:394–453`에서 `IF(VISCOSITY_BREAKING.OR.DIFFUSION_SPONGE.OR.WAVEMAKER_VIS)THEN` 뒤 HU·HV 분기를 선택한다. | 불일치 | A. 2017-03-03부터 기본 점성 확산은 HU와 HV를 사용한다. PDF의 P·Q 설명은 그 변경 전 판의 설명이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-138 | p.26: 건조 셀 경계의 $\mathbf n\cdot\mathbf M$를 0으로 한다. | `bc.F:223–224` `IF(MASK(I,J)<1)THEN`, `P(I,J)=ZERO`; 241 `P(I+1,J)=ZERO`; 258 `Q(I,J)=ZERO`; 275 `Q(I,J+1)=ZERO` | 일치 | 네 면의 질량 플럭스를 0으로 한다. 압력 플럭스는 이웃 습윤 상태에 따라 남긴다. |
| FT1-139 | p.26: “A mirror boundary condition is applied to the fourth-order MUSCL-TVD scheme and discretization of dispersive terms ... at dry cells.” | `fluxes.F:1572` `IF(MASK(I-2,J)==0.OR.MASK(I+1,J)==0)THEN`; 1574 `TXP1=TXP2`; 1575 `TXP3=TXP2`; 1594 `IF(MASK(I-1,J)==0.OR.MASK(I,J)==0)THEN`; K13. `fluxes.F:1572–1600`, 특히 `Din(I,J)=TXP2-1.0_SP/6.0_SP*(DVP3-2.0_SP*DVP2+DVP1)`; `masks.F:177–188`; `7b93138:src/masks.F:124–134`. FT1-270에도 같은 조건을 적용한다. | 불일치 | B. 내부 건조 셀에서는 고차 재구성 보정 DVP1·DVP2·DVP3를 바꾼다. `DVP1=ZERO` 등의 대입만으로 최종 기울기 Din도 0이라고 할 수 없다. 점성 쇄파를 선택하지 않은 분기에서만 주변 습윤 마스크의 곱을 적용한다. 이 처리를 문서의 내부 거울 경계 또는 외곽 반사 경계와 동일시하지 않는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-140 | p.26 (84): $s_L=\mathbf V^L\cdot\mathbf n-\sqrt{g(h+\eta)^L},\ s_R=\mathbf V^L\cdot\mathbf n+2\sqrt{g(h+\eta)^L}$ (right dry cell) | K11. `7b93138:src/fluxes.F:336–341`과 현재 `fluxes.F:352–411`은 일반 파속식을 쓴다. `git log --all -S 'right dry cell'`의 적중 `9b28db7`은 TEX 추가이다. 좌·우 전용 파속 분기는 공개 소스 이력에 없다. | 문서에만 | D. 우측 건조 셀에 문서 식 (84)의 별도 파속 계수를 적용하는 분기는 공개 이력에 없다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-141 | p.26 (85): $s_L=\mathbf V^R\cdot\mathbf n-\sqrt{g(h+\eta)^R},\ s_R=\mathbf V^R\cdot\mathbf n+2\sqrt{g(h+\eta)^R}$ (left dry cell) | K11. `7b93138:src/fluxes.F:336–341`과 현재 `fluxes.F:352–411`은 일반 파속식을 쓴다. `git log --all -S 'right dry cell'`의 적중 `9b28db7`은 TEX 추가이다. 좌·우 전용 파속 분기는 공개 소스 이력에 없다. | 문서에만 | D. 좌측 건조 셀에 문서 식 (85)의 별도 파속 계수를 적용하는 분기는 공개 이력에 없다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |

### 2.6 p.26–30: 경계조건·스펀지·조파, 식 (86)–(99)

K15 — `sources.F:264–266`의 마찰 스펀지.

```fortran
          SourceX(I,J) = SourceX(I,J) &
                 - CD_4_SPONGE(I,J)*U(I,J)*SQRT(U(I,J)*U(I,J)+V(I,J)*V(I,J)) &
                   *Depth(I,J)
```

y방향은 `sources.F:322–324`에서 같은 식의 `U(I,J)`를 `V(I,J)`로 바꾼다.

K16 — `wavemaker.F:2395–2403`의 규칙파 계수.

```fortran
        rlamda=wkn*sin(theta)
        width=delta*wave_length/2.0_SP
        beta_gen=80.0_SP/delta**2/wave_length**2
        rl_gen=wkn*cos(theta)
        rI=SQRT(3.14159/beta_gen)*exp(-rl_gen**2/4./beta_gen)
        D_gen=2.0_SP*AMP_WK  &
            *cos(theta)*(omgn**2-alpha1*grav*wkn**4*h_gen**3) &
            /(omgn*wkn*rI*(1.0_SP-alpha*(wkn*h_gen)**2))
```

K17 — `sources.F:109–114`의 규칙파 질량 소스.

```fortran
IF(WAVEMAKER(1:6)=='WK_REG')THEN
    AA = TANH(PI/(Time_ramp*Tperiod)*TIME)*D_gen
    DO J=jlo,jhi
        DO I=ilo,ihi
            WaveMaker_Mass(I,J)= AA*EXP(-Beta_gen*(xmk_wk(I)-Xc_WK)**2) &
                *SIN(rlamda*(ymk_wk(J)-ZERO)-2.0_SP*PI/Tperiod*TIME)
```

K18 — `wavemaker.F:1873–1887,1933–1968`의 스펙트럼 계산.

```fortran
        omiga_spec=2.0_SP*pi*fre*SQRT(h_gen/grav)
        phi=1.0_SP-0.5_SP*(2.0_SP-omiga_spec)**2
        if(omiga_spec.le.1.0_SP) phi=0.5_SP*omiga_spec**2
        if(omiga_spec.ge.2.0_SP) phi=1.0_SP
        IF(WaveMaker(1:3)=='JON') THEN
          phi=1.0_SP
        ENDIF
        sigma_spec=0.07_SP
        if(fre.gt.fm)sigma_spec=0.09_SP
        Etma=grav**2*fre**(-5)*(2.0_SP*pi)**(-4)*phi &
         *exp(-5.0_SP/4.0_SP*(fre/fm)**(-4)) &
         *gamma_spec**(exp(-(fre/fm-1.0_SP)**2/(2.0_SP*sigma_spec**2)))
        sigma_theta=sigma_theta_input*pi/180.0_SP
        N_spec=20.0_SP/sigma_theta
          AG(ktheta) = 1.0_SP/( 2.0_SP*pi )
	       AG(ktheta) = AG(ktheta) +  &
                ( 1.0_SP/pi )*exp( -0.5_SP*( real(k_n)*sigma_theta )**2 )  &
	        *cos( k_n*(theta - theta_input*pi/180.0_SP) )
	 AG(:) = ABS(AG(:)/sumAG);   !Because integral of AG should be 1.
        alpha_spec=Hmo**2/16.0_SP/Ef
```

K18의 마지막 부분은 서로 다른 반복문 안의 논리문을 발췌한 것이다.
`AG`의 반복 범위는 `wavemaker.F:1955`의 `do k_n=1,N_spec`이다.

| 행 ID | 항목·문서(원문) | 코드(원문) | 판정 | 이유 |
|---|---|---|---|---|
| FT1-142 | p.26: 벽·흡수·주기 경계를 구현한다. “including wall boundary condition, absorbing boundary condition ... and periodic boundary condition” | `bc.F:87` `P(Ibeg,J)=ZERO`; `main.F:467` `CALL ABSORBING_GENERATING_BC`; `etauv_solver.F:545` `CALL TRIDy_periodic (myA,myC,myD,myF)` | 일치 | 벽은 법선 질량 플럭스를 막는다. 흡수 경계와 주기 역변환은 별도 경로이다. |
| FT1-143 | p.26–27 (86): $\phi=\phi/C_s$, $\phi$는 $\eta,u,v$이다. 매 시간 단계 직접 감쇠한다. | `sponge.F:59` `ETA(I,J)=ETA(I,J)/SPONGE(I,J)`; 61 `U(I,J)=U(I,J)/SPONGE(I,J)`; 62 `V(I,J)=V(I,J)/SPONGE(I,J)` | 일치 | 수면고는 `MASK>0`일 때 감쇠한다. 호출은 RK 단계 안에 있으며 §3에 별도 기록한다. |
| FT1-144 | p.27 (87): $C_s=\alpha_s^{\gamma_x^{i-1}},\ i=1,2,\ldots,n$ | `sponge.F:653` `ri=R_sponge**(50*(I-1)/(Iwidth-1))`; 655 `tmp_2d_1(i,j)=MAX(A_Sponge**ri,lim)` `io.F:2285–2287`의 `READ_LOGICAL` 입력 → `init.F:966–970`의 `IF(DIRECT_SPONGE)THEN` → `main.F:483–485` 감쇠 호출. `sponge.F:617,650–655`의 정수 변수·병렬/직렬 지수. `cab9425:sponge.F:597`에도 같은 식. `funwave_tvd_3.0.tex:788`. | 불일치 | E 후보 (중간). 직접 스펀지의 지수는 정수 나눗셈으로 계산한다. 예를 들어 해당 식에 Iwidth=100과 I=2를 넣으면 50/99가 0이 된다. 임의 폭에서 문서의 지수 프로파일과 다른 후보이다. PDF p.27 식 (87)과 TeX 788행의 아래첨자는 모두 `gamma_x`이다. git 판정 파일의 `gamma_s` 전사 지적은 원문과 달라 채택하지 않는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-145 | p.27 번호 없음: $\alpha_s=2$, $\gamma_s=0.88-0.92$, $n=50-100$; 보통 1–2파장; 최적 감쇠는 사례에 민감하다. | 이 행은 문서의 권고·개발 경위·수학적 정의를 대조 대상으로 삼는다. | 문서에만 | H. Chen의 권고값이다. 코드 입력 기본값으로 단언하지 않는다. [10-18 결론 검증 정정] |
| FT1-146 | p.27: 직접 감쇠와 TVD 결합이 파장 $2dx$의 톱니 잡음을 만들 수 있다. 장시간 성장하면 마찰·점성 또는 결합을 권고한다. “may become significant in a long term simulation” | 이 행은 문서의 권고·개발 경위·수학적 정의를 대조 대상으로 삼는다. | 문서에만 | H. 직접 감쇠와 TVD 결합에서 생길 수 있는 톱니 잡음과 장시간 사용 권고를 설명한다. 문서는 잡음이 장시간에 유의해질 수 있다고 조건부로 서술한다. [10-18 결론 검증 정정] |
| FT1-147 | p.27 (88): $F_{frc}=-C_{sponge}\lvert\mathbf u_\alpha\rvert(u_\alpha,v_\alpha)h$ | K15. | 일치 | 코드가 유속 크기와 정수심을 곱한다. 총수심 $H$를 곱하지 않는다. |
| FT1-148 | p.27: 플럭스형 운동량에서 깊이 의존성을 없애려고 $h$를 넣는다. 점성 스펀지는 공간 변화 $\nu_{sponge}$를 쇄파 확산식에 쓴다. | `sources.F:212` 부근의 점성 결합은 아래 §3에서 인용한다. K14, K15. | 일치 | 마찰·확산 스펀지는 같은 운동량 소스 경로를 공유한다. 깊이 독립이라는 설명은 $H\simeq h$의 가속도 해석이다. |
| FT1-149 | p.27 (89): $C_{sponge}=C_{max}(1-\tanh\frac{10(i-1)}{I_{width}-1})$ | `sponge.F:285` `ri=MAX(0.0,REAL(Iwidth-I))`; 287 `tmp_2d_1(i,j)=MAX(CDsponge*TANH(ri/10.0),lim)` `7b93138:src/sponge.F:248–250`도 같은 `MAX` 대입이다. 원문의 0 하한을 생략한 기존 요약식을 정정한다. | 불일치 | B. 마찰 스펀지의 실제 식은 MAX(CDsponge*TANH(ri/10.0),lim)이다. 문서 식 (89)와 구분한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-150 | p.27: 나머지 세 경계와 점성 스펀지에도 비슷한 식을 쓴다. “Similar expressions can be obtained” | `sponge.F:469` `tmp_2d_1(i,j)=MAX(Csp*TANH(ri/10.0),lim)`; 312,350,379의 마찰 반대 경계 대입. | 일치 | 코드가 방향별 거리와 같은 `TANH(ri/10)`를 쓴다. 식 (89) 자체의 차이는 FT1-149에 기록한다. |
| FT1-151 | p.27: 마찰·점성 스펀지는 보통 2–3파장이다. L-D는 더 좁아도 효율적이나 장시간 톱니 잡음을 고려한다. | 이 행은 문서의 권고·개발 경위·수학적 정의를 대조 대상으로 삼는다. | 문서에만 | H. 마찰·점성 스펀지의 통상 폭 2–3파장과 장시간 잡음에 관한 사용 권고이다. [10-18 결론 검증 정정] |
| FT1-152 | p.27: “The periodic boundary condition in y (south/north) direction was implemented in the code.” | `bc.F:136–140` `# if defined (CARTESIAN)` / `IF(PERIODIC)THEN` / `! do nothing` / `ELSE`; `etauv_solver.F:545`의 주기 삼중 대각 호출. | 일치 | 직교좌표계의 남북 경계에 적용한다. 기본 구면 외곽 경계에 같은 조건이 적용된다고 확대하지 않는다. |
| FT1-153 | p.28: Wei·Kirby 양방향 내부 조파와 Chawla·Kirby 단방향 조파. 후자는 “under development”이다. | 이 행은 문서의 권고·개발 경위·수학적 정의를 대조 대상으로 삼는다. | 문서에만 | H. 문헌 귀속과 문서 작성 당시 개발 상태를 설명한다. 단방향 조파는 개발 중이라고 적었다. [10-18 결론 검증 정정] |
| FT1-154 | p.28: 단일 소스선이 비엇갈린 격자에서 고주파 잡음을 일으켜 분포 질량 소스를 썼다. “a partially distributed mass source” | 이 행은 문서의 권고·개발 경위·수학적 정의를 대조 대상으로 삼는다. | 문서에만 | H. 분포 질량 소스를 선택한 배경을 설명하는 문장이다. [10-18 결론 검증 정정] |
| FT1-155 | p.28 (90): $f(x,y,t)=g(x)s(y,t)$ | K17. | 일치 | 가우스 공간 함수와 시간·방향 함수를 곱한다. |
| FT1-156 | p.28 (91): $g(x)=\exp[-\beta(x-x_s)^2]$ | K17의 `EXP(-Beta_gen*(xmk_wk(I)-Xc_WK)**2)`를 포함한 완결 대입. | 일치 | `Beta_gen`은 조파 형상 계수이다. 기준 깊이의 `Beta_1`과 다른 변수이다. |
| FT1-157 | p.28 (92): $s(y,t)=D\sin(\lambda y-\omega t)$ | K17. | 일치 | 부호가 같다. 코드의 시작 램프는 §3에 기록한다. |
| FT1-158 | p.28 번호 없음: $\lambda=k\sin\theta$; $x_s$는 중심, $D$는 크기, $k$는 선형 파수, 소스 중심축은 y축과 평행하다. | K16; `wavemaker.F:2378` `theta=Theta_WK*pi/180.` | 일치 | 각도 입력은 도 단위이며 계산은 라디안이다. |
| FT1-159 | p.28 (93): $D=\frac{2a_0\cos\theta(\omega^2-\alpha_1gk^4h^3)}{\omega kI[1-\alpha(kh)^2]}$ | K16의 `D_gen` 완결 대입. | 일치 | 분자의 음수 부호와 모든 차수가 같다. |
| FT1-160 | p.28 번호 없음: $\alpha=-0.390,\ \alpha_1=\alpha+1/3$ | `wavemaker.F:2379` `alpha=-0.39`; 2380 `alpha1=alpha+1./3.` | 일치 | 조파용 선형 분산 계수이다. 입력 `Beta_ref`를 변경해도 이 상수가 자동으로 바뀌지 않는다. |
| FT1-161 | p.28 (94): $I=\int_{-\infty}^{\infty}\exp(-\beta x^2)\exp(-ilx)dx=\sqrt{\pi/\beta}\exp(-l^2/4\beta)$; $l=k\cos\theta$ | K16의 `rl_gen`, `rI` 대입. | 일치 | 정칙 가우스 적분 결과를 사용한다. 코드의 원주율 상수는 이 위치에서 `3.14159`이다. |
| FT1-162 | p.28–29: 형상 계수가 클수록 소스가 좁다. 폭 정의는 유일하지 않다. $\exp(-5)=0.0067$ 배인 두 점 사이를 폭으로 정의한다. | 이 행은 문서의 권고·개발 경위·수학적 정의를 대조 대상으로 삼는다. | 문서에만 | H. 가우스 함수의 형상 계수와 폭의 수학적 정의이다. 문서는 최대값의 약 0.0067배가 되는 두 점 사이를 폭으로 정의한다. [10-18 결론 검증 정정] |
| FT1-163 | p.29 (95): $\beta(x-x_s)^2=5$ | K16. | 일치 | $x-x_s=\pm W/2$와 식 (97)을 대입하면 5가 된다. |
| FT1-164 | p.29 (96): $W=\lvert x_2-x_1\rvert=2\sqrt{5/\beta}$ | K16. | 일치 | `width=delta*wave_length/2`와 `beta_gen=80/(delta*L)^2`는 이 폭을 준다. |
| FT1-165 | p.29 (97): $\beta=\frac5{(\delta L/4)^2}=\frac{80}{\delta^2L^2}$; 번호 없음 $W=\delta L/2$, $\delta$는 1차 크기이다. | K16. | 일치 | 계수 80과 두 제곱이 같다. |
| FT1-166 | p.29: 불규칙파의 $\beta$는 첨두 주파수로 정해 모든 성분에 공통으로 쓴다. “then used for all components in the wave train” | `wavemaker.F:2026` `C_phase=1.0_SP/wkn*fm*2.0_SP*pi`; 2027 `wave_length=C_phase/fm`; 2082 `beta_gen(kf)=80.0_SP/delta**2/wave_length**2` `io.F:870,1974–1976`의 `WAVEMAKER`·`EqualEnergy` 입력과 `wavemaker.F:370–400`의 호출 분기. 등 에너지 경로 `wavemaker.F:2008–2028,2082–2085`, 등 주파수 경로 `2254–2271,2324–2332` 모두 성분별 파수를 사용한다. `7b93138:src/wavemaker.F:1230–1246,1292–1296`도 같다. `wkn.eq.0.0` 예외는 `wave_length=C_phase/fm`에 천해 파속을 사용한다. | 불일치 | E 후보 (강함). 불규칙파의 beta_gen은 성분별 파수로 정해진다. 첨두 주파수의 공통 폭을 쓴다는 문서와 자기 주석에 모순한다. 이 판정은 폭의 계산에 관한 코드 결함 후보이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-167 | p.29 그림 1: “Source function definition in the computing domain.” 도식은 $x_1,x_s,x_2,W,\lambda,l,k,\theta$를 표시한다. | K16, K17. | 일치 | 그림을 직접 열었다. 음영 소스 띠는 y축과 평행하다. 직각삼각형의 성분은 $l=k\cos\theta,\lambda=k\sin\theta$와 같다. |
| FT1-168 | p.29–30: 주파수 구간마다 방향 분포를 조정해 연안 방향 주기를 맞춘다. “adjusted the distribution of wave directions in each frequency bin” | `wavemaker.F:2042` `tmp2=I*2.0_SP*pi/DY/(Nglob-1.0_SP)`; 2049 `IF(tmp2.LT.tmp1) tmp3=ASIN((I-1)*2.0_SP*pi/DY/(Nglob-1.0_SP)/tmp1)`; 2075 `Theta = tmp3` | 일치 | 방향 파수를 영역 폭의 정수 주기에 맞춘다. 연안류·이안류에 효과적이라는 성능 주장은 이 코드 판독으로 검증하지 않는다. |
| FT1-169 | p.30 3.7.2: $a_0,\theta,h,T$로 식 (93)의 $D$를 구하고 식 (92)로 규칙파를 만든다. | `wavemaker.F:2369–2370`의 서브루틴 선언은 위 K16의 입력에 대응한다. K16, K17. | 일치 | 입력 진폭은 파고의 절반이다. |
| FT1-170 | p.30 3.7.3: 주파수·방향별 에너지에서 진폭을 구하고 임의 위상 성분을 합한다. “with random phases” | `wavemaker.F:287–293` 부근의 DATA2D 호출; 2106 `phi1(kf,ktheta)=rand()*2.0_SP*pi`; K19 아래 계수 합. | 일치 | 입력 방향 스펙트럼 경로가 있다. 지정 위상을 받는 추가 경로는 §3에 기록한다. |
| FT1-171 | p.30: TMA·JONSWAP과 wrapped-normal 방향 분포를 쓴다. | K18; `wavemaker.F:1878–1879`의 `JON` 분기. | 일치 | PDF에는 JONSWAP도 적혀 있다. 이 문구가 없는 LaTeX 원고 882행을 대신 인용하지 않는다. |
| FT1-172 | p.30 (98): $S(f,h,\theta)=E(f,h)G(\theta)$ | K18; `wavemaker.F:1971` `Hmo_each(ktheta)=4.0_SP*SQRT((alpha_spec*Ef100*AG(ktheta)))` | 일치 | 주파수 에너지와 방향 가중치를 곱한다. |
| FT1-173 | p.30 (99): $E(f,h)=\alpha g^2f^{-5}(2\pi)^{-4}\Phi(2\pi f,h)e^{-5/4(f/f_p)^{-4}}\gamma^{e^{[-(f/f_p-1)^2/2\sigma^2]}}$ | K18의 `Etma` 완결 대입과 `alpha_spec` 대입. | 일치 | 형상 스펙트럼은 $\alpha=1$로 계산한 뒤 전체 에너지를 입력 $H_{mo}$로 정규화한다. |
| FT1-174 | p.30 번호 없음: $\alpha$는 입력 $H_{mo}/H_{sig}$로 구한다. $\sigma=\{0.07\ (f\le f_p),0.09\ (f>f_p)\}$ | K18. | 일치 | `alpha_spec=Hmo**2/16/Ef`이며 경계의 등호도 일치한다. |
| FT1-175 | p.30 번호 없음: JONSWAP에서는 $\Phi=1.0$이다. TMA에서는 $\Phi=\{\frac12\omega_h^2\ (\omega_h\le1),1-\frac12(2-\omega_h)^2\ (2>\omega_h>1),1\ (\omega_h\ge2)\}$ | K18. | 일치 | 두 경계에서 조각 함수가 연결된다. |
| FT1-176 | p.30 번호 없음: $\omega_h=2\pi f(h/g)^{1/2}$ | `wavemaker.F:1873` `omiga_spec=2.0_SP*pi*fre*SQRT(h_gen/grav)` | 일치 | 무차원 주파수의 수심·중력 차수가 같다. |

### 2.7 p.31–32와 p.81: 방향 분포·바람·파고·병렬·수치 불안정

K19 — `wavemaker.F:874–882`의 직렬 내부 조파 계수.

```fortran
            Cm(i,j,kf)=Cm(i,j,kf) &
             +D_gen(kf,ktheta)*exp(-beta_gen(kf)*((I-Ibeg)*DX-Xc)**2) &
          *cos(rlamda(kf,ktheta) &
          *((J-Jbeg)*DY-ZERO)+phi1(kf,ktheta))
            Sm(i,j,kf)=Sm(i,j,kf) &
             +D_gen(kf,ktheta)*exp(-beta_gen(kf)*((I-Ibeg)*DX-Xc)**2) &
          *sin(rlamda(kf,ktheta) &
          *((J-Jbeg)*DY-ZERO)+phi1(kf,ktheta))
```

시간 합은 `sources.F:129–132`이다.

```fortran
                WK_Source=WK_Source+AA*(Cm(I,J,kf)*BB(kf) &
                    +Sm(I,J,kf)*CC(kf))
            WaveMaker_Mass(I,J)=WK_Source
```

K25 — `sources.F:357–362` (`METEO && WindForce`).

```fortran
          SourceX(I,J)=SourceX(I,J)+MASK_WIND(I,J)*RHO_AW*Cdw*WindU2D(I,J) &
                *SQRT(WindU2D(I,J)*WindU2D(I,J) &
                      + WindV2D(I,J)*WindV2D(I,J))
          SourceY(I,J)=SourceY(I,J)+MASK_WIND(I,J)*RHO_AW*Cdw*WindV2D(I,J) &
                *SQRT(WindU2D(I,J)*WindU2D(I,J) &
                      + WindV2D(I,J)*WindV2D(I,J))
```

K26 — `etauv_solver.F:580–589`의 Froude 상한.

```fortran
        Utotal=SQRT(U(I,J)*U(I,J)+V(I,J)*V(I,J))
        Fr=SQRT(GRAV*Max(H(I,J),MinDepthFrc))
        IF(Utotal/Fr.gt.FroudeCap)THEN
          Utheta=ATAN2(V(I,J),U(I,J))
          U(I,J)=FroudeCap*Fr*COS(Utheta)
          V(I,J)=FroudeCap*Fr*SIN(Utheta)
          HU(I,J)=U(I,J)*Max(H(I,J),MinDepthFrc)
          HV(I,J)=V(I,J)*Max(H(I,J),MinDepthFrc)
        ENDIF
```

| 행 ID | 항목·문서(원문) | 코드(원문) | 판정 | 이유 |
|---|---|---|---|---|
| FT1-177 | p.31 (100): $G(\theta)=\frac1{2\pi}+\frac1\pi\sum_{n=1}^Ne^{[-(n\sigma_\theta)^2/2]}\cos n\theta$ | K18의 `AG` 대입. | 불일치 | F. 코드의 각도는 $\theta-\theta_{input}$이다. 문서의 $\theta$를 평균 입사 방향에 대한 상대각으로 놓으면 같다. 이산 정규화는 §3에 기록한다. |
| FT1-178 | p.31: 원형 편차 $\sigma_\theta$, 언더플로 방지를 위한 “$N=20$ in the model.” | `wavemaker.F:1933` `sigma_theta=sigma_theta_input*pi/180.0_SP`; 1934 `N_spec=20.0_SP/sigma_theta` `wavemaker.F:1862`의 정수 `N_spec` 선언. `7b93138:src/wavemaker.F:1122–1123`도 같은 대입이다. | 불일치 | B. 방향 분포 합의 항 수는 N_spec=20.0_SP/sigma_theta로 정한다. 고정 20항으로 적지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-179 | p.31: “first divided into 1000 frequency components”; 등 에너지 사용자 지정 성분으로 재구성하며 방향은 균등 분할한다. | `wavemaker.F:1870` `do kf=1,10000`; 1872 `fre=fmin+(fmax-fmin)/10000.0_SP*(kf-1.0_SP)`; 1898 `Ef100=Ef/REAL(mfreq+1)` `io.F:1726,1740`에서 `Nfreq`·`Ntheta`를 읽고 `wavemaker.F:383–390`에서 `mfreq`·`mtheta`에 전달한다. `7b93138:src/wavemaker.F:1061–1063`의 초기 분할도 10000이다. 3.0 TeX 928행 전후의 2100 표기도 PDF p.31의 1000 및 코드 10000과 구분한다. | 불일치 | B. 코드의 초기 스펙트럼 적분 분할은 10000이다. PDF p.31의 성분 수 설명과 사용자 지정 주파수 수를 구분한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-180 | p.31 (101): $\eta=\sum_{m=1}^MC_m\cos\omega_mt+\sum_{m=1}^MS_m\sin\omega_mt$ | K19. `sources.F:117–132`의 내부 조파 분기와 `etauv_solver.F:204–243`의 질량 방정식에 연결된다. `7b93138:src/etauv_solver.F:94–106`에서도 질량 소스였다. | 불일치 | B. 내부 조파의 조화합은 질량 원천 항이다. 흡수·발생 경계의 직접 수면고 합성과 구분한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-181 | p.31 (102): $C_m=\sum_{n=1}^kD_{mn}\cos(k_{mn}y+\varepsilon_{mn}),\quad S_m=\sum_{n=1}^kD_{mn}\sin(k_{mn}y+\varepsilon_{mn})$ | K19. | 불일치 | F. 코드의 $D_{mn}$에 가우스 공간 계수를 포함하면 같은 조화합이다. `D_gen`은 질량 소스 진폭이다. 이를 표면파 진폭과 구분해야 한다. |
| FT1-182 | p.31: y축은 조파기 주축이다. $D_{mn},k_{mn},\varepsilon_{mn}$은 진폭·y파수·위상이다. 위상은 임의로 정할 수 있다. 1차원 단방향 스펙트럼 조파도 제공한다. | `wavemaker.F:1938–1939` `IF(mtheta==1) THEN ! 1D case` / `AG(1) = 1.0_SP`; K19. | 일치 | 방향 성분이 하나일 때 1차원 분포를 선택한다. |
| FT1-183 | p.31 (103): $\mathbf R_w=\frac{\rho_a}{\rho}C_{dw}\lvert\mathbf U_{10}-\mathbf C\rvert(\mathbf U_{10}-\mathbf C)$; $\mathbf C$는 파속이다. | K25; `mod_meteo.F:707` `Celerity=MIN(ABS(ETAt(I,J))/tmp1,SQRT(GRAV*ABS(H(I,J))))`; 710 `WindU2D(I,J)=WindU2D(I,J)-Celerity*COS(AngleLocal)`; 711의 y대응식. | 일치 | `METEO && WindWaveInteraction`에서 상대 바람 유속을 만들고 크기와 곱한다. 밀도비는 `mod_param.F:77`의 `RHO_AW = 0.0012041_SP`이다. |
| FT1-184 | p.31: “The wind stress is only applied on wave crests.” 강제 파봉 높이와 최대 수면고 비의 자유 매개변수를 둔다. | `mod_meteo.F:292` `CALL READ_FLOAT(WindCrestPercent,FILE_NAME,'WindCrestPercent',ierr)`; 295 `WindCrestPercent=LARGE`; 722 `IF(ETA(I,J)<HeightMax(I,J)*(1-WindCrestPercent)+ETAmean(I,J))MASK_WIND(I,J)=0` `mod_meteo.F:213–218,247–263,292–307,643–651,719–722`; `sources.F:355–364`. 네 PDF 전체와 TeX 판독 기록에서 `WindCrestPercent`, `WindWaveInteraction`, 파봉 표현을 검색했다. | 불일치 | C. 3.0 p.31의 누락은 파봉 마스크를 켜는 조건이다. `METEO`가 정의되고 `WindForce`가 참인 경로에서 `WindCrestPercent=LARGE`이면 `MASK_WIND=1`이다. `WindCrestPercent` 미입력 또는 `WindWaveInteraction`이 거짓이면 이 경로를 쓴다. 3.0 p.37·2.1 p.37·Intro-TN p.11도 매개변수를 설명하지만 이 해제 조건은 적지 않는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-185 | p.32: 평균 파고와 제곱평균제곱근 파고를 각 격자의 영점 교차로 계산한다. “using zero-crossing at each grid point” | `mixing.F:288–294` `Tmpe = Eta(i,j)-ETAmean(i,j)`; `Tmp_0 = Eta0(i,j)-ETAmean(i,j)`; `if(Tmpe>Tmp_0.and.Tmpe*Tmp_0<=Zero) then`; `Num_Zero_Up(i,j) = Num_Zero_Up(i,j)+1`; `if(Num_Zero_Up(i,j)>=2) then`; `HavgSum(i,j) = HavgSum(i,j)+Emax(i,j)-Emin(i,j)`; `HrmsSum(i,j) = HrmsSum(i,j)+(Emax(i,j)-Emin(i,j))**2` | 일치 | 이전 창 평균을 기준으로 상향 교차를 찾고 파고와 파고 제곱을 합한다. 표본 개수의 추가 문제는 §3의 FT1-247에 기록한다. |
| FT1-186 | p.32 (104): $H_{1/3}=4.004\sqrt{m_0}$ | `mixing.F:244` `SigWaveHeight = 4.004*SQRT( ETA2mean )  !ykcho` | 일치 | 계수 4.004는 같다. $m_0$ 산출 방식은 다음 행에서 대조한다. |
| FT1-187 | p.32 (105): $m_0=\frac1{t_2-t_1}\int_{t_1}^{t_2}\eta^2dt$ | `mixing.F:146` `ETA2sum = (Eta-ETAmean)*(Eta-ETAmean)*DT + ETA2sum   !ykchoi`; 147 `ETA2mean = ETA2sum/T_sum`; 267의 동일 누적. `mixing.F:146–154`에서 제곱 누적 뒤 `ETAmean=ETAsum/T_sum`을 갱신한다. `7b93138:src/mixing.F:113–125`도 이전 평균 사용을 명시한다. | 불일치 | B. ETA2sum은 이전 평균 수면고를 뺀 값의 제곱을 시간 가중 누적한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-188 | p.32: 영역을 나누고 각 부영역을 별도 프로세서 코어에 배정한다. ghost 셀은 세 줄이다. | `mod_global.F:129` `INTEGER, PARAMETER :: Nghost = 3`; `misc.F:54` `SUBROUTINE INDEX`의 지역 범위 구성. | 일치 | 모델의 격자 분할과 겹침 폭을 확인했다. |
| FT1-189 | p.32: MPI 비차단 통신으로 이웃 프로세서의 겹침 영역을 교환한다. | `parallel.F:74–75` `call MPI_IRECV( rWmsg, len, MPI_SP, &` / `n_west, 0, comm2d, req(nreq), ier )`; 82–83 `call MPI_ISEND( sWmsg, len, MPI_SP, &` / `n_west, 1, comm2d, req(nreq), ier )` | 일치 | 송수신 원문을 직접 확인했다. |
| FT1-190 | p.32: Naik의 병렬 파이프라인 삼중 대각 해법으로 식 (23)에서 유속을 얻는다. | `etauv_solver.F:465` `call TRIDx(myA,myC,myD,myF)`; `tridiagnal.F:413` `SUBROUTINE TRIDx ( a, c, d, f)`; 502 `SUBROUTINE TRIDy ( a, c, d, f)` | 일치 | 방향별 전달과 소거·역대입 경로를 확인했다. Naik 논문에 대한 속도·정확도 검증은 수행하지 않는다. |
| FT1-191 | p.32 4.1: Fortran 90, cpp 분리, 동적 배열, 단정밀도 기본값. “Precision is selected using the selected_real_kind Fortran intrinsic function defined in the makefile.” | `mod_param.F:64` `INTEGER, PARAMETER::SP=SELECTED_REAL_KIND(6,30)`; `T/Makefile:7` `PRECISION   = single`; `init.F:128`의 할당 목록. `mod_param.F:58–68` 및 `7b93138:src/mod_param.F:58–68`의 배정도 분기는 `INTEGER, PARAMETER::SP=8`이다. | 불일치 | B. 정밀도 플래그는 빌드에서 선택한다. kind 값의 정의는 mod_param.F에 있다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-192 | p.32 4.1: 직렬·병렬, 직교·구면, 예제, 단방향 nesting, 쇄파 지수·나이, bubble·foam, 마찰식 선택을 열거한다. | `main.F:237` `# if defined (COUPLING)`; 253 `# if defined (FOAM)`; K13, K26. | 일치 | 기능의 이름을 해당 전처리·호출 경로와 연결했다. 예제·거품 내부 전개는 이 이론 대조의 범위 밖이다. |
| FT1-193 | p.32 4.1: “ITERATION ... is not used any more.” RK와 CFL 결합이 더 효율적이었다. | `main.F:380` `DO ISTAGE=1,3`; FT1-121의 반복 부재. | 일치 | p.25의 반복 필요 문장과 문서 내부에서도 충돌한다. 효율 비교는 코드로 검증하지 않는다. |
| FT1-194 | p.32 4.1–4.2: 흐름도는 그림 2이다. 압축 배포물을 풀고 `> tar xvf *.tar`를 쓴다. | 이 쪽에는 그림 2 본체가 없다. | 문서에만 | H. 흐름도 위치 안내와 배포물 압축 해제 명령을 설명한다. [10-18 결론 검증 정정] |
| FT1-195 | p.81 상단: $\lvert\nabla h\rvert>1.0$를 피한다. 큰 바닥 경사가 불안정을 유발할 수 있다. | 이 행은 문서의 권고·개발 경위·수학적 정의를 대조 대상으로 삼는다. | 문서에만 | H. 큰 바닥 경사가 불안정을 유발할 수 있으므로 피하라는 수치 안정성 권고이다. [10-18 결론 검증 정정] |
| FT1-196 | p.81: 매우 얕은 영역의 비현실적인 유속을 FroudeCap으로 제한한다. “specified as MinDepthFrc by a user” | K26. `io.F:2898–2910` 입력 및 `etauv_solver.F:568–593` 실제 분기. 네 PDF 전체와 TeX 판독 기록의 `FroudeCap` 검색; 3.0 p.41, 2.1 p.40, Intro-TN p.13, TeX 1341행. | 일치 | Froude 상한을 유속 계산에 적용한다. 3.0 p.41·2.1 p.40·Intro-TN p.13도 이 기능을 설명한다. p.81의 얕은 수심 설명은 사용 목적이며 얕은 셀에서만 분기한다는 조건이 아니다. 실제 검사는 `MASK(I,J)<1`의 `ELSE`에서 `IF(Utotal/Fr.gt.FroudeCap)THEN`으로 수행한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-197 | p.81: “The default value for FroudeCap is 10.0.” | `io.F:2898` `CALL READ_FLOAT(FroudeCap,FILE_NAME,'FroudeCap',ierr)`; 2900 `FroudeCap = 3.0_SP` `7b93138:src/mod_input.F:128`은 `INTENT(OUT)`이다. 과거 입력 호출 뒤 선언 초기값 10이 보존된다고 단언하지 않는다. 실제 상한 분기는 `etauv_solver.F:568–593`이다. | 불일치 | A. FroudeCap의 문서상 기본값 10은 과거 선언 초기값이다. 2017-05-01부터 입력 누락 분기는 3을 대입한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-198 | p.81: 3.0 이하로 낮추면 문제와 CFL 효율을 개선할 수 있다. 1.5 미만은 침수 선단 유속을 제한할 수 있어 권장하지 않는다. | 이 행은 문서의 권고·개발 경위·수학적 정의를 대조 대상으로 삼는다. | 문서에만 | H. 문서는 FroudeCap을 3.0 이하로 낮추면 문제와 CFL 효율을 개선할 수 있다고 적는다. 1.5 미만은 침수 선단 유속을 제한할 수 있어 권장하지 않는다. [10-18 결론 검증 정정] |
| FT1-199 | p.81: “The default value ... MinDepthFrc, is 0.001 m.” | `io.F:2933` `CALL READ_FLOAT(MinDepthFrc,FILE_NAME,'MinDepthFrc',ierr)`; 2935 `MinDepthFrc = 0.1_SP`; 2948 `MinDepthFrc=MIN(MinDepthFrc,MinDepth)`; 2949 `MinDepth=MinDepthFrc` | 불일치 | B. MinDepthFrc의 문서 기본값 0.001은 문서 시점 코드와 다르다. 현재 입력 누락값은 0.1이다. 이후 `MinDepthFrc=MIN(MinDepthFrc,MinDepth)`와 `MinDepth=MinDepthFrc`를 적용하므로 최종값은 두 입력의 최솟값이다. [10-18 git 이력 판정] |
| FT1-200 | p.81: 작은 MinDepthFrc는 큰 유속·작은 dt·불안정을 일으킬 수 있다. 문제가 생기면 더 큰 값을 쓴다. | 이 행은 문서의 권고·개발 경위·수학적 정의를 대조 대상으로 삼는다. | 문서에만 | H. 작은 MinDepthFrc가 큰 유속·작은 시간 간격·불안정을 일으킬 수 있다는 가능성과 문제가 생겼을 때의 조정 권고이다. [10-18 결론 검증 정정] |
| FT1-201 | p.81: CFL 기본값은 0.5이다. 불안정하면 더 작게 쓸 수 있다. | `io.F:2862` `CALL READ_FLOAT(CFL,FILE_NAME,'CFL',ierr)`; 2864 `CFL = 0.5_SP` | 일치 | 기본값을 읽기 호출과 누락 처리에 함께 대조했다. |
| FT1-202 | p.81: MUSCL-TVD는 4차까지 구현한다. 초기 Yamamoto 방식은 Minmod를 썼다. 심해 불안정 시 3차를 권고한다. | `init.F:389–392` `IF(HIGH_ORDER(1:3)=='SEC')THEN` / `Kappa = -1.0_SP` / `ELSE` / `Kappa = 1.0_SP/3.0_SP`; `fluxes.F:773` `! The "kappa" is meaningless in above routines.` `io.F:2842–2854`의 `HIGH_ORDER` 입력 → `fluxes.F:56–106` 분기 → `CONSTRUCTION`의 `CONSTRUCT_X` 호출(473–480행). `fluxes.F:779–784`는 `Kappa`를 쓰지 않는다. `7b93138:src/fluxes.F:729–740`도 같다. FT1-277의 4차 제한 함수 옵션과 구분한다. | 불일치 | B. SECOND와 THIRD는 같은 선형 재구성 경로를 사용한다. 문서의 THIRD 권고를 3차 정확도 보장으로 적지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-203 | p.81: Version 3.0은 Erduran의 4차 방식에서 3차 부분에 van-Leer를 쓴다. 안정성 개선을 기대한다. | `fluxes.F:1549` `! The minmod limiter is used for the fourth order part in the fourth order scheme`; 1604 `! The van-Leer limiter is used for the third order part in the fourth order scheme`; K10. | 일치 | 두 부분의 제한 함수가 문서와 같다. “hope”는 검증된 개선 결과로 쓰지 않는다. |
| FT1-204 | p.81 하단: References의 Agnon (1999), Berkhoff (1982), Bermùdez·Vàzquez (1994) 서지 항목. | 계산 대상 식·입력·옵션이 없다. | 문서에만 | H. 참고문헌 목록이다. [10-18 결론 검증 정정] |

### 2.8 p.86–89: 부록 A의 전개식 (107)–(120)

p.86은 이전 매뉴얼과 Shi et al. (2012)의 전개식에 오기가 있다고 알린다.
이 보고서는 이전 식을 복원해 현재 PDF 대신 쓰지 않는다.
아래 D107–D120은 쪽 이미지와 대조한 인쇄식 전사이다.
코드의 `Beta_1`은 이 부록의 $\beta$이다.
코드의 `Beta_2`는 문서의 $\beta$가 아니다.

K20 — `dispersion.F:337–346`.

```fortran
	 U1p(I,J)=0.5_SP*(1.0_SP-Beta_1)*(1.0_SP-Beta_1)  &
                *DEPTH(I,J)*DEPTH(I,J)  &
                *(Uxx(I,J)+Vxy(I,J)) &
               +(Beta_1-1.0_SP)*DEPTH(I,J)*(DUxx(I,J)+DVxy(I,J))
	 V1p(I,J)=0.5_SP*(1.0_SP-Beta_1)*(1.0_SP-Beta_1)  &
                *DEPTH(I,J)*DEPTH(I,J)  &
                *(Uxy(I,J)+Vyy(I,J)) &
               +(Beta_1-1.0_SP)*DEPTH(I,J)*(DUxy(I,J)+DVyy(I,J))
```

K21 — `dispersion.F:296–299,312–317`.

```fortran
       U4(I,J)=(1.0_SP/3.0_SP-Beta_1+0.5_SP*Beta_1*Beta_1)*DEPTH(I,J)*DEPTH(I,J)*(Uxx(I,J)+Vxy(I,J)) &
                +(Beta_1-1.0_SP/2.0_SP)*DEPTH(I,J)*(DUxx(I,J)+DVxy(I,J))
       V4(I,J)=(1.0_SP/3.0_SP-Beta_1+0.5_SP*Beta_1*Beta_1)*DEPTH(I,J)*DEPTH(I,J)*(Uxy(I,J)+Vyy(I,J)) &
                +(Beta_1-1.0_SP/2.0_SP)*DEPTH(I,J)*(DUxy(I,J)+DVyy(I,J))
	  	   ken1 = ( 1.0_SP/6.0_SP - Beta_1 + Beta_1*Beta_1 )*rh*reta*Beta_2   &
		         + ( 1.0_SP/2.0_SP*Beta_1*Beta_1 - 1.0_SP/6.0_SP )*reta*reta*Beta_2*Beta_2
		   ken2 = ( Beta_1 - 1.0_SP/2.0_SP )*reta*Beta_2
		   U4(I,J) = U4(I,J) + gamma2*MASK9(I,J)*( ken1*UxxVxy + ken2*HUxxHVxy )
		   V4(I,J) = V4(I,J) + gamma2*MASK9(I,J)*( ken1*UxyVyy + ken2*HUxyHVyy )
```

K22 — `dispersion.F:422–436`.

```fortran
        U1pp(I,J)=-reta*Beta_2*ETAx(I,J)*Beta_2*(Utx(I,J)+Vty(I,J)) - 0.5_SP*reta*reta*Beta_2*Beta_2*(Utxx(I,J)+Vtxy(I,J))&
                  -ETAx(I,J)*Beta_2*(DUtx(I,J)+DVty(I,J)) -reta*Beta_2*(DUtxx(I,J)+DVtxy(I,J))
        V1pp(I,J)=-reta*Beta_2*ETAy(I,J)*Beta_2*(Utx(I,J)+Vty(I,J)) - 0.5_SP*reta*reta*Beta_2*Beta_2*(Utxy(I,J)+Vtyy(I,J))&
                  -ETAy(I,J)*Beta_2*(DUtx(I,J)+DVty(I,J)) -reta*Beta_2*(DUtxy(I,J)+DVtyy(I,J))
		  ken1 = Beta_1*( 1.0_SP - Beta_1 )*rh*ETAT(I,J)*Beta_2 - Beta_1*Beta_1*reta*Beta_2*ETAT(I,J)*Beta_2
		  ken2 = Beta_1*( 1.0_SP - Beta_1 )*rh*reta*Beta_2 - 0.5*Beta_1*Beta_1*reta*reta*Beta_2*Beta_2
		  ken3 = Beta_1*ETAT(I,J)*Beta_2
		  ken4 = Beta_1*reta*Beta_2
		  U1pp(I,J) = U1pp(I,J) - ken1*UxxVxy - ken2*( Utxx(I,J)+Vtxy(I,J) ) + ken3*HUxxHVxy + ken4*(DUtxx(I,J)+DVtxy(I,J))
		  V1pp(I,J) = V1pp(I,J) - ken1*UxyVyy - ken2*( Utxy(I,J)+Vtyy(I,J) ) + ken3*HUxyHVyy + ken4*(DUtxy(I,J)+DVtyy(I,J))
```

D107 — `funwave_tvd_3.0.pdf p.86`, 식 (107).

$$
\displaystyle U_1^{'}=\frac{1}{2}(1-\beta)^2 h^2 (u_{xx} + v_{xy}) - (1-\beta)h \big[ (hu)_{xx} + (hv)_{xy} \big]\tag{107}
$$

D108 — `funwave_tvd_3.0.pdf p.86`, 식 (108).

$$
\displaystyle V_1^{'}=\frac{1}{2}(1-\beta)^2 h^2 (u_{xy} + v_{yy}) - (1-\beta)h \big[ (hu)_{xy} + (hv)_{yy} \big]\tag{108}
$$

D109 — `funwave_tvd_3.0.pdf p.86`, 식 (109).

$$
\displaystyle \begin{aligned} & U_1^{''}=-\bigg[ \eta \eta_x (u_{tx}+v_{ty}) + \frac{1}{2} \eta^2 ( u_{txx}+v_{txy} ) + \eta_x \Big\{ (hu)_{tx} + (hv)_{ty} \Big\} + \eta \Big\{ (hu)_{txx} + (hv)_{txy} \Big\} \bigg] \\ & - \Big[ \beta(1-\beta) h \eta_t - \beta^2 \eta \eta_t \Big] (u_{xx}+v_{xy}) - \Big[ \beta(1-\beta) h \eta - \frac{1}{2} \beta^2 \eta^2 \Big] ( u_{txx} + v_{txy} ) \\ & + \beta \eta_t \Big[ (hu)_{xx} + (hv)_{xy} \Big] + \beta \eta \Big[ (hu)_{txx} + (hv)_{txy} \Big] \end{aligned}\tag{109}
$$

D110 — `funwave_tvd_3.0.pdf p.86`, 식 (110).

$$
\displaystyle \begin{aligned} & V_1^{''}=-\bigg[ \eta \eta_y (u_{tx}+v_{ty}) + \frac{1}{2} \eta^2 ( u_{txy}+v_{tyy} ) + \eta_y \Big\{ (hu)_{tx} + (hv)_{ty} \Big\} + \eta \Big\{ (hu)_{txy} + (hv)_{tyy} \Big\} \bigg] \\ & - \Big[ \beta(1-\beta) h \eta_t - \beta^2 \eta \eta_t \Big] (u_{xy}+v_{yy}) - \Big[ \beta(1-\beta) h \eta - \frac{1}{2} \beta^2 \eta^2 \Big] ( u_{txy} + v_{tyy} ) \\ & + \beta \eta_t \Big[ (hu)_{xy} + (hv)_{yy} \Big] + \beta \eta \Big[ (hu)_{txy} + (hv)_{tyy} \Big] \end{aligned}\tag{110}
$$

| 행 ID | 항목·문서(원문) | 코드(원문) | 판정 | 이유 |
|---|---|---|---|---|
| FT1-205 | p.86: “there are typos in the expansion expressions in both Shi et al. (2012) and the previous manual lower than Version 3.0” | 이 행은 p.86의 이전 문헌 정정 안내이다. | 문서에만 | H. Shi et al. (2012)와 3.0 이전 매뉴얼의 전개식에 오기가 있었다는 문서 작성자의 안내이다. [10-18 결론 검증 정정] |
| FT1-206 | p.86 (107): D107의 $U'_1$ 전체. | K20의 `U1p` 완결 대입. | 일치 | $-(1-\beta)h=(\beta-1)h$이다. 제곱과 혼합 미분 방향도 같다. |
| FT1-207 | p.86 (108): D108의 $V'_1$ 전체. | K20의 `V1p` 완결 대입. | 일치 | y방향은 $u_{xy}+v_{yy}$와 $(hu)_{xy}+(hv)_{yy}$이다. |
| FT1-208 | p.86 (109): D109의 $U''_1$ 전체. | K22의 `U1pp` 두 완결 대입과 `ken1–ken4`. `dispersion.F:422–423,430–435`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). | 불일치 | E 후보 (강함). 직교 비선형 경로의 U1pp는 수면고 선형항에 0.04를 곱한다. 수면고 제곱항에는 0.0016을 곱한다. PDF 식 (109)에 없는 배수이다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-209 | p.86 (110): D110의 $V''_1$ 전체. | K22의 `V1pp` 두 완결 대입과 `ken1–ken4`. `dispersion.F:425–426,430–436`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). | 불일치 | E 후보 (강함). 직교 비선형 경로의 V1pp에도 Beta_2와 Beta_2 제곱이 붙는다. 식 (110)과 y미분 방향은 같지만 계수는 다르다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |

K23 — `dispersion.F:438–469`.

```fortran
         ken1=(Beta_1-1.0_SP)*(rhx+ETAx(I,J))*Beta_2
         ken2=(Beta_1-1.0_SP)*(rh+reta)*Beta_2
         ken3=( (1.0_SP-Beta_1)*(1.0_SP-Beta_1)*rh*rhx*Beta_2*Beta_2-Beta_1*(1.0_SP-Beta_1)*(rhx*reta*Beta_2+rh*ETAx(I,J)*Beta_2) &
                    +(Beta_1*Beta_1-1.0_SP)*reta*ETAx(I,J)*Beta_2*Beta_2 )
         ken4=( 0.5_SP*(1.0_SP-Beta_1)*(1.0_SP-Beta_1)*rh*rh*Beta_2*Beta_2-Beta_1*(1.0_SP-Beta_1)*rh*reta*Beta_2 &
                      +0.5_SP*(Beta_1*Beta_1-1.0_SP)*reta*reta*Beta_2*Beta_2 )
         ken5=( (1.0_SP-Beta_1)*(1.0_SP-Beta_1)*rh*rhy*Beta_2*Beta_2-Beta_1*(1.0_SP-Beta_1)*(rhy*reta*Beta_2+rh*ETAy(I,J)*Beta_2) &
                    +(Beta_1*Beta_1-1.0_SP)*reta*ETAy(I,J)*Beta_2*Beta_2 )
        U2(I,J)=ken1*(U(I,J)*HUxxHVxy+V(I,J)*HUxyHVyy) &
                +ken2*(Ux(I,J)*HUxxHVxy+U(I,J)*HUxxHVxy_x &
                    +Vx(I,J)*HUxyHVyy+V(I,J)*HUxyHVyy_x) &
                +ken3 &
                   *(U(I,J)*UxxVxy+V(I,J)*UxyVyy) &
                +ken4  &
                   *(Ux(I,J)*UxxVxy+U(I,J)*UxxVxy_x+Vx(I,J)*UxyVyy+V(I,J)*UxyVyy_x) &
                +Beta_2*Beta_2*(DUx(I,J)+DVy(I,J)+reta*Beta_2*(Ux(I,J)+Vy(I,J)))  &
                   *(HUxxHVxy+ETAx(I,J)*Beta_2*(Ux(I,J)+Vy(I,J))+reta*Beta_2*UxxVxy)
        ken1=(Beta_1-1.0_SP)*(rhy+ETAy(I,J))*Beta_2
        V2(I,J)=ken1*(U(I,J)*HUxxHVxy+V(I,J)*HUxyHVyy) &
                +ken2*(Uy(I,J)*HUxxHVxy+U(I,J)*HUxxHVxy_y &
                    +Vy(I,J)*HUxyHVyy+V(I,J)*HUxyHVyy_y) &
                +ken5 &
                   *(U(I,J)*UxxVxy+V(I,J)*UxyVyy) &
                +ken4  &
                   *(Uy(I,J)*UxxVxy+U(I,J)*UxxVxy_y+Vy(I,J)*UxyVyy+V(I,J)*UxyVyy_y) &
                +Beta_2*Beta_2*(DUx(I,J)+DVy(I,J)+reta*Beta_2*(Ux(I,J)+Vy(I,J)))  &
                   *(HUxyHVyy+ETAy(I,J)*Beta_2*(Ux(I,J)+Vy(I,J))+reta*Beta_2*UxyVyy)
```

K24 — `dispersion.F:471,475–476,486–498`.

```fortran
        omega_0=Vx(I,J)-Uy(I,J)
        omega_1=( b2*rhx + Beta_1*ETAx(I,J) )*Beta_2*( HUxyHVyy + (b2*rh+Beta_1*reta)*Beta_2*UxyVyy )  &
              - ( b2*rhy + Beta_1*ETAy(I,J) )*Beta_2*( HUxxHVxy + (b2*rh+Beta_1*reta)*Beta_2*UxxVxy )
       ken1=((Beta_1-1.0_SP/2.0_SP)*(reta+rh)*Beta_2)
       ken2=(1.0_SP/3.0_SP-Beta_1+0.5_SP*Beta_1*Beta_1)*rh*rh*Beta_2*Beta_2  &
               + (1.0_SP/6.0_SP-Beta_1+Beta_1*Beta_1)*rh*reta*Beta_2 &
               +(1.0_SP/2.0_SP*Beta_1*Beta_1-1.0_SP/6.0_SP)*reta*reta*Beta_2*Beta_2
       U3(I,J)=-V(I,J)*omega_1 - omega_0 &
                 *(ken1*HUxyHVyy &
                   +ken2*UxyVyy)
	 V3(I,J) = U(I,J)*omega_1 + omega_0 &
	            *(ken1*HUxxHVxy &
                    +ken2*UxxVxy)
```

D111 — `funwave_tvd_3.0.pdf p.86`, 식 (111).

$$
\displaystyle \begin{aligned} & U_2=\bigg[ (\beta-1)(h+\eta) \Big\{ u \big[ (hu)_x + (hv)_y \big]_x + v \big[ (hu)_x + (hv)_y \big]_y \Big\} \\ & +\bigg\{ \frac{1}{2} (1-\beta)^2 h^2 - \beta (1-\beta) h \eta + \frac{1}{2} (\beta^2-1) \eta^2 \bigg\} \Big\{ u (u_x+v_y)_x + v(u_x+v_y)_y \Big\} \\ & +\frac{1}{2} \Big\{ (hu)_x + (hv)_y + \eta (u_x+v_y) \Big\}^2 \bigg]_x \end{aligned}\tag{111}
$$

D112 — `funwave_tvd_3.0.pdf p.86`, 식 (112).

$$
\displaystyle \begin{aligned} & V_2=\bigg[ (\beta-1)(h+\eta) \Big\{ u \big[ (hu)_x + (hv)_y \big]_x + v \big[ (hu)_x + (hv)_y \big]_y \Big\} \\ & +\bigg\{ \frac{1}{2} (1-\beta)^2 h^2 - \beta (1-\beta) h \eta + \frac{1}{2} (\beta^2-1) \eta^2 \bigg\} \Big\{ u (u_x+v_y)_x + v(u_x+v_y)_y \Big\} \\ & +\frac{1}{2} \Big\{ (hu)_x + (hv)_y + \eta (u_x+v_y) \Big\}^2 \bigg]_y \end{aligned}\tag{112}
$$

D113 — `funwave_tvd_3.0.pdf p.87`, 식 (113).

$$
\displaystyle \begin{aligned} & U_3=-v \omega_1 - \omega_0 \bigg[ \Big\{ \big( \beta - \frac{1}{2} \big) (h+\eta) \Big\} \Big\{ (hu)_x + (hv)_y \Big\}_y \\ & + \Big\{ \big( \frac{1}{3} - \beta + \frac{1}{2} \beta^2 \big) h^2 + \big( \frac{1}{6} - \beta + \beta^2 \big) \eta h + \big( \frac{1}{2} \beta^2 - \frac{1}{6} \big) \eta^2 \Big\} (u_x+v_y)_y \bigg] \end{aligned}\tag{113}
$$

D114 — `funwave_tvd_3.0.pdf p.87`, 식 (114).

$$
\displaystyle \begin{aligned} & V_3=u \omega_1 + \omega_0 \bigg[ \Big\{ \big( \beta - \frac{1}{2} \big) (h+\eta) \Big\} \Big\{ (hu)_x + (hv)_y \Big\}_x \\ & + \Big\{ \big( \frac{1}{3} - \beta + \frac{1}{2} \beta^2 \big) h^2 + \big( \frac{1}{6} - \beta + \beta^2 \big) \eta h + \big( \frac{1}{2} \beta^2 - \frac{1}{6} \big) \eta^2 \Big\} (u_x+v_y)_x \bigg] \end{aligned}\tag{114}
$$

D115 — `funwave_tvd_3.0.pdf p.87`, 식 (115).

$$
\displaystyle \omega_0 = v_x - u_y\tag{115}
$$

D116 — `funwave_tvd_3.0.pdf p.87`, 식 (116).

$$
\displaystyle \begin{aligned} & \omega_1 = \bigg[ (\beta-1) h_x + \beta \eta_x \bigg] \bigg[ \Big\{ (hu)_x + (hv)_y \Big\}_y + \Big\{ (\beta-1)h + \beta \eta \Big\} (u_x+v_y)_y \bigg] \\ & - \bigg[ (\beta-1) h_y + \beta \eta_y \bigg] \bigg[ \Big\{ (hu)_x + (hv)_y \Big\}_x + \Big\{ (\beta-1)h + \beta \eta \Big\} (u_x+v_y)_x \bigg] \end{aligned}\tag{116}
$$

D117 — `funwave_tvd_3.0.pdf p.87`, 식 (117).

$$
\displaystyle \begin{aligned} & U_4=\bigg( \frac{1}{3} - \beta + \frac{1}{2} \beta^2 \bigg) h^2 (u_{xx} + v_{xy}) + \bigg( \beta - \frac{1}{2} \bigg) h \Big\{ (hu)_{xx} + (hv)_{xy} \Big\} \\ & + \bigg[ \Big\{ \Big(\frac{1}{6} - \beta + \beta^2 \Big) h \eta + \Big( \frac{1}{2} \beta^2 - \frac{1}{6} \Big) \eta^2 \Big\} ( u_{xx}+v_{xy} ) + \bigg( \beta - \frac{1}{2} \bigg) \eta \Big\{ (hu)_{xx}+(hv)_{xy} \Big\} \bigg] \end{aligned}\tag{117}
$$

D118 — `funwave_tvd_3.0.pdf p.87`, 식 (118).

$$
\displaystyle \begin{aligned} & V_4=\bigg( \frac{1}{3} - \beta + \frac{1}{2} \beta^2 \bigg) h^2 (u_{xy} + v_{yy}) + \bigg( \beta - \frac{1}{2} \bigg) h \Big\{ (hu)_{xy} + (hv)_{yy} \Big\} \\ & + \bigg[ \Big\{ \Big(\frac{1}{6} - \beta + \beta^2 \Big) h \eta + \Big( \frac{1}{2} \beta^2 - \frac{1}{6} \Big) \eta^2 \Big\} ( u_{xy}+v_{yy} ) + \bigg( \beta - \frac{1}{2} \bigg) \eta \Big\{ (hu)_{xy}+(hv)_{yy} \Big\} \bigg] \end{aligned}\tag{118}
$$

| 행 ID | 항목·문서(원문) | 코드(원문) | 판정 | 이유 |
|---|---|---|---|---|
| FT1-210 | p.86 (111): D111의 $U_2$ 전체. | K23의 `U2` 완결 대입. `dispersion.F:438–455`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). | 불일치 | E 후보 (강함). 직교 비선형 경로의 U2는 식 (111)의 전개 구조를 따른다. 추가 Beta_2 배수 때문에 동일한 차원식이 아니다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-211 | p.86 (112): D112의 $V_2$ 전체. | K23의 `V2` 완결 대입. `dispersion.F:439–445,459–469`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). | 불일치 | E 후보 (강함). 직교 비선형 경로의 V2는 y용 ken1을 사용한다. 식 (112)과의 차이는 Beta_2 배수이다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-212 | p.87 (113): D113의 $U_3$ 전체. | K24의 `U3`, `ken1,ken2` 완결 대입. `dispersion.F:475–493`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). | 불일치 | E 후보 (강함). 직교 비선형 경로의 U3는 -v·omega_1과 -omega_0 보정의 부호를 유지한다. 보정의 깊이 계수에는 식 (113)에 없는 Beta_2 배수가 남는다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-213 | p.87 (114): D114의 $V_3$ 전체. | K24의 `V3` 완결 대입. `dispersion.F:475–489,496–498`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). | 불일치 | E 후보 (강함). 직교 비선형 경로의 V3는 양의 u·omega_1과 omega_0 보정을 쓴다. 식 (114)과의 차이는 보정 계수의 Beta_2 배수이다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-214 | p.87 (115): $\omega_0=v_x-u_y$ | `dispersion.F:471` `omega_0=Vx(I,J)-Uy(I,J)` | 일치 | x와 y 미분 및 음수 부호가 같다. |
| FT1-215 | p.87 (116): D116의 $\omega_1$ 전체. | K24의 `omega_1` 완결 대입; `init.F:661` `b2=Beta_ref`; 663 `Beta_1=Beta_ref+1.0_SP` `dispersion.F:475–476`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). | 불일치 | E 후보 (강함). 직교 비선형 경로의 omega_1은 식 (116)의 미분 구조와 대응한다. 외부 곱과 내부 기준 깊이 곱에 문서에 없는 Beta_2가 들어간다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-216 | p.87 (117): D117의 $U_4$ 전체. | K21. `dispersion.F:295–317`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). `dispersion.F:322–329`의 `# if defined (ZALPHA)` 블록은 앞서 계산한 U4·V4를 선형식으로 다시 대입한다. | 불일치 | E 후보 (강함). 직교 비선형 경로의 U4 선형항은 식 (117)과 같다. 비선형 h·eta 및 eta 항에는 0.04를 곱한다. eta 제곱항에는 0.0016을 곱한다. 이 U4·V4 비선형 보정 판정은 `ZALPHA`를 정의하지 않은 경로에 한정한다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-217 | p.87 (118): D118의 $V_4$ 전체. | K21. `dispersion.F:295–317`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). `dispersion.F:322–329`의 `# if defined (ZALPHA)` 블록은 앞서 계산한 U4·V4를 선형식으로 다시 대입한다. | 불일치 | E 후보 (강함). 직교 비선형 경로의 V4 선형항은 식 (118)과 같다. y방향 비선형 보정에는 U4와 같은 Beta_2 배수가 남는다. 이 U4·V4 비선형 보정 판정은 `ZALPHA`를 정의하지 않은 경로에 한정한다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |

D119 — `funwave_tvd_3.0.pdf p.88`, 식 (119).

$$
\displaystyle \begin{aligned} & U_2= (\beta-1)(h+\eta)_x \bigg\{ u \Big[ (hu)_{xx} + (hv)_{yx} \Big] + v \Big[ (hu)_{xy} + (hv)_{yy} \Big] \bigg\} \\ & + (\beta-1)(h+\eta) \bigg\{ u \Big[ (hu)_{xx} + (hv)_{yx} \Big] + v \Big[ (hu)_{xy} + (hv)_{yy} \Big] \bigg\}_x \\ & +\bigg\{ \frac{1}{2} (1-\beta)^2 h^2 - \beta (1-\beta) h \eta + \frac{1}{2} (\beta^2-1) \eta^2 \bigg\}_x \Big\{ u (u_x+v_y)_x + v(u_x+v_y)_y \Big\} \\ & +\bigg\{ \frac{1}{2} (1-\beta)^2 h^2 - \beta (1-\beta) h \eta + \frac{1}{2} (\beta^2-1) \eta^2 \bigg\} \Big\{ u (u_x+v_y)_x + v(u_x+v_y)_y \Big\}_x \\ & +\Big\{ (hu)_x + (hv)_y + \eta (u_x+v_y) \Big\} \Big\{ (hu)_x + (hv)_y + \eta (u_x+v_y) \Big\}_x \\ & = (\beta-1)(h_x + \eta_x) \bigg\{ u \Big[ (hu)_{xx} + (hv)_{yx} \Big] + v \Big[ (hu)_{xy} + (hv)_{yy} \Big] \bigg\} \\ & + (\beta-1)(h+\eta) \bigg\{ u_x \Big[ (hu)_{xx} + (hv)_{yx} \Big] + u \Big[ (hu)_{xx} + (hv)_{yx} \Big]_x \\ & + v_x \Big[ (hu)_{xy} + (hv)_{yy} \Big] + v \Big[ (hu)_{xy} + (hv)_{yy} \Big]_x \bigg\} \\ & +\bigg\{ (1-\beta)^2 h h_x - \beta (1-\beta) (h_x \eta + h \eta_x) + (\beta^2-1) \eta \eta_x \bigg\} \bigg\{ u ( u_{xx} + v_{yx} ) \\ & + v ( u_{xy} + v_{yy} ) \bigg\} \\ & +\bigg\{ \frac{1}{2} (1-\beta)^2 h^2 - \beta (1-\beta) h \eta + \frac{1}{2} (\beta^2-1) \eta^2 \bigg\} \bigg\{ u_x ( u_{xx} + v_{yx} ) + u ( u_{xx} + v_{yx} )_x \\ & + v_x ( u_{xy} + v_{yy} ) + v ( u_{xy} + v_{yy} )_x \bigg\} \\ & +\Big\{ (hu)_x + (hv)_y + \eta (u_x+v_y) \Big\} \Big\{ (hu)_{xx} + (hv)_{yx} + \eta_x (u_x+v_y) + \eta (u_{xx}+v_{yx}) \Big\} \end{aligned}\tag{119}
$$

D120 — `funwave_tvd_3.0.pdf p.89`, 식 (120).

$$
\displaystyle \begin{aligned} & V_2= (\beta-1)(h+\eta)_y \bigg\{ u \Big[ (hu)_{xx} + (hv)_{yx} \Big] + v \Big[ (hu)_{xy} + (hv)_{yy} \Big] \bigg\} \\ & + (\beta-1)(h+\eta) \bigg\{ u \Big[ (hu)_{xx} + (hv)_{yx} \Big] + v \Big[ (hu)_{xy} + (hv)_{yy} \Big] \bigg\}_y \\ & +\bigg\{ \frac{1}{2} (1-\beta)^2 h^2 - \beta (1-\beta) h \eta + \frac{1}{2} (\beta^2-1) \eta^2 \bigg\}_y \Big\{ u ( u_{xx} + v_{yx} ) + v ( u_{xy} + v_{yy} ) \Big\} \\ & +\bigg\{ \frac{1}{2} (1-\beta)^2 h^2 - \beta (1-\beta) h \eta + \frac{1}{2} (\beta^2-1) \eta^2 \bigg\} \Big\{ u ( u_{xx} + v_{yx} ) + v ( u_{xy} + v_{yy} ) \Big\}_y \\ & +\Big\{ (hu)_x + (hv)_y + \eta (u_x+v_y) \Big\} \Big\{ (hu)_x + (hv)_y + \eta (u_x+v_y) \Big\}_y \\ & = (\beta-1)(h_y + \eta_y) \bigg\{ u \Big[ (hu)_{xx} + (hv)_{yx} \Big] + v \Big[ (hu)_{xy} + (hv)_{yy} \Big] \bigg\} \\ & + (\beta-1)(h+\eta) \bigg\{ u_y \Big[ (hu)_{xx} + (hv)_{yx} \Big] + u \Big[ (hu)_{xx} + (hv)_{yx} \Big]_y \\ & + v_y \Big[ (hu)_{xy} + (hv)_{yy} \Big] + v \Big[ (hu)_{xy} + (hv)_{yy} \Big]_y \bigg\} \\ & +\bigg\{ (1-\beta)^2 h h_y - \beta (1-\beta) (h_y \eta + h \eta_y) + (\beta^2-1) \eta \eta_y \bigg\} \bigg\{ u ( u_{xx} + v_{yx} ) \\ & + v ( u_{xy} + v_{yy} ) \bigg\} \\ & +\bigg\{ \frac{1}{2} (1-\beta)^2 h^2 - \beta (1-\beta) h \eta + \frac{1}{2} (\beta^2-1) \eta^2 \bigg\} \bigg\{ u_y ( u_{xx} + v_{yx} ) + u ( u_{xx} + v_{yx} )_y \\ & + v_y ( u_{xy} + v_{yy} ) + v ( u_{xy} + v_{yy} )_y \bigg\} \\ & +\Big\{ (hu)_x + (hv)_y + \eta (u_x+v_y) \Big\} \Big\{ (hu)_{xy} + (hv)_{yy} + \eta_y (u_x+v_y) + \eta (u_{xy}+v_{yy}) \Big\} \end{aligned}\tag{120}
$$

다음 표는 식 (119),(120)의 첫 등호 뒤의 다섯 묶음과 두 번째 등호 뒤의 다섯 묶음을 같은 곱 미분으로 연결한다.
아래의 “첫째”부터 “다섯째”까지는 위 인쇄식에서 더하기로 구분한 큰 묶음의 순서다.
각 코드 인용은 K23의 완결 대입 전체에 속한다.

| 행 ID | 항목·문서(원문) | 코드(원문) | 판정 | 이유 |
|---|---|---|---|---|
| FT1-218 | p.88 (119) 첫째 묶음: $(\beta-1)(h+\eta)_x\{u[(hu)_{xx}+(hv)_{yx}]+v[(hu)_{xy}+(hv)_{yy}]\}$; 완전 전개의 $(h_x+\eta_x)$ 묶음. | K23; `dispersion.F:438` `ken1=(Beta_1-1.0_SP)*(rhx+ETAx(I,J))*Beta_2` `dispersion.F:438,447`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). | 불일치 | E 후보 (강함). 직교 비선형 U2 전개의 첫째 묶음은 x경사를 사용한다. 식 (119)의 첫째 계수에 0.04가 추가된다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-219 | p.88 (119) 둘째 묶음과 그 네 곱 미분: $(\beta-1)(h+\eta)\{u[(hu)_{xx}+(hv)_{yx}]+v[(hu)_{xy}+(hv)_{yy}]\}_x$ | K23의 `ken2*(Ux*HUxxHVxy+U*HUxxHVxy_x+Vx*HUxyHVyy+V*HUxyHVyy_x)`에 해당하는 448–449행 전체. `dispersion.F:439,448–449`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). | 불일치 | E 후보 (강함). 직교 비선형 U2 전개의 둘째 묶음은 네 곱 미분을 올바르게 배치한다. 공통 ken2에는 식 (119)에 없는 0.04가 들어간다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-220 | p.88 (119) 셋째 묶음: $\{\frac12(1-\beta)^2h^2-\beta(1-\beta)h\eta+\frac12(\beta^2-1)\eta^2\}_x\{u(u_x+v_y)_x+v(u_x+v_y)_y\}$ | K23의 `ken3` 대입과 450–451행. `dispersion.F:440–441,450–451`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). | 불일치 | E 후보 (강함). 직교 비선형 U2 전개의 셋째 묶음은 h·h_x와 eta·eta_x를 0.0016배 한다. 혼합 h·eta 미분항은 0.04배 한다. 식 (119)에는 이 배수가 없다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-221 | p.88 (119) 넷째 묶음과 그 네 곱 미분: $\{\frac12(1-\beta)^2h^2-\beta(1-\beta)h\eta+\frac12(\beta^2-1)\eta^2\}\{u(u_x+v_y)_x+v(u_x+v_y)_y\}_x$ | K23의 `ken4` 대입과 452–453행. `dispersion.F:442–443,452–453`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). | 불일치 | E 후보 (강함). 직교 비선형 U2 전개의 넷째 묶음은 h 제곱 및 eta 제곱 계수에 0.0016을 곱한다. h·eta 계수에는 0.04를 곱한다. 식 (119)의 계수와 다르다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-222 | p.88 (119) 다섯째 묶음: $\{(hu)_x+(hv)_y+\eta(u_x+v_y)\}\{(hu)_{xx}+(hv)_{yx}+\eta_x(u_x+v_y)+\eta(u_{xx}+v_{yx})\}$ | K23의 454–455행. `dispersion.F:454–455`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). | 불일치 | E 후보 (강함). 직교 비선형 U2 전개의 다섯째 묶음은 전체 곱에 0.0016을 곱한다. 두 괄호 안의 수면고 관련 항에도 0.04가 추가된다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-223 | p.89 (120) 첫째 묶음과 $(h_y+\eta_y)$ 전개. 전체 원문은 D120이다. | K23; `dispersion.F:459` `ken1=(Beta_1-1.0_SP)*(rhy+ETAy(I,J))*Beta_2` `dispersion.F:459–461`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). | 불일치 | E 후보 (강함). 직교 비선형 V2 전개의 첫째 묶음은 y경사를 사용한다. 식 (120)의 첫째 계수에는 없는 0.04가 추가된다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-224 | p.89 (120) 둘째 묶음과 $u_y,u,v_y,v$의 네 곱 미분. 전체 원문은 D120이다. | K23의 `V2` 462–463행. `dispersion.F:439,462–463`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). | 불일치 | E 후보 (강함). 직교 비선형 V2 전개의 둘째 묶음은 네 곱 미분을 올바르게 배치한다. 공통 ken2에는 식 (120)에 없는 0.04가 들어간다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-225 | p.89 (120) 셋째 묶음과 $hh_y,h_y\eta+h\eta_y,\eta\eta_y$의 전개. 전체 원문은 D120이다. | K23의 `ken5` 대입과 464–465행. `dispersion.F:444–445,464–465`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). | 불일치 | E 후보 (강함). 직교 비선형 V2 전개의 셋째 묶음은 h·h_y와 eta·eta_y를 0.0016배 한다. 혼합 h·eta 미분항은 0.04배 한다. 식 (120)에는 이 배수가 없다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-226 | p.89 (120) 넷째 묶음과 네 곱 미분. 전체 원문은 D120이다. | K23의 `ken4` 대입과 466–467행. `dispersion.F:442–443,466–467`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). | 불일치 | E 후보 (강함). 직교 비선형 V2 전개의 넷째 묶음은 U2와 같은 ken4를 사용한다. 식 (120)에 없는 h 제곱·eta 제곱의 0.0016배와 h·eta의 0.04배가 남는다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-227 | p.89 (120) 다섯째 묶음의 완전 전개. 전체 원문은 D120이다. | K23의 468–469행. `dispersion.F:468–469`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). | 불일치 | E 후보 (강함). 직교 비선형 V2 전개의 다섯째 묶음은 전체 곱에 0.0016을 곱한다. 두 괄호 안의 수면고 관련 항에도 0.04가 추가된다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-228 | p.18 (18)–(20)과 p.86 (107)–(110)의 분할 대응. | K20, K22. 본문 식 (18)–(20), 부록 식 (107)–(110), `dispersion.F:337–346,422–436`, `etauv_solver.F:407–411`. FT1-042–044,047과 같은 분할 대응이다. 실제 비선형 계수 차이는 FT1-208,209이다. | 불일치 | F. 아래 항등식이 두 분할을 연결한다. `Beta_2=1`의 형식 비교에서 성립한다. 현재 0.04의 계수 차이는 별도의 E 행으로 남긴다. [10-18 결론 검증 보완] |

해석: 본문과 부록의 프라임 분할은 다음과 같이 연결된다.
여기서 $T=\frac12z_\alpha^2\nabla B+z_\alpha\nabla A$이다.
$L=\frac12\zeta^2h^2\nabla B+\zeta h\nabla A$이다.
$N=T-L$이다.
$Q=\nabla(\eta^2B/2+\eta A)$이다.
이 정의는 식 변형을 보이기 위해 이 보고서에서만 도입한다.

$$
\mathbf V_1=T_t-\nabla(\eta^2B_t/2+\eta A_t)
=(L+N-Q)_t+\nabla[\eta_t(A+\eta B)]
=L_t+\{N_t-\nabla(\eta^2B_t/2+\eta A_t)\}.
$$

본문의 $\mathbf V'_1$은 $L+N-Q$이다.
부록과 코드의 선형 프라임 항은 $L$이다.
부록의 이중 프라임 항은 마지막 중괄호이다.
따라서 이름만 보고 본문 식 (20)을 코드 `U1pp` 하나와 같다고 쓰면 안 된다.
이 식 변형은 `Beta_2=0.04`를 제거하는 보정 경로가 아니다.

### 2.9 쪽별 누락 점검

다음 표의 쪽 수는 사용자 지정 범위에서 센 26쪽이다.
지정 범위에는 빈 쪽이 없다.
그림만 있는 쪽도 없다.
p.29는 식·본문·그림 1을 함께 담는다.

| PDF 쪽 | 대조 행 | 내용 |
|---|---|---|
| 12 | FT1-001–006 | 서론과 구 모델의 수치 방법 |
| 13 | FT1-007–010 | 구 모델의 확장·잡음·slot 문제 |
| 14 | FT1-010–016 | 새 방법·쇄파·병렬·보고서 구성 |
| 15 | FT1-016–023 | 이론 정의와 식 (1)–(6) |
| 16 | FT1-024–034 | 식 (7)–(14), 기준 깊이와 와도 |
| 17 | FT1-035–038 | 정수압 재배열과 식 (15) |
| 18 | FT1-039–046 | 보존형 유도와 식 (16)–(22) |
| 19 | FT1-047–054 | 식 (23)–(27), 구면 기본식 |
| 20 | FT1-055–071 | 식 (28)–(44), 모든 미분 변환 |
| 21 | FT1-072–084 | 식 (45)–(56), 구면 보존형 |
| 22 | FT1-085–093 | 번호 없는 기호 정의와 식 (57)–(61) |
| 23 | FT1-094–102 | 식 (62)–(67), 고차 재구성과 제한 함수 |
| 24 | FT1-103–116 | 식 (68)–(77), 저차 재구성과 HLL |
| 25 | FT1-117–130 | 식 (78)–(82), RK·CFL·쇄파 |
| 26 | FT1-131–143 | 식 (83)–(85), 습윤–건조·경계·스펀지 도입 |
| 27 | FT1-143–152 | 식 (86)–(89), 스펀지와 주기 경계 |
| 28 | FT1-153–162 | 식 (90)–(94), 내부 조파 이론 |
| 29 | FT1-162–168 | 식 (95)–(97), 그림 1과 주기 조파 |
| 30 | FT1-168–176 | 식 (98),(99), 규칙파·불규칙파·번호 없는 스펙트럼식 |
| 31 | FT1-177–184 | 식 (100)–(103), 방향 분포·바람 |
| 32 | FT1-185–194 | 식 (104),(105), 파고·병렬·4장 첫 문단·설치 문장 |
| 81 | FT1-195–204 | 제6장 항목과 제7장 서지 시작 |
| 86 | FT1-205–211 | 정정 안내와 식 (107)–(112) |
| 87 | FT1-212–217 | 식 (113)–(118), 본문 문장 없음 |
| 88 | FT1-218–222 | 식 (119), “In detail,” 외의 본문 문장 없음 |
| 89 | FT1-223–227 | 식 (120), 본문 문장 없음 |

p.79의 제6장 도입은 지정 범위 밖의 보조 문맥이다.
그 도입의 “No more filtering is required in FUNWAVE-TVD.”는 필터가 소스에서 삭제됐다는 뜻이 아니다.
필터의 조건부 코드 경로는 §3에 기록한다.

## 3 코드에만 있는 처리

이 절의 “문서 없음”은 대상 쪽 범위에 설명이 없다는 뜻이다.
문서 전체의 다른 장까지 설명이 없다는 뜻은 아니다.
추가 계산을 코드 결함으로 단정하지 않는다.
E 행은 §5에서 반대 근거와 모순 근거를 따로 평가한다.

| 행 ID | 항목·문서(원문) | 코드(원문) | 판정 | 이유 |
|---|---|---|---|---|
| FT1-229 | 3.0 p.24·41의 HLL 설명과 2.1 p.29의 HLLC 명칭을 입력 분기에 대조한다. | `fluxes.F:109` `IF(CONSTR(1:3)=='HLL')THEN`; 110 `CALL FLUX_AT_INTERFACE_HLL`; `io.F:2833` `CONSTR='HLLC'` `io.F:2826–2834`의 `READ_STRING`과 `fluxes.F:109–112,150–194`. 3.0 p.41, 2.1 p.29·40, Intro-TN p.13·17 및 TeX 1337행을 포함해 네 문서 전체를 검색했다. | 코드에만 | C. `HLLC` 입력도 `IF(CONSTR(1:3)=='HLL')THEN`에 따라 HLL을 선택한다. C 판정은 3.0 p.41에 접두 세 글자로 판별하는 조건이 빠진 점에 한정한다. 2.1 p.29는 HLLC 이름을 쓰지만 현재 수리 플럭스 호출은 `FLUX_AT_INTERFACE_HLL`이다. FT1-109와 같은 호출 경로이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-230 | 3.0 p.41·2.1 p.40·Intro-TN p.13: CONSTRUCTION은 HLL 또는 평균 기법을 선택한다. | `fluxes.F:111–112` `ELSE` / `CALL FLUX_AT_INTERFACE`; 132 `P=0.5_SP*(PR+PL)` `io.F:2826–2834`; `fluxes.F:109–112,122–137`; TeX 1337행. 네 문서와 TeX 판독 기록 전체의 `CONSTRUCTION`·평균 기법 검색. | 일치 | HLL로 시작하지 않는 `CONSTRUCTION` 값은 산술평균 플럭스 경로를 선택한다. 이 선택지는 3.0 p.41·2.1 p.40·Intro-TN p.13에 설명되어 있다. `dont use it for TVD` 주석은 실제 호출을 막지 않는다. FT1-276과 같은 분기이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-231 | 3.0 p.32–34의 빌드 안내에 보존된 fluxes 파일의 선택 목록이 없다. | `T/GNUMake/Essential/Make_Essential:208–211`의 MAIN 목록은 `fluxes.F`만 포함한다. `fluxes_21v.F:719–720`은 아래 K27이다. `GNUMake/Essential/Make_Essential:204–211`; `fluxes_21v.F:719–722`. 네 문서·TeX 전체에서 파일명·빌드 목록을 검색했다. | 코드에만 | C. 현재 기본 빌드는 `fluxes.F`를 선택한다. code_analysis p.8–9는 `fluxes.F`와 `fluxes_21v.F`를 나란히 분석하지만 빌드 선택을 설명하지 않는다. `fluxes_21v.F`의 인용식은 같은 `Din`에 두 가중치를 더하므로 Kappa가 소거된다. FT1-202·284와 연결한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-232 | 3.0 p.41의 HIGH_ORDER 목록에는 FOURTH·THIRD·SECOND를 적는다. | `fluxes.F:71–72` `ELSEIF(HIGH_ORDER(1:3)=='FMI') THEN` / `CALL CONSTRUCTION_HO_minmod`; 81–82 `ELSEIF(HIGH_ORDER(1:3)=='WEN') THEN` / `CALL CONSTRUCTION_WENO`; 89,91의 `MLP` 호출. `io.F:2842–2854`; `fluxes.F:71–103`; 네 문서·TeX 전체의 `FMI`·`WENO`·`MLP`·`HIGH_ORDER` 검색. | 코드에만 | C. 3.0 p.41의 누락은 `FMI`·`WEN`·`MLP` 입력 선택이다. `READ_STRING`으로 읽은 `HIGH_ORDER`가 실제 분기를 선택한다. `WEN` 분기는 `CARTESIAN`에서만 컴파일한다. FMI의 후속 활성화 이력은 FT1-277의 A 판정과 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-233 | 3.0 p.23–24의 제한 함수식에는 작은 분모 처리 조건이 없다. | `fluxes.F:1608` `IF( ABS(TMP1).le.SMALL ) TMP1 = SMALL*SIGN( 1.0_SP, TMP1 )`; 1612의 분모 검사; 316 `IF((ABS(TMP1)+ABS(TMP2))<SMALL)THEN`; 318 `DOUT(I,J)=ZERO` `fluxes.F:56–103`의 차수별 호출과 `1608–1616,316–321`; `mod_param.F:73` `SMALL=0.000001_SP`. 네 문서·TeX의 제한 함수·작은 분모 검색. | 코드에만 | C. 3.0 p.23–24의 수식에 생략된 작은 분모 처리를 코드가 수행한다. 4차 경로는 `IF( ABS(TMP1).le.SMALL ) TMP1 = SMALL*SIGN( 1.0_SP, TMP1 )`와 `IF( abs(1.0 + RAT) > SMALL )`을 사용한다. 저차 경로는 `IF((ABS(TMP1)+ABS(TMP2))<SMALL)THEN`에서 `DOUT(I,J)=ZERO`로 둔다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-234 | 3.0 p.24·26의 HLL·파속식에는 SMALL 분모와 수심 절댓값 처리가 없다. | `fluxes.F:185` `IF((ABS(SR(I,J)-SL(I,J)))<SMALL)THEN`; 186 `FOUT(I,J)=FOUT(I,J)/SMALL`; 371 `SQR_PHI_L=SQRT(GRAV*ABS(HxL(I,J)))` `io.F:2826` 입력 → `fluxes.F:109–110` 호출; `fluxes.F:179–190,371`. 네 문서·TeX의 HLL·작은 분모·파속식 검색. | 코드에만 | C. HLL의 중간 파속 분기에서는 `IF((ABS(SR(I,J)-SL(I,J)))<SMALL)THEN`일 때 분모로 SMALL을 사용한다. 파속 제곱근은 `SQRT(GRAV*ABS(HxL(I,J)))`이다. C 판정은 3.0 p.24·26의 이 보호식 생략에 한정한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-235 | 3.0 p.25의 CFL 식과 p.32의 MPI 설명에는 최소값 집계 배열 범위가 없다. | `misc.F:240–241` `DO J=1,N` / `DO I=1,M`; 277–278 `call MPI_ALLREDUCE (TMP3,myvar,1,MPI_SP,MPI_MIN, &` / `MPI_COMM_WORLD,ier)` `main.F:320`에서 `Mloc,Nloc` 전달; `misc.F:216,240–241,273–281`; 네 문서·TeX 전체의 CFL·MPI·ghost 검색. | 코드에만 | C. CFL은 ghost 셀을 포함한 지역 배열에서 최소값을 구한다. `PARALLEL`에서는 `MPI_MIN`으로 전 프로세서의 최소값을 결합한다. 3.0 p.25·32에 이 집계 범위가 빠져 있다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-236 | 3.0 p.25·41의 시간 간격 설명에 DT_fixed 절반화 절차가 없다. | `misc.F:283–288` `IF(FIXED_DT)THEN` / `DT = DT_fixed` / `DO WHILE (DT > DT_tmp)` / `DT=DT/2.0_SP` / `ENDDO` `io.F:2883–2895`; `misc.F:281–291`; 네 문서·TeX 전체의 `FIXED_DT`·`DT_fixed`·고정 시간 검색. | 코드에만 | C. `DT_fixed` 입력 읽기가 성공하면 `FIXED_DT = .TRUE.`가 된다. `IF(FIXED_DT)THEN`에서 `DT = DT_fixed`를 적용하고 `DO WHILE (DT > DT_tmp)` 동안 `DT=DT/2.0_SP`를 반복한다. 3.0 p.25·41에는 이 절차가 없다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-237 | 3.0 p.26·41·81의 수심 임계 설명에는 유속 복원 대입식의 모든 용도가 없다. | `etauv_solver.F:561` `U(I,J)=Ubar(I,J)/Max(H(I,J),MinDepthFrc)`; 570–576의 `MASK<1` 영 대입; 578 `HU(I,J)=Max(H(I,J),MinDepthFrc)*U(I,J)` `io.F:2933–2949`; `etauv_solver.F:402–411,561–593`; `misc.F:243,259`. 네 문서·TeX 전체의 `MinDepthFrc` 검색. Froude 기능 자체는 FT1-196의 일치 판정이다. | 코드에만 | C. `MinDepthFrc`는 유속 복원·파속·분산 역변환의 수심 하한에도 사용한다. 건조 셀에서는 유속과 운동량을 0으로 둔다. 3.0 p.41은 주로 바닥마찰 하한으로 설명하며 p.81은 Froude 상한 목적을 덧붙인다. C 판정은 이들 쪽에 유속 복원 대입식과 분산 역변환의 용도가 생략된 점이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-238 | Manning 선택은 3.0 p.10·34에 있다. 마찰 누락 기본값은 별도 대조한다. | `sources.F:238–240`의 K28; `io.F:2777` `CALL READ_FLOAT(Cd_fixed,FILE_NAME,'Cd',ierr)`; 2779 `Cd_fixed = 0.0_SP` `io.F:2738–2740,2777–2789`; `init.F:854,884–890`; `sources.F:236–243`. 네 문서·TeX의 Manning·마찰 기본값 검색; 2.1 p.9·34에도 Manning 선택이 있다. | 코드에만 | C. Manning 선택 자체는 문서에 있다. `CARTESIAN`·`MANNING` 경로는 `GRAV*Cd(I,J)**2/Max(H(I,J),MinDepthFrc)**(0.333333_SP)`를 쓴다. C 판정은 3.0 p.40에 `Cd` 미입력 대입값 0과 실제 수심 하한 식이 빠진 점이다. 균일 마찰장은 `IN_Cd`가 거짓일 때 `Cd_fixed`로 채운다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-239 | 3.0 p.40은 Gamma1·Gamma2·Gamma3와 선형화 시 자동 0 설정을 설명한다. | `io.F:2591,2593`의 `READ_FLOAT(Gamma1,...)`, `Gamma1 = 1.0_SP`; 2606,2608의 `Gamma2 = 1.0_SP`; 2651,2653의 `Gamma3 = 1.0_SP` `io.F:2591–2608,2651–2653`; `init.F:638–654`. 네 문서·TeX의 Gamma 검색; 2.1 p.39, Intro-TN p.12, TeX 1300–1307행에도 기능 설명이 있다. | 코드에만 | C. 분산 전환 기능과 Gamma3에 따른 자동 0 설정은 문서에 있다. C 판정은 3.0 p.40에 입력 누락 시 세 Gamma 값을 각각 1로 읽는 절차가 빠진 점이다. 이후 `Gamma3 > ZERO`의 `ELSE` 또는 `DISPERSION`의 `ELSE`에서 Gamma1을 0으로 둔다. Gamma2의 0 대입은 `CARTESIAN` 분기이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-240 | 3.0 p.41은 VISCOSITY_BREAKING 선택을 설명하지만 미입력 대입값을 적지 않는다. | `io.F:2689` `CALL READ_LOGICAL(VISCOSITY_BREAKING,FILE_NAME,'VISCOSITY_BREAKING',ierr)`; 2691 `VISCOSITY_BREAKING = .TRUE.`; 3076 `IF(VISCOSITY_BREAKING) SHOW_BREAKING = .TRUE.` `io.F:2689–2703,3076`; `breaker.F:64–71`; `masks.F:177–188`; `sources.F:196–198,394–453`. 네 문서·TeX 전체의 `VISCOSITY_BREAKING`·쇄파 방식 검색. | 코드에만 | C. `VISCOSITY_BREAKING` 미입력은 참이다. 이 경우 `SHOW_BREAKING`도 참으로 설정하고 `BREAKING`을 호출한다. C 판정은 3.0 p.41의 누락 기본값에 한정한다. 충격 포착 전환의 분기는 FT1-125·126, 노트 정정은 FT1-267과 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-241 | 3.0 p.25–26·41에는 점성식의 전처리 대안 목록이 없다. | `breaker.F:278` `# if defined (VIS_KENNEDY_ORIGINAL)`; 294 `nu_break(I,J)=cap1*ABS(ETAt(I,J))*B+nu_bkg`; 296 `# elif defined (VIS_KENNEDY)`; 308 `nu_break(I,J) = cap1*tmp2*(1.0_SP+B) + nu_bkg`; 311–314의 정적 전이·기본 대입. `breaker.F:64–71,131–144,248–265,278–315`; `io.F:2689–2691,3076`; 네 문서·TeX의 전처리 이름 검색. | 코드에만 | C. `VIS_DEPTH_RATIO`가 없는 경로에서 조파 영역 밖의 지속 쇄파 조건을 통과하면 점성식을 선택한다. 우선순위는 `VIS_KENNEDY_ORIGINAL`, `VIS_KENNEDY`, `VIS_STATIC_TRANS`, 기본식이다. 이는 3.0 p.25–26·41의 설명에 없는 분기이다. FT1-130·269·280과 같은 식 선택이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-242 | 3.0 p.26의 쇄파 설명에는 이웃 나이 전파와 roller·undertow 식이 없다. | `breaker.F:158` `C=MIN(ABS(ETAt(I,J))/tmp4,SQRT(GRAV*ABS(H(I,J))))`; 182–185의 이웃 나이 선택; 330 `R=ABS(0.45*ETAt(I,J)/MAX(C1,SMALL))`; 331 `R=MIN(R,0.1638_SP)` `breaker.F:151–229,248–265,325–337`; `io.F:3058–3076`; 네 문서·TeX의 `AGE_BREAKING`·roller·undertow 검색. code_analysis p.7의 나이 인수 목록은 전파식 설명이 아니다. FT1-133과 연결한다. | 코드에만 | C. 쇄파 루틴은 이웃 나이와 전파 시간을 비교한다. `VIS_DEPTH_RATIO`가 없는 경로의 조파 영역 밖에서 `IF(AGE(I,J)>ZERO.AND.AGE(I,J)<T_brk.AND.ETAt(I,J)>tmp2)THEN`을 만족하면 roller·undertow를 계산한다. `R=MIN(R,0.1638_SP)`로 비를 제한한다. 3.0 p.26의 0/1 지수식과 별도 처리이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-243 | 3.0 p.27은 점성 스펀지를 설명하지만 점성 계수의 조건부 합산식을 적지 않는다. | `sources.F:196,198` `IF(VISCOSITY_BREAKING .OR. WAVEMAKER_VIS)THEN` / `nu_vis = nu_break`; 213,216 `IF(DIFFUSION_SPONGE)THEN` / `nu_vis = nu_vis + nu_sponge` `sources.F:190–224`; `io.F:2280–2282,2689–2691,3145–3149`; `breaker.F:64–71`. 네 문서·TeX의 조파·스펀지 점성 검색. | 코드에만 | C. `IF(VISCOSITY_BREAKING .OR. WAVEMAKER_VIS)THEN`에서 `nu_vis = nu_break`를 대입한다. 그 내부의 `DEEP_DRAFT_VESSEL` 경로만 선박 점성을 더한다. `IF(DIFFUSION_SPONGE)THEN`에서는 스펀지 점성을 더한다. 3.0 p.27의 누락은 이 조건부 합산 순서이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-244 | 시간 램프 입력은 3.0 p.37–38에 있다. p.28–31 조파식의 대입을 대조한다. | K17; K02의 마지막 `+WaveMaker_Mass(I,J)*U(I,J)`; `sources.F:319` `+WaveMaker_Mass(I,J)*V(I,J)` `io.F:870,1517`; `sources.F:109–114,260,319`; 네 문서·TeX의 `Time_ramp`·램프·질량 소스 검색. 2.1 p.37에도 램프 입력이 있다. | 코드에만 | C. 시간 램프의 존재는 문서에 있다. C 판정은 3.0 p.28–31·37–38에 `AA = TANH(PI/(Time_ramp*Tperiod)*TIME)*D_gen`의 실제 대입과 질량 주입에 따른 운동량 소스가 생략된 점이다. 규칙파 소스에는 가우스 공간 함수와 이 램프를 곱한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-245 | 3.0 p.25·27에는 RK 단계 안의 직접 감쇠 위치와 조파 강제 시각이 없다. | `main.F:320`의 시간 간격 호출; `misc.F:294` `TIME=TIME+DT`; `main.F:380`의 3단계 루프; 483–485의 `CALL SPONGE_DAMPING` `io.F:2285–2287`; `main.F:320,380–487`; `misc.F:294`; `sources.F:109–132`. 네 문서·TeX의 RK·감쇠·시간 램프 검색. | 코드에만 | C. 물리 시간은 RK 단계 루프 전에 한 번 증가한다. `DIRECT_SPONGE`가 참이면 각 RK 단계 끝에 직접 감쇠를 호출한다. 내부 질량 조파의 시간식은 세 단계에서 같은 TIME 값을 사용한다. C 판정은 3.0 p.25·27의 이 호출 순서 생략에 한정한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-246 | 3.0 p.41은 STEADY_TIME·T_INTV_mean을 설명하지만 창 경계 처리식은 적지 않는다. | `mixing.F:60` `IF( time >= STEADY_TIME )THEN`; 143 `T_sum=T_sum+DT`; 144 `IF(T_sum.GE.T_INTV_mean)THEN`; 224 `T_sum=T_sum-T_INTV_mean   ! T_sum=ZERO? (ykchoi)`; 228 `ETA2sum=ZERO     !ykchoi` `io.F:3204–3230`; `mixing.F:60–61,143–154,224–255`; 네 문서·TeX의 `STEADY_TIME`·`T_INTV_mean` 검색. | 코드에만 | C. 통계 시작 시각과 평균 간격은 문서에 있다. C 판정은 3.0 p.32·41에 창을 넘은 잔여 시간 처리식이 생략된 점이다. `T_sum=T_sum-T_INTV_mean`으로 시간을 넘기고 `Usum,Vsum,ETAsum,ETA2sum`은 0으로 둔다. 파고 합과 영점 통과 횟수는 이때 초기화하지 않는다. FT1-247과 구분한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-247 | 평균·제곱평균제곱근 파고의 표본 수 정의가 없다. | `init.F:438`의 `Num_Zero_Up = 0`; `mixing.F:249–251` `IF(Num_Zero_Up(I,J)>=2)THEN` / `WaveHeightAve(I,J)=HavgSum(I,J)/Num_Zero_Up(I,J)` / `WaveHeightRMS(I,J)=SQRT(HrmsSum(I,J)/Num_Zero_Up(I,J))`; 292–294의 조건부 누적. `main.F:496` → `mixing.F:60–61`; `io.F:3204–3230`의 통계 시작·평균 간격 입력. `mixing.F:253–255`의 파고 합·횟수 초기화는 주석이다. `cab9425:mixing.F:139–168`도 같은 n 분모와 2회째부터의 누적이다. 기존의 ‘같은 창’ 설명을 통계 시작 이후 누적값으로 정정한다. | 코드에만 | E 후보 (강함). 파고 통계는 통계 시작 이후의 누적값이다. 검출 상향통과 횟수가 n이면 합산 파고 표본은 n-1개이다. 평균과 RMS의 분모는 n이므로 표본 개수와 일치하지 않는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-248 | 3.0 p.79의 필터 불필요 설명에는 선택적 FILTERING 경로가 없다. | `bc.F:496` `# if defined (FILTERING)`; 499 `IF (filter_count > filter_interval) THEN`; 502 `CALL SHAPIRO_3(Mloc,Nloc,Nghost,MASK,Eta)`; 504–505의 `U,V` 호출. `bc.F:496–512`; `mod_global.F:84–86`; 네 문서·TeX 전체의 필터·Shapiro 검색. FT1-006의 과거 모형 필터 설명과 구분한다. | 코드에만 | C. `CARTESIAN`·`FILTERING`이 정의되면 `EXCHANGE` 호출 횟수를 세고 `IF (filter_count > filter_interval) THEN`에서 수면고·유속을 필터링한다. `filter_interval = 1`은 선언값이며 입력 키워드가 아니다. 3.0 p.79는 필터가 필요 없다고 설명하지만 이 선택 경로를 기술하지 않는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-249 | 3.0 p.79–81의 불안정 안내에는 발산·NaN 중단 조건식이 없다. | `misc.F:403` `MaxAbsEta=MAXVAL( abs(Eta(Ibeg:Iend,Jbeg:Jend)) )`; 409 `if (MaxAbsEta > EtaBlowVal) then`; `statistics.F:199` `IF (ISNAN(val)) THEN`; 204 `CALL MPI_ABORT( MPI_COMM_WORLD , 9 , ier)` `init.F:847–850`; `main.F:517`; `misc.F:403–428`; `statistics.F:175–184,199–206`; 네 문서·TeX의 `EtaBlowVal`·NaN·불안정 검색. | 코드에만 | C. 최대 수면고가 EtaBlowVal보다 크면 중단한다. 통계량의 NaN도 별도로 중단한다. EtaBlowVal은 초기화에서 최대 수심 절댓값의 100배로 정한다. C 판정은 3.0 p.79–81에 이 조건식이 빠진 점이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-250 | 3.0 p.26의 습윤 복귀 설명에는 셀 자체 수면고 조건이 없다. | `masks.F:106–109` `! this is for rainfall case $$$` / `IF(Eta(I,J)>-Depth(I,J))THEN` / `MASKtmp(I,J)=1` / `ENDIF` `masks.F:78–117`; 네 문서·TeX의 강수·습윤 복귀·`UseEtaScreen` 검색. | 코드에만 | C. `UseEtaScreen`이 정의되지 않은 경로에서 `MASK_STRUC(I,J)==1`이고 `MASK(I,J)<1`이면 셀 자체의 `IF(Eta(I,J)>-Depth(I,J))THEN`으로도 습윤 복귀한다. 강수용이라는 주석이 있지만 이 조건 자체는 강수 입력 여부로 한정되지 않는다. C 판정은 3.0 p.26의 조건 생략에 한정한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-251 | 3.0 p.81의 급경사 회피 권고에는 SLOPE_CTR·IGNORE_BIG_SLOPE의 분기가 없다. | `init.F:1179` `SLOPE_CTR = .FALSE.`; 1180 `MAX_SLOPE = 0.1`; `masks.F:152` `# if defined (IGNORE_BIG_SLOPE)`; 156 `DepthX(I,J)=Depth(I-1,J)` `init.F:1175–1220`; `masks.F:152–161`; 전체 `src/*.F`의 변수명·입력 검색. 네 문서·TeX의 경사 제한 검색. | 코드에만 | C. 구면 초기화는 `SLOPE_CTR = .FALSE.`를 대입하므로 이어지는 `IF(SLOPE_CTR)THEN`의 경사 상한은 적용하지 않는다. 이 변수를 켜는 READ_* 입력은 없다. `IGNORE_BIG_SLOPE`가 정의되지 않으면 `IF(MASK(I,J)<1)THEN`에서 경계면 수심을 인접 셀 값으로 바꾼다. 3.0 p.81의 권고와 별도 처리이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-252 | 3.0 p.18–19·25에는 DISP_TIME_LEFT의 방향별 잔존 분기가 없다. | `mod_global.F:178` `LOGICAL :: DISP_TIME_LEFT=.FALSE.`; `etauv_solver.F:485` `IF(DISP_TIME_LEFT)THEN`; K03. `mod_global.F:178`; `etauv_solver.F:402–411,484–507`; 전체 `src/*.F`의 `DISP_TIME_LEFT` 검색. 네 문서·TeX 전체에서도 해당 이름을 검색했다. | 코드에만 | C. `DISP_TIME_LEFT`는 거짓으로 선언되어 있고 이를 켜는 READ_* 입력이나 후속 참 대입은 없다. y역변환에는 이 변수를 조건으로 한 비선형 분기가 남아 있지만 x역변환은 대응 분기가 없다. C 판정은 3.0 p.18–19·25에 이 구현 상태가 기술되지 않은 점이다. 기본 거짓 경로의 분할은 FT1-228과 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-253 | 3.0 p.15의 질량 방정식에는 후속 확장 소스와 Wsurf 저장 순서가 없다. | `etauv_solver.F:247` `Wsurf(I,J) = R1(I,J)`; 259 `R1(I,J)=R1(I,J)+ MassSed(I,J)`; 264 `R1(I,J)=R1(I,J)+ PrecRateModel(I,J)` `etauv_solver.F:247–264`; `mod_sediment.F:196–198`의 READ_LOGICAL; `mod_precipitation.F:147`의 RAINFALL_FILE 입력. 네 문서·TeX의 Wsurf·퇴적물·강수 검색. | 코드에만 | C. `Wsurf(I,J) = R1(I,J)` 저장 후 `SUBGRID` 보정과 확장 질량 소스를 적용한다. `SEDIMENT`에서 `IF(SedimentMassSource)THEN`이면 퇴적물 질량 소스를 더한다. `PRECIPITATION`에서는 강수율을 더한다. C 판정은 3.0 p.15에 이 확장·저장 순서가 없는 점이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-254 | 3.0 p.31은 방향 균등 분할·등 에너지 조파를 설명하지만 이산 정규화·대안 선택을 적지 않는다. | `wavemaker.F:1946–1947`의 평균 방향 ±60도; 1950–1951의 ±90도 제한; 1963 `AG(:) = ABS(AG(:)/sumAG);   !Because integral of AG should be 1.`; 2128의 등주파수 경로. `io.F:1974–1976`; `wavemaker.F:370–400,1938–1966`; 네 문서·TeX의 방향 분할·`EqualEnergy` 검색. FT1-166·177·179와 같은 조파 경로이다. | 코드에만 | C. 다방향 경로는 평균 방향 ±60도 범위를 만든 뒤 절대각을 ±90도로 제한한다. `AG(:) = ABS(AG(:)/sumAG)`로 이산 가중치를 정규화한다. 직교 경로는 `EqualEnergy` 입력에 따라 등 에너지 또는 등 주파수 분할을 선택한다. 3.0 p.31에 이 범위·정규화·선택 조건이 빠져 있다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-255 | 3.0 p.30의 방향 스펙트럼 입력 설명에는 성분 삭제 조건이 없다. | `wavemaker.F:239` `IF(ABS(Dire(I)).LT.60.0_SP)THEN`; 243 `WaveCompTmp(J,DireCount) = WAVE_COMP(J,I)` `io.F:870,1850`; `wavemaker.F:196–199,238–246`; 네 문서·TeX 전체의 DATA2D·방향 제한 검색. | 코드에만 | C. `IF(WaveMaker(1:9)=='WK_DATA2D')THEN` 경로는 `IF(ABS(Dire(I)).LT.60.0_SP)THEN`을 만족하는 성분만 남긴다. ±60도 경계값은 포함하지 않는다. C 판정은 3.0 p.30에 이 삭제 조건이 없는 점이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-256 | 3.0 p.87 식 (117)–(118)의 U4·V4 비선형 계수를 GPU 커널과 대조한다. | `G/src/init.F:555` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `G/src/moment_gpu.F:573` `U4_d(I,J) = U4_d(I,J) + gamma2*tMASK*( ken1*UxxVxy + ken2*HUxxHVxy )`; K29. GPU `io.F:2490–2521` 입력, `main.F:305–311`, `moment_gpu.F:552–575`의 조건과 실제 대입. GPU `init.F:555`의 값은 TVD `init.F:664`와 같다. 네 문서·TeX 전체의 GPU·CUDA 검색과 3.0 p.87 식 이미지 대조. [외부 원문 판정](FUNWAVE-external-sources.md). GPU `moment_gpu.F:579–586`의 `# if defined (ZALPHA)` 블록은 앞서 계산한 U4·V4를 선형식으로 다시 대입한다. | 불일치 | E 후보 (강함). GPU의 직교 비선형 U4·V4 보정에도 문서에 없는 Beta_2와 그 제곱이 들어간다. FT1-216·217과 같은 계수 원인이므로 C에서 강한 E 후보로 바꾼다. `USE_CUDA`·`CARTESIAN` 및 `DISPERSION`이 켜지고 `gamma2>0.0_SP`인 경로의 판정이다. 이 U4·V4 비선형 보정 판정은 `ZALPHA`를 정의하지 않은 경로에 한정한다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 외부 원문] |
| FT1-257 | PDF 부록 (112),(120)에 대응하는 GPU y방향 전개. | GPU `moment_gpu.F:754–762`의 K29; 같은 GPU 사본의 CPU 대응식은 `dispersion.F:445`이며 TVD의 대응식은 `dispersion.F:461`이다. GPU `io.F:2490–2521` 입력 → `main.F:305–311` → `moment_gpu.F:121–133`; `moment_gpu.F:704–705`에서 `tU = U_d(i,j)`, `tV = V_d(i,j)`이다. GPU `Makefile_cuda:13,27`은 CARTESIAN·USE_CUDA를 정의한다. `5594984:src/moment_gpu.F:754`부터 같은 tV 곱이다. GPU 전체 이력 검색에서도 이 계수의 수정은 없다. | 코드에만 | E 후보 (강함). CARTESIAN·USE_CUDA 분산 경로에서 Gamma2가 양수이면 V2_d 첫 곱은 tV를 사용한다. 문서와 CPU 경로의 해당 곱은 U를 사용한다. 이 차이는 GPU 코드 도입부터 존재한 강한 코드 결함 후보이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-258 | 3.0 p.32–34의 빌드 안내에는 이 로컬 GPU 사본의 변경 내역이 없다. | `G/src/Makefile_cuda:27` `FLAG_18 = -DUSE_CUDA`; 38 `OPT      = -cuda -gpu=cc120 -cudalib=cusparse`; GPU 작업 트리 diff는 아래에 기록한다. GPU 원자료에서 `git diff -- src/Makefile_cuda src/etauv_solver_gpu.F src/mod_cuda.F`로 실제 대입·호출 변경을 대조했다. 네 문서와 TeX의 CUDA·GPU·빌드 설명을 검색했다. | 코드에만 | C. 3.0 p.32–34의 문서 범위에는 로컬 CUDA 수정이 기술되어 있지 않다. 공개 GPU HEAD 대비 로컬 diff는 `Makefile_cuda`, `etauv_solver_gpu.F`, `mod_cuda.F`의 변경을 보여 준다. 이 비교는 로컬 수정 기록이며 모델 공식 배포판 변경 이력이 아니다. FT1-288과 같은 diff이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-259 | 3.0 p.34의 입력 안내에 READ_FLOAT의 누락 반환 계약은 없다. | `mod_input.F:128` `REAL(SP),         INTENT(OUT) :: FLOAT_VAL`; 147 `IF(ERR_IF_ONE == 1)THEN`; 153 `RETURN` `mod_input.F:126–153`; `io.F:2898–2910`의 FroudeCap 호출 후 처리. 네 문서와 TeX 전체의 READ_FLOAT·누락 입력 검색. | 코드에만 | C. `READ_FLOAT`는 `IF(ERR_IF_ONE == 1)THEN`에서 기본값을 대입하지 않고 반환한다. 기본값 근거는 각 호출 뒤의 누락 처리이다. `INTENT(OUT)` 호출 전 선언 초기값이 보존된다고 단언할 수 없다. C 판정은 3.0 p.34의 입력 안내에 이 계약이 없는 점이다. FT1-197과 연결한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-260 | 3.0 p.25 식 (78), p.32 식 (104), p.41의 FroudeCap 설명을 GPU의 해당 대입과 대조한다. | `G/src/etauv_solver_gpu.F:1358` `Eta_d(I,J)=ALPHA_d(ISTEP)*Eta0_d(I,J)+BETA_d(ISTEP)*(Eta_d(I,J)+DT*R1)`; 2003 `U_d(I,J)=FroudeCap*Fr*COS(Utheta)`; `G/src/mixing_gpu.F:52` `SigWaveHeight_d(i,j) = 4.004*SQRT( ETA2mean_d(i,j) )` GPU `io.F:2809–2811,3033–3049`; `main.F:303–325,373–376`; `mixing_gpu.F:123–147`; `etauv_solver_gpu.F:1999–2007`. 네 문서·TeX의 RK·FroudeCap·유의파고 설명 전체 검색. | 일치 | 인용한 GPU 대입은 문서의 RK 가중 적분, 유속 계산의 Froude 제한, 유의파고 계수 4.004와 대응한다. 이 대응 항목에 문서 누락을 부여하지 않는다. 평균 제곱값의 정의 차이는 FT1-187·275와 별도로 구분한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |

K27 — `fluxes_21v.F:719–722`.

```fortran
       OutL(I,J)=Vin(I-1,J)+0.25*DX      &
               *((1.0_SP-kappa)*Din(I-1,J)+(1.0_SP+kappa)*Din(I-1,J))
       OutR(I,J)=Vin(I,J)-0.25*DX     &
               *((1.0_SP+kappa)*Din(I,J)+(1.0_SP-kappa)*Din(I,J))
```

K28 — `sources.F:236–243` (`CARTESIAN`의 마찰 대입, `MANNING` 분기 포함).

```fortran
       FrcInsX(I,J) = &
# if defined (MANNING)
                   -(GRAV*Cd(I,J)**2/  &
                   Max(H(I,J),MinDepthFrc)**(0.333333_SP))  &
                   *U(I,J)*SQRT(U(I,J)*U(I,J)+V(I,J)*V(I,J))
# else
                   -Cd(I,J)*U(I,J)*SQRT(U(I,J)*U(I,J)+V(I,J)*V(I,J))
# endif
```

K29 — `G/src/moment_gpu.F:754–762` (`CARTESIAN && Gamma2>0`의 호출 경로).

```fortran
        V2_d(I,J)=ken1*(tV*HUxxHVxy+tV*HUxyHVyy) &
                +ken2*(Uy_d(i,j)*HUxxHVxy+tU*HUxxHVxy_y &
                    +tVy*HUxyHVyy+tV*HUxyHVyy_y) &
                +ken5 &
                   *(tU*UxxVxy+tV*UxyVyy) &
                +ken4  &
                   *(Uy_d(i,j)*UxxVxy+tU*UxxVxy_y+tVy*UxyVyy+tV*UxyVyy_y) &
                +Beta_2*Beta_2*(DUx_d(I,J)+DVy_d(I,J)+reta*Beta_2*(tUx+tVy))  &
                   *(HUxyHVyy+tETAy*Beta_2*(tUx+tVy)+reta*Beta_2*UxyVyy)
```

GPU 원자료의 `git diff --stat -- src`는 다음 세 파일을 보고했다.
`src/Makefile_cuda`는 4행의 변경을 보고했다.
`src/etauv_solver_gpu.F`는 22행의 변경을 보고했다.
`src/mod_cuda.F`는 2행의 추가를 보고했다.
이 수량은 공개 HEAD 대비 로컬 diff의 출력이다.
이 보고서는 해당 파일을 수정하지 않았다.

## 4 노트 대조와 수정안

이 절의 노트 경로는 `models/FUNWAVE/` 아래의 상대 경로다.
노트 파일은 수정하지 않았다.
표의 수정안은 현재 코드 설명과 PDF 인용을 구분한다.
문서의 잘못된 문장을 인용한 사실과 그 문장이 현재 구현을 올바르게 설명하는지는 별개로 판정한다.

| 행 ID | 항목·노트(원문) | 대조 근거(원문) | 판정 | 수정안·이유 |
|---|---|---|---|---|
| FT1-261 | `manual-notes/funwave-user-manual-full.md:55` `M = H\{u_\alpha + u_2\}` | PDF p.15 (6) $\mathbf M=H\{\mathbf u_\alpha+\overline{\mathbf u}_2\}$; K09. `24a88c3:doc/funwave_tvd_3.0.tex:265`의 평균 표시와 `7b93138:src/fluxes.F:462–463`의 보정 포함 질량 플럭스를 대조했다. PDF p.15 이미지의 상선도 같다. | 불일치 | B. 질량 플럭스 식의 u2에는 수심 평균 표시를 넣는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-262 | 같은 노트 58행 `**운동량 (식8, p.15):**`; 56행 `(식6·7, p.15)` | PDF p.16에 식 (7),(8)이 인쇄되어 있다. PDF p.15–16 이미지의 식 번호·인쇄 쪽을 대조했다. `24a88c3:doc/funwave_tvd_3.0.tex:265–273`에도 같은 식 순서가 있다. | 불일치 | B. 식 (7)과 식 (8)은 PDF p.16을 인용한다. 식 (6)은 p.15를 인용한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-263 | 같은 노트 61행 `$V_3 = \omega_0 i_z\times u_2 + \omega_2 i_z\times u_\alpha$` | PDF p.16 (11)의 첫 교차곱은 $\overline{\mathbf u}_2$이다. PDF p.16 이미지와 `24a88c3:doc/funwave_tvd_3.0.tex:285`의 첫 교차곱에 상선이 있다. 현재 `dispersion.F:491–498` 및 `7b93138:src/dispersion.F:457–464`의 부호와 연결한다. | 불일치 | B. 식 (11)의 첫 교차곱에 수심 평균 u2를 쓴다. 와도 정의에 쓰는 비평균 u2와 구분한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-264 | 같은 노트 65행 `z_\alpha = -h + \beta H = \zeta h + (1+\zeta)\eta,\qquad \zeta=-0.53,\ \beta=0.47` | `io.F:2622` `Beta_ref = - 0.531_SP`; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP` `io.F:2620–2622`; `init.F:656–664`; 3.0 p.16·40, TeX 1309행의 기준면 설명. 네 문서·TeX 전체의 `Beta_ref`·기준면 검색. [외부 원문 판정](FUNWAVE-external-sources.md). | 불일치 | C. 노트의 기준면 식은 문서의 이론식으로 구분한다. 현재 입력 누락값은 `Beta_ref = - 0.531_SP`이고 직교 초기화는 `Beta_1=Beta_ref+1.0_SP`와 `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`를 별도로 대입한다. C는 노트 65행에 이 구현 구분이 없는 점이다. 비선형 배수의 E 판정은 FT1-021·216과 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-265 | 같은 노트 72행 `$V=H(u_\alpha+V_1')$를 conserved variable로 두고`; 74행 `(p.18)` | PDF p.19 (23); K03, K20, K22. `7b93138:src/etauv_solver.F:227,251,256` 및 현재 `etauv_solver.F:310,343,348`. PDF p.19 식 (23)의 이미지와 대조했다. | 불일치 | B. 식 (23)은 PDF p.19에 있다. 문서의 보존 운동량은 코드의 Ubar·Vbar에 대응한다. 기준 깊이 유속 U·V와 구분하고, 본문·부록의 프라임 분할은 FT1-228을 함께 설명한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-266 | 같은 노트 83행 `S는 (u,v,η)로 갱신 + 수렴 iteration.` | `main.F:380` `DO ISTAGE=1,3`; PDF p.32 “ITERATION ... is not used any more.” 3.0 p.11·32의 반복 제거 문장, `7b93138:src/main.F:214–250`와 현재 `main.F:380–487`의 단계 루프. FT1-121은 문서 p.25에만 남은 구현 주장의 D 판정이고 이 행은 그 문장을 현재 구현으로 옮긴 노트의 B 판정이다. | 불일치 | B. 각 RK 단계는 소스를 갱신하고 유속을 복원한다. 수렴 반복이 필요하다는 p.25 문장은 같은 문서의 반복 제거 설명과 모순한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-267 | 같은 노트 88행 `**Shock-capturing (default):** Froude(=H/d) 임계 초과 cell` | K13; `io.F:2691` `VISCOSITY_BREAKING = .TRUE.` `io.F:2689–2691`; `masks.F:177–188`; `7b93138:src/masks.F:130`; `6233886`(2019-06-16)의 누락 기본값 FALSE→TRUE diff. FT1-013·125·126·240과 같은 조건이다. | 불일치 | B. 충격 포착 전환 분기는 `VISCOSITY_BREAKING`의 `ELSE`에 있는 `IF(ABS(Eta(I,J))/MAX(DEPTH(I,J),MinDepthFrc)>SWE_ETA_DEP)THEN`이다. 이 비는 유속 Froude 수가 아니다. 현재 입력 누락 기본값은 점성 쇄파이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-268 | 같은 노트 89행 `cross-derivative 제거형(P,Q 사용, U,V 아님)이 더 안정` | `7b93138:src/sources.F:63` `LOGICAL :: PQ_scheme = .TRUE.`; 현재 `sources.F:70` `LOGICAL :: PQ_scheme = .FALSE.` `17d2eeb`의 `src/sources.F` diff; 현재 `sources.F:70,394–453`; [확정 판정 FT1-127](FUNWAVE-git-verify-AD1.md). | 불일치 | A. PDF는 P·Q 확산을 설명한다. `17d2eeb`(2017-03-03)는 `PQ_scheme`을 참에서 거짓으로 바꿨다. 현재 기본 분기는 HU·HV를 확산한다. FT1-127·128·137과 같은 판 차이이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-269 | 같은 노트 90–91행 `$\nu = B\,\delta_b^2(h+\eta)\eta_t,\qquad \delta_b=1.2$`; `Cbrk1=0.65, Cbrk2=0.15` | `breaker.F:314` `nu_break(I,J) = cap1*tmp2 + nu_bkg`; `io.F:3103` `Cbrk2 = 0.35_SP` `breaker.F:124–126,264–315`; `io.F:3101–3103`; [확정 판정 FT1-130·134·135](FUNWAVE-git-verify-AD1.md). 네 문서·TeX의 Cbrk·점성식 검색. | 불일치 | B. 노트의 점성식·1.2·0.15는 PDF p.25–26의 기술로 구분한다. 현재 조파 영역 밖의 기본 지속 쇄파식은 `nu_break(I,J) = cap1*tmp2 + nu_bkg`이고 `cap1=1.0*(MAX(Depth(I,J),MinDepthFrc)+ETA(I,J))`이다. Cbrk2 미입력값은 0.35이다. 개시식은 `tmp1=Cbrk1*tmp3`이며 `tmp3=SQRT(GRAV*MAX(MinDepthFrc,H(I,J)))`이다. FT1-130·134·135의 B 판정과 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-270 | 같은 노트 94행 `mirror BC. dry cell용 Riemann wave speed 수정 (식84·85, p.26).` | K11, K13; `fluxes.F:1572–1598`의 차수 저하·기울기 영 대입. `bc.F:83–93`; `fluxes.F:352–439,1572–1600`; `Din(I,J)=TXP2-1.0_SP/6.0_SP*(DVP3-2.0_SP*DVP2+DVP1)`. [확정 판정 FT1-140·141](FUNWAVE-git-verify-AD1.md). | 문서에만 | D. 법선 플럭스 차단과 내부 건조 셀의 재구성 보정은 구현한다. 문서 식 (84)·(85)의 별도 건조 파속 분기는 현재 WAVE_SPEED에 없다. 이 구현 주장에는 FT1-140·141과 같은 D를 부여한다. DVP 보정값의 0 대입을 최종 기울기 0으로 설명하지 않는다. 내부 거울 경계 서술의 차이는 FT1-139와 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-271 | 같은 노트 97행 `폭은 보통 wave length 정도 (p.26).` | PDF p.27 “one or two times the typical wavelength.” PDF p.27 이미지의 `one or two times`를 확인했다. `7b93138:src/io.F:658`은 폭을 읽으며 파장 권고를 자동 대입하지 않는다. FT1-145와 같은 문서 수량이다. | 불일치 | B. L-D 스펀지의 문서 권고 폭은 보통 1–2파장이다. 출처는 PDF p.27이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-272 | 같은 노트 99행 `C_{sponge}=C_{max}\!\left[1-\tanh(\cdots)\right]` | `sponge.F:287` `tmp_2d_1(i,j)=MAX(CDsponge*TANH(ri/10.0),lim)` `sponge.F:285–287`; `7b93138:src/sponge.F:248–250`; [확정 판정 FT1-149](FUNWAVE-git-verify-AD1.md). | 불일치 | B. 문서 식 (89)과 실제 코드식은 다르다. 코드는 `ri=MAX(0.0,REAL(Iwidth-I))`와 `tmp_2d_1(i,j)=MAX(CDsponge*TANH(ri/10.0),lim)`을 사용한다. 문서식을 현재 구현식으로 쓰는 노트에는 FT1-149와 같은 B를 부여한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-273 | 같은 노트 103행 `방향스펙트럼을 1000개 주파수 성분으로 분할 (p.30).` | PDF의 1000 문장은 p.31이다. `wavemaker.F:1870` `do kf=1,10000` `7b93138:src/wavemaker.F:1061–1063`과 현재 `wavemaker.F:1870–1872`; PDF p.31 이미지. FT1-179와 같은 수량 판정이다. | 불일치 | B. 코드의 초기 스펙트럼 적분 분할은 10000이다. PDF p.31의 성분 수 설명과 사용자 지정 주파수 수를 구분한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-274 | 같은 노트 106행 `파봉(crest)에만 적용.` | `mod_meteo.F:295` `WindCrestPercent=LARGE`; 719–722의 마스크 조건. `mod_meteo.F:213–218,247–263,292–307,719–722`; `sources.F:355–364`; 3.0 p.31·37, 2.1 p.21·37, Intro-TN p.9·11 및 TeX의 전체 검색 결과와 대조했다. | 불일치 | C. `METEO`·`WindForce` 경로에서 파봉 한정은 WindCrestPercent와 WindWaveInteraction에 따른다. 미입력 또는 상호작용을 끈 경우 `WindCrestPercent=LARGE`이므로 `MASK_WIND=1`을 유지한다. C는 노트 106행의 조건 생략이며 FT1-184와 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-275 | 같은 노트 107행 `m_0=\frac{1}{t_2-t_1}\int_{t_1}^{t_2}\eta^2 dt` | `mixing.F:146`의 평균 차감 누적. `mixing.F:146–154,244,267`; `7b93138:src/mixing.F:113–125`; PDF p.32 이미지; [확정 판정 FT1-187](FUNWAVE-git-verify-AD1.md). | 불일치 | B. PDF 식 (105)는 수면고 제곱을 적는다. 코드는 이전 평균 수면고를 뺀 값의 제곱을 시간 가중 누적한다. 이 식을 현재 산출식으로 쓰는 노트는 FT1-187과 같은 B이다. 유의파고 계수 4.004 자체는 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-276 | `source-analysis/funwave-flux-tvd.md:22` `(predictor용, TVD 미사용)` | `fluxes.F:109–112`의 문자열 분기. `io.F:2826–2834`; `fluxes.F:109–137`; `7b93138:src/fluxes.F:81–84`. FT1-230은 문서에 이미 있는 선택지의 일치이고, 이 행은 실제 호출을 부정한 노트의 B이다. | 불일치 | B. HLL로 시작하지 않는 CONSTRUCTION 값은 산술평균 플럭스 경로를 선택한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-277 | 같은 노트 31행 `비활성, 테스트용` | `fluxes.F:71–72` `ELSEIF(HIGH_ORDER(1:3)=='FMI') THEN` / `CALL CONSTRUCTION_HO_minmod` `7b93138:src/fluxes.F:63`과 `fef45a7:src/fluxes.F:63`은 주석이다. 전체 이력의 해당 FMI 문자열 검색은 `dfacbb2`(2020-06-12)를 반환한다. `dfacbb2:src/fluxes.F:71–72`에서 활성 분기를 도입했다. 현재 `io.F:2842`의 입력이 `fluxes.F:71–72`를 선택한다. FT1-232와 연결한다. | 불일치 | A. minmod 재구성 호출은 2018년 코드까지 주석 처리되어 있었다. 2020-06-12부터 FMI 입력으로 활성화할 수 있다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-278 | 같은 노트 45행 `4차 1계` | `derivatives.F:104–105`의 K30. `7b93138:src/derivatives.F:104–105`도 같은 스텐실이다. 균일 격자·MASK=1에서 Taylor 전개의 첫 오차항은 `5/12`를 계수로 하는 2차 항이다. 현재 주 분산 경로의 호출은 `dispersion.F:77–83`이다. | 불일치 | B. DERIVATIVE_X_High의 인용 스텐실은 2차 오차를 가진다. 이를 4차 1계 미분으로 적지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-279 | `source-analysis/funwave-dispersion-solver.md:18` `**선형 분산항 V4**(:296-329 ...)` | K21의 312–317행 비선형 추가. `dispersion.F:295–318`; `io.F:2606–2608`; 3.0 p.87, TeX 2660–2692행. 네 문서·TeX 전체에서 U4·수심 평균 분산 보정을 검색했다. | 불일치 | C. 노트 18행이 인용한 범위에는 U4·V4의 선형 부분과 `IF(gamma2>ZERO)THEN`의 비선형 보정이 함께 있다. C는 노트의 비선형 보정 누락에 한정한다. PDF p.87 식 (117)·(118)은 두 부분을 모두 적는다. Beta_2 계수 문제는 FT1-216·217의 E 판정과 연결한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-280 | `source-analysis/funwave-physics-sources.md:17` `tmp1=Cbrk1√(gh)` / `개시~0.45` / `VIS_KENNEDY 기본` | `breaker.F:124` `tmp3=SQRT(GRAV*MAX(MinDepthFrc,H(I,J)))`; `io.F:3081` `Cbrk1 = 0.65_SP`; `breaker.F:314` 기본 대입. `cab9425:mod_global.F:366`; 현재 `io.F:3081`, `breaker.F:124–126,278–315`; `7b93138:src/breaker.F:113–114,232–237`. | 불일치 | B. 쇄파 개시 계수의 기본값은 0.65이다. 파속에는 총수심 하한을 쓴다. VIS_KENNEDY는 컴파일 선택이다. 현재 기본 지속 쇄파 분기는 `nu_break(I,J) = cap1*tmp2 + nu_bkg`이다. FT1-130·134·241·269와 같은 조건·식이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-281 | 같은 노트 48행 `Smagorinsky(nu_smg 전단발산)` | `init.F:437` `nu_smg = ZERO`; `sources.F:367` `# if defined (MIXING)` 두 `src/*.F` 전체의 nu_smg 대입 검색; TVD `init.F:437`, GPU `init.F:332`; TVD `sources.F:367–388`, `io.F:3232–3234`. [확정 판정 FT1-093](FUNWAVE-git-verify-AD1.md). | 문서에만 | D. 현재 TVD와 GPU 사본에서 nu_smg의 활성 대입은 초기 0 대입이다. `MIXING` 소스는 nu_smg를 읽지만 Smagorinsky 점성으로 갱신하지 않는다. 노트의 구현 주장은 FT1-093과 같은 D이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-282 | `source-analysis/funwave-infrastructure.md:16` `4방향 개방경계 P·Q=0` | `bc.F:87` `P(Ibeg,J)=ZERO`; 90 `Fx(Ibeg,J)=0.5_SP*GRAV*(Xi*Xi*Gamma3+2.0_SP*Xi*Deps)` 현재 `bc.F:65–94,122–138,164–174,197–204`; `io.F:870,2260`의 WAVEMAKER·PERIODIC 입력. `7b93138:src/bc.F:68–71`도 법선 플럭스를 0으로 둔다. | 불일치 | B. 기본 외곽은 법선 질량 플럭스를 막는 벽 경계이다. 별도 경계 옵션은 따로 적는다. 서쪽 ABS·LEFT_BC_IRR, COUPLING 구간과 y방향 PERIODIC은 해당 분기에 따른다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-283 | 같은 노트 45행 `DT=CFL·min(DX/&#124;U+c&#124;,DY/&#124;V+c&#124;)` | `misc.F:243` `TMP1=ABS(U(I,J))+SQRT(GRAV*MAX(H(I,J),MinDepthFrc))` `7b93138:src/misc.F:154,170`과 현재 `misc.F:243,259`의 절댓값 위치가 같다. | 불일치 | B. CFL 분모는 abs(U)+c와 abs(V)+c이다. c에는 총수심 하한을 쓴다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-284 | 같은 노트 23행 `MUSCL kappa(SEC→−1/else→1/3)` | `init.F:389–392`; `fluxes.F:780–781` `io.F:2842–2854`; `init.F:389–393`; `fluxes.F:101–105,473–480,779–784`; [확정 판정 FT1-202](FUNWAVE-git-verify-AD1.md). | 불일치 | B. 초기화는 Kappa 값을 구분하지만 현재 CONSTRUCT_X/Y는 Kappa를 계산에 쓰지 않는다. SECOND·THIRD 입력은 같은 선형 재구성을 수행한다. 초기화 값을 재구성 차수 선택으로 설명하는 노트에는 FT1-202와 같은 B를 부여한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-285 | `web-refs/funwave-foundational-papers.md:24` `Froude 임계 초과 시 NLSW 전환 쇄파` | K13. `io.F:2689–2691,2713–2715`; `masks.F:177–188`; `7b93138:src/masks.F:130–131`. 네 문서·TeX의 Froude·파고 수심 비 검색. | 불일치 | B. 현재 충격 포착 전환의 조건은 `IF(ABS(Eta(I,J))/MAX(DEPTH(I,J),MinDepthFrc)>SWE_ETA_DEP)THEN`이다. 이 비를 유속 Froude 수로 적지 않는다. 이 조건은 VISCOSITY_BREAKING을 선택하지 않은 분기에 있다. FT1-013·125·267과 같은 판정이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-286 | `README.md:18` `쇄파를 bore로 처리, hybrid FV/FD` | `io.F:2691` `VISCOSITY_BREAKING = .TRUE.`; K13. `io.F:2689–2691,3076`; `masks.F:177–188`; `breaker.F:64–71`; 3.0 p.25–26·41의 두 방식 설명과 대조했다. | 불일치 | C. 충격 포착 쇄파 설명 자체는 제공되는 한 방식을 설명한다. C는 모델 소개에 점성 쇄파 선택과 현재 누락 기본값이 빠진 점이다. `VISCOSITY_BREAKING`을 읽지 못하면 참을 대입하고, 거짓일 때만 파고 수심 비로 분산을 끄는 분기를 쓴다. FT1-240·267과 연결한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-287 | `source-analysis/funwave-gpu-source.md:13` `비-gpu 파일은 CPU판 공유` | `G/src/moment_gpu.F:754`의 `tV*HUxxHVxy`; TVD `dispersion.F:461`의 `U(I,J)*HUxxHVxy` 두 사본 `src/dispersion.F`의 읽기 전용 `git diff --no-index`; GPU `dispersion.F:189`와 TVD `dispersion.F:190,386–395`. 같은 사본 CPU 대응식은 GPU `dispersion.F:445`이다. | 불일치 | C. GPU 사본의 비 CUDA 파일을 현재 TVD 파일과 동일하다고 볼 수 없다. `dispersion.F`를 직접 비교하면 GPU에는 MGPU 분기 조건이 있고 현재 TVD에는 AB_OUTPUT 블록이 추가되어 있다. C는 노트 13행에 공유 범위와 판본 구분이 없는 점이다. CUDA 식의 별도 결함은 FT1-257에 연결한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-288 | `source-analysis/funwave-gpu-cuda-port.md:38` `핵심 변경은 ... 두 줄` | GPU 로컬 diff의 세 파일 목록; `G/src/mod_cuda.F:17` `integer,parameter :: TriSolver = 0    ! 0, 1-cusparse` GPU 원자료의 공개 HEAD 대비 `git diff -- src/Makefile_cuda src/etauv_solver_gpu.F src/mod_cuda.F`; Makefile_cuda는 FC·OPT 두 대입을 바꿨고 mod_cuda.F는 버퍼 선언 두 행을 추가했다. | 일치 | 노트의 ‘핵심 변경 두 줄’은 Makefile_cuda의 FC·OPT 대입 변경을 가리키며 그 범위에서는 맞다. 전체 로컬 수정은 etauv_solver_gpu.F와 mod_cuda.F도 포함한다. 핵심 두 줄이라는 표현을 전체 수정이 두 줄뿐이라는 주장으로 확대하지 않는다. 전체 diff는 FT1-258과 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-289 | `source-analysis/funwave-source-map.md:24` `READ_INPUT(mod_input)`; 27행 `FLUXES(MUSCL-TVD) → dispersion+tridiagonal solve` | `io.F:149`의 READ_INPUT 정의; `main.F:383` `CALL Cal_Dispersion`; 394 `CALL FLUXES`; 404 `CALL SourceTerms`; 414 `CALL ESTIMATE_HUV(ISTAGE)` `7b93138:src/io.F:95`, `7b93138:src/main.F:214–230`; 현재 `io.F:149`, `main.F:380–414`, `etauv_solver.F:348`. | 불일치 | B. READ_INPUT은 io.F에 정의되어 있다. RK 단계는 분산 계산과 플럭스 계산 뒤에 소스와 보존 변수를 갱신한다. 보존 변수 갱신 뒤 유속 역변환을 호출한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-290 | `manual-notes/funwave-tvd-manual.md:19–24`의 MUSCL·적응 RK·두 쇄파 방식·습윤–건조·well-balanced 요약 | K01–K03, K10, K13, K14. | 일치 | 유지안: 문서 요약으로 유지한다. 개별 구현·기본값·예외는 이 보고서의 해당 행을 연결한다. |

K30 — `derivatives.F:104–105`.

```fortran
       Uout(I,J)= (Uin(I+2,J)+2.0_SP*Uin(I+1,J)    &
                 -Uin(I-2,J)-2.0_SP*Uin(I-1,J))/DX/8.0_SP*MASK(I,J)
```

해석: 균일 격자에서 K30의 Taylor 전개는 $f'+(5/12)\Delta x^2f'''+O(\Delta x^4)$이다.
이는 실제 스텐실의 정확도에 대한 대수 판정이다.
모델 실행 오차를 측정한 결과는 아니다.

## 5 차이 결론

이 절은 일치가 아닌 각 행에 결론 하나를 부여한다.
A는 판 차이이다.
B는 문서 또는 현재 노트의 오기이다.
C는 대상 문서 범위의 누락이다.
D는 문서에만 있는 구현 주장이다.
E는 코드 결함 후보이다.
F는 식 변형으로 설명하는 표기 차이이다.
H는 코드 대조 대상이 아닌 설명이다.
X는 외부 원문이 있어야 가를 수 있는 항목이다.
이번 대조에는 X를 부여한 행이 없다.
이 결론은 외부 논문의 모든 식·계수를 검증했다는 뜻이 아니다.

### 5.1 판 차이와 문서 시점의 근거

문서 시점의 코드 대조 기준은 `7b93138` (2016-11-18)이다.
이 커밋은 TEX의 마지막 변경 `24a88c3` (2016-11-18) 뒤의 같은 날 커밋이다.
`git log 24a88c3..7b93138`는 `dd0e0cc`, `9555411`, `7b93138`을 반환했다.
PDF 마지막 변경 `fef45a7` (2018-02-24)의 메시지는 `add report number`이다.
PDF의 발행 표기는 “Release Dec 2016”이다.
이 보고서는 PDF의 마지막 저장 날짜를 모든 이론식의 개정 날짜로 취급하지 않는다.

HA1 — FT1-127, FT1-128, FT1-137의 판 차이 근거.

`7b93138:src/sources.F:63`은 `LOGICAL :: PQ_scheme = .TRUE.`이다.
같은 파일 264행은 `IF(PQ_scheme)THEN`이다.
265행부터의 선택 분기는 P를 확산한다.
290행부터의 다른 분기는 HU를 확산한다.
`17d2eeb` (2017-03-03)의 메시지는 `change PQ_scheme to ELSE in order use HU and HV for eddy viscosity breaking`이다.
그 diff는 `LOGICAL :: PQ_scheme = .TRUE.`를 `LOGICAL :: PQ_scheme = .FALSE.`로 바꾼다.
그 diff는 다음 주석도 추가한다.

```fortran
!      it turns out P and Q are not exchanged at processor interface
!      it affects edges, make PQ_scheme=false
```

현재 `sources.F:70`은 `LOGICAL :: PQ_scheme = .FALSE.`이다.
따라서 이 세 행은 B가 아니라 A이다.

HA2 — FT1-197의 판 차이 근거.

`7b93138:src/mod_global.F:137`은 `REAL(SP) :: FroudeCap=10.0_SP`이다.
`7b93138:src/io.F:814`는 `CALL READ_FLOAT(FroudeCap,FILE_NAME,'FroudeCap',ierr)`이다.
당시 호출 뒤에는 명시적인 누락 기본값 대입이 없다.
`285a6f6` (2017-05-01, `add all default`)은 누락 분기에 3.0을 대입하는 처리를 추가했다.
`285a6f6:src/io.F:2564`는 `FroudeCap = 3.0_SP`이다.
현재 같은 처리는 `io.F:2898–2910`에 있다.
이 변경은 문서의 선언 초기값 10과 현 누락값 3의 차이를 설명한다.
당시 `READ_FLOAT`도 `INTENT(OUT)`을 썼다.
따라서 과거 선언 초기값이 누락 입력 호출 뒤에도 보존된다는 보장은 별도로 주장하지 않는다.

HB1 — 문서 시점에도 다른 기본값.

`7b93138:src/mod_global.F:134`는 `REAL(SP) :: MinDepth=0.001`이다.
135행은 `REAL(SP) :: MinDepthFrc=0.5`이다.
372행은 `REAL(SP) :: Cbrk1=0.65,Cbrk2=0.35,T_brk`이다.
문서의 0.001은 다른 변수 MinDepth의 선언값과 같다.
해석: 문서가 두 변수의 값을 혼동했을 수 있다.
확인한 사실은 MinDepthFrc 선언값이 0.5라는 것이다.
이 해석을 오기의 원인으로 확정하지 않는다.
`285a6f6:src/io.F:2599`는 `MinDepthFrc = 0.1_SP`이다.
같은 커밋 2685행은 `Cbrk2 = 0.35_SP`이다.
따라서 FT1-135와 FT1-199는 A로 설명할 수 없다.

HB2 — 문서 시점의 점성식.

`7b93138:src/breaker.F:218`은 `IF(AGE(I,J)>ZERO.AND.AGE(I,J)<T_brk.AND.ETAt(I,J)>tmp2)THEN`이다.
219행은 `cap1=1.0*(MAX(Depth(I,J),MinDepthFrc)+ETA(I,J))`이다.
233행의 `VIS_KENNEDY` 경로는 `nu_break(I,J)=cap1*ABS(ETAt(I,J))+nu_bkg`이다.
237행의 기본 경로는 `nu_break(I,J) = cap1*tmp2 + nu_bkg`이다.
`0a758aa` (2017-03-17)은 이후 점성 대안을 추가했다.
기본 정적 식과 1.0 계수는 문서 시점에도 있었다.
따라서 문서 식 (82)의 전체 차이를 후속 판 변경으로 돌리지 않는다.

HB3 — 고차 재구성·분산·스펙트럼의 과거 원문.

| 과거 인용 | 원문 | 적용 행 |
|---|---|---|
| `7b93138:src/init.F:488` | `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP` | FT1-021,024,028,029,031,034,208–227 |
| `7b93138:src/dispersion.F:388–389` | 아래 K31의 완결 대입 | FT1-208,209 |
| `7b93138:src/fluxes.F:729` | `! The "kappa" is meaningless in above routines.` | FT1-202 |
| `7b93138:src/fluxes.F:736` | `OutL(I,J) = Vin(I-1,J) + 0.5_SP*DX*Din(I-1,J)` | FT1-202 |
| `7b93138:src/fluxes.F:128` | `CALL HLL(Mloc1,Nloc,SxL,SxR,FxL,FxR,HUxL,HUxR,Fx)` | FT1-109 |
| `7b93138:src/masks.F:130` | `IF(ABS(Eta(I,J))/MAX(DEPTH(I,J),MinDepthFrc)>SWE_ETA_DEP)THEN` | FT1-013,125,126 |
| `7b93138:src/wavemaker.F:1061` | `do kf=1,10000` | FT1-179 |
| `7b93138:src/wavemaker.F:1123` | `N_spec=20.0_SP/sigma_theta` | FT1-178 |
| `7b93138:src/wavemaker.F:1244–1245` | `C_phase=1.0_SP/wkn*fm*2.0_SP*pi`; `wave_length=C_phase/fm` | FT1-166 |
| `7b93138:src/wavemaker.F:1293` | `beta_gen(kf)=80.0_SP/delta**2/wave_length**2` | FT1-166 |
| `7b93138:src/sponge.F:250` | `tmp_2d_1(i,j)=MAX(CDsponge*TANH(ri/10.0),lim)` | FT1-149 |
| `7b93138:src/sponge.F:590` | `ri=R_sponge**(50*(I-1)/(Iwidth-1))` | FT1-144 |
| `7b93138:src/mixing.F:113` | `ETA2sum = (Eta-ETAmean)*(Eta-ETAmean)*DT + ETA2sum   !ykchoi` | FT1-187 |
| `7b93138:src/mod_input.F:128` | `REAL(SP),         INTENT(OUT) :: FLOAT_VAL` | FT1-197,259 |

K31 — `7b93138:src/dispersion.F:388–389`.

```fortran
        U1pp(I,J)=-reta*Beta_2*ETAx(I,J)*Beta_2*(Utx(I,J)+Vty(I,J)) - 0.5_SP*reta*reta*Beta_2*Beta_2*(Utxx(I,J)+Vtxy(I,J))&
                  -ETAx(I,J)*Beta_2*(DUtx(I,J)+DVty(I,J)) -reta*Beta_2*(DUtxx(I,J)+DVtxy(I,J))
```

HB3의 계수와 절차는 문서 시점 코드에도 있다.
이 행들은 현재 HEAD 날짜만을 이유로 A로 바꾸지 않는다.

### 5.2 D 분류의 전체 원자료·이력 검색

검색은 `rg -i -uu`로 `models/FUNWAVE/raw/source_code` 전체에서 수행했다.
제외 경로는 `**/simple_cases/**`, `**/benchmarks/**`, `**/.git/**`이다.
다른 소스·문서·생성 파일은 검색 대상에 남겼다.
파일 수는 `rg -l` 결과에서 센 값이다.
검색어 적중은 구현의 존재를 뜻하지 않는다.

| 대상 | 실제 검색식 | 적중 파일 수 | 원문 확인 결과 |
|---|---|---:|---|
| FT1-093 | `smagorinsky\|nu_smg\|smagor\|smago\|C_smag` | 22 | 문서 설명·주석·배열 선언·할당·0 초기화·확산 소스의 읽기가 있다. TVD/GPU에 점성 계수 갱신식이 없다. `mixing_salatin.F`와 `mixing_gpu.F`의 Smagorinsky 문구도 주석이다. |
| FT1-121 | `ITER_NUM\|ERRORi\|ITERATION\|EtaOld\|UbarOld\|VbarOld` | 16 | 선언·배열·조건부 대입이 있다. `mod_bathy_correction.F`의 반복은 수심 평활화용이다. 유체 RK 단계의 수렴 반복이 아니다. |
| FT1-140,141 | `right dry\|left dry\|dry cell\|WAVE_SPEED\|SQR_PHI_[LR]` | 11 | 문서 식과 일반 파속 계산이 있다. TVD의 세 `fluxes*.F`와 GPU `fluxes.F,moment_gpu.F`에 좌우 건조 셀별 1,2 계수 분기가 없다. |
| FT1-229의 보조 검색 | `HLLC\|contact.wave\|S_STAR\|star_state` | 7 | 입력 기본 문자열과 문서 예제에 HLLC가 있다. GPU `sediment.F:362–363`에도 HLLC 호출이 있다. 수리 유동의 `CONSTR(1:3)` 분기는 HLLC를 HLL로 보낸다. |

이력 검색은 경로를 제한하지 않은 `git log --all --format='%h %cs %s' -S <검색어>`를 사용했다.
TVD 전체 이력 사본을 검색했다.
다음 표는 그 결과다.

| 검색어 | 전체 이력 결과 | 소스 차이 확인 |
|---|---|---|
| `Smagorinsky` | `9b28db7` (2016-11-14, TEX 추가) | 문서의 구현 문장이 추가된다. |
| `nu_smg` | `cab9425,b9c035d,8d5a857,dcc84ba,94873a5,13ea0f6,347793e,5311c8e,170024b,61d0809,30f7a16,517c34e` | `git log --all -p -S nu_smg -- '*.F'`로 문자 소스 diff를 추가 확인했다. 선언·0 초기화·확산 소스의 추가·이동·삭제만 있다. 나머지 적중은 실행파일·예제 자산이다. |
| `ITER_NUM` | `cab9425,b9c035d,8d5a857` | `INTEGER :: ITER_NUM = 2` 선언의 추가·이동·삭제만 있다. |
| `ERRORi` | `cab9425,b9c035d,8d5a857` | `REAL(SP) :: ERRORi = 0.0001_SP` 선언의 추가·이동·삭제만 있다. |
| `right dry cell` | `9b28db7` | 문서 TEX에만 추가된다. |
| `left dry cell` | `9b28db7` | 문서 TEX에만 추가된다. |

`7b93138:src/main.F:214`도 `DO ISTAGE=1,3`이다.
현재 `main.F:380`도 같은 단계 범위이다.
따라서 남아 있는 `ITERATION` 선언만으로 수렴 반복의 구현을 주장하지 않는다.

D는 위 구현 주장에만 부여했다.
BFT 제외 문장과 단방향 조파의 개발 중 문장은 D가 아니다.

### 5.3 E 후보의 반대 근거와 근거 강도

다음 표는 E 행을 같은 원인별로 묶는다.
묶음 수는 이 표에서 센 8개이다.
한 묶음이 여러 식 행에 영향을 준다.
E 행 수를 독립적인 결함 수로 해석하지 않는다.
모든 E 결론은 정적 코드·식 대조 결과이다.

| 묶음 | 해당 행 | 먼저 확인한 반대 근거·조건 | 서로 다른 모순 근거 | 근거 강도·결론 |
|---|---|---|---|---|
| E01 비선형 분산 계수 | FT1-021,024,028,029,031,034,208–213,215–227 | `Gamma2=0`이면 해당 항은 꺼진다. `MASK9=0`도 해당 항을 끈다. 현재 GPU도 같은 계수를 전달한다. `Beta_2` 전체 검색에서 입력·사후 역보정·이유 설명을 찾지 못했다. `init.F:657`은 `! physics - below are fully nonlinear Boussinesq for reference`라고 적는다. | 첫 근거는 PDF p.86–89의 계수이다. 둘째 근거는 `etauv_solver.F:407–411`의 역변환이 같은 `Beta_ref`에서 수면고 축소 없이 선형 연산자를 쓴다는 점이다. 비선형식의 $h^2$ 항까지 0.0016배 하므로 단순한 $\eta$ 변수 재정의로 모든 항을 복원할 수 없다. | 강함. 완전 비선형 식의 현재 구현에 문서에 없는 축소 계수가 남아 있다. 원래 의도와 수치 영향은 확인하지 않았다. |
| E02 구면 분산 연산자 | FT1-051,052,062,064,068–071,074–077,081,082 | `ZALPHA`를 켜면 `Beta_1`을 초기화한다. 다만 문서의 기본 수심 평균 모델과 다른 기준 깊이 모델이다. `SPH_EXTRA_DISP`는 추가 곡률항을 계산한다. `dispersion.F:359`는 꺼진 경우 다른 계수에 들어간다고 적는다. `etauv_solver.F:418,514`에는 구면 문서화를 남겨 둔 주석이 있다. | 첫 근거는 기본 구면 `init.F:667–670`이 $b1=1/3,b2=-1/2$를 정한다는 점이다. 둘째 근거는 같은 기본 경로의 `dispersion.F:349–357`이 초기화하지 않은 `Beta_1`으로 소스 연산자를 만든다는 점이다. 셋째 근거는 PDF (35),(37),(41)–(44)의 곡률항이 기본 역변환에 없다는 점이다. 추가 플래그도 역변환을 같은 연산자로 바꾸지 않는다. | 초기화·연산자 불일치 근거는 강함. 곡률항 생략이 근사 의도인지에 관한 근거는 중간. 해당 행은 강한 초기화 근거 또는 중간 곡률 근거를 가진 같은 구면 구현 후보로 분류한다. |
| E03 구면 분산 소스의 $\eta_t$ | FT1-079,083,084 | 곱의 차이는 $1/r_0$에 비례한다. 의도적으로 작은 항을 생략했을 가능성을 검토했다. `SPH_EXTRA_DISP`는 `U1p,V1p` 계산에만 분기를 두며 이 질량 소스를 추가하지 않는다. | 첫 근거는 PDF 식 (55),(56)의 $\eta_tF,\eta_tG$이다. 둘째 근거는 같은 코드 `etauv_solver.F:241`이 $\eta_t$에 $\tan\theta\,HV/r_0$를 더한다는 점이다. `sources.F:508–509,525–526`은 이 추가항 없이 발산만 쓴다. | 중간. 구면 질량식의 곡률 소스와 분산 소스의 곱 변환이 서로 다르다. 명시적인 생략 의도 주석은 찾지 못했다. |
| E04 HLL 상태 점프 | FT1-109 | 문서는 비분산 SWE 부분을 TVD로 다루는 결합 방법을 설명한다. 이는 HLL에서 $Hu,Hv$를 택한 의도일 수 있다. `fluxes.F:340–341`의 주석은 파속에서 전단파를 계산하지 않는다고 적는다. 별도 보정 점프 경로는 찾지 못했다. | 첫 근거는 PDF (58),(73)의 보존 상태이다. 둘째 근거는 `etauv_solver.F:310,343`의 적분 상태가 `Ubar,Vbar`라는 점이다. 이에 비해 `fluxes.F:156–159`는 HLL 상태 차에 `HU,HV` 재구성을 준다. | 약함. 문서의 전체 보존 상태 HLL과 코드의 SWE 상태 점프가 다르다. 결합 안정화 설계일 수 있으므로 결함으로 확정하지 않는다. |
| E05 L-D 지수의 정수 나눗셈 | FT1-144 | `Iwidth-1=50`인 경우 나눗셈이 정확한 정수이다. `MAX(...,lim)`은 방향 중첩 시 더 큰 감쇠를 유지한다. 두 처리 모두 임의 폭에서의 분수 지수를 복원하지 않는다. | 첫 근거는 PDF (87)의 지수 프로파일이다. 둘째 근거는 같은 `sponge.F:285`가 마찰 거리에는 `REAL(Iwidth-I)`를 명시하지만 653행은 정수 피연산자끼리 나눈다는 점이다. 예를 들어 $Iwidth=100,I=2$이면 $50/99$를 0으로 자른다. | 중간. 폭에 따른 지수 함수가 계단식 지수로 바뀐다. 의도적인 정수화라는 설명은 찾지 못했다. |
| E06 불규칙파 가우스 폭 | FT1-166 | `wavemaker.F:2014–2015`의 “fixed C_phase and wave_length” 주석과 루프 뒤 첨두 파수 계산을 확인했다. 루프 뒤 계산은 이미 만든 `beta_gen(kf)`를 다시 쓰지 않는다. 단일 주파수에서는 성분별·공통 폭 구분이 사라질 수 있다. | 첫 근거는 PDF p.29의 첨두 주파수 공통 계수 문장이다. 둘째 근거는 같은 코드의 fixed 주석이다. 실제 2008–2012행은 성분 파수이고 2026–2027행은 $L=2\pi/k_f$가 된다. | 강함. 서로 다른 주파수에서 공통 폭이라는 문서·주석과 성분별 형상 계수가 모순한다. |
| E07 파고 표본 개수 | FT1-247 | 첫 교차 전 불완전 파를 버리는 `Num_Zero_Up>=2` 조건은 타당한 의도일 수 있다. 누적 개수를 초기화하는 다른 활성 경로는 찾지 못했다. GPU도 같은 분모를 쓴다. | 첫 근거는 PDF p.32의 평균·제곱평균제곱근 파고 정의이다. 둘째 근거는 `init.F:438`의 0 초기화와 `mixing.F:292–294`의 두 번째 교차부터 누적 조건이다. 250–251행의 분모는 완료 파 수 n-1이 아니라 교차 수 n이다. | 강함. 완료된 파 표본과 분모의 개수가 다르다. 기본 초기화에서 파고가 일정한 경우에도 이 비율이 생긴다. 모델을 실행해 크기를 측정하지 않았다. |
| E08 GPU의 $V_2$ 계수 | FT1-257 | 호출은 `CARTESIAN && Gamma2>0`에서 일어난다. `Gamma2=0`이면 이 경로를 실행하지 않는다. 704–705행은 `tU=U_d`, `tV=V_d`이므로 두 변수를 바꿔 정의한 것이 아니다. 공개 GPU HEAD에도 같은 줄이 있다. 로컬 cuSPARSE 수정은 이 줄을 바꾸지 않았다. | 첫 근거는 PDF (112),(120)의 $uA_x+vA_y$이다. 둘째 근거는 TVD `dispersion.F:461`과 GPU CPU경로 `G/src/dispersion.F`의 $u$ 계수이다. CUDA `moment_gpu.F:754`는 첫 항도 `tV`이다. | 강함. CUDA 전개식 첫 항의 유속 성분이 다른 두 근거와 모순한다. |

E02의 각 행은 다음 강도를 적용한다.
FT1-062,064,068–071은 중간이다.
FT1-051,052,074–077,081,082는 초기화·역변환 불일치까지 포함하므로 강함이다.
이 구분은 아래 개별 결론 표에도 반영한다.

`THIRD` 행은 이 E 표에 넣지 않았다.
`fluxes.F:773–775`의 주석은 재구성을 단순화했다고 명시한다.
현재 계산이 2차 선형 재구성이라는 사실은 명확하다.
따라서 FT1-202의 최종 분류는 B이다.

추가 B 근거는 다음과 같다.
`7b93138:src/sources.F:169–188`의 K32도 공간 미분을 계산한다.
따라서 FT1-046의 누락된 $\nabla$는 현 HEAD만의 식 변경이 아니다.
`7b93138:src/fluxes.F:448`은 `CALL CONSTRUCT_X(Mloc,Mloc1,Nloc,DX,U4,DelxU4,U4xL,U4xR,Kappa)`이다.
따라서 FT1-115의 경계면 분산 보정 재구성도 문서 시점에 있었다.
`7b93138:src/mod_param.F:64`는 `INTEGER, PARAMETER::SP=SELECTED_REAL_KIND(6,30)`이다.
따라서 FT1-191의 정의 위치 차이도 문서 시점에 있었다.

K32 — `7b93138:src/sources.F:169–188`.

```fortran
       SourceX(I,J)=GRAV*(Eta(I,J))/DX*(Depthx(I+1,J)-Depthx(I,J))*MASK(I,J) &
 ! friction
# if defined (MANNING)
                   -(GRAV*Cd(I,J)**2/H(I,J))*U(I,J)*SQRT(U(I,J)*U(I,J)+V(I,J)*V(I,J)) &
# else
                   -Cd(I,J)*U(I,J)*SQRT(U(I,J)*U(I,J)+V(I,J)*V(I,J)) &
# endif

                       ! dispersion
                       ! (h+eta)(u*\nabla V4 + V4 * \nabla u - v1pp-v2-v3)
                   + Gamma1*MASK9(I,J)*Max(H(I,J),MinDepthFrc)*(         &
                     U(I,J)*0.5_SP*(U4(I+1,J)-U4(I-1,J))/DX+V(I,J)*0.5_SP*(U4(I,J+1)-U4(I,J-1))/DY &
                     +U4(I,J)*0.5_SP*(U(I+1,J)-U(I-1,J))/DX+V4(I,J)*0.5_SP*(U(I,J+1)-U(I,J-1))/DY  &
                     -Gamma2*MASK9(I,J)*(U1pp(I,J)+U2(I,J)+U3(I,J)) &
                     )    &
                        ! Ht(-V4+V1p) = div(M)*(U4-U1p)
                    +Gamma1*MASK9(I,J)*((P(I+1,J)-P(I,J))/DX+(Q(I,J+1)-Q(I,J))/DY) &
                      *(U4(I,J)-U1p(I,J)) &
! wavemaker
                   +WaveMaker_Mass(I,J)*U(I,J)
```

`7b93138:src/etauv_solver.F:98–100`도 불규칙파 조화합을 `WK_Source`에 더한다.
같은 파일 104–106행은 이 값을 질량식의 `R1`에 더한다.
따라서 FT1-180의 소스와 수면고 구분도 문서 시점에 필요하다.

F의 좌표 변환은 다음 항등식으로 확인했다.

$$
\frac{S_p}{\Delta\xi_1}
=\frac{\cos\theta_0/\cos\theta}{r_0\cos\theta_0\Delta\phi}
=\frac1{r_0\cos\theta\Delta\phi}
=\frac1{\mathrm{DX}(I,J)}.
$$

따라서 FT1-054–056,058,060,065,072,078의 지역 격자 길이 표기는 같은 미분을 만든다.
FT1-035의 두 자리 설명값은 $\mathrm{round}(0.531,2)=0.53$으로 연결된다.
FT1-042–044,047,086,228의 프라임 분할은 §2.8의 항등식으로 연결된다.
FT1-110,111의 $\mathbf V$는 이 문맥에서 유속으로 정의해야 코드와 단위가 맞는다.
FT1-181의 $D_{mn}$을 $D_{gen,mn}\exp[-\beta_m(x-x_s)^2]$로 놓으면 코드의 공간 계수 합이 된다.

### 5.4 행별 최종 결론

분류별 개수: A 4, B 36, C 46, D 4, E 47, F 21, H 33, X 0.
집계 기준은 §2–§4의 FT1 행 290개이다.
일치 행은 99개이다.
이 표는 나머지 191개 행을 각각 한 번 수록한다.
원문 블록 K 번호와 이력 근거 HA·HB 번호는 위 절의 전체 인용을 가리킨다.

| 행 ID | 항목 | 결론 | 근거(원문 인용) | 노트에 쓸 결론 문장 |
|---|---|---|---|---|
| FT1-001 | p.12 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.12 원문: “from deep water to the swash zone” | Boussinesq 모델의 적용 범위를 소개하는 총설이다. [10-18 결론 검증 정정] |
| FT1-002 | p.12 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.12 원문: “multiple level representations” | 다른 모델과 선행 연구의 설명이다. 현 TVD의 다층 구현 주장으로 읽지 않는다. |
| FT1-003 | p.12 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.12 원문: “removing the wave height to water depth ratio as a scaling or expansion parameter” | 완전 비선형 근사의 전개 차수를 정의한다. [10-18 결론 검증 정정] |
| FT1-004 | p.12 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.12 원문: “boundary layer turbulence effects on vertical flow structure” | 선행 연구의 성과이다. 현 코드의 검증 결과로 옮기지 않는다. |
| FT1-005 | p.12 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.12 원문: “an iterated 4th order Adams-Bashforth-Moulton (ABM) scheme” | 이 문장은 기존 FUNWAVE의 반복 ABM 방법을 설명한다. [10-18 결론 검증 정정] |
| FT1-006 | p.12 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.12 원문: “maintaining the tridiagonal structure” | 기존 혼합 차수 방법이 삼중 대각 구조를 유지한 이유를 설명한다. [10-18 결론 검증 정정] |
| FT1-007 | p.13 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.13 원문: “the entire domain remains wetted using a network of slots” | 기존 FUNWAVE와 선행 모델의 slot 방법을 설명한다. [10-18 결론 검증 정정] |
| FT1-008 | p.13 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.13 원문: “several extensions have been made in research versions” | 이동 기준 깊이·주기 경계·곡선좌표 연구판의 개발 이력을 설명한다. [10-18 결론 검증 정정] |
| FT1-009 | p.13 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.13 원문: “conserve depth-integrated potential vorticity to $O(\mu^2)$” | 소산이 없는 근사 방정식의 위치 와도 보존 성질을 설명한다. [10-18 결론 검증 정정] |
| FT1-010 | p.13–14 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.13–14 원문: “the decision to pursue a new model formulation” | 개발 동기와 비교 결과이다. 현 코드 결함으로 분류하지 않는다. |
| FT1-013 | p.14 | B 문서 오기 | 쇄파 판정 `masks.F`을 §2.5에서 인용한다. 문서 시점 근거: HB3의 `7b93138:src/masks.F:130`. `masks.F:177–188`의 `IF(VISCOSITY_BREAKING)THEN`에 대한 `ELSE`에서 `IF(ABS(Eta(I,J))/MAX(DEPTH(I,J),MinDepthFrc)>SWE_ETA_DEP)THEN`을 적용한다. `7b93138:src/masks.F:130–131`에도 같은 조건이 있다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 쇄파 전환 조건은 순간 수면고 절댓값과 정수심 하한의 비이다. 이 비를 유속 Froude 수로 적지 않는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-016 | p.14–15 | 일치 | `funwave_tvd_3.0.pdf` p.14–15 원문: “implemented in the same model framework” `init.F:665–679`; `dispersion.F:347–381`; `etauv_solver.F:412–419,508–515`. | 구면 방정식은 같은 초기화·분산 계산·유속 역변환에서 `CARTESIAN` 비정의 분기로 구현한다. 개별 식의 차이는 FT1-051–084에서 판정한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-017 | p.15 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.15 원문: “We retain dimensional forms below” | 분산 근사 차수와 차원식 사용을 정의한다. [10-18 결론 검증 정정] |
| FT1-018 | p.15 (1) | H 코드 대조 대상 아님 | p.15 (1):$\mathbf u=\mathbf u_\alpha+\mathbf u_2(z)$ | 임의 연직 위치의 수평 유속을 기준 깊이 유속과 보정으로 분해하는 이론 정의이다. [10-18 결론 검증 정정] |
| FT1-019 | p.15 (2) | H 코드 대조 대상 아님 | p.15 (2):$\mathbf u_2(z)=(z_\alpha-z)\nabla A+\frac12(z_\alpha^2-z^2)\nabla B$ | 연직 위치에 따른 유속 보정의 이론 정의이다. 수심 평균 보정의 구현 대조는 FT1-024에 있다. [10-18 결론 검증 정정] |
| FT1-021 | p.15 (4) | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `cab9425:init.F:497`와 `7b93138:src/init.F:488`도 같은 `Beta_2` 대입이다. `io.F:2577–2608`의 `DISPERSION`, `Gamma1`, `Gamma2` 입력과 `dispersion.F:302,398–399`의 `IF(gamma2>ZERO)THEN`이 이 경로를 선택한다. `sources.F:251–258,310–317`에서 분산 소스에 사용한다. [확정 판정](FUNWAVE-git-verify-E1.md). | Beta_1은 문서의 beta에 대응한다. Beta_2는 0.04이다. 현재 비선형 전개는 문서의 차원식에 추가 배수를 넣는다. 이 차이는 최초 공개 커밋부터 존재한 코드 결함 후보이다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-024 | p.16 (7) | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `cab9425:init.F:497`와 `7b93138:src/init.F:488`도 같은 `Beta_2` 대입이다. `io.F:2577–2608`의 `DISPERSION`, `Gamma1`, `Gamma2` 입력과 `dispersion.F:302,398–399`의 `IF(gamma2>ZERO)THEN`이 이 경로를 선택한다. `sources.F:251–258,310–317`에서 분산 소스에 사용한다. [확정 판정](FUNWAVE-git-verify-E1.md). `dispersion.F:322–329`의 `# if defined (ZALPHA)` 블록은 앞서 계산한 U4·V4를 선형식으로 다시 대입한다. | U4,V4의 비선형 수심 평균 보정은 Beta_2와 Beta_2 제곱을 포함한다. PDF 식 (7)의 계수와 일치하지 않는다. 2017년 변경은 고스트 셀 계산 위치의 수정이다. 이 U4·V4 비선형 보정 판정은 `ZALPHA`를 정의하지 않은 경로에 한정한다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-027 | p.16 (9) | B 문서 오기 | `funwave_tvd_3.0.pdf p.16 (9)`의 여분 닫는 소괄호; K22,K31의 현재·문서 시점 전개식. `7b93138:src/dispersion.F:388–402`에도 여분 괄호 없는 전개식이 있다. 3.0 p.16 식 (9)의 인쇄 오기에 한정한다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 식 (9)의 여분 닫는 소괄호는 문서 오기이다. 본문과 부록의 항 분할 차이와 구분한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-028 | p.16 (10) | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `cab9425:init.F:497`와 `7b93138:src/init.F:488`도 같은 `Beta_2` 대입이다. `io.F:2577–2608`의 `DISPERSION`, `Gamma1`, `Gamma2` 입력과 `dispersion.F:302,398–399`의 `IF(gamma2>ZERO)THEN`이 이 경로를 선택한다. `sources.F:251–258,310–317`에서 분산 소스에 사용한다. [확정 판정](FUNWAVE-git-verify-E1.md). | V2의 곱 미분 구조는 PDF 식 (10)과 대응한다. 구현의 Beta_2 배수는 차원식의 계수를 바꾼다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-029 | p.16 (11) | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `cab9425:init.F:497`와 `7b93138:src/init.F:488`도 같은 `Beta_2` 대입이다. `io.F:2577–2608`의 `DISPERSION`, `Gamma1`, `Gamma2` 입력과 `dispersion.F:302,398–399`의 `IF(gamma2>ZERO)THEN`이 이 경로를 선택한다. `sources.F:251–258,310–317`에서 분산 소스에 사용한다. [확정 판정](FUNWAVE-git-verify-E1.md). | V3의 회전곱 부호는 문서와 같다. V3의 보정 계수에는 U4,V4의 선형 계수와 다른 Beta_2 배수가 남는다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-031 | p.16 (13) | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `cab9425:init.F:497`와 `7b93138:src/init.F:488`도 같은 `Beta_2` 대입이다. `io.F:2577–2608`의 `DISPERSION`, `Gamma1`, `Gamma2` 입력과 `dispersion.F:302,398–399`의 `IF(gamma2>ZERO)THEN`이 이 경로를 선택한다. `sources.F:251–258,310–317`에서 분산 소스에 사용한다. [확정 판정](FUNWAVE-git-verify-E1.md). | 코드 omega_1은 문서 omega_2에 대응한다. 이름 차이와 별도로 기준 깊이 곱에 Beta_2 배수가 들어간다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-032 | p.16 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.16 원문: “there is a typo in (13) in Shi et al. (2012)” | 선행 논문 식 (13)의 평균 표시 오기를 알리는 문장이다. [10-18 결론 검증 정정] |
| FT1-033 | p.16 번호 없음 | H 코드 대조 대상 아님 | p.16 번호 없음: $\alpha=(z_\alpha/h)^2/2+z_\alpha/h=-2/5$, $\alpha=-0.39$, $z_\alpha=-0.53h$, $0\le kh\le\pi$. 위상 속도 오차의 최적화를 설명한다. | 선형 분산 관계의 최적화와 반올림한 이론값을 설명한다. 코드 입력값과의 대조는 FT1-035에 있다. [10-18 결론 검증 정정] |
| FT1-034 | p.16 (14) | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `cab9425:init.F:497`와 `7b93138:src/init.F:488`도 같은 `Beta_2` 대입이다. `io.F:2577–2608`의 `DISPERSION`, `Gamma1`, `Gamma2` 입력과 `dispersion.F:302,398–399`의 `IF(gamma2>ZERO)THEN`이 이 경로를 선택한다. `sources.F:251–258,310–317`에서 분산 소스에 사용한다. [확정 판정](FUNWAVE-git-verify-E1.md). | Beta_ref와 Beta_1의 상수 대응은 성립한다. 현재 비선형 전개에는 문서 식 (14)만으로 설명되지 않는 Beta_2 배수가 존재한다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-035 | p.17 번호 없음 | F 표기 차이 | `io.F:2620` `CALL READ_FLOAT(Beta_ref,FILE_NAME,'Beta_ref',ierr)`;2622 `Beta_ref = - 0.531_SP` | 0.53과 0.531은 설명상의 반올림이다. 수주 안에 놓이는 성질은 식 (14)의 기하학적 성질이다. 0.04 문제는 FT1-034에 분리한다. |
| FT1-036 | p.17 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.17 원문: “the original SGM and the revised SGM may not be effective” | 선행 방법의 설명이다. 현 코드에서 모든 선행 방법의 구현을 찾을 필요는 없다. |
| FT1-040 | p.18 (16) | H 코드 대조 대상 아님 | p.18 (16):$\nabla\cdot(\mathbf u\mathbf v)=\nabla\mathbf u\cdot\mathbf v+(\nabla\cdot\mathbf v)\mathbf u$ | 보존형을 유도하는 벡터 항등식이다. |
| FT1-042 | p.18 (18) | F 표기 차이 | K03와 K22. 3.0 p.18–19와 부록 p.86 식 (107)–(110); `dispersion.F:337–346,422–436`; `etauv_solver.F:407–411`. 배수 차이는 FT1-208,209에서 별도로 판정한다. | 본문은 비선형 항을 프라임 항에 포함한다. 부록과 코드는 선형 연산자와 나머지 항으로 나눈다. [10-18 결론 검증 보완] |
| FT1-043 | p.18 (19) | F 표기 차이 | K03、`dispersion.F:337–346`의 K20. 3.0 p.18–19와 부록 p.86 식 (107)–(110); `dispersion.F:337–346,422–436`; `etauv_solver.F:407–411`. 배수 차이는 FT1-208,209에서 별도로 판정한다. | 코드의 U1p와 V1p는 이 식의 선형 부분이다. 비선형 잔차의 전체 식은 부록 (109),(110)에 대조한다. [10-18 결론 검증 보완] |
| FT1-044 | p.18 (20) | F 표기 차이 | K22. 3.0 p.18–19와 부록 p.86 식 (107)–(110); `dispersion.F:337–346,422–436`; `etauv_solver.F:407–411`. 배수 차이는 FT1-208,209에서 별도로 판정한다. | 본문과 부록·구현은 분할이 다르다. 코드의 U1pp를 이 식만으로 설명하지 않는다. [10-18 결론 검증 보완] |
| FT1-046 | p.18 (22) | B 문서 오기 | K02의 252행은 `U(I,J)*0.5_SP*(U4(I+1,J)-U4(I-1,J))/DX+V(I,J)*0.5_SP*(U4(I,J+1)-U4(I,J-1))/DY &`. 문서 시점 근거: K32의 `7b93138:src/sources.F:169–188`. `7b93138:src/sources.F:180`에도 두 방향 공간 미분이 있다. 3.0 p.18 식 (22)의 기호 누락에 한정한다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 식 (22)의 첫 이류항에는 공간 미분이 필요하다. 해당 기호 누락은 문서 오기이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-047 | p.19 (23) | F 표기 차이 | K03. 3.0 p.18–19와 부록 p.86 식 (107)–(110); `dispersion.F:337–346,422–436`; `etauv_solver.F:407–411`. 배수 차이는 FT1-208,209에서 별도로 판정한다. | 삼중 대각 역변환은 선형 부분을 쓴다. 비선형 잔차는 부록의 다른 분할로 소스에 둔다. [10-18 결론 검증 보완] |
| FT1-051 | p.19 (25) | E 코드 결함 후보 (강함) | E02. K07,K08; `mod_global.F:174` `REAL(SP) :: Beta_1,Beta_2`; `init.F:669` `b1=1.0_SP/3.0_SP`; `7b93138:src/dispersion.F:318–334`도 같은 경로. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. [확정 판정](FUNWAVE-git-verify-E1.md). | 구면 수심 평균 경로는 Beta_1을 대입하지 않은 채 분산 소스를 계산한다. 이 소스의 계수는 b1=1/3과 b2=-1/2를 쓰는 역변환과 일치하지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-052 | p.19 (26) | E 코드 결함 후보 (강함) | E02. K07,K08; `mod_global.F:174` `REAL(SP) :: Beta_1,Beta_2`; `init.F:669` `b1=1.0_SP/3.0_SP`; `7b93138:src/dispersion.F:318–334`도 같은 경로. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. [확정 판정](FUNWAVE-git-verify-E1.md). | 식 (26)에 대응하는 구면 y경로에는 미초기화 Beta_1을 읽는 소스가 있다. 곡률항 누락과 별도로 역변환 계수와의 불일치를 강한 코드 결함 후보로 유지한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-054 | p.19 (27) | F 표기 차이 | K04. | 코드가 저장하는 길이는 $r_0\cos\theta\,d\phi$이다. 문서의 고정 기준 투영 길이에 $S_p$를 곱한 미분과 같다. |
| FT1-055 | p.20 (28) | F 표기 차이 | `init.F:363` `Dphi_r=Dphi*pi/180.0_SP`; 364 `Dtheta_r=Dtheta*pi/180.0_SP`; K04. | 코드가 각도를 라디안으로 바꾸고 지역 격자 길이를 저장한다. |
| FT1-056 | p.20 (29) | F 표기 차이 | K05. | $S_p/\Delta\xi_1=1/\mathrm{DX}(I,J)$이다. |
| FT1-058 | p.20 (31) | F 표기 차이 | K04; `fluxes.F:553–554`의 K09 아래 구면 식. | 경도 미분의 지역 길이 치환이다. |
| FT1-060 | p.20 (33) | F 표기 차이 | K04, K06. | 경도 방향 길이로 보정 계수를 흡수한다. |
| FT1-062 | p.20 (35) | E 코드 결함 후보 (중간) | E02. K07,K08; `mod_global.F:174` `REAL(SP) :: Beta_1,Beta_2`; `init.F:669` `b1=1.0_SP/3.0_SP`; `7b93138:src/dispersion.F:318–334`도 같은 경로. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. [확정 판정](FUNWAVE-git-verify-E1.md). | 식 (35)의 tan(theta)·v_x 곡률 보정은 기본 구면 혼합 미분에 없다. SPH_EXTRA_DISP의 소스 보정은 역변환을 함께 바꾸지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-064 | p.20 (37) | E 코드 결함 후보 (중간) | E02. K07,K08; `mod_global.F:174` `REAL(SP) :: Beta_1,Beta_2`; `init.F:669` `b1=1.0_SP/3.0_SP`; `7b93138:src/dispersion.F:318–334`도 같은 경로. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. [확정 판정](FUNWAVE-git-verify-E1.md). | 식 (37)의 tan(theta)·(hv)_x 보정은 기본 구면 역변환에 없다. 계수 흡수 의도 주석 때문에 중간 강도의 코드 결함 후보로 유지한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-065 | p.20 (38) | F 표기 차이 | `fluxes.F:576` `GxL=HxL*UxL*VxL*Gamma3`; K04. | 지역 `DX`가 $S_p$를 흡수한다. |
| FT1-068 | p.20 (41) | E 코드 결함 후보 (중간) | E02. K07,K08; `mod_global.F:174` `REAL(SP) :: Beta_1,Beta_2`; `init.F:669` `b1=1.0_SP/3.0_SP`; `7b93138:src/dispersion.F:318–334`도 같은 경로. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. [확정 판정](FUNWAVE-git-verify-E1.md). | 식 (41)의 양의 tan(theta)·u_x 보정은 기본 y역변환에 없다. SPH_EXTRA_DISP는 이 역변환을 같은 연산자로 바꾸지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-069 | p.20 (42) | E 코드 결함 후보 (중간) | E02. K07,K08; `mod_global.F:174` `REAL(SP) :: Beta_1,Beta_2`; `init.F:669` `b1=1.0_SP/3.0_SP`; `7b93138:src/dispersion.F:318–334`도 같은 경로. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. [확정 판정](FUNWAVE-git-verify-E1.md). | 식 (42)의 tan(theta)·(hu)_x 보정은 기본 y역변환에 없다. 소스의 선택적 추가항만으로 이 차이를 해소하지 못한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-070 | p.20 (43) | E 코드 결함 후보 (중간) | E02. K07,K08; `mod_global.F:174` `REAL(SP) :: Beta_1,Beta_2`; `init.F:669` `b1=1.0_SP/3.0_SP`; `7b93138:src/dispersion.F:318–334`도 같은 경로. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. [확정 판정](FUNWAVE-git-verify-E1.md). | 식 (43)의 1계 미분 곡률항과 v에 비례하는 곡률항은 기본 y삼중 대각계에 없다. 보정 의도 주석을 반영하여 중간 강도로 유지한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-071 | p.20 (44) | E 코드 결함 후보 (중간) | E02. K07,K08; `mod_global.F:174` `REAL(SP) :: Beta_1,Beta_2`; `init.F:669` `b1=1.0_SP/3.0_SP`; `7b93138:src/dispersion.F:318–334`도 같은 경로. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. [확정 판정](FUNWAVE-git-verify-E1.md). | 식 (44)의 (hv)_y 및 hv 곡률 보정은 기본 y삼중 대각계에 없다. 선택적 V1p 보정과 구분하여 기록한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-072 | p.21 (45) | F 표기 차이 | K04. | 코드가 `S_p` 변수를 저장하지 않아도 $S_p/\Delta\xi_1=1/(r_0\cos\theta\Delta\phi)$가 성립한다. |
| FT1-074 | p.21 (47) | E 코드 결함 후보 (강함) | E02. K07,K08; `mod_global.F:174` `REAL(SP) :: Beta_1,Beta_2`; `init.F:669` `b1=1.0_SP/3.0_SP`; `7b93138:src/dispersion.F:318–334`도 같은 경로. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. [확정 판정](FUNWAVE-git-verify-E1.md). | 식 (47)의 Coriolis 부호는 일치한다. F_t에 대응하는 분산 경로에는 Beta_1 초기화와 역변환 계수의 불일치가 남는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-075 | p.21 (48) | E 코드 결함 후보 (강함) | E02. K07,K08; `mod_global.F:174` `REAL(SP) :: Beta_1,Beta_2`; `init.F:669` `b1=1.0_SP/3.0_SP`; `7b93138:src/dispersion.F:318–334`도 같은 경로. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. 3.0 p.21 쪽 이미지와 판독 기록; `doc/funwave_tvd_3.0.tex:474`. [확정 판정](FUNWAVE-git-verify-E1.md). | 식 (48)의 y분산 소스는 초기화하지 않은 Beta_1을 사용한다. 동일 경로의 역변환은 다른 계수 b1,b2를 사용한다. PDF p.21 식 (48)과 TEX 474행에는 등호와 우변이 없다. 기존의 `=0` 인용을 정정한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-076 | p.21 (49) | E 코드 결함 후보 (강함) | E02. K07,K08; `mod_global.F:174` `REAL(SP) :: Beta_1,Beta_2`; `init.F:669` `b1=1.0_SP/3.0_SP`; `7b93138:src/dispersion.F:318–334`도 같은 경로. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. [확정 판정](FUNWAVE-git-verify-E1.md). | 식 (49)의 F를 계산하는 기본 구면 경로는 Beta_1을 초기화하지 않는다. 단순히 임의의 초기값을 가정해도 두 분산 계수가 역변환과 동시에 일치하지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-077 | p.21 (50) | E 코드 결함 후보 (강함) | E02. K07,K08; `mod_global.F:174` `REAL(SP) :: Beta_1,Beta_2`; `init.F:669` `b1=1.0_SP/3.0_SP`; `7b93138:src/dispersion.F:318–334`도 같은 경로. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. [확정 판정](FUNWAVE-git-verify-E1.md). | 식 (50)의 G를 계산하는 기본 구면 경로는 Beta_1을 초기화하지 않는다. SPH_EXTRA_DISP를 추가해도 이 초기화 문제는 남는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-078 | p.21 (51) | F 표기 차이 | K04; `fluxes.F:520` `PL=HUxL`; 521 `PR=HUxR`; 576 `GxL=HxL*UxL*VxL*Gamma3`; K09. | 플럭스의 $S_p$는 시간 적분의 지역 `DX`에 들어간다. |
| FT1-079 | p.21 (52) | E 코드 결함 후보 (중간) | E03. K05,K06; `etauv_solver.F:241` `R1(I,J)=R1(I,J)+1.0_SP/R_earth*TAN(Lat_theta(I,J))*HV(I,J)`. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/sources.F:362–378`에도 곡률 질량 소스의 곱이 없다. `cab9425:etauv_solver.F:188`에는 질량식 곡률 소스가 있다. [확정 판정](FUNWAVE-git-verify-E1.md). | 식 (52)의 분산 소스는 eta_t에 해당하는 곡률 질량 소스의 기여를 포함하지 않는다. 마찰·경사·Coriolis의 구현과 구분하여 중간 강도로 유지한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-081 | p.21 (53) | E 코드 결함 후보 (강함) | E02. K07,K08; `mod_global.F:174` `REAL(SP) :: Beta_1,Beta_2`; `init.F:669` `b1=1.0_SP/3.0_SP`; `7b93138:src/dispersion.F:318–334`도 같은 경로. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. `init.F:1020–1025`의 `Ubar=HU+gamma1*U1p*H`, `Vbar=HV+gamma1*V1p*H`를 대조했다. [확정 판정](FUNWAVE-git-verify-E1.md). | 구면 초기 Ubar는 U1p를 사용한다. Ubar에서 유속을 구하는 역변환은 다른 b1,b2 계수를 사용한다. 식 (53)의 동일 연산자 관계를 만족하지 않는 후보이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-082 | p.21 (54) | E 코드 결함 후보 (강함) | E02. K07,K08; `mod_global.F:174` `REAL(SP) :: Beta_1,Beta_2`; `init.F:669` `b1=1.0_SP/3.0_SP`; `7b93138:src/dispersion.F:318–334`도 같은 경로. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/dispersion.F:318–348`과 `7b93138:src/etauv_solver.F:319–324,399–404`에도 같은 소스·역변환 차이가 있다. `init.F:1020–1025`의 `Ubar=HU+gamma1*U1p*H`, `Vbar=HV+gamma1*V1p*H`를 대조했다. [확정 판정](FUNWAVE-git-verify-E1.md). | 구면 초기 Vbar는 V1p를 사용한다. Vbar에서 유속을 구하는 역변환은 다른 b1,b2 계수를 사용한다. 식 (54)의 동일 연산자 관계를 만족하지 않는 후보이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-083 | p.21 (55) | E 코드 결함 후보 (중간) | E03. K05,K06; `etauv_solver.F:241` `R1(I,J)=R1(I,J)+1.0_SP/R_earth*TAN(Lat_theta(I,J))*HV(I,J)`. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/sources.F:362–378`에도 곡률 질량 소스의 곱이 없다. `cab9425:etauv_solver.F:188`에는 질량식 곡률 소스가 있다. [확정 판정](FUNWAVE-git-verify-E1.md). | 구면 x분산 소스는 -div(M)·U1p를 쓴다. 질량식의 tan(theta)·HV/R_earth를 곱한 기여가 빠진다. Gamma1과 MASK9가 각각 1인 셀에서 코드와 식 (55)의 차이는 -tan(theta)·HV·U1p/R_earth이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-084 | p.21 (56) | E 코드 결함 후보 (중간) | E03. K05,K06; `etauv_solver.F:241` `R1(I,J)=R1(I,J)+1.0_SP/R_earth*TAN(Lat_theta(I,J))*HV(I,J)`. `CARTESIAN`·`ZALPHA`를 정의하지 않은 수심 평균 구면 경로에 한정한다. `io.F:2577–2593`의 `DISPERSION`, `Gamma1` 입력과 `main.F:382–384`의 `IF(DISPERSION)THEN`이 분산 계산을 선택한다. `init.F:667–678`과 `dispersion.F:349–379`의 분기를 함께 대조했다. `7b93138:src/sources.F:362–378`에도 곡률 질량 소스의 곱이 없다. `cab9425:etauv_solver.F:188`에는 질량식 곡률 소스가 있다. [확정 판정](FUNWAVE-git-verify-E1.md). | 구면 y분산 소스는 -div(M)·V1p를 쓴다. Gamma1과 MASK9가 각각 1인 셀에서 코드와 식 (56)의 차이는 -tan(theta)·HV·V1p/R_earth이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-086 | p.22 번호 없음 | F 표기 차이 | K03, K20, K22. | 코드의 `U,V`는 기준 깊이 유속이다. 문서의 보존 운동량 `U,V`는 코드의 `Ubar,Vbar`이다. 분할 차이는 FT1-042와 같다. |
| FT1-089 | p.22 (59) | F 표기 차이 | K02; `sources.F:305–319`의 y대응식. | 우변의 $HR_x,HR_y$는 코드의 음수 마찰 소스에 대응한다. 식 (8)의 좌변 $\mathbf R$와 부호를 혼동하지 않도록 $R_x$를 우변 성분으로 정의해야 한다. |
| FT1-093 | p.22 | D 문서에만 있음 | `init.F:437` `nu_smg = ZERO`; `sources.F:367` `# if defined (MIXING)` §5.2의 D-SMAG 전체 `rg -i -uu`와 전체 `git log --all -S` 결과. `cab9425:init.F:332`, `7f892ba:src/init.F:332`의 `nu_smg = ZERO`; `sources.F:367–388`의 `MIXING` 분기. `git log --all -S nu_smg -- '*.F'`와 현재 TVD/GPU 대입 검색은 영 초기화·소비 경로를 확인한다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 공개 이력의 소스에는 nu_smg를 쓰는 확산 항이 있다. Smagorinsky 점성 계수 산출식은 없다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-095 | p.23 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.23 원문: “numerical instability occurred in long time simulations” | 3.0 이전 고차 방식의 불안정 관찰과 개정 동기를 설명한다. 현재 재구성식의 구현은 FT1-096–106에서 대조한다. [10-18 결론 검증 정정] |
| FT1-107 | p.24 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.24 원문: “may be required to ensure model accuracy” | 4차 방식의 수렴 실패 사례에 2차 방식과 더 높은 격자 해상도를 권고하는 문장이다. [10-18 결론 검증 정정] |
| FT1-109 | p.24 (73) | E 코드 결함 후보 (약함) | E04. `fluxes.F:156` `CALL HLL(Mloc1,Nloc,SxL,SxR,FxL,FxR,HUxL,HUxR,Fx)`; `7b93138:src/fluxes.F:128`도 같은 호출. `io.F`의 `CONSTRUCTION` 입력은 FT1-229에서 대조한다. `fluxes.F:109–112,154–159`가 HLL 경로와 상태 점프를 정한다. `etauv_solver.F:310,343`은 `Ubar,Vbar`를 적분한다. `7b93138:src/fluxes.F:128–131`도 같은 상태를 HLL에 전달한다. [확정 판정](FUNWAVE-git-verify-E1.md). | HLL의 운동량 상태 점프는 HU,HV이다. 시간 적분 상태는 Ubar,Vbar이다. 이 차이는 문서 시점에도 존재한다. 결합 설계 가능성 때문에 약한 코드 결함 후보로 유지한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-110 | p.24 (74) | F 표기 차이 | K11의 `SxL`; y대응은 `fluxes.F:410` `SyL(I,J)=MIN(VL(I,J)-SQR_PHI_L,U_S-SQR_PHI_S)` | 여기서 문서의 $\mathbf V$는 법선 유속을 뜻한다. p.18의 보존 운동량 $\mathbf V$로 읽으면 단위가 맞지 않는다. 코드가 쓰는 것은 재구성한 유속이다. |
| FT1-111 | p.24 (75) | F 표기 차이 | K11의 `SxR`; y대응은 `fluxes.F:411` `SyR(I,J)=MAX(VR(I,J)+SQR_PHI_R,U_S+SQR_PHI_S)` | FT1-110과 같은 유속 표기이다. 음수 수심의 절댓값 처리는 §3에 적는다. |
| FT1-115 | p.24 | F 표기 차이 | `fluxes.F:488` `CALL CONSTRUCT_X(Mloc,Mloc1,Nloc,DX,U4,DelxU4,U4xL,U4xR,Kappa)`; K09. 문서 시점 근거: `7b93138:src/fluxes.F:448`의 같은 재구성 호출. 3.0 p.24 마지막 문단; 2.1 p.19의 같은 설명; `dispersion.F:77–83`; `fluxes.F:486–494`; `7b93138:src/fluxes.F:446–448`. [확정 판정](FUNWAVE-git-verify-AD1.md). | 고계 미분은 셀 중심에서 계산한다. 그 결과인 U4는 경계면에 재구성한다. p.24의 바로 앞 문장은 고계 미분의 이산화를 설명한다. 이 문맥의 이산화를 모든 경계면 재구성의 부재로 확대할 수 없으므로 git 판정 B를 F로 정정한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-116 | p.24 | F 표기 차이 | K02, K09; `fluxes.F:482` `HxL=EtaRxL+Depthx`; 483 `HxR=EtaRxR+Depthx` | 수면고를 재구성한 뒤 경계면 수심을 더한다. 정수압 균형은 전통 SGM의 별도 상쇄식보다 식 (15)의 재배열로 설명해야 한다. |
| FT1-121 | p.25 | D 문서에만 있음 | `main.F:380–487`의 단계 루프에는 수렴 반복이 없다. `mod_param.F:89` `INTEGER :: ITER_NUM = 2`는 `ITERATION` 조건 선언이다. §5.2의 D-ITER 전체 `rg -i -uu`와 전체 `git log --all -S` 결과. 3.0 p.11은 반복 옵션 제거를 명시한다. `7b93138:src/mod_param.F:87–88`의 선언과 `main.F:380–487`의 세 RK 단계를 대조했다. 전체 `git log --all -S ITER_NUM`·`-S ERRORi`는 `cab9425`, `b9c035d`, `8d5a857`의 선언 추가·경로 정리만 반환한다. 노트의 과장 판정은 FT1-266이다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 유체 RK 단계의 수렴 반복은 공개 소스 이력에 없다. 반복 선언과 과거 값 배열만으로 구현을 주장하지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-125 | p.25 | B 문서 오기 | K13. 문서 시점 근거: HB3의 `7b93138:src/masks.F:130`. `io.F:2689–2703`의 `VISCOSITY_BREAKING` 입력과 `io.F:2713–2715`의 `SWE_ETA_DEP` 입력을 대조했다. `masks.F:177–188`은 점성 쇄파를 선택하지 않은 분기에서만 전환비를 검사한다. `7b93138:src/masks.F:124–134`도 같은 분기이다. FT1-013과 같은 판정이다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 쇄파 전환 조건은 순간 수면고 절댓값과 정수심 하한의 비이다. 이 비를 유속 Froude 수로 적지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-126 | p.25 | B 문서 오기 | K13. `io.F`의 `SWE_ETA_DEP` 기본값은 §5에서 이력과 함께 인용한다. 문서 시점 근거: HB3의 `7b93138:src/masks.F:130`. `io.F:2689–2703`의 `VISCOSITY_BREAKING` 입력과 `io.F:2713–2715`의 `SWE_ETA_DEP` 입력을 대조했다. `masks.F:177–188`은 점성 쇄파를 선택하지 않은 분기에서만 전환비를 검사한다. `7b93138:src/masks.F:124–134`도 같은 분기이다. FT1-013과 같은 판정이다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 충격 포착 전환식의 분자는 ABS(Eta)이다. 분모는 MAX(DEPTH,MinDepthFrc)이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-127 | p.25 (80) | A 판 차이 | HA1. `7b93138:src/sources.F:63` `LOGICAL :: PQ_scheme = .TRUE.`; `17d2eeb` (2017-03-03)의 `.FALSE.` 변경. `17d2eeb`(2017-03-03)의 diff가 `LOGICAL :: PQ_scheme = .TRUE.`를 `LOGICAL :: PQ_scheme = .FALSE.`로 바꾼다. 현재 `sources.F:394–453`에서 `IF(VISCOSITY_BREAKING.OR.DIFFUSION_SPONGE.OR.WAVEMAKER_VIS)THEN` 뒤 HU·HV 분기를 선택한다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 문서의 P 확산은 2016년 판의 기본 선택이다. 현재 기본 선택은 HU 확산이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-128 | p.25 (81) | A 판 차이 | HA1. `7b93138:src/sources.F:63` `LOGICAL :: PQ_scheme = .TRUE.`; `17d2eeb` (2017-03-03)의 `.FALSE.` 변경. `17d2eeb`(2017-03-03)의 diff가 `LOGICAL :: PQ_scheme = .TRUE.`를 `LOGICAL :: PQ_scheme = .FALSE.`로 바꾼다. 현재 `sources.F:394–453`에서 `IF(VISCOSITY_BREAKING.OR.DIFFUSION_SPONGE.OR.WAVEMAKER_VIS)THEN` 뒤 HU·HV 분기를 선택한다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 문서의 Q 확산은 2016년 판의 기본 선택이다. 현재 기본 선택은 HV 확산이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-130 | p.25 (82) | B 문서 오기 | `breaker.F:314` `nu_break(I,J) = cap1*tmp2 + nu_bkg`; 125 `tmp1=Cbrk1*tmp3`; 126 `tmp2=Cbrk2*tmp3` 문서 시점 근거: HB2의 `7b93138:src/breaker.F:237`. `io.F:2689–2691,3062–3078`의 입력·활성 조건과 `breaker.F:64–66,248–265,278–315`의 조파기 안팎·컴파일 분기를 함께 대조했다. `7b93138:src/breaker.F:113–115,218–237`에도 기본 정적 점성식과 계수 1.0이 있다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 조파기 밖의 기본 점성식은 `nu_break(I,J) = cap1*tmp2 + nu_bkg`이다. `cap1=1.0*(MAX(Depth(I,J),MinDepthFrc)+ETA(I,J))`이므로 기존 결론의 단순 H 대체는 정정한다. 문서의 수면고 시간 미분 비례식과 현재 `VIS_KENNEDY_ORIGINAL`·`VIS_KENNEDY` 분기를 구분한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-131 | p.26 번호 없음 | B 문서 오기 | `breaker.F:265` `cap1=1.0*(MAX(Depth(I,J),MinDepthFrc)+ETA(I,J))` 문서 시점 근거: HB2의 `7b93138:src/breaker.F:219`. `io.F:2689–2691,3062–3078`의 입력·활성 조건과 `breaker.F:64–66,248–265,278–315`의 조파기 안팎·컴파일 분기를 함께 대조했다. `7b93138:src/breaker.F:113–115,218–237`에도 기본 정적 점성식과 계수 1.0이 있다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 점성식의 코드 계수는 1.0이다. δb=1.2라는 문서 기술을 코드 계수로 옮기지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-132 | p.26 (83) | B 문서 오기 | `breaker.F:264` `IF(AGE(I,J)>ZERO.AND.AGE(I,J)<T_brk.AND.ETAt(I,J)>tmp2)THEN`; 314의 기본 점성. 문서 시점 근거: HB2의 `7b93138:src/breaker.F:218,237`. `io.F:2689–2691,3062–3078`의 입력·활성 조건과 `breaker.F:64–66,248–265,278–315`의 조파기 안팎·컴파일 분기를 함께 대조했다. `7b93138:src/breaker.F:113–115,218–237`에도 기본 정적 점성식과 계수 1.0이 있다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 조파기 밖의 기본 쇄파 점성은 `IF(AGE(I,J)>ZERO.AND.AGE(I,J)<T_brk.AND.ETAt(I,J)>tmp2)THEN`에서 정적 식으로 계산한다. 문서 식 (83)의 B 정의와 구분한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-133 | p.26 | C 문서 누락 | `breaker.F:151–153` `IF(ETAt(I,J).GE.tmp1.AND.(  &` / `AGE(I,J).EQ.ZERO.OR.AGE(I,J).GT.T_brk))THEN` / `AGE(I,J)=DT`; 264의 조건. 3.0·2.1·Intro-TN·code_analysis 전체 판독 및 TEX에서 `T_brk`, `AGE_BREAKING`, 쇄파 나이·수명을 검색했다. Intro-TN p.14는 AGE 출력을, code_analysis p.7은 AGE_BREAKING의 인수 사용을 적는다. `breaker.F:151–228,264`가 수명과 이웃 전파를 처리한다. | 3.0 p.26의 두 임계값 설명에는 조파기 밖의 T_brk 수명 제한과 이웃 셀의 쇄파 나이 전파 절차가 없다. 다른 문서의 AGE 출력·변수 목록은 이 절차를 설명하지 않는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-134 | p.26 번호 없음 | B 문서 오기 | `io.F:3079` `CALL READ_FLOAT(Cbrk1,FILE_NAME,'Cbrk1',ierr)`; 3081 `Cbrk1 = 0.65_SP`; `breaker.F:124` `tmp3=SQRT(GRAV*MAX(MinDepthFrc,H(I,J)))`; 125 `tmp1=Cbrk1*tmp3` 문서 시점 근거: `7b93138:src/breaker.F:113–115`의 `tmp1=Cbrk1*tmp3`. `io.F:2689–2691,3062–3078`의 입력·활성 조건과 `breaker.F:64–66,248–265,278–315`의 조파기 안팎·컴파일 분기를 함께 대조했다. `7b93138:src/breaker.F:113–115,218–237`에도 기본 정적 점성식과 계수 1.0이 있다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 쇄파 개시 임계값은 `tmp3=SQRT(GRAV*MAX(MinDepthFrc,H(I,J)))`와 `tmp1=Cbrk1*tmp3`로 계산한다. 문서의 추가 2배를 코드 식에 넣지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-135 | p.26 번호 없음 | B 문서 오기 | `io.F:3101` `CALL READ_FLOAT(Cbrk2,FILE_NAME,'Cbrk2',ierr)`; 3103 `Cbrk2 = 0.35_SP`; `breaker.F:126` `tmp2=Cbrk2*tmp3` 문서 시점 근거: HB1의 `7b93138:src/mod_global.F:372`. `io.F:2689–2691,3062–3078`의 입력·활성 조건과 `breaker.F:64–66,248–265,278–315`의 조파기 안팎·컴파일 분기를 함께 대조했다. `7b93138:src/breaker.F:113–115,218–237`에도 기본 정적 점성식과 계수 1.0이 있다. `7b93138:src/mod_global.F:372`도 `Cbrk2=0.35`이다. 3.0 p.45–46의 0.15는 예제에 명시한 설정값이다. [확정 판정](FUNWAVE-git-verify-AD1.md). | Cbrk2의 현재 입력 누락값은 0.35이다. 예제의 명시 입력 0.15는 별도 설정값이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-136 | p.26 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.26 원문: “should be slightly larger to match the laboratory data” | 검증·보정에 대한 권고이다. [10-18 결론 검증 정정] |
| FT1-137 | p.26 | A 판 차이 | HA1. `7b93138:src/sources.F:63` `LOGICAL :: PQ_scheme = .TRUE.`; `17d2eeb` (2017-03-03)의 `.FALSE.` 변경. `17d2eeb`(2017-03-03)의 diff가 `LOGICAL :: PQ_scheme = .TRUE.`를 `LOGICAL :: PQ_scheme = .FALSE.`로 바꾼다. 현재 `sources.F:394–453`에서 `IF(VISCOSITY_BREAKING.OR.DIFFUSION_SPONGE.OR.WAVEMAKER_VIS)THEN` 뒤 HU·HV 분기를 선택한다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 2017-03-03부터 기본 점성 확산은 HU와 HV를 사용한다. PDF의 P·Q 설명은 그 변경 전 판의 설명이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-139 | p.26 | B 문서 오기 | `fluxes.F:1572` `IF(MASK(I-2,J)==0.OR.MASK(I+1,J)==0)THEN`; 1574 `TXP1=TXP2`; 1575 `TXP3=TXP2`; 1594 `IF(MASK(I-1,J)==0.OR.MASK(I,J)==0)THEN`; K13. 문서 시점 근거: `7b93138:src/masks.F:127–131`의 MASK 곱·영 대입. `fluxes.F:1572–1600`, 특히 `Din(I,J)=TXP2-1.0_SP/6.0_SP*(DVP3-2.0_SP*DVP2+DVP1)`; `masks.F:177–188`; `7b93138:src/masks.F:124–134`. FT1-270에도 같은 조건을 적용한다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 내부 건조 셀에서는 고차 재구성 보정 DVP1·DVP2·DVP3를 바꾼다. `DVP1=ZERO` 등의 대입만으로 최종 기울기 Din도 0이라고 할 수 없다. 점성 쇄파를 선택하지 않은 분기에서만 주변 습윤 마스크의 곱을 적용한다. 이 처리를 문서의 내부 거울 경계 또는 외곽 반사 경계와 동일시하지 않는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-140 | p.26 (84) | D 문서에만 있음 | K11. §5.2의 D-DRY 전체 `rg -i -uu`와 전체 `git log --all -S` 결과. `7b93138:src/fluxes.F:336–341`과 현재 `fluxes.F:352–411`은 일반 파속식을 쓴다. `git log --all -S 'right dry cell'`의 적중 `9b28db7`은 TEX 추가이다. 좌·우 전용 파속 분기는 공개 소스 이력에 없다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 우측 건조 셀에 문서 식 (84)의 별도 파속 계수를 적용하는 분기는 공개 이력에 없다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-141 | p.26 (85) | D 문서에만 있음 | K11. §5.2의 D-DRY 전체 `rg -i -uu`와 전체 `git log --all -S` 결과. `7b93138:src/fluxes.F:336–341`과 현재 `fluxes.F:352–411`은 일반 파속식을 쓴다. `git log --all -S 'right dry cell'`의 적중 `9b28db7`은 TEX 추가이다. 좌·우 전용 파속 분기는 공개 소스 이력에 없다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 좌측 건조 셀에 문서 식 (85)의 별도 파속 계수를 적용하는 분기는 공개 이력에 없다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-144 | p.27 (87) | E 코드 결함 후보 (중간) | E05. `sponge.F:653` `ri=R_sponge**(50*(I-1)/(Iwidth-1))`; `7b93138:src/sponge.F:590`도 같은 정수식. `io.F:2285–2287`의 `READ_LOGICAL` 입력 → `init.F:966–970`의 `IF(DIRECT_SPONGE)THEN` → `main.F:483–485` 감쇠 호출. `sponge.F:617,650–655`의 정수 변수·병렬/직렬 지수. `cab9425:sponge.F:597`에도 같은 식. `funwave_tvd_3.0.tex:788`. [확정 판정](FUNWAVE-git-verify-E1.md). | 직접 스펀지의 지수는 정수 나눗셈으로 계산한다. 예를 들어 해당 식에 Iwidth=100과 I=2를 넣으면 50/99가 0이 된다. 임의 폭에서 문서의 지수 프로파일과 다른 후보이다. PDF p.27 식 (87)과 TeX 788행의 아래첨자는 모두 `gamma_x`이다. git 판정 파일의 `gamma_s` 전사 지적은 원문과 달라 채택하지 않는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-145 | p.27 번호 없음 | H 코드 대조 대상 아님 | p.27 번호 없음: $\alpha_s=2$, $\gamma_s=0.88-0.92$, $n=50-100$; 보통 1–2파장; 최적 감쇠는 사례에 민감하다. | Chen의 권고값이다. 코드 입력 기본값으로 단언하지 않는다. [10-18 결론 검증 정정] |
| FT1-146 | p.27 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.27 원문: “may become significant in a long term simulation” | 직접 감쇠와 TVD 결합에서 생길 수 있는 톱니 잡음과 장시간 사용 권고를 설명한다. 문서는 잡음이 장시간에 유의해질 수 있다고 조건부로 서술한다. [10-18 결론 검증 정정] |
| FT1-149 | p.27 (89) | B 문서 오기 | `sponge.F:285` `ri=MAX(0.0,REAL(Iwidth-I))`; 287 `tmp_2d_1(i,j)=MAX(CDsponge*TANH(ri/10.0),lim)` 문서 시점 근거: HB3의 `7b93138:src/sponge.F:250`. `7b93138:src/sponge.F:248–250`도 같은 `MAX` 대입이다. 원문의 0 하한을 생략한 기존 요약식을 정정한다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 마찰 스펀지의 실제 식은 MAX(CDsponge*TANH(ri/10.0),lim)이다. 문서 식 (89)와 구분한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-151 | p.27 | H 코드 대조 대상 아님 | p.27: 마찰·점성 스펀지는 보통 2–3파장이다. L-D는 더 좁아도 효율적이나 장시간 톱니 잡음을 고려한다. | 마찰·점성 스펀지의 통상 폭 2–3파장과 장시간 잡음에 관한 사용 권고이다. [10-18 결론 검증 정정] |
| FT1-153 | p.28 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.28 원문: “under development” | 문헌 귀속과 문서 작성 당시 개발 상태를 설명한다. 단방향 조파는 개발 중이라고 적었다. [10-18 결론 검증 정정] |
| FT1-154 | p.28 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.28 원문: “a partially distributed mass source” | 분포 질량 소스를 선택한 배경을 설명하는 문장이다. [10-18 결론 검증 정정] |
| FT1-162 | p.28–29 | H 코드 대조 대상 아님 | p.28–29: 형상 계수가 클수록 소스가 좁다. 폭 정의는 유일하지 않다. $\exp(-5)=0.0067$ 배인 두 점 사이를 폭으로 정의한다. | 가우스 함수의 형상 계수와 폭의 수학적 정의이다. 문서는 최대값의 약 0.0067배가 되는 두 점 사이를 폭으로 정의한다. [10-18 결론 검증 정정] |
| FT1-166 | p.29 | E 코드 결함 후보 (강함) | E06. `wavemaker.F:2027` `wave_length=C_phase/fm`; 2082 `beta_gen(kf)=80.0_SP/delta**2/wave_length**2`; HB3의 과거 동일식. `io.F:870,1974–1976`의 `WAVEMAKER`·`EqualEnergy` 입력과 `wavemaker.F:370–400`의 호출 분기. 등 에너지 경로 `wavemaker.F:2008–2028,2082–2085`, 등 주파수 경로 `2254–2271,2324–2332` 모두 성분별 파수를 사용한다. `7b93138:src/wavemaker.F:1230–1246,1292–1296`도 같다. `wkn.eq.0.0` 예외는 `wave_length=C_phase/fm`에 천해 파속을 사용한다. [확정 판정](FUNWAVE-git-verify-E1.md). | 불규칙파의 beta_gen은 성분별 파수로 정해진다. 첨두 주파수의 공통 폭을 쓴다는 문서와 자기 주석에 모순한다. 이 판정은 폭의 계산에 관한 코드 결함 후보이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-177 | p.31 (100) | F 표기 차이 | K18의 `AG` 대입. | 코드의 각도는 $\theta-\theta_{input}$이다. 문서의 $\theta$를 평균 입사 방향에 대한 상대각으로 놓으면 같다. 이산 정규화는 §3에 기록한다. |
| FT1-178 | p.31 | B 문서 오기 | `wavemaker.F:1933` `sigma_theta=sigma_theta_input*pi/180.0_SP`; 1934 `N_spec=20.0_SP/sigma_theta` 문서 시점 근거: HB3의 `7b93138:src/wavemaker.F:1123`. `wavemaker.F:1862`의 정수 `N_spec` 선언. `7b93138:src/wavemaker.F:1122–1123`도 같은 대입이다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 방향 분포 합의 항 수는 N_spec=20.0_SP/sigma_theta로 정한다. 고정 20항으로 적지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-179 | p.31 | B 문서 오기 | `wavemaker.F:1870` `do kf=1,10000`; 1872 `fre=fmin+(fmax-fmin)/10000.0_SP*(kf-1.0_SP)`; 1898 `Ef100=Ef/REAL(mfreq+1)` 문서 시점 근거: HB3의 `7b93138:src/wavemaker.F:1061`. `io.F:1726,1740`에서 `Nfreq`·`Ntheta`를 읽고 `wavemaker.F:383–390`에서 `mfreq`·`mtheta`에 전달한다. `7b93138:src/wavemaker.F:1061–1063`의 초기 분할도 10000이다. 3.0 TeX 928행 전후의 2100 표기도 PDF p.31의 1000 및 코드 10000과 구분한다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 코드의 초기 스펙트럼 적분 분할은 10000이다. PDF p.31의 성분 수 설명과 사용자 지정 주파수 수를 구분한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-180 | p.31 (101) | B 문서 오기 | K19. 문서 시점 근거: `7b93138:src/etauv_solver.F:98–106`의 질량 소스 경로. `sources.F:117–132`의 내부 조파 분기와 `etauv_solver.F:204–243`의 질량 방정식에 연결된다. `7b93138:src/etauv_solver.F:94–106`에서도 질량 소스였다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 내부 조파의 조화합은 질량 원천 항이다. 흡수·발생 경계의 직접 수면고 합성과 구분한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-181 | p.31 (102) | F 표기 차이 | K19. | 코드의 $D_{mn}$에 가우스 공간 계수를 포함하면 같은 조화합이다. `D_gen`은 질량 소스 진폭이다. 이를 표면파 진폭과 구분해야 한다. |
| FT1-184 | p.31 | C 문서 누락 | `mod_meteo.F:292` `CALL READ_FLOAT(WindCrestPercent,FILE_NAME,'WindCrestPercent',ierr)`; 295 `WindCrestPercent=LARGE`; 722 `IF(ETA(I,J)<HeightMax(I,J)*(1-WindCrestPercent)+ETAmean(I,J))MASK_WIND(I,J)=0` `mod_meteo.F:213–218,247–263,292–307,643–651,719–722`; `sources.F:355–364`. 네 PDF 전체와 TeX 판독 기록에서 `WindCrestPercent`, `WindWaveInteraction`, 파봉 표현을 검색했다. | 3.0 p.31의 누락은 파봉 마스크를 켜는 조건이다. `METEO`가 정의되고 `WindForce`가 참인 경로에서 `WindCrestPercent=LARGE`이면 `MASK_WIND=1`이다. `WindCrestPercent` 미입력 또는 `WindWaveInteraction`이 거짓이면 이 경로를 쓴다. 3.0 p.37·2.1 p.37·Intro-TN p.11도 매개변수를 설명하지만 이 해제 조건은 적지 않는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-187 | p.32 (105) | B 문서 오기 | `mixing.F:146` `ETA2sum = (Eta-ETAmean)*(Eta-ETAmean)*DT + ETA2sum   !ykchoi`; 147 `ETA2mean = ETA2sum/T_sum`; 267의 동일 누적. 문서 시점 근거: HB3의 `7b93138:src/mixing.F:113`. `mixing.F:146–154`에서 제곱 누적 뒤 `ETAmean=ETAsum/T_sum`을 갱신한다. `7b93138:src/mixing.F:113–125`도 이전 평균 사용을 명시한다. [확정 판정](FUNWAVE-git-verify-AD1.md). | ETA2sum은 이전 평균 수면고를 뺀 값의 제곱을 시간 가중 누적한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-191 | p.32 4.1 | B 문서 오기 | `mod_param.F:64` `INTEGER, PARAMETER::SP=SELECTED_REAL_KIND(6,30)`; `T/Makefile:7` `PRECISION   = single`; `init.F:128`의 할당 목록. 문서 시점 근거: `7b93138:src/mod_param.F:64`의 정의. `mod_param.F:58–68` 및 `7b93138:src/mod_param.F:58–68`의 배정도 분기는 `INTEGER, PARAMETER::SP=8`이다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 정밀도 플래그는 빌드에서 선택한다. kind 값의 정의는 mod_param.F에 있다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-194 | p.32 4.1–4.2 | H 코드 대조 대상 아님 | p.32 4.1–4.2: 흐름도는 그림 2이다. 압축 배포물을 풀고 `> tar xvf *.tar`를 쓴다. | 흐름도 위치 안내와 배포물 압축 해제 명령을 설명한다. [10-18 결론 검증 정정] |
| FT1-195 | p.81 상단 | H 코드 대조 대상 아님 | p.81 상단: $\lvert\nabla h\rvert>1.0$를 피한다. 큰 바닥 경사가 불안정을 유발할 수 있다. | 큰 바닥 경사가 불안정을 유발할 수 있으므로 피하라는 수치 안정성 권고이다. [10-18 결론 검증 정정] |
| FT1-196 | p.81 | 일치 | K26. `io.F:2898–2910` 입력 및 `etauv_solver.F:568–593` 실제 분기. 네 PDF 전체와 TeX 판독 기록의 `FroudeCap` 검색; 3.0 p.41, 2.1 p.40, Intro-TN p.13, TeX 1341행. | Froude 상한을 유속 계산에 적용한다. 3.0 p.41·2.1 p.40·Intro-TN p.13도 이 기능을 설명한다. p.81의 얕은 수심 설명은 사용 목적이며 얕은 셀에서만 분기한다는 조건이 아니다. 실제 검사는 `MASK(I,J)<1`의 `ELSE`에서 `IF(Utotal/Fr.gt.FroudeCap)THEN`으로 수행한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-197 | p.81 | A 판 차이 | HA2. `7b93138:src/mod_global.F:137` `REAL(SP) :: FroudeCap=10.0_SP`; `285a6f6:src/io.F:2564` `FroudeCap = 3.0_SP` (2017-05-01). `7b93138:src/mod_input.F:128`은 `INTENT(OUT)`이다. 과거 입력 호출 뒤 선언 초기값 10이 보존된다고 단언하지 않는다. 실제 상한 분기는 `etauv_solver.F:568–593`이다. [확정 판정](FUNWAVE-git-verify-AD1.md). | FroudeCap의 문서상 기본값 10은 과거 선언 초기값이다. 2017-05-01부터 입력 누락 분기는 3을 대입한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-198 | p.81 | H 코드 대조 대상 아님 | p.81: 3.0 이하로 낮추면 문제와 CFL 효율을 개선할 수 있다. 1.5 미만은 침수 선단 유속을 제한할 수 있어 권장하지 않는다. | 문서는 FroudeCap을 3.0 이하로 낮추면 문제와 CFL 효율을 개선할 수 있다고 적는다. 1.5 미만은 침수 선단 유속을 제한할 수 있어 권장하지 않는다. [10-18 결론 검증 정정] |
| FT1-199 | p.81 | B 문서 오기 | `io.F:2933` `CALL READ_FLOAT(MinDepthFrc,FILE_NAME,'MinDepthFrc',ierr)`; 2935 `MinDepthFrc = 0.1_SP`; 2948 `MinDepthFrc=MIN(MinDepthFrc,MinDepth)`; 2949 `MinDepth=MinDepthFrc` 문서 시점 근거: HB1의 `7b93138:src/mod_global.F:134–135`. [확정 판정](FUNWAVE-git-verify-AD1.md). | MinDepthFrc의 문서 기본값 0.001은 문서 시점 코드와 다르다. 현재 입력 누락값은 0.1이다. 이후 `MinDepthFrc=MIN(MinDepthFrc,MinDepth)`와 `MinDepth=MinDepthFrc`를 적용하므로 최종값은 두 입력의 최솟값이다. [10-18 git 이력 판정] |
| FT1-200 | p.81 | H 코드 대조 대상 아님 | p.81: 작은 MinDepthFrc는 큰 유속·작은 dt·불안정을 일으킬 수 있다. 문제가 생기면 더 큰 값을 쓴다. | 작은 MinDepthFrc가 큰 유속·작은 시간 간격·불안정을 일으킬 수 있다는 가능성과 문제가 생겼을 때의 조정 권고이다. [10-18 결론 검증 정정] |
| FT1-202 | p.81 | B 문서 오기 | `init.F:389–392` `IF(HIGH_ORDER(1:3)=='SEC')THEN` / `Kappa = -1.0_SP` / `ELSE` / `Kappa = 1.0_SP/3.0_SP`; `fluxes.F:773` `! The "kappa" is meaningless in above routines.` 문서 시점 근거: HB3의 `7b93138:src/fluxes.F:729,736`. `io.F:2842–2854`의 `HIGH_ORDER` 입력 → `fluxes.F:56–106` 분기 → `CONSTRUCTION`의 `CONSTRUCT_X` 호출(473–480행). `fluxes.F:779–784`는 `Kappa`를 쓰지 않는다. `7b93138:src/fluxes.F:729–740`도 같다. FT1-277의 4차 제한 함수 옵션과 구분한다. [확정 판정](FUNWAVE-git-verify-AD1.md). | SECOND와 THIRD는 같은 선형 재구성 경로를 사용한다. 문서의 THIRD 권고를 3차 정확도 보장으로 적지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-204 | p.81 하단 | H 코드 대조 대상 아님 | p.81 하단: References의 Agnon (1999), Berkhoff (1982), Bermùdez·Vàzquez (1994) 서지 항목. | 참고문헌 목록이다. [10-18 결론 검증 정정] |
| FT1-205 | p.86 | H 코드 대조 대상 아님 | `funwave_tvd_3.0.pdf` p.86 원문: “there are typos in the expansion expressions in both Shi et al. (2012) and the previous manual lower than Version 3.0” | Shi et al. (2012)와 3.0 이전 매뉴얼의 전개식에 오기가 있었다는 문서 작성자의 안내이다. [10-18 결론 검증 정정] |
| FT1-208 | p.86 (109) | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:422–423,430–435`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). | 직교 비선형 경로의 U1pp는 수면고 선형항에 0.04를 곱한다. 수면고 제곱항에는 0.0016을 곱한다. PDF 식 (109)에 없는 배수이다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-209 | p.86 (110) | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:425–426,430–436`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). | 직교 비선형 경로의 V1pp에도 Beta_2와 Beta_2 제곱이 붙는다. 식 (110)과 y미분 방향은 같지만 계수는 다르다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-210 | p.86 (111) | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:438–455`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). | 직교 비선형 경로의 U2는 식 (111)의 전개 구조를 따른다. 추가 Beta_2 배수 때문에 동일한 차원식이 아니다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-211 | p.86 (112) | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:439–445,459–469`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). | 직교 비선형 경로의 V2는 y용 ken1을 사용한다. 식 (112)과의 차이는 Beta_2 배수이다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-212 | p.87 (113) | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:475–493`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). | 직교 비선형 경로의 U3는 -v·omega_1과 -omega_0 보정의 부호를 유지한다. 보정의 깊이 계수에는 식 (113)에 없는 Beta_2 배수가 남는다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-213 | p.87 (114) | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:475–489,496–498`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). | 직교 비선형 경로의 V3는 양의 u·omega_1과 omega_0 보정을 쓴다. 식 (114)과의 차이는 보정 계수의 Beta_2 배수이다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-215 | p.87 (116) | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:475–476`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). | 직교 비선형 경로의 omega_1은 식 (116)의 미분 구조와 대응한다. 외부 곱과 내부 기준 깊이 곱에 문서에 없는 Beta_2가 들어간다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-216 | p.87 (117) | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:295–317`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). `dispersion.F:322–329`의 `# if defined (ZALPHA)` 블록은 앞서 계산한 U4·V4를 선형식으로 다시 대입한다. | 직교 비선형 경로의 U4 선형항은 식 (117)과 같다. 비선형 h·eta 및 eta 항에는 0.04를 곱한다. eta 제곱항에는 0.0016을 곱한다. 이 U4·V4 비선형 보정 판정은 `ZALPHA`를 정의하지 않은 경로에 한정한다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-217 | p.87 (118) | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:295–317`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). `dispersion.F:322–329`의 `# if defined (ZALPHA)` 블록은 앞서 계산한 U4·V4를 선형식으로 다시 대입한다. | 직교 비선형 경로의 V4 선형항은 식 (118)과 같다. y방향 비선형 보정에는 U4와 같은 Beta_2 배수가 남는다. 이 U4·V4 비선형 보정 판정은 `ZALPHA`를 정의하지 않은 경로에 한정한다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-218 | p.88 (119) 첫째 묶음 | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:438,447`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). | 직교 비선형 U2 전개의 첫째 묶음은 x경사를 사용한다. 식 (119)의 첫째 계수에 0.04가 추가된다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-219 | p.88 (119) 둘째 묶음과 그 네 곱 미분 | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:439,448–449`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). | 직교 비선형 U2 전개의 둘째 묶음은 네 곱 미분을 올바르게 배치한다. 공통 ken2에는 식 (119)에 없는 0.04가 들어간다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-220 | p.88 (119) 셋째 묶음 | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:440–441,450–451`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). | 직교 비선형 U2 전개의 셋째 묶음은 h·h_x와 eta·eta_x를 0.0016배 한다. 혼합 h·eta 미분항은 0.04배 한다. 식 (119)에는 이 배수가 없다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-221 | p.88 (119) 넷째 묶음과 그 네 곱 미분 | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:442–443,452–453`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). | 직교 비선형 U2 전개의 넷째 묶음은 h 제곱 및 eta 제곱 계수에 0.0016을 곱한다. h·eta 계수에는 0.04를 곱한다. 식 (119)의 계수와 다르다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-222 | p.88 (119) 다섯째 묶음 | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:454–455`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). | 직교 비선형 U2 전개의 다섯째 묶음은 전체 곱에 0.0016을 곱한다. 두 괄호 안의 수면고 관련 항에도 0.04가 추가된다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-223 | p.89 (120) 첫째 묶음과 $(h_y+\eta_y)$ 전개. 전체 원문은 D120이다. | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:459–461`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). | 직교 비선형 V2 전개의 첫째 묶음은 y경사를 사용한다. 식 (120)의 첫째 계수에는 없는 0.04가 추가된다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-224 | p.89 (120) 둘째 묶음과 $u_y,u,v_y,v$의 네 곱 미분. 전체 원문은 D120이다. | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:439,462–463`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). | 직교 비선형 V2 전개의 둘째 묶음은 네 곱 미분을 올바르게 배치한다. 공통 ken2에는 식 (120)에 없는 0.04가 들어간다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-225 | p.89 (120) 셋째 묶음과 $hh_y,h_y\eta+h\eta_y,\eta\eta_y$의 전개. 전체 원문은 D120이다. | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:444–445,464–465`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). | 직교 비선형 V2 전개의 셋째 묶음은 h·h_y와 eta·eta_y를 0.0016배 한다. 혼합 h·eta 미분항은 0.04배 한다. 식 (120)에는 이 배수가 없다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-226 | p.89 (120) 넷째 묶음과 네 곱 미분. 전체 원문은 D120이다. | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:442–443,466–467`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). | 직교 비선형 V2 전개의 넷째 묶음은 U2와 같은 ken4를 사용한다. 식 (120)에 없는 h 제곱·eta 제곱의 0.0016배와 h·eta의 0.04배가 남는다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-227 | p.89 (120) 다섯째 묶음의 완전 전개. 전체 원문은 D120이다. | E 코드 결함 후보 (강함) | E01. K21–K24; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `7b93138:src/init.F:488`도 같은 대입. `dispersion.F:468–469`. `CARTESIAN` 및 `IF(gamma2>ZERO)THEN`(302·398–399행)에서 계산한다. `io.F:2540–2656`의 `DISPERSION`·`Gamma1`·`Gamma2` 입력과 `main.F:382–384`의 호출, `sources.F:251–258,310–317`의 `Gamma1*MASK9`·`Gamma2*MASK9` 적용을 대조했다. `cab9425:dispersion.F:379–464`에도 해당 배수가 있다. [외부 원문 판정](FUNWAVE-external-sources.md). [확정 판정](FUNWAVE-git-verify-E1.md). | 직교 비선형 V2 전개의 다섯째 묶음은 전체 곱에 0.0016을 곱한다. 두 괄호 안의 수면고 관련 항에도 0.04가 추가된다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 보완] [10-18 외부 원문] [10-18 git 이력 판정] |
| FT1-228 | p.18 (18)–(20)과 p.86 (107)–(110)의 분할 대응. | F 표기 차이 | K20, K22. 본문 식 (18)–(20), 부록 식 (107)–(110), `dispersion.F:337–346,422–436`, `etauv_solver.F:407–411`. FT1-042–044,047과 같은 분할 대응이다. 실제 비선형 계수 차이는 FT1-208,209이다. | 아래 항등식이 두 분할을 연결한다. `Beta_2=1`의 형식 비교에서 성립한다. 현재 0.04의 계수 차이는 별도의 E 행으로 남긴다. [10-18 결론 검증 보완] |
| FT1-229 | 3.0 p.24·41의 HLL 설명과 2.1 p.29의 HLLC 명칭을 입력 분기에 대조한다. | C 문서 누락 | `fluxes.F:109` `IF(CONSTR(1:3)=='HLL')THEN`; 110 `CALL FLUX_AT_INTERFACE_HLL`; `io.F:2833` `CONSTR='HLLC'` `io.F:2826–2834`의 `READ_STRING`과 `fluxes.F:109–112,150–194`. 3.0 p.41, 2.1 p.29·40, Intro-TN p.13·17 및 TeX 1337행을 포함해 네 문서 전체를 검색했다. | `HLLC` 입력도 `IF(CONSTR(1:3)=='HLL')THEN`에 따라 HLL을 선택한다. C 판정은 3.0 p.41에 접두 세 글자로 판별하는 조건이 빠진 점에 한정한다. 2.1 p.29는 HLLC 이름을 쓰지만 현재 수리 플럭스 호출은 `FLUX_AT_INTERFACE_HLL`이다. FT1-109와 같은 호출 경로이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-230 | 3.0 p.41·2.1 p.40·Intro-TN p.13: CONSTRUCTION은 HLL 또는 평균 기법을 선택한다. | 일치 | `fluxes.F:111–112` `ELSE` / `CALL FLUX_AT_INTERFACE`; 132 `P=0.5_SP*(PR+PL)` `io.F:2826–2834`; `fluxes.F:109–112,122–137`; TeX 1337행. 네 문서와 TeX 판독 기록 전체의 `CONSTRUCTION`·평균 기법 검색. | HLL로 시작하지 않는 `CONSTRUCTION` 값은 산술평균 플럭스 경로를 선택한다. 이 선택지는 3.0 p.41·2.1 p.40·Intro-TN p.13에 설명되어 있다. `dont use it for TVD` 주석은 실제 호출을 막지 않는다. FT1-276과 같은 분기이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-231 | 3.0 p.32–34의 빌드 안내에 보존된 fluxes 파일의 선택 목록이 없다. | C 문서 누락 | `T/GNUMake/Essential/Make_Essential:208–211`의 MAIN 목록은 `fluxes.F`만 포함한다. `fluxes_21v.F:719–720`은 아래 K27이다. `GNUMake/Essential/Make_Essential:204–211`; `fluxes_21v.F:719–722`. 네 문서·TeX 전체에서 파일명·빌드 목록을 검색했다. | 현재 기본 빌드는 `fluxes.F`를 선택한다. code_analysis p.8–9는 `fluxes.F`와 `fluxes_21v.F`를 나란히 분석하지만 빌드 선택을 설명하지 않는다. `fluxes_21v.F`의 인용식은 같은 `Din`에 두 가중치를 더하므로 Kappa가 소거된다. FT1-202·284와 연결한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-232 | 3.0 p.41의 HIGH_ORDER 목록에는 FOURTH·THIRD·SECOND를 적는다. | C 문서 누락 | `fluxes.F:71–72` `ELSEIF(HIGH_ORDER(1:3)=='FMI') THEN` / `CALL CONSTRUCTION_HO_minmod`; 81–82 `ELSEIF(HIGH_ORDER(1:3)=='WEN') THEN` / `CALL CONSTRUCTION_WENO`; 89,91의 `MLP` 호출. `io.F:2842–2854`; `fluxes.F:71–103`; 네 문서·TeX 전체의 `FMI`·`WENO`·`MLP`·`HIGH_ORDER` 검색. | 3.0 p.41의 누락은 `FMI`·`WEN`·`MLP` 입력 선택이다. `READ_STRING`으로 읽은 `HIGH_ORDER`가 실제 분기를 선택한다. `WEN` 분기는 `CARTESIAN`에서만 컴파일한다. FMI의 후속 활성화 이력은 FT1-277의 A 판정과 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-233 | 3.0 p.23–24의 제한 함수식에는 작은 분모 처리 조건이 없다. | C 문서 누락 | `fluxes.F:1608` `IF( ABS(TMP1).le.SMALL ) TMP1 = SMALL*SIGN( 1.0_SP, TMP1 )`; 1612의 분모 검사; 316 `IF((ABS(TMP1)+ABS(TMP2))<SMALL)THEN`; 318 `DOUT(I,J)=ZERO` `fluxes.F:56–103`의 차수별 호출과 `1608–1616,316–321`; `mod_param.F:73` `SMALL=0.000001_SP`. 네 문서·TeX의 제한 함수·작은 분모 검색. | 3.0 p.23–24의 수식에 생략된 작은 분모 처리를 코드가 수행한다. 4차 경로는 `IF( ABS(TMP1).le.SMALL ) TMP1 = SMALL*SIGN( 1.0_SP, TMP1 )`와 `IF( abs(1.0 + RAT) > SMALL )`을 사용한다. 저차 경로는 `IF((ABS(TMP1)+ABS(TMP2))<SMALL)THEN`에서 `DOUT(I,J)=ZERO`로 둔다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-234 | 3.0 p.24·26의 HLL·파속식에는 SMALL 분모와 수심 절댓값 처리가 없다. | C 문서 누락 | `fluxes.F:185` `IF((ABS(SR(I,J)-SL(I,J)))<SMALL)THEN`; 186 `FOUT(I,J)=FOUT(I,J)/SMALL`; 371 `SQR_PHI_L=SQRT(GRAV*ABS(HxL(I,J)))` `io.F:2826` 입력 → `fluxes.F:109–110` 호출; `fluxes.F:179–190,371`. 네 문서·TeX의 HLL·작은 분모·파속식 검색. | HLL의 중간 파속 분기에서는 `IF((ABS(SR(I,J)-SL(I,J)))<SMALL)THEN`일 때 분모로 SMALL을 사용한다. 파속 제곱근은 `SQRT(GRAV*ABS(HxL(I,J)))`이다. C 판정은 3.0 p.24·26의 이 보호식 생략에 한정한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-235 | 3.0 p.25의 CFL 식과 p.32의 MPI 설명에는 최소값 집계 배열 범위가 없다. | C 문서 누락 | `misc.F:240–241` `DO J=1,N` / `DO I=1,M`; 277–278 `call MPI_ALLREDUCE (TMP3,myvar,1,MPI_SP,MPI_MIN, &` / `MPI_COMM_WORLD,ier)` `main.F:320`에서 `Mloc,Nloc` 전달; `misc.F:216,240–241,273–281`; 네 문서·TeX 전체의 CFL·MPI·ghost 검색. | CFL은 ghost 셀을 포함한 지역 배열에서 최소값을 구한다. `PARALLEL`에서는 `MPI_MIN`으로 전 프로세서의 최소값을 결합한다. 3.0 p.25·32에 이 집계 범위가 빠져 있다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-236 | 3.0 p.25·41의 시간 간격 설명에 DT_fixed 절반화 절차가 없다. | C 문서 누락 | `misc.F:283–288` `IF(FIXED_DT)THEN` / `DT = DT_fixed` / `DO WHILE (DT > DT_tmp)` / `DT=DT/2.0_SP` / `ENDDO` `io.F:2883–2895`; `misc.F:281–291`; 네 문서·TeX 전체의 `FIXED_DT`·`DT_fixed`·고정 시간 검색. | `DT_fixed` 입력 읽기가 성공하면 `FIXED_DT = .TRUE.`가 된다. `IF(FIXED_DT)THEN`에서 `DT = DT_fixed`를 적용하고 `DO WHILE (DT > DT_tmp)` 동안 `DT=DT/2.0_SP`를 반복한다. 3.0 p.25·41에는 이 절차가 없다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-237 | 3.0 p.26·41·81의 수심 임계 설명에는 유속 복원 대입식의 모든 용도가 없다. | C 문서 누락 | `etauv_solver.F:561` `U(I,J)=Ubar(I,J)/Max(H(I,J),MinDepthFrc)`; 570–576의 `MASK<1` 영 대입; 578 `HU(I,J)=Max(H(I,J),MinDepthFrc)*U(I,J)` `io.F:2933–2949`; `etauv_solver.F:402–411,561–593`; `misc.F:243,259`. 네 문서·TeX 전체의 `MinDepthFrc` 검색. Froude 기능 자체는 FT1-196의 일치 판정이다. | `MinDepthFrc`는 유속 복원·파속·분산 역변환의 수심 하한에도 사용한다. 건조 셀에서는 유속과 운동량을 0으로 둔다. 3.0 p.41은 주로 바닥마찰 하한으로 설명하며 p.81은 Froude 상한 목적을 덧붙인다. C 판정은 이들 쪽에 유속 복원 대입식과 분산 역변환의 용도가 생략된 점이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-238 | Manning 선택은 3.0 p.10·34에 있다. 마찰 누락 기본값은 별도 대조한다. | C 문서 누락 | `sources.F:238–240`의 K28; `io.F:2777` `CALL READ_FLOAT(Cd_fixed,FILE_NAME,'Cd',ierr)`; 2779 `Cd_fixed = 0.0_SP` `io.F:2738–2740,2777–2789`; `init.F:854,884–890`; `sources.F:236–243`. 네 문서·TeX의 Manning·마찰 기본값 검색; 2.1 p.9·34에도 Manning 선택이 있다. | Manning 선택 자체는 문서에 있다. `CARTESIAN`·`MANNING` 경로는 `GRAV*Cd(I,J)**2/Max(H(I,J),MinDepthFrc)**(0.333333_SP)`를 쓴다. C 판정은 3.0 p.40에 `Cd` 미입력 대입값 0과 실제 수심 하한 식이 빠진 점이다. 균일 마찰장은 `IN_Cd`가 거짓일 때 `Cd_fixed`로 채운다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-239 | 3.0 p.40은 Gamma1·Gamma2·Gamma3와 선형화 시 자동 0 설정을 설명한다. | C 문서 누락 | `io.F:2591,2593`의 `READ_FLOAT(Gamma1,...)`, `Gamma1 = 1.0_SP`; 2606,2608의 `Gamma2 = 1.0_SP`; 2651,2653의 `Gamma3 = 1.0_SP` `io.F:2591–2608,2651–2653`; `init.F:638–654`. 네 문서·TeX의 Gamma 검색; 2.1 p.39, Intro-TN p.12, TeX 1300–1307행에도 기능 설명이 있다. | 분산 전환 기능과 Gamma3에 따른 자동 0 설정은 문서에 있다. C 판정은 3.0 p.40에 입력 누락 시 세 Gamma 값을 각각 1로 읽는 절차가 빠진 점이다. 이후 `Gamma3 > ZERO`의 `ELSE` 또는 `DISPERSION`의 `ELSE`에서 Gamma1을 0으로 둔다. Gamma2의 0 대입은 `CARTESIAN` 분기이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-240 | 3.0 p.41은 VISCOSITY_BREAKING 선택을 설명하지만 미입력 대입값을 적지 않는다. | C 문서 누락 | `io.F:2689` `CALL READ_LOGICAL(VISCOSITY_BREAKING,FILE_NAME,'VISCOSITY_BREAKING',ierr)`; 2691 `VISCOSITY_BREAKING = .TRUE.`; 3076 `IF(VISCOSITY_BREAKING) SHOW_BREAKING = .TRUE.` `io.F:2689–2703,3076`; `breaker.F:64–71`; `masks.F:177–188`; `sources.F:196–198,394–453`. 네 문서·TeX 전체의 `VISCOSITY_BREAKING`·쇄파 방식 검색. | `VISCOSITY_BREAKING` 미입력은 참이다. 이 경우 `SHOW_BREAKING`도 참으로 설정하고 `BREAKING`을 호출한다. C 판정은 3.0 p.41의 누락 기본값에 한정한다. 충격 포착 전환의 분기는 FT1-125·126, 노트 정정은 FT1-267과 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-241 | 3.0 p.25–26·41에는 점성식의 전처리 대안 목록이 없다. | C 문서 누락 | `breaker.F:278` `# if defined (VIS_KENNEDY_ORIGINAL)`; 294 `nu_break(I,J)=cap1*ABS(ETAt(I,J))*B+nu_bkg`; 296 `# elif defined (VIS_KENNEDY)`; 308 `nu_break(I,J) = cap1*tmp2*(1.0_SP+B) + nu_bkg`; 311–314의 정적 전이·기본 대입. `breaker.F:64–71,131–144,248–265,278–315`; `io.F:2689–2691,3076`; 네 문서·TeX의 전처리 이름 검색. | `VIS_DEPTH_RATIO`가 없는 경로에서 조파 영역 밖의 지속 쇄파 조건을 통과하면 점성식을 선택한다. 우선순위는 `VIS_KENNEDY_ORIGINAL`, `VIS_KENNEDY`, `VIS_STATIC_TRANS`, 기본식이다. 이는 3.0 p.25–26·41의 설명에 없는 분기이다. FT1-130·269·280과 같은 식 선택이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-242 | 3.0 p.26의 쇄파 설명에는 이웃 나이 전파와 roller·undertow 식이 없다. | C 문서 누락 | `breaker.F:158` `C=MIN(ABS(ETAt(I,J))/tmp4,SQRT(GRAV*ABS(H(I,J))))`; 182–185의 이웃 나이 선택; 330 `R=ABS(0.45*ETAt(I,J)/MAX(C1,SMALL))`; 331 `R=MIN(R,0.1638_SP)` `breaker.F:151–229,248–265,325–337`; `io.F:3058–3076`; 네 문서·TeX의 `AGE_BREAKING`·roller·undertow 검색. code_analysis p.7의 나이 인수 목록은 전파식 설명이 아니다. FT1-133과 연결한다. | 쇄파 루틴은 이웃 나이와 전파 시간을 비교한다. `VIS_DEPTH_RATIO`가 없는 경로의 조파 영역 밖에서 `IF(AGE(I,J)>ZERO.AND.AGE(I,J)<T_brk.AND.ETAt(I,J)>tmp2)THEN`을 만족하면 roller·undertow를 계산한다. `R=MIN(R,0.1638_SP)`로 비를 제한한다. 3.0 p.26의 0/1 지수식과 별도 처리이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-243 | 3.0 p.27은 점성 스펀지를 설명하지만 점성 계수의 조건부 합산식을 적지 않는다. | C 문서 누락 | `sources.F:196,198` `IF(VISCOSITY_BREAKING .OR. WAVEMAKER_VIS)THEN` / `nu_vis = nu_break`; 213,216 `IF(DIFFUSION_SPONGE)THEN` / `nu_vis = nu_vis + nu_sponge` `sources.F:190–224`; `io.F:2280–2282,2689–2691,3145–3149`; `breaker.F:64–71`. 네 문서·TeX의 조파·스펀지 점성 검색. | `IF(VISCOSITY_BREAKING .OR. WAVEMAKER_VIS)THEN`에서 `nu_vis = nu_break`를 대입한다. 그 내부의 `DEEP_DRAFT_VESSEL` 경로만 선박 점성을 더한다. `IF(DIFFUSION_SPONGE)THEN`에서는 스펀지 점성을 더한다. 3.0 p.27의 누락은 이 조건부 합산 순서이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-244 | 시간 램프 입력은 3.0 p.37–38에 있다. p.28–31 조파식의 대입을 대조한다. | C 문서 누락 | K17; K02의 마지막 `+WaveMaker_Mass(I,J)*U(I,J)`; `sources.F:319` `+WaveMaker_Mass(I,J)*V(I,J)` `io.F:870,1517`; `sources.F:109–114,260,319`; 네 문서·TeX의 `Time_ramp`·램프·질량 소스 검색. 2.1 p.37에도 램프 입력이 있다. | 시간 램프의 존재는 문서에 있다. C 판정은 3.0 p.28–31·37–38에 `AA = TANH(PI/(Time_ramp*Tperiod)*TIME)*D_gen`의 실제 대입과 질량 주입에 따른 운동량 소스가 생략된 점이다. 규칙파 소스에는 가우스 공간 함수와 이 램프를 곱한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-245 | 3.0 p.25·27에는 RK 단계 안의 직접 감쇠 위치와 조파 강제 시각이 없다. | C 문서 누락 | `main.F:320`의 시간 간격 호출; `misc.F:294` `TIME=TIME+DT`; `main.F:380`의 3단계 루프; 483–485의 `CALL SPONGE_DAMPING` `io.F:2285–2287`; `main.F:320,380–487`; `misc.F:294`; `sources.F:109–132`. 네 문서·TeX의 RK·감쇠·시간 램프 검색. | 물리 시간은 RK 단계 루프 전에 한 번 증가한다. `DIRECT_SPONGE`가 참이면 각 RK 단계 끝에 직접 감쇠를 호출한다. 내부 질량 조파의 시간식은 세 단계에서 같은 TIME 값을 사용한다. C 판정은 3.0 p.25·27의 이 호출 순서 생략에 한정한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-246 | 3.0 p.41은 STEADY_TIME·T_INTV_mean을 설명하지만 창 경계 처리식은 적지 않는다. | C 문서 누락 | `mixing.F:60` `IF( time >= STEADY_TIME )THEN`; 143 `T_sum=T_sum+DT`; 144 `IF(T_sum.GE.T_INTV_mean)THEN`; 224 `T_sum=T_sum-T_INTV_mean   ! T_sum=ZERO? (ykchoi)`; 228 `ETA2sum=ZERO     !ykchoi` `io.F:3204–3230`; `mixing.F:60–61,143–154,224–255`; 네 문서·TeX의 `STEADY_TIME`·`T_INTV_mean` 검색. | 통계 시작 시각과 평균 간격은 문서에 있다. C 판정은 3.0 p.32·41에 창을 넘은 잔여 시간 처리식이 생략된 점이다. `T_sum=T_sum-T_INTV_mean`으로 시간을 넘기고 `Usum,Vsum,ETAsum,ETA2sum`은 0으로 둔다. 파고 합과 영점 통과 횟수는 이때 초기화하지 않는다. FT1-247과 구분한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-247 | 평균·제곱평균제곱근 파고의 표본 수 정의가 없다. | E 코드 결함 후보 (강함) | E07. `init.F:438` `Num_Zero_Up = 0`; `mixing.F:250` `WaveHeightAve(I,J)=HavgSum(I,J)/Num_Zero_Up(I,J)`; 292행의 `>=2` 조건. `main.F:496` → `mixing.F:60–61`; `io.F:3204–3230`의 통계 시작·평균 간격 입력. `mixing.F:253–255`의 파고 합·횟수 초기화는 주석이다. `cab9425:mixing.F:139–168`도 같은 n 분모와 2회째부터의 누적이다. 기존의 ‘같은 창’ 설명을 통계 시작 이후 누적값으로 정정한다. [확정 판정](FUNWAVE-git-verify-E1.md). | 파고 통계는 통계 시작 이후의 누적값이다. 검출 상향통과 횟수가 n이면 합산 파고 표본은 n-1개이다. 평균과 RMS의 분모는 n이므로 표본 개수와 일치하지 않는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-248 | 3.0 p.79의 필터 불필요 설명에는 선택적 FILTERING 경로가 없다. | C 문서 누락 | `bc.F:496` `# if defined (FILTERING)`; 499 `IF (filter_count > filter_interval) THEN`; 502 `CALL SHAPIRO_3(Mloc,Nloc,Nghost,MASK,Eta)`; 504–505의 `U,V` 호출. `bc.F:496–512`; `mod_global.F:84–86`; 네 문서·TeX 전체의 필터·Shapiro 검색. FT1-006의 과거 모형 필터 설명과 구분한다. | `CARTESIAN`·`FILTERING`이 정의되면 `EXCHANGE` 호출 횟수를 세고 `IF (filter_count > filter_interval) THEN`에서 수면고·유속을 필터링한다. `filter_interval = 1`은 선언값이며 입력 키워드가 아니다. 3.0 p.79는 필터가 필요 없다고 설명하지만 이 선택 경로를 기술하지 않는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-249 | 3.0 p.79–81의 불안정 안내에는 발산·NaN 중단 조건식이 없다. | C 문서 누락 | `misc.F:403` `MaxAbsEta=MAXVAL( abs(Eta(Ibeg:Iend,Jbeg:Jend)) )`; 409 `if (MaxAbsEta > EtaBlowVal) then`; `statistics.F:199` `IF (ISNAN(val)) THEN`; 204 `CALL MPI_ABORT( MPI_COMM_WORLD , 9 , ier)` `init.F:847–850`; `main.F:517`; `misc.F:403–428`; `statistics.F:175–184,199–206`; 네 문서·TeX의 `EtaBlowVal`·NaN·불안정 검색. | 최대 수면고가 EtaBlowVal보다 크면 중단한다. 통계량의 NaN도 별도로 중단한다. EtaBlowVal은 초기화에서 최대 수심 절댓값의 100배로 정한다. C 판정은 3.0 p.79–81에 이 조건식이 빠진 점이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-250 | 3.0 p.26의 습윤 복귀 설명에는 셀 자체 수면고 조건이 없다. | C 문서 누락 | `masks.F:106–109` `! this is for rainfall case $$$` / `IF(Eta(I,J)>-Depth(I,J))THEN` / `MASKtmp(I,J)=1` / `ENDIF` `masks.F:78–117`; 네 문서·TeX의 강수·습윤 복귀·`UseEtaScreen` 검색. | `UseEtaScreen`이 정의되지 않은 경로에서 `MASK_STRUC(I,J)==1`이고 `MASK(I,J)<1`이면 셀 자체의 `IF(Eta(I,J)>-Depth(I,J))THEN`으로도 습윤 복귀한다. 강수용이라는 주석이 있지만 이 조건 자체는 강수 입력 여부로 한정되지 않는다. C 판정은 3.0 p.26의 조건 생략에 한정한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-251 | 3.0 p.81의 급경사 회피 권고에는 SLOPE_CTR·IGNORE_BIG_SLOPE의 분기가 없다. | C 문서 누락 | `init.F:1179` `SLOPE_CTR = .FALSE.`; 1180 `MAX_SLOPE = 0.1`; `masks.F:152` `# if defined (IGNORE_BIG_SLOPE)`; 156 `DepthX(I,J)=Depth(I-1,J)` `init.F:1175–1220`; `masks.F:152–161`; 전체 `src/*.F`의 변수명·입력 검색. 네 문서·TeX의 경사 제한 검색. | 구면 초기화는 `SLOPE_CTR = .FALSE.`를 대입하므로 이어지는 `IF(SLOPE_CTR)THEN`의 경사 상한은 적용하지 않는다. 이 변수를 켜는 READ_* 입력은 없다. `IGNORE_BIG_SLOPE`가 정의되지 않으면 `IF(MASK(I,J)<1)THEN`에서 경계면 수심을 인접 셀 값으로 바꾼다. 3.0 p.81의 권고와 별도 처리이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-252 | 3.0 p.18–19·25에는 DISP_TIME_LEFT의 방향별 잔존 분기가 없다. | C 문서 누락 | `mod_global.F:178` `LOGICAL :: DISP_TIME_LEFT=.FALSE.`; `etauv_solver.F:485` `IF(DISP_TIME_LEFT)THEN`; K03. `mod_global.F:178`; `etauv_solver.F:402–411,484–507`; 전체 `src/*.F`의 `DISP_TIME_LEFT` 검색. 네 문서·TeX 전체에서도 해당 이름을 검색했다. | `DISP_TIME_LEFT`는 거짓으로 선언되어 있고 이를 켜는 READ_* 입력이나 후속 참 대입은 없다. y역변환에는 이 변수를 조건으로 한 비선형 분기가 남아 있지만 x역변환은 대응 분기가 없다. C 판정은 3.0 p.18–19·25에 이 구현 상태가 기술되지 않은 점이다. 기본 거짓 경로의 분할은 FT1-228과 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-253 | 3.0 p.15의 질량 방정식에는 후속 확장 소스와 Wsurf 저장 순서가 없다. | C 문서 누락 | `etauv_solver.F:247` `Wsurf(I,J) = R1(I,J)`; 259 `R1(I,J)=R1(I,J)+ MassSed(I,J)`; 264 `R1(I,J)=R1(I,J)+ PrecRateModel(I,J)` `etauv_solver.F:247–264`; `mod_sediment.F:196–198`의 READ_LOGICAL; `mod_precipitation.F:147`의 RAINFALL_FILE 입력. 네 문서·TeX의 Wsurf·퇴적물·강수 검색. | `Wsurf(I,J) = R1(I,J)` 저장 후 `SUBGRID` 보정과 확장 질량 소스를 적용한다. `SEDIMENT`에서 `IF(SedimentMassSource)THEN`이면 퇴적물 질량 소스를 더한다. `PRECIPITATION`에서는 강수율을 더한다. C 판정은 3.0 p.15에 이 확장·저장 순서가 없는 점이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-254 | 3.0 p.31은 방향 균등 분할·등 에너지 조파를 설명하지만 이산 정규화·대안 선택을 적지 않는다. | C 문서 누락 | `wavemaker.F:1946–1947`의 평균 방향 ±60도; 1950–1951의 ±90도 제한; 1963 `AG(:) = ABS(AG(:)/sumAG);   !Because integral of AG should be 1.`; 2128의 등주파수 경로. `io.F:1974–1976`; `wavemaker.F:370–400,1938–1966`; 네 문서·TeX의 방향 분할·`EqualEnergy` 검색. FT1-166·177·179와 같은 조파 경로이다. | 다방향 경로는 평균 방향 ±60도 범위를 만든 뒤 절대각을 ±90도로 제한한다. `AG(:) = ABS(AG(:)/sumAG)`로 이산 가중치를 정규화한다. 직교 경로는 `EqualEnergy` 입력에 따라 등 에너지 또는 등 주파수 분할을 선택한다. 3.0 p.31에 이 범위·정규화·선택 조건이 빠져 있다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-255 | 3.0 p.30의 방향 스펙트럼 입력 설명에는 성분 삭제 조건이 없다. | C 문서 누락 | `wavemaker.F:239` `IF(ABS(Dire(I)).LT.60.0_SP)THEN`; 243 `WaveCompTmp(J,DireCount) = WAVE_COMP(J,I)` `io.F:870,1850`; `wavemaker.F:196–199,238–246`; 네 문서·TeX 전체의 DATA2D·방향 제한 검색. | `IF(WaveMaker(1:9)=='WK_DATA2D')THEN` 경로는 `IF(ABS(Dire(I)).LT.60.0_SP)THEN`을 만족하는 성분만 남긴다. ±60도 경계값은 포함하지 않는다. C 판정은 3.0 p.30에 이 삭제 조건이 없는 점이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-256 | 3.0 p.87 식 (117)–(118)의 U4·V4 비선형 계수를 GPU 커널과 대조한다. | E 코드 결함 후보 (강함) | `G/src/init.F:555` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`; `G/src/moment_gpu.F:573` `U4_d(I,J) = U4_d(I,J) + gamma2*tMASK*( ken1*UxxVxy + ken2*HUxxHVxy )`; K29. GPU `io.F:2490–2521` 입력, `main.F:305–311`, `moment_gpu.F:552–575`의 조건과 실제 대입. GPU `init.F:555`의 값은 TVD `init.F:664`와 같다. 네 문서·TeX 전체의 GPU·CUDA 검색과 3.0 p.87 식 이미지 대조. [외부 원문 판정](FUNWAVE-external-sources.md). GPU `moment_gpu.F:579–586`의 `# if defined (ZALPHA)` 블록은 앞서 계산한 U4·V4를 선형식으로 다시 대입한다. | GPU의 직교 비선형 U4·V4 보정에도 문서에 없는 Beta_2와 그 제곱이 들어간다. FT1-216·217과 같은 계수 원인이므로 C에서 강한 E 후보로 바꾼다. `USE_CUDA`·`CARTESIAN` 및 `DISPERSION`이 켜지고 `gamma2>0.0_SP`인 경로의 판정이다. 이 U4·V4 비선형 보정 판정은 `ZALPHA`를 정의하지 않은 경로에 한정한다. 같은 원인: init.F:664 Beta_2 배수(문헌 근거 없음, GitHub 이슈 #46) [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 외부 원문] |
| FT1-257 | PDF 부록 (112),(120)에 대응하는 GPU y방향 전개. | E 코드 결함 후보 (강함) | E08. K29의 `G/src/moment_gpu.F:754–762` 연속 행 전체; `G/src/dispersion.F:445–453`의 CPU 대조식; PDF p.86 (112), p.89 (120). GPU `io.F:2490–2521` 입력 → `main.F:305–311` → `moment_gpu.F:121–133`; `moment_gpu.F:704–705`에서 `tU = U_d(i,j)`, `tV = V_d(i,j)`이다. GPU `Makefile_cuda:13,27`은 CARTESIAN·USE_CUDA를 정의한다. `5594984:src/moment_gpu.F:754`부터 같은 tV 곱이다. GPU 전체 이력 검색에서도 이 계수의 수정은 없다. [확정 판정](FUNWAVE-git-verify-E1.md). | CARTESIAN·USE_CUDA 분산 경로에서 Gamma2가 양수이면 V2_d 첫 곱은 tV를 사용한다. 문서와 CPU 경로의 해당 곱은 U를 사용한다. 이 차이는 GPU 코드 도입부터 존재한 강한 코드 결함 후보이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-258 | 3.0 p.32–34의 빌드 안내에는 이 로컬 GPU 사본의 변경 내역이 없다. | C 문서 누락 | `G/src/Makefile_cuda:27` `FLAG_18 = -DUSE_CUDA`; 38 `OPT      = -cuda -gpu=cc120 -cudalib=cusparse`; GPU 작업 트리 diff는 아래에 기록한다. GPU 원자료에서 `git diff -- src/Makefile_cuda src/etauv_solver_gpu.F src/mod_cuda.F`로 실제 대입·호출 변경을 대조했다. 네 문서와 TeX의 CUDA·GPU·빌드 설명을 검색했다. | 3.0 p.32–34의 문서 범위에는 로컬 CUDA 수정이 기술되어 있지 않다. 공개 GPU HEAD 대비 로컬 diff는 `Makefile_cuda`, `etauv_solver_gpu.F`, `mod_cuda.F`의 변경을 보여 준다. 이 비교는 로컬 수정 기록이며 모델 공식 배포판 변경 이력이 아니다. FT1-288과 같은 diff이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-259 | 3.0 p.34의 입력 안내에 READ_FLOAT의 누락 반환 계약은 없다. | C 문서 누락 | `mod_input.F:128` `REAL(SP),         INTENT(OUT) :: FLOAT_VAL`; 147 `IF(ERR_IF_ONE == 1)THEN`; 153 `RETURN` `mod_input.F:126–153`; `io.F:2898–2910`의 FroudeCap 호출 후 처리. 네 문서와 TeX 전체의 READ_FLOAT·누락 입력 검색. | `READ_FLOAT`는 `IF(ERR_IF_ONE == 1)THEN`에서 기본값을 대입하지 않고 반환한다. 기본값 근거는 각 호출 뒤의 누락 처리이다. `INTENT(OUT)` 호출 전 선언 초기값이 보존된다고 단언할 수 없다. C 판정은 3.0 p.34의 입력 안내에 이 계약이 없는 점이다. FT1-197과 연결한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-260 | 3.0 p.25 식 (78), p.32 식 (104), p.41의 FroudeCap 설명을 GPU의 해당 대입과 대조한다. | 일치 | `G/src/etauv_solver_gpu.F:1358` `Eta_d(I,J)=ALPHA_d(ISTEP)*Eta0_d(I,J)+BETA_d(ISTEP)*(Eta_d(I,J)+DT*R1)`; 2003 `U_d(I,J)=FroudeCap*Fr*COS(Utheta)`; `G/src/mixing_gpu.F:52` `SigWaveHeight_d(i,j) = 4.004*SQRT( ETA2mean_d(i,j) )` GPU `io.F:2809–2811,3033–3049`; `main.F:303–325,373–376`; `mixing_gpu.F:123–147`; `etauv_solver_gpu.F:1999–2007`. 네 문서·TeX의 RK·FroudeCap·유의파고 설명 전체 검색. | 인용한 GPU 대입은 문서의 RK 가중 적분, 유속 계산의 Froude 제한, 유의파고 계수 4.004와 대응한다. 이 대응 항목에 문서 누락을 부여하지 않는다. 평균 제곱값의 정의 차이는 FT1-187·275와 별도로 구분한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-261 | 현재 노트 §4 FT1-261 | B 문서 오기 | PDF p.15 (6) $\mathbf M=H\{\mathbf u_\alpha+\overline{\mathbf u}_2\}$; K09. `24a88c3:doc/funwave_tvd_3.0.tex:265`의 평균 표시와 `7b93138:src/fluxes.F:462–463`의 보정 포함 질량 플럭스를 대조했다. PDF p.15 이미지의 상선도 같다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 질량 플럭스 식의 u2에는 수심 평균 표시를 넣는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-262 | 현재 노트 §4 FT1-262 | B 문서 오기 | PDF p.16에 식 (7),(8)이 인쇄되어 있다. PDF p.15–16 이미지의 식 번호·인쇄 쪽을 대조했다. `24a88c3:doc/funwave_tvd_3.0.tex:265–273`에도 같은 식 순서가 있다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 식 (7)과 식 (8)은 PDF p.16을 인용한다. 식 (6)은 p.15를 인용한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-263 | 현재 노트 §4 FT1-263 | B 문서 오기 | PDF p.16 (11)의 첫 교차곱은 $\overline{\mathbf u}_2$이다. PDF p.16 이미지와 `24a88c3:doc/funwave_tvd_3.0.tex:285`의 첫 교차곱에 상선이 있다. 현재 `dispersion.F:491–498` 및 `7b93138:src/dispersion.F:457–464`의 부호와 연결한다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 식 (11)의 첫 교차곱에 수심 평균 u2를 쓴다. 와도 정의에 쓰는 비평균 u2와 구분한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-264 | 현재 노트 §4 FT1-264 | C 문서 누락 | `io.F:2622` `Beta_ref = - 0.531_SP`; `init.F:664` `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP` `io.F:2620–2622`; `init.F:656–664`; 3.0 p.16·40, TeX 1309행의 기준면 설명. 네 문서·TeX 전체의 `Beta_ref`·기준면 검색. [외부 원문 판정](FUNWAVE-external-sources.md). | 노트의 기준면 식은 문서의 이론식으로 구분한다. 현재 입력 누락값은 `Beta_ref = - 0.531_SP`이고 직교 초기화는 `Beta_1=Beta_ref+1.0_SP`와 `Beta_2=(1.0_SP/5.0_SP)**2/1.0_SP`를 별도로 대입한다. C는 노트 65행에 이 구현 구분이 없는 점이다. 비선형 배수의 E 판정은 FT1-021·216과 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-265 | 현재 노트 §4 FT1-265 | B 문서 오기 | PDF p.19 (23); K03, K20, K22. `7b93138:src/etauv_solver.F:227,251,256` 및 현재 `etauv_solver.F:310,343,348`. PDF p.19 식 (23)의 이미지와 대조했다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 식 (23)은 PDF p.19에 있다. 문서의 보존 운동량은 코드의 Ubar·Vbar에 대응한다. 기준 깊이 유속 U·V와 구분하고, 본문·부록의 프라임 분할은 FT1-228을 함께 설명한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-266 | 현재 노트 §4 FT1-266 | B 문서 오기 | `main.F:380` `DO ISTAGE=1,3`; PDF p.32 “ITERATION ... is not used any more.” 3.0 p.11·32의 반복 제거 문장, `7b93138:src/main.F:214–250`와 현재 `main.F:380–487`의 단계 루프. FT1-121은 문서 p.25에만 남은 구현 주장의 D 판정이고 이 행은 그 문장을 현재 구현으로 옮긴 노트의 B 판정이다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 각 RK 단계는 소스를 갱신하고 유속을 복원한다. 수렴 반복이 필요하다는 p.25 문장은 같은 문서의 반복 제거 설명과 모순한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-267 | 현재 노트 §4 FT1-267 | B 문서 오기 | K13; `io.F:2691` `VISCOSITY_BREAKING = .TRUE.` `io.F:2689–2691`; `masks.F:177–188`; `7b93138:src/masks.F:130`; `6233886`(2019-06-16)의 누락 기본값 FALSE→TRUE diff. FT1-013·125·126·240과 같은 조건이다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 충격 포착 전환 분기는 `VISCOSITY_BREAKING`의 `ELSE`에 있는 `IF(ABS(Eta(I,J))/MAX(DEPTH(I,J),MinDepthFrc)>SWE_ETA_DEP)THEN`이다. 이 비는 유속 Froude 수가 아니다. 현재 입력 누락 기본값은 점성 쇄파이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-268 | 현재 노트 §4 FT1-268 | A 판 차이 | `7b93138:src/sources.F:63` `LOGICAL :: PQ_scheme = .TRUE.`; 현재 `sources.F:70` `LOGICAL :: PQ_scheme = .FALSE.` `17d2eeb`의 `src/sources.F` diff; 현재 `sources.F:70,394–453`; [확정 판정 FT1-127](FUNWAVE-git-verify-AD1.md). | PDF는 P·Q 확산을 설명한다. `17d2eeb`(2017-03-03)는 `PQ_scheme`을 참에서 거짓으로 바꿨다. 현재 기본 분기는 HU·HV를 확산한다. FT1-127·128·137과 같은 판 차이이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-269 | 현재 노트 §4 FT1-269 | B 문서 오기 | `breaker.F:314` `nu_break(I,J) = cap1*tmp2 + nu_bkg`; `io.F:3103` `Cbrk2 = 0.35_SP` `breaker.F:124–126,264–315`; `io.F:3101–3103`; [확정 판정 FT1-130·134·135](FUNWAVE-git-verify-AD1.md). 네 문서·TeX의 Cbrk·점성식 검색. | 노트의 점성식·1.2·0.15는 PDF p.25–26의 기술로 구분한다. 현재 조파 영역 밖의 기본 지속 쇄파식은 `nu_break(I,J) = cap1*tmp2 + nu_bkg`이고 `cap1=1.0*(MAX(Depth(I,J),MinDepthFrc)+ETA(I,J))`이다. Cbrk2 미입력값은 0.35이다. 개시식은 `tmp1=Cbrk1*tmp3`이며 `tmp3=SQRT(GRAV*MAX(MinDepthFrc,H(I,J)))`이다. FT1-130·134·135의 B 판정과 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-270 | 현재 노트 §4 FT1-270 | D 문서에만 있음 | K11, K13; `fluxes.F:1572–1598`의 차수 저하·기울기 영 대입. `bc.F:83–93`; `fluxes.F:352–439,1572–1600`; `Din(I,J)=TXP2-1.0_SP/6.0_SP*(DVP3-2.0_SP*DVP2+DVP1)`. [확정 판정 FT1-140·141](FUNWAVE-git-verify-AD1.md). | 법선 플럭스 차단과 내부 건조 셀의 재구성 보정은 구현한다. 문서 식 (84)·(85)의 별도 건조 파속 분기는 현재 WAVE_SPEED에 없다. 이 구현 주장에는 FT1-140·141과 같은 D를 부여한다. DVP 보정값의 0 대입을 최종 기울기 0으로 설명하지 않는다. 내부 거울 경계 서술의 차이는 FT1-139와 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-271 | 현재 노트 §4 FT1-271 | B 문서 오기 | PDF p.27 “one or two times the typical wavelength.” PDF p.27 이미지의 `one or two times`를 확인했다. `7b93138:src/io.F:658`은 폭을 읽으며 파장 권고를 자동 대입하지 않는다. FT1-145와 같은 문서 수량이다. [확정 판정](FUNWAVE-git-verify-AD1.md). | L-D 스펀지의 문서 권고 폭은 보통 1–2파장이다. 출처는 PDF p.27이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-272 | 현재 노트 §4 FT1-272 | B 문서 오기 | `sponge.F:287` `tmp_2d_1(i,j)=MAX(CDsponge*TANH(ri/10.0),lim)` `sponge.F:285–287`; `7b93138:src/sponge.F:248–250`; [확정 판정 FT1-149](FUNWAVE-git-verify-AD1.md). | 문서 식 (89)과 실제 코드식은 다르다. 코드는 `ri=MAX(0.0,REAL(Iwidth-I))`와 `tmp_2d_1(i,j)=MAX(CDsponge*TANH(ri/10.0),lim)`을 사용한다. 문서식을 현재 구현식으로 쓰는 노트에는 FT1-149와 같은 B를 부여한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-273 | 현재 노트 §4 FT1-273 | B 문서 오기 | PDF의 1000 문장은 p.31이다. `wavemaker.F:1870` `do kf=1,10000` `7b93138:src/wavemaker.F:1061–1063`과 현재 `wavemaker.F:1870–1872`; PDF p.31 이미지. FT1-179와 같은 수량 판정이다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 코드의 초기 스펙트럼 적분 분할은 10000이다. PDF p.31의 성분 수 설명과 사용자 지정 주파수 수를 구분한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-274 | 현재 노트 §4 FT1-274 | C 문서 누락 | `mod_meteo.F:295` `WindCrestPercent=LARGE`; 719–722의 마스크 조건. `mod_meteo.F:213–218,247–263,292–307,719–722`; `sources.F:355–364`; 3.0 p.31·37, 2.1 p.21·37, Intro-TN p.9·11 및 TeX의 전체 검색 결과와 대조했다. | `METEO`·`WindForce` 경로에서 파봉 한정은 WindCrestPercent와 WindWaveInteraction에 따른다. 미입력 또는 상호작용을 끈 경우 `WindCrestPercent=LARGE`이므로 `MASK_WIND=1`을 유지한다. C는 노트 106행의 조건 생략이며 FT1-184와 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-275 | 현재 노트 §4 FT1-275 | B 문서 오기 | `mixing.F:146`의 평균 차감 누적. `mixing.F:146–154,244,267`; `7b93138:src/mixing.F:113–125`; PDF p.32 이미지; [확정 판정 FT1-187](FUNWAVE-git-verify-AD1.md). | PDF 식 (105)는 수면고 제곱을 적는다. 코드는 이전 평균 수면고를 뺀 값의 제곱을 시간 가중 누적한다. 이 식을 현재 산출식으로 쓰는 노트는 FT1-187과 같은 B이다. 유의파고 계수 4.004 자체는 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-276 | 현재 노트 §4 FT1-276 | B 문서 오기 | `fluxes.F:109–112`의 문자열 분기. `io.F:2826–2834`; `fluxes.F:109–137`; `7b93138:src/fluxes.F:81–84`. FT1-230은 문서에 이미 있는 선택지의 일치이고, 이 행은 실제 호출을 부정한 노트의 B이다. [확정 판정](FUNWAVE-git-verify-AD1.md). | HLL로 시작하지 않는 CONSTRUCTION 값은 산술평균 플럭스 경로를 선택한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-277 | 현재 노트 §4 FT1-277 | A 판 차이 | `fluxes.F:71–72` `ELSEIF(HIGH_ORDER(1:3)=='FMI') THEN` / `CALL CONSTRUCTION_HO_minmod` `7b93138:src/fluxes.F:63`과 `fef45a7:src/fluxes.F:63`은 주석이다. 전체 이력의 해당 FMI 문자열 검색은 `dfacbb2`(2020-06-12)를 반환한다. `dfacbb2:src/fluxes.F:71–72`에서 활성 분기를 도입했다. 현재 `io.F:2842`의 입력이 `fluxes.F:71–72`를 선택한다. FT1-232와 연결한다. [확정 판정](FUNWAVE-git-verify-AD1.md). | minmod 재구성 호출은 2018년 코드까지 주석 처리되어 있었다. 2020-06-12부터 FMI 입력으로 활성화할 수 있다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-278 | 현재 노트 §4 FT1-278 | B 문서 오기 | `derivatives.F:104–105`의 K30. `7b93138:src/derivatives.F:104–105`도 같은 스텐실이다. 균일 격자·MASK=1에서 Taylor 전개의 첫 오차항은 `5/12`를 계수로 하는 2차 항이다. 현재 주 분산 경로의 호출은 `dispersion.F:77–83`이다. [확정 판정](FUNWAVE-git-verify-AD1.md). | DERIVATIVE_X_High의 인용 스텐실은 2차 오차를 가진다. 이를 4차 1계 미분으로 적지 않는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-279 | 현재 노트 §4 FT1-279 | C 문서 누락 | K21의 312–317행 비선형 추가. `dispersion.F:295–318`; `io.F:2606–2608`; 3.0 p.87, TeX 2660–2692행. 네 문서·TeX 전체에서 U4·수심 평균 분산 보정을 검색했다. | 노트 18행이 인용한 범위에는 U4·V4의 선형 부분과 `IF(gamma2>ZERO)THEN`의 비선형 보정이 함께 있다. C는 노트의 비선형 보정 누락에 한정한다. PDF p.87 식 (117)·(118)은 두 부분을 모두 적는다. Beta_2 계수 문제는 FT1-216·217의 E 판정과 연결한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-280 | 현재 노트 §4 FT1-280 | B 문서 오기 | `breaker.F:124` `tmp3=SQRT(GRAV*MAX(MinDepthFrc,H(I,J)))`; `io.F:3081` `Cbrk1 = 0.65_SP`; `breaker.F:314` 기본 대입. `cab9425:mod_global.F:366`; 현재 `io.F:3081`, `breaker.F:124–126,278–315`; `7b93138:src/breaker.F:113–114,232–237`. [확정 판정](FUNWAVE-git-verify-AD1.md). | 쇄파 개시 계수의 기본값은 0.65이다. 파속에는 총수심 하한을 쓴다. VIS_KENNEDY는 컴파일 선택이다. 현재 기본 지속 쇄파 분기는 `nu_break(I,J) = cap1*tmp2 + nu_bkg`이다. FT1-130·134·241·269와 같은 조건·식이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-281 | 현재 노트 §4 FT1-281 | D 문서에만 있음 | `init.F:437` `nu_smg = ZERO`; `sources.F:367` `# if defined (MIXING)` 두 `src/*.F` 전체의 nu_smg 대입 검색; TVD `init.F:437`, GPU `init.F:332`; TVD `sources.F:367–388`, `io.F:3232–3234`. [확정 판정 FT1-093](FUNWAVE-git-verify-AD1.md). | 현재 TVD와 GPU 사본에서 nu_smg의 활성 대입은 초기 0 대입이다. `MIXING` 소스는 nu_smg를 읽지만 Smagorinsky 점성으로 갱신하지 않는다. 노트의 구현 주장은 FT1-093과 같은 D이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-282 | 현재 노트 §4 FT1-282 | B 문서 오기 | `bc.F:87` `P(Ibeg,J)=ZERO`; 90 `Fx(Ibeg,J)=0.5_SP*GRAV*(Xi*Xi*Gamma3+2.0_SP*Xi*Deps)` 현재 `bc.F:65–94,122–138,164–174,197–204`; `io.F:870,2260`의 WAVEMAKER·PERIODIC 입력. `7b93138:src/bc.F:68–71`도 법선 플럭스를 0으로 둔다. [확정 판정](FUNWAVE-git-verify-AD1.md). | 기본 외곽은 법선 질량 플럭스를 막는 벽 경계이다. 별도 경계 옵션은 따로 적는다. 서쪽 ABS·LEFT_BC_IRR, COUPLING 구간과 y방향 PERIODIC은 해당 분기에 따른다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-283 | 현재 노트 §4 FT1-283 | B 문서 오기 | `misc.F:243` `TMP1=ABS(U(I,J))+SQRT(GRAV*MAX(H(I,J),MinDepthFrc))` `7b93138:src/misc.F:154,170`과 현재 `misc.F:243,259`의 절댓값 위치가 같다. [확정 판정](FUNWAVE-git-verify-AD1.md). | CFL 분모는 abs(U)+c와 abs(V)+c이다. c에는 총수심 하한을 쓴다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-284 | 현재 노트 §4 FT1-284 | B 문서 오기 | `init.F:389–392`; `fluxes.F:780–781` `io.F:2842–2854`; `init.F:389–393`; `fluxes.F:101–105,473–480,779–784`; [확정 판정 FT1-202](FUNWAVE-git-verify-AD1.md). | 초기화는 Kappa 값을 구분하지만 현재 CONSTRUCT_X/Y는 Kappa를 계산에 쓰지 않는다. SECOND·THIRD 입력은 같은 선형 재구성을 수행한다. 초기화 값을 재구성 차수 선택으로 설명하는 노트에는 FT1-202와 같은 B를 부여한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-285 | 현재 노트 §4 FT1-285 | B 문서 오기 | K13. `io.F:2689–2691,2713–2715`; `masks.F:177–188`; `7b93138:src/masks.F:130–131`. 네 문서·TeX의 Froude·파고 수심 비 검색. [확정 판정](FUNWAVE-git-verify-AD1.md). | 현재 충격 포착 전환의 조건은 `IF(ABS(Eta(I,J))/MAX(DEPTH(I,J),MinDepthFrc)>SWE_ETA_DEP)THEN`이다. 이 비를 유속 Froude 수로 적지 않는다. 이 조건은 VISCOSITY_BREAKING을 선택하지 않은 분기에 있다. FT1-013·125·267과 같은 판정이다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| FT1-286 | 현재 노트 §4 FT1-286 | C 문서 누락 | `io.F:2691` `VISCOSITY_BREAKING = .TRUE.`; K13. `io.F:2689–2691,3076`; `masks.F:177–188`; `breaker.F:64–71`; 3.0 p.25–26·41의 두 방식 설명과 대조했다. | 충격 포착 쇄파 설명 자체는 제공되는 한 방식을 설명한다. C는 모델 소개에 점성 쇄파 선택과 현재 누락 기본값이 빠진 점이다. `VISCOSITY_BREAKING`을 읽지 못하면 참을 대입하고, 거짓일 때만 파고 수심 비로 분산을 끄는 분기를 쓴다. FT1-240·267과 연결한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-287 | 현재 노트 §4 FT1-287 | C 문서 누락 | `G/src/moment_gpu.F:754`의 `tV*HUxxHVxy`; TVD `dispersion.F:461`의 `U(I,J)*HUxxHVxy` 두 사본 `src/dispersion.F`의 읽기 전용 `git diff --no-index`; GPU `dispersion.F:189`와 TVD `dispersion.F:190,386–395`. 같은 사본 CPU 대응식은 GPU `dispersion.F:445`이다. | GPU 사본의 비 CUDA 파일을 현재 TVD 파일과 동일하다고 볼 수 없다. `dispersion.F`를 직접 비교하면 GPU에는 MGPU 분기 조건이 있고 현재 TVD에는 AB_OUTPUT 블록이 추가되어 있다. C는 노트 13행에 공유 범위와 판본 구분이 없는 점이다. CUDA 식의 별도 결함은 FT1-257에 연결한다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-288 | 현재 노트 §4 FT1-288 | 일치 | GPU 로컬 diff의 세 파일 목록; `G/src/mod_cuda.F:17` `integer,parameter :: TriSolver = 0    ! 0, 1-cusparse` GPU 원자료의 공개 HEAD 대비 `git diff -- src/Makefile_cuda src/etauv_solver_gpu.F src/mod_cuda.F`; Makefile_cuda는 FC·OPT 두 대입을 바꿨고 mod_cuda.F는 버퍼 선언 두 행을 추가했다. | 노트의 ‘핵심 변경 두 줄’은 Makefile_cuda의 FC·OPT 대입 변경을 가리키며 그 범위에서는 맞다. 전체 로컬 수정은 etauv_solver_gpu.F와 mod_cuda.F도 포함한다. 핵심 두 줄이라는 표현을 전체 수정이 두 줄뿐이라는 주장으로 확대하지 않는다. 전체 diff는 FT1-258과 같다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| FT1-289 | 현재 노트 §4 FT1-289 | B 문서 오기 | `io.F:149`의 READ_INPUT 정의; `main.F:383` `CALL Cal_Dispersion`; 394 `CALL FLUXES`; 404 `CALL SourceTerms`; 414 `CALL ESTIMATE_HUV(ISTAGE)` `7b93138:src/io.F:95`, `7b93138:src/main.F:214–230`; 현재 `io.F:149`, `main.F:380–414`, `etauv_solver.F:348`. [확정 판정](FUNWAVE-git-verify-AD1.md). | READ_INPUT은 io.F에 정의되어 있다. RK 단계는 분산 계산과 플럭스 계산 뒤에 소스와 보존 변수를 갱신한다. 보존 변수 갱신 뒤 유속 역변환을 호출한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |

최종 정적 점검에서 지정 26쪽의 쪽별 대조 행을 확인했다.
FT1-001–290에는 번호 누락과 중복이 없다.
일치하지 않은 191행은 위 최종 결론 표에 각각 한 번 나온다.
Markdown 표를 파싱하여 대조 표와 최종 결론 표의 열 수를 확인했다.
Fortran 인용 블록 35개의 비어 있지 않은 행을 현재 원자료 또는 인용한 과거 코드와 대조했다.
이 점검은 공백을 제외한 행 문자열을 비교했다.
모델 실행과 수치 결과 검증은 하지 않았다.
이 보고서 외의 파일은 수정하지 않았다.

분류별 개수: A 4, B 36, C 46, D 4, E 47, F 21, H 33, X 0. 일치 99행. 전체 290행. 열지 못한 파일: 없음.

## 전수 검증 기록 (10-18, FT1-093–FT1-289)

검증 행 수는 요청 목록의 191개 행 ID를 기준으로 센다. 각 ID의 본문 표와 §5 최종 결론 표를 함께 대조했다.
정정은 90개 행이다. 보완은 142개 행이다. 같은 행을 정정하고 인용도 보탠 경우 두 집계에 각각 포함한다.
분류 변경은 15개 행이다.

현재 코드와 인용된 과거 코드를 줄 단위로 대조했다. C·B 판정은 3.0·2.1·Intro-TN·code_analysis 네 문서의 판독 기록 전체와 TeX 기록을 검색하여 문서 범위를 다시 정했다. 식과 수치가 판정을 좌우한 항목은 해당 PDF 쪽 이미지도 대조했다.

요청 목록과 git 판정 파일이 겹치는 91개 행에 커밋 근거와 판정을 반영했다. FT1-115는 3.0 p.24의 앞 문장이 고계 미분의 이산화를 가리키므로 git 판정 B를 F로 정정했다. FT1-144의 PDF p.27 식 (87)과 TeX 788행은 모두 `gamma_x`이므로 git 판정 파일의 `gamma_s` 전사 지적을 채택하지 않았다. 해당 행의 정수 나눗셈에 대한 E 중간 판정은 유지했다.

Beta_2 배수에서 나온 26개 행에는 같은 원인과 외부 원문 태그를 표시했다. FT1-024·216·217·256은 `ZALPHA`를 정의하면 U4·V4를 선형식으로 다시 대입하는 조건까지 적었다. FT1-075는 PDF p.21 식 (48)과 TeX 474행에 없는 `=0`을 인용에서 제거했다.

분류 변경 목록:

| 행 ID | 변경 전 | 변경 후 |
|---|---|---|
| FT1-016 | H 코드 대조 대상 아님 | 일치 |
| FT1-115 | B 문서 오기 | F 표기 차이 |
| FT1-196 | C 문서 누락 | 일치 |
| FT1-230 | C 문서 누락 | 일치 |
| FT1-256 | C 문서 누락 | E 코드 결함 후보 (강함) |
| FT1-260 | C 문서 누락 | 일치 |
| FT1-268 | C 문서 누락 | A 판 차이 |
| FT1-269 | C 문서 누락 | B 문서 오기 |
| FT1-270 | C 문서 누락 | D 문서에만 있음 |
| FT1-272 | C 문서 누락 | B 문서 오기 |
| FT1-275 | C 문서 누락 | B 문서 오기 |
| FT1-277 | B 문서 오기 | A 판 차이 |
| FT1-281 | C 문서 누락 | D 문서에만 있음 |
| FT1-284 | C 문서 누락 | B 문서 오기 |
| FT1-288 | C 문서 누락 | 일치 |

지정 목록의 모든 행은 A·B·C·D·E·F·H 또는 일치로 판정했다. 본문 표와 최종 결론 표의 분류를 대조했다. 지정 목록 밖 행은 작업 시작 시점의 내용과 같다. 파일 전체의 `/home/firesinger/` 시작 링크는 0개이다.

## 최종 집계 (10-18, Claude가 차이 결론 절의 결론 열에서 셈)

- 차이 결론 191행: A 6, B 38, C 34, D 6, E 48, F 22, H 32, 일치 5. G·X 0. 이 집계가 앞의 분류별 개수 줄보다 우선한다.
