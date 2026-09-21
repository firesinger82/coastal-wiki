# snapshot migration — 미결 항목 (backlog)

DESIGN v2.0 파일럿 라운드(ADCIRC·EFDC·SWAN·ROMS·Celeris·asgs·hydromt·Delft3D·LISFLOOD-FP·SFINCS·XBeach·ShorelineS)에서
**파일럿 범위 밖으로 밀어둔 것**을 한 곳에 모은다. 각 항목은 그때그때 판정을 남겼고, 여기서는 위치와 성격만 가리킨다.
새 파일럿은 이 목록을 다시 열지 않는다 — 별도 작업 단위로 승인받아 착수한다.

## 문서축 (원문 판독 필요)

| 항목 | 위치 | 성격 |
|---|---|---|
| **ShorelineS 공식 매뉴얼 v1.0 발췌** | `doc/ShorelineS_manual_v1.0.pdf`(66쪽, upstream `f3ec863` 2026-08-13 신규) | ShorelineS **최초** 공식 매뉴얼. 현재 `manual-notes/` 는 Frontiers 2020 + FAQ 2건뿐이고 매뉴얼 축이 비어 있었다. 66쪽 판독 → `manual-notes/` 신규 노트. AUDIT-LEDGER §14 '문서축 잔여 1' |
| XBeach 3 노트 'source revision unknown' 표기 | XBeach notes | 사용자 확정 2026-09-20, 아직 미반영 |

## 인용 좌표 (해결 보류)

| 항목 | 건수 | 성격 |
|---|---|---|
| ADCIRC bare line reference | 117 | 파일 미지정 `:NNNN` 형태. `_staging/adcirc-upstream-review/BACKLOG-bare-line-references.md` |
| EFDC·SWAN·ADCIRC unresolved | 44 | ROMS 파일럿에서 '다시 열지 않는다'로 고정한 잔여 |
| EFDC 코드블록 내 인용 | 9 | 스냅샷 bump 후 stale. 코드블록은 excluded ledger 대상이라 자동 수정 안 함 |
| `roms_matlab` | file-line 2 / file-only 12 | MIGRATION_CANDIDATE — 아직 파일럿 미실시 |

## 사전 존재 결함 (마이그레이션이 만든 것이 아님)

| 항목 | 위치 | 성격 |
|---|---|---|
| Delft3D 전칭 과장 2건 | "모든 NetCDF 추적" / "모든 writer 2-pass" | 소스가 뒷받침하지 않는 전칭 단언 |
| Delft3D 범위 초과 인용 3건 | 예: `chknum.f90:66-160` (실제 133줄 파일) | 인용 범위가 파일 길이를 넘음 |
| SWAN coverage-audit 계수 불일치 | `swan-source-coverage-audit.md` | "58 source files" vs 실측 80 / §1.1 "47" vs 열거 51 |
| `efdc_vertical.md:133` | "IINTPG option benchmark" | 처분 미정 |

## 정리 대상

- `~/.cache/coastal-snapshots/` staging clone — 의도적으로 보존 중(게이트 fixture 가 Celeris clone 을 참조한다: `test_reanchor.py:13`). 삭제 시 게이트 fixture 3건이 건너뛰기로 바뀐다.
