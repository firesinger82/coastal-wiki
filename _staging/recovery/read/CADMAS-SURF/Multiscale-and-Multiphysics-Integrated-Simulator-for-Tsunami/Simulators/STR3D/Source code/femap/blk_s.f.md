---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/femap/blk_s.f
lines: 7
sha256: 565c6afe46cffcc8beb627f1adc83ea8f1414f11a3a01e93aa5764a729665645
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# blk_s.f — 판독 구간 기록

구간은 1행부터 7행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | BLK_S는 IFL 장치에 공백 세 개를 앞에 둔 -1 구분 문자열을 출력한 뒤 (3X,I0) 형식으로 ID를 출력한다(3–5). 루틴 선언, 빈 줄과 END를 포함한다. 원문: `      SUBROUTINE BLK_S(ID,IFL)` (1). `      WRITE(IFL,'(A)') '   -1'` (3). `      WRITE(IFL,'(3X,I0)') ID` (5). `      END` (7). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
