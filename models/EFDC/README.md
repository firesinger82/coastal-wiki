# models/EFDC

> **Canonical source**: 이 디렉토리(`models/EFDC/`)가 EFDC 모델의 구현·메커닉에 대한 진실의 원천.

## 정체 카드

- **이름**: EFDC (Environmental Fluid Dynamics Code)
- **저자/관리주체**: 원본 — John Hamrick (VIMS, 1992~). 현 분기 다수.
- **본 위키 보유 분기**:
  - **EFDCPlus_Stable** (DSI EFDC+) — `raw/source_code/EFDCPlus_Stable/` (CMake 빌드, [ReadMe.md](raw/source_code/EFDCPlus_Stable/ReadMe.md))
  - **EFDC-GVC** — `raw/source_code/EFDC-GVC/` (별도 분기)
- **라이선스**: EFDC+ Stable — GPL-3.0 (DSI LLC). EFDC-GVC 별도 확인.
- **공식 사이트**: [DSI EFDC+ Modeling System](https://www.dsi-llc.com/efdc-modeling-system/), GitHub [dsi-llc/EFDC_Plus](https://github.com/dsi-llc/EFDC_Plus)
- **공식 메뉴얼**: `raw/manuals/pdfs/` 6 PDFs:
  - `EFDC_Manual.pdf` (general user manual)
  - `EFDC_Theory_Document_Ver_12.pdf` (이론서)
  - `EFDC_Implementation_Guide.pdf`
  - `EFDC+_Propwash_WhitePaper.pdf` (propeller wash)
  - `EFDC_Training_Overview.pdf`
  - (textbook 매니페스트 `efdc-general`, `efdc-sed-trans-2003` source_id — [`textbook/sources.yml`](../../textbook/sources.yml))
- **사용 도메인**: 3D hydro·water quality·sediment·temperature·salinity·biogeochemistry
- **격자**: curvilinear orthogonal horizontal + sigma vertical layer
- **수치 기법**: ADI (Alternating Direction Implicit) hydro core + MPI parallel decomposition

## 하위 디렉토리 현황

| 경로 | 노트 수 | 상태 | 비고 |
|---|---:|---|---|
| `source-analysis/` | 38 verified | **종결 2026-07-11** (AUDIT-LEDGER §6) | hydro core·external PCG·**internal 전단솔버(efdc_internal_shear_caluvw, 2026-07-11 = 마지막 코어 갭)**·transport·turbulence·SedTran/SEDZLJ 양 분기·diagenesis·RPEM·heat/ice·surface forcing·baroclinic EOS·bottom friction·WQ·boundary·wetdry·MPI·GVC legacy 등. 실측 2026-07-11 (stale 19→38 정정) |
| `manual-notes/` | 9 verified | **Theory Ch-series 소진** | overview(6 manuals 인덱스)·user-manual-r850·theory-doc-v12 + **Ch2 수력·Ch5 온도·Ch6 유사 cross-walk**·implementation-guide·sediment-theory-2003(Tetra Tech legacy)·Training/Grid. **implementation-guide·user-manual-r850에 v12.4 소스 드리프트 ⚠️ 주석 11항 (2026-07 감사)**. 실측 2026-07-11 (stale 4→9 정정) |
| `web-refs/` | 1 verified | **신설 2026-05-24** | efdc-official-resources.md — DSI LLC·eemodelingsystem.com·GitHub dsi-llc/EFDC_Plus·핵심 논문 (Hamrick 1992-96·Park 1995·Ziegler-Lick·James 2010) |
| `raw/` | 726 .md + 6 pdf + 257 fortran (2.2 GB) | archive | EFDCPlus_Stable + EFDC-GVC 두 분기 |

## 본 위키에서의 핵심 활용

- [`concepts/sediment-transport/06-model-application.md`](../../concepts/sediment-transport/06-model-application.md) — EFDC SedTran-Original (ISTRAN=6/7 CALSED/CALSND) vs SEDZLJ unified multi-bed-layer (ssedtox.f90 dispatch)
- [`concepts/sediment-transport/`](../../concepts/sediment-transport/) — Van Rijn + Soulsby 정형 + EFDC 구현 비교
- `source-analysis/efdc_sediment.md` — codex source-code 직접 분석 (canonical reference)
- (예정) 축산항 등 EFDC 운영 사례 → 바이블 검증 통과 시 `experience/` 로 카테고리화 (canonical 미수록, source-needed)

## 작성 우선순위 (남은 작업)

1. ✅ **M-C 1차**: `manual-notes/` 4 노트 (overview + r850 + v12 + 2003) — DONE 2026-05-24
2. **M-C 2차**: Theory v12 챕터별 deep notes (Ch 2 hydro·Ch 5 temperature·Ch 6 sediment) + r850 §1.3.1 Primary Run Control 51p input card family + SedTran↔SEDZLJ algorithm cross-walk
3. **M-E**: `web-refs/` — DSI 사이트·EFDC+ 릴리스·핵심 논문 (Hamrick 1992 등)
4. 추가 source-analysis: ssedtox.f90 dispatch 상세, MPI decomposition 운영 매뉴얼
