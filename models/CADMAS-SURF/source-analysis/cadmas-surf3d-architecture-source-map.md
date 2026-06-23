---
title: "CADMAS-SURF/3D 아키텍처 소스맵 — SMAC+VOF 시간적분 루프·명명규칙·데이터모델 (vf_a1main.f)"
model: CADMAS-SURF
component: src (main driver / architecture)
canonical_source: self
verification_method: "CADMAS-SURF/3D-MG 소스 직접 read (raw/source_code/.../CADMAS-SURF-3D/Source code/). vf_a1main.f(1240줄) 헤더 주석 verbatim(:3-9 해석대상·해석방법·좌표계·언어) + 변수사전(:38-218 데이터모델) + ver4.9.1(:366) + 시간적분 루프 호출순서(:915-1145: PMGP2C/C2P·CDTCAL·CWMSRC·V1CAL·T1CAL·S1CAL·K1CAL·F1CAL) 직접 인용. 240 Fortran 파일 명명규칙 ls 확정."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-23
related:
  - models/CADMAS-SURF/README.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-smac-velocity-pressure-solver.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-vof-free-surface.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-turbulence-and-porous-resistance.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-wave-generation-and-boundaries.md
---

# CADMAS-SURF/3D 아키텍처 소스맵

> CADMAS-SURF/3D 의 **진실의 원천 진입점**. 메인 드라이버 `vf_a1main.f` 가 정의하는 해석대상·수치기법·시간적분 루프 구조와 240 Fortran 파일의 명명규칙·데이터모델을 정리. 경로 루트(이하 모든 `vf_*.f` 인용): `raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/`.

## 1. 정체 — 헤더 주석 verbatim (vf_a1main.f:3-9)

```
CDT   VF_A1MAIN:CADMAS-SURF/3D-MGのメインルーチン
CD      (1)解析対象:自由表面を含む3次元非圧縮性流体
CD      (2)解析方法:差分法,SMAC法,VOF法
CD      (3)座標系  :デカルト座標系
CD      (4)言語    :Fortran90(配列の動的アロケートのため)
```

권위있는 1차 정의:
- **해석대상**: 자유표면을 포함하는 **3차원 비압축성 유체** (`vf_a1main.f:6`)
- **해석방법**: **差分法(유한차분) + SMAC法 + VOF法** (`vf_a1main.f:7`) — 압력-속도 결합은 **SMAC**(Simplified Marker And Cell), 자유수면 추적은 **VOF**
- **좌표계**: 데카르트(직교) (`vf_a1main.f:8`)
- **언어**: Fortran90 (동적 배열 할당 목적, FORTRAN77 코딩 준수 — 영문 매뉴얼 Ch1 (a))
- **버전**: 실행 시 출력 `*** ver4.9.1 ***` (`vf_a1main.f:366`), 시작 배너 `CADMAS-SURF/3D-MG Ver.I.I` (`vf_a1main.f:1208-1209`)
- **병렬**: `MGRANK`/`MYRANK`/`NPROCS` MPI rank (`vf_a1main.f:18` `INCLUDE 'mpif.h'`, MPMD 초기화 `init_mpmd` :351). "MG" = Multi-Grid(다중격자 nesting, 親/子격자) — `VF_PMG*` 패밀리.

## 2. 파일 명명규칙 (240 Fortran, `vf_<class><name>.f`)

`vf_` = **VOF**(Volume of Fluid) 코드 접두. 두번째 토큰이 서브시스템:

| 접두 | 서브시스템 | 대표 파일 |
|---|---|---|
| `vf_a*` | 메인·관리(admin) | `vf_a1main`(메인) `vf_a2dflt`(디폴트값) `vf_a2err` `vf_a2cput`(타이머) |
| `vf_b*` | 경계조건 — `bw`=경계면, `bs`=표면셀 | `vf_bwuwn`(법선속도) `vf_bwuwt`(접선속도) `vf_bwff`(VOF경계) `vf_bsuwn`(표면셀+조파소스) |
| `vf_c*` | compute/setup·조파·난류점성 | `vf_cinit` `vf_cgrid` `vf_cdtcal`(Δt) `vf_cforce`(파력) `vf_cwmak0/1/2`(조파) `vf_cnut0`(νt) `vf_cglv`(관성공극) |
| `vf_f*` | **F함수(VOF 자유수면)** | `vf_f1cal`(드라이버) `vf_fconv`(이류) `vf_feuler`(시간적분) `vf_fnfini/fnfprv`(NF 재구성) `vf_fcut01`(클리핑) `vf_fbubup`(기포) `vf_fdropf`(물방울) |
| `vf_v*` | 속도(velocity) — SMAC | `vf_v1cal`(드라이버) `vf_veuler`(예측자) `vf_vflxd[uvw]`(운동량 플럭스) `vf_vpcoef`(Poisson 계수) `vf_vpsol`(Poisson solve) `vf_vmodif`(속도보정) `vf_vgene`(소스·drag) |
| `vf_k*` | k-ε 난류 | `vf_k1cal`(드라이버) `vf_kgene`(생성·소산) |
| `vf_m*`,`vf_mz*` | 선형 solver | `vf_m1bcgs`(BiCGSTAB) `vf_mzdcmp`(ILU분해) `vf_mzminv`(전처리 적용) |
| `vf_s*`,`vf_t*` | 스칼라농도(s)·온도(t) 수송 | `vf_s1cal` `vf_t1cal` `vf_sconvd`(이류) `vf_sdiff`(확산) `vf_seuler` |
| `vf_p*`,`vf_pmg*` | 병렬(MPI)·압력 멀티그리드 nesting | `vf_p0init` `vf_p1sumd`(reduce) `vf_pmgp2c`/`pmgc2p`(親↔子 전송) |
| `vf_i*` | 입력 파서 | `vf_ii1inp`(메인) `vf_iimdl`(모델) `vf_iiporo`(공극) `vf_iigrid` `vf_iiboun` |
| `vf_o*` | 출력 — `ol`리스트 `og`도화 `om`멀티에이전트 `or`상세 `ot`시계열 | `vf_ol1trn` `vf_og1trn` `vf_om1trn` `vf_or1trn` `vf_ot1trn` |
| `vf_w*` | 파(wave theory) 구현 | `vf_wstk0`(Stokes) `vf_wcnd0`(cnoidal) `vf_wsfmb2`(stream-function B) |
| `vf_z*`,`vf_zxmg/zxmp*` | 유틸·MPI 래퍼 | `vf_zsetr3`(배열초기화) `vf_zgetim` `vf_zxmp_*`(MPI 추상화) |
| `vf_stoc_*` | STOC 광역모델 결합 glue | `vf_stoc_init/recv/send` |

## 3. 데이터모델 (vf_a1main.f:38-218 변수사전)

배열은 전부 `ALLOCATABLE`(동적, `vf_a1main.f:231-293`), 3D는 `(NUMI,NUMJ,NUMK)`. 핵심:

| 변수 | 의미 | 인용 |
|---|---|---|
| `UU,VV,WW` | x/y/z 속도 (staggered) | `vf_a1main.f:59-61` |
| `PP` | 압력 | `vf_a1main.f:62` |
| `FF` | **VOF 함수 F** (유체체적률) | `vf_a1main.f:63` |
| `ANU` | 분자동점성 + 渦동점성(νt)의 합 | `vf_a1main.f:64` |
| `CM0,CD0` | 관성력계수·저항계수 (포러스 body) | `vf_a1main.f:65-66` |
| `GGV` / `GGX,GGY,GGZ` | **공극률** / x·y·z **면적투과율** | `vf_a1main.f:67-70` |
| `GLV` = `GGV+(1-GGV)*CM` 외 GLX/Y/Z | 관성 가중 공극(가상질량) | `vf_a1main.f:71-74` |
| `AK,AE` / `ANUT` | 난류에너지 k·산일 ε / 渦점성 νt | `vf_a1main.f:92-94` |
| `TT` / `CC` | 온도 / 스칼라농도(LEQC종) | `vf_a1main.f:97·103` |
| `SRCUV` | 造波소스용 속도 | `vf_a1main.f:120` |
| `TBUB`,`DROP*` | 기포상승·물방울 자유낙하 처리 | `vf_a1main.f:81-87` |

**NF 셀상태 인덱스** (VOF 자유수면 분류, `vf_a1main.f:124-133`):
- `-1`=장애물셀, `0`=유체셀, `1~6`=표면셀(유체가 각각 x-/x+/y-/y+/z-/z+ 측), `8`=기체셀

**INDB 경계조건 코드** (`vf_a1main.f:159-168`, `INDB(3,L)`=속도·압력 BC):
`0`미정의 `1`슬립 `2`논슬립 `3`속도고정 `4`프리 `5`**造波경계** `6`**대수칙** `7`**방사경계** `8`**완전조면**. VOF F 경계(`INDB(4,L)`)는 `5`造波·`7`방사만 (`vf_a1main.f:173-174`).

> 3중 읽기: Fortran90 ALLOCATE 의 정합 배열 할당을 위해 입력파일을 `VF_II1INP` 로 **3회 읽음**(읽기→할당→재읽기), `vf_a1main.f:396-663` 의 주석 명시.

## 4. SMAC+VOF 시간적분 루프 (vf_a1main.f:915-1145)

라벨 `500 CONTINUE`(:919)~`GOTO 500`(:1145) 가 메인 시간스텝 루프. 헤더 주석 `SMAC法およびVOF法の計算ループ`(`vf_a1main.f:915`). 1스텝 호출순서:

1. **멀티그리드 親↔子 데이터 전송** — `VF_PMGP2C`(:923)·`VF_PMGC2P`(:929) (격자 nesting)
2. **적응 시간刻み Δt** — `VF_CDTCAL`(:940) (CFL 기반, `IDTTYP≠0`) 또는 고정 `DTCNST`(:938)
3. **종료조건 판정** — `NNOW≥NEND` 또는 `TNOW+0.5Δt≥TEND`(:947), 경과시간 ETIME 초과 시 리스타트(:1002)
4. **출력** — 리스트 `VF_OL1TRN`(:962)·도화 `VF_OG1TRN`(:971)·멀티에이전트 `VF_OM1TRN`(:979)·상세 `VF_OR1TRN`(:982)·시계열 `VF_OT1TRN`(:990)
5. **STOC 정보교환** — `VF_STOC_RECV`(:1011)/`VF_STOC_SEND`(:1012) (`NB_SC>0` 시, 광역모델 결합)
6. **造波소스 갱신** — `VF_CWMSRC`(:1037) (`ISCTYP(1)≠0` 시)
7. **流速·압력 SMAC 서브루프** — `DO 600 ILOOP=1,LOOPS`(:1044) 내 `VF_V1CAL`(:1058) — **SMAC 핵심**(예측자→압력 Poisson→보정). → [smac-velocity-pressure-solver](cadmas-surf3d-smac-velocity-pressure-solver.md)
8. **온도** `VF_T1CAL`(:1077) (`LEQT≠0`)
9. **스칼라농도** `VF_S1CAL`(:1086) (`LEQC>0`)
10. **k-ε 2방정식 난류** `VF_K1CAL`(:1095) (`LEQK≠0`). → [turbulence-and-porous-resistance](cadmas-surf3d-turbulence-and-porous-resistance.md)
11. **VOF 함수 F 계산 + NF 재설정** `VF_F1CAL`(:1104). → [vof-free-surface](cadmas-surf3d-vof-free-surface.md)
12. **NF 변경 후 경계값 재설정** — 대수칙 `VF_BWKELG`(:1120), νt 재계산 `VF_CNUT0`(:1124)·`VF_CNU00`(:1125), 온도·농도 경계(:1129-1142)

> 진단량(스텝당 리스트 출력): `FSUM`(전유체체적)·`FCUT`(클리핑 질량오차)·`!VD!`(발산)·`!B!`/`!R!`(Poisson 잔차)·`ITR`(반복수) — `vf_a1main.f:956·1214-1228`.

## 5. 결합 컴포넌트 경계

본 노트는 단상 `CADMAS-SURF/3D`. 2상(기액 VOF)은 `CADMAS-SURF-3D2F`(CADMAS-2F), 구조·지반 FEM 은 `STR3D`, 광역 tsunami 전파(정수압/비정수압)는 PARI `STOC-ML/IC`. 결합 사슬·라이선스·정체 → [README](../README.md).

## 다음 심화 후보

- `vf_cdtcal.f` CFL 조건식 정밀 (Δt 결정 인자)
- `vf_pmgp2c.f`/`vf_pmgc2p.f` 親-子 격자 보간(2011.04 추가 XPF/YPF/ZPF 보간계수)
- `vf_stoc_send.f`/`vf_stoc_recv.f` STOC 결합 인터페이스 (광역→국소 핸드오프)
- 영문 매뉴얼 Ch1 지배방정식과 본 소스 대조 (manual-notes)
