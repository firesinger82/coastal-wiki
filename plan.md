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

### G8. canonical 정화 원칙 (2026-06-18, 대규모 정화 후 코드화 — Codex 적대검증 MODIFY 반영)

위키 = 케이스 *공급원*(reference), 저장소 아님. 개인 케이스는 위키 밖에서 구축. 4 하위 규칙(역할 분담 명확화):

- **G8a 레이어 경계** (CLAUDE.md 절대규칙 8): 개인 run 결과·calibration 수치·작성자/프로젝트 실행에만 의존하는 운영 지침은 canonical 금지. 예외 = 소스코드·식·algorithm 이 main claim 인 failure-patterns/heuristics/playbooks(`models/<model>/source-analysis/` 하위, triage 규칙), wrapper-only `06-model-application.md`. 제거는 `_staging/`·`_archive/` 경유(즉시 삭제 = 별도 게이트, 2a.9/phase 6 동일).
- **G8b 경로 문법** (CONVENTIONS §4): 작성자 로컬 머신·마운트·홈·드라이브·실행 워크스페이스 *식별* 절대경로(`D:\`·`E:\`·`/mnt/[de]/`·`~/...`·`\\wsl$`)는 canonical 어디에도 금지. 허용 = repo-상대 소스코드 `file:line`, 공식 매뉴얼/vendor 표기 경로의 출처 인용. **적용 범위 = canonical 콘텐츠(`concepts/`·`models/`·`textbook/` 노트)**. 거버넌스/결정기록 문서(본 plan.md 의 마이그레이션 이력 등)·`sources.yml` 레지스트리·`raw/`·`_staging/`·`_archive/` 는 비대상(이력·레지스트리·vendor 미러).
- **G8c 출처 식별 단위** (CONVENTIONS §3): 1 source_id = 1 bibliographic/work + edition. 미러·로컬 사본 = alias. 별개 문서·에디션·repo·논문·데이터셋·릴리스노트 = 별도 source_id (예: `khoa-notice-2021-7` 고시 ≠ `khoa-tide-model` 수치조류도).
- **G8d 본문 위생** (CONVENTIONS §6): canonical 노트에 개인·프로젝트·실행 사례 기입 유도 placeholder(빈 heading·TODO·체크박스, 예 `▢ User-experience cases`) 금지. 면제 = `source-needed`/객관·공식 내용 대기 stub(개인사례 비요청), `_template/`.

근거 프레임워크: Diátaxis(reference↔how-to 분리), DRY/SSOT(Hunt-Thomas), Wilson et al. 2017 "Good enough practices in scientific computing"(portable paths), FAIR R1.2(provenance), Matuschak evergreen concept-oriented(= concepts/ 1차축 정합).

**Codex 적대검증 반영(2026-06-18)**: ① 삭제 기본값 → `_staging/`·`_archive/` 수명주기 정합 ② vendor/공식 매뉴얼 경로·repo-상대 file:line 면제 명시 ③ "이질 출처" → work+edition 단위로 정밀화(source_id 과잉분열 방지) ④ source-grounded 플레이북·wrapper-06 면제 명시.

**후속(미결)**: G8b(경로)·G8d(placeholder)는 regex 자동검증 가능 → `tools/validate-canonical-hygiene.sh` 신설 후보. G8c 의미론적 혼용 탐지는 `sources.yml` 스키마(`work_id`/`edition`/`format`) 보강 시 가능.

## 미결 사항

- textbook 자료 13권 중 어느 것부터 노트화할지 우선순위
- private repo 호스팅(GitHub/GitLab/self-hosted) 결정
- modeling-wiki → coastal-wiki/experience/ 마이그레이션 시점 결정
- experience/ 레이어 실작성 시점 (객관 레이어가 얼마나 채워진 후)

## 검증 이력

- 2026-05-21: 초기 plan → Codex adversarial review → MODIFY 판정 → Governance Decisions G1-G7 추가
- 2026-06-18: 대규모 canonical 정화 → Codex adversarial review(MODIFY) → 반영 후 Codex 최종 review(MODIFY, 정합성 4건) → 반영 → G8(a-d) 추가
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

---

# Phase 2 Plan (2026-05-23 후속, v8 — codex review 1~7차 반영) — deterministic codex archive + mandatory evidence sha256 + raw_path resolution

> v8 변경 사항 (codex review 7차 3 findings 반영):
> - **O1**: codex archive naming deterministic — extract session_id 후 `<session_id>.output` 정규 이름으로 copy. `.log` 등 비일관 형식 reject
> - **O2**: manifest schema 14 → **15 컬럼** — `codex_evidence_sha256` **mandatory** (codex-review row). archived file + sums.txt 둘 다 match
> - **O3**: marker 에 `raw_path` 추가 또는 inline citation 의 `source_id` → `textbook/sources.yml` resolve → manifest 의 `raw_path` 자동 일치 확인
>
> v7 변경 사항 (codex review 6차 3 findings 반영):
> - **N1**: post-archive set equality 정확 정의 — `actual = find archive_root -type f`, `expected = {archive_path_for(row) for row in manifest}`, `expected == actual` + per-file sha256
> - **N2**: codex-review evidence durable archive — `_archive/codex-reviews/<session_id>.output` 으로 copy + sha256, ephemeral path 거부
> - **N3**: self-cited-line — exact citation marker (`<!-- cite:source_id=...,raw_path=...,line=... -->`) 또는 structured field. ±3 proximity false-positive 차단
>
> v6 변경 사항 (codex review 5차 2 findings 반영):
> - **M1**: Rule A condition 6 의 semantic validation 강화 — regex 만으론 부족, validator 가 각 form 의 실제 의미 검증 (date parseable, codex review file 존재, self-cited-line 파일·라인 매핑)
> - **M2**: 2a.7 post-archive integrity — **모든 50 rows** (skip-readme + 46 content) 의 archive path 존재 + sha256 == sha256_before set equality 검증
>
> v5 변경 사항 (codex review 4차 2 findings 반영):
> - **L1**: manifest 13 → 14 컬럼 (`claim_mapping_verified_by` 추가) + Rule A condition 6 의 machine-enforceable 형태 명시 + `tools/validate-phase2a-manifest.sh` 작성 명세 + regression fixtures
> - **L2**: inventory 정정 — **실제 50 files = 46 content + 4 README** (adcirc-sources/xbeach-sources README 없음). P1 listing count 11 정정. skip-readme validation order (pre-archive vs post-archive) explicit
>
> v4 변경 사항 (codex review 3차 3 findings 반영):
> - **K1**: dest 파일 frontmatter `citation_status` ↔ manifest `citation_status_target` cross-check 강제 (Phase 2a validator rule)
> - **K2**: README explicit disposition — `classification=skip-readme` enum 추가
> - **K3**: D5 의 partial-verified 표시 제거 — Option A 일관성 유지
> 
> v3 변경 사항 (codex review 2차 5 findings 반영):
> - **J1**: manifest schema 8 → 13 컬럼 + verified 강제 enforcement rule
> - **J2**: 2a step 순서 재정렬 — link rewrite **먼저**, validate, archive, final delete
> - **J3**: storm-surge/05 target = `source-needed` (KHOA 페이지 직접 인용 전까지)
> - **J4**: manifest inventory `find _staging/...` 자동 생성, set equality gate
> - **J5 (Option A)**: **`partial-verified` 도입 보류**, wrapper-only 페이지 = `source-needed` 유지. CONVENTIONS·validator·INDEX semantics 변경 없음.

## 컨텍스트

[Phase 1 (modeling-wiki 통합)](#통합-결정-2026-05-23--modeling-wiki--coastal-wiki) 완료 후 6 commit 점진적 진척:
- methods 107 노트 → models/<M>/source-analysis/ promote (D 작업)
- SST 토픽 5/6 verified · storm-surge 3/6 · sediment-transport 5/6 · littoral-drift 1/2 verified
- experience 5 노트 (KHOA tide·SLR·SST·SST-global·NIFS-vertical)

남은 영역:
- `_staging/from-modeling-wiki/knowledge/` 잔존 ~46 항목
- concepts source-needed: tides/06 · sediment-transport/05 · currents/06 · sst/06 · storm-surge/{03·05·06 미생성} · littoral-drift/{02·03·04·05·06 미생성}
- experience 확장 후보

## Phase 2 v1 → v2 — codex review 6 findings 반영

**v1 (2026-05-23 작성, codex review 1차)**: verdict `needs-attention` — 6 findings. v2 에서 다음 반영:

| Finding | 반영 |
|---|---|
| H1 P3/B 수치 모순 + 우발적 verified | §B 의 single canonical table 도입, 각 file 별 source_id·claim scope·target status 명시 |
| H2 manual catalog artifact gate 부재 | §2a 의 catalog promote 시 raw artifact 존재 확인·source_id 부착, 부재 시 citation_status: source-needed 유지 |
| H3 Phase A copy-verify-archive 명목뿐 | §2a 의 migration manifest schema 도입, copy → validate → archive → separate final delete 분리 |
| M1 failure/heuristic mixed default | §P1 의 triage checklist + **mixed 시 default = experience/ + source-needed** |
| M2 Chuksan 정량 verified gate | §C 의 efdc-chuksan-sediment.md 강제 citation_status: source-needed, 수치 "anecdotal" 라벨 |
| M3 scope creep | Phase 2 → **2a/2b/2c/2d 분리**, 각 sub-phase 별 독립 review·commit·codex check |

## Sub-phase 분리

| Sub-phase | 범위 | 분량 | 의존성 |
|---|---|---|---|
| **2a** | _staging 잔존 promote (manifest + copy + verify + archive + final delete) | 한 세션 | 단독 |
| **2b** | concepts 갭 보강 (canonical table 기반) | 한 세션 | 2a (manual-notes 안정화) |
| **2c** | experience 3 신규 (chuksan source-needed 강제) | 한 세션 | 2b 일부 |
| **2d** | 정책·도구 정리 (sources.yml·BOUNDARY·INDEX 최종) | 짧음 | 2a-2c |

각 sub-phase 마다 commit + push + (선택) codex:review.

---

## Sub-phase 2a — _staging 잔존 promote (manifest 기반)

### P1. failure-patterns / heuristics / playbooks 분류 (M1 반영)

#### 분류 triage checklist

각 노트에 다음 질문 순서로 적용:

1. **"본 노트가 모델 source-code line·equation·algorithm 을 인용하는가?"**
   - YES → 다음 질문
   - NO → **`experience/` + citation_status: source-needed** (mixed default)
2. **"인용된 모델 메커닉이 노트의 main claim 인가, 보조 reference 인가?"**
   - main → `models/<MODEL>/source-analysis/{failure-patterns,heuristics,playbooks}/`
   - 보조 → split: source-analysis fragment (cited) + experience fragment (operational)
3. **모호 시** → **default = `experience/` + source-needed** (objective layer 보호)

#### 대상 노트 (11개, L2 정정 — 4+3+4=11, 이전 10 표기 정정)

`_staging/from-modeling-wiki/knowledge/`:
- `failure-patterns/`: adcirc-wide6-provenance-gap.md, efdc-water-level-good-current-bad.md, efdc-wetdry-connectivity-bias.md, xbeach-morphology-interpretation-drift.md
- `heuristics/`: adcirc-baseline-before-tool-revalidation.md, efdc-check-comparison-basis-before-friction-tuning.md, xbeach-validate-hydrodynamics-before-trusting-morphology.md
- `playbooks/`: adcirc-wide6-reconstruction-checklist.md, efdc-boundary-forcing-checklist.md, efdc-tidal-calibration-order.md, xbeach-first-storm-baseline-checklist.md

각 노트는 위 checklist 적용해 manifest 의 classification 컬럼 기록.

### P2. methods/<model>-sources/ catalog (H2 반영)

`adcirc-sources/` 32 + `xbeach-sources/` 3 = 35 catalog 노트.

#### 분리 정책

각 노트를 두 layer 로 분리:
- **Raw artifact index** → `models/<MODEL>/manual-notes/index/<##>-<topic>.md`. citation_status: verified — 단 raw artifact (manuals/PDF, github URL, examples) 가 `models/<MODEL>/raw/` 또는 외부 URL 로 검증 가능할 때만.
- **Interpretive note** (사용자 분석·요약) → 동일 파일 안 §해석 섹션, 또는 별도 `manual-notes/notes/<##>-<topic>.md` (citation_status: verified 단 source-analysis 기반)

#### 각 노트의 manifest 필드

| 필드 | 의미 |
|---|---|
| `source_id` | textbook/sources.yml 등록명 (없으면 신규 추가) |
| `raw_path` | `models/<M>/raw/manuals/<file>` 또는 외부 URL |
| `raw_sha256` | (raw 가 본 위키 내 파일이면) — 없으면 null |
| `captured_date` | acquired 일자 |
| `audit_status` | `audited` (raw 확인 + claim ↔ raw 매핑 가능) / `unaudited` (raw 없거나 매핑 안 됨) |
| `citation_status` | audited=verified, unaudited=source-needed |

→ **raw artifact 부재 시 verified 금지**.

### 2a Migration manifest schema (H3+J1+K1+L1 반영) — 14 컬럼

`_staging/manifests/phase2a-manifest.csv`:

| 컬럼 | 의미 |
|---|---|
| `source_path` | _staging 안 원본 경로 |
| `dest_path` | 목표 위치 (skip-readme 의 경우 `_archive/.../<orig>` 또는 empty) |
| `sha256_before` | promote 전 source 파일 sha256 |
| `classification` | P1 checklist 결과: source-analysis / experience-mixed / experience-only / manual-notes-catalog / **skip-readme** |
| `citation_status_target` | verified / source-needed (skip-readme 의 경우 `n/a`) |
| `audit_status` | audited / unaudited (catalog 노트 한정, 그 외 empty) |
| `source_id` | textbook/sources.yml 등록명 (catalog 노트 한정) |
| `raw_path` | catalog raw artifact 경로 또는 URL |
| `raw_sha256` | raw artifact 가 본 위키 내 파일이면 sha256 |
| `captured_date` | raw artifact acquired 일자 |
| **`claim_mapping_verified_by`** | (L1 신규) verified 인 row 의 claim ↔ raw artifact 매핑을 누가·언제 확인했는지. 허용 값: `user-<name>-<YYYYMMDD>`, `codex-review-<session_id>`, `self-cited-line-<file>:<line>` (본 위키 내 노트가 src code line 직접 인용 시) |
| **`codex_evidence_sha256`** | (O2 신규) `claim_mapping_verified_by = codex-review-*` 인 row 만 사용. `_archive/codex-reviews/<session_id>.output` 의 sha256 hash. validator 가 archive 파일의 실제 sha256 + `_archive/codex-reviews/sha256sums.txt` 의 hash 둘 다 매치 확인. 다른 form (user-, self-cited-line-) 인 row 는 empty 허용 |
| `link_rewrite_needed` | 본문 안 `_staging/...` 참조 검출 시 갱신 필요 (true/false) |
| `validator_passed` | validate-research-isolation.sh + validate-phase2a-manifest.sh 통과 (true/false) |
| `notes` | 분류·결정의 짧은 사유 (free-form) |

### Enforcement rule (J1+K1 반영)

#### Rule A — manifest row의 verified 강제 조건 (J1+L1)

`citation_status_target = verified` 는 다음 모두 충족 시에만 허용:
1. `audit_status = audited` (catalog 노트의 경우; 그 외 empty 허용)
2. `source_id` 가 textbook/sources.yml 에 등록됨 (또는 본 위키 내부 reference)
3. `raw_path` nonempty
4. `raw_path` 가 local 파일이면 그 파일 존재 + 계산한 sha256 == `raw_sha256`
5. `raw_path` 가 외부 URL 이면 `captured_date` 명시
6. **`claim_mapping_verified_by` nonempty + semantic validation 통과** (L1+M1 반영)
   - 1차: regex `^(user-\S+-\d{8}|codex-review-019e[0-9a-f-]+|self-cited-line-.+:\d+)$` 매치
   - 2차: **semantic validation** (M1 반영) — form 별 추가 check:
     - `user-<name>-<YYYYMMDD>`:
       - YYYYMMDD 가 valid date (datetime.strptime 성공) + 2024-01-01 ≤ date ≤ today
       - `<name>` 가 `tools/manifests/reviewer-allowlist.txt` 또는 본 위키의 git config user.email base 와 매치
     - `codex-review-<session_id>` (N2+O1+O2 강화):
       - **반드시** `_archive/codex-reviews/<session_id>.output` 에 사전 copy 되어있어야 함 (durable). 파일명은 deterministic — session_id 외 prefix/extension 추가 금지 (O1)
       - manifest 의 **`codex_evidence_sha256` 필수** (O2) — empty 시 fail
       - validator check (3 단계, 모두 통과 필수):
         1. `_archive/codex-reviews/<session_id>.output` 파일 존재
         2. 그 파일의 실제 sha256 == manifest 의 `codex_evidence_sha256` (O2 manifest match)
         3. `_archive/codex-reviews/sha256sums.txt` 안 같은 `<session_id>.output` 줄의 hash 도 manifest 와 match (O2 cross-check, 동시 변조 방지)
       - **ephemeral path** (`/tmp/claude-*`, `~/.claude/plugins/.../jobs/...`) 만으로는 verified 거부 — durable archive 필수
       - validator 가 1·2·3 중 하나라도 fail 시 row reject
     - `self-cited-line-<file>:<line>` (N3+O3 강화):
       - `<file>` 가 repo 내 실제 존재
       - `<line>` 이 valid (1 ≤ line ≤ wc -l file)
       - **해당 line 자체** 에 다음 중 하나의 explicit citation marker 가 있어야 함:
         - **HTML comment** (가장 명시적): `<!-- cite:source_id=<id>,raw_path=<path>[,page=<N>] -->` — `source_id` + `raw_path` 모두 명시
         - **Inline citation**: `(<source_id> [§/p.] ...)` 또는 `(<source_id>, ...)` — `source_id` 만 명시. **validator 가 sources.yml 의 `<source_id>` entry 의 `filename` 또는 `raw_path` 를 resolve 해서 manifest 의 `raw_path` 와 일치 확인** (O3 반영)
         - **Source-code reference**: `<file_path_pattern>:<LN>` 또는 `<basename>:<LN>` (예: `wind.F:5798`, `models/ADCIRC/raw/source_code/adcirc/src/wind.F:5798`) — manifest 의 `raw_path` basename 과 매치
       - ~±3 line proximity 만 통과는 거부~ — exact line 의 marker 필수
       - validator 의 각 marker form 별 raw_path 일치 확인 절차:
         - HTML comment: marker 의 `raw_path` 값 == manifest `raw_path` 직접 비교
         - Inline citation: `source_id` 로 sources.yml lookup → `filename` 또는 entry 의 raw_path field 가 manifest `raw_path` 와 prefix-match 또는 equality
         - Source-code reference: marker 의 file:LN 의 file part 가 manifest `raw_path` 의 basename 또는 path 와 매치
       - **모든 marker form 이 raw_path 와 mapping 가능** — O3 reject false-negative 방지
   - 1차 또는 2차 fail 시 → row 의 `validator_passed = false`, Rule A 미통과

위 6 조건 중 하나라도 미충족 → `citation_status_target = source-needed` 강제.

#### Rule B — dest 파일 frontmatter ↔ manifest cross-check (K1+L2 skip-readme order)

Phase 2a validator (`tools/validate-phase2a-manifest.sh` 신설) 의 mandatory check:

1. manifest 의 모든 content row (classification ≠ skip-readme) 에 대해 `dest_path` 파일 존재 확인
2. content row 의 `dest_path` frontmatter 파싱 → `citation_status` 추출
3. **`citation_status (dest frontmatter) == citation_status_target (manifest)` 강제**. 불일치 시 fail.
4. dest frontmatter 가 `verified` 인데 manifest Rule A 6 조건 미통과 → fail.
5. **skip-readme row 의 validation order** (L2 반영):
   - **Pre-archive** (2a.6 시점): dest_path 가 empty 이거나 archive 위치 — frontmatter check **skip**. Rule B 의 1-4 적용 안 함.
   - **Post-archive** (2a.7 이후): archived path (`_archive/.../<orig>`) 존재 확인 + 원본 sha256 (manifest 의 `sha256_before`) 와 archive 의 현재 sha256 일치 확인.

→ copy 단계 (2a.4) 의 template 실수로 verified 인 frontmatter 가 dest 에 들어가도 validator (2a.6) 가 catch.

#### Validator script 명세 (`tools/validate-phase2a-manifest.sh`, L1+M1+M2 반영)

작성 위치: `tools/validate-phase2a-manifest.sh` (thin bash entry) + `tools/validate-phase2a-manifest.py` (Python 본체, validate-research-isolation 과 같은 pattern).

구현 작업 (2a.0 사전 단계):

- (a) python script 가 manifest CSV 파싱 + 모든 row 에 대해 Rule A·B 적용
- (b) **regression fixtures `tools/test_validate_phase2a.py`** — 최소 22 case (M1+M2+N1+N2+N3+O1+O2+O3):
  1. verified pass (모든 조건 + 모든 marker form 합법)
  2. verified fail — `claim_mapping_verified_by` empty
  3. verified fail — `user-fake-20260523` regex OK 인데 date out of range (M1)
  4. verified fail — `codex-review-019e...` archive 부재 (N2)
  5. verified fail — `self-cited-line-fake.md:999` file 존재 X (M1)
  6. verified fail — `self-cited-line-real.md:5` ±3 line 안 source_id 있지만 cited line 에 marker 없음 (N3)
  7. verified fail — sha256_before mismatch
  8. verified fail — dest frontmatter `verified` vs manifest target `source-needed` (Rule B)
  9. source-needed pass
  10. skip-readme pre-archive
  11. skip-readme post-archive
  12. post-archive content row sha256 mismatch (M2)
  13. post-archive set equality fail — missing in archive (N1)
  14. post-archive set equality fail — extra in archive (N1)
  15. N2 ephemeral-only evidence rejection
  16. N2 archived codex output hash mismatch
  17. N3 self-cited-line HTML comment marker pass
  18. N3 false-positive proximity but no marker
  19. **O1 codex archive non-deterministic naming rejected** — `cp $log $(basename $log)` 결과 `.log` 확장자 그대로 → validator reject. Normalized `<session_id>.output` 만 accept
  20. **O2 codex_evidence_sha256 missing fail** — manifest row 의 codex-review row 에서 컬럼 empty → fail
  21. **O3 inline citation marker raw_path resolution pass** — `(pugh-sea-level §6:3 p.194)` 의 source_id 가 sources.yml 의 raw_path 와 일치 + manifest raw_path 와 매치
  22. **O3 inline citation raw_path resolution fail** — sources.yml entry 없음, 또는 sources.yml 의 filename 이 manifest raw_path 와 불일치
- (c) exit codes: 0 (all pass), 1 (Rule A fail), 2 (Rule B fail), 3 (Rule A+B fail), 4 (inventory set equality fail), 5 (post-archive set equality fail — N1), 6 (post-archive sha256 mismatch — M2), 7 (codex evidence archive missing/mismatch — N2+O2), 8 (codex archive naming non-deterministic — O1), 9 (marker raw_path resolution fail — O3)
- (d) 2a 작업 시작 전 위 script + fixtures 모두 작성·통과 확인 → **2a.0 gate**

#### Post-archive integrity check (M2+N1 반영)

2a.7 (archive 후) 별도 mandatory gate. **filesystem set 과 manifest set 양방향 비교**:

```python
# 명확한 pseudo-code (N1 반영)
ARCHIVE_ROOT = Path("_archive/from-modeling-wiki-knowledge-phase2a-2026-05-23")

def archive_path_for(source_path):
    """manifest source_path → expected archive path"""
    return str(ARCHIVE_ROOT / Path(source_path).relative_to(
        "_staging/from-modeling-wiki/knowledge"))

# Set 1: manifest 가 예상하는 archive paths (expected)
expected = {archive_path_for(row['source_path']) for row in manifest}

# Set 2: 실제 filesystem 의 archive 내 모든 파일 (actual)
actual = {str(p) for p in ARCHIVE_ROOT.rglob("*") if p.is_file()}

# Set equality: 누락도 잉여도 없음
missing_in_archive = expected - actual    # manifest 가 기대했는데 없는 파일
extra_in_archive = actual - expected      # archive 에 있는데 manifest 모르는 파일
assert missing_in_archive == set(), f"Missing: {missing_in_archive}"
assert extra_in_archive == set(), f"Extra: {extra_in_archive}"

# Per-file sha256 일치
for row in manifest:
    ap = archive_path_for(row['source_path'])
    assert sha256(ap) == row['sha256_before'], f"sha256 mismatch: {ap}"
```

→ **모든 50 rows** (46 content + 4 skip-readme) 의 archive integrity 확인. content row 누락 / archive 에 stale extra file / sha256 변형 모두 catch.

#### codex-review evidence durable archive (N2+O1 정정)

verified row 중 `claim_mapping_verified_by = codex-review-<session_id>` 인 경우:

```bash
# 2a.0 사전 작업: codex output 을 deterministic naming 으로 durable archive 로 copy
mkdir -p _archive/codex-reviews

# Session ID 추출 패턴 (O1 deterministic):
#   /tmp/claude-*/tasks/<id>.output  → id 추출
#   ~/.claude/plugins/data/codex-openai-codex/state/*/jobs/review-<id>.log → review-<id> 추출
extract_session_id() {
    local path="$1"
    local base
    base=$(basename "$path")
    # tasks/*.output: id 가 그대로 basename without .output
    if [[ "$path" == */tasks/*.output ]]; then
        echo "${base%.output}"
    # jobs/review-*.log: review-<id> prefix 유지
    elif [[ "$path" == */jobs/*.log ]]; then
        echo "${base%.log}"
    else
        return 1  # unsupported format, reject
    fi
}

for log in /tmp/claude-*/tasks/*.output ~/.claude/plugins/data/codex-openai-codex/state/*/jobs/*.log; do
    [ -f "$log" ] || continue
    session_id=$(extract_session_id "$log") || { echo "skip unparseable: $log"; continue; }
    # deterministic name (O1)
    cp "$log" "_archive/codex-reviews/${session_id}.output"
done

# sha256sums 만 normalized filename 으로 (O1)
(cd _archive/codex-reviews && sha256sum *.output > sha256sums.txt)
git add _archive/codex-reviews/ && git commit -m "archive: codex review outputs for phase 2a evidence (deterministic naming)"
```

manifest CSV 의 `codex-review-<session_id>` row 작성 시:
- `claim_mapping_verified_by = codex-review-<session_id>` (extract_session_id 결과 사용)
- `codex_evidence_sha256 = <sha256 of _archive/codex-reviews/<session_id>.output>` (O2 mandatory)

validator 가 위 3 check (file exists, sha256 match, sums.txt cross-check) 자동 수행.

2a 의 step table 에 2a.0 추가 + 2a.7 의 게이트 확장 (다음 §).

### 2a Inventory generation (J4+K2 반영)

```bash
# manifest 의 source_path 컬럼 자동 생성
find _staging/from-modeling-wiki/knowledge -type f > /tmp/phase2a-source-files.txt
# CSV 의 source_path set 과 동일성 확인
diff <(sort /tmp/phase2a-source-files.txt) <(cut -d, -f1 _staging/manifests/phase2a-manifest.csv | tail -n +2 | sort)
# diff 비어있어야 2a.1 gate 통과
```

→ 모든 파일 (README 포함) include/exclude 명시, skip 불가.

#### README 4 disposition (K2+L2 정정)

**실제 inventory** (`find _staging/from-modeling-wiki/knowledge -type f | wc -l`): **50 files = 46 content + 4 README**. adcirc-sources/xbeach-sources 디렉토리 안 README 없음 (4차 codex 확인).

| README | classification | dest_path |
|---|---|---|
| `_staging/from-modeling-wiki/knowledge/failure-patterns/README.md` | skip-readme | `_archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/failure-patterns/README.md` |
| `_staging/from-modeling-wiki/knowledge/heuristics/README.md` | skip-readme | `_archive/.../heuristics/README.md` |
| `_staging/from-modeling-wiki/knowledge/playbooks/README.md` | skip-readme | `_archive/.../playbooks/README.md` |
| `_staging/from-modeling-wiki/knowledge/methods/README.md` | skip-readme | `_archive/.../methods/README.md` |

`skip-readme` row 의 manifest 처리:
- `classification = skip-readme`
- `dest_path` = `_archive/.../<orig>` (post-archive path, pre-archive 에는 존재 안 함)
- `citation_status_target = n/a`
- `audit_status`, `source_id`, `raw_path`, `raw_sha256`, `captured_date`, `claim_mapping_verified_by` = empty
- `link_rewrite_needed` = false (README 안 본문 참조 없음을 grep 으로 사전 확인)
- `validator_passed` = manual confirmation + post-archive 의 sha256 check

#### 콘텐츠 inventory (L2 정정)

**46 content** 의 카테고리 별 정확한 분포:

| 카테고리 | 개수 |
|---|---:|
| `failure-patterns/<adcirc-wide6, efdc-water-level, efdc-wetdry, xbeach-morphology>` | 4 |
| `heuristics/<adcirc-baseline, efdc-friction, xbeach-hydro>` | 3 |
| `playbooks/<adcirc-wide6-reconstruction, efdc-boundary-forcing, efdc-tidal-calibration, xbeach-first-storm>` | 4 |
| `methods/adcirc-sources/01..32` | 32 |
| `methods/xbeach-sources/01..03` | 3 |
| **총** | **46** |

P1 의 failure+heuristic+playbook listing = **11** content (4+3+4), 35 catalog (32+3). 총 46 content + 4 README = 50. v4 의 "45 content + 5 README" 정정.

### 2a 진행 단계 (gated, J2+L1 반영 — validator script 사전 작성)

| Step | 작업 | 게이트 |
|---|---|---|
| **2a.0** | **Validator script + fixtures 작성** — `tools/validate-phase2a-manifest.{sh,py}` + `tools/test_validate_phase2a.py` (6+ regression case). 작성 + 모두 pass 확인 | test EXIT=0 |
| 2a.1 | **Inventory** — `find` 로 source_path 자동 생성, manifest 의 source_path 컬럼과 set equality 확인. README 포함 모든 파일 include/exclude 결정 명시 | diff 비어있음 |
| 2a.2 | manifest 의 `classification`, `citation_status_target`, `claim_mapping_verified_by` 채우기 (P1 checklist + P2 raw artifact gate + L1 evidence) | all content rows 채워짐 |
| 2a.3 | `sha256_before` 계산 (`sha256sum` 일괄) | manifest 의 sha256_before 모두 nonempty |
| 2a.4 | **Copy** (rsync) — `_staging/` 에 원본 유지하면서 dest 에 복제 + frontmatter 추가 (citation_status = manifest target 과 일치하게) | dest 파일 모두 존재, 별도 sha256 verify |
| 2a.5 | **Link rewrite** — 본문 (concepts/·models/·experience/·tools/) 에서 `_staging/from-modeling-wiki/knowledge/...` 참조 grep → 새 경로로 일괄 replace | grep 후 매치 0 |
| 2a.6 | **Validate** — tools/validate-research-isolation.sh + `tools/validate-phase2a-manifest.sh` (Rule A + Rule B) | EXIT=0 모두 |
| 2a.7 | **Archive** — `_staging/from-modeling-wiki/knowledge/` 전체를 `_archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/` 로 atomic mv | rename 성공 + **모든 50 rows** (46 content + 4 skip-readme) 의 archive path 존재 + sha256 == sha256_before (M2 반영) |
| 2a.8 | **Repo-wide link check (post-archive)** — 본문에서 `_staging/from-modeling-wiki/knowledge/` 참조 (구 경로) 검출 시 fail | grep 매치 0 |
| 2a.9 | **(별도 게이트)** Final delete `_archive/.../knowledge/` — 사용자 명시 OK + 1~2개월 유예 | 2a.7 commit + push 성공 + 시간 경과 |

→ **각 step 실패 시 rollback** (2a.7 까지는 _staging archive 보존).
→ **2a.9 는 별도 의사결정 게이트** — phase 마무리에 포함 안 함, plan 의 phase 6 와 동일.

---

## Sub-phase 2b — concepts 갭 보강 (canonical table, H1 반영)

### 단일 canonical table — 모든 후보 파일

`source_needed` 또는 `미생성` 각 파일별 정확한 결정. **J5 반영**: wrapper-only 페이지는 `source-needed` 유지 (partial-verified 도입 보류).

| File | 현재 | source_id / 근거 | claim scope | target |
|---|---|---|---|---|
| `concepts/tides/06-model-application.md` | source-needed | models/ADCIRC + Delft3D source-analysis | **wrapper-only** — 각 모델별 1-2문단 요약 + source-analysis 링크. equation·detail 은 source-analysis 가 canonical | **`source-needed` 유지** (wrapper-only) |
| `concepts/currents/06-model-application.md` | source-needed | 동상 | 동상 | **`source-needed` 유지** |
| `concepts/sst/06-model-application.md` | source-needed | EFDC heat module + Delft3D thermal source-analysis + concepts/sst/02-theory §3 인용 | wrapper + heat budget bulk flux 식 직접 인용 (02 verified 의 인용) | **`source-needed`** (전체 verified 가 안 되므로) |
| `concepts/storm-surge/03-analysis-methods.md` | 미생성 | Pugh §7:8 tide-surge separation + Mann-Kendall (concepts/sst/03 공유) | tide-surge separation 식 (Pugh 직접) + return period (joint Pugh §8:3:3) | `verified` |
| `concepts/storm-surge/05-examples.md` | 미생성 | KHOA Annual Report 2003·2012·2019·2022 §3 — **사용자가 PDF 페이지·표 번호 확인 후 row 별 source_id+page 명시 필요** | KHOA 보고 surge 값 + 본 위키 storm-surge/04 의 코드 인용 | **`source-needed`** (J3 반영, 실 페이지 인용 확보 후 verified) |
| `concepts/storm-surge/06-model-application.md` | 미생성 | 04 wrapper + models/ADCIRC/source-analysis/storm-surge/ 7 노트 인용 | wrapper-only | **`source-needed`** (wrapper-only) |
| `concepts/sediment-transport/05-examples.md` | source-needed | experience/efdc-chuksan-sediment.md (2c) → 분리 | **delegated to experience/** | `source-needed` 유지 (experience 작성 후 본 파일에 인용만 추가) |
| `concepts/littoral-drift/02-theory.md` | 미생성 | textbook/md/Waves-Holthuijsen2007.md Ch 8 radiation stress + Bowen 1969 + Battjes 1974 | radiation stress 직접 인용 (Longuet-Higgins-Stewart 1964) + longshore current 식 | `verified` |
| `concepts/littoral-drift/03-analysis-methods.md` | 미생성 | concepts/sediment-transport/03 + CERC SPM 1984 + Komar-Inman 1970 | tracer experiments, beach profile survey, budget control volume | `source-needed` (학회 자료·CERC PDF 확보 후 verified) |
| `concepts/littoral-drift/04-code-and-tools.md` | 미생성 | models/XBeach/source-analysis + GENESIS 외부 + UNIBEST-LT 외부 | XBeach 인용 + GENESIS·UNIBEST 외부 reference | **`source-needed`** (외부 GENESIS/UNIBEST 인용 cite 전까지) |
| `concepts/littoral-drift/05-examples.md` | 미생성 | 한국 안목항·울산항·태안 — 학회·KMOU 보고서 | 한국 case | `source-needed` |
| `concepts/littoral-drift/06-model-application.md` | 미생성 | XBeach + EFDC SED 인접 | wrapper-only | **`source-needed`** (wrapper-only) |

→ v3 의 verified target = **2 파일만** (storm-surge/03 + littoral-drift/02). 나머지 wrapper-only 또는 외부 source 미확보 = `source-needed`. 정직성 우선.

### 2b 진행 단계

1. canonical table 의 file 별로:
   - 현재 frontmatter 의 `citation_status` 확인
   - 본문 작성·갱신
   - target `citation_status` 부여 (source-needed 또는 verified)
2. INDEX.md 갱신 — 토픽별 (verified/source-needed/미생성) 카운트 갱신
3. CONVENTIONS.md / validate 스크립트 / templates **변경 없음** (J5 Option A 반영 — partial-verified 보류)

---

## Sub-phase 2c — experience 3 신규 노트

### 표

| File | citation_status (강제) | 근거 source | 비고 |
|---|---|---|---|
| `experience/khoa-2024-mhw-extreme.md` | **verified** | data/sst-global/mhw/daily_2024_*.csv (본 위키 fetch + Hobday 알고리즘 검증) | 본 분석 직접, raw 데이터 본 위키 안 |
| `experience/efdc-chuksan-sediment.md` | **source-needed** (M2 강제) | 사용자 메모리 ID 1215 + EFDC source-analysis | 수치 (±1.5 cm/yr, 15년 ±22 cm) 는 **"user memory / anecdotal"** 라벨. raw run outputs 없으면 verified 금지. |
| `experience/khoa-tide-surge-coupling.md` | **verified** (단 KHOA OpenAPI 실 fetch 후) | Hinnamnor 2022 + 다른 한국 태풍의 KHOA `surveyTideLevel` 직접 fetch | tide 예측 (`bscTdlvHgt`) vs 실측 (`tdlvHgt`) residual 분석 |

### 2c 진행 단계

1. C1 (`khoa-2024-mhw-extreme.md`) — daily_2024_events.csv 인용 + KHOA Annual Report 2024 보고 cross-check
2. C2 (`efdc-chuksan-sediment.md`) — **source-needed** 강제, "user memory" 라벨, raw 추가 시 verified
3. C3 (`khoa-tide-surge-coupling.md`) — KHOA OpenAPI 직접 fetch (Hinnamnor 2022-09-06 인천 등 10분 시계열) + 본 위키 storm-surge/02 의 식 검증

---

## Sub-phase 2d — 정책·도구 최종 정리

| # | 작업 |
|---|---|
| D1 | `textbook/sources.yml` 신규 등록: `pugh-sea-level`, `cerc-spm-1984`, `komar-inman-1970`, 기타 source-needed → verified 승격 시 발견된 것 |
| D2 | `tools/sst-cross-check/README.md` — 모든 스크립트 (fetch 4 + analyze 3 + identify 2) 통합 안내 |
| D3 | `_staging/from-modeling-wiki/` 가 비워졌으면 → 디렉토리 삭제, `_archive/` 의 phase2a manifest 만 보존 |
| D4 | `BOUNDARY.md` 상단에 "M4 마이그레이션 완료 (2026-05-23 Phase 1 + 2a-2d)" 헤더 |
| D5 | `INDEX.md` 최종 정리 — 모든 토픽·모델 상태 갱신. 기존 3-tier (draft/source-needed/verified) 만 사용. **partial-verified 표시 제거** (K3 반영, Option A 일관성) |
| D6 | ~~`CONVENTIONS.md §2` 에 `partial-verified` 정책 명시~~ — **Option A 적용으로 skip** (K3 반영). 미래 schema change 시 별도 phase 로 분리 |

---

## 위험·우려 (v3 갱신)

1. ~~`partial-verified` 새 status~~ → **보류** (J5 Option A). 4-tier 도입 회피, wrapper = source-needed.
2. **manifest CSV 작성 비용** — 50 노트 × 13 컬럼 = 650 cells. find 자동 inventory + sha256sum 자동 + classification 만 수동.
3. **link rewrite scope** (J2 반영) — 본문 안 `_staging/from-modeling-wiki/knowledge/...` 참조 검출 grep:
   ```bash
   rg -l "_staging/from-modeling-wiki/knowledge/" concepts/ models/ experience/ tools/ INDEX.md
   ```
   현재 알려진: concepts/storm-surge/01-concept.md, 02-theory.md, concepts/sediment-transport/06-model-application.md.
4. **2c C3 KHOA OpenAPI archive 한계** — `surveyTideLevel` (조위) 의 archive 범위 미확인 (SST 와 다를 수 있음). 2c 시작 시 1차 fetch 시도 → archive 한계 시 대안 (KHOA 백서 직접 인용) 명시.
5. **2a 별도 final delete (2a.9)** — phase 마무리 안 포함, plan Phase 6 와 동일 정책 (1-2개월 유예).
6. **2b verified target 축소** — v2 의 8 verified → v3 의 2 verified (storm-surge/03 + littoral-drift/02). 나머지 6 source-needed 유지. **정직성 vs 진척 속도 trade-off** — v3 가 보수적이지만 코드inference 무결성 우선.

## 검증 대기

이 v8 plan 은 `/codex:adversarial-review` 8차 대기 중. approve 또는 minor-only 받으면 2a 부터 진행.

추이: 1차 6 (high 4) → 2차 5 → 3차 3 → 4차 2 → 5차 2 → 6차 3 → 7차 3 (**high 0**) → **8차 ?**

7차에서 high 사라짐. 8차에서 medium 도 사라지거나 approve 기대.

---

# LLM-Wiki 서빙 레이어 설계 (2026-06-21) — "wiki over RAG" + 멀티머신

작성: Claude Opus 4.8 (1M context) + 사용자 합의
상태: **설계안 (codex 적대검토 대기)**

## 배경·문제

사용자 지적: "관련정보의 LLM-WIKI로서의 기능이 너무 부족". 진단 = coastal-wiki(700 .md·1740 `[[wikilink]]`·`citation_status`·`sources.yml`)는 **콘텐츠·규약은 갖췄으나 검색·서빙(MCP) 레이어가 비어** LLM이 관련정보를 못 꺼냄. G6(qmd 인덱스)는 설계만 있고 미가동.

## Landscape (motivation, 결정근거 아님 — codex F7 반영)

> ⚠ 이 절은 **방향 동기(motivation)**일 뿐 아키텍처 채택의 출처 근거가 아니다(객관 레이어 출처엄격성과 구분). **실제 결정 근거는 Phase 0/1 로컬 PoC 지표**(검색 precision, verified-filter 성공률, stale-index 감지, MCP latency)로 대체한다.

조사(2026-06-21: GitHub repo search + HN Algolia + X/Grok via Hermes x_search) 시사점 — **"wiki over RAG"가 다수 패턴** (Karpathy "LLM Wiki"):
- 파일 우선(markdown + git). 순수 벡터 RAG는 개인/팀 규모엔 과잉 — "80~90% 케이스는 wiki layer로 충분" (desktopcommander 2026 roundup, X/Grok 합의).
- "Obsidian = memory, Claude = reasoning, MCP = bridge" (X 합의).
- 하이브리드 검색으로 **qmd (Tobi Lütke) 거명** → 사용자 기보유 QMD가 트렌드와 일치.
- claim+citation = trust graph / 저장보다 pruning → coastal-wiki 정화철학(G8·바이블)과 동일.
- agent가 wiki를 lint·update하는 루프 (Labhund/llm-wiki Auditor·Adversary).
- ⚠ SurfSense류 클라우드·벡터 NotebookLM 대안은 minimal-setup·local-first와 어긋나 미채택 (RRF·인용 아이디어만 차용).

## 아키텍처 (레이어)

| 레이어 | 역할 | 구현/레퍼런스 | 현황 |
|---|---|---|---|
| L0 콘텐츠 | 바이블 (md+wikilink+citation_status+sources.yml) | coastal-wiki | ✅ |
| **L1 검색** | 하이브리드(BM25+시맨틱) 인덱스 | **QMD** (mcp__qmd__query), G6 | △ 미가동 |
| **L3 MCP 브리지** | `wiki_search`/`wiki_read`(viewport)/`wiki_manifest` | Electro-resonance/LLM-WIKI-MCP, obsidian-vault-mcp 패턴 | ❌ |
| L4 유지보수 루프 | citation_status 자동 adversary·링크감사 | Labhund/llm-wiki 패턴 + 기존 pre-commit validator 확장 | △ |
| L5 수집 루프 | inbox→구조화(claim-evidence-limitation)→promote | 사용자 논문분석 프롬프트 + loop-library "verification-first" | △ collect.py만 |
| L2 그래프 | entity·claim·관계 그래프 | Understand-Anything (Egonex-AI, git JSON 증분, article-analyzer) | ❌ |
| L6 (선택) | 코스탈 전문가 에이전트 양성 | Paideia-Agent (sinmb79) | — |
| 운영 패브릭 | 루프 실행·재인덱스·멀티머신·추적 | Hermes·cron·Fleet Tailscale·Kanban | ✅ |

**핵심: 비어있는 건 L1 가동 + L3 MCP 브리지뿐이고, 그게 페인의 정확한 원인.** 나머지(L2/L4/L5/L6)는 증분 강화.

## 멀티머신 활용 설계 (다른 컴퓨터에서 사용)

전제: CLAUDE.md §동기화 — writer=이 PC(WSL ext4), reader=다른 PC(git clone+pull, **read-only**). Fleet Tailscale mesh 보유.

세 가지 배치 옵션:

| 옵션 | 방식 | 장점 | 단점 |
|---|---|---|---|
| **A. Tailscale 중앙 MCP** (권장) | writer PC(또는 지정 노드)에서 MCP+QMD 1개 가동, Tailscale MagicDNS 호스트명으로 노출. 타 머신 Claude Code/Hermes의 MCP config가 그 호스트 가리킴 | 단일 인덱스(중복 없음)·항상 최신·mesh 그대로 활용·reader는 설정 1줄 | writer 노드 온라인 필요 |
| B. Git 분산 로컬 | 콘텐츠+그래프(JSON)만 git, 각 reader가 pull 후 자기 QMD 인덱스 로컬 재빌드, MCP 로컬 가동 | 오프라인 가능·서버 의존 없음 | 머신마다 인덱스 재빌드 비용·신선도 pull 시점 |
| C. 하이브리드 | A를 기본, git clone을 오프라인 fallback | 온라인=최신 중앙, 오프라인=로컬 | 구성 복잡도 ↑ |

**권장 = A(+C fallback):** mesh가 이미 있으므로 중앙 MCP가 가장 경제적. reader는 `~/.claude/mcp.json`(또는 Hermes config)에 Tailscale 호스트:포트만 등록 → read-only 질의. 인덱스는 writer에서 cron 재빌드 1회 → 전 머신 즉시 최신.

**인덱스 산출물 git 정책:** `knowledge-graph.json`(L2, 작고 diff 가능) = **추적**. QMD 벡터 인덱스(크고 머신·임베딩모델 의존) = **gitignore + cron 재빌드**. 콘텐츠가 SSOT, 인덱스는 파생물(재현 가능).

## 구현 시퀀스 (codex 1차 반영 — gate 분리·전제 검증 선행)

각 단계는 **독립 gate**다. 앞 단계 acceptance 미충족 시 다음 진행 금지(catalog stub 금지·minimal-setup 동형).

- **Phase 0 (전제 검증, 비용 최소)** — ❶ **L1/L3 후보 3-way 벤치마크**: (a) **QMD** (mcp__qmd__query) (b) **SQLite FTS5+metadata** 자체 (c) **Obsidian MCP** off-the-shelf (cyanheads/obsidian-mcp-server=frontmatter+STDIO/HTTP 595★, jacksteamdev 827★, StevenStavrakis 715★). **결정 기준 4개**: ⓐ **헤드리스 가능**(Obsidian GUI 앱·Local REST API 플러그인 상시구동 불필요 — WSL writer·Hermes cron·Tailscale 서빙이 전부 헤드리스라 GUI 의존은 탈락사유) ⓑ frontmatter/`citation_status` 필터 ⓒ corpus scoping ⓓ remote transport. **헤드리스 Obsidian MCP가 4개 통과 시 채택 → L3 자체구축 불필요**(minimal-setup 이득); GUI 의존이면 탈락하고 QMD or FTS5. ❷ **corpus policy 확정**(F4): 검색대상 allowlist(`concepts/`·`models/`·`textbook/`·`experience/`) / denylist(`research/`·`_staging/`·`_archive/`·`raw/`), 결과에 `citation_status`·path-class 필수 반환, **default = verified+canonical**, research/staging/archive는 명시 옵션 없이는 제외.
- **Phase 1 (토대, 로컬 read-only PoC만)** — L3 최소셋을 **로컬 stdio MCP**로: `wiki_search`(rg + frontmatter 필터 기반, Phase 0 결과 따라 QMD or FTS5), `wiki_read`(viewport: section/grep/full, **realpath sandbox=repo root**, read-only), `wiki_manifest`(INDEX 계층 + **repo git sha·index sha/timestamp·dirty 여부·indexed file count 반환**, F3). **QMD·Tailscale·cron 제외**. acceptance = 검색 precision·verified-filter·stale 감지 PoC 지표 충족.
- **Phase 1b (인덱싱 gate)** — Phase 0서 QMD 합격 시 QMD 인덱싱 결선, 불합격 시 FTS5. **SSOT = clean working tree + last committed git sha**(F3) — 서빙은 commit 기준, uncommitted draft 노출 금지. 재인덱스 = 큰 변경 후 수동/post-commit hook(G6 기조).
- **Phase 1c (멀티머신 gate, 별도 PoC)** — remote MCP transport(stdio→SSE/HTTP adapter) 검증 후에만 옵션 A. **read-only 전용 바이너리/config 분리**(F5: realpath sandbox·denylist·Tailscale tag ACL·bind 제한·request log·optional token). write 도구는 writer PC localhost only.
- **Phase 2** — L5: 사용자 논문분석 프롬프트를 coastal-promote "구조화 추출(claim-evidence-limitation)" 단계로.
- **Phase 3** — L4: citation_status 자동 adversary·링크감사 = Hermes cron + Kanban(기존 validator 확장).
- **Phase 4** — L2: Understand-Anything claim/entity 그래프. **산출물 git 추적 여부는 이 gate에서 결정**(F8: deterministic+compact+provenance-preserving일 때만 추적; source-needed/research claim 혼입 시 별도 오염면이므로 배제).
- **Phase 5 (선택)** — L6: Paideia로 L0~L3 교재화 전문가 에이전트.

## 위험·우려 (codex 1차 반영)

- **W1 QMD 능력 미검증 의존**(F2 HIGH): L1=QMD를 전제로 두면 verified-filter·source_id provenance가 가정 위. → Phase 0 capability matrix gate, 실패 시 FTS5 fallback 기본값.
- **W2 SSOT/single-writer**(F3 HIGH): 중앙 MCP가 working tree 직독 시 reader가 미커밋 draft·검증전 변경 노출. cron 인덱스도 commit 기준과 어긋난 stale snapshot. → 서빙 기준 "clean tree + committed sha", manifest에 sha/dirty/timestamp 노출. write는 writer localhost only.
- **W3 검색 scope = canonical purity**(F4 HIGH): research/staging/archive/source-needed/raw vendor가 같은 검색면에 섞이면 신뢰등급 소실(CONVENTIONS §research 격리·G8). → corpus allowlist/denylist + citation_status 필수 + default verified+canonical.
- **W4 Phase 범위 과다**(F1 HIGH): 원 Phase 1이 QMD+MCP+Tailscale+cron 동시. G6는 "수동 재빌드·일상은 rg로 충분" 이미 결정. → Phase 0/1/1b/1c gate 분리, Phase 1=로컬 read-only PoC.
- **W5 Tailscale 보안 과신**(F5 MED): ACL은 네트워크 경계일 뿐 path traversal·과도 read scope·실수 write·타 장비 compromise 미방어. → read-only 분리·sandbox·denylist·tag·bind·log·token을 Phase 1c acceptance에.
- **W6 remote transport 전제화**(F6 MED): 옵션 A 성립조건(qmd remote transport)이 미검증. → Phase 1c 별도 PoC, Phase 1은 local stdio로 tool contract만 고정.
- **W7 도구 증식 vs minimal-setup**: L2·L6 의존성↑. Phase 1으로 페인 해소되면 ROI 보고 결정.
- **W8 단일점**: writer 오프라인 시 reader 질의 불가 → 옵션 C(git clone 오프라인 fallback).

## 미결 사항 (Phase 0 입력)

- L1/L3 3-way 벤치마크: QMD vs FTS5 자체 vs **Obsidian MCP**(cyanheads 등). 핵심 변별 = **헤드리스 가능 여부**(Obsidian GUI 앱 의존이면 WSL/cron/Tailscale 자동화 부적합) + frontmatter 필터 + corpus scoping + remote transport.
- 헤드리스 Obsidian MCP가 통과하면 L3 자체구축 생략(off-the-shelf 채택). 참고: 2023Anita/obsidian-llm-knowledge-base (Karpathy LLM KB + Obsidian 워크플로 가이드).

## 검증 이력 — Codex Adversarial Review

**1차 (2026-06-21): 8 findings (high 4 / medium 3 / low 1).** 방향 승인, Phase 1 gate 부족 지적. 전 findings 반영 완료:
- F1(HIGH 범위과다)→Phase 0/1/1b/1c gate 분리, Phase 1=로컬 read-only PoC.
- F2(HIGH QMD 미검증)→Phase 0 capability matrix + FTS5 fallback 기본값.
- F3(HIGH SSOT)→서빙 "clean tree+committed sha", manifest sha/dirty/timestamp.
- F4(HIGH purity)→corpus allowlist/denylist + citation_status 필수 + default verified+canonical.
- F5(MED 보안)→read-only 분리·sandbox·denylist·tag·bind·log·token (Phase 1c).
- F6(MED transport)→Phase 1c 별도 PoC, Phase 1 local stdio only.
- F7(MED 근거)→Landscape를 motivation으로 격하, 결정근거=PoC 지표.
- F8(LOW 그래프 추적)→Phase 4 gate로 이연, deterministic+provenance 조건부.

**1차 후 보강 (2026-06-21, 사용자 지적):** Obsidian-네이티브 서빙 누락 → Phase 0 **L1/L3 3-way 벤치마크에 Obsidian MCP**(cyanheads/obsidian-mcp-server frontmatter+HTTP 595★ 등) 1급 후보로 추가. 결정 변별 = **헤드리스 가능 여부**(GUI 앱 의존이면 WSL/cron/Tailscale 부적합). 통과 시 L3 자체구축 생략.

**다음:** Phase 0(L1/L3 3-way 벤치마크 + corpus policy) 착수 → 결과 보고 후 Phase 1 PoC. (필요 시 2차 적대검토.)

