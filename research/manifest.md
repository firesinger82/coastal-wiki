# research manifest

작성: 2026-05-23
운영 주체: Hermes `coastal-research` profile
작업 루트: `/home/firesinger/coastal-wiki/research/`

## 목적

`research/`는 coastal-wiki의 verified 본문을 오염시키지 않고, 외부 동향을 탐색·수집·정리하기 위한 격리 워크벤치다.

주요 입력원:

- X/Twitter 검색 샘플
- arXiv 및 논문 검색
- GitHub repository / release / issue
- 모델 공식 문서, 매뉴얼, 위키
- 기관·학회·저널·프로젝트 공지
- 블로그·기술 노트

## 수집 방법

### X/Hermes 검색

초기에는 공식 X API가 아니라 Hermes `x_search` 기반 샘플링을 사용한다.

주의:

- 전수 수집이 아니다.
- engagement 기준 정량 랭킹이 아니다.
- X 검색 노출 알고리즘과 쿼리 선택의 영향을 받는다.
- 결과는 “검색 결과 샘플에서 반복 관측된 후보”로만 해석한다.

대표 키워드 세트:

```text
"numerical modeling"
"numerical modelling"
"computational modeling"
"finite element modeling"
"coastal numerical model"
"coastal modelling"
"storm surge model"
"hydrodynamic model"
"wave model"
"morphodynamic model"
"sediment transport model"
"coastal flooding model"
XBeach
ADCIRC
Delft3D
SWAN
SCHISM
TELEMAC
ROMS
FVCOM
MIKE21
HEC-RAS
"machine learning" "storm surge"
"deep learning" "coastal flooding"
"surrogate model" "hydrodynamic"
"physics-informed" "coastal"
PINN "shallow water equations"
```

### 공식 API 전환 조건

다음이 필요해질 때 X Developer API 또는 별도 수집 파이프라인을 검토한다.

- tweet ID, author ID, created_at, public_metrics 저장
- 중복 제거와 장기 시계열 분석
- engagement 기준 정렬
- 재현 가능한 쿼리 로그
- SQLite/CSV 기반 주간 랭킹

자격증명은 이 repo에 저장하지 않는다.

## 산출물 위치

- 새 후보: `research/inbox/YYYY-MM-DD-<slug>.md`
- 주간 digest: `research/digests/YYYY-WW-coastal-modeling.md`
- 월간 digest: `research/digests/YYYY-MM-coastal-modeling.md`
- 추적 대상: `research/watchlist/*.md`
- prompt 파일(governance): `research/prompts/*.md`

## 운영 빈도

- **주간 자동 수집**: cron 매주 월요일 09:00 KST.
  - prompt: `research/prompts/weekly-collection.md`
  - 산출: `research/inbox/YYYY-MM-DD-*.md` + `research/digests/YYYY-WW-coastal-modeling.md`
  - **자동 커밋** (2026-05-26 결정): Hermes 가 수집 직후 `chore(research): YYYY-WW hermes ingest` 단일 commit. cron 실패 시 다음 세션에서 backfill.
- **단발 주제 탐색**: `research/prompts/<topic>-deep-dive.md`, 수동 실행.
- **watchlist 등록·갱신**: `research/prompts/register-watchlist.md`, 수동 실행.
- **inbox 트리아지** (2026-05-26 결정): Claude 세션 시작 시 30일+ 항목 또는 신규 digest 감지하면 트리아지 제안. 사용자 명시 요청 시 즉시. 트리아지 = `promote_candidate` 갱신 + promote/archive/delete 분기 (정책: `research/README.md §체류 및 폐기 정책 (Hybrid)`).
- **inbox 90일 체류 추적**: 주간 digest 안에 90일 초과 항목 별도 섹션. 90일 초과 미트리아지 = 자동 archive 후보 (delete 아님).

## arXiv 카테고리 권장

자동 수집 prompt 에서 다음 카테고리 우선:

- `physics.ao-ph` (Atmospheric and Oceanic Physics) — 1차
- `physics.flu-dyn` (Fluid Dynamics) — 1차
- `cs.LG` (Machine Learning) — ML/PINN 계열 보강
- `physics.geo-ph` (Geophysics) — 퇴적·해저 지형 관련
- `physics.comp-ph` (Computational Physics) — 수치기법 보강

## Promote 정책

`research/`의 내용은 본문에서 직접 인용하지 않는다. 본문 반영이 필요하면 다음 위치로 promote한다.

- 객관 도메인 일반화 → `concepts/<topic>/`
- 모델 자료 → `models/<MODEL>/`
- 검증된 경험·노하우 → `experience/`

Promote 시 원 출처를 재확인하고, coastal-wiki의 `CONVENTIONS.md` 인용 규칙을 따른다.
