---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Communication/Mod_SEND_RECV.f90
lines: 130
sha256: 2888e2a902c0e8e217d2ae14e2a11c0c861a6fb097d0d95df8884def567c5a91
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Mod_SEND_RECV.f90 — 판독 구간 기록

구간은 1행부터 130행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | EFDC+ 웹사이트·저장소, DSI의 2021–2024 저작권, GNU GPLv2 머리말(1–8). 정밀도(precision)를 자동으로 처리하는 MPI 송수신이라는 설명과 작성자 Paul M. Craig·날짜 2021-06-21 및 빈 줄(9–12). |
| 13–47 | `Mod_DSI_SendRecv` 모듈 시작(13). GLOBAL·MPI·Variables_MPI 사용, implicit none·save(15–21). 공개 DSI_SEND 제네릭 인터페이스(generic interface)는 Integer·Real4·Real8 송신 루틴을 연결한다(23–32). 공개 DSI_RECV 인터페이스는 같은 세 자료형의 수신 루틴을 연결한다(34–41). 43행 주석은 MPI_SEND·MPI_RECV가 반환하는 STATUS를 송수신 바이트 수라고 설명한다. contains와 빈 줄(45–47). |
| 48–60 | 시작 시 13행 Mod_DSI_SendRecv 모듈 안. `DSI_SEND_Integer`는 assumed-size 정수 입력 ValIn(*)과 정수 iLen·iDir 및 지역 IERR·status_message를 선언한다(48–52). `if( num_Processors > 1 )then` (54)이면 IERR를 0으로 설정하고 `call MPI_SEND(ValIn, iLen, mpi_integer, iDir, process_id, DSIcomm, IERR)` (56)를 호출한다. 송신 개수는 iLen, 목적지는 iDir, 태그(tag)는 process_id이다. 분기·루틴 종료·빈 줄(57–60). |
| 61–73 | 시작 시 13행 Mod_DSI_SendRecv 모듈 안. `DSI_SEND_Real4`는 real(4) ValIn(*)과 정수 iLen·iDir·IERR를 선언한다(61–65). `if( num_Processors > 1 )then` (67)이면 IERR를 0으로 설정하고 `call MPI_SEND(ValIn, iLen, mpi_real4, iDir, process_id, DSIcomm, IERR)` (69)를 호출한다. 송신 개수는 iLen, 목적지는 iDir, 태그는 process_id이다. 분기·루틴 종료·빈 줄(70–73). |
| 74–89 | 시작 시 13행 Mod_DSI_SendRecv 모듈 안. `DSI_SEND_Real8`은 real(8) ValIn(*)과 정수 iLen·iDir·IERR를 선언한다(74–78). `if( num_Processors > 1 )then` (80)이면 IERR를 0으로 설정하고 `call MPI_SEND(ValIn, iLen, mpi_real8, iDir, process_id, DSIcomm, IERR)` (82)를 호출한다. 송신 개수는 iLen, 목적지는 iDir, 태그는 process_id이다. 분기·루틴 종료(83–85). 구분 주석·송신에 관한 details 주석·빈 줄(86–89). |
| 90–102 | 시작 시 13행 Mod_DSI_SendRecv 모듈 안. `DSI_RECV_Integer`는 intent(out) 정수 Valout(*)과 정수 iLen·iDir 및 IERR·status_message(MPI_Status_Size)를 선언한다(90–94). `if( num_Processors > 1 )then` (96)이면 IERR를 0으로 설정하고 `call MPI_RECV(Valout, iLen, mpi_integer, iDir, iDir, DSIcomm, status_message, IERR)` (98)를 호출한다. 수신 개수는 iLen이고 발신 프로세스(process)와 태그는 모두 iDir이다. 분기·루틴 종료·빈 줄(99–102). |
| 103–115 | 시작 시 13행 Mod_DSI_SendRecv 모듈 안. `DSI_RECV_Real4`는 intent(out) real(4) Valout(*)과 정수 iLen·iDir 및 IERR·status_message(MPI_Status_Size)를 선언한다(103–107). `if( num_Processors > 1 )then` (109)이면 IERR를 0으로 설정하고 `call MPI_RECV(Valout, iLen, mpi_real4, iDir, iDir, DSIcomm, status_message, IERR)` (111)를 호출한다. 수신 개수는 iLen이고 발신 프로세스와 태그는 모두 iDir이다. 분기·루틴 종료·빈 줄(112–115). |
| 116–128 | 시작 시 13행 Mod_DSI_SendRecv 모듈 안. `DSI_RECV_Real8`은 intent(out) real(8) Valout(*)과 정수 iLen·iDir 및 IERR·status_message(MPI_Status_Size)를 선언한다(116–120). `if( num_Processors > 1 )then` (122)이면 IERR를 0으로 설정하고 `call MPI_RECV(Valout, iLen, mpi_real8, iDir, iDir, DSIcomm, status_message, IERR)` (124)를 호출한다. 수신 개수는 iLen이고 발신 프로세스와 태그는 모두 iDir이다. 분기·루틴 종료·빈 줄(125–128). |
| 129–130 | 시작 시 13행 Mod_DSI_SendRecv 모듈 안. 모듈 종료와 마지막 공백 행(129–130). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 43·52·56: 43행 주석은 MPI_SEND·MPI_RECV의 STATUS를 설명한다. DSI_SEND_Integer의 MPI_SEND 호출에는 status_message 인수가 없다. 52행에서 선언한 status_message는 해당 루틴에서 사용하지 않는다.
- 94·98·107·111·120·124: 세 수신 루틴은 status_message를 MPI_RECV에 전달한다. 해당 호출 뒤에는 status_message를 검사하는 실행문이 없다.
- 55–57·68–70·81–83·97–99·110–112·123–125: 여섯 루틴은 MPI 호출 전에 IERR를 0으로 설정한다. MPI 호출 뒤에는 IERR에 따른 조건 분기가 없다.
- 92–101·105–114·118–127: 세 수신 루틴의 Valout은 intent(out)이다. num_Processors가 1 이하일 때 실행되는 Valout 대입문은 이 루틴들에 없다.
