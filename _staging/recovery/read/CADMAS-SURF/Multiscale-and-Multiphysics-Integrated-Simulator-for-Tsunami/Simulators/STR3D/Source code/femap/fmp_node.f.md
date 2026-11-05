---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/femap/fmp_node.f
lines: 12
sha256: 125be1998f9a7001416fc50801e61173de74330bd1e3a97c0464f66607bb433e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fmp_node.f — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | FMP_NODE는 실수 IMPLICIT 선언과 배열 X(3)를 사용한다. 해석: X(3)는 절점 좌표로 보인다. ID·고정 필드·X(:)를 내부 문자열 CHAR에 쓴 뒤 WT_DATA를 호출한다. 7–8행 WRITE는 고정형식 연속문이다. 원문: `      SUBROUTINE FMP_NODE(ID,X,IFL)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      CHARACTER*200 CHAR` (4); `      DIMENSION X(3)` (5); `      WRITE(CHAR,'(I10,10I3,1P3E13.5,2I2)') ` (7); `     &  ID,0,0,1,46,0,0,0,0,0,0,X(:),0,0` (8); `      CALL WT_DATA(CHAR,IFL)` (10); `      END` (12) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
