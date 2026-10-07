---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Domain_Decomp/Read_JSON_Decomp.f90
lines: 96
sha256: 8e3b8c965aa6191a1c18c90b3bbcb3aef8bf7956225be6701e23c855896d7c9b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Read_JSON_Decomp.f90 — 판독 구간 기록

구간은 1행부터 96행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | EFDC+·저작권·GPLv2 머리말과 DECOMP.JNP의 x/y 분할 폭 판독 목적·작성자·날짜 주석(1–13). `Read_JSON_Decomp`를 시작한다(14). GLOBAL·Variables_MPI·Broadcast_Routines·fson·mod_fson_value·MPI를 사용한다(16–23). 지역 정수·MPI 오류 변수, JSON 파서(parser)의 fson_value 포인터 json_data, 길이 1024의 문자열 두 개를 선언한다(26–34). |
| 36–64 | 시작 시 14행 Read_JSON_Decomp 안. `if( process_id == master_id )then` (37)에서 `fson_parse("decomp.jnp")`를 호출하여 포인터를 연결한다(41). fson_get으로 number_i_subdomains·number_j_subdomains·number_active_subdomains를 각각 n_x_partitions·n_y_partitions·active_domains에 읽는다(43–45). i_subdomain_widths·j_subdomain_widths를 ic_decomp·jc_decomp에 읽는다(48–49). `if( sum(ic_decomp) /= IC )then` (52), `if( sum(jc_decomp) /= JC )then` (57)은 각각 폭 합과 전역 IC/JC의 불일치를 출력하고 pause·stop을 실행한다(53–55·58–60). 두 검사·master 조건 종료와 빈 줄(56–64). |
| 65–79 | 시작 시 14행 Read_JSON_Decomp 안이며 master 판독 조건 밖. `Broadcast_Scalar`를 세 번 호출하여 n_x_partitions·n_y_partitions·active_domains를 master_id에서 배포한다(66–68). `if( process_id /= master_id )then` (70)은 ic_decomp를 n_x_partitions, jc_decomp를 n_y_partitions 크기로 할당한다(72–73). 조건 밖에서 `Broadcast_Array(ic_decomp, master_id)`·`Broadcast_Array(jc_decomp, master_id)`를 호출한다(77–78). 빈 줄을 포함한다. |
| 80–96 | 시작 시 14행 Read_JSON_Decomp 안. `WriteBreak` 호출 뒤 분할 폭과 x/y 분할 수를 MPI 로그에 출력하고 다시 WriteBreak를 호출한다(81–89). 배열 출력 FORMAT 950은 `100(I5)`이다(91). FORMAT 1000도 선언한다(92). `MPI_Barrier(DSIcomm, ierr)` 호출·빈 줄·루틴 종료(94–96). 이 출력 블록에는 MPI_Write_Flag 조건이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20·26–28·34·92: 명시적으로 가져온 fson_value_count·fson_value_get, n_skip·iso·it·max_partition_size_write_out·strval·strval2, FORMAT 1000은 이 파일에서 사용되지 않는다.
- 32·41·96: json_data에 파싱 결과를 연결한다. 이 파일에는 파싱 결과를 해제하는 호출이 없다.
- 37·52–61·66–78: 폭 합 불일치 경로는 master 판독 조건 안에서 pause·stop을 실행한다. 이 루틴의 브로드캐스트(broadcast)는 그 조건 뒤에 있다. 불일치 경로에는 MPI_ABORT 호출이 없다.
