# 현재 폴더 구조 — 2026-09-12 실측

사용자의 “현재 폴더 구조부터 파악” 지시에 따라 디스크의 실제 디렉터리, Git 추적 파일, 폴더별 안내문, 검색 범위 코드를 대조했다. 개편안의 이상적인 구조가 아니라 **현재 상태**다. 기준 커밋 `36b7f34`, [집계 원본](structure-inventory.json). 원본 솔버·부속 라이브러리 내부는 판독하지 않았다.

## 실제 디렉터리

```text
coastal-wiki/
├── README.md · INDEX.md                  전체 목적·탐색
├── AGENTS.md · CLAUDE.md                 작업 진입·공통 규칙
├── CONVENTIONS.md · BOUNDARY.md          인용·배치·저장소 경계
├── plan.md                              누적 결정·계획·작업 이력
├── RUNS-CHANNEL.md · SYNC.md             실행 결과 채널·동기화
├── concepts/                            개념 10개 + _template
│   ├── tides/ · waves/ · currents/ · sst/
│   ├── sediment-transport/ · littoral-drift/
│   └── storm-surge/ · swash-zone/ · rip-currents/ · compound-flooding/
├── models/                              모델 13개 + _template
│   ├── INDEX.md · AUDIT-LEDGER.md         모델 목차·감사 원장
│   ├── ADCIRC/ · EFDC/ · Delft3D/ · ROMS/
│   ├── SWAN/ · SWASH/ · XBeach/ · FUNWAVE/ · Celeris/
│   ├── CADMAS-SURF/ · SFINCS/ · LISFLOOD-FP/ · ShorelineS/
│   └── 각 모델/
│       ├── README.md · manifest.md       manifest는 일부 모델만 존재
│       ├── source-analysis/             작성한 구현 설명
│       ├── manual-notes/                작성한 매뉴얼 해설
│       ├── web-refs/                    공식 자료·논문 안내
│       └── raw/                         로컬 원본, Git 집계에서 제외
│           ├── source_code/             13개 모델 모두 존재
│           └── manuals/                 일부 모델에 존재
├── textbook/
│   ├── sources.yml · INDEX.md · POLICY.md · THEORY-LEDGER.md
│   ├── md/                             교과서 텍스트 변환본
│   └── notes/                          교과서·이론 작성 노트
├── standards/
│   ├── README.md
│   └── kds-64/                         KDS 항만·어항 기준 변환본 34개
├── examples/                           통합 실습 4개
│   ├── swan-to-swash-nesting/
│   ├── adcirc-swan-surge-coupling/
│   ├── delft3d-flow-wave-morphology/
│   └── khoa-surge-eva-pipeline/          시나리오별 code·results 등
├── experience/                         검증된 경험·분석 결과 노트
│   └── failure-patterns/ · heuristics/ · playbooks/
├── data/                               경험·분석의 근거 데이터
│   ├── khoa-analysis/                  원자료 추출·중간 JSON
│   └── sst-global/                     시계열·분석 결과·로컬 NetCDF
├── research/                           새 자료 수집·검토 공간
│   └── inbox/ · digests/ · watchlist/ · prompts/ · seeds/
├── references/
│   └── collect.py                      arXiv → research/inbox 수집 코드
├── tools/                              검색·인용 검사·감사·재현 도구
│   ├── llm-wiki-poc/ · llm-wiki-audit/ · resume-gate/
│   ├── khoa-validation/ · sst-cross-check/ · manifests/
│   └── validate-* · count-notes.* · install-hooks.sh 등
├── _staging/                           미반영 작업·검토 증거
│   ├── total-read/                     전수 판독·모델 감사 기록
│   ├── audit/ · manifests/ · runs-feedback/
│   ├── wiki-structure-20260912/          이번 현황 조사·계획 초안
│   └── _staging/total-read/records/     중첩 디렉터리, 파일은 관측되지 않음
├── _archive/                           이전 통합본·검토 이력
│   └── modeling-wiki/ · from-modeling-wiki-knowledge-phase2a-2026-05-23/
│       codex-reviews/ · XBeach/
└── .git/ · .obsidian/ · .agents/ · .claude/ · .codex/
    .playwright-mcp/ · .venv/            저장소·앱·에이전트·실행 환경
```

루트에는 `swan_prd.md`, `swan_ecs.md`, `pyproject.toml`, `uv.lock`, `.gitignore`, `.mcp.json`도 있다. 위 트리는 역할을 읽기 쉽게 묶은 것이며 개별 파일 전부를 열거하지 않았다. 숨김 설정의 비밀값은 읽지 않았다.

## 규모 — Git 추적 파일 기준

| 영역 | 추적 파일 | 그중 Markdown | 해석 |
|---|---:|---:|---|
| concepts | 74 | 74 | 템플릿 7개 포함. 10개 토픽의 본문·README 합계는 67개 |
| models | 478 | 478 | 13개 모델 작성 문서 472개 + 템플릿 4개 + 공통 목차·원장 2개 |
| textbook | 57 | 53 | notes 32개, md 변환 관련 21개, 루트 정책·목차·원장·출처 매니페스트 4개 |
| standards | 35 | 35 | 기준 변환본 34개와 README |
| examples | 20 | 10 | 시나리오 문서·코드·보조 파일 |
| experience | 22 | 22 | 경험·분석 노트와 안내 |
| data | 38 | 1 | 추적하는 분석 데이터. 로컬 대용량 원본 전체 개수가 아님 |
| research | 115 | 101 | 이번 직전 조사 수집물 포함 |
| references | 1 | 0 | 수집 스크립트 |
| tools | 124 | 13 | 검사·검색·분석 코드와 문서 |
| _staging | 5,645 | 196 | 이 중 total-read 5,369개. JSON·판독 영수증·검토 등의 작업 증거 포함 |
| _archive | 102 | 87 | 보존 이력 |

전체 Git 추적 파일은 6,731개다. 루트·추적 설정 파일도 전체에 포함된다. **이 수치는 지식량·디스크 용량·판독률·완료율이 아니다.** Git 제외 원본·로컬 환경과 이번 턴의 미추적 계획 파일은 수치에서 빠진다. 작업 증거가 파일 수를 크게 차지한다고 해서 곧바로 불필요한 파일이라고 판단하지 않는다.

## 실제 구조와 현재 안내의 차이

1. [README](../../README.md)의 주요 디렉터리 표에는 `standards/`, `data/`, `references/`, `tools/`가 없다. 실제 지식 근거·운영 구조를 파악하려면 별도 디렉터리를 확인해야 한다.
2. [models/INDEX](../../models/INDEX.md)는 10개 모델만 나열하고 SWASH·SFINCS·LISFLOOD-FP가 빠졌다고 스스로 명시한다. EFDC·ADCIRC·XBeach의 TBD와 실제 작성 문서도 일치하지 않는다. 반면 루트 INDEX와 AUDIT-LEDGER가 별도 상태를 제공한다. 개편 대상은 중복 상태의 기준과 갱신 책임이다.
3. [검색 구현](../../tools/llm-wiki-poc/fts5_index.py)은 `concepts/models/textbook/experience`를 대상으로 한다. `standards/examples/data/references/research/_staging/_archive`는 현재 대상이 아니다. **존재하는 자료, 탐색 가능한 자료, 검증된 근거는 서로 다르다.** 검색 제외가 곧 잘못된 정책이라는 결론은 내리지 않는다.
4. `models/*/raw`는 검색에서 제외하지만 `textbook/md`는 원문 lookup을 위해 포함하고 작성 노트보다 낮게 정렬한다. “원본은 모두 검색 제외”라는 단순 설명도 정확하지 않다.
5. [concept 템플릿](../../concepts/_template/README.md)은 6개 파일 채우기를 안내하지만 [README](../../README.md)는 두 파일부터 시작하도록 한다. 템플릿과 현재 규약 사이에 불일치가 있다.
6. [XBeach README](../../models/XBeach/README.md)는 구현 모드·노트·감사 이력을 함께 담는다. `source-analysis` 40개, `manual-notes` 8개, `web-refs` 1개와 루트 README·manifest 2개가 실제 51개다. 파일은 이미 존재하며 “미완”은 이 문서가 없다는 뜻이 아니다.
7. [data/khoa-analysis 안내](../../data/khoa-analysis/README.md)는 experience의 raw·intermediate 근거를, [references/collect.py](../../references/collect.py)는 arXiv 수집 실행을 담당한다. 이 둘을 이름만 보고 각각 개인 실행 결과나 문헌 보관소라고 재분류하면 안 된다.

## 계획에 반영할 경계

현재 구조는 작성 지식(concepts/models/textbook notes/experience), 원자료·변환본(models raw/textbook md/standards), 적용·근거(examples/data), 수집(research/references), 도구·검토(tools/_staging), 과거 이력(_archive)이 한 저장소 안에서 역할을 나눈 형태다. 각각의 물리 위치와 독자에게 보여 줄 탐색 분류는 같은 문제일 필요가 없다.

따라서 개편안은 먼저 **모든 실제 영역을 빠짐없이 설명하고, 중복 목차·상태와 검색 경계를 정리하는 것**부터 비교해야 한다. 폴더 이동·삭제·검색 대상 확대는 아직 수행하지 않았다. 원자료 변환의 정확성이나 KDS 규정의 현재 유효성을 이번 디렉터리 조사로 검증했다고 주장하지 않는다.
