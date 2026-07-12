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

### G6. 검색 인덱싱 (2026-06-21 갱신 — qmd→FTS5)

- **구현 = `coastal-wiki` MCP** (`tools/llm-wiki-poc/`, SQLite FTS5 순수 stdlib). `wiki_search`/`wiki_read`/`wiki_manifest`. 상세: [plan.md "LLM-Wiki 서빙 레이어 설계"](plan.md).
- 인덱스(`*.db`) = 파생물, **gitignore + 기동 시 자동 재빌드(~0.5s)**. 정기 cron 불필요(단일 writer; 큰 변경 후 재빌드).
- corpus = canonical allowlist(concepts/models/textbook/experience), research·_staging·_archive·raw 제외. frontmatter `citation_status`·`path_class` 필터.
- ~~`qmd embed`/`mcp__qmd__`~~ = **미설치 stale**. Phase 0 벤치마크서 QMD 미설치 확인 → FTS5 채택(헤드리스·의존성0·4기준 통과).
- 일상 키워드 검색은 `rg`/grep 으로도 충분.

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

### G9. disclosed-gap 정책 — verified + 기계가독 갭 플래그 (2026-06-21, L4 V1 실감사 발견 → 하이브리드, **Codex 1차 needs-attention 반영, 재검토 대기**)

**문제:** `wiki_search` 는 파일 단위 `citation_status` 를 반환하는데, currents/02~06 처럼 `verified` 파일이 내부에 미확정 절(예: 한국 조류 typical값·KHOA OpenAPI endpoint·모델 forcing 포맷)을 품는 경우가 실재. 파일 한 줄 "verified" 가 그 절들에 대해 과함. 한편 모든 절 100% sourced 강제 시 위키 거의 전부 탈락(frontier 갭은 정상) — 솔직한 disclosure 는 오히려 좋은 인식론. 코퍼스에 `partial-verified`·`partially-verified` 각 1건(오타 표기 흔들림) 잔존 = 이 긴장을 누군가 이미 손으로 반친 증거.

**Codex 1차 적대검증(needs-attention, no-ship as written):** 순수 명문화(A)는 `verified` 의 의미를 약화시키면서 그 약화를 **소비자(`wiki_search`)가 볼 방법을 안 줌** → trust-boundary 후퇴. 라벨이 노출 증거보다 강해짐(정화철학 G8 모순). 처방 = 별도 status(C) 또는 검색층 갭 메타데이터(B) 중 하나로 **갭을 기계가독화**.

**결정(하이브리드 — A 정신 + 최소 기계가독 신호):** status 택소노미 증가(C)·검색층 sub-file 파싱(B 전체) 둘 다 회피하되, frontmatter 불리언 1필드로 trust-boundary 복원.

- **G9a verified 정의** (CONVENTIONS §2 보강): `verified` = **모든 사실 단언이 (a)출처 인용 또는 (b)`source-needed` 로 명시적 in-text 표기. 미출처 AND 미표기 = 0.** 갭이 있어도 *disclosed* 면 verified 유지 — 단 G9e 플래그 필수.
- **G9b disclosure 마커**: 절·문장에 `source-needed` 문자열 포함 disclaimer 또는 `> [!source-needed]` 콜아웃(lint·audit 가 undisclosed 와 구분 가능하게). 산문 암시만으로는 불충분, 명시 토큰 필요.
- **G9e 기계가독 갭 플래그 (Codex 반영 핵심) — 명확한 트라이스테이트**: `has_source_needed` 의 직렬화 값은 **정확히 3상태, 생략은 단 하나의 의미**(Codex 2차 반영):
  - `true` = **L4 감사됨 + disclosed 갭 보유**
  - `false` = **L4 감사됨 + 완전 sourced** (완전 sourced여도 **`false` 명시 필수 — 생략 불가**)
  - **필드 부재 = "미감사(unknown)" 단 하나의 의미** — 완전 sourced 로 단정 절대 금지
  **`wiki_search`·`wiki_manifest` 가 이 값을 그대로 반환**(true/false/부재 구별). 소비자는 부재 시 완전성 주장 불가. status 택소노미 불변·검색층 sub-file 파싱 불요(frontmatter 1필드).
- **G9f 호환·마이그레이션 규칙**: 기존 `verified` 소비자 — `has_source_needed` 부재 = unknown(미감사), 보수적 해석(완전 sourced 단정 금지). L4 감사가 **모든 감사된 verified 파일에 `true`/`false` 를 명시 기입**(omission→확정). `wiki_manifest` 가 verified 중 (true/false/부재) 3분 카운트 = **감사 커버리지** 노출 → 과도기 가시화. **구현 게이트**: 플래그 파싱·반환 배포 전, 또는 직후 우선과제로 verified 전수 L4 백필(부재 0 목표). currents/02~06 은 이미 감사·disclosed 갭 → `has_source_needed: true` 1차 백필.
- **G9c L4 mandate 확정**: `coastal-audit`(L4)의 INTEGRITY-VIOLATION = verified 파일의 **미출처 AND 미disclosed** 단언. disclosed 갭은 verified-confirmed(refute) + `has_source_needed: true` 자동 set/검증. 제안 패치 = 인용 추가 *또는* disclosure 마커 추가. (실증: currents/01 §7 undisclosed→위반·수정 / 02~06 disclosed→통과.)
- **G9d status 정규화**: `partial-verified`/`partially-verified` 2건 → 미상 일괄처리 금지(G9a 위반). **개별 L4 감사 후** disclosed→`verified`+`has_source_needed:true` / undisclosed→`source-needed` 로 정규화.

**근거:** ① disclosed 관행은 이미 운영 중(compound-flooding/01) — 명시일 뿐 ② G9e 가 trust-boundary 복원(Codex 해소): 라벨 강도 ≤ 노출 증거 ③ minimal-setup 보존: 새 status·검색 파싱 없이 frontmatter 1불리언 ④ L4 가 플래그 집행기 ⑤ Diátaxis·FAIR·Matuschak honest uncertainty 정합.

**적용 시 편집 대상**: CONVENTIONS §2(verified 정의+마커+`has_source_needed`), `mcp_server.py`/`fts5_index.py`(frontmatter `has_source_needed` 파싱·검색/manifest 반환), `coastal-audit` SKILL.md(G9c·G9e mandate), validate-canonical-hygiene(G9b undisclosed 탐지·G9e 플래그 정합 lint 후보), partial-verified 2건 개별 정규화. **santa-method**: 본 개정 → `/codex:adversarial-review` 재검토 → 반영 → 편집.

## 미결 사항

- textbook 자료 13권 중 어느 것부터 노트화할지 우선순위
- private repo 호스팅(GitHub/GitLab/self-hosted) 결정
- modeling-wiki → coastal-wiki/experience/ 마이그레이션 시점 결정
- experience/ 레이어 실작성 시점 (객관 레이어가 얼마나 채워진 후)

## 검증 이력

- 2026-05-21: 초기 plan → Codex adversarial review → MODIFY 판정 → Governance Decisions G1-G7 추가
- 2026-06-18: 대규모 canonical 정화 → Codex adversarial review(MODIFY) → 반영 후 Codex 최종 review(MODIFY, 정합성 4건) → 반영 → G8(a-d) 추가
- 2026-06-21: L4 자가 감사 V1 currents 실감사 → disclosed-gap 긴장 발견 → G9 정책 기록(A안) → Codex 적대검증 **needs-attention(trust-boundary 후퇴)** → 하이브리드 개정(G9e `has_source_needed` 플래그) → Codex 2차 **needs-attention(생략 의미 모순: G9e "false/생략" vs G9f "생략=미상")** → 트라이스테이트 명확화(true/false/부재 각 1의미, 완전sourced도 false 명시). **Codex 3차 재검토 대기 중.**
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

**실측 mesh (2026-06-21 `tailscale status`):** wsl-rag(100.83.117.111 linux)=**writer/서빙 노드** / desktop-64pt1f7·desktop-rop5h5e(windows 온라인) / desktop-rop5h5e-1(linux offline) / ipad171·iphone171(iOS). repo=GitHub `firesinger82/coastal-wiki`. **인덱스 재빌드 = 0.48s**(어느 머신서든, markdown만 있으면).

**권장 = 하이브리드(0.48s 재빌드가 default를 바꿈):**
- **데스크톱/리눅스 → 방식 1 (Git 분산 + 로컬 재빌드)**: `git pull` → FTS5 인덱스 로컬 재빌드(0.48s, post-merge hook 또는 MCP 기동 시) → **로컬 stdio MCP(read-only)**. 완전 오프라인·서버의존0·원격transport 불필요·**pip 설치 불필요(stdlib only)**. 0.48s라 "중앙 서버 필수"가 아님.
- **iOS·"항상 최신" → 방식 2 (Tailscale 중앙 HTTP MCP)**: wsl-rag에서 FTS5-MCP를 HTTP/SSE로 100.83.117.111(MagicDNS `wsl-rag`)에 바인드, 타 머신 mcp.json이 가리킴. iOS는 python 불가라 이 방식만 가능. ACL=tailnet 내부 한정.
- **공통**: reader 전부 **read-only**(search/read만), write는 wsl-rag에서만 → single-writer 보존.

**인덱스 산출물 git 정책:** FTS5 인덱스(`*.db`, 머신·tokenizer 의존, 0.48s 재생성) = **gitignore + 로컬 재빌드**. `knowledge-graph.json`(L2, 작고 diff 가능)은 Phase 4 gate서 결정(F8). 콘텐츠가 SSOT, 인덱스는 파생물.

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

## Phase 0 벤치마크 결과 (2026-06-21 실측)

PoC: `tools/llm-wiki-poc/fts5_index.py` (511 canonical docs 인덱싱 0.47s / 19MB).

**환경 실측:** QMD = **미설치**(바이너리·패키지·MCP설정 전무 — CLAUDE.md G6의 `mcp__qmd__query`는 설계만, 실제 가동된 적 없음). SQLite FTS5 = **즉시 가능**(3.45.1, stdlib, 신규의존 0). Node v22 OK, coastal-wiki는 실제 Obsidian vault(`.obsidian/`).

**3-way 판정 (4 기준):**

| 후보 | ⓐ 헤드리스 | ⓑ frontmatter 필터 | ⓒ corpus scope | ⓓ transport | 판정 |
|---|---|---|---|---|---|
| QMD | ? (미설치) | ? | ? | ? | 보류 — 설치+평가 필요, semantic만이 차별점 |
| **FTS5 자체** | ✅ stdlib | ✅ **실측**(verified 419 필터·BM25 랭킹) | ✅ **실측**(research/_archive/raw=0) | ✅ wrapper(stdio/http) | **PASS (all 4)** |
| Obsidian MCP | ❌ **GUI앱+REST플러그인 필요**(cyanheads·jacksteamdev·StevenStavrakis·aaronsb 전부) | ✅(REST) | △(설정) | ✅ | 헤드리스 탈락 → 자동화 백본 부적합 |

**결론:**
- **L1 = FTS5 자체 채택** (헤드리스 백본; 4 기준 실측 통과, 의존성 0). BM25 keyword-only가 한계지만 consensus("개인 KB엔 벡터 과잉, 텍스트검색 80% 충분")와 정합. semantic 필요 시 동일 DB에 sqlite-vec 증분(후속).
- **Obsidian MCP = 보조(interactive desktop)로만** — 사용자가 Obsidian 앱 켜둔 머신에서의 대화형 편의용. cron/Tailscale 헤드리스 서빙 백본은 아님.
- **QMD = 미채택** (미설치 + FTS5가 이미 기준 충족; 설치 ROI 낮음). ⚠ CLAUDE.md §검색·G6의 `mcp__qmd__query` 참조는 **stale** → 후속 정정 필요.
- **부수 발견(데이터 위생):** citation_status 값에 `partial-verified`(1)·`partially-verified`(1) 비표준 혼용 + 빈값 74(주로 README/template). 표준 enum(draft-unsourced/source-needed/verified)과 어긋남 → L4 validator에서 enum 강제 후보.

**다음:** Phase 1 = FTS5를 **로컬 stdio MCP**로 래핑(`wiki_search`/`wiki_read`/`wiki_manifest`, read-only sandbox, manifest에 git sha/dirty/timestamp). corpus policy(Phase 0 ❷)는 PoC에 이미 구현(allowlist/denylist + citation_status 반환).

## Phase 1 결과 (2026-06-21 — 로컬 stdio MCP 완성)

`tools/llm-wiki-poc/mcp_server.py` — **순수 stdlib** newline-delimited JSON-RPC 2.0 stdio MCP, read-only. 다른 머신서 pip 설치 불필요(방식 1 정합, system python3 3.12 + FTS5 stdlib 확인). `.mcp.json`에 `coastal-wiki` 등록.

**E2E 실측 통과:** initialize(protocol 2024-11-05) → tools/list(3종) → `wiki_search`('storm surge ADCIRC coupling', status=verified → 3 hits, BM25) → `wiki_manifest`(git_sha + **dirty_working_tree** + doc 511 + verified 419, **F3 충족**) → `wiki_read`(section/grep/full). **보안(F5) 실측:** `../../etc/passwd` 차단·`research/` denylist 차단.

**도구 3종:** `wiki_search(query,status?,path_class?,k?)` / `wiki_read(path,mode=section|grep|full,pattern?)` realpath sandbox / `wiki_manifest()`.

**다음:** ① Claude Code 재기동해 MCP 활성화·실사용 검증 ✅**② post-merge/post-checkout git hook 자동 재빌드 완료**(install-hooks.sh, 방식1 멀티머신; clone 후 1회 실행→pull마다 0.5s 재인덱스) ✅**④ stale 정정 완료**(CLAUDE.md §검색·G6→FTS5) ③ Phase 1c = HTTP/SSE transport(iOS·중앙, 방식2) ⑤ Phase 2(L5 수집루프).

## 랭킹 튜닝 — textbook/md 원문 강등 (2026-06-21, commit a80f7de)

**문제:** `textbook/md/<file>.md`(PDF→md 원문 덤프, 19건)는 POLICY.md §"텍스트 추출"상 페이지 lookup·AI cross-ref용으로 **의도적으로 인덱싱**되지만, 순수 BM25에선 원문 전문이 정제 노트보다 상위로 뜨는 경우 발생(예: `Holthuijsen waves shallow water` 쿼리에서 `Waves-Holthuijsen2007.md` bm25 `-8.511`이 `concepts/littoral-drift/01`·`-8.324`보다 위). reference(원문)↔정제(notes·source-analysis·manual-notes·concepts)의 우선순위 역전.

**방식 (deterministic tier 강등):** FTS5 bm25는 음수(낮을수록 우수). raw dump에만 `tier=RAW_DEMOTE(+1000.0)` 컬럼 부여 → `ORDER BY bm25(idx)+tier`. raw dump는 어떤 매치에서도 정제 문서 전체 **아래 티어**로 고정, 같은 티어 내부는 BM25 순서 유지. 노출 `score`는 순수 bm25 그대로(투명성 보존), 강등은 정렬에만 적용. 판별 = `is_raw_dump(rel)`(`textbook/md/` 한정; `raw/`는 이미 denylist 제외라 인덱스 밖).

**효과(실측):** `Holthuijsen` 쿼리에서 `Waves-Holthuijsen2007.md`가 7위→12위(맨 끝)로 강등, bm25가 더 나쁜 정제 문서들이 모두 그 위로. **원문은 여전히 검색·노출됨**(페이지 lookup 유지), 단 동일 매치에선 항상 후순위. `fts5_index.py`: `is_raw_dump`/`RAW_DEMOTE`·fts5 `tier` 컬럼·query 정렬식 3곳 수정. 근거 = Diátaxis reference↔how-to/explanation 분리 원칙의 검색층 반영.

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

---

# L4 자가 감사 루프 PoC 설계 (2026-06-21) — citation_status adversary

LLM-Wiki 4계층(L1 검색·L2 graph·L3 MCP·**L4 유지보수 루프**) 중 L4의 최소 PoC. 현재 coastal-wiki는 수동 서빙(L1/L3 ✅)까지 완성, **AI 자율 감사 루프는 미착수**. 본 설계 = "밤마다 도는 사서 AI"(V3)의 한 iteration을 손으로 돌려보는 V0.

## 빈틈 특정 (기존 자산 비중복)

결정론적 pre-commit 검증(링크·wikilink resolve·G8b 로컬경로·G8d placeholder·research 참조)이 **못 잡는 단 하나** = CLAUDE.md 절대규칙 #1의 의미 판단: canonical(`concepts/`·`models/`)의 **모든 단언은 출처 인용 필수** — "이 문장이 출처 없는 단언인가/인용된 사실인가/의견인가"는 정규식 불가, LLM 판단 필요. **PoC 범위 = 이 빈틈 하나만**(plan.md L4 "citation_status 자동 adversary").

## 설계 원칙 4

1. **Report-only, auto-edit 금지** — single-writer·무결성 규칙상 에이전트가 canonical 직접 수정 불가. 산출물 = 지적 리포트, 사람이 게이트.
2. **AI는 판단만, 배관은 결정론적** — 파일선택·집계·상태추적=스크립트. LLM은 "이 단언 출처 있나?"만.
3. **가장 작은 슬라이스** — 1회 실행 N=5–10파일, ledger로 변경분만 점진 소진(=루프). 전수 1방 금지(W4 회피).
4. **minimal-setup** — cron/autonomous 아님. `coastal-promote`처럼 수동 트리거 스킬(`coastal-audit`)로 먼저. 자율은 신뢰 축적 후.

## 통합 루프 V0 (단일 감사 + verdict 분기)

타깃 "verified 적대 감사"와 "빈/source-needed 분류"는 별개 파이프라인 아님 — **AI 작업은 동일하게 "각 단언에 출처 있나?" 한 패스**, 차이는 결과를 현재 citation_status와 대조하는 결정론적 verdict뿐.

```
[Selector] 결정론적: verified ∪ (빈/source-needed) 중 변경된 슬라이스 N파일 (git sha vs ledger)
   ▼
[Auditor] AI 1패스: 각 단언 → {sourced / UNSOURCED / opinion}  (현재 status는 미열람 — 편향 방지)
   ▼
[Adversary] AI: UNSOURCED 플래그만 refute 시도 → 반박 실패분만 confirmed (precision 우선)
   ▼
[Verdict] 결정론적 매트릭스 (아래)
   ▼
[Report] _staging/audit/L4-<date>.md (file:line·단언·사유·verdict) + ledger 갱신(파일별 audited_sha)
   ▼
[Human gate] 사람이 리포트 보고 출처 보강 / 강등 / 승격 결정
```

**Verdict 매트릭스** (현재 status × 미출처 단언 수):

| 현재 citation_status | 미출처 | 판정 | 성격 |
|---|---|---|---|
| `verified` | >0 | ⚠ **무결성 위반**(verified 거짓) — 강등 or 출처 보강 | 적대 감사 |
| `verified` | 0 | ✅ verified 재확인 | — |
| 빈/`source-needed` | 0 | ⬆ verified 승격 후보 | 분류 정리 |
| 빈/`source-needed` | >0 | ↻ source-needed 유지(작업목록) | 분류 정리 |
| any | 실질 단언 0 | 🏷 scaffolding(README 등)·면제 표시 | 분류 정리 |

## 상태 = ledger 1파일
`_staging/audit/ledger.json` = `{ "<path>": {"audited_sha": "...", "verdict": "clean|N findings"} }`. 미변경 파일 skip → 반복 실행이 곧 루프(슬라이스 점진 소진).

## Acceptance (타깃별 분리)
- **무결성 위반 행**(verified×미출처): **precision ≥ 0.8** 必(오탐=신뢰 타격). Adversary 단계 필수.
- **분류 행**(빈/source-needed): precision 느슨 OK(제안일 뿐, 사람 승인). recall 우선.
- 1슬라이스 완주 + ledger 기록 + 사람 1회 검수.

## 성장 경로 V0→V3
| | 트리거 | 범위 | 산출 | 상태 |
|---|---|---|---|---|
| **V0** | 수동 스킬 `coastal-audit` | 변경된 N파일(혼합 status) | 리포트만 | ✅ 구현·dry-run 실증 |
| **V1** | 수동 + 라운드로빈 | 전 canonical 회전 | 리포트 + 제안 패치(미적용) | ✅ 구현·테스트 |
| V2 | post-commit hook | 커밋된 파일만 | 리포트 + pre-commit 경고 통합 | 미착수 |
| V3 | cron(야간 04:00) | 전수 + 신규(라운드로빈) | 자율 감사, 사람은 리포트만(=사서 AI) | ✅ 러너 구현·e2e 검증·**crontab 설치(2026-06-22)** |

### V1 결과 (2026-06-21 — 라운드로빈 + 제안 패치)

- **라운드로빈**(`select_audit.py`): slice 항목에 `reason`(new/changed/rotation) 부여. changed/new 우선(verified 먼저) → 남은 슬롯을 rotation(가장 오래 감사 안 된 순)으로 채움. 정적 verified(대다수)가 1회 감사 후 영영 안 도는 V0 맹점 해소 — 전 canonical 순환 감사. `--changed-only` = V0 동작. 실측: 전 407파일 ledger 충전 시 changed 0·rotation_pool 407·slice=오래된순 5 PASS.
- **제안 패치**(`record_audit.py`): findings 의 `proposals:[{old_string,new_string,rationale}]`(Edit식, old_string=committed verbatim)을 committed 본문(SSOT, `git show HEAD:`) 대비 git-apply 가능한 unified diff 로 렌더 → `_staging/audit/proposals/L4-<date>-<HHMMSS>.patch` **생성만**(절대 미적용, report-only). old_string 0/다중 매치는 "수동 처리"로 표기(깨진 패치 금지). 실측: 실파일 패치 생성 + `git apply --check` PASS + 워킹트리 무변경 PASS.
- 적용은 **항상 사람**(`git apply` 검토 후). 자동 적용·pre-commit 통합(V2)은 미포함.
- **Codex review 2차 반영**: ① 라운드로빈 정체(`audited_date` 날짜 해상도라 같은 날 반복 시 동일 N개 재선정) → ledger 에 마이크로초 `audited_at` 기록·rotation 정렬 키로 사용(같은 날도 전진). ② 동일 파일 다중 proposal 패치 무효(각 edit 을 원본서 독립 diff → 인접 hunk context 겹침) → 단일 버퍼 순차 적용 후 1회 diff. 실측: 같은 날 run2 전진(겹침 0)·인접 2줄 단일 hunk `git apply --check` PASS.

**다음:** V2(post-commit hook 통합) 또는 textbook/experience 대상 확장. (V0·V1 모두 Codex 2-round 검토 반영 완료.)

### V3 구현 (2026-06-21 — 야간 자율 cron 러너)

런타임 결정: coastal-audit 은 **Claude Code 스킬**이라 V3 = `claude -p "/coastal-audit --n N"` **headless** 호출(Hermes `fin -z` 야간 패턴과 동급, 단 Claude Code CLI 사용). Hermes(별 에이전트·별 skills dir)가 아님. cron = 시스템 crontab.

러너 `tools/llm-wiki-audit/run-audit-cron.sh` (report-only 이중 차단):
1. **사전조건 가드**: `_staging/audit/` 외 미커밋 변경 있으면 `exit 2` (writer 작업 중 충돌·오염 방지). — DRY 실증: 미커밋 시 정확히 abort.
2. `git pull --ff-only`(divergence 시 경고·현 HEAD 진행) → `claude -p` headless(`--permission-mode acceptEdits`, `--allowedTools Read,Bash,Write,Skill,Glob,Grep`).
3. **하드 가드**: 실행 후 `_staging/audit/` 외 모든 tracked 수정은 `git checkout -- . ':(exclude)_staging/audit'`로 복원, *이번 run 이 새로 만든* untracked 만 제거(실행 전 스냅샷 diff). 1차 보장은 커밋 스코프(`git add _staging/audit/` + 스테이징 assert) — 가드가 뚫려도 canonical 은 history 에 안 들어감.
4. `_staging/audit/` 만 커밋(감사 메타=canonical 아님), **push 안 함**(사람 검토). 로그·lock 은 `_staging/audit/cron-logs/`(gitignore).
5. flock overlap 차단. env: `L4_DRY_RUN`·`L4_NO_COMMIT`·`L4_AUDIT_N`·`COASTAL_WIKI_DIR`.

**적대검토(2026-06-22, 자체 — Codex 2회 hang 으로 대체):** 발견·반영:
- ★치명: 초기 하드닝의 blanket `git clean -fd` 가 **Hermes research/inbox·_archive·_staging/from-modeling-wiki·작성중 모델노트 등 정상 untracked 워크벤치를 매일 파괴**(`-fdn` 미리보기로 적발). 동일 원인으로 step0 도 untracked 때문에 매번 abort. → step0=tracked 수정만 검사, step3=스냅샷 diff 로 *새 untracked 만* 제거(기존 보존). DRY+e2e 로 Hermes 3건 보존 실증.
- F1: 가드를 canonical 한정→`_staging/audit` 외 tracked 전부 복원(`:(exclude)`).
- F2(잔여): claude ~2분 실행 *중* writer 가 tracked 편집하면 가드가 되돌릴 수 있음 → flock + 야간 시각 + step0 완화, cron 04:00 KST(writer idle).
- F3: flock. F4: 커밋 스테이징 scope assert + 가드후 tracked leftover assert.

**활성화됨(2026-06-22):** `claude -p` headless 인증 실증(`AUTH_OK_L4V3`) + 해피패스 e2e 2회(canonical 무변경·HEAD 불변·Hermes 보존·report 생성) 후 **crontab 설치 `0 4 * * *`**(매일 04:00 KST). never-audited 399→ 점진 소진 개시. 해제=`crontab -e` 해당 줄 삭제.

### 외부 프레이밍 정렬 (개념 참고 — 미검증 2차 출처)

업계에서 부상한 "loop engineering"(프롬프트가 아니라 *루프*를 설계) 담론이 본 L4 설계와 같은 골격을 가리킨다. 어휘 정렬용으로만 참조하며, **출처는 미검증 2차 가공**(Rahul `@sairahul1` 트위터 스레드 → 일본어 블로그 재정리)이라 위키 canonical 인용 불가 — Boris Cherny/Peter Steinberger 귀속 인용·토큰 수치·arXiv 링크(`2605.01428`, 미래 채번·블로그가 arXiv PDF라는 점에서 의심) 모두 액면 신뢰 금지. Phase 1 F7(Landscape를 motivation으로 격하)과 동일 처리.

- **5단계 루프**(DISCOVER→PLAN→EXECUTE→VERIFY→ITERATE) = 본 V0 매핑: Select→verdict 매트릭스→AI Auditor→AI Adversary(refute)→ledger 점진 소진.
- **closed vs open loop**: 본 설계는 의도적 **closed**(사람이 path·verdict·종료조건 고정, human gate). open(에이전트 자유 재량)은 토큰 폭발·품질 게이트 부재 위험으로 보류 — minimal-setup·신뢰 축적 원칙과 정합.
- **maker/checker 분리**(별 에이전트로 검증) = Auditor↔Adversary 분리로 이미 구현. 본 담론이 VERIFY 단계의 핵심으로 지목하는 패턴.
- **6 빌딩블록** 대비 현황: Skills(`SKILL.md`+`CLAUDE.md`)·Connectors(`coastal-wiki` MCP+git)·Subagents(maker/checker)·Memory(`ledger.json`) = 충족 / Automation(=V3 cron)·Worktrees(read-only 감사라 불필요) = 미적용.
- 단일 에이전트 루프 ↔ fleet(오케스트레이터+스페셜리스트) 구분은 V0(단일)→ 추후 다축 감사(링크·출처·신선도 병렬) 시 fleet 고려 여지.


---

# Applied Study 전환 계획 (2026-07-12, v2 — Codex adversarial review 1차 MODIFY 반영)

## 트리거

2026-07-12 **12/12 전 모델 종결**(AUDIT-LEDGER) — 바이블(객관 레이어) 1차 완성. 사용자 지시: "시스템 검토 및 이론적 내용을 어떻게 접목해서 applied study로 갈 것인지 Codex 검토를 통해 계획을 세워보자."

## 1. 시스템 검토 (현황 진단)

| 레이어 | 상태 | 평가 |
|---|---|---|
| canonical (concepts 10토픽 + models 12종) | 전 모델 종결·cross-model 7편·L4 자가감사 cron 가동 | **1차 완성** — 유지보수 모드 전환 가능 |
| examples (4건) | 절차 템플릿 수준 (재현 데이터 없음) | 케이스와 연결 시 실체화 |
| experience (10건 + heuristics/failure-patterns) | 전부 **데이터 분석 계열**(KHOA 조위·SST·EVA) — **모델 run 계열 0건** | 3조건 게이트는 실증됐으나 run 채널 미사용 |
| coastal-runs 채널 | 계약·양측 클론 완료, observations 실질 0건 | **가장 큰 갭 — 이론→run 연결 실증 0** |
| 위키 밖 연구본선 | Rmax ±σ 12런 완주·JPM/EVA §15·TSI 보정 경로·KHOA 2024 대기 | run 산출물 채널 미등록 |

**진단**: 병목은 지식이 아니라 **파이프라인 실사용** — 바이블→케이스 방향의 prospective 완주 사례가 없다.

## 2. 접목 메커니즘 (Codex 반영판)

1. **Setup 근거 인용 체계**: 케이스의 모든 설정 선택에 위키 verified 노트 인용 부착 — 단, **`coastal-wiki@<sha>` + 경로·절을 run 문서 필수 필드로 고정**(노트 개정에 따른 근거 드리프트 방지, Codex #4). 예: 기본 마찰 off 함정 3형제, ADCIRC NFFR 부호(내향 양)·NWS=13 경로, SWASH β sentinel.
2. **Pre-run 체크리스트 — claim 기준 분할**(D-1 확정, Codex #1): 소스코드·식에서 직접 도출되고 항목별 file:line 근거가 있는 **안정적 함정 원형**만 `models/<model>/source-analysis/playbooks/`(G8 허용). 특정 격자·forcing·보정값·실행순서 의존 체크리스트와 체크 **결과**는 coastal-runs 에 두고 위키 playbook 을 고정 커밋으로 인용.
3. **run→experience 게이트 구체화**(Codex #5·#6): observations frontmatter 에 기존 3조건 외 **reviewer·판정일·기각/대기 사유** 기록. 반복 관찰 = **독립 케이스**(동일 설정 단순 재실행은 1회로 계수) 최소 2건 + evidence 파일 사람 확인. 최종 승격 책임 = 사용자(G7). **phase 기술적 완료 ≠ experience 승격** — 별도 상태(1회 파일럿은 phase 완료 가능하되 승격은 반복 축적 후).
4. **역방향 피드백 — source 확인 게이트**(Codex #7): run 발견(버그·미문서 거동) → **소스코드로 독립 확인 성공 시에만** canonical SA 노트 반영(선례: SFINCS Green-Ampt 도 소스 라인 확인 후 기록). 소스 확인 실패분은 coastal-runs observations 또는 게이트 후 experience 에만.
5. **재현성 증거 강화**(Codex 구조결함 지적): setup/+manifest.sha256 에 더해 **실행 명령·모델 binary/source SHA·환경·forcing/관측자료 버전** 기록 — RUNS-CHANNEL §2.1 스키마 개정 대상.

## 3. Applied study 트랙 (조건부 의존성 그래프 — Codex #8, 구 B→A→C 직렬 폐기)

| 트랙 | 내용 | 진척 | 상태 |
|---|---|---|---|
| **A. 폭풍해일 설계 (JPM·EVA)** | 한국 연안 확률론적 설계해일고 — 논문 v0.7 방어 단계·Rmax ±σ 12런 완주 | **최고** | **활성 (즉시)** |
| **B. 조석 캘리브레이션** | ADCIRC 한국 연안 조석, KHOA 49정점 16yr UTide 검증 기준 | 중 | 활성 (병렬) |
| **C. Surge surrogate/ML** | run DB → surrogate 훈련 (사용자 핵심 관심사) | 하 | C0(설계)만 조기 착수 |
| **D. 커플링/복합침수** | ADCIRC+SWAN↔SFINCS | 하 | **backlog** (첫 run→experience 완주 전 보류, Codex #10) |

**의존성 (조건부)**: B 는 A 의 선행조건이 **아님** — A 는 기존 진척으로 즉시 지속. 단 **B 와 A 가 동일 ADCIRC 격자·수심·마찰·경계 체계를 공유함이 입증되면** B 조석 보정 결과가 A2/A3 의 조건부 게이트가 됨(공유 여부 확인이 B1 산출물). C 는 A3 run DB 에 의존하되 **C0(데이터 계약·입출력 변수·DOE 표본설계)는 A3 이전 병렬 착수** — EVA 용 JPM 표본과 ML 훈련 표본은 요구 분포가 다름(parameter-space coverage·극값 밀도), A3 를 이중목적으로 쓰려면 C0 설계가 먼저.

## 4. 로드맵 (phase — 명칭 트랙 접두)

- **P0 (schema spike, 즉시)**: **대표 케이스 1건**(Rmax 12런 중 1)만 coastal-runs 스키마로 등록(구 A0 전량 소급 폐기 — Codex #3 과잉 판정). provenance 결손(당시 환경·해시 미보존)은 복원하지 않고 **결손으로 명시**(`reproducible: false` + 사유). 성공조건: 스키마 필드 전부 채워지고 게이트 심사 1회 모의 통과.
- **B1 (조석 파일럿)**: ADCIRC 조석 1케이스 — **범위 확정 필수**(Codex #9): 계산기간·검증 정점 subset(49 전체가 아닌 대표 N)·캘리브레이션 변수(마찰·경계 분조)·합격 임계값(RMSE/분조 진폭·위상 오차)을 B1 착수 시 명문화. fort.15 셋업 전체 위키 인용 문서화(§2-1 표준 확립).
- **A2 (surge hindcast)**: 실태풍(Hinnamnor 등) GAHM vs JMA-MSM(NWS=13) 이원 forcing — B1 과 모델 구성 공유 시 B1 통과를 게이트로.
- **A3 (JPM run DB 확장)**: EVA 갱신 + (C0 설계 충족 시) surrogate 훈련데이터 겸용 — **EVA 표본과 ML 표본 설계를 분리 정의**.
- **C1 (surrogate 훈련)**: C0 적합성 검사를 통과한 A3 DB 로.
- 각 phase 게이트: 기술적 완료(산출물 체크) / experience 승격(3조건+reviewer) **분리 심사**.

## 5. 결정 기록 (Codex 1차 검토 판정 반영)

- **[D-1 확정]** claim 기준 분할 — source-grounded 원형=위키 playbooks, case-specific=coastal-runs (Codex MODIFY→반영).
- **[D-2 확정]** coastal-runs 단일 SSOT (Codex APPROVE). 논문 원고·배포 코드가 독립 협업/공개 수명주기를 가질 때만 별도 repo, run 데이터는 복제 않고 `coastal-runs@<sha>` 참조.
- **[D-3 확정]** 대표 케이스 1건 schema spike (Codex APPROVE — 전량 소급은 허위 재현성 위험).
- **[D-4 폐기→재설계]** B→A→C 직렬 의존 REJECT — §3 조건부 그래프로 교체.
- **[D-5 반영]** 비례성 역전 교정 — 백필 축소·게이트 기준 구체화(§2-3)·D 트랙 backlog.

## 검증 이력

- 2026-07-12 Codex adversarial review 1차: **MODIFY** — D-1 MODIFY/D-2 APPROVE/D-3 APPROVE(대표만)/D-4 REJECT/D-5 MODIFY + 구조결함 10건(게이트 판정 모호·phase/승격 혼동·역방향 G8 위반 가능·재현성 증거 부족·위키 드리프트·A3 이중목적·A1 범위·소유권·명칭 충돌·범위 팽창) → v2 전면 반영.

---

# 4-레이어 지식 아키텍처 (2026-07-12, v2 — Codex adversarial review 2회차 MODIFY 전면 반영, 사용자 승인)

## 트리거·정정

사용자 제안: **① 이론 → ② 모델(소스·매뉴얼 = 현 구조) → ③ 모델 및 분석 내용(실제 적용) → ④ 응용(연구·융합)**. 이론 원천 = `E:\numerical_models\textbook-ai-data-full`(교재 16챕터 MDX, 인용 없는 AI 합성본 — 원 코퍼스 12권은 위키 `textbook/md/`·sources.yml 기등록). 직전 "Applied Study 전환 계획 v2" 는 **3분해**(Codex 지적 — 단일 소속 오류): run 실행·provenance=③(P0/B1 로드맵 유지) / 연구 해석·융합 노트=④ / 개인 검증 결과=experience(횡단).

**사용자 확정 전제(2026-07-12)**: (a) 이론 이식 = 챕터별 인용보강(textbook/md 대조 → (source_id, page) 부착), (b) ④ 응용 노트 = concepts/<topic>/ 신규 파일, (c) 기존 verified 노트 오염 금지.

**설계 근거(외부 리서치 2026-07-12)**: Karpathy LLM Wiki 패턴(2026-04 X, raw/wiki/schema + ingest/query/lint) — coastal-wiki 와 동형(raw=textbook/md·wiki=canonical·schema=CONVENTIONS+sources.yml·query=MCP·lint=L4 감사), **결여 연산 = ingest** → 본 계획이 채움. 인용접지 파이프라인 표준(원자 단언 분해→신뢰 KB 검색→검증 스코어링, PaperTrail arXiv:2602.21045 등) = §3 이식 절차의 근거. 하네스 공학(장기 작업 = 단일 드리프트 세션 금지, 스테이지+체크포인트+품질게이트 — philschmid 2026·RepoProver maker/checker).

## 1. 레이어 ↔ 위키 물리 구조 매핑

**레이어는 비배타적 논리 역할이다 — 디렉토리·파일 번호가 자동 분류 기준이 아니며, claim·문서 역할로 판정한다** (Codex #1: concepts/03 에도 분석 이론이, 04 에도 일반 도구 설명이 있을 수 있음).

| 레이어 | 정의 | 주 물리 위치 | 현황 | 갭 |
|---|---|---|---|---|
| **① 이론** | 교과서 수준 수식 유도·물리 원리 | `textbook/notes/theory-*` (신설 계열) | md 코퍼스 10권+sources.yml 완비, 체계 이론노트 부재 | 교재 16챕터 이식(T 트랙) |
| **② 모델** | 소스코드·매뉴얼·공식자료 분석 | `models/<model>/` | **12/12 종결**(2026-07-12) | 유지보수 모드 |
| **③ 실제 적용** | 출처 기반·**일반화 가능한** 셋업·검증·분석 절차 | concepts 03·04·06 중 해당 claim + `examples/` (canonical) / coastal-runs→experience (개인) | 03·04·06 다수 verified, examples 4건, runs 실사용 0 | P0·B1 로드맵(구 v2 계승) |
| **④ 응용** | 연구·융합 — 문헌 종합·연구 설계·ML surrogate 등 | `concepts/<topic>/NN-applied-*.md` (다음 빈 번호) | 선례: storm-surge/07-ml-emulators | AP 트랙 신설 |
| (횡단) 경험 | 3조건 통과 개인 검증 — **별도 provenance 레이어** | `experience/` | 10건 | ④는 experience 를 **커밋고정 링크로만 소비**(본문 복제 금지) |

- **③ canonical 허용 기준**(Codex #3): 출처 기반·일반화 가능 절차만 concepts/examples. case-specific 설정·보정값·결과 수치는 G8 대로 coastal-runs 강제.
- **① 소유권**(드리프트 방지): 상세 이론의 canonical = ① theory 노트. concepts 01-02·models manual-notes 는 요약+링크로 소비. 신규 ① 노트가 기존 노트와 겹치면 ①이 상세본, 기존 노트는 손대지 않고 이후 자연 갱신 시점에 링크 전환.

## 2. 참조 규율 — "근거 의존성의 단방향" (Codex #5 개칭)

- **근거 의존성**(이 노트의 단언이 저 노트의 검증에 기댐)은 ④→③→②→① 단방향. **탐색용 cross-link 는 claim 복제를 만들지 않는 범위에서 양방향 허용** — ① 이론 노트가 "모델 구현은 [[모델노트]] 참조"라 안내하는 것은 탐색 링크(허용), ① 이 ② 의 소스 분석을 자기 단언의 근거로 쓰는 것은 위반.
- 인용 단위: ①=(source_id, page) / ②=file:line·페이지 / ③=①② verified 링크+재현 절차 / ④=①②③ 링크+외부 문헌.
- 개인 run 산출물은 어느 레이어에도 직접 못 들어옴(#8) — coastal-runs 경유 experience 만.
- **집행**(Codex #6): 신규 파일 전용 frontmatter `layer:`·`depends_on:` + pre-commit lint(`tools/validate-layer-deps.sh`) — 근거 의존 방향만 검사. **기존 verified 파일은 검사·백필 대상 제외.** 이식 커밋이 기존 verified 본문을 변경하지 않았는지 scope guard 동시 검사.

## 3. T 트랙 — 교재 이식 (레이어 ①)

- 파일명: `textbook/notes/theory-ch<NN>-<slug>.md`. frontmatter: `layer: 1`, AI 합성 provenance 명기, `citation_status` 는 인용보강 결과로 판정.
- 챕터당 절차(인용접지 파이프라인): MDX 이식(인터랙티브 컴포넌트 제거) → **원자 단언 분해** → textbook/md FTS5·페이지 대조 → `(source_id, p.N)` 부착 → **미매칭 단언 = 삭제 또는 source-needed 콜아웃**(부분 부착 ≠ 파일 verified, Codex 지적) → validator.
- **페이스 = 지표 기반**(Codex #8, "세션당 1-2챕터" 고정 폐기): T1 파일럿(08 선형파동)에서 단언 수·출처 매칭률·소요시간 측정 → `textbook/THEORY-LEDGER.md` 에 기록 → stop/go 게이트 후 장별 scope 재산정.
- 순서: **T1=08(파일럿 ✅) → T2=12 조석** → 09→10→13→14 → 기초 00.5~07(8챕터 — F-4 (a) 사용자 확정으로 전부 개별 이식) → **11·15(SWAN·EFDC)는 claim-level 분해** — 일반 이론만 ①에, 모델 구현 서술은 복제하지 않고 기존 models/ 노트 탐색 링크(Codex #4); 일반 이론 잔여가 없으면 노트 신설 없이 "검토 완료" 처리 가능(F-4 검토).
- 교재 챕터 자체는 sources.yml 에 등록하지 않음(AI 합성본은 출처 아님 — #3). 원 교재 12권이 출처.

## 4. AP 트랙 — 응용 노트 규약 (레이어 ④)

- 명명: **다음 빈 번호** `NN-applied-<slug>.md`(고정 07 아님 — waves/07·08 기점유, Codex #7). 토픽 횡단 연구는 주 연구질문 기준 한 곳만 canonical + INDEX 응용 표에서 연결.
- 성격: 연구·융합(JPM/EVA 방법론·surrogate 설계·커플링 연구 종합). citation_status 규율 동일.
- **문헌 기반 ④ 노트는 experience 승격 선행 불요**(Codex #9) — 개인 결과를 주장하는 ④ 노트만 experience 링크 선행.

## 5. 실행 하네스·순서 (명칭 T*/AP* — 기존 L1 검색/L4 감사와 충돌 회피, Codex #10; **시퀀싱 개정 2026-07-12 F-6**)

- **cron/자동 loop 미사용** — 인용 검증은 사람 게이트. 기존 L4 cron 이 신규 노트 자동 감사(lint 기존재). **동시 진행 한도 = 1 트랙**.
- **확정 시퀀스(사용자 전략 2026-07-12)**: ⑴ 거버넌스+하네스 ✅ → ⑵ T1 파일럿+게이트 ⓐ ✅ → ⑶ **T 트랙 완주** — 분모 = **15챕터 전부**(00.5~15, ch00 Intro 만 제외; **F-4 사용자 확정 = (a) 전부 이식** — 리뷰어 양측(Claude·Codex)의 (b) 도메인 축소 권고 기각, 기록) → ⑷ **실제 프로젝트 착수** — 프로젝트 안에서 ③(run 실행·provenance)·④(연구 종합) 동시 실증. **③ P0/B1 은 위키 로드맵 활성 phase 에서 제외** — 구 "Applied Study 전환 계획 v2" 는 폐기 아닌 **미래 실프로젝트 실행 템플릿**으로 보존(F-6).
- Codex 게이트: ⓐ 완료(MODIFY→반영) ⓒ 배치(~4챕터)마다 ⓓ AP 규약 확정 시. 같은 스레드 `--resume`.
- **거버넌스 moratorium(F-5)**: 신규 규칙은 기본 동결 — 기존 규칙(절대규칙·G1-G9·§8.1) 훅 강화로 대응. 기존 규칙으로 표현 불가능 + 반복 사례 확인 시에만 adversarial gate 경유 신설.

## 검증 이력

- 2026-07-12 Codex adversarial review 2회차(스레드 019f5661): **MODIFY** — E-1 APPROVE(분산 매핑, 단 논리 분류 명시)/E-2 MODIFY(①→② 링크가 단방향 규칙과 자기모순 → 근거/탐색 링크 분리)/E-3 APPROVE(단 07+ 번호 기점유 → NN-applied)/E-4 MODIFY(고정 페이스 폐기→지표 기반, 12장 조기)/E-5 MODIFY(집행 불가능 → 근거 의존성 한정+경량 lint) + 구조결함 10건(v2 단일소속 오류·G8 누출·experience 역할 중첩·규칙 자기모순·레이어 배타성 착각·오염 scope guard·3중 복사본 드리프트·AI 합성본 권위상승·명칭 충돌·writer 과부하) → v2 전면 반영. 사용자 plan-mode 승인(2026-07-12).
- 2026-07-12 Codex 3회차 = 게이트 ⓐ(T1 파일럿+lint): **MODIFY** → 필수 6건 반영(cac8be1) — T1 인용 정밀화(진행파 p.78 정정·선형화 페이지 분리·residue 2건 해소)·lint 강제/실존성/HEAD scope guard.
- 2026-07-12 Codex 5회차 = **② 모델분석 레이어 표본 재검증(사용자 지시)**: **MODIFY** — 표본 anchor 대부분 정확(ADCIRC NFFR·EFDC CALUVW·XBeach wet/dry·SWASH solvers 전부 raw 일치). ⚠높음 2건: **SWASH 종결**(swashtech Ch2/5 비코어 판정이 자기 자료와 모순 — 보존성·mimetic 재판정 open)·**SWAN 종결**(swanmain 실질 로직 존재 + swan-foundation 은 source coverage 부적격 — C/S 재분류 open). 중간: xnl4=선택형 core physics 재분류·Delft3D chkadv 인용 라인 정정(주석→실호출 trisol.f90:2250,2260,3336,3346·z_trisol 2회 1923,2895). 낮음: XBeach 형태학 재판정 범위 wetz 한정·★'docs ln 오염' finding 은 **검증 도구 오류(rg -r 치환 플래그)로 판명 — 철회**(적대 검증이 검증자 오류를 적발한 사례). 구조 취약점 6패턴 기록: flag 소진≠coverage·S/T 분류의 파일 역할 편향·자기참조 closure(cross-model↔model note 순환)·anchor 드리프트·overview 의 S-tier 재사용·작성-검증 주체 미분리. 낮음·중간 즉시 반영, 높음 2건 = 레저 ⚠재검토 open.
- 2026-07-12 Codex 4회차 = 총평 수정안 F-검토: F-1 MODIFY(count-notes+--check)/F-2 APPROVE(lint 회귀테스트)/**F-3 REJECT**(동일 layer 전면 금지 과함 → ①→① 유도 의존 허용·claim 복제 금지·순환만 금지)/**F-4 (b) 권고 → 사용자 (a) 확정**(16챕터 전부 — 기각 기록)/F-5 MODIFY(moratorium 형)/F-6 APPROVE(로드맵-전략 모순 제거) + 신규 F-7(모델 종결 freshness 수명주기 — snapshot 판정 명시·사용 직전 upstream delta 확인)·F-8(validate-all 단일 진입점, L4 와 구현 분리 유지)·F-9(ledger 이원화 유지·INDEX 얇은 색인). 전 항목 반영 커밋 참조.
