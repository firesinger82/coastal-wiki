---
title: "COAWST 파랑-해류 상호작용(WCI) 정량 검증 — Benetazzo et al. 2013 (Gulf of Venice)"
topic: roms-web-refs
canonical_source: self
citation_status: verified
has_source_needed: false
verification_method: "Benetazzo A., Carniel S., Sclavo M., Bergamasco A. (2013) 'Wave–current interaction: Effect on the wave field in a semi-enclosed basin', Ocean Modelling 70:152-165, doi:10.1016/j.ocemod.2012.12.009 — **출판본 PDF 전문(14쪽) 직접 read (2026-07-19, pdftotext -layout)**. 격자·수치설정 §2.4(p.155-156)·결합 유속평균 Eq(6) Kirby-Chen(p.156)·vortex-force Eq(7)-(11)(p.157)·검증통계 Table 1(p.159)·WCI 정량효과 §4(p.160-162)·결론 §5(p.163-164) 페이지·식·표 단위 인용. 인용 수치는 표·본문 병기 대조(부호는 본문 서술로 확정 — pdftotext 음부호 소실 대비)."
note_author: "Claude Fable 5"
note_date: 2026-07-19
verification_by: "Claude Fable 5 — 출판본 PDF 직독"
verification_date: 2026-07-19
related:
  - models/ROMS/web-refs/roms-coawst-adriatic-applications.md
  - models/ROMS/source-analysis/roms_wec.md
  - models/SWAN/web-refs/swan-official-resources.md
  - concepts/waves/06-model-application.md
---

# COAWST 파랑-해류 상호작용(WCI) 정량 검증 — Gulf of Venice

> [`roms-coawst-adriatic-applications.md`](roms-coawst-adriatic-applications.md)(Carniel et al. 2013 리뷰)가 정성적으로만 언급한 **"결합이 더 나은 예보를 준다"의 정량 근거 원전**. 리뷰 §3 이 인용한 test case 논문. ROMS↔SWAN 결합 메커닉은 [`source-analysis/roms_wec.md`](../source-analysis/roms_wec.md)(vortex-force) 가 canonical, 본 노트는 적용·검증 맥락.

## 1. 출처

| 항목 | 값 |
|---|---|
| 제목 | "Wave–current interaction: Effect on the wave field in a semi-enclosed basin" |
| 저자 | A. Benetazzo, S. Carniel, M. Sclavo, A. Bergamasco (ISMAR-CNR, Venice) |
| 게재 | *Ocean Modelling* **70** (2013) 152–165 |
| DOI | `10.1016/j.ocemod.2012.12.009` (Available online 2013-01-07) |

★**리뷰(Carniel 2013)의 운영 NA-COAWST 와 구분할 것**: 본 논문은 **2010-09-01 ~ 2011-08-31 12개월 hindcast** 실험(§2.4 p.155). 운영 NA-COAWST(2011-11-25 개시)는 이 test case 를 근거로 뒤에 구축된 별개 구성.

## 2. 실험 구성 (§2.4, p.155-156)

| 항목 | 값 |
|---|---|
| Parent grid | **2.0 km** 등간격(양방향)·**연직 20 σ-level**, 전 Adriatic, 남측 개방경계 Otranto |
| Child grid | **0.5 km**, 북 Adriatic(Gulf of Venice) — ★**offline(one-way) nesting**(Mason et al. 2010). 격자중첩은 단방향, "two-way"는 ROMS↔SWAN 결합을 지칭 |
| 0.5 km 선정근거 | 북 Adriatic 내부 Rossby 변형반경 **여름 10 km ~ 겨울 1 km** → 2 km 는 eddy-resolving 아님, downscaling 필요 |
| ROMS | v3.4. **GLS 난류**(Kantha & Carniel 2003; Umlauf & Burchard 2003; Warner et al. 2005)·**COARE 3.0** bulk flux·**MPDATA** 이류 |
| ROMS 시간간격 | baroclinic **60 s**, baroclinic 당 barotropic **20** 스텝. 출력 0.5 h(coarse)/3 h(fine) |
| SWAN | v40.81. 방향 **24** 등간격 · 주파수 **32** 기하분포 `f(n+1)=1.1·f(n)`, `f1=0.05 Hz`. 3세대 모드, DIA 4파상호작용, Komen et al.(1984) 백파(기본계수), Battjes-Janssen 쇄파, Madsen 저면마찰, **BSBT** 이류, 비정상 **600 s** |
| 대기 | **COSMO-I7** — 비정수압, 수평 **7 km**, **연직 35 층**, 1 h 출력, 경계=ECMWF IFS, 도메인 2–22°E/32–52°N. 일 00 UTC 런의 **첫 24 h 예보**만 사용, ROMS/SWAN 격자로 공간 선형내삽 |
| 조석 | 개방경계 **5 분조 (M2·S2·N2·O1·K1)**, OSU 모델 |
| 하천 | Po 일평균 실측 + 그 외 **총 26 하천** 월평균 climatology(Raicich 1994) |
| 해양 경계 | Mediterranean Forecasting System(INGV, MyOcean). Child 경계 = Chapman(자유수면) + Flather(2D 운동량), 0.5 h 간격 |
| 결합 | **MCT 동기 결합, 0.5 h 간격**. 실험군 = **2WC**(two-way coupled) vs **UNC**(uncoupled), 겨울 2011-01~03 |

### 2.1 ★결합 시 유속 평균 — Kirby & Chen (1989) (Eq.6, p.156)

ROMS 3D 유속을 SWAN 에 넘길 때 **어느 깊이 유속을 쓸 것인가**의 선택지(표층 1st level / depth-integrated / 위상속도 수정 깊이) 중, 본 구현은 Stewart & Joy(1974)를 유한수심 확장한 **Kirby & Chen (1989)** 가중평균 채택:

```
U_k = [2k / sinh(2kd)] ∫_{-d}^{0} U(z)·cosh[2k(d+z)] dz          (Eq. 6, p.156)
```

- 물리 의미: **단주기파는 표층 유속만, 장주기파는 더 깊은 유속까지 느낀다** — 가중을 파수 `k` 함수로.
- COAWST 구현은 이 가중평균을 **spectral mean wavenumber** 기준으로 계산해 SWAN Eq.(2) 에 투입.
- 수치모델 적용 논의는 Olabarrieta et al. (2012).

### 2.2 파랑→해류 방향 (vortex-force, p.157)

wave→ocean 전달량: 파랑에너지 소산 `ebr`·`Hs`·쇄파율 `Q`·`Tp`·`Tm,bot`·`θm`·평균파수 `k`·저면궤도유속 `Ubot`. 해류측은 **Vortex-Force(VF) formalism**(McWilliams 2004·Uchiyama 2010·Kumar 2012) — 수평 VF Eq.(7), 압력보정 `Pcor ∝ Hs²` Eq.(9), 연직 VF Eq.(10), Stokes 유속 Eq.(11). 쇄파 시 표면조도 = `0.5·Hs`(Stacey 1999), BBL = Warner et al. (2008) 파-류 결합 저면경계층.
→ 코드 레벨 메커닉은 [`source-analysis/roms_wec.md`](../source-analysis/roms_wec.md).

## 3. ★검증 통계 (Table 1, p.159) — Acqua Alta tower + 위성 고도계

관측: CNR-ISMAR **Acqua Alta** 타워(45°18′83″N, 12°30′53″E, 수심 약 16 m, 베네치아 석호 외해 8 마일). Nortek **AWAC** (2 Hz, 30분마다 20분 버스트; 정확도 파고 1 cm·방향 2°·유속 측정값의 1%). 풍속 15 m 고도 관측 → 10 m 표준고도 보정. 위성 = Jason-1·Jason-2·Envisat 고도계.

| 변수 | 회귀기울기 p | Bias | RMSD | CC | Rstd |
|---|---:|---:|---:|---:|---:|
| **U10** (Acqua Alta) | 0.90 | −0.18 m/s | 2.12 m/s | 0.77 | 1.03 |
| **U10** (위성) | 0.98 | 0.07 m/s | 1.82 m/s | 0.72 | 1.11 |
| **Hs** (Acqua Alta) | 0.89 | 0.01 m | **0.20 m** | **0.90** | 0.92 |
| **Hs** (위성) | 0.94 | −0.02 m | 0.26 m | 0.81 | 1.12 |
| **Tm02** (Acqua Alta) | 0.92 | −0.14 s | 0.52 s | 0.80 | 1.06 |

- 응답오차 정의 **E = 100(1−p)** (p = 최적적합 직선 기울기). 본문 판정: 풍속·Hs·Tm02 **모두 E ≈ 10% 수준**, 결론부(p.164)는 "풍속 10% 미만·Hs 20% 미만" 표현.
- **풍속 의존 편차**(p.158): 저풍속(<5 m/s) 과대(bias +0.16 m/s) → 고풍속(>10 m/s) 과소(bias −1.43 m/s). ★북 Adriatic Bora 시 고풍속 과소는 **대기모델이 산악을 평활화**하는 데서 오는 전형적 현상(Signell 2005·Cavaleri & Bertotti 2003).
- **파고 의존 편차**(p.158): 소파(Hs<0.7 m) 과대(+0.03 m) → `Hs≈1.2 m`·`Tm02≈2 s` 부터 과소 시작, 고파(Hs>2 m) 에서 bias **−0.42 m**(AA)·−0.16 m(위성).
- ★**풍속오차 증폭 논리**(p.158): Pierson-Moskowitz 기준 `Hs ∝ U²` → **풍속 10% 과소 = 파고 최대 20% 과소**. 파랑 검증오차가 대기 검증오차보다 큰 구조적 이유.
- **downscaling 단독 효과는 미미**(p.159-160): 0.5 km vs 2.0 km 를 Acqua Alta 에서 대조 — Hs 는 **E=1%·RMSD 0.04 m·CC 1.00·bias −0.01 m**, Tm02 는 E=2%·RMSD 0.17 s·CC 1.0. 즉 **격자만 조밀하게 해도 정점 파랑량은 거의 안 변함** — 0.5 km 의 필요성은 파랑 통계가 아니라 내부 순환(eddy) 해상에 있음(§2.4 근거와 정합).

## 4. ★WCI 정량 효과 — 2WC vs UNC (§4, p.160-162)

대상: 겨울 2011-01~03, `Hs_max > 2.5 m`(풍속 10–15 m/s 이상) 폭풍. 대표 2사례 = **Bora(분지 횡단풍)·Sirocco(분지 종단풍)**.

| 사례 | 기간 | 풍속 | 조석 | 유속 | **ΔHs (2WC−UNC)** | **Δθ (파향)** |
|---|---|---|---|---|---|---|
| **Bora** | 2011-01-27~29 | 최대 14 m/s (AA) | 소조, 조차 ~0.6 m | 국지 평균 **0.45 m/s** | 폭풍 평균 **0.2 m** | 최대 **20°** |
| **Sirocco** | 2011-02-15~17 | 최대 12 m/s | 대조, 조차 1.4 m | **0.1 m/s** 제한 | **0.1 m** 제한 | **5°** 제한 |

- **겨울 전체(1~3월) 격자별 최대차**(p.162, Fig.21): 결합계는 북 Adriatic 중앙에서 **Hs 최대 약 0.6 m 감소**. 반대로 **Trieste·Kvarner 만, 이탈리아 Conero 곶** 주변은 증가.
- **방향 의존이 지배**(abstract·§4): 파가 **따라가는 흐름(following current)** 을 만나면 에너지 **감소**, **거스르는 흐름(opposing current)** 에서는 **증가(shoaling)** — Eq.(1)·Fig.1 의 해석해와 정합. 따라서 **북 Adriatic WCI 는 바람 방향에 강하게 의존**(Bora 뚜렷 / Sirocco 미미)하며, 그 실체적 원인은 **바람이 만드는 유속 크기 차이**(0.45 vs 0.1 m/s).
- ★**결합이 유속 재현을 개선한 증거**(p.160, Bora): 관측 대비 유속 — UNC 는 RMSD 0.04 m/s·**CC 0.70**, 2WC 는 RMSD 동일·**CC 0.75 로 상승**. (파고 쪽은 UNC 과대예측이 2WC 에서 최대 0.2 m 축소되어 "약간 개선(slightly improved)" — 단 폭풍 피크에서는 2WC 가 Hs 를 과소예측, 이는 유속 과대예측과 상쇄.)
- 파랑→해류 되먹임: 2WC 에서 파랑력·난류운동에너지 주입으로 **해류가 강화**됨(Carniel et al. 2009).

### 4.1 선행연구 비교값 (Intro, p.153)

| 연구 | 시스템 | WCI 로 인한 파랑 변화 |
|---|---|---|
| Warner et al. (2010) | 동일 3D COAWST, 허리케인 | 역류 조우 시 **Hs 최대 20% 증가** |
| Hersbach & Bidlot (2008) | ECMWF 운영 | 해류 존재 시 **Hs 최대 0.5 m 변화** |
| Osuna & Monbaliu (2004) | WAM + 2D 수리모델, 남 북해 | 유속 1 m/s 에서 Hs 약 0.2 m·주기 약 1 s 차 |
| Bolaños et al. (2011) | POLCOMS + WAM, 북서지중해 | 저유속 → 결합/비결합 차 작음 |

→ 본 연구 0.6 m(계절 최대)·0.2 m(폭풍 평균)는 이 선행값들과 같은 자릿수.

## 5. 본 위키 접점

| 본 위키 자료 | 접점 |
|---|---|
| [`roms-coawst-adriatic-applications.md`](roms-coawst-adriatic-applications.md) | 이 논문이 그 리뷰 §3 NA-COAWST 의 근거 test case — 정량 gap 해소 |
| [`source-analysis/roms_wec.md`](../source-analysis/roms_wec.md) | vortex-force Eq.(7)-(11)·Stokes drift 의 적용 사례 |
| [[../../SWAN/web-refs/swan-official-resources]] | SWAN 40.81 설정(24방향·32주파수·BSBT·Komen 백파) |
| [`concepts/waves/06-model-application.md`](../../../concepts/waves/06-model-application.md) | 파랑-흐름 결합(조류 영향) 모델 선택 근거 |
| [`concepts/currents/06-model-application.md`](../../../concepts/currents/06-model-application.md) | 반폐쇄해 바람구동 순환 + 파랑 되먹임 |

→ **한국 적용 함의**: 반폐쇄해에서 **파-류 결합의 실익은 유속 크기가 좌우**한다는 정량 기준선 — 유속 ~0.45 m/s 급에서 Hs 0.2~0.6 m 차, ~0.1 m/s 급에서는 0.1 m 이하로 무시가능. 조류가 강한 한국 서해(대조 시 1 m/s 초과 구간 존재)에서는 결합 효익이 본 사례보다 클 가능성이 있으나 **직접 실증 아님**(본 논문 도메인=Adriatic).
