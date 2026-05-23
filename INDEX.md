# INDEX

위키 전체 항목의 living map. 새 항목 추가 시 여기에도 등록.

## concepts/ (도메인 개념)

| 토픽 | 상태 | 비고 |
|---|---|---|
| [tides](concepts/tides/) | **DRAFT** (01-05 verified, 06 source-needed) | 조석 — 5/6 verified. 06은 `models/<model>/` 작성 후 verified 가능 |
| [waves](concepts/waves/) | **STABLE** (01-06 verified) | 파랑 — 6/6 verified. Holthuijsen 2007 + KHOA 284 용어 + SWAN library + MPT 74정점 |
| [sediment-transport](concepts/sediment-transport/) | **DRAFT** (01-04 verified, 05·06 source-needed) | 표사이동 — Soulsby 1997 + KHOA 113 용어. EFDC SED 사용자 주력 |
| [currents](concepts/currents/) | **DRAFT** (01-05 verified, 06 source-needed) | 조류 — 5/6 verified (UTide 2D + 수치조류도 + KHOA 60+ 용어). 동해 수치조류도 미커버 명시 |
| [sst](concepts/sst/) | **MINIMAL** (01 verified) | 해수면 수온 — 1/6 verified (정의·측정 정형화·시공간 스케일, Stewart §5-6 + KHOA). experience/khoa-sst-warming-trend.md 와 연결 |
| [littoral-drift](concepts/littoral-drift/) | TBD | 연안표사 |
| [storm-surge](concepts/storm-surge/) | TBD | 폭풍해일 |

## models/ (모델별 객관 자료)

| 모델 | 상태 | 비고 |
|---|---|---|
| [EFDC](models/EFDC/) | TBD | 사용자 주력 모델 |
| [SWAN](models/SWAN/) | **WIP** (README + action-balance + wink-pattern verified) | 천해 풍파 spectral · Holthuijsen 공동개발 · WINK 13 middle + 56 detail |
| [ADCIRC](models/ADCIRC/) | TBD | |
| [XBeach](models/XBeach/) | TBD | |
| [Delft3D](models/Delft3D/) | TBD | |

## textbook/ (교과서 통합)

| 노트 | source_id | 상태 |
|---|---|---|
| [tides-lubbad2009-overview.md](textbook/notes/tides-lubbad2009-overview.md) | lubbad2009-tides-slides | draft-unsourced |

원본 PDF 매니페스트: [textbook/sources.yml](textbook/sources.yml).
토픽별 분류: [textbook/INDEX.md](textbook/INDEX.md).

## examples/ (통합 실습)

| 예제 | 다루는 개념 | 사용 모델 | 상태 |
|---|---|---|---|
| (없음) | | | |

## experience/ (검증 통과 경험)

| 항목 | 통과 기준 | 상태 |
|---|---|---|
| [KHOA 15정점 1년 조위 UTide 검증](experience/khoa-multi-station-tide-validation-2026.md) | 3조건 통과 (15정점 독립 / KHOA 공식값 ±0.1% / fetch+analyze 스크립트 재현 가능) | **verified** |
| [KHOA 14년 기후 추세 — 한국 연안 SLR 2007-2025](experience/khoa-annual-climate-trend.md) | 3조건 통과 (13정점 19년 / KHOA Annual Report 직접 데이터 / 선형회귀 재현 가능) | **verified** |
| [KHOA 9년 SST 가온 추세 — 한국 연안 2017-2025](experience/khoa-sst-warming-trend.md) | 3조건 통과 (13정점 9년 / KHOA Annual Report 직접 데이터 / 회귀+SLR 정합성 cross-check) | **verified** (단기 caveat 명시) |

## research/ (Hermes coastal-research 워크벤치)

| 영역 | 역할 | 상태 |
|---|---|---|
| [research/README.md](research/README.md) | inbox 정책, promote 규칙, frontmatter 표준 | active |
| [research/manifest.md](research/manifest.md) | Hermes 프로필 운영 기록, 수집 방법, 쿼리 세트, 한계 | active |
| [research/inbox/](research/inbox/) | X·arXiv·블로그·툴 신규 후보 | empty |
| [research/digests/](research/digests/) | 주간·월간 Hermes 요약 | empty |
| [research/watchlist/](research/watchlist/) | 모니터링 대상 계정·저자·기관·repo·키워드 | empty |

## 상태 표기

- `TBD` — 디렉토리만 존재, 내용 없음
- `WIP` — 작성 중 (citation_status가 draft-unsourced/source-needed 혼재 또는 일부 파일만 작성)
- `DRAFT` — 초안 완료, 사용자 verify 대기
- `STABLE` — 모든 frontmatter `citation_status: verified`
- `DEPRECATED` — 보존하되 새 작업 금지

상세 인용 상태는 각 파일 frontmatter의 `citation_status` 참조 ([CONVENTIONS.md §2](CONVENTIONS.md)).
