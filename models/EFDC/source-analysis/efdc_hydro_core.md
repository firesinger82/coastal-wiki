---
title: "efdc hydro core"
topic: currents
canonical_source: self
citation_status: verified
verification_method: "EFDC source code 직접 분석 (models/EFDC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/efdc_hydro_core.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
last_source_check: 2026-10-08 (recovery 재판독 대조)
---

## Scope

How EFDC+ assembles momentum and continuity, splits external (depth-integrated 2D) from internal (3D shear) modes, switches between 3-time-level (leapfrog + trapezoidal corrector) and 2-time-level paths, applies buoyancy / non-hydrostatic / boundary forcing, and where the depth/free-surface update happens. Use this when debugging mass conservation, switching between IS2TIM modes, or wiring a non-hydrostatic case.

## Source basis

- `aaefdc.f90:3189-3190` — top-level dispatch: `IS2TIM==0 → HDMT` (3TL), `IS2TIM>=1 → HDMT2T` (2TL).
- `calexp.f90`, `calexp2t.f90` — external (depth-integrated) momentum.
- `calpuv9c.f90`, `calpuv2c.f90` — external continuity solver (preconditioned conjugate gradient).
- `caluvw.f90` — internal (3D) momentum, vertical velocity W, barotropic correction.
- `calbuoy.f90`, `calebi.f90` — density and external buoyancy integral.
- `calpnhs.f90` — quasi-non-hydrostatic pressure.
- `setopenbc.f90`, `calpser.f90` — open BC and PSER tide series.

## A. External momentum (CALEXP / CALEXP2T)

- Advection fluxes `FUHU/FVHU/FUHV/FVHV` built per layer, upwind or central (`calexp.f90:218-227`); flux divergence assembled into `FX/FY` (`:685-686`). 2TL mirror in `calexp2t.f90:224-228`.
- Coriolis + curvature: `CAC = FCORC + metric + HP` (`calexp.f90:571`); `FCAX/FCAY` (`:620-621`).
- Vertical sums to depth-integrated `FCAXE/FCAYE`, `FXE/FYE` (`calexp.f90:1133-1136`; `calexp2t.f90:1062-1065`).
- 2TL은 CALTSXY를 외부 모드 전에 호출한다. (`hdmt2t.f90:601` — `call CALTSXY(0)`; `hdmt.f90:749` — `call CALTSXY(0)`) 3TL 일반 단계는 CALTSXY를 외부 모드 뒤에 호출한다. (`hdmt2t.f90:601` — `call CALTSXY(0)`; `hdmt.f90:749` — `call CALTSXY(0)`) 3TL 외부 모드는 앞 계산의 표면 응력을 읽는다. (`hdmt2t.f90:601` — `call CALTSXY(0)`; `hdmt2t.f90:627` — `call CALPUV2C`; `hdmt.f90:690` — `call CALPUV9C`; `hdmt.f90:749` — `call CALTSXY(0)`; `hdmt.f90:757` — `DU(L,KS) = DU(L,KS) - CDZUU(L,KS)*TSX(L)`; `hdmt.f90:758` — `DV(L,KS) = DV(L,KS) - CDZUV(L,KS)*TSY(L)`) HDMT는 새 표면 응력을 내부 모드 DU/DV에 주입한다. (`hdmt.f90:757` — `DU(L,KS) = DU(L,KS) - CDZUU(L,KS)*TSX(L)`; `hdmt.f90:758` — `DV(L,KS) = DV(L,KS) - CDZUV(L,KS)*TSY(L)`)
- 수평 확산 항은 후반 CALHDMF 또는 CALHDMF3가 생산한다. (`hdmt2t.f90:827` — `call CALHDMF`) 다음 운동량 계산이 이 값을 읽는다. (`hdmt2t.f90:619` — `call CALEXP2T`; `hdmt2t.f90:827` — `call CALHDMF`; `calhdmf.f90:358` — `FMDUX(L,K) = FMDUX0(L,K)`; `calexp2t.f90:895` — `FX(L,K) = FX(L,K) - SDX(L)*( FMDUX(L,K) + FMDUY(L,K) )`)

문서의 u·v 개별 스칼라 확산과 코드의 응력 발산을 구분한다. (`calhdmf3.f90:267` — `FMDUX0(L,K) = 2.0* DYP(L)*H1P(L)*AH(L,K)*DXU1(L,K)`; `calhdmf3.f90:268` — `FMDUY0(L,K) = 0.5*( DXU(L) + DXU(LS) )*H1C(L)*AHC(L,K)*( DYU1(L,K) + DXV1(L,K) )`; `calexp.f90:953` — `FX(L,K) = FX(L,K) - SUB3D(L,K)*SDX(L)*( FMDUX(L,K) - FMDUX(LW,K) + FMDUY(LN,K) - FMDUY(L,K) )`; EFDC_Theory_Document_Ver_12.pdf, PDF 24쪽·인쇄 11쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 50쪽·인쇄 37쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 53쪽·인쇄 40쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 54쪽·인쇄 41쪽) 3시각 정상 응력은 2AH·∂u/∂x와 2AH·∂v/∂y이다. (`calhdmf3.f90:267` — `FMDUX0(L,K) = 2.0* DYP(L)*H1P(L)*AH(L,K)*DXU1(L,K)`; `calhdmf3.f90:269` — `FMDVY0(L,K) = 2.0* DXP(L)*H1P(L)*AH(L,K)*DYV1(L,K)`; EFDC_Theory_Document_Ver_12.pdf, PDF 24쪽·인쇄 11쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 50쪽·인쇄 37쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 53쪽·인쇄 40쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 54쪽·인쇄 41쪽) 2시각 정상 응력의 계수는 1이다. (`calhdmf.f90:310` — `FMDUX0(L,K) = ( DYP(L) *HP(L) *AH(L,K) *DXU1(L,K) - DYP(LW)*HP(LW)*AH(LW,K)*DXU1(LW,K) )*SUB(L)`; `calhdmf.f90:313` — `FMDVY0(L,K) = ( DXP(L) *HP(L) *AH(L,K) *DYV1(L,K) - DXP(LS)*HP(LS)*AH(LS,K)*DYV1(LS,K) )*SVB(L)`; EFDC_Theory_Document_Ver_12.pdf, PDF 24쪽·인쇄 11쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 50쪽·인쇄 37쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 53쪽·인쇄 40쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 54쪽·인쇄 41쪽) 교차 응력은 AH·(∂u/∂y+∂v/∂x)이다. (`calhdmf3.f90:268` — `FMDUY0(L,K) = 0.5*( DXU(L) + DXU(LS) )*H1C(L)*AHC(L,K)*( DYU1(L,K) + DXV1(L,K) )`; `calhdmf3.f90:270` — `FMDVX0(L,K) = 0.5*( DYV(L) + DYV(LW) )*H1C(L)*AHC(L,K)*( DYU1(L,K) + DXV1(L,K) )`; `calhdmf.f90:216` — `SXY(L,K) = DYU1(L,K) + DXV1(L,K)`; EFDC_Theory_Document_Ver_12.pdf, PDF 24쪽·인쇄 11쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 50쪽·인쇄 37쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 53쪽·인쇄 40쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 54쪽·인쇄 41쪽) 문서 식 2.130은 이 교차 합에 추가로 2를 곱한다. (EFDC_Theory_Document_Ver_12.pdf, PDF 53쪽·인쇄 40쪽, 식 2.130) 식 2.129·2.131의 일치는 3시각 분기에 한정한다. (`calhdmf3.f90:267` — `FMDUX0(L,K) = 2.0* DYP(L)*H1P(L)*AH(L,K)*DXU1(L,K)`; `calhdmf3.f90:269` — `FMDVY0(L,K) = 2.0* DXP(L)*H1P(L)*AH(L,K)*DYV1(L,K)`; `calhdmf.f90:310` — `FMDUX0(L,K) = ( DYP(L) *HP(L) *AH(L,K) *DXU1(L,K) - DYP(LW)*HP(LW)*AH(LW,K)*DXU1(LW,K) )*SUB(L)`; EFDC_Theory_Document_Ver_12.pdf, PDF 53쪽·인쇄 40쪽, 식 2.129; EFDC_Theory_Document_Ver_12.pdf, PDF 54쪽·인쇄 41쪽, 식 2.131)

- Implicit bottom/vegetation drag coefficients `RCX/RCY` at `calpuv9c.f90:269-270`, applied at `:287-288`.

## B. External continuity (CALPUV9C / CALPUV2C)

- 단일 프로세스는 MDCHH=0에서 CONGRAD를 호출한다. (`calpuv2c.f90:660` — `if( MDCHH == 0 ) Call Congrad_MPI   ! *** MSCHH> = 1 not parallelized yet @todo`; `calpuv2c.f90:662` — `if( MDCHH == 0 ) CALL CONGRAD`; `calpuv2c.f90:663` — `if( MDCHH >= 1 ) CALL CONGRADC`) 단일 프로세스는 MDCHH>=1에서 CONGRADC를 호출한다. (`calpuv2c.f90:660` — `if( MDCHH == 0 ) Call Congrad_MPI   ! *** MSCHH> = 1 not parallelized yet @todo`; `calpuv2c.f90:662` — `if( MDCHH == 0 ) CALL CONGRAD`; `calpuv2c.f90:663` — `if( MDCHH >= 1 ) CALL CONGRADC`) 다중 프로세스는 MDCHH=0에서 Congrad_MPI를 호출한다. (`calpuv2c.f90:660` — `if( MDCHH == 0 ) Call Congrad_MPI   ! *** MSCHH> = 1 not parallelized yet @todo`; `calpuv2c.f90:662` — `if( MDCHH == 0 ) CALL CONGRAD`; `calpuv2c.f90:663` — `if( MDCHH >= 1 ) CALL CONGRADC`) 다중 프로세스의 MDCHH>=1 분기에는 이 위치의 해법 호출이 없다. (`calpuv2c.f90:660` — `if( MDCHH == 0 ) Call Congrad_MPI   ! *** MSCHH> = 1 not parallelized yet @todo`; `calpuv2c.f90:662` — `if( MDCHH == 0 ) CALL CONGRAD`; `calpuv2c.f90:663` — `if( MDCHH >= 1 ) CALL CONGRADC`)
- Linear system: RHS `FP` at `calpuv9c.f90:609`; coefficients `CC/CS/CW/CE/CN` at `:623-631`.
- Free-surface / depth update:
  - 3TL: `HP = H2P + DELT * DXYIP * (QSUME − 0.5*div(UHDYE+UHDY2E, VHDXE+VHDX2E))` (`calpuv9c.f90:771-772`).

코드의 수직 연속식은 Wk−Wk−1이다. (`caluvw.f90:733` — `W(L,K) = W(L,K-1) - 0.5*DXYIP(L)  &`; EFDC_Theory_Document_Ver_12.pdf, PDF 47쪽·인쇄 34쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 48쪽·인쇄 35쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 50쪽·인쇄 37쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 51쪽·인쇄 38쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 52쪽·인쇄 39쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 54쪽·인쇄 41쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 56쪽·인쇄 43쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 58쪽·인쇄 45쪽) PDF 식 2.100의 더하기와 다르다. (`caluvw.f90:733` — `W(L,K) = W(L,K-1) - 0.5*DXYIP(L)  &`; EFDC_Theory_Document_Ver_12.pdf, PDF 47쪽·인쇄 34쪽, 식 2.100) y 운동량은 −FCAYE와 y 면 계수를 사용한다. (`calpuv9c.f90:257` — `FVHDXE(L) = VHDX1E(L) - DELTD2*SVB(L)*HRVO(L)*HVTMP(L)*(P1(L)-P1(LS)) + SVB(L)*DELT*DYIV(L)*(DXYV(L)*(TSY1(L)-RITB1*TBY1(L)) - FCAYE(L) + FPGYE(L) - SNLT*FYE(L))`; `calexp.f90:1134` — `FCAYE(L) = FCAYE(L) + FCAY(L,K)*SGZV(L,K)`; EFDC_Theory_Document_Ver_12.pdf, PDF 47쪽·인쇄 34쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 48쪽·인쇄 35쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 50쪽·인쇄 37쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 51쪽·인쇄 38쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 52쪽·인쇄 39쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 54쪽·인쇄 41쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 56쪽·인쇄 43쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 58쪽·인쇄 45쪽) PDF 식 2.102의 mx·Su와 식 2.113의 +코리올리·k 가중은 코드와 다르다. (`calpuv9c.f90:257` — `FVHDXE(L) = VHDX1E(L) - DELTD2*SVB(L)*HRVO(L)*HVTMP(L)*(P1(L)-P1(LS)) + SVB(L)*DELT*DYIV(L)*(DXYV(L)*(TSY1(L)-RITB1*TBY1(L)) - FCAYE(L) + FPGYE(L) - SNLT*FYE(L))`; `calexp.f90:1134` — `FCAYE(L) = FCAYE(L) + FCAY(L,K)*SGZV(L,K)`; EFDC_Theory_Document_Ver_12.pdf, PDF 48쪽·인쇄 35쪽, 식 2.102; EFDC_Theory_Document_Ver_12.pdf, PDF 50쪽·인쇄 37쪽, 식 2.113) BI1C와 BI2C는 서로 다른 적분이다. (`calebi.f90:123` — `BI1C  = BI1C + DZCBK`; `calebi.f90:124` — `BI2C  = BI2C + DZCBK + ZZC(K,L)*DZCB(K,ND)`; EFDC_Theory_Document_Ver_12.pdf, PDF 47쪽·인쇄 34쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 48쪽·인쇄 35쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 50쪽·인쇄 37쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 51쪽·인쇄 38쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 52쪽·인쇄 39쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 54쪽·인쇄 41쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 56쪽·인쇄 43쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 58쪽·인쇄 45쪽) PDF 식 2.116은 둘을 같은 β̂로 쓴다. (`calebi.f90:123` — `BI1C  = BI1C + DZCBK`; `calebi.f90:124` — `BI2C  = BI2C + DZCBK + ZZC(K,L)*DZCB(K,ND)`; EFDC_Theory_Document_Ver_12.pdf, PDF 50쪽·인쇄 37쪽, 식 2.116) 코드의 응력 발산은 각 방향을 한 번 사용한다. (`calexp.f90:953` — `FX(L,K) = FX(L,K) - SUB3D(L,K)*SDX(L)*( FMDUX(L,K) - FMDUX(LW,K) + FMDUY(LN,K) - FMDUY(L,K) )`; `calexp.f90:963` — `FY(L,K) = FY(L,K) - SVB3D(L,K)*SDY(L)*( FMDVY(L,K) - FMDVY(LS,K) + FMDVX(LE,K) - FMDVX(L,K) )`; EFDC_Theory_Document_Ver_12.pdf, PDF 47쪽·인쇄 34쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 48쪽·인쇄 35쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 50쪽·인쇄 37쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 51쪽·인쇄 38쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 52쪽·인쇄 39쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 54쪽·인쇄 41쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 56쪽·인쇄 43쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 58쪽·인쇄 45쪽) PDF 식 2.96·2.117·2.118에는 코드와 다른 중복·누락 기호가 있다. (`calexp.f90:953` — `FX(L,K) = FX(L,K) - SUB3D(L,K)*SDX(L)*( FMDUX(L,K) - FMDUX(LW,K) + FMDUY(LN,K) - FMDUY(L,K) )`; `calexp.f90:963` — `FY(L,K) = FY(L,K) - SVB3D(L,K)*SDY(L)*( FMDVY(L,K) - FMDVY(LS,K) + FMDVX(LE,K) - FMDVX(L,K) )`; EFDC_Theory_Document_Ver_12.pdf, PDF 47쪽·인쇄 34쪽, 식 2.96; EFDC_Theory_Document_Ver_12.pdf, PDF 51쪽·인쇄 38쪽, 식 2.117; EFDC_Theory_Document_Ver_12.pdf, PDF 52쪽·인쇄 39쪽, 식 2.118) 3시각 원천 시간 계수는 2DT이다. (`calpuv9c.f90:130` — `DELT = DT2`; `calpuv9c.f90:784` — `HP(L) = H1P(L) + DELT*DXYIP(L)*( QSUME(L) - 0.5*( UHDYE(LE) + UHDY1E(LE) - UHDYE(L) - UHDY1E(L) &`; EFDC_Theory_Document_Ver_12.pdf, PDF 47쪽·인쇄 34쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 48쪽·인쇄 35쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 50쪽·인쇄 37쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 51쪽·인쇄 38쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 52쪽·인쇄 39쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 54쪽·인쇄 41쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 56쪽·인쇄 43쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 58쪽·인쇄 45쪽) 식 2.119는 DT만 인쇄한다. (`calpuv9c.f90:130` — `DELT = DT2`; `calpuv9c.f90:784` — `HP(L) = H1P(L) + DELT*DXYIP(L)*( QSUME(L) - 0.5*( UHDYE(LE) + UHDY1E(LE) - UHDYE(L) - UHDY1E(L) &`; EFDC_Theory_Document_Ver_12.pdf, PDF 52쪽·인쇄 39쪽, 식 2.119) y 플럭스의 x 발산은 x 방향 차분이다. (`calexp.f90:686` — `FY(L,K) = FSGZV(L,K)*( FVHV(L,K)-FVHV(LS,K) + FUHV(LE,K)-FUHV(L,K) ) + FVHJ(L,K)   ! ***  M4/S2`; EFDC_Theory_Document_Ver_12.pdf, PDF 47쪽·인쇄 34쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 48쪽·인쇄 35쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 50쪽·인쇄 37쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 51쪽·인쇄 38쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 52쪽·인쇄 39쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 54쪽·인쇄 41쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 56쪽·인쇄 43쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 58쪽·인쇄 45쪽) 식 2.134는 해당 미분도 δy로 인쇄한다. (`calexp.f90:686` — `FY(L,K) = FSGZV(L,K)*( FVHV(L,K)-FVHV(LS,K) + FUHV(LE,K)-FUHV(L,K) ) + FVHJ(L,K)   ! ***  M4/S2`; EFDC_Theory_Document_Ver_12.pdf, PDF 56쪽·인쇄 43쪽, 식 2.134) 식 2.144의 좌변은 표층 PK를 뜻한다. (`caluvw.f90:517` — `UHE(L) = UHE(L) + CDZDU(L,K)*DU(L,K)`; `caluvw.f90:525` — `UHDYF(L,KC) = UHE(L)*SUB(L)`; `caluvw.f90:531` — `UHDYF(L,K) = SUB3D(L,K)*(UHDYF(L,K+1) - DU(L,K))`; EFDC_Theory_Document_Ver_12.pdf, PDF 58쪽·인쇄 45쪽, 식 2.144)

  - 2TL: `HP = H1P + DELTD2 * DXYIP * (2*QSUME − div(new+old flows))` (`calpuv2c.f90:733-734`).

외부 압력 상태 P는 G*(HP+BELV)이다. (`calpuv2c.f90:750` — `HP(L) = GI*P(L) - BELV(L)`; `calpuv2c.f90:733` — `HP(L) = H1P(L) + DELTD2*DXYIP(L)*( 2.*QSUME(L) - ( UHDYE(LE)+UHDY1E(LE)-UHDYE(L)-UHDY1E(L)  &`; `calpuv2c.f90:975` — `P(L) = G*(HP(L) + BELV(L))`) HP는 수심이다. (`calpuv2c.f90:750` — `HP(L) = GI*P(L) - BELV(L)`; `calpuv2c.f90:733` — `HP(L) = H1P(L) + DELTD2*DXYIP(L)*( 2.*QSUME(L) - ( UHDYE(LE)+UHDY1E(LE)-UHDYE(L)-UHDY1E(L)  &`; `calpuv2c.f90:975` — `P(L) = G*(HP(L) + BELV(L))`) 경계에서는 HP=GI*P−BELV로 수심을 복원한다. (`calpuv2c.f90:750` — `HP(L) = GI*P(L) - BELV(L)`; `calpuv2c.f90:733` — `HP(L) = H1P(L) + DELTD2*DXYIP(L)*( 2.*QSUME(L) - ( UHDYE(LE)+UHDY1E(LE)-UHDYE(L)-UHDY1E(L)  &`; `calpuv2c.f90:975` — `P(L) = G*(HP(L) + BELV(L))`) 내부 셀은 연속식으로 수심을 갱신한다. (`calpuv2c.f90:750` — `HP(L) = GI*P(L) - BELV(L)`; `calpuv2c.f90:733` — `HP(L) = H1P(L) + DELTD2*DXYIP(L)*( 2.*QSUME(L) - ( UHDYE(LE)+UHDY1E(LE)-UHDYE(L)-UHDY1E(L)  &`; `calpuv2c.f90:975` — `P(L) = G*(HP(L) + BELV(L))`)

## C. Internal (3D) mode coupling (CALUVW)

전단(DU/DV) 연직 **완전 implicit tridiagonal + Sherman-Morrison** solve 자체는 → **[[efdc_internal_shear_caluvw]]** (2026-07-11 신설; 본 절은 그 이후의 정합 복원만).

Three-step consistency restoration:

1. Shear reconstruction from external unit flows (`caluvw.f90:523-532`).
2. **Barotropic correction**: depth-sum `UHDYF/VHDXF` into `TVARE/TVARN` (`:601-606`), subtract external `UHDYE/VHDXE` (`:610-614`), redistribute via `CERRU/CERRV` (`:617-624`).
3. Mass-flux correction at open boundaries — face-by-face replacement using neighbor-3D − neighbor-external + boundary-external (`:766, 784, 800, 815` for S/N/E/W).

CALUVW는 층 유량과 외부 유량의 차이를 보정한다. (`caluvw.f90:613` — `TVARE(L) = TVARE(L) - UHDYE(L)`; `caluvw.f90:621` — `UHDYF(L,K) = UHDYF(L,K) - TVARE(L)*CERRU(L,K)`) 이 보정을 제거한 실행의 질량 오차는 확인하지 않음. (`caluvw.f90:613` — `TVARE(L) = TVARE(L) - UHDYE(L)`; `caluvw.f90:621` — `UHDYF(L,K) = UHDYF(L,K) - TVARE(L)*CERRU(L,K)`)

## D. Time-stepping (3TL vs 2TL)

| Mode | `IS2TIM` | Driver | `ISTL` | DELT | Use case |
|---|---|---|---|---|---|
| 3TL leapfrog | `0` | `HDMT` | `3` predictor / `2` corrector | `DT2` | Stability, classic EFDC default |
| 3TL trapezoidal corrector | (within `HDMT`) | `HDMT` | `2`; `ROLD=RNEW=0.5` | `DT` | 보정은 ISTL=2와 DELT=DT를 사용한다. (`hdmt.f90:1337` — `ISTL = 2`; `hdmt.f90:1338` — `DELT = DT          ! *** NOT USED IN HDMT BUT INDICATIVE`) ROLD와 RNEW는 각각 0.5이다. (`hdmt.f90:1340` — `ROLD = 0.5`; `hdmt.f90:1341` — `RNEW = 0.5`) |
| 2TL | `>=1` | `HDMT2T` | `2` 고정 | `DT`; 동적 간격은 `DTDYN` | 2TL 동적 간격은 DTDYN이다. (`hdmt2t.f90:482` — `DELT    = DTDYN`; `hdmt2t.f90:483` — `DELTD2  = DTDYN/2.`) |

- 3TL leapfrog labeled at `hdmt.f90:1344-1349` and `calexp.f90:256` ("THREE TIME LEVEL (LEAP-FROG)").
- Corrector at `hdmt.f90:1335-1342`; `calexp.f90:184` ("THREE TIME LEVEL CORRECTOR STEP").
- 2TL at `hdmt2t.f90:114-115`.

## E. Buoyancy

- `CALBUOY` (`calbuoy.f90:128-179`) computes density from S, T, or both: `B = (ρ/ρ₀) − 1`.

CALBUOY는 ISGOTM>0 또는 IBSC=2에서 TEM을 PTEM으로 변환한다. (`calbuoy.f90:95` — `tm  = TEM(L,K)                    ! *** In-situ temperature [deg C]`; `calbuoy.f90:97` — `PTEM(L,K) = gsw_pt_from_t (sa, tm, PSW, p_ref)`)

- `CALEBI` (`calebi.f90:106-175`) integrates `B` into external buoyancy integrals `BI1/BI2/BE`.
- External pressure-gradient `FPGXE/FPGYE` assembled in CALPUV (`calpuv9c.f90:217-228`) and added to external momentum (`:256-257`).

## F. Non-hydrostatic (CALPNHS)

Activated when `KC > 1 .and. ISPNHYDS >= 1`:
- CALEXP adds non-hydrostatic pressure-gradient term (`calexp.f90:1010, 1052-1055`).
- CALUVW calls `CALPNHS` (`caluvw.f90:1319`).
- CALPNHS의 역변환은 인터페이스 W와 층 중심 ZZ를 함께 쓴다. (`calpnhs.f90:69` — `WZ(L,K) = W(L,K)+GI*ZZ(L,K)*( DELTI*(P(L)-P1(L)) &`; EFDC_Theory_Document_Ver_12.pdf, PDF 25쪽·인쇄 12쪽) 코드의 역변환에는 저면 시간 변화 항이 있다. (`calpnhs.f90:72` — `+ (1.-ZZ(L,K))*( DELTI*(BELV(L)-BELV1(L)) &`; EFDC_Theory_Document_Ver_12.pdf, PDF 25쪽·인쇄 12쪽) 고정 저면·같은 수직 평가 위치에서만 문서 좌표 관계를 동일한 식으로 비교한다. (`calpnhs.f90:69` — `WZ(L,K) = W(L,K)+GI*ZZ(L,K)*( DELTI*(P(L)-P1(L)) &`; `calpnhs.f90:72` — `+ (1.-ZZ(L,K))*( DELTI*(BELV(L)-BELV1(L)) &`; EFDC_Theory_Document_Ver_12.pdf, PDF 25쪽·인쇄 12쪽)

This is a **quasi-non-hydrostatic** correction (pressure-projection style), not a fully wave-resolving non-hydrostatic solve.

## G. Boundary forcing into the hydro core

- `CALPSER` (`calpser.f90:45`) interpolates `PSERT(NS)` from time series + offset, called from `HDMT` (`hdmt.f90:676-677`) or `HDMT2T` (`hdmt2t.f90:611-613`) **before** the external solve.
- `SETOPENBC` writes elevation/pressure BC into `FP(L)` from side-specific `PSERT(NPSER*)`:
  - South `setopenbc.f90:252`, West `:357`, East `:460`, North `:566`.
- After PCG, boundary `HP = GI*P − BELV` (`calpuv9c.f90:804-807`).
- `CALPUV` calls `SETOPENBC` before solve (`calpuv9c.f90:638-639`; 2TL `calpuv2c.f90:591-592`).

## Decision Guide

| Situation | Setting |
|---|---|
| Standard tidal/coastal run | IS2TIM과 NTSTBC는 실행 입력으로 읽는다. (`mod_var_global.f90:76` — `integer :: IS2TIM         !< Time stepping option: 0 - 3TL, 1 - 2TL`; `input.f90:150` — `read(1,*,IOSTAT = ISO) IS2TIM, IGRIDH, IGRIDV, KMINV, SGZHPDELTA  !, ISWGS84        ! NTL: Waiting for the implementation of Geographic Coordinate`; `input.f90:376` — `read(1,*,IOSTAT = ISO) NTC, NTSPTC, NLTC, NTTC, ldum, NTSTBC, ldum, NTCVB, NTSMMT, ldum, NDRYSTP, NRAMPUP, NUPSTEP`) 권장 NTSTBC 범위는 이 정적 대조에서 확인하지 않음. (`input.f90:376` — `read(1,*,IOSTAT = ISO) NTC, NTSPTC, NLTC, NTTC, ldum, NTSTBC, ldum, NTCVB, NTSMMT, ldum, NDRYSTP, NRAMPUP, NUPSTEP`) |
| Sediment / water quality dominant | 2TL (`IS2TIM>=1`); allows dynamic timestep coupling |
| Density-stratified estuary | C2의 9번째 입력은 ldum이다. (`input.f90:170` — `read(1,*,IOSTAT = ISO) ISRESTI, ISRESTO, ISRESTR, ISGREGOR, ISLOG, ISDIVEX, ISNEGH, ISMMC, ldum, ICONTINUE, ISHOW`; `input.f90:311` — `read(1,*,IOSTAT = ISO) ISTRAN(NS), ISTOPT(NS), ISQUICK, ISADAC(NS), ISFCT(NS), ldum, ldum, ldum, ISCI(NS), ISCO(NS)`; `input.f90:2582` — `read(1,*,IOSTAT = ISO) BSC, IBSC, TEMO, tmp, tmp, NCBS, NCBW, NCBE, NCBN, IVOLTEMP, VOL_VEL_MAX, VOL_DEP_MIN`; `setbcs.f90:449` — `if( IINTPG == 0 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_2.md:52` — `\* ISBAL: 1 FOR ACTIVATING MASS, MOMENTUM AND ENERGY BALANCES AND`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_2.md:54` — `\* WRITING RESULTS TO FILE bal.out`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_5.md:64` — `\* IINTPG: 0 ORIGINAL INTERNAL PRESSURE GRADIENT FORMULATION`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_5.md:66` — `\*              1 JACOBIAN FORMULATION`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_5.md:68` — `\*              2 FINITE VOLUME FORMULATION`; EFDC_Manual.pdf, PDF 21쪽·인쇄 17쪽; EFDC_Manual.pdf, PDF 23쪽·인쇄 19쪽) SAL·TEM transport 선택은 C6의 ISTRAN(1)·ISTRAN(2)가 담당한다. (`input.f90:311` — `read(1,*,IOSTAT = ISO) ISTRAN(NS), ISTOPT(NS), ISQUICK, ISADAC(NS), ISFCT(NS), ldum, ldum, ldum, ISCI(NS), ISCO(NS)`; EFDC_Manual.pdf, PDF 21쪽·인쇄 17쪽; EFDC_Manual.pdf, PDF 23쪽·인쇄 19쪽) C46의 BSC·IBSC가 부력 계산을 제어한다. (`input.f90:2582` — `read(1,*,IOSTAT = ISO) BSC, IBSC, TEMO, tmp, tmp, NCBS, NCBW, NCBE, NCBN, IVOLTEMP, VOL_VEL_MAX, VOL_DEP_MIN`; EFDC_Manual.pdf, PDF 21쪽·인쇄 17쪽; EFDC_Manual.pdf, PDF 23쪽·인쇄 19쪽) 현재 setbcs는 IINTPG=0일 때 좁은 수로의 외부 밀도 구배 플래그를 설정한다. (`setbcs.f90:449` — `if( IINTPG == 0 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_5.md:64` — `\* IINTPG: 0 ORIGINAL INTERNAL PRESSURE GRADIENT FORMULATION`; EFDC_Manual.pdf, PDF 21쪽·인쇄 17쪽; EFDC_Manual.pdf, PDF 23쪽·인쇄 19쪽) |
| Wave-resolving short-wave runup | `ISPNHYDS>=1` + `KC>1` (non-hydrostatic) |
| External-mode CFL violation | Reduce `DT` first; PCG itself rarely the bottleneck |
| Mass drift | Verify CALUVW barotropic correction at `:601-624` runs, and `IS2TIM`/timestep are consistent across hot-start |

## Working Rules

- 3TL with overly long `NTSTBC` (>100) lets leapfrog computational mode grow — symptom is checkerboard `HP` field; cure is shorter `NTSTBC`.
- The PCG tolerance (`RPADJ`-related) defaults work for most cases; tighten only if PCG iteration count is large *and* mass-balance closure is poor.
- HDMT는 ISTL=3으로 진입한다. (`hdmt.f90:387` — `ISTL = 3`) 보정 조건은 NCTBC=NTSTBC이다. (`aaefdc.f90:478` — `NCTBC = 1`; `hdmt.f90:1335` — `if( NCTBC == NTSTBC )then`) 재시작 직후가 자동으로 ISTL=2인지는 확인하지 않음. (`hdmt.f90:387` — `ISTL = 3`)
- Non-hydrostatic mode requires `KC>=4` for meaningful pressure projection; `KC=2` usually under-resolves.
- Open BC `LOPENBCDRY` flag (`setopenbc.f90:295-306, etc.`) auto-disables a BC cell when forced elevation falls below `BELV` — important for tide gauges near dry land.

## Common Pitfalls

- ▢ Setting `IS2TIM` mid-run via hot-start without resetting `H1P/H2P` arrays — mass jump.
- ▢ Forgetting to update `PSER.INP` time origin when changing `TBEGIN` — boundary tide goes out of phase silently.
- ▢ Activating `ISPNHYDS=1` without increasing `KC` — non-hydrostatic correction is negligible.
- ▢ Using `CALPUV2C` (2TL) with stratification + leapfrog-style `NTSTBC` — `NTSTBC` does nothing in 2TL; corrector concept doesn't exist there.
- ▢ Open BC flat-elevation series with steep bathymetry — `LOPENBCDRY` switches it off; check log for "OPEN BC DRY".

## Next expansion

- ~~CALUVW vertical velocity W detailed note~~ — [[efdc_vertical]] (W 연속식 :686-872) + [[efdc_internal_shear_caluvw]] (전단 solve) 로 커버 완료 (2026-07-11).
- PCG preconditioner choice and convergence tuning (separate ops note).
- Curvilinear metric details (CAC term decomposition).

## References

- Hamrick 1992 (EFDC theoretical documentation, GWCE-style external/internal split).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/efdc/source_code/EFDCPlus_Stable/EFDC`. Auto-draft = false; review_required = true.
