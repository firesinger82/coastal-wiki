# Source snapshot provenance 조사 제안 — 2026-09-19

최종 판정은 Claude가 한다. manifest의 13개 모델 × 29개 저장소를 모두 대조했다. CSV는 대표 29행과 충돌 추가 근거 2행, 총 31행이다. 상태 집계는 저장소별 한 번만 센다. snapshot 채택·갱신 또는 노트 수정 필요성: Claude 판단 필요.

## 방법과 판정 범위

- `current_local_commit`은 입력 `manifest.csv`의 `pinned_commit_sha`만 사용했다. 원격 HEAD·latest release·CURRENT/BEHIND 필드는 provenance 일치 판정에 사용하지 않았다.
- `rg --files`로 `models/**/*.md`(모든 `raw/` 제외), `concepts/**/*.md`, `textbook/notes/**/*.md`를 열거하고 검색했다. 각 모델 README·manifest, frontmatter, `models/AUDIT-LEDGER.md` 포함. 모델 13개 노트 572개, concepts 74개, textbook/notes 30개를 검색했다(모델 공통 색인·템플릿 별도).
- `_staging/`의 build·audit·total-read·crosswalk·ledger·source-index 기록을 검색했다. Markdown 외 JSON/JSONL/CSV/YAML/TXT 기록도 포함했다. 주요 원장은 `_staging/total-read/PROVENANCE.md` 및 `.json`, 모델별 preflight REPORT, 판독·감사 영수증이다. 결과 파일과 현재 snapshot manifest는 과거 provenance 증거로 재사용하지 않았다.
- 검색 패턴: `(?<![\w])[a-f0-9]{7,40}(?![\w])`, `v?숫자.숫자[.숫자]`, `DIMRset`, `Version_`, `roms-4`, `branch`, `clone`, `checkout`, `depth.?1`, `commit`, `audited_ref`, `source snapshot`, `based on`, `verified against`, `스냅샷`, `file:line`, `verification_method`, `notes`, `source`, 날짜. 숫자·파일 SHA-256·claim ID·위키 자체 commit은 모델 commit과 구분했다.
- 26개 Git 저장소에 대해 과거 원장의 full SHA와 입력 pinned SHA가 전부 동일했다. 각 저장소에서 `git -c safe.directory='*' -C <repo> cat-file -e <sha>^{commit}`를 실행하여 26/26 exit 0을 확인했다. shallow clone이지만 이번 조회 실패는 없었다. 동일 SHA이므로 ancestry 검사는 불필요했다. .git 없는 3개에는 상위 위키 저장소를 대신 조회하지 않았다.
- EXPLICIT_MATCH는 해당 판독 코퍼스의 명시적 commit 기준점이 현재 local commit과 일치한다는 뜻이다. 이를 모든 노트의 최초 작성 SHA 또는 dirty 작업 트리의 바이트 동일성으로 해석하지 않는다. 날짜·branch·release 소개만으로 INDIRECT_MATCH를 부여하지 않았다.
- 버전 문자열은 CSV의 `tag` 타입에 release/version도 포함한다. SVN revision은 `phrase` 또는 그 근거의 `file-line`으로 기록한다. `n-a`는 UNKNOWN인 현재 SHA와 비교 불가이며 불일치(no)가 아니다. confidence는 제안된 증거 분류의 확신 수준이다.

## 저장소 상태 집계

| 상태 | 저장소 수 |
|---|---:|
| EXPLICIT_MATCH | 26 |
| EXPLICIT_DIFFERENT | 0 |
| INDIRECT_MATCH | 0 |
| UNVERIFIED_BASELINE | 1 |
| CONFLICTING_EVIDENCE | 2 |
| NO_PROVENANCE | 0 |

## 모델별 요약

| 모델 | 저장소 수 | 제안 | 근거·한계 |
|---|---:|---|---|
| ADCIRC | 7 | EXPLICIT_MATCH 7 | 2026-07-21 판독 원장 full SHA 일치; testsuite 당시 dirty=776; 최근 조석 보강에도 2개 SHA 명시 |
| CADMAS-SURF | 1 | EXPLICIT_MATCH 1 | 2026-07-21 판독 원장 full SHA 일치 |
| Celeris | 1 | EXPLICIT_MATCH 1 | 2026-07-21 판독 원장 full SHA 일치 |
| Delft3D | 3 | EXPLICIT_MATCH 3 | 2026-07-21 판독 원장 full SHA 일치 |
| EFDC | 2 | EXPLICIT_MATCH 2 | 2026-07-21 판독 원장 full SHA 일치 |
| FUNWAVE | 2 | EXPLICIT_MATCH 2 | 2026-07-21 판독 원장 full SHA 일치; TVD dirty=5, GPU dirty=55 기록; build 포팅 기록 |
| LISFLOOD-FP | 1 | CONFLICTING_EVIDENCE 1 | v8.2 배포본 vs 헤더 8.1.0; 기존 기록에 stale/정정 설명 있음 |
| ROMS | 7 | EXPLICIT_MATCH 7 | 2026-07-21 판독 원장 full SHA 일치 |
| SFINCS | 1 | UNVERIFIED_BASELINE 1 | 과거 Galibier SHA·하위트리 diff 기록 있음; 현재 SHA UNKNOWN |
| SWAN | 1 | EXPLICIT_MATCH 1 | 2026-07-21 판독 원장 full SHA 일치 |
| SWASH | 1 | EXPLICIT_MATCH 1 | 2026-07-21 판독 원장 full SHA 일치 |
| ShorelineS | 1 | EXPLICIT_MATCH 1 | 2026-07-21 판독 원장 full SHA 일치 |
| XBeach | 1 | CONFLICTING_EVIDENCE 1 | SVN export r6155 vs configure.ac 기반 r5583; 서로 다른 revision 단위 가능 |

## 저장소별 SHA·branch 증거

다음은 `_staging/total-read/PROVENANCE.json:2`의 `"generated": "2026-07-21T14:12:52Z"`에 귀속된다. `PROVENANCE.md:3`은 이 원장을 “이 판독이 어느 스냅샷 기준인가”를 특정하는 자료로 설명한다. 전 항목 full SHA는 CSV에 보존했다.

| 모델 / 저장소 | SHA 앞자리 | 원장 줄 | branch | 당시 dirty |
|---|---|---:|---|---:|
| ADCIRC / FigureGen | `d3517e4a5cdb` | 22 | `master` | 0 |
| ADCIRC / StormEvents | `fd0da544dc86` | 54 | `main` | 0 |
| ADCIRC / adcirc | `6037225ce457` | 46 | `main` | 0 |
| ADCIRC / adcirc-testsuite | `72bb573073ea` | 30 | `main` | 776 |
| ADCIRC / adcircpy | `0eb84de6e743` | 62 | `main` | 0 |
| ADCIRC / asgs | `aeb383324bb4` | 14 | `master` | 0 |
| ADCIRC / gahm | `bcbb0fe85709` | 38 | `main` | 0 |
| CADMAS-SURF / Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami | `da7668f97f4e` | 81 | `main` | 0 |
| Celeris / Celeris-WebGPU | `f6fd78bd12af` | 100 | `main` | 0 |
| Delft3D / Delft-FIAT | `a1fd66cf6f27` | 119 | `master` | 0 |
| Delft3D / Delft3D | `513eccdbe249` | 135 | `main` | 0 |
| Delft3D / hydromt_delft3dfm | `1f3dead6972e` | 127 | `main` | 0 |
| EFDC / EFDC-GVC | `68dc93fa04c4` | 154 | `main` | 0 |
| EFDC / EFDCPlus_Stable | `3ed76b6eb126` | 162 | `main` | 0 |
| FUNWAVE / FUNWAVE-GPU | `7f892bad51c1` | 189 | `master` | 55 |
| FUNWAVE / FUNWAVE-TVD | `b4c322e75820` | 181 | `master` | 5 |
| ROMS / WRF | `ee6e88c9e050` | 266 | `Coupling` | 0 |
| ROMS / roms | `32c79b7435ee` | 242 | `develop` | 0 |
| ROMS / roms-jedi | `8b0d52b39fce` | 226 | `develop` | 0 |
| ROMS / roms_eccofs | `0259dbb7b37b` | 250 | `develop` | 0 |
| ROMS / roms_libs | `3b40351dfdb8` | 258 | `main` | 0 |
| ROMS / roms_matlab | `58c108c013b0` | 218 | `main` | 0 |
| ROMS / roms_test | `91433821654e` | 234 | `main` | 0 |
| SWAN / swan | `55441526ec43` | 295 | `main` | 0 |
| SWASH / swash | `a486d5f9ae56` | 314 | `main` | 0 |
| ShorelineS / shorelines | `7bf4481ab84c` | 333 | `master` | 0 |

## 충돌·미확정 사례 원문

### XBeach — CONFLICTING_EVIDENCE 제안

- `models/XBeach/manifest.md:3`:
  > **Acquired**: 2026-05-03

- `models/XBeach/manifest.md:9`:
  > | trunk | https://svn.oss.deltares.nl/repos/xbeach/trunk/ (rev 6155, 2026-04-23) | 100M | svn export (no .svn metadata) |

- `_staging/total-read/PROVENANCE.md:24`:
  > | **XBeach** | SVN **r5583** (`trunk`) | `configure.ac:3` `$Revision: 5583 $` | Deltares **SVN** (git 아님) |

위 문구는 export revision과 파일 내 revision을 각각 가리킬 수 있다. 버전 표기 충돌을 제안하되 서로 다른 snapshot이라는 최종 판정은 하지 않는다. 현재 manifest SHA는 UNKNOWN이다. Claude 판단 필요.

### LISFLOOD-FP — CONFLICTING_EVIDENCE 제안(기존 해소 설명 포함)

- `models/LISFLOOD-FP/manifest.md:9`:
  > | Zenodo **doi:10.5281/zenodo.13121102** | **v8.2** (2024-07-29) | LISFLOOD-FP-v8.2.zip (348 MB, 3170 files) | ~810M (raw extracted, gitignored) |

- `_staging/total-read/PROVENANCE.md:28`:
  > **LISFLOOD-FP `VersionHistory.h:16-19` 는 `8.1.0` 을 선언하지만 실제 코퍼스는 v8.2.**

- `_staging/total-read/PROVENANCE.md:29`:
  > - 그 파일의 이력이 **2020-07 `8.0.1` 에서 끊김**

- `_staging/total-read/PROVENANCE.md:32`:
  > - **함의: 소스 내 버전 문자열을 신뢰하면 오판한다.** 실제로 본 판독 중 1차로 8.1.0 으로 잘못 읽었고, 사용자 지적으로 정정.

8.1.0을 새로운 유효 baseline 후보로 승격하지 않는다. 기존 기록 자체가 v8.2와 stale 헤더의 차이를 정정했다고 명시한다. 이 상태 제안은 서로 다른 버전 문자열의 존재를 보존하는 보수적 분류이며, 미해결 소스 교체를 뜻하지 않는다. 현재 SHA UNKNOWN. Claude 판단 필요.

### SFINCS — UNVERIFIED_BASELINE 제안

- `models/SFINCS/manifest.md:9`:
  > | sfincs | <https://github.com/Deltares/SFINCS> (Deltares, GPL-3.0) | `git clone --depth 1` (main HEAD, 2026-06-18) | ~105M (raw, gitignored) |

- `models/SFINCS/manifest.md:13`:
  > - **재현**: `git clone --depth 1 https://github.com/Deltares/SFINCS.git` → `models/SFINCS/raw/source_code/sfincs/`. depth-1 이라 exact commit sha 미기록(main HEAD 2026-06-18). 정확 버전 필요 시 full clone 후 `git log -1`.

- `models/SFINCS/manifest.md:21`:
  > - **★ provenance 확정 (2026-06-27)**: `git clone --branch v2.4.0_Galibier_release` → **정확 sha `1f1d8286520a8709b2e513854dff18a3616583db`**(2026-06-15, "2026.01 galibier release #341"). 위키 감사 raw clone(`raw/source_code/sfincs/source/src/`)과 **`diff -rq` = 0 차이** → **위키 SFINCS 소스 감사 = v2.4.0 Galibier 소스로 확정**(SnapWave submodule main 2026-06-10 포함).

- `models/SFINCS/README.md:23`:
  >   - ⚠️ v2.4.0 Galibier(2026.01) 릴리스 = **바이너리(exe)+PDF만, 소스 미동봉** — 소스는 GitHub 태그 `v2.4.0_Galibier_release`(GPL-3.0). 위키 raw clone = main HEAD 2026-06-18(태그 미기록)

2026-06-27의 태그/소스 대조는 명시적이지만 현재 manifest에는 Git SHA가 없다. 당시 `source/src/` 비교를 현재 전체 트리의 동일성으로 확장할 수 없다. main 취득 기록과 후속 태그 판정은 시점 차이로 양립 가능하므로 별도의 commit 충돌로 세지 않았다. Claude 판단 필요.

### EXPLICIT_DIFFERENT / INDIRECT_MATCH

해당 제안은 0건이다. release 소개나 clone 날짜만으로 현재 HEAD와 같은지·다른지 추정하지 않았다.

## 추가 증거와 오인 방지

- **ADCIRC / adcirc**: models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:16,28 (2026-09-14 한정 대조); models/ADCIRC/source-analysis/adcirc-topic-map.md:29.
- **ADCIRC / adcirc-testsuite**: models/ADCIRC/source-analysis/adcirc-topic-map.md:31; models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:87.
- **CADMAS-SURF / Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami**: models/CADMAS-SURF/README.md:5 (da7668f, 2026-06-23).
- **EFDC / EFDC-GVC**: models/EFDC/manifest.md:18 (full SHA, 2026-07-04 provenance 절).
- **EFDC / EFDCPlus_Stable**: models/EFDC/manifest.md:17 (full SHA, EFDCPlus_12.4, 2026-07-04).
- **FUNWAVE / FUNWAVE-TVD**: _staging/total-read/model-audit/FUNWAVE/connectivity-preflight/REPORT.md:16; models/FUNWAVE/source-analysis/funwave-build-and-blackwell-port.md:5,18 (2026-06-12, v3.6).
- **FUNWAVE / FUNWAVE-GPU**: _staging/total-read/model-audit/FUNWAVE/connectivity-preflight/REPORT.md:16; models/FUNWAVE/source-analysis/funwave-build-and-blackwell-port.md:5,19,32-44 (2026-06-12, TVD v3.3 기반/로컬 포팅).
- **SWAN / swan**: models/SWAN/source-analysis/swan-setup-solver-swancom1-crosswalk.md:8,151 (v41.51 raw clone); tag-to-SHA 직접 연결 아님.
- **SWASH / swash**: models/SWASH/source-analysis/swash-initialization-grid.md:49 (SwashInit.ftn90:79 VERNUM=12.01); tag-to-SHA 직접 연결 아님.
- **ShorelineS / shorelines**: models/ShorelineS/README.md:16; models/AUDIT-LEDGER.md:353 (full SHA, depth-1 clone 2026-07-17).

- `models/ADCIRC/manifest.md:3,10-18`, `models/ROMS/manifest.md:3,9-15`, `models/Delft3D/manifest.md:3,9-11`: 2026-05-03 취득 기록. 개별 SHA 연결은 후속 7월 원장을 사용했다.
- `models/Celeris/README.md:5,41`: 2026-06-15 Celeris-WebGPU 전수조사 및 JS/WGSL file:line 인용. SHA는 7월 원장으로 보완.
- `models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:7`: v8.2 Zenodo DOI와 `lisflood.cpp:20-27,34,53-169` 직접 판독 기록. `lisflood-fp-mwdg2-adaptive-mra.md:7`은 2026-07-07 및 `lisflood.cpp:444-448` 명시.
- `models/SFINCS/source-analysis/sfincs-architecture-source-map.md:7`: depth-1 clone과 `sfincs_lib.f90:584,618,610` 기록. 줄번호 자체는 commit 식별자가 아니다.
- `models/SWASH/source-analysis/swash-initialization-grid.md:49`: “**버전**: `VERNUM = 12.01` (`SwashInit.ftn90:79`). 이 위키가 v12.01 기준임을 코드가 확정한다.” 과거 노트의 주장만 인용했고 소스를 다시 읽지 않았다.
- `models/ADCIRC/manual-notes/10-github-repo-and-releases.md:29`의 `v56.2.1`, `models/Delft3D/web-refs/delft3d-official-resources.md:103-113`의 `DIMRset_2026.02`/`DIMRset_2026.01`은 release 소개·비교다. local checkout 기준판이라는 선언이 아니므로 다른 SHA 증거로 취급하지 않았다.
- `models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md:132`의 `ADCIRC V45.07`은 실행 식별 문자열, `v56.0.1-21-gbcb79a8`은 testsuite control NetCDF 속성이다. 본문이 현재 solver SHA와 구분하므로 본체 snapshot 충돌로 세지 않았다.
- `models/SWAN/source-analysis/swan-main-boundary-init-sourcemap.md:39`의 change `41.99`, 감사기록 `_staging/audit/L4-2026-08-30-040401.md:69`는 변경 주석이다. 전체 소스 release 41.99라는 명시적 선언이 아니므로 v41.51과 자동 충돌 처리하지 않았다.
- 다수 frontmatter의 `at commit a9618df^`는 modeling-wiki 마이그레이션 원본 commit이다(예: `models/SWAN/source-analysis/swan-whitecapping.md:6`). 모델 소스 commit으로 사용하지 않았다. `concepts/compound-flooding/wetting-drying-cross-model.md:7`의 `4224c40`도 노트 신설 commit이다.
- `_staging/total-read/PROVENANCE.md:15`의 FUNWAVE “dirty:5 — GPU ...” 요약은 JSON의 TVD=5/GPU=55(`PROVENANCE.json:183,191`)와 귀속·수량이 다르다. 원장값을 그대로 보존했으며 commit 차이로 세지 않았다. 로컬 포팅 근거는 build 노트 32–44줄이다. Claude 판단 필요.

## 한계와 무변경 확인

- SHA 일치가 노트별 전체 provenance 완결을 의미하지 않는다. 7월 원장은 판독 코퍼스의 기준점이다. 그 이전 노트, 별도 PR 분석, 외부 매뉴얼 및 후속 노트의 모든 문장을 동일 snapshot에 소급하지 않았다.
- 당시 dirty 수는 수정·미추적 파일의 종류까지 설명하지 않는다. Merkle/file SHA-256 기록은 Git commit과 구분했고 현재 raw에 대한 재해시·내용 검색·diff는 하지 않았다.
- SFINCS/LISFLOOD-FP/XBeach의 현재 commit UNKNOWN은 Git 메타데이터 부재를 뜻한다. 과거 tag·배포본·SVN 기록이 없다는 뜻은 아니다. raw를 읽지 않는 범위에서 현재 트리와 배포본의 동일성은 검증 불가다.
- 네트워크, fetch/pull/checkout, 원본 소스 내용 검색을 사용하지 않았다. read-only Git 객체 존재 조회만 수행했다.
- 조사 시작 시 `models/` diff 없음. 작성 직전에도 `git status --porcelain -- models/` 및 `git diff HEAD --stat -- models/` 출력 없음. 최종 검사에서도 두 명령 출력이 모두 빈 문자열임을 확인했다. 기존 `plan.md` 변경 및 XBeach interfaces 미추적 디렉터리는 그대로 두었다.
- 입력 manifest SHA-256(작성 전·후): `e9ccc1c0b02161e52ff35fafb4ff75ab927b929a6ef0b5e54eb496e8d87578ca`. 이 파일은 입력으로만 열었다. 이번 쓰기는 `provenance.csv`와 `provenance-readme.md` 두 파일뿐이다.

## Claude 최종 판정 (2026-09-19) — `provenance-final.csv`

Codex 제안(EXPLICIT_MATCH 26)은 근거가 거의 전부 `_staging/total-read/PROVENANCE.json`(2026-07-21 판독 코퍼스 기록)이었다. 이는 7-21 시점 로컬 SHA를 증명할 뿐 그 이전 노트의 근거 버전을 증명하지 않으므로, 위키 문서에 SHA가 **직접 명시된** 저장소만 EXPLICIT_MATCH로 두고 나머지는 추가 증거로 INDIRECT_MATCH로 재분류했다.

추가 증거(읽기 전용):
- 26개 git 저장소 모두 `.git/logs/HEAD` 1줄 = clone 후 HEAD 불변. clone일: 대부분 2026-05-03, testsuite 04-12, Celeris·FUNWAVE 06-12, SWASH 06-15, CADMAS 06-23, ShorelineS 07-17.
- 코드 줄(`file:line`)을 인용한 노트 241개 중 frontmatter 날짜가 해당 clone일보다 앞선 노트 0개(날짜 없는 노트는 판정 밖).
- 표본 원문 대조: ADCIRC itpackv.F:551, Delft3D drychk.f90:77-78, ROMS step3d_uv.F:124-125, SWAN mod_xnl4v5.ftn90:4570 — 인용 내용과 현재 코드 일치.

결과: EXPLICIT_MATCH 6 / INDIRECT_MATCH 21 / CONFLICTING_EVIDENCE 2 (XBeach, LISFLOOD-FP) / EXPLICIT_DIFFERENT 0 / UNVERIFIED 0 / NO_PROVENANCE 0. FUNWAVE-GPU는 작업트리 DIRTY(추적 파일 3개 로컬 수정) — 근거 = pinned SHA + 로컬 패치.

### 사용자 확정 (2026-09-20)

provenance status 와 local modification state 를 별도 축으로 분리했다(`provenance-final.csv` 에 `worktree_state`·`reproducibility` 열 추가).

- **XBeach**: CONFLICTING_EVIDENCE 유지. 충돌 근거는 **2026-04-30 노트 3편이 provenance 미확인 별도 source copy 를 참조**한 점 하나다(r6155 vs r5583 은 근거에서 제거 — export rev 와 파일 `$Revision$` 키워드라 층위가 다름). 해당 노트 3편에 *source revision unknown* 표시가 필요하다 — 노트 수정은 별도 작업.
- **LISFLOOD-FP**: CONFLICTING_EVIDENCE 유지. 충돌 근거는 **manifest 의 3,170 files 와 로컬 추출본 1,672 files 불일치**(8.1.0 stale 헤더는 근거에서 제거).
- **FUNWAVE-GPU**: provenance 는 INDIRECT_MATCH 유지. 별도 축으로 `WORKTREE_STATE=MODIFIED`, `REPRODUCIBILITY=BASE_SHA_PLUS_LOCAL_PATCH` — 노트의 정확한 재현에는 base SHA 와 로컬 패치(추적 파일 3개)가 모두 필요하다.
