---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_stm_scatter_d.f
lines: 53
sha256: af84da68516d4617bea2dcac5b1a1ef31633e3186eaa0d63f432ae55e9f99a91
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_stm_scatter_d.f — 판독 구간 기록

구간은 1행부터 53행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | SF_STM_SCATTER_D 시작. 암시적 실수 선언·세 INCLUDE 및 전역·로컬 배열과 포인터를 선언한다(1–11). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      SUBROUTINE SF_STM_SCATTER_D(X,X0)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      INCLUDE 'VF_A0PRM.h'` (5)<br>`      INCLUDE 'VF_ANUMBI.h'` (6)<br>`      INCLUDE 'VF_APARAI.h'` (7)<br>`      DIMENSION X0(NUMI0,NUMJ0),X(NUMI,NUMJ),IPT(4)` (9)<br>`      REAL(8), POINTER :: XW(:,:)` (11) |
| 13–38 | 시작 시 1행 루틴 안. 순위(rank) 0은 전역 부분 배열을 복사한다. 순위 0은 `DO IP = 1, NPROCS - 1`의 각 IP에서 범위를 받는다. 순위 0은 NI·NJ를 계산하고 작업 배열을 할당·전송·해제한다(17–37). MPI 래퍼(wrapper)의 인수를 그대로 적는다. 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      IF( MYRANK == 0 ) THEN` (13)<br>`        X(:,:) = X0(MYGIS:MYGIE,MYGJS:MYGJE)` (15)<br>`        DO IP = 1, NPROCS - 1` (17)<br>`          CALL SF_MPI_RECV_I(IPT,4,IP)` (19)<br>`          IS = IPT(1)` (21)<br>`          IE = IPT(2)` (22)<br>`          JS = IPT(3)` (23)<br>`          JE = IPT(4)` (24)<br>`          NI = IE - IS + 1` (26)<br>`          NJ = JE - JS + 1` (27)<br>`          ALLOCATE( XW(NI,NJ) )` (29)<br>`          XW(:,:) = X0(IS:IE,JS:JE)` (31)<br>`          CALL SF_MPI_SEND_D(XW,NI*NJ,IP)` (33)<br>`          DEALLOCATE( XW )` (35)<br>`        ENDDO` (37) [11-04 전수 검증 정정] |
| 39–53 | 시작 시 13행 `IF( MYRANK == 0 ) THEN`의 분기 경계다. 이 IF는 50행 `ENDIF`에서 닫힌다. `ELSEIF( MYRANK > 0 ) THEN` 다음에는 ELSE가 없다. 양의 순위는 자신의 범위를 0번에 보내고 로컬 배열을 받는다(39–48). 분기와 루틴을 닫는다. 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      ELSEIF( MYRANK > 0 ) THEN` (39)<br>`        IPT(1) = MYGIS` (41)<br>`        IPT(2) = MYGIE` (42)<br>`        IPT(3) = MYGJS` (43)<br>`        IPT(4) = MYGJE` (44)<br>`        CALL SF_MPI_SEND_I(IPT,4,0)` (46)<br>`        CALL SF_MPI_RECV_D(X,NUMI*NUMJ,0)` (48)<br>`      ENDIF` (50)<br>`      END` (52) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
