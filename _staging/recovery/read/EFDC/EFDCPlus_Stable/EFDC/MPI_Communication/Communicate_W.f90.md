---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Communication/Communicate_W.f90
lines: 256
sha256: c21c5763131bef113e348a59952a5cebd30b20e5920e1c1d1a9b2577ad0a7696
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Communicate_W.f90 — 판독 구간 기록

구간은 1행부터 256행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | EFDC+ 소속·웹사이트·저장소·2021–2022 DSI 저작권·GNU GPLv2 머리말과 개발 구분 주석(1–11). W 해의 일부인 UHDY/VHDX를 통신한다는 설명, 작성자·날짜 주석(12–15), 빈 줄(16). |
| 17–58 | `COMMUNICATE_W` 시작(17), GLOBAL·Variables_MPI·MPI 사용 및 implicit none(19–23). I/J/II/L/K·istatus·length_arg·INTEGER(4) IERR 선언(26–29). 메시지 전달 인터페이스(Message Passing Interface, MPI) 통신용 실수 save·allocatable 방향별 송수신 버퍼 8개 선언(31–38). `IF(.NOT.ALLOCATED(WSENDW))THEN` (40)에서 동서 버퍼는 max_width_y*4*KCM, 남북 버퍼는 max_width_x*4*KCM 크기로 할당(41–48). 모두 0.0 초기화(49–56), 조건 종료·빈 줄(57–58). |
| 59–82 | 시작 시 17행 `COMMUNICATE_W` 안. 서쪽 송신 `IF (nbr_west.NE.-1)THEN` (60), II=0, `DO K = 1, KC` (62)·`DO I =3,4` (63)·`DO J = 3,JC-2` (64)에서 L=LIJ(I,J)(65). `II =II + 1` (66) 다음 `if( l > 0) then` (67)이면 UHDY(L,K)를 WSENDW(II)에 복사(68). `II = II + 1` (70) 다음 `if( l > 0) then` (71)이면 VHDX(L,K)를 복사(72). IERR=0(77), `length_arg = (JC-4)*4*KC` (78). MPI 송신 호출은 `CALL MPI_SEND(WSENDW,length_arg,mpi_real,nbr_west,process_id,  &` (79)와 다음 계속행 `comm_2d, IERR)` (80). 대상은 nbr_west, 태그(tag)는 process_id, 통신자(communicator)는 comm_2d이다. 분기·루프 종료 및 빈 줄을 포함한다. |
| 83–108 | 시작 시 17행 `COMMUNICATE_W` 안. 동쪽 수신 `IF (nbr_east.NE.-1)THEN` (84), `length_arg = (JC-4)*4*KC` (86). 호출은 `CALL MPI_RECV(WRECVE,length_arg, mpi_real, nbr_east, nbr_east,  &` (88)와 계속행 `comm_2d, ISTATUS, IERR)` (89)이며 송신자·태그는 nbr_east이다. II=0, `DO K = 1,KC` (92)·`DO I =IC-1,IC` (93)·`DO J = 3,JC-2` (94)에서 L을 구한다(95). `II =II + 1` (96) 다음 `if( l > 0) then` (97)이면 동쪽 고스트 셀(ghost cell)의 UHDY에 WRECVE 복사(98). `II = II + 1` (100) 다음 `if( l > 0) then` (101)이면 VHDX에 복사(102). 분기·루프 종료 및 빈 줄을 포함한다. |
| 109–132 | 시작 시 17행 `COMMUNICATE_W` 안. 동쪽 송신 `IF (nbr_east.NE.-1)THEN` (110), ii=0, `DO K = 1,KC` (112)·`DO I =IC-3,IC-2` (113)·`DO J = 3,JC-2` (114)에서 L을 구한다(115). `II =II + 1` (116) 다음 `if( l > 0) then` (117)이면 UHDY를 WSENDE에 복사(118). `II = II + 1` (120) 다음 `if( l > 0) then` (121)이면 VHDX를 복사(122). IERR=0(127), `length_arg = (JC-4)*4*KC` (128). 호출은 `CALL MPI_SEND(WSENDE,length_arg,mpi_real,nbr_east,process_id,  &` (129)와 계속행 `comm_2d, IERR)` (130)이며 대상은 nbr_east, 태그는 process_id이다. 분기·루프 종료 및 빈 줄을 포함한다. |
| 133–157 | 시작 시 17행 `COMMUNICATE_W` 안. 서쪽 수신 `IF (nbr_west.NE.-1)THEN` (134), `length_arg = (JC-4)*4*KC` (136). 호출은 `CALL MPI_RECV(WRECVW,length_arg,mpi_real,nbr_west,nbr_west, &` (138)와 계속행 `comm_2d,ISTATUS,IERR)` (139)이며 송신자·태그는 nbr_west이다. II=0, `DO K = 1,KC` (141)·`DO I =1,2` (142)·`DO J = 3,JC-2` (143)에서 L을 구한다(144). `II =II + 1` (145) 다음 `if( l > 0) then` (146)이면 서쪽 고스트 UHDY에 WRECVW 복사(147). `II = II + 1` (149) 다음 `if( l > 0) then` (150)이면 VHDX에 복사(151). 분기·루프 종료 및 빈 줄을 포함한다. |
| 158–181 | 시작 시 17행 `COMMUNICATE_W` 안. 북쪽 송신 `IF (nbr_north.NE.-1)THEN` (159), II=0, `DO K = 1,KC` (161)·`DO I = 1, IC` (162)·`DO J = JC-3,JC-2` (163)에서 L을 구한다(164). `II =II + 1` (165) 다음 `if( l > 0) then` (166)이면 UHDY를 WSENDN에 복사(167). `II = II + 1` (169) 다음 `if( l > 0) then` (170)이면 VHDX를 복사(171). IERR=0(176), `length_arg = IC*4*KC` (177). 호출은 `CALL MPI_SEND(WSENDN,length_arg,mpi_real,nbr_north,process_id, &` (178)와 계속행 `comm_2d, IERR)` (179)이며 대상은 nbr_north, 태그는 process_id이다. 분기·루프 종료 및 빈 줄을 포함한다. |
| 182–204 | 시작 시 17행 `COMMUNICATE_W` 안. 남쪽 수신 `IF (nbr_south.NE.-1)THEN` (183), `length_arg = IC*4*KC` (184). 호출은 `CALL MPI_RECV(WRECVS,length_arg,mpi_real,nbr_south,nbr_south, &` (185)와 계속행 `comm_2d,ISTATUS,IERR)` (186)이며 송신자·태그는 nbr_south이다. II=0, `DO K = 1,KC` (188)·`DO I = 1,IC` (189)·`DO J = 1,2` (190)에서 L을 구한다(191). `II =II + 1` (192) 다음 `if( l > 0) then` (193)이면 남쪽 고스트 UHDY에 WRECVS 복사(194). `II = II + 1` (196) 다음 `if( l > 0) then` (197)이면 VHDX에 복사(198). 분기·루프 종료 및 빈 줄을 포함한다. |
| 205–229 | 시작 시 17행 `COMMUNICATE_W` 안. 남쪽 송신 `IF (nbr_south.NE.-1)THEN` (206), II=0, `DO K = 1,KC` (208)·`DO I = 1, IC` (209)·`DO J = 3,4` (210)에서 L을 구한다(211). `II =II + 1` (212) 다음 `if( l > 0) then` (213)이면 UHDY를 WSENDS에 복사(214). `II = II + 1` (216) 다음 `if( l > 0) then` (217)이면 VHDX를 복사(218). IERR=0(224), `length_arg = IC*4*KC` (225). 호출은 `CALL MPI_SEND(WSENDS,length_arg,mpi_real,nbr_south,process_id, &` (226)와 계속행 `comm_2d, IERR)` (227)이며 대상은 nbr_south, 태그는 process_id이다. 분기·루프 종료 및 빈 줄을 포함한다. |
| 230–256 | 시작 시 17행 `COMMUNICATE_W` 안. 북쪽 수신 `IF (nbr_north.NE.-1)THEN` (231), `length_arg = IC*4*KC` (233). 호출은 `CALL MPI_RECV(WRECVN,length_arg,mpi_real,nbr_north,nbr_north, &` (235)와 계속행 `comm_2d,ISTATUS,IERR)` (236)이며 송신자·태그는 nbr_north이다. II=0, `DO K = 1,KC` (238)·`DO I = 1,IC` (239)·`DO J = JC-1,JC` (240)에서 L을 구한다(241). `II =II + 1` (242·246) 뒤 각각 `if( l > 0) then` (243·247)이면 북쪽 고스트 UHDY/VHDX에 WRECVN 복사(244·248). 분기·루프 종료, 빈 줄(254–255), 루틴 종료(256). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27·88–89·138–139·185–186·235–236: istatus는 단일 Integer 변수로 선언되어 있다. MPI_RECV 네 호출은 이 단일 변수를 상태 인수로 전달한다.
- 40–57·66–73·116–123·165–172·212–219: 송신 버퍼 전체 0 초기화는 최초 할당 조건 안에만 있다. 각 포장 루프는 L>0 검사 앞에서 II를 증가시킨다. L<=0인 위치에는 해당 호출에서 버퍼 값을 대입하지 않는다. 송신 길이는 유효 L 개수와 무관한 격자 크기식이다(78·128·177·225).
- 31–57: 방향별 버퍼는 save로 유지된다. 모든 버퍼의 할당은 WSENDW 미할당 조건으로 묶여 있다. 이 루틴에는 격자 크기 변경에 따른 재할당문이나 deallocate문이 없다.
- 29·77–80·127–130·176–179·224–227 및 네 MPI_RECV 호출: IERR는 MPI 호출의 반환 인수로 사용된다. 0 대입은 MPI_SEND 앞에 있다. 이 파일에는 반환 IERR나 ISTATUS를 검사하는 조건이 없다.
- 17–58·60·84·110·134·159·183·206·231: 이 루틴에는 num_Processors==1 조기 반환문이 없다. 통신 실행 조건은 방향별 이웃 번호가 -1과 다른지의 검사이다.
- 62–64·92–94·112–114·141–143·161–163·188–190·208–210·238–240: 모든 수직 순회는 K=1..KC이고 층별 KSZ(L) 조건은 없다. 송수신 경계 폭은 두 셀로 고정되어 있다.
