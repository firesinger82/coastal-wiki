# models/ INDEX

디렉터리로 존재하는 모델 13개의 진입 링크다. **문서 상태**는 각 모델의 `source-analysis/`·`manual-notes/`·`web-refs/` 노트 frontmatter(README 제외)에서 읽은 인용 상태이며, 전수 감사의 완료 판정이 아니다. 감사·종결 이력은 각 모델 README와 [AUDIT-LEDGER.md](AUDIT-LEDGER.md)에서 별도로 확인한다.

문서 상태 표기:

- `전부 verified` — 작성 노트 전원 `citation_status: verified`
- `초안 혼재` — `draft-unsourced` 노트가 함께 있음
- 갭: `일부 공시`(`has_source_needed: true` 존재) / `갭 없음 표기`(`false`만) / `갭 미감사`(필드 부재 — `false`가 아니라 확인하지 않았다는 뜻)

| 모델 | 문서 상태 | 도메인 | 격자 |
|---|---|---|---|
| [EFDC](EFDC/) | 전부 verified, 갭 미감사 다수(1편만 갭 없음 표기) | 3D 수리·수질·표사 | curvilinear, sigma |
| [ADCIRC](ADCIRC/) | 전부 verified, 갭 일부 공시·미감사 혼재 | 2D/3D 조석·해일 | unstructured |
| [XBeach](XBeach/) | **초안 혼재** — verified 다수 + 2026-09-12 연결 보충 4편 `draft-unsourced`(사람 검토 대기). verified 노트 일부에 AI 정정 `source_correction_human_approval: not-issued` = 기존 verified 이력이 새 승인을 뜻하지 않음. 갭 일부 `false` 표기·나머지 미감사. [모델 목차](XBeach/README.md) | 폭풍 침식·범람 | 직교/곡선 |
| [Delft3D](Delft3D/) | 전부 verified, 갭 미감사 | 3D 수리·파랑·표사 | 구조 또는 비구조 |
| [SWAN](SWAN/) | 전부 verified, 갭 1편 공시·나머지 미감사 | 천해 풍파 spectral (위상평균) | 구조/곡선/비구조 |
| [ROMS](ROMS/) | 전부 verified, 갭 일부 공시·미감사 혼재 | 3D 해양순환·4D-Var DA | 곡선 직교, terrain-sigma |
| [FUNWAVE](FUNWAVE/) | 전부 verified, 갭 미감사 | 위상해상 fully-nonlinear Boussinesq nearshore (배치 HPC) | 직교, MPI |
| [Celeris](Celeris/) | 전부 verified, 갭 미감사 | GPU 실시간 위상해상 확장 Boussinesq (WebGPU 브라우저) | structured, moving shoreline |
| [CADMAS-SURF](CADMAS-SURF/) | 전부 verified, 갭 일부 공시·미감사 혼재 | VOF 수치파동수조 — 자유수면 RANS·내파설계 파력·월파 (CDIT/PARI) | 직교 staggered, porous body |
| [ShorelineS](ShorelineS/) | 전부 verified, 갭 미감사 | free-form one-line 해안선 진화 — 연안표사 경사, 월~세기 (IHE Delft/Deltares, MATLAB) | 벡터 해안선(자유 이동점), 다중 섹션·스핏 |
| [SWASH](SWASH/) | 전부 verified, 갭 미감사 | [모델 README 참조](SWASH/README.md) | [모델 README 참조](SWASH/README.md) |
| [SFINCS](SFINCS/) | 전부 verified, 갭 미감사 | [모델 README 참조](SFINCS/README.md) | [모델 README 참조](SFINCS/README.md) |
| [LISFLOOD-FP](LISFLOOD-FP/) | 전부 verified, 갭 미감사 | [모델 README 참조](LISFLOOD-FP/README.md) | [모델 README 참조](LISFLOOD-FP/README.md) |

SWASH·SFINCS·LISFLOOD-FP는 이 목차에 처음 등록하며, 도메인·격자 서술은 새로 쓰지 않고 각 모델 README로 연결한다.

새 모델 추가: `_template/` 복사 → `<model-name>/`로 이름 변경.

> 상태 출처: 문서 상태 = 노트 frontmatter 스캔([`_staging/wiki-navigation-20260913/model-state-summary.json`](../_staging/wiki-navigation-20260913/model-state-summary.json), 2026-09-13) / 감사 완료 = [AUDIT-LEDGER.md](AUDIT-LEDGER.md) §0 대시보드. 모델별 상세 이력은 루트 [INDEX.md](../INDEX.md) 및 각 모델 README.
