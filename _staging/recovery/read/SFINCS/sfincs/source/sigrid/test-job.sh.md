---
file: models/SFINCS/raw/source_code/sfincs/source/sigrid/test-job.sh
lines: 31
sha256: 4966fd85f43938929e01c1d0510962dcfd7d53b135419a26b0b95a412edab76e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# test-job.sh — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | `/bin/bash` shebang(1), `MODELDIR=$1` (3), `MODEL=$2` (4). 빈 줄·SGE options 주석(2·5–9·14). SGE 지시문 `#$ -S /bin/bash` (10), `#$ -cwd` (11), `#$ -q test-c7` (12), `#$ -V` (13). |
| 15–24 | `cd $SGE_O_WORKDIR` (15), 실행 명령 안내 주석·빈 줄(16–20), `echo $HOSTNAME ` (21), 빈 줄·Modules 주석(22–23), `module load singularity` (24). 21행 인수 뒤에는 원문 공백 문자가 있다. |
| 25–31 | 빈 줄(25·29·31). `echo "Running model $MODEL."` (26), `singularity run -B ${MODELDIR}/${MODEL}:/data sfincs-cpu.sif` (27), `echo finished ` (28), `exit` (30). 컨테이너에 모델 경로를 /data로 바인드한다. 28행 인수 뒤에는 원문 공백 문자가 있다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12·27: 큐 이름 test-c7, 컨테이너 파일명 sfincs-cpu.sif, 바인드 대상 /data가 고정되어 있다.
- 3–4·15·27: 두 입력 인수나 SGE_O_WORKDIR를 검사하는 조건은 없다. cd와 바인드 경로의 변수 확장에는 따옴표가 없다.
- 27–30: singularity 종료 상태를 검사하거나 저장하는 문장이 없다. 그 뒤에 echo와 인수 없는 exit가 있다.
