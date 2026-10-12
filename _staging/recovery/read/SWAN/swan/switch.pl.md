---
file: models/SWAN/raw/source_code/swan/switch.pl
lines: 111
sha256: b4b0eab4cc5c8a2dfc170e3d5c52bea1040d9a73bae3bc3361c11af1ab00ac9e
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# switch.pl — 판독 구간 기록

구간은 1행부터 111행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 인수 판독 머리말(1). 스위치 기본값은 `$esmf = "FALSE";` (2), `$tim = "FALSE";` (3), `$jac = "FALSE";` (4), `$ffro = "FALSE";` (5), `$mpi = "FALSE";` (6), `$f95 = "FALSE";` (7), `$dos = "FALSE";` (8), `$unx = "FALSE";` (9), `$cry = "FALSE";` (10), `$sgi = "FALSE";` (11), `$imp = "FALSE";` (12), `$cvi = "FALSE";` (13), `$adc = "FALSE";` (14), `$coh = "FALSE";` (15), `$met = "FALSE";` (16), `$ncf = "FALSE";` (17), `$mv4 = "FALSE";` (18). |
| 19–39 | `while ( $ARGV[0]=~/-.*/ )` (19)에서 맨 앞 인수를 검사한다. 실행문은 `if ($ARGV[0]=~/-esmf/) {$esmf="TRUE";shift;}` (21), `if ($ARGV[0]=~/-timg/) {$tim="TRUE";shift;}` (22), `if ($ARGV[0]=~/-jac/) {$jac="TRUE";shift;}` (23), `if ($ARGV[0]=~/-fixfront/) {$ffro="TRUE";shift;}` (24), `if ($ARGV[0]=~/-mpi/) {$mpi="TRUE";shift;}` (25), `if ($ARGV[0]=~/-f95/) {$f95="TRUE";shift;}` (26), `if ($ARGV[0]=~/-dos/) {$dos="TRUE";shift;}` (27), `if ($ARGV[0]=~/-unix/) {$unx="TRUE";shift;}` (28), `if ($ARGV[0]=~/-cray/) {$cry="TRUE";shift;}` (29), `if ($ARGV[0]=~/-sgi/) {$sgi="TRUE";shift;}` (30), `if ($ARGV[0]=~/-impi/) {$imp="TRUE";shift;}` (31), `if ($ARGV[0]=~/-cvis/) {$cvi="TRUE";shift;}` (32), `if ($ARGV[0]=~/-adcirc/) {$adc="TRUE";shift;}` (33), `if ($ARGV[0]=~/-coh/) {$coh="TRUE";shift;}` (34), `if ($ARGV[0]=~/-metis/) {$met="TRUE";shift;}` (35), `if ($ARGV[0]=~/-netcdf/) {$ncf="TRUE";shift;}` (36), `if ($ARGV[0]=~/-matl4/) {$mv4="TRUE";shift;}` (37). 각 if는 독립 검사이며 일치할 때 현재 첫 인수를 제거한다. 루프 종료와 빈 줄(38–39). |
| 40–49 | 미지원 조합 검사 주석(40). `if ($esmf=~/TRUE/ && $adc=~/TRUE/)` (41)이면 `die "$0: -esmf and -adcirc is not supported.\n";` (43)로 종료한다. 별도 `if ($esmf=~/TRUE/ && $met=~/TRUE/)` (45)이면 `die "$0: -esmf and -metis is not supported.\n";` (47)로 종료한다. 괄호·빈 줄도 포함(42·44·46·48–49). |
| 50–56 | 파일 목록 구성 주석(50). `@files = ();` (51)로 비운다. `foreach (@ARGV) {` (52)에서 `@files = (@files , glob );` (53)로 남은 인수의 파일 패턴을 확장한다. 루프 종료·빈 줄·파일 처리 주석(54–56). |
| 57–71 | `foreach $file (@files)` (57)에서 출력 이름을 만든다. `if ($unx=~/TRUE/)` (60) 안에서는 `($tempf)=split(/.ftn/, $file);` (62), `$ext = ($file =~ m/ftn90/) ? "f90" : "f";` (63), `$outfile = join(".",$tempf,$ext);` (64). `else` (66) 안에서는 `($tempf)=split(/.ftn/, $file);` (68), `$ext = ($file =~ m/ftn90/) ? "f90" : "for";` (69), `$outfile = join(".",$tempf,$ext);` (70). -unix 선택 시 고정 형식(fixed form)은 .f, 그 외에는 .for이며 ftn90은 양쪽 모두 .f90이다. 이름 분기 종료(71). |
| 72–81 | 시작 시 57행 파일 루프 안. 처리 조건은 `if (   (! -e $outfile)            #outfile doesn't exist` (73), `\|\| (-M $file < -M $outfile) ) #.ftn file recently modified` (74). 출력이 없거나 원본이 더 최근이면 `open file or die "can't open $file\n";` (76), `open(OUTFILE,">".$outfile);` (77)를 실행한다. `while ($line=<file>)` (78)에서 `$newline=$line;` (80)로 행을 복사한다. ESMF를 먼저 처리한다는 주석(81). |
| 82–92 | 시작 시 57행 파일 루프·73–74행 재생성 참 분기·78행 행 판독 루프 안. `if ($esmf=~/TRUE/) {$newline=~s/^!ESMF//;}` (82), `else               {$newline=~s/^!!ESMF//;} #second "!" is negation` (83): -esmf는 !ESMF, 미선택은 !!ESMF를 먼저 제거한다. `if ($tim=~/TRUE/) {$newline=~s/^!TIMG//;}` (84)는 -timg에서 !TIMG를 제거한다. `if ($jac=~/TRUE/) {$newline=~s/^!JAC//;}` (85), `else              {$newline=~s/^!WFR//;}` (86): -jac는 !JAC, 미선택은 !WFR. `if ($ffro=~/TRUE/) {$newline=~s/^!FXFRO//;}` (87), `else               {$newline=~s/^!GRAPH//;}` (88): -fixfront는 !FXFRO, 미선택은 !GRAPH. `if ($mpi=~/TRUE/) {$newline=~s/^!MPI//;}` (89), `if ($f95=~/TRUE/) {$newline=~s/^!F95//;}` (90), `if ($dos=~/TRUE/) {$newline=~s/^!DOS//;}` (91), `if ($unx=~/TRUE/) {$newline=~s/^!UNIX//;}` (92)는 각각 -mpi·-f95·-dos·-unix에서 해당 행 첫머리 표시를 제거한다. |
| 93–105 | 시작 시 57행 파일 루프·73–74행 재생성 참 분기·78행 행 판독 루프 안. `if ($cry=~/TRUE/) {$newline=~s/^!\/Cray//;}` (93), `if ($sgi=~/TRUE/) {$newline=~s/^!\/SGI//;}` (94), `if ($imp=~/TRUE/) {$newline=~s/^!\/impi//;}` (95), `if ($cvi=~/TRUE/) {$newline=~s/^!CVIS//;}` (96)는 각각 -cray·-sgi·-impi·-cvis에서 해당 표시를 제거한다. `if ($adc=~/TRUE/) {$newline=~s/^!ADC//;}` (97), `if ($adc=~/FALSE/) {$newline=~s/^!NADC//;}` (98)는 -adcirc 선택/미선택의 쌍이다. `if ($coh=~/TRUE/) {$newline=~s/^!COH//;}` (99), `if ($coh=~/FALSE/){$newline=~s/^!NCOH//;}` (100)는 -coh 선택/미선택의 쌍이다. `if ($met=~/TRUE/) {$newline=~s/^!METIS//;}` (101)는 -metis. `if ($ncf=~/TRUE/) {$newline=~s/^!NCF//;}` (102), `if ($ncf=~/FALSE/){$newline=~s/^!NNCF//;}` (103)는 -netcdf 선택/미선택의 쌍이다. `if ($mv4=~/TRUE/) {$newline=~s/^!MatL4//;}` (104), `if ($mv4=~/FALSE/) {$newline=~s/^!MatL5//;}` (105)는 -matl4 선택/미선택의 쌍이다. |
| 106–111 | 시작 시 57행 파일 루프·73–74행 재생성 참 분기·78행 행 판독 루프 안. `print OUTFILE $newline;` (106)로 변환 행을 쓴다. 행 루프 종료(107) 후 `close file;` (108), `close(OUTFILE);` (109)를 실행한다. 재생성 조건과 파일 루프 종료(110–111). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–38: 인수 제거는 열거된 if의 참 분기에서만 수행한다. 어떤 스위치에도 일치하지 않는 대시 포함 첫 인수를 제거하거나 오류로 종료하는 분기는 없다.
- 62·68: 출력 이름 분리에 쓰는 정규식은 `/.ftn/`이다. 점을 이스케이프하지 않는다.
- 73–74: 재생성 조건은 출력 존재 여부와 파일 수정 시간만 검사한다. 스위치 조합의 변경 여부는 검사하지 않는다.
- 76–77: 입력 open에는 실패 시 die가 있다. 출력 open에는 반환값 검사나 die가 없다.
