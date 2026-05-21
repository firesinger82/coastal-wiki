# textbook 통합 정책

## 원본 위치

원본 PDF는 **`D:\Study\textbook\`에 그대로 보관**. wiki에 복사·심볼릭 링크하지 않음.

이유:
- PDF는 git에 부담 (LFS 불필요)
- 교과서는 변경 없는 자료 → 원본 위치 안정

## 인용 안정화 — source_id 사용

raw 파일명·Windows 경로 **직접 인용 금지**. 모든 인용은 [sources.yml](sources.yml)에 등록된 안정적 `source_id` 사용:

- 직접 인용: `> "원문…" (holthuijsen2007, p.47)`
- paraphrase: `… (van-rijn-1993, ch.5 §5.3)`

파일 교체·이동·판 변경 시 [sources.yml](sources.yml)의 해당 항목만 갱신하면 전 인용 일관성 유지.

## 노트 작성 규칙

`textbook/notes/`에 챕터·섹션별 발췌·요약을 둠.

### 파일명

`<topic>-<source_id>-<chapter>.md`

예시:
- `tides-tides-and-currents-ch3.md` (Tides and Currents, Chapter 3)
- `sediment-van-rijn-1993-ch5.md`
- `waves-holthuijsen2007-ch7.md`

### 노트 상단 frontmatter 필수

```yaml
---
title: "<topic> — <source 짧은 이름> ch.<N>"
source_id: holthuijsen2007            # sources.yml 매니페스트의 ID
chapter: 7
pages: "120-148"
page_offset_applied: false            # PDF 표시 페이지와 본문 페이지가 다르면 true
topic: waves
canonical_source: self                # textbook 노트 자체가 canonical
citation_status: draft-unsourced | source-needed | verified
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: ""                   # verified 단계에서 사용자 명시
verification_date: ""
---
```

`source` 필드(Windows 경로) **제거됨**. `source_id`로 대체.

### 본문 구조

1. **핵심 정의·공식** — 원문에서 직접 추출. 인용 시 페이지 명시.
2. **요약** — 요지 정리 (AI 가공 구간임을 명시).
3. **수식·도표** — LaTeX/Markdown으로 옮기되 원문 페이지 인용.
4. **연결** — `concepts/<topic>/` 문서로의 링크.

### 인용 표기

본문 내에서:
- 직접 인용: `> "원문…" (source_id, p.NN)`
- paraphrase: `… (source_id, ch.N §N.M)`

### 검증 상태와 인용 가능 범위

`citation_status` 필드(CONVENTIONS.md G3 모델):

| 상태 | 의미 |
|---|---|
| `draft-unsourced` | AI 초안. 페이지·내용 미검증 |
| `source-needed` | 골격 OK, 일부 인용 보강 필요 |
| `verified` | 사용자 검토 + 페이지 대조 완료 |

`concepts/<topic>/`에 인용 시 **`verified` 노트만** 사용. 미검증 노트를 참조하면 인용하는 쪽 frontmatter도 `source-needed`로 표시.

## 원본 PDF 목록·매니페스트

- [sources.yml](sources.yml) — 모든 source_id, sha256, 메타데이터 (단일 진실)
- [INDEX.md](INDEX.md) — 토픽별 분류 가이드 (사람 가독성)

## 작성 우선순위

작업 토픽이 정해진 후 그에 맞는 PDF부터 노트화. **한 권 전체 노트는 권장하지 않음** — 필요한 챕터 단위로 진행. 미사용 자료는 sources.yml에 등록만 해두고 노트화는 보류.
