---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_rface0.f
lines: 62
sha256: a4e564f3e90538cc8bc0b7cffe5f3165273e1f2daee11c9394fbea5bc3cbcab9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_rface0.f — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | SF_RFACE0의 선언부다. MYRANK>0이면 반환한다(13). CR1은 85.D0/180.D0*PI의 사인에 음수를 붙인 값이다(15). CR2는 15.D0/180.D0*PI의 사인이다(16). IELM(3,IE)=2인 면에 SF_NRMVEC를 호출한다(22–25). E(3)<CR1이면 IRFACE=1, E(3)>CR2이면 2로 분류한다(26–30). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_RFACE0()` (1); `      USE SF_ARRAY` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'VF_A0PRM.h'` (7); `      INCLUDE 'VF_APARAI.h'` (8); `      INCLUDE 'SF_STRUCT.h'` (9); `      DIMENSION E(3)` (11); `      IF( MYRANK > 0 ) RETURN` (13); `      CR1 = -DSIN( 85.D0 / 180.D0 * PI )` (15); `      CR2 =  DSIN( 15.D0 / 180.D0 * PI )` (16); `      ALLOCATE( IRFACE(NPFC0) )` (18); `      IRFACE(:) = 0` (20); `      DO I = 1, NPFC0` (22); `        IE = IPFACE0(3,I)` (23); `        IF( IELM(3,IE) == 2 ) THEN` (24); `          CALL SF_NRMVEC(E,IPFACE0(5,I),IPFACE0(4,I),GRID)` (25); `          IF( E(3) < CR1 ) THEN` (26); `            IRFACE(I) = 1` (27); `          ELSEIF( E(3) > CR2 ) THEN` (28); `            IRFACE(I) = 2` (29); `          ENDIF` (30); `        ENDIF` (31); `      ENDDO` (32). 26–30행의 IF/ELSEIF에는 ELSE가 없다. 두 조건이 모두 거짓이면 IRFACE(I)는 20행의 초기값 0을 유지한다. [11-04 전수 검증 정정] |
| 34–62 | 시작 시 1행 SF_RFACE0 루틴 안. SF_RFACE0 안이며 앞 면 루프 밖. IRGRID0를 0으로 초기화한 후 IELM(3,I)=2 요소의 절점을 -1로 표시한다(34–43). IRFACE=2인 면의 절점을 1로 바꾸고 그 후 IRFACE=1인 면의 절점을 0으로 바꾼다(45–57). DELZ0·IFIX0를 할당한다(59–60). 원문(연속 표시는 앞 문장에 이어짐): `      ALLOCATE( IRGRID0(NNOD0) )` (34); `      IRGRID0(:) = 0` (36); `      DO I = 1, NELM` (38); `        IF( IELM(3,I) == 2 ) THEN` (39); `          N = IELM(4,I)` (40); `          IRGRID0( IELM(5:4+N,I) ) = -1` (41); `        ENDIF` (42); `      ENDDO` (43); `      DO I = 1, NPFC0` (45); `        IF( IRFACE(I) == 2 ) THEN` (46); `          N = IPFACE0(4,I)` (47); `          IRGRID0( IPFACE0(5:4+N,I) ) = 1` (48); `        ENDIF` (49); `      ENDDO` (50); `      DO I = 1, NPFC0` (52); `        IF( IRFACE(I) == 1 ) THEN` (53); `          N = IPFACE0(4,I)` (54); `          IRGRID0( IPFACE0(5:4+N,I) ) = 0` (55); `        ENDIF` (56); `      ENDDO` (57); `      ALLOCATE( DELZ0(NNOD0) )` (59); `      ALLOCATE( IFIX0(NNOD0) )` (60); `      END` (62). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–16: 면 분류의 각도 계수는 85도·15도로 고정되어 있다.
- 45–57: IRFACE=2 절점 표시 뒤 IRFACE=1 절점을 0으로 덮어쓴다. 두 종류 면에 속하는 절점의 최종 값은 0이다.
- 59–60: DELZ0·IFIX0는 할당만 하며 이 루틴에는 값 초기화가 없다.
