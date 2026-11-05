---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_send_surf.f
lines: 42
sha256: e569b6bd8f06f532eb29e0faa6c3da14073974e0f46f2dbda3cf5f655b88ae35
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_send_surf.f — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | SF_SEND_SURF의 선언부다. MYRANK>0이면 반환한다(17). WVLVL과 ZZ(1,NUMK)를 이 순서로 IROOTS에 보낸다(19–20). 이어서 SF_GIPND(IPND0,IPGRID0,NNOD0)를 호출한다(22). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_SEND_SURF(IPND0,IPFACE0,AFC,IPGRID0,ZZ,IRFACE` (1); `     &                       ,IRGRID0)` (2); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      INCLUDE 'VF_A0PRM.h'` (6); `      INCLUDE 'VF_ANUMBI.h'` (7); `      INCLUDE 'VF_APARAI.h'` (8); `      INCLUDE 'VF_APHYSR.h'` (9); `      INCLUDE 'SF_STRUCT.h'` (10); `      DIMENSION IPND0(NNOD0),IPGRID0(2,NNOD0),IPFACE0(12,NPFC0)` (12); `     &         ,AFC(NPFC0),ZZ(MAXG1,NUMK),IRFACE(NPFC0),IRGRID0(NNOD0)` (13); `      INTEGER, POINTER :: IPF(:,:)` (15); `      IF( MYRANK > 0 ) RETURN` (17); `      CALL SF_C_MPI_SEND_D(WVLVL,1,IROOTS)` (19); `      CALL SF_C_MPI_SEND_D(ZZ(1,NUMK),1,IROOTS)` (20); `      CALL SF_GIPND(IPND0,IPGRID0,NNOD0)` (22). 해석: WVLVL은 수위로 읽힌다. 해석: ZZ(1,NUMK)는 상단 Z 좌표로 읽힌다. 해석: SF_GIPND는 절점 표시를 구하는 루틴으로 읽힌다. [11-04 전수 검증 정정] |
| 24–42 | 시작 시 1행 SF_SEND_SURF 루틴 안. SF_SEND_SURF 안이며 루트(root) 처리다. IPF(10,NPFC0)에 IPFACE0의 3:12 성분을 복사하여 면 수와 함께 전송하고 IPF를 해제한다(24–32). AFC·IPND0를 보낸다(34–35). ISTM=1일 때 IRFACE·IRGRID0를 추가 전송한다(37–40). 원문(연속 표시는 앞 문장에 이어짐): `      ALLOCATE( IPF(10,NPFC0) )` (24); `      IPF(:,:) = 0` (26); `      IPF(:,:) = IPFACE0(3:12,:)` (27); `      CALL SF_C_MPI_SEND_I(NPFC0,1,IROOTS)` (29); `      CALL SF_C_MPI_SEND_I(IPF,NPFC0*10,IROOTS)` (30); `      DEALLOCATE( IPF )` (32); `      CALL SF_C_MPI_SEND_D(AFC,NPFC0,IROOTS)` (34); `      CALL SF_C_MPI_SEND_I(IPND0,NNOD0,IROOTS)` (35); `      IF( ISTM == 1 ) THEN` (37); `        CALL SF_C_MPI_SEND_I(IRFACE,NPFC0,IROOTS)` (38); `        CALL SF_C_MPI_SEND_I(IRGRID0,NNOD0,IROOTS)` (39); `      ENDIF` (40); `      END` (42). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
