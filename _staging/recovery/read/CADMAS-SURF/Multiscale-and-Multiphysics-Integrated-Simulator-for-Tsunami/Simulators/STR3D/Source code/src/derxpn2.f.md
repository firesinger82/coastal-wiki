---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/derxpn2.f
lines: 16
sha256: 0704d1d4b3866f6da93836f3dd6cc9c3369f5a3e9f648cbea6895d542df5a70c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# derxpn2.f — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | DERXPN2의 입출력과 배열을 선언한다. `節点数`는 절점 수(number of nodes), `節点座標`는 절점좌표(nodal coordinate)다. DNDX는 공간 미분, DET는 야코비안(Jacobian) 행렬식이다. 원문: `      SUBROUTINE DERXPN2(DNDX,DET,N,X,XG1,XG2,XG3,ITO)` (1); 주석 원문 `!     DNDX : OUT : DNDX(i,j) = ∂Nj/∂xi` (3); 주석 원문 `!     DET  : OUT : \|J\| ( Jij = ∂xj/∂ξi )` (4); 주석 원문 `!     N    : IN  : 節点数` (5); 주석 원문 `!     X    : IN  : 節点座標` (6); 주석 원문 `!     XGi  : IN  : ξi` (7); `      IMPLICIT REAL*8(A-H,O-Z)` (9); `      DIMENSION P(3,N),X(3,N),XJI(3,3),DNDX(3,N)` (10). |
| 12–16 | 시작 시 1행 DERXPN2 루틴 안. DERPN2·JACOB3·AXB를 인용된 인수 순서로 호출한다. 해석: 이 호출 순서는 P의 형상함수 미분과 XJI의 행렬 곱으로 DNDX를 계산하는 절차에 해당한다. 루틴 끝을 포함한다. 원문: `      CALL DERPN2(P,N,XG1,XG2,XG3)` (12); `      CALL JACOB3(N,P,X,XJI,DET,ITO)` (13); `      CALL AXB(DNDX,XJI,P,3,3,N)` (14); `      END` (16). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10·12: 작업 배열 P의 두 번째 크기는 N이다. DERPN2에 전달하기 전 이 파일에서 N 값을 검사하지 않는다.
