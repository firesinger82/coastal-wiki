# PDF 31 — CADMAS-STR Program Instructions 91–113쪽 전수 대조

- 검증일은 2026-11-04이다.
- 대상은 [p091-113.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Manual/CADMAS-STR_Program%20Instructions_English.pdf/p091-113.md)이다.
- 원본 PDF의 전체 쪽 수는 대상 기록의 frontmatter 기준 113쪽이다.
- 대조한 쪽 수는 PDF p.91–113의 23쪽이다.
- 제공된 PNG 23개를 이미지 보기 도구로 직접 열었다.
- PNG 메타데이터의 해상도는 모두 2480 × 3508 픽셀이다.
- PNG 메타데이터의 dpi는 모두 약 300이다.
- p.93·99·101과 p.103–113은 원래 해상도로 확대해서 확인했다.
- 고친 쪽 수는 아래 변경 목록의 서로 다른 쪽 번호 기준 20쪽이다.
- 정정한 쪽은 p.99·105·108·110·111의 5쪽이다.
- 보완한 쪽은 p.91·92·93·95·96·97·99·100·101·102·104·105·106·107·108·109·110·111·112·113의 20쪽이다.
- 정정과 보완이 겹치는 쪽은 p.99·105·108·110·111의 5쪽이다.
- 일치한 쪽은 p.94·98·103의 3쪽이다.
- 정정과 보완이 모두 있는 행에는 두 표지를 모두 붙였다.
- 마지막 줄의 정정 수와 보완 수는 각각 해당 표지가 붙은 쪽 수이다.
- 기록 표의 쪽별 행 수는 수정 전후 모두 23행이다.
- 기존 frontmatter 항목은 유지했다.
- frontmatter에는 요청된 `verified_by` 한 줄을 추가했다.

## 정정·보완 목록

표의 쪽 번호는 PDF 쪽 번호이다.
근거는 해당 쪽의 제공된 PNG이다.
앞 쪽의 절 이름을 사용하는 경우에는 이어지는 절이라는 설명을 추가했다.

| 쪽 | 이전 | 새 | 근거 |
|---|---|---|---|
| p.91 | 누락 | [보완] 위 표의 열 이름은 `classification.`, `variable name`, `type`, `contents`이다. `NOD(2*MINT,NPECG)`는 절점 번호이다. `IEL(2*ME,NPECG)`는 요소 번호이다. `IPF(MPF,NPECG)`는 면 요소 번호이다. `NODG(MAX(NG),NPECG)`는 면 무게중심점 번호이다. | p.91 위·아래 표의 머리글과 번호 배열 설명. |
| p.92 | 4.3.2 `M_PART` 접촉해석 자료표의 계속이다. | [보완] 앞 쪽에서 이어지는 절 4.3.2 `M_PART`의 접촉해석 자료표이다. 이 쪽에는 절 제목이 다시 인쇄되어 있지 않다. | p.92는 표의 첫 행부터 시작한다. |
| p.92 | 누락 | [보완] 송신 항목 `NPEXPX`, `NEXPX`, `IPEXPX(NPEXPX)`, `IDXEXPX(2,NPEXPX)`, `NODEXPX(NEXPX)`는 각각 송신 프로세스 수, 송신 절점 수, 송신 상대 프로세스 번호, `NODEXPX` 목록의 시작·끝 주소, 송신 절점 번호이다. | p.92 표 하단 송신 항목 다섯 행. |
| p.93 | 누락 | [보완] 자료 배분 뒤에는 프로세스 사이에서 자료를 통신하면서 병렬 계산을 수행한다. 위 전체 격자의 절점 번호는 아래 행부터 왼쪽에서 오른쪽으로 `1,2,3,4,5`, `6,7,8,9,10`, `11,12,13,14,15`, `16,17,18,19,20`, `21,22,23,24,25`이다. 분할 뒤 `PE#1`의 지역 번호는 위 행부터 `15,6,7`, `14,13,4,5`, `10,1,2,3`, `8,9,11,12`이다. `PE#1`의 첫 행은 나머지 행보다 왼쪽 절점이 하나 적다. `PE#2`의 지역 번호는 위 행부터 `4,5,6,12`, `1,2,3,11`, `7,8,9,10`이다. `PE#3`의 지역 번호는 위 행부터 `10,9,11,12`, `8,4,5,6`, `7,1,2,3`이다. `PE#4`의 지역 번호는 위 행부터 `11,10,12`, `5,6,9`, `3,4,8`, `1,2,7`이다. 원형 절점은 검정색·회색·흰색으로 구별되어 있다. 영역에는 서로 다른 회색 음영이 있다. 아래 `transmission` 그림에서 `PE#3`의 `1,4`는 `PE#4`의 `7,8`로 전송된다. 같은 그림에서 `PE#3`의 `4,5,6`은 `PE#1`의 `9,11,12`로 전송된다. 아래 `reception` 그림에서 `PE#4`의 `2,4,6`은 `PE#3`의 `7,8,10`으로 전송된다. 같은 그림에서 `PE#1`의 `1,2,3`은 `PE#3`의 `9,11,12`로 전송된다. 굵은 직사각형은 해당 절점 묶음을 둘러싼다. 아래 두 그림 사이에는 잘린 문자 조각 `(t`가 보인다. | p.93 첫 문단과 위 격자 번호 및 아래 통신 그림의 표시. |
| p.95 | 누락 | [보완] 계산 프로세스의 공통 자료 수신 상자 이름도 `BCAST_TBL`이다. `PARTITION` 바깥틀은 루트의 `PART`·`PART_C`·`BCAST_TBL`·`SEND_TBL`과 계산 프로세스의 `BCAST_TBL`·`RECV_TBL`을 포함한다. | p.95 오른쪽 BCAST_TBL 상자 및 PARTITION 바깥틀. |
| p.96 | 누락 | [보완] 그림의 열 이름은 `root process（RANK = 0）`과 `calculation process（RANK > 0）`이다. `NPFLOW0`은 수신한 각 `PART`의 잔차 노름과 압력 고정점 유량을 합산한다. `NPFLOW0`은 메시지를 출력한다. `CONT_INIT_0`은 각 `PART`의 절점 정보를 받는다. `CONT_INIT_0`은 해당 `PART` 밖의 절점 정보를 계산 프로세스에 보낸다. `CONT_INIT_0`은 접촉점 정보를 생성하여 보낸다. `CONT_INIT_0`은 접촉상태를 받아 갱신한 뒤 보낸다. `CONT_INIT_P`는 절점 정보를 송수신한다. `CONT_INIT_P`는 접촉점 정보를 받는다. `CONT_INIT_P`는 접촉상태를 판정하고 송수신한다. | p.96 NPFLOW0 및 CONT_INIT_0·CONT_INIT_P 상자의 각 설명 행. |
| p.97 | [2] 통신 흐름도의 계속이다. | [보완] 앞 쪽에서 이어지는 절 [2]의 통신 흐름도이다. 이 쪽에는 절 제목과 프로세스 열 이름이 다시 인쇄되어 있지 않다. | p.97 상단은 양쪽 바깥틀의 계속이다. |
| p.97 | 누락 | [보완] `RECV_TBLX`는 요소 정보를 루트로 보낸다. `PART_SEND_TBLX`는 각 `PART`의 요소 정보를 받는다. `PART_SEND_TBLX`는 방정식 조립용 추가 자료를 작성하여 보낸다. `PART_SEND_TBLX`는 추가 프로세스 간 통신 자료를 작성하여 보낸다. `RECV_TBLX`는 두 추가 자료를 받는다. `CONTACT0`은 각 `PART`의 절점 정보를 받는다. `CONTACT0`은 해당 `PART` 밖의 절점 정보를 계산 프로세스에 보낸다. `CONTACT0`은 접촉점 정보를 생성하여 보낸다. `CONTACT0`은 접촉상태를 받아 갱신한 뒤 보낸다. `CONTACT0`은 수렴 판정 플래그를 보낸다. `CONTACTP`는 절점 정보를 송수신한다. `CONTACTP`는 접촉점 정보를 받는다. `CONTACTP`는 접촉상태를 판정하고 송수신한다. `CONTACTP`는 수렴 플래그를 받는다. `CONTACTP`는 마찰상태를 보낸다. `MDPRESSP`는 결정된 수압을 받는다. | p.97 PART_SEND_TBLX·RECV_TBLX·CONTACT0·CONTACTP·MDPRESSP 상자. |
| p.99 | [3]의 `NL_STATIC` 흐름도이다. | [보완] 앞 쪽에서 이어지는 절 [3]의 `NL_STATIC` 흐름도이다. 이 쪽에는 [3] 절 제목이 다시 인쇄되어 있지 않다. | p.99 상단 NL_STATIC 바깥틀. |
| p.99 | `MPCCORR, RMPCCAL`은 접촉 종속점(slave points) 위치와 MPC 조건식 계수를 계산한다. | [정정] `MPCCORR, RMPCCAL`은 접촉 종속점(slave points)의 위치를 보정한다. 같은 상자는 MPC 조건식 계수 계산을 설명한다. | p.99의 원문은 Position correction of slave points in contact이다. |
| p.99 | 누락 | [보완] `PCNSTR`의 압력 증분 설정 대상은 압력 고정점이다. 오른쪽 안쪽 되돌림 선은 `MKINDEX` 뒤의 `MPCCORR, RMPCCAL` 직전으로 들어온다. `NPFORCE`의 읽히는 설명은 변형률·응력 계산을 포함한다. | p.99 PCNSTR·NPFORCE 설명 및 이름 없는 안쪽 반복 화살표. |
| p.100 | `NL_STATIC` 흐름도의 계속이다. | [보완] 앞 쪽에서 이어지는 절 [3]의 `NL_STATIC` 흐름도이다. 이 쪽에는 `NL_STATIC` 이름이 다시 인쇄되어 있지 않다. | p.100 바깥틀에는 이름이 없다. |
| p.100 | 누락 | [보완] 판정 마름모의 원문 이름은 `Residual convergence`와 `Contact convergence`이다. `NPFLOWD`의 등가 절점력은 `pore pressure`에 대한 것이다. `NPFRICD`의 등가 절점력은 `friction`에 대한 것이다. `CONTACT`는 `contact processing`을 수행한다. 잔차 반복의 복귀 위치는 앞 쪽 `MPCCORR, RMPCCAL` 직전이다. | p.100 판정 마름모와 NPFLOWD·NPFRICD·CONTACT 상자 및 p.99의 되돌림 선. |
| p.101 | `NL_TRANSIENT` 흐름도이다. | [보완] 앞 쪽에서 이어지는 절 [3]의 `NL_TRANSIENT` 흐름도이다. `NL_TRANSIENT` 이름은 이 쪽 바깥틀에 인쇄되어 있다. | p.101 상단 바깥틀. |
| p.101 | 누락 | [보완] `MKINDEX`는 연립일차방정식 조립용 `INDEX`를 생성한다. `MPCCORR, RMPCCAL`은 접촉 종속점의 위치를 보정한다. `PCNSTR`는 압력 고정점의 압력 증분을 설정한다. 접촉 반복의 원문 표시는 `contact loop`이다. 오른쪽 가장 안쪽 되돌림 선은 `MPCCORR, RMPCCAL` 직전으로 들어온다. 왼쪽 빈 공간에는 글자가 없는 짧은 세로 선 두 개가 있다. | p.101 MKINDEX·MPCCORR, RMPCCAL·PCNSTR 상자 및 반복선. |
| p.102 | `NL_TRANSIENT` 흐름도의 계속이다. | [보완] 앞 쪽에서 이어지는 절 [3]의 `NL_TRANSIENT` 흐름도이다. 이 쪽에는 `NL_TRANSIENT` 이름이 다시 인쇄되어 있지 않다. | p.102 바깥틀에는 이름이 없다. |
| p.102 | 누락 | [보완] 판정 마름모의 원문 이름은 `Residual convergence`와 `Contact convergence`이다. `GLBSTFG`의 행렬은 `seepage flow`에 대한 것이다. `FRICSTF`의 행렬은 `friction`에 대한 것이다. `NPFLOWD`의 등가 절점력은 `Pore Water Pressure`에 대한 것이다. `NPFRICD`의 등가 절점력은 `friction`에 대한 것이다. `CNTRFC`는 접촉 반력을 계산한다. `CONTACT`는 `Contact processing`을 수행한다. `IST_UPDT`의 설명은 `Plasticity, Crack Treatment`이다. 단계 반복의 원문 표시는 `step loop`이다. 잔차 반복은 앞 쪽 `MPCCORR, RMPCCAL` 직전으로 돌아간다. | p.102 각 상자의 설명과 판정·반복 표기 및 p.101의 되돌림 선. |
| p.104 | 누락 | [보완] (1)의 둘째 문단은 이 계의 감쇠 특성이 감쇠계수와 임계감쇠계수의 비로 결정된다고 설명한다. (3)의 첫 문단은 ①을 모드 분해하고 대입한다고 설명한다. 곱셈 지시문의 원문은 `Multiply [φ]ᵀ from left to right`이다. | p.104 (1)의 감쇠 특성 문단 및 (3)의 대입·곱셈 문단. |
| p.105 | Appendix 2의 (4)–(6). | [보완] 앞 쪽에서 이어지는 절 `Appendix 2`의 (4)–(6)이다. 이 쪽에는 부록 제목이 다시 인쇄되어 있지 않다. | p.105는 (4) 문단부터 시작한다. |
| p.105 | 수식의 C_K | [정정] 모든 수식의 계수를 소문자 c_K로 옮겼다. 본문의 CK는 그대로 유지했다. | p.105 (4)의 본문 식 및 (4)–(6)의 모든 감쇠계수 식. |
| p.105 | 분자 \(2\zeta_i\)에는 `← Substituting 2C/C0` | [정정] 분자 \(2\zeta_i\)에는 `← Substituting` \(2C/C_0\) | p.105 빨간 분자 테두리 오른쪽에서 C의 0은 아래첨자이다. |
| p.105 | \(\omega_i\) 이상 진동 모드 | [정정] \(\omega_i\)를 초과하는 진동 모드 | p.105 문구는 above ω_i이다. |
| p.105 | 누락 | [보완] 분자에 대한 주석은 \(2C/C_0\)를 대입한다는 뜻이다. 분모에 대한 주석은 `W4`를 대입한다는 뜻이다. | p.105 빨간 테두리의 두 주석. |
| p.106 | 누락 | [보완] 식 (2)의 빨간 설명 `Regarding displacement increments`는 변위 증분에 관한 차수라는 뜻이다. `First`는 \({}_{0}e_{ij}\) 아래에 있다. `second`는 \({}_{0}\eta_{ij}\) 아래에 있다. | p.106 식 (2)의 빨간 차수 설명. |
| p.107 | Appendix 3의 2 계속 및 3 `Discretization`. | [보완] 앞 쪽에서 이어지는 절 `Appendix 3`의 2와 이 쪽에서 시작하는 3 `Discretization`이다. 2의 절 제목은 이 쪽에 다시 인쇄되어 있지 않다. | p.107 식 (4) 위에는 절 제목이 없고, 중간에 3 Discretization이 있다. |
| p.107 | 누락 | [보완] 식 (2)와 식 (3)을 사용하여 식 (1)의 피적분함수를 증분 분해한다. 식 (4)를 사용한 선형 근사는 변위 증분의 `first order`보다 낮은 차수의 항만 남긴다고 원문에 적혀 있다. 식 (5)를 식 (1)에 대입하여 식 (6)을 얻는다. 원문은 식 (6)을 전체 라그랑주 형식 가상일 원리의 증분 분해와 선형 근사라고 설명한다. 빨간 설명 `Regarding displacement increments`는 변위 증분에 관한 차수라는 뜻이다. 마지막 문장은 각 항의 계산법을 뒤의 [1]–[3]에 제시한다고 안내한다. | p.107 식 (4) 뒤의 세 문단과 빨간 차수 설명 및 마지막 문장. |
| p.108 | Appendix 3의 3 [1] `First term of the left-hand side`. | [보완] 앞 쪽에서 이어지는 절 `Appendix 3`의 3에 속한다. 이 쪽의 인쇄 소제목은 [1] `First term of the left-hand side`이다. | p.108 상단에는 [1] 소제목만 인쇄되어 있다. |
| p.108 | ([{}_{0}^{t}B_L]\{U\})\,d{}^{0}V | [정정] ([{}_{0}^{t}B_L]\{U\})\,dV | p.108 수식 1의 세 번째 적분 말미는 dV이며 V 왼쪽 위에 0이 없다. |
| p.108 | 수식 2의 중간 벡터 전단 성분 세 행에 선형항과 첫 곱항 사이 +를 넣었다. | [정정] 해당 + 세 개를 제거하여 인쇄 그대로 옮겼다. | p.108 아래쪽 왼쪽 벡터의 제4·5·6행에는 해당 +가 인쇄되어 있지 않다. |
| p.109 | Appendix 3의 3 [1] 계속이다. | [보완] 앞 쪽에서 이어지는 절 `Appendix 3`의 3 [1]이다. 이 쪽에는 절 제목이 인쇄되어 있지 않다. | p.109는 수식만 있는 쪽이다. |
| p.110 | Appendix 3의 3 [1] 계속이다. | [보완] 앞 쪽에서 이어지는 절 `Appendix 3`의 3 [1]이다. 이 쪽에는 절 제목이 인쇄되어 있지 않다. | p.110는 수식만 있는 쪽이다. |
| p.110 | \frac{\partial {}^{t}u_{2}}{\partial{}^{0}x_{2}}\frac{\partial u_{2}}{\partial{}^{0}x_{3}}+\frac{\partial {}^{t}u_{3}}{\partial{}^{0}x_{2}}\frac{\partial u_{3}}{\partial{}^{0}x_{3}} | [정정] \frac{\partial {}^{t}u_{2}}{\partial{}^{0}x_{2}}\frac{\partial u_{2}}{\partial{}^{0}x_{3}}\frac{\partial {}^{t}u_{3}}{\partial{}^{0}x_{2}}\frac{\partial u_{3}}{\partial{}^{0}x_{3}} | p.110 두 번째 벡터 제5행의 두 번째 곱항과 세 번째 곱항 사이에는 +가 없다. |
| p.111 | Appendix 3의 3 [1] 계속이다. | [보완] 앞 쪽에서 이어지는 절 `Appendix 3`의 3 [1]이다. 이 쪽에는 절 제목이 인쇄되어 있지 않다. | p.111는 수식만 있는 쪽이다. |
| p.111 | \frac{\partial {}^{t}u_{2}}{\partial{}^{0}x_{3}}\frac{\partial}{\partial{}^{0}x_{2}}(N_1U_{2}^{1}+\cdots+N_nU_{2}^{n})+\frac{\partial {}^{t}u_{3}} | [정정] \frac{\partial {}^{t}u_{2}}{\partial{}^{0}x_{3}}\frac{\partial}{\partial{}^{0}x_{2}}(N_1U_{2}^{1}+\cdots+N_nU_{2}^{n})\frac{\partial {}^{t}u_{3}} | p.111 상단 연속 벡터의 제5·6성분에서 두 번째 괄호 뒤에는 +가 없다. |
| p.111 | \frac{\partial {}^{t}u_{2}}{\partial{}^{0}x_{1}}\frac{\partial}{\partial{}^{0}x_{3}}(N_1U_{2}^{1}+\cdots+N_nU_{2}^{n})+\frac{\partial {}^{t}u_{3}} | [정정] \frac{\partial {}^{t}u_{2}}{\partial{}^{0}x_{1}}\frac{\partial}{\partial{}^{0}x_{3}}(N_1U_{2}^{1}+\cdots+N_nU_{2}^{n})\frac{\partial {}^{t}u_{3}} | p.111 상단 연속 벡터의 제5·6성분에서 두 번째 괄호 뒤에는 +가 없다. |
| p.112 | Appendix 3의 3 [2] `Second term of the left-hand side`. | [보완] 앞 쪽에서 이어지는 절 `Appendix 3`의 3에 속한다. 이 쪽의 인쇄 소제목은 [2] `Second term of the left-hand side`이다. | p.112 상단에는 [2] 소제목만 인쇄되어 있다. |
| p.112 | 누락 | [보완] `In this case`는 ‘이 경우’라는 뜻이다. `If it is assumed that`은 ‘다음과 같이 가정하면’이라는 뜻이다. | p.112 수식 사이의 두 도입구. |
| p.113 | Appendix 3의 3 [3] `The second term of the right-hand side`. | [보완] 앞 쪽에서 이어지는 절 `Appendix 3`의 3에 속한다. 이 쪽의 인쇄 소제목은 [3] `The second term of the right-hand side`이다. | p.113 상단에는 [3] 소제목만 인쇄되어 있다. |
| p.113 | 누락 | [보완] `In this case`는 ‘이 경우’라는 뜻이다. | p.113 응력벡터 앞의 도입구. |

## 원문 인쇄에서 확인한 사실

- p.99에는 `PCNSTRI` 상자가 연속 두 번 인쇄되어 있다.
- p.99의 `TSPCDSETU`·`NPFORCE`·`NPFLOW` 설명 끝부분은 확대 후에도 완전한 단어를 확정할 수 없다.
- p.101의 `MPCCORR, RMPCCAL` 설명 끝부분은 확대 후에도 완전한 단어를 확정할 수 없다.
- 위 네 설명의 판독 불가 표지는 유지했다.
- p.100의 `GLBSTFG` 설명에는 `creation,` 뒤의 완전한 단어가 보이지 않는다.
- p.103의 Bathe 참고문헌에는 `pp.` 뒤의 쪽수가 없다.
- p.104의 일본어 `モードベクトル`은 기존 기록의 원문 인용과 일치한다.
- 기존 기록은 `モードベクトル`의 한국어 뜻을 ‘모드 벡터’로 적었다.
- p.106의 변위 증분 정의 뒤에는 `(displacement of material point at time t)`가 인쇄되어 있다.
- p.108 수식 1의 세 번째 적분은 다른 적분과 달리 `dV`로 끝난다.
- p.108·110·111에서 확인한 더하기 기호 누락은 수학적으로 보정하지 않았다.
- 원문 인쇄의 이상은 대상 기록 끝의 ‘판독 중 확인된 사실’에도 적었다.
- 이 대조는 문서 판독 검증이다.
- 수식의 수학적 타당성과 프로그램 실행 결과는 검증하지 않았다.

## 열지 못한 이미지

없음.
p.91부터 p.113까지의 PNG를 모두 열었다.

정정 5, 보완 20, 일치 3
