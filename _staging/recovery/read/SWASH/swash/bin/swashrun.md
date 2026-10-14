---
file: models/SWASH/raw/source_code/swash/bin/swashrun
lines: 137
sha256: 8b99acbe906c0078f17c71b67befda89be30097696223f9e0026c9d42adce340
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# swashrun — 판독 구간 기록

구간은 1행부터 137행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `#!/bin/sh` (1)로 셸을 지정한다. 초기화 구분 주석(2–6) 뒤 `input=` (7)로 input을 비운다. `npmpi=1` (8)과 `npomp=1` (9)로 병렬 실행 수의 기본값을 설정한다. `export OMP_NUM_THREADS=1` (10)은 OpenMP 스레드(thread) 기본값을 1로 내보낸다. 인수 판독 구분 주석(11–15)이 이어진다. [10-15 전수 검증 보완] |
| 16–28 | `while [ $# -ge 2 ]` (16)와 `case $1 in` (18)으로 두 인수씩 처리한다. ``-input) input=`basename $2 .sws`;;`` (19)은 경로와 .sws 접미사를 제거한다. `-omp)   npomp=$2;;` (20), `-mpi)   npmpi=$2;;` (21)은 병렬 실행 수를 받는다. `*)      echo unknown parameter: $1` (22), `echo ' Usage: swashrun -input file [-omp n \| -mpi n]'` (23), `echo` (24), `exit ;;` (25)은 알 수 없는 옵션 처리다. `shift 2` (27) 뒤 루프를 닫는다(28). |
| 29–60 | 주석(29–33) 뒤 `if [ -z "$input" ]; then` (34)이면 `echo` (35·37·39), `echo '***ERROR: no name SWASH input file given!'` (36), `echo ' Usage: swashrun -input file [-omp n \| -mpi n]'` (38)로 오류와 사용법을 출력한다. 이어 `exit 1` (40)을 실행한다. 이 분기는 `fi` (41)로 닫힌다. MPI(Message Passing Interface) 검사 주석(42–46) 뒤 `IFS="${IFS= 	}"; IFS="${IFS}:"` (47), `for dir in $PATH; do` (48), `test -z "$dir" && dir=.` (49)로 검색 경로를 순회한다. `if test -f $dir/mpirun; then` (50)이면 `mpi=1` (51)을 설정한다. 이어 `break` (52)로 반복을 벗어난다. 이 분기는 `fi` (53)로 닫힌다. PATH 반복은 `done` (54)으로 닫힌다. `if [ $npmpi -gt 1 -a -z "$mpi" ]; then` (55)이면 `echo` (56·58)와 `echo "***ERROR: MPI is not available!"` (57)로 오류를 출력한다. 이어 `exit 1` (59)을 실행한다. 이 분기는 `fi` (60)로 닫힌다. [10-15 전수 검증 보완] |
| 61–80 | 머신 목록(machinefile) 생성 주석(61–65). `if [ $npmpi -gt 1 -a ! -z "$mpi" ]; then` (66) 안의 `if [ ! -f machinefile -a ! -h machinefile ]; then` (67)이면 `echo "localhost" > machinefile` (68)을 실행하고 `hfc=1` (69)을 둔다. 분기 종료(70–71) 뒤 실행 주석(72–77), `PATH=.:$PATH` (78), 빈 줄(79), `type swash.exe` (80)로 현재 디렉터리 실행파일을 우선 탐색한다. [10-15 전수 검증 보완] |
| 81–99 | `if [ -r $input.sws ]; then` (81)이면 `orig=n` (82), `cp $input.sws INPUT` (83)이다. `if [ $npomp -gt 1 ]; then` (84)은 `export OMP_NUM_THREADS=$npomp` (85), `swash.exe` (86)을 실행한다. `elif [ $npmpi -gt 1 -o ! -z "$mpi" ]; then` (87) 안의 `if [ ! -f swash.exe ]; then` (88)은 ``ln -s `which swash.exe` swash.exe`` (89)와 `orig=y` (90)이다. 88행 조건은 `fi` (91)로 닫힌다. 이어 `if [ $npmpi -gt 1 ]; then` (92)은 `mpirun -np $npmpi -machinefile machinefile swash.exe` (93), `else` (94)는 `swash.exe` (95)이다. 92행 조건은 `fi` (96)로 닫힌다. 84행 분기의 `else` (97)도 `swash.exe` (98)을 실행한다. 84행 분기 사슬은 `fi` (99)로 닫힌다. [10-15 전수 검증 보완] |
| 100–119 | 시작 시 `if [ -r $input.sws ]; then` (81)의 참 분기 안이다. 이 바깥 분기의 `else`는 133행이다. 바깥 분기는 `fi` (136)로 닫힌다. `if [ $npmpi -gt 1 ]; then` (100)은 `inode=0` (101) 뒤 `while [ $inode -lt $npmpi ]; do` (102)로 프로세스별 출력을 처리한다. ``inode=`expr $inode + 1` `` (103), ``inode=`echo $inode \| awk '{ printf "%03.0f", $0 }'` `` (104)로 번호를 증가시키고 세 자리로 만든다. `if [ -f PRINT-$inode ]; then` (105)은 `mv PRINT-$inode $input.prt-$inode` (106), `if [ -r Errfile-$inode ]; then` (108)은 `mv Errfile-$inode $input.erf-$inode` (109)이다. 루프 종료(111) 뒤 `else` (112)에서 `if [ -f PRINT ]; then` (113)은 `mv PRINT $input.prt` (114), `if [ -r Errfile ]; then` (116)은 `mv Errfile $input.erf` (117)이다. 100행 조건은 `fi` (119)로 닫힌다. [10-15 전수 검증 보완] |
| 120–137 | 120–132행은 `if [ -r $input.sws ]; then` (81)의 참 분기 안이다. 이 바깥 분기의 `else`는 133행이다. 바깥 분기는 `fi` (136)로 닫힌다. `if [ -r ERRPTS ]; then` (120)은 `mv ERRPTS $input.erp` (121), `if [ -f norm_end ]; then` (123)은 `cat norm_end` (124)이다. `if [ \( -f machinefile -o -h machinefile \) -a ! -z "$hfc" ]; then` (126)은 `rm -f machinefile` (127)이다. `if [ -h swash.exe -a "$orig" = y ]; then` (129)은 `rm -f swash.exe` (130)이다. `rm -f INPUT` (132) 뒤 81행 분기의 `else` (133)는 `echo "file $input.sws does not exist"` (134), `exit 1` (135)이다. 분기 종료와 마지막 주석(136–137). [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–28: 인수 판독 루프는 남은 인수가 2개 이상일 때만 실행한다. 마지막에 남은 인수 1개를 별도로 검사하는 문장은 없다.
- 19·81·83: -input 값에는 basename을 적용한다. 입력파일 검사와 복사는 현재 디렉터리의 `$input.sws`를 대상으로 한다.
- 84–100: OpenMP 분기는 MPI 분기보다 먼저 선택한다. 실행 후 출력 처리 분기는 npmpi만 검사한다.
- 86·93·95·98·100–132: 실행파일 호출의 종료 상태를 검사하는 조건은 없다. 호출 이후 출력 이동과 정리 명령이 이어진다.
