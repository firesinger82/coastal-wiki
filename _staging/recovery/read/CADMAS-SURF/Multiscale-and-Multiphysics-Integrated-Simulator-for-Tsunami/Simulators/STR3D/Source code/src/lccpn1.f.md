---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/lccpn1.f
lines: 39
sha256: 6ebc15cb798491cc1663333690fe9a486896af455b0274474aa5470f2240e973
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# lccpn1.f — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | LCCPN1의 일본어 인수 설명과 배열 선언이다. KN(1)·KN(4), KN(2)·KN(5), KN(3)·KN(6) 절점 쌍의 중점을 X의 각 열로 계산한다. 해석: 각 쌍은 두 삼각형 면의 대응 절점이다. 두 변 벡터와 DIRCOS·CROSS2 호출로 국소 축 E를 구성한다. 원문: `      SUBROUTINE LCCPN1(TE,GE,UE,GRID,UG,KN)` (1)； `C     TE   : OUT : global -> local 座標変換行列` (3) (전역 좌표(global coordinates)에서 국소 좌표(local coordinates)로의 좌표 변환행렬 출력이다.)； `C     GE   : OUT : 構成節点座標(local)` (4) (구성 절점의 국소 좌표 출력이다.)； `C     UE   : OUT : 構成節点変位(local)` (5) (구성 절점의 국소 변위 출력이다.)； `C     GRID : IN  : 節点座標(global)` (6) (전역 절점 좌표 입력이다.)； `C     UG   : IN  : 節点変位(global)` (7) (전역 절점 변위 입력이다.)； `C     KN   : IN  : 構成節点番号` (8) (구성 절점 번호 입력이다.)； `      IMPLICIT REAL*8(A-H,O-Z)` (10)； 연속문(11–12): `      DIMENSION X(3,3),GRID(3,*),KN(6),V12(3),V13(3),E(3,3),TE(3,3)` (11)； `     &          ,GG(3,6),GE(3,6),UG(6,*),UE(3,6)` (12)； `      X(:,:) = ( GRID(:,KN(1:3)) + GRID(:,KN(4:6)) ) * .5D0` (14)； `      V12(:) = X(:,2) - X(:,1)` (16)； `      V13(:) = X(:,3) - X(:,1)` (17)； `      CALL DIRCOS(E(1,1),V12,3)` (19)； `      CALL CROSS2(E(1,1),V13,E(1,3))` (20)； `      CALL CROSS2(E(1,3),E(1,1),E(1,2))` (21)。 [11-04 전수 검증 정정] |
| 23–39 | 시작 시 1행 LCCPN1 루틴 안이다. E의 전치(transpose)를 TE로 저장한다. X(:,1)을 원점으로 각 절점의 상대 좌표 GG를 계산한다. AXB로 여섯 절점의 좌표 GE와 앞 세 변위 UE를 국소 좌표로 변환한다. 원문: `      DO I=1,3` (23)； `        DO J=1,3` (24)； `          TE(I,J)=E(J,I)` (25)； `        ENDDO` (26)； `      ENDDO` (27)； `      DO I=1,6` (29)； `        GG(:,I) = GRID(:,KN(I)) - X(:,1)` (30)； `      ENDDO` (31)； `      CALL AXB(GE,TE,GG,3,3,6)` (33)； `      DO I = 1, 6` (35)； `        CALL AXB(UE(1,I),TE,UG(1,KN(I)),3,3,1)` (36)； `      ENDDO` (37)； `      END` (39)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
