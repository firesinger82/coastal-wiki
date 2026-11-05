---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/gsurf.f
lines: 25
sha256: 66d61b049592d2ef1de9442090d05c671aeb2f1134d585d266ef1988e4075943
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gsurf.f — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | 루틴·암시적 자료형·배열을 선언하고 출력 위치 IP를 1로 초기화한다(1–6). 요소 1..NELM을 순회하면서 IBEL=0은 건너뛴다(8–10). 요소 절점 수 NNP가 6이면 GSFPN을 호출하고 IP를 3 늘리며, 8이면 GSFHX를 호출하고 IP를 6 늘린다(12–21). 루프·루틴을 끝낸다(23–25). 원문: `      SUBROUTINE GSURF(XG,XX,IELM,NM,NELM,IBEL,NDIM)` (1); `      IMPLICIT REAL*8(A-H,O-Z)      ` (3); `      DIMENSION XG(NDIM,*),XX(NDIM,*),IELM(NM,NELM),IBEL(NELM)` (4); `      IP = 1` (6); `      DO I = 1, NELM` (8); `        IF( IBEL(I) == 0 ) CYCLE` (10); `        NNP = IELM(3,I)` (12); `        SELECT CASE( NNP )` (14); `        CASE( 6 )` (15); `          CALL GSFPN(XG(1,IP),XX,IELM(8,I),NDIM)` (16); `          IP = IP + 3` (17); `        CASE( 8 )` (18); `          CALL GSFHX(XG(1,IP),XX,IELM(8,I),NDIM)` (19); `          IP = IP + 6` (20). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–21: 절점 수 선택에는 6·8만 있고 CASE DEFAULT는 없다.
