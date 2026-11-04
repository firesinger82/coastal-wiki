---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Run_Tridiag_Solver_js.md
lines: 30
sha256: 85238521b1831417c480760ea88f469924417c19d2c589ed729e7dad33d014a3
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Run_Tridiag_Solver_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Run_Tridiag_Solver.js`

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | 원문 링크와 Boussinesq/COULWAVE 암시 PCR 실행·계수 교대 제어 역할이다(1–7). 조건 `NLSW_or_Bous == 0`은 `current_stateUVstar`를 `txNewState`로 복사한다(11). 나머지 모드에서 x 반복마다 `p`·`s = 2^p`를 설정한다(15). `p == 0`은 `coefMatx -> newcoef_x`, 홀수는 `newcoef_x -> txtemp_PCRx`, 첫 반복 뒤 짝수는 `txtemp_PCRx -> newcoef_x`다(16). 최종 `txtemp2_PCRx`를 `txNewState`로 복사하고 y는 `coefMaty`, `newcoef_y`, `txtemp_PCRy`, `txtemp2_PCRy`로 반복한다(17–18). 실제 PCR 계산식은 WGSL에 있으며 이 파일은 pass 순서·반복 횟수·계수 전달을 제어한다(7). [11-04 전수 검증 보완] |
| 20–30 | `Px`·`Py`는 `constants_load_calc.js`에서 오며 행/열 축소에 충분해야 한다. WGSL은 wraparound 인덱스, 경계 계수는 항등형을 쓴다(22). COULWAVE는 바닥 바인딩·최종 속도→운동량 변환을 쓴다(24). `txtemp2_PCR*`는 최종 반복에서만 쓰며 `coefMat*`→`newcoef_*` 사전 복사와 `txtemp_PCR*`→`newcoef_*` 반복 복사를 피한다(26). 현재 즉시 제출 방식을 쓰고 이전 반복 복사문은 주석으로 남아 있다고 적는다(30). 경계 행의 항등형 계는 가장자리 셀을 제어된 상태로 유지한다(22). 중간 반복은 축소 계수만 출력한다(26). 주 pass loop는 encoder-stack 방식이며 현재 파일의 즉시 제출 방식과 다르다(30). 활성 경로는 계수 의존성을 bind-group ping-pong으로 처리한다(30). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26·30: 문서는 이전 매 반복 복사문이 주석이며 활성 경로가 계수 텍스처 교대를 사용한다고 적는다.
