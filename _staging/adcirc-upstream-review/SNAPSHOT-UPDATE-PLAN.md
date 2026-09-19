# ADCIRC SNAPSHOT UPDATE PLAN — 6037225 → e8b62a70

> 상태: **NEEDS_USER_APPROVAL**. 계획만 작성했고 source·wiki·provenance 어느 것도 수정하지 않았다. 작성 2026-09-20, Claude Opus 5(사용자 승인 예외).
> 기준: [PROJECT_REQUIREMENTS.md](../../PROJECT_REQUIREMENTS.md) models/ 잠금 절차, [CLAUDE.md 역할 분담](../../CLAUDE.md), 파일럿 검증 결과(`claude-final-status.csv`).

- WIKI_BASELINE_OLD = `6037225ce4573efd3c1f8877a5dc908d01c199a8` (2026-04-16, 로컬 clone 2026-05-03, reflog 1줄)
- WIKI_BASELINE_NEW = `e8b62a70db39dbc8875785ee999a2214be75302b` (2026-08-31, upstream `main` tip, 2026-09-19 확인)
- 구간: 14커밋 / 31파일 / +736 −197

## 1. SNAPSHOT_UPDATE_PLAN (SOURCE UPDATE)

| 항목 | 값 |
|---|---|
| 현재 source path | `models/ADCIRC/raw/source_code/adcirc` (root 소유 `dr-xr-xr-x`, shallow clone, gitignore 대상) |
| 준비(staging) 경로 | `~/.cache/coastal-snapshots/adcirc-e8b62a70/` (사용자 소유, 위키 밖 — repo 오염·용량 회피) |
| 백업 경로 | `/opt/coastal-snapshots/adcirc-6037225.tar.zst` (root 소유, sudo 로 생성) |

절차(잠금 절차 준수: 준비 → 승인 → sudo 적용 → 검증 → 재잠금):

1. **현재 commit 검증(사용자 없이 가능, 읽기 전용)**
   `git -c safe.directory='*' -C models/ADCIRC/raw/source_code/adcirc rev-parse HEAD` → `6037225…199a8` 확인, `--no-optional-locks status --porcelain` 으로 추적 파일 수정 0 확인(현재 0).
2. **upstream 확보(staging, 사용자 소유 경로)**
   `git clone --depth 1 --branch main https://github.com/adcirc/adcirc.git ~/.cache/coastal-snapshots/adcirc-e8b62a70` → `git -C … rev-parse HEAD` 가 `e8b62a70…302b` 인지 확인(다르면 중단: upstream tip 이동). `--depth 1` 이라 현재 설치본과 같은 shallow 성격 유지.
3. **설치 전 대조(읽기 전용)**: staging 과 현재 설치본의 파일 목록·내용 해시를 비교해 **변경 파일이 31개뿐인지** 확인(예상 목록은 §2). 예상 밖 파일이 나오면 중단·보고.
4. **사용자 sudo 적용** (§7 명령 블록): 백업 → 설치 → 소유·권한 복구.
5. **적용 후 검증(Claude, 읽기 전용)**: §8 ACCEPTANCE_CRITERIA.
6. **재잠금 확인**: `models/` 이하 root 소유·읽기 전용 상태 복구 확인.

## 2. FILES_EXPECTED_TO_CHANGE (31)

- **ADCIRC 코어 17**: `prep/prep.F`, `prep/presizes.F`, `src/constants.F90`, `src/couple2swan.F`, `src/cstart.F`, `src/global.F`, `src/gwce.F`, `src/hstart.F`, `src/mesh.F`, `src/netcdfio.F90`, `src/nodalattr.F`, `src/owiwind.F`, `src/read_input.F`, `src/timestep.F`, `src/vsmy.F`, `src/weir_boundary.F90`, `src/write_output.F`
- **util 1**: `util/adcircResultsComparison.F90`
- **thirdparty/swan 11**: `SwanBpntlist.ftn90`, `SwanCompUnstruc.ftn90`, `SwanGriddata.ftn90`, `SwanReadADCGrid.ftn90`, `SwanVTKPDataSets.ftn90`, `swanout2.ftn`, `swanparll.ftn`, `swanpre1.ftn`, `swanpre2.ftn`, `swmod1.ftn`, `swmod2.ftn`
- **메타 2**: `CITATION.cff`(신규), `README.md`
- 삭제·rename 없음(전부 modified, CITATION.cff 만 added).

## 3. WIKI_UPDATE_PLAN (UPDATE_REQUIRED 2건)

### 3.1 `models/ADCIRC/source-analysis/adcirc-swan-coupling.md`

| 항목 | 내용 |
|---|---|
| 현재 서술 | 176행 `## SWAN Temporal Controls (PR #498, phase 1 of 2)`, 178행 "PR #498 (**OPEN**, branch `Spatial-and-Temporal-Controls`, +274 −30, 17 files)"; 19행 `couple2swan.F:67-1236`; 54행 "interpolation midpoint used for time-centering (`couple2swan.F:1212-1215`)" |
| upstream 사실 | 커밋 `976fc5b6cafb`("Adding SWAN temporal controls", 17 파일)가 `main` 에 포함 — 새 baseline 에서는 OPEN PR 이 아니라 반영된 코드. `couple2swan.F` hunk `@@ -1212,7 +1241,55 @@`: `SwanTimeStep` 이 `[1, SWAN_MTC]` 일 때만 `SWMAIN` 호출, 그 밖에는 출력값(`Swan_*Out`)과 radiation stress 배열을 초기화·이월 |
| 근거 | commit `976fc5b6cafb`; `patches/src__couple2swan.F.patch` hunk 5(그 외 4개 hunk: 954, 963, 1079, 1104) |
| 최소 수정 | ① 제목·본문의 "PR #498 (OPEN)" → "upstream `main` 반영(커밋 `976fc5b6`), phase 2(spatial controls)는 미반영" ② 54행 인용 `couple2swan.F:1212-1215` → 새 스냅샷 기준 위치로 교체(현재 인용 구간은 변경 hunk 내부 — 새 줄 번호는 적용 후 실측) ③ 19행 범위 인용 `67-1236` → 새 파일 길이에 맞게 실측 후 조정 ④ frontmatter 에 새 baseline 재검증 기록(§5) |
| 다른 부분 영향 | 같은 노트의 PR #498 요약(sentinel·fallback 서술)이 merge 된 코드와 일치하는지 §4 절차로 재확인 필요. `models/ADCIRC/README.md`·`AUDIT-LEDGER.md` 의 "PR #498 OPEN" 요약 문구도 같은 사실을 인용 → 동반 수정 후보(별도 확인) |

### 3.2 `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md`

| 항목 | 내용 |
|---|---|
| 현재 서술 | 21행 `## 1. Attribute 카탈로그 (nodalattr.F:636-686)` — 16 attribute 카탈로그에 `swan_local_control` 없음 |
| upstream 사실 | `976fc5b6` 가 nodal attribute `swan_local_control` 추가. 새 파일에서 선언 주석 89행, `CASE("swan_local_control")` 분기 669·814·1092·1233·1401행(읽기·XDMF·기본값·초기화 경로) |
| 근거 | `patches/src__nodalattr.F.patch` (26 hunk), 매핑: 기존 636→657, 686→709 |
| 최소 수정 | ① 카탈로그에 `swan_local_control` 1행 추가(용도는 커밋 메시지·코드 근거 범위에서만 서술: SWAN 계산을 수행할 영역 지정용 nodal attribute) ② 절 제목의 `nodalattr.F:636-686` → `657-709`(적용 후 실측 확인) ③ frontmatter 재검증 기록 |
| 다른 부분 영향 | "16 attribute" 개수를 인용하는 다른 노트가 있는지 확인(현재 grep 기준 이 노트 내부에 한정). ADCIRC README 의 nodal attribute 요약은 개수 서술 없음 |

※ 두 노트 모두 `citation_status` 는 유지하되, 새 주장에는 새 baseline 근거(`file:line` + 커밋)를 붙인다. 과거 사람 승인(HG)은 새 주장에 승계하지 않는다(CONVENTIONS §2).

## 4. REVIEW_ONLY_VALIDATION_PLAN (27개 노트, 기계 검사)

전체 재독 금지. 새 스냅샷 설치 후 스크립트 1회 실행으로 참조만 검사한다.

입력: `NOTE_REFERENCES.csv`(파일 809 / 파일:줄 394 / 심볼 997 중 변경 파일 관련분), `compare.json` 의 hunk 매핑.

| 검사 | 방법 | 판정 |
|---|---|---|
| 파일 존재 | 새 트리에서 경로 존재 확인 | 없으면 UPDATE_REQUIRED 승격 |
| 줄 이동 | baseline 줄 → 새 줄 매핑(hunk delta). 매핑된 줄의 **내용 문자열이 baseline 과 동일**한지 대조 | 동일 + 이동 ⇒ `LINE_REFERENCE_UPDATE` / 동일 + 이동 없음 ⇒ `NO_CHANGE` |
| 변경 구간 내부 | 인용이 hunk 내부(매핑 불가) | 내용 대조 후 의미 변화면 `UPDATE_REQUIRED` 승격, 서식·주석뿐이면 `LINE_REFERENCE_UPDATE` |
| 심볼 존재 | 새 트리에서 `rg -n '\bSYMBOL\b'` 존재 확인 | 사라졌으면 UPDATE_REQUIRED 승격 |

산출물: `review-only-validation.csv`(note, ref, old_line, new_line, content_match, verdict). 기술 서술이 영향받지 않으면 본문은 고치지 않고 줄 번호만 고친다. 승격 건은 즉시 보고(사용자 승인 전 본문 수정 금지).

## 5. PROVENANCE_UPDATE_PLAN

두 축을 **분리**해 기록한다. 과거 provenance 를 새 SHA 로 소급 변경하지 않는다.

- `historical_source_provenance` = `6037225…199a8` — 그 노트가 실제로 보고 작성·검증된 스냅샷. **불변**.
- `current_validated_against` = `e8b62a70…302b` — 새 스냅샷 기준으로 **실제 재검증·수정된 경우에만** 기록.

| 대상 | 기록 위치 | 값 |
|---|---|---|
| 저장소 수준 | `models/ADCIRC/manifest.md`(sudo 필요) + `_staging/source-snapshots-20260919/provenance-final.csv` | `wiki_baseline` 를 두 열(historical / current_validated)로 분리 |
| UPDATE_REQUIRED 2건 | 각 노트 frontmatter | `current_validated_against: e8b62a70` + `verification_date`·`verification_method`(새 커밋·hunk 근거) |
| LINE_REFERENCE_UPDATE 만 발생한 노트 | 노트 본문 줄 번호만 갱신 | `current_validated_against: e8b62a70 (line refs only)` — 기술 서술 재검증은 하지 않았음을 명시 |
| NO_ACTION 35건 | 변경 없음 | 두 축 모두 그대로(historical 만 유지) |

## 6. ROLLBACK_PLAN

1. 적용 전 `/opt/coastal-snapshots/adcirc-6037225.tar.zst`(root 소유) 를 만든다 — 현재 설치본 **전체**(.git 포함, 추적 외 파일 포함).
2. 되돌릴 때: 설치본 삭제 → tar 복원 → 소유·권한 복구(§7 rollback 블록) → `rev-parse HEAD` 가 `6037225…` 인지, 파일 해시가 백업과 일치하는지 확인.
3. 위키 측 rollback 은 git: 이 작업의 커밋을 `git revert`(노트 수정은 모두 단일 커밋으로 묶어 revert 가능하게 한다).
4. 백업 보존 기간: 새 baseline 으로 ACCEPTANCE 통과 + 1주 후 사용자 판단으로 삭제.

## 7. SUDO_COMMANDS_REQUIRED (사용자 실행, 승인 후)

```bash
set -euo pipefail
SRC=~/.cache/coastal-snapshots/adcirc-e8b62a70          # 준비된 새 스냅샷(사용자 소유)
DST=~/coastal-wiki/models/ADCIRC/raw/source_code/adcirc  # 설치 위치(root, 읽기 전용)

# (1) 백업
sudo mkdir -p /opt/coastal-snapshots
sudo tar --zstd -cf /opt/coastal-snapshots/adcirc-6037225.tar.zst -C "$(dirname "$DST")" adcirc
sudo test -s /opt/coastal-snapshots/adcirc-6037225.tar.zst

# (2) 설치 (교체)
sudo rm -rf "$DST.old" && sudo mv "$DST" "$DST.old"
sudo cp -a "$SRC" "$DST"

# (3) 소유·권한 복구 = 재잠금
sudo chown -R root:root "$DST"
sudo chmod -R a-w "$DST"

# (4) 즉시 확인
sudo -u "$USER" git -c safe.directory='*' -C "$DST" rev-parse HEAD   # e8b62a70db39dbc8875785ee999a2214be75302b
stat -c '%A %U' "$DST"                                               # dr-xr-xr-x root

# (5) 검증 통과 후에만 이전 트리 제거
# sudo rm -rf "$DST.old"
```

rollback:
```bash
sudo rm -rf "$DST" && sudo tar --zstd -xf /opt/coastal-snapshots/adcirc-6037225.tar.zst -C "$(dirname "$DST")"
sudo chown -R root:root "$DST" && sudo chmod -R a-w "$DST"
git -c safe.directory='*' -C "$DST" rev-parse HEAD   # 6037225ce4573efd3c1f8877a5dc908d01c199a8
```

## 8. ACCEPTANCE_CRITERIA

| # | 기준 | 확인 방법 |
|---|---|---|
| 1 | `models/ADCIRC/raw/source_code/adcirc` HEAD = `e8b62a70…302b` | `git rev-parse HEAD` |
| 2 | staging ↔ 설치본 source hash 일치 | 두 트리의 `find -type f` 목록 + sha256 대조(.git 제외) 0 불일치 |
| 3 | 예상 밖 변경 없음 | 설치 전후 트리 비교 결과가 §2 의 31파일과 정확히 일치, 추적 파일 로컬 수정 0 |
| 4 | UPDATE_REQUIRED 2건 수정 완료 | 두 노트의 서술·인용이 새 스냅샷 근거와 일치(Claude 재대조) |
| 5 | REVIEW_ONLY 27건 검사 완료 | `review-only-validation.csv` 전 행 판정, 승격 건 보고·처리 |
| 6 | NO_ACTION 35건 무수정 | `git diff --stat` 에 해당 파일 없음 |
| 7 | 위키 검증 통과 | `tools/validate-all.sh` OK, G8e 탐지 0 |
| 8 | provenance 갱신 | manifest·provenance-final.csv 의 historical / current_validated 두 축 기록 |
| 9 | rollback 가능 | 백업 tar 존재·해제 시험(별도 임시 경로에서 목록 확인) |
| 10 | 잠금 복구 | `models/` 이하 root 소유·읽기 전용 |

## 9. 범용화 메모

이번 절차(diff → reference intersection → semantic verification)는 Delft3D·ROMS·SWAN 등 BEHIND 13개 저장소에 그대로 적용 가능하다. 다만 ADCIRC 는 14커밋이라 GitHub compare 1회로 끝났고, Delft3D(+1,771) 처럼 큰 구간은 파일 단위 compare·필터가 먼저 필요하다. 파일럿 종료 후 별도 결정.
