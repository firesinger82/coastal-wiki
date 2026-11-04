---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_SedTrans_Pass1_js.md
lines: 26
sha256: d18c1b1714a5efd66629050b08410afbbc21cb3c2e5e63be82d857bdd8e3f9ab
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_SedTrans_Pass1_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_SedTrans_Pass1.js`

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 원문 링크와 `SedTrans_Pass1.wgsl`의 퇴적물 농도 재구성 바인드 그룹(bind group)이다(1–7). |
| 9–26 | `0` 퇴적물/계산 uniform, `1` 현재 `txState_Sed`, `2` `txBottom`, `3` 물 면수심 `txH`, `4/5/6/7` 출력 `txSed_C1`/`txSed_C2`/`txSed_C3`/`txSed_C4`다(11–18). `up to four` 농도 등급을 `txH`, `txU`, `txV`와 같은 면 순서로 재구성한다(22). 현재 주로 `class 1`을 쓰지만 `four-class` 배치를 유지하라고 적는다(26). 네 binding을 유지하라는 지침의 예외는 전체 퇴적물 pipeline을 의도적으로 축소하는 경우다(26). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
