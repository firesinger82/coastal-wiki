---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/SedTrans_Pass3_wBedUpdate_wgsl.md
lines: 19
sha256: 5e60a55b85363d2b91c51f08916bf61b0d0b87f28707719228c18c0fa8101464
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# SedTrans_Pass3_wBedUpdate_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/SedTrans_Pass3_wBedUpdate.wgsl`

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 원문 링크와 한 셰이더에서 부유 농도·바닥을 함께 갱신하려는 prototype이다(1–7). 비활성이고 현재는 `SedTrans_Pass3.wgsl` 다음 `SedTrans_UpdateBottom.wgsl`을 쓴다(11). |
| 13–19 | 바인딩 목록에 선언하지 않은 bed-state·bed-gradient 텍스처(texture) 같은 식별자를 참조하므로 불완전 prototype으로 취급하라고 적는다(15). 재개 시 완전한 handler/배치를 먼저 정하고 결합 비용을 판단하라고 적는다(19). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11: 문서는 현재 비활성 prototype으로 구분한다.
- 15: 문서는 바인딩에 선언되지 않은 bed-state·bed-gradient 식별자 참조를 적는다.
