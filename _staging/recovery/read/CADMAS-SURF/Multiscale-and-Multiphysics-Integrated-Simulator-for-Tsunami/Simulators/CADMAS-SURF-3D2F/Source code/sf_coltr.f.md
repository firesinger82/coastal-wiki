---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_coltr.f
lines: 15
sha256: 95ac9aad3d79cf78b245f641e522d866bb0873397d2cc8c09ed9f1fa0f2dae27
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_coltr.f — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | IP(3)와 JP(NP)를 선언한다. IP의 세 항 각각에 대해 JP의 1..NP를 검색한다. 일치하면 GOTO 10으로 바깥 I 루프의 ENDDO에 이동한다. 한 항이라도 없으면 IBING=0으로 즉시 반환한다. 세 항이 모두 발견되면 IBING=1로 끝낸다. 원문: `      SUBROUTINE SF_COLTR(IBING,IP,JP,NP)` (1); `      DIMENSION IP(3),JP(NP)` (3); `      DO I = 1, 3` (5); `        DO J = 1, NP` (6); `          IF( IP(I) == JP(J) ) GOTO 10` (7); `        ENDDO` (8); `        IBING = 0` (9); `        RETURN` (10); `   10 ENDDO` (11); `      IBING = 1` (13); `      END` (15) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5–13: JP에서 발견한 항을 소비하거나 표시하는 배열은 없다. 같은 JP 항이 서로 다른 IP 항의 일치 검사에 반복 사용될 수 있다.
