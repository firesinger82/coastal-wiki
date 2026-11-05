---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/lencd.f
lines: 17
sha256: f351f7ad4aa3aa9231ae9ecc1446e8e92f057e4a00c7e7c59397df89d792a8b7
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# lencd.f — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 루틴·암시적 자료형·배열을 선언한다(1–4). SUBVEC로 첫 점에서 두 번째·세 번째 점으로의 벡터를 구한다(6–7). VECML1 두 호출의 내적 A·B에서 투영 비율(projection ratio) RT=A/B를 계산한다(9–11). RMULT1로 선 위 투영 벡터를 만들고 SUBVEC로 세 번째 점에서 투영점으로 향하는 V34를 구한다(13–14). RETURN·END로 끝낸다(16–17). 원문: `      SUBROUTINE LENCD(RT,V34,XYZ)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION V12(3),V13(3),V14(3),V34(3),XYZ(3,3)` (4); `      CALL SUBVEC(V12,XYZ(1,2),XYZ(1,1),3)` (6); `      CALL SUBVEC(V13,XYZ(1,3),XYZ(1,1),3)` (7); `      CALL VECML1(A,V13,V12,3)` (9); `      CALL VECML1(B,V12,V12,3)` (10); `      RT=A/B` (11); `      CALL RMULT1(V14,V12,RT,3)` (13); `      CALL SUBVEC(V34,V14,V13,3)` (14). 호출 의미의 근거는 같은 STR3D 원문 트리의 `util/subvec.f:9–11`(벡터 차), `util/vecml1.f:19–22`(내적), `util/rmult1.f:16–18`(스칼라 곱)이다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10–11: B를 분모로 쓰기 전에 B의 0 여부를 검사하지 않는다.
