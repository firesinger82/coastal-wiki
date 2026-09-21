# snapshot migration — 미결 항목 (backlog)

DESIGN v2.0 파일럿 라운드(ADCIRC·EFDC·SWAN·ROMS·Celeris·asgs·hydromt·Delft3D·LISFLOOD-FP·SFINCS·XBeach·ShorelineS)에서
**파일럿 범위 밖으로 밀어둔 것**을 한 곳에 모은다. 각 항목은 그때그때 판정을 남겼고, 여기서는 위치와 성격만 가리킨다.
새 파일럿은 이 목록을 다시 열지 않는다 — 별도 작업 단위로 승인받아 착수한다.

## 문서축 (원문 판독 필요)

| 항목 | 위치 | 성격 |
|---|---|---|
| ~~**ShorelineS 공식 매뉴얼 v1.0 발췌**~~ | `doc/ShorelineS_manual_v1.0.pdf` 66쪽 | **✅완료 2026-09-22** — `manual-notes/shorelines-technical-manual-v1.md`(220행). 부수 성과: 매뉴얼 본문↔Appendix B 불일치 3건을 코드로 판정, **`rotfac` 키워드가 회절 루틴에서 무시됨**(`wave_diffraction.m:113`) 확정 |
| XBeach 3 노트 'source revision unknown' 표기 | XBeach notes | 사용자 확정 2026-09-20, 아직 미반영 |

## 코드↔문서 격차 (신규 2026-09-22)

| 항목 | 위치 | 성격 |
|---|---|---|
| ShorelineS `RAY` 수송분기 미문서화 | `transport.m:194` | 매뉴얼 v1.0 §5.1 이 7공식을 문서화하면서 격차가 RAY 하나로 줄었다. upstream 보고 후보 |
| ShorelineS `rotfac` 입력 무효 | `wave_diffraction.m:113` 이 `STRUC.rotfac` 을 무시하고 지역값 0.8 로 덮어씀 | 사용자가 키워드를 줘도 효과 없음. Appendix B 의 1.5 는 사문. upstream 보고 후보 |
| ShorelineS 매뉴얼 `Kw`=1.2 (p49) | 실제 `initialize_defaultvalues.m:193` = 4.2 | 매뉴얼 본문 stale |

## 인용 좌표 (해결 보류)

| 항목 | 건수 | 성격 |
|---|---|---|
| ADCIRC bare line reference | 117 | 파일 미지정 `:NNNN` 형태. `_staging/adcirc-upstream-review/BACKLOG-bare-line-references.md` |
| EFDC·SWAN·ADCIRC unresolved | 44 | ROMS 파일럿에서 '다시 열지 않는다'로 고정한 잔여 |
| EFDC 코드블록 내 인용 | 9 | 스냅샷 bump 후 stale. 코드블록은 excluded ledger 대상이라 자동 수정 안 함 |
| ~~`roms_matlab`~~ | ~~file-line 2 / file-only 12~~ | **✅완료 2026-09-21** — 교집합 0(인용 13건 전부 `tidal_ellipse/`, 해당 디렉터리 무변경) |

## 사전 존재 결함 (마이그레이션이 만든 것이 아님)

| 항목 | 위치 | 성격 |
|---|---|---|
| Delft3D 전칭 과장 2건 | "모든 NetCDF 추적" / "모든 writer 2-pass" | 소스가 뒷받침하지 않는 전칭 단언 |
| Delft3D 범위 초과 인용 3건 | 예: `chknum.f90:66-160` (실제 133줄 파일) | 인용 범위가 파일 길이를 넘음 |
| SWAN coverage-audit 계수 불일치 | `swan-source-coverage-audit.md` | "58 source files" vs 실측 80 / §1.1 "47" vs 열거 51 |
| `efdc_vertical.md:133` | "IINTPG option benchmark" | 처분 미정 |

## 정리 대상

- `~/.cache/coastal-snapshots/` staging clone — 의도적으로 보존 중(게이트 fixture 가 Celeris clone 을 참조한다: `test_reanchor.py:13`). 삭제 시 게이트 fixture 3건이 건너뛰기로 바뀐다.
- ~~Delft3D 롤백 트리 1.4G + `/opt/coastal-snapshots` tar 562M~~ **✅정리 2026-09-21** — `_staging/delft3d-prescan/rollback-cleanup-delft3d.sh`. 표본 200 `--filters` 대조 불일치 0 확인 후 삭제, 약 2.0G 회수. `models/` 의 `.old-*` 자산은 이제 **0건**이다.

## 측정·판정 기준 (2026-09-22 신규)

| 항목 | 위치 | 성격 |
|---|---|---|
| `adcirc-testsuite` 크기 표기 166M vs 실측 8,140M | `models/ADCIRC/manifest.md` | Git LFS 저장소. LFS 실체가 내려받아져 있어 커밋된 포인터와 작업트리가 달라 `git status` 가 **776 파일을 modified** 로 본다(손상 아님). 두 가지가 필요하다 — 크기 측정 기준 통일, **LFS 저장소의 clean-tree 판정 규칙**(현 apply 스크립트의 사전조건은 LFS 저장소에서 통과하지 못한다) |
| ADCIRC manifest 나머지 행 미검증 | 같음 | StormEvents 만 실측 갱신, 나머지는 caveat 으로 표시 |
