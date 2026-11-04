---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Run_Compute_Shader_js.md
lines: 27
sha256: e1cbebe65f1b39a0082dce99a0d6c8316d25e5c54a66c776c39ca007ec3155a0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Run_Compute_Shader_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Run_Compute_Shader.js`

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 원문 링크와 `main.js`의 공통 WebGPU 실행·복사 보조 역할이다(1–7). 즉시 helper는 encoder 생성·계산/복사 기록·명령 종료·제출을 하며 `_EncStack` 변형은 기존 encoder에 누적해 적은 제출로 묶는다(11–13). `fetchShader()`는 URL/경로의 WGSL을 실행 시 가져온다(17). 공통 helper는 shader마다 command-encoder boilerplate를 중복하는 일을 피한다(7). `_EncStack`은 기존 encoder를 반환한다(13). 실행 중 shader fetch는 앱이 정적이고 bundle되지 않기 때문에 사용하는 소스 로드 방식이다(17). [11-04 전수 검증 보완] |
| 19–27 | 실행 크기는 `calc_constants.DispatchX`·`DispatchY`이며 일반 셰이더 `@workgroup_size(16, 16)`가 격자를 덮어야 한다(21). 임시 저장 출력을 원래 상태 텍스처(texture)에 복사하는 동작도 수치 알고리즘의 일부다(23). 단계 루프에서는 encoder 누적 helper를 쓰고 상대 경로는 서비스 루트 기준으로 유지하라고 적는다(27). 추가 즉시 제출은 성능을 떨어뜨리고 동기화 시점을 바꿀 수 있다(27). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
