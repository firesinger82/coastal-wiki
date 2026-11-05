# CADMAS-SURF 차이 결론 재대조 — KU1

## 1 요약

대상은 `cadmas-tutorials-build-vs-code.md`의 「5 차이 결론」에 있는 KU1 109행이다.
최종 결론은 A 3행, B 17행, C 23행, D 1행, E 34행, F 2행, H 28행, 일치 1행이다.
E의 강도는 강함 33행과 중간 1행이다.
보고서 결론을 유지한 행은 102행이다.
보고서 결론에서 분류가 바뀐 행은 7행이다.
변경 행은 KU1-076·200·289·325·810·811·813이다.
원문 인용·목록·조건을 고친 행은 5행이다.
정정 행은 KU1-067(영역 목록), KU1-289(출력 조건), KU1-803(파서 호출 조건), KU1-804(DTMIN 적용 조건), KU1-813(문서에 없다는 판독)이다.
이 집계는 아래 109행의 최종 결론·바뀜·이유 칸에서 산출했다.

원문과 이 문서의 판정 문장을 구분한다. 이 문서는 AI가 작성한 대조 기록이다.
`R`은 `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami`다.
`S`는 `R/Simulators`다.
`3D/`, `2F/`, `STR/`, `AG/`는 각각 `S/CADMAS-SURF-3D/Source code/`, `S/CADMAS-SURF-3D2F/Source code/`, `S/STR3D/Source code/`, `S/AGENT/Source code/`다.
`루트 README.md`는 `R/README.md`다. 각 `ReadMe.md`는 해당 시뮬레이터 폴더의 파일이다.
튜토리얼과 매뉴얼의 쪽은 PDF 쪽이다. 이미지 접두어는 `cad-3d-tutorial`, `cad-2f-tutorial`, `cad-stoc-jp`, `cad-3d-manual`이다.
판 판정 결론은 AD4와 E3의 KU1 행을 참고했다. E1·E2·AD1·AD2·AD3·AD5와 외부 원문 최종 표에는 해당 KU1 판정이 없다.
‘바뀜’은 분류 또는 E 강도가 바뀐 경우다. 인용 정정과 문장 보완은 이유 칸에 따로 적는다.

STR의 소스 부재 판정은 `rg --files --hidden --no-ignore S`의 파일 목록과 S 전체의 대소문자 무시 정의 검색을 함께 사용했다.
정의 검색식은 `(subroutine|function|entry)[[:space:]]+(대상 루틴명)[[:space:](]`이다.
KU1-733–780과 KU1-916에 열거한 36개 루틴의 정의 검색 결과는 0건이다.
기본 빌드 개수는 각 Makefile의 SRCS·SRCSM 또는 하위 makefile의 OBJS를 파일 목록과 대조한 값이다.

## 2 행별 최종 결론 표

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| KU1-001 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | 3D·2F tutorial p.1 | 두 표지가 같은 고립파 충돌 예제의 주제를 적는다. | 두 튜토리얼은 고립파 벽 충돌 예제를 설명한다. |
| KU1-003 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | 3D·2F tutorial p.3 | SketchUp의 STL 작성 절차다. | 장애물 STL 작성은 외부 전처리 절차다. |
| KU1-004 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | 3D·2F tutorial p.4 | ST 파일은 CADMAS-MESH 입력이다. 이미지의 행렬은 `1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1`이다. | ST 파일 형식과 4×4 변환행렬은 전처리기 입력이다. |
| KU1-013 | C 문서 누락 | - | C 문서 누락 | 아니오 | 2F tutorial p.7; 2F/vf_iimate.f:36–61; 2F/vf_a2dflt.f:170–173 | 문서는 물의 물성만 설명한다. 코드는 `IF (NWD.LT.4) THEN`에서 `RHO0(2)=RHO0(1)`과 `ANU0(2)=ANU0(1)`을 적용한다. | 3D2F에서 밀도·동점성계수를 한 값만 지정하면 두 상에 같은 값이 적용된다. |
| KU1-017 | B 문서 오기 | B 문서 오기 | B 문서 오기 | 아니오 | 3D·2F tutorial p.7; 3D/vf_iimdl.f:50–66 | 같은 쪽 예제는 `FUNC MATRIX`를 적는다. 설명 상자는 필수 FUNC를 생략한다. | 조파 함수 형식은 `MODEL WAVE-BC {DIR} FUNC {TYPE}`로 적는다. |
| KU1-024 | B 문서 오기 | B 문서 오기 | B 문서 오기 | 아니오 | 3D·2F tutorial p.8; 3D/vf_iiboun.f:142–150,220–232 | 같은 쪽 예제는 `B.C. D VP SLIP`과 `B.C. D F FREE`를 적는다. 설명 상자는 VP·F 필드를 생략한다. | 기본 경계 형식은 `B.C. D VP {조건}`과 `B.C. D F {조건}`이다. |
| KU1-031 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | 3D·2F tutorial p.11 | STEP 2787–2790과 CPU 시간은 예제 실행 결과다. | 튜토리얼의 계산값·CPU 시간은 예시다. |
| KU1-033 | B 문서 오기 | B 문서 오기 | B 문서 오기 | 아니오 | 3D·2F tutorial p.9,12 | p.12의 `set in 5-8-(1)`은 실제 입력 위치인 p.9의 4장 8절 (ii)와 모순한다. | 압력 시계열 입력의 참조를 4-8-(ii)로 정정한다. |
| KU1-035 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | 3D·2F tutorial p.13 | CADMAS-VR의 시작·파일 읽기 화면을 설명한다. | grp 시각화는 CADMAS-VR을 사용하는 외부 후처리 절차다. |
| KU1-060 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | STOC manual p.1 | 연성 계산 자료의 표지다. | STOC 자료의 표지에는 판 번호와 날짜가 없다. |
| KU1-061 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | STOC manual p.2 | 본문은 자료의 범위를 개요로 규정한다. 단독 알고리즘은 개별 자료를 참조하라고 적는다. | 이 자료는 연성 준비 절차의 개요다. |
| KU1-062 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | STOC manual p.2 | CADMAS-MESH-MULTI·CADMAS-MESH로 입력을 만드는 외부 전처리 절차다. | STOC-CADMAS 입력 작성 안내는 CADMAS-MESH-MULTI와 CADMAS-MESH의 사용 절차다. |
| KU1-064 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | STOC manual p.3 | 전파·처오름·파력은 시스템의 적용 목적이다. | STOC-CADMAS 자료는 전파·처오름·구조물 파력을 적용 목적으로 든다. |
| KU1-065 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | STOC manual p.4 | STOC-ML·STOC-IC·CADMAS-SURF3D의 영역 배치 그림이다. | p.4는 광역·국소 영역의 시스템 구성 그림이다. |
| KU1-066 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | STOC manual p.5 | 원문은 영역별 반복과 필요한 경우의 장애물 설정을 구분한다. | MULTI의 입력 작성 절차는 영역별로 반복하며 장애물은 필요할 때 설정한다. |
| KU1-067 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | STOC manual p.6 | 솔버 선택 및 격자 영역 수치는 GUI 사례다. 영역 목록은 GRID00000, GRID00001-000, GRID00001-001, GRID00003–GRID00007이다. | p.6의 영역·분할 숫자는 전처리기 사례 설정이다. |
| KU1-068 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | STOC manual p.7 | 대상 문장은 MULTI의 3D 모듈을 사용하는 전처리 절차다. | CADMAS 수직격자 작성은 MULTI의 3D 모듈 절차다. |
| KU1-070 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | STOC manual p.8 | sgrid 행 전체는 격자 정보와 영역 수만큼의 생성 및 해석 조건 추가를 설명한다. | ML·IC 격자 정보다. 영역 수만큼 생성한다. 조건을 더하여 각 영역 .in을 작성해야 한다. |
| KU1-071 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | STOC manual p.8 | str 행 전체는 지형·공극·초기수위와 영역별 생성 및 이 파일만의 바이너리 출력을 명시한다. | 지형·공극·초기수위를 담는다. 영역 수만큼 생성한다. 이 파일만 바이너리로 출력한다. |
| KU1-072 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | STOC manual p.8 | data.in 행은 ML·IC 부모·자식 관계를 적는다. IC 아래 CADMAS 영역이 있으면 편집하라고 적는다. | ML·IC의 부모·자식 관계다. IC 아래에 CADMAS가 있으면 편집해야 한다. |
| KU1-073 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | STOC manual p.8 | cgrid 행은 CADMAS 격자·장애물·공극률과 해석 조건 추가를 설명한다. | CADMAS 격자·장애물·공극률 정보다. 해석 조건을 더하여 각 영역 .in을 작성해야 한다. |
| KU1-076 | B 문서 오기 | B 문서 오기 | C 문서 누락 | 예 | STOC manual p.9; 3D/vf_pmginp.f:25–33; 2F/vf_pmginp.f:29–49 | 이전 AD4는 코드와의 차이만으로 B로 판정했다. 문서의 한 줄 예제는 영역 수 레코드와 영역 정보 레코드의 구분을 빠뜨렸다. 두 사본의 READ는 이 구분을 요구한다. | data.env는 첫 줄에 영역 수 1을 쓰고 다음 줄에 `'a08_cad' 64 -1`을 쓴다. |
| KU1-077 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | STOC manual p.9; 3D/vf_pmginp.f:28–33 | 아홉 필드의 data.in은 외부 STOC의 입력이다. CADMAS의 환경 입력 파서는 이 형식을 읽지 않는다. | p.9의 data.in 표는 STOC 측 입력이며 CADMAS의 data.in 카드와 구분한다. |
| KU1-102 | C 문서 누락 | - | C 문서 누락 | 아니오 | 루트 README.md:3,6; 2F/vf_iiopt.f:81–87; 2F/user_eos.f:23–34; 2F/A11111.in:686–703 | 비압축으로 한정한 문구의 위치는 README 6행이다. 3행은 기액 두 상 VOF 연결을 설명한다. 입력 설명은 ISTATE=0과 ISTATE=1을 구분한다. | 3D2F는 ISTATE=0에서 비압축 기체를 선택한다. ISTATE=1에서는 `RHOG   = (PP + P0)/(RCONS*TCONS)`로 등온 기체 밀도를 계산한다. |
| KU1-105 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | 루트 README.md:10–12 | PARI가 별도로 공개하는 STOC 솔버의 배포 안내다. | STOC-ML과 STOC-IC는 별도 배포 솔버로 구분한다. |
| KU1-106 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | 루트 README.md:14–17 | 전후처리기 네 종류와 용도의 안내다. | README의 전후처리기 목록은 도구 안내다. |
| KU1-107 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | 루트 README.md:18–20 | 문장은 출판물의 인용을 요구한다. | 출판물의 인용 요구와 계산 기능을 구분한다. |
| KU1-109 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | 3D·2F ReadMe.md:2 | 개발 주체와 설계 적용에 관한 소개다. | 개발 배경과 설계 적용 소개를 알고리즘 검증과 구분한다. |
| KU1-110 | B 문서 오기 | B 문서 오기 | B 문서 오기 | 아니오 | 3D·2F·AG ReadMe.md:4; STR ReadMe.md:9; 각 Source code/Makefile 또는 makefile | Sourse는 실제 폴더 Source code의 철자 오기다. | 소스 폴더 이름을 `Source code`로 정정한다. |
| KU1-111 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | 3D·2F ReadMe.md:5–9 | 제목이 Recommended pre and post-processors다. 이 목록은 권고 도구를 열거한다. | 전후처리기 권고와 빌드 의존성을 구분한다. |

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| KU1-112 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | 3D·2F ReadMe.md:10–14 | 이 행은 기능·인용·문헌으로 이동하는 링크다. | 기능·인용·논문 링크는 별도 자료의 포인터다. |
| KU1-119 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | STR ReadMe.md:6 | 원문은 masonry materials를 적용 대상으로만 적는다. | 조적 재료는 README가 소개한 적용 대상이다. |
| KU1-121 | B 문서 오기 | B 문서 오기 | B 문서 오기 | 아니오 | STR ReadMe.md:10–11; STR/main/astea_mechanical.f:40–43; 2F/Makefile:5 | 표시 대상은 CADMAS-SURF/3D2F다. 링크의 CADMAS-2F는 배포 경로와 다르다. | STR3D의 연성 링크를 `Simulators/CADMAS-SURF-3D2F`로 정정한다. |
| KU1-122 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | STR ReadMe.md:12–13,19–24 | Femap은 권고 전후처리기다. 나머지는 외부 안내 링크다. | Femap 권고와 외부 안내 링크를 구현 근거와 구분한다. |
| KU1-125 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | AG ReadMe.md:5–12 | CADMAS-VR 권고와 외부 자료 탐색 안내다. | AGENT의 권고 도구와 기능 링크는 외부 자료 안내다. |
| KU1-200 | B 문서 오기 | B 문서 오기 | C 문서 누락 | 예 | 3D·2F/A11111.in:1–11; 3D/A11111.in:297–306; 3D/VF_A0PRM.h:2–23; 3D/vf_zgetln.f:76–89; 3D/vf_iigrid.f:76–79 | AD4의 B 근거는 현재 파서의 예외였다. A11111은 GRID END 뒤 단어를 거부하는 실행 규칙을 적지 않는다. `IF (I.NE.NWD) CALL VF_A2ERR('VF_IIGRID','SYNTAX ERROR.')`가 이 예외다. | 일반 카드의 남는 단어는 무시하지만 GRID의 END는 그 줄의 마지막 단어여야 한다. |
| KU1-219 | B 문서 오기 | B 문서 오기 | B 문서 오기 | 아니오 | 3D·2F/A11111.in:81,102; 3D/vf_iimate.f:48–51; 3D/vf_a2dflt.f:163 | 같은 문서 행의 이름 GRZ0와 제한 칸 GZR0가 모순한다. | 중력가속도 변수명은 GRZ0다. |
| KU1-220 | B 문서 오기 | B 문서 오기 | B 문서 오기 | 아니오 | 3D·2F/A11111.in:94,113–114; 3D/vf_iimate.f:10,72–79 | LC의 제한 칸에 LS를 적은 철자 오기가 있다. 파서는 `CALL VF_ZSTOI(LC,TEXT(IS(3):IE(3)))`로 읽는다. 거부 조건은 `IF (LC.LE.0 .OR. LC.GT.LEQC)`다. | DIFFUS의 농도 성분 번호 LC는 정수다. 허용 범위는 1부터 LEQC까지다. |
| KU1-221 | B 문서 오기 | B 문서 오기 | B 문서 오기 | 아니오 | 3D·2F/A11111.in:96,117; 3D/A11111.in:479–482; 2F/A11111.in:444–447; 3D/vf_iimate.f:115–121; 3D/vf_a2dflt.f:184 | 같은 문서에서 초기 농도는 K로 적고 경계 농도는 무차원으로 적는다. | 초기 농도 CINI는 무차원 값이며 기본 0이다. |
| KU1-222 | A 판 차이 | A 판 차이 | A 판 차이 | 아니오 | 2F/A11111.in:79–85,100–107; 3D·2F/vf_iimate.f diff @@ -35,14 +35,30 @@, @@ -95,17 +111,32 @@; 2F/vf_a2dflt.f:164–181 | 단상 스칼라를 두 상 배열로 바꾼 사본 차이가 판 근거다. AD4의 A와 같다. | 2F A11111의 단상 물성 표는 3D 형식을 남겼다. 판 근거는 vf_iimate.f의 3D·2F diff `@@ -35,14 +35,30 @@`와 `@@ -95,17 +111,32 @@`이다. 현재 2F는 두 상의 물성과 초기값을 구분한다. |
| KU1-241 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | 3D/A11111.in:233–234; 2F/A11111.in:218–219 | 원문은 차수 2를 권고한다. 감쇠함수 기본값의 권고 조건은 영역 폭 두 파장이다. | 차수 2와 두 파장 폭은 문서의 권고 조건이다. |
| KU1-245 | B 문서 오기 | B 문서 오기 | B 문서 오기 | 아니오 | 3D/A11111.in:242,256–257; 2F/A11111.in:227,241–242; 3D/vf_iimdl.f:296–303; 3D/vf_a2dflt.f:178 | LC와 제한 칸 LS의 철자가 모순한다. `CALL VF_ZSTOI(LC,TEXT(IS(4):IE(4)))`는 정수 읽기다. | SCHMIDT의 성분 번호 LC는 정수다. |
| KU1-251 | B 문서 오기 | B 문서 오기 | B 문서 오기 | 아니오 | 3D/A11111.in:270,281–282; 2F/A11111.in:255,266–267; 3D/vf_iicomp.f:62–71; 3D/vf_a2dflt.f:63 | LC와 제한 칸 LS의 철자가 모순한다. 코드가 정수 LC를 검사한다. | C-DONOR의 성분 번호 LC는 정수다. |
| KU1-253 | B 문서 오기 | B 문서 오기 | B 문서 오기 | 아니오 | 3D/A11111.in:273,284; 2F/A11111.in:258,269; 3D/vf_iicomp.f:91–94; 3D/vf_a2dflt.f:38 | 표의 ICGMAT만 같은 문서의 입력 형식 ICGMAX와 다르다. | 최대 반복 횟수의 변수명을 ICGMAX로 통일한다. |
| KU1-274 | B 문서 오기 | B 문서 오기 | B 문서 오기 | 아니오 | 3D/A11111.in:437–438; 2F/A11111.in:402–403; 3D/vf_iiboun.f:220–232 | 같은 표는 F FIX와 F FREE를 구분하면서 설명을 모두 슬립라고 적는다. 파서는 각각 IB=1과 IB=2로 구분한다. | F FIX는 VOF값 고정 조건이다. F FREE는 자유 조건이다. |
| KU1-275 | C 문서 누락 | - | C 문서 누락 | 아니오 | 3D/A11111.in:471; 2F/A11111.in:436; 3D/vf_iiboun.f:223–229 | 제한 칸은 비어 있다. 코드는 `IF (BF.LT.0.0D0 .OR. BF.GT.1.0D0)`에서 입력을 거부한다. | F FIX의 BF는 0부터 1까지다. |
| KU1-279 | B 문서 오기 | B 문서 오기 | B 문서 오기 | 아니오 | 3D/A11111.in:458–466,478–482; 2F/A11111.in:423–431,443–447; 3D/vf_iiboun.f:420–481 | LC와 제한 칸 LS의 철자가 모순한다. `CALL VF_ZSTOI(LC,TEXT(IS(IP):IE(IP)))`로 성분 번호를 읽는다. | 농도 경계의 성분 번호 LC는 정수다. |
| KU1-289 | B 문서 오기 | B 문서 오기 | C 문서 누락 | 예 | 3D/A11111.in:559; 2F/A11111.in:500; 3D/vf_iifile.f:107–108; 3D/vf_ol1trn.f:215–224 | AD4는 GLY 누락을 B로 분류했다. 최신 기준에서 코드의 출력 항목을 적지 않은 경우는 C다. 보고서의 결론 문장에 출력 조건을 보완했다. | `IF (ILPON(6).NE.0 .AND. IPRNT.GT.1) THEN`에서 LAMBDA 목록 출력은 GLV·GLX·GLY·GLZ를 기록한다. |
| KU1-290 | E 코드 결함 후보 | E 유지(중간) | E 코드 결함 후보 · 중간 | 아니오 | 3D/A11111.in:573–579; 3D manual p.125; 3D/VF_AFILEI.h:2–11; 3D/vf_a2dflt.f:5,92; 3D/vf_a1main.f:390; 3D/vf_iifile.f:135–138; 3D/vf_ol1trn.f:119,147; 2F/VF_AFILEI.h:4; 2F/vf_a2dflt.f:103 | 선언은 ILPON(21)인데 `CALL VF_ZSETI1(ILPON ,0,19)`는 19개만 초기화한다. 기본 비출력 문서 및 19개 선언을 19개 초기화하는 2F 경로와 모순한다. 3D ILPON 대입 검색에서 20·21의 기본 대입은 없었다. COMMON의 환경별 영초기화는 설계 의도를 입증하지 않는다. PVCP0 조건과 환경 의존성 때문에 중간을 유지한다. | 코드 결함 후보(중간): 3D의 IPVC·PPPVC 출력 플래그 두 개는 명시적으로 초기화되지 않는다. |
| KU1-292 | B 문서 오기 | B 문서 오기 | B 문서 오기 | 아니오 | 3D/A11111.in:585,596–601; 2F/A11111.in:524,535–540; 3D/vf_iifile.f:169–187; 3D manual p.125 | KC는 같은 표의 KC2와 모순한다. 엄격한 상한은 같은 표의 기본값 NI-1·NJ-1·NK-1도 배제한다. | GRP AREA는 IC1·JC1·KC1·IC2·JC2·KC2를 받으며 끝 셀 상한을 포함한다. |
| KU1-303 | B 문서 오기 | B 문서 오기 | B 문서 오기 | 아니오 | 3D/A11111.in:692; 2F/A11111.in:623; 3D/vf_iifile.f:375–378 | LC와 제한 칸 LS의 철자가 모순한다. 정수 읽기와 `IF (LC.LE.0 .OR. LC.GT.LEQC)`를 확인했다. | 시계열 농도 출력의 LC는 정수다. |
| KU1-321 | C 문서 누락 | - | C 문서 누락 | 아니오 | 3D/A11111.in:860–865; 3D/vf_iiopt.f:170–173; 3D/vf_a2dflt.f:218; 3D/vf_veuler.f:125–128 | 기본값 칸은 비어 있다. 코드는 `VVMAX=30.0D0`을 대입한다. 입력 거부 조건은 `IF (VVMAX.LE.ZERO )`다. | 잠정 속도는 기본 30 m/s로 제한하며 MAX-VELOCITY의 입력값은 ZERO보다 커야 한다. |
| KU1-325 | B 문서 오기 | B 문서 오기 | F 표기 차이 | 예 | 2F/A11111.in:699–700; 2F/vf_a2dflt.f:71 | 문서의 8.3145는 코드의 8.31451을 소수 넷째 자리로 표시한 값이다. 분모와 단위는 같다. AD4의 B를 표시 정밀도 차이인 F로 바꾼다. | 기체상수의 코드 기본값은 `8.31451D0/0.029D0`이다. |
| KU1-733 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:5; STR/src/bdyfc.f:40; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `bdfpn1.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 bdfpn1.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-734 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:6; STR/src/bdyfc.f:38; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `bdfte2.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 bdfte2.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-736 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:8; STR/src/estfhx1.f:44; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `blmhx1.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 blmhx1.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-738 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:10; STR/seq/cgindx2_s.f:57–58; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `cgindx1.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 cgindx1.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-740 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:12; STR/src/beam0.f:19; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `dbeam2.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 dbeam2.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-741 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:13; STR/src/enpfbm.f:15; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `derxbm0.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 derxbm0.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-743 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:15; STR/geo/gmtxte2.f:30; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `derxte2.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 derxte2.f를 빌드에 요구하지만 소스를 포함하지 않는다. |

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| KU1-745 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:17; STR/src/efrcp.f:15; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `efpte2.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 efpte2.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-747 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:19; STR/src/emassmtx.f:13; STR/src/emassmtx.f:11; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `emasspn1.o`·`emasste2.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 emasspn1.f·emasste2.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-748 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:20; STR/contact/npforced.f:57; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `enpfadd.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 enpfadd.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-749 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:21; STR/src/enpfrc.f:20; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `enpfhx1.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 enpfhx1.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-752 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:24; STR/src/estfmtx.f:18; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `estfpn2.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 estfpn2.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-753 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:25; STR/src/estfmtx.f:12; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `estfte1.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 estfte1.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-754 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:26; STR/src/estfpn1.f:53; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `etapn1.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 etapn1.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-755 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:27; STR/src/dflt_damp.f:36; STR/src/stpress.f:6; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `evolhx2.o`·`findint.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 evolhx2.f·findint.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-756 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:28; STR/seq/nl_static_s.f:162–165; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `glbstf.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 glbstf.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-757 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:29; STR/src/enpfbm.f:31; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `green_bm.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 green_bm.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-759 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:31; STR/src/jacob3.f:21; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `inv3.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 inv3.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-760 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:32; STR/src/ist_updt.f:29–30; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `ist_sol.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 ist_sol.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-761 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:33; STR/src/enpfbm.f:13; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `lccbm.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 lccbm.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-762 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:34; STR/src/pld_cadmas.f:36; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `loadtr1.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 loadtr1.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-763 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:35; STR/seq/nl_static_s.f:191–193; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `mergdu.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 mergdu.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-765 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:37; STR/main/astea_mechanical.f:114; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `nl_transient.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 nl_transient.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-766 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:38; STR/src/pload4.f:27; STR/src/pload4.f:36; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `nodset1.o`·`nodset5.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 nodset1.f·nodset5.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-767 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:39; STR/src/nl_static.f:107–109; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `npforce.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 npforce.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-768 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:40; STR/seq/nl_static_s.f:67–68; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `parslv.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 parslv.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-771 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:43; STR/src/iccg.f:25; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `scalsy.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 scalsy.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-772 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:44; STR/geo/gmtxpn2.f:50; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `sfnpn2.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 sfnpn2.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-773 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:45; STR/src/loadtr2.f:40; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `sfntr2.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 sfntr2.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-774 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:46; STR/src/tspcdseti.f:36; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `spcdseti.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 spcdseti.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-776 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:48; STR/femap/fmp_sol.f:47; STR/femap/fmp_sol.f:41; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `strpn2.o`·`strte1.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 strpn2.f·strte1.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-780 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR/src/makefile:52; STR/seq/nl_transient_s.f:67; STR/src/makefile:55–60; STR/makefile:27–30,80–81 | `wt_restart.o`는 필수 OBJS다. 인용한 CALL은 주석이 아니다. 같은 이름의 소스·사전 객체·다른 루틴 정의는 없다. src의 생성 규칙은 .f.o뿐이다. 빌드 요구와 실제 호출이 배포 누락을 함께 가리킨다. | 코드 결함 후보(강함): STR 배포본은 wt_restart.f를 빌드에 요구하지만 소스를 포함하지 않는다. |
| KU1-800 | C 문서 누락 | - | C 문서 누락 | 아니오 | 2F/A11111.in:79–117; 2F tutorial p.7; 2F/vf_iimate.f:118–122,133–140; 2F/vf_a2dflt.f:167–181 | 짧은 입력 설명에는 VG·KG 초기값 카드가 없다. 코드의 두 번째 상 배열에 기체 초기값을 저장한다. | 3D2F는 `MATE I.C. VG`와 `MATE I.C. KG`로 기체 초기값을 지정한다. |
| KU1-801 | C 문서 누락 | - | C 문서 누락 | 아니오 | 2F/A11111.in:390–447; 2F/vf_iiboun.f:153–156,264–267,310–313 | 문서 경계 선택 목록에는 VG·KG·EG가 없다. 이 선택자는 LGF=3을 지정한다. | 3D2F의 기체 경계 선택자는 VG·KG·EG다. |
| KU1-802 | C 문서 누락 | - | C 문서 누락 | 아니오 | 2F/A11111.in:120–259; 2F/vf_iimdl.f:246–266; 2F/vf_a2dflt.f:157–159 | 입력 설명의 모델 카드에 PORO-BC가 없다. 코드는 VP에서 IPRTB(1)을 바꾼다. VG에서는 IPRTB(3)을 바꾼다. | 3D2F는 액체·기체의 다공체 경계 조건을 MODEL PORO-BC로 선택한다. |
| KU1-803 | C 문서 누락 | - | C 문서 누락 | 아니오 | 2F/A11111.in:1–752; 3D/A11111.in:1–904; 2F/vf_ii1inp.f:151–155; 2F/vf_iihidm.f:31–36 | 두 입력 설명의 HIDEM 검색 결과는 없다. 상위 파서가 `IF (LEVEL.LE.0) THEN`에서 VF_IIHIDM을 호출한다. 이 호출 조건을 결론 문장에 보완했다. | HiDEM 입력 형식은 `HIDEM YES` 또는 `HIDEM NO`다. 상위 파서는 `IF (LEVEL.LE.0) THEN`에서 이 카드를 처리한다. |
| KU1-804 | C 문서 누락 | - | C 문서 누락 | 아니오 | 3D·2F tutorial p.6; 3D·2F/A11111.in:53–69; 3D/vf_cdtcal.f:141–147 | 문서는 증가율 제한을 적지 않는다. 보고서의 무조건적인 1.20배 상한 설명을 고쳤다. 마지막 MAX의 DTMIN이 증가율 제한보다 우선할 수 있다. | 자동 시간간격은 `DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)`을 적용한다. 기준값은 `W=DTNOW`다. `IF (NNOW.EQ.0) W=DTINIT`를 적용한다. DTMIN은 MIN 계산 뒤에 하한으로 적용한다. |

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| KU1-805 | C 문서 누락 | - | C 문서 누락 | 아니오 | 3D/A11111.in:513–527; 3D/vf_ii1inp.f:344–357 | 문서는 ars의 재시작 스텝 읽기만 설명한다. 코드의 `IF (IRETYP.EQ.-999)`는 CALCULATION END. 오류 경로를 호출한다. | 3D의 FILE RES AUTO는 .ars의 -999를 계산 완료 표지로 처리한다. |
| KU1-806 | C 문서 누락 | - | C 문서 누락 | 아니오 | 3D/A11111.in:529–579; 2F/A11111.in:472–518; 3D/vf_ol1trn.f:215–224; 3D/VF_AFILEI.h:174–177 | 출력 목록 설명에는 IPRNT 조건이 없다. 코드 조건은 `IF (ILPON(6).NE.0 .AND. IPRNT.GT.1) THEN`이다. | LAMBDA 목록 출력은 출력 스위치와 공극률 시간자료 수 IPRNT>1을 함께 요구한다. |
| KU1-807 | C 문서 누락 | - | C 문서 누락 | 아니오 | 2F/A11111.in:647–714; 2F/vf_iiopt.f:161–164 | 2F 입력 설명에서 MAX-VELOCITY 검색 결과는 없다. 코드는 `IF (VVMAX.LE.ZERO ) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')`로 검사한다. | 3D2F에도 OPTION MAX-VELOCITY 입력이 구현돼 있다. |
| KU1-808 | C 문서 누락 | - | C 문서 누락 | 아니오 | 2F/A11111.in:519–646; 3D/A11111.in:713–714; 2F/vf_iifile.f:434–453 | 2F 입력 설명에서 MAM 검색 결과는 없다. STEP는 IMMTRN에 정수 세 개를 저장한다. TIME은 RMMTRN에 실수 세 개를 저장한다. 각 경로는 시작이 끝을 넘거나 간격이 0 이하이면 거부한다. | 3D2F에도 FILE MAM STEP·TIME이 구현돼 있다. |
| KU1-809 | C 문서 누락 | - | C 문서 누락 | 아니오 | 3D/A11111.in:743–757; 2F/A11111.in:659–673; 3D/vf_a2dflt.f:45,151; 2F/vf_a2dflt.f:45,156; 3D/vf_iiopt.f:46–74 | 문서는 선택 형식을 열거하고 기본 선택을 적지 않는다. IDROP=1은 FREE-RUNDOWN이다. IBSUW0=0은 D2U=0이다. | 기본값은 T-DOOR DROP FREE-RUNDOWN과 S-CELL-VEL D2U=0이다. |
| KU1-810 | C 문서 누락 | - | A 판 차이 | 예 | 2F/A11111.in:647–714; 2F/vf_iiopt.f:103–117,159; 2F/vf_a2dflt.f:244–246 | SEA-BOTTOM 입력은 `2016.09 start`와 `2016.09 end` 블록에 있다. CALC 추가에는 `cadd 20130703(s)`와 `(e)`가 있다. 날짜 표지로 변경 영역을 특정할 수 있으므로 C에서 A로 바꾼다. | 3D2F는 `2016.09 start`·`end`로 표시된 vf_iiopt.f:103–159 블록에 OPTION SEA-BOTTOM을 구현한다. ON·OFF·CALC는 각각 ISEABT=1·0·-1을 지정한다. 기본값은 vf_a2dflt.f:244–246의 같은 날짜 블록에서 ISEABT=0이다. |
| KU1-811 | C 문서 누락 | - | A 판 차이 | 예 | 2F/A11111.in:647–714; 2F/vf_iiopt.f:103,120–159 | COORDINATE·FAULT-SYSTEM·GRID-SYSTEM은 같은 `2016.09 start`·`end` 블록에 있다. 날짜 표지로 추가 입력 영역을 특정하므로 C에서 A로 바꾼다. | 3D2F는 vf_iiopt.f:103–159의 `2016.09 start`·`end` 블록에서 평면직각좌표·UTM과 단층·격자 측지계를 선택한다. 평면직각좌표 번호의 거부 조건은 `IF (ICOORD.LT.1.OR.ICOORD.GT.19)`다. 측지계 선택은 TOKYO·JGD2000·WGS84다. |
| KU1-812 | C 문서 누락 | - | C 문서 누락 | 아니오 | 3D·2F/A11111.in:113–114; 3D/vf_iimate.f:72–79; 3D/vf_a2dflt.f:185; 2F/vf_a2dflt.f:198 | 문서의 DF 기본값 칸은 비어 있다. 기본 배열 CDF0는 0이다. 명시 입력 거부 조건은 `IF (SC.LT.ZERO)`다. | 분자 확산계수는 생략하면 0이지만 명시 입력은 ZERO 이상이어야 한다. |
| KU1-813 | C 문서 누락 | - | 일치 | 예 | 3D/A11111.in:873–901; 2F/A11111.in:721–749; 3D/vf_iidbg.f:33–38,55–60 | 보고서의 ‘저장 개수를 적지 않는다’는 원문 판독이 틀렸다. 3D 884·901행과 2F 732·749행에 `注)最後に入力された一つのボックスのみ`가 있다. 코드는 동일 배열을 덮어쓴다. | DEBUG F-BOX와 TD-VEL은 각각 마지막 지정 영역 하나를 저장한다. |
| KU1-814 | C 문서 누락 | - | C 문서 누락 | 아니오 | STOC manual p.7–9; 3D/vf_stoc_area.f:121–165 | 문서의 수직 분할 조건과 별개인 수평 병렬 분할 검사다. `IF( IS*IE*JS*JE.EQ.0 ) THEN`에서 오류를 출력하고 VF_ZXMG_ABORT를 호출한다. | STOC 연성에서는 CADMAS의 수평 병렬 분할선을 STOC-IC 격자선에 맞춘다. |
| KU1-815 | C 문서 누락 | - | C 문서 누락 | 아니오 | 3D/VF_A0PRM.h:2–23; 3D/A11111.in:494–714; 2F/A11111.in:459–634 | 파일 장치 번호는 모델 입출력의 상수다. 문서의 FILE 제어 형식에는 이 번호가 없다. | 파일 장치 번호는 VF_A0PRM.h의 PARAMETER로 고정한다. |
| KU1-816 | C 문서 누락 | - | C 문서 누락 | 아니오 | 3D/Makefile:16–87; 3D/dummy.f90:1,8; 3D/vf_pcdc2p.f:1–2; 3D/vf_pcdp2c.f:1–2; 3D/vf_zgetln_mpversion.f:1; 3D 파일 목록 | 파일 목록의 Fortran은 240개다. SRCS·SRCSM의 대상은 236개다. dummy.f90·vf_pcdc2p.f·vf_pcdp2c.f·vf_zgetln_mpversion.f를 제외한다. DUMMY는 Makefile 내부에서 값을 지정하지 않는다. | 3D의 실제 Fortran 240개 중 기본 빌드 목록은 236개다. |
| KU1-817 | C 문서 누락 | - | C 문서 누락 | 아니오 | 2F/Makefile:12–114; 2F/dummy.f90:1,8; 2F 파일 목록 | 파일 목록의 Fortran은 388개다. SRCS·SRCSM의 대상은 387개다. 기본 빌드가 제외하는 소스는 dummy.f90이다. | 3D2F의 실제 Fortran 388개 중 기본 빌드 목록은 387개다. |
| KU1-818 | C 문서 누락 | - | C 문서 누락 | 아니오 | AG/Makefile:11–56; AG/underwater_function.f90:1; AG 파일 목록 | 파일 목록의 Fortran은 40개다. SRCS·SRCSM의 대상은 39개다. 기본 빌드가 제외하는 소스는 underwater_function.f90이다. | AGENT의 실제 Fortran 40개 중 기본 빌드 목록은 39개다. |
| KU1-902 | F 표기 차이 | - | F 표기 차이 | 아니오 | 3D/Makefile:41,84,94–96; 3D/vf_im2inp.f:1 | SRCS의 .o 이름은 `.f=.o` 치환 후에도 같은 객체 이름이다. 대응 .f와 변환 규칙이 있다. | SRCS의 vf_im2inp.o는 치환 뒤에도 같은 객체를 뜻한다. |
| KU1-907 | D 문서에만 있음 | D 문서에만 있음 | D 문서에만 있음 | 아니오 | AG/Makefile:11–56,85; S 전체 검색 | `rg --no-ignore -i -n 'read_danger' S`의 결과는 AG/Makefile:85 한 줄이다. S 파일 목록에 같은 이름의 소스는 없다. SRCS·SRCSM에는 이 대상이 없다. | AGENT의 read_danger.o 선행조건 행은 남아 있지만 대응 소스와 기본 빌드 대상은 없다. |
| KU1-916 | E 코드 결함 후보 | E 유지(강함) | E 코드 결함 후보 · 강함 | 아니오 | STR 하위 makefile의 OBJS 전체; STR/src/makefile:5–60; STR/makefile:27–30,80–81; KU1-733–780의 호출 줄 | 하위 makefile의 필수 객체 625개 중 대응 소스가 없는 객체는 src의 36개다. 파일 목록에 사전 .o가 없다. S 전체의 해당 이름 SUBROUTINE·FUNCTION·ENTRY 검색 결과는 없다. src/makefile은 .f.o 규칙만 제공한다. 필수 대상과 실제 호출이라는 독립 근거가 일치한다. | 코드 결함 후보(강함): STR3D 배포본은 필수 객체 36개의 대응 소스를 포함하지 않는다. |
| KU1-950 | B 문서 오기 | B 문서 오기 | B 문서 오기 | 아니오 | models/CADMAS-SURF/source-analysis/str3d-linear-solvers.md:60; STR/geo/gmtxte1.f:1; STR/geo/gmtxte2.f:1; STR/geo/makefile:6–7 | 노트가 부재라고 적은 두 파일이 실제 배포 소스와 빌드 목록에 있다. AD4의 B를 유지한다. | `geo/gmtxte1.f`와 `geo/gmtxte2.f`가 있으며 geo 빌드 목록에 포함된다. |
| KU1-951 | B 문서 오기 | B 문서 오기 | B 문서 오기 | 아니오 | models/CADMAS-SURF/manual-notes/cadmas-2f-manual-compressibility.md:52; 2F/A11111.in:707; 2F/vf_iiopt.f:90–93 | 노트의 DENS_ERROR는 입력 키워드 DENS-ERROR의 한 글자 오기다. | 입력 키워드는 `OPTION DENS-ERROR`다. |

대상 109행: 유지 102, 변경 7
