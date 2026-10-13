---
title: "SWAN swantech Ch 7 Parallel implementation aspects — domain decomposition + load balancing + block wavefront/Jacobi verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) Ch 7 Parallel implementation aspects §7.1 Load balancing + §7.2 Parallelization of implicit propagation schemes, doc p.129-134 (무방정식 서술). References: Fox 1988, Chrisochoides et al. 1994, Tolman 2002, Meurant 1988, Van der Vorst 1989, Bastian-Horton 1991, Templates 1994, Campbell et al. 2002, Zijlema 2005."
citation_status: verified
verification_method: "swantech PDF 137–141쪽의 제7장을 대조했다. 제7장은 번호가 붙은 방정식 없이 병렬 알고리즘을 서술한다. 본문은 원문 인용과 AI 한국어 요약을 함께 포함한다. 2026-10-13 recovery 대조 보고서 R1–R8 반영분의 추가·수정 27줄을 현재 코드·과거 커밋·PDF·웹 HTML·최종 보고서와 대조했다." # [10-13 전수 검증 정정]
last_source_check: "2026-10-13 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — SPMD/halo/RCB/wavefront/Jacobi + 41.10 history verbatim"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-tech-ch3-discretization.md
  - models/SWAN/manual-notes/swan-tech-ch3-solution-iteration-limiter.md
  - models/SWAN/manual-notes/swan-tech-ch8-unstructured.md
---

# swantech Ch 7 Parallel implementation aspects — verified verbatim

> swantech.pdf (v41.51) Ch 7 직접 read (**무방정식, 서술 only**). SWAN 의 **분산메모리 병렬화** — domain decomposition + load balancing + implicit four-sweep 병렬화(block wavefront vs Jacobi). §3.3 four-sweep([swan-tech-ch3-solution-iteration-limiter](swan-tech-ch3-solution-iteration-limiter.md))의 병렬 처리.

## 1. §7 Domain decomposition (SPMD)

CFD 의 대형 sparse 계(FD/FV) 분산메모리 해법. $\vec{x}$-space 를 **contiguous·non-overlapping subdomain** 으로 분할 → 각 processor 에 할당. 동일 알고리즘이 각 processor 의 자체 데이터에 수행 (**SPMD** 모델).

- 각 subdomain 은 4 변마다 다중 neighbor 가능 → 관계 정보 저장 data structure
halo 폭은 `-jac`에서 1이고 기본 WFR에서 3이다. 공간 기법을 보고 폭을 바꾸는 대입은 없다. (`src/swmod2.ftn:1148–1149` `!JAC     &           IHALOX = 1, IHALOY = 1`; `!WFR     &          ,IHALOX = 3, IHALOY = 3`; R1:TN-176)
- subdomain 경계 데이터 교환 필요 + **stopping criterion(Eq 3.37) 평가엔 global communication**
- **MPI** 표준 (popular: **MPICH** free software) — point-to-point + collective 만 사용

## 2. §7.1 Load balancing

Subdomain→processor 매핑: 계산부하 균등 + 통신비용 최소. 직관적으론 동수 grid point contiguous block. 연안 SWAN 의 난점:
1. **wet/dry 불균등** (dry 점은 무계산)
2. tidal 로 dry↔wet 변동 → 불균형 (→ **dynamic load balancing** 가능)
3. end-user 가 직접 분할 꺼림 → **자동 분할** 필요

### 2.1 두 분할법 (Fox 1988, Chrisochoides 1994)

- **Stripwise partitioning**: 한 방향 절단 (horizontal/vertical strip). 절단방향은 interface 크기 최소화로 선택
- **RCB (Recursive Co-ordinate Bisection)**: horizontal/vertical 교대 bisection 재귀 → 통신량(interface 총크기) 추가 감소

### 2.2 SWAN 구현

정렬 영역 분할은 활성 격자 번호와 프로세서 가중치를 사용한다. 같은 가중치에서는 균등 크기에 대응한다. (`src/swanparll.ftn:2277` `IF ( KGRPGL(IX,IY).NE.1 ) THEN`; `src/swanparll.ftn:2291–2292` `IWORK(2,I) = (NACTP*ICNT)/SUM(IWEIG) - NPCUM`; `NPCUM      = (NACTP*ICNT)/SUM(IWEIG)`; R1:TN-178)

비정렬 METIS 분할과 ghost 교환은 별도 경로이다. 균등 분할 가중치는 `tpwgts = 1./real(np)`이다. 통신은 `MPI_IRECV`·`MPI_ISEND`·`MPI_WAITALL` 교환을 사용한다. (`src/SwanParallel.ftn90:483`; `src/SwanParallel.ftn90:1261,1274,1285`; R1:TN-185)
> SWAN 경험상 wet 점당 계산량이 시뮬 중 거의 일정 → **dynamic load balancing 불필요**.

### 2.3 Tolman (2002) 대안 거부

각 $p$번째 wet 점을 동일 processor 할당($p$=총 processor 수) → 자동 동수이나 **공간 전파를 효과적으로 계산 불가** (전 격자 데이터를 단일 processor 로 gather = full data transpose 필요). Domain decomposition 보다 통신 多 → SWAN 부적합.

## 3. §7.2 Implicit propagation 병렬화

Explicit 와 달리 implicit 는 subdomain interface coupling 으로 병렬화 난해. Four-sweep first sweep: $N(i,j,l,m)$ 갱신은 $N(i-1,j,l,m), N(i,j-1,l,m)$ 갱신 후에야 → 병렬 불가. 수정 필요 (이상적: 순차 대비 연산 증가 없이).

### 3.1 Block Jacobi (multicolor)

Subdomain interface 데이터를 **explicit 처리** = implicit 연산자의 **block Jacobi 근사**. RCB 분할(균형·저통신) 사용. 고병렬성이나 **수렴 저하** 가능. 완화: subdomain 을 **4색**(red/yellow/green/black) 칠하고 4 sweep 의 unknown 번호를 색에 맞춰 permute (Fig 7.1) → 각 색 subdomain 이 같은 sweep 내 다른 ordering 시작 → synchronization point 감소. **Multicolor ordering** (Meurant 1988, Van der Vorst 1989).

### 3.2 Block wavefront (Bastian-Horton 1991) — 채택

도메인을 strip 분할(예: $y$축 평행). First sweep: strip 1 processor 가 $j=1$ 행 $N(i,1,l,m)$ 갱신 → strip 2 와 통신 → strip 1 의 $j=2$ 와 strip 2 의 $j=1$ 병렬 갱신 → … start-up 후 전 processor 가동 (Fig 7.2). 4 sweep 반복.
> **순차 알고리즘 연산순서 불변 → 수렴성 보존**, serial start-up/shut-down 으로 병렬효율만 다소 저하 (**Amdahl's law**). Pointwise wavefront(대각선 unknown 독립, Templates 1994; Campbell 2002 OpenMP)와 유사.

### 3.3 성능 + 버전 history (Zijlema 2005)

Beowulf cluster 실 응용 실험:
- **Block wavefront**: 좋은 speedup (strip 이 너무 얇지 않으면), 충분히 scalable → **현 운영판 채택**
- **Block Jacobi**: 성능 큰 저하 (약한 stopping criterion(§3.3)으로 iteration 배증하는 numerical overhead + 비현실적 정확도 가능)
- **버전 41.10 부터 block Jacobi 도 대안 사용 가능** (Implementation Manual 참조). 단 **curvature-based termination(§3.4) 권장** → scalability 대폭 향상 (특히 (quasi-)nonstationary)

## 4. SWAN 옵션 매핑

| Tech (PDF §7) | User cmd / 빌드 | 비고 |
|---|---|---|
| domain decomposition | MPI 빌드 (`swanrun -mpi n`) | SPMD, MPICH |
| §7.1 정렬 분할 | internal | 활성 계산점 표지와 IWEIG를 적용한다. (R1:TN-178) |
| 비정렬 분할·교환 | `-metis`, `-mpi` | METIS 분할과 ghost 교환은 별도 경로이다. (R1:TN-185) |
| §7.2 wavefront | (default 운영판) | 수렴 보존 |
| §7.2 block Jacobi | (since 41.10, Impl Manual) | curvature stopping 권장 |

## 5. 한계

- Ch 7 무방정식 — Fig 7.1(4색 block)·7.2(wavefront)는 도식 (본 노트 서술 요약).
- OpenMP(Campbell 2002) 세부는 미수록 (MPI 중심).
- RCB/multicolor 구체 알고리즘은 인용문헌 (Fox 1988, Meurant 1988 등).

## 6. 연결

- [swan-tech-ch3-discretization](swan-tech-ch3-discretization.md) — §3.2 propagation scheme; halo 폭은 빌드 선택별 JAC=1·WFR=3이다. (R1:TN-176)
- [swan-tech-ch3-solution-iteration-limiter](swan-tech-ch3-solution-iteration-limiter.md) — §3.3 four-sweep(병렬화 대상) + §3.4 curvature stopping(Jacobi scalability)
- [swan-tech-ch8-unstructured-grid-scheme](swan-tech-ch8-unstructured-grid-scheme.md) — Ch 8 unstructured 병렬(다음)

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

확정 결론과 원문 인용: [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론), [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R1:TN-176 | halo 폭 | swantech PDF 137쪽 / 인쇄 129쪽: 연속된 비중첩 소영역을 각 프로세서에 배정한다. halo 폭은 BSBT·SORDUP·S&L에서 각각 1·2·3이다. | `src/swanparll.ftn:2525–2528` `MXF = MAX(1  ,MXF-IHALOX)`; `MYF = MAX(1  ,MYF-IHALOY)`; `MXL = MIN(MXC,MXL+IHALOX)`; `MYL = MIN(MYC,MYL+IHALOY)`<br>`src/swmod2.ftn:1148–1149` `!JAC     &           IHALOX = 1, IHALOY = 1`; `!WFR     &          ,IHALOX = 3, IHALOY = 3` | B 문서 오기 | 해석: 실제 halo 폭은 공간 기법별 1·2·3이 아니라 빌드 선택별 JAC=1·WFR=3이다. 공간 기법을 보고 폭을 바꾸는 대입은 없다. 소유권 비중첩과 halo 배열 중첩은 양립한다. |
| R1:TN-178 | 영역 분할 가중치 | swantech PDF 138쪽 / 인쇄 130쪽: 소영역 크기 $=$ 총 wet점 수 / 소영역 수.<br>swanuse PDF 21–22·46의 예외값 격자와 MPI 부하 분산 설명. | `src/swanparll.ftn:2277,2291–2292` `IF ( KGRPGL(IX,IY).NE.1 ) THEN`; `IWORK(2,I) = (NACTP*ICNT)/SUM(IWEIG) - NPCUM`; `NPCUM      = (NACTP*ICNT)/SUM(IWEIG)` | C 문서 누락 | 분할 기준은 활성 계산점 표지이며 프로세서별 `IWEIG`를 적용한다. swanuse가 말하는 예외값 제외 격자는 이 활성점 개념과 대응한다. C는 swantech 제7장의 균등 wet점 설명에 가중치와 동적 수심 검사의 구분이 없는 점이다. 같은 가중치에서는 균등 크기에 대응한다. |
| R1:TN-183 | 병렬 성능·권고 | PDF 138,140–141/인쇄 130,132–133: 동적 부하 재분배가 불필요하다는 경험; speedup·scalability; Jacobi 반복 증가; 곡률 기준 권고. | — | H 코드 대조 대상 아님 | 특정 실험의 병렬 성능 주장과 권고이다. 성능의 관측값과 구현 알고리즘을 구분하는 H 판정이다. |
| R1:TN-185 | METIS 비정렬 병렬 경로 | 제7장 swantech PDF 137–141쪽 / 인쇄 129–133쪽에는 METIS 비정렬 통신식이 없다.<br>swanimp PDF 19·22·25 및 웹 [METIS 지원](../raw/manuals/website/online_doc/swanimp/node13.html):48–53, [CMake 옵션](../raw/manuals/website/online_doc/swanimp/node17.html):79–81. `src/SwanCompUnstruc.ftn90:1350–1355`; `switch.pl:89,101`. | `src/SwanParallel.ftn90:483,504` `tpwgts = 1./real(np)`; `ierr = METIS_PartGraphKway (nv, ncon, xadj, adjncy, vwgt, vsize, adjw, np, tpwgts, ubvec, options, edgecut, ipown)` | C 문서 누락 | swanimp §3.2.5는 METIS를 통한 비정렬 격자 분할과 분산 메모리 실행을 이미 설명한다. `-metis`의 분할 활성화도 swanimp에 있다. C는 swantech 제7장에 가중치 균등 분할 `tpwgts = 1./real(np)`·`MPI_IRECV`/`MPI_ISEND`/`MPI_WAITALL` 교환·`if ( ACUPDA .and. PARLL ) then` 조건이 없는 점이다. 호출의 `!METIS`와 통신의 `!MPI`는 해당 빌드 선택에서 활성화된다. CMake의 METIS 기본값은 OFF이다. |
| R7:H-139 | ADCIRC 기반 비구조 병렬화 | `website/modifications/modifications.htm:139` `Inclusion of parallel, unstructured mesh implementation utilizing the parallel infrastructure from ADCIRC.` | `src/SwanParallel.ftn90:504` `ierr = METIS_PartGraphKway (nv, ncon, xadj, adjncy, vwgt, vsize, adjw, np, tpwgts, ubvec, options, edgecut, ipown)`<br>`24a7d67:src/SwanParallel.ftn90:504` `    ierr = METIS_PartGraphKway (nv, ncon, xadj, adjncy, vwgt, vsize, adjw, np, tpwgts, ubvec, options, edgecut, ipown)` | A 판 차이 | 40.85의 ADCIRC 병렬 기반 도입 이후에 Git 코드는 독립 METIS 분할 경로를 추가했다(24a7d67, 2023-10-16). 현재 비정렬 MPI 절차는 내부 METIS 경로를 포함한다. METIS 경로는 METIS 빌드 옵션을 선택한 경우에 사용한다. |
| R7:H-949p | Jacobi 비정상 효율 | `website/modifications/modifications.htm:949` `An option at compile level is available to switch from the wavefront to the block Jacobi approach for parallel MPI runs. The latter is very efficient for nonstationary computations. See Implementation Manual for more details.` | `src/CMakeLists.txt:17` `if( JAC )` | H 코드 대조 대상 아님 | 계산 효율 주장이다. 빌드 분기의 존재와 성능을 구분한다. |
