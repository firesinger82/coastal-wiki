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
---

# SFINCS v2.4.0 Galibier 릴리스 델타

> SFINCS v2.4.0 "Galibier"(2026.01) 공식 릴리스 매뉴얼(§1.2 Developments)의 **버전 변경내역·알려진 이슈**. 위키 [SFINCS 소스 감사](../source-analysis/sfincs-architecture-source-map.md)는 GitHub main HEAD(2026-06-18)였으므로 이 노트가 **버전 태그·델타** 보완.

## 버전 정체

- **v2.4.0 "Galibier"** = 'Generating Accurate Large-scale Inundation: Better Insights for Emergency Response' (2026 첫 공식 릴리스, §1.2.3)
- 배포 채널: GitHub `releases/tag/v2.4.0_Galibier_release`(GPL-3.0 소스) · Windows exe(download.deltares.nl/sfincs) · Docker `deltares/sfincs-cpu:sfincs-v2.4.0-Galibier-Release`
- **기반**: 2025.02 **v2.3.0 'mt. Faber'** 전 기능 + 아래 변경. 버전 계보: 2023 Cauberg → v2.2.0 col d'Eze → v2.3.0 mt.Faber → **v2.4.0 Galibier**
- ⚠️ **provenance 갭**: 본 릴리스는 **바이너리(exe)+PDF만, 소스 미동봉**(컴파일 옵션 제공 안 함). 소스는 GitHub 태그 `v2.4.0_Galibier_release`. 위키 raw clone 은 depth-1 **main HEAD 2026-06-18**(태그 미기록) → 정확 버전 대조하려면 `git clone --branch v2.4.0_Galibier_release`. manifest 갱신 권고.

## Changelog — 신규/추가 (§1.2.3)

- **`timestep_analysis=1`**: 타임스텝 제한 변수(`average_required_timestep`·`percentage_limiting_timestep`)를 sfincs_map.nc·화면 출력 → 어느 셀이 전역 Δt 제한하는지 분석
- **Quadtree sfincs_map.nc 직접 QGIS 로드·시각화** 가능
- **`huvmin`**(속도계산 최소수심, `uv=q/max(hu,huvmin)`, 출력·이류용)
- **`snapwave_waveforces_factor`**(=0 시 파력·incident wave setup 끔)
- **`sfincs_his.nc` 파 관련 변수명 일관화**(예 `point_hm0`) — ⚠ **post-processing 스크립트 breaking change**
- **wavemaker 입력변수 rename**(예 `wavemaker_wvmfile`, 레거시 호환 변수 유지)
- **QC testbed v2.0** — 검증테스트 **2배 증가**([validation 노트](sfincs-v2.4.0-galibier-validation-testbed.md))
- **HydroMT-SFINCS v2.0.0**(Python setup tool 신버전 권장)

## Changelog — 버그픽스 (§1.2.3)

- **Curve Number 침투** `storecumprcp=0`(기본) 시 침투 미처리 버그 → **v2.3.0 mt.Faber 영향, Galibier서 수정**(Known issue 였음)
- wavemaker 북쪽 강제 파 버그
- regular grid 구 binary sbgfile 버그(레거시)
- Neumann 경계(`msk=6`) 특정케이스 버그
- **SnapWave IG source term** 구현 버그(Yasmine Elmessary)

## Alpha/beta (고급, Deltares 문의 필요)

- 급경사 SnapWave **쇄파·파유발 setup** 개선
- SnapWave **식생 효과**([Wu 식생 검증케이스](sfincs-v2.4.0-galibier-validation-testbed.md))
- wavemaker incident wave energy 강제 옵션
- "hyper-fast but scandalous" **bathtub** 옵션
- **GPU 구현 개선**

## Known issues (§1.2.2)

- **restartfile 호환**: 2023 Cauberg 이전 restartfile 은 col d'Eze·mt.Faber·이후 릴리스서 재생성 필요
- **BMI**: SFINCS BMI = XMI(BMI+확장, Hughes 2022, `xmipy`)와 최신이나 **CSDMS standard BMI 2.0 미반영**
- ~~Curve Number storecumprcp=0~~ → Galibier서 **수정됨**(위 버그픽스)

## 개발 상태 (§1.2.1)

2026-06 기준 development status 표(Fig 1.10-1.11) — SFINCS 코어 + HydroMT-SFINCS(Python) 별 GA(General Available) 기능 녹색표시. 2017년부터 지속 개발.

> 핵심: Galibier = mt.Faber + 분석/QGIS/wave 옵션 + 버그픽스 5 + testbed 2배 + HydroMT v2.0. **소스 미동봉**(GitHub 태그)·**his.nc 변수명 breaking change** 주의. 검증 → [testbed 노트](sfincs-v2.4.0-galibier-validation-testbed.md).
