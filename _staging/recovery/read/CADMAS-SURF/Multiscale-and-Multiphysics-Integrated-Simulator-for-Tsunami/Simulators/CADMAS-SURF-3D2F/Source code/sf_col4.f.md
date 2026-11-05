---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_col4.f
lines: 21
sha256: 37631a6e45de7463f8b305944a85397173dbee9623e28f4d53828511d3f2cbce
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_col4.f — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | 크기 4인 IP·JP·JM과 DATA JM / 4, 1, 2, 3 /를 선언하고 IBING=0으로 초기화한다. 원문: `      SUBROUTINE SF_COL4(IBING,IP,JP)` (1); `      DIMENSION IP(4),JP(4),JM(4)` (3); `      DATA JM / 4, 1, 2, 3 /` (4); `      IBING = 0` (6) |
| 8–21 | 시작 시 1행 SF_COL4 루틴 안이다. J1=1..4에서 첫 항 일치를 찾는다. `J2 = JM(J1)` (10)과 `J3 = JM(J2)` (12)를 순서대로 적용한다. `DATA JM / 4, 1, 2, 3 /` (4)에 따라 인덱스 1의 다음 조회값은 4이고, 4의 다음 조회값은 3이며, 3의 다음 조회값은 2이고, 2의 다음 조회값은 1이다. 세 중첩 IF에는 ELSE가 없다. IP(2)·IP(3)가 대응 JP와 같으면 IBING=1이다. 첫 항 일치 분기에서 EXIT한다. 원문: `      DO J1 = 1, 4` (8); `        IF( IP(1) == JP(J1) ) THEN` (9); `          J2 = JM(J1)` (10); `          IF( IP(2) == JP(J2) ) THEN` (11); `            J3 = JM(J2)` (12); `            IF( IP(3) == JP(J3) ) THEN` (13); `              IBING = 1` (14); `            ENDIF` (15); `          ENDIF` (16); `          EXIT` (17); `        ENDIF` (18); `      ENDDO` (19); `      END` (21) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 3·9–14: IP·JP 차원은 4이다. 비교식은 IP(1)·IP(2)·IP(3)만 사용하며 IP(4) 비교문은 없다.
- 9–17: IP(1)과 처음 일치한 JP 항에서 EXIT한다. 같은 값을 가진 JP 항이 뒤에 있어도 그 위치에서는 다시 검사하지 않는다.
