---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/femap/wt_zero_i.f
lines: 9
sha256: 5589f20ed7f3df70eec70cbb195e382b8c604009589b8c83a6dd31b26001ac1c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# wt_zero_i.f — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | WT_ZERO_I는 먼저 개수 N과 쉼표를 출력한다. implied-DO의 I=1,N 범위로 정수 0과 쉼표를 출력한다. 포맷은 한 레코드당 10쌍이다. 원문: `      SUBROUTINE WT_ZERO_I(N,IFL)` (1); `      CHARACTER*1 C /','/` (3); `      WRITE(IFL,'(I0,A)') N,C` (5); `      WRITE(IFL,'(10(I1,A))') (0,C,I=1,N)` (7); `      END` (9) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
