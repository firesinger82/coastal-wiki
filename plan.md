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
