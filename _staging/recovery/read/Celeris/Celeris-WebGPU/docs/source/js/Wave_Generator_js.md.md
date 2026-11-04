---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Wave_Generator_js.md
lines: 30
sha256: 0175b1011723d6098e8b68939c7000c348ee52121c8c9606911bde252c861b74
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Wave_Generator_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Wave_Generator.js`

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 원문 링크와 UI 입사파를 `main.js`의 `txWaves` 업로드 전에 CPU 행으로 만드는 역할이다(1–7). 행은 `waves.txt`와 같은 amplitude·period·라디안 direction·라디안 random phase다(9–14). |
| 16–23 | `buildSineWaveData(calc_constants)`는 단일 성분의 진폭을 `incident_wave_H / 2`로 만든다. 입사 경계의 횡방향 `two boundaries`가 주기이면 양 끝 위상이 맞도록 방향을 조정하고 아니면 요청 방향을 유지한다(18). `buildTmaWaveData(calc_constants)`는 고정 스펙트럼 계수의 JONSWAP/TMA이며 피크 `incident_wave_T`·`incident_wave_direction`, `about 100 frequencies`, `1 / (3 * incident_wave_T)`부터 `3 / incident_wave_T`다(20). 방향은 `nine directions`, `incident_wave_direction - 20`부터 `incident_wave_direction + 20` degrees, `5-degree` 간격이다. 주기이면 `boundaryLength - 2 * ds`와 `BoundaryPass.wgsl` 인덱스 `1`부터 `N-2`를 사용한다. 정수 경계 파수의 식은 `k_parallel = sign(k_parallel_raw) * 2*pi*N / activeBoundaryLength`이며 비주기이면 방향을 유지한다(22). 주기 방향 맞춤은 입사 경계에 횡방향인 두 경계가 주기인 경우 업로드 전에 적용한다(22). 각 성분은 경계 방향 파랑 수를 정수로 선택하여 활성 양 끝의 위상을 맞춘다(22). [11-04 전수 검증 보완] |
| 24–30 | TMA 캐시 키는 파고·주기·방향·격자 간격·경계 형상·기준 수심·활성 경계형이다. 무관한 UI 변경에서 난수 위상을 보존하고 입사 조건/형상이 바뀌면 재생성한다(26). `GENERATED_BOUNDARY_WAVE_TEXTURE_CAPACITY`를 내보내 `waves.txt`가 `one row`만 있어도 `main.js`가 충분한 `txWaves` 행을 할당하게 한다(30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20: 문서는 JONSWAP/TMA 생성이 고정 스펙트럼 계수를 사용한다고 적는다.
