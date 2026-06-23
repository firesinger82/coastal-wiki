---
title: "STR3D 선형 solver — 4 back-end(ICCG·BiCGStab 반복 / PARDISO·MUMPS 직접)·ILU 전처리·CRS 저장 (iccg·bcgstb·cg3ilu·mumps·cgindx·mkindex)"
model: CADMAS-SURF
component: src (STR3D FEM linear solver)
canonical_source: self
verification_method: "STR3D 소스 직접 read (raw/.../Simulators/STR3D/Source code/). 디스패치 KK(21)=ISOLV src/nl_static.f:154-168(1=ICCG·11=BiCGStab·3/13=PARDISO·4/14=MUMPS) + ICCG iccg.f:46-66(alpha :51·beta :64·잔차 :55·수렴 :57) + ILU 전처리 cg3ilu.f·전후치환 cg3fwb.f + BiCGStab bcgstb.f:32-61 + CRS 저장 cgindx3.f:11-31(IDSK/IDCG)·조립 cgadm.f:34-41 + 매트벡 vecmid.f + MUMPS src/mumps.f:8-14(JOB=5)·mkindex.f:263-310(COO)·module/m_mumps.f90·T티어 dmumps_struc.h(MUMPS 4.10). file:line 직접 인용."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-23
related:
  - models/CADMAS-SURF/source-analysis/str3d-fem-core-newmark-elasto-plastic.md
  - models/CADMAS-SURF/README.md
---

# STR3D 선형 solver

> STR3D FEM 시스템 `Ax=b` solve. **4 back-end**(반복 ICCG·BiCGStab / 직접 PARDISO·MUMPS), 동일 CRS 저장 공유. [FEM 코어](str3d-fem-core-newmark-elasto-plastic.md)의 Newton 매 반복 호출. 경로 루트: `raw/.../Simulators/STR3D/Source code/`.

## 1. solver 선택 — KK(21)=ISOLV

`SELECT CASE(KK(21))` (`src/nl_static.f:154-168`):
| KK(21) | solver | 종류 | 호출 |
|---|---|---|---|
| **1** | `ICCG` | IC/ILU 전처리 CG (반복) | `nl_static.f:156` |
| **11** | `BCGSTB` | BiCGStab (반복) | `:159` |
| 2 | ASESLV | (비활성) | `:162` |
| **3 / 13** | `PARSLV` | Intel PARDISO 직접 | `:165` |
| **4 / 14** | `MUMPS` | MUMPS 멀티프론탈 직접 | `:168` |

관례: `≤10`=대칭저장, `>10`=비대칭(`cgindx3.f:9`·`mkindex.f:266-270`). 인덱스/팩터라이저 셋업도 동 플래그(`src/mkindex.f:153-263`).

## 2. 반복 — ICCG (ILU 전처리 CG)

`src/iccg.f` 표준 전처리 CG. 빌딩블록(프롬프트 전제 교정 — fwb/ilu/ml = 단일 ICCG의 3요소, multigrid 아님):
- `cg3ilu.f`(불완전분해 IC/ILU, 헤더 `:4 INCOMPLETE DECOMPOSITION`; `DATA DFAC/1.5/` 대각시프트, pivot 음수 시 bump→`DFAC>5` 실패 `:30-43`)
- `cg3fwb.f`(전후치환 = 전처리 적용 `M⁻¹r`)
- `cg3ml2/ml3.f`(**매트릭스-벡터곱 `Y=A·X`**, "ml"=matrix-mult, 각행 `VECMID`)

CG 반복(`iccg.f:46-66`): `q=A·p`(`CG3ML2`)→`ALP=pᵀq`→**α=ALP1/ALP2**(`:51`)→`x+=α·p`·`r-=α·q`(`RMULT4`)→**잔차 `RES=rᵀr`**(`:55`)·수렴 `RES<TOL`(`:57`, `TOL=CGTOL²·BNRM`)→`z=M⁻¹r`(`CG3FWB`)→`BETA1=zᵀr`→**β=BETA1/BETA2**(`:64`)→`p=z+β·p`. 미수렴 `ERRSTP(21)`. `MAXITR=MXITCG` 또는 `NEQ/5`(≥50).

## 3. 반복 — BiCGStab

`src/bcgstb.f` 동일 IC/ILU 전처리(`CG3ILU2`)+`CG3FWB2`/`CG3ML3`. 반복(`:32-61`): `ALP=C1/C2`·안정자 `C3=C31/C32`·`x` 갱신(`ADDVEC`)·`RES`·`BETA=C1/(C2·C3)`. `MAXITR=NEQ/2`.

## 4. CRS 저장 + 조립

행인덱스 sparse(CRS형, 비대칭은 주석상 "skyline"): `IDSK(NEQ+1)`=행시작·`IDCG`=열인덱스·`STF/A`=값. 구축 `cgindx3.f:11-31`(`IDSK(I)=NCG·IDCG(NCG)=I`·`IDSK(NEQ+1)=NCG+1`). 연결성 `cgindx2.f`(`IELM`·DOF맵 `INDOF(6,*)`, NDF=6 shell/beam·3 그외). 대칭은 하삼각만. **조립** `cgadm.f:34-41`: 요소강성 `ESTF`를 `(IDSK,IDCG)` 인덱스로 `STF(K)+=ESTF`. 매트벡 커널 `vecmid.f`(LINPACK식 인덱스 dot/AXPY). 분산 dot `dtprdct.f`(`CG_MPI_ALLREDUCE_D` → CG가 MPI 병렬). 대각스케일 `scalsy/scalus.f`.

> 동일 `(IDSK,IDCG,STF)` CRS를 CG족·MUMPS 공유.

## 5. 직접 — MUMPS (T티어)

⬛ **T티어**: `module/dmumps_struc.h:2` `MUMPS 4.10.0`(CERFACS/CNRS/ENS Lyon/INRIA 공개, vendored 헤더 — 내부 미분석). 통합층:
- `module/m_mumps.f90`: `TYPE(DMUMPS_STRUC) MUMPS_PAR` 단일 인스턴스
- 분석/심볼릭(`mkindex.f:263-310`, `CASE(4,14)`): `JOB=-1` 초기화→**COO(IJV) 변환**(`%N=NEQ`·`%NZ=NCGSPC`·`%IRN`=행·`%JCN=>IDCG`·`%A=>STF`·`%RHS=>RHV`)→`JOB=1` 분석. `%SYM=1`(대칭, ISOLV=4)/0·`%ICNTL(14)=100`(메모리완화%)
- 팩터+solve(`src/mumps.f:8-14`): `%JOB=5`(분해+해 동시)→`DMUMPS`→`X=%RHS`. Newton 매반복 호출(`nl_static.f:168`)
- 정리(`clsindex.f:60-73`): `JOB=-2` + dealloc
- JOB 단계: `-1`초기화→`1`분석(mkindex)→`5`분해+해(mumps)→`-2`종료(clsindex)

> 반복(ICCG/BiCGStab, `cg3ilu`/`cg3fwb`/`vecmid` 커널) vs 직접(PARDISO/MUMPS). 보조 매트벡·벡터연산은 `util/`(rmult4/5·vecml3)에 — `gmtxte*.f`는 부재(전제 교정), 커널=`vecmid*.f`.
