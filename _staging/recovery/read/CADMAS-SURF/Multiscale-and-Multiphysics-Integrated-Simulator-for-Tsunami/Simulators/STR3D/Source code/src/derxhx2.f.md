---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/derxhx2.f
lines: 16
sha256: 05c30f7b5fc21c3454fc2459fa1df84f0b24f183ab55d22997f347bef739b92d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# derxhx2.f — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | DERXHX2의 입출력과 배열을 선언한다. `節点座標`는 절점좌표(nodal coordinate), `節点数`는 절점 수(number of nodes)다. DNDX는 공간 미분, DET는 야코비안(Jacobian) 행렬식이다. 원문: `      SUBROUTINE DERXHX2(DNDX,DET,XG1,XG2,XG3,X,N,ITO)` (1); 주석 원문 `!     DNDX : OUT : DNDX(i,j) = ∂Nj/∂xi` (3); 주석 원문 `!     DET  : OUT : \|J\| ( Jij = ∂xj/∂ξi )` (4); 주석 원문 `!     XGi  : IN  : ξi` (5); 주석 원문 `!     X    : IN  : 節点座標` (6); 주석 원문 `!     N    : IN  : 節点数` (7); `      IMPLICIT REAL*8(A-H,O-Z)` (9); `      DIMENSION DNDX(3,N),X(3,N),P(3,N),XJI(3,3)` (10). |
| 12–16 | 시작 시 1행 DERXHX2 루틴 안. DERHX2에 좌표와 N을 전달한다. 이어 JACOB3와 AXB를 인용된 인수 순서로 호출한다. 해석: 이 호출 순서는 P의 형상함수 미분을 공간 미분 DNDX로 변환하는 절차에 해당한다. 루틴 끝을 포함한다. 원문: `      CALL DERHX2(XG1,XG2,XG3,N,P)` (12); `      CALL JACOB3(N,P,X,XJI,DET,ITO)` (13); `      CALL AXB(DNDX,XJI,P,3,3,N)` (14); `      END` (16). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10·12: 작업 배열 P의 두 번째 크기는 N이다. DERHX2에 전달하기 전 이 파일에서 N 값을 검사하지 않는다.
