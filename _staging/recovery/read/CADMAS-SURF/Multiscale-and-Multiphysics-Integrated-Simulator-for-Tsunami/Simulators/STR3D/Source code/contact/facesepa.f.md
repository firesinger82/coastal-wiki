---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/facesepa.f
lines: 16
sha256: 7b20400fe77e52000f7a6069641d1bec07145ed2ea403a6c07e7de25a8ddeb7b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# facesepa.f — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 루틴·암시적 자료형·배열을 선언한다(1–4). 두 SUBVEC와 CROSS2를 호출하여 E를 구한다(6–8). VECML1에 F와 E를 전달하여 FN을 구한다(9). 해석: E를 면 법선으로 보고 F를 힘으로 보면 FN은 법선 성분이다. FN이 -FTOL 이상이면 상태 3과 IFACE를 저장한다(10–13). RETURN·END로 끝낸다(15–16). 원문: `      SUBROUTINE FACESEPA(ISLV,F,FTOL,IFACE,IELC,POS)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION POS(3,*),E(3),IELC(3),V12(3),V13(3),F(3),ISLV(2)` (4); `      CALL SUBVEC(V12,POS(1,IELC(2)),POS(1,IELC(1)),3)` (6); `      CALL SUBVEC(V13,POS(1,IELC(3)),POS(1,IELC(1)),3)` (7); `      CALL CROSS2(V12,V13,E)` (8); `      CALL VECML1(FN,F,E,3)` (9); `      IF( FN .GE. -FTOL ) THEN` (10); `        ISLV(1)=3` (11); `        ISLV(2)=IFACE` (12). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10–13: FN < -FTOL이면 ISLV에 대입하는 실행문이 없다.
