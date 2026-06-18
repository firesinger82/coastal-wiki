---
title: "Delft3D-FLOW User Manual — 개경계/forcing 사양 (§4.5.6 GUI Data Group Boundaries + App A.2.10~15 파일 포맷 + §9.4 물리)"
model: Delft3D
canonical_source: self
citation_status: verified
verification_method: "models/Delft3D/raw/manuals/pdfs/Delft3D-FLOW_User_Manual.pdf (Deltares, v4.07.01, Rev 80907, 3 May 2026) 직접 pdftotext -layout 추출. §4.5.6 Boundaries (인쇄 p.43-60, PDF p.65-86), Appendix A.2.10 Open boundaries(.bnd, 인쇄 p.453-454)·A.2.11 Astronomic(.bca, p.455-456)·A.2.12 Corrections(.cor, p.457)·A.2.13 Harmonic(.bch, p.459)·A.2.14 QH(.bcq, p.460)·A.2.15 Time-series(.bct, p.461) (PDF p.476-483), §9.4.1.2 Open boundary conditions (인쇄 p.192-194, PDF p.214-216) 직접 인용. 인쇄 페이지 = PDF 물리 페이지 − 22 (예: PDF 65 = 인쇄 43, PDF 476 = 인쇄 454)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
verification_by: "Claude Opus 4.8 (1M context) — PDF 직접 추출 확인"
verification_date: 2026-06-18
related:
  - models/Delft3D/manual-notes/delft3d-flow-user-manual.md
  - models/Delft3D/manual-notes/delft3d-flow-physics-numerics.md
  - models/Delft3D/manual-notes/delft3d-tide-user-manual.md
  - concepts/tides/06-model-application.md
  - concepts/currents/06-model-application.md
---

# Delft3D-FLOW 개경계 / forcing 사양

> 출처: [`Delft3D-FLOW_User_Manual.pdf`](../raw/manuals/pdfs/Delft3D-FLOW_User_Manual.pdf) (Deltares, v4.07.01, Rev 80907, 3 May 2026).
> 페이지 인용은 **인쇄 페이지번호** 기준. PDF 물리 페이지 = 인쇄 + 22 (offset frontmatter 참조).
>
> 이 노트는 [[delft3d-flow-user-manual]](MDF/TOC)·[[delft3d-flow-physics-numerics]](지배방정식)와 **구분되는 경계 forcing 사양 전담 노트**. `concepts/tides/06`·`concepts/currents/06` 이 source-needed 로 남긴 `.bnd`/`.bca` 조석 경계 forcing 포맷 gap 충족.

## 1. 개경계 개념과 종류 (§4.5.6, 인쇄 p.43-44)

개경계(open boundary)는 모델 영역 밖 "외부 세계"의 영향을 표현하며, flow + transport 경계조건이 모두 필요하다 (p.43). Flow forcing 으로 사용 가능한 물리량: 수위(water level)·유속(current)·수위경사(Neumann)·유량(discharge, total/per-cell)·Riemann invariant (수위+유속 결합) (p.43).

| 경계 type | 의미 | 비고 |
|---|---|---|
| Water level | 수위 지정 | 대해역·하구 내륙측 표준. 대각선 grid line 가능한 유일 type (p.46, p.49) |
| Current (velocity) | 법선유속 지정 | 항만 전면 cross flow 등 (p.44) |
| Neumann | 연안방향 수위경사 ∂ζ/∂n | cross-shore 경계에서만, seaward 수위경계와 **결합 필수**(well-posed) (p.43-44) |
| Discharge per cell / Total discharge | grid cell별 / 단면 총유량 | river upstream flux 등 (p.44) |
| Riemann | 약반사(weakly reflective) 경계 | σ-model 에서만 테스트됨 (p.44 각주, p.49) |

원칙 (p.44-45): 모든 경계에 같은 type 적용 회피(직선수로 양단 velocity → 연속성 문제로 dry up/overflow). 한쪽 법선유속 + 반대쪽 수위가 안정. 대형 조석 basin 은 수위경계만으로 forcing 이 건전. 수위는 globally varying 량이라 작은 오차가 넓은 영역 유속에 큰 응답을 유발 → 경계를 관심영역에서 **가능한 멀리** 배치.

## 2. 경계 section 정의 + .bnd 파일 (§4.5.6 p.46-49 + App A.2.10 p.453-454)

경계는 begin(A)/end(B) 두 **support point** 로 정의되고, 중간점은 양단 forcing 의 **선형보간**으로 산출 (p.45). 진폭·위상으로 표현된 경계는 보간이 (계산된 시간의존 경계값이 아니라) 진폭·위상 자체에 적용됨 (p.45 Remark).

GUI Data Group Boundaries 에서 정의(name, begin/end grid index (M1,N1)-(M2,N2), type, 반사계수 Alfa, forcing type, 연직 profile)하고 확장자 `bnd` 파일로 저장 (p.46 Open/Save).

**.bnd 레코드 포맷** (App A.2.10, p.453-454) — ASCII, 텍스트는 fix-format / 수치는 free-format. 1 레코드 = 1 경계 section:

| 필드 | 내용 |
|---|---|
| Name | 경계 section 명 (20 char, position 1 시작) |
| Type of boundary (1 char) | `Z` 수위 · `C` 유속 · `N` Neumann · `Q` discharge per cell · `T` total discharge · `R` Riemann |
| Type of data (1 char) | `A` astronomic · `H` harmonic · `Q` QH table(수위경계 한정) · `T` time-series |
| Grid 인덱스 (4 int) | begin·end 점 (M1 N1 M2 N2) |
| Reflection coeff (1 real) | Alfa — Neumann·Riemann 에는 없음 |
| Vertical profile (3 strings) | 3D + velocity type(C,Q,T,R)만: Uniform / Logarithmic / 3D profile |
| 두 label (각 12 char) | data type=A 일 때만, `.bca` 진폭·위상 블록 참조 (두 번째 label 은 첫 label 시작 +13 이상 위치) |

제약 (p.454): max 레코드 길이 132; section 명은 position 1; astronomic·harmonic 경계는 QH 보다 먼저, QH 는 time-series 보다 먼저; astronomic·harmonic **혼용 불가**. section 수 ≤ 300 (p.48). Alfa 범위 0~10,000 default 0 (p.48). 반사계수는 Neumann·Riemann 에 적용 안 됨 (p.49).

**.bnd 예시** (p.454, 원문 그대로):
```
Paradise Bay 1   Q A   1   1    1   5 0.0 Uniform      Paradise_1A   Paradisee_lB
Paradise Bay 2   C A  16   3   16   6 0.0 Logarithmic  Paradise_2A   Paradisee_2B
Sea Entrance     Z T   4   8   14   8 0.0
```

## 3. Astronomic tide forcing + .bca 파일 (§4.5.6.1 p.50-53 + App A.2.11 p.455-456)

조석 조화상수(amplitude/phase)로 forcing. 주로 Delft3D-TIDE 또는 Delft3D-TRIANA 같은 조화분석 프로그램에서 산출 (p.50, p.455). 조석 일반식 (식 4.5, p.51):

$$H(t) = A_0 + \sum_{i=1}^{k} A_i F_i \cos\left(\omega_i t + (V_0+u)_i - G_i\right)$$

여기서 $A_0$=평균수위, $A_i$=국지 조석진폭, $F_i$=nodal amplitude factor, $\omega_i$=각속도, $(V_0+u)_i$=천문인수(astronomical argument), $G_i$=개선 kappa(국지 위상지연). 사용자는 **진폭·위상·주파수(분조명)** 만 제공; $F_i$, $(V_0+u)_i$ 는 모델이 계산. **nodal factor 와 천문인수는 기본 6시간마다 재계산** (변경은 §B.21, p.51).

GUI: 각 경계 끝점(A/B)에 **Component set**(분조 Name·Amplitude·Phase 묶음) 할당 (p.51). 주의 (p.52 Remarks): 평균값 A0 는 위상 없음; Total discharge type 은 A·B 에 같은 set 하나만; 중간점 진폭·위상은 양단 선형보간(A 1° / B 359° → 중간 180°, 회피하려면 A 에 361° 지정).

**.bca 레코드 포맷** (App A.2.11, p.455-456) — ASCII, FLOW-GUI 또는 Delft3D-TRIANA 오프라인 생성:

| Record | 내용 |
|---|---|
| 1 | end point A label (12 char, no blanks) |
| 2 ~ 2+NCOM−1 | 각 분조: name(8 char) + amplitude + phase (2 reals) |
| 2+NCOM | end point B label (12 char) |
| 2+NCOM+1 ~ 2+2·NCOM | 각 분조 name·amplitude·phase |

(NCOM = 분조 수; 위 블록을 경계 section 마다 반복.) 제약 (p.456): A·B label 은 `.bnd` 에서 정의; 분조명 전부 **대문자**; label·분조명 position 1 시작; section 간 분조 수·종류 다를 수 있으나 **한 section 의 양단은 동일 분조집합**.

**.bca 예시** (p.456, 원문 발췌):
```
East_bound_A      {section name, end point A}
A0 0.02 0.0       {mean value}
M2 1.87 314.3     {component name, amplitude and phase}
S2 0.32 276.4
O1 0.21 14.3
East_bound_B      {section name, end point B}
A0 0.03 0.0
M2 1.89 264.7
...
```

primary·compound 분조 목록은 Appendix C (p.51).

### 3.1 조석 보정 .cor (App A.2.12 p.457-458)

calibration 단계의 진폭(곱셈)·위상(덧셈) 보정. 확장자 `.cor` (p.52, p.457). label·분조명·보정계수(2 reals); A0 는 보정 불가 (p.52 Remark, p.458). 보정대상 section/분조의 부분집합에만 적용 가능 (p.52). 예시 `M2 0.90 10.0` = 진폭 ×0.90, 위상 +10.0° (p.458).

## 4. Harmonic forcing + .bch 파일 (§4.5.6.1 p.54-55 + App A.2.13 p.459)

사용자 정의 주파수·진폭·위상으로 신호 합성 (식 4.6, p.55):

$$F(t) = \sum_{i=1}^{N} A_i \cos(\omega_i t - \varphi)$$

진폭 단위는 forcing 량에 따라: 수위 [m] · Neumann [-] · 유속 [m/s] · flux [m³/s] · Riemann [m/s] (p.55). 입력: 주파수 [degrees/hour], 양단 A·B 진폭·위상 (p.55). 평균값은 zero frequency + zero phase 로 지정(항상 지정 필수); 모든 harmonic 경계는 **동일 주파수** 사용 (p.55 Remarks). max 주파수 234 (p.54, p.55).

**.bch 포맷** (App A.2.13, p.459) — free-format. Record 1=주파수들(0.0 포함), blank, 이어서 각 section begin 진폭 → end 진폭 → blank → begin 위상 → end 위상 (평균값 위상은 blank). NTOH = harmonic 경계 section 수. max 레코드 132 (p.459).

## 5. QH-relation + .bcq 파일 (§4.5.6.1 p.56 + App A.2.14 p.460)

수위경계 전용. 유출유량 ↔ 수위 관계 지정, 중간값 선형보간(보간법 변경 불가), 최대/최소 유량 밖에서는 수위 일정 (p.56). 유량은 **증가순** 지정(양수 소→대, 음수 대→소) (p.56 Restriction). relaxation parameter 는 Numerical parameters 에서 (p.56).

**.bcq 포맷** (App A.2.14, p.460) — header 는 fix-format 키워드(각 20 char), 시계열 데이터는 free. 헤더는 compulsory `records in table` 키워드+레코드 수로 종료. 각 데이터 레코드 = discharge [m³/s] + water level [m]. positive discharge = M/N 양의 방향 흐름; QH 는 **outflow 경계로만** (p.460).

## 6. Time-series + .bct 파일 (§4.5.6.1 p.57-58 + App A.2.15 p.461)

수위/Neumann/유속/유량/Riemann 값을 time breakpoint 별로 A·B 양단 지정, 중간 선형보간 (p.57). 제약 (p.58): breakpoint 는 시작시각으로부터 time-step 의 정수배; 첫 breakpoint ≤ 시뮬 시작, 마지막 ≥ 시뮬 종료; 오름차순; time-series forcing 은 astronomic·harmonic·QH **다음에** 위치. Total discharge type 은 section 전체에 유량 1개만 (p.57 Remark).

**.bct 포맷** (App A.2.15, p.461) — header(fix-format 키워드) + data(free) 두 블록 쌍, 경계 segment 마다. FLOW-GUI · **Delft3D-NESTHD** · 수동 오프라인 생성. (NESTHD 는 대형모델 nesting 으로 layer별 3D profile `.bct` 생성, §9.4 p.193 Remark.)

## 7. Transport 경계조건 (§4.5.6.2 p.59-60)

Processes 에서 켠 모든 양(염분·수온·constituent)의 경계조건은 **time-series 로만** 지정 (p.43, p.59). inflow 농도를 지정, outflow 는 free (§9.4 p.193).

- **Thatcher-Harleman time lag** (p.59): 유출→유입 전환 시 농도가 경계 지정값으로 복귀하는 return time (Thatcher & Harleman, 1972). 3D 는 표층·저층 별도 지정(층간 선형보간). 강한 순환 → 짧은 return time.
- **연직 profile** (p.60): Uniform / Linear(표·저층 보간) / Step(profile jump 깊이에서 불연속) / Per layer(nesting). 3D 에서 constituent 는 연직 profile 지정 필수. Step 의 jump 깊이는 초기수위로 layer 번호 환산 후 고정 — hot start 시 mismatch 로 spurious oscillation 가능 (p.60 Remark).

## 8. 물리·수치 배경 (§9.4.1.2, 인쇄 p.192-194)

개경계는 가상 "water-water" 경계; 법선흐름 가정(tangential 성분 0) (p.192). 정확히 입사파를 지정 못하면 유출파가 반사되어 교란 전파 (p.192).

**Riemann invariant** (식 9.70, p.192): $R = U \pm 2\sqrt{gH}$. 선형화(식 9.71): 지정값 $f(t) = U + \zeta\sqrt{g/d}$, $2\sqrt{gd}$ 는 수심장에서 계산해 더함. 1D 약반사적이나 2D 에서는 법선입사·Coriolis/마찰 무시 시에만 약반사 (p.192).

계산부 경계조건 분류 (p.192): 수위 $\zeta = F_\zeta(t)+\delta_{atm}$ · 유속 $U=F_U(t)$ · 유량 $Q=F_Q(t)$ · Neumann $\partial\zeta/\partial n = f(t)$ · Riemann $U \pm \zeta\sqrt{g/d} = F_R(t)$.

**반사계수 α (Alfa)** — Stelling(1984)이 Riemann invariant 의 시간미분을 수위·유속 경계에 더해 모델 고유진동수 교란에 덜 반사적으로 만듦(cold start spin-up 단축) (p.193):

$$\text{수위: } \zeta + \alpha\frac{\partial}{\partial t}\{U \pm 2\sqrt{gH}\} = F_\zeta(t) \quad (9.74)$$
$$\text{유속: } U + \alpha\frac{\partial}{\partial t}\{U \pm 2\sqrt{gH}\} = F_U(t) \quad (9.75)$$

권장값 (식 9.76-77, p.193): 수위경계 $\alpha = T_d\sqrt{H/g}$ [s²], 유속경계 $\alpha = T_d$ [s], $T_d$=자유표면파가 좌→우 경계 통과 시간. **대해역·조석모델에서는 $T_d$ 가 조석주기와 동급이므로 α=0** 으로 둬야 함(아니면 분조 진폭이 감쇠) (p.193). GUI §4.5.6 의 조석 계산 권장 Alfa 값 50 또는 100 은 단파교란 댐핑용이며 (p.44), Neumann·Riemann 에는 적용 안 됨.

기타 키워드 (p.193): `PavBnd`(경계 평균기압, $\delta_{atm}=(p_{avg}-p_{atm})/\rho g$, 식 9.72, Additional parameters); `BarocP = #NO#`(개경계 baroclinic 압력항 차단, default #YES#).

## 9. concepts gap 충족 (cross-ref)

| source-needed 였던 곳 | 본 노트가 충족한 사양 |
|---|---|
| [`concepts/tides/06`](../../../concepts/tides/06-model-application.md) §5.2 — `.bnd`/`.bca` 정확 포맷 | §2 (.bnd type/data 코드), §3 (.bca 분조 레코드+예시) |
| [`concepts/currents/06`](../../../concepts/currents/06-model-application.md) §1 — `.bca`/`.bnd` 조류 분조 카드 | §2-3; 유속경계는 type `C` + 3D `Logarithmic`/3D-profile |

> D3D-4 FLOW 의 조류 forcing 도 동일 `.bnd`/`.bca` 메커니즘 사용 — type `C`(velocity) 경계에 분조 set 할당, 3D 는 연직 profile(Uniform/Logarithmic/3D profile) 지정 (§2, §8). Delft3D-TIDE 산출 분조 → `.bca` 의 흐름은 [[delft3d-tide-user-manual]] 참조(TIDE 는 분석/예측 도구, 경계 적용은 본 노트).

## 10. 관련 자료

- [[delft3d-flow-user-manual]] — MDF 12 family 중 §4.5.6 Boundaries 위치(인쇄 p.43)
- [[delft3d-flow-physics-numerics]] — §9.4 전체 지배방정식·표층/저층 경계조건
- [[delft3d-tide-user-manual]] — 조화분석·예측(.bca 분조 산출 도구)
- 외부: Verboom & Slob (1984), Verboom & Segal (1986), Stelling (1984), Thatcher & Harleman (1972), Engquist & Majda (1977,1979) — manual 인용 (p.44, p.193, p.59)
