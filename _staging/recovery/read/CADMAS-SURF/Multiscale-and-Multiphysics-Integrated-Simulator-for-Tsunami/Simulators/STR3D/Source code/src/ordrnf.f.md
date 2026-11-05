---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/ordrnf.f
lines: 30
sha256: 4afd92ebbeea27b6aa70079cd0e2781bac925d14edafdc15d116796d6f4df931
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ordrnf.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | 입구와 선언이다(1–10). 주석은 고유값(eigenvalue) A를 내림차순으로 정렬하고 대응 고유벡터(eigenvector) B를 함께 옮긴다고 설명한다(5–8). 원문: `      SUBROUTINE ORDRNF(A,B,N,NB)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); 주석: `C      ORDERING IN DESCENDING SEQUENCE` (5); 주석: `C      OUTPUT` (7); 주석: `C      A...EIGVAL,B(I,1)..1ST EIGVECTR, B(I,2)..2ND EIGVECTR...` (8); `      DIMENSION A(*),B(NB,*)` (10) |
| 12–30 | 시작 시 ORDRNF 루틴(1) 안이다. 각 J에서 남은 A의 최댓값 위치 IM을 찾고 A와 B의 열을 교환한다(12–27). 원문: `      NM=N-1` (12); `      DO 4000 J=1,NM` (13); `      VMAX=-1.0E+30` (14); `      DO 2000 I=J,N` (15); `      IF(A(I).LT.VMAX) GO TO 2000` (16); `      IM=I` (17); `      VMAX=A(I)` (18); ` 2000 CONTINUE` (19); `      AA=A(J)` (20); `      A(J)=A(IM)` (21); `      A(IM)=AA` (22); `      DO 3000 K=1,NB` (23); `      BB=B(K,J)` (24); `      B(K,J)=B(K,IM)` (25); ` 3000 B(K,IM)=BB` (26); ` 4000 CONTINUE` (27); `      RETURN` (29); `      END` (30) `GO TO 2000`(16)의 대상은 19행의 `2000 CONTINUE`이다. 이 이동은 `A(I).LT.VMAX`일 때 IM 갱신을 건너뛴다. 같거나 큰 값에서는 IM을 I로 갱신한다(17). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–22: VMAX의 초기값은 -1.0E+30이다. IM은 `IF(A(I).LT.VMAX) GO TO 2000`(16)에서 이동하지 않을 때 대입한다(17). 이 루프 앞에는 IM 초기화가 없다. [11-04 전수 검증 정정]
