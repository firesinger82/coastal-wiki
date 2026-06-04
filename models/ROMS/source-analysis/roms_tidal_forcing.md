---
title: "ROMS 조석 forcing(set_tides.F) — SSH_TIDES(조위)/UV_TIDES(조류) 경계·body force, tidal constituent(amp/phase/Tperiod) + nodal correction + AVERAGES_DETIDE de-tiding"
topic: roms
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/source_code/roms/ROMS/Nonlinear/set_tides.F (645) 직접 read — SSH_TIDES/UV_TIDES CPP(3), tidal elevation+current 추가(12), set_tides_tile + mod_tides, AVERAGES_DETIDE(32-48) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-04
verification_by: "Claude Opus 4.8 (1M context) — 조석 forcing verbatim"
verification_date: 2026-06-04
related:
  - models/ROMS/source-analysis/roms_open_boundaries.md
  - models/ROMS/source-analysis/roms_barotropic_2d.md
---

# ROMS 조석 forcing (set_tides.F)

> `set_tides.F`(645, module `set_tides_mod`) 직접 read. ROMS 의 **조석 강제** — 경계/body 에 **조위(SSH_TIDES)·조류(UV_TIDES)** 추가. `SSH_TIDES || UV_TIDES` CPP 활성. ADCIRC 의 tidal potential body-force([[../ADCIRC/source-analysis/adcirc-tidal-forcing]])와 달리 ROMS 는 주로 **경계 조석**(외부 조화상수 → 경계 조위/조류).

## 1. 조석 추가 (set_tides.F:12)

> "adds tidal elevation (m) and tidal currents (m/s)"
- **SSH_TIDES**: 조위 조화상수(`SSH_Tamp`·`SSH_Tphase`) × `cos(ω·t − φ)` 합 → 경계 자유표면([[roms_open_boundaries]] Chapman/Flather BC 에 입력).
- **UV_TIDES**: 조류 타원(`UV_Tamp`/`UV_Tphase`/`UV_Tangle`/ellipse) → 경계 barotropic 유속.
- `Tperiod` = 분조 주기(M2/S2/K1/O1 등), `mod_tides` 가 조화상수 보관.

## 2. Nodal correction + equilibrium

- 조석 forcing 파일(tide forcing NetCDF)의 진폭/위상은 기준시각 기준 → **nodal correction**(18.6년 교점 보정)·equilibrium argument 로 현재 시각 보정(`tide_start`).
- ramp(점진 도입)로 초기 충격 완화.

## 3. AVERAGES_DETIDE — de-tiding (set_tides.F:32-48)

- `AVERAGES_DETIDE`: 출력 시 **조석 성분 제거**(harmonic 누적으로 조석 분리) → 잔차(residual/subtidal) 순환만 출력. `itide` 분조별 누적. 조석평균 흐름 분석(ADCIRC harmonic analysis [[../ADCIRC/source-analysis/adcirc-tidal-forcing]] §5 와 유사 목적, 반대 방향=제거).

## 4. 위치

- 경계 조석([[roms_open_boundaries]]) + barotropic mode([[roms_barotropic_2d]]) 에 적용. ADCIRC(전영역 tidal potential)와 달리 ROMS 는 **regional 모델**이라 경계 조석 + (선택) equilibrium tidal potential.
- 조석 조화상수는 외부(TPXO/FES/OTPS) → ROMS forcing 파일.

## 5. 연결

- [[roms_open_boundaries]] — 경계 조위/조류 BC(set_tides 가 공급)
- [[roms_barotropic_2d]] — barotropic 조석 흐름
- [[../ADCIRC/source-analysis/adcirc-tidal-forcing]] — ADCIRC tidal potential(전영역, 대비)
- TPXO/FES/OTPS(외부 조화상수) / Foreman(nodal correction)
