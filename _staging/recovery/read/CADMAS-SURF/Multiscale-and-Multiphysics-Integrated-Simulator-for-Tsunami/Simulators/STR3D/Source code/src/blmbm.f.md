---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/blmbm.f
lines: 32
sha256: 986c6ba92c9f05ff026abc4be2729361bc17ff59ef286b6ebaf175d8217c6dd9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# blmbm.f — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | BLMBM의 암시적 형과 B·BX·BY·BZ·UX·UY·UZ·WK1·WK2 배열 선언. BX·BY·BZ의 선형 항으로 B의 세 행을 구성한다. IGNL=0이면 반환한다. 원문: `      SUBROUTINE BLMBM(B,BX,BY,BZ,UX,UY,UZ,IGNL)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); 연속문(4–5): `      DIMENSION B(3,12),BX(3,12),BY(3,12),BZ(3,12),UX(3),UY(3),UZ(3)` <br> `     &         ,WK1(12),WK2(12)`; `      B(1,:) = BX(1,:)` (8); `      B(2,:) = BY(1,:) + BX(2,:)` (10); `      B(3,:) = BZ(1,:) + BX(3,:)` (12); `      IF( IGNL == 0 ) RETURN` (14). [11-04 전수 검증 정정] |
| 16–32 | BLMBM 루틴 안이며 `IF( IGNL == 0 ) RETURN` (14)을 실행하지 않은 IGNL /= 0 경로. AXB 호출로 UX·UY·UZ와 BX·BY·BZ의 곱을 얻는다. 첫 행에는 한 곱, 둘째·셋째 행에는 두 곱을 더한다. 30행 END 뒤의 빈 행까지 포함한다. 원문: `      CALL AXB(WK1,UX,BX,1,3,12)` (16); `      B(1,:) = B(1,:) + WK1(:)` (18); `      CALL AXB(WK1,UX,BY,1,3,12)` (20); `      CALL AXB(WK2,UY,BX,1,3,12)` (21); `      B(2,:) = B(2,:) + WK1(:) + WK2(:)` (23); `      CALL AXB(WK1,UX,BZ,1,3,12)` (25); `      CALL AXB(WK2,UZ,BX,1,3,12)` (26); `      B(3,:) = B(3,:) + WK1(:) + WK2(:)` (28); `      END` (30). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
