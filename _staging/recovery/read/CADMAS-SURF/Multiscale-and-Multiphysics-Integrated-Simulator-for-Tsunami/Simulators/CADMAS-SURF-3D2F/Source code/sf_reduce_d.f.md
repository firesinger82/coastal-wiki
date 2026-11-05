---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_reduce_d.f
lines: 50
sha256: 39ca670a5c21df25537b83f4460acfe5d1d90dde54d45937f5d7e81a01ff49f6
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_reduce_d.f — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | SF_REDUCE_D의 선언부다. MYRANK=0이면 X0를 0으로 초기화한 후 N>0일 때 IDX 위치의 로컬(local) 값을 더한다(13–17). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_REDUCE_D(X0,N0,X,IDX,N)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      INCLUDE 'VF_A0PRM.h'` (5); `      INCLUDE 'VF_APARAI.h'` (6); `      DIMENSION X0(N0),X(N),IDX(N)` (8); `      INTEGER, POINTER :: IDXW(:)` (10); `      REAL(8), POINTER :: XW(:)` (11); `      IF( MYRANK == 0 ) THEN` (13); `        X0(:) = 0.` (15); `        IF( N > 0 ) X0( IDX(:) ) = X0( IDX(:) ) + X(:)` (17). |
| 19–37 | 시작 시 `      IF( MYRANK == 0 ) THEN` (13)의 참 분기 안이다. 이 분기 사슬은 47행 ENDIF에서 닫힌다. 다른 프로세스마다 NW를 받는다(19–21). NW=0이면 건너뛴다(23). 임시 IDXW·XW를 할당하여 받고 전역 대응 위치에 더한 뒤 해제한다(25–34). 원문(연속 표시는 앞 문장에 이어짐): `        DO IP = 1, NPROCS - 1` (19); `          CALL SF_MPI_RECV_I(NW,1,IP)` (21); `          IF( NW == 0 ) CYCLE` (23); `          ALLOCATE( IDXW(NW) )` (25); `          ALLOCATE( XW(NW) )` (26); `          CALL SF_MPI_RECV_I(IDXW,NW,IP)` (28); `          CALL SF_MPI_RECV_D(XW,NW,IP)` (29); `          X0( IDXW(:) ) = X0( IDXW(:) ) + XW(:)` (31); `          DEALLOCATE( IDXW )` (33); `          DEALLOCATE( XW )` (34); `        ENDDO` (36). [11-04 전수 검증 보완] |
| 38–50 | 시작 시 `      IF( MYRANK == 0 ) THEN` (13)에서 시작한 IF/ELSEIF 사슬 안이다. 38행부터 MYRANK>0 분기를 읽는다. 이 사슬은 47행 ENDIF에서 닫힌다. MYRANK>0인 병렬 분기는 N을 루트(root)로 보낸다(38–40). N>0이면 IDX·X를 보낸다(42–45). 분기와 루틴을 닫고 마지막 빈 줄을 포함한다(47–50). 원문(연속 표시는 앞 문장에 이어짐): `      ELSEIF( MYRANK > 0 ) THEN` (38); `        CALL SF_MPI_SEND_I(N,1,0)` (40); `        IF( N > 0 ) THEN` (42); `          CALL SF_MPI_SEND_I(IDX,N,0)` (43); `          CALL SF_MPI_SEND_D(X,N,0)` (44); `        ENDIF` (45); `      ENDIF` (47); `      END` (49). 이 IF/ELSEIF 사슬에는 ELSE가 없다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 17·31: IDX·IDXW를 전역 배열의 벡터 첨자로 사용한다. 이 루틴에는 첨자의 범위·중복 여부 검사문이 없다.
