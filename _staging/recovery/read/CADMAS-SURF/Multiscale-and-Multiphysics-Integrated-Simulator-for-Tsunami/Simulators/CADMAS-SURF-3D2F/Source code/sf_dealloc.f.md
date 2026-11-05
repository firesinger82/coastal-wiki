---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_dealloc.f
lines: 49
sha256: 2b34483afdccb5e27772bcb65c10e62ff1b0ab2e24e1ee97935ab3b14d4c70d2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_dealloc.f — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | SF_DEALLOC은 VF_A2ARRAY를 사용하고 두 INCLUDE를 포함한다(1–8). IERR=0으로 시작하여 아래에 인용한 배열들을 STAT=IERR로 해제한다(10–46). 해석: 배열 이름은 격자·공극률·경계조건 자료를 가리키는 것으로 보인다. LEQK가 0이 아니면 K·E 관련 배열을, LEQT가 0이 아니면 T 관련 배열을, LEQC가 양수이면 C 관련 배열을 추가 해제한다(24–45). 마지막 IERR가 0이 아니면 VF_A2ERR를 호출한다(47). 원문: `      SUBROUTINE SF_DEALLOC()` (1)<br>`      USE VF_A2ARRAY` (3)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (5)<br>`      INCLUDE 'VF_A0PRM.h'` (7)<br>`      INCLUDE 'VF_ANUMBI.h'` (8)<br>`      IERR = 0` (10)<br>`      DEALLOCATE(GGV_0,STAT=IERR)` (11)<br>`      DEALLOCATE(GGX_0,STAT=IERR)` (12)<br>`      DEALLOCATE(GGY_0,STAT=IERR)` (13)<br>`      DEALLOCATE(GGZ_0,STAT=IERR)` (14)<br>`      DEALLOCATE(INDX0,STAT=IERR)` (15)<br>`      DEALLOCATE(INDY0,STAT=IERR)` (16)<br>`      DEALLOCATE(INDZ0,STAT=IERR)` (17)<br>`      DEALLOCATE(BCU0,STAT=IERR)` (18)<br>`      DEALLOCATE(BCV0,STAT=IERR)` (19)<br>`      DEALLOCATE(BCW0,STAT=IERR)` (20)<br>`      DEALLOCATE(BCP0,STAT=IERR)` (21)<br>`      DEALLOCATE(BCF0,STAT=IERR)` (22)<br>`      DEALLOCATE(BCVI0,STAT=IERR)` (23)<br>`      IF (LEQK.NE.0) THEN` (24)<br>`        DEALLOCATE(BCK0,STAT=IERR)` (25)<br>`        DEALLOCATE(BCE0,STAT=IERR)` (26)<br>`      ENDIF` (27)<br>`      IF (LEQT.NE.0) THEN` (28)<br>`        DEALLOCATE(BCT0,STAT=IERR)` (29)<br>`        DEALLOCATE(BCTI0,STAT=IERR)` (30)<br>`      ENDIF` (31)<br>`      IF (LEQC.GT.0) THEN` (32)<br>`        DEALLOCATE(BCC0,STAT=IERR)` (33)<br>`        DEALLOCATE(BCCI0,STAT=IERR)` (34)<br>`      ENDIF` (35)<br>`      DEALLOCATE(INDB0,STAT=IERR)` (36)<br>`      IF (LEQK.NE.0) THEN` (37)<br>`        DEALLOCATE(INDBK0,STAT=IERR)` (38)<br>`        DEALLOCATE(INDBE0,STAT=IERR)` (39)<br>`      ENDIF` (40)<br>`      IF (LEQT.NE.0) THEN` (41)<br>`        DEALLOCATE(INDBT0,STAT=IERR)` (42)<br>`      ENDIF` (43)<br>`      IF (LEQC.GT.0) THEN` (44)<br>`        DEALLOCATE(INDBC0,STAT=IERR)` (45)<br>`      ENDIF` (46)<br>`      IF (IERR.NE.0) CALL VF_A2ERR('SF_DEALLOC','CAN NOT DEALLOC.')` (47)<br>`      END` (49) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–47: 각 DEALLOCATE는 같은 IERR에 상태를 기록한다. 오류 검사는 모든 해제문 뒤에 한 번만 있다.
