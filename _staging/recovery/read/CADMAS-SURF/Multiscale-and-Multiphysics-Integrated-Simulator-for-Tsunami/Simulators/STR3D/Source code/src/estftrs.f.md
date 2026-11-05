---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/estftrs.f
lines: 56
sha256: a46c11a076bd3032c4e87f74f23e5e0d48fbfe56d6a566016680cb078c356077
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# estftrs.f — 판독 구간 기록

구간은 1행부터 56행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | ESTFTRS 선언과 DATA 단위행렬을 준비한다. IGNL == 0이면 ER에 `XR0(:) / AXR0`를 대입한다. ELSE에서는 ER에 `XR(:) / AXR`를 대입한다. 해석: 전자는 초기 축 방향이고 후자는 상대 변위를 반영한 현재 축 방향이다. 원문: `      SUBROUTINE ESTFTRS(ESTF,GRID,UG,NP,A,GR,S,IGNL)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； 연속문(4–5): `      DIMENSION GRID(3,*),UG(6,*),NP(2),XR0(3),XR(3),UR(3),ER(3),E(3,3)` (4)； `     &         ,RK(3,3),ESTF(21)` (5)； 연속문(7–9): `      DATA E / 1.D0, 0.D0, 0.D0,` (7)； `     &         0.D0, 1.D0, 0.D0,` (8)； `     &         0.D0, 0.D0, 1.D0 /` (9)； `      XR0(:) = GRID(:,NP(2)) - GRID(:,NP(1))` (11)； `      CALL VECML2(AXR0,XR0,3)` (13)； `      IF( IGNL == 0 ) THEN` (15)； `        ER(:) = XR0(:) / AXR0` (17)； `      ELSE` (19)； `        UR(:) = UG(1:3,NP(2)) - UG(1:3,NP(1))` (21)； `        XR(:) = XR0(:) + UR(:)` (23)； `        CALL VECML2(AXR,XR,3)` (25)； `        ER(:) = XR(:) / AXR` (27)； `      ENDIF` (29)。 [11-04 전수 검증 정정] |
| 31–56 | 시작 시 1행 ESTFTRS 루틴 안이다. 3×3 RK를 계산한다. IGNL > 0이면 S를 포함한 항을 더한다. 해석: S를 포함한 항은 응력에 의한 항이다. I=1..6과 J=I..6 순서로 ESTF의 21개 성분을 저장한다. I와 J가 모두 3 이하이면 RK(I,J)를 저장한다. I만 3 이하이면 -RK(I,J-3)를 저장한다. I가 3보다 크면 RK(I-3,J-3)를 저장한다. 해석: 이는 6×6 대칭행렬의 상삼각 저장이다. 원문: `      DO I = 1, 3` (31)； `        DO J = 1, 3` (32)； `          RK(I,J) = GR * A / AXR0 * ER(I) * ER(J)` (33)； 연속문(34–35): `          IF( IGNL > 0 )` (34)； `     &      RK(I,J) = RK(I,J) + S * A / AXR * ( E(I,J) - ER(I) * ER(J) )` (35)； `        ENDDO` (36)； `      ENDDO` (37)； `      IP = 0` (39)； `      DO I = 1, 6` (41)； `        DO J = I, 6` (42)； `          IP = IP + 1` (43)； `          IF( I <= 3 ) THEN` (44)； `            IF( J <= 3 ) THEN` (45)； `              ESTF(IP) = RK(I,J)` (46)； `            ELSE` (47)； `              ESTF(IP) = -RK(I,J-3)` (48)； `            ENDIF` (49)； `          ELSE` (50)； `            ESTF(IP) = RK(I-3,J-3)` (51)； `          ENDIF` (52)； `        ENDDO` (53)； `      ENDDO` (54)； `      END` (56)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 17·27·33–35: AXR0 또는 AXR로 나누기 전에 해당 값이 0인지 검사하는 조건은 이 파일에 없다. [11-04 전수 검증 정정]
- 15–35: IGNL이 0이 아니면 `ER(:) = XR(:) / AXR`를 계산한다. S를 포함한 항을 더하는 조건은 `IGNL > 0`이다. [11-04 전수 검증 정정]
