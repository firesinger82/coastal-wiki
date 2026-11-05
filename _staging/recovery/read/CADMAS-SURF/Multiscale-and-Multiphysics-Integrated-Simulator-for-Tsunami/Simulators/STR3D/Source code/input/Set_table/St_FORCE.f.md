---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Set_table/St_FORCE.f
lines: 27
sha256: 43c3a273ba9df88ad1e4bfe5a7f88c1a10c9bac1473afa3c627190ea6dc8fa12
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# St_FORCE.f — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | ST_FORCE는 J_FRC(1,J)와 IFC(1,I)가 같은 항목을 모은다. 암시적 배정밀도 선언과 IFC·NFC·FC·J_FRC·R_FRC의 크기를 명시한다(4–6). 세트 식별자가 일치하면 IP를 증가시키고 J_FRC의 2·3 성분과 R_FRC의 6성분을 복사한다(10–20). IFC의 두 번째 성분은 누적 끝 위치다(19). 각 NFC(1,I)를 INDGR로 변환한다(22–25). NFC(2,I)가 양수일 때만 ICRDR로 변환한다(24). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE ST_FORCE( IFC, NFC, FC, NIFC, NNFC, J_FRC, R_FRC,` (1) <br> `     &                     N_FRC, ICRDR, INDGR )` (2) <br> `      IMPLICIT REAL*8 (A-H,O-Z)` (4) <br> `      DIMENSION IFC(2,NIFC), NFC(2,NNFC), FC(6,NNFC), J_FRC(3,N_FRC),` (5) <br> `     &          R_FRC(6,N_FRC), INDGR(*), ICRDR(*)` (6) <br> `      IP = 0` (8) <br> `      DO I = 1, NIFC` (10) <br> `        DO J = 1, N_FRC` (11) <br> `          IF( J_FRC(1,J) == IFC(1,I) ) THEN` (12) <br> `            IP = IP + 1` (13) <br> `            NFC(1,IP) = J_FRC(2,J)` (14) <br> `            NFC(2,IP) = J_FRC(3,J)` (15) <br> `            FC(:,IP) = R_FRC(:,J)` (16) <br> `          ENDIF` (17) <br> `        ENDDO` (18) <br> `        IFC(2,I) = IP` (19) <br> `      ENDDO` (20) <br> `      DO I = 1, NNFC` (22) <br> `        NFC(1,I) = INDGR( NFC(1,I) )` (23) <br> `        IF( NFC(2,I) > 0 ) NFC(2,I) = ICRDR( NFC(2,I) )` (24) <br> `      ENDDO` (25) <br> `      END` (27) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
