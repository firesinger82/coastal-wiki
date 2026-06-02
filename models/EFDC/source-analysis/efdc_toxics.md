---
title: "EFDC+ Toxics/ChemFate 모듈 — 오염물 3-phase 분배 + sediment 결합 fate&transport (CALTOX/CALTOXB/KINETICS) verified"
topic: sediment-transport
canonical_source: external
external_source: "EFDC+ source_code/EFDCPlus_Stable/EFDC/ChemFate/ (caltox.f90 1390 + caltoxb.f90 490 + caltox_kinetics.f90 287 + partmix.f90 + setfpocb.f90) + SedTran-Original/ssedtox.f90 (driver). 저자 Paul M. Craig 외. Housatonic River fPOC = HydroQual 2003-03-17."
citation_status: verified
verification_method: "source 직접 read: caltox.f90 (partition 100-275 + 정규화 283-330 + settling/bed flux 346-412) + caltox_kinetics.f90 전체(287, ITOXKIN 6 process + ViscosityW) + caltoxb/partmix/setfpocb header + ssedtox 호출. TOXPFW/TOXF/ITOXKIN/ISTOC/ITXPARW 식·flag verbatim."
note_author: "Claude Opus 4.8 (1M context) raw source direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — partition/flux/kinetics 식 + flag verbatim"
verification_date: 2026-06-02
related:
  - models/EFDC/source-analysis/sediment/efdc_propwash.md
  - models/EFDC/source-analysis/sediment/efdc_sedzlj.md
  - models/EFDC/source-analysis/efdc_dispersion.md
---

# EFDC+ Toxics/ChemFate 모듈 — verified

> EFDC+ ChemFate/ (caltox 1390 + caltoxb 490 + kinetics 287 + partmix + setfpocb) 직접 read. **오염물(toxic contaminant) fate & transport** — 3-phase 평형분배 → sediment 결합 침강/침식 flux → bed 교환 + 화학 kinetics(decay/biodeg/volatil). **SedTran-Original·SEDZLJ 공용**, driver = `SSEDTOX`. 동기: **오염 sediment remediation** (Superfund), [[efdc_propwash]] fast-settling 연계.

## 0. 구조 + driver

| 파일 | 줄 | 역할 |
|---|---|---|
| `caltox.f90` (CALTOX) | 1390 | **water column** 분배 + settling/bed-exchange flux. SSEDTOX 호출, SedTran/SEDZLJ 공용 |
| `caltoxb.f90` (CALTOXB) | 490 | **sediment bed** 오염물 transport + sediment/water interface flux (2017-05 Original+SEDZLJ 통합) |
| `caltox_kinetics.f90` | 287 | **decay/kinetics** (bulk + biodeg + volatil). SSEDTOX서 `NKINETICS>0` 시 호출 |
| `partmix.f90` (PARTMIX) | — | bed **particle mixing**(bioturbation) top layer [PMXDEPTH] |
| `setfpocb.f90` (SETFPOCB) | — | bed fPOC 설정 (Housatonic River, HydroQual 2003) |

driver `SedTran-Original/ssedtox.f90` — `CALL CALTOX` / `CALTOXB` / `CALTOX_KINETICS(NKINETICS>0)`.

NTOX 종 오염물, 각각 NSP2(NT) sorbent phase. ISTRAN(5)>0 = toxics 활성.

## 1. 평형 분배 (CALTOX, 3-phase)

오염물은 **free dissolved + DOC-complexed + particulate-sorbed** 3상 평형. `TOXPFW(L,K,NS,NT)` = phase NS 의 분배비(interim), 합 `TOXPFTW = Σ_NS TOXPFW`.

### 1.1 ISTOC 분기 (분배 접근법)

- **`ISTOC(NT)==0` — Kd approach**: `TOXPFW = SED × TOXPARW` (TOXPARW = $K_d$ [L/mg = m³/g] 분배계수)
- **`ISTOC(NT)>1` — fPOC-based** (organic-carbon 정규화): `TOXPFW = SED × STFPOCW × TOXPARW` (STFPOCW = sediment 의 fraction POC, TOXPARW = $K_{oc}$)
- **`ISTOC==1`**: 3-phase (DOC + POC 별도), **`ISTOC==2`**: DOC complexation

### 1.2 ITXPARW 선형/비선형

- **`ITXPARW==0`** (linear, non-solids based): `TOXPFW = SED × ... × TOXPARW`
- **`ITXPARW==1`** (non-linear, solids-based, **Freundlich**형): `TOXPFW = SED^CONPARW × SED × ... × TOXPARW` (CONPARW = Freundlich 지수)

### 1.3 4 sorbent phase

| phase | 변수 | 식 (Kd 예) |
|---|---|---|
| **cohesive** (ISTRAN6) | SED(L,K,NS) | `TOXPFW = SED·TOXPARW` |
| **noncohesive** (ISTRAN7) | SND(L,K,NX), NS=NX+NSED2 | `TOXPFW = SND·TOXPARW` |
| **DOC** (complexed, ISTOC 1/2) | STDOCW, NFD index | `TOXPFW(NFD) = STDOCW·TOXPARWC(1)` |
| **POC** (particulate, ISTOC 1) | STPOCW, NFD+1 | `TOXPFW(NFD+1) = STPOCW·TOXPARWC(2)` |

### 1.4 분율 정규화 (dimensionless)

$$\text{sorbed fraction: } \text{TOXPFW} = \frac{\text{TOXPFW}}{1 + \text{TOXPFTW}}$$
$$\text{free dissolved: } \text{TOXFDFW} = \frac{1}{1 + \text{TOXPFTW}},\qquad \text{DOC-complexed: } \text{TOXCDFW} = \text{TOXPFW}(NFD)$$
> 모든 분율 합 = 1. **dissolved (free + DOC) 만 advection-diffusion·volatilization 가능**, particulate 는 sediment 와 함께 이동.

## 2. Settling / bed exchange flux (CALTOX 346-412)

`TOXF(L,1:KS,NT)` = settling + bed exchange flux (+상향/−하향, m/s), `TOXF(L,0,NT)` = depositional flux, `TOXFB(L,NT)` = erosional flux (final 1/s).

**오염물 flux = sediment flux × 분배** (sorbed toxic 가 sediment 따라 침강/침식):
$$\text{TOXF}(L,K,NT) \mathrel{+}= \text{SEDF}(L,K,NS) \times \text{STFPOCW} \times \text{TOXPARW} \quad \text{(fPOC, m/s)}$$
- `SEDF` = sediment settling flux (G/M²/S, water column 항상 음=하향). Kd 시 STFPOCW 생략, Freundlich 시 ×SED^CONPARW
- → toxic ↔ sediment transport(SEDZLJ/Original) **완전 결합**. [[efdc_sedzlj]] 의 erosion/deposition 이 toxic 재분배 구동.

## 3. Bed (CALTOXB) + bioturbation

- **CALTOXB**: bed layer 별 분배(`TOXPFB`/`TOXPFTB` 동일 Kd/fPOC 체계) + **pore water** dissolved + sediment/water interface diffusive flux. Original·SEDZLJ 공용 (2017-05).
- **PARTMIX(NT)**: top bed layer [`PMXDEPTH`] 의 **particle mixing(bioturbation)** — 생물교란으로 오염물 연직 재분배.
- **SETFPOCB**: bed 조성 기반 fPOC 함수 (Housatonic River 사례, HydroQual 2003-03-17 — % → fraction 변환).

## 4. 화학 kinetics (CALTOX_KINETICS, 287)

`ITOXKIN(1:6, NT)` process flag (2017-09 Craig biodeg+volatil 추가):

| # | process | flag | 구현 |
|---|---|---|---|
| 1 | **Bulk decay** | 0/1 | water `BLK_KW`, bed `BLK_KB`(depth≤`BLK_MXD`) |
| 2 | **Biodegradation** | 0/1 | **Q10 온도의존** |
| 3 | **Volatilization** | 0/1simple/2computed | **two-film** (CALVOLTERM) |
| 4 | Photolysis | (미구현) | RKTOXP/SKTOXP placeholder |
| 5 | Hydrolysis | (미구현) | — |
| 6 | Daughter products | (미구현) | — |

### 4.1 Decay 적용

- **Bulk decay**: `TOX = TOX·(1 - TOXTIME·CDECAYW)` (water), `TOXB = TOXB·(1 - TOXTIME·CDECAYB)` (bed)
- **Biodegradation Q10** (water): `COEFF = BIO_KW · BIO_Q10W^(0.1·(TEM - BIO_TW))` (CDECAYW 누적). bed: BIO_KB·Q10B^(0.1·(TEMB - BIO_TB)), depth≤BIO_MXD. bed 온도 simulated 시 TEMB, else 바닥층 water 온도.

### 4.2 Volatilization (two-film, KL_OPT>0)

상층(KC)만, `CALVOLTERM(...)` — 수면 two-film: 액상 $K_L$ + 기상 $K_G$, Henry's law `VOL.HE`, wind(WINDST), Schmidt 수(점성 `ViscosityW = 2.414e-5·10^(247.8/(TK-140))` Pa·s), 분자량 `TOXMW = 1/MW^0.667`. `TOX(KC) -= VOLTERM·TOXTIME`. **PFTWC(sorbed fraction)로 dissolved 만 휘발** (particulate 비휘발).
- 기체상수 `RCONST = 8.206e-5` atm·m³/mol·K
- toxic step `TOXSTEPW` 간격 (sediment substep)

## 5. Propwash 연계

`caltox.f90` 의 **"Propwash fast settling"** 분기 (`if NSED2 > NSED`): [[efdc_propwash]] 가 재부유시킨 **fast-settling sediment class** (Variables_Propwash `fraction_fast`/`fast_multiplier`)에 대한 별도 분배. propwash 가 오염 sediment 재부유 → toxic 재분배 → settling/transport 의 fate&transport 폐루프.

## 6. 핵심 finding

1. **toxic = sediment 의 passenger** — TOXF = SEDF×분배. SEDZLJ/Original 의 erosion/deposition 이 오염물 fate 직접 구동. propwash([[efdc_propwash]]) → 오염 재부유 → toxic flux.
2. **3-phase 평형분배** (free/DOC/particulate) + Kd vs fPOC(K_oc) + linear vs Freundlich(CONPARW) — hydrophobic organic(K_oc·fPOC) + metal(Kd) 모두 대응.
3. **fate 4 process** 중 bulk decay·biodeg(Q10)·volatil(two-film)만 구현, photolysis/hydrolysis/daughter 미구현.
4. **bed 완전 모델링**: pore water dissolved + bioturbation(PARTMIX) + bed decay → 장기 sediment 오염 fate.
5. Superfund remediation 평가의 핵심 (Housatonic 등 site-specific fPOC).

## 7. 한계

- `caltoxb.f90`(490)·`partmix.f90` 본문 식 미상세 read — header + 역할만 (bed 분배는 water 동일 체계 추정).
- `CALVOLTERM` 함수 본문(two-film K_L/K_G 식) 미read — ChemFate 별 파일 추정.
- ssedtox.f90 driver 전체 흐름(toxic substep·SEDF 연계 순서) 미상세 — 호출만 확인.
- foodchain(ISFDCH)·time-series(TMSR) 후처리 미커버.

## 8. 연결

- [[efdc_propwash]] — propwash fast-settling → toxic 재분배 (NSED2>NSED 연계)
- [[efdc_sedzlj]] — SEDF(settling/erosion flux) = toxic flux 구동원
- [[efdc_dispersion]] — dissolved toxic advection-diffusion
- concepts/sediment-transport — 오염 sediment fate
