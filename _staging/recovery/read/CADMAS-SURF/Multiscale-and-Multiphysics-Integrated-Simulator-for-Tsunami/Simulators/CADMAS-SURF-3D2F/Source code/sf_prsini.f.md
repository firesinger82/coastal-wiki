---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_prsini.f
lines: 40
sha256: 17fb38f0fb69a2cc723a9b720d7510208d21ee488793d253856800cc4d83eabc
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_prsini.f — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | SF_PRSINI의 선언부다. MYRANK가 0이 아니면 반환한다(15). data.prs를 열고 IOSTAT가 양수이면 VF_A2ERR를 호출한다(17–19). ITPFIL에 MFILTP를 저장한다(20). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_PRSINI(IPFACE0,AFC,IPGRID0,IPND0,ZZ)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      INCLUDE 'VF_A0PRM.h'` (5); `      INCLUDE 'VF_AFILEI.h'` (6); `      INCLUDE 'VF_ANUMBI.h'` (7); `      INCLUDE 'VF_APARAI.h'` (8); `      INCLUDE 'VF_APHYSR.h'` (9); `      INCLUDE 'SF_STRUCT.h'` (10); `      DIMENSION IPFACE0(12,NPFC0),IPGRID0(2,NNOD0),IPND0(NNOD0)` (12); `     &         ,AFC(NPFC0),ZZ(MAXG1,NUMK)` (13); `      IF( MYRANK /= 0 ) RETURN` (15); `      OPEN(MFILTP,FILE='data.prs',IOSTAT=IERR)` (17); `      IF( IERR > 0 )` (18); `     &    CALL VF_A2ERR('SF_PRSINI','CAN NOT OPEN (data.prs).')` (19); `      ITPFIL = MFILTP` (20). |
| 22–40 | 시작 시 1행 SF_PRSINI 루틴 안. SF_PRSINI 안이며 루트(root) 프로세스다. WVLVL·ZZ(1,NUMK)·NPFC0·각 IPFACE0(:,I)의 3:12 성분·AFC를 이 순서로 정해진 서식에 맞춰 쓴다(22–32). SF_GIPND 호출 후 NNOD0개 IPND0를 I1 서식으로 쓴다(34–38). 원문(연속 표시는 앞 문장에 이어짐): `      WRITE(ITPFIL,'(1P2E15.7)') WVLVL,ZZ(1,NUMK)` (22); `      WRITE(ITPFIL,'(I10)') NPFC0` (24); `      DO I = 1, NPFC0` (26); `        WRITE(ITPFIL,'(10I10)') IPFACE0(3:12,I)` (27); `      ENDDO` (28); `      DO I = 1, NPFC0` (30); `        WRITE(ITPFIL,'(1PE15.7)') AFC(I)` (31); `      ENDDO` (32); `      CALL SF_GIPND(IPND0,IPGRID0,NNOD0)` (34); `      DO I = 1, NNOD0` (36); `        WRITE(ITPFIL,'(I1)') IPND0(I)` (37); `      ENDDO` (38); `      END` (40). 해석: WVLVL은 수위로 읽힌다. 해석: ZZ(1,NUMK)는 상단 Z 좌표로 읽힌다. [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 17·40: 출력 파일명은 data.prs로 고정되어 있다. 이 루틴에는 CLOSE 호출이 없다.
