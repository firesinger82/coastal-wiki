---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_Updateneardry_js.md
lines: 21
sha256: e52410e50e425e906a84ff115f9c7e3f1c636b630a9e492cc6fdc73a17288697
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Updateneardry_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_Updateneardry.js`

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 원문 링크와 `Update_neardry.wgsl`의 바닥 변경 후 메타자료 바인드 그룹(bind group) 설명이다(1–7). `0` 격자 크기 uniform, `1` 현재 `txBottom`, `2` near-dry·섬 정리를 반영한 저장 출력 `txtemp_bottom`이다(11–13). |
| 15–21 | 지형 편집·이동 바닥·퇴적물 갱신 후 실행하고 JavaScript가 `txtemp_bottom`을 `txBottom`으로 복사한다(17). near-dry는 Boussinesq/COULWAVE의 분산성(dispersive) 항과 삼중대각 계수에 영향을 주므로 바닥 변경 뒤 실행해야 한다(21). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
