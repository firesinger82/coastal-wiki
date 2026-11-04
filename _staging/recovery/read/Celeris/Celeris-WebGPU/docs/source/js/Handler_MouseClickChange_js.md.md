---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_MouseClickChange_js.md
lines: 26
sha256: b9b66fa418aa8dcbb53b0f29ac94863bc08f9a1a1b2699725dcb5c3243e30921
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_MouseClickChange_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_MouseClickChange.js`

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 원문 링크·역할 설명(1–7). `MouseClickChange.wgsl`의 지형·마찰·추적자/발생원·수면·설계 편집용 바인드 그룹(bind group)을 만든다(7). |
| 9–26 | `0` 편집 uniform, `1` `txBottom`, `2` `txBottomFriction`, `3` `txContSource`, `4` `txState`, `5` `txDesignComponents`, `6` 첫 임시 출력, `7` 두 번째 임시 출력이다(11–18). 방사형 브러시를 병렬 적용하며 `main.js`가 활성 패널·편집 표면에 따라 복사할 임시 출력을 정한다(22). 지형·해수면 편집 뒤 near-dry를, Boussinesq/COULWAVE에서는 삼중대각 계수를 갱신해야 한다(26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
