---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Domain_Decomp/Scan_JSON_Decomp.f90
lines: 121
sha256: ce21e3ab5e02549d1e4fad00bb53a99ebeadd2e678ce8d479e62af4f14d7b978
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Scan_JSON_Decomp.f90 — 판독 구간 기록

구간은 1행부터 121행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | EFDC+·저작권·GPLv2 머리말과 JSON 분할 파일을 스캔하여 배열 할당용 변수를 얻는 목적·작성자·날짜 주석(1–13). `Scan_JSON_Decomp`를 시작하고 GLOBAL·Variables_MPI·Broadcast_Routines·fson·mod_fson_value·MPI를 사용한다(14–23). 정수·allocatable itmp·JSON 값 포인터 세 개·길이 1024 문자열 두 개를 선언한다(26–35). 선언 기본값은 `integer :: scan_decomp_unit = 200` (29). |
| 37–67 | 시작 시 14행 Scan_JSON_Decomp 안. `if( process_id == master_id )then` (37)은 안내 출력과 `fson_parse("decomp.jnp")` 호출을 수행한다(38–41). fson_get으로 x/y 분할 수·활성 영역 수·x/y 폭 배열·active_flag 배열을 읽는다(43–52). `nelements = size(itmp)` (53). `if( nelements /= n_x_partitions*n_y_partitions )then` (56)은 개수 불일치 출력과 stop을 실행한다(57–58). 조건 밖이지만 master 분기 안에서 `max_width_x = maxval(ic_decomp, 1)` (61), `max_width_y = maxval(jc_decomp, 1)` (62), `max_width_x = max_width_x + 4` (63), `max_width_y = max_width_y + 4` (64). master 조건 종료와 빈 줄(66–67). |
| 68–92 | 시작 시 14행 Scan_JSON_Decomp 안이며 master 판독 조건 밖. 주석은 DSIcomm 초기화 전이므로 MPI_Comm_World를 사용한다고 적는다(68–69). MPI_BCAST로 n_x_partitions·n_y_partitions·active_domains·max_width_x·max_width_y를 원소 수 1·MPI_Integer·master_id·MPI_Comm_World로 배포하고 각 호출 뒤 MPI_BARRIER를 호출한다(70–83). nelements를 같은 방식으로 배포한다(85). `if( process_id /= master_id )then` (86)은 itmp(nelements)를 할당하고 0으로 초기화한다(87–88). 조건 밖에서 itmp를 nelements개 MPI_Integer로 배포한 뒤 barrier를 호출한다(90–91). |
| 93–113 | 시작 시 14행 Scan_JSON_Decomp 안. decomp_active·process_map을 두 차원 모두 `0:n_x_partitions+1`, `0:n_y_partitions+1` 범위로 할당한다(94–95). 기본 설정은 decomp_active=0, process_map=-1, it=0, nD=0이다(96–101). j=1..n_y_partitions 바깥 루프·i=1..n_x_partitions 안쪽 루프에서 `it = it + 1` (104), decomp_active(i,j)=itmp(it) 복사(105). `if( itmp(it) == 1 )then` (107)이면 process_map(i,j)에 nD를 넣고 `nD = nD + 1` (109). process_map의 활성 영역 번호는 0부터 증가한다(108). 조건·루프 종료와 빈 줄(110–113). |
| 114–121 | 시작 시 14행 Scan_JSON_Decomp 안. 일관성 검사 주석(114). `if( nD /= active_domains )then` (115)의 본문은 `! do something` 주석뿐이다(116). 조건 종료·return·빈 줄·루틴 종료(117–121). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9·38·41: 머리말은 DECOMP.inp라고 적는다. 안내 출력은 DECOMP.JNP이며 파서 호출은 decomp.jnp를 사용한다.
- 20·26–35: 명시적으로 가져온 fson_value_count·fson_value_get과 지역 변수 idim·jdim·iso·scan_decomp_unit·array·item·strval·strval2는 실행문에서 사용되지 않는다.
- 56–64·94–109: active_flag는 전체 원소 수만 검사한다. process_map 번호 부여 조건은 값이 정확히 1인 경우이다. 이 파일에는 active_flag 값이 0 또는 1인지 검사하는 분기가 없다.
- 61–64: 최대 분할 폭에 더하는 여유 폭은 두 방향 모두 하드코딩된 4이다.
- 114–117: nD와 active_domains가 다른 조건의 본문에는 실행문이 없다.
