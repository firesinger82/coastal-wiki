---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_stm_gather_i.f
lines: 76
sha256: 0db0eacd1fb64c3f3a49e38240ef775da4604119ed255d9dd210576a42a100af
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_stm_gather_i.f — 판독 구간 기록

구간은 1행부터 76행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | SF_STM_GATHER_I의 선언부다. ID=1·MYMIE=1이면 IOP=1, 그 외에는 0이다(13–17). ID=2·MYMJE=1이면 JOP=1, 그 외에는 0이다(19–23). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_STM_GATHER_I(K0,K,ID)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      INCLUDE 'VF_A0PRM.h'` (5); `      INCLUDE 'VF_ANUMBI.h'` (6); `      INCLUDE 'VF_APARAI.h'` (7); `      DIMENSION K0(NUMI0,NUMJ0),K(NUMI,NUMJ),IPT(4)` (9); `      INTEGER, POINTER :: KW(:,:)` (11); `      IF( ID == 1 .AND. MYMIE == 1 ) THEN` (13); `        IOP = 1` (14); `      ELSE` (15); `        IOP = 0` (16); `      ENDIF` (17); `      IF( ID == 2 .AND. MYMJE == 1 ) THEN` (19); `        JOP = 1` (20); `      ELSE` (21); `        JOP = 0` (22); `      ENDIF` (23). |
| 25–49 | 시작 시 1행 SF_STM_GATHER_I 루틴 안. SF_STM_GATHER_I 안. MYRANK=0이면 전역 정수 K0를 0으로 초기화하고 로컬(local) 구간을 복사한다(25–29). 다른 프로세스별로 IPT에서 시작 위치와 크기를 받아 KW를 할당한다(31–40). KW를 받아 전역 직사각형 구간에 복사하고 해제한다(42–46). 원문(연속 표시는 앞 문장에 이어짐): `      IF( MYRANK == 0 ) THEN` (25); `        K0(:,:) = 0` (27); `        K0(MYIS:MYIE+IOP,MYJS:MYJE+JOP) = K(MYIS:MYIE+IOP,MYJS:MYJE+JOP)` (29); `        DO IP = 1, NPROCS - 1` (31); `          CALL SF_MPI_RECV_I(IPT,4,IP)` (33); `          IS = IPT(1)` (35); `          NI = IPT(2)` (36); `          JS = IPT(3)` (37); `          NJ = IPT(4)` (38); `          ALLOCATE( KW(NI,NJ) )` (40); `          CALL SF_MPI_RECV_I(KW,NI*NJ,IP)` (42); `          K0(IS:IS+NI-1,JS:JS+NJ-1) = KW(:,:)` (44); `          DEALLOCATE( KW )` (46); `        ENDDO` (48). |
| 50–76 | 시작 시 `      IF( MYRANK == 0 ) THEN` (25)에서 시작한 IF/ELSEIF 사슬 안이다. 50행부터 MYRANK>0 분기를 읽는다. 이 사슬은 73행 ENDIF에서 닫힌다. MYRANK>0인 분기는 전역 시작 위치 IS·JS와 크기 NI·NJ를 계산한다(50–56). IPT를 루트(root)로 보낸다(58–63). 로컬 배열 구간을 KW에 복사하여 보내고 해제한다(65–71). 마지막 빈 줄도 포함한다(76). 원문(연속 표시는 앞 문장에 이어짐): `      ELSEIF( MYRANK > 0 ) THEN` (50); `        IS = MYGIS + MYMIS` (52); `        NI = MYIE - MYIS + 1 + IOP` (53); `        JS = MYGJS + MYMJS` (55); `        NJ = MYJE - MYJS + 1 + JOP` (56); `        IPT(1) = IS` (58); `        IPT(2) = NI` (59); `        IPT(3) = JS` (60); `        IPT(4) = NJ` (61); `        CALL SF_MPI_SEND_I(IPT,4,0)` (63); `        ALLOCATE( KW(NI,NJ) )` (65); `        KW(:,:) = K(MYIS:MYIE+IOP,MYJS:MYJE+JOP)` (67); `        CALL SF_MPI_SEND_I(KW,NI*NJ,0)` (69); `        DEALLOCATE( KW )` (71); `      ENDIF` (73); `      END` (75). 이 IF/ELSEIF 사슬에는 ELSE가 없다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 44: 수신 값을 K0에 직접 대입한다. 수신 구간의 중첩 여부 검사나 합산은 이 문장에 없다.
