# research/ — Hermes coastal-research 워크벤치

`research/`는 Hermes `coastal-research` 프로필이 X, arXiv, 블로그, GitHub, 기관 공지, 툴 업데이트를 수집·요약하는 작업 공간이다.

이 디렉토리는 `concepts/`, `models/`, `experience/`의 verified 본문 레이어가 아니다. 모든 내용은 후보·초안·digest이며, 본문에서 직접 인용하지 않는다.

## 역할

- `inbox/`: 새로 발견한 후보 항목. X 포스트, 논문, 블로그, 툴 릴리스, 계정, 데이터셋 등. (Hermes write)
- `digests/`: Hermes가 만든 주간·월간 트렌드 요약. (Hermes write)
- `watchlist/`: 모니터링 대상 키워드, 계정, 저자, 기관, 저장소, 저널. (Hermes write)
- `prompts/`: Hermes 호출용 prompt 파일 (cron 등록 + 단발 실행). **governance** — frontmatter 면제, validator 검사 제외.
- `manifest.md`: Hermes 프로필 운영 기록, 수집 방법, 쿼리 세트, 한계, 운영 빈도. **governance**.
- `README.md`: 이 파일. **governance**.

## 핵심 원칙

1. `research/`는 워크벤치다. 본문 지식의 canonical source가 아니다.
2. `research/` 내부 파일은 `concepts/`, `models/`, `experience/`에서 직접 인용하지 않는다.
3. 본문으로 옮길 때는 출처를 다시 확인하고 해당 canonical 위치로 promote한다.
4. 검색 노출 기반 결과는 정량 랭킹처럼 표현하지 않는다.
5. 자동 피드 계정, 연구자/기관 계정, 소프트웨어/툴 계정을 구분해 기록한다.
6. X/Hermes 검색 결과는 “샘플에서 반복 관측된 항목”으로 표기한다.

## Frontmatter 표준

`research/inbox/`와 `research/digests/`의 일반 문서는 다음 frontmatter를 사용한다.

```yaml
---
title: "<문서 제목>"
origin: hermes-coastal-research
discovered_date: YYYY-MM-DD
source_url: "<원문 URL 또는 검색 URL. 없으면 null>"
source_type: x | arxiv | paper | blog | github | documentation | tool | account | dataset | mixed
query: "<사용한 검색어 또는 null>"
citation_status: draft-unsourced
promote_candidate: concepts | models | experience | watchlist | discard | undecided
---
```

`source_url`이 여러 개이면 본문 `## Sources` 섹션에 목록으로 둔다.

## 체류 기간

- `inbox/` 항목은 발견 후 90일 안에 다음 중 하나로 처리한다.
  - promote 후보로 본문 검증 작업에 넘김
  - `watchlist/`로 이동
  - digest에만 반영하고 archive/discard
- 90일 이상 방치된 항목은 기본적으로 archive 또는 폐기 후보로 본다.

## Promote 경로

| 후보 성격 | Promote 위치 | 조건 |
|---|---|---|
| 객관·도메인 일반화 | `concepts/<topic>/` | 논문·교과서·공식 문서 등 출처 보강 후 |
| 모델 자료 | `models/<MODEL>/web-refs/`, `models/<MODEL>/manual-notes/`, `models/<MODEL>/source-analysis/` | 공식 문서·코드·논문 기준으로 재확인 후 |
| 검증된 개인 노하우 | `experience/` | 반복 관찰 + 객관 데이터 + 재현 가능 3조건 충족 후 |
| 모니터링 대상 | `research/watchlist/` | 계정·저자·기관·repo·키워드 추적 가치가 있을 때 |
| 단순 노이즈 | discard/archive | 출처 불충분, 반복성 없음, 도메인 관련성 낮음 |

## 금지

- `research/` 파일을 verified 본문에서 직접 인용 금지.
- X 검색 결과를 “많이 언급됨”, “인기 순위”처럼 정량 랭킹으로 단정 금지.
- Client ID, Client Secret, API token 등 자격증명을 기록 금지.
- 개인 계정의 private 정보, DM, 비공개 데이터 저장 금지.

## 권장 digest 표현

- “최근 7일 X 검색 결과 샘플에서 반복적으로 관측된 항목”
- “정량 랭킹이 아니라 탐색적 트렌드 스냅샷”
- “검색 노출 기반 후보군”
- “coastal-wiki 본문 promote 전 추가 출처 확인 필요”

## Hermes 운영

Hermes `coastal-research` 프로필은 이 디렉토리를 주 작업 루트로 삼는다. 단, 본문 수정이 필요할 때는 `research/`에서 직접 확정하지 않고 `concepts/`, `models/`, `experience/`의 각 정책을 따른다.
