# models/ INDEX

| 모델 | 상태 | 도메인 | 격자 |
|---|---|---|---|
| [EFDC](EFDC/) | TBD | 3D 수리·수질·표사 | curvilinear, sigma |
| [ADCIRC](ADCIRC/) | TBD | 2D/3D 조석·해일 | unstructured |
| [XBeach](XBeach/) | TBD | 폭풍 침식·범람 | 직교/곡선 |
| [Delft3D](Delft3D/) | TBD | 3D 수리·파랑·표사 | 구조 또는 비구조 |
| [SWAN](SWAN/) | STABLE+ | 천해 풍파 spectral (위상평균) | 구조/곡선/비구조 |
| [ROMS](ROMS/) | WIP | 3D 해양순환·4D-Var DA | 곡선 직교, terrain-sigma |
| [FUNWAVE](FUNWAVE/) | WIP | 위상해상 fully-nonlinear Boussinesq nearshore (배치 HPC) | 직교, MPI |
| [Celeris](Celeris/) | WIP | GPU 실시간 위상해상 확장 Boussinesq (WebGPU 브라우저) | structured, moving shoreline |
| [CADMAS-SURF](CADMAS-SURF/) | WIP | VOF 수치파동수조 — 자유수면 RANS·내파설계 파력·월파 (CDIT/PARI) | 직교 staggered, porous body |

새 모델 추가: `_template/` 복사 → `<model-name>/`로 이름 변경.

> ⚠️ 본 INDEX 는 stale — SWASH·SFINCS·LISFLOOD-FP 미등록(전수 검수 완료 모델). 전체 모델 추적은 [AUDIT-LEDGER.md](AUDIT-LEDGER.md) §0 대시보드.
