---
title: "SWAN swantech Ch 6 Iterative solvers — Strongly Implicit Procedure (SIP) + SOR verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) Ch 6 Iterative solvers §6.1 Strongly Implicit Procedure (SIP) + §6.2 Successive Over Relaxation (SOR) technique, doc p.127-128 (Eq 6.1-6.3). References: Stone 1968, Ferziger-Perić 1999, Botta-Ellenbroek 1985."
citation_status: verified
verification_method: "swantech.pdf (v41.51) Ch 6 직접 read via pdftotext (식 번호 context-verified: AN=b 6.1·M=LU=A+K 6.2·SIP iteration 6.3) + website_markdown node78-80.md LaTeX alt-text. Ch 6은 chapter-local 번호라 website=PDF 일치. §6.2 SOR은 PDF 'under preparation' (Botta-Ellenbroek 1985 참조만).; 2026-10-13 recovery 대조 보고서 R1–R8 반영"
last_source_check: "2026-10-13 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 6.1-6.3 verbatim, PDF 식 번호 context-검증, SOR stub 명시"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-tech-ch3-solution-iteration-limiter.md
  - models/SWAN/manual-notes/swan-tech-ch4-5-bc-2d-setup.md
---

# swantech Ch 6 Iterative solvers (SIP/SOR) — verified verbatim

> swantech.pdf (v41.51) Ch 6은 SIP 원리와 SOR 절을 싣는다. 스펙트럼 SWSOR는 존재하지만 호출문이 없다. 제5장의 setup SOR와 별개의 루틴이다. (swantech PDF 135–136쪽 / 인쇄 127–128쪽; R1:TN-170–175 수정안)
>
> **식 번호 주의**: Ch 6은 chapter-local 번호 → **website = PDF 일치**.

## 1. §6.1 Strongly Implicit Procedure (SIP)

선형계:
$$A\vec{N} = \vec{b} \quad \text{(6.1)}$$
- $A$ = 비대칭 **penta-diagonal** 행렬, $\vec{N}$ = wave action vector, $\vec{b}$ = source term + 경계값
> ([swan-tech-ch3-solution-iteration-limiter](swan-tech-ch3-solution-iteration-limiter.md) §3.3 Eq 3.20 의 $A\vec{N}=\vec{b}$ 와 동일 — directional quadrant 의 spectral 계.)

### 1.1 SIP 원리 (Stone 1968, Ferziger-Perić 1999)

LU 분해는 우수한 범용 solver 이나 sparseness 활용 못함. Iterative method 서 $M = LU$ 가 $A$ 의 좋은 근사면 빠른 수렴 → **$A$ 의 근사 LU 분해를 iteration matrix $M$ 으로**:
$$M = L\,U = A + K \quad \text{(6.2)}$$
- $L, U$ sparse, $K$ small
- **ILU (incomplete LU)**: $A$ 의 0 원소엔 $L$/$U$ 대응 원소도 0. 단 $LU$ 는 $A$ 보다 비영 대각 증가 → $K$ 가 그 추가 대각 포함 (느린 수렴)
- **Stone 통찰**: elliptic PDE 근사면 해 smooth → 추가 대각 unknown 을 주변 점 보간으로 근사. $K$ 가 7 대각 모두 비영 허용 + 보간 → 주어진 근사해 $\phi$ 서 **$K\phi \approx 0$** → $M$ 이 $A$ 에 근접 (6.2)

현재 고정값은 보정 인자 0이다. 구현 골격은 SIP이지만 활성 인수분해는 Stone 교차 보정 없는 ILU 형태이다. (`src/swancom1.ftn:8438` `PARAMETER (ALFA=0.0,SMALL=1.E-15)`; `src/swancom1.ftn:8620–8621` `P1 = ALFA*CMATUA(ID ,ISM)`; `P2 = ALFA*CMAT6U(IDM,IS )`; R1:TN-175)

### 1.2 SIP iteration (Eq 6.3)

초기 추정 $\vec{N}^0$ 부터:
$$U\vec{N}^{s+1} = L^{-1}K\vec{N}^s + L^{-1}\vec{b} \quad \text{(6.3)}$$
- $U$ upper triangular → **back substitution** 효율
- $L$ 쉽게 invertible (핵심 feasibility)
- $s=0,1,2,\cdots$ 수렴까지 반복

## 2. §6.2 Successive Over Relaxation (SOR)

> **PDF "This section is under preparation. See also Botta and Ellenbroek (1985)."** — 식 미수록.

스펙트럼 SWSOR는 $\omega=0.8$의 완화 Gauss–Seidel 갱신을 구현한다. 이 값은 과소이완이다. 전 소스의 `call\s+swsor` 검색은 0건이다. swanuse의 SETUP SOR는 수위 상승을 푸는 별도 해법이다. (`src/swancom1.ftn:9036` `PARAMETER (OMEG=0.8)`; `src/swancom1.ftn:9255–9256` `AC2I = AC2I*OMEG*INVMDA(ID,IS)+`; `&                                     (1.-OMEG)*AC2(ID,IS,KCGRD(1))`; R1:TN-173)

## 3. 두 solver 의 역할 구분

| solver | 적용 계 | 행렬 | 위치 |
|---|---|---|---|
| **SIP** (§6.1, Eq 6.1-6.3) | action balance spectral 계 ($A\vec{N}=\vec{b}$) | 비대칭 penta-diagonal | [swan-tech-ch3-solution-iteration-limiter](swan-tech-ch3-solution-iteration-limiter.md) §3.3 |
| **스펙트럼 SWSOR** | 스펙트럼 갱신 | $\omega=0.8$, 호출문 없음 | R1:TN-173 |
| **SETUP SOR** | 수위 상승 | 스펙트럼 SWSOR와 별개의 해법 | [swan-tech-ch4-5-bc-2d-setup](swan-tech-ch4-5-bc-2d-setup.md) Ch 5; R1:TN-173 |

> 해법 선택은 흐름뿐 아니라 DYNDEP와 주파수 전파 설정도 따른다. (`src/swancom1.ftn:3681–3682` `ELSEIF ( (DYNDEP .OR. ICUR .EQ. 1) .AND.`; `&           PNUMS(8).NE.0.                 ) THEN`; R8:T1-010)

## 4. 한계

- §6.2 SOR 은 PDF 미완성 (under preparation) — modified SOR 알고리즘 식은 Botta-Ellenbroek(1985) 원논문 참조.
- SIP 의 $L,U,K$ 구체 7-대각 구성·보간 계수는 Stone(1968)/Ferziger-Perić(1999) 참조 (본 절은 원리 + iteration 식만).

## 5. 연결

- [swan-tech-ch3-solution-iteration-limiter](swan-tech-ch3-solution-iteration-limiter.md) — §3.3 SIP 적용 (action balance $A\vec{N}=\vec{b}$, penta-diagonal)
- [swan-tech-ch4-5-bc-2d-setup](swan-tech-ch4-5-bc-2d-setup.md) — Ch 5 SOR 적용 (2D setup Poisson $Ax=f$)

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

확정 결론과 원문 인용: [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론), [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R1:TN-171 | 문서 식 (6.3) | swantech PDF 136쪽 / 인쇄 128쪽, (6.3): $U\vec N^{s+1}=L^{-1}K\vec N^s+L^{-1}\vec b$. | `src/swancom1.ftn:8737–8739,8848–8850` `RES(ID,IS) = (RES(ID,IS) - CMAT5L(ID,IS)*RES(ID ,ISM)`; `RES(ID,IS) = RES(ID,IS) - CMAT6U(ID,IS)*RES(ID ,ISP)`; `AC2(ID,IS,KCGRD(1)) = AC2(ID,IS,KCGRD(1)) + RES(ID,IS)` | F 표기 차이 | 해석: 코드는 $LU\delta N=b-AN^s,\ N^{s+1}=N^s+\delta N$를 푼다. $LU=A+K$를 대입하면 문서 식이 된다. |
| R1:TN-172 | SIP 반복·정지·복구 | swantech PDF 136쪽 / 인쇄 128쪽: “until convergence is reached”. 수치 문턱 식은 없다.<br>swanuse PDF 95쪽 / 인쇄 87쪽 및 웹 [NUMERIC](../raw/manuals/website/online_doc/swanuse/node29.html):555–639. `src/swancom1.ftn:8808–8813`의 큰 잔차 중단과 제곱근. | `src/swancom1.ftn:8638–8639,8649,8655,8854` `EPSLIN = REPS*BNORM`; `UEPS   = 1000.*UNDFLW*BNORM`; `EPSLIN = UEPS`; `IF ( ICONV.EQ.0 .AND. IT.LT.MAXIT ) THEN`; `IF ( RNORM.GT.UNDFLW**2 .AND. RNORM.GT.EPSLIN ) ICONV = 0` | C 문서 누락 | SIP의 상대 잔차 기준과 기본 `REPS=1.E-4`, `MAXIT=20`은 swanuse에 명시되어 있다. C는 swantech §6.1에 문턱 하한 보강·큰 잔차 중단·실패 복구가 없는 점이다. 코드는 갱신 전 잔차의 2-norm을 만든다. `IF ( RNORM.GT.UNDFLW**2 .AND. RNORM.GT.EPSLIN ) ICONV = 0`으로 반복 여부를 정하고 `ICONV.EQ.0` 종료 시 `AC2OLD`로 복구한다. |
| R1:TN-173 | SWSOR 존재와 호출 | swantech PDF 136쪽 / 인쇄 128쪽, §6.2: “This section is under preparation.”<br>swanuse PDF 95 및 웹 [NUMERIC](../raw/manuals/website/online_doc/swanuse/node29.html):521–524,589–607의 SETUP·수위 상승 정지식. | `src/swancom1.ftn:9036` `PARAMETER (OMEG=0.8)`<br>`src/swancom1.ftn:9255–9256` `AC2I = AC2I*OMEG*INVMDA(ID,IS)+`; `&                                     (1.-OMEG)*AC2(ID,IS,KCGRD(1))` | C 문서 누락 | SWSOR는 $\omega=0.8$의 완화 Gauss–Seidel 갱신을 구현한다. 이 값은 과소이완이다. 전 소스의 `call\s+swsor` 검색은 0건이다. C는 swantech §6.2의 스펙트럼 해법 설명 누락이다. swanuse의 SETUP SOR는 수위 상승을 푸는 별도 해법이다. |
| R1:TN-174 | SWSOR 정지·복구 | swantech PDF 136쪽 / 인쇄 128쪽, §6.2에는 정지식이 없다.<br>swanuse PDF 95 및 웹 [NUMERIC](../raw/manuals/website/online_doc/swanuse/node29.html):589–607의 SOR 미지수는 수위 상승이다. | `src/swancom1.ftn:9258–9260,9364,9372` `RES = ABS(AC2(ID,IS,KCGRD(1)) - AC2I)`; `RESM  = RES`; `IF ( RESM.GT.REPS ) ICONV = 0`; `AC2(:,:,KCGRD(1)) = AC2OLD(:,:)` | C 문서 누락 | 스펙트럼 SWSOR의 검사량은 방정식 잔차가 아니라 최대 갱신량이다. SIP의 상대 잔차 문턱과 다르다. 상한·큰 갱신량으로 실패하면 이전 값을 복구한다. C는 swantech §6.2에 이 정지·복구 절차가 없는 점이다. swanuse의 수위 상승 SOR 정지식을 이 루틴의 설명으로 대체하지 않는다. |
| R1:TN-175 | SIP 고정 ALFA | swantech PDF 135쪽 / 인쇄 127쪽: Stone의 보간으로 $K\phi\approx0$이 되도록 보정한다는 설명. | `src/swancom1.ftn:8438` `PARAMETER (ALFA=0.0,SMALL=1.E-15)`<br>`src/swancom1.ftn:8620–8621` `P1 = ALFA*CMATUA(ID ,ISM)`; `P2 = ALFA*CMAT6U(IDM,IS )` | C 문서 누락 | 현재 고정값은 보정 인자 0이다. 구현 골격은 SIP이지만 활성 인수분해는 Stone 교차 보정 없는 ILU 형태이다. 문서는 이 고정값과 작은 대각 보강값을 적지 않는다. |
| R7:H-336p | SIP의 정확도·성능 | `website/modifications/modifications.htm:336` `The Stone's SIP solver is implemented for solving action density equation, in case of non-stationary depth or ambient current. This solver is 4 to 5 times faster than the preconditioned BiCGSTAB solver.` | `src/swancom1.ftn:3693` `CALL SWSIP ( AC2, SWMATR(1,1,JMATD), SWMATR(1,1,JMATR),` | H 코드 대조 대상 아님 | 성능·정확도·관측 적합성에 관한 문장이다. 소스 분기의 존재만으로 이 효과의 크기나 보편성을 판정하지 않는다. |
| R7:H-599 | SIP 개선 | `website/modifications/modifications.htm:599` `The SIP solver is considerably improved. (Already done with patch C of the previous version 40.31.)` | `src/swancom1.ftn:3693` `CALL SWSIP ( AC2, SWMATR(1,1,JMATD), SWMATR(1,1,JMATR),` | H 코드 대조 대상 아님 | patch C의 개선 내용이 특정되지 않은 기록이다. 현재 SWSIP 존재를 성능 개선의 증명으로 쓰지 않는다. |
