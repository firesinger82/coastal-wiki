---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Working_with_Models/Running_a_Model/OMP_Runs/KMP_Offset_Theory.md
lines: 32
sha256: d2ac73ac821bdaeaebb43fe5bd1d0a9d4d7339642a7880a9aba38d7f828a6ad3
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# KMP_Offset_Theory.md — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 앞부분 메타데이터. `title: "KMP Offset Theory"` (3) 및 페이지 ID, space, URL, 버전, 갱신 시각과 문서 계층을 포함한다(1–9). |
| 10–16 | KMP Offset의 적용 조건과 동시 실행 예시. OMP에서 쓰며 MPI에는 적용되지 않는다. 보통 0으로 두고 같은 PC에서 여러 모델을 실행할 때만 조정한다고 적는다. 16개 코어·32개 스레드 PC의 적용 조건, 두 실행의 설정 및 CPU 표시 설명을 원문으로 옮긴다: `When using OMP, it is possible to use the *KMP Offset* option*,* which is the core offset for the current run. This option is not applicable for MPI runs. The *KMP Offset* relates to the number of cores already being used by the system and is, therefore, usually set to zero. The *KMP Offset* should only be adjusted if the user wishes to run more than one model on the same machine. In order to run the second model, the *KMP Offset* should be set to the number of cores being used in the already running model. For example, if you are using a machine with 16 cores, 32 threads, then` (10) `- Run 1:   # Threads = 8, KMP Offset = 0` (12) `- Run 2:   # Threads = 8, KMP Offset = 8` (13) `This will lock each thread to a unique core.  Run 1 will be using 8 cores and Run 2 the other 8 cores.  The total CPU usage will only show 50% because those calculations are based on the total number of threads, i.e. 32.` (15) |
| 17–24 | KMP_AFFINITY 구문과 예시. 일반적인 Intel I7의 코어 수 `4 to 6 cores` (17)와 스레드 배치 환경변수(environment variable)를 설명한다. 구문, 토폴로지(topology) 출력 및 개별 스레드의 코어 배치 예시는 `KMP\_AFFINITY=[<*modifier*>,...]<*type*>[,<*permute*>][,<*offset*>]` (19) `For example, to list a machine topology map, specify "KMP\_AFFINITY=verbose, none" to use a modifier of verbose and a type of none.` (21) `"KMP\_AFFINITY = granular = fine, compact, 1,0", will assign individual threads to different cores. When it assigns the threads it also spreads them out. If the modifier is set to verbose, then a map of threads will also be produced.` (23)이다. modifier를 verbose로 설정하면 스레드 지도를 출력한다고 적는다(23). |
| 25–30 | 0_RunEFDC 파일과 OpenMP 바인딩(binding) 그림. 실행마다 플래그 파일을 만들고 성공적 완료 시 지운다. 관련 매개변수를 파일에서 확인할 수 있다고 적는다. 파일 조건과 그림 적용 설정: `Note that the file "0\_RunEFDC" is created in the model folder each time the EFDC+ model is run. This file is also used by EE to determine whether the model ran to completion or not, as it is deleted on successful model completion. If the user opens that file then they can see the KMP offset-related parameters` (25) `[Figure 1](#Figure1) illustrates the binding of the OpenMP thread to hardware thread contexts when specifying "KMP\_AFFINITY=granularity=fine, compact".` (27) 그림 29는 `Machine/Node` (29)에서 `Package 0` (29) 및 `Package 3` (29)으로 아래쪽 가지가 갈라진다. 각 Package에서 `Core 0` (29)과 `Core 1` (29)으로 다시 갈라진다. 각 Core는 번호 `0` (29)과 `1` (29)의 Thread context 두 개로 연결된다. 왼쪽부터 OpenMP global thread IDs `0, 1, 2, 3, 4, 5, 6, 7` (29)이 순서대로 대응한다. 연결선에는 화살촉이 없다. |
| 31–32 | 추가 구문 참조. KMP_AFFINITY 환경변수와 필수 구문에 관한 Intel 문서 링크를 제공한다. 링크 원문: `<http://software.intel.com/sites/products/documentation/hpc/composerxe/en-us/cpp/mac/optaps/common/optaps_openmp_thread_affinity.htm>` (32) |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 예시 설정에 `KMP\_AFFINITY = granular = fine, compact, 1,0` (23)라고 적는다. 그림 설명의 설정에는 `KMP\_AFFINITY=granularity=fine, compact` (27)라고 적는다. 같은 문서에서 키워드 철자가 granular와 granularity로 다르다(23, 27).

