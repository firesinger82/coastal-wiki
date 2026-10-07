---
file: models/EFDC/raw/source_code/EFDC-GVC/csndset.for
lines: 28
sha256: b5508c7a52b5aebc45b8298ed9df7a4e1a69080d9f4ad4928e2db5c89f2f1053
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# csndset.for — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 구분 주석과 `REAL FUNCTION CSNDSET(SND,SDEN,IOPT)` (6) 선언. EFDC-FULL 1.0a·2001-11-01 수정 표기, 빈 변경 이력 양식(8–17). 비응집성 퇴적물(noncohesive sediment) 등급 NS의 간섭 침강(hindered settling) 보정을 계산한다는 주석(19–20). EFDC.PAR 포함(22). |
| 24–28 | 시작 시 6행 CSNDSET 함수 안. `ROPT=FLOAT(IOPT)` (24); `CSNDSET=(1.-SDEN*SND)**ROPT` (25). IOPT를 실수 지수 ROPT로 바꿔 1−SDEN*SND의 거듭제곱을 반환한다. 주석·RETURN·END(26–28). 조건 분기·호출문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24–25: IOPT는 FLOAT를 거쳐 거듭제곱 지수로 사용된다. 밑 1.-SDEN*SND와 IOPT의 범위를 검사하거나 제한하는 조건문은 없다.

