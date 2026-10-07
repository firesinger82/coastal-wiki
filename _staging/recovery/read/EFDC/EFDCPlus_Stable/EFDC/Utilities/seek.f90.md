---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Utilities/seek.f90
lines: 68
sha256: 352ee1478c2cb6d285ce1ff5d3a0898a44f349e98405eec1deedd4d18c76cc4d
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# seek.f90 — 판독 구간 기록

구간은 1행부터 68행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | EFDC+·GPLv2 머리말(1–8). SEEK 입구·GLOBAL의 IKV/CARDNO·Variables_MPI 사용·implicit none(9–14). 입력 ISKIP과 입출력 TAG, 지역 정수·길이 120 TEXT·OPN/ECHO 선언·빈 줄(16–22). |
| 23–37 | 시작 시 9행 SEEK 안. ECHO=.TRUE.(23), `if( ISKIP > 0 ) ECHO = .FALSE.` (24). CARDNO에 TAG를 복사하고 mpi_efdc_out_unit의 열린 상태를 조회한다(26–27). `L = LEN(TAG)` (29), I=1:L 루프(30)에서 `J = ICHAR(TAG(I:I))` (31). `if( 97 <= J .and. J <= 122 )then` (32)은 `TAG(I:I) = CHAR(J-32)` (33). `if( OPN ) WRITE(mpi_efdc_out_unit,'(A,A)')'SEEKING GROUP: ',TAG` (36). |
| 38–57 | 시작 시 9행 SEEK 안. `do K = 1,2` (38)에서 레이블 10의 UNIT 1 read가 END=20을 지정한다(39). `M = max(1,LEN_TRIM(TEXT))` (40), `if( OPN .and. ECHO ) WRITE(mpi_efdc_out_unit,'(A)') TEXT(1:M)` (41). `do while( M > L .and. TEXT(1:1) == '' )` (42)은 왼쪽으로 문자열을 옮기고 끝 문자를 공백으로 설정한다(43–44). `M = M-1` (45). `if( M < L )GO TO 10` (47). I=1:M 루프(48)의 `J = ICHAR(TEXT(I:I))` (49), `if( 97 <= J .and. J <= 122 )then` (50), `TEXT(I:I) = CHAR(J-32)` (51)로 대문자화한다. `if( TEXT(1:L) /= TAG )     GO TO 10` (54), `if( TEXT(L+1:L+1) /= ' ' ) GO TO 10` (55). 루프 종료·빈 줄(56–57). |
| 58–68 | 시작 시 9행 SEEK 안이며 두 번 검색하는 K 루프 밖. 정상 return(58). 파일 끝 레이블 20은 표준 출력과 mpi_error_file에 그룹 미발견 메시지를 쓴다(60–61). PAUSE(63), `call STOPP('.')` (65), 빈 줄·루틴 종료(66–68). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26·29–35: CARDNO에 TAG를 복사한 뒤 TAG 자체를 대문자로 바꾼다.
- 38–56: 검색 루프는 K=1,2이다. 두 번째 검색 전에 rewind·backspace하는 실행문은 없다.
- 20·29·54–55: TEXT는 길이 120이고 L은 LEN(TAG)이다. TEXT(1:L)·TEXT(L+1:L+1) 참조 앞에 L의 상한을 확인하는 조건은 없다.
- 11: 가져온 IKV는 이 파일의 다른 선언·실행문에서 사용되지 않는다.
