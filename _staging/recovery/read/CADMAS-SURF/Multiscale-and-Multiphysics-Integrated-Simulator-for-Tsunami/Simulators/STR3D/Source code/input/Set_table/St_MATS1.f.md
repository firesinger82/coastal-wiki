---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Set_table/St_MATS1.f
lines: 18
sha256: d2b735d322ec7422e26e19f767fb0c41635fa2b38487d09e47991ee32bc44042
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# St_MATS1.f — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | ST_MATS1은 재료(material) 역표로 IMAT를 얻는다(7–9). IMAT가 양수일 때만 MAT 두 번째 성분과 AMAT의 11·12·13 성분을 채운다(10–15). R_MATS1의 2·1·3 순서를 각각 사용한다(12–14). 인수 배열 범위와 암시적 배정밀도 선언을 포함한다(1–5). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE ST_MATS1( MAT, AMAT, IMATR, J_MATS1, R_MATS1, N_MATS1 )` (1) <br> `      IMPLICIT REAL*8 (A-H,O-Z)` (3) <br> `      DIMENSION MAT(2,*), AMAT(33,*), IMATR(*), J_MATS1(2,N_MATS1),` (4) <br> `     &          R_MATS1(3,N_MATS1)` (5) <br> `      DO I = 1, N_MATS1` (7) <br> `        MID = J_MATS1(1,I)` (8) <br> `        IMAT = IMATR(MID)` (9) <br> `        IF( IMAT > 0 ) THEN` (10) <br> `          MAT(2,IMAT) = J_MATS1(2,I)` (11) <br> `          AMAT(11,IMAT) = R_MATS1(2,I)` (12) <br> `          AMAT(12,IMAT) = R_MATS1(1,I)` (13) <br> `          AMAT(13,IMAT) = R_MATS1(3,I)` (14) <br> `        ENDIF` (15) <br> `      ENDDO` (16) <br> `      END` (18) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
