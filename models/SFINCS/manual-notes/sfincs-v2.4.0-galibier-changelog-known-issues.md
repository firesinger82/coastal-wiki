---
title: "SFINCS v2.4.0 Galibier 릴리스 델타 — Changelog·Known issues·버전 provenance (2026.01, mt.Faber 기반)"
model: SFINCS
component: manual-notes (release notes)
canonical_source: self
verification_method: "SFINCS v2.4.0 Galibier manual report(108p, Tim Leijnse, 2026-06-15) pdftotext: §1.2.2 Known issues·§1.2.3 Releases Changelog 본문 직접 추출(변경/버그픽스/alpha 리스트·버전명·릴리스 채널). 위키 SFINCS 소스감사 manifest(main HEAD 2026-06-18) 대조. 문서제목+section 인용."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-27
related:
  - models/SFINCS/manual-notes/sfincs-v2.4.0-galibier-validation-testbed.md
  - models/SFINCS/README.md
  - models/SFINCS/manifest.md
last_source_check: 2026-10-12 (recovery 차이 결론 반영)
---

# SFINCS v2.4.0 Galibier 릴리스 델타

공식 변경 기록은 v2.4.0 Galibier의 수정 이력을 서술한다. `docs/developments.rst:32` `Official open source version 2026.01: v2.4.0 Galibier release release`
현재 소스는 Galibier 판명을 하드코딩한다. `sfincs_lib.f90:97` `build_revision = "$Rev: v2.4.0 Galibier Release"`
기존 노트는 main HEAD 2026-06-18 수집을 기록한다. 기존 판 기록(수정 전 이 노트:18·25): `main HEAD 2026-06-18`.
이 대조는 세 기록의 revision 동일성을 확인하지 못했다. `docs/developments.rst:32` `Official open source version 2026.01: v2.4.0 Galibier release release`; `sfincs_lib.f90:97` `build_revision = "$Rev: v2.4.0 Galibier Release"`; `sfincs_lib.f90:98` `build_date     = "$Date: 2026-06-11"`; 기존 판 기록(수정 전 이 노트:18·25): `main HEAD 2026-06-18`.
현재 구현의 판정은 인용한 소스 줄을 따른다. `sfincs_lib.f90:97` `build_revision = "$Rev: v2.4.0 Galibier Release"`; `sfincs_lib.f90:98` `build_date     = "$Date: 2026-06-11"`

## 버전 정체

- **v2.4.0 "Galibier"** = 'Generating Accurate Large-scale Inundation: Better Insights for Emergency Response' (2026 첫 공식 릴리스, §1.2.3)
- 배포 채널: GitHub `releases/tag/v2.4.0_Galibier_release`(GPL-3.0 소스) · Windows exe(download.deltares.nl/sfincs) · Docker `deltares/sfincs-cpu:sfincs-v2.4.0-Galibier-Release`
- **기반**: 2025.02 **v2.3.0 'mt. Faber'** 전 기능 + 아래 변경. 버전 계보: 2023 Cauberg → v2.2.0 col d'Eze → v2.3.0 mt.Faber → **v2.4.0 Galibier**
- 기존 판 기록은 raw clone을 depth-1 main HEAD 2026-06-18로 적었다. 기존 판 기록(수정 전 이 노트:25): `main HEAD 2026-06-18`.
  판 동일성을 확정하려면 수집 시점의 revision 증거 또는 해당 판의 별도 소스 원문이 필요하다. `docs/developments.rst:32` `Official open source version 2026.01: v2.4.0 Galibier release release`; `sfincs_lib.f90:97` `build_revision = "$Rev: v2.4.0 Galibier Release"`; `sfincs_lib.f90:98` `build_date     = "$Date: 2026-06-11"`

## Changelog — 신규/추가 (§1.2.3)

- **`timestep_analysis=1`**: 타임스텝 제한 변수(`average_required_timestep`·`percentage_limiting_timestep`)를 sfincs_map.nc·화면 출력 → 어느 셀이 전역 Δt 제한하는지 분석
B042의 근거와 판정은 [검증 정본](../source-analysis/sfincs_io_data.md#cv-s-b042)을 따른다. [10-12 결론 검증 보완]
- **`huvmin`**(속도계산 최소수심, `uv=q/max(hu,huvmin)`, 출력·이류용)
- 파력 배율의 활성 입력 이름은 snapwave_waveforces_ratio이다. `sfincs_input.f90:308` `call read_real_input(500,'snapwave_waveforces_ratio',waveforces_ratio,1.0)` 근거: `docs/developments.rst:32` `Official open source version 2026.01: v2.4.0 Galibier release release`<br>`docs/developments.rst:54` `* Added input variable 'snapwave_waveforces_factor' which you can set to 0 to turn off wave forces and thus incident wave setup.`<br>`sfincs_lib.f90:97` `build_revision = "$Rev: v2.4.0 Galibier Release"`<br>`sfincs_input.f90:308` `call read_real_input(500,'snapwave_waveforces_ratio',waveforces_ratio,1.0)`<br>`sfincs_snapwave.f90:502` `fwuv(ip) = waveforces_ratio * (0.5 * (cosrot * fwx0(nm) + sinrot * fwy0(nm)) + 0.5 * ( cosrot * fwx0(nmu) + sinrot * fwy0(nmu))) / rhow` [대조 보고서 §5 E014·B044·K140·C018](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:965) 결론: 문서 오기. 이 판은 snapwave_waveforces_ratio를 0으로 설정하면 SnapWave의 직접 파력 전달을 끈다.
  읽기 기본값은 1.0이다. `sfincs_input.f90:308` `call read_real_input(500,'snapwave_waveforces_ratio',waveforces_ratio,1.0)`
배율 0은 SnapWave의 직접 파력 전달을 끈다. 단위와 사용식은 [파력 전달 정본](../source-analysis/sfincs_snapwave.md#cv-s-wave-force)을 따른다. 전달되는 fwuv의 차원은 m²/s²이다. [10-12 결론 검증 정정]
  공식 변경 기록은 같은 기능의 이름을 snapwave_waveforces_factor로 적는다. `docs/developments.rst:54` `* Added input variable 'snapwave_waveforces_factor' which you can set to 0 to turn off wave forces and thus incident wave setup.`
  내부 변수 이름은 waveforces_ratio이다. `sfincs_input.f90:308` `call read_real_input(500,'snapwave_waveforces_ratio',waveforces_ratio,1.0)`; `sfincs_snapwave.f90:502` `fwuv(ip) = waveforces_ratio * (0.5 * (cosrot * fwx0(nm) + sinrot * fwy0(nm)) + 0.5 * ( cosrot * fwx0(nmu) + sinrot * fwy0(nmu))) / rhow`; `sfincs_snapwave.f90:508` `fwuv(ip) = waveforces_ratio * (0.5 * (-sinrot * fwx0(nm) + cosrot * fwy0(nm)) + 0.5 * (-sinrot * fwx0(nmu) + cosrot * fwy0(nmu))) / rhow`
- **`sfincs_his.nc` 파 관련 변수명 일관화**(예 `point_hm0`) — ⚠ **post-processing 스크립트 breaking change**
- **wavemaker 입력변수 rename**(예 `wavemaker_wvmfile`, 레거시 호환 변수 유지)
- **QC testbed v2.0** — 검증테스트 **2배 증가**([validation 노트](sfincs-v2.4.0-galibier-validation-testbed.md))
- **HydroMT-SFINCS v2.0.0**(Python setup tool 신버전 권장)

## Changelog — 버그픽스 (§1.2.3)

B047·C021의 누적 강수 결함 후보와 반대 근거는 [검증 정본](../source-analysis/sfincs_infiltration.md#cv-s-b047)을 따른다. 결론은 강수 활성·CN A·storecumprcp=0에 한정한 E이다. [10-12 결론 검증 보완]
  현재 코드의 판정은 [Curve Number 수정 이력과 현재 코드](#curve-number-수정-이력과-현재-코드)를 따른다. `sfincs_meteo.f90:1321` `if (store_cumulative_precipitation) then`; `sfincs_meteo.f90:1534` `if (store_cumulative_precipitation) then`; `sfincs_infiltration.f90:709` `if (store_cumulative_precipitation) then`
### 문서와 코드 차이 (외부 원문 판정)

| 보고서 행 ID | 항목 | 근거 | 결론 |
|---|---|---|---|
| B048 | 북쪽에서 파를 가하는 wavemaker 버그 | [검증 정본](../source-analysis/sfincs_nonhydrostatic_wavemaker.md#cv-s-b048) | 근거와 판정은 정본을 따른다. [10-12 결론 검증 보완] |
| B049 | 정규격자 binary sbgfile 버그 | [검증 정본](../source-analysis/sfincs_subgrid_quadtree.md#cv-s-b049) | 근거와 판정은 정본을 따른다. [10-12 결론 검증 보완] |
| B050 | Neumann 경계(msk=6) 버그 | [검증 정본](../source-analysis/sfincs_boundaries_forcing.md#cv-s-b050) | 근거와 판정은 정본을 따른다. [10-12 결론 검증 보완] |
| B051 | SnapWave IG 생성항 버그 | [검증 정본](../source-analysis/sfincs_snapwave.md#cv-s-b051) | 근거와 판정은 정본을 따른다. [10-12 결론 검증 보완] |

## Curve Number 수정 이력과 현재 코드

공식 v2.4.0 변경 기록은 storecumprcp=0의 Curve Number 문제를 수정했다고 기록한다. `docs/developments.rst:27` `* Issue in SFINCS v2.3.0 mt Faber Release regarding Curve Number infiltration if storecumprcp = 0 (default), then infiltration is not processed correctly and can result to unrealistic results! Simple solution for now: put storecumprcp = 1 when using this infiltration option. This issue is fixed in the 2026.01 Galibier Release!`; `docs/developments.rst:63` `* Fixed bug with Curve Number infiltration if storecumprcp = 0 (default).`
현재 코드의 CN A 식은 cumprcp와 cuminf를 사용한다. `sfincs_infiltration.f90:689` `if (cumprcp(nm) > sfacinf * qinffield(nm)) then ! qinffield is S`; `sfincs_infiltration.f90:693` `Qq  = (cumprcp(nm) - sfacinf * qinffield(nm))**2 / (cumprcp(nm) + (1.0 - sfacinf) * qinffield(nm))  ! cumulative runoff in m`; `sfincs_infiltration.f90:695` `qinfmap(nm) = (I - cuminf(nm)) / dt           ! infiltration in m/s`
B047·C021의 누적 강수 결함 후보와 반대 근거는 [검증 정본](../source-analysis/sfincs_infiltration.md#cv-s-b047)을 따른다. 결론은 강수 활성·CN A·storecumprcp=0에 한정한 E이다. [10-12 결론 검증 보완]
현재 코드에서 출력 플래그 의존성의 제거를 확인하지 못했다. `sfincs_input.f90:280` `call read_int_input(500,'storecumprcp',storecumprcp,0)`; `sfincs_input.f90:511` `store_cumulative_precipitation = .false.`; `sfincs_input.f90:512` `if (storecumprcp==1) then`; `sfincs_input.f90:513` `store_cumulative_precipitation = .true.`; `sfincs_meteo.f90:1321` `if (store_cumulative_precipitation) then`; `sfincs_meteo.f90:1534` `if (store_cumulative_precipitation) then`; `sfincs_infiltration.f90:709` `if (store_cumulative_precipitation) then`
문서의 수정 이력과 현재 코드의 상태를 구분한다. `docs/developments.rst:27` `* Issue in SFINCS v2.3.0 mt Faber Release regarding Curve Number infiltration if storecumprcp = 0 (default), then infiltration is not processed correctly and can result to unrealistic results! Simple solution for now: put storecumprcp = 1 when using this infiltration option. This issue is fixed in the 2026.01 Galibier Release!`; `docs/developments.rst:63` `* Fixed bug with Curve Number infiltration if storecumprcp = 0 (default).`; `sfincs_meteo.f90:1321` `if (store_cumulative_precipitation) then`; `sfincs_meteo.f90:1534` `if (store_cumulative_precipitation) then`; `sfincs_infiltration.f90:709` `if (store_cumulative_precipitation) then`
실제 영향과 수정 반영 판은 별도 증거가 필요하다. `docs/developments.rst:27` `* Issue in SFINCS v2.3.0 mt Faber Release regarding Curve Number infiltration if storecumprcp = 0 (default), then infiltration is not processed correctly and can result to unrealistic results! Simple solution for now: put storecumprcp = 1 when using this infiltration option. This issue is fixed in the 2026.01 Galibier Release!`; `docs/developments.rst:63` `* Fixed bug with Curve Number infiltration if storecumprcp = 0 (default).`; `sfincs_meteo.f90:1321` `if (store_cumulative_precipitation) then`; `sfincs_meteo.f90:1534` `if (store_cumulative_precipitation) then`; `sfincs_infiltration.f90:709` `if (store_cumulative_precipitation) then`
판정: 정적 판독으로 확인, 실행으로는 확인하지 않음. `docs/developments.rst:27` `* Issue in SFINCS v2.3.0 mt Faber Release regarding Curve Number infiltration if storecumprcp = 0 (default), then infiltration is not processed correctly and can result to unrealistic results! Simple solution for now: put storecumprcp = 1 when using this infiltration option. This issue is fixed in the 2026.01 Galibier Release!`; `docs/developments.rst:63` `* Fixed bug with Curve Number infiltration if storecumprcp = 0 (default).`; `sfincs_input.f90:280` `call read_int_input(500,'storecumprcp',storecumprcp,0)`; `sfincs_input.f90:511` `store_cumulative_precipitation = .false.`; `sfincs_input.f90:512` `if (storecumprcp==1) then`; `sfincs_input.f90:513` `store_cumulative_precipitation = .true.`; `sfincs_meteo.f90:1321` `if (store_cumulative_precipitation) then`; `sfincs_meteo.f90:1323` `cumprcp(nm) = cumprcp(nm) + prcp(nm) * dt`; `sfincs_meteo.f90:1534` `if (store_cumulative_precipitation) then`; `sfincs_meteo.f90:1535` `cumprcp(nm) = cumprcp(nm) + ptmp * dt`; `sfincs_infiltration.f90:689` `if (cumprcp(nm) > sfacinf * qinffield(nm)) then ! qinffield is S`; `sfincs_infiltration.f90:693` `Qq  = (cumprcp(nm) - sfacinf * qinffield(nm))**2 / (cumprcp(nm) + (1.0 - sfacinf) * qinffield(nm))  ! cumulative runoff in m`; `sfincs_infiltration.f90:695` `qinfmap(nm) = (I - cuminf(nm)) / dt           ! infiltration in m/s`; `sfincs_infiltration.f90:709` `if (store_cumulative_precipitation) then`; `sfincs_infiltration.f90:713` `cuminf(nm) = cuminf(nm) + qinfmap(nm) * dt`; `sfincs_infiltration.f90:143` `cuminf = 0.0`; `sfincs_infiltration.f90:140` `cumprcp = 0.0`

## Alpha/beta (고급, Deltares 문의 필요)

- 급경사 SnapWave **쇄파·파유발 setup** 개선
- SnapWave **식생 효과**([Wu 식생 검증케이스](sfincs-v2.4.0-galibier-validation-testbed.md))
- wavemaker incident wave energy 강제 옵션
- "hyper-fast but scandalous" **bathtub** 옵션
- **GPU 구현 개선** 근거: `docs/developments.rst:77` `* Improved GPU immplementation`<br>`docs/developments.rst:139` `* Upgraded GPU implementation for consistent results with CPU version.`<br>`sfincs_openacc.f90:15` `!$acc enter data, copyin( kcs, kfuv, kcuv, zs, zs0, zsderv, q, q0, uv, uv0, zb, zbuv, zbuvmx, zsmax, maxzsm, qmax, vmax, twet, zsm, z_volume, &`<br>`sfincs_momentum.f90:156` `!$acc loop, reduction( min : min_dt ), gang, vector`<br>`sfincs_continuity.f90:336` `!$acc loop gang vector` [대조 보고서 §5 B056](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1030) 결론: 코드 대조 대상 아님. 문서의 GPU 향상과 CPU 결과 일치 문장은 비교 시험으로 판정할 성능 주장이다. [10-12 G 정리]

## Known issues (§1.2.2)

- **restartfile 호환**: 2023 Cauberg 이전 restartfile 은 col d'Eze·mt.Faber·이후 릴리스서 재생성 필요 근거: `docs/developments.rst:88` `Official open source version 2025.02: v2.3.0 mt. Faber release`<br>`docs/developments.rst:121` `* Fixed bug with restartfile where fluxes were not read in fully correctly due to mismatch length of variable (dummy +1). NOTE - if you are still using restartfiles from SFINCS 2023 Cauberg release or older, you should remake your restartfiles to overcome potential issues!`<br>`sfincs_initial_conditions.F90:36` `allocate(iniq(npuv+ncuv+1)) ! Note: q is actually larger than npuv! It has size npuv + ncuv + 1`<br>`sfincs_domain.f90:2197` `! q, q0, uv, and uv0 also contain the combined values at quadtree transition cells. Plus 1 for dummy values set to 0.0.`<br>`sfincs_domain.f90:2199` `allocate(q(npuv + ncuv + 1))`<br>`sfincs_initial_conditions.F90:229` `read(500)iniq`<br>`sfincs_output.f90:710` `write(911)q` [대조 보고서 §5 B066](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1031) 결론: 판 차이. 이 판은 재시작 유량 배열을 dummy 원소를 포함한 npuv+ncuv+1 길이로 읽고 쓴다.
- **BMI**: SFINCS BMI = XMI(BMI+확장, Hughes 2022, `xmipy`)와 최신이나 **CSDMS standard BMI 2.0 미반영**
B047·C021의 누적 강수 결함 후보와 반대 근거는 [검증 정본](../source-analysis/sfincs_infiltration.md#cv-s-b047)을 따른다. 결론은 강수 활성·CN A·storecumprcp=0에 한정한 E이다. [10-12 결론 검증 보완]
  현재 코드에서 출력 플래그 의존성의 제거를 확인하지 못했다. `sfincs_input.f90:280` `call read_int_input(500,'storecumprcp',storecumprcp,0)`; `sfincs_input.f90:511` `store_cumulative_precipitation = .false.`; `sfincs_input.f90:512` `if (storecumprcp==1) then`; `sfincs_input.f90:513` `store_cumulative_precipitation = .true.`; `sfincs_meteo.f90:1321` `if (store_cumulative_precipitation) then`; `sfincs_meteo.f90:1534` `if (store_cumulative_precipitation) then`; `sfincs_infiltration.f90:709` `if (store_cumulative_precipitation) then`
  판정: 정적 판독으로 확인, 실행으로는 확인하지 않음. `sfincs_meteo.f90:1321` `if (store_cumulative_precipitation) then`; `sfincs_meteo.f90:1534` `if (store_cumulative_precipitation) then`; `sfincs_infiltration.f90:689` `if (cumprcp(nm) > sfacinf * qinffield(nm)) then ! qinffield is S`; `sfincs_infiltration.f90:693` `Qq  = (cumprcp(nm) - sfacinf * qinffield(nm))**2 / (cumprcp(nm) + (1.0 - sfacinf) * qinffield(nm))  ! cumulative runoff in m`; `sfincs_infiltration.f90:695` `qinfmap(nm) = (I - cuminf(nm)) / dt           ! infiltration in m/s`; `sfincs_infiltration.f90:709` `if (store_cumulative_precipitation) then`

## 개발 상태 (§1.2.1)

2026-06 기준 development status 표(Fig 1.10-1.11) — SFINCS 코어 + HydroMT-SFINCS(Python) 별 GA(General Available) 기능 녹색표시. 2017년부터 지속 개발.

> 핵심: Galibier = mt.Faber + 분석/QGIS/wave 옵션 + 버그픽스 5 + testbed 2배 + HydroMT v2.0. **소스 미동봉**(GitHub 태그)·**his.nc 변수명 breaking change** 주의. 검증 → [testbed 노트](sfincs-v2.4.0-galibier-validation-testbed.md).

## 문서 참고 링크 오류

참고 링크 오류: `docs/developments.rst:283` 근처의 [`releases/tag/v2.0.2`](https://github.com/Deltares/SFINCS/releases/tag/v2.0.2)는 존재하지 않는 태그 링크이다. 실제 태그 이름은 [`v2.0.2_Blockhaus_release`](https://github.com/Deltares/SFINCS/releases/tag/v2.0.2_Blockhaus_release)이다. [외부 원문 판정 B103](../../../_staging/recovery/compare/external-results-sf.md#b103-개선된-2차원-이류-항).
