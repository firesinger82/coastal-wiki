---
title: "ROMS biology(생태계) 프레임워크 — biology.F dispatcher(7-file/CPP 선택) + 모델 카탈로그(NPZD Franks/Powell/iron · Fennel 질소 순환·선택 CARBON/OXYGEN/PO4/RIVER_DON · NEMURO · EcoSim · ECB · hypoxia · red_tide). bio tracer = T/S처럼 transport + 모델별 source/sink"
topic: roms
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/ 직접 read — biology.F(7-file 구조·CPP dispatch 주석 11-66) + 모델 .h 인벤토리(fennel.h 2375/npzd_Franks 589/npzd_Powell 663/nemuro/ecosim/ecb/hypoxia_srm/red_tide) + fennel.h 헤더(NO3/NH4/phyto/chloro/zoo/SDeN/LDeN + CARBON DIC/TAlk + OXYGEN, nitrif/denitrif/Wanninkhof2014/Zeebe-Wolf-Gladrow2001, Nsink=6(CARBON)/4(비 CARBON)) file:line 인용. 2026-10-14 ROMS recovery 대조 보고서 반영."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
last_source_check: "2026-10-14 (recovery 대조 반영)"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — biology 프레임워크·모델 카탈로그·Fennel 과정 verbatim"
verification_date: 2026-06-03
related:
  - models/ROMS/source-analysis/roms_baroclinic_3d.md
  - models/ROMS/source-analysis/roms_advection.md
  - models/ROMS/source-analysis/roms_nonlinear_physics_modules.md
  - models/ROMS/source-analysis/sediment/roms_sediment.md
---

# ROMS biology(생태계) 프레임워크

> `ROMS/Nonlinear/Biology/` 직접 read. ROMS 의 **생물지화학(biogeochemistry) 생태계 모델** 시스템 — 영양염·플랑크톤·탄소·산소 cycle. bio 변수는 **passive tracer 처럼 advection-diffusion**([roms_advection](roms_advection.md)/[roms_baroclinic_3d](roms_baroclinic_3d.md) step3d_t)되고, **source/sink(reaction) 만 모델별** 으로 추가. `BIOLOGY` CPP 정의 시 활성([roms_nonlinear_physics_modules](roms_nonlinear_physics_modules.md)).

## 1. 프레임워크 — biology.F dispatcher (주석 11-66)

각 생태계 모델 = **7 파일** 세트:
| 파일 | 역할 |
|---|---|
| `<model>.h` | source/sink 이산 방정식(reaction kernel) |
| `<model>_mod.h` | 내부 파라미터 선언 |
| `<model>.in` | 파라미터 입력 스크립트 |
| `<model>_inp.h` | 입력 읽기 |
| `<model>_var.h` | 변수 index 할당 |
| `<model>_wrt.h` / `_def.h` | 출력 write / netCDF define |

- **CPP flag 로 1개 모델 선택**(`BIO_FENNEL`/`NPZD_FRANKS`/`NPZD_POWELL`/`NPZD_IRON`/`NEMURO`/`ECOSIM`/`ECB`/`HYPOXIA_SRM`/`RED_TIDE`). biology.F 가 dispatch.
- bio tracer 개수 `NBT` 만큼 tracer 배열(`t(:,:,:,:,iNO3_)` 등) 확장 — T/S 와 같은 transport 커널 공유, 매 step `biology` 커널이 reaction 적용.

## 2. 모델 카탈로그

| 모델 (CPP) | 파일 | 복잡도 |
|---|---|---|
| **NPZD** Franks/Powell/iron | npzd_Franks.h(589)/Powell.h(663)/iron.h | N-P-Z-D 기본 4변수와 조건부 철 제한 (§4) |
| **Fennel** (BIO_FENNEL) | fennel.h(2375) | 질소 순환에 선택 기능을 추가한 구현 (§3) |
| **NEMURO** | nemuro.h | 북태평양 11-변수(2 phyto·3 zoo·silica) |
| **EcoSim** | ecosim.h | bio-optical(Bissett, 다종·색소 spectral) |
| **ECB** | ecb.h | estuarine carbon biogeochemistry |
| **hypoxia_srm** | hypoxia_srm.h | 단순 산소 소모(저산소 진단) |
| **red_tide** | red_tide.h | 적조(Alexandrium cyst) |

### 2.1 NEMURO

선택 조건의 원문은 `# elif defined NEMURO`이다. (`ROMS/Nonlinear/Biology/biology.F:117`; [NT-001](../../../_staging/recovery/compare/roms-biology-vs-code.md#4-노트-대조와-수정안))
CPP 조건과 입력 차이는 보고서 [§2.7](../../../_staging/recovery/compare/roms-biology-vs-code.md#27-nemuro의-입력-항목)과 [§3.6](../../../_staging/recovery/compare/roms-biology-vs-code.md#36-nemuro의-이산-식검사내부-상수)을 참조한다.

### 2.2 EcoSim

선택 조건의 원문은 `# elif defined ECOSIM`이다. (`ROMS/Nonlinear/Biology/biology.F:113`; [NT-001](../../../_staging/recovery/compare/roms-biology-vs-code.md#4-노트-대조와-수정안))
CPP 조건과 입력 차이는 보고서 [§2.8](../../../_staging/recovery/compare/roms-biology-vs-code.md#28-ecosim의-입력-항목)과 [§3.7](../../../_staging/recovery/compare/roms-biology-vs-code.md#37-ecosim의-이산-식검사내부-상수)을 참조한다.

### 2.3 ECB

선택 조건의 원문은 `# elif defined ECB`이다. (`ROMS/Nonlinear/Biology/biology.F:111`; [NT-001](../../../_staging/recovery/compare/roms-biology-vs-code.md#4-노트-대조와-수정안))
CPP 조건과 입력 차이는 보고서 [§2.9](../../../_staging/recovery/compare/roms-biology-vs-code.md#29-ecb의-입력-항목)과 [§3.8](../../../_staging/recovery/compare/roms-biology-vs-code.md#38-ecb의-이산-식검사내부-상수)을 참조한다.

### 2.4 HYPOXIA_SRM

선택 조건의 원문은 `# elif defined HYPOXIA_SRM`이다. (`ROMS/Nonlinear/Biology/biology.F:115`; [NT-001](../../../_staging/recovery/compare/roms-biology-vs-code.md#4-노트-대조와-수정안))
CPP 조건과 입력 차이는 보고서 [§2.10](../../../_staging/recovery/compare/roms-biology-vs-code.md#210-hypoxia_srm의-입력-항목)과 [§3.9](../../../_staging/recovery/compare/roms-biology-vs-code.md#39-hypoxia_srm의-이산-식검사내부-상수)을 참조한다.

### 2.5 RED_TIDE

선택 조건의 원문은 `# elif defined RED_TIDE`이다. (`ROMS/Nonlinear/Biology/biology.F:125`; [NT-001](../../../_staging/recovery/compare/roms-biology-vs-code.md#4-노트-대조와-수정안))
CPP 조건과 입력 차이는 보고서 [§2.11](../../../_staging/recovery/compare/roms-biology-vs-code.md#211-red_tide의-입력-항목)과 [§3.10](../../../_staging/recovery/compare/roms-biology-vs-code.md#310-red_tide의-이산-식검사내부-상수)을 참조한다.

## 3. Fennel 모델 (fennel.h, 2375) — 대표 biogeochem ★

현재 Fennel 구현은 질소 순환 모델에 선택 기능을 추가한 구현이다. ([NT-002](../../../_staging/recovery/compare/roms-biology-vs-code.md#4-노트-대조와-수정안))
`CARBON`·`OXYGEN`·`PO4`·`RIVER_DON`을 모두 끈 기본 생물 추적자는 7개이다. ([NT-002](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론))
기본 생물 추적자는 엽록소 `iChlo`를 포함한다. ([NT-002](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론))
이 옵션들을 추가하면 `NBT`가 달라진다. (`ROMS/Nonlinear/Biology/fennel_mod.h:184-224`)
- **기본 N cycle** 상태변수: `NO3`(질산), `NH4`(암모늄), `Phyt`(식물플랑크톤), `Chlo`(엽록소, variable C:Chl), `Zoop`(동물플랑크톤), `SDeN`/`LDeN`(small/large detritus N).
- `CARBON`은 `iLDeC`, `iSDeC`, `iTIC_`, `iTAlk`를 추가한다. (`ROMS/Nonlinear/Biology/fennel_mod.h:513-518`)
- `CARBON`과 `RIVER_DON`을 함께 켜면 `iRDeC`도 추가한다. (`ROMS/Nonlinear/Biology/fennel_mod.h:519-522`)
- `CARBON` 경로에서 `pCO2_RZ`는 Zeebe–Wolf-Gladrow 탄산계 루틴을 선택한다. `pCO2_RZ`가 없으면 OCMIP 루틴을 사용한다. (`ROMS/Nonlinear/Biology/fennel.h:38-40,1201-1220`) [10-14 전수 검증 정정]
- **OXYGEN** option: + `Oxyg`(용존산소).
- **과정**: 광합성(PAR light limitation) · **nitrification**(NH4→NO3) · grazing · mortality · remineralization · sinking · air-sea O2/CO2 flux.
- Fennel의 `Nsink`는 `CARBON`을 켜면 6이다. (`ROMS/Nonlinear/Biology/fennel.h:324-325`)
- `CARBON`을 끄면 `Nsink`는 4이다. (`ROMS/Nonlinear/Biology/fennel.h:326-328`)
- `RIVER_DON`의 유기물은 침강 목록에 없다. ([NT-004](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론))
- `BIO_FENNEL`에서 산소 교환은 `OXYGEN`을 요구한다. ([NT-005](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론))
- `BIO_FENNEL`에서 CO₂ 교환은 `CARBON`을 요구한다. ([NT-005](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론))
- 각 경로에서 `RW14_OXYGEN_SC`와 `RW14_CO2_SC`가 Wanninkhof (2014) 계수 선택에 관여한다. ([NT-005](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론))
- 산소 Schmidt 수는 `OCMIP_OXYGEN_SC`, `RW14_OXYGEN_SC`, 기본식 순으로 선택한다. ([NT-005](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론))
- `BIO_SEDIMENT`에서 해저 도달 질소를 `NH4`로 복귀시킨다. (`ROMS/Nonlinear/Biology/fennel.h:1464-1484`; [RN1-041](../../../_staging/recovery/compare/roms-sediment-ice-vegetation-vs-code.md#4-노트-대조와-수정안))
- `DENITRIFICATION`을 함께 선택하면 복귀량은 `4/16`이다. (`ROMS/Nonlinear/Biology/fennel.h:1473,1483-1484`; [NT-006](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론))

## 4. NPZD (Franks/Powell) — 최소 모델

4 상태변수 `N`(nutrient)-`P`(phytoplankton)-`Z`(zooplankton)-`D`(detritus). Franks et al. 1986 / Powell et al. 2006.

Franks는 `EXP(K_ext*z_r)`를 광 제한에 쓴다. (`ROMS/Nonlinear/Biology/npzd_Franks.h:319-321`)
Powell은 PAR와 self-shading을 계산한다. ([NT-007](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론))
Franks·Powell·iron의 `K_NO3`는 현재 식에서 농도와 더해진다. ([NT-007](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론))
Fennel `K_NO3`는 농도에 곱해지는 역수 계수다. ([NT-007](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론))
`NPZD_IRON`에서 `IRON_LIMIT`을 함께 켜면 `NBT=6`이다. (`ROMS/Nonlinear/Biology/npzd_iron_mod.h:144-145`)
`NPZD_IRON`에서 `IRON_LIMIT`을 끄면 `NBT=4`이다. (`ROMS/Nonlinear/Biology/npzd_iron_mod.h:146-148`)
연안 철 완화는 `IRON_LIMIT`과 `IRON_RELAX`가 함께 정의되고 `IF (h(i,j).le.FeHmin(ng)) THEN`일 때 적용된다. (`ROMS/Nonlinear/Biology/npzd_iron.h:305,311-313`; [NT-008](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론))

## 5. 결합 — tracer transport 와의 관계

```
step3d_t (tracer 방정식): ∂(Hz·C)/∂t + advection + diffusion = Hz·(bio source/sink)
```
- 생물 추적자는 T/S와 추적자 수송 루프를 공유한다. 이류 스킴은 추적자별로 선택한다. (`ROMS/Nonlinear/step3d_t.F:405-412,432-472`; [roms_advection](roms_advection.md)) 생물 반응은 모델별 `biology` 커널에서 계산한다 (`ROMS/Nonlinear/Biology/biology.F:109-126`). [10-14 전수 검증 정정]
- Fennel의 수직 침강은 별도의 PPM 재구성과 WENO 보정을 사용한다 (`ROMS/Nonlinear/Biology/fennel.h:1286-1295,1321-1340`). Fennel의 광합성 광 제한은 PAR를 사용한다 (`ROMS/Nonlinear/Biology/fennel.h:701-736`). [10-14 전수 검증 정정]
- Fennel은 `BIO_SEDIMENT`와 `CARBON`을 함께 선택하면 해저에 도달한 쇄설물 탄소를 `iTIC_`에 더한다 (`ROMS/Nonlinear/Biology/fennel.h:1464,1512-1521`). [10-14 전수 검증 정정]

내부 농도 제한과 최종 transport 배열의 음수 허용을 함께 적는다. ([NT-010](../../../_staging/recovery/compare/roms-biology-vs-code.md#4-노트-대조와-수정안))
`ROMS/Nonlinear/Biology/fennel.h:1551`의 조건문 원문은 `#ifdef CARBON`이다.
`ROMS/Nonlinear/Biology/fennel.h:1554`의 원문은 `            Bio(i,k,iTIC_)=MIN(Bio(i,k,iTIC_),3000.0_r8)`이다.
`ROMS/Nonlinear/Biology/fennel.h:1555`의 원문은 `            Bio(i,k,iTIC_)=MAX(Bio(i,k,iTIC_),400.0_r8)`이다.
`ROMS/Nonlinear/Biology/fennel.h:1558`의 원문은 `#endif`이다.
`ROMS/Nonlinear/Biology/fennel.h:1545-1547`의 원문은 `!  zero. Notice that final tracer values, t(:,:,:,nnew,:) are not`, `!  bounded >=0 so that we can preserve total inventory of N and`, `!  C even when advection causes tracer concentration to go negative.`이다.

## 6. 식·입력·단위 대조

본 노트는 프레임워크·모델 카탈로그·Fennel/NPZD 구조를 정리한다. ([NT-011·NT-025](../../../_staging/recovery/compare/roms-biology-vs-code.md#4-노트-대조와-수정안))
현재 HEAD의 식·입력·단위 대조는 [생물 대조 보고서](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론)를 참조한다. ([NT-011·NT-025](../../../_staging/recovery/compare/roms-biology-vs-code.md#4-노트-대조와-수정안))
입력 예의 수치와 생략 시 자동 초기화를 구분한다. ([NT-026](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론))
main3d의 생물 호출에는 `BIOLOGY` 조건이 있으나 `Lbiology` 런타임 가드는 없다. (`ROMS/Nonlinear/main3d.F:1035-1037`; [NT-026](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론))
Fennel 입력의 `CASE ('Vadvection')` 중복은 `ADJOINT`·`TANGENT`·`TL_IOMS` 중 하나가 정의될 때 드러난다. (`ROMS/Nonlinear/Biology/fennel_inp.h:222,233,245`; [NT-026](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론))
Fennel·ECB의 `PhyIP`와 EcoSim `NFIX_flag`·`RefugeDep`는 입력·출력에 있으나 해당 비선형 반응식에는 소비되지 않는다. ([NT-026](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론))
EcoSim 주석은 깊이별 refuge 처리를 제거했다고 명시한다. (`ROMS/Nonlinear/Biology/ecosim.h:552-555`; [NT-026](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론))
단위 문제는 `UN-012`·`UN-015`의 입력 설명 오기 B와 `UN-013`·`UN-014`·`UN-016`의 메타데이터 결함 후보 E로 구분한다. ([NT-026](../../../_staging/recovery/compare/roms-biology-vs-code.md#5-차이-결론))

- biology_floats.F = Lagrangian float 기반 bio(별도).

## 7. 연결

- [roms_baroclinic_3d](roms_baroclinic_3d.md) — step3d_t tracer 방정식(bio tracer 가 타는 transport)
- [roms_advection](roms_advection.md) — bio tracer advection 스킴(T/S 공유) + WENO(biology/sediment)
- [roms_nonlinear_physics_modules](roms_nonlinear_physics_modules.md) — BIOLOGY CPP 활성·모듈 dispatch
- [roms_sediment](sediment/roms_sediment.md) — 퇴적물 물리 과정의 별도 노트이다. Fennel의 저층 탄소 복귀는 위 `BIO_SEDIMENT`·`CARBON` 경로를 참조한다 (`ROMS/Nonlinear/Biology/fennel.h:1464,1512-1521`). [10-14 전수 검증 정정]
- Fennel et al. 2006 / Franks 1986 / Powell 2006 / Kishi(NEMURO) / Bissett(EcoSim) / Wanninkhof 2014 / Zeebe-Wolf-Gladrow 2001

## 문서와 코드 차이 (10-14 대조)

문서 판: ROMS 위키 wikitext, 2026-05-03 받음, 쪽별 revid는 [manifest.json](../raw/manuals/wiki/manifest.json). 코드 판: 원본 저장소 HEAD `57aecf58`, 2026-09-18, roms-4.2 이후 4.3 개발.

- [roms_biology-differences-1.md](roms_biology-differences-1.md).
- [roms_biology-differences-2.md](roms_biology-differences-2.md).

결론별 개수는 [ROMS-assign-*.tsv](../../../_staging/recovery/assign/)의 3열이 `source-analysis/roms_biology.md`인 행에서 집계했다: A 2, B 68, C 167, D 2, E 25, F 22, 합계 286행.
