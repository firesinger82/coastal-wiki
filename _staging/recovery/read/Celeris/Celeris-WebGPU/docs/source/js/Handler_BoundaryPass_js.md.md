---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_BoundaryPass_js.md
lines: 32
sha256: 0212ab663023473191f982c6fe72d1c6a000026456f079c16c5515c1875cfd2c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_BoundaryPass_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_BoundaryPass.js`

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 원문 링크·역할 설명(1–7). `BoundaryPass.wgsl`의 명시·암시 갱신 후 경계와 습윤/건조 정리를 위한 바인드 그룹(bind group)을 만든다(7). |
| 9–32 | `0` 경계/계산 uniform, `1` 물 상태, `2` `txBottom`, `3` `txWaves`, `4` 퇴적물 상태, `5` 임시 물 상태, `6` 임시 퇴적물, `7` `txBreaking`, `8` 임시 쇄파, `9` `txBoundaryForcing`, `10/11/12/13`은 각각 남/북/서/동 경계형 `5` 시계열 텍스처(texture)다(11–24). 벽·스펀지·주기 교환·입사파·시계열·하천 수위/유량·경계 퇴적물 초기화·해안선 정리를 처리하며 JavaScript가 임시 결과를 복사한다(28). 분산성(dispersive) 모드에서는 단계마다 여러 번 실행해 명시 상태와 PCR 이후 상태에 모두 영향을 준다고 적는다(32). binding `1`·`4`·`7`은 입력이며 `5`·`6`·`8`은 출력이다(12–19). `txWaves`는 wave-forcing 행을 담는다(14). 임시 출력은 dispatch 뒤 canonical 텍스처로 복사한다(28). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
