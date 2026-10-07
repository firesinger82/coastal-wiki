---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/KMP_Offset_Theory__OLD.md
lines: 35
sha256: b3d79c0dcaea3c7bbf9832e80db563aca26e5203fcc9db8ef0e48e9d63bd1959
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# KMP_Offset_Theory__OLD.md — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 ID, `_OLD` 제목, space, 원문 URL, 판본, 갱신 시각과 경로를 담은 frontmatter를 읽었다(1–9). |
| 10–16 | KMP Offset / 동시 실행 예 — 코어 오프셋(core offset)은 시스템에서 이미 사용하는 코어 수와 관련되며 보통 0으로 설정한다고 설명한다(10). 동일 PC에서 여러 모델을 실행할 때만 조정해야 한다는 조건 원문: `The user may also set the *KMP Offset,* which is the core offset for the current run. The *KMP Offset* relates to the number of cores already being used by the system and is therefore usually set to zero. The *KMP Offset* should only be adjusted if the user wishes to run more than one model on the same machine. In order to run the second model, the *KMP Offset* should be set to the number of cores being used in the already running model. For example, if you are using a machine with 16 cores, 32 threads, then` (10). 16코어·32스레드(thread) PC의 두 실행 설정 원문: `Run 1:   # Threads = 8, KMP Offset = 0` (12); `Run 2:   # Threads = 8, KMP Offset = 8` (14). 각 실행이 서로 다른 8코어를 쓰며 총 32스레드를 기준으로 CPU 사용량이 50%로 보인다는 설명 원문: `This will lock each thread to a unique core.  Run 1 will be using 8 cores and Run 2 the other 8 cores.  The total CPU usage will only show 50% because those calculations are based on the total number of threads, i.e. 32.` (16). |
| 17–26 | KMP_AFFINITY / 구문·실행 표시 파일 — 일반적인 Intel I7의 코어 수와 EFDC의 환경변수(environment variable)를 소개한다(18). 변수 구문과 설정 예 원문: `KMP\_AFFINITY=[<*modifier*>,...]<*type*>[,<*permute*>][,<*offset*>]` (20); `For example, to list a machine topology map, specify "KMP\_AFFINITY=verbose, none" to use a modifier of verbose and a type of none.` (22); `"KMP\_AFFINITY = granular = fine, compact, 1,0", will assign individual threads to different cores. When it assigns the threads it also spreads them out. If the modifier is set to verbose, then a map of threads will also be produced.` (24). 실행마다 모델 폴더에 만드는 파일과 성공 완료 시 삭제 조건 원문: `Note that the file "0\_RunEFDC" is created in the model folder each time the EFDC+ model is run. This file is also used by EE to determine whether the model ran to completion or not, as it is deleted on successful model completion. If the user opens that file then they can see this KMP offset related parameters` (26). |
| 27–35 | OpenMP 결합 도식·외부 문서 링크 — 그림의 결합 설정 원문: `  Figure 1 illustrates the binding of OpenMP thread to hardware thread contexts when specifying "KMP\_AFFINITY=granularity=fine, compact".` (28). `attachments/609616191/worddav70a9fbea27345733ecb44fe3b0c31554.png`를 열었다(30). 도식은 위의 `Machine/Node`를 왼쪽 `Package 0`와 오른쪽 `Package 3`에 연결한다(30 그림). 각 Package는 `Core 0`, `Core 1`에 연결되고 각 Core는 하드웨어 스레드 문맥(thread context) `0`, `1`에 연결된다(30 그림). 아래 `OpenMP* global thread IDs`는 왼쪽부터 `0, 1, 2, 3, 4, 5, 6, 7`이다(30 그림). `Package 0`의 Core 0·1은 각각 ID 0·1과 2·3에 연결된다. `Package 3`의 Core 0·1은 각각 ID 4·5와 6·7에 연결된다. 연결선에는 화살촉이 없고 수식·축·단위는 없다(30 그림). Intel 제공 캡션과 환경변수 구문에 관한 외부 URL을 읽었다(32–35). 링크 대상 웹문서는 이 판독 범위에 포함하지 않았다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 20: 구문은 `<*permute*>`를 포함하지만 이 문서는 해당 항목의 의미를 정의하지 않는다.
- 24·28: 24행의 설정 문자열은 `granular = fine`을 사용한다. 28행의 설정 문자열은 `granularity=fine`을 사용한다.
