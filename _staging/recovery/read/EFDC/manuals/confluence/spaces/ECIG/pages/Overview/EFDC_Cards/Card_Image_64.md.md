---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_64.md
lines: 24
sha256: 4e740354b904bb66b2ad1c4ec63f0e76f26b816e3119df7f7adf9cc65d759567
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_64.md — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 원문 메타데이터(frontmatter) — 문서 ID·제목·space·URL·버전·갱신 시각·계층 경로를 적는다(1–9). |
| 10–22 | C64 TIME CONSTANT BOTTOM CONC ON NORTH CONC BOUNDARIES — 북측 농도 경계(concentration boundary)의 시간 불변 저층(bottom layer) 유입 점착성 퇴적물(cohesive sediment)·비점착성 퇴적물(non-cohesive sediment) 농도를 설명한다(10–20). 앞의 `NSED`개 값과 뒤의 `NSND`개 값을 구분한다(16·20). 주석 표식과 빈 줄을 포함한다(11–22). 원문: `C64 TIME CONSTANT BOTTOM CONC ON NORTH CONC BOUNDARIES` (10); `\* SED: NSED ULTIMATE INFLOWING BOTTOM LAYER COHESIVE SEDIMENT` (14); `\*          CONCENTRAIONS FIRST NSED VALUES SED(N), N=1,NSND` (16); `\* SND: NSND ULTIMATE INFLOWING BOTTOM LAYER NON-COHESIVE SEDIMENT` (18); `\*          CONCENTRATIONS LAST NSND VALUES SND(N), N=1,NSND` (20). |
| 23–24 | C64 입력 열 제목 — `SED1`과 `SND1` 열을 제시한다(24). 앞 빈 줄을 포함한다(23). 원문: `C64 SED1 SND1` (24). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14–16행: 점착성 퇴적물 설명은 `NSED`와 `FIRST NSED VALUES`를 쓰지만 배열의 끝 첨자는 `N=1,NSND`로 적는다.

