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
last_source_check: 2026-10-07 (recovery 재판독 대조)
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
- **Quadtree sfincs_map.nc 직접 QGIS 로드·시각화** 가능
- **`huvmin`**(속도계산 최소수심, `uv=q/max(hu,huvmin)`, 출력·이류용)
- 파력 배율의 활성 입력 이름은 snapwave_waveforces_ratio이다. `sfincs_input.f90:308` `call read_real_input(500,'snapwave_waveforces_ratio',waveforces_ratio,1.0)`
  읽기 기본값은 1.0이다. `sfincs_input.f90:308` `call read_real_input(500,'snapwave_waveforces_ratio',waveforces_ratio,1.0)`
  0을 설정하면 SnapWave 파력의 SFINCS 가속도 전달을 0으로 만든다. `sfincs_snapwave.f90:502` `fwuv(ip) = waveforces_ratio * (0.5 * (cosrot * fwx0(nm) + sinrot * fwy0(nm)) + 0.5 * ( cosrot * fwx0(nmu) + sinrot * fwy0(nmu))) / rhow`; `sfincs_snapwave.f90:503` `! waveforces_ratio = 1.0 by default, but can be set to 0 to avoid double counting incident setup if wavemaker_hinc true`; `sfincs_snapwave.f90:508` `fwuv(ip) = waveforces_ratio * (0.5 * (-sinrot * fwx0(nm) + cosrot * fwy0(nm)) + 0.5 * (-sinrot * fwx0(nmu) + cosrot * fwy0(nmu))) / rhow`
  공식 변경 기록은 같은 기능의 이름을 snapwave_waveforces_factor로 적는다. `docs/developments.rst:54` `* Added input variable 'snapwave_waveforces_factor' which you can set to 0 to turn off wave forces and thus incident wave setup.`
  내부 변수 이름은 waveforces_ratio이다. `sfincs_input.f90:308` `call read_real_input(500,'snapwave_waveforces_ratio',waveforces_ratio,1.0)`; `sfincs_snapwave.f90:502` `fwuv(ip) = waveforces_ratio * (0.5 * (cosrot * fwx0(nm) + sinrot * fwy0(nm)) + 0.5 * ( cosrot * fwx0(nmu) + sinrot * fwy0(nmu))) / rhow`; `sfincs_snapwave.f90:508` `fwuv(ip) = waveforces_ratio * (0.5 * (-sinrot * fwx0(nm) + cosrot * fwy0(nm)) + 0.5 * (-sinrot * fwx0(nmu) + cosrot * fwy0(nmu))) / rhow`
- **`sfincs_his.nc` 파 관련 변수명 일관화**(예 `point_hm0`) — ⚠ **post-processing 스크립트 breaking change**
- **wavemaker 입력변수 rename**(예 `wavemaker_wvmfile`, 레거시 호환 변수 유지)
- **QC testbed v2.0** — 검증테스트 **2배 증가**([validation 노트](sfincs-v2.4.0-galibier-validation-testbed.md))
- **HydroMT-SFINCS v2.0.0**(Python setup tool 신버전 권장)

## Changelog — 버그픽스 (§1.2.3)

- 공식 v2.4.0 변경 기록은 storecumprcp=0의 Curve Number 문제를 수정했다고 기록한다. `docs/developments.rst:27` `* Issue in SFINCS v2.3.0 mt Faber Release regarding Curve Number infiltration if storecumprcp = 0 (default), then infiltration is not processed correctly and can result to unrealistic results! Simple solution for now: put storecumprcp = 1 when using this infiltration option. This issue is fixed in the 2026.01 Galibier Release!`; `docs/developments.rst:63` `* Fixed bug with Curve Number infiltration if storecumprcp = 0 (default).`
  현재 코드의 판정은 [Curve Number 수정 이력과 현재 코드](#curve-number-수정-이력과-현재-코드)를 따른다. `sfincs_meteo.f90:1321` `if (store_cumulative_precipitation) then`; `sfincs_meteo.f90:1534` `if (store_cumulative_precipitation) then`; `sfincs_infiltration.f90:709` `if (store_cumulative_precipitation) then`
- wavemaker 북쪽 강제 파 버그
- regular grid 구 binary sbgfile 버그(레거시)
- Neumann 경계(`msk=6`) 특정케이스 버그
- **SnapWave IG source term** 구현 버그(Yasmine Elmessary)

## Curve Number 수정 이력과 현재 코드

공식 v2.4.0 변경 기록은 storecumprcp=0의 Curve Number 문제를 수정했다고 기록한다. `docs/developments.rst:27` `* Issue in SFINCS v2.3.0 mt Faber Release regarding Curve Number infiltration if storecumprcp = 0 (default), then infiltration is not processed correctly and can result to unrealistic results! Simple solution for now: put storecumprcp = 1 when using this infiltration option. This issue is fixed in the 2026.01 Galibier Release!`; `docs/developments.rst:63` `* Fixed bug with Curve Number infiltration if storecumprcp = 0 (default).`
현재 코드의 CN A 식은 cumprcp와 cuminf를 사용한다. `sfincs_infiltration.f90:689` `if (cumprcp(nm) > sfacinf * qinffield(nm)) then ! qinffield is S`; `sfincs_infiltration.f90:693` `Qq  = (cumprcp(nm) - sfacinf * qinffield(nm))**2 / (cumprcp(nm) + (1.0 - sfacinf) * qinffield(nm))  ! cumulative runoff in m`; `sfincs_infiltration.f90:695` `qinfmap(nm) = (I - cuminf(nm)) / dt           ! infiltration in m/s`
현재 코드는 store_cumulative_precipitation이 true일 때만 두 누적량을 갱신한다. `sfincs_meteo.f90:1321` `if (store_cumulative_precipitation) then`; `sfincs_meteo.f90:1323` `cumprcp(nm) = cumprcp(nm) + prcp(nm) * dt`; `sfincs_meteo.f90:1534` `if (store_cumulative_precipitation) then`; `sfincs_meteo.f90:1535` `cumprcp(nm) = cumprcp(nm) + ptmp * dt`; `sfincs_infiltration.f90:709` `if (store_cumulative_precipitation) then`; `sfincs_infiltration.f90:713` `cuminf(nm) = cuminf(nm) + qinfmap(nm) * dt`
현재 코드에서 출력 플래그 의존성의 제거를 확인하지 못했다. `sfincs_input.f90:280` `call read_int_input(500,'storecumprcp',storecumprcp,0)`; `sfincs_input.f90:511` `store_cumulative_precipitation = .false.`; `sfincs_input.f90:512` `if (storecumprcp==1) then`; `sfincs_input.f90:513` `store_cumulative_precipitation = .true.`; `sfincs_meteo.f90:1321` `if (store_cumulative_precipitation) then`; `sfincs_meteo.f90:1534` `if (store_cumulative_precipitation) then`; `sfincs_infiltration.f90:709` `if (store_cumulative_precipitation) then`
문서의 수정 이력과 현재 코드의 상태를 구분한다. `docs/developments.rst:27` `* Issue in SFINCS v2.3.0 mt Faber Release regarding Curve Number infiltration if storecumprcp = 0 (default), then infiltration is not processed correctly and can result to unrealistic results! Simple solution for now: put storecumprcp = 1 when using this infiltration option. This issue is fixed in the 2026.01 Galibier Release!`; `docs/developments.rst:63` `* Fixed bug with Curve Number infiltration if storecumprcp = 0 (default).`; `sfincs_meteo.f90:1321` `if (store_cumulative_precipitation) then`; `sfincs_meteo.f90:1534` `if (store_cumulative_precipitation) then`; `sfincs_infiltration.f90:709` `if (store_cumulative_precipitation) then`
실제 영향과 수정 반영 판은 별도 증거가 필요하다. `docs/developments.rst:27` `* Issue in SFINCS v2.3.0 mt Faber Release regarding Curve Number infiltration if storecumprcp = 0 (default), then infiltration is not processed correctly and can result to unrealistic results! Simple solution for now: put storecumprcp = 1 when using this infiltration option. This issue is fixed in the 2026.01 Galibier Release!`; `docs/developments.rst:63` `* Fixed bug with Curve Number infiltration if storecumprcp = 0 (default).`; `sfincs_meteo.f90:1321` `if (store_cumulative_precipitation) then`; `sfincs_meteo.f90:1534` `if (store_cumulative_precipitation) then`; `sfincs_infiltration.f90:709` `if (store_cumulative_precipitation) then`
판정: 정적 판독으로 확인, 실행으로는 확인하지 않음. `docs/developments.rst:27` `* Issue in SFINCS v2.3.0 mt Faber Release regarding Curve Number infiltration if storecumprcp = 0 (default), then infiltration is not processed correctly and can result to unrealistic results! Simple solution for now: put storecumprcp = 1 when using this infiltration option. This issue is fixed in the 2026.01 Galibier Release!`; `docs/developments.rst:63` `* Fixed bug with Curve Number infiltration if storecumprcp = 0 (default).`; `sfincs_input.f90:280` `call read_int_input(500,'storecumprcp',storecumprcp,0)`; `sfincs_input.f90:511` `store_cumulative_precipitation = .false.`; `sfincs_input.f90:512` `if (storecumprcp==1) then`; `sfincs_input.f90:513` `store_cumulative_precipitation = .true.`; `sfincs_meteo.f90:1321` `if (store_cumulative_precipitation) then`; `sfincs_meteo.f90:1323` `cumprcp(nm) = cumprcp(nm) + prcp(nm) * dt`; `sfincs_meteo.f90:1534` `if (store_cumulative_precipitation) then`; `sfincs_meteo.f90:1535` `cumprcp(nm) = cumprcp(nm) + ptmp * dt`; `sfincs_infiltration.f90:689` `if (cumprcp(nm) > sfacinf * qinffield(nm)) then ! qinffield is S`; `sfincs_infiltration.f90:693` `Qq  = (cumprcp(nm) - sfacinf * qinffield(nm))**2 / (cumprcp(nm) + (1.0 - sfacinf) * qinffield(nm))  ! cumulative runoff in m`; `sfincs_infiltration.f90:695` `qinfmap(nm) = (I - cuminf(nm)) / dt           ! infiltration in m/s`; `sfincs_infiltration.f90:709` `if (store_cumulative_precipitation) then`; `sfincs_infiltration.f90:713` `cuminf(nm) = cuminf(nm) + qinfmap(nm) * dt`; `sfincs_infiltration.f90:143` `cuminf = 0.0`; `sfincs_infiltration.f90:140` `cumprcp = 0.0`

## Alpha/beta (고급, Deltares 문의 필요)

- 급경사 SnapWave **쇄파·파유발 setup** 개선
- SnapWave **식생 효과**([Wu 식생 검증케이스](sfincs-v2.4.0-galibier-validation-testbed.md))
- wavemaker incident wave energy 강제 옵션
- "hyper-fast but scandalous" **bathtub** 옵션
- **GPU 구현 개선**

## Known issues (§1.2.2)

- **restartfile 호환**: 2023 Cauberg 이전 restartfile 은 col d'Eze·mt.Faber·이후 릴리스서 재생성 필요
- **BMI**: SFINCS BMI = XMI(BMI+확장, Hughes 2022, `xmipy`)와 최신이나 **CSDMS standard BMI 2.0 미반영**
- 공식 v2.4.0 변경 기록은 storecumprcp=0의 Curve Number 문제를 수정했다고 기록한다. `docs/developments.rst:27` `* Issue in SFINCS v2.3.0 mt Faber Release regarding Curve Number infiltration if storecumprcp = 0 (default), then infiltration is not processed correctly and can result to unrealistic results! Simple solution for now: put storecumprcp = 1 when using this infiltration option. This issue is fixed in the 2026.01 Galibier Release!`; `docs/developments.rst:63` `* Fixed bug with Curve Number infiltration if storecumprcp = 0 (default).`
  현재 코드에서 출력 플래그 의존성의 제거를 확인하지 못했다. `sfincs_input.f90:280` `call read_int_input(500,'storecumprcp',storecumprcp,0)`; `sfincs_input.f90:511` `store_cumulative_precipitation = .false.`; `sfincs_input.f90:512` `if (storecumprcp==1) then`; `sfincs_input.f90:513` `store_cumulative_precipitation = .true.`; `sfincs_meteo.f90:1321` `if (store_cumulative_precipitation) then`; `sfincs_meteo.f90:1534` `if (store_cumulative_precipitation) then`; `sfincs_infiltration.f90:709` `if (store_cumulative_precipitation) then`
  판정: 정적 판독으로 확인, 실행으로는 확인하지 않음. `sfincs_meteo.f90:1321` `if (store_cumulative_precipitation) then`; `sfincs_meteo.f90:1534` `if (store_cumulative_precipitation) then`; `sfincs_infiltration.f90:689` `if (cumprcp(nm) > sfacinf * qinffield(nm)) then ! qinffield is S`; `sfincs_infiltration.f90:693` `Qq  = (cumprcp(nm) - sfacinf * qinffield(nm))**2 / (cumprcp(nm) + (1.0 - sfacinf) * qinffield(nm))  ! cumulative runoff in m`; `sfincs_infiltration.f90:695` `qinfmap(nm) = (I - cuminf(nm)) / dt           ! infiltration in m/s`; `sfincs_infiltration.f90:709` `if (store_cumulative_precipitation) then`

## 개발 상태 (§1.2.1)

2026-06 기준 development status 표(Fig 1.10-1.11) — SFINCS 코어 + HydroMT-SFINCS(Python) 별 GA(General Available) 기능 녹색표시. 2017년부터 지속 개발.

> 핵심: Galibier = mt.Faber + 분석/QGIS/wave 옵션 + 버그픽스 5 + testbed 2배 + HydroMT v2.0. **소스 미동봉**(GitHub 태그)·**his.nc 변수명 breaking change** 주의. 검증 → [testbed 노트](sfincs-v2.4.0-galibier-validation-testbed.md).
