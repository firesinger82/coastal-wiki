---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/TriDiag_PCRy_wgsl.md
lines: 29
sha256: 313e3bd35ce1a0df97c8be4b5e320d0e881e2777bdb69a7b071c3e1e5c2bbcb3
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# TriDiag_PCRy_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/TriDiag_PCRy.wgsl`

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 원문 링크·설명이다(1–3). 표준 Boussinesq y방향 병렬 순환 축소(Parallel Cyclic Reduction, PCR) 한 반복이다(1–7). 입력은 y계수·보통 x풀이 뒤 상태·첫 반복 y 운동량 우변 `current_stateUVstar`의 `b`·전체 y반복 uniform `P`다(13–16). `txtemp`는 다음 계수, `txtemp2`는 최종 반복에서만 갱신한 y 운동량 해다(20–21). |
| 23–29 | `TriDiag_PCRx.wgsl`과 같으나 y 이웃을 높이 modulo로 읽는다. `txtemp`는 항상 쓰고 `p == P - 1`에서만 `current_state`를 읽고 `txtemp2`를 쓴다(25). 두 방향 순서는 JavaScript가 정하며 채널 변경 시 `Run_Tridiag_Solver.js`·x변형을 수정한다(29). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
