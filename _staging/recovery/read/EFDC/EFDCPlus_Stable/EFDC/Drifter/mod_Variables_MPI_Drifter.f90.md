---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Drifter/mod_Variables_MPI_Drifter.f90
lines: 64
sha256: 5b368469fb7122cc45f067189e4d2571fb26ce17de4bbf8a8fd944a95986bdc3
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_Variables_MPI_Drifter.f90 — 판독 구간 기록

구간은 1행부터 64행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | EFDC+ 안내와 DSI 저작권·GPLv2 머리말을 포함한다(1–8). 표류자(drifter) 루틴의 영역 분할(domain decomposition)용 새 변수를 보관한다는 설명이다(9). 작성자 Zander Mausolff와 날짜 문자열 9/4/0219 및 빈 줄을 적는다(10–12). |
| 13–33 | Variables_MPI_Drifter 모듈을 시작하고 GLOBAL·implicit none을 사용한다(13–17). 할당 가능한 논리 마스크(logical mask) mask_lla(:)와 송신 합계 local_tot_drifters_send를 선언한다(19–21). 서브도메인(subdomain)의 수신 여부에 관한 주석 뒤 동서남북 송신 개수 send_east·send_west·send_north·send_south와 수신 개수 recv_east·recv_west·recv_north·recv_south를 정수로 선언한다(23–32). 선언에는 초기값이 없다. |
| 34–42 | 시작 시 13행 Variables_MPI_Drifter 모듈 안. 할당 가능한 정수 배열 LLA_Process(:)를 선언한다(34). 방향별 송신 개수 num_drifters_send_west·east·north·south와 프로세스 전체 통신 대상 최대 개수 global_max_drifters_to_comm을 선언한다(36–41). 빈 줄도 포함한다(35·40·42). 초기값·배열 크기 확정·실행식은 없다. |
| 43–56 | 시작 시 13행 Variables_MPI_Drifter 모듈 안. 방향별 표류자 ID 송신 배열 drifter_ids_send_west·east·north·south를 할당 가능한 1차원 정수 배열로 선언한다(43–48). 현재 영역에서 해당 방향 서브도메인으로 보낸다는 주석을 포함한다(43–45). 대응 수신 ID 배열 네 개와 전체 영역 대응 배열 gl_drift_mapping(:)을 선언한다(50–55). 빈 줄을 포함하며 이 구간에는 할당·값 대입문이 없다. |
| 57–64 | 시작 시 13행 Variables_MPI_Drifter 모듈 안. 입력 파일에서 읽은 전체 영역 자료라는 주석이 있다(57). LA_BEGTI_Global(:)·LA_ENDTI_Global(:)는 real(RKD), save, allocatable이다(58–59). LLA_Global(:)는 할당 가능한 정수 배열이고 LA_GRP_Global(:)는 정수·save·allocatable이다(60–61). 빈 줄과 마지막 모듈 종료문을 포함한다(62–64). 조건·계산식·루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11: 날짜 주석의 원문 문자열은 `! @date 9/4/0219`이다.
- 19–61: 개수 정수 변수의 선언에는 초기값이 없다. allocatable 배열의 선언에는 allocate나 값 대입이 없다. 이 모듈에는 contains 절이나 초기화 루틴이 없다.
