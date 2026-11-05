---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/output0.f
lines: 98
sha256: 3b218d01a9d8d4e968582fb37cda89c9b9584a915dbe91e9243276c35486743e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# output0.f — 판독 구간 기록

구간은 1행부터 98행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | M_VAL·파일명·4자리 문자열 NO와 UG 포인터를 선언한다(3–10). DATA JOUT / -1 /로 시작하고 호출마다 JOUT을 1 늘린다(12·17). str_out/ 접두 경로와 길이 N=8+NLEN을 만들고 I4.4 형식 번호를 생성한다(14–18). 원문: `      SUBROUTINE OUTPUT0(KK,IFL,FLNAME,NLEN,ICHK)` (1); `      USE M_VAL` (3); `      CHARACTER*256 FLNAME` (5); `      CHARACTER*256 FLN` (6); `      CHARACTER*4 NO` (7); `      DIMENSION KK(*),IFL(*)` (9); `      REAL(8),POINTER :: UG(:,:)` (10); `      DATA JOUT / -1 /` (12); `C-----------------------------------------------------------------------` (13); `      FLN = 'str_out/'//FLNAME(1:NLEN)` (14); `      N = 8 + NLEN` (15); `      JOUT = JOUT + 1` (17); `      WRITE(NO,'(I4.4)') JOUT` (18). |
| 20–44 | 시작 시 1행 output0 루틴 안. .disp_·.vel_·.acc_·.rfc_ 파일을 연다(20–23). KK(25) 양수이면 .pprs_도 연다(24–25). OUTNOD0 호출 후 파일을 닫는다(27–33). .sols_·.sole_·.solps_ 파일을 열고 OUTSOL0 호출 후 닫는다(35–43). 원문: `      OPEN( IFL(20), FILE = FLN(1:N)//'.disp_'//NO )` (20); `      OPEN( IFL(21), FILE = FLN(1:N)//'.vel_'//NO )` (21); `      OPEN( IFL(22), FILE = FLN(1:N)//'.acc_'//NO )` (22); `      OPEN( IFL(23), FILE = FLN(1:N)//'.rfc_'//NO )` (23); `      IF( KK(25) > 0 ) ` (24); `     &  OPEN( IFL(24), FILE = FLN(1:N)//'.pprs_'//NO )` (25); `      CALL OUTNOD0(KK(8),KK(25),IFL)` (27); `      CLOSE( IFL(20) )` (29); `      CLOSE( IFL(21) )` (30); `      CLOSE( IFL(22) )` (31); `      CLOSE( IFL(23) )` (32); `      IF( KK(25) > 0 ) CLOSE( IFL(24) )` (33); `      OPEN( IFL(20), FILE = FLN(1:N)//'.sols_'//NO )` (35); `      OPEN( IFL(21), FILE = FLN(1:N)//'.sole_'//NO )` (36); `      OPEN( IFL(22), FILE = FLN(1:N)//'.solps_'//NO )` (37); `      CALL OUTSOL0(KK(8),IFL)` (39); `      CLOSE( IFL(20) )` (41); `      CLOSE( IFL(21) )` (42); `      CLOSE( IFL(22) )` (43). |
| 45–63 | 시작 시 1행 output0 루틴 안. KK(25) 양수이면 .flux_ 파일에 OUTSOIL0으로 결과를 쓴다(45–53). ICHK<2이면 반환한다(55). KK(81) 또는 KK(92) 양수이면 .dispw_를 열고 UG(6,KK(8)+KK(94))를 수집하여 GSURFQ를 호출한다(57–62). 원문: `      IF( KK(25) > 0 ) THEN` (45); `        OPEN( IFL(20), FILE = FLN(1:N)//'.flux_'//NO )` (47); `        CALL OUTSOIL0(KK(8),IFL(20))` (49); `        CLOSE( IFL(20) )` (51); `      ENDIF` (53); `      IF( ICHK < 2 ) RETURN` (55); `      IF( KK(81) > 0 .OR. KK(92) > 0 ) THEN` (57); `        OPEN( IFL(20), FILE = FLN(1:N)//'.dispw_'//NO )` (58); `        ALLOCATE( UG(6,KK(8)+KK(94)) )` (59); `        CALL GATHER_NODAL_D(UG,6)` (60); `        CALL GSURFQ(UG(1,KK(8)+1),6,KK(94),UG,IELQ,IVRQ(KK(8)+1))` (61); `      ENDIF` (62). |
| 64–82 | 시작 시 1행 output0 루틴 안. KK(81) 양수이면 .surfp_를 열고 PPND를 수집한다(64–68). OUTNODW를 호출한다(70–71). UG·PPND와 해당 파일은 각 할당 조건에 대응하는 분기에서 해제·종료한다(73–81). 원문: `      IF( KK(81) > 0 ) THEN` (64); `        OPEN( IFL(21), FILE = FLN(1:N)//'.surfp_'//NO )` (65); `        ALLOCATE( PPND(KK(8)) )` (66); `        CALL GATHER_NODAL_D(PPND,1)` (67); `      ENDIF` (68); `      CALL OUTNODW(UG,PPND,KK(8),KK(11),KK(81),KK(92),KK(94),N_PART` (70); `     &            ,NG_ENSW,IG_ENSW,IFL)` (71); `      IF( KK(81) > 0 .OR. KK(92) > 0 ) THEN` (73); `        DEALLOCATE( UG )` (74); `        CLOSE( IFL(20) )` (75); `      ENDIF` (76); `      IF( KK(81) > 0 ) THEN` (78); `        DEALLOCATE( PPND )` (79); `        CLOSE( IFL(21) )` (80); `      ENDIF` (81). |
| 83–98 | 시작 시 1행 output0 루틴 안. KK(81) 양수이면 .surfa_를 열고 AFC(KK(81))를 수집한다(83–88). WTSURF로 결과를 기록하고 AFC 해제·파일 종료 후 루틴을 끝낸다(90–98). 원문: `      IF( KK(81) > 0 ) THEN` (83); `        OPEN( IFL(20), FILE = FLN(1:N)//'.surfa_'//NO )` (85); `        ALLOCATE( AFC(KK(81)) )` (87); `        CALL GATHER_SURFACE(AFC,1)` (88); `        CALL WTSURF(AFC,KK(11),KK(81),N_PART,NE_ENSW,IE_ENSW,IFL(20))` (90); `        DEALLOCATE( AFC )` (92); `        CLOSE( IFL(20) )` (94); `      ENDIF` (96); `      END` (98). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7·12·17–18: 출력 번호 문자열은 길이 4이며 JOUT은 DATA의 -1에서 증가하여 첫 호출에 0을 출력한다. 4자리 범위 초과를 처리하는 분기는 이 파일에 없다.
- 55–71: ICHK>=2이면 OUTNODW 호출에 도달한다. UG와 PPND의 할당은 각각 KK(81)/KK(92) 조건과 KK(81) 조건에 달려 있다. 호출 루틴 내부는 이번 판독 대상이 아니다.
