---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/tredge.f
lines: 23
sha256: b260d3c82ba04ff47cbfb12f2009baab1b3446c0b37dc2132029e64b776d8e72
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# tredge.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | TREDGE는 9×15 변환 행렬(transformation matrix) TR을 0으로 초기화하고 첫 세 대각 항을 1.D0으로 설정한다(4–10). 선언과 빈 줄을 포함한다. 원문: `      SUBROUTINE TREDGE(TR)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). `      DIMENSION TR(9,15)` (4). `      TR(:,:) = 0.` (6). `      DO I = 1, 3` (8). `        TR(I,I) = 1.D0` (9). `      ENDDO` (10). |
| 12–23 | 시작 시 1행 TREDGE 루틴 안. 네 열 블록의 대응 성분에 .25D0을 채워 4분의 1 가중 행을 만든다(12–17). 마지막 세 행의 6+I 열에는 1.D0을 넣는다(19–21). END를 포함한다. 원문: `      DO J = 1, 4` (12). `        JP = 3 * ( J - 1 )` (13). `        DO I = 1, 3` (14). `          TR(3+I,JP+I) = .25D0` (15). `        ENDDO` (16). `      ENDDO` (17). `      DO I = 7, 9` (19). `        TR(I,6+I) = 1.D0` (20). `      ENDDO` (21). `      END` (23). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4·12–17: 행렬 크기 9×15와 네 블록의 가중치 .25D0은 고정되어 있다.
