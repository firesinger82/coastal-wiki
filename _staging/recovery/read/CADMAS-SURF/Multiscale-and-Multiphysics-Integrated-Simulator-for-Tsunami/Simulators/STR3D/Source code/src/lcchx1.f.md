---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/lcchx1.f
lines: 53
sha256: de72b059186e96b98cda5ec109090418f86c86770f04f47989003ba43fdc469d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# lcchx1.f — 판독 구간 기록

구간은 1행부터 53행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | LCCHX1의 전역·국소 좌표 변환 설명과 배열 선언이다. 절점 묶음 (1,4,5,8)·(2,3,6,7)·(1,2,5,6)·(4,3,8,7)의 좌표 평균을 각각 CENTER1..4에 저장한다. SUBVEC·DIRCOS·CROSS2를 호출한다. 해석: 네 면의 절점 평균으로 두 방향 벡터를 만들고 E의 세 축을 구성한다. 원문: `      SUBROUTINE LCCHX1(TE,GE,UE,GRID,UG,KN)` (1)； `C     TE   : OUT : global -> local 座標変換行列` (3) (전역 좌표(global coordinates)에서 국소 좌표(local coordinates)로의 좌표 변환행렬 출력이다.)； `C     GE   : OUT : 構成節点座標(local)` (4) (구성 절점의 국소 좌표 출력이다.)； `C     UE   : OUT : 構成節点変位(local)` (5) (구성 절점의 국소 변위 출력이다.)； `C     GRID : IN  : 節点座標(global)` (6) (전역 절점 좌표 입력이다.)； `C     UG   : IN  : 節点変位(global)` (7) (전역 절점 변위 입력이다.)； `C     KN   : IN  : 構成節点番号` (8) (구성 절점 번호 입력이다.)； `      IMPLICIT REAL*8(A-H,O-Z)` (10)； 연속문(11–13): `      DIMENSION GG(3,20),GRID(3,*),E(3,3),TE(3,3),GE(3,8),KN(8)` (11)； `     &         ,V12(3),V34(3),CENTER(3),CENTER1(3),CENTER2(3)` (12)； `     &         ,CENTER3(3),CENTER4(3),UG(6,*),UE(3,8)` (13)； `      DO 500 I=1,3` (15)； 연속문(16–17): `        CENTER1(I) = ( GRID(I,KN(1)) + GRID(I,KN(4)) + GRID(I,KN(5))` (16)； `     &               + GRID(I,KN(8)) ) * 0.25D0` (17)； 연속문(18–19): `        CENTER2(I) = ( GRID(I,KN(2)) + GRID(I,KN(3)) + GRID(I,KN(6))` (18)； `     &               + GRID(I,KN(7)) ) * 0.25D0` (19)； 연속문(20–21): `        CENTER3(I) = ( GRID(I,KN(1)) + GRID(I,KN(2)) + GRID(I,KN(5))` (20)； `     &               + GRID(I,KN(6)) ) * 0.25D0` (21)； 연속문(22–23): `        CENTER4(I) = ( GRID(I,KN(4)) + GRID(I,KN(3)) + GRID(I,KN(8))` (22)； `     &               + GRID(I,KN(7)) ) * 0.25D0` (23)； `  500 CONTINUE` (24)； `      CALL SUBVEC(V12,CENTER2,CENTER1,3)` (26)； `      CALL SUBVEC(V34,CENTER4,CENTER3,3)` (27)； `      CALL DIRCOS(E(1,1),V12,3)` (28)； `      CALL CROSS2(E(1,1),V34,E(1,3))` (29)； `      CALL CROSS2(E(1,3),E(1,1),E(1,2))` (30)。 [11-04 전수 검증 정정] |
| 32–53 | 시작 시 1행 LCCHX1 루틴 안이다. E의 전치(transpose)를 TE에 저장한다. CENTER1·CENTER2의 중점을 원점으로 삼아 여덟 절점의 상대 좌표를 계산한다. AXB로 좌표 GE와 각 절점의 앞 세 변위 UE를 변환한다. 원문: `      DO 100 I=1,3` (32)； `        DO 110 J=1,3` (33)； `          TE(I,J)=E(J,I)` (34)； `  110   CONTINUE` (35)； `  100 CONTINUE` (36)； `      DO 400 I=1,3` (38)； `        CENTER(I) = ( CENTER1(I) + CENTER2(I) ) * 0.5D0` (39)； `  400 CONTINUE` (40)； `      DO 200 I=1,8` (42)； `        CALL SUBVEC(GG(1,I),GRID(1,KN(I)),CENTER,3)` (43)； `  200 CONTINUE` (44)； `      CALL AXB(GE,TE,GG,3,3,8)` (46)； `      DO 300 I=1,8` (48)； `        CALL AXB(UE(1,I),TE,UG(1,KN(I)),3,3,1)` (49)； `  300 CONTINUE` (50)； `      RETURN` (52)； `      END` (53)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11·42–49: GG의 두 번째 첨자 크기는 20이지만 이 루틴에서 채우고 변환하는 절점 범위는 1..8이다.
