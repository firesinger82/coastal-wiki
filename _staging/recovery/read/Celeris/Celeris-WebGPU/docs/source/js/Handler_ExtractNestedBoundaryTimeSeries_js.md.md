---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_ExtractNestedBoundaryTimeSeries_js.md
lines: 21
sha256: 7e27d7659642ed629e702b3e34c98acbb9b9a6b5c96b85f384e520fd94c3d9ff
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_ExtractNestedBoundaryTimeSeries_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_ExtractNestedBoundaryTimeSeries.js`

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 원문 링크·역할 설명(1–7). `ExtractNestedBoundaryTimeSeries.wgsl`의 사용자 사각형 `four edges` 추출용 바인드 그룹(bind group)과 배치를 만든다(7). |
| 9–21 | `0` 격자·사각형 경계/면 길이/표본 인덱스 uniform, `1` 보통 승인된 단계의 `txNewState`, `2/3/4/5` 남/북/서/동 출력, `6` 건조 셀 판별용 바닥 텍스처(texture)다(11–17). 요청 출력 구간을 마칠 때까지 GPU에 유지한 뒤 한 번 회수해 경계형 `5` 파일을 쓴다. 건조 조건 `eta - bottom <= 0`에서는 `eta`, `hu`, `hv`를 영값으로 써 DEM 고도가 수면으로 출력되지 않게 한다(21). binding `0`의 격자 정보는 grid bounds다(11). pass는 사각형 가장자리 셀만 compact 출력 텍스처에 쓴다(21). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
