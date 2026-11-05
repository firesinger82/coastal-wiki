---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/partition/ex_add.f
lines: 21
sha256: 86f2de5a28eb36ab16e8169d7656e5e28c5083fbe33e8945888837ad80263b2a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ex_add.f — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | EX_ADD의 인수·배열 선언과 탐색 시작 위치 J=1 초기화. 원문: `      SUBROUTINE EX_ADD(IADW,IAD,NI,NO,NJ)` (1); `      DIMENSION IADW(NI),IAD(NI),NO(NJ)` (3); `      J = 1` (5). |
| 7–21 | EX_ADD 루틴 안. IAD의 각 경계에 대해 NO를 현재 J부터 순차 탐색한다. JP가 경계 이하이면 끝 위치를 갱신하고 경계를 넘으면 내부 루프를 빠져나온다. 원문: `      DO I = 1, NI` (7); `        IE = IAD(I)` (8); `        IADW(I) = J - 1` (9); `        JS = J` (10); `        DO J = JS, NJ` (11); `          JP = NO(J)` (12); `          IF( JP <= IE ) THEN` (13); `            IADW(I) = J` (14); `          ELSEIF( JP > IE ) THEN` (15); `            EXIT` (16); `          ENDIF` (17); `        ENDDO` (18); `      ENDDO` (19); `      END` (21). 13·15행의 IF/ELSEIF 사슬에는 ELSE가 없다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5–18: J를 1로 한 번 초기화하며 외부 I 루프마다 재설정하지 않는다. NO와 IAD의 정렬 상태를 검사하는 문장은 없다.
