---
title: "STR3D 접촉역학·유체결합 — MPC node-to-surface 접촉·정규화 Coulomb 마찰·STR3D↔CADMAS-2FC MPMD 압력/변위 교환 (contact·mpccorr·npfface·recv_pres·send_pos)"
model: CADMAS-SURF
component: src (STR3D contact mechanics + fluid coupling)
canonical_source: self
verification_method: "STR3D 소스 직접 read (raw/.../Simulators/STR3D/Source code/). 접촉 contact/contact.f:1-54(상태머신 POINT/EDGE/FACE)·MPC 투영 mpccorr.f:11-25·mpccorr11/12/13.f·제약기하 spcdface1.f:6-8·corrface1.f:6-7·MPC소거 mpcset/mpcslv.f + 마찰 npfface.f:39-40(arctan Coulomb)·:43-125(bilinear stick-slip)·캡 :11-19(FN≥0) + 결합 mod_comm.f90:40-41·57(comm_2fc_str)·c_mpi_init.f:8(CPLWORLD) + 수신 recv_surf.f·recv_pres.f(PRESS/AFC/IPND)·하중 pld_cadmas.f:46-49(FT-=FC·AFC) + 송신 send_pos.f(POS 변형위치)·glb_comm.f:15-64(opcode). file:line 직접 인용. 전제 교정: 접촉=MPC(penalty 아님)."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-23
related:
  - models/CADMAS-SURF/source-analysis/str3d-fem-core-newmark-elasto-plastic.md
  - models/CADMAS-SURF/source-analysis/cadmas-2f-structure-coupling-cutcell.md
  - models/CADMAS-SURF/README.md
---

# STR3D 접촉역학·유체결합

> STR3D 의 (A) 구조-구조/지반 접촉(케이슨 활동·블록 충돌)과 (B) CADMAS↔STR3D 유체결합. [FEM 코어](str3d-fem-core-newmark-elasto-plastic.md)의 외부 접촉루프 + 멀티스케일 압력/변위 교환. 경로 루트: `raw/.../Simulators/STR3D/Source code/`(contact/·mpi_comm/·glb_comm/).

## A. 접촉역학 (MPC node-to-surface)

> ⚠️ **전제 교정**: penalty 법 아님. **MPC(다점제약) node-to-surface, master-slave DOF 소거** + 직접 기하투영. `pen*.f`는 penalty 아닌 **관입(penetration) 검출**. tangential 마찰(IFMDL=2)만 penalty형 강성 `RKF` 사용.

**상태머신**: slave node `I`의 상태 `ISLV(1,I)` = 1 POINT(절점-정점)·2/4 EDGE·3/5 FACE·0 FREE. 드라이버 `contact/contact.f:40-54`(`VRTXCHK/EDGECHK/FACECHK/PENCHK` 디스패치). 상태변화 수렴 `istchk.f:30-44`. 관입검출 `penchk.f`→provisional `penst.f:30-49`(정점11/edge12/face13, barycentric `RL`). slave 법선 `slvnrm.f:11-28`(면적가중 면법선 평균). 병렬변형 `contactp.f`(opcode `IOP=24`).

**제약 강제** (매 접촉 sub-iteration, `MPCCORR`, `nl_static.f:88`): slave를 master에 직접투영하고 `UG·POS` 보정:
- `mpccorr11.f:6-9`(정점): `DUG=POS(MA)-POS(NS); UG+=DUG; POS+=DUG`
- `mpccorr12.f:23-32`(edge): 파라미터 `T` 투영 + 기존 SPC DOF 처리
- `mpccorr13.f:24-35`(face): barycentric `RL`→`SPCDFACE1/2/3`(기제약 DOF수 `NC`별)
- 제약기하: `spcdface1.f:6-8`(`P=RL(1)X1+RL(2)X2+RL(3)X3` 면상 접촉점)·`corrface1.f:6-7`(gap `H`→보정 `DUG=-H·RN`)

**시스템 MPC 소거**: `mpcset.f`(종속 DOF 테이블)·`mpcslv.f`([B][C] 제약변환 sparse)·`MPCTRNS/RMPCCAL`(요소강성 적용, `fricstf.f:38`). 접촉 DOF는 master-slave 소거 = MPC 법.

**마찰 — 정규화 Coulomb** (`‖FT‖≤μ·FN` 캡, `IFMDL=KK(96)`):
- `IFMDL=1` **arctan 평활**(`npfface.f:39-40`): `RMU=(2μ₀/π)·atan(|vr|/vr₀)`·`FT=RMU·FN·vr/|vr|`, 일관접선 `estfface.f:31-48`
- `IFMDL=2` **bilinear stick-slip**(`npfface.f:43-125`): stick `RKF=μ₀FN/EPS0`→slip `RKF=μ₀FN/|vr|`, 정/동마찰 `RMU0/RMUD`, 접선강성 `estfface.f:52-83`
- 법선력 캡(인장불가): `npfface.f:11-19` `CROSS2(...RN); VECML1(FN,F,RN); FN=MAX(FN,0)`
- edge 병렬커널 `npfedge/estfedge/fricedge.f`

**접촉 sub-iteration** (`nl_static.f:72` `DO ITER2=1,MAXITER2=20`, `I_BCT>0`): ①`MPCCORR` 투영 보정 ②`FRICSET` 마찰참조 ③Newton(`NPFRIC` RHS·`FRICSTF` 접선) ④`CNTRFC` 반력 ⑤`CONTACT` 상태재평가, `ICONV2` 무변화 시 EXIT.

## B. 유체결합 (STR3D ↔ CADMAS-SURF/2FC)

**MPMD — CADMAS 와 동일 프레임워크** (`module/mod_comm.f90`): STR3D 모델ID `my_model=l_str`(14, `:40-41`), 파트너 CADMAS-2FC(`l_cadmas_2fc=11`). 전용 inter-model 커뮤니케이터 **`comm_2fc_str`**(`:57`, `mpi_comm_split` :209). 결합월드 `CPLWORLD=COMM_WORK_2FC_STR`(`mpi_comm/c_mpi_init.f:8`), 모든 `C_MPI_*` 가 사용. `ICPL==2`일 때 결합 활성(`c_mpi_init.f:31`).

**STR3D 수신** (CADMAS→STR3D):
- `RECV_SURF`(`mpi_comm/recv_surf.f`, opcode 11): `WLEVEL/ALEVEL`(수위·기압쿠션) + `NPFC`(압력면수)·`IPFC`(면연결)·`AFC`(젖음면적률)·`IPND`(절점압력플래그). `astea_mechanical.f:72`
- `RECV_PRES`(`recv_pres.f`, opcode 12): **`PRESS(NNOD)`**(구조절점 표면압) + `AFC/IPND` 갱신 + 다음결합시각 `TNEXT`. `nl_static.f:46`(ICPL=2). = CADMAS-2F `sf_pos_update2.f` 대응측

**압력→절점력** (하중조립): `mdpress.f`(CADMAS 압력→구조표면 절점 barycentric 투영; 완전수몰 `IPND=2`는 정수압 fallback `(WLEVEL-z)·g·1e3` :14-17). `pld_cadmas.f:34-49`: 절점압 `PPND`을 면 `IPFC` 상 `LOADTR1/QU2` 형상함수 적분→`AFC` 가중→**음부호** `FT(1:3,NOD) -= FC·AFC`(외향압=내향하중).

**STR3D 송신** (STR3D→CADMAS):
- `SEND_POS`(`mpi_comm/send_pos.f`, opcode 14): **`POS(3,NNOD)`**(변형 구조절점좌표) + `FLUX`(`IGEO>0`). `TIM≥TNEXT`마다. `nl_static.f:240`. → **이 변형위치가 CADMAS-2F `sf_pos_update`/표면셀 갱신에 공급**(`POS/DVEL`). 속도 `VELE` 동반
- `SEND_CONT`(`send_cont.f`, opcode 21): 접촉격자 테이블 `ICRG/ICSF/ICTB`

**glb_comm opcode 디스패처** (`glb_comm/glb_comm.f:13-64`): rank0이 `M_MPI_RECV_I(IOP)` 블록→opcode 디스패치(11 RECV_SURF0·12 RECV_PRES0·14 SEND_POS0·21 SEND_CONT0·24 CONTACT0·25 MDPRESS0). 저수준 cross-model = `mpi_comm/c_mpi_*`(CPLWORLD), intra-model gather/scatter = `glb_comm/`.

> 결합 닫힘: CADMAS 유체압→STR3D 구조해석(접촉 포함)→변형위치→CADMAS-2F cut-cell 공극 갱신([cadmas-2f-structure-coupling](cadmas-2f-structure-coupling-cutcell.md)). 양방향 FSI.
