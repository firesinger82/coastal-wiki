---
title: "COULWAVE 고차 분산 이론 — Celeris NLSW_or_Bous==2 모드의 원논문 계보"
model: Celeris
citation_status: verified
source: "원논문 서지(권·호·페이지·DOI)는 WebSearch/WebFetch 직접 확인(2026-06-15, royalsocietypublishing/ascelibrary/sciencedirect/scholar landing-page) + repo docs/architecture/REFERENCE_PAPERS.md + 소스 txCW_zalpha 텍스처(z_α reference velocity). 방정식 유도 본문은 미정독(서지·요지 수준)."
note_date: 2026-06-15
---

# COULWAVE 고차 분산 이론 — Celeris `NLSW_or_Bous==2` 모드의 계보

> 소스 분석 [`../source-analysis/celeris-coulwave.md`](../source-analysis/celeris-coulwave.md)가 "WGSL로 환원 불가 → 원논문" 으로 미룬 항목(분산 정확도 차수·multi-layer 유도·z_α reference velocity 물리·deep-water 한계)을 채우는 노트.
>
> ⚠️ **주의**: Celeris 자체 문서(`docs/architecture/REFERENCE_PAPERS.md`)는 Celeris 논문(Tavakkol-Lynett 2017/2020, Lynett 2026)만 인용하며 **COULWAVE 원논문은 직접 인용하지 않는다**. 코드는 "higher-order/COULWAVE-style formulation"이라고만 규정. 아래는 그 COULWAVE 이론을 거슬러 올라간 **상류 계보**이며, Celeris 코드가 *이 논문들의 식을 그대로 구현했다는 1:1 검증은 아니다*(코드↔식 매핑은 §4 수준). 정확한 구현 동등성은 방정식 정독 필요.

---

## 1. COULWAVE 모델 패키지

- **COULWAVE** = **Co**rnell **U**niversity **L**ong and Intermediate **Wave** Modeling Package.
- **개발**: Patrick J. Lynett (Cornell 대학원생, 지도교수 Philip L.-F. Liu) ~2000 최초 작성 → 2002 highly-dispersive **multi-layer Boussinesq** 이론 편입(이때부터 wind wave 적용). 지진·해저사태 생성파 시뮬레이션이 출발점.
- **메뉴얼**: Lynett, P., Liu, P.L.-F. *Modeling Wave Generation, Evolution, and Interaction with Depth-Integrated, Dispersive Wave Equations — COULWAVE Code Manual, v.2.0.* Cornell University.
- **지배방정식**: depth-integrated, **fully nonlinear**(파고/수심비 = O(1)) **dispersive** Boussinesq, 가변 지형.
- Lynett은 이후 USC로 이동 — Celeris(Tavakkol·Lynett)와 같은 연구계보. Celeris의 COULWAVE 모드는 이 이론의 GPU 위상해상 구현.

---

## 2. 분산 정확도 계보 (왜 "higher-order"인가)

Celeris 3 모드의 분산 정확도는 이 계보의 단계에 대응한다.

### 2.1 Nwogu 1993 — reference velocity z_α (★코드 `txCW_zalpha`의 근거)

- **Nwogu, O. (1993)** "Alternative form of Boussinesq equations for nearshore wave propagation." *Journal of Waterway, Port, Coastal, and Ocean Engineering* **119**(6):618-638. DOI: [10.1061/(ASCE)0733-950X(1993)119:6(618)](https://doi.org/10.1061/(ASCE)0733-950X(1993)119:6(618)).
- 핵심: 종속변수를 depth-averaged velocity가 아니라 **임의 기준고도 z=z_α의 수평속도**로 택해 선형 분산관계를 대폭 개선. 표준 Boussinesq를 더 넓은 수심범위(intermediate water)로 확장.
- 파라미터 α = (z_α/h)²/2 + z_α/h. 최적 z_α ≈ −0.531·h 부근에서 Padé[2,2] 분산에 근접.
- **코드 연결**: Celeris COULWAVE는 셀별로 z_α를 계산해 `txCW_zalpha` 텍스처에 저장(`shaders/Pass3A_COULWAVE.wgsl:83`, store; `Pass3B_COULWAVE.wgsl:50`·`Pass3_COULWAVE.wgsl:230` load). 소스 분석 노트의 "za reference-velocity 고도"가 바로 이 z_α.

### 2.2 Wei·Kirby·Grilli·Subramanya 1995 — fully nonlinear 확장 Boussinesq (단층, kh≈3)

- **Wei, G., Kirby, J.T., Grilli, S.T., Subramanya, R. (1995)** "A fully nonlinear Boussinesq model for surface waves. Part 1. Highly nonlinear unsteady waves." *Journal of Fluid Mechanics* **294**:71-92. DOI: [10.1017/S0022112095002813](https://doi.org/10.1017/S0022112095002813).
- Nwogu의 z_α 속도변수를 **완전비선형**으로 확장(약비선형 가정 제거 → 쇄파 직전 강한 상호작용 모사). 단층(single-layer) 확장 Boussinesq의 표준형.
- 분산 유효범위 대략 **kh ≲ 3** (intermediate water). → Celeris의 `NLSW_or_Bous==1`(Pass3_Bous) 모드가 이 단층급에 해당.
- FUNWAVE-TVD의 분산 이론과 같은 계보(Wei-Kirby 1995 / Chen 2006) — [`../../FUNWAVE/source-analysis/funwave-dispersion-solver.md`](../../FUNWAVE/source-analysis/funwave-dispersion-solver.md).

### 2.3 Lynett·Wu·Liu 2002 — COULWAVE runup 기반

- **Lynett, P.J., Wu, T.-R., Liu, P.L.-F. (2002)** "Modeling wave runup with depth-integrated equations." *Coastal Engineering* **46**(2):89-107. DOI: [10.1016/S0378-3839(02)00043-1](https://doi.org/10.1016/S0378-3839(02)00043-1).
- COULWAVE의 moving-shoreline runup 정식화 — wet/dry·처오름. Celeris의 moving shoreline 운용(README 정체카드)과 같은 문제의식.

### 2.4 Lynett·Liu 2004 — two-layer / multi-layer (★kh≈6, deep water 확장)

- **Lynett, P., Liu, P.L.-F. (2004)** "A two-layer approach to wave modelling." *Proceedings of the Royal Society A* **460**(2049):2637-2669. DOI: [10.1098/rspa.2004.1305](https://doi.org/10.1098/rspa.2004.1305).
- 핵심: 원시 운동방정식을 **두 임의 층으로 piecewise 적분**, 각 층 독립 속도 프로파일. 최적화 자유파라미터 3개. **선형 분산 + 2차 비선형 모두 kh ≈ 6까지 양호** — 단층(kh≈3)보다 약 2배 깊은 물까지 확장.
- 이것이 COULWAVE에 2002년 편입된 "highly-dispersive multi-layer Boussinesq"의 정식 출판. → Celeris `NLSW_or_Bous==2`(COULWAVE 모드)가 노리는 **deep-water 정확도 향상**의 이론 근거.
- **차수↔비용 트레이드오프 답**: 단층 Pass3_Bous는 kh≲3, COULWAVE 다층은 kh≈6까지 — 그래서 매 step Pass3A/3B 보조패스 + 3D 텍스처 packing + z_α 명시계산의 추가 비용을 진다(소스 노트 §4 트레이드오프의 물리적 근거).

---

## 3. 코드 ↔ 이론 매핑 (소스 분석 노트 미결 해소)

| 소스 분석 노트가 미룬 것 | 이 노트의 답 |
|---|---|
| z_α(=za) reference velocity의 물리적 의미 | Nwogu 1993: 속도변수를 평가하는 기준고도. 분산관계 최적화 지렛대 (§2.1) |
| 분산 정확도 차수 | 단층(Bous, Wei-Kirby 1995) kh≲3 → 다층(COULWAVE, Lynett-Liu 2004) kh≈6 (§2.2·2.4) |
| multi-layer Boussinesq 유도 | Lynett-Liu 2004: 2층 piecewise 적분, 독립 속도 프로파일, 3 자유파라미터 (§2.4) |
| deep-water 적용한계 | kh≈6 근방까지 선형·2차비선형 양호(그 이상은 이론적으로 벗어남) (§2.4) |
| S·T·E·vorticity 고차 그룹의 출처 | 다층 적분에서 나오는 고차 분산항. **정확한 항별 대응은 방정식 정독 필요(미완)** |

⚠️ S/T/E grouping 항의 정확한 방정식 대응(`Pass3B_COULWAVE`가 만드는 발산·구배 항이 Lynett-Liu 2004 어느 식인지)은 **방정식 정독이 필요한 미결 항목**. 본 노트는 계보·차수까지만 verified.

---

## 4. 쇄파 (참고)

COULWAVE/Celeris 공유 eddy-viscosity 쇄파는 Kennedy 계열:
- **Kennedy, A.B., Chen, Q., Kirby, J.T., Dalrymple, R.A. (2000)** "Boussinesq modeling of wave transformation, breaking, and runup. I: 1D." *Journal of Waterway, Port, Coastal, and Ocean Engineering* **126**(1):39-47.
- 코드 연결: [`../source-analysis/celeris-breaking-boundary.md`](../source-analysis/celeris-breaking-boundary.md) §1 (Pass_Breaking의 ∂η/∂t 기준 Kennedy-style).

---

## 5. 본 위키 cross-ref

- 코드 구현: [`../source-analysis/celeris-coulwave.md`](../source-analysis/celeris-coulwave.md) (Pass3A/3B·COULWAVE PCR)
- Celeris 공식 논문: [`celeris-official-resources.md`](celeris-official-resources.md)
- 정체·분류: [`../README.md`](../README.md)
- 같은 분산 계보(Wei-Kirby): [`../../FUNWAVE/source-analysis/funwave-dispersion-solver.md`](../../FUNWAVE/source-analysis/funwave-dispersion-solver.md)
