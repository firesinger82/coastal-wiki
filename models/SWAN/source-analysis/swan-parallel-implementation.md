---
title: "swan parallel implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-parallel-implementation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시. 2026-10-13 recovery 대조 보고서 R1–R8 반영"
last_source_check: "2026-10-13 (recovery 대조 반영)"
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# SWAN parallel implementation — MPI domain decomp + OpenMP sweeps

## Scope note

스레드 동기화와 MPI 실행은 서로 다른 경로이다. 현행 CMake는 OPENMP와 MPI의 동시 선택을 거부한다. `src/CMakeLists.txt:71–79`의 원문은 `if( OPENMP AND MPI )`와 `message( FATAL_ERROR "-- Cannot use both OpenMP and MPI" )`이다. [R1 §4](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#4-노트-대조와-수정안), [R7:N-029](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론).

## Source basis

Codex deep scan 2026-05-06 of:
- `src/swanmain.ftn` — main entry, MPI/OMP setup
- `src/swanparll.ftn` — MPI domain decomposition
- `src/swancom1.ftn` — OpenMP region, sweep parallelism, reductions
- `src/swmod*.ftn` — parallel state holders

## A. MPI initialization

- `MPI_INIT`, `MPI_COMM_RANK`, `MPI_COMM_SIZE` are inside `SWINITMPI` at `[file=src/swanparll.ftn line=140]`, `[file=src/swanparll.ftn line=157]`, `[file=src/swanparll.ftn line=173]`
- These calls are tagged with `!MPI!NCOH` markers — meaning they are conditionally activated at compile time (preprocessor) for MPI builds; serial builds skip them
- Serial defaults: `INODE = 0`, `NPROC = 1` at `[file=src/swanparll.ftn line=152-153]`
- Rank conversion: `INODE = INODE + 1` at `[file=src/swanparll.ftn line=158]` (MPI 0-based → SWAN 1-based)
- Master detection: `IAMMASTER = INODE.EQ.MASTER` at `[file=src/swanparll.ftn line=196]`, with `MASTER` parameter at `[file=src/swmod2.ftn line=1145]` (= 1 in SWAN's 1-based indexing, i.e., MPI rank 0)

## B. MPI domain decomposition

Main path: `SWDECOMP → SWPARTIT → SWBLADM → ...`

- `SWDECOMP` at `[file=src/swanparll.ftn line=2649]`
- `SWBLADM` at `[file=src/swanparll.ftn line=2411]`
- `SWCOLLECT` at `[file=src/swanparll.ftn line=3560]`

### Local extents

`SWBLADM` scans `IPOWN(IX,IY) == INODE` to derive local bounding box `MXF, MXL, MYF, MYL` at `[file=src/swanparll.ftn line=2489-2498]`.

### Halo expansion

실제 halo 폭은 공간 기법별 1·2·3이 아니라 빌드 선택별 JAC=1·WFR=3이다. 공간 기법을 보고 폭을 바꾸는 대입은 없다. `src/swmod2.ftn:1148–1149`의 원문은 `!JAC     &           IHALOX = 1, IHALOY = 1`과 `!WFR     &          ,IHALOX = 3, IHALOY = 3`이다. `IHALOX, IHALOY`는 아래 범위 확장에 사용된다:
```
MXF -= IHALOX
MXL += IHALOX
(clamped to domain bounds)
```
at `[file=src/swanparll.ftn line=2525-2528]`.

### Edge flags

`LMXF, LMXL, LMYF, LMYL` set from bounds + node position (`INODE==1` / `INODE==NPROC`) with orientation-dependent logic at `[file=src/swanparll.ftn line=2534-2543]`.

### Ghost interface metadata

Per-neighbor send/recv indices (`ICSEND`, `ICRECV`) packed into `IBLKAD` at `[file=src/swanparll.ftn line=2557-2643]`.

### Local sizes finalized

```
MXC = MXL - MXF + 1
MYC = MYL - MYF + 1
MCGRD = (recomputed over cropped box)
```
at `[file=src/swanparll.ftn line=2798-2805]`.

**No `IXOFFS`, `IYOFFS`, `MXC_LOCAL`, `MYC_LOCAL` symbols** in this codebase — SWAN reuses `MXF/MXL/MYF/MYL` and resized `MXC/MYC` directly.

## C. MPI message passing during sweep

### Wrappers

- `SWSYNC` (global barrier) at `[file=src/swanparll.ftn line=329]`, `[file=src/swanparll.ftn line=437]` — wraps `MPI_BARRIER` (also `!MPI!NCOH` tagged)
- `SWSENDNB` (point-to-point send) at `[file=src/swanparll.ftn line=454]`, `[file=src/swanparll.ftn line=569-570]` — `MPI_SEND` to `IDEST-1`
- `SWRECVNB` (blocking receive) at `[file=src/swanparll.ftn line=587]`, `[file=src/swanparll.ftn line=708-709]` — `MPI_RECV` from `ISOURCE-1`

### Halo exchange during sweep

`SWEXCHG` (WFR variant) at `[file=src/swanparll.ftn line=3044]`, `[file=src/swanparll.ftn line=3197]`, `[file=src/swanparll.ftn line=3215]` iterates neighbors and calls `SWSENDNB` then `SWRECVNB` using `IBLKAD` interface maps.

Sweep-phase row/interface exchanges (`SWRECVAC`, `SWSENDAC`, `SWEXCHG`) called from `swancom1.ftn` at `[file=src/swancom1.ftn line=1964-1968]`, `[file=src/swancom1.ftn line=2058-2062]`, `[file=src/swancom1.ftn line=2107]`.

MPI 호출 명칭에 관한 주장은 SWSENDNB·SWRECVNB wrapper에 한정한다. 이 wrapper는 `src/swanparll.ftn:569–570`의 `MPI_SEND`와 `src/swanparll.ftn:708–709`의 `MPI_RECV`를 각각 쓴다. [R1 §4](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#4-노트-대조와-수정안).

## D. OpenMP parallelism in `SWCOMP`

### Main parallel region

`[file=src/swancom1.ftn line=1170-1188]`:
```fortran
!$OMP PARALLEL DEFAULT(SHARED)
!$OMP+ PRIVATE(...)        ! extensive list
!$OMP+ COPYIN(...)         ! threadprivate imports
```

### Barriers and FLUSH

- Barriers at `[file=src/swancom1.ftn line=1424]`, `[file=src/swancom1.ftn line=1692]`, `[file=src/swancom1.ftn line=1733]`, `[file=src/swancom1.ftn line=1854]`, `[file=src/swancom1.ftn line=2098]`, `[file=src/swancom1.ftn line=2126]`, `[file=src/swancom1.ftn line=2344]`
- `!$OMP FLUSH` at `[file=src/swancom1.ftn line=1855]`, `[file=src/swancom1.ftn line=1994]`, `[file=src/swancom1.ftn line=1996]` — for ordering around lock-based dependency checks (`LLOCK`) in pipelined sweep

### Per-thread buffers

Allocated **inside** the parallel region — each thread owns private work arrays:
- `CAX, CAY, CAS, CAD, SWMATR, LSWMAT, ...` at `[file=src/swancom1.ftn line=1204-1224]`

### Sweep workload

`!$OMP DO SCHEDULE(STATIC, 1)` with `FIRSTPRIVATE/LASTPRIVATE` on `WWINT` at `[file=src/swancom1.ftn line=1936-1938]`.

정렬 OpenMP 경로는 SWMATR를 PRIVATE으로 선언한다. 하위 루틴의 IMAT*는 이 작업 배열의 전달된 절편을 읽고 쓴다. `src/swancom1.ftn:1175`의 원문은 `!$OMP+PRIVATE(SWMATR, LSWMAT, ALIMW, GROWW, IDCMIN, IDCMAX)`이다. [R8:N1-004](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론).

## E. Reduction operations

### `ACCUR` reduction (% converged points)

In `SACCUR` at `[file=src/swancom1.ftn line=4876-4886]`:
1. Thread-local `IACCURt` atomically accumulated to shared `IACCUR`
2. Master MPI global sum: `CALL SWREDUCE(IACCUR, 1, SWINT, SWSUM)`
3. Compute `% = IACCUR * 100 / NINDX`

### Hs/Tm change reduction

`[file=src/swancom1.ftn line=4779-4787]`:
- `CALL SWREDUCE(ARR, 2, SWREAL, SWSUM)`
- `CALL SWREDUCE(NINDX, 1, SWINT, SWSUM)`

### Curvature criterion

`SWSTPC` at `[file=src/swancom1.ftn line=9922-9928]` packs `[IACCUR, WETGRD]` into `IARR` and does **one** integer reduction.

### Wrappers

`SWREDUCI`/`SWREDUCR` at `[file=src/swanparll.ftn line=1279-1280]`, `[file=src/swanparll.ftn line=1415-1416]` execute `MPI_ALLREDUCE` for integer/real arrays.

## F. Boundary file I/O in parallel

Master-only read pattern:
- `[file=src/swanmain.ftn line=6908-6925]` — `IF (INODE.EQ.MASTER) CALL RBFILE ...` loop over all boundary files
- After read, broadcast: `CALL SWBROADC(BSPECS, ...)` at `[file=src/swanmain.ftn line=6929]`

Same pattern for external field files (`INAR2D` on master, then `SWBROADC`):
- Wind: `[file=src/swanmain.ftn line=8741-8749]`
- Other: `[file=src/swanmain.ftn line=8769-8777]`

`RBFILE` itself imports `IAMMASTER`: `[file=src/swanmain.ftn line=7469]`, `[file=src/swanmain.ftn line=7480]`.

So **only master process opens/reads files**; all other ranks receive via broadcast.

## G. Output collection (per-PE → global)

Two patterns in code:

### Field collection (in-memory)

`SWCOLLECT` at `[file=src/swanmain.ftn line=740]`, `[file=src/swanparll.ftn line=3560]` collects distributed fields to global form on master. Uses `SWGATHER` (MPI gather/gatherv wrapper) at `[file=src/swanparll.ftn line=3716]`, `[file=src/swanparll.ftn line=3725]`, `[file=src/swanparll.ftn line=3746]` for bounds, index maps, field data.

### File output (per-PE files merged by master)

Each process writes its own per-PE file (suffix `-###`):
- `[file=src/swanparll.ftn line=4479-4504]`
- `[file=src/swanparll.ftn line=4513-4559]`
- `[file=src/swanparll.ftn line=4820-4845]`
- `[file=src/swanparll.ftn line=4932-4998]`

Master post-processes: opens all per-PE files, merges by ownership (`BLKND`) into generic outputs.

After merge: per-process intermediate files closed/deleted at `[file=src/swanparll.ftn line=4259-4262]`.

So SWAN ships with a **built-in merge stage** — unlike ADCIRC which uses fort.80 + adcprep+adcpost, SWAN handles per-PE → global file consolidation internally.

## 빌드 선택과 비정렬 통신 (10-13 recovery 대조)

MPI·OpenMP 선택의 기본값은 OFF이다. `CMakeLists.txt:42–43`의 원문은 `option( OPENMP "" OFF )`와 `option( MPI "" OFF )`이다. OPENMP와 MPI가 함께 참이면 구성을 중단한다. `src/CMakeLists.txt:71–75`의 원문은 `if( OPENMP AND MPI )`와 `message( FATAL_ERROR "-- Cannot use both OpenMP and MPI" )`이다. [R7:I-035·C-002](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md).

swanimp §3.2.5는 METIS를 통한 비정렬 격자 분할과 분산 메모리 실행을 이미 설명한다. `src/SwanParallel.ftn90:483,504`의 원문은 `tpwgts = 1./real(np)`와 `ierr = METIS_PartGraphKway (nv, ncon, xadj, adjncy, vwgt, vsize, adjw, np, tpwgts, ubvec, options, edgecut, ipown)`이다. 비정렬 통신은 `src/SwanParallel.ftn90:1261,1274,1285`의 `MPI_IRECV`·`MPI_ISEND`·`MPI_WAITALL` 경로를 쓴다. CMake의 METIS 기본값은 OFF이다. [R1:TN-185](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론).

## Decision Guide

| Configuration | Run command | Notes |
|---------------|-------------|-------|
| Single CPU serial | `swanrun -input X` | no MPI/OMP |
| OpenMP | `swanrun -input X -omp N` | UNIX 래퍼는 외부 OMP_NUM_THREADS를 처음에 1로 덮어쓴다. `bin/swanrun:10` `export OMP_NUM_THREADS=1` |
| MPI | `swanrun -input X -mpi N` | 기본 명령 파일은 INPUT이다. `src/ocpids.ftn:182` `INPFIL = 'INPUT'` |
| Coupled with ADCIRC | controlled by ADCIRC's MPI | SWAN inherits MPI comm |

## Working Rules

1. **OpenMP defaults to SHARED** in the parallel region — any custom code added inside must explicitly mark variables PRIVATE if per-thread state.
2. **Master-only I/O** is enforced: never call `OPEN`/`READ` from inside a parallel region. Use `IF(IAMMASTER)` or move outside.
3. “hybrid”를 기본 빌드 지원의 증거로 사용하지 않는다. OPENMP와 MPI가 함께 참이면 구성을 중단한다. `src/CMakeLists.txt:71–75`의 원문은 `if( OPENMP AND MPI )`와 `message( FATAL_ERROR "-- Cannot use both OpenMP and MPI" )`이다.
4. **`SWCOLLECT` brings distributed arrays to master** — used before global output operations.
5. **Built-in per-PE file merge** — no external `swanpost` step needed; output files are unified after run.

## Common Pitfalls

- **Custom variables in OMP region not declared PRIVATE** → race conditions visible only with `OMP_NUM_THREADS > 1`.
- **Reading an input file from a non-master rank** → blocks or deadlocks the run.
- **Mismatched `IBLKAD`** between neighbors → halo data corruption silently ruins sweep convergence.
- **Forgetting `SWBROADC` after master-side read** → other ranks see uninitialized boundary data.
- **MPI build flags missing** → `!MPI!NCOH` tags become no-ops; runs as serial despite `-np N`.

## References

- `src/swanmain.ftn` — main entry, master-only read patterns, `SWCOLLECT` for output.
- `src/swanparll.ftn` — `SWINITMPI`, `SWDECOMP`/`SWBLADM`, `SWSYNC`/`SWSENDNB`/`SWRECVNB`, `SWEXCHG`, `SWREDUCE`/`SWGATHER`, per-PE file merge.
- `src/swancom1.ftn` — OpenMP `PARALLEL` region, sweep `OMP DO`, `SACCUR`/`SWSTPC` reductions.
- `src/swmod2.ftn` — `MASTER` parameter, `IAMMASTER`, `INODE`, `NPROC`.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex scan | 50+ file:line citations |
| Coverage | MPI init + decomp, halo exchange, OpenMP region, reductions, master I/O, output merge |
| Review status | 2026-10-13 recovery 대조 보고서 R1–R8 반영 |

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R1:TN-176 | halo 폭 | swantech PDF 137쪽 / 인쇄 129쪽: 연속된 비중첩 소영역을 각 프로세서에 배정한다. halo 폭은 BSBT·SORDUP·S&L에서 각각 1·2·3이다 | `src/swanparll.ftn:2525–2528`: `MXF = MAX(1  ,MXF-IHALOX)`; `MYF = MAX(1  ,MYF-IHALOY)`; `MXL = MIN(MXC,MXL+IHALOX)`; `MYL = MIN(MYC,MYL+IHALOY)`. `src/swmod2.ftn:1148–1149`: `!JAC     &           IHALOX = 1, IHALOY = 1`; `!WFR     &          ,IHALOX = 3, IHALOY = 3`. | B 문서 오기 | 해석: 실제 halo 폭은 공간 기법별 1·2·3이 아니라 빌드 선택별 JAC=1·WFR=3이다. 공간 기법을 보고 폭을 바꾸는 대입은 없다. 소유권 비중첩과 halo 배열 중첩은 양립한다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-178 | 영역 분할 가중치 | swantech PDF 138쪽 / 인쇄 130쪽: 소영역 크기 $=$ 총 wet점 수 / 소영역 수 | `src/swanparll.ftn:2277,2291–2292`: `IF ( KGRPGL(IX,IY).NE.1 ) THEN`; `IWORK(2,I) = (NACTP*ICNT)/SUM(IWEIG) - NPCUM`; `NPCUM      = (NACTP*ICNT)/SUM(IWEIG)`.<br>swanuse PDF 21–22·46쪽의 예외값 격자와 MPI 부하 분산 설명. | C 문서 누락 | 분할 기준은 활성 계산점 표지이며 프로세서별 `IWEIG`를 적용한다. swanuse가 말하는 예외값 제외 격자는 이 활성점 개념과 대응한다. C는 swantech 제7장의 균등 wet점 설명에 가중치와 동적 수심 검사의 구분이 없는 점이다. 같은 가중치에서는 균등 크기에 대응한다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-183 | 병렬 성능·권고 | swantech PDF 138,140쪽–141쪽 / 인쇄 130,132쪽–133쪽: 동적 부하 재분배가 불필요하다는 경험; speedup·scalability; Jacobi 반복 증가; 곡률 기준 권고.<br>TN-179–182의 구현. | — | H 코드 대조 대상 아님 | 특정 실험의 병렬 성능 주장과 권고이다. 성능의 관측값과 구현 알고리즘을 구분하는 H 판정이다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R1:TN-185 | METIS 비정렬 병렬 경로 | 제7장 swantech PDF 137쪽–141쪽 / 인쇄 129쪽–133쪽에는 METIS 비정렬 통신식이 없다 | `src/SwanParallel.ftn90:483,504`: `tpwgts = 1./real(np)`; `ierr = METIS_PartGraphKway (nv, ncon, xadj, adjncy, vwgt, vsize, adjw, np, tpwgts, ubvec, options, edgecut, ipown)`; 1261·1274·1285의 `MPI_IRECV`·`MPI_ISEND`·`MPI_WAITALL`.<br>swanimp PDF 19·22·25쪽 및 웹 [METIS 지원](../raw/manuals/website/online_doc/swanimp/node13.html):48–53, [CMake 옵션](../raw/manuals/website/online_doc/swanimp/node17.html):79–81. `src/SwanCompUnstruc.ftn90:1350–1355`; `switch.pl:89,101`. | C 문서 누락 | swanimp §3.2.5는 METIS를 통한 비정렬 격자 분할과 분산 메모리 실행을 이미 설명한다. `-metis`의 분할 활성화도 swanimp에 있다. C는 swantech 제7장에 가중치 균등 분할 `tpwgts = 1./real(np)`·`MPI_IRECV`/`MPI_ISEND`/`MPI_WAITALL` 교환·`if ( ACUPDA .and. PARLL ) then` 조건이 없는 점이다. 호출의 `!METIS`와 통신의 `!MPI`는 해당 빌드 선택에서 활성화된다. CMake의 METIS 기본값은 OFF이다. [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론) |
| R4:T1-066 | MODE ONED의 병렬 제한 | swanuse PDF 37쪽–38쪽 / 인쇄 29쪽–30쪽의 MODE 설명에는 병렬 제한이 없다 | `src/swanpre1.ftn:760` `IF (PARLL) THEN`; 761 `CALL MSGERR(4,'1D mode is not supported in parallel run')`. | C 문서 누락 | MODE ONED는 병렬 실행에서 중단 오류를 낸다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R7:I-049 | OMP_NUM_THREADS | swanimp PDF 32쪽–33쪽, 인쇄 26쪽–27쪽: `export OMP_NUM_THREADS=4`; `the UNIX script will set OMP NUM THREADS to n`; swanimp PDF 33쪽: `default: n = 1` | `bin/swanrun:10` `export OMP_NUM_THREADS=1`; 85행 `export OMP_NUM_THREADS=$npomp` | C 문서 누락 | swanimp는 `-omp n`의 설정과 생략 시 기본값 1을 적는다. Unix 래퍼는 시작할 때 기존 `OMP_NUM_THREADS`도 1로 덮어쓴다. C는 외부 환경 값까지 덮어쓰는 초기화 설명이 없는 부분에 한정한다. 1보다 큰 스레드 수를 래퍼에 전달하려면 `-omp n`을 사용한다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:I-053 | machinefile | swanimp PDF 33쪽, 인쇄 27쪽: `one node per line`; `node2:2`; `a space should be used instead of a colon`; 같은 쪽: `may also need a machinefile` | `bin/swanrun:93` `mpirun -np $npmpi -machinefile machinefile swan.exe`; `bin/swanrun.bat:39` `mpiexec -n %nprocs% swan.exe` | C 문서 누락 | swanimp의 `may also need a machinefile`은 조건부 안내이다. Unix 래퍼는 `-machinefile machinefile`을 전달한다. Windows 래퍼의 `mpiexec -n %nprocs% swan.exe`에는 이 인자가 없다. C는 Windows용 파일 구문을 안내하면서 제공 배치 파일에는 전달 절차가 없다는 부분에 한정한다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:C-002 | OpenMP와 MPI의 동시 선택 거부 | swanimp PDF 25쪽의 MPI·OPENMP 옵션 표에는 동시 선택 시의 구성 중단 조건이 없다 | `src/CMakeLists.txt:17–19,71–75` `set( MPI ON )`, `if( OPENMP AND MPI )`, `message( FATAL_ERROR "-- Cannot use both OpenMP and MPI" )` | C 문서 누락 | OPENMP와 MPI가 함께 참이면 구성을 중단한다. JAC는 18행 `set( MPI ON )`으로 MPI를 켠다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:C-003 | Metis 선택의 MPI 의존성 미검사 | swanimp PDF 22쪽(인쇄 16쪽), `models/SWAN/raw/manuals/website/online_doc/swanimp/node13.html:48–51`은 `an MPI implementation is still required`라고 적는다. CMake가 MPI 옵션을 켜거나 의존성을 검사하는지는 적지 않는다 | `src/CMakeLists.txt:17–24` `if( JAC )`, `set( MPI ON )`, `if( METIS )`, `list( APPEND SWITCHES -metis )` | C 문서 누락 | Metis의 MPI 요구는 문서에 있다. METIS만 선택해도 CMake는 -metis를 추가한다. 이 분기는 JAC 분기와 달리 MPI를 자동으로 켜지 않는다. C는 이 옵션 처리 차이의 설명 누락으로 한정한다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:C-004 | 비 GNU MPI의 호환 모듈 스위치 | swanimp PDF 20쪽(인쇄 14쪽)은 USE MPI를 지원하지 않는 컴파일러의 -impi를 설명한다. CMake가 GNU 여부만으로 이를 선택하는 규칙은 적지 않는다 | `src/CMakeLists.txt:9–14` `if( MPI OR JAC )`, `if( CMAKE_Fortran_COMPILER_ID MATCHES "GNU" )`, `list( APPEND SWITCHES -impi -mpi )` | C 문서 누락 | MPI 또는 JAC를 선택하면 GNU 이외 컴파일러에 -impi와 -mpi를 함께 추가한다. 문서의 USE MPI 호환성 설명과 이 CMake 선택 규칙을 구분한다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:C-013 | 병렬 라이브러리 검색 캐시 정리 | swanimp PDF 25쪽의 병렬 옵션 표에는 다른 병렬 방식의 탐색 캐시를 지우는 규칙이 없다 | `src/CMakeLists.txt:81–94` `unset( MPI_Fortran_FOUND CACHE )`, `unset( OpenMP_Fortran_FLAGS CACHE )` | C 문서 누락 | OpenMP 경로는 MPI 검색 캐시를 지운다. MPI 경로는 OpenMP_Fortran_FLAGS 캐시를 지운다. 직렬 경로는 두 종류의 캐시를 지운다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:C-014 | OpenMP 환경 변수 초기화 | swanimp PDF 32쪽–33쪽과 `models/SWAN/raw/manuals/website/online_doc/swanimp/node20.html:172–184`는 -omp n의 환경 변수 설정과 생략값 n=1을 설명한다. 기존 환경 값을 래퍼 시작 때 덮어쓰는 동작은 적지 않는다 | `bin/swanrun:7–10,84–85` `export OMP_NUM_THREADS=1`, `if [ $npomp -gt 1 ]; then`, `export OMP_NUM_THREADS=$npomp` | C 문서 누락 | -omp n의 설정과 생략값 1은 문서에 있다. UNIX 래퍼는 시작할 때 기존 OMP_NUM_THREADS도 1로 덮어쓴다. n이 1보다 클 때만 실행 직전에 다시 설정한다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:C-017 | MPI 실행기 탐색 조건 | swanimp PDF 32쪽은 MPI 실행기의 PATH 설정을 설명한다. 래퍼가 mpirun을 일반 파일 여부로 찾는 조건은 적지 않는다 | `bin/swanrun:47–54`의 IFS 설정과 PATH 반복; `if test -f $dir/mpirun; then`. | C 문서 누락 | PATH를 분리하려고 IFS에 콜론을 추가한다. mpirun을 일반 파일 여부로 검사한다. 실행 권한 검사는 이 조건에 없다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:C-020 | MPI 탐지 후 로컬 심볼릭 링크 | 공개 patch 41.51.A:366–368,390–391에 심볼릭 링크 생성·정리 문맥이 있다. swanimp 제5장에는 MPI 실행기를 발견하면 단일 프로세스에서도 링크 분기에 들어가는 조건이 없다 | `bin/swanrun:47–54,87–95,129–130` `elif [ $npmpi -gt 1 -o ! -z "$mpi" ]; then`, ``ln -s `which swan.exe` swan.exe`` | C 문서 누락 | mpirun을 발견하고 OpenMP 분기를 선택하지 않으면 프로세스 수가 1이어도 링크 분기에 들어갈 수 있다. 로컬 swan.exe가 없으면 링크를 만든다. 정리는 이번 호출이 만든 링크에 한정한다. C는 단일 프로세스에서 이 분기에 들어가는 조건의 설명 누락이다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:N-027 | OpenMP 실행 명령 | `models/SWAN/source-analysis/swan-parallel-implementation.md:183` ``\| OpenMP only (multi-core, single node) \| `OMP_NUM_THREADS=N swanrun -input X` \| thread per core \|``; swanimp PDF 33쪽(인쇄 27쪽), `models/SWAN/raw/manuals/website/online_doc/swanimp/node20.html:163–184`의 -omp n 안내 | `bin/swanrun:10` `export OMP_NUM_THREADS=1`; 20행 -omp 판독; 84–86행 `if [ $npomp -gt 1 ]; then`, `export OMP_NUM_THREADS=$npomp`. | B 문서 오기 | UNIX 래퍼는 외부 OMP_NUM_THREADS를 처음에 1로 덮어쓴다. 노트의 래퍼 실행 예시는 `swanrun -input X -omp N`으로 고친다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:N-028 | MPI 입력 전달 | `models/SWAN/source-analysis/swan-parallel-implementation.md:184` ``\| MPI only (multi-node) \| `mpirun -np N swan.exe < X` \| requires MPI build \|``; swanimp PDF 27쪽(인쇄 21쪽), `models/SWAN/raw/manuals/website/online_doc/swanimp/node19.html:58–63`의 기본 명령 파일 INPUT | `src/ocpids.ftn:181–182` `INPUTF = 3`, `INPFIL = 'INPUT'`; 293–299행 `IF (INPFIL.NE.'    ') THEN`에서 FILE=INPFIL을 연다. `bin/swanrun:81–83,92–93`의 X.swn→INPUT 복사와 mpirun 호출. | B 문서 오기 | 기본 swaninit에서는 표준입력 리다이렉션만으로 명령 파일을 바꿀 수 없다. X.swn을 입력하는 래퍼 예시는 `swanrun -input X -mpi N`이다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:N-029 | 혼합 병렬 권고 | `models/SWAN/source-analysis/swan-parallel-implementation.md:185` ``\| Hybrid MPI + OMP \| `OMP_NUM_THREADS=K mpirun -np N swan.exe < X` \| best for many-core nodes \|`` | `src/CMakeLists.txt:71–79` `if( OPENMP AND MPI )`, `message( FATAL_ERROR "-- Cannot use both OpenMP and MPI" )`; `src/ocpids.ftn:181–182,293–299`의 기본 INPUT 파일 열기. | B 문서 오기 | 현행 CMake는 OPENMP와 MPI의 동시 선택을 거부한다. 이 배포의 지원 실행 예시에서 hybrid 행을 제외한다. 기본 명령 파일은 INPUT이다. ‘best for many-core nodes’라는 성능 순위는 이 코드 근거에서 도출되지 않는다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
