---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/fric_updt.f
lines: 44
sha256: eb8dfccda3c037dc230db7e9a7972ad6972f24ec643ac1da2bf137421c48e28c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fric_updt.f — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 암시적 배정밀도(implicit double precision)와 IFRIC(10,*)·FRIC(10,*)·U0(3,4,*)·RL0(3,*) 등 인수 범위를 선언한다(3–6). MAXVAL(NINC)를 수신 버퍼의 마지막 차원으로 사용한다(11–14). 원문: `      SUBROUTINE FRIC_UPDT(IFRIC,FRIC,U0,RL0,NP,MINC,NINC,INC,INDCP)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION IFRIC(10,*),FRIC(10,*),NINC(NP),INC(MINC,NP),INDCP(2,*)` (5); `     &         ,U0(3,4,*),RL0(3,*)` (6); `      INTEGER, POINTER :: IFRICW(:,:)` (8); `      REAL(8), POINTER :: FRICW(:,:),U0W(:,:,:),RL0W(:,:)` (9); `      ALLOCATE( IFRICW(10,MAXVAL(NINC)) )` (11); `      ALLOCATE( FRICW(10,MAXVAL(NINC)) )` (12); `      ALLOCATE( U0W(3,4,MAXVAL(NINC)) )` (13); `      ALLOCATE( RL0W(3,MAXVAL(NINC)) )` (14). |
| 16–38 | 시작 시 1행 fric_updt 루틴 안. IP=1..NP에서 NINC(IP)가 0이면 건너뛴다(16–20). 마찰(friction) 정보와 U0·RL0를 10*N·12*N·3*N 크기로 수신한다(22–25). INC로 전역 위치 J를 얻고 INDCP(1,J)가 IP와 같을 때만 네 배열을 복사한다(27–35). 원문: `      DO IP = 1, NP` (16); `        N = NINC(IP)` (18); `        IF( N == 0 ) CYCLE` (20); `        CALL M_MPI_RECV_I(IFRICW,10*N,IP)` (22); `        CALL M_MPI_RECV_D(FRICW,10*N,IP)` (23); `        CALL M_MPI_RECV_D(U0W,12*N,IP)` (24); `        CALL M_MPI_RECV_D(RL0W,3*N,IP)` (25); `        DO I = 1, N` (27); `          J = INC(I,IP)` (28); `          IF( INDCP(1,J) == IP ) THEN` (29); `            IFRIC(:,J) = IFRICW(:,I)` (30); `            FRIC(:,J) = FRICW(:,I)` (31); `            U0(:,:,J) = U0W(:,:,I)` (32); `            RL0(:,J) = RL0W(:,I)` (33); `          ENDIF` (34); `        ENDDO` (35); `      ENDDO` (37). |
| 39–44 | 시작 시 1행 fric_updt 루틴 안. 수신 버퍼 네 개를 해제하고 종료한다(39–44). 원문: `      DEALLOCATE( IFRICW )` (39); `      DEALLOCATE( FRICW )` (40); `      DEALLOCATE( U0W )` (41); `      DEALLOCATE( RL0W )` (42); `      END` (44). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–14: 수신 버퍼 크기는 MAXVAL(NINC)에 의존한다. NP=0인 경우를 별도로 처리하는 분기는 이 파일에 없다.
