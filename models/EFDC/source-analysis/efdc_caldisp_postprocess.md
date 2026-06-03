---
title: "EFDC CALDISP2/3 — Taylor 전단분산 텐서 사후처리 (잔차 조석평균 D_xx/D_xy/D_yx/D_yy + DISTEN/UVTSC/UVERV/DISDIA.OUT)"
topic: efdc
canonical_source: self
citation_status: verified
verification_method: "models/EFDC/raw/source_code/EFDC-GVC/caldisp2.for (336 lines) + caldisp3.for (557 lines) 직접 read. 호출부 hdmt*.for (ISDISP=2/3 dispatch, N>=NDISP & NCTBC==1) + aaefdc.for (NDISP=NTS-NTSPTC+2, TPN=NTSPTC) 직접 확인. 알고리즘·출력파일·변수 file:line 인용. John Hamrick 2001-11-01 EFDC-FULL 1.0a."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — caldisp2/3 알고리즘 + 호출 맥락 verbatim"
verification_date: 2026-06-03
related:
  - models/EFDC/source-analysis/efdc_dispersion.md
  - concepts/currents/
---

# EFDC CALDISP2/CALDISP3 — Taylor 전단분산 텐서 사후처리

> `caldisp2.for`(336) + `caldisp3.for`(557) 직접 read (EFDC-GVC, John Hamrick 2001-11-01 EFDC-FULL 1.0a). **연직 전단류(vertical shear)가 유발하는 수평 dispersion 텐서**를 시뮬레이션 마지막 조석주기에 누적·산출하는 **진단 사후처리(post-process) 도구**. 본 위키 [[efdc_dispersion]] 의 HMD(수평운동량확산 Smagorinsky)와는 **별개** — 이쪽은 transport 의 effective dispersion 계수를 Taylor shear-flow dispersion 으로 도출. 운영 main loop 물리에는 미사용(진단 출력 전용).

## 1. 정체·호출 맥락 (hdmt*.for + aaefdc.for 직접 확인)

```fortran
! hdmt.for:1600-1601 (hdmt2t/hdmtgvc/hdmt1d 동일)
IF(N.GE.NDISP.AND.NCTBC.EQ.1)THEN
  IF(ISDISP.EQ.2) CALL CALDISP2
  IF(ISDISP.EQ.3) CALL CALDISP3
! aaefdc.for:307,285
NDISP = NTS - NTSPTC + 2          ! 마지막 1 조석주기부터 누적 시작
TPN   = FLOAT(NTSPTC)             ! 조석주기당 timestep 수 (정규화·평균 window)
```
- **ISDISP** (input) = 2 → CALDISP2, 3 → CALDISP3 선택. (1/0 등은 비활성)
- 누적 구간: `N ≥ NDISP` = 전체 run 의 **마지막 조석주기**(NTSPTC steps). harmonic(조석) 평균과 정합.
- 계산 대상 cell: `LCT(L)==5 .AND. SPB(L)≠0` (특정 cell type + active scalar boundary/transport cell).

## 2. 물리 — 연직 전단 + 연직혼합 → 수평 dispersion

깊이평균 대비 **velocity 편차** `UP(K)=u(K)-ū`, `VP(K)=v(K)-v̄` (line 75-89; ū=Σ DZC·u 깊이평균)가, 연직 eddy diffusivity `AB(L,K)`에 의한 혼합과 결합하여 effective 수평 dispersion 텐서 `D_xx, D_xy, D_yx, D_yy`를 생성 — **Taylor(1953/54) shear-flow dispersion** 의 이산 일반화(Hamrick 구현).

연직 implicit 확산 연산자 행렬 `CDISP` (tridiagonal, line 95-114):
```
대각: 1 - DELT·(CDZKMK·AB_{K-1} + CDZKK·AB_K)·HPI       (×DZC)
부대각: -DELT·CDZ··AB·HPI                                  (×DZC)
```
- `HPI=1/H`, `DZC`=layer thickness fraction, `CDZKK/CDZKMK`=연직격자 metric.
- **DELT**: CALDISP2 = `DT` (매 step), CALDISP3 = `NTSTBC·DT` (transport sub-cycle 배수).

## 3. 알고리즘 (누적 phase, N<NTS)

각 대상 cell L 에서:
1. **연직 연산자 역행렬** `CDISPI`:
   - CALDISP2: `SVDCMP`(특이값분해) → `CDISPT/WTMP` → `CDISPI` (line 116-144). 특이값 `SVAL` 보존.
   - CALDISP3: `LUDCMP`+`LUBKSB`(LU 분해, 단위행렬 역산, line 114-128).
2. **BDISP propagator** 갱신: `BDISP(K,KK,L) ← CDISPI · BDISP` (line 146-160) — 누적 연직 전달행렬(초기 단위행렬, line 46-50).
3. **응답함수** `FUDISP/FVDISP`: `CDISPI·(FUDISP - DT·UP/HMIN)` (line 162-176) — 전단 forcing 에 대한 velocity-deviation 응답.
4. **텐서 누적** (line 182-191): `DXXTCA += Σ DZC·UP·FUDISP · HP` 등 4성분 (XX/XY/YX/YY).
5. `CUDISPT/CVDISPT(K,L) = Σ DZC·UP·BDISP · HP` (line 193-202).

## 4. 완결 (N≥NTS, line 207-271)

steady-state dispersion 으로 마무리:
```fortran
CDISP = I - BDISP                          ! line 218-224
solve (I-BDISP) x = FUDISP   →  CSOL       ! SVBKSB(2) / LUBKSB(3)
DXXTCA = -(DXXTCA + Σ CUDISPT·CSOL)·HMIN/TPN   ! CALDISP3: TPN→TPNN=TPN/NTSTBC
... DYX/DYY/DXY 동일 ...
DXXTCA(L) = DXXTCA(L)/HLPF(L)              ! line 267 - 잔차(low-pass) 수심으로 정규화
```
- **HLPF** = low-pass(조석평균 잔차) 수심. `TPN`(=NTSPTC) = 조석주기 정규화. `HMIN` = 최소수심 scale.
- 결과 `DXXTCA/DXYTCA/DYXTCA/DYYTCA` = **조석평균 잔차 전단분산 텐서** (m²/s).

## 5. CALDISP3 전용 — 이상치 평활 (DISDIA.OUT, line 258-501) ★

`DMAX=10000` 초과/음수 텐서 성분을 **4-이웃 평균**으로 교체 (CALDISP2 엔 없음):
- `DXX<0 또는 >DMAX` → flag(`DISDIA.OUT` 기록) 후 `DXXTCA=0` → 유효 이웃(SUB/SVB face mask) 평균 `(W+E+S+N)/WTX`.
- DXY 는 `|DXY|>DMAX`, DYX 는 `DYX>DMAX`, DYY 는 `<0 또는 >DMAX` 기준.
- ※ **코드 이상**: DYX 평활 블록(line 414-430)이 `DYYSOUT/DYYNORT` 변수에 대입하면서 `DYXSOUT/DYXNORT` 를 체크 — 변수명 copy-paste 흔적(SOUT/NORT 이웃이 DYX 평활에 실제 미반영 가능). 진단 도구라 영향 제한적이나 기록.

## 6. 출력 파일

| 파일 | 내용 | CALDISP2 | CALDISP3 |
|---|---|---|---|
| **DISTEN.OUT** | dispersion 텐서 I,J,LON,LAT,DXX,DXY,DYX,DYY | ✓ | ✓ |
| **UVTSC.OUT** | 조석 harmonic 진폭 AMCPT/AMSPT(elevation ×GI) + AMCUE/AMSUE/AMCVE/AMSVE(velocity) | ✓ | ✓ |
| **UVERV.OUT** | 잔차 HLPF(수심)·UELPF·VELPF·SALLPF(저층/표층 염분) | ✓ | ✓ |
| **SINVAL.OUT** | 연직 연산자 특이값 SVAL(K,L) | ✓ (SVD) | — |
| **DISDIA.OUT** | 이상치 텐서 진단(평활 대상 cell) | — | ✓ |

- `AMCP/AMSP/AMCUE/AMSUE/AMCVE/AMSVE` = 다른 곳에서 누적된 조석 cosine/sine 조화 진폭(압력·u·v). `GI`=1/g.

## 7. CALDISP2 vs CALDISP3 차이 요약

| 항목 | CALDISP2 | CALDISP3 |
|---|---|---|
| 역행렬 | SVD (SVDCMP/SVBKSB) | LU (LUDCMP/LUBKSB) |
| DELT | DT | NTSTBC·DT |
| 정규화 | /TPN | /TPNN = TPN/NTSTBC |
| 이상치 평활 | 없음 | DISDIA.OUT 4-이웃 평균 |
| 특이값 출력 | SINVAL.OUT | 없음 |

→ CALDISP3 가 transport sub-cycling(NTSTBC) 정합 + 강건성(LU + 이상치 평활) 측면에서 후속·실용판. CALDISP2 는 SVD 로 연직 연산자 conditioning 진단 가능(특이값).

## 8. 연결

- [[efdc_dispersion]] — HMD Smagorinsky 수평확산(main loop 물리). 본 노트는 transport effective dispersion 진단(post-process). `caldisp2/3.for`가 §line 293 후속으로 명시됐던 신설 대상.
- 이론 lineage: Taylor(1953/1954) shear-flow dispersion + Fischer et al.(1979) — 연직전단×연직혼합 → 종방향 분산. (소스 주석엔 명시 없음; 알고리즘 구조 기반 식별)
- concepts/currents/ — 잔차(조석평균) 순환·dispersion 적용 맥락
