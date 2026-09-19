# Source snapshot manifest — 2026-09-19

- checked_at (UTC, local inventory completed): 2026-09-19T13:06:36.324445+00:00
- completed_at (UTC): 2026-09-19T13:07:52.797497+00:00
- 범위: models/*/raw/source_code/*/ 직접 하위 디렉터리 전체 및 그 아래 중첩 Git 메타데이터 탐색.
- 결과: 13개 모델, 29개 대상 디렉터리 = Git 저장소 26개 + .git 없는 소스 디렉터리 3개. 중첩 Git 저장소 0개.
- 상태: CURRENT 0 / BEHIND 0 / UNKNOWN 29.

## 방법

manifest.csv의 repository는 해당 모델 raw/source_code 기준 상대 경로다. pinned_commit_sha는 로컬 HEAD 전체 40자 SHA이며 pinned_date는 git show -s --format=%cI HEAD의 committer date다. shallow는 Git의 실제 판독값이다.

모든 Git 명령은 git -c safe.directory='*'를 사용했다. GIT_OPTIONAL_LOCKS=0, GIT_NO_LAZY_FETCH=1, GIT_TERMINAL_PROMPT=0으로 선택적 잠금·자동 객체 가져오기·인증 프롬프트를 억제했다. fetch/checkout/pull/merge/reset/gc, 저장소 설정 변경은 실행하지 않았다.

로컬 명령: symbolic-ref --quiet --short HEAD; rev-parse --verify HEAD; show -s --format=%cI HEAD; rev-parse --is-shallow-repository; config --get remote.origin.url; config --get branch.<branch>.remote 및 .merge. 각 행 evidence에 명령과 로컬 tracking 설정을 기록했다. 로컬 tracking 설정은 현재 원격 브랜치 존재 또는 upstream HEAD의 증거로 사용하지 않았다.

.git 없는 디렉터리는 상위 위키 저장소의 HEAD를 잘못 사용하지 않도록 Git 명령을 실행하지 않았다. Git 메타데이터 부재로 로컬 branch/SHA/date/shallow/origin은 UNKNOWN이다. 파일명·수정 시각으로 commit 또는 origin을 추정하지 않았다.

원격 조회는 아래 한 번만 시도했다. 샌드박스의 DNS 실패를 network blocked로 기록하고 사용자 STOP CONDITION에 따라 이후 모든 원격 조회를 중단했다. GitHub/GitLab API, 다른 도구·네트워크 경로를 통한 재시도는 하지 않았다.

```text
git -c safe.directory='*' ls-remote --symref https://github.com/ccht-ncsu/FigureGen.git HEAD
exit 128: fatal: unable to access 'https://github.com/ccht-ncsu/FigureGen.git/': Could not resolve host: github.com
```

upstream_branch, upstream_head_sha, upstream_head_date, latest_release_or_tag(+date)는 전부 UNKNOWN(reason: network blocked)이다. 원격 branch/HEAD/date/release/tag를 확인하지 못했으므로 CURRENT 또는 BEHIND를 판정하지 않았다. 로컬 remote-tracking ref나 로컬 tag를 최신 원격 값으로 대체하지 않았다. 일반 판정 기준은 동일 HEAD일 때 CURRENT, 로컬 HEAD가 원격 HEAD의 조상임이 확인될 때 BEHIND, 그 밖에는 UNKNOWN이다.

## 모델별 요약

| 모델 | 대상 | Git | .git 없음 | CURRENT | BEHIND | UNKNOWN |
|---|---:|---:|---:|---:|---:|---:|
| ADCIRC | 7 | 7 | 0 | 0 | 0 | 7 |
| CADMAS-SURF | 1 | 1 | 0 | 0 | 0 | 1 |
| Celeris | 1 | 1 | 0 | 0 | 0 | 1 |
| Delft3D | 3 | 3 | 0 | 0 | 0 | 3 |
| EFDC | 2 | 2 | 0 | 0 | 0 | 2 |
| FUNWAVE | 2 | 2 | 0 | 0 | 0 | 2 |
| LISFLOOD-FP | 1 | 0 | 1 | 0 | 0 | 1 |
| ROMS | 7 | 7 | 0 | 0 | 0 | 7 |
| SFINCS | 1 | 0 | 1 | 0 | 0 | 1 |
| SWAN | 1 | 1 | 0 | 0 | 0 | 1 |
| SWASH | 1 | 1 | 0 | 0 | 0 | 1 |
| ShorelineS | 1 | 1 | 0 | 0 | 0 | 1 |
| XBeach | 1 | 0 | 1 | 0 | 0 | 1 |

## UNKNOWN 목록과 사유

모든 행: 원격 정보 network blocked. 아래 .git 없음 표시는 로컬 정보도 확인할 수 없는 추가 사유다.

| 모델 | repository | 사유 |
|---|---|---|
| ADCIRC | FigureGen | network blocked |
| ADCIRC | StormEvents | network blocked |
| ADCIRC | adcirc | network blocked |
| ADCIRC | adcirc-testsuite | network blocked |
| ADCIRC | adcircpy | network blocked |
| ADCIRC | asgs | network blocked |
| ADCIRC | gahm | network blocked |
| CADMAS-SURF | Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami | network blocked |
| Celeris | Celeris-WebGPU | network blocked |
| Delft3D | Delft-FIAT | network blocked |
| Delft3D | Delft3D | network blocked |
| Delft3D | hydromt_delft3dfm | network blocked |
| EFDC | EFDC-GVC | network blocked |
| EFDC | EFDCPlus_Stable | network blocked |
| FUNWAVE | FUNWAVE-GPU | network blocked |
| FUNWAVE | FUNWAVE-TVD | network blocked |
| LISFLOOD-FP | LISFLOOD-FP | network blocked; no Git metadata (.git 없음) |
| ROMS | WRF | network blocked |
| ROMS | roms | network blocked |
| ROMS | roms-jedi | network blocked |
| ROMS | roms_eccofs | network blocked |
| ROMS | roms_libs | network blocked |
| ROMS | roms_matlab | network blocked |
| ROMS | roms_test | network blocked |
| SFINCS | sfincs | network blocked; no Git metadata (.git 없음) |
| SWAN | swan | network blocked |
| SWASH | swash | network blocked |
| ShorelineS | shorelines | network blocked |
| XBeach | trunk | network blocked; no Git metadata (.git 없음) |

## models/ 무변경 검사

- 조사 시작 전 허용 경로에 임시 .check-start marker를 만들었다. 검사 후 marker는 삭제했다. 파일 목록 스냅샷이나 대용량 중간 파일은 저장하지 않았다.
- 조사 전후 find models -newer <marker> -not -path '*/raw/*': 시작 0건, 종료 0건.
- raw Git 저장소 26개의 HEAD를 rev-parse --verify HEAD로 재확인: 불일치 0건.
- 추가 검사: os.walk + lstat로 models/ 전체(raw 및 Git 메타데이터 포함)의 marker 이후 mtime 항목 수만 집계: 0건. 목록은 저장하지 않았다.
- 위 경량 검사에서 변경 징후 없음. 전체 파일 내용 해시 대조는 수행하지 않았으며, HEAD 검사는 미커밋 파일 내용까지 검증하지 않는다.
- 생성 산출물은 허용된 _staging/source-snapshots-20260919/manifest.csv 및 README.md 두 파일뿐이다. models/에 쓰기 작업은 실행하지 않았다.

## 원격 필드 보완 (Claude, 2026-09-19)

Codex 실행 샌드박스에서 DNS가 차단되어(`Could not resolve host`) 원격 항목이 전부 UNKNOWN이었다. 사용자 결정(A안)에 따라 Claude가 원격 필드만 보완했다. 로컬 열(model~origin_url)은 Codex 값을 그대로 유지(보완 전후 동일 확인).

- 방법(읽기 전용): `git ls-remote --symref <origin> HEAD refs/heads/<local_branch>` → upstream HEAD. GitHub: `gh api repos/<o>/<r>/commits/<head>`(날짜), `compare/<pinned>...<head>`(상태: ahead→BEHIND, behind→AHEAD, diverged→DIVERGED), `releases/latest`(없으면 `git ls-remote --tags --sort=-version:refname` 최상위 태그). GitLab(tudelft): `repository/commits/<head>`, `repository/merge_base`, `releases`, `repository/tags`.
- upstream_branch = 로컬 추적 브랜치명(원격 기본 브랜치와 다를 수 있음 — 예: ROMS/WRF `Coupling`).
- 결과: git 저장소 26개 원격 조회 **성공 26 / 실패 0**. 상태 **CURRENT 12 / BEHIND 14 / AHEAD 0 / DIVERGED 0 / UNKNOWN 3**(LISFLOOD-FP, SFINCS, XBeach trunk — `.git` 없음, 원격 미조회).
- models/ 무변경.
