---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/cont_init_0.f
lines: 72
sha256: 60b29e9e14886199cff81fd99ed96e509d18df38ab7b69e9f24625ce942b923d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cont_init_0.f — 판독 구간 기록

구간은 1행부터 72행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | CONT_INIT_0는 MPI_PARAM·M_VAL·M_PART를 사용하여 접촉(contact) 초기 자료를 구성한다. 실수 IMPLICIT·KK(*)·POSW 포인터를 선언한다. KK에서 NNOD·NBDY·NIGSF·NINDC0를 얻고 NPROCS-1을 NPECG로 설정한다. POS(3,NNOD+NIGSF)를 할당하고 GATHER_NODAL_D에 POS와 3을 전달한다. GSURFQ의 첫 인수는 POS(1,NNOD+1)이다. 해석: 두 호출은 절점 위치 수집과 추가 표면 위치 계산용으로 보인다. POSW는 (3,SIZE(NODC,1))로 할당한다. 원문: `      SUBROUTINE CONT_INIT_0(KK)` (1); `      USE MPI_PARAM` (3); `      USE M_VAL` (4); `      USE M_PART` (5); `      IMPLICIT REAL*8 (A-H,O-Z)` (7); `      DIMENSION KK(*)` (8); `      REAL(8), POINTER :: POSW(:,:)` (9); `      NNOD = KK(8)` (11); `      NBDY = KK(92)` (12); `      NIGSF = KK(94)` (13); `      NINDC0 = KK(102)` (14); `      NPECG = NPROCS - 1` (16); `      ALLOCATE( POS(3,NNOD+NIGSF) )` (18); `      CALL GATHER_NODAL_D(POS,3)` (20); `      CALL GSURFQ(POS(1,NNOD+1),3,NIGSF,POS,IELQ,IVRQ(NNOD+1))` (22); `      ALLOCATE( POSW(3,SIZE(NODC,1)) )` (24) [11-04 전수 검증 정정] |
| 26–52 | 프로세스(process) IP=1,NPECG에서 N=NN_EXTC(IP)>0이면 NODC에 대응하는 위치를 POSW에 복사하여 목적지 IP에 전송한다. POSW를 해제한다. PSLV(3,4,NINDC0)를 할당하고 0으로 초기화한 뒤 두 번째 슬롯에 POS(:,INDC0(:))를 넣는다. M_MPI_BCAST_D로 12*NINDC0개를 방송(broadcast)한다. PSLV 해제 뒤 RSLV0를 할당한다. ISLV_UPDT의 48–51행 연속 호출에 ISLV0·ISLVP·RSLV0 등을 전달한다. 해석: ISLV_UPDT는 접촉 상태 갱신용으로 보인다. 원문: `      DO IP = 1, NPECG` (26); `        N = NN_EXTC(IP)` (27); `        IF( N > 0 ) THEN` (28); `          POSW(:,1:N) = POS(:,NODC(1:N,IP))` (29); `          CALL M_MPI_SEND_D(POSW,3*N,IP)` (30); `        ENDIF` (31); `      ENDDO` (32); `      DEALLOCATE( POSW )` (34); `      ALLOCATE( PSLV(3,4,NINDC0) )` (36); `      PSLV(:,:,:) = 0.` (38); `      PSLV(:,2,:) = POS(:,INDC0(:))` (40); `      CALL M_MPI_BCAST_D(PSLV,12*NINDC0)` (42); `      DEALLOCATE( PSLV )` (44); `      ALLOCATE( RSLV0(3,NINDC0) )` (46); `      CALL ISLV_UPDT(ISLV0,ISLVP,RSLV0,NNOD,NINDC0,NPECG,NN_EXT,NN_EXTC` (48); `     &              ,NOD,SIZE(NOD,1),NODG,SIZE(NODG,1),NODP,IEG` (49); `     &              ,SIZE(IEG,1),IEDGP,IEC,SIZE(IEC,1),IELCP,INDC0,IEDG` (50); `     &              ,IELC,IELQ,IFCQ,IEDQ,IVRQ)` (51) [11-04 전수 검증 정정] |
| 53–72 | IBDY=1,NBDY마다 ADDSET4에 IS·IE·IEDA·IBDY를 전달한다. J=IS,IE에서 LENGTH에 DIST와 IEDG(1,J)·IEDG(2,J)가 가리키는 POS를 전달한다. DIST를 EDML(IBDY)에 더한다. 합계를 IE-IS+1로 나눈다. 해석: 이 계산은 물체(body)별 평균 모서리 길이 계산으로 보인다. POS를 해제하고 IFRIC·FRIC·U0·RL0를 할당한다. IFRIC 전체를 0으로 초기화한다. 원문: `      DO IBDY = 1, NBDY` (53); `        CALL ADDSET4(IS,IE,IEDA,IBDY)` (54); `        EDML(IBDY) = 0.` (55); `        DO J = IS, IE` (56); `          CALL LENGTH(DIST,POS(1,IEDG(1,J)),POS(1,IEDG(2,J)),3)` (57); `          EDML(IBDY) = EDML(IBDY) + DIST` (58); `        ENDDO` (59); `        EDML(IBDY) = EDML(IBDY) / ( IE - IS + 1 )` (60); `      ENDDO` (61); `      DEALLOCATE( POS )` (63); `      ALLOCATE( IFRIC(10,NINDC0) )` (65); `      ALLOCATE( FRIC(10,NINDC0) )` (66); `      ALLOCATE( U0(3,4,NINDC0) )` (67); `      ALLOCATE( RL0(3,NINDC0) )` (68); `      IFRIC(:,:) = 0` (70); `      END` (72) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 56–60: EDML(IBDY)는 IE-IS+1로 나눈다. 해석: EDML은 평균 모서리 길이로 보인다. 이 파일에는 IS·IE 범위나 분모의 0 검사문이 없다. [11-04 전수 검증 정정]
- 65–70: IFRIC·FRIC·U0·RL0를 할당한다. 이 네 배열 중 이 파일에서 명시적으로 0을 대입하는 배열은 IFRIC이다. PSLV는 38행에서 별도로 0을 대입한다. [11-04 전수 검증 정정]
