---
title: "SWAN swantech Ch 7 Parallel implementation aspects — domain decomposition + load balancing + block wavefront/Jacobi verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) Ch 7 Parallel implementation aspects §7.1 Load balancing + §7.2 Parallelization of implicit propagation schemes, doc p.129-134 (무방정식 서술). References: Fox 1988, Chrisochoides et al. 1994, Tolman 2002, Meurant 1988, Van der Vorst 1989, Bastian-Horton 1991, Templates 1994, Campbell et al. 2002, Zijlema 2005."
citation_status: verified
verification_method: "swantech.pdf (v41.51) Ch 7 직접 read via pdftotext + website_markdown node81-83.md. Ch 7은 무방정식(서술 only) — 알고리즘·라이브러리·버전 history verbatim 정리."
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

> swantech.pdf (v41.51) Ch 7 직접 read (**무방정식, 서술 only**). SWAN 의 **분산메모리 병렬화** — domain decomposition + load balancing + implicit four-sweep 병렬화(block wavefront vs Jacobi). §3.3 four-sweep([[swan-tech-ch3-solution-iteration-limiter]])의 병렬 처리.

## 1. §7 Domain decomposition (SPMD)

CFD 의 대형 sparse 계(FD/FV) 분산메모리 해법. $\vec{x}$-space 를 **contiguous·non-overlapping subdomain** 으로 분할 → 각 processor 에 할당. 동일 알고리즘이 각 processor 의 자체 데이터에 수행 (**SPMD** 모델).

- 각 subdomain 은 4 변마다 다중 neighbor 가능 → 관계 정보 저장 data structure
- **Halo layer**: subdomain 을 **1~3 grid point auxiliary layer** 로 둘러쌈 (neighbor 의 halo data 저장). 층 수 = geographic propagation scheme 의존:
  - **BSBT → 1 점**, **SORDUP → 2 점**, **Stelling-Leendertse → 3 점** ([[swan-tech-ch3-discretization]] §3.2 stencil 폭과 일치)
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

**wet 점만 자동 분할** (subdomain 크기 = 총 wet 점 / subdomain 수). Stripwise 절차: 빈 strip 생성 → 크기 도달까지 점별 할당 → 잔여 wet 점 있으면 동일 part 에 추가, 없으면 다음 strip. → **모든 strip 직선 interface + 근사 동수 wet 점**.
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
| §7.1 partitioning | (internal, 자동 wet-only) | stripwise/RCB |
| §7.2 wavefront | (default 운영판) | 수렴 보존 |
| §7.2 block Jacobi | (since 41.10, Impl Manual) | curvature stopping 권장 |

## 5. 한계

- Ch 7 무방정식 — Fig 7.1(4색 block)·7.2(wavefront)는 도식 (본 노트 서술 요약).
- OpenMP(Campbell 2002) 세부는 미수록 (MPI 중심).
- RCB/multicolor 구체 알고리즘은 인용문헌 (Fox 1988, Meurant 1988 등).

## 6. 연결

- [[swan-tech-ch3-discretization]] — §3.2 propagation scheme (halo 1/2/3 점 = BSBT/SORDUP/S&L stencil)
- [[swan-tech-ch3-solution-iteration-limiter]] — §3.3 four-sweep(병렬화 대상) + §3.4 curvature stopping(Jacobi scalability)
- [[swan-tech-ch8-unstructured]] — Ch 8 unstructured 병렬(다음)
