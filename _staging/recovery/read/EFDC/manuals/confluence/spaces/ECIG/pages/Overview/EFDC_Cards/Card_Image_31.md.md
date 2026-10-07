---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_31.md
lines: 34
sha256: d6a7ced8632187d4549ca83c38237d6bbddd4d1905399999e2e9c1ded905038b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_31.md — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | C31 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 시간에 대해 일정한 제트·플룸 공급원(time constant jet/plume source)의 일정 유입 농도(inflow concentration) 제목을 제시한다(10). 빈 줄과 주석 표식도 포함한다(11–13). 원문: ` C31 TIME CONSTANT INFLOW CONCENTRATIONS FOR TIME CONSTANT JET/PLUME SOURCES ` (10). |
| 14–21 | 점착성 퇴적물(cohesive sediment) — 농도 배열 표기와 범위를 제시한다(14–16). 처음 NSED개 값이 점착성 퇴적물이며, 해당 수송이 비활성일 때도 단일 기본값이 필요하다고 적는다(18–20). 원문: ` \* SED: NSED COHESIVE SEDIMENT CONCENTRATIONS CORRESPONDING TO ` (14); ` \*          INFLOW ABOVE WRITTEN AS SEDC(N), N=1,NSED. I.E., THE FIRST ` (16); ` \*          NSED VALUES ARE COHESIVE A SINGLE DEFAULT VALUE IS REQUIRED ` (18); ` \*          EVEN IF COHESIVE SEDIMENT TRANSPORT IS INACTIVE ` (20). |
| 22–31 | 비점착성 퇴적물(non-cohesive sediment) — 농도 배열 표기와 범위를 제시한다(22–24). 마지막 NSND개 값이 비점착성 퇴적물이며, 해당 수송이 비활성일 때도 단일 기본값이 필요하다고 적는다(26–28). 원문: ` \* SND: NSND NON-COHESIVE SEDIMENT CONCENTRATIONS CORRESPONDING TO ` (22); ` \*          INFLOW ABOVE WRITTEN AS SND(N), N=1,NSND. I.E., THE LAST ` (24); ` \*          NSND VALUES ARE NON-COHESIVE. A SINGLE DEFAULT VALUE IS ` (26); ` \*          REQUIRED EVEN IF NON-COHESIVE SEDIMENT TRANSPORT IS INACTIVE ` (28). |
| 32–34 | C31 입력 형식 — SED1과 SND1 열 이름(32)을 제시한다. 자료 위치에는 Jet/Plume 주석만 있다(34). 사이 빈 줄도 구간에 포함한다(33). 원문: ` C31 SED1  SND1  ! ID ` (32); `                             ! Jet/Plume ` (34). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 18–20·26–28·32–34행: 설명은 두 퇴적물 수송이 비활성일 때도 단일 기본값을 요구한다. 입력 예시의 자료 줄(34)은 `! Jet/Plume` 주석만 있고 `SED1`과 `SND1`의 농도 값은 없다.
