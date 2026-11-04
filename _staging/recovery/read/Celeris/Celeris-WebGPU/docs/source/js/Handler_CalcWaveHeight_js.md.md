---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_CalcWaveHeight_js.md
lines: 24
sha256: b03e8a6cc2a78cd3c10ac837c1286011dbe3f16cd81343836c5a408515677858
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_CalcWaveHeight_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_CalcWaveHeight.js`

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 원문 링크·역할 설명(1–7). `CalcWaveHeight.wgsl`의 누적 파고 통계용 바인드 그룹(bind group)을 만든다(7). |
| 9–24 | `0` 파고 uniform, `1` `txState`, `2` `txNewState`, `3` `txMeans`, `4` `txWaveHeight`, `5` 임시 파고 출력이다(11–16). 평균 주위 eta 분산으로 RMS/대표 유의파고를 계산하고 영점 교차법은 주석에 남아 있다고 적는다(20). `txWaveHeight` 채널 변경 시 `fragment.wgsl`, `ExtractTimeSeries.wgsl`, 색상 막대 이름을 맞추라고 적는다(24). `txWaveHeight`의 채널 의미는 시각화·출력을 위한 계약이다(24). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20: 문서는 영점 교차 파고법이 주석 처리되어 있다고 적는다.
