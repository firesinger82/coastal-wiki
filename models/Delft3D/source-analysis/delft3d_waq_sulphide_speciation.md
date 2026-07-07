---
title: "Delft3D WAQ 용존 황화물 화학종 분배 source-analysis — sulfid.f90 (H2S/HS⁻/S²⁻ diprotic speciation)"
model: Delft3D
component: waq-process
canonical_source: self
citation_status: verified
verification_method: "Delft3D raw 직접 read: src/engines_gpl/waq/waq_process/sulfid.f90(150) 전수 — 2단 산해리 speciation·간극수 보정·frsdis 음수가드 file:line 직접 검증(2026-07-07). ★active-cell 게이트 부재·ks1/ks2 주석오류(H2CO3) 확인."
note_author: "Claude Fable 5"
note_date: 2026-07-07
related:
  - models/Delft3D/source-analysis/delft3d_waq_process_library.md
  - models/Delft3D/source-analysis/delft3d_waq_ph_carbonate.md
  - models/Delft3D/source-analysis/delft3d_waq_sediment_oxygen_demand.md
---

# Delft3D WAQ 용존 황화물 분배 — `sulfid.f90` (SUBROUTINE SULFID)

> 소스: `.../src/engines_gpl/waq/waq_process/sulfid.f90` (150줄, `module m_sulfid`).
> **정체**: 공극수(pore water) **총 용존 황화물(SUD) → H2S / HS⁻ / S²⁻ 3 화학종 분배**. 무산소(anoxic) 저니·저층수의 황산염 환원 산물 — H2S 는 독성·악취·금속(FeS) 결합의 주역. [[delft3d_waq_ph_carbonate]]의 탄산계와 동형 수학(diprotic Bjerrum)이나 물질(황) 신설. 진단(diagnostic) process.

## 0. 진단 process — 화학종 분율만
flux 미갱신, 출력 6(농도 3 + 분율 3)만 기입(:131-136). 총 SUD 는 별도 process(황산염 환원·산화)가 구동, 본 루틴은 순간 pH·T 평형 분배.

## 1. 2단 산해리 speciation (diprotic)
```fortran
h_ion = 10.**(-ph)                                    ! :105 양성자 농도
ks1 = 10.**lksth2s * tcksth2s**(temp-20.)             ! :106 H2S ↔ HS⁻ + H⁺
ks2 = 10.**lksths  * tcksths **(temp-20.)             ! :107 HS⁻ ↔ S²⁻ + H⁺
csdt = sud / (32000. * poros)                         ! :108 gS/m³ → mol/l 공극수
csd1 = csdt / (1 + ks1/H + ks1·ks2/H²)                ! :109 H2S(비해리)
csd2 = ks1·csd1/h_ion                                 ! HS⁻
csd3 = csdt - csd1 - csd2                              ! S²⁻ (잔차)
```
- 해리상수 `ks = 10^(log K)·TC^(T−20)` — log 형 입력 + Arrhenius형 온도보정.
- **Bjerrum 분배**: 공통분모 `1 + ks1/H + ks1ks2/H²` 로 H2S 분율 → HS⁻·S²⁻ 순차.
- 분율 출력 `frh2sdis=csd1/csdt` 등(:114-116).

## 2. ★간극수 농도 보정 `sud/(32000·poros)`
`csdt = SUD/(32000·POROS)`(:108) — 32000 = 황 원자량 32 g/mol × 1000(m³→l), `/POROS` 로 벌크 gS/m³ 를 **공극수 mol/l** 로 환산. [[delft3d_waq_opal_silica_dissolution]] `CSID/POROS` 와 동일 철학 — 저니 반응 매질은 물 부피뿐. 저니(POROS<1) 적용 전제.

## 3. ★주요 findings
- **★active-cell 게이트 부재**: 다른 WAQ process(phcarb·densed·dissi 모두 `IF(BTEST(IKNMRK,0))`)와 달리 **IKNMRK 검사 없이 전 셀 루프**(:90) — inactive 셀도 speciation 계산(무해하나 불필요 연산). 진단이라 flux 오염은 없음.
- **★코드 주석 오류(탄산 복붙)**: 지역변수 선언 주석이 `ks1 ! acidity ... for H2CO3`·`ks2 ! ... for CO2`(:79-80) — 실제는 황화물 해리(lksth2s/lksths 로 계산, :106-107). [[delft3d_waq_ph_carbonate]]에서 복사된 주석 잔재. 심볼명 ks1/ks2 도 탄산 관례 — **인용 시 주석 무시, 코드 로직 기준**.
- **★frsdis 음수 가드**: `frsdis = 1 − fr1 − fr2` 가 부동소수 오차로 <0 이면 `csd3/csdt` 재계산(:117-119) — S²⁻ 분율이 극미(고pH 아니면 ~0)라 언더플로 대비.
- **SUD≤1e-20 → 전 출력 0**(:101, else :122-128): 무황화물 셀 단락.
- **pH·온도 외부 의존**: pH 는 [[delft3d_waq_ph_carbonate]] 등이 공급 — S²⁻ 는 고pH에서만 유의, 하구 pH 7–8 대에선 H2S+HS⁻ 지배.

## 4. Primary sources
- Delft3D-WAQ Processes Library — 황화물 speciation process(`Speciation`/`SpecSud`) 파라미터(lksth2s·lksths·tc). in-code 문헌 인용 없음(표준 산해리 평형), 정의 [[delft3d_waq_process_library]].

## 5. 관련
- [[delft3d_waq_ph_carbonate]] — 동형 diprotic 분배(탄산; 본 노트 주석이 복붙된 출처)
- [[delft3d_waq_sediment_oxygen_demand]] — 무산소 저니(황산염 환원·메탄, 황화물 공급 맥락)
- [[delft3d_waq_process_library]] — process 호출 규약·인접 kinetics
