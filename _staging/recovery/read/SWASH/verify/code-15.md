# SWASH 전수 대조 기록 — code-15

대상 기록은 `swash/src/SwashExpLay2DHflow.ftn90.md`이다.
원문은 frontmatter의 `models/SWASH/raw/source_code/swash/src/SwashExpLay2DHflow.ftn90`이다.
대상은 원문 1–3873행에 걸친 기록 표의 90개 구간 행이다.
경계 구간 3867–3902행은 전체를 대조한다.
각 원문 구간은 `nl -ba <원문> | sed -n 'A,Bp'`로 연다.
각 출력은 200행 이하로 제한한다.
전처리 표시의 활성 조건은 `models/SWASH/raw/source_code/swash/switch.pl` 57–66행을 기준으로 삼는다.

대상 구간의 대조를 완료했다.

| 기록 | 대조한 구간 행 수 | 실제 대조한 원문 행 | 정정 행 | 보완 행 | 두 표시가 함께 있는 행 | 이상 없음 |
|---|---:|---|---:|---:|---:|---:|
| [SwashExpLay2DHflow.ftn90.md](../swash/src/SwashExpLay2DHflow.ftn90.md) | 90 | 1–3902 (3902행) | 17 | 27 | 7 | 53 |

집계 단위는 기록 표의 구간 행이다.
정정과 보완을 함께 한 7개 행은 두 열에 각각 포함했다.
실제로 수정한 구간 행은 37개이다.
다음 표의 기록 경로는 `_staging/recovery/read/SWASH/swash/src/SwashExpLay2DHflow.ftn90.md`이다.
다음 표의 원문 행은 이 기록의 frontmatter에 적힌 원문 파일을 가리킨다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| SwashExpLay2DHflow.ftn90.md:1–84 | 공간 이산화 방법의 이름만 요약하여 적용 조건과 상대 수직 속도 정의를 생략함. | 보완: 유동 수축 조건, defect correction, wom 정의와 정수압 분기, w의 압력·수직 항 이산화를 보완함. | 62–81 |
| SwashExpLay2DHflow.ftn90.md:149–205 | epsab2를 AB2 가중치라고 설명함. kwd·kwu의 조건별 값을 설명하는 선언 주석을 생략함. | 정정·보완: epsab2를 AB2 가중치를 수정하는 작은 보정량으로 정정함. 각 인접 층의 존재 여부에 따른 1·0 주석을 인용함. 실행 초기화와 구분함. | 157; 172–173, 1847–1850 |
| SwashExpLay2DHflow.ftn90.md:255–317 | wetu(nm) /= 1 조건을 영구 건조라고 한정함. | 정정: wetu(nm)가 1이 아니거나 nmu가 1인 조건으로 정정함. | 281–300 |
| SwashExpLay2DHflow.ftn90.md:384–424 | udep(nm) > udep(nmd)를 수심 감소라고 설명함. | 정정: 비교 방향과 논리 결합을 원문 조건 그대로 명시함. | 396–404 |
| SwashExpLay2DHflow.ftn90.md:886–915 | gmatu(nm,1,1/3)을 바닥층이라고 설명함. | 정정: k=1을 최상층으로 정정함. 바깥 ihydro 분기의 전환과 닫힘을 명시함. | 823, 891–892, 916, 1008, 1366–1377 |
| SwashExpLay2DHflow.ftn90.md:916–987 | ihydro=2 구간을 ihydro=1 참 분기 안이라고 표시함. | 정정: 같은 IF 사슬의 ihydro=2 ELSE IF 분기로 정정함. | 823, 916, 1008 |
| SwashExpLay2DHflow.ftn90.md:988–1009 | kmax를 윗층으로, k=1을 바닥층으로 설명함. 감산 계수의 배수가 모호함. ELSE 유무를 생략함. | 정정·보완: kmax를 최하층으로, k=1을 최상층으로 정정함. 두 배 가산과 한 배 감산을 구분함. ELSE 없는 IF 사슬을 명시함. | 993–1008, 1366–1422 |
| SwashExpLay2DHflow.ftn90.md:1010–1071 | iproj 분기 사슬의 ELSE 유무와 닫힘을 생략함. | 보완: ELSE 없는 사슬과 내부·외부 ENDIF 행을 명시함. | 1012–1070 |
| SwashExpLay2DHflow.ftn90.md:1214–1273 | ihvisc>1 구간을 ihvisc=1 참 분기 안이라고 표시함. | 정정: 같은 IF 사슬의 ihvisc>1 ELSE IF 분기로 정정함. | 1156, 1214, 1306 |
| SwashExpLay2DHflow.ftn90.md:1274–1307 | 바깥 젖음 조건과 루프의 닫힘 및 ihvisc 사슬의 ELSE 유무를 생략함. | 보완: 바깥 IF와 세 루프의 닫힘을 명시함. ELSE 없는 ihvisc 사슬을 명시함. | 1156, 1214–1235, 1298–1306 |
| SwashExpLay2DHflow.ftn90.md:1447–1484 | irough/=0 구간을 irough=11 분기 안이라고 표시함. ELSE 유무를 생략함. | 정정·보완: 세 번째 ELSE IF 분기로 정정함. 앞선 두 조건의 배제와 ELSE 부재를 명시함. | 1408, 1429, 1447–1483 |
| SwashExpLay2DHflow.ftn90.md:1485–1545 | fcor를 세 인덱스로 표기함. 안정성 주석에서 비점성 조건을 생략함. | 정정: fcor(nm,1)로 정정함. 준2차 방식과 비점성 조건을 복원함. | 1502, 1522 |
| SwashExpLay2DHflow.ftn90.md:1581–1605 | 바깥 iamb=1 분기의 끝을 생략함. | 보완: 1687행의 분기 전환과 1831행의 IF 사슬 닫힘을 명시함. | 1548, 1687, 1831 |
| SwashExpLay2DHflow.ftn90.md:1606–1637 | 바깥 iamb=1 분기의 끝을 생략함. | 보완: 1687행의 분기 전환과 1831행의 IF 사슬 닫힘을 명시함. | 1548, 1687, 1831 |
| SwashExpLay2DHflow.ftn90.md:1638–1686 | 바깥 iamb=1 분기의 끝을 생략함. | 보완: 1687행의 분기 전환과 1831행의 IF 사슬 닫힘을 명시함. | 1548, 1687, 1831 |
| SwashExpLay2DHflow.ftn90.md:1687–1721 | iamb=2 구간을 iamb=1 참 분기 안이라고 표시함. | 정정: 같은 IF 사슬의 iamb=2 ELSE IF 분기로 정정함. | 1548, 1687, 1831 |
| SwashExpLay2DHflow.ftn90.md:1722–1751 | 바깥 iamb=2 분기의 닫힘을 생략함. | 보완: 1831행의 ENDIF를 명시함. | 1687, 1831 |
| SwashExpLay2DHflow.ftn90.md:1752–1782 | 바깥 iamb=2 분기의 닫힘을 생략함. | 보완: 1831행의 ENDIF를 명시함. | 1687, 1831 |
| SwashExpLay2DHflow.ftn90.md:1783–1832 | 주변류 분기 사슬의 ELSE 유무를 생략함. | 보완: ELSE 없는 iamb 사슬을 명시함. | 1548, 1687, 1831 |
| SwashExpLay2DHflow.ftn90.md:1886–1925 | 바깥 ELSE의 조건식과 두 부호 분기의 ELSE 부재를 생략함. | 보완: 중앙차분 조건의 ELSE임을 명시함. 계수 0일 때의 무갱신과 바깥 블록의 닫힘을 명시함. | 1840–1864, 1875, 1890–1944 |
| SwashExpLay2DHflow.ftn90.md:2139–2187 | 이전 구현 주석만 언급하고 주석 속 두 계수식을 생략함. | 보완: 주석 처리된 두 식과 구현 복귀 주석을 인용함. 실행되지 않는 식임을 구분함. | 2157–2161 |
| SwashExpLay2DHflow.ftn90.md:2188–2247 | 주석 속 두 계수식과 이전 구현 복귀 주석을 생략함. | 보완: 주석 식과 복귀 주석을 인용함. 실행 대입식과 구분함. | 2208–2212 |
| SwashExpLay2DHflow.ftn90.md:2313–2364 | 바깥 iamb=1 고차 보정 분기의 끝을 생략함. | 보완: 2438행의 분기 전환과 2614행의 IF 사슬 닫힘을 명시함. | 2265, 2438, 2614 |
| SwashExpLay2DHflow.ftn90.md:2365–2387 | 바깥 iamb=1 고차 보정 분기의 끝을 생략함. | 보완: 2438행의 분기 전환과 2614행의 IF 사슬 닫힘을 명시함. | 2265, 2438, 2614 |
| SwashExpLay2DHflow.ftn90.md:2388–2437 | 바깥 iamb=1 고차 보정 분기의 끝을 생략함. | 보완: 2438행의 분기 전환과 2614행의 IF 사슬 닫힘을 명시함. | 2265, 2438, 2614 |
| SwashExpLay2DHflow.ftn90.md:2438–2487 | iamb=2 고차 보정 구간을 iamb=1 참 분기 안이라고 표시함. iamb=2 고차 보정 분기의 닫힘을 생략함. | 정정·보완: 같은 IF 사슬의 iamb=2 및 propsc/=1 ELSE IF 분기로 정정함. 2614행의 ENDIF를 명시함. | 2265, 2438; 2438, 2614 |
| SwashExpLay2DHflow.ftn90.md:2488–2538 | iamb=2 고차 보정 분기의 닫힘을 생략함. | 보완: 2614행의 ENDIF를 명시함. | 2438, 2614 |
| SwashExpLay2DHflow.ftn90.md:2539–2566 | iamb=2 고차 보정 분기의 닫힘을 생략함. | 보완: 2614행의 ENDIF를 명시함. | 2438, 2614 |
| SwashExpLay2DHflow.ftn90.md:2567–2615 | 주변류 고차 보정 사슬의 ELSE 유무를 생략함. | 보완: ELSE 없는 iamb·propsc 사슬을 명시함. | 2265, 2438, 2614 |
| SwashExpLay2DHflow.ftn90.md:3207–3236 | gmatv(nm,1,1/3)을 바닥층이라고 설명함. | 정정: k=1을 최상층으로 정정함. 바깥 ihydro 분기의 전환과 닫힘을 명시함. | 1366–1377, 3144, 3212–3213, 3237, 3329 |
| SwashExpLay2DHflow.ftn90.md:3237–3308 | ihydro=2 구간을 ihydro=1 참 분기 안이라고 표시함. | 정정: 같은 IF 사슬의 ihydro=2 ELSE IF 분기로 정정함. | 3144, 3237, 3329 |
| SwashExpLay2DHflow.ftn90.md:3309–3330 | kmax를 윗층으로, k=1을 바닥층으로 설명함. ELSE 유무를 생략함. | 정정·보완: 최하층과 최상층을 정정함. ELSE 없는 ihydro 사슬을 명시함. | 3314–3329, 1366–1422 |
| SwashExpLay2DHflow.ftn90.md:3331–3392 | iproj 분기 사슬의 ELSE 유무와 닫힘을 생략함. | 보완: ELSE 없는 사슬과 내부·외부 ENDIF 행을 명시함. | 3333–3391 |
| SwashExpLay2DHflow.ftn90.md:3535–3594 | ihvisc>1 구간을 ihvisc=1 참 분기 안이라고 표시함. | 정정: 같은 IF 사슬의 ihvisc>1 ELSE IF 분기로 정정함. | 3477, 3535, 3627 |
| SwashExpLay2DHflow.ftn90.md:3595–3628 | 바깥 젖음 조건과 루프의 닫힘 및 ihvisc 사슬의 ELSE 유무를 생략함. | 보완: 바깥 IF와 세 루프의 닫힘을 명시함. ELSE 없는 ihvisc 사슬을 명시함. | 3477, 3535–3556, 3619–3627 |
| SwashExpLay2DHflow.ftn90.md:3768–3805 | irough/=0 구간을 irough=11 분기 안이라고 표시함. ELSE 유무를 생략함. | 정정·보완: 세 번째 ELSE IF 분기로 정정함. 앞선 두 조건의 배제와 ELSE 부재를 명시함. | 3729, 3750, 3768–3804 |
| SwashExpLay2DHflow.ftn90.md:3806–3866 | fcor를 세 인덱스로 표기함. 시간 적분 방식과 안정성 주석을 생략함. | 정정·보완: fcor(nm,2)로 정정함. 준2차 Adams-Bashforth 방식의 비점성 조건부 안정성 주석을 보완함. | 3823, 3843 |

행 번호가 붙은 백틱 인용 1773개를 원문과 기계 대조했다.
해당 인용에서 문자열과 행 번호의 불일치는 없었다.
대상 원문의 조건·루프·호출·대입·초기값 선언 1588개 행에는 모두 행 번호가 붙은 백틱 인용이 있다.
기계 대조는 각 구간의 원문 판독과 의미 대조를 마친 뒤 수행했다.

바깥 블록의 조건식과 분기 소속을 원문과 대조했다.
대상 범위에서 닫히는 ELSE 없는 IF/ELSE IF 사슬 12개를 확인했다.
12개 사슬의 ELSE 부재를 해당 기록에 명시했다.
층 방향은 같은 원문의 `top layer only` 주석과 `rhsu(nm,1)` (1366·1377, 3687·3698)에서 확인했다.
최하층은 `bottom layer only` 주석과 `amatu(nm,kmax,1)` (1406·1422, 3727·3743)에서 확인했다.

`switch.pl` 57–66행은 해당 변수에 `TRUE`가 포함되면 행 첫머리의 전처리 표시를 제거한다.
검사한 표시는 `!TIMG`, `!MPI`, `!F95`, `!DOS`, `!UNIX`, `!/Cray`, `!/SGI`, `!/impi`, `!CVIS`, `!MatL4`이다.
대상 원문 1–3902행에는 이 표시로 시작하는 행이 없다.
대상 원문에는 오류 메시지를 작성하는 WRITE 문이나 GOTO·STOP 문이 없다.
대상 원문의 `if (STPNOW()) return`은 호출 루틴으로 반환하는 문장으로 대조했다.

frontmatter와 구간 경계는 작업 시작본과 일치한다.
원문 SHA-256은 작업 시작 때와 같은 `4c71a25b0bb2df1411278e26bb7102382442725341b8a244e63ee88af64805f1`이다.
이번 작업의 패치는 대상 구간 행과 이 보고서에만 적용했다.
작업 중 대상 밖 기록에서 별도 변경을 확인했다.
대상 밖 변경은 수정하거나 이번 집계에 포함하지 않았다.
모델은 실행하지 않았다.
Git에는 쓰기 작업을 하지 않았다.

정정 17, 보완 27, 이상 없음 53
