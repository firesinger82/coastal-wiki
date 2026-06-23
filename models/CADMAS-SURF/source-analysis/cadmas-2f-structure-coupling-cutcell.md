---
title: "CADMAS-2F 유체-구조 결합 — sf_* cut-cell 공극엔진(이동구조 FSI·가동상)·사면체 다면체 클리핑 (sf_str·sf_stm·sf_cut3·sf_tetdiv·sf_mdporo)"
model: CADMAS-SURF
component: src (CADMAS-SURF/3D2F structure/movable-bed coupling)
canonical_source: self
verification_method: "CADMAS-SURF/3D2F 소스 직접 read (raw/.../CADMAS-SURF-3D2F/Source code/). sf_* 전수 헤더/본문 read: 클리핑 sf_cut3.f(6면 half-space)·sf_cut3x.f(marching-tet 562줄)·sf_tetdiv.f(요소→1/11/24 tet)·sf_tetvol.f(부호체적) + 공극 sf_mdporo.f:151·305-317(GGV/GGX/GGY/GGZ 감소) + FSI 드라이버 sf_str0-3.f·sf_str_obst.f:63·72-74(VF_CGLV 전달) + 가동상 sf_stm0-3.f·sf_dpth_update.f + 위치갱신 sf_pos_update2.f:20-34(MPI POS/DVEL 외부 구조solver) + 법선 sf_cross2.f·sf_nrmvec.f·런업면 sf_rface0.f:14-29. file:line 직접 인용."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-23
related:
  - models/CADMAS-SURF/source-analysis/cadmas-2f-twophase-compressible-gas.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-turbulence-and-porous-resistance.md
  - models/CADMAS-SURF/README.md
---

# CADMAS-2F 유체-구조 결합 (sf_* cut-cell 공극엔진)

> CADMAS-2F 의 `sf_*` 패밀리(388 Fortran 중 다수)는 **2상 물리가 아니라** 별도 **유체-구조 결합층**: 변형/이동하는 FE 구조메시(`sf_str*`)·가동상 지형(`sf_stm*`)을 직교격자에 **사면체 다면체 클리핑(cut-cell)**으로 잘라 셀 개방체적·면개구율(`GGV/GGX/GGY/GGZ`=공극·면적투과율)을 산출 → [porous body 운동량](cadmas-surf3d-turbulence-and-porous-resistance.md#b-포러스-body-저항-소파블록투과방파제)에 공급. 2상 기상은 [cadmas-2f-twophase-compressible-gas](cadmas-2f-twophase-compressible-gas.md). 경로 루트: `raw/.../Simulators/CADMAS-SURF-3D2F/Source code/`.

## 1. 정체 — 구조커플링이지 2상 아님

`sf_*`는 `vf_*`와 달리 `CDT` 헤더 스타일 다름. `SF_STRUCT.h` COMMON `/SF_STRUCT/`: `ICPL`(결합플래그)·`NELM/NNOD`(FE 요소·절점수)·`NPFC`(면수)·`ISTM`(가동상). `SF_TYPE`(`sf_type.f90`): `SPACE{IFIX;N;ID;P}` 요소별 sub-cell 다면체. 산출물은 단상/2상 공통 `VF_*` solver 의 공극 입력.

## 2. 기하 클리핑 커널 (cut-cell 부피적분)

FE 메시→직교격자 **정확 다면체 클리핑**(사면체 분해 + 6면 half-space 순차 클리핑):
- `SF_TETDIV`(`sf_tetdiv.f`): FE 요소→사면체 분해(tet→1, penta→11 `SF_MKTEPN` :18, hex→24 `SF_MKTEHX` :24)
- `SF_CUT3`(`sf_cut3.f`): 사면체를 6 셀면 평면 `XG/YG/ZG`에 `SF_CUT3X` 6중 클리핑(`:18-34`), `SF_TETVOL` 체적합(`:36`) → 클립체적 `VV` + 3 절단면적 `SX/SY/SZ`. `EPSV=Δx·Δy·Δz·1e-9`(`:12`)
- `SF_CUT3X`(`sf_cut3x.f`): 사면체 1평면 half-space 클립 — 4정점 below/on/above 분류(`:35-60`), case index `IST`로 marching-tetrahedra식 재분할(562줄). **정확 다면체 교차**(선형 PLIC 아님)
- `SF_CUT2/2X/2TR`(`sf_cut2*.f`): 2D 삼각형↔셀edge 클립(면적, `sf_pface3.f` 면적분용)
- 기하 헬퍼: `SF_TETVOL`(부호 사면체체적 3×3 행렬식/6 `sf_tetvol.f:19-21`)·`SF_S34`(삼각/사각 부호면적)·`SF_STRIA`(삼각면적)

## 3. 공극(개방률) 산출 — sf_mdporo.f

cut 기하 → 셀 분율 감소(`sf_mdporo.f`):
```
:151  CALL SF_CUT3(V,SX,SY,SZ,P(1,1,IT),XG,YG,ZG,EPS)   ! 유일 체적 caller
:305  GGV(I,J,K) = (1 - VV(I,J,K)/VV0)*GGV(I,J,K)       ! 공극 감소
:316  GGX(I,J,K) = (1 - SSX(I,J,K)/SSX0)*GGX(I,J,K)     ! 면적투과율 (GGY/GGZ 동형)
```
`P`는 FE 절점(`SF_TETDIV`)·`XG/YG/ZG`는 셀edge 좌표. 드라이버 `sf_str_obst.f:63 SF_MDPORO → :72 VF_CGLV → :74 VF_CGLXYZ` (분율을 VF solver 가상질량/관성공극에 전달). 가동상은 `SF_MDPORO_H`(`sf_mdporo_h.f`).

## 4. FSI 드라이버 (sf_str*) + 가동상 (sf_stm*)

- **`SF_STR*`=구조(FSI) 드라이버**: `sf_str0`(구조메시 read `SF_RD_OBST`·면 `SF_PFACE*`·초기 공극/BC) `sf_str1`(init/restart) `sf_str2`(스텝: 위치갱신 `SF_POS_UPDATE1/2`→공극 재계산→BC) `sf_str3`(출력). `ICPL>0` 게이트. 메인루프 호출 `SF_STR0`(`vf_a1main.f:750`)·`SF_STR1`(:996)·`SF_STR3`(:1097)·`SF_STR2`(:1141)
- **`SF_STM*`=가동상(Sea-Terrain/Movable bed)**: `sf_stm0-3` — 수심 `SF_DPTH_INIT/UPDATE`(`sf_stm1.f:14`·`sf_stm2.f:8`)·지형공극 `SF_MDPORO_H`. `ISTM==1` 게이트. 전용 `sf_stm_*_mpi_*` 서브커뮤니케이터
- 둘 다 surface-tension/stream 아님 — "str"=structure, "stm"=sea-terrain

## 5. 외부 구조 solver MPI 결합 (FSI)

`sf_pos_update2.f:20-34`: `SF_C_MPI_RECV_D(POS20)/(DVEL20)` 외부 구조solver(rank `IROOTS`)에서 변위/속도 수신 → 압력/면개구율 `AFC` 송신. = 진정한 **FSI 결합**(VOF 계면 이류 아님). `sf_volchk.f:39-43` 변형셀 `V/V0<0.2` 퇴화 가드.

## 6. 보조 — 법선·면·전치

- 법선: `SF_CROSS1`(|A×B| `sf_cross1.f`)·`SF_CROSS2`(단위 A×B/|A×B| `sf_cross2.f:5`)·`SF_NRMVEC`(요소면 법선 `sf_nrmvec.f:17`)·`SF_DIRCOS`(방향코사인). **런업면 분류용**(VOF 계면 아님): `sf_rface0.f:14-29` 법선 z성분으로 `IRFACE=1`(연직면, `CR1=-sin85°`)/`2`(수평면) — run-up/wetting 면 식별
- 면: `SF_PFACE0`(요소타입별 면연결 `sf_pface0.f:16`)·`SF_PFACE3`(면개구율 `AFC` cut `sf_pface3.f`)·`SF_RFACE0/2`(런업면)
- 전치/프레임: `SF_TRNS1/2`(국소면 좌표변환)·`SF_TRM1/2`(회전행렬, "trm"=transform-matrix)
- 토폴로지: `SF_COL3/4/COLTR`(공유면 매칭)·`SF_MEAN4`(절점중심)

## 7. MPI·IO·메모리

- MPI: `sf_bcast_*`·`sf_comm_*`·`sf_reduce_*`·`sf_mpi_*`/`sf_c_mpi_*`/`sf_stm_c_mpi_*`(send/recv/isend/irecv/wait/reduce/allreduce/barrier)
- IO: `sf_ens_geom/out`(EnSight)·`sf_send_surf/rst`·`sf_rd/wt_restart`
- 메모리: `sf_alloc0/1`·`sf_dealloc`·`sf_realloc`·`sf_dcopy/icopy`

> 결론: CADMAS-2F 는 **기액 압축성 2상**([twophase 노트](cadmas-2f-twophase-compressible-gas.md)) + **이동구조/가동상 FSI cut-cell 공극엔진**(본 노트) 두 축을 단상 SURF/3D 에 추가. `sf_*`는 **PLIC/Youngs 계면 재구성이 아니라 고체 다면체 정확 클리핑**.
