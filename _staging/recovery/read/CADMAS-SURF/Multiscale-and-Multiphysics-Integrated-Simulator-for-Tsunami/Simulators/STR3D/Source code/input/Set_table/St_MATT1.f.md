---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Set_table/St_MATT1.f
lines: 17
sha256: 1eef16b3e0901b72fe7d96e8d85cf7a47f8d1a18a083e33c25c80c2041c4d3ec
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# St_MATT1.f — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | ST_MATT1은 J_MATT1의 외부 재료 번호를 IMATR로 변환하고 2:6 성분을 MATT에 복사한다(5–8). 모든 재료의 5개 성분을 순회하고 양수 표 번호만 ITBM1R로 변환한다(10–15). 배열 MATT(5,NMAT)·J_MATT1(6,N_MATT1)과 역표를 선언한다(3). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE ST_MATT1( MATT, NMAT, J_MATT1, N_MATT1, IMATR, ITBM1R )` (1) <br> `      DIMENSION MATT(5,NMAT), J_MATT1(6,N_MATT1), IMATR(*), ITBM1R(*)` (3) <br> `      DO I = 1, N_MATT1` (5) <br> `        IMAT = IMATR( J_MATT1(1,I) )` (6) <br> `        MATT(:,IMAT) = J_MATT1(2:6,I)` (7) <br> `      ENDDO` (8) <br> `      DO I = 1, NMAT` (10) <br> `        DO J = 1, 5` (11) <br> `          IT = MATT(J,I)` (12) <br> `          IF( IT > 0 ) MATT(J,I) = ITBM1R(IT)` (13) <br> `        ENDDO` (14) <br> `      ENDDO` (15) <br> `      END` (17) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5–7: IMATR 결과가 양수인지 검사하는 조건 없이 MATT(:,IMAT)에 대입한다.
