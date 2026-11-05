# CADMAS-SURF 호출 흐름 차이 결론 재대조

## 1 요약

대상은 `_staging/recovery/flow/CADMAS-SURF-callflow.md` §8의 RF-001–RF-021 전부이다.
대상 행 수는 21행이다.
집계 단위는 아래 표의 행 ID이다.

| 최종 결론 | 행 수 |
|---|---:|
| A 판 차이 | 0 |
| B 문서 오기 | 11 |
| C 문서 누락 | 5 |
| D 문서에만 있음 | 0 |
| E 코드 결함 후보 · 강함 | 2 |
| E 코드 결함 후보 · 중간 | 0 |
| E 코드 결함 후보 · 약함 | 0 |
| F 표기 차이 | 1 |
| H 코드 대조 대상 아님 | 1 |
| 일치 | 1 |
| 합계 | 21 |

보고서 결론을 유지한 행은 18행이다.
보고서 결론에서 바뀐 행은 3행이다.
RF-004는 C에서 일치로 바뀌었다.
RF-015는 E 중간에서 E 강함으로 바뀌었다.
RF-019는 D에서 B로 바뀌었다.
표의 ‘바뀜’은 분류 또는 E 강도의 변경을 뜻한다.

인용을 고친 행은 10행이다.
이 집계는 최종 문장에 빠진 원문 조건을 복원한 행을 포함한다.
해당 행은 RF-002·004·007·009·011·014·015·016·017·018이다.
RF-004에서는 `nnow.ge.100`의 범위를 명시했다.
RF-017에서는 대변형 기능 사용 조건을 복원했다.
나머지 해당 행에서는 호출·대입·수식의 적용 조건을 보완했다.
줄 번호를 덧붙인 경우와 같은 식을 원문 표기로 옮긴 경우는 별도로 세지 않았다.

코드 경로의 공통 루트 `S`는 `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/`이다.
`3D/`는 `S/CADMAS-SURF-3D/Source code/`이다.
`2F/`는 `S/CADMAS-SURF-3D2F/Source code/`이다.
`STR/`는 `S/STR3D/Source code/`이다.
`AG/`는 `S/AGENT/Source code/`이다.
`노트/`는 `models/CADMAS-SURF/source-analysis/`이다.

쪽 이미지의 공통 루트 `P`는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/`이다.
표의 영어 문서 약칭은 `P/cadpages/<약칭>-NNN.png`를 뜻한다.
문서 쪽은 PDF 쪽 번호이다.
인쇄 쪽은 괄호 안에 따로 적었다.
일본어판은 표에 적은 `P/cadjp/` 이미지를 직접 대조했다.

판 판정 열의 `AD4`는 `CADMAS-SURF-version-verify-AD4.md`의 확정 결론이다.
판 판정 열의 `E3`는 `CADMAS-SURF-version-verify-E3.md`의 확정 결론이다.
지정된 나머지 판 판정 파일에는 추가로 대응하는 RF 행이 없다.
`CADMAS-SURF-external-sources.md`의 ‘최종’과 ‘Claude 확인 (11-04)’에는 RF 행이 없다.

## 2 행별 최종 결론 표

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| RF-001 | B 문서 오기 | B 문서 오기(AD4) | B 문서 오기 | 아니오 | `cad-2f-manual` p.2(464)·68(530). `2F/vf_a1main.f:1182–1194,1347–1386`. | Figure 0-4-1은 `State equation` 뒤에 두 번째 `Update analysis time` 상자를 둔다. `convergence`의 되돌림은 이 상자를 포함한다. 같은 문서 p.2의 `within the time step`과 모순된다. 코드의 `TNOW =TNOW+DTNOW`는 `DO 600 ILOOP=1,LOOPS` 안에 있다. 이 대입은 `DO LL=1,MAXITR`보다 앞에 있다. 밀도 반복의 종료문은 `IF(SERR.LE.SERROR) EXIT`이다. 판 판정과 같다. | 시각은 부분 시간 단계마다 한 번 갱신한다. 밀도 수렴 반복은 시각을 갱신하지 않는다. |
| RF-002 | C 문서 누락 | - | C 문서 누락 | 아니오 | `cad-2f-manual` p.68(530). `2F/vf_a1main.f:749–753,995–999,1095–1100,1124–1161`. | 흐름도는 구조·가동상·DEM의 조건부 경로를 생략한다. 실제 코드는 모델 사이의 자료 교환과 계산 조건 갱신을 수행한다. `SF_STM2`는 독립된 IF가 아니라 `SF_STR2`의 ELSEIF이다. DEM 호출에는 `IPRNT`와 `IHIDEM`의 중첩 조건이 있다. 인용 수정은 이 조건의 복원이다. | 2F 흐름도에 SF_STR2·SF_STM2·VF_JPHDM2의 조건부 경로를 추가한다. `IF(ICPL.EQ.2) THEN`에서 `CALL SF_STR2(DT,DTOLD)`를 실행한다. 같은 분기의 `ELSEIF(ISTM.EQ.1) THEN`에서 `CALL SF_STM2(DT,DTOLD)`를 실행한다. `IF (IPRNT.GT.1) THEN` 안에서 `IF (IHIDEM.EQ.0) THEN`의 `ELSE` 경로가 VF_JPHDM2를 호출한다. |
| RF-003 | B 문서 오기 | B 문서 오기(AD4) | B 문서 오기 | 아니오 | `cad-agent-manual` p.25–26(24–25). 일본어판 p.25(24), `P/cadjp/AD4-agent-25.png`. `AG/solver.f90:78–81`, `AG/read_cadmas.f90:171`, `AG/make_potential_shelter.f90:46`, `AG/make_potential_mob.f90:1`, `AG/allocate_cadmas.f90:1`, `AG/recursive_search_shelter.f90:1`. | 영어 흐름도의 `make_potential_mod`·`allocate_cadms`·`recursive_serch_shelter`를 직접 확인했다. 일본어판 루틴 목록은 코드와 같은 철자를 쓴다. 호출문과 정의도 같은 철자를 쓴다. 기능 차이가 아니라 루틴 이름의 철자 오기이다. 판 판정과 같다. | 실제 루틴 이름은 make_potential_mob, allocate_cadmas, recursive_search_shelter이다. |
| RF-004 | C 문서 누락 | - | 일치 | 예 | `cad-2f-manual` p.68(530)·142(604). `2F/vf_a1main.f:1172–1190`, `2F/vf_iiopt.f:80–87`, `2F/vf_v1eos.f:63–74`, `2F/user_eos.f:23–38`. `rg -i -n --hidden --no-ignore '\bicomp\b' 'S/CADMAS-SURF-3D2F/Source code'`의 일치 결과는 `vf_a1main.f:1178` 한 줄이다. | 문서 p.142는 ISTATE=0을 비압축으로 적는다. 같은 쪽은 ISTATE=1을 등온 과정으로 적는다. 코드의 실제 선택도 이 설명과 같다. ICOMP의 값을 읽는 문장이 없으므로 이 지역 대입은 모델 동작을 바꾸지 않는다. 따라서 이 대입의 미기재는 C의 모델 동작 누락에 해당하지 않는다. 인용 수정은 ‘100단계’를 100 이상 조건으로 명시한 것이다. | `if(nnow.ge.100) ICOMP = 1`은 NNOW가 100 이상일 때 실행하는 미사용 지역 대입이다. 압축성 선택은 ISTATE로 판단한다. `IF(ISTATE.EQ.0) RETURN`은 상태방정식 계산을 건너뛴다. 제공된 USER_EOS는 `IF(ISTATE.EQ.1) THEN`에서 등온 상태방정식을 계산한다. 이 선택은 매뉴얼의 OPTION STATE 설명과 일치한다. |
| RF-005 | E 코드 결함 후보 · 강함 | E 코드 결함 후보 · 강함(E3) | E 코드 결함 후보 · 강함 | 아니오 | `cad-str-instr` p.98(95)·101–102(98–99). `STR/main/astea_mechanical.f:110–120`, `STR/seq/nl_transient_s.f:1,173–176,202–204`, `STR/src/makefile:28,35,37,55–60`, `STR/makefile:24–30,77–81`. Simulators 전체의 대소문자 무시 정의 검색 결과는 0행이다. 검색식은 `(subroutine\|function\|entry)[[:space:]]+(nl_transient\|glbstf\|mergdu\|parslv\|wt_restart)[[:space:](]\|\b(nl_transient_\|glbstf_\|mergdu_)\s*\(`이다. | 메인 호출은 `IF( KK(1) == 0 ) THEN`에서 NL_TRANSIENT를 요구한다. NL_TRANSIENT_S도 GLBSTF와 MERGDU를 호출한다. 문서 흐름도에도 해당 루틴이 있다. src/makefile은 각각의 객체를 필수 대상으로 지정한다. 해당 이름의 정의·ENTRY·C 대응 이름이 없다. 빌드 규칙은 `.f.o :`의 소스 컴파일이며 누락 소스의 생성 규칙이 아니다. 이 근거들은 의도적으로 생략 가능한 루틴이라는 해석과 맞지 않는다. 판 판정과 같다. | STR3D 제공 트리는 NL_TRANSIENT·GLBSTF·MERGDU의 호출과 필수 빌드 객체를 남긴 채 대응 정의를 빠뜨린 코드 결함 후보이다. 강도는 강함이다. |
| RF-006 | B 문서 오기 | B 문서 오기(AD4) | B 문서 오기 | 아니오 | `노트/cadmas-surf3d-architecture-source-map.md:84`. `3D/vf_a1main.f:169–174`, `3D/vf_iiboun.f:219–234`. | 노트는 VOF 경계를 5·7만으로 한정한다. 같은 코드의 사전은 `=1:値固定`와 `=2:フリー`를 함께 적는다. 입력 파서는 FIX에 `IB=1`을 지정한다. 입력 파서는 FREE에 `IB=2`를 지정한다. 노트가 인용한 코드 자체와 모순되는 제한이다. 판 판정과 같다. | VOF 경계 코드는 1 값 고정, 2 자유, 5 조파, 7 방사이다. |
| RF-007 | B 문서 오기 | B 문서 오기(AD4) | B 문서 오기 | 아니오 | `노트/cadmas-surf3d-smac-velocity-pressure-solver.md:68`. `3D/vf_vmodif.f:200–206`, `3D/vf_f1cal.f:233–239`, `3D/vf_bspp.f:33–67`. | 노트의 ‘압력은 여기서만 갱신’은 VF_F1CAL의 VF_BSPP 호출과 모순된다. 보고서가 인용한 `PP(I,J,K)=0.0D0`에는 바깥의 PVCP0 조건과 NF 조건이 있다. 인용 수정은 이 두 조건의 복원이다. 판 판정과 같다. | VF_VMODIF 외에도 VOF 뒤의 표면·기체 압력 설정이 PP를 갱신한다. VF_BSPP의 `IF (PVCP0.LT.ZERO) THEN` 경로에서 `IF     (NF(I,J,K).EQ.8) THEN`이면 `PP(I,J,K)=0.0D0`을 실행한다. |
| RF-008 | B 문서 오기 | B 문서 오기(AD4) | B 문서 오기 | 아니오 | `노트/cadmas-surf3d-smac-velocity-pressure-solver.md:43–45`. `3D/vf_vflxdu.f:67–82`. 3D·2F `vf_vflxdu.f`의 `diff -u`에서 이 가중치·플럭스 구간은 같다. | 같은 노트의 ‘사실상 1차 풍상’ 단정은 SCMVP 혼합 설명과 모순된다. 원문의 가중치는 `SU=SCMVP`와 `SC=1.0D0-SCMVP`이다. 중심 플럭스는 `FG =WIN*(UU(I,J,K)+UU(I+1,J,K))*0.5D0`이다. FLUU 식은 풍상 항에 SU를 곱한다. 같은 식은 중심 항에 SC를 곱한다. 사본 차이의 CBUG·C2F 변경은 이 가중치를 없애지 않는다. 판 판정과 같다. | DONOR 루틴은 SCMVP로 풍상·중심 플럭스를 혼합한다. SCMVP=1에서 순수 풍상이다. |
| RF-009 | B 문서 오기 | B 문서 오기(AD4) | B 문서 오기 | 아니오 | `노트/cadmas-surf3d-timestep-nesting-stoc-coupling.md:74`. `3D/vf_a1main.f:997–1019`. | MPI_MAX 호출은 1003–1004행이다. STOC 수신·송신은 1011–1013행이다. MPI_MIN 호출은 1018–1019행이다. 노트의 ‘매 교환 전’은 최소 시간 간격 합의의 위치와 모순된다. 인용 수정은 종료 분기와 NB_SC 조건의 복원이다. 판 판정과 같다. | 종료 플래그 합의는 STOC 교환 앞이다. 최소 시간 간격 합의는 STOC 교환 뒤이다. `IF (IE.EQ.1 .OR. IEE.EQ.1) GOTO 1000`에서 종료하지 않은 경로가 뒤의 교환·시간 간격 합의에 도달한다. STOC 수신·송신은 `IF (NB_SC.GT.0) THEN` 안에서 실행한다. |
| RF-010 | B 문서 오기 | B 문서 오기(AD4) | B 문서 오기 | 아니오 | `노트/cadmas-2f-structure-coupling-cutcell.md:46`. `2F/vf_a1main.f:749–753,995–999,1096–1100,1140–1144`. | 노트는 SF_STR*를 모두 ICPL>0으로 묶는다. SF_STR0·SF_STR1·SF_STR3의 바깥 조건은 `IF(ICPL.GT.0) THEN`이다. SF_STR2의 바깥 조건은 `IF(ICPL.EQ.2) THEN`이다. 노트가 인용한 현재 코드 안에서 조건이 다르다. 판 판정과 같다. | 초기·출력 구조 경로는 ICPL.GT.0을 사용한다. 시간 반복의 SF_STR2는 ICPL.EQ.2를 사용한다. |
| RF-011 | B 문서 오기 | B 문서 오기(AD4) | B 문서 오기 | 아니오 | `노트/cadmas-2f-structure-coupling-cutcell.md:52`, `노트/str3d-contact-and-fluid-coupling.md:53`. `cad-str-instr-cadmas` p.4. `STR/module/m_val.f90:240–243`, `STR/mpi_comm/send_pos.f:1–30`, `STR/seq/nl_transient_s.f:312–314`. `2F/sf_pos_update2.f:28–49`. | 문서 표는 POS20을 TSTR2 시각의 구조 절점 좌표로 설명한다. 같은 표의 DVEL20 설명은 `Dulcie flow velocity at ground (time:TSTR2)(all processes)`이다. 코드의 `! --- DARCY FLUX ---` 아래 VELE가 SEND_POS의 FLUX 인수로 전달된다. 노트의 일반 변위·속도 설명은 이 배열 의미와 다르다. 인용 수정은 시각·rank·지반·접촉 조건의 복원이다. 판 판정과 같다. | POS20은 구조 절점 좌표이다. DVEL20은 지반 Darcy 유속이다. 송수신 원문은 sf_pos_update2.f:39–49이다. 이 교환은 `IF( TNEXT > TSTR2 ) THEN` 안의 `IF( MYRANK == 0 ) THEN` 경로에서 수행한다. DVEL20 수신문은 `IF( IGEO == 1 ) CALL SF_C_MPI_RECV_D(DVEL20,NELM0*3,IROOTS)`이다. AFC·IPND0 송신은 `IF( ICON == 1 ) THEN` 안에서 수행한다. |
| RF-012 | B 문서 오기 | B 문서 오기(AD4) | B 문서 오기 | 아니오 | `노트/str3d-fem-core-newmark-elasto-plastic.md:22`. `STR/main/main.f:41–48,77–95`, `STR/main/astea_mechanical.f:110–120`. | 노트가 지목한 81행은 PARTITION 호출이다. 실제 ASTEA_MECHANICAL 호출은 86·92행이다. β 대입 원문은 `RR(4)  = 1.D0/3.D0      ! BETA`이다. α 대입 원문은 `RR(7)  = 1.D0           ! ALPHA`이다. 값 자체는 노트와 같다. 인용 줄 번호가 잘못되었다. 판 판정과 같다. | ASTEA_MECHANICAL 호출은 main/main.f:86·92이다. β 기본값은 45행이다. α 기본값은 48행이다. |
| RF-013 | B 문서 오기 | B 문서 오기(AD4) | B 문서 오기 | 아니오 | `노트/cadmas-agent-evacuation-simulator.md:53–54`. `cad-agent-manual` p.11(10), Table 3-2. `3D/vf_om1trn.f:55–61,72–88,100–113,122–128`. `AG/read_cadmas.f90:191–205,223–232,253–256`, `AG/remesh.f90:203–231`. 3D·2F `vf_om1trn.f`의 `diff -u` 출력은 없다. | 출력식은 `ZF=GGV(I,J,K)*FF(I,J,K)*ZZ(2,K)`로 적분 두께를 만든다. `UWK=UWK+(UU(I,J,K)+UU(I+1,J,K))*ZF`를 누적한 뒤 `WK01(I,J,2)=REAL(UWK*0.5D0)`을 전달한다. 이 식에는 수심 나눗셈이 없다. AG 입력 주석도 `流量uの読み込み`와 `流量vの読み込み`이다. 따라서 노트의 유속 표기는 인용 코드와 모순된다. AD4의 B 결론은 유지한다. 다만 AD4의 ‘이 파일에는 날짜 표지가 없다’는 설명은 고친다. 55행의 `Cmod20130605`는 시간 출력 조건의 옛 줄을 표시한다. 이 표지는 유량 적분식의 판 변경 근거가 아니다. | AGENT가 CADMAS에서 받는 uu_c·vv_c는 수직 적분 유량이다. remesh는 이 값을 공간 보간한다. |
| RF-014 | F 표기 차이 | - | F 표기 차이 | 아니오 | `cad-str-instr` p.9(6). `STR/seq/npforce_s.f:16–19,43–46,65–75`, `STR/seq/nl_transient_s.f:326`. 보고서 본문 식은 `CADMAS-SURF-callflow.md:7434–7436`. | 문서 식의 첫 등식은 `\{\bar F\}_n=\beta\{F\}_{n+1}+(1-2\beta)\{F\}_n+\beta\{F\}_{n-1}`이다. 다음 등식은 `\beta(\{\Delta F\}+\{F\}'_{n+1})+(1-2\beta)\{F\}_n+\beta\{F\}_{n-1}`이다. 보고서 전사와 같다. 코드의 이력 이동은 `FCK(:,:,1:2) = FCK(:,:,2:3)`이다. 시점 기호와 배열 첨자는 같은 내부력을 나타낸다. 인용 수정은 동적 조립 조건 `IF( IDYN == 1 ) THEN`의 복원이다. | 문서의 세 시점 내부력은 FCK의 세 번째 축 1·2·3에 대응한다. FCK(:,:,1)은 n−1 시점의 내부력이다. FCK(:,:,2)는 n 시점의 내부력이다. FCK(:,:,3)은 n+1 시점의 내부력이다. `IF( IDYN == 1 ) THEN`에서 내부력 항은 `( BETA * FCK(:,:,3) + ( 1.D0 - 2.D0*BETA )*FCK(:,:,2) + BETA * FCK(:,:,1) )`이다. |
| RF-015 | E 코드 결함 후보 · 중간 | E 코드 결함 후보 · 강함(E3) | E 코드 결함 후보 · 강함 | 예 | `2F/vf_vpdrdt.f:30–40,77–118,122–166`, `2F/vf_v1cal.f:357–372`, `2F/vf_v1eos.f:63–109`, `2F/user_eos.f:23–38`. `cad-2f-manual` p.3(465). | AUI의 자기 주석은 `I+1に関する成分`이다. 115행의 차분 주석도 I+1을 가리킨다. y·z축의 대응 분기는 각각 `DRHODP(I,J+1,K)`와 `DRHODP(I,J,K+1)`을 읽는다. 그러나 x축 118행만 `DRHODP(I-1,J,K)`를 읽는다. 파일의 보정·수정·변경·날짜·BUG 표지 검색에는 일치가 없다. AUI 재대입 검색은 118행만 반환한다. VF_V1CAL은 이 계수를 보정 없이 VF_VPSOL에 전달한다. 표면셀 밀도 복사는 내부 기체셀의 좌우 미분값을 항상 같게 만드는 설계가 아니다. 호출 경로가 존재하므로 비활성 루틴 오류가 아니다. 독립적인 자기 주석과 다른 축 코드 경로가 모순을 지지하므로 E3와 같이 강함이다. 인용 수정은 셀 조건·속도 분기·영 계수 조건의 복원이다. | VF_VPDRDT의 x축 양의 이웃 계수는 코드 결함 후보이다. 강도는 강함이다. `IF(ISTATE.EQ.0) RETURN`을 통과한 뒤 `IF(NF(I,J,K).GT.0) THEN` 안에서 해당 계수를 조립한다. `IF(WUC.GT.0.0D0) THEN`의 `ELSE` 안에서 `IF(NF(I+1,J,K).GT.0) THEN`이면 `AUI(I,J,K) = AUI(I,J,K) + DCOEF*DRHODP(I-1,J,K)`를 실행한다. 이때 계수는 `DCOEF = AVLT*WUC*XX(5,I+1)`이다. 자기 주석과 y·z축 대응 경로는 양의 이웃을 가리킨다. WUC=0이면 DCOEF도 0이다. 제공된 ISTATE=1 계산에서 WUC<0이고 DCOEF가 0이 아니며 좌우 DRHODP가 다르면 이 첨자 차이가 AUI에 반영된다. |
| RF-016 | C 문서 누락 | - | C 문서 누락 | 아니오 | `cad-3d-manual` p.60(372), Figure 0-4-1. `3D/vf_a1main.f:919–940,1003–1019`. | 흐름도에 중첩 격자 교환과 STOC 교환 상자가 없다. 코드의 VF_PMGP2C·VF_PMGC2P 호출은 시간 간격 계산 앞에 있다. `2011.04 start/end`는 두 호출의 추가 인수 부분을 둘러싼다. 이 표지는 교환 호출 자체가 문서 이후에 생겼다는 근거가 아니다. 따라서 해당 흐름도의 경로 누락을 C로 유지한다. 인용 수정은 종료 분기와 NB_SC 조건의 복원이다. | 중첩 격자 교환은 반복 머리에 있다. STOC 교환은 종료 분기 뒤에 있다. `IF (IE.EQ.1 .OR. IEE.EQ.1) GOTO 1000`에서 종료하지 않은 경로가 STOC 교환 위치에 도달한다. STOC 교환은 `IF (NB_SC.GT.0) THEN` 안에서 수행한다. |
| RF-017 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `cad-str-manual` p.14, §2 [2](2)①과 GUI 화면. | 원문 지시의 앞부분은 `In cases where the large deformation feature is utilized,`이다. 보고서 인용은 이 조건을 생략했다. 이어지는 문장은 Analysis Set Manager의 NASTRAN Bulk Data Options에서 LGDISP를 선택하는 절차이다. GUI 조작 지침이므로 H를 유지한다. 인용 수정은 대변형 기능 사용 조건의 복원이다. | 대변형 기능을 사용할 때 Analysis Set Manager의 NASTRAN Bulk Data Options에서 LGDISP를 선택한다. 이 문장은 데이터 작성 GUI의 조작 지침이다. 계산 루틴 순서와 대조하지 않는다. |
| RF-018 | C 문서 누락 | - | C 문서 누락 | 아니오 | `cad-agent-manual` p.7(6)·25–26(24–25). `AG/move_agent.f90:28–61,74–104,134–136`. | 입력 예제의 n_slope 설명에는 `1:consider slope_function 0:not consider`가 있다. 따라서 기능 자체가 문서에서 빠진 것은 아니다. Figure 6-1에는 move_agent 아래 get_direction만 있다. slope_function의 호출 위치가 흐름도에서 빠졌다. 인용 수정은 해당 분기 이전의 RETURN·CYCLE·수직 피난 우회 조건을 반영한 것이다. | AGENT 흐름도는 move_agent 안의 slope_function 호출을 생략한다. `if( n_slope==1 ) then`에 도달한 에이전트 경로는 `call slope_function(S,F)`를 실행한다. `if(time<=agent_start(n)) return`은 이 분기 전에 루틴을 반환한다. 영역 밖 에이전트와 상태 0·3의 에이전트는 이 분기 전에 CYCLE로 건너뛴다. 수직 피난에서 `agent_z(n)<shelter_height(m)`이면 `go to 10`으로 이 분기를 건너뛴다. |
| RF-019 | D 문서에만 있음 | B 문서 오기·번역 오기(AD4) | B 문서 오기 | 예 | `cad-str-instr` p.98(95). 일본어판 p.98(96), `P/cadjp/AD4-str-098.png`. `2F/sf_pos_init.f:1–3,28–44`, `STR/mpi_comm/recv_surf.f:13–16,33–36`. `rg -i -n --hidden --no-ignore 'sf_pos_init_s' 'S'`의 검색 결과는 0행이다. | 영어판 RECV_SURF 왼쪽 상자는 `CADMAS SUB. SF_POS_INIT_S`이다. 일본어판의 대응 상자는 `CADMAS SUB. SF_POS_INIT`이다. 코드 정의는 `SUBROUTINE SF_POS_INIT(POS,POS2,DVEL,DVEL2,POS0,POS20,DVEL20`로 시작한다. 초기 송신 항목은 RECV_SURF의 수신 항목과 대응한다. 영어판만 루틴 이름에 `_S`를 붙였다. 철자·번역 오기는 D보다 B를 우선하는 기준을 적용했다. 판 판정과 같다. | 영어판의 SF_POS_INIT_S는 SF_POS_INIT의 번역 편집 오기이다. 실제 초기 교환은 SF_POS_INIT에서 추적한다. |
| RF-020 | C 문서 누락 | - | C 문서 누락 | 아니오 | `노트/cadmas-surf3d-timestep-nesting-stoc-coupling.md:39`. `3D/vf_cdtcal.f:141–147`. | 노트의 DT_prev 설명은 첫 단계의 DTINIT 선택을 적지 않는다. 원문은 `W=DTNOW` 다음에 `IF (NNOW.EQ.0) W=DTINIT`를 실행한다. 최종 식은 `DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)`이다. CAKIY 표지는 144행의 이전 최소값 통신 호출에 붙어 있다. 이 표지는 첫 단계 기준을 바꾼 판 근거가 아니다. | NNOW.EQ.0이면 성장 상한의 기준은 DTINIT이다. 이후 기준은 DTNOW이다. 원문의 선택문은 `IF (NNOW.EQ.0) W=DTINIT`이다. 최종 식은 `DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)`이다. |
| RF-021 | C 문서 누락 | - | C 문서 누락 | 아니오 | `노트/cadmas-agent-evacuation-simulator.md:24`. `AG/solver.f90:17,66–99`. | 노트는 time≥time_end만 종료 조건으로 적는다. 원문에는 `time_end-time.lt.eps`가 OR 조건으로 함께 있다. 허용 오차 선언은 `real(8),parameter:: eps=1.0d-10`이다. 보고서 본문의 종료 조건 인용은 원문과 같다. 종료 판단은 output 호출 뒤에 있다. | AGENT는 time>=time_end 또는 time_end-time<eps이면 시간 반복을 끝낸다. 종료문 원문은 `if( time.ge.time_end .or. time_end-time.lt.eps) exit`이다. eps는 1.0d-10이다. |

대상 21행: 유지 18, 변경 3
