---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_alloc0.f
lines: 88
sha256: 7f93a2bff4cde1abb0d86e933675b32eccca72f629e7907b40dec3d949c2e8a2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_alloc0.f — 판독 구간 기록

구간은 1행부터 88행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | VF_A2ARRAY와 포함 헤더·암시적 자료형을 사용한다. GGV_0·GGX_0·GGY_0·GGZ_0·INDX0·INDY0·INDZ0를 NUMI·NUMJ·NUMK 크기로 할당한다. 각 원본 배열을 해당 배열로 복사한다. 할당 묶음 뒤 IERR가 비영이면 VF_A2ERR를 호출한다. 원문: `      SUBROUTINE SF_ALLOC0()` (1); `      USE VF_A2ARRAY` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'VF_A0PRM.h'` (7); `      INCLUDE 'VF_ANUMBI.h'` (8); `      IERR = 0` (10); `      ALLOCATE(GGV_0(NUMI,NUMJ,NUMK),STAT=IERR)` (11); `      ALLOCATE(GGX_0(NUMI,NUMJ,NUMK),STAT=IERR)` (12); `      ALLOCATE(GGY_0(NUMI,NUMJ,NUMK),STAT=IERR)` (13); `      ALLOCATE(GGZ_0(NUMI,NUMJ,NUMK),STAT=IERR)` (14); `      ALLOCATE(INDX0(NUMI,NUMJ,NUMK),STAT=IERR)` (15); `      ALLOCATE(INDY0(NUMI,NUMJ,NUMK),STAT=IERR)` (16); `      ALLOCATE(INDZ0(NUMI,NUMJ,NUMK),STAT=IERR)` (17); `      IF (IERR.NE.0) CALL VF_A2ERR('SF_ALLOC0','CAN NOT ALLOC.')` (18); `      GGV_0 = GGV` (19); `      GGX_0 = GGX` (20); `      GGY_0 = GGY` (21); `      GGZ_0 = GGZ` (22); `      INDX0 = INDX` (23); `      INDY0 = INDY` (24); `      INDZ0 = INDZ` (25) [11-04 전수 검증 정정] |
| 27–57 | 시작 시 1행 SF_ALLOC0 루틴 안이다. BCU0부터 INDBC0까지 아래 배열을 할당한다. 선택 배열은 `IF (LEQK.NE.0) THEN` (34·47), `IF (LEQT.NE.0) THEN` (38·51), `IF (LEQC.GT.0) THEN` (42·54) 조건에서만 할당한다. 해석: BC*0와 INDB*0는 경계값과 경계 인덱스의 보존 배열로 보인다. 배열 차원과 오류 처리 조건을 인용한다. 원문: `      IERR = 0` (27); `      ALLOCATE(BCU0  (NUMB,3    ),STAT=IERR)` (28); `      ALLOCATE(BCV0  (NUMB,3    ),STAT=IERR)` (29); `      ALLOCATE(BCW0  (NUMB,3    ),STAT=IERR)` (30); `      ALLOCATE(BCP0  (NUMB,3    ),STAT=IERR)` (31); `      ALLOCATE(BCF0  (NUMB      ),STAT=IERR)` (32); `      ALLOCATE(BCVI0 (NUMB      ),STAT=IERR)` (33); `      IF (LEQK.NE.0) THEN` (34); `        ALLOCATE(BCK0 (  NUMB,3 ),STAT=IERR)` (35); `        ALLOCATE(BCE0 (  NUMB,3 ),STAT=IERR)` (36); `      ENDIF` (37); `      IF (LEQT.NE.0) THEN` (38); `        ALLOCATE(BCT0 (  NUMB   ),STAT=IERR)` (39); `        ALLOCATE(BCTI0(2,NUMB   ),STAT=IERR)` (40); `      ENDIF` (41); `      IF (LEQC.GT.0) THEN` (42); `        ALLOCATE(BCC0 (  NUMB,LEQC),STAT=IERR)` (43); `        ALLOCATE(BCCI0(2,NUMB,LEQC),STAT=IERR)` (44); `      ENDIF` (45); `      ALLOCATE(INDB0(MAXB1,NUMB),STAT=IERR)` (46); `      IF (LEQK.NE.0) THEN` (47); `        ALLOCATE(INDBK0(MAXBK1,NUMB),STAT=IERR)` (48); `        ALLOCATE(INDBE0(MAXBE1,NUMB),STAT=IERR)` (49); `      ENDIF` (50); `      IF (LEQT.NE.0) THEN` (51); `        ALLOCATE(INDBT0(NUMB     ),STAT=IERR)` (52); `      ENDIF` (53); `      IF (LEQC.GT.0) THEN` (54); `        ALLOCATE(INDBC0(NUMB,LEQC),STAT=IERR)` (55); `      ENDIF` (56); `      IF (IERR.NE.0) CALL VF_A2ERR('SF_ALLOC0','CAN NOT ALLOC.')` (57) [11-04 전수 검증 정정] |
| 58–88 | 시작 시 1행 SF_ALLOC0 루틴 안이다. BCU부터 INDBC까지 아래 원본 배열을 대응하는 이름 끝이 0인 배열로 복사한다. 선택 방정식 배열은 할당 때와 같은 조건으로 복사한다. 모든 조건 종료 뒤 루틴을 끝낸다. 원문: `      BCU0 = BCU` (58); `      BCV0 = BCV` (59); `      BCW0 = BCW` (60); `      BCP0 = BCP` (61); `      BCF0 = BCF` (62); `      BCVI0= BCVI` (63); `      IF (LEQK.NE.0) THEN` (64); `        BCK0 = BCK` (65); `        BCE0 = BCE` (66); `      ENDIF` (67); `      IF (LEQT.NE.0) THEN` (68); `        BCT0 = BCT` (69); `        BCTI0= BCTI` (70); `      ENDIF` (71); `      IF (LEQC.GT.0) THEN` (72); `        BCC0 = BCC` (73); `        BCCI0= BCCI` (74); `      ENDIF` (75); `      INDB0 = INDB` (76); `      IF (LEQK.NE.0) THEN` (77); `        INDBK0 = INDBK` (78); `        INDBE0 = INDBE` (79); `      ENDIF` (80); `      IF (LEQT.NE.0) THEN` (81); `        INDBT0 = INDBT` (82); `      ENDIF` (83); `      IF (LEQC.GT.0) THEN` (84); `        INDBC0 = INDBC` (85); `      ENDIF` (86); `      END` (88) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–18·28–57: 연속된 ALLOCATE들이 같은 STAT=IERR를 사용한다. 각 묶음의 마지막에서만 IERR를 검사한다.
