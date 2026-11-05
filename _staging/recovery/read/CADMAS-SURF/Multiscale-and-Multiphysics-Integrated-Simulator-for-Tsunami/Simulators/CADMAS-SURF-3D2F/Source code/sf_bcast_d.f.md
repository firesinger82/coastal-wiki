---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_bcast_d.f
lines: 52
sha256: f70601d11e1a05b7aa20e6485796de3f236bccce7e54dd12914b44cba83817b7
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_bcast_d.f — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 배정밀도(double precision) 자료 분배 입구와 IMPLICIT·INCLUDE·X(M,N)·IDX(N)·X0(M,N0)·임시 포인터(pointer)를 선언한다. 원문: `      SUBROUTINE SF_BCAST_D(X,IDX,N,X0,N0,M)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      INCLUDE 'VF_A0PRM.h'` (5); `      INCLUDE 'VF_APARAI.h'` (6); `      DIMENSION X(M,N),IDX(N),X0(M,N0)` (8); `      INTEGER, POINTER :: IDXW(:)` (10); `      REAL(8), POINTER :: XW(:,:)` (11) |
| 13–36 | 시작 시 1행 SF_BCAST_D 루틴 안이다. 순위(rank) 0은 `IF( N > 0 ) X(:,:) = X0(:,IDX(:))` (15)에 따라 N>0일 때만 자기 IDX 자료를 X0에서 선택한다. IP=1부터 NPROCS-1까지 요청 개수 NW를 받고 NW==0이면 건너뛴다. 인덱스와 작업 배열을 할당하고 해당 열을 선택하여 SF_MPI_SEND_D로 M*NW개를 송신한 뒤 해제한다. 원문: `      IF( MYRANK == 0 ) THEN` (13); `        IF( N > 0 ) X(:,:) = X0(:,IDX(:))` (15); `        DO IP = 1, NPROCS - 1` (17); `          CALL SF_MPI_RECV_I(NW,1,IP)` (19); `          IF( NW == 0 ) CYCLE` (21); `          ALLOCATE( IDXW(NW) )` (23); `          ALLOCATE( XW(M,NW) )` (24); `          CALL SF_MPI_RECV_I(IDXW,NW,IP)` (26); `          XW(:,:) = X0(:,IDXW(:))` (28); `          CALL SF_MPI_SEND_D(XW,M*NW,IP)` (30); `          DEALLOCATE( IDXW )` (32); `          DEALLOCATE( XW )` (33); `        ENDDO` (35) [11-04 전수 검증 보완] |
| 37–52 | 시작 시 1행 SF_BCAST_D 루틴·`IF( MYRANK == 0 ) THEN` (13)의 `ELSEIF( MYRANK > 0 ) THEN` (37) 분기이다. 이 사슬에는 ELSE가 없다. 바깥 조건은 `ENDIF` (49)에서 닫힌다. 양수 순위는 N을 0번에 송신한다. N>0일 때 인덱스를 보내고 배정밀도 자료 M*N개를 받는다. 조건·루틴을 끝내며 마지막 빈 줄도 포함한다. 원문: `      ELSEIF( MYRANK > 0 ) THEN` (37); `        CALL SF_MPI_SEND_I(N,1,0)` (39); `        IF( N > 0 ) THEN` (41); `          CALL SF_MPI_SEND_I(IDX,N,0)` (43); `          CALL SF_MPI_RECV_D(X,M*N,0)` (45); `        ENDIF` (47); `      ENDIF` (49); `      END` (51) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13–49: 이름은 BCAST이지만 이 파일의 실제 호출은 SF_MPI_SEND_I·SF_MPI_RECV_I·SF_MPI_SEND_D·SF_MPI_RECV_D이다. MPI_BCAST 직접 호출은 없다.
- 21–30: NW==0 검사 뒤 임시 배열을 할당한다. 이 블록에는 NW 음수 검사나 IDXW의 1..N0 범위 검사문이 없다.
