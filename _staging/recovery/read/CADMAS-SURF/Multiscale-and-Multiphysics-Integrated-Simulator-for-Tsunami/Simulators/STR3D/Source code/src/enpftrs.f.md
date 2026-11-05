---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/enpftrs.f
lines: 43
sha256: 7f1d651d02fc548bf0ec9073a1e843d8099b1d96be0eb328764b65fb8be2d575
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# enpftrs.f — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | ENPFTRS는 GRID와 UG의 두 절점 성분 차이를 계산한다. EPS0에 EPS를 저장한다. VECML2를 호출하여 AXR0를 받는다. 해석: XR0는 초기 좌표 차이이고 UR은 상대 변위이다. 해석: EPS0는 이전 변형률이고 AXR0는 초기 길이이다. 원문: `      SUBROUTINE ENPFTRS(FC,EPS,S,GRID,UG,NP,A,GR,IGNL)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； `      DIMENSION XR0(3),XR(3),UR(3),GRID(3,*),UG(6,*),NP(2),ER(3),FC(3,2)` (4)； `      XR0(:) = GRID(:,NP(2)) - GRID(:,NP(1))` (6)； `      CALL VECML2(AXR0,XR0,3)` (8)； `      UR(:) = UG(1:3,NP(2)) - UG(1:3,NP(1))` (10)； `      EPS0 = EPS` (12)。 [11-04 전수 검증 정정] |
| 14–43 | 시작 시 1행 ENPFTRS 루틴 안이다. 해석: IGNL이 0이면 초기 축 방향의 상대 변위로 변형률을 구한다. 해석: ELSE에서는 현재 길이와 초기 길이의 비로 변형률을 구한다. 해석: 변형률 증분으로 응력을 갱신한다. `FT = S * A`를 계산한다. FC의 두 열에 `FT * ER(:)`를 반대 부호로 대입한다. 원문: `      IF( IGNL == 0 ) THEN` (14)； `        ER(:) = XR0(:) / AXR0` (16)； `        CALL VECML1(AUR,UR,ER,3)` (18)； `        EPS = AUR / AXR0` (20)； `      ELSE` (22)； `        XR(:) = XR0(:) + UR(:)` (24)； `        CALL VECML2(AXR,XR,3)` (26)； `        ER(:) = XR(:) / AXR` (28)； `        EPS = AXR / AXR0 - 1.D0` (30)； `      ENDIF` (32)； `      DEPS = EPS - EPS0` (34)； `      S = S + GR * DEPS` (36)； `      FT = S * A` (38)； `      FC(:,1) = -FT * ER(:)` (40)； `      FC(:,2) =  FT * ER(:)` (41)； `      END` (43)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16·20·28·30: AXR0 또는 AXR로 나누기 전에 해당 값이 0인지 검사하는 조건은 이 파일에 없다. [11-04 전수 검증 정정]
