---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/SedTrans_UpdateBottom_testing_wgsl.md
lines: 19
sha256: 555ce1b0cc17c106503b171cdca7a08e2418e9c082eed6efad58c1bfd6cc69e3
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# SedTrans_UpdateBottom_testing_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/SedTrans_UpdateBottom_testing.wgsl`

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 원문 링크와 실험적 퇴적물 바닥 갱신이다(1–7). 누적 변위를 계산하나 활성 코드 경로에서는 대체로 초기 바닥을 유지한다고 적는다(7). 현재 선택은 이 파일이 아닌 `SedTrans_UpdateBottom.wgsl`이다(11). |
| 13–19 | 간격 갱신용 `n_sim`, `sedUpdateInt`·최근 변화 경로가 있지만 상당 부분은 주석이며 활성 handler와 배치도 다르다(15). 시험용으로 취급하고 handler·JavaScript 실행을 재구성하기 전 운영 동작에 의존하지 말라고 적는다(19). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11: 문서는 현재 비활성 시험 변형으로 구분한다.
- 15: 문서는 간격 갱신 로직 상당 부분이 주석이고 활성 handler와 배치가 다르다고 적는다.
