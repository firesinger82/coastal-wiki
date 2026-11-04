---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/TriDiag_PCRx_wgsl.md
lines: 33
sha256: 14777d5b457f7cff1aa0ef9be5b7f4f4a41c1b91fdb28fffcfe3ea730ebde1c0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# TriDiag_PCRx_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/TriDiag_PCRx.wgsl`

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 원문 링크와 표준 Boussinesq x방향 병렬 순환 축소(Parallel Cyclic Reduction, PCR) 한 반복이다(1–7). 입력은 현재 x계수·상태·첫 반복의 x 운동량 우변 `current_stateUVstar`의 `g`, 최종 검출 uniform `P`다(13–16). `txtemp`는 다음 축소 계수, `txtemp2`는 최종 반복에서만 갱신 x 운동량 해다(20–21). uniform `P`는 전체 x PCR 반복 수다(16). [11-04 전수 검증 보완] |
| 23–33 | 조건 `p == 0`은 대각으로 계수를 정규화하고 `current_stateUVstar.g`에서 우변을 읽는다. 이후 계수 alpha에 저장된 축소 계수·우변을 읽는다(25). `txtemp`는 항상 쓰며 `p == P - 1`에서만 `current_state`를 읽고 `txtemp2`를 써 JavaScript 계수 교대를 지원한다(27). 이웃 인덱스는 폭으로 modulo 순환하며 경계 행은 계수 갱신에서 항등형이어야 한다(29). 해에서 x 운동량을 갱신한 뒤 `TriDiag_PCRy.wgsl`이 이어진다(33). [11-04 전수 검증 정정] 이 방식은 중간 solution 출력을 생략한다(27). 해 텍스처에서 갱신 대상은 x 운동량 성분뿐이다(33). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
