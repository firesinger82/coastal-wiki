---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Communication/mod_allreduce.f90
lines: 399
sha256: 1a69cc0fc32c7f5856f23077378182f0cd279fef5aa0a4f20a05d85a8ae0e116
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_allreduce.f90 — 판독 구간 기록

구간은 1행부터 399행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–44 | EFDC+·저작권·GPLv2 머리말과 전체 축약(all-reduce)의 시간 측정 목적·작성자·날짜 주석(1–11). `MPI_All_Reduce` 모듈을 시작한다(12). MPI 연산 상수의 16진수 설명 주석이 있다(14–16). GLOBAL·MPI·Variables_MPI를 사용하고 implicit none·save를 선언한다(18–24). 공개 제네릭 인터페이스(generic interface) `DSI_All_Reduce`는 Integer·Real4·Real8·Real48·Reduce2_8·Reduce2의 여섯 루틴을 연결한다(26–38). MPI_SEND·MPI_RECV의 STATUS에 관한 주석과 contains·빈 줄을 포함한다(40–44). |
| 45–77 | `DSI_All_Reduce_Integer`의 정수 입력·출력과 실수 시간 출력, DSTIME·지역 변수 선언(45–53). `if( num_Processors > 1 )then` (55) 안에서 `if( iWait > 0 )then` (56)이면 DSTIME 시작값을 저장하고 `MPI_barrier`를 호출하며 `WaitTime = DSTIME(0) - TTDS` (59)를 계산한다. `elseif( iWait < 0 )then` (60)이면 WaitTime을 0으로 설정하고 barrier를 호출한다(61–62). 축약 시작 시간을 저장하고 `MPI_ALLREDUCE(ValIn, ValOut, 1, MPI_Integer, iOp, DSIcomm, IERR)`를 호출한다(64–66). `ElapsedTime = DSTIME(0) - TTDS` (68). 바깥 else에서는 입력을 출력으로 복사하고 두 시간을 0으로 설정한다(69–72). 조건·루틴 종료와 빈 줄(73–77). |
| 78–110 | `DSI_All_Reduce_Real4`는 RK4 스칼라 입력·출력과 RKD 시간 출력이다(78–87). `if( num_Processors > 1 )then` (89), `if( iWait > 0 )then` (90), `elseif( iWait < 0 )then` (94)로 barrier의 측정 여부를 나눈다. 양의 iWait에서는 `WaitTime = DSTIME(0) - TTDS` (93), 음의 iWait에서는 WaitTime=0과 barrier 호출(95–96). `MPI_ALLREDUCE`는 원소 수 1·MPI_Real4·iOp·DSIcomm을 사용한다(100). `ElapsedTime = DSTIME(0) - TTDS` (102). 바깥 else는 출력 복사·두 시간 0 설정(103–106). 조건·루틴 종료와 빈 줄(107–110). |
| 111–143 | `DSI_All_Reduce_Real8`는 real(8) 입력·출력과 RKD 시간 출력이다(111–120). `if( num_Processors > 1 )then` (122), `if( iWait > 0 )then` (123), `elseif( iWait < 0 )then` (127). 양의 iWait에서는 barrier 뒤 `WaitTime = DSTIME(0) - TTDS` (126), 음의 iWait에서는 WaitTime=0과 barrier 호출(128–129). `MPI_ALLREDUCE`는 원소 수 1·MPI_Real8을 사용한다(133). `ElapsedTime = DSTIME(0) - TTDS` (135). 바깥 else는 출력 복사·두 시간 0 설정(136–139). 조건·루틴 종료와 빈 줄(140–143). |
| 144–178 | `DSI_All_Reduce_Real48`은 RK4 입력을 RKD 출력으로 축약한다(144–154). `if( num_Processors > 1 )then` (156), `if( iWait > 0 )then` (157), `elseif( iWait < 0 )then` (161). barrier 측정식은 `WaitTime = DSTIME(0) - TTDS` (160). 음의 iWait에서는 WaitTime=0과 barrier 호출(162–163). `VAL8 = DBLE(ValIn)` (167) 후 원소 수 1·MPI_Real8로 `MPI_ALLREDUCE`를 호출한다(168). `ElapsedTime = DSTIME(0) - TTDS` (170). 바깥 else에서 `ValOut = DBLE(ValIn)` (172), 두 시간 0 설정(173–174). 조건·루틴 종료와 빈 줄(175–178). |
| 179–225 | `DSI_All_Reduce2`는 RK4 값과 정수 식별자를 함께 받는다(179–195). MPI·Variables_MPI·Broadcast_Routines를 사용한다(181–183). 프로세서 수 크기의 displ·IRECV, 길이 2의 VarSend와 `num_Processors*2`의 VarRec를 선언한다(198–203). `if( num_Processors > 1 )then` (205) 안에서 `if( iWait > 0 )then` (206)일 때 barrier와 `WaitTime = DSTIME(0) - TTDS` (209), `elseif( iWait < 0 )then` (210)일 때 WaitTime=0과 barrier를 수행한다. 시작 시간을 저장한다(214). `do i = 1,num_Processors` (216)에서 `displ(i) = (i-1)*2` (217). 수신 배열·ierr를 0으로 설정한다(219–220). 첫 송신값을 복사하고 `VarSend(2) = REAL(VarIn2)` (223), IRECV=2(224). `MPI_GatherV`는 각 프로세서의 MPI_Real4 두 원소를 master_id에 모은다(225). |
| 226–288 | 시작 시 179행 DSI_All_Reduce2·205행 다중 프로세서 참 분기 안. VarOut2=0(227). `if( process_id == master_id )then` (228) 안에서 `if( iOp == MPI_SUM )then` (230)은 `VarOp = 0.0` (232), `II = (i-1)*2 + 1` (234), `VarOp = VarOp + VarRec(II)` (235). `elseif( iOp == MPI_MAX )then` (238)은 iMax=0과 `VarOp = -1.e32` (241), `II = (i-1)*2 + 1` (243), `if( VarOp < VarRec(II) )then` (244)일 때 값·iMax를 갱신하고(245–246) `VarOut2 = VarRec(II+1)` (247)를 대입한다. `elseif( iOp == MPI_MIN )then` (251)은 iMin=0과 `VarOp = 1.e32` (254), `II = (i-1)*2 + 1` (256), `if( VarOp > VarRec(II) )then` (257)일 때 값·iMin을 갱신하고(258–259) `VarOut2 = VarRec(II+1)` (260)를 대입한다. `elseif( iOp == MPI_PROD )then` (264)은 `VarOp = 1._8` (266), `II = (i-1)*2 + 1` (268), `VarOp = VarOp * VarRec(II)` (269). 각 연산은 프로세서 1..num_Processors를 순회한다(233·242·255·267). master 조건 종료 뒤 `Broadcast_Scalar(VarOp, master_id)`를 호출하고 VarOut1에 복사한다(275–277). `ElapsedTime = DSTIME(0) - TTDS` (279). 205행 조건의 else는 두 입력을 출력에 복사하고 시간을 0으로 설정한다(280–284). 조건·루틴 종료와 빈 줄(285–288). |
| 289–335 | `DSI_All_Reduce2_8`은 RKD 값과 정수 식별자를 함께 받는다(289–305). MPI·Variables_MPI·Broadcast_Routines와 배열 선언을 포함한다(291–313). `if( num_Processors > 1 )then` (315), `if( iWait > 0 )then` (316), `elseif( iWait < 0 )then` (320). 양의 iWait에서는 barrier 뒤 `WaitTime = DSTIME(0) - TTDS` (319). 음의 iWait에서는 WaitTime=0과 barrier 호출(321–322). `do i = 1,num_Processors` (326)에서 `displ(i) = (i-1)*2` (327). 수신 배열·ierr를 0으로 설정한다(329–330). 첫 송신값을 복사하고 `VarSend(2) = REAL(VarIn2,8)` (333), IRECV=2(334). `MPI_GatherV`는 MPI_Real8 두 원소를 master_id에 모은다(335). |
| 336–399 | 시작 시 289행 DSI_All_Reduce2_8·315행 다중 프로세서 참 분기 안. VarOut2=0(337). `if( process_id == master_id )then` (338). `if( iOp == MPI_SUM )then` (340)은 `VarOp = 0.0` (342), `II = (i-1)*2 + 1` (344), `VarOp = VarOp + VarRec(II)` (345). `elseif( iOp == MPI_MAX )then` (348)은 iMax=0과 `VarOp = -1.e32` (351), `II = (i-1)*2 + 1` (353), `if( VarOp < VarRec(II) )then` (354)일 때 값·iMax를 갱신하고(355–356) `VarOut2 = VarRec(II+1)` (357)를 대입한다. `elseif( iOp == MPI_MIN )then` (361)은 iMin=0과 `VarOp = 1.e32` (364), `II = (i-1)*2 + 1` (366), `if( VarOp > VarRec(II) )then` (367)일 때 값·iMin을 갱신하고(368–369) `VarOut2 = VarRec(II+1)` (370)를 대입한다. `elseif( iOp == MPI_PROD )then` (374)은 `VarOp = 1._8` (376), `II = (i-1)*2 + 1` (378), `VarOp = VarOp * VarRec(II)` (379). 각 연산은 프로세서 1..num_Processors를 순회한다(343·352·365·377). master 조건 밖에서 `Broadcast_Scalar(VarOp, master_id)`를 호출하고 VarOut1에 복사한다(385–387). `ElapsedTime = DSTIME(0) - TTDS` (389). 315행 조건의 else는 두 입력 복사·시간 0 설정(390–394). 조건·루틴·모듈 종료와 빈 줄(395–399). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–16: 상수 설명 주석은 MPI_MIN과 MPI_SUM에 같은 16진수 0x58000003을 적는다. 실행문은 MPI 모듈의 기호 상수를 사용한다(230·251·340·361).
- 55–68·89–102·122–135·156–170·205–214·315–324: 다중 프로세서 경로에서 iWait=0이면 WaitTime에 대입하는 문장이 없다. WaitTime은 각 루틴에서 intent(out)이다.
- 227–277·337–387: 두 입력 루틴은 VarOut2를 모든 프로세서에서 0으로 설정한다. 극값에 대응하는 식별자 대입은 master 조건 안에 있다. Broadcast_Scalar 호출의 인수는 VarOp뿐이다.
- 223·247·260·333·357·370: 정수 식별자를 실수 송신 배열에 변환하여 넣는다. 극값 선택 뒤 실수 수신 배열의 식별자 성분을 정수 VarOut2에 대입한다.
- 230–272·340–382: 연산 분기는 SUM·MAX·MIN·PROD만 포함한다. 나머지 iOp에 대한 else나 VarOp 초기화 문장은 이 분기 밖에 없다.
- 241·244·254·257·351·354·364·367: 최대·최소 연산의 시작값은 각각 -1.e32·1.e32이다. 극값 갱신 조건은 엄격한 부등호이다.
- 198·240·246·253·259·308·350·356·363·369: j·k·L은 선언 이후 사용되지 않는다. iMax·iMin은 초기화와 갱신 이후 다른 실행문에서 참조되지 않는다.
