---
file: models/SWAN/raw/source_code/swan/bin/swanrun
lines: 137
sha256: a11de572c32f3122da7ef616638abc5f275a469bc3d688bf785051933f0f91af
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# swanrun — 판독 구간 기록

구간은 1행부터 137행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | POSIX 셸(POSIX shell) 진입점과 초기화 주석(1–6). 입력 이름은 비어 있다(7). MPI 프로세스 수와 OpenMP 스레드 수의 기본값은 각각 1이다(8–10). 매개변수 판독 안내와 빈 주석도 포함한다(11–15). 원문: `input=` (7); `npmpi=1` (8); `npomp=1` (9); `export OMP_NUM_THREADS=1` (10). |
| 16–29 | 인수를 두 개씩 소비하는 루프(16–28). case는 입력 파일의 basename에서 .swn을 제거하고 OpenMP 또는 MPI 수를 받는다(18–21). 알 수 없는 옵션은 사용법을 출력한 뒤 인수 없는 exit를 실행한다(22–25). 원문: `while [ $# -ge 2 ]` (16); `do` (17); `case $1 in` (18); ``-input) input=`basename $2 .swn`;;`` (19); `-omp)   npomp=$2;;` (20); `-mpi)   npmpi=$2;;` (21); `*)      echo unknown parameter: $1` (22); `echo ' Usage: swanrun -input file [-omp n \| -mpi n]'` (23); `echo` (24); `exit ;;` (25); `esac` (26); `shift 2` (27). |
| 30–42 | 입력 이름 누락 검사와 오류 출력(30–41). 빈 이름이면 exit 1을 실행한다(34–40). 원문: `if [ -z "$input" ]; then` (34); `echo` (35); `echo '***ERROR: no name SWAN input file given!'` (36); `echo` (37); `echo ' Usage: swanrun -input file [-omp n \| -mpi n]'` (38); `echo` (39); `exit 1` (40). |
| 43–61 | MPI 사용 가능 여부 안내(43–46). IFS에 콜론을 추가하고 PATH를 순회한다(47–54). 빈 경로는 현재 디렉터리로 바꾸며 mpirun의 일반 파일 존재 여부를 검사한다(49–50). MPI 프로세스 수가 1보다 크고 mpi가 비어 있으면 오류 종료한다(55–60). 원문: `IFS="${IFS= 	}"; IFS="${IFS}:"` (47); `for dir in $PATH; do` (48); `test -z "$dir" && dir=.` (49); `if test -f $dir/mpirun; then` (50); `mpi=1` (51); `break` (52); `if [ $npmpi -gt 1 -a -z "$mpi" ]; then` (55); `echo` (56); `echo "***ERROR: MPI is not available!"` (57); `echo` (58); `exit 1` (59). |
| 62–76 | machinefile 생성 안내와 조건 블록(62–71). 병렬 MPI 요청과 mpirun 발견 조건 안에서 machinefile이 일반 파일도 심볼릭 링크(symbolic link)도 아니면 localhost를 기록하고 hfc=1로 생성 사실을 표시한다(66–69). 실행 안내·빈 주석도 포함한다(72–76). 원문: `if [ $npmpi -gt 1 -a ! -z "$mpi" ]; then` (66); `if [ ! -f machinefile -a ! -h machinefile ]; then` (67); `echo "localhost" > machinefile` (68); `hfc=1` (69). |
| 77–99 | PATH 맨 앞에 현재 디렉터리를 추가하고 swan.exe 위치를 출력한다(77–80). 읽을 수 있는 입력을 INPUT으로 복사한다(81–83). OpenMP 요청 분기가 먼저 실행된다(84–86). 그 분기 불성립 시 MPI 요청 또는 mpi 발견 분기를 실행한다(87–96). 이 분기는 필요하면 which 결과를 swan.exe 링크로 만들고 orig=y를 설정한다(88–90). MPI 요청이면 mpirun으로 실행하고 그 외에는 swan.exe를 직접 실행한다(92–98). 원문: `PATH=.:$PATH` (78); `type swan.exe` (80); `if [ -r $input.swn ]; then` (81); `orig=n` (82); `cp $input.swn INPUT` (83); `if [ $npomp -gt 1 ]; then` (84); `export OMP_NUM_THREADS=$npomp` (85); `swan.exe` (86); `elif [ $npmpi -gt 1 -o ! -z "$mpi" ]; then` (87); `if [ ! -f swan.exe ]; then` (88); ``ln -s `which swan.exe` swan.exe`` (89); `orig=y` (90); `fi` (91); `if [ $npmpi -gt 1 ]; then` (92); `mpirun -np $npmpi -machinefile machinefile swan.exe` (93); `else` (94); `swan.exe` (95); `fi` (96); `else` (97); `swan.exe` (98). |
| 100–119 | 시작 시 81행 입력 가독성 참 분기 안. MPI 프로세스 수가 1보다 크면 프로세스 번호 루프에서 번호를 증가시키고 세 자리 형식으로 변환한다(100–104). PRINT와 Errfile을 입력 이름 기반 출력 파일로 옮긴다(105–110). MPI 수 조건의 else는 접미사가 없는 PRINT와 Errfile을 옮긴다(112–118). 원문: `if [ $npmpi -gt 1 ]; then` (100); `inode=0` (101); `while [ $inode -lt $npmpi ]; do` (102); `` inode=`expr $inode + 1` `` (103); `` inode=`echo $inode \| awk '{ printf "%03.0f", $0 }'` `` (104); `if [ -f PRINT-$inode ]; then` (105); `mv PRINT-$inode $input.prt-$inode` (106); `fi` (107); `if [ -r Errfile-$inode ]; then` (108); `mv Errfile-$inode $input.erf-$inode` (109); `fi` (110); `done` (111); `else` (112); `if [ -f PRINT ]; then` (113); `mv PRINT $input.prt` (114); `fi` (115); `if [ -r Errfile ]; then` (116); `mv Errfile $input.erf` (117); `fi` (118). [10-13 전수 검증 정정] |
| 120–137 | 시작 시 81행 입력 가독성 참 분기 안. ERRPTS는 .erp로 옮기고 norm_end는 출력한다(120–125). 스크립트가 만든 machinefile과 swan.exe 링크를 각각 조건부 삭제한다(126–131). INPUT을 삭제한다(132). 81행 조건의 else는 파일 부재를 출력하고 exit 1을 실행한다(133–135). 마지막 fi·주석을 포함한다(136–137). 원문: `if [ -r ERRPTS ]; then` (120); `mv ERRPTS $input.erp` (121); `fi` (122); `if [ -f norm_end ]; then` (123); `cat norm_end` (124); `fi` (125); `if [ \( -f machinefile -o -h machinefile \) -a ! -z "$hfc" ]; then` (126); `rm -f machinefile` (127); `fi` (128); `if [ -h swan.exe -a "$orig" = y ]; then` (129); `rm -f swan.exe` (130); `fi` (131); `rm -f INPUT` (132); `else` (133); `echo "file $input.swn does not exist"` (134); `exit 1` (135). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–28: 인수 판독 루프는 남은 인수가 두 개 이상일 때만 돈다. 남은 단일 인수를 별도로 검사하는 문장은 없다.
- 19·47–54·78·83·89: basename의 $2, PATH 순회 변수 $dir, 입력 복사 경로와 which 결과에는 따옴표가 없다. IFS에는 콜론을 추가한 뒤 복원하는 문장이 없다.
- 22–25·34–40: 알 수 없는 매개변수 분기의 exit에는 상태 인수가 없다. 입력 이름 누락 분기는 exit 1을 사용한다.
- 84–98·100–119: npomp>1 분기는 MPI 실행 분기보다 먼저 선택된다. 출력 이름 변경은 실행 분기와 별개로 npmpi>1을 검사한다.
- 86·93·95·98·120–132: 실행 직후 swan.exe 또는 mpirun의 종료 상태를 검사하는 문장은 없다. 이후 출력 파일 처리와 INPUT 삭제를 수행한다.
