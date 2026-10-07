---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/Creating_AWS_Parallel_Cluster_and_Running_EFDC_on_it.md
lines: 194
sha256: e82192e23bb1074fbbc4546f853c7fa0940650d313b9d23003ffdb9cc1062f53
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Creating_AWS_Parallel_Cluster_and_Running_EFDC_on_it.md — 판독 구간 기록

구간은 1행부터 194행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(metadata) — 페이지 ID(2), 제목(3), space(4), 원문 URL(5), 버전(6), 갱신 시각(7), 문서 계층 경로(8)를 기록한다. `---` 구분자를 포함한다(1·9). |
| 10–15 | 문서 목적 / Setting up a cluster on AWS — AWS 클러스터를 구성하고 EFDC+를 실행하는 방법을 설명하려는 문서이다(10). 명령행 인터페이스(command line interface)에서 클러스터를 구성하고 접속할 도구 설치를 이 절의 목표로 적는다(12–15). |
| 16–37 | Prerequisites / 도구 설치 문서 — AWS 계정, 구성에 필요한 충분한 vCPU 한도, 설치된 Python과 Pip를 요구한다(18–21). 원문은 Ubuntu 18.04, Python 3.6+와 Pip 설치 상태를 가정한다(23). 요구 조건 원문: `- AWS Account` (18); `- AWS vCPU limit must be high enough to handle your configuration. You can calculate your requirements and see your limits here: [https://console.aws.amazon.com/ec2/home?#LimitsCalculator:](https://console.aws.amazon.com/ec2/home?region=us-east-1#LimitsCalculator:)` (19); `- Python 3.6+ Installed` (20); `- Pip Installed` (21); `All of this is assumed to be done with Ubuntu 18.04 and Python 3.6+, and Pip installed.` (23). AWS CLI 가상환경(virtual environment) 설치 안내 링크와 작성자의 설치 경험을 포함한다(25–27). `aws-parallelcluster` 설치 안내와 인터페이스 PDF 링크를 포함한다(29–35). 마지막 수평 구분선을 포함한다(37). 이 기록은 링크된 별도 문서의 내용을 판독하지 않았다. |
| 38–46 | AWS 콘솔 / 접근 키 — 실행 전 AWS 콘솔 로그인 상태를 준비하는 안내를 적는다(39–40). 사용자 이름 메뉴의 `My Security Credentials`와 접근 키(access key) 생성 절차를 설명한다(42–44). 다음 구성 단계에서 생성한 정보를 사용한다고 적는다(44). 빈 줄 및 수평 구분선을 포함한다(38·41·43·45–46). |
| 47–64 | AWS 계정 및 클러스터 구성 — 생성한 접근 키 정보를 `aws configure`에 입력하고 `pcluster configure`로 구성을 만든다(48–61). 명령·설정 원문: `$ aws configure` (50); `- AWS access key ID:` (54); `- Secret Access Key (unique value, can only have a max of 2 with a single aws user)` (55); `- default region: use **us-east-1**` (56); `- default output format: **none**` (57); `$ pcluster configure` (61). 63행은 구성 질문을 기억하지 못한다고 적는다. 같은 줄은 샘플 구성에 노드 3개가 있는 것으로 생각하며 노드 4개로 구성하고 싶을 수 있다고 적는다. 노드 수에 관한 이 문장의 불확실성을 유지했다. 원문: `I forgot all of the options that come up at this prompt. But they can all be changed later anyway. all that matters is running this script creates the parallel\_config file. I have attached a sample one that should be used. I think the same one has 3 nodes, we might want to set this system up with 4.` (63). |
| 65–93 | Setting Up Intel MPI / 설치 시작 — Intel MPI 안내 링크와 `Cluster_Distribution` 폴더 이동 안내를 포함한다(65–69). 압축 해제, 디렉터리 이동, 설치 스크립트 실행, 계약 동의와 기본 단일 노드 설치를 적는다(71–86). 명령·조건 원문: `tar -xvf l\_mpi\_2019.6.166.tgz` (71); `tar -xvf l_mpi_2019.6.166.tgz` (74); `cd l_mpi_2019.6.166` (75); `./install.sh` (81); `Press enter and read the agreement and type ‘accept’` (84); `Install on the default - (Single - Node)` (86). 기본 설치 경로를 바꾸는 안내 원문: `The default install location will be` (88); `/home/ubuntu/intel` (90); `Lets change that to /fsx/intel` (92). 코드 블록 및 빈 줄도 포함한다(73·76·80·82 등). |
| 94–121 | Customize Installation / 설치 경로 — 설치 사용자 지정에서 `2`를 입력하고 디렉터리 변경에서도 `2`를 입력한 뒤 `/fsx/intel`을 입력하는 절차를 적는다(94–112). 프롬프트(prompt)의 경로가 바뀌었는지 보고 Enter로 계속하며 설치 파일이 `/fsx/intel` 아래에 생길 것이라고 적는다(114–120). 입력 예시 원문: `2` (97); `2` (105); `/fsx/intel` (111); `/fsx/intel` (120). 코드 블록과 빈 줄을 포함한다. |
| 122–148 | MPI 실행 파일 경로 — Intel 설정 스크립트를 source하고 로그인 때마다 실행하도록 `.bashrc`에 추가하라고 적는다(122–129). `.bashrc` 수정 뒤 source하고 `which mpiexec`으로 경로를 확인하는 절차이다(131–147). `sample_bashrc` 예시 언급을 포함한다(122). 명령·예상 출력 원문: `source /fsx/intel/bin/compilervars.sh -arch intel64` (125); `source /fsx/intel/impi/2019.6.166/intel64/bin/mpivars.sh` (126); `source ~/.bashrc` (134); `which mpiexec` (140); `/fsx/itel/compilers_and_libraries_2020.0.166/linux/mpi/intel64/bin/mpiexec` (146). 예상 경로의 철자와 버전을 원문대로 옮겼다. |
| 149–168 | Setting the Path for the OpenMP Runtime libraries — 스레드(thread)마다 접근하는 OpenMP 공유 실행 라이브러리(runtime libraries)는 MPI 배포본에 포함되지 않으며 `Cluster_Distribution`의 `intel64_lin` 폴더에 있다고 적는다(151). `.bashrc`에 `LD_LIBRARY_PATH`를 추가하고 source한 뒤 수정 여부를 확인한다(153–167). 설정·명령·확인 조건 원문: `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/fsx/Cluster_Distribution/intel64_lin` (156); `Remember to source the .bashrc` (159); `Verify the LD\_LIBRARY\_PATH was modified` (161); `echo $LD_LIBRARY_PATH` (164); ``You should see the `/fsx/Cluster_Distribution/intel64_lin` at the end of your path`` (167). 코드 블록 및 빈 줄을 포함한다. |
| 169–194 | Running EFDC+ from the Command Line on Cluster Systems — MPI 프로세스(process) 수, 노드(node)당 프로세스 수, 호스트(host), 진단·고정 설정, 스레드 수와 EFDC 실행 인자를 제시한다(169–176). 일반 명령 원문: `mpiexec -n (# processes) -ppn (# processes per node) -hosts host1,host2 -genv I_MPI_DEBUG=5 -genv I_MPI_PIN_DOMAIN=omp -genv OMP_NUM_THREADS=(# threads) efdc+.exe -NT(# threads)` (176). 32개 하위 영역, 노드 2개, 프로세스당 스레드 2개 조건의 실행 예시를 적는다(179–183). 조건과 예시 원문: `For example, if I wanted to run with a domain decomposed into 32 subdomains across 2 nodes with 2 threads/process I could execute the following script` (179); `mpiexec -n 32 -ppn -hosts node1,node2 -genv I_MPI_DEBUG=5 -genv I_MPI_PIN_DOMAIN=omp -genv OMP_NUM_THREADS=2 efdc+.exe -NT2` (182). 원문은 노드별 16프로세스와 프로세스별 2스레드로 노드별 32코어를 사용한다고 적는다(185). 설명 및 작성자의 생각 원문: `This would run 16 processes on node1 and 16 processes on node2 with 2 threads per process. So each node would be utilizing 32 cores during a run.  ` (185); `I think its easiest to think of a process as the "master" thread and any additional threads work with that master thread to provide additional calculation capability.` (186). AWS 노드 이름 확인 명령은 `$ qnodes` (191)이다. 출력의 어딘가에 노드 이름과 추가 정보가 나올 것이라고 적는다(188–194). 이 기록에서는 명령을 실행하지 않았다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 40행: 표시된 URL은 `https://console.aws.amazon.com/`이다. 실제 링크 대상은 `https://console.aws.amazon.com/c`이다. 이 기록에서는 대상 URL의 접속 결과를 확인하지 않았다.
- 63·122행: 샘플 `parallel_config` 및 `sample_bashrc`를 언급한다. 이 파일에는 두 샘플 파일을 가리키는 첨부 링크가 없다.
- 74–75·92·125–126·146행: 설치·설정 경로는 `intel`을 쓰지만 예상 `mpiexec` 경로는 `/fsx/itel/`을 쓴다. 설치 파일과 설정 스크립트의 MPI 버전은 `2019.6.166`이며 예상 경로의 라이브러리 버전 문자열은 `2020.0.166`이다.
- 176·182행: 일반 명령은 `-ppn (# processes per node)`를 적는다. 실행 예시의 `-ppn` 뒤에는 수치 인자가 없고 곧바로 `-hosts`가 나온다.

