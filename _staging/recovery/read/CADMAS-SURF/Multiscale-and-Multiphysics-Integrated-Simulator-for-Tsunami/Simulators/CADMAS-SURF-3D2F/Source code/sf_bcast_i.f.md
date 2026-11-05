---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_bcast_i.f
lines: 51
sha256: b7244402fb79880142aea6746382b94734ed3e87b7683db60574d31f1ba78309
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_bcast_i.f — 판독 구간 기록

구간은 1행부터 51행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | 정수 자료 분배 입구와 IMPLICIT·INCLUDE·K(M,N)·IDX(N)·K0(M,N0) 및 임시 정수 포인터(pointer)를 선언한다. 원문: `      SUBROUTINE SF_BCAST_I(K,IDX,N,K0,N0,M)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      INCLUDE 'VF_A0PRM.h'` (5); `      INCLUDE 'VF_APARAI.h'` (6); `      DIMENSION K(M,N),IDX(N),K0(M,N0)` (8); `      INTEGER, POINTER :: IDXW(:),KW(:,:)` (10) |
| 12–35 | 시작 시 1행 SF_BCAST_I 루틴 안이다. 순위(rank) 0은 `IF( N > 0 ) K(:,:) = K0(:,IDX(:))` (14)에 따라 N>0일 때만 자기 인덱스의 열을 복사한다. IP 루프로 요청 개수 NW·인덱스 IDXW를 받은 뒤 선택 자료 KW를 SF_MPI_SEND_I로 M*NW개 송신한다. NW==0이면 건너뛰며 임시 배열은 사용 후 해제한다. 원문: `      IF( MYRANK == 0 ) THEN` (12); `        IF( N > 0 ) K(:,:) = K0(:,IDX(:))` (14); `        DO IP = 1, NPROCS - 1` (16); `          CALL SF_MPI_RECV_I(NW,1,IP)` (18); `          IF( NW == 0 ) CYCLE` (20); `          ALLOCATE( IDXW(NW) )` (22); `          ALLOCATE( KW(M,NW) )` (23); `          CALL SF_MPI_RECV_I(IDXW,NW,IP)` (25); `          KW(:,:) = K0(:,IDXW(:))` (27); `          CALL SF_MPI_SEND_I(KW,M*NW,IP)` (29); `          DEALLOCATE( IDXW )` (31); `          DEALLOCATE( KW )` (32); `        ENDDO` (34) [11-04 전수 검증 보완] |
| 36–51 | 시작 시 1행 SF_BCAST_I 루틴·`IF( MYRANK == 0 ) THEN` (12)의 `ELSEIF( MYRANK > 0 ) THEN` (36) 분기이다. 이 사슬에는 ELSE가 없다. 바깥 조건은 `ENDIF` (48)에서 닫힌다. 양수 순위는 N을 0번으로 보내며 N>0이면 IDX 송신과 K의 M*N개 수신을 수행한다. 조건·루틴 종료와 끝 빈 줄이다. 원문: `      ELSEIF( MYRANK > 0 ) THEN` (36); `        CALL SF_MPI_SEND_I(N,1,0)` (38); `        IF( N > 0 ) THEN` (40); `          CALL SF_MPI_SEND_I(IDX,N,0)` (42); `          CALL SF_MPI_RECV_I(K,M*N,0)` (44); `        ENDIF` (46); `      ENDIF` (48); `      END` (50) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–48: 이름은 BCAST이지만 실제 호출은 SF_MPI_SEND_I·SF_MPI_RECV_I이다. MPI_BCAST 직접 호출은 없다.
- 20–29: NW==0 검사 뒤 임시 배열을 할당한다. 이 블록에는 NW 음수 검사나 IDXW의 1..N0 범위 검사문이 없다.
