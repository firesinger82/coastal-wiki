---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/Pass3B_COULWAVE_wgsl.md
lines: 24
sha256: 333d30f7cd8e04a0f797a160ec0380caf95d9255edefe4c27de08dd5aac3aaec
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Pass3B_COULWAVE_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/Pass3B_COULWAVE.wgsl`

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 원문 링크·설명이다(1–3). 두 번째 COULWAVE 보조 pass로 `Pass3A_COULWAVE` 출력에서 미분·발생항을 계산한다(1–7). `four 2D` 텍스처(texture)를 `txCW_groupings`로 포장한다. `txCW_STval`: `S`, `T`, `d2udxdy`, `d2vdxdy`; `txCW_STgrad`: `dSdx`, `dSdy`, `dTdx`, `dTdy`; `txCW_Eterms`: `E1`, `E2`, `E`, `dvdx - dudy`; `txCW_FGterms`: `EzST`, `TzS2`, `uSxvSy`, `uTxvTy`다(11–16). pass가 네 2D 텍스처를 쓰고 JavaScript가 나중에 `txCW_groupings`로 포장한다(11). [11-04 전수 검증 보완] |
| 18–24 | `Pass3_COULWAVE`의 고차 발생항에 공급하며 현재 `second-order` 미분 계산 격자 묶음(stencil)을 쓰고 대체 `fourth-order` 블록은 주석이다(20). `E`에 `dU_by_dt.x`를 사용하므로 해당 substep 미분 텍스처가 생성된 뒤 실행해야 한다(24). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20: 문서는 대체 `fourth-order` 미분 블록을 주석으로 구분한다.
