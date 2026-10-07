---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/Unit_Testing/Running_EFDC_with_MPI.md
lines: 76
sha256: 59c134873c230bfcc23a110181a42217f94959f6ba8f1d6bf2446ea2ec6d3215
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Running_EFDC_with_MPI.md — 판독 구간 기록

구간은 1행부터 76행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 머리말 — 페이지 제목은 Running EFDC+ with MPI이다(3). 페이지 ID, space, URL, 버전, 갱신 시각과 문서 경로를 기록한다(2–8). |
| 10–22 | Modifying the EFDC+ Run Script — MPI 실행 예시를 제시한다(10). mpiexec.exe가 EFDC+ 실행 파일 앞에 와야 하고 MPI 프로세스 수는 domain.inp의 총 하위 영역(subdomain) 수와 일치해야 한다고 적는다(18–19). OpenMP 스레드(thread)를 사용하면 추가 실행 환경 변수가 필요하고 클러스터(cluster)에서는 host_file도 지정해야 한다고 적는다(21). 조건과 옵션 표기를 그대로 옮긴다. 원문: `- The *mpiexec.exe* executable needs to precede the EFDC+ executable.` (18); `- the '- n # processes', this specifies the total number of MPI processes. It should match up to the total number of subdomains specified in the domain.inp file.` (19); `Additionally, depending on the if OpenMP threading is utilized an additional run time environment variable must be set. If running on a cluster system a host\_file must be specified as well. To differentiate between the run options, each method is described in the sections below.` (21). |
| 23–38 | Running with MPI Only on a Single Node — 단일 노드(single node) MPI 실행 예시는 KMP_AFFINITY 설정, 제목, 작업 폴더 이동, 프로세스 수 4와 -NT1 -NOP 실행 옵션, PAUSE를 포함한다(28–36). 스크립트의 비어 있지 않은 줄을 그대로 옮긴다. 수치·옵션은 예시이며 기본값으로 정의하지 않는다. 원문: `SET KMP_AFFINITY=granularity=fine,compact,1,0` (28); `TITLE Title of the model` (30); `CD "C:\Location\of\Working\Directory"` (32); `EE\EFDC\mpi_distribution\mpiexec -n 4 "\path\to\EFDCPlus_101_MPI.exe" -NT1 -NOP` (34); `PAUSE` (36). |
| 39–54 | Running with MPI and OpenMP Only on a Single Node — MPI·OpenMP 실행은 -genv I_MPI_PIN_DOMAIN=omp를 실행 줄에 추가하도록 적는다(41). 예시는 프로세스 수 4와 -NT2 -NOP를 사용한다(50). 제목의 반복된 ^ 문자와 코드 블록·빈 줄을 포함한다(39–54). 설명과 스크립트의 비어 있지 않은 줄을 그대로 옮긴다. 원문: `To run with MPI and OpenMP an additional enviornment variable should be specified in the execution line, i.e., -genv I\_MPI\_PIN\_DOMAIN=omp. An example script is given below.` (41); `SET KMP_AFFINITY=granularity=fine,compact,1,0` (44); `TITLE Title of the model` (46); `CD "C:\Location\of\Working\Directory"` (48); `\EE\EFDC\mpi_distribution\mpiexec -n 4 -genv I_MPI_PIN_DOMAIN=omp "\path\to\EFDCPlus_101_MPI.exe" -NT2 -NOP` (50); `PAUSE` (52). |
| 55–76 | Running on MPI a Cluster (Multi Node) / Advanced Feature — 노드 IP 주소 또는 DNS 이름을 얻는 설명과 Windows 명령 프롬프트에서 NSLOOKUP을 입력하는 절차를 제시한다(57–60). 여러 노드의 클러스터 실행에는 실행 호스트 주소 목록을 적은 host_file이 필요하다고 적는다(62). 외부 Intel 안내 링크를 제시한다(64). 예시는 -f host_file, 프로세스 수 4, -NT1 -NOP를 사용한다(73). 스크립트의 비어 있지 않은 줄을 그대로 옮긴다(67–75). 연결된 안내의 내용은 이번 판독에서 읽지 않았다. 원문: `- Type **NSLOOKUP** and hit **Enter**.  The default Server is set to your local DNS, the Address will be your local IP.` (60); `To run on a cluster with multiple nodes requires the specification of a host\_file. The host\_file specifies a list of hosts on which to run the executable. These hosts correspond to address of each computer.` (62); `SET KMP_AFFINITY=granularity=fine,compact,1,0` (67); `TITLE Title of the model` (69); `CD "C:\Location\of\Working\Directory"` (71); `EE\EFDC\mpi_distribution\mpiexec -f host_file -n 4 "\path\to\EFDCPlus_101_MPI.exe" -NT1 -NOP` (73); `PAUSE` (75). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 34·50·73행: 예시에 `-NT1`, `-NT2`, `-NOP`를 사용하지만 이 파일에는 해당 옵션의 정의가 없다.
- 39행: 절 제목 뒤에 반복된 `^` 문자가 본문 제목 문자열로 남아 있다.

