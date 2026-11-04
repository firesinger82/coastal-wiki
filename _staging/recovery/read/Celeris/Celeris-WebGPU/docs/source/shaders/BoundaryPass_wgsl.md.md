---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/BoundaryPass_wgsl.md
lines: 33
sha256: 5648023f0195d7dce74c2308012eba3b50add84994eb9ac6c508706628e44eeb
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# BoundaryPass_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/BoundaryPass.wgsl`

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 원문 링크·설명이다(1–3). 경계·파랑/하천 강제·퇴적물·쇄파 복사·습윤/건조를 처리하고 임시 텍스처(texture)를 JavaScript가 복사한다(1–7). 벽의 법선 운동량 반사·cosine 스펀지·`two-cell` 주기 영역·`txWaves` sine/transient·고립파·경계형 `5` `eta/hu/hv`·고정 하천 수위/유량을 지원한다(13–19). 형 `5`는 관측점 공간과 JavaScript가 고른 `two time rows`를 선형 보간한다. 남/북은 x/경도, 서/동은 y/위도이며 `grid_type == 2`에서는 `lon_LL`·`lat_LL`을 더해 절대 도 좌표를 쓴다(21). |
| 23–33 | 강제 후 음수심 제한·단일 셀 습윤/건조 제거·좁은 끝 셀 고정을 수행한다(25). 여러 경계에서 퇴적물을 영값으로 초기화하고 주기 쇄파를 복사하며 일부 하천/강제에서는 지운다(29). 이웃과 내부 해안선에도 영향을 주며 분산성(dispersive) 모드의 암시 풀이 전후 실행한다(33). 좁은 수로 끝 셀 고정은 적절한 경우에 적용한다(25). 이 정리는 해안선 안정성에 중요하다(25). 퇴적물 영값 처리는 여러 forced/damped/solid 경계 영역에서 수행한다(29). 이웃 셀을 읽으며 경계와 해안선 근처 내부 셀에 영향을 줄 수 있다(33). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
