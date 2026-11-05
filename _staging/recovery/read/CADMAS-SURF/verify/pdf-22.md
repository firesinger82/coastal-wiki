# CADMAS-AGENT_Manual_English.pdf 1–18쪽 전수 대조

검증일은 2026-11-04이다.
원본은 `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Manual/CADMAS-AGENT_Manual_English.pdf`이다.
수정 기록은 `_staging/recovery/read/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Manual/CADMAS-AGENT_Manual_English.pdf/p001-018.md`이다.

지정된 300 dpi PNG의 PDF p.1–18을 모두 이미지 보기 도구로 열었다.
대조한 쪽 수는 18쪽이다.
고친 쪽 수는 중복을 제외하고 12쪽이다.
정정 표식은 2쪽에 붙였다: p.15, p.17.
보완 표식은 12쪽에 붙였다: p.2, p.4, p.7, p.8, p.9, p.10, p.11, p.12, p.14, p.15, p.16, p.17.
p.15, p.17에는 정정과 보완이 함께 있다.
일치 표식은 6쪽에 붙였다: p.1, p.3, p.5, p.6, p.13, p.18.
마지막 줄의 수는 표식이 붙은 쪽 수이다.
정정과 보완의 쪽 수는 중복을 포함한다.

각 쪽의 본문 문단을 기록 행과 대조했다.
식 (2-1)의 아래첨자와 부호는 확대 이미지에서 확인했다.
입력 예제의 키워드·값·단위·조건을 대조했다.
수치 배열은 중간 행까지 대조했다.
출력 레코드의 변수명과 자료형은 확대 이미지에서 확인했다.
일본어 화면 항목은 확대 이미지에서 확인했다.
텍스트 추출본은 철자 확인에만 참고했다.
이미지와 추출본이 다를 때는 이미지를 따랐다.
표의 쪽 행 18개를 유지했다.
기존 frontmatter는 유지했다.
frontmatter에는 요청한 `verified_by` 한 줄만 추가했다.

## 정정·보완 목록

| p.N | 이전 | 새 | 근거 |
|---|---|---|---|
| p.2 | 4.2 단독 계산 예제는 14쪽이다. | 보완: 4.2 `Example of single (offline) calculation execution`은 14쪽이다. | p.2 목차 4.2의 영문 제목 |
| p.2 | 6.1.1 `m_agent`, 6.1.2 `m_cadmas`, 6.1.3 `m_potential`, 6.1.4 `m_timectl`, 6.1.5 `m_output`, 6.1.6 `m_flag` 항목의 표시 쪽은 각각 18, 19, 20, 21, 21, 22이다. | 보완: 6.1.1 `Module variables about agents（m_agent）`는 18쪽이다. 6.1.2 `Module variables about CADMAS-SURF（m_cadmas）`는 19쪽이다. 6.1.3 `Module variables about potential（m_potential）`는 20쪽이다. 6.1.4 `Module variables about timeintegration（m_timectl）`는 21쪽이다. 6.1.5 `Module variables about output（m_output）`는 21쪽이다. 6.1.6 `Module variables about evacuation route search method flag（m_flag）`는 22쪽이다. | p.2 목차 6.1.1–6.1.6의 전체 제목 |
| p.4 | (누락) | 보완: 그림의 자료 블록 이름 `agent data`는 `agent.inp`에 붙어 있다. `Condition data`는 `namelist.inp`에 붙어 있다. `Entry permission data`는 `move_boundary.inp`에 붙어 있다. `Various input data`는 `shelter.inp`와 `signpost.inp`에 붙어 있다. `CADMAS-SURF output data`는 `data.ma`에 붙어 있다. `Result data`는 `agent.out`에 붙어 있다. `statistic data`는 `statistics_i.csv`와 `statistics_r.csv`에 붙어 있다. | p.4 Figure 1-1의 자료 블록 이름 |
| p.7 | (누락) | 보완: 본문은 기본 해석 조건을 지정한다고 설명한다. `rw_dt`의 원문 주석은 `update interval of randomwalk information (rw_theta)[s]`이다. `danger_path`의 원문 주석은 `tusnami arrived time data path`이다. `flag_WPprob`의 원문 주석은 `OnOff flag writing potential for each indivisual 1:write 0:not write`이다. `flag_RPprob`의 원문 주석은 `OnOff flag reading potential for each indivisual 1:read 0:not read`이다. `ini_prob`는 초기 회피 확률이라는 뜻이다. `relaxation_rate`는 증가한 회피 확률이라는 뜻이다. 그림에서 `&time`, `&agent`, `&potential`, `&output`, `&offline`, `&flag`, `&danger`는 각각 `/`로 닫힌다. | p.7 본문 첫 문장과 Figure 3-1의 주석·구분자 |
| p.8 | (누락) | 보완: 대피소 자료도 쉼표로 구분한다. | p.8 3.1.3 본문의 separated by commas |
| p.9 | `Figure 3-5 Entry permission data（move_boundary.inp）`는 `0`으로 채운 행들과 중간 통로 부분만 `0`으로 남긴 `-1` 장벽 행들을 보여 준다. | 보완: `Figure 3-5 Entry permission data（move_boundary.inp）`의 첫 줄은 `#`이다. 그림의 수치 배열은 25행과 60열이다. 이 행·열 수는 그림의 인쇄값을 위에서 아래로, 왼쪽에서 오른쪽으로 세었다. 수치 10행과 20행은 1–26열이 `-1`이다. 이 두 행의 27–34열은 `0`이다. 이 두 행의 35–60열은 `-1`이다. 나머지 수치 행은 모든 열이 `0`이다. | p.9 Figure 3-5 확대 이미지의 모든 행과 열 |
| p.9 | 그림의 첫 행은 `9999.00 166.79 9999.00 9999.00 9999.00 9999.00 9999.00 9999.00 9999.00`이다. 마지막 행은 `9999.00 157.53 158.58 159.64 160.70 161.75 162.75 163.71 9999.00`이다. | 보완: Figure 3-6의 중간 행을 포함하여 14행·9열을 모두 기록했다. | p.9 Figure 3-6 확대 이미지의 14행·9열 |
| p.10 | 첫 행은 `0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00`이다. 마지막 행은 `726.60 714.00 705.00 678.60 664.46 658.53 653.57 647.66`이다. | 보완: Figure 3-7의 14행·8열을 모두 기록했다. | p.10 Figure 3-7 확대 이미지의 14행·8열 |
| p.10 | `Figure 3-8 Time-series tsunami arrived probability data（ex：0920.txt）`의 첫 행은 `25.00 25.00 25.00 25.00 25.00 25.00 25.00 25.00 28.00`이다. 그림에는 `52.00 70.00 70.00 0.00 0.00 0.00 0.00 0.00 0.00`인 행도 있다. | 보완: Figure 3-8의 16행·9열을 모두 기록했다. | p.10 Figure 3-8 확대 이미지의 16행·9열 |
| p.10 | 첫 행은 `9999.00 166.79 9999.00 9999.00 9999.00 9999.00 9999.00 9999.00 9999.00`이다. 마지막 행은 `9999.00 157.53 158.58 159.64 160.70 161.75 162.75 163.71 9999.00`이다. | 보완: Figure 3-9의 14행·9열을 모두 기록했다. | p.10 Figure 3-9 확대 이미지의 14행·9열 |
| p.11 | 3.1.10의 계속이다. | 보완: 앞 쪽에서 이어지는 절 3.1.10 `CADMAS-SURF output data（data.ma）`의 내용이다. | p.11 상단에는 새 절 제목이 없으며 p.10의 문장이 이어짐 |
| p.11 | (누락) | 보완: Figure 3-10의 장애물 입력 행은 `OBST 28 26 1 28 30 31`, `OBST 29 26 1 29 30 32`, `OBST 30 26 1 30 30 33`이다. 경계조건 입력 행은 `B.C. D VP SLIP`, `B.C. D F FREE`, `B.C. Z 1 1 1 30 5 1 VP FIX-V 0.00 0.00 1.00`이다. | p.11 Figure 3-10의 OBST 및 B.C. 입력값 |
| p.12 | (누락) | 보완: 헤더 `N_agent`의 설명은 `Number of agent`이다. 이 설명은 에이전트 수라는 뜻이다. 본체 `time`의 설명은 `Time`이다. 본체 `nstep`의 설명은 `Step`이다. 본체는 지정된 각 시간에 반복 출력한다. 본체 `record5`의 설명은 `Variable attribute value real of real type real(4)`로 인쇄되어 있다. | p.12 Table 3-3의 변수 설명과 본체 반복 조건 |
| p.14 | (누락) | 보완: 입력 파일은 계산 실행 디렉터리에 준비한다. 파일 목록 확인 명령은 `/calc_MPMD % ls`이다. 파일 내용 확인 명령은 `/calc_MPMD % cat appfile`과 `/calc_MPMD % cat go`이다. 빨간 주석의 원문은 `Running tsunami calculations with machine1`, `Running a Multi-agent calculation with machine2`, `Load modules for CADMAS-SURF`, `Load modules for Multi-agent`이다. 스크립트의 처음 주석은 `# Definition`이다. 종료 조건 앞의 주석은 `# Clean & Exit`이다. 복사 조건문은 `if [ -f $CADMAS ]; then /bin/cp -fp $CADMAS CADMAS; fi`와 `if [ -f $MA ]; then /bin/cp -fp $MA MA ; fi`이다. 스크립트는 `mpirun` 명령 뒤의 `exit`로 끝난다. | p.14 본문 ①과 명령 상자·빨간 주석·스크립트 |
| p.15 | 마지막 명령 줄은 `/calc_FILE mpirun -np 1 ../src_ma/ma.out`으로 인쇄되어 있다. 이 줄에는 앞의 명령 줄들과 달리 `%`가 보이지 않는다. | 정정: 마지막 명령 줄은 `/calc_FILE % mpirun -np 1 ../src_ma/ma.out`으로 인쇄되어 있다. 이 줄에는 디렉터리와 `mpirun` 사이에 `%`가 있다. | p.15 ③ 실행 상자의 확대 이미지에서 %를 직접 확인 |
| p.15 | (누락) | 보완: 파일 목록 확인 명령은 `/calc_CADMAS-SURF % ls`와 `/calc_FILE % ls`이다. 빨간 주석의 원문은 `Load module of CADMAS-SURF`와 `Load module of Multi-agent`이다. | p.15 ①–③ 명령 상자의 목록 명령과 주석 |
| p.16 | (누락) | 보완: 시작 화면의 전체 메뉴·좌표축·상태값을 보완했다. 파일 선택 창의 폴더명·수정 시각·열 제목·필터를 보완했다. 일본어 항목에 한국어 뜻을 붙였다. | p.16 Figure 5-1·5-2 확대 이미지 |
| p.17 | `AGENT指定（複数可、カンマ区切り）` | 정정: `AGENT指定 (複数可, カンマ区切り)` | p.17 설정 창 확대 이미지의 원문 구두점 |
| p.17 | `変移量のスケール` | 정정: `変移量スケール` | p.17 설정 창 하단의 항목명에는 の가 없음 |
| p.17 | (누락) | 보완: 레이어 파일명과 표시값을 보완했다. 일본어 항목의 원문과 뜻을 보완했다. 라디오 버튼·체크박스 상태와 재생창·좌표축·시점 상태값을 보완했다. | p.17 Figure 5-1의 레이어 창·설정 창·재생 창·상태 표시 확대 이미지 |

## 판독 중 확인된 사실 반영

p.15의 “`%`가 보이지 않는다”는 기존 사실 목록도 정정했다.
원문의 오기로 보이는 철자는 인쇄대로 유지했다.
해당 철자는 기록 끝의 “판독 중 확인된 사실”에 모았다.
p.11은 “앞 쪽에서 이어지는 절 3.1.10”으로 표시했다.
p.9의 Figure 3-5는 확대 이미지에서 센 25행·60열의 값 배치를 기록했다.
p.9의 Figure 3-6과 p.10의 Figure 3-9는 각각 14행·9열 전체를 기록했다.
p.10의 Figure 3-7은 14행·8열 전체를 기록했다.
p.10의 Figure 3-8은 16행·9열 전체를 기록했다.
이 배열 크기는 각 그림에 보이는 수치의 행과 열을 센 값이다.
p.16의 네트워크 컴퓨터 이름 일부는 원본 화면 경계에 잘려 있다.
잘린 전체 이름은 추정하여 채우지 않았다.

## 열지 못한 이미지

없음.
지정 이미지 `cad-agent-manual-001.png`부터 `cad-agent-manual-018.png`까지 모두 열었다.

정정 2, 보완 12, 일치 6
