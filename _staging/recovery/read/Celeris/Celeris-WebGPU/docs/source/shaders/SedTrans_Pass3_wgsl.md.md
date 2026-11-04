---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/SedTrans_Pass3_wgsl.md
lines: 33
sha256: 4f5069ac80cedb63b2b3324bb4d64c0a2ef32b4c91be7f8be6cb0ca001f9cd61
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# SedTrans_Pass3_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/SedTrans_Pass3.wgsl`

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | 원문 링크와 부유사 농도·침식·퇴적·소류사 경사 갱신이다(1–7). 물 상태·면속도·퇴적물 유량·바닥·hard bottom·쇄파를 읽어 부유사 유량 발산·마찰/전단속도·Shields/critical-Shields 침식·낙하 퇴적·hard-bottom 침식 억제·`class 1` Meyer-Peter/Muller형 소류사 경사를 계산한다(11–18). |
| 20–33 | 물과 같은 명시·예측/수정 및 이전/예측 미분 텍스처(texture)를 쓰고 음의 농도를 영값으로 제한한다(22). 출력 `txNewState_Sed`는 농도, `dU_by_dt_Sed`는 이력 미분, `erosion_Sed`는 침식+소류사 경사, `depostion_Sed`는 퇴적이다(26–29). JavaScript와 공유하는 철자 `depostion_Sed`를 보존하라고 적는다(33). `erosion_Sed`는 후속 bottom update에서 사용한다(28). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 29·33: 문서는 퇴적 출력 철자를 `depostion_Sed`로 명시한다.
