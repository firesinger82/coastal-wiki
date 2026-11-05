---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/strpn1.f
lines: 18
sha256: 103d6fa23d611c02243cb74f8d73beb944b38d4852ec8cc3bcd1230a2180537e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# strpn1.f — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | STRPN1 입구와 IMPLICIT·배열 선언이다(1–6). TRNSMTX7·CHTNSR를 차례로 호출한다(8–10). INTPLPN1을 EPS·EPSG와 SIG·SIGG에 각각 호출한다(12–13). 이어서 ATXB를 EPS0와 SIG0에 대해 호출한다(15–16). 해석: 이 호출 순서를 변형률·응력의 보간과 좌표·텐서 변환으로 볼 수 있다. 원문: `      SUBROUTINE STRPN1(EPS0,SIG0,EPSG,SIGG,GRID,KN)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION TE(3,3),TE1(6,6),TE2(6,6),X(3,6),GRID(3,*),KN(6)`<br>`     &         ,EPS(6,6),SIG(6,6),EPSG(6,3,2),SIGG(6,3,2),EPS0(6,6)`<br>`     &         ,SIG0(6,6)` (4–6); `      CALL TRNSMTX7(TE,X,GRID,KN)` (8); `      CALL CHTNSR(TE,TE1,TE2)` (10); `      CALL INTPLPN1(EPS,EPSG)` (12); `      CALL INTPLPN1(SIG,SIGG)` (13); `      CALL ATXB(EPS0,TE1,EPS,6,6,6)` (15); `      CALL ATXB(SIG0,TE2,SIG,6,6,6)` (16); `      END` (18) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
