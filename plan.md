# coastal-wiki 초기 구조 결정 기록

작성: 2026-05-21
작성자: Claude Opus 4.7 (1M context) + 사용자 합의

## 목적

연안공학 도메인 지식의 **객관 레이어**를 단일 writer 위키로 관리. `D:\Study\textbook` 교과서 자료와 EFDC/ADCIRC/XBeach/Delft3D 모델 자료를 통합해 도메인 개념 중심 구조로 정리. 개인 경험은 객관화 검증 통과 후 별도 레이어로 추가.

## 결정사항

### 1. 위치: `~/coastal-wiki` (WSL2 ext4)

- 초기에 `D:\coastal-wiki`(=`/mnt/d/coastal-wiki`)로 생성했으나 2026-05-21 WSL ext4(`/home/firesinger/coastal-wiki`)로 이전.
- 이유: I/O 성능 (git/grep 5~10배), AI 주 작성자 워크플로 적합. Windows 앱(Obsidian 등)은 `\\wsl$\Ubuntu\home\firesinger\coastal-wiki`로 접근.
- 대안 검토:
  - (A) `/mnt/d/coastal-wiki` 유지 — 거부. 9P 프로토콜 오버헤드 + AI 워크플로 효율 손실.
  - (B) modeling-wiki 안에 신규 디렉토리 — 거부. 객관/경험 축 분리 흐려짐.
  - (C) modeling-wiki를 coastal-wiki/experience/로 이전 — 보류. 객관 레이어 자리 잡은 후 결정.

### 2. 구조: concepts 중심, models 부축

```
coastal-wiki/
├── concepts/                # 1차 축: 도메인 개념
│   └── <topic>/
│       ├── 01-concept.md
│       ├── 02-theory.md
│       ├── 03-analysis-methods.md
│       ├── 04-code-and-tools.md
│       ├── 05-examples.md
│       └── 06-model-application.md
├── models/                  # 2차 축: 모델 객관 자료
│   └── <model>/
│       ├── source-analysis/
│       ├── manual-notes/
│       └── web-refs/
├── textbook/                # D:\Study\textbook 통합 노트
├── examples/                # 통합 실습
└── experience/              # 검증 통과 경험 (지금 비움)
```

- 이유: 사용자 명시 — "조석이면 조석에 대한 개념·일반론·분석방법·코드까지 쫘악 정리되고 이걸 기반으로 예제 학습도 가능하고 실제 모델 적용까지 이어지게". 도메인 우선, 모델은 적용 단계.

### 3. textbook 통합: 원본은 D:\Study\textbook 유지, wiki는 노트만

- 이유: PDF는 git에 부담 (LFS 도입 회피). 교과서 자료는 변경 없음 → 원본 위치 안정.
- 방식: `textbook/notes/<topic>-<source_id>-chN.md` 형식으로 챕터별 발췌. raw 파일명·Windows 경로 직접 인용 **금지** — 안정적 `source_id`(예: `holthuijsen2007`) 페어 사용. 매니페스트는 `textbook/sources.yml`.
- 갱신 규칙은 [G2](#g2-textbook-매니페스트--인용-안정화)에서 상세.

### 4. 파일·디렉토리 명: 영문, 본문: 한·영 자유

- 이유: git/cross-PC 안전 (한글 디렉토리는 Windows/WSL/Linux 간 인코딩 이슈 가능성).

### 5. 객관-경험 분리

- `concepts/`, `models/`에는 "내가 해보니" 화법 금지.
- 모든 단언에 출처(소스코드 file:line / 메뉴얼 페이지 / 논문 / 교과서 챕터) 인용 필수.
- 경험은 `experience/`에 들어가되 3조건 (반복 관찰, 객관 데이터 근거, 재현 가능) 모두 만족 시에만.

### 6. 동기화: git + 단일 writer

- writer = 이 PC (`~/coastal-wiki` = WSL2 ext4. Windows 접근: `\\wsl$\Ubuntu\home\firesinger\coastal-wiki`)
- reader = 다른 PC (git clone 후 pull)
- private repo로 push (GitHub/GitLab) — 다음 단계에서 결정

### 7. 워크플로

큰 변경 시: `plan.md` 작성 → `/codex:adversarial-review` → 반영 → 구현 → `/codex:review`

## Governance Decisions (Codex MODIFY 검토 반영, 2026-05-21)

Codex adversarial review가 HIGH 4 + MID 6 위험 지적. 다음 결정으로 처리.

### G1. concepts ↔ models 소유권 규칙

- **모델 메커닉(어떻게 구현됐는가)** → `models/<model>/`이 **canonical source**
- **도메인 개념(무엇인가)** → `concepts/<topic>/`이 **canonical source**
- `concepts/<topic>/06-model-application.md`는 **요약 + `models/<model>/` 링크**만 가짐. 구현 디테일 복제 금지
- 모든 모델 적용 문서 상단에 `Canonical source: models/<model>/<file>` 블록 명시

### G2. textbook 매니페스트 + 인용 안정화

- `textbook/sources.yml` 도입 — 각 PDF에 `source_id`(stable), `filename`, `edition`, `sha256`, `page_offset` 기록
- 인용은 `(source_id, page)` 페어 사용. Windows 경로 직접 인용 금지
- 파일 이동·교체·손상 시 `sources.yml`만 갱신하면 전 인용 일관성 유지

### G3. 인용 상태 워크플로

frontmatter `citation_status` 필드 도입:

| 값 | 의미 | 위치 허용 |
|---|---|---|
| `draft-unsourced` | 초안, 출처 미정 | `drafts/` 또는 `concepts/<topic>/`의 frontmatter에 명시 |
| `source-needed` | 구조는 OK, 인용 보완 필요 | 같음 |
| `verified` | 출처 명시·검증 완료 | canonical 페이지 승격 가능 |

`INDEX.md`에 비-`verified` 항목 표시.

### G4. modeling-wiki 경계 정책

- `D:\modeling-wiki/` = 경험·실험 로그 (experience 레이어 prototype)
- `~/coastal-wiki/` = 객관 + experience 통합 우산
- 마이그레이션: `modeling-wiki/knowledge/`의 검증된 항목 → `coastal-wiki/experience/` (분기 미정, 별도 의사결정 필요)
- 새 객관 자료는 **coastal-wiki에만** 작성 (modeling-wiki에 새 객관 노트 금지)
- 별도 BOUNDARY.md에 상세

### G5. 라이선스

- 콘텐츠 라이선스: **본인용 비공개** (당분간 private repo). 외부 공개 시점에 CC BY-NC-SA 등 재결정
- textbook 인용은 fair use 범위 (요약·발췌·교육 목적). 본문 대량 복붙 금지
- 코드 스니펫: 원본 라이선스 명시, 인용

### G6. 검색 인덱싱

- 인덱스 재빌드: **수동**, 큰 변경 후 (`qmd embed` 또는 `mcp__qmd__` 도구). 정기 cron 불필요
- 일상 검색: `rg`/grep으로 충분
- frontmatter `topic`, `citation_status`, `model` 필드 기반 필터링 우선

### G7. AI 노트 검증 책임

- AI 초안 작성자 = 모델명 + 날짜 명시 (이미 POLICY.md에 있음)
- 검증 책임자 = **사용자** (firesinger). 다른 AI 모델이 spot-check 가능하지만 최종 `verified` 승격은 사용자 검토 후
- AI 간 cross-verification (Claude → Codex review)은 보조 도구. 책임은 사용자

## 미결 사항

- textbook 자료 13권 중 어느 것부터 노트화할지 우선순위
- private repo 호스팅(GitHub/GitLab/self-hosted) 결정
- modeling-wiki → coastal-wiki/experience/ 마이그레이션 시점 결정
- experience/ 레이어 실작성 시점 (객관 레이어가 얼마나 채워진 후)

## 검증 이력

- 2026-05-21: 초기 plan → Codex adversarial review → MODIFY 판정 → Governance Decisions 추가 (위 G1-G7)
- 2026-05-23: modeling-wiki 통합 결정 plan 작성 (아래 "통합 결정 (2026-05-23)" 섹션). Codex adversarial review 대기 중.

---

# 통합 결정 (2026-05-23) — modeling-wiki → coastal-wiki

## 트리거

[BOUNDARY.md](BOUNDARY.md) "통합 결정 시점" 정의 中 사용자 판단 트리거 발동:
> "사용자가 'modeling-wiki 더 이상 분리 의미 없음' 판단"
> "위 시점에 별도 plan.md 작성 → adversarial review → 통합 또는 분리 유지"

사용자 명시 (2026-05-23):
- "큰 틀은 coastal-wiki, modeling은 서브로 들어가야 한다"
- "wiki는 순수하게 코드·메뉴얼·예제를 기반으로 정확하고 객관적인 지식체계를 만드는 것"
- "오염되지 않게, 그걸 바탕으로 experience해서 노하우 축적"

## 현황 정리 (2026-05-23 시점)

### E:\ 의 modeling 관련 폴더 3종

| 폴더 | 크기 | 정체 |
|---|---|---|
| **`E:\modeling-wiki/`** | 16GB | 4월 시작 위키. `knowledge/` (164개 검증된 노하우 노트), `raw/code/adcirc/adcirc-testsuite/` (16GB 풀 클론), 정책 인프라(README/protocols/templates) |
| **`E:\models/`** | ~3GB 추정 | 5월 3일 Hermes skill `acquire-model-source`로 acquire한 **신선한 객관 카탈로그**. 각 모델별 `source_code/` + `manuals/` + `manifest.md` |
| **`E:\numerical_models/`** | 177GB | 실행 환경 + 시뮬레이션 결과 (코드·메시·run 데이터). adcirc 153GB가 대부분 — **통합 대상 아님** (실행 자산은 별개 관리) |

### modeling-wiki/knowledge/ 자산 (164개 .md)

- `failure-patterns/` 4개 (adcirc, efdc x2, xbeach)
- `heuristics/` 3개 (adcirc, efdc, xbeach)
- `methods/` 다수 — adcirc 메커닉·운영 규칙 (fort15-nws13, gwce-impl, hotstart, baseline-anatomy 등)
- `playbooks/` (확인 필요)

### E:\models/<model>/ 구조 (각 모델 동일)

- `source_code/`: GitHub 공식 repo lean clone (adcirc 생태계 7개, delft3d FM, EFDC+, ROMS 7개, swan, xbeach)
- `manuals/`: pdfs/, notes/, refs/, website/, website_markdown/, wiki/ — 매우 풍부 (adcirc: PDF 42 + website 306)
- `manifest.md`: acquisition 기록 (날짜·URL·크기·라이선스)

## 결정사항

### M1. coastal-wiki를 단일 위키로

modeling-wiki를 별개 위키로 유지하지 않고, **`coastal-wiki/models/<MODEL>/` 안으로 객관 자료 흡수**, **검증된 knowledge → `coastal-wiki/experience/` 또는 `concepts/<topic>/`로 promote**.

이유:
- 객관/경험 축이 BOUNDARY.md에 이미 정의되어 있음 — 별도 위키 분리 불필요
- 단일 writer·단일 git repo·단일 CLAUDE.md로 운영 간소화
- E:\models/가 이미 깔끔한 객관 카탈로그 형태 — coastal-wiki/models/와 자연 연결

### M2. coastal-wiki/models/<MODEL>/ 확장 구조 (D4 반영, 2026-05-23)

기존 authored 레이어 (`source-analysis/` + `manual-notes/` + `web-refs/`) 위에, raw vendor docs 는 `raw/` 격리:

```
models/<MODEL>/
├── README.md            ← 모델 정체성·라이선스·공식 사이트
├── manifest.md          ← (신규) acquisition 기록 (URL, commit/tag, sha, license)
├── source-analysis/     ← (기존) 사용자 작성 서브루틴별 분석 노트 (authored)
├── manual-notes/        ← (기존) 사용자 작성 메뉴얼 발췌 (authored)
├── web-refs/            ← (기존) 사용자 작성 위키·논문 인용 (authored)
└── raw/                 ← (신규) vendor 원본 — frontmatter 규약 면제
    ├── source_code/     ← 공식 GitHub repo clone (D1 .gitignore 대상)
    └── manuals/         ← 공식 PDF·website·wiki 다운로드 (D1 .gitignore 대상)
```

**역할 분리**:
- `README.md`, `manifest.md`, `source-analysis/`, `manual-notes/`, `web-refs/` = **authored 레이어** (CONVENTIONS frontmatter 적용, citation_status 추적)
- `raw/source_code/`, `raw/manuals/` = **vendor 원본** (CONVENTIONS frontmatter 검사 면제, .gitignore 대상)

**Authored 노트는 raw 를 인용한다**:
- `source-analysis/<file>.md` → `(<MODEL>/raw/source_code/repo/file.f90:LN-LN)` 형식으로 file:line 인용
- `manual-notes/<chapter>.md` → `(<MODEL>/raw/manuals/<doc>.pdf, p.NN)` 형식
- raw 트리는 git 추적 안 되지만 manifest.md 의 (repo URL, commit/tag, sha) 로 reader 재현

**CONVENTIONS frontmatter 예외** (§2.1 갱신 대상):
- `models/*/raw/**` 전체는 frontmatter 의무 면제 (vendor 원본은 우리 규약을 따르지 않음)
- validation 스크립트도 raw/ 를 검사 대상에서 제외

### M3. adcirc-testsuite는 풀버전(16GB) 유지 (D1·D4 반영)

- `E:\modeling-wiki/raw/code/adcirc/adcirc-testsuite/` (16GB, 데이터 풍부) → `coastal-wiki/models/ADCIRC/raw/source_code/adcirc-testsuite/` 로 이동
- `E:\models/adcirc/source_code/adcirc-testsuite/` (166M, lean clone) → 폐기 (풀버전으로 대체)
- 이유: 사용자 명시 — "테스트까지 놔둬야 돼, 분석 베이스"
- **git 처리 (D1)**: `models/*/raw/source_code/` 는 `.gitignore` 됨. testsuite 16GB 는 로컬 ext4 + 외부 백업으로만 보존. reader 가 필요하면 `git clone https://github.com/adcirc/adcirc-testsuite` 별도 clone — `models/ADCIRC/manifest.md` 에 repo URL·commit sha 기록.

### M4. knowledge/ promote는 staging 거쳐 한 건씩

- `coastal-wiki/_staging/from-modeling-wiki/` 임시 디렉토리 생성
- modeling-wiki/knowledge/ 164개를 그대로 staging으로 복사
- BOUNDARY.md 마이그레이션 규칙 (2회 이상 독립 관측 + 객관 데이터 + 재현 가능) 적용해 한 건씩:
  - 객관·도메인 일반화 가능 → `concepts/<topic>/`
  - 검증된 개인 경험 → `experience/`
  - 검증 안 됨 → staging에 유지 또는 archive
- promote 작업은 별도 PR/세션에서 진행 (이번 통합과 분리)

### M5. modeling-wiki/raw/code/adcirc/adcirc/ (125M, 4월본)은 폐기

- E:\models/adcirc/source_code/adcirc/ (89M, 5월 3일 신선 clone)이 대체
- 4월본의 .git history는 GitHub에서 항상 재취득 가능 → 폐기 안전

### M6. modeling-wiki의 운영 자산은 흡수 또는 archive

- `README.md`, `protocols/`, `templates/`, `context/`: 핵심 정책만 coastal-wiki의 CONVENTIONS.md / plan.md에 흡수, 나머지는 `_archive/modeling-wiki/`로 이동
- `experiments/2026/`: 검토 후 `experience/` 후보 또는 archive
- `indexes/`, `graphify-out/`: archive

### M7. BOUNDARY.md는 "통합 완료" 상태로 갱신

- 본문 상단에 "**2026-05-23 통합 완료 — 이 문서는 통합 이전 정책의 역사적 기록**" 명시
- 본문은 보존 (마이그레이션 규칙·외부 편집 인테이크 등은 single-writer 정책의 일반화된 자산)

### M8. E:\models/ 와 E:\modeling-wiki/ 처리

- 흡수 완료 확인 후 → `E:\models.archive-2026-05-23/`, `E:\modeling-wiki.archive-2026-05-23/`로 rename
- 1~2개월 후 정상 동작 확인되면 archive 삭제
- `E:\numerical_models/` 는 **건드리지 않음** (실행 자산, 별개)

### M9. WSL ext4 공간 확인 필수

- 예상 추가 용량: ~17–18GB (testsuite 16GB + 다른 모델 manuals·source ~1.5GB)
- coastal-wiki 현재 크기 확인 + WSL 디스크 여유 확인 후 진행
- 부족하면 Windows 디스크 (`/mnt/c` 또는 `/mnt/d`)의 적당한 위치에 모델별 source_code/manuals만 두고 symlink 검토 (단, ext4 우선)

### M10. Hermes coastal-research 프로필 영역 신설

- `~/coastal-wiki/research/`를 Hermes `coastal-research` 프로필의 주 작업 루트로 둔다.
- `research/`는 X, arXiv, 블로그, GitHub, 기관 공지, 툴 업데이트를 수집·요약하는 **격리 워크벤치**다.
- `concepts/`, `models/`, `experience/`는 verified/canonical 본문 레이어로 유지하고, `research/` 산출물은 본문에서 직접 인용하지 않는다.
- Promote 방향은 `_staging/from-modeling-wiki/`와 같은 단방향 패턴을 따른다:
  - 객관·도메인 일반화 → `concepts/<topic>/`
  - 모델 자료 → `models/<MODEL>/web-refs/`, `models/<MODEL>/manual-notes/`, `models/<MODEL>/source-analysis/`
  - 검증된 개인 노하우 → `experience/`
  - 모니터링 대상 → `research/watchlist/`
- `research/manifest.md`에 수집 방법, 검색 쿼리, 한계, 공식 API 전환 조건을 기록한다.
- `research/inbox/` 항목은 `origin`, `discovered_date`, `source_url`, `source_type`, `query`, `citation_status`, `promote_candidate` frontmatter를 사용한다.
- `inbox/` 항목은 90일 안에 promote, watchlist 이동, archive/discard 중 하나로 처리한다.

#### 상세 정책

modeling-wiki 통합과 동일 시점에 Hermes 도구의 `coastal-research` 프로필 작업 루트를 위키 내부 격리 영역으로 도입.

**위치**: `~/coastal-wiki/research/`

**이유**:
- Hermes는 X/arXiv/논문/툴 트렌드를 자동 스캔·요약하는 워크벤치. 자동 산출물이 객관 위키 본문(concepts/, models/, experience/)과 섞이면 **CLAUDE.md 절대규칙 #1·#3 (객관 레이어 출처 인용 필수, AI 요약과 원본 명확 구분) 위반**
- 외부 별도 디렉토리(`~/coastal-research/`)는 위키와 동기 비용 증가
- 위키 내부 격리는 단일 git 이력 유지 + 본문과 명확 분리 + 자연스러운 promote 방향 확보
- modeling-wiki 통합의 `_staging/from-modeling-wiki/`와 같은 "격리 후 단방향 promote" 사상 — 일관성

**구조**:

```
research/
├── README.md          # inbox 정책: 체류 기간, promote 규칙, frontmatter 표준
├── inbox/             # 새 후보 (X·arXiv·블로그·repo 발견)
│   └── YYYY-MM-DD-<slug>.md
├── digests/           # Hermes 주간·월간 요약
├── watchlist/         # 모니터링 대상 (저자·기관·repo·키워드)
└── manifest.md        # Hermes 프로필 운영 기록 (acquisition method, 빈도, 변경 이력)
```

**frontmatter 표준** (research/ 내부 모든 파일):

```yaml
origin: hermes-coastal-research
discovered_date: YYYY-MM-DD
source_url: <원본 링크>
source_type: paper|tweet|repo|blog|tool|other
citation_status: draft-unsourced   # 디폴트
relevance: <어떤 위키 토픽·모델과 연관되는지>
```

**Promote 경로** (research → 본문, 단방향):

| 자료 유형 | promote 대상 | 필요 조건 |
|---|---|---|
| 도메인 일반화 가능 (이론·정의·법칙) | `concepts/<topic>/` | 출처 보강해 `citation_status: verified`로 |
| 모델 공식 자료 업데이트 (논문·메뉴얼 신판) | `models/<MODEL>/web-refs/` 또는 `manuals/` | 공식성 확인 |
| 검증된 개인 노하우 (반복 관찰+객관 데이터+재현) | `experience/` | [BOUNDARY.md](BOUNDARY.md) 3조건 적용 |
| 비검증·일회성 | research/inbox 잔류 또는 archive | — |

**금지**:
- research/ 내부 파일을 위키 본문 노트에서 직접 인용 (promote 거친 후만 인용 가능)
- inbox 체류 90일 초과 자료의 자동 promote (수동 검토 필수)
- research/ 안에 본문 성격의 객관 단언 작성 (canonical 자리 잡지 못함)

**Hermes 프로필 설정** (사용자가 별도 수행):

```bash
hermes --profile coastal-research
# cwd: /home/firesinger/coastal-wiki/research
# 정책: README, INDEX.md, CONVENTIONS, BOUNDARY 참조
# 출력: inbox/, digests/, watchlist/만 write 허용
# 본문(concepts/, models/, experience/)은 read-only
```

**`_staging/`와 `research/`의 역할 분리**:

- `_staging/from-modeling-wiki/` = **이미 존재하는 자산을 위키로 가져오기** (1회성·과거)
- `research/inbox/` = **새로 발견되는 자산을 위키로 가져오기** (지속·미래)
- 둘 다 promote 후 archive 또는 폐기. 본문 자리 아님

## 새 구조 (통합 후, D4 반영)

```
~/coastal-wiki/
├── concepts/                      # 도메인 개념 (조석·파랑·해류·퇴적 등)
├── models/                        # 모델 객관 자료
│   ├── INDEX.md, _template/
│   ├── ADCIRC/
│   │   ├── README.md               # 모델 정체성·라이선스
│   │   ├── manifest.md             # acquisition 기록 (repo URL, commit, sha)
│   │   ├── source-analysis/        # authored: 사용자 분석 노트 (frontmatter 적용)
│   │   ├── manual-notes/           # authored: 사용자 메뉴얼 발췌 (frontmatter 적용)
│   │   ├── web-refs/               # authored: 사용자 위키·논문 인용 (frontmatter 적용)
│   │   └── raw/                    # vendor 원본 (frontmatter 면제, .gitignore 됨)
│   │       ├── source_code/        # 공식 GitHub repo clone
│   │       │   ├── adcirc/, asgs/, gahm/, adcircpy/, StormEvents/, FigureGen/
│   │       │   └── adcirc-testsuite/   # 16GB 풀버전 (별도 clone으로만 재현)
│   │       └── manuals/            # 공식 PDF·website·wiki
│   ├── Delft3D/, EFDC/, SWAN/, XBeach/  # 같은 패턴
├── textbook/, examples/, experience/, data/
├── tools/                          # 위키 유지 스크립트
│   ├── validate-research-isolation.sh   # D3: research/ 격리 검증
│   ├── install-hooks.sh                  # D3: pre-commit hook 설치
│   └── khoa-validation/                  # (기존)
├── research/                       # Hermes coastal-research 프로필 작업 루트 (M10)
│   ├── README.md, manifest.md
│   ├── inbox/, digests/, watchlist/
├── _staging/from-modeling-wiki/   # knowledge/ 164개 임시 (단계적 promote 대기, M4)
├── _archive/modeling-wiki/         # 정책·운영 자산 보존 (M6)
├── .git/hooks/pre-commit          # D3: validate-research-isolation.sh 자동 실행
├── .gitignore                     # D1: models/*/raw/** 제외 룰 포함
├── INDEX.md, README.md, CLAUDE.md, CONVENTIONS.md, BOUNDARY.md, plan.md, SYNC.md, AGENTS.md
```

## 마이그레이션 단계 (D2 반영 — copy-verify-archive 패턴)

**원칙**: 원본 보존이 최우선. 모든 delete 는 copy + checksum verify + commit/push 성공 확인 **이후**로 미룬다. 중간 중단 시 partial state 에서 resume 가능하도록 idempotent.

### Phase 0 — Preflight (절대 비가역 작업 금지)

| # | 작업 | 검증 기준 |
|---|---|---|
| P1 | WSL ext4 공간 확인 (`df -h ~`) | 20GB+ 여유 |
| P2 | D1 `.gitignore` 룰 commit 되어 있는지 확인 (`git check-ignore -v models/ADCIRC/raw/source_code/test`) | `.gitignore` 매치 출력 |
| P3 | D3 pre-commit hook 설치 확인 (`ls .git/hooks/pre-commit && bash tools/validate-research-isolation.sh`) | `EXIT=0` |
| P4 | E:\ 측 원본 read-only 마운트 가능성 점검 (가능하면 적용) | I/O 사고 시 원본 보호 |

### Phase 1 — Manifest 생성 (read-only, 원본 변경 0)

**중요 (F4)**: 모든 checksum/inventory 는 **각 트리 root 기준 상대 경로**로 생성. source(`E:\...`)와 target(`models/...`)의 prefix 가 다르므로 절대 경로로 만들면 diff 가 절대 비지 않음 → verify gate 무력화. 표준 명령:

```bash
# source 측 — 예: E:\modeling-wiki\raw\code\adcirc\adcirc-testsuite
cd "/mnt/e/modeling-wiki/raw/code/adcirc/adcirc-testsuite" \
  && find . -type f -print0 | LC_ALL=C sort -z \
  | xargs -0 sha256sum > "$WIKI/_staging/manifests/sha256-source-adcirc-testsuite.txt"

# target 측 — 예: models/ADCIRC/raw/source_code/adcirc-testsuite (rsync 완료 후 Phase 3)
cd "$WIKI/models/ADCIRC/raw/source_code/adcirc-testsuite" \
  && find . -type f -print0 | LC_ALL=C sort -z \
  | xargs -0 sha256sum > "$WIKI/_staging/manifests/sha256-target-adcirc-testsuite.txt"
```

두 산출물 모두 첫 컬럼이 sha256, 둘째가 `./relative/path` — `diff` 가 prefix 무관하게 동작.

| # | 작업 | 산출물 |
|---|---|---|
| M1 | 각 source 트리에 대해 위 명령으로 상대경로 sha256 manifest 생성 | `_staging/manifests/sha256-source-<area>.txt` |
| M2 | 각 source 트리 파일 수·총 크기 기록 (`find . -type f \| wc -l; du -sh .`) | `_staging/manifests/size-source-<area>.txt` |
| M3 | 인벤토리(파일 목록만, sha 없이) 도 별도 생성 (`find . -type f \| LC_ALL=C sort`) | `_staging/manifests/files-source-<area>.txt` |

### Phase 2 — Copy (원본 유지, 신규 위치에 복제)

| # | 작업 | rollback |
|---|---|---|
| C1 | `rsync -av --partial --append-verify E:\modeling-wiki/raw/code/adcirc/adcirc-testsuite/ → models/ADCIRC/raw/source_code/adcirc-testsuite/` | 부분 복사 시 재실행으로 resume |
| C2 | 각 `E:\models/<m>/source_code/` → `models/<MODEL>/raw/source_code/` rsync (모델별 반복) | 동일 |
| C3 | 각 `E:\models/<m>/manuals/` → `models/<MODEL>/raw/manuals/` rsync | 동일 |
| C4 | `E:\models/<m>/manifest.md` → `models/<MODEL>/manifest.md` 복사 (authored 레이어로 승격, frontmatter 검증 대상) | 동일 |
| C5 | `E:\modeling-wiki/knowledge/` → `_staging/from-modeling-wiki/` rsync (164개) | 동일 |
| C6 | `E:\modeling-wiki/{README,protocols,templates,context,experiments,indexes,graphify-out}/` → `_archive/modeling-wiki/` rsync | 동일 |

### Phase 3 — Verify (체크섬·count·참조)

각 target 트리에 대해 Phase 1 과 **동일한 root-relative 명령**으로 sha256 manifest 를 만들어 `diff source target` 이 깨끗하게 비어야 함.

| # | 작업 | 합격 기준 |
|---|---|---|
| V1 | 각 target 트리에 대해 root-relative sha256 manifest 생성 (Phase 1 의 target 측 명령 그대로) | manifest 생성 성공 |
| V2 | `diff -u sha256-source-<area>.txt sha256-target-<area>.txt` | 출력 비어있음 (모든 sha + 상대경로 일치) |
| V3 | `diff -u files-source-<area>.txt files-target-<area>.txt` | 출력 비어있음 (파일 누락/추가 없음) |
| V4 | target 측 파일 수 == source 측 파일 수 (`wc -l`) | 동일 |
| V5 | `models/ADCIRC/raw/source_code/adcirc-testsuite/` 의 대표 5개 파일 sha256 spot-check | source 와 일치 |
| V6 | `bash tools/validate-research-isolation.sh` | `EXIT=0` |
| V7 | (D1·F3 안전 점검) `git status --ignored` 가 `models/*/raw/` 트리를 무시하는지, 그리고 `git diff --cached --name-only` 에 raw 경로 부재 | ignored 분류 + index 에 raw 없음 |

### Phase 4 — Policy commits (분할)

| # | 작업 | branch/PR |
|---|---|---|
| P-1 | ① 정책 commit: `.gitignore`, `tools/`, `CONVENTIONS.md`, `plan.md`, `BOUNDARY.md`, `INDEX.md`, `README.md`, `research/` | commit 1 |
| P-2 | ② models/ authored 흡수: `README.md`, `manifest.md`, `source-analysis/`, `manual-notes/`, `web-refs/` (raw/ 는 .gitignore 됨) | commit 2 |
| P-3 | ③ `_staging/from-modeling-wiki/` (164개 + manifest) | commit 3 |
| P-4 | ④ `_archive/modeling-wiki/` (운영 자산) | commit 4 |
| P-5 | `git push` — 4개 commit 모두 reject 없이 통과 확인 | push 성공 |

### Phase 5 — Archive rename (원본은 살아있음, 단지 이름 변경)

| # | 작업 | 비가역성 |
|---|---|---|
| A1 | `E:\models/` → `E:\models.archive-2026-05-23/` (rename, 데이터 보존) | rollback 가능 |
| A2 | `E:\modeling-wiki/` → `E:\modeling-wiki.archive-2026-05-23/` (rename, 데이터 보존) | rollback 가능 |
| A3 | archive 트리에 대해 한 번 더 sha256 manifest 생성, Phase 1 manifest 와 diff | diff 비어있음 (rename 만 한 거 검증) |

### Phase 6 — Delete (1~2개월 유예 후 별도 의사결정)

| # | 작업 | 게이트 |
|---|---|---|
| D1 | E:\*.archive-2026-05-23/ 삭제 | (a) 사용자 명시 OK + (b) 최소 1개월 정상 동작 + (c) 외부 백업(OneDrive 등) 검증 |

**중단 시 재진입 규칙**:
- Phase 0~3 중단: 부분 산출물은 모두 idempotent rsync · sha256 결과. 재실행으로 resume.
- Phase 4 중단: `git reset --soft HEAD~N` 으로 commit 만 되돌리고 Phase 3 재검증.
- Phase 5 중단: rename 은 atomic. 한쪽만 됐으면 나머지만 마저.
- Phase 6 는 의사결정 게이트이므로 "중단" 개념 없음.

## 위험·우려 (자체 식별 + Codex 1차 반영 2026-05-23)

1. **WSL ext4 디스크 압박** — 17~18GB 추가는 디스크 용량 검토 필수 (Phase 0 P1). 부족하면 NTFS에 raw/만 두고 ext4에는 authored 노트만 두는 hybrid 검토.
2. **knowledge/ promote 누락** — 164개를 staging에 두고 잊으면 자산 사장. `_staging/from-modeling-wiki/STAGING-PROGRESS.md` 로 진척 추적 (체크박스 + 마감일).
3. **`models/raw/` 와 authored 레이어 혼동** — D4 로 raw/ 격리해 이름 충돌 해소. CONVENTIONS §2.1 에 "models/*/raw/** frontmatter 면제 + validation 제외" 명시.
4. **`manifest.md` 와 `README.md` 역할 분리** — manifest.md = acquisition 메타 (repo URL, commit, sha, license), README.md = 모델 정체성·라이선스 요약. 둘 다 authored, frontmatter 적용.
5. ~~**adcirc-testsuite 16GB git 부담**~~ → **해결**: D1 `.gitignore` + 외부 백업. testsuite 는 별도 clone 으로 재현 (manifest.md 에 repo URL·sha 기록).
6. **modeling-wiki 의 `.graphifyignore`, `graphify-out/` 의존성** — graphify 도구 워크플로 미사용으로 결정 시 `_archive/modeling-wiki/` 로 이동 (Phase 2 C6 에 포함).
7. **단방향 promote 정책 위반 우려** — BOUNDARY.md "modeling-wiki 원본 보존" 정책은 통합으로 종료 (BOUNDARY.md 상단 헤더로 명시). history 는 `_archive/` 에 보존.
8. ~~**대규모 commit 시 git push 부담**~~ → **해결**: D1 으로 raw 트리 제외. 첫 commit 은 authored 자료 + 정책만 → 100MB·1GB 한도 안전.
9. **rollback 안전성** — D2 의 copy-verify-archive 패턴으로 모든 delete 가 commit/push 성공 후로 연기. 중단 시 idempotent resume. Phase 6 delete 는 1~2개월 유예 + 외부 백업 검증 게이트.
10. **research/ 격리 silent 위반** — D3 의 `validate-research-isolation.sh` + pre-commit hook 으로 enforce. 본문에서 `research/` 직접 참조 또는 research/ 내 frontmatter 위반 시 commit fail.

## 미결 사항 (운영 게이트 — 마이그레이션과 무관)

- graphify 도구 유지 여부 (현 시점 결정 보류 → archive 행, 필요 시 추후 복원)
- E:\numerical_models/ 처리 (이번 통합 범위 밖이지만 swan.zip/xbeach.zip 중복 정리 등은 별도 진행)
- E:\AI_ENV/ 잔여물 (claude-code-best-practice 53M 등) 처리
- 회사 PC의 modeling-wiki·models 동기화 (있다면)
- Hermes coastal-research 프로필의 자동화 빈도 (수동 트리거 / cron 주간 / 실시간 webhook 중)
- research/inbox/ 체류 한계 90일이 적절한지 (운영 후 조정)
- research/manifest.md에 기록할 acquisition 메서드 표준 (X scraping, arXiv API, GitHub trending 등)

## 검증 이력 — Codex Adversarial Review

- **2026-05-23 1차 (working tree)**: verdict `needs-attention`. critical 1, high 2, medium 1.
  - C1 (16GB git 정책 미결) → D1 결정: `.gitignore` + 외부 백업 + manifest.md 재현 정보
  - H1 (rollback safety) → D2 결정: copy-verify-archive 6-phase 재작성
  - H2 (research/ 격리 enforce 부재) → D3 결정: `tools/validate-research-isolation.sh` + pre-commit hook
  - M1 (raw upstream .md frontmatter 충돌) → D4 결정: `models/<M>/raw/` 격리 + CONVENTIONS §2.1 예외
- **2026-05-23 2차 (D1~D4 적용 후)**: verdict `needs-attention`. high 2, medium 2.
  - F1 (hook 이 working tree 만 검사, staged 우회 가능) → `tools/validate-research-isolation.py` 도입, `--staged` 모드: `git diff --cached` + `git show :path` 로 staged snapshot 검증
  - F2 (참조 detector 가 ../../research/ 등 흔한 패턴 놓침) → Python 으로 재작성: inline/angle/reference-style 링크 추출, 파일 위치 기준 `os.path.normpath` 로 정규화 후 repo-root research/ 판정. 9개 synthetic case 통과.
  - F3 (.gitignore 가 `git add -f` 무력) → pre-commit hook 에 staged path guard 추가: `^models/[^/]+/raw/(source_code|manuals)/` 패턴 reject, 50MB 초과 blob 경고 (임계치 `COASTAL_WIKI_MAX_BLOB_MB`)
  - F4 (source/target manifest prefix 불일치로 diff 무력) → Phase 1·3 명령을 `cd "$root" && find . -type f -print0 | LC_ALL=C sort -z | xargs -0 sha256sum` 로 통일, root-relative path 로 diff
- **2026-05-23 3차 (F1~F4 적용 후)**: verdict `needs-attention`. high 1, medium 1. F1/F3/F4 모두 closed 확인. F2 부분 미완.
  - G1 (indented reference definition 우회) → `REF_DEF_RE` 에 leading 0~3 space/tab 허용 (CommonMark 사양). 4-space 이상은 code block 으로 해석되므로 의도적 제외.
  - G2 (root-relative `/research/...` 무시) → `target_resolves_into_research` 가 `/` prefix 를 repo-root 기준 상대로 normalize. Obsidian vault / static site renderer 컨벤션 대응.
  - 회귀 테스트 도입: `tools/test_validate_research_isolation.py` — 25개 fixture (inline/angle/refdef, indented, root-relative, fragment/query, scheme, code block 무시, false positive). 모두 통과.
- **2026-05-23 4차 (G1~G2 적용 후)**: verdict `needs-attention`. high 1, medium 2. G2 closed, 25 fixtures pass. G1 부분 closure (CommonMark spec 더 정확히 봐야 함) + 신규 HTML href/src 우회 지적.
  - H1 (no-space refdef 우회) → `REF_DEF_RE` 의 `:\s+` 를 `:[ \t]*` 로 (0+ whitespace 허용). CommonMark spec 준수.
  - H2 (tab-indent refdef false positive) → `[ \t]{0,3}` 를 `[ ]{0,3}` 로 (space only). CommonMark column-based indent — tab 은 4+ col expand → code block. 회귀 fixture "tab-indented → 위반 아님" 으로 정정.
  - H3 (raw HTML href/src 우회) → `HTML_HREF_RE = (?i)(?:href|src)\s*=\s*("([^"]+)"|'([^']+)')` 추가. extract_link_targets 에 통합. uppercase, single/double quoted, root-relative `/research/` 패턴 fixture 추가.
  - 회귀 테스트 33개로 확장 (link 28 + frontmatter 5). 모두 통과.
- **2026-05-23 5차 (H1~H3 적용 후)**: verdict `needs-attention`. high 2. 명시 케이스 모두 pass. Codex 본인이 출구 명시: *"parser-free implementation is acceptable for a non-public single-writer wiki if documented as a conservative policy scanner rather than exact CommonMark compliance."*
  - I1 (no-line-ending refdef 못 잡음) → `REF_DEF_RE` 에 `(?:\n[ \t]*)?` 추가, multi-line destination 지원 (CommonMark 0.31.2: colon 뒤 최대 1 line ending). 단, blank line 은 refdef 종료로 의도적 reject.
  - I2 (unquoted HTML + data-href false positive) → `HTML_HREF_RE` 에 unquoted alt `([^\s>"'`]+)` + `(?<![\w-])` lookbehind. data-href / data-src / x-href fixture 추가, false positive 차단 확인.
  - 회귀 테스트 42개로 확장 (link 37 + frontmatter 5). 모두 통과.
  - **Scope 명시**: 스크립트 docstring 에 "conservative policy scanner, not CommonMark parser. 일반 실수·흔한 변형 케이스 cover. spec-pathological 변형은 의도적으로 cover 안 함 — multi-defense (사용자 review + ultrareview) 로 처리." 명시.
- **2026-05-23 6차 (I1~I2 + scope docs 적용 후)**: verdict **`approve`**. No material findings. ✅ Migration may proceed.
  > "Ship. I1 and I2 are closed: multi-line refdefs are detected while blank-line-separated destinations are rejected, unquoted href/src is detected, and data-href/data-src/x-href false positives are blocked. The 42 regression tests pass, the working-tree validator passes, and the docstring explicitly scopes this as a conservative policy scanner rather than a CommonMark parser. Migration may proceed at this point."
