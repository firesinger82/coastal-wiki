---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Working_with_Models/Running_a_Model/OMP_Runs.md
lines: 36
sha256: 13b83dd3ecddd77c6c5e4217d7e498cd3d81566e2ff2e2e40c5d30083e7b9309
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# OMP_Runs.md — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 앞부분 메타데이터. `title: "OMP Runs"` (3) 및 페이지 ID, space, URL, 버전, 갱신 시각과 문서 계층을 포함한다(1–9). |
| 10–17 | OMP Runs 개요와 General 설정. Open Multi-Processing(OMP)은 다중 스레드(multi-thread) 생성·동기화를 제공하는 API로 설명된다. 스레드 선호도(thread affinity)의 속도 영향은 하드웨어 구성, 애플리케이션과 운영체제에 의존한다. 2TL·3TL 모두 OMP를 지원한다(10). 코어 수 권고 및 KMP Offset 정의는 `In the *General* frame of *EFDC+ Run Options*, set *#OMP Cores Used* and *KMP Offset* as shown in [Figure 1](#Figure1). It is recommended not to set *# OMP Cores Used* greater than or equal to the *Available CPU Cores*. Setting the number of cores to the maximum number of cores will result in diminished performance.` (12) `The user may also set the *KMP Offset,* which is the core offset for the current run. More information about KMP Offset is described in [KMP Offset Theory](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/609616191)` (14)이다. 그림 16은 General 탭이다. `Available CPU Cores: 6` (16), `# OMP Cores Used: 1` (16), `KMP Offset: 0` (16), `L: 2722` (16), `I: 34` (16), `J: 66` (16), `Print Interval: 500` (16), `Output Interval (min.): 60` (16)이 보인다. MPI 및 부가 출력·자동 검보정 선택 상자는 선택되어 있지 않다. |
| 18–23 | Other options / Run Time Status. 표시할 매개변수와 L·I·J 셀 인덱스(index)를 선택한다. Print Interval은 런타임 창(runtime window) 갱신 사이의 시간 단계 수이다. 정의 원문: `This contains the settings for feedback to EFDC's runtime window during the model run. The user selects a parameter to display for a grid cell which is defined by the L, I, J indices. The number in the *Print Interval:* specifies the number of time steps after which the output written in the Model runtime Window is refreshed.` (22) |
| 24–29 | EFDC+ Explorer Post Processing and Linkage. 출력 빈도를 설정한다: `*Output interval*: Set time for EE to the write output frequency` (26) 선택적 EE_Arrays.out 출력의 항목 이름과 난류(turbulence)의 수평 확산(horizontal diffusivity)을 켰을 때 추가되는 배열의 조건을 그대로 옮긴다: `*Write EE\_Arrays.out Linkage file (optional):*These arrays can be output if the user is interested in analyzing outputs that are beyond the standard outputs for model verification or research purposes. These outputs include Horizontal Eddy Viscosity (AH), Vertical Viscosity (AV), Turbulence (QQ), and Layer Thickness (HPK). If horizontal diffusivity is turned on for Turbulence, then additional outputs are generated. These include horizontal diffusion in XX (FMDUX), XY (FMDUY), YY (FMDVX), and YX (FMDVY). For more details about linkage files, please refer to the EFDC+ documentation. The users that can compile EFDC+ source code can specify the outputs that can be written in these linkage files.` (28) |
| 30–31 | Auto-generate Calibration Plots & Statistics. 실행 또는 충돌 여부를 나타내는 0run 플래그(flag)를 이용한다. 같은 EE 인스턴스에서 새 모델을 열면 자동 생성이 중단된다. 다른 모델을 열려면 새 EE 창을 열어야 한다고 적는다. 조건과 파일명을 포함한 원문: `*Auto-generate Calibration Plots & Statistics*: EE has an option of automatically generating calibration plots and statistics. In order to accomplish this, a file named "0run" is created as a flag that tells EE that the model is still running or has crashed. When this is not the case, EE automatically generates the plots and statistics. If the user opens a new EFDC+ model with the same instance of EE while the EFDC+ model is running, the automatic plot/statistics generation function is aborted. A new EE window should be opened if the user needs to open another EFDC model.` (30) |
| 32–36 | 종료 시 대기·이전 결과 덮어쓰기·실행 파일. 완료 시 키 입력 대기를 피하는 선택 상자, 기존 출력이 있는 모델의 실행 조건, 이전 결과를 보존하려면 새 모델로 저장해야 하는 의무 및 일반적인 실행 파일 위치 예시를 모두 보존한다: `When EFDC+ finishes execution, the model waits for the user to press a key to continue/exit. If the user does not want the pause function, they may check the box *Do not pause when the run completes* on the *EFDC+ Run Options* form.` (32) `In case the user opens the model that already has output from an older run, *Overwrite the existing model outputs?* box appears. The model can run only if the user checks on this box to overwrite results. If the user wants to preserve the output from a previous run, then they must save the existing model as a new model.` (34) `*Executable*: The user should browse to the correct EFDC executable to run the model. The default executable is generally located in the installation folder (e.g. C:\Program Files\DSI\EEMS10.X).` (36) |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음

