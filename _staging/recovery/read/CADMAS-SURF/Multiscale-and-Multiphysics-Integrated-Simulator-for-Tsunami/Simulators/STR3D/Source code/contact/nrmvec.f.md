---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/nrmvec.f
lines: 10
sha256: c5e49f751f44c63cfe87f69c5fbba008946a73daee5d31bcabeea6944ff42fd8
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# nrmvec.f — 판독 구간 기록

구간은 1행부터 10행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | NRMVEC는 세 점 X의 두 차 벡터(vector) V12,V13을 계산하고 CROSS2(V12,V13,RN)을 호출한다(6–8). 암시적 형, 배열 선언, 빈 줄과 END를 포함한다. CROSS2 내부는 이 파일에 없다. 원문: `      SUBROUTINE NRMVEC(RN,X)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). `      DIMENSION X(3,3),V12(3),V13(3),RN(3)` (4). `      V12(:) = X(:,2) - X(:,1)` (6). `      V13(:) = X(:,3) - X(:,1)` (7). `      CALL CROSS2(V12,V13,RN)` (8). `      END` (10). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
