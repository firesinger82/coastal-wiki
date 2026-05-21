# textbook 통합 정책

## 원본 위치

원본 PDF는 **`D:\Study\textbook\`에 그대로 보관**. wiki에 복사·심볼릭 링크하지 않음.

이유:
- PDF는 git에 부담 (LFS 불필요)
- 교과서는 변경 없는 자료 → 원본 위치 안정
- 인용 시 절대 경로로 명시 가능

## 노트 작성 규칙

`textbook/notes/`에 챕터·섹션별 발췌·요약을 둠.

### 파일명

`<topic>-<source-shortname>-<chapter>.md`

예시:
- `tides-tides-and-currents-ch3.md` (Tides and Currents, Chapter 3)
- `sediment-mechanics-of-sediment-transport-ch5.md`
- `efdc-efdc-manual-ch12.md`

### 노트 상단 메타블록 필수

```yaml
---
source: "D:\\Study\\textbook\\134340780-Tides-and-Currents.pdf"
source_title: "Tides and Currents"
chapter: 3
pages: "45-72"
topic: tides
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification: unverified | spot-checked | full-checked
---
```

### 본문 구조

1. **핵심 정의·공식** — 원문에서 직접 추출. 인용 시 페이지 명시.
2. **요약** — 요지 정리 (AI 가공 구간임을 명시).
3. **수식·도표** — LaTeX/Markdown으로 옮기되 원문 페이지 인용.
4. **연결** — `concepts/<topic>/` 문서로의 링크.

### 인용 표기

본문 내에서:
- 직접 인용: `> "원문..." (Tides and Currents, p.47)`
- paraphrase: `... (Tides and Currents, ch3 §3.2)`

### AI 요약 검증 단계

| 단계 | 의미 |
|---|---|
| `unverified` | AI 단일 패스 요약. 사용자 검토 전 |
| `spot-checked` | 사용자가 핵심 부분 원문 대조 |
| `full-checked` | 전체 원문 대조 완료 |

객관 레이어로 인용하려면 최소 `spot-checked` 필요. `concepts/`에 인용 시 `verification: spot-checked` 이상 노트만.

## 원본 PDF 목록 인덱스

[INDEX.md](INDEX.md) 참조 — `D:\Study\textbook\` 전체 목록을 토픽별로 분류.

## 우선순위

작업 우선 토픽이 정해진 후 그에 맞는 PDF부터 노트화. 한 권 전체 노트는 권장하지 않음 — 필요한 챕터 단위로 진행.
