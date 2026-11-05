# CADMAS-SURF 차이 결론 원문 재검증 — KF2

## 1 요약

대상은 cadmas-2f-manual-program-vs-code.md의 「5 차이 결론」 안 §5.3에 있는 KF2-002–363 중 121행이다. H 행과 강도가 붙은 E 행을 포함한다. 집계는 아래 표의 서로 다른 행 ID를 기준으로 한다.

| 최종 결론 | 행 수 |
|---|---:|
| A 판 차이 | 19 |
| B 문서 오기 | 56 |
| C 문서 누락 | 36 |
| D 문서에만 있음 | 0 |
| E 코드 결함 후보 | 3 |
| F 표기 차이 | 3 |
| H 코드 대조 대상 아님 | 3 |
| 일치 | 1 |
| 합계 | 121 |

E의 강도는 강함 1행·중간 2행·약함 0행이다.

보고서 결론에서 바뀐 행은 4행이다. KF2-114는 A에서 C로 바뀐다. KF2-123은 A에서 일치로 바뀐다. KF2-139는 A에서 B로 바뀐다. KF2-360은 E 강함에서 E 중간으로 바뀐다. 나머지 117행은 분류와 강도를 유지한다.

인용을 고친 행은 14행이다. 해당 행은 KF2-002·003·102·142·307·328·342·343·346·349·353·357·359·360이다. 인용 수정은 본문·결론의 원문 해석, 조건, 수량, 식 또는 출처 위치를 바로잡은 행을 센다. 판 근거의 추가와 단순 문장 정리는 인용 수정에 포함하지 않는다.

이 문서는 AI가 작성한 판정 기록이다. 바뀜은 보고서의 분류 또는 E 강도가 바뀌었는지를 뜻한다. 보고서 결론 열의 E 강도는 같은 보고서 §5.2의 강도를 함께 표시한다.

원문 경로의 기준은 `S = models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators`다. `2F 파일:줄`은 `S/CADMAS-SURF-3D2F/Source code/파일:줄`이다. `3D 파일:줄`은 `S/CADMAS-SURF-3D/Source code/파일:줄`이다. 각 칸에서 사본 이름을 생략한 후속 파일은 2F 파일이다.

EN은 CADMAS-2F_Manural_English.pdf의 PDF 쪽이다. EN 인쇄 쪽은 PDF 쪽에 462를 더한다. JP는 CADMAS-2F_Manual_Japanese.pdf의 쪽이다. 문서 근거는 사용자 지정 cadpages와 cadjp의 쪽 이미지를 직접 열어 판독했다. E1·AD2는 같은 compare 디렉터리의 CADMAS-SURF-version-verify-E1.md·AD2.md를 뜻한다. external-sources의 최종 8행에는 KF2 행이 없다.

## 2 행별 최종 결론 표

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| KF2-002 | F | - | F | 아니오 | 2F vf_v1eos.f:116–172; EN p.61 식 (3.127) | 정규화 저장만 비교한 F다. 이류 인자 차이는 KF2-003으로 구분한다. | DRHODT는 코드가 계산한 밀도 실질미분을 현재 RHOG로 나누어 저장한다. 문서 식과의 이류 계수 차이는 KF2-003에 적는다. |
| KF2-003 | E · 중간 | E · 중간 (E1) | E · 중간 | 아니오 | 2F vf_v1eos.f:118–172; vf_vpdrdt.f:98–104; vf_vpcoef.f:421–423; user_eos.f:23–34; EN p.61 식 (3.127) | 문서 식과 별도 연속식 경로는 추가 비를 쓰지 않는다. 두 압축성 경로의 같은 비는 반대 근거지만 그 비를 보상하는 항이나 설계 설명은 없다. 인용 수정: 공극률만으로 차이 조건을 정하지 않는다. | 밀도 이류의 `GV = GGV(I,J,K)/GLV(I,J,K)` 추가 인자는 중간 강도의 코드 결함 후보이다. GGV와 GLV가 다르고 밀도 이류항이 0이 아닐 때 문서 식과 차이가 난다. ISTATE=0이면 이 계산 전에 반환한다. |
| KF2-004 | C | - | C | 아니오 | 2F vf_v1eos.f:116–166; EN p.61 식 (3.127) | 문서 식은 이웃 NF 검사를 적지 않는다. | 기상 밀도 기울기는 풍상 이웃의 NF>0인 경우에만 계산한다. |
| KF2-006 | F | - | F | 아니오 | 2F vf_vmodif.f:318–328; EN p.61 식 (3.128) | 일정 밀도에서 `PP(I,J,K)=PP(I,J,K)-PT(I,J,K)/DTNOW`에 PT=ρφ를 대입하면 문서 압력 보정과 같다. | 일정 밀도에서 코드 PT는 문서 ρφ에 대응한다. |
| KF2-009 | H | - | H | 아니오 | 2F vf_m1bcgs.f:9; EN p.63 | 70%에서 90% 초과라는 시간 비율은 성능 주장이다. | 선형계 풀이의 시간 비율과 성능 주장은 실행 검증 결과와 구별한다. |
| KF2-016 | C | - | C | 아니오 | 2F vf_m1bcgs.f:106–115,144,218–219; EN p.63 ⑥ | 문서의 상대오차 단독식은 절대오차와 전처리 우변을 생략한다. | BCGSTAB은 전처리 우변 노름에 대한 상대오차와 절대오차를 함께 사용한다. 반복 중 종료 조건은 `IF (XNORM.LE.BNORM*EPSR2+EPSA2) GOTO 2000`이다. |
| KF2-017 | F | - | F | 아니오 | 2F vf_m1bcgs.f:177–178,226–227,241; EN p.63 ①·⑦ | α 식을 대입하면 분자와 분모가 같다. | 코드의 β=W1*ALPHA/(S*OMEGA)는 문서 β 식과 동치이다. |
| KF2-020 | B | B (AD2) | B | 아니오 | 2F vf_cdtcal.f:104–145; EN p.64 식 (3.129) | 문서 식의 음의 속도는 음의 시간 상한을 만든다. 코드 ABS는 양의 유량 크기를 만든다. | 이류 시간 간격은 셀 공극 체적과 여섯 면의 최대 절댓값 유량으로 제한한다. |
| KF2-022 | C | - | C | 아니오 | 2F vf_cdtcal.f:65,152–157; EN p.64 식 (3.131) | 최종 보정과 첫 스텝의 DTINIT 선택이 문서 식에 없다. | 자동 시간 간격은 전역 최솟값·DTMAX·DTMIN·1.20배 증가 제한을 반영한다. `IF (NNOW.EQ.0) W=DTINIT`를 적용한 뒤 `DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)`를 계산한다. |
| KF2-023 | C | - | C | 아니오 | 2F vf_iitime.f:38–44; EN p.64 | 문서의 권장 범위와 실제 입력 허용 범위는 별개다. | TIME AUTO 입력은 DTSAFE의 상한 1을 검사하지 않는다. 오류 조건은 `IF (DTSAFE.LT.ZERO) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')`이다. |
| KF2-027 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:1190,1347–1386; EN p.61,66,68 | 흐름도의 EOS 반복 안 시각 갱신은 p.61의 같은 시각 압력 반복 설명과 모순된다. | EOS의 LL 반복 안에서는 TNOW를 증가시키지 않는다. |
| KF2-031 | A | B (AD2) | A | 아니오 | 2F vf_zxmg_init.f:20–21; mod_comm.f90:98–100; vf_a1main.f:14,276,1113–1114; EN p.69 | AD2와 다르다. 마스크의 `CCC      CALL MPI_INIT(IERR)`가 옛 초기화 경로로 남는다. 현재 초기화는 mod_comm으로 이동했다. 2016.09 표지는 이 변경의 근거로 쓰지 않는다. | 현재 통합판은 VF_ZXMP 밖에서도 MPI를 직접 호출한다. 마스크에 주석으로 남은 `CALL MPI_INIT(IERR)`와 mod_comm의 활성 `call mpi_init(ierr)`가 초기화 경로 변경의 근거다. |
| KF2-035 | H | - | H | 아니오 | 2F vf_p3srd2.f:5,58–59; EN p.70 | 스텐실에 따른 필요 통신 폭은 수치법의 일반 설명이다. | 필요 통신 폭의 이론 설명과 실제 두 층 교환 구현을 구별한다. |
| KF2-038 | A | A (AD2) | A | 아니오 | 2F vf_hsort.f:1–3; vf_jphdm1.f:1–10; vf_jpcoef.f:1–7; 3D vf_hsort.f:1; EN p.73 | 3D 파일 목록에는 j 계열이 없다. 2F 파일 목록에는 vf_jphdm1·vf_jphdm2·vf_jpcoef가 있다. h는 두 사본에 공통이다. | 현재 3D2F 판에는 h 계열 정렬과 j 계열 HiDEM 인터페이스가 있다. 3D 사본에 없는 j 계열의 추가가 판 차이 근거다. |
| KF2-042 | H | - | H | 아니오 | 2F vf_a1main.f:22; vf_v1eos.f:16; EN p.74 | include의 오류 예방 효과는 작성 방법에 관한 일반 주장이다. | include는 공통 선언을 공유하는 작성 수단이다. 오류 예방 효과는 정적 대조 결과로 보증하지 않는다. |
| KF2-044 | B | B (AD2) | B | 아니오 | 2F vf_a2err.f:1; vf_iitime.f:64; EN p.77–78 | p.77 A2ERR은 p.78의 VF_A2ERR와도 이름이 다르다. | 오류 처리 루틴의 실제 이름은 VF_A2ERR이다. |
| KF2-046 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:1548; vf_a2err.f:68; EN p.78; JP p.68 | 일본어 문장은 정상 종료와 오류 종료를 구분한다. 영어 문장은 두 경로를 잘못 연결한다. | 정상 종료는 VF_A1MAIN 경로다. 일반 오류 종료는 VF_A2ERR 경로다. |
| KF2-047 | A | A (AD2) | A | 아니오 | 3D vf_a1main.f:231–238; 2F vf_a1main.f:13; vf_a2array.f90:1–8; EN p.79 | MAIN 사본 diff에서 배열 선언을 제거하고 모듈 사용을 추가한다. | 3D2F 전역 배열의 실제 선언 위치는 VF_A2ARRAY 모듈이다. 3D MAIN의 직접 배열 선언과 3D2F의 `use vf_a2array` 차이가 판 근거다. |
| KF2-084 | B | B (AD2) | B | 아니오 | 2F VF_A0PRM.h:14,50; EN p.81; JP p.72 | 영어판의 최대 기포 수 설명은 일본어판 영 판정값과 다르다. | ZERO는 영 판정값 1.0D-20이다. |
| KF2-085 | B | B (AD2) | B | 아니오 | 2F VF_A0PRM.h:14,51; EN p.81; JP p.72 | 일본어판의 격자 간격 영 판정값이 코드와 같다. | ZEROG는 격자 간격의 영 판정값 1.0D-6이다. |
| KF2-086 | B | B (AD2) | B | 아니오 | 2F VF_A0PRM.h:15,52; EN p.81; JP p.72 | 영어판 영 판정값과 일본어판 원주율의 번역·편집 차이다. | PI는 원주율이다. |
| KF2-097 | B | B (AD2) | B | 아니오 | 2F VF_ACOMPI.h:4,40; vf_a1main.f:1347; EN p.82; JP p.72 | MAXITER는 실제 이름 MAXITR에 E 한 글자가 더 있는 철자 오기다. | 밀도 최대 반복 횟수의 실제 변수명은 MAXITR이다. |
| KF2-102 | C | - | C | 아니오 | 2F VF_ACOMPR.h:18; vf_m1bcgs.f:111–115,249; vf_vpsol.f:70–75; EN p.83 | 문서와 주석은 우변 노름이라고만 적는다. 전처리는 실행문에서 확인한다. 인용 수정: 주석 자체가 전처리를 명시한다는 본문 번역을 고친다. | CGBNRM은 전처리 우변 M⁻¹b의 노름이다. |
| KF2-110 | B | B (AD2) | B | 아니오 | 2F VF_ACOMPR.h:26–28; EN p.83; JP p.73 | Secondary center는 일본어 2次中心을 잘못 옮긴 표현이다. | SCMVP=0.0은 2차 중심 차분이다. SCMVP=1.0은 1차 풍상 차분이다. |
| KF2-114 | A | B (AD2) | C | 예 | 2F VF_ACOMPR.h:5; VF_A0PRM.h:10; vf_a2dflt.f:69–72; vf_iiopt.f:81–87; EN p.83; JP p.73 | AD2와 다르다. 활성 초기화 길이 10만으로 옛 선언이나 문서 당시 오기를 입증할 수 없다. 문서에는 현재 입력 저장 용량 MAXWDS-3의 설명이 빠져 있다. | SPARAM의 실제 크기는 MAXWDS-3이다. 현재 상수로 125개다. 문서의 SPARAM(10)은 현재 입력 저장 용량을 모두 설명하지 않는다. |
| KF2-122 | A | A (AD2) | A | 아니오 | 2F vf_ztimec.f:35–45; vf_p1time.f:15–16; vf_zxmp_wtime.f:21; vf_a2cput.f:42–43; EN p.84 | 주석으로 남은 CPU_TIME 경로와 활성 MPI 계측 경로가 다르다. | CPUS는 현재 MPI 판에서 경과시간 차를 합산한다. `C     CALL CPU_TIME(E)`로 남은 CPU 시간 계측 경로가 판 차이 근거다. |
| KF2-123 | A | F (AD2) | 일치 | 예 | 2F vf_a2cput.f:34–35; vf_ztimec.f:42–44; EN p.84; JP p.73 | AD2와 다르다. 문서의 타이머 시작 시각이라는 정의는 코드와 그대로 같다. 다른 수식이나 표기 변환도 없다. | CPUW는 타이머 시작 시각을 저장한다. 현재 MPI 경로에서는 MPI_WTIME 계측값을 저장한다. |
| KF2-126 | B | B (AD2) | B | 아니오 | 2F VF_ADBGR.h:1,5,9; vf_a1main.f:18; EN p.85 | 표 제목 Real과 형 I*4가 같은 문서 안에서 모순된다. | RDBGF는 R*8 실수다. |
| KF2-127 | B | B (AD2) | B | 아니오 | 2F VF_ADBGR.h:1,5,10–13; vf_a1main.f:18; EN p.85 | 표 제목 Real과 I*4가 모순된다. 암시적 형 선언은 R로 시작하는 배열을 실수로 정한다. | RDBGTD(3)는 x·y·z 속도를 저장하는 R*8 실수 배열이다. |
| KF2-139 | A | B (AD2) | B | 예 | 2F VF_AFILEI.h:4,42; 3D VF_AFILEI.h:4; EN p.86–87; JP p.75 | 영어판만 21을 적는다. 일본어판 19는 3D2F 선언과 같다. | 3D2F의 ILPON 크기는 19다. 3D 사본의 크기는 21이다. |

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| KF2-142 | B | B (AD2) | B | 아니오 | 2F VF_AFILEI.h:85–95; vf_iifile.f:164–182; EN p.87 | 도형 파일 항목 안의 list file 설명이 문서 내부에서 모순된다. 코드 주석도 リストファイル로 적혀 있으나 실제 FILE GRP AREA 경로는 도형 출력 영역을 설정한다. | IGRARA(6)는 도형 파일 출력 영역의 시작·끝 셀 번호다. |
| KF2-148 | B | B (AD2) | B | 아니오 | 2F VF_AFILEI.h:114–117; EN p.88; JP p.77 | 영어판은 출력 방법 선택값을 반복한다. 일본어판의 시작·종료·간격은 코드 주석과 같다. | ITRTRN(3)은 시계열 출력 시작 스텝·종료 스텝·간격이다. |
| KF2-150 | B | B (AD2) | B | 아니오 | 2F VF_AFILEI.h:119–132; EN p.88–89; JP p.77 | 영어판의 power는 다음 쪽의 force 및 일본어판 波力와 모순된다. | ITRPRM 계산 방법 11은 장애물 파력을 뜻한다. |
| KF2-171 | A | A (AD2) | A | 아니오 | 2F VF_ANUMBI.h:1,12–13; vf_cgindx.f:67,232–237; vf_a1main.f:1209–1217; 3D↔2F VF_ANUMBI.h diff; EN p.93 | 3D/3D2F diff에서 이동 장애물용 NUMB0가 추가된다. 활성 경로는 NUMB를 갱신한 뒤 경계 배열을 다시 할당한다. | NUMB는 이동 장애물 처리 중 바뀔 수 있다. 3D/3D2F VF_ANUMBI.h의 NUMB0 추가 구간이 판 차이 근거다. |
| KF2-203 | B | B (AD2) | B | 아니오 | 2F VF_APHYSI.h:1,10–21; EN p.95 | 문서가 첫 차원을 2로 적으면서 같은 표에서 첫 첨자 3과 4를 설명한다. | IBCTYP의 실제 크기는 (4,4)다. |
| KF2-206 | A | A (AD2) | A | 아니오 | 2F VF_APHYSR.h:1,20–39; 3D↔2F VF_APHYSR.h 선언부 diff; EN p.97 | 3D의 스칼라 선언이 3D2F에서 두 상의 배열 선언으로 바뀐다. | 3D2F의 UINI는 액상과 기상의 두 값을 저장한다. 3D/3D2F VF_APHYSR.h에서 UINI의 스칼라가 UINI(2)로 바뀐 구간이 판 차이 근거다. |
| KF2-207 | A | A (AD2) | A | 아니오 | 2F VF_APHYSR.h:1,20–39; 3D↔2F VF_APHYSR.h 선언부 diff; EN p.97 | 3D의 스칼라 선언이 3D2F에서 두 상의 배열 선언으로 바뀐다. | 3D2F의 VINI는 액상과 기상의 두 값을 저장한다. 3D/3D2F VF_APHYSR.h에서 VINI의 스칼라가 VINI(2)로 바뀐 구간이 판 차이 근거다. |
| KF2-208 | A | A (AD2) | A | 아니오 | 2F VF_APHYSR.h:1,20–39; 3D↔2F VF_APHYSR.h 선언부 diff; EN p.97 | 3D의 스칼라 선언이 3D2F에서 두 상의 배열 선언으로 바뀐다. | 3D2F의 WINI는 액상과 기상의 두 값을 저장한다. 3D/3D2F VF_APHYSR.h에서 WINI의 스칼라가 WINI(2)로 바뀐 구간이 판 차이 근거다. |
| KF2-209 | A | A (AD2) | A | 아니오 | 2F VF_APHYSR.h:2,20–39; 3D↔2F VF_APHYSR.h 선언부 diff; EN p.97 | 3D의 스칼라 선언이 3D2F에서 두 상의 배열 선언으로 바뀐다. | 3D2F의 RHO0는 액상과 기상의 두 값을 저장한다. 3D/3D2F VF_APHYSR.h에서 RHO0의 스칼라가 RHO0(2)로 바뀐 구간이 판 차이 근거다. |
| KF2-210 | A | A (AD2) | A | 아니오 | 2F VF_APHYSR.h:2,20–39; 3D↔2F VF_APHYSR.h 선언부 diff; EN p.97 | 3D의 스칼라 선언이 3D2F에서 두 상의 배열 선언으로 바뀐다. | 3D2F의 ANU0는 액상과 기상의 두 값을 저장한다. 3D/3D2F VF_APHYSR.h에서 ANU0의 스칼라가 ANU0(2)로 바뀐 구간이 판 차이 근거다. |
| KF2-215 | A | A (AD2) | A | 아니오 | 2F VF_APHYSR.h:3,20–39; 3D↔2F VF_APHYSR.h 선언부 diff; EN p.97 | 3D의 스칼라 선언이 3D2F에서 두 상의 배열 선언으로 바뀐다. | 3D2F의 AKINIK는 액상과 기상의 두 값을 저장한다. 3D/3D2F VF_APHYSR.h에서 AKINIK의 스칼라가 AKINIK(2)로 바뀐 구간이 판 차이 근거다. |
| KF2-216 | A | A (AD2) | A | 아니오 | 2F VF_APHYSR.h:3,20–39; 3D↔2F VF_APHYSR.h 선언부 diff; EN p.97 | 3D의 스칼라 선언이 3D2F에서 두 상의 배열 선언으로 바뀐다. | 3D2F의 AKINIE는 액상과 기상의 두 값을 저장한다. 3D/3D2F VF_APHYSR.h에서 AKINIE의 스칼라가 AKINIE(2)로 바뀐 구간이 판 차이 근거다. |
| KF2-252 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:47–51,351; VF_A0PRM.h:10; EN p.101 | 문서의 (84,J)는 같은 표의 여섯 성분 범위와 모순되는 철자 오기다. | YY의 역격자 폭 성분 번호는 (4,J)다. |
| KF2-270 | A | A (AD2) | A | 아니오 | 2F vf_a2array.f90:23; vf_a1main.f:548; 3D↔2F vf_a1main.f 배열 선언부 diff; EN p.103 | 3D의 일차원 경계값 배열이 3D2F의 상별 이차원 배열로 바뀐다. | 3D2F의 BCU 실제 크기는 (NUMB,3)이다. 3D vf_a1main.f의 BCU 일차원 선언과 3D2F vf_a2array.f90의 이차원 선언 차이가 판 근거다. |
| KF2-271 | A | A (AD2) | A | 아니오 | 2F vf_a2array.f90:23; vf_a1main.f:549; 3D↔2F vf_a1main.f 배열 선언부 diff; EN p.103 | 3D의 일차원 경계값 배열이 3D2F의 상별 이차원 배열로 바뀐다. | 3D2F의 BCV 실제 크기는 (NUMB,3)이다. 3D vf_a1main.f의 BCV 일차원 선언과 3D2F vf_a2array.f90의 이차원 선언 차이가 판 근거다. |
| KF2-272 | A | A (AD2) | A | 아니오 | 2F vf_a2array.f90:23; vf_a1main.f:550; 3D↔2F vf_a1main.f 배열 선언부 diff; EN p.103 | 3D의 일차원 경계값 배열이 3D2F의 상별 이차원 배열로 바뀐다. | 3D2F의 BCW 실제 크기는 (NUMB,3)이다. 3D vf_a1main.f의 BCW 일차원 선언과 3D2F vf_a2array.f90의 이차원 선언 차이가 판 근거다. |
| KF2-273 | A | A (AD2) | A | 아니오 | 2F vf_a2array.f90:23; vf_a1main.f:551; 3D↔2F vf_a1main.f 배열 선언부 diff; EN p.103 | 3D의 일차원 경계값 배열이 3D2F의 상별 이차원 배열로 바뀐다. | 3D2F의 BCP 실제 크기는 (NUMB,3)이다. 3D vf_a1main.f의 BCP 일차원 선언과 3D2F vf_a2array.f90의 이차원 선언 차이가 판 근거다. |
| KF2-275 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:93,553; vf_a2array.f90:24; EN p.103; JP p.92 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 BCVI는 속도 경계의 벽면 거칠기이다. |
| KF2-276 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:94,383; vf_a2array.f90:28; EN p.103; JP p.92 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 TBUB는 기포 상승 처리를 마지막으로 수행한 시각이다. |
| KF2-277 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:95,384; vf_a2array.f90:29; EN p.103; JP p.92 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 DROPTX는 x 자유낙하 처리를 마지막으로 수행한 시각이다. |
| KF2-278 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:96,385; vf_a2array.f90:29; EN p.103; JP p.92 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 DROPTY는 y 자유낙하 처리를 마지막으로 수행한 시각이다. |
| KF2-279 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:97,386; vf_a2array.f90:30; EN p.103; JP p.92 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 DROPTZ는 z 자유낙하 처리를 마지막으로 수행한 시각이다. |
| KF2-280 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:98,387; vf_a2array.f90:30; EN p.103; JP p.92 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 DROPUU는 x 자유낙하 속도이다. |
| KF2-281 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:99,388; vf_a2array.f90:31; EN p.103; JP p.92 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 DROPVV는 y 자유낙하 속도이다. |
| KF2-282 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:100,389; vf_a2array.f90:31; EN p.103; JP p.92 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 DROPWW는 z 자유낙하 속도이다. |
| KF2-283 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:101,656; vf_a2array.f90:32; EN p.103; JP p.92 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 GGVOLD는 전 시각 블록의 공극률이다. |
| KF2-284 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:102,657; vf_a2array.f90:32; EN p.103; JP p.92 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 GGVNOW는 현재 시각 블록의 공극률이다. |
| KF2-285 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:108,681; vf_a2array.f90:36; EN p.103; JP p.92 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 GGV0는 시간 의존 공극률이다. |
| KF2-286 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:109,682; vf_a2array.f90:36; EN p.103; JP p.92 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 GLV0는 시간 의존 셀 관성 계수이다. |
| KF2-287 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:111,391; vf_a2array.f90:37; EN p.103; JP p.92 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 ANUT는 와점성계수이다. |

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| KF2-288 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:112,392; vf_a2array.f90:37; EN p.103; JP p.93 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 AK는 난류에너지이다. |
| KF2-289 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:113,393; vf_a2array.f90:37; EN p.103; JP p.93 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 AE는 난류에너지 소산율이다. |
| KF2-290 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:114,555; vf_a2array.f90:38; EN p.104; JP p.93 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 BCK는 난류에너지 경계값이다. |
| KF2-291 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:115,556; vf_a2array.f90:38; EN p.104; JP p.93 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 BCE는 난류에너지 소산율 경계값이다. |
| KF2-292 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:116,396; vf_a2array.f90:40; EN p.104; JP p.93 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 TT는 온도이다. |
| KF2-293 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:117,397; vf_a2array.f90:40; EN p.104; JP p.93 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 ALM는 열전도율과 난류 열전도율의 합이다. |
| KF2-294 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:118,559; vf_a2array.f90:41; EN p.104; JP p.93 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 BCT는 온도 경계값이다. |
| KF2-295 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:119–121,560; vf_a2array.f90:42; EN p.104; JP p.93 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 BCTI는 열전달계수 또는 열유속과 외부 온도이다. |
| KF2-296 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:122,400; vf_a2array.f90:43; EN p.104; JP p.93 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 CC는 농도이다. |
| KF2-297 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:123,401; vf_a2array.f90:43; EN p.104; JP p.93 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 DD는 분자 확산계수와 난류 확산계수의 합이다. |
| KF2-298 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:124,563; vf_a2array.f90:44; EN p.104; JP p.93 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 BCC는 농도 경계값이다. |
| KF2-299 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:125–127,564; vf_a2array.f90:45; EN p.104; JP p.93 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 BCCI는 물질전달계수 또는 확산유속과 외부 농도이다. |
| KF2-300 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:128,719; vf_a2array.f90:46; EN p.104; JP p.93 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 DMTBTT는 행렬 자료의 무차원 위상이다. |
| KF2-301 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:129,724; vf_a2array.f90:47; EN p.104; JP p.93 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 DMTBZZ는 평균 수위를 0으로 한 행렬 자료 z 좌표이다. |
| KF2-302 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:130,721; vf_a2array.f90:48; EN p.104; JP p.93 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 DMTBHH는 행렬 자료 수위이다. |
| KF2-303 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:131,725; vf_a2array.f90:49; EN p.104; JP p.93 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 DMTBUN는 행렬 자료 수평 유속이다. |
| KF2-304 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:132,726; vf_a2array.f90:50; EN p.104; JP p.94 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 DMTBUT는 행렬 자료 수직 유속이다. |
| KF2-305 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:133,403; vf_a2array.f90:51; EN p.104; JP p.94 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | 코드의 DBUF는 실수 병렬 버퍼이다. |
| KF2-306 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:135,404–421; vf_a2array.f90:54–59; EN p.104; JP p.94 | 영어판 변수 설명이 행과 어긋난다. 일본어판 설명은 코드 주석·선언과 같다. | WK01–WK17은 실수 작업 배열이다. 코드에는 추가 WK18도 있다. |
| KF2-307 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:136,566,1244–1252; vf_a2array.f90:60; EN p.105; JP p.94 | 영어판 설명이 정수 셀 상태 설명으로 밀려 있다. 일본어판은 작업 배열이라고 적는다. 할당 길이에는 재할당 조건을 보충한다. | WKBC는 경계 실수 작업 배열이다. 초기 할당 길이는 NUMB*3이다. NUMB 변경 후 재할당에서 `IF (2*LEQC.GT.3) THEN`이면 길이는 2*NUMB*LEQC다. 그 외에는 NUMB*3이다. |
| KF2-308 | C | - | C | 아니오 | 2F vf_a1main.f:137–147,422; vf_cgindx.f:96–102; EN p.106 | 문서의 상태 목록에는 실제 이동 장애물 셀 값 -2가 없다. | 셀 상태의 -1·0·1–6·8과 여섯 액상 방향은 같다. 코드가 이동 장애물 셀 -2를 추가한다. 문서는 이 값을 적지 않는다. |
| KF2-309 | C | - | C | 아니오 | 2F vf_a1main.f:148–153,423; vf_cgindx.f:199–205,228–237; EN p.106 | 문서의 x 면 상태 목록에는 이동 장애물 면 값과 추가 경계 포인터 범위가 없다. | 주석의 뜻은 x 면 상태 인덱스이다. 문서에 있는 선택값·방향은 같다. 코드의 이동 장애물 값 -2와 NUMB0를 넘는 경계 포인터 설명은 문서에 없다. |
| KF2-310 | C | - | C | 아니오 | 2F vf_a1main.f:154–159,424; vf_cgindx.f:262–268,291–300; EN p.106 | 문서의 y 면 상태 목록에는 이동 장애물 면 값과 추가 경계 포인터 범위가 없다. | 주석의 뜻은 y 면 상태 인덱스이다. 문서에 있는 선택값·방향은 같다. 코드의 이동 장애물 값 -2와 NUMB0를 넘는 경계 포인터 설명은 문서에 없다. |
| KF2-311 | C | - | C | 아니오 | 2F vf_a1main.f:160–165,425; vf_cgindx.f:325–331,354–360; EN p.106 | 문서의 z 면 상태 목록에는 이동 장애물 면 값과 추가 경계 포인터 범위가 없다. | 주석의 뜻은 z 면 상태 인덱스이다. 문서에 있는 선택값·방향은 같다. 코드의 이동 장애물 값 -2와 NUMB0를 넘는 경계 포인터 설명은 문서에 없다. |
| KF2-312 | A | A (AD2) | A | 아니오 | 3D↔2F vf_cindc.f:40–49 diff; 2F vf_a1main.f:426; EN p.106 | 같은 NF=8 분기의 INDC 대입이 3D의 -1에서 3D2F의 0으로 바뀐다. | 3D2F의 VF_CINDC는 기체 셀도 계산 대상으로 설정한다. 3D/3D2F vf_cindc.f:42–43의 `INDC(I,J,K)=-1`과 `INDC(I,J,K)=0` 차이가 판 근거다. |
| KF2-313 | C | - | C | 아니오 | 2F vf_a1main.f:171–206,567; vf_iiboun.f:214–221; EN p.107–108 | 문서가 설명하는 INDB 성분은 1–4다. 실제 기상 경계 종류는 (5,L)에 저장된다. | 3D2F INDB는 액상 경계와 별도로 기상 속도·압력 경계 종류를 저장한다. |
| KF2-315 | A | A (AD2) | A | 아니오 | 3D vf_a1main.f:177; 3D↔2F vf_a1main.f 선언부 diff; 2F vf_a1main.f:209–211,569; vf_a2array.f90:65; VF_A0PRM.h:11; EN p.108 | 3D의 한 상 벡터가 3D2F에서 액상·기상 두 행의 배열로 바뀐다. | 3D2F의 INDBK는 액상·기상 경계조건을 나누어 저장한다. 첫 배열 크기는 2다. 3D vf_a1main.f의 INDBK(NUMB)와 3D2F의 두 상 선언 차이가 판 근거다. |
| KF2-316 | A | A (AD2) | A | 아니오 | 3D vf_a1main.f:185; 3D↔2F vf_a1main.f 선언부 diff; 2F vf_a1main.f:219–221,570; vf_a2array.f90:65; VF_A0PRM.h:11; EN p.108 | 3D의 한 상 벡터가 3D2F에서 액상·기상 두 행의 배열로 바뀐다. | 3D2F의 INDBE는 액상·기상 경계조건을 나누어 저장한다. 첫 배열 크기는 2다. 3D vf_a1main.f의 INDBE(NUMB)와 3D2F의 두 상 선언 차이가 판 근거다. |
| KF2-320 | B | B (AD2) | B | 아니오 | 2F vf_a2array.f90:73; vf_a1main.f:254,429; EN p.110; JP p.98 | 두 언어판 NWK01에는 실제 이름 NWK1에 없는 숫자 0이 들어간다. | 정수 작업 배열의 실제 이름은 NWK1이다. |
| KF2-327 | B | B (AD2) | B | 아니오 | 2F vf_a1main.f:70,365; user_eos.f:29–34; EN p.110; JP p.99 | 일본어판은 압력에 대한 밀도 미분이라고 적는다. 영어판은 미분 순서를 거꾸로 옮긴다. 코드의 저장 정의에는 밀도 정규화가 포함된다. | DRHODP는 (dρ/dp)/ρ를 저장한다. 단위는 1/Pa이다. |

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| KF2-328 | C | - | C | 아니오 | 2F vf_a1main.f:71,366; vf_v1eos.f:116–172; vf_vpdrdt.f:95,156; EN p.110; JP p.99 | 양 언어판의 변수 설명에는 밀도로 나누는 저장 정의가 없다. | DRHODT는 코드가 계산한 밀도 실질미분을 RHOG로 나눈 값을 저장한다. 단위는 1/s이다. 계산식의 공극률 계수 차이는 KF2-003의 결함 후보에 해당한다. |
| KF2-330 | B | B (AD2) | B | 아니오 | 2F VF_AFILEI.h:1–10; EN p.86–89,91; JP p.75 | 같은 문서에서 캡션의 총수 4와 파일 표기의 총수 3이 서로 다르다. | VF_AFILEI 표는 네 부분으로 나뉜다. 파일 표기의 1/3·2/3은 오기다. |
| KF2-331 | B | B (AD2) | B | 아니오 | 2F VF_APARAI.h:4,8–28; vf_a1main.f:18; EN p.80,93–94 | p.80의 정수 설명 및 p.93–94의 I*4와 p.93 제목 real이 서로 모순된다. | VF_APARAI의 표에 열거한 병렬 변수는 정수다. MGNAME의 문자형은 별도로 적는다. |
| KF2-334 | C | - | C | 아니오 | 2F vf_cgrid.f:43–71; EN p.101 | 일반 격자 식에는 첫 위치에서 0을 넣는 예외가 설명되지 않는다. | 첫 격자 위치의 중심 거리와 역수는 0으로 초기화한다. |
| KF2-335 | C | - | C | 아니오 | 2F vf_cglv.f:32–36; EN p.102 | 문서의 일반 식에는 비결합 장애물 셀의 예외 조건이 없다. | `IF (NF(I,J,K).LE.-1 .AND. ICPL.EQ.0 .AND. ISTM.EQ.0) THEN`에서 `GLV(I,J,K)=1.0D0`이다. 그 외에는 `GLV(I,J,K)=GGV(I,J,K)+(1.0D0-GGV(I,J,K))*CM0(I,J,K)`이다. |
| KF2-336 | C | - | C | 아니오 | 2F vf_cglxyz.f:60–94; EN p.102 | 문서의 일반 식에는 장애물 면의 예외와 CM을 선택하는 분기가 없다. | 장애물 면의 관성 계수는 1이다. x 방향에서는 `IF (INDX(I,J,K).LE.-1) THEN`이 이 조건이다. 일반 면은 `ELSEIF (INDX(I,J,K).EQ.0) THEN`에서 `CM=XX(6,I)*(XX(2,I)*CM0(I,J,K)+XX(2,I-1)*CM0(I-1,J,K))`을 쓴다. 경계면은 `ELSEIF (NF(I,J,K).GT.-1) THEN`에서 현재 셀의 CM0를 쓴다. 마지막 ELSE에서는 I-1 셀의 CM0를 쓴다. y·z 방향도 대응하는 첨자로 처리한다. |
| KF2-338 | B | B (AD2) | B | 아니오 | 2F vf_cindb.f:29–31; EN p.110; JP p.100 | 문서가 J 방향을 NUMJ로 정의하면서 예시 J 반복에는 NUMK를 사용한다. | p.110 왼쪽 예시에서 J 반복 상한은 NUMJ-1로 읽어야 한다. |
| KF2-340 | B | B (AD2) | B | 아니오 | 2F vf_cindb.f:50–52; EN p.110; JP p.100 | J 방향 크기 NUMJ와 반복 상한 NUMK가 서로 다르다. DO 110과 종료 레이블 111도 서로 다르다. | p.110 오른쪽 예시에서 J 반복 상한은 NUMJ-1이다. DO 110의 끝 레이블은 110이다. |
| KF2-341 | C | - | C | 아니오 | 2F VF_A0PRM.h:5–13,46; vf_pmginp.f:25–43; vf_cgindb.f:25; EN p.81; 2F 전체 rg -n '\bMAXM1\b' | 문서 상수 표에 파일 번호와 추가 배열 크기가 없다. MAXM1 검색 결과는 PARAMETER 한 곳과 주석 두 곳이다. | MFILEN=10은 MG 환경 파일 번호다. MFILTP=25·MFILBT=26·MFILBT2=27은 추가 파일 번호다. MAXBK1=2·MAXBE1=2·MAXM1=5·MAXPVC=500은 추가 크기 상수다. MAXM1은 PARAMETER와 주석에만 등장한다. |
| KF2-342 | C | - | C | 아니오 | 2F VF_ACOMPR.h:39–47; user_eos.f:23–34; vf_a1main.f:1355–1369; EN p.83 | 문서는 SRELAX와 EOS 매개변수의 단위를 생략한다. 보고서의 모든 셀 표현을 실제 반복 범위로 고친다. | ISTATE=1에서 SPARAM(1)은 기준압력[Pa]이다. SPARAM(2)는 기체상수[J/kg/K]다. SPARAM(3)은 온도[K]다. SRELAX는 밀도 완화계수다. `DO K=2,NUMK-1`, `DO J=MYJS,MYJE`, `DO I=MYIS,MYIE` 범위에서 `IF(NF(I,J,K).EQ.8) THEN`인 셀만 SERR에 기여한다. 같은 반복 범위의 RHOG는 NF와 무관하게 `RHOG(I,J,K) =        SRELAX *RHOG(I,J,K)`와 연속행 `     &                      + (1.0D0-SRELAX)*WK01(I,J,K)`로 완화한다. |
| KF2-343 | C | - | C | 아니오 | 2F vf_iiopt.f:81–101; vf_a2dflt.f:47–48,69–74; EN p.82–83 | 표에는 입력 키워드·선택 인수·검사·기본값이 없다. 결론에 생략된 기본값과 선택 인수 조건을 명시한다. | OPTION STATE는 ISTATE와 뒤따르는 SPARAM 값을 읽는다. ISTATE의 값 검사는 `IF (ISTATE.GT.1) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')`다. OPTION DENS-ERROR는 SERROR를 읽는다. `IF (NWD.GE.4) THEN`에서 MAXITR를 읽는다. `IF (NWD.GE.5) THEN`에서 SRELAX를 읽는다. 값 검사는 각각 `IF (SERROR.LE.ZERO) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')`, `IF (MAXITR.LE.0) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')`, `IF (SRELAX.LT.ZERO) CALL VF_A2ERR('VF_IIOPT','INVALID VALUE.')`다. 기본 ISTATE=0·MAXITR=1·SERROR=1.0D-4·SRELAX=1.0D0이다. SPARAM의 기본 세 대입은 `SPARAM(1) =1.0D5`, `SPARAM(2) =8.31451D0/0.029D0`, `SPARAM(3) =300.`이다. |
| KF2-344 | C | - | C | 아니오 | 2F VF_AFILEI.h:1–10,26–27,159–166; VF_AFILER.h:1–4,34–42; vf_a1main.f:1110–1114; EN p.86–92 | 추가 파일 제어·행위자 자료 출력·자동 재시작 시간 제한이 문서 표에 없다. | ITPFIL은 구조물 표면압력 파일 번호다. IMMFIL·IMMTYP·IMMTRN(3)·RMMTRN(4)은 행위자 자료 출력 제어다. ETIME은 자동 재시작을 위한 경과시간 상한이다. |
| KF2-345 | C | - | C | 아니오 | 2F VF_AFILEI.h:67–80; vf_ol1ini.f:470–479; vf_ol1trn.f:203–212; EN p.86–87 | 문서 목록에 ILPON(13–19)와 ILPON(6)의 GLY가 빠져 있다. | ILPON(13–19)은 온도·열전도율·농도·확산계수·난류에너지·난류 소산율·와점성계수의 출력 여부다. ILPON(6)의 실제 출력에는 GLY도 있다. 문서의 `GLV, GLX, GLZ` 열거는 GLY를 빠뜨린다. 일본어 주석의 뜻은 이 문장에 적은 일곱 물리량이다. |
| KF2-346 | C | - | C | 아니오 | 2F vf_ol1trn.f:91–104; VF_AFILER.h:12–31; EN p.91–92 | 문서에는 출력 시각 배열의 갱신 절차가 없다. 보고서 결론에 빠진 반 시간 간격을 포함한다. | 리스트 출력의 스텝 방식은 `IF (NNOW.GE.ILPTRN(1) .AND. NNOW.LE.ILPTRN(2)) THEN` 안에서 `IF (MOD(NNOW-ILPTRN(1),ILPTRN(3)).EQ.0) IO=1`을 적용한다. 시각 방식은 `IF (TNOW.GE.RLPTRN(1)-ZERO .AND. TNOW.LE.RLPTRN(2)+ZERO) THEN` 안에서 `W=(TNOW+0.5D0*DT)-RLPTRN(4)`를 계산한다. `IF (W.GE.0.0D0) THEN`이면 출력한다. 다음 출력 시각은 `RLPTRN(4)=RLPTRN(4)+DBLE(INT(W/RLPTRN(3))+1)*RLPTRN(3)`로 갱신한다. |
| KF2-347 | C | - | C | 아니오 | 2F VF_ANUMBI.h:1,12–13; vf_cgindx.f:67,232–237; vf_a1main.f:1210–1218; EN p.93 | 문서 표에 NUMB0와 이동 장애물 경계 갱신 절차가 없다. | NUMB0는 이동 장애물이 없는 경계면 수다. 현재 경계면 수 NUMB가 바뀌면 INDB를 다시 할당한다. 문서의 NUMB CNS 표기를 현재 실행 중 불변이라는 뜻으로 적용할 수 없다. |
| KF2-348 | C | - | C | 아니오 | 2F VF_APARAI.h:2–24,32–72; vf_a1main.f:18; EN p.93–94 | 추가된 변수는 모델 간 통신과 격자 관계를 저장한다. 외부 MPI 라이브러리 내부가 아니므로 C다. | MAXPRO=MAXNPI*MAXNPJ다. MGPROC·MGRANK·MGCOMM·MGARAN·MGNAME(MAXPRO)·MGNLEN(MAXPRO)·MGNPIN(MAXPRO)·MGPARE(MAXPRO)·MGAREA(MAXPRO)·MGPRNK·MGPINF(9)·MGCNUM·MGCRNK(MAXPRO)·MGCINF(9,MAXPRO)·MGCPOS(6,MAXPRO)·MYHOST·MA_RANK가 추가된다. MGNAME은 CHARACTER*(MAXCHR)다. 나머지는 정수다. 문서의 병렬 정수 블록 제목만으로 MGNAME도 정수라고 읽으면 안 된다. |
| KF2-349 | C | - | C | 아니오 | 2F vf_cpara.f:34–49,64–87,102–106; EN p.70,93–94 | 문서 변수 목록에는 분할 검사와 국소 배열 크기 산정 절차가 없다. 분할 폭 검사가 실행되는 조건을 보충한다. | `IF (NUMNPI.GT.1) THEN`에서 x 분할 폭을 2 이상으로 검사한다. `IF (NUMNPJ.GT.1) THEN`에서 y 분할 폭을 2 이상으로 검사한다. `IF (NPROCS.NE.NUMNPI*NUMNPJ)`이면 오류 처리한다. 물리 경계 가상 셀 두께는 1이다. 내부 프로세스 경계 두께는 2다. NUMI·NUMJ는 이 두께를 더한 국소 배열 크기다. NUMBUF는 max(NUMI,NUMJ)*NUMK다. |
| KF2-350 | C | - | C | 아니오 | 2F VF_APHYSI.h:1–2,40–50; VF_APHYSR.h:10–12,100; vf_fpvcip.f:207,262–274; EN p.95–98 | 문서의 물리 변수 표에 이동 장애물·기포 자료와 속도 제한값이 없다. | IPRTB(3)는 이동 장애물 경계에서 액상 속도·압력·기상 속도 조건을 저장한다. NPVCB·IPVCBC(MAXPVC)는 고립 기포 관련 인덱스다. PVCP0·PVCGM·PVCDIV·PVCPES·PVCPFS·PVCVES·PVCVFS는 고립 기포용 자료다. VVMAX는 속도 제한값[m/s]이다. IPRTB 주석의 뜻은 액상·기상 이동 장애물 경계조건이며 속도 선택 1=슬립·2=논슬립·3=이동속도 고정, 압력 선택 2=프리다. |
| KF2-351 | C | - | C | 아니오 | 2F VF_ASEABT.h:1–3; VF_ASTOCI.h:1–46; VF_ASTOCR.h:1–20; SF_STRUCT.h:1–5; EN p.79–80 | 문서의 공통 자료 목록에 지형 변화와 시뮬레이터 결합 블록이 없다. | VF_ASEABI는 지형 변화 선택 ISEABT를 저장한다. ISEABT=0은 지형 변화를 고려하지 않는다는 뜻이다. ISEABT=1은 지형 변화를 고려한다는 뜻이다. VF_ASTOCI는 STOC 결합 인덱스를 저장한다. VF_ASTOCR는 STOC에서 받는 경계 속도와 VOF를 저장한다. SF_STRUCT는 구조·토사 결합 공통 자료다. |
| KF2-352 | C | - | C | 아니오 | 2F vf_a2array.f90:5–9,18; vf_a1main.f:64–66,75,357–371,1009,1166,1187; EN p.101–110 | 문서의 배열 목록에 스태거드 VOF와 추가 압력 보관 배열이 없다. | FX·FY·FZ는 유속 정의 위치의 VOF다. PPBK는 압력 보관 배열이다. PPO는 전 시각 압력이다. 모두 R*8 3차원 배열이다. 문서의 RHOG·UUO 등 추가 표에도 이 이름은 없다. |
| KF2-353 | C | - | C | 아니오 | 2F vf_a2array.f90:25–39,52–53,68–71; vf_a1main.f:103–110,649–687; sf_str2.f:36–37; EN p.101–110; 2F 전체 rg -n GVL0 | 문서 배열 목록에 이동 장애물 관련 자료가 없다. GVL0는 선언뿐 아니라 할당·초기화가 있으므로 설명을 고친다. | BCU0·BCV0·BCW0·BCP0·BCF0·BCVI0·BCK0·BCE0는 기준 경계값 보관 배열이다. GGVEL·GGVELO·GGVELN·GGVLO·GGVLN은 이동속도 자료다. GVL0는 이동속도 배열로 주석이 달려 있다. GVL0는 `IF (IPRNT.GT.1) THEN`에서 할당되고 1.0D0으로 초기화된다. 3D2F의 GVL0 참조는 선언·주석·할당·초기화 네 곳이다. RBUF는 실수 버퍼다. PPPVC·IPVC는 기포 자료다. INDX0·INDY0·INDZ0·INDB0는 이동 장애물 이전 인덱스다. |
| KF2-354 | C | - | C | 아니오 | 2F vf_a2array.f90:59,75–95; vf_a1main.f:256–268,633–640; EN p.101–110 | 문서 배열 목록에 MG·구조·토사·지형 변화 자료와 추가 작업 배열이 없다. | XPF·YPF·ZPF·IPF·JPF·KPF는 MG 보간 자료다. DGGV·DGLV·GGV_0·GGX_0·GGY_0·GGZ_0·BCT0·BCTI0·BCC0·BCCI0·INDBK0·INDBE0·INDBT0·INDBC0는 구조 결합 보관 자료다. GGW·GGR·FLFU·FLFV·LNDC·LNDC0·LNDC_0·KST·DZ·SUMZ는 토사 결합 배열이다. WK18·WK19·WK20은 추가 작업 배열이다. DELH·DELH_IN은 지형 변화에 따른 수위 증분 배열이다. |
| KF2-355 | C | - | C | 아니오 | 2F vf_m1bcgs.f:98–108,142–165,217–223; vf_vpsol.f:76–81; EN p.63 | 문서의 해법 알고리즘에는 초기 수렴과 실패 종류별 종료 처리가 없다. | 코드는 초기 잔차 수렴도 검사한다. 불완전 분해 실패·최대 반복 초과·발산을 구별한다. 호출자는 각각 오류 종료한다. 상대·절대·발산 허용값은 제곱하여 비교한다. |
| KF2-356 | C | - | C | 아니오 | 2F vf_iicomp.f:32–110; vf_a2dflt.f:37–67; EN p.82–83 | 문서 변수 표에는 입력 구문과 기본 대입이 없다. | COMP SCHM은 VP-DONOR·FF-DN-AC·FF-SLOPE·KE-DONOR·T-DONOR·C-DONOR를 해석한다. COMP MTRX는 ILUBCGSTAB·M-ILUBCGSTAB·MAX-ITR·A-ERROR·R-ERROR를 해석한다. 각 DONOR 계수는 0 이상 1 이하로 검사한다. C-DONOR는 농도 성분 번호도 읽는다. 기본 ICGTYP=1·ICGMAX=500·CGPARA=0.95D0·CGEPSA=1.0D-15·CGEPSR=1.0D-12·CGDIV=1.0D+30이다. 기본 ISCMVP·ISCMFF·ISCMK·ISCMT·ISCMC는 0이다. 기본 SCMVP·SCMK·SCMT·SCMC는 1.0D0이다. |
| KF2-357 | C | - | C | 아니오 | 2F vf_cdtcal.f:67–98,144–145; EN p.64 | 문서의 점성 제한식에 열전도·농도 확산을 합치는 절차가 없다. 열 및 농도 항이 활성화되는 조건을 보충한다. | WK01은 ANU로 시작한다. `IF (LEQT.NE.0) THEN`에서는 ALM/(RHO2*TCP0)와의 최댓값을 취한다. `DO 190 LC=1,LEQC`에서는 각 DD와의 최댓값을 취한다. 열 제한의 혼합 밀도는 `RHO2=FF(I,J,K)*RHO0(1)+(1.0D0-FF(I,J,K))*RHO0(2)`다. RHOG를 사용하는 대체 줄은 주석이다. |
| KF2-358 | C | - | C | 아니오 | 2F vf_a1main.f:1107–1147,1347–1386; EN p.66,68 | 문서 흐름도에는 결합 시간 조정과 경과시간 상한에 따른 종료 공유가 없다. | ETIME을 넘는지 검사하고 결합 통신자에서 종료 여부를 공유한다. 구조·토사 결합으로 공극률과 시간 간격을 조정한다. 시간 간격을 LOOPS로 나눈다. 이 처리는 EOS 내부 반복 횟수와 다르다. 경과시간 판정은 `IF(WTM2-WTM1.GT.ETIME) IEND1(2)=1`이다. 세분 시간 간격은 `DTNOW=DT/DBLE(LOOPS)`다. |
| KF2-359 | E · 강함 | E · 강함 (E1) | E · 강함 | 아니오 | 2F vf_vpdrdt.f:77,93–150; vf_v1eos.f:126–138; vf_vpsol.f:30; vf_mzax.f:46–52; vf_v1cal.f:357–372; EN p.61 식 (3.127)–(3.128) | 자기 차분 주석·y/z 경로·별도 EOS 차분·행렬 곱은 모두 I+1을 지지한다. 행렬 곱에서 첨자 의미가 뒤집히는 반대 근거도 없다. ISTATE=0·WUC=0·DCOEF=0 또는 양쪽 DRHODP가 같은 경우에는 이 첨자 차이의 영향이 없지만 음의 흐름 분기는 활성 경로다. | AUI의 `AUI(I,J,K) = AUI(I,J,K) + DCOEF*DRHODP(I-1,J,K)`는 강한 첨자 결함 후보다. AUI는 I+1 미지수의 계수다. `IF(ISTATE.EQ.0) RETURN`을 통과한 뒤 `IF(NF(I,J,K).GT.0) THEN` 내부에서 `IF(WUC.GT.0.0D0) THEN`의 ELSE와 `IF(NF(I+1,J,K).GT.0) THEN`을 거쳐 실행된다. 실제 차이는 WUC가 음수이고 DCOEF가 0이 아니며 I-1과 I+1의 DRHODP가 다를 때 생긴다. 자기 차분 주석·y/z 경로·별도 EOS 차분·행렬 곱은 I+1을 지지한다. |
| KF2-360 | E · 강함 | E · 중간 (E1) | E · 중간 | 예 | 2F vf_v1eos.f:63–105; vf_fnfprv.f:162–189; vf_cindc.f:39–49; vf_a1main.f:977,1351,1363–1364; 3D↔2F vf_fnfprv.f diff; EN p.61,106 | 자기 주석은 기체 셀에서 채운다고 적는다. 문서 NF 방향과 VF_FNFPRV의 실제 분류는 복사 원점이 액체 쪽임을 입증한다. 사본 diff에도 방향 반전은 없다. 액체 셀 EOS 계산과 여섯 방향의 일관된 복사는 단순 첨자 실수라는 해석을 약화한다. 해당 경로에는 액체 방향 복사의 설계 목적을 명시한 근거가 없다. E1의 중간 강도를 채택한다. | 표면 셀의 기상 밀도·압력 미분 복사 방향은 중간 강도의 코드 결함 후보다. 자기 주석 `C 表面セルの気相密度は、気体セルから埋め込む`는 기체 셀에서 채운다는 뜻이다. `IF     (NF(I,J,K).EQ.1) THEN`에서 실제 대입은 `RHOG(I,J,K)   = RHOG  (I-1,J,K)`와 `DRHODP(I,J,K) = DRHODP(I-1,J,K)`다. NF=1의 I-1은 액체 방향이다. 다른 다섯 방향도 액체 방향에서 복사한다. 액체 셀에도 EOS를 계산하므로 복사 원점은 계산된 값이다. `IF(ISTATE.EQ.0) RETURN`이면 이 복사에 도달하지 않는다. |
| KF2-361 | C | - | C | 아니오 | 2F vf_iitime.f:31–60; vf_a2dflt.f:229–242; EN p.64,99–100 | 문서 변수 표에는 입력 구문과 기본 대입이 없다. | TIME CONST는 DTCNST 하나를 읽는다. TIME AUTO는 DTINIT·DTSAFE를 읽는다. TIME LIMIT는 DTMIN·DTMAX를 읽는다. TIME END는 NEND·TEND를 읽는다. 기본 방식은 AUTO다. 기본 DTCNST=1.0D-3·DTINIT=1.0D-6·DTMIN=ZERO·DTMAX=1.0D0/ZERO·DTSAFE=1.0D-1이다. 종료 스텝과 종료 시각은 0이다. |
| KF2-362 | C | - | C | 아니오 | 2F vf_bwuwn.f:75–78; vf_bwuwt.f:48–51; vf_bwuwg.f:47–50; vf_pmginp.f:139–184; mod_fault.f:259–271; EN p.78; 2F .f·.f90에 rg -n -i '^ *stop\b' | 검색에서 MAIN·VF_A2ERR 외에도 경계 루틴 세 파일·MG 입력 파일·단층 계산 파일의 STOP이 나온다. 화면 메시지가 아니라 모델 실행을 종료하는 제어문이다. | MAIN·VF_A2ERR 이외의 경계 루틴·MG 입력·단층 계산도 STOP을 가진다. VF_BWUWN·VF_BWUWT는 `IF (NUMB0.LE.0) THEN`에서 직접 STOP한다. VF_BWUWG는 `IF (NUMB0.LT.0 .OR. NUMB0.GT.NUMB) THEN`에서 직접 STOP한다. VF_PMGINP는 오류 경로에서 VF_A2CLOS와 VF_P0ENDA를 호출한 뒤 STOP한다. mod_fault.f의 EN2LB는 뉴턴 반복의 `ELSEIF( N==10 ) THEN`에서 STOP한다. |
| KF2-363 | C | - | C | 아니오 | 2F vf_bwuwn.f:96–101,199–208; vf_a1main.f:181,197; EN p.103 | 문서는 NUMB 벡터만 적는다. 실제 상별 열 선택과 혼합 경계식이 설명되지 않는다. | 열 1은 혼합 경계값이다. 열 2는 액상 값이다. 열 3은 기상 값이다. 같은 모양을 BCV·BCW도 사용한다. 문서의 NUMB 벡터 설명은 세 열의 결합식을 적지 않는다. x 방향 식은 `BCU(L,1) =BCF(L)*BCU(L,2)+(1.0D0-BCF(L))*BCU(L,3)`이다. |

대상 121행: 유지 117, 변경 4
