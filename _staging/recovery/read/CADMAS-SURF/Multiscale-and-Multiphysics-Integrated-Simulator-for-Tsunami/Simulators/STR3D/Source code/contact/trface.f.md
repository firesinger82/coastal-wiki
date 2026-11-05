---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/trface.f
lines: 23
sha256: cc1b4abeb550617cee761fef2855ecbc371c68f1467c3c07c6f1ea18248425fa
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# trface.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | TRFACE는 12×15 변환 행렬(transformation matrix) TR을 0으로 초기화하고 첫 여섯 대각 항을 1.D0으로 설정한다(4–10). 선언과 빈 줄을 포함한다. 원문: `      SUBROUTINE TRFACE(TR)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). `      DIMENSION TR(12,15)` (4). `      TR(:,:) = 0.` (6). `      DO I = 1, 6` (8). `        TR(I,I) = 1.D0` (9). `      ENDDO` (10). |
| 12–23 | 시작 시 1행 TRFACE 루틴 안. 네 열 블록의 대응 성분에 .25D0을 채워 7–9행의 가중 행을 만든다(12–17). 마지막 세 행의 3+I 열에는 1.D0을 넣는다(19–21). END를 포함한다. 원문: `      DO J = 1, 4` (12). `        JP = 3 * ( J - 1 )` (13). `        DO I = 1, 3` (14). `          TR(6+I,JP+I) = .25D0` (15). `        ENDDO` (16). `      ENDDO` (17). `      DO I = 10, 12` (19). `        TR(I,3+I) = 1.D0` (20). `      ENDDO` (21). `      END` (23). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4·12–17: 행렬 크기 12×15와 네 블록의 가중치 .25D0은 고정되어 있다.
