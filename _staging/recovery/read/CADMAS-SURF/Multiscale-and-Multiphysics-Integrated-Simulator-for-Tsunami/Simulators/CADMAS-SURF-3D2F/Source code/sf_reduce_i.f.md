---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_reduce_i.f
lines: 49
sha256: 7c7e74f0d9abf88f1536d3bda1d12deec7bff7f886f3bb6e69b65a6ad0d46310
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_reduce_i.f — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | SF_REDUCE_I의 선언부다. MYRANK=0이면 정수 K0를 0으로 초기화한 후 N>0일 때 IDX 위치의 로컬(local) 값을 더한다(12–16). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_REDUCE_I(K0,N0,K,IDX,N)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      INCLUDE 'VF_A0PRM.h'` (5); `      INCLUDE 'VF_APARAI.h'` (6); `      DIMENSION K0(N0),K(N),IDX(N)` (8); `      INTEGER, POINTER :: IDXW(:),KW(:)` (10); `      IF( MYRANK == 0 ) THEN` (12); `        K0(:) = 0.` (14); `        IF( N > 0 ) K0( IDX(:) ) = K0( IDX(:) ) + K(:)` (16). |
| 18–36 | 시작 시 `      IF( MYRANK == 0 ) THEN` (12)의 참 분기 안이다. 이 분기 사슬은 46행 ENDIF에서 닫힌다. 다른 프로세스마다 NW를 받는다(18–20). NW=0이면 건너뛴다(22). 임시 IDXW·KW를 할당하여 받고 전역 대응 위치에 더한 뒤 해제한다(24–33). 원문(연속 표시는 앞 문장에 이어짐): `        DO IP = 1, NPROCS - 1` (18); `          CALL SF_MPI_RECV_I(NW,1,IP)` (20); `          IF( NW == 0 ) CYCLE` (22); `          ALLOCATE( IDXW(NW) )` (24); `          ALLOCATE( KW(NW) )` (25); `          CALL SF_MPI_RECV_I(IDXW,NW,IP)` (27); `          CALL SF_MPI_RECV_I(KW,NW,IP)` (28); `          K0( IDXW(:) ) = K0( IDXW(:) ) + KW(:)` (30); `          DEALLOCATE( IDXW )` (32); `          DEALLOCATE( KW )` (33); `        ENDDO` (35). [11-04 전수 검증 보완] |
| 37–49 | 시작 시 `      IF( MYRANK == 0 ) THEN` (12)에서 시작한 IF/ELSEIF 사슬 안이다. 37행부터 MYRANK>0 분기를 읽는다. 이 사슬은 46행 ENDIF에서 닫힌다. MYRANK>0이면 N을 루트(root)로 보낸다(37–39). N>0이면 IDX·K를 보낸다(41–44). 분기와 루틴을 닫고 마지막 빈 줄을 포함한다(46–49). 원문(연속 표시는 앞 문장에 이어짐): `      ELSEIF( MYRANK > 0 ) THEN` (37); `        CALL SF_MPI_SEND_I(N,1,0)` (39); `        IF( N > 0 ) THEN` (41); `          CALL SF_MPI_SEND_I(IDX,N,0)` (42); `          CALL SF_MPI_SEND_I(K,N,0)` (43); `        ENDIF` (44); `      ENDIF` (46); `      END` (48). 이 IF/ELSEIF 사슬에는 ELSE가 없다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16·30: IDX·IDXW를 전역 배열의 벡터 첨자로 사용한다. 이 루틴에는 첨자의 범위·중복 여부 검사문이 없다.
