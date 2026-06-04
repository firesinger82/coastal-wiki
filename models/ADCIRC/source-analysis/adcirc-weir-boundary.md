---
title: "ADCIRC weir/levee 경계(weir_boundary.F90) — internal/external barrier 월류(overtopping) free/submerged flow + time-varying weir(TVW) + IBTYPE 4/24 levee·64 vertical element wall. BARMIN 임계"
topic: adcirc
canonical_source: self
citation_status: verified
verification_method: "models/ADCIRC/raw/source_code/adcirc/src/weir_boundary.F90 (2715, module WEIR) 직접 read — BARINHT/BARLANHT(internal/external barrier 고도 47-50), BARMIN 0.04m 임계(51), vertical element wall BARMIN64=1.2·H0(259), TVW(time-varying weir) namelist file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-04
verification_by: "Claude Opus 4.8 (1M context) — weir 월류·TVW verbatim"
verification_date: 2026-06-04
related:
  - models/ADCIRC/source-analysis/adcirc-boundary-conditions.md
  - models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md
  - models/ADCIRC/source-analysis/adcirc-momentum-implementation.md
---

# ADCIRC weir/levee 경계 (weir_boundary.F90)

> `weir_boundary.F90`(2715, module `WEIR`) 직접 read. [[adcirc-boundary-conditions]] 의 **internal barrier(IBTYPE 4/24 levee·5/25 +pipes·64 vertical element wall)** 월류(overtopping) 계산의 실제 구현. paired weir node 양쪽 수위차로 둑 위 월류 유량 산출. 제방·방조제·도로 둑의 범람(overtopping flooding) 핵심 — 한국 연안 방조제·storm surge 침수.

## 1. Barrier 고도 (module WEIR, :47-55)

| 변수 | 의미 |
|---|---|
| `BARINHT1/2` | **internal** barrier(levee, 양면 wet) 고도 — 이전/현 step |
| `BARLANHT1/2` | **external** barrier(land, 한면 wet) 고도 |
| `BARMIN` | weir 식 적용 최소 수심(둑 위, **0.04 m**) |
| `BARMIN64*` | vertical element wall(IBTYPE 64) 의 submerged 판정 임계(`1.2·H0`, wetdry HOFF 등가) |

## 2. Weir 월류 (overtopping)

paired node(둑 양쪽, [[adcirc-boundary-conditions]] §2 weir/weird dual)의 수위 `ζ1/ζ2` 와 둑 고도 `BARHT` 로:
- **둑 위 수심** `H_up = ζ_high − BARHT`. `H_up < BARMIN`(0.04m) 이면 월류 없음(둑 위 마름).
- **free flow**(자유 월류, 한쪽만 둑 위): supercritical broad-crested weir 식 — `Q ∝ C·H_up^{3/2}` (둑 위 수심의 3/2승).
- **submerged flow**(양쪽 둑 위, 잠긴 둑): subcritical — `Q ∝ C·H_d·√(ζ_high − ζ_low)` (수위차 기반).
- supercritical/subcritical 전환은 하류/상류 수심비로 판정. → 월류 유량 `Q` 가 [[adcirc-momentum-implementation]] 의 normal flux 로 양 node 에 부호 반대 적용(질량 보존).

## 3. Vertical element wall — IBTYPE 64 (:259)

- 격자 element edge 를 따라 세운 **수직 벽**(submerged weir, SB). `BARMIN64 = 1.2·H0`(wetting-drying HOFF 와 등가). submerged/non-submerged 판정(`BARMIN64_SUBM/NOSUBM/SLIM 0.5`) + 경사(slope) 고려. element-based weir → 더 세밀한 둑 표현.

## 4. Time-Varying Weir (TVW)

- `INT_TVW`/`EXT_TVW`(namelist `found_tvw_nml`): **시변 둑 고도** — 둑 붕괴(breach)·가동보·해체를 시간에 따라(`BARINHT1→2` 보간) 모사. 제방 붕괴 시나리오·levee failure surge 모의.

## 5. 위치

- [[adcirc-boundary-conditions]] 가 IBTYPE 카탈로그(둑 종류)를, 본 노트가 **월류 유량 계산 메커니즘**을 담당. wetting-drying([[adcirc-wetting-drying-implementation]])과 연계(둑 위 wet/dry).
- 응용: 방조제 월파 침수, 제방 붕괴 범람, hurricane levee overtopping(New Orleans 등).

## 6. 연결

- [[adcirc-boundary-conditions]] — IBTYPE 4/5/24/25/64 weir 카탈로그(본 노트가 그 월류 구현)
- [[adcirc-momentum-implementation]] — 월류 Q → normal flux
- [[adcirc-wetting-drying-implementation]] — 둑 위 wet/dry(BARMIN·H0)
