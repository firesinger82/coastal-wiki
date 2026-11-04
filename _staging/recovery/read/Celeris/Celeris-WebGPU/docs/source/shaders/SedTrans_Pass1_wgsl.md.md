---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/SedTrans_Pass1_wgsl.md
lines: 24
sha256: 565902aef14cf4c113972579de33f24c60518a1aaf69fd7d5ab586f310095ca7
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# SedTrans_Pass1_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/SedTrans_Pass1.wgsl`

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 원문 링크와 `up to four sediment classes` 면 농도 재구성이다(1–7). 표준 `Pass1`처럼 minmod·습윤/건조 보호로 재구성한 뒤 `txH`의 면수심으로 나눠 농도형 값을 얻는다(11). |
| 13–24 | `txSed_C1` through `txSed_C4`의 `x/y/z/w`는 북/동/남/서면이다(15–20). `four classes`를 재구성하지만 뒤 로직 상당수는 `class 1`을 쓰므로 의도적 단순화가 아니면 다등급 배치를 유지한다(24). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
