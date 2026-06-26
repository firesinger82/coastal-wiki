---
title: "STR3D S티어 + geo/ 병렬 FEM 쌍둥이 — MPI통신·METIS 분할·FEMAP 출력·NASTRAN 입력 + 기하강성/pore-flow 병렬판·remesh·Rayleigh 감쇠 (mpi_comm·glb_comm·partition·femap·input·geo)"
model: CADMAS-SURF
component: src (STR3D S-tier support + parallel FEM twin)
canonical_source: self
verification_method: "STR3D 소스 전수 카탈로그 (raw/.../Simulators/STR3D/Source code/, C티어 3노트 외 잔여 디렉토리 전부). mpi_comm/(39 c_mpi/m_mpi/cg_mpi 1:1 MPI + comm_* 버퍼)·glb_comm/(40 opcode 디스패치)·util/(43)·femap/(18 FEMAP neutral 출력)·input/(NASTRAN 카드 Count/Read/Set)·partition/(20+1 METIS 분할)·geo/(31 FEM 코어 MPI 쌍둥이 geomtx/glbstfg/gmtx*/gnpf*/vel*) 헤더 인용. 적발 hidden physics: mpi_comm/remesh.f(이동메시)·src/dflt_damp.f(Rayleigh 감쇠)·util/{chtnsr,harf*}·seq/geomtx_s 형제. file:line 직접 인용."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-24
related:
  - models/CADMAS-SURF/source-analysis/str3d-fem-core-newmark-elasto-plastic.md
  - models/CADMAS-SURF/source-analysis/str3d-linear-solvers.md
  - models/CADMAS-SURF/source-analysis/str3d-contact-and-fluid-coupling.md
---

# STR3D S티어 + geo/ 병렬 FEM 쌍둥이

> STR3D 587 파일 중 [C티어 3노트](str3d-fem-core-newmark-elasto-plastic.md)(src/ 코어·solver·contact) 외 **잔여 디렉토리 전부**. (A) 순수 지원(MPI·분할·메시IO) + (B) **geo/ = FEM 물리 코어의 MPI 병렬 쌍둥이**(C티어, seq/+src/ 직렬판과 대응) + (C) 적발 hidden physics. 경로 루트: `raw/.../Simulators/STR3D/Source code/`.

## A. 순수 지원 (S티어)

### A-1 mpi_comm/ (39) — MPI 프리미티브
- 1:1 래퍼(21): `c_mpi_*`(8, cross-model allreduce/barrier/init/send/recv/waitall)·`m_mpi_*`(7, intra-model master)·`cg_mpi_*`(6, CG solver). 예 `c_mpi_send_d.f:11 MPI_SEND`
- 버퍼 pack/unpack(10): `comm_{cg,cg2,cgx,dbl,intx}`(halo gather/scatter)·`recv/send_{kk,rr}`. 순수 통신

### A-2 glb_comm/ (40) — opcode 디스패치
마스터 `glb_comm.f:13-64`(`M_MPI_RECV_I(IOP)` → `SELECT CASE(IOP)` 1-32 → `*0` 핸들러). gather/scatter `gather/scatter_nodal_{d,i}`·`gather/scatter_surface`. 핸들러(33): `recv_pres0/send_pos0/recv_surf0/output0/femap_out0/ens_geom0...` 마샬링.

### A-3 util/ (43) — 헬퍼
순수(28): `addset/clear/shift/order/mean/sumvec/addvec/subvec/rmult1-5/vecml1-3/length/errstp(MPI_ABORT)`. 사소.

### A-4 femap/ (18) — FEMAP neutral 파일 **출력** writer
(입력 아님). `femap_geom.f`(메시: block 100/403 노드/404 요소/402 prop/601 mat)·`femap_out.f`(결과: 450/1051, `fmp_nodal` 변위/속도/력·`fmp_sol` 응력 30-37·`fmp_rod/bar`·`fmp_soil` pore flux). 마커 `blk_s/blk_e`.

### A-5 input/ (Count/Read/Set 3단계) — NASTRAN bulk-data 파서
`input.f`(Count→Read→Set→Check). 카드: GRID·CTETRA/CHEXA/CPENTA·CTRIA/CQUAD·MAT1/MAT9/MATS1·PBAR(L)·FORCE/MOMENT·PLOAD*·SPC*/MPC·GRAV/RFORCE·CORD2C/R·TLOAD/RLOAD·TSTEP(NL)/NLPARM·CONTACT/FRIC/BCTSET. 순수 파싱.

### A-6 partition/ (20+1) — METIS 도메인 분할
`metis_partition.c`(METIS_PartMeshDual C 래퍼)·`part/part_c/partition/part_geom.f`(메시→그래프 분할)·`ens_geom_p.f`(파티션별 기하)·`*_tbl*`(테이블 분배)·`ex_{add,spc,spc1,pload4}`(ghost 확장). 순수 분할/통신.

### A-7 module/ S부분
`m_val.f90`(전역 메시/재료 테이블)·`input_work.f90`(파서 scratch)·`mavbl/mused.f90`(메모리 회계). ⬛ T티어: `dmumps_{root,struc}.h`(MUMPS 4.10 헤더, [solver 노트](str3d-linear-solvers.md)).

## B. ★ geo/ (31) = FEM 코어의 MPI 병렬 쌍둥이 (C티어)

[FEM 코어](str3d-fem-core-newmark-elasto-plastic.md)의 src/+seq/ 직렬판과 **대응되는 MPI 도메인분할 병렬판**(물리 동일):
- 기하강성(geometric stiffness, 초기응력): `geomtx.f`(디스패처)·`glbstfg.f`(전역 K_g 조립)·요소별 `gmtxhx2/pn2/te1/te2.f`(`∫∂N/∂x⊗∂N/∂x dV` Gauss). 직렬 쌍둥이 `seq/geomtx_s.f:1-26`·`gmtx*_s.f`
- Biot pore-flow(지반): `gnpflw/gnpflwd.f`·요소 `gnpfhx2/pn2/te1/te2.f` (직렬 `seq/gnpflw_s`)
- 속도복원: `velhx2/pn2/te1/te2.f`·`vintpn1/2.f`·`vavrg.f`
- 제약/조립: `spcdrhvg.f`·`mpctrnsg.f`·`pcnstr/pcnstri.f`·`cgadmg.f`·`cgindx1g.f`·`mergdp.f`
- 지반출력: `outsoil.f`·`wtsoil.f`·`npflow/npflowd.f`

> geo/는 [FEM 코어 노트](str3d-fem-core-newmark-elasto-plastic.md)의 물리(요소강성·Biot 지반)를 MPI 병렬로 구현 — 별도 물리 아님, 병렬 미러.

## C. 적발 hidden physics (S티어 디렉토리 내)

| 파일 | 정체 | 분류 |
|---|---|---|
| `mpi_comm/remesh.f:70-99` | 이동메시 Lagrange 보간(`DZ=ΣRL·DELZ`)+`GRID/POS` 갱신 | C티어 kinematics |
| `src/dflt_damp.f:40-56` | 기본 Rayleigh 감쇠 `CK=RLB_MIN·√(ρ/E)`·`AMAT(4)=CK·W4` | C티어 구성식 |
| `util/chtnsr.f:22-75` | 6×6 Voigt 응력/변형 회전행렬 | FEM 코어 |
| `util/harfab/harfb/...` | 대칭(1D-packed) 행렬곱 = 요소강성/질량 조립 | FEM 코어 |
| `util/areacd2·intpl` | 요소 형상좌표·테이블 보간 | FEM 코어 |
| `src/gauss_*.h` | Gauss 적분점/가중(ln_3·pn_73·te_5) | C티어 데이터([요소](str3d-fem-core-newmark-elasto-plastic.md)) |
| `femap/fmp_{nodal,sol,soil}` | 출력시 속도/응력/pore 복원 | 출력층 물리 |

> 결론: STR3D 587 전 디렉토리 포섭. 순수지원(A) + geo/ 병렬쌍둥이(B) + hidden physics 적발(C). geo/는 코어 물리의 MPI 미러로 별도 노트 불요(본 카탈로그서 매핑).
