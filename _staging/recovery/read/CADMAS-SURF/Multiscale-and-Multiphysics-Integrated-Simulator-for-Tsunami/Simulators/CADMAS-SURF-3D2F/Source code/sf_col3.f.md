---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_col3.f
lines: 21
sha256: e7090d5844dcbe09090625a7525855bca4463328ef798b0572bcc204a40bdd67
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_col3.f — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | 크기 3인 IP·JP·JM과 DATA JM / 3, 1, 2 /를 선언한다. 결과 IBING을 0으로 초기화한다. 원문: `      SUBROUTINE SF_COL3(IBING,IP,JP)` (1); `      DIMENSION IP(3),JP(3),JM(3)` (3); `      DATA JM / 3, 1, 2 /` (4); `      IBING = 0` (6) |
| 8–21 | 시작 시 1행 SF_COL3 루틴 안이다. J1=1..3에서 첫 항 일치를 찾는다. `J2 = JM(J1)` (10)과 `J3 = JM(J2)` (12)를 순서대로 적용한다. `DATA JM / 3, 1, 2 /` (4)에 따라 인덱스 1의 다음 조회값은 3이고, 3의 다음 조회값은 2이며, 2의 다음 조회값은 1이다. 세 값 모두 일치하면 IBING=1이다. 세 중첩 IF에는 ELSE가 없다. 첫 항이 일치한 분기의 EXIT는 뒤 항의 일치 여부와 관계없이 실행된다. 원문: `      DO J1 = 1, 3` (8); `        IF( IP(1) == JP(J1) ) THEN` (9); `          J2 = JM(J1)` (10); `          IF( IP(2) == JP(J2) ) THEN` (11); `            J3 = JM(J2)` (12); `            IF( IP(3) == JP(J3) ) THEN` (13); `              IBING = 1` (14); `            ENDIF` (15); `          ENDIF` (16); `          EXIT` (17); `        ENDIF` (18); `      ENDDO` (19); `      END` (21) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–17: IP(1)과 처음 일치한 JP 항에서 EXIT한다. 같은 값을 가진 JP 항이 뒤에 있어도 그 위치에서는 다시 검사하지 않는다.
