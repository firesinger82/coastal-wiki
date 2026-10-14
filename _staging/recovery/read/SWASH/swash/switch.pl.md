---
file: models/SWASH/raw/source_code/swash/switch.pl
lines: 73
sha256: ac742991c0ff2202af855d9d18e0baabf4d53f97552a8c2fe5103cf1a07425bb
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# switch.pl — 판독 구간 기록

구간은 1행부터 73행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | 인수 처리 주석(1), `$tim = "FALSE";` (2), `$mpi = "FALSE";` (3), `$f95 = "FALSE";` (4), `$dos = "FALSE";` (5), `$unx = "FALSE";` (6), `$cry = "FALSE";` (7), `$sgi = "FALSE";` (8), `$imp = "FALSE";` (9), `$cvi = "FALSE";` (10), `$mv4 = "FALSE";` (11)로 모든 스위치 기본값 설정. `while ( $ARGV[0]=~/-.*/ )` (12) 안에서 `if ($ARGV[0]=~/-timg/) {$tim="TRUE";shift;}` (14), `if ($ARGV[0]=~/-mpi/) {$mpi="TRUE";shift;}` (15), `if ($ARGV[0]=~/-f95/) {$f95="TRUE";shift;}` (16), `if ($ARGV[0]=~/-dos/) {$dos="TRUE";shift;}` (17), `if ($ARGV[0]=~/-unix/) {$unx="TRUE";shift;}` (18), `if ($ARGV[0]=~/-cray/) {$cry="TRUE";shift;}` (19), `if ($ARGV[0]=~/-sgi/) {$sgi="TRUE";shift;}` (20), `if ($ARGV[0]=~/-impi/) {$imp="TRUE";shift;}` (21), `if ($ARGV[0]=~/-cvis/) {$cvi="TRUE";shift;}` (22), `if ($ARGV[0]=~/-matl4/) {$mv4="TRUE";shift;}` (23)를 순서대로 평가. 일치한 조건은 플래그를 TRUE로 바꾸고 선두 인수를 제거한다. 루프 종료·빈 줄(24–25). |
| 26–31 | 파일 목록 구성 주석(26), `@files = ();` (27). 남은 인수에 대해 `foreach (@ARGV) {` (28), `@files = (@files , glob );` (29)로 파일명 패턴 확장(glob) 결과를 누적한다. 루프 종료·빈 줄(30–31). |
| 32–47 | 파일 변환 주석과 `foreach $file (@files)` (32–34). 출력 이름 결정은 `if ($unx=~/TRUE/)` (36)이며 참 분기는 `($tempf)=split(/.ftn/, $file);` (38), `$ext = ($file =~ m/ftn90/) ? "f90" : "f";` (39), `$outfile = join(".",$tempf,$ext);` (40). `else` (42)는 `($tempf)=split(/.ftn/, $file);` (44), `$ext = ($file =~ m/ftn90/) ? "f90" : "for";` (45), `$outfile = join(".",$tempf,$ext);` (46). `-unix`가 있으면 ftn90은 f90, 그 밖은 f이며, 기본 분기는 f90 또는 for이다. 조건 종료(47); 파일 루프는 계속된다. |
| 48–56 | 시작 시 `foreach $file (@files)` (33)의 루프 안이며 73행에서 닫힌다. 처리 조건은 `if (   (! -e $outfile)            #outfile doesn't exist` (49); `\|\| (-M $file < -M $outfile) ) #.ftn file recently modified` (50)의 연속 두 행이다. 출력이 없거나 입력 수정 시각이 더 최근일 때 `open file or die "can't open $file\n";` (52), `open(OUTFILE,">".$outfile);` (53)로 입력과 출력 파일을 연다. `while ($line=<file>)` (54)에서 줄을 읽고 `$newline=$line;` (56)으로 복사한다. 여는 중괄호·처리 주석도 포함(48·51·55). 변환 조건은 ELSE 없이 72행에서 닫힌다. 입력 줄 루프는 69행에서 닫힌다. [10-15 전수 검증 보완] |
| 57–69 | 시작 시 `foreach $file (@files)` (33)의 루프 안이며 73행에서 닫힌다. 바깥 변환 조건은 `if (   (! -e $outfile)            #outfile doesn't exist` (49); `\|\| (-M $file < -M $outfile) ) #.ftn file recently modified` (50)이며 ELSE 없이 72행에서 닫힌다. 바깥 입력 줄 루프는 `while ($line=<file>)` (54)이며 69행에서 닫힌다. 행 첫머리 표시 제거 규칙은 `if ($tim=~/TRUE/) {$newline=~s/^!TIMG//;}` (57), `if ($mpi=~/TRUE/) {$newline=~s/^!MPI//;}` (58), `if ($f95=~/TRUE/) {$newline=~s/^!F95//;}` (59), `if ($dos=~/TRUE/) {$newline=~s/^!DOS//;}` (60), `if ($unx=~/TRUE/) {$newline=~s/^!UNIX//;}` (61), `if ($cry=~/TRUE/) {$newline=~s/^!\/Cray//;}` (62), `if ($sgi=~/TRUE/) {$newline=~s/^!\/SGI//;}` (63), `if ($imp=~/TRUE/) {$newline=~s/^!\/impi//;}` (64), `if ($cvi=~/TRUE/) {$newline=~s/^!CVIS//;}` (65), `if ($mv4=~/TRUE/) {$newline=~s/^!MatL4//;}` (66)이다. 각각 -timg·-mpi·-f95·-dos·-unix·-cray·-sgi·-impi·-cvis·-matl4에서 해당 표시를 지운다. 66행에 붙은 `else              {$newline=~s/^!MatL5//;}` (67)는 -matl4가 없을 때 MatL5 표시를 지운다. !DIFF·!MUD·!TEST·!VEGE 제거 규칙은 이 목록에 없으므로 그 표시가 붙은 Fortran 행은 주석으로 남는다. `print OUTFILE $newline;` (68)로 변환 줄을 쓰고 줄 루프를 끝낸다(69). [10-15 전수 검증 보완] |
| 70–73 | 시작 시 `foreach $file (@files)` (33)의 루프 안이다. 바깥 변환 조건은 `if (   (! -e $outfile)            #outfile doesn't exist` (49); `\|\| (-M $file < -M $outfile) ) #.ftn file recently modified` (50)이다. `while ($line=<file>)` (54)의 입력 줄 루프는 69행에서 닫혔다. `close file;` (70), `close(OUTFILE);` (71)로 파일을 닫는다. 변환 조건 종료(72), 파일 루프 종료(73). [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–24: 옵션 조건은 서로 독립된 if이며 일치한 if마다 shift한다. 열거된 옵션과 일치하지 않는 하이픈 포함 선두 인수를 제거하는 문장은 이 루프에 없다.
- 14–23·38–45: 옵션 정규식에는 시작·끝 앵커가 없다. 파일명 split의 `/.ftn/`에서 점은 이스케이프하지 않았다.
- 49–50: 변환 실행 조건은 출력 파일 존재 여부와 입력·출력 수정 시각만 검사한다. 선택한 스위치의 변경 여부는 이 조건에 없다.
- 52–53: 입력 open에는 실패 시 die가 붙어 있다. 출력 open의 반환값을 검사하는 문장은 없다.
- 66–67: MatL5 제거는 MatL4 조건의 else에서 수행한다. -matl4가 없으면 다른 스위치의 상태와 관계없이 MatL5 표시를 지운다.
