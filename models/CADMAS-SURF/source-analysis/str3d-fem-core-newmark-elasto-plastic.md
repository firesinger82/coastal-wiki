---
title: "STR3D FEM 코어 — Newmark-β 음함수 동해석·요소 라이브러리·탄소성(von Mises/Drucker-Prager)+균열·Biot 지반 (main·nl_transient·npforce·estfmtx·yfunc·sol0)"
model: CADMAS-SURF
component: src (STR3D FEM structural/soil core)
canonical_source: self
verification_method: "STR3D 소스 직접 read (raw/.../Simulators/STR3D/Source code/). 시간적분 Newmark-β=1/3 main/main.f:42·잔차 seq/npforce_s.f:65-72·접선 contact/npforced.f:48-50·3변위레벨 module/m_val.f90:126-128 + 요소 estfmtx.f:8-28(shell/solid/truss/beam/soil)·Gauss gauss_*.h·B행렬 blmtx.f:17-41(TL 대변형)·질량 emass*.f·하중 efrcp.f(유체압) + 구성식 dsol0.f(탄성)·yfunc.f:14-19(von Mises/Drucker-Prager)·sol0/sol2.f(탄소성 접선)·koji3d.f+dsol1.f(인장균열) + Biot 지반 ITYP6 glbstfg_s.f:21·30(θ=1). file:line 직접 인용."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-23
related:
  - models/CADMAS-SURF/source-analysis/str3d-linear-solvers.md
  - models/CADMAS-SURF/source-analysis/str3d-contact-and-fluid-coupling.md
  - models/CADMAS-SURF/README.md
---

# STR3D FEM 코어 (구조·지반)

> 멀티스케일 사슬의 구조 컴포넌트 — CADMAS 유체압을 받아 구조 변형·응력을 FEM 으로 풀고 변형 위치를 CADMAS-2F 로 환류([cadmas-2f-structure-coupling](cadmas-2f-structure-coupling-cutcell.md)). 본 노트=FEM 코어(시간적분·요소·구성식). solver·접촉·유체결합은 자매노트. 경로 루트: `raw/.../Simulators/STR3D/Source code/`(하위 src/·seq/·main/·module/·contact/).

## 1. 시간적분 — Newmark-β 음함수 동해석 (β=1/3)

메인 `main/main.f:1`(`PROGRAM MAIN`)→`ASTEA_MECHANICAL`(`:81·87`). Newmark 파라미터 하드디폴트: `main/main.f:42 RR(4)=1/3 !BETA`·`:45 RR(7)=1 !ALPHA`. 드라이버 분기(`main/astea_mechanical.f`): `KK(1)=0`→구조(`NL_STATIC`+`NL_TRANSIENT`), `≠0`→지반(`NL_STATIC_S`+`NL_TRANSIENT_S`).

**음함수 동해석 Newmark-β, 3변위레벨**(`UG1/UG2/UG3`=u_{n-1}/u_n/u_{n+1}, `module/m_val.f90:126-128`, roll `nl_transient_s.f:316-317`), 가변스텝 `DT1/DT2`·`DT12=½(DT1+DT2)`. 잔차(동적 내력 `FTI`, `seq/npforce_s.f:65-72`):
```
FTI = (FCM3/DT2 - (1/DT2+1/DT1)FCM2 + FCM1/DT1)/DT12     ! M·a (중심 2차차분)
    + 질량비례감쇠 + 강성비례감쇠
    + (β·FCK3 + (1-2β)·FCK2 + β·FCK1)                     ! Newmark-β 가중 K·u
```
`β=RR(4)=1/3`. 접선강성(`contact/npforced.f:48-50`): `ESTF=(1/DT2+0.5CM)/DT12·EMASS + (0.5/DT2·GE+β)·ESTF` — 잔차의 일관 Jacobian. **HHT-α 아님**(α 보간 없음, Rayleigh 감쇠 `AMAT(4)`=강성비례·`AMAT(5)`=질량비례). Newton-Raphson 내부루프(`nl_transient_s.f:123`) + 접촉 외부루프(`:111`). 대회전 director는 Rodrigues 회전(`src/dirupdt.f:30-35`, `IGNL>0`).

> 지반(soil, `ITYP=6`)은 Biot 압밀(pore-pressure 연성): `ELHM=ECPP/DT12·0.5 + ALP·EKPP`, `ALP=1`(θ=1 후진Euler형, `seq/glbstfg_s.f:11·30`).

## 2. 요소 라이브러리

요소타입 `ITYP`(`IELM(2,*)`): **1=shell·2=solid·3=truss·4=beam·6=soil**(Biot pore-pressure 연성 solid). 디스패치 `estfmtx.f:8-28`·`emassmtx.f:7-23`. solid족: te1(4)/te2(10)/pn1(6)/pn2(15)/hx1(8)/hx2(20) (`estfmtx.f:11-22`).

- **형상함수 도함수·Gauss**: `derhx2.f`(hex 8/20, 2³ 또는 3³ Gauss `gauss_ln_3.h`)·`derpn2.f`(prism, `gauss_pn_73.h` 7×3)·`derte2.f`(tet 10, `gauss_te_5.h` 5점)·`dertr2/derqu2`(tri/quad). Jacobian `det3.f`(|J|<1e-20 abort :23-26)
- **강성 B/D**: `BLMTX`(`blmtx.f:17-25` 6×3N 변형-변위 B행렬, `IGNL>0` 시 TL 대변형 비선형항 :30-41). 요소접선 `estfhx2.f:42-55`: `ESTF=Σ_gp(Bᵀ·D·B + Sᵀ·E)·|J|·W` — 재료강성 + 기하(초기응력)강성(`IGNL>0`)
- **질량 `emass*.f`**: consistent(`Σρ·H·Hᵀ·|J|·W`) + lumped, `LUMP=KK(30)` 선택. ⚠헤더 주석(0=lumped/1=consistent)과 코드 분기 라벨 반전(`emasste1.f:30-35`)
- **하중**: `efrcp.f`(유체압 `PPND`→`FCP`, [§유체결합](str3d-contact-and-fluid-coupling.md))·`efp*.f`(면압)·`bdf*.f`/`bdyfc.f`(체적력)

## 3. 구성식 (재료)

**선형탄성 + von Mises/Drucker-Prager 탄소성(등방경화) + 평활 인장균열 + Rayleigh 감쇠.** Cam-Clay·Mohr-Coulomb 파일 없음(DP=MC 평활 cone).

- **탄성 D행렬**: `dsol0.f:22-24`(E,ν 등방 3D), 균열 D `dsol1.f`(균열법선 `D=E·1e-4` smeared-crack)
- **항복함수** `yfunc.f`: `IYLD=1`→**von Mises** `F=√(3·J2D)`(`:14-15`), `IYLD=2`→**Drucker-Prager** `F=A(α·J1+√J2D)`, `A=1/(1/√3-α)`(`:16-19`), `α=AMAT(13)`
- **유동법칙** `dfdsg.f`(∂F/∂σ 연관, von Mises :9-21 / DP :25-31)
- **탄소성 접선** `sol2.f:16-26`: `Dᵉᵖ=Dᵉ-(Dᵉ a aᵀ Dᵉ)/(H+aᵀ Dᵉ a)`, 경화 `HD=AMAT(12)`
- **인장균열** `sol0.f:7-25`: 주응력 `PR(1)≥ST`(인장강도 `AMAT(14)`)이면 `KOJI3D`(`koji3d.f` 주응력 고유해)로 주축회전→균열 D `DSOL1`→역변환
- 상태갱신 `ist_updt.f:18-35`(`E/ν/HD/α/ST` 읽고 `IST_SOL/TRS/BEAM` 디스패치)

**재료표 `AMAT` 열**: 1=E·2=ν·3=ρ·4=GE(강성감쇠)·5=CM(질량감쇠)·12=HD(경화)·13=α(DP)·14=ST(인장강도) (`ist_updt.f:18-24`).

## 4. 전역 데이터 구조 (module/)

- `m_val.f90`: 중앙 전역상태 — 연결 `IELM`·좌표 `GRID`·재료 `MAT/AMAT`·3변위 `UG1/2/3`·beam director `VG`·력벡터 `FCK/FCD/FCM`·pore압 `PG1/2/3`·Gauss 변형/응력 `EPSG/SIGG`·속도 `VELG`
- `m_part.f90`: 영역분할/MPI 파티션 테이블 + 파티션간 통신 인덱스
- `input_work.f90`: NASTRAN형 카드(GRID·CTRIA/CQUAD·CTETRA/CHEXA·CROD·CBAR) 파싱 스테이징
- `mavbl.f90`/`mused.f90`: 메모리 budget 회계

> 코어: Newmark-β 음함수 동해석 + 탄소성-균열 구성식 + Biot 지반. CADMAS 유체압이 외력(`efrcp.f`)으로 진입, 변형이 환류. solver→[str3d-linear-solvers](str3d-linear-solvers.md), 접촉·결합→[str3d-contact-and-fluid-coupling](str3d-contact-and-fluid-coupling.md).
