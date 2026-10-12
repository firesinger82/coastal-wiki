# ADCIRC 차이 결론 반영

작성일: 2026-10-12.

다섯 대조 보고서의 §5를 반영했다. 각 행의 `[10-12 ...]` 표시를 최종 결론으로 사용했다. 결론 문장과 근거 원문 인용을 ADCIRC 노트에 옮겼다.

아래 개수는 §5의 행 ID를 펼쳐 센 값이다. 묶음 수는 §5 표의 물리적 행 수다. 기존 노트의 재인용과 결함 후보 표의 재인용은 반영 행 수에 중복으로 더하지 않았다.

## 보고서별 반영 행 수

| 보고서 | §5 대상 행 ID 수 | 반영 행 ID 수 | 반영 묶음 수 | 제외 X | 제외 G | E 행 ID 수 | E 묶음 수 |
|---|---:|---:|---:|---:|---:|---:|---:|
| [ADCIRC-fort15-vs-code.md](../compare/ADCIRC-fort15-vs-code.md#5-차이-결론) | 330 | 330 | 150 | 0 | 0 | 15 | 8 |
| [ADCIRC-inputfiles-vs-code.md](../compare/ADCIRC-inputfiles-vs-code.md#5-차이-결론) | 211 | 211 | 113 | 0 | 0 | 13 | 12 |
| [ADCIRC-outputs-vs-code.md](../compare/ADCIRC-outputs-vs-code.md#5-차이-결론) | 820 | 819 | 136 | 0 | 1 | 35 | 22 |
| [ADCIRC-theory-vs-code.md](../compare/ADCIRC-theory-vs-code.md#5-차이-결론) | 324 | 324 | 114 | 0 | 0 | 5 | 3 |
| [ADCIRC-features-vs-code.md](../compare/ADCIRC-features-vs-code.md#5-차이-결론) | 276 | 272 | 186 | 4 | 0 | 14 | 7 |
| 합계 | 1961 | 1956 | 699 | 4 | 1 | 82 | 52 |

기존 표의 434행에 결론 열을 붙였다. 가까운 기존 절에 결론 문장 504행을 추가했다. 이 두 개수는 반영한 노트의 편집 위치 수다. 하나의 보고서 묶음이 여러 노트에 있으면 편집 위치 수에는 각각 포함한다.

## 넣지 않은 X·G 행

이 목록의 행에는 이번 결론을 노트에 추가하지 않았다. 다음 반영 단계의 대상으로 남겼다.

| 보고서 | §5 줄 | 행 ID | 분류 | 항목 |
|---|---:|---|---|---|
| ADCIRC-outputs-vs-code.md | 1665 | L1446 | G 근거 부족 | N01 · binary 거부의 최초 판 |
| ADCIRC-features-vs-code.md | 854 | T09 (423줄) | X 외부 원문 대조 중 | Bell 이론과 IT_Fric 입력 생성식의 대응 |
| ADCIRC-features-vs-code.md | 883 | F17 (542줄)<br>F19 (544줄)<br>C33 (682줄) | X 외부 원문 대조 중 | UNESCO 다항식의 S*T³ 계수 부호 |

## 코드 결함 후보 절

절 본문은 `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md`에 있다. 모델 README는 이 절로 연결한다.

표 행 수는 54행이다. §5의 E 묶음 52행을 모두 포함했다. E 묶음의 원래 행 ID 수는 다섯 보고서에서 합계 82행이다. 사용자 지정 보충 후보 2행을 추가했다.

같은 원인을 공유한 보고서 묶음도 출처 보고서별로 유지했다. 예를 들어 inputfiles의 WEIR-06과 features의 B69·B70·K11·C12는 같은 분 단독 시간 검사에 대한 별도 묶음이다. 54행은 고유 결함 개수가 아니다.

최종 E 행의 근거에서 의도된 변경 주석으로 모순이 해소되는 행은 확인하지 않았다. 최종 §5에서 E가 아닌 행은 이 표에 넣지 않았다.

| 사용자 지정 후보 | 처리 | 반영 위치 |
|---|---|---|
| netcdfio.F90:1272–1276의 u 단위 두 번 설정 | outputs의 L593·L594·L1504 E 묶음에 이미 있으므로 해당 행으로 반영했다. | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:134` |
| netcdfio.F90:1267의 NWS=7 응력 속도 단위 속성 | 원문을 열어 확인한 뒤 보충 행으로 반영했다. | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:158` |
| mesh.F:1249–1261의 XDMF 파이프 경계 배열 혼용 | 원문을 열어 확인한 뒤 보충 행으로 반영했다. | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:159` |

결함 후보 절의 제목 위치는 `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:100`이다. README의 링크 위치는 `models/ADCIRC/README.md:11`이다.

## 반영 위치

각 표 행은 보고서 §5의 묶음 하나다. 위치는 최종 수정 파일의 줄 번호다. 결함 후보 표의 재인용 위치도 함께 적었다.

### ADCIRC-fort15-vs-code.md

| §5 줄 | 보고서 행 ID | 항목 | 결론 | 반영 위치(노트:줄) |
|---:|---|---|---|---|
| 901 | L60, L61 | RUNDES·RUNID 길이 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:349` (결론 문장) |
| 902 | L62 | NFOVER와 수위 한계 설정 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:350` (결론 문장) |
| 903 | L64 | NSCREEN의 정수 간격 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:351` (결론 문장) |
| 904 | L66 | 음수 ICS | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:352` (결론 문장) |
| 905 | L67, L644, L646 | 폐기한 IM=20·30 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:235` (기존 표의 결론 열) |
| 906 | L68 | IDEN의 첫 위치 입력 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:353` (결론 문장) |
| 907 | L69, L100, L101, L102, L675, C03 (L841) | NOLIBF=3과 마찰 속성 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:236` (기존 표의 결론 열) |
| 908 | L70, L676, L682 | NOLIFA=3 및 H0 읽기 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:354` (결론 문장) |
| 909 | L75, L76, L679, L680 | Cartesian의 NCOR·NTIP 조합 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:355` (결론 문장) |
| 910 | L77, L345, C19 (L857) | NWS13 개요의 forcing 종류 | B 문서 오기 | `models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md:172` (결론 문장)<br>`models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md:116` (결론 문장) |
| 911 | L78 | NRAMP=0의 DRAMP 줄 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:356` (결론 문장) |
| 912 | L80, L714 | TAU0의 ignored 적용 범위 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:238` (기존 표의 결론 열) |
| 913 | L81, L82, L716, C02 (L840) | TAU0=-5.x의 필수 줄과 제한 순서 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:238` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:21` (결론 문장) |
| 914 | L104 | ESLM 읽기 조건과 IM=10 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:357` (결론 문장) |
| 915 | L106 | CORI의 위치 입력 조건 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:237` (기존 표의 결론 열) |
| 916 | L129, L130 | IBTYPE=52의 QNAM·QNPH | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:358` (결론 문장) |
| 917 | L138, L471, L472, L473, L474, L475, L476, L477, L478 | WTIMINC의 NWS=11 예외와 NWS=30 필수 토큰 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:256` (기존 표의 결론 열) |
| 918 | L140 | RSTIMINC의 읽기 조건 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:359` (결론 문장) |
| 919 | L141 | NWS=29 계열의 얼음 시간 간격 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:106` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:360` (결론 문장) |
| 920 | L145, L146, L147, L148, L149, L150, L362, L363, L364, L365, L366, L367, L368, L369 | NWS=3 계열의 두 입력 줄 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:253` (기존 표의 결론 열) |
| 921 | L151, L152, L153, L154, L155, L156, L394, L395, L396, L397 | NWS=7의 구조 격자 입력 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:254` (기존 표의 결론 열) |
| 922 | L166 | DRAMP의 시간 원점 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:361` (결론 문장) |
| 923 | L167 | FluxSettlingTime 적용과 종료 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:362` (결론 문장) |
| 924 | L180, L187, L201, L208, L212, L220, L293, L300, L307, L314, L318, L322, C07 (L845) | 시계열 binary 폐기와 출력 형식 확장 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:239` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:240` (기존 표의 결론 열) |
| 925 | L181, L182, L188, L189, L202, L203, L209, L210, L213, L214, L217, L218, L221, L222, L234, L235 | 출력·조화 분석 시간의 STATIM 기준 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:363` (결론 문장) |
| 926 | L184, L191, L198, L205 | 외부 관측소 파일명 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:364` (결론 문장) |
| 927 | L185, L186, L192, L193, L199, L200, L206, L207 | 계산 영역 밖 관측소 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:365` (결론 문장) |
| 928 | L194, L216 | 농도 출력 파일과 지원 형식 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:366` (결론 문장) |
| 929 | L238, C12 (L850) | NHSTAR 추가 선택 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:177` (결론 문장) |
| 930 | L240 | ITITER와 실제 솔버 선택 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:241` (기존 표의 결론 열) |
| 931 | L242 | CONVCR의 상대 정지 검사 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:367` (결론 문장) |
| 932 | L244, L245, L246, L247 | 조화 분석 형식 2–5와 보정 경고 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:368` (결론 문장) |
| 933 | L254, L255 | ISLIP=1/3의 VSSOL 하상 마찰 재설계 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:369` (결론 문장) |
| 934 | L257 | Manning 속성 이름 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:370` (결론 문장) |
| 935 | L261 | IEVC=22·23 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:371` (결론 문장) |
| 936 | L265 | RES_BC_FLAG=1 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:372` (결론 문장) |
| 937 | L266, L269 | 여섯 자리 3D baroclinic 경계·상태방정식 입력 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:373` (결론 문장) |
| 938 | L267, L281 | 음수 RES_BC_FLAG의 열 경계 시간 줄 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:374` (결론 문장) |
| 939 | L268 | SPONGEDIST 출력 활성 조건 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:375` (결론 문장) |
| 940 | L270 | 중복 TTBCTIMEINC 단독 줄 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:376` (결론 문장) |
| 941 | L271 | NTF 위치 입력 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:377` (결론 문장) |
| 942 | L275, L277, L279 | 3D 해양 경계 시간의 NOPE 조건 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:378` (결론 문장) |
| 943 | L276, L278, L280, L282 | 경계 시작 시각의 단위 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:242` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:243` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:244` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:245` (기존 표의 결론 열) |
| 944 | L296, L310 | 3D 출력 간격 설명의 잘못된 변수 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:379` (결론 문장) |
| 945 | L298, L299, L305, L306, L312, L313 | 3D 관측소 좌표 줄의 읽기 조건 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:380` (결론 문장) |
| 946 | L302 | TO3DFVF와 TO3DSVF의 위치 이름 | F 표기 차이 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:381` (결론 문장) |
| 947 | L343, L346 | NWS 음수 허용 검사와 -19의 실행 경로 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:107` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:382` (결론 문장) |
| 948 | L344, C16 (L854) | NWS=-14의 OWI 결합 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:119` (결론 문장) |
| 949 | L348 | NCICE와 음수 NWS의 호환 검사 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:108` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:383` (결론 문장) |
| 950 | L349 | NRS=5 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:384` (결론 문장) |
| 951 | L406 | NWS=9의 폐기 표시 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:255` (기존 표의 결론 열) |
| 952 | L491, L773 | SWANTimeControl.RunStartDateTime | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:385` (결론 문장) |
| 953 | L493, C22 (L860) | 얼음 항력 이름과 초기 허용 검사 | E 코드 결함 후보 | `models/ADCIRC/manual-notes/19-ice-coverage.md:120` (결론 문장)<br>`models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:109` (코드 결함 후보 표) |
| 954 | L495 | rhoAir 기본값 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:246` (기존 표의 결론 열) |
| 955 | L496 | invertedBarometerOnElevationBoundary의 namelist 소속 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:248` (기존 표의 결론 열) |
| 956 | L497, L774 | metControl.nPowellSearchDomains | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:386` (결론 문장) |
| 957 | L498 | subdomainOn 생략 기본값 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:110` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:387` (결론 문장) |
| 958 | L502, L775 | wetDryControl.StatPartWetFix | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:388` (결론 문장) |
| 959 | L503, L776 | wetDryControl.How2FixStatPartWet | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:389` (결론 문장) |
| 960 | L504, L777 | wetDryControl.slim | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:390` (결론 문장) |
| 961 | L505, L778 | wetDryControl.windlim | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:391` (결론 문장) |
| 962 | L506, L779 | wetDryControl.directvelWD | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:392` (결론 문장) |
| 963 | L507, L780 | wetDryControl.useHF | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:393` (결론 문장) |
| 964 | L511, L781 | VEW1DChannelControl.BARMIN64_SUBM | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:394` (결론 문장) |
| 965 | L512, L782 | VEW1DChannelControl.BARMIN64_NOSUBM | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:395` (결론 문장) |
| 966 | L513, L783 | VEW1DChannelControl.BARMIN64_SLIM | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:396` (결론 문장) |
| 967 | L514, L784 | VEW1DChannelControl.BARSLIM64_ELEM | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:397` (결론 문장) |
| 968 | L515, L785 | VEW1DChannelControl.BARSLIM64_EDGE | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:398` (결론 문장) |
| 969 | L518, L519, L520, L521 | TVWControl의 출력 일정 상속 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:111` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:249` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:250` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:251` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:252` (기존 표의 결론 열) |
| 970 | L523, L786 | dynamicWaterLevelCorrectionControl.dynamicWaterLevelCorrectionMethod | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:399` (결론 문장) |
| 971 | L533 | CAliDisp의 후속 IM 설정 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:400` (결론 문장) |
| 972 | L540 | densityForcingType의 대소문자 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:401` (결론 문장) |
| 973 | L542, C17 (L855), C18 (L856) | NWS13ColdStartString 필수값 검사 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:112` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md:173` (결론 문장)<br>`models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md:117` (결론 문장) |
| 974 | L545, L787 | subgridControl.subgridFilename | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:402` (결론 문장) |
| 975 | L546, L788 | subgridControl.level0 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:403` (결론 문장) |
| 976 | L547, L789 | subgridControl.level1 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:404` (결론 문장) |
| 977 | L548, L790 | subgridControl.phi_time_derivative | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:405` (결론 문장) |
| 978 | L549, L791 | WindGrib2NetCdf.read_NWS14_NetCdf_using_core_0 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:406` (결론 문장) |
| 979 | L550, L792 | InterpInset.UseInterpInset | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:407` (결론 문장) |
| 980 | L551, L793 | InterpInset.PFile_inset | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:408` (결론 문장) |
| 981 | L552, L794 | InterpInset.Wfile_inset | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:409` (결론 문장) |
| 982 | L553, L795 | InterpInset.InsetControlFile | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:410` (결론 문장) |
| 983 | L554, L796 | TidalPotentialControl.UseFullTIPFormula | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:411` (결론 문장) |
| 984 | L555, L797 | TidalPotentialControl.TIPOrder | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:412` (결론 문장) |
| 985 | L556, L798 | TidalPotentialControl.TIPStartDate | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:413` (결론 문장) |
| 986 | L557, L799 | TidalPotentialControl.MoonSunPositionComputeMethod | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:414` (결론 문장) |
| 987 | L558, L800 | TidalPotentialControl.MoonSunCoordFile | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:415` (결론 문장) |
| 988 | L559, L801 | TidalPotentialControl.IncludeNutation | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:416` (결론 문장) |
| 989 | L560, L802 | TidalPotentialControl.k2Value | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:417` (결론 문장) |
| 990 | L561, L803 | TidalPotentialControl.h2Value | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:418` (결론 문장) |
| 991 | L562, L804 | TidalPotentialControl.UniformResMoonSunTimeData | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:419` (결론 문장) |
| 992 | L566 | Smag_Control 예제의 활성 플래그 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:420` (결론 문장) |
| 993 | L569, L591, L805 | WaveWindMultiplier의 정확한 철자 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:247` (기존 표의 결론 열) |
| 994 | L570, L806 | waveCoupling.Limit_WaveStressGrad | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:421` (결론 문장) |
| 995 | L571, L807 | waveCoupling.WaveStressGrad_Cap | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:422` (결론 문장) |
| 996 | L572, L808 | baroclinic3D.iterateEqnState2 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:423` (결론 문장) |
| 997 | L573, L809 | baroclinic3D.densityIntegration | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:424` (결론 문장) |
| 998 | L574, L810 | baroclinic3D.verticalInterpolationScheme | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:425` (결론 문장) |
| 999 | L575, L811 | baroclinic3D.useLeithViscosity | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:426` (결론 문장) |
| 1000 | L576, L812 | baroclinic3D.lambdaLeith | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:427` (결론 문장) |
| 1001 | L577, L813 | baroclinic3D.viscosityOperator | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:428` (결론 문장) |
| 1002 | L578, L814 | baroclinic3D.diffusionOperator | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:429` (결론 문장) |
| 1003 | L579, L815 | baroclinic3D.useAdaptiveFilter | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:430` (결론 문장) |
| 1004 | L580, L816 | baroclinic3D.outputFort48 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:431` (결론 문장) |
| 1005 | L581, L817 | nws08Control.vortexModel | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:432` (결론 문장) |
| 1006 | L582, L818 | nws08Control.backgroundWindModel | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:433` (결론 문장) |
| 1007 | L583, L819 | nws08Control.BCalc | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:434` (결론 문장) |
| 1008 | L584, L820 | nws08Control.thetaLatDep | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:435` (결론 문장) |
| 1009 | L585, L821 | nws08Control.useInflow | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:436` (결론 문장) |
| 1010 | L586, L822 | nws08Control.windspeed_averaging_minute | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:437` (결론 문장) |
| 1011 | L587, L823 | nws08Control.w_cool | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:438` (결론 문장) |
| 1012 | L588, L824 | nws08Control.CkCd_calc | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:439` (결론 문장) |
| 1013 | L589, L825 | nws08Control.CkCd | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:440` (결론 문장) |
| 1014 | L590, L826 | nws08Control.WindMultiplier | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:441` (결론 문장) |
| 1015 | L654, C26 (L864) | IM 첫 자리 7 및 3D 선택 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:49` (결론 문장)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:235` (기존 표의 결론 열) |
| 1016 | L672, L673 | IM 마지막 자리의 추가 선택 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:235` (기존 표의 결론 열) |
| 1017 | L674 | IM 각 자리의 개별 검증 부재 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:235` (기존 표의 결론 열) |
| 1018 | L712, L713, C01 (L839) | TAU0 수심 경계 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:238` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:72` (결론 문장) |
| 1019 | L715 | 시간 변화 TAU0의 상한과 TK 정의 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:238` (기존 표의 결론 열) |
| 1020 | L719 | 음수 TAU0의 출력 자리 판독 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:238` (기존 표의 결론 열) |
| 1021 | L720 | TAU0 갱신 조건 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:238` (기존 표의 결론 열) |
| 1022 | L733, L828 | AttrName=swan_local_control | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:442` (결론 문장) |
| 1023 | L741, L829 | AttrName=average_horizontal_eddy_diffusivity_in_sea_water_wrt_depth | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:443` (결론 문장) |
| 1024 | L749, L830 | AttrName=subgrid_barrier | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:444` (결론 문장) |
| 1025 | L750, L831 | AttrName=overland_reduction_factor | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:445` (결론 문장) |
| 1026 | L757, L758 | THETA1·THETA2의 IEVC 조건 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:446` (결론 문장) |
| 1027 | L759 | legacy iWarnElevDump의 변환 순서 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:113` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:447` (결론 문장) |
| 1028 | L760, L827 | stationNames(k) (관측소 줄의 선택 토큰) | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:448` (결론 문장) |
| 1029 | L761 | WRAMP 입력의 부재 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:449` (결론 문장) |
| 1030 | C04 (L842) | OutputTau0의 입력 지위 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:450` (결론 문장) |
| 1031 | C05 (L843) | NOUT 부호와 파일 손상 주장 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:451` (결론 문장) |
| 1032 | C06 (L844) | NHSTAR·NHSINC 변경의 silent drift 주장 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:452` (결론 문장) |
| 1033 | C08 (L846) | NWS 변경의 hot restart 손상 주장 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:453` (결론 문장) |
| 1034 | C09 (L847) | 관측소 compact ASCII 주장 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:522` (결론 문장) |
| 1035 | C10 (L848) | NetCDF 미지원 fallback 주장 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:523` (결론 문장) |
| 1036 | C11 (L849) | hot start 출력 부호 규약 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:524` (결론 문장) |
| 1037 | C13 (L851) | NWS의 자리 분리 순서 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:50` (결론 문장) |
| 1038 | C14 (L852) | NWS13 namelist 이름 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:140` (결론 문장) |
| 1039 | C15 (L853) | NWS 부호와 응력·풍속 구별 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:51` (결론 문장) |
| 1040 | C20 (L858) | NWS13과 GAHM | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:319` (결론 문장) |
| 1041 | C21 (L859), C25 (L863) | 얼음 PDF의 NWS=1000+ 문구 | B 문서 오기 | `models/ADCIRC/README.md:16` (결론 문장)<br>`models/ADCIRC/manual-notes/19-ice-coverage.md:121` (결론 문장) |
| 1042 | C23 (L861) | 기본 DragLawString의 빌드 조건 | C 문서 누락 | `models/ADCIRC/manual-notes/19-ice-coverage.md:122` (결론 문장) |
| 1043 | C24 (L862) | IceCube 최대값 규칙의 적용 범위 | C 문서 누락 | `models/ADCIRC/manual-notes/19-ice-coverage.md:123` (결론 문장) |
| 1044 | C27 (L865) | 3D baroclinic을 IM=21+로 표현한 노트 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:50` (결론 문장) |
| 1045 | C28 (L866) | IM=21과 IDEN>=5의 조합 권고 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:51` (결론 문장) |
| 1046 | C29 (L867) | KP가 실제 마찰 계산에 남는지 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:92` (결론 문장) |
| 1047 | U01 (L876) | tau0_gen.f 생성 유틸리티 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:454` (결론 문장) |
| 1048 | U02 (L877) | TAU0<1의 primitive 방정식 설명 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:455` (결론 문장) |
| 1049 | U03 (L878) | NCDATE 시간대 접미부의 수용 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:456` (결론 문장) |
| 1050 | U04 (L879) | BCFLAG_TEMP=2/3의 실제 TMP 합산 규칙 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:457` (결론 문장) |

### ADCIRC-inputfiles-vs-code.md

| §5 줄 | 보고서 행 ID | 항목 | 결론 | 반영 위치(노트:줄) |
|---:|---|---|---|---|
| 963 | F14-12 | ASCII IBTYPEE 입력 | D 문서에만 있음 | `models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:33` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:257` (기존 표의 결론 열) |
| 964 | F14-19, F14-20 | fort.14의 추가 경계 레코드 | C 문서 누락 | `models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:45` (결론 문장) |
| 965 | F14-21 | 40·41의 ASCII reader와 후속 처리 | E 코드 결함 후보 | `models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:38` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:114` (코드 결함 후보 표) |
| 966 | F14-28, F14-29 | 장벽 높이의 종료 조건 | B 문서 오기 | `models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:35` (기존 표의 결론 열)<br>`models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:36` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:258` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:259` (기존 표의 결론 열) |
| 967 | F13-13 | 알 수 없는 노드 속성의 건너뛰기 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:89` (결론 문장) |
| 968 | F10-04 | 모델의 3D fort.10 읽기 | D 문서에만 있음 | `models/ADCIRC/manual-notes/05-input-files-reference.md:33` (기존 표의 결론 열) |
| 969 | F11-08 | 2DDI fort.11의 둘째 레코드 | B 문서 오기 | `models/ADCIRC/manual-notes/05-input-files-reference.md:34` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:260` (기존 표의 결론 열) |
| 970 | F11-11, F11NC-01, F11NC-02, F11NC-03 | 외부 3D 결합 netCDF 입력 | C 문서 누락 | `models/ADCIRC/manual-notes/05-input-files-reference.md:35` (기존 표의 결론 열)<br>`models/ADCIRC/manual-notes/05-input-files-reference.md:36` (기존 표의 결론 열)<br>`models/ADCIRC/manual-notes/05-input-files-reference.md:37` (기존 표의 결론 열) |
| 971 | F18-02, F18-03, F18-04, F18-05, F18-06, F18-07, F18-08, F18-09, F18-10, F18-11, F18-12, F18-13, F18-14, F18-15, F18-16, F18-17, F18-18, F18-19, F18-20, F18-21, F18-22, F18-23, F18-24, F18-25, F18-26, F18-27, F18-28, F18-29, F18-30 | fort.18의 레코드 schema | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:108` (결론 문장) |
| 972 | F19-01 | fort.19와 NBFR 조건 | B 문서 오기 | `models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:34` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:261` (기존 표의 결론 열) |
| 973 | F19-05, F20-06 | ETIMINC·FTIMINC 반복 | B 문서 오기 | `models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:35` (기존 표의 결론 열)<br>`models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:42` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:262` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:264` (기존 표의 결론 열) |
| 974 | F20-01 | fort.20의 NFFR=-1 | B 문서 오기 | `models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:41` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:263` (기존 표의 결론 열) |
| 975 | F20-04 | IBTYPE=32의 수위 필드 | C 문서 누락 | `models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:62` (결론 문장) |
| 976 | F24-02 | SAL Alpha 레코드의 문자값 수 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:265` (기존 표의 결론 열) |
| 977 | F24-04 | SAL 성분 이름과 순서 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:266` (기존 표의 결론 열) |
| 978 | NA-01 | Tau0 노드 속성의 단위 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:267` (기존 표의 결론 열) |
| 979 | NA-04 | Tau0MinMax 초기화값 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:63` (기존 표의 결론 열) |
| 980 | NA-06, NA-12, NA-13 | 바닥 마찰 속성의 NOLIBF 제한 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:268` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:270` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:271` (기존 표의 결론 열) |
| 981 | NA-09 | 교각 속성 이름 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:269` (기존 표의 결론 열) |
| 982 | NA-16 | 점성 속성과 확산 속성 이름 혼동 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:272` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:60` (기존 표의 결론 열) |
| 983 | NA-17, NA-28 | Smagorinsky 계수의 무차원 단위 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:273` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:290` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:61` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:62` (기존 표의 결론 열) |
| 984 | NA-18 | ASCII 확산 속성의 발견 플래그 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:115` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:90` (결론 문장) |
| 985 | NA-21 | 초기 하천 수위의 적용 방식 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:274` (기존 표의 결론 열) |
| 986 | NA-31, NA-32 | 추가 SWAN·육상 거칠기 속성 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:145` (결론 문장) |
| 987 | NA-33, NA-34 | subgrid_barrier 값과 소비 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:91` (결론 문장) |
| 988 | NA-35, NA-37 | 내부 조석 마찰의 다섯 성분과 기본값 배열 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:116` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:64` (기존 표의 결론 열) |
| 989 | F35-03, FORT36-03, FORT37-03 | 3D 해양 경계의 시간 단위 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:52` (결론 문장) |
| 990 | FORT36-01, FORT37-01 | 염분·온도 경계의 추가 읽기 조건 | C 문서 누락 | `models/ADCIRC/manual-notes/05-input-files-reference.md:47` (기존 표의 결론 열)<br>`models/ADCIRC/manual-notes/05-input-files-reference.md:48` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:275` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:276` (기존 표의 결론 열) |
| 991 | F38-05 | TMP 성분의 실제 부호 조합 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:53` (결론 문장) |
| 992 | F39-01 | river 경계 유형과 IDEN 조건 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:277` (기존 표의 결론 열) |
| 993 | F39-03 | RIVBCSTATIM 단위 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:278` (기존 표의 결론 열) |
| 994 | F14-30 | 102·112의 읽기와 배열 할당 | E 코드 결함 후보 | `models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:37` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:117` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:279` (기존 표의 결론 열) |
| 995 | BATH-01 | NDDT 입력 파일 | B 문서 오기 | `models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:33` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:67` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:280` (기존 표의 결론 열) |
| 996 | BATH-04, BATH-05, BATH-06 | 시변 수심의 생략·sentinel·분할 형식 | C 문서 누락 | `models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:36` (기존 표의 결론 열)<br>`models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:37` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:70` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:71` (기존 표의 결론 열) |
| 997 | WEIR-01 | 시변 weir의 기본 파일명 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:281` (기존 표의 결론 열) |
| 998 | WEIR-06 | 분 단독 시간 지정 검사 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:118` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:282` (기존 표의 결론 열) |
| 999 | WEIR-10 | schedule offset의 hotstart 조건 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:283` (기존 표의 결론 열) |
| 1000 | SCH-03 | schedule 끝 시간의 초 항 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:119` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:284` (기존 표의 결론 열) |
| 1001 | SCH-05, SCH-06 | schedule별 HOT와 파일 디렉터리 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:87` (결론 문장) |
| 1002 | ROT-04 | 회전행렬의 입력 열 | E 코드 결함 후보 | `models/ADCIRC/manual-notes/05-input-files-reference.md:41` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:120` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:44` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:285` (기존 표의 결론 열) |
| 1003 | STA-05 | 외부 관측점의 이름 필드 | C 문서 누락 | `models/ADCIRC/manual-notes/05-input-files-reference.md:46` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:49` (기존 표의 결론 열) |
| 1004 | CLI-10, CLI-11, CLI-12, CLI-13 | ADCIRC 옵션 대소문자 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:286` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:287` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:288` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:289` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:43` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:44` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:45` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:46` (기존 표의 결론 열) |
| 1005 | CLI-14, CLI-15, CLI-23, CLI-24, CLI-25 | ADCIRC·adcprep의 추가 명령줄 규칙 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:47` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:48` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:50` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:51` (기존 표의 결론 열) |
| 1006 | CLI-22 | --prep88 제거 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:49` (기존 표의 결론 열) |
| 1007 | NA-29 | 경사 제한 활성 상태의 수명 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:291` (기존 표의 결론 열) |
| 1008 | F24-06 | fort.24.nc 우선 입력 | C 문서 누락 | `models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md:110` (결론 문장) |
| 1009 | NWS-12101, NWS-12102, NWS-12107, NWS-12301, NWS-12302, NWS-12307, NWS-12401, NWS-12402, NWS-12407 | 얼음과 직접 응력의 아홉 조합 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:52` (결론 문장) |
| 1010 | NWS-extra, MET-46 | 종합 NWS 표 밖의 추가 선택 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:120` (결론 문장) |
| 1011 | NWS-heading | v53 파랑 입력 표 머리 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:53` (결론 문장) |
| 1012 | MET-02 | NWS=2의 WTIMINC 위치 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:210` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:302` (기존 표의 결론 열) |
| 1013 | MET-05 | NWS=3의 좌표계 한정 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:211` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:303` (기존 표의 결론 열) |
| 1014 | MET-07 | NWS=±4의 기압 단위 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:212` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:304` (기존 표의 결론 열) |
| 1015 | MET-09 | NWS=6의 날짜 레코드 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:213` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:305` (기존 표의 결론 열) |
| 1016 | MET-13 | NWS=8의 반구 처리 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:306` (기존 표의 결론 열) |
| 1017 | MET-15, MET-26 | 트랙 레코드의 생략된 필드 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:54` (결론 문장) |
| 1018 | MET-16 | NWS=8의 모형 이름 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:307` (기존 표의 결론 열) |
| 1019 | MET-28, MET-30 | 기상 입력 후 제한과 혼합 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:55` (결론 문장) |
| 1020 | MET-32, F200-10, NC13-12, NC14-12 | -I의 입력 경로 예외 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:199` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:216` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:224` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:308` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:316` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:320` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:325` (기존 표의 결론 열) |
| 1021 | MET-34 | HWind 격자 간격 단위 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:217` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:309` (기존 표의 결론 열) |
| 1022 | MET-36 | 기상 snapshot 수와 시간 검사 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:171` (결론 문장) |
| 1023 | MET-38 | NWS=16 예제의 Pc | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:218` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:310` (기존 표의 결론 열) |
| 1024 | MET-42, MET-44 | GFDL ASCII 형식 변경 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:219` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:311` (기존 표의 결론 열) |
| 1025 | F200-03 | NWS=10의 얼음 필드 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:56` (결론 문장) |
| 1026 | F200-05 | NWS=11의 배열 저장 순서 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:220` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:312` (기존 표의 결론 열) |
| 1027 | F200-06 | NWS=11의 formatted OPEN | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:121` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:221` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:313` (기존 표의 결론 열) |
| 1028 | F200-07 | NWS=11의 기압 환산 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:122` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:222` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:314` (기존 표의 결론 열) |
| 1029 | F200-09 | NWS=11 dataset 간격 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:223` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:315` (기존 표의 결론 열) |
| 1030 | OWI-04 | OWI의 파일 목록과 셋째 기본 격자 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:121` (결론 문장) |
| 1031 | OWI-06 | OWI 중첩 격자의 시작 시각 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:317` (기존 표의 결론 열) |
| 1032 | OWI-09 | P/W 일치 검사와 오류 코드 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:123` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:122` (결론 문장) |
| 1033 | NC13-02 | NWS=13의 입력 종류 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:197` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:318` (기존 표의 결론 열) |
| 1034 | NC13-04 | OWI netCDF 메타데이터의 사용 여부 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:141` (결론 문장) |
| 1035 | NC13-08 | time units의 날짜 시작 위치 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:198` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:319` (기존 표의 결론 열) |
| 1036 | NC13-11 | OWI netCDF 결측값·scale·offset | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:142` (결론 문장) |
| 1037 | NC14-03 | 얼음 변수 이름을 읽는 조건 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:321` (기존 표의 결론 열) |
| 1038 | NC14-06 | refdate 시간 형식 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:322` (기존 표의 결론 열) |
| 1039 | NC14-07, NC14-08 | NWS=-14의 형식·부호 의미 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:323` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:324` (기존 표의 결론 열) |
| 1040 | NC14-10, NC14-11, NC14-13, NC14-14 | NWS=14의 추가 입력·fallback | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:172` (결론 문장) |
| 1041 | MET-40 | NWS=6의 격자 범위 처리와 외삽 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:57` (결론 문장) |
| 1042 | MET-41 | NWS=±7의 응력·풍속 혼동 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:214` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:326` (기존 표의 결론 열) |
| 1043 | MET-45 | 기본 바람 항력 상한 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:327` (기존 표의 결론 열) |
| 1044 | ICE-01 | 얼음 파일 제목 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:328` (기존 표의 결론 열) |
| 1045 | ICE-02 | NCICE의 자릿수 설명 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:329` (기존 표의 결론 열) |
| 1046 | ICE-04, ICE-12, ICE-13, ICE-14 | 얼음 입력의 생략된 후속 규칙 | C 문서 누락 | `models/ADCIRC/manual-notes/19-ice-coverage.md:66` (결론 문장) |
| 1047 | ICE-06 | 음수 얼음값 처리 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:330` (기존 표의 결론 열) |
| 1048 | ICE-10 | 기본 얼음 항력법 | A 판 차이 | `models/ADCIRC/README.md:47` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:331` (기존 표의 결론 열) |
| 1049 | ICE-11 | IceCube의 상수항과 농도 표기 | B 문서 오기 | `models/ADCIRC/README.md:48` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:332` (기존 표의 결론 열) |
| 1050 | NA-36 | 해상 거칠기의 풍속 지수 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:333` (기존 표의 결론 열) |
| 1051 | F23-01 | fort.23과 NWS 크기 조건 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:334` (기존 표의 결론 열) |
| 1052 | F23-06, F23-07, F23-08, F23-09 | STWAVE type=2의 제어·자료 구조 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:458` (결론 문장) |
| 1053 | HS-02, HS-06, HS-15 | binary 핫스타트의 추가 상태·선택 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:178` (결론 문장) |
| 1054 | HS-04, HS-11, HS-12 | binary 핫스타트의 배열 배치 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:335` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:338` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:339` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:139` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:170` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:171` (기존 표의 결론 열) |
| 1055 | HS-08 | EP 제거와 출력 카운터 복원 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:336` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:155` (기존 표의 결론 열) |
| 1056 | HS-09, HS-13, HS-16, HS-21 | 핫스타트 블록의 상세 선택 조건 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:337` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:340` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:341` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:343` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:161` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:163` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:169` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:172` (기존 표의 결론 열) |
| 1057 | HS-20 | harmonic 부하 벡터의 NOUT·NHA 조건 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:342` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:162` (기존 표의 결론 열) |
| 1058 | HS-22 | 핫스타트 timestep 변경 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:344` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:116` (기존 표의 결론 열) |
| 1059 | HSNC-01, HSNC-02, HSNC-03, HSNC-04 | netCDF 핫스타트의 기본·파랑 상태 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:223` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:224` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:225` (기존 표의 결론 열) |
| 1060 | HSNC-05, HSNC-06, HSNC-07 | netCDF harmonic·평균·분산 누적 상태 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:226` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:227` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:228` (기존 표의 결론 열) |
| 1061 | HSNC-08, HSNC-09, HSNC-10 | netCDF 3D 상태와 출력 계수 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:229` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:230` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:231` (기존 표의 결론 열) |
| 1062 | SG-01, SG-02, SG-03 | subgrid lookup schema | C 문서 누락 | `models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:44` (기존 표의 결론 열)<br>`models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:45` (기존 표의 결론 열)<br>`models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:46` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:86` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:87` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:88` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:73` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:74` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:75` (기존 표의 결론 열) |
| 1063 | XDMF-01, XDMF-02, XDMF-03 | XDMF 격자·경계·노드 속성 schema | C 문서 누락 | `models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:52` (기존 표의 결론 열)<br>`models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:53` (기존 표의 결론 열)<br>`models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md:54` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:104` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:105` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:106` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:81` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:82` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:83` (기존 표의 결론 열) |
| 1064 | NA-38 | ESLNodes.63 핫스타트 재입력 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:92` (결론 문장) |
| 1065 | NA-39 | sponge 속성의 둘째 저장 성분 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:93` (결론 문장) |
| 1066 | CLI-26, CLI-27 | aswip 추가 옵션 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:52` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md:53` (기존 표의 결론 열) |
| 1067 | F14-32 | prep의 내부 장벽 짝 노드 라벨 | E 코드 결함 후보 | `models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md:39` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:124` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:345` (기존 표의 결론 열) |
| 1068 | F19-06, F20-07 | prep의 복사 열 폭 | C 문서 누락 | `models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md:63` (결론 문장) |
| 1069 | MET-47 | NWS=±4의 prep 고정 형식 처리 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:125` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:215` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:346` (기존 표의 결론 열) |
| 1070 | U-01 | fort.38 TMP 열별 가중치와 단위 처리 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:54` (결론 문장) |
| 1071 | U-02 | 외부 3D 변수의 실제 읽기·소비·단위 검사 범위 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:55` (결론 문장) |
| 1072 | U-03 | subgrid 값의 의미·차원 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:116` (결론 문장) |
| 1073 | U-04 | 내부 조석 마찰 다섯 성분의 실제 계산·검사 범위 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:155` (결론 문장) |
| 1074 | U-05 | GRIB2 압력 선택의 실제 검색 규칙 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md:58` (결론 문장) |
| 1075 | U-06 | sponge 둘째 성분의 선택값 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-boundary-conditions.md:63` (결론 문장) |

### ADCIRC-outputs-vs-code.md

| §5 줄 | 보고서 행 ID | 항목 | 결론 | 반영 위치(노트:줄) |
|---:|---|---|---|---|
| 1550 | L121, L128, L1171 | D01 · 시계열 binary ±2 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:460` (기존 표의 결론 열) |
| 1551 | L124, L125, L131 | 2차원 출력 형식의 추가 조건 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:525` (결론 문장) |
| 1552 | L134 | D02 · 농도 파일명 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:461` (기존 표의 결론 열) |
| 1553 | L135, L136 | D01·D03 · NOUTGC 출력 형식 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:460` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:462` (기존 표의 결론 열) |
| 1554 | L137 | D04 · NOUTE 정의 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:463` (기존 표의 결론 열) |
| 1555 | L139, L1350 | ASCII FileFmtVersion 추가 필드 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:526` (결론 문장) |
| 1556 | L141, L1351 | sparse 시각 레코드의 추가 필드 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:527` (결론 문장) |
| 1557 | L144 | D05 · 관측소 식별자 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:126` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:464` (기존 표의 결론 열) |
| 1558 | L145 | 건조 노드의 대체값 조건 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:528` (결론 문장) |
| 1559 | L153 | XDMF의 직접 진단 출력 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:529` (결론 문장) |
| 1560 | L155 | D06 · fort.16의 GFDL 절 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:465` (기존 표의 결론 열) |
| 1561 | L156 | D07 · ITPACK 로그 대상 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:466` (기존 표의 결론 열) |
| 1562 | L211, L212 | D09 · 기상 관측소 보간 원본 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:468` (기존 표의 결론 열) |
| 1563 | L242 | D08 · fort.77 자료 세트 수 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:467` (기존 표의 결론 열) |
| 1564 | L262, L295 | D10 · fort.83 농도 복원 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:127` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:469` (기존 표의 결론 열) |
| 1565 | L268, L296 | fort.90 활성 조건 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:530` (결론 문장) |
| 1566 | L284, L285 | 회전 구면 좌표의 유속 출력 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:531` (결론 문장) |
| 1567 | L286, L514 | D12·D29 · 풍속과 정규화 응력 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:152` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:470` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:487` (기존 표의 결론 열) |
| 1568 | L287, L289, L293 | fort.75·76·81의 netCDF 디스패치 제한 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:532` (결론 문장) |
| 1569 | L288 | fort.76 형식 강제 변환 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:533` (결론 문장) |
| 1570 | L291 | D13 · fort.77 위키 복사 블록 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:471` (기존 표의 결론 열) |
| 1571 | L292, L294, L1498 | fort.81·83의 실제 입력·출력 연결 범위 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:534` (결론 문장) |
| 1572 | L302 | I3D=0의 기존 문서 확인 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:535` (결론 문장) |
| 1573 | L305 | 3차원 binary 지원 중단 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:536` (결론 문장) |
| 1574 | L306, L308 | D14 · 3차원 netCDF | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:103` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:104` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:472` (기존 표의 결론 열) |
| 1575 | L307, L309 | 3차원 형식과 간격 검사 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:537` (결론 문장) |
| 1576 | L347 | 밀도별 IRTYPE 초기값 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:538` (결론 문장) |
| 1577 | L348 | D16 · fort.44 마지막 헤더 값 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:108` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:474` (기존 표의 결론 열) |
| 1578 | L349 | D21 · fort.45·46의 IRTYPE 재사용 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:128` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:121` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:479` (기존 표의 결론 열) |
| 1579 | L359, L360, L361 | D15 · fort.41 밀도·염분·온도 순서 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:105` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:106` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:107` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:473` (기존 표의 결론 열) |
| 1580 | L364, L367, L370 | D17 · fort.44 SIGMA 반복 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:110` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:111` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:112` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:475` (기존 표의 결론 열) |
| 1581 | L380 | D18 · ISTA와 lSta | F 표기 차이 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:115` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:476` (기존 표의 결론 열) |
| 1582 | L392 | D19 · EV의 수직 점성 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:116` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:477` (기존 표의 결론 열) |
| 1583 | L393, L597, L621, L622, L623, L624, L625, L626, L627, L628, L629, L644, L645, L646, L647, L648, L649, L650, L651, L652, L1361, L1362, L1363, L1372, L1373, L1374 | 3차원 netCDF 변수 schema | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:539` (결론 문장) |
| 1584 | L394, L397, L398, L1180 | D20 · 표층 수온의 제어값 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:117` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:118` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:119` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:120` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:478` (기존 표의 결론 열) |
| 1585 | L395 | fort.47의 제한된 일치 판정 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:540` (결론 문장) |
| 1586 | L401 | fort.47 netCDF 조건 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:541` (결론 문장) |
| 1587 | L409, L411, L413, L414, L415 | 조화 출력 제어값의 경계 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:542` (결론 문장) |
| 1588 | L410, L412, L416 | D22 · 조화분석 netCDF | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:73` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:74` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:75` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:480` (기존 표의 결론 열) |
| 1589 | L423, L432, L1181, L1182 | D23 · 관측소 식별자 줄 누락 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:76` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:77` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:78` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:79` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:481` (기존 표의 결론 열) |
| 1590 | L458, L600 | D25 · 유속 진폭 단위 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:83` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:84` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:483` (기존 표의 결론 열) |
| 1591 | L461, L468, L1186 | D24 · fort.55 줄 분리 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:80` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:81` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:82` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:482` (기존 표의 결론 열) |
| 1592 | L485 | D26 · EAVDIF·EVADIF | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:85` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:484` (기존 표의 결론 열) |
| 1593 | L486 | 유속 평균·분산의 비율 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:543` (결론 문장) |
| 1594 | L497, L498, L528, L529, L534, L535, L540, L541 | D28 · 극값 파일의 간격 필드 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:144` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:145` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:146` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:147` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:148` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:149` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:150` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:151` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:486` (기존 표의 결론 열) |
| 1595 | L504, L510, L513, L516, L519 | D27 · 극값 형식 제어 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:139` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:140` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:141` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:142` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:143` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:485` (기존 표의 결론 열) |
| 1596 | L517 | D30 · maxrs 자료 의미 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:153` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:488` (기존 표의 결론 열) |
| 1597 | L522, L524, L525 | 극값 형식 변환의 부호 차이 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:544` (결론 문장) |
| 1598 | L546 | D31 · 침수 파일의 재시작 연속성 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:175` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:489` (기존 표의 결론 열) |
| 1599 | L547, L557 | 침수 활성과 initiallydry sparse 제한 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:545` (결론 문장) |
| 1600 | L549 | D32 · 건조 시간 초기값 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:129` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:158` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:490` (기존 표의 결론 열) |
| 1601 | L550 | D33 · 처음 습윤인 노드의 침수 시간 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:159` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:491` (기존 표의 결론 열) |
| 1602 | L552 | D34 · 침수 시간 문서의 자료명 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:160` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:492` (기존 표의 결론 열) |
| 1603 | L555 | D36 · initiallydry 초기 레코드 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:155` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:494` (기존 표의 결론 열) |
| 1604 | L559 | D37 · endrisinginun ASCII 헤더 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:130` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:156` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:495` (기존 표의 결론 열) |
| 1605 | L563 | D35 · wet/dry 시계열의 자료 세트 수 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:131` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:154` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:493` (기존 표의 결론 열) |
| 1606 | L564, L565 | D38 · noff의 노드 labels와 배열 크기 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:132` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:157` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:496` (기존 표의 결론 열) |
| 1607 | L566 | D59 · 유일한 요소 출력이라는 설명 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:512` (기존 표의 결론 열) |
| 1608 | L581, L831 | netCDF fill·dry 속성 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:546` (결론 문장) |
| 1609 | L583 | D42 · 관측소 netCDF의 격자 포함 범위 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:185` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:500` (기존 표의 결론 열) |
| 1610 | L584, L711, L1414 | netCDF time 기준 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:547` (결론 문장) |
| 1611 | L585, L586, L708, L709, L710, L1413 | 관측소 이름·좌표 schema | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:548` (결론 문장) |
| 1612 | L587, L588 | D60 · English 길이와 m 고정 속성 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:133` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:187` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:188` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:513` (기존 표의 결론 열) |
| 1613 | L589 | D67 · 최대 침수 깊이의 단위 범위 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:164` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:519` (기존 표의 결론 열) |
| 1614 | L593, L594, L1504 | 풍응력 netCDF의 English 단위와 성분 속성 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:134` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:549` (결론 문장) |
| 1615 | L595 | 얼음 백분율과 fraction 속성 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:135` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:550` (결론 문장) |
| 1616 | L598 | D44 · 수직 유속 방향 속성 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:136` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:122` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:501` (기존 표의 결론 열) |
| 1617 | L602 | D39 · inun_time의 길이 단위 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:137` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:161` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:497` (기존 표의 결론 열) |
| 1618 | L604 | D40 · 최대 침수 깊이 기준면 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:138` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:162` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:498` (기존 표의 결론 열) |
| 1619 | L605 | D41 · 건조 시간과 발생 시각 속성 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:139` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:163` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:499` (기존 표의 결론 열) |
| 1620 | L607, L1502 | D47 · fort.77.nc의 시간 차원 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:140` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:186` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:502` (기존 표의 결론 열) |
| 1621 | L609 | D66 · 3차원 English 속성 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:141` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:123` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:518` (기존 표의 결론 열) |
| 1622 | L630, L631, L632, L633, L634, L635, L656, L657, L658, L659, L660, L661, L712, L713, L714, L715, L716, L717, L718, L719, L1364, L1365, L1377, L1378, L1415, L1416 | 조화분석 netCDF 변수 schema | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:551` (결론 문장) |
| 1623 | L636, L637, L638, L639, L662, L663, L666, L667, L670, L671, L1366, L1367, L1368, L1379, L1380, L1382, L1384, L1385 | 2차원 수위·유속·기압·TAU0·drag schema | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:552` (결론 문장) |
| 1624 | L640, L641, L642, L674, L675, L681, L1369, L1370, L1387, L1391 | 기상·얼음 netCDF 변수 schema | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:553` (결론 문장) |
| 1625 | L643, L707, L1335, L1336, L1371, L1412 | 동적 수위 보정 파일과 변수 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:554` (결론 문장) |
| 1626 | L653, L654, L655, L682, L683, L1337, L1339, L1375, L1376, L1392 | 표층 수온·경압 기울기·복사응력 기울기 schema | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:555` (결론 문장) |
| 1627 | L664, L665, L668, L669, L672, L673, L676, L677, L678, L679, L699, L700, L701, L702, L703, L704, L705, L706, L1381, L1383, L1386, L1388, L1389, L1407, L1408, L1409, L1410, L1411 | 극값·침수 netCDF 변수 schema | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:556` (결론 문장) |
| 1628 | L680, L1390 | fort.77.nc 변수 이름 정의 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:557` (결론 문장) |
| 1629 | L684, L685, L686, L687, L688, L689, L690, L691, L692, L693, L694, L695, L696, L697, L698, L1218, L1219, L1220, L1221, L1222, L1223, L1224, L1225, L1340, L1341, L1342, L1343, L1344, L1345, L1346, L1347, L1393, L1394, L1395, L1396, L1397, L1398, L1399, L1400, L1401, L1402, L1403, L1404, L1405, L1406 | SWAN 추가 파일·최대값·netCDF schema | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:558` (결론 문장) |
| 1630 | L720, L721, L722, L723, L724, L725, L726, L727, L728, L729, L730, L731, L732, L733, L734, L735, L736, L737, L738, L739, L740, L741, L742, L743, L744, L745, L746, L747, L1149, L1237, L1238, L1239, L1240, L1241, L1242, L1243, L1244, L1245, L1246, L1247, L1248, L1249, L1250, L1251, L1252, L1253, L1254, L1255, L1256, L1257, L1258, L1259, L1260, L1261, L1262, L1263, L1264, L1265, L1417 | netCDF 핫스타트의 2차원 상태 schema·저장 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:235` (결론 문장) |
| 1631 | L748, L749, L750, L751, L752, L753, L754, L755, L756, L757, L758, L811, L812, L813, L814, L815, L816, L817, L818, L819, L820, L821, L822, L823, L824, L1266, L1267, L1268, L1269, L1270, L1271, L1272, L1273, L1274, L1275, L1276, L1277, L1278, L1279, L1280, L1281, L1282, L1283, L1284, L1285, L1286, L1287, L1288, L1289, L1290, L1418, L1425 | netCDF 핫스타트의 조화 상태 schema·저장 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:236` (결론 문장) |
| 1632 | L759, L760, L761, L762, L763, L764, L825, L1291, L1292, L1293, L1294, L1295, L1296, L1297, L1419, L1426 | netCDF 핫스타트의 평균·분산 schema·저장 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:237` (결론 문장) |
| 1633 | L765, L766, L767, L768, L769, L770, L771, L772, L773, L774, L775, L776, L777, L778, L779, L780, L781, L782, L783, L784, L785, L786, L787, L788, L789, L790, L791, L1298, L1299, L1300, L1301, L1302, L1303, L1304, L1305, L1306, L1307, L1308, L1309, L1310, L1311, L1312, L1313, L1314, L1315, L1316, L1317, L1318, L1319, L1320, L1321, L1322, L1323, L1324, L1420, L1421 | netCDF 핫스타트의 3차원 schema·저장 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:238` (결론 문장) |
| 1634 | L792, L793, L794, L795, L796, L797, L798, L799, L800, L801, L802, L803, L804, L805, L806, L807, L808, L809, L810, L833, L834, L835, L836, L837, L838, L839, L840, L841, L842, L843, L844, L845, L846, L847, L1422, L1423, L1424 | netCDF 격자·경계 schema | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:559` (결론 문장) |
| 1635 | L832, L848, L849, L850, L851, L852, L853, L854, L855, L856, L857, L858, L859, L860, L861, L862, L863, L864, L865, L866, L867, L868, L869, L870, L871, L872, L873, L874, L875, L876, L877, L878, L879, L880, L881, L882, L883, L884, L885, L886, L887, L888, L889, L890, L891, L892, L893, L894, L895, L896, L897, L898, L899, L900, L901, L902, L903, L904, L905, L906, L907, L908, L909, L910, L911, L912, L913, L914, L915, L916 | netCDF 제어값·전역 메타데이터 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:560` (결론 문장) |
| 1636 | L938, L942 | XDMF 발표 자료와 native writer | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:561` (결론 문장) |
| 1637 | L944, L945, L946, L947, L948, L949, L950 | native XDMF 변수·성분·지원 단위 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:562` (결론 문장) |
| 1638 | L952, L1501 | XDMF 출력 창의 최종화·병렬 자료 수 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:142` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:563` (결론 문장) |
| 1639 | L953, L968, L969, L970, L971, L972, L973, L974, L975, L976, L977, L978, L979, L980, L981, L982, L983, L984, L985, L986, L987, L988, L989, L990, L991, L992, L993, L994, L995, L996, L997, L998, L999, L1000, L1001, L1002, L1003, L1004, L1005, L1006, L1007, L1008, L1009, L1010, L1011, L1012, L1013, L1014, L1015, L1016, L1017, L1018, L1019, L1020, L1021, L1022, L1023, L1024, L1025, L1026, L1027, L1028, L1029, L1030, L1031, L1032, L1033, L1034, L1035, L1036, L1037, L1038, L1039, L1040, L1041, L1042, L1043, L1044, L1045, L1046, L1047, L1048, L1049 | XDMF 제어 Information | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:564` (결론 문장) |
| 1640 | L954, L955, L956, L957, L958 | XDMF 경계 Attribute | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:565` (결론 문장) |
| 1641 | L1062, L1065, L1066, L1067, L1069 | 핫스타트의 추가 제어 모드 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:179` (결론 문장) |
| 1642 | L1070, L1085, L1087, L1088, L1089, L1090, L1091, L1092, L1093, L1094, L1095 | binary 핫스타트 추가 크기·상태·자리 채움 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:180` (결론 문장) |
| 1643 | L1071, L1072, L1073, L1074, L1075, L1076, L1077, L1078, L1189 | D48 · binary 핫스타트 헤더 확장 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:50` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:51` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:52` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:53` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:60` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:503` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:504` (기존 표의 결론 열) |
| 1644 | L1079, L1080, L1081, L1082, L1083, L1084 | D49 · 2차원 핫스타트 배열 순서 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:54` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:55` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:56` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:57` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:58` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:59` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:504` (기존 표의 결론 열) |
| 1645 | L1096, L1097, L1098, L1099, L1100, L1101, L1102, L1103 | D50 · 제거된 EP와 출력 위치 자리 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:61` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:62` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:63` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:64` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:65` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:66` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:67` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:68` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:505` (기존 표의 결론 열) |
| 1646 | L1112, L1113, L1114, L1115, L1116, L1117, L1118, L1119, L1120, L1121, L1122, L1123, L1124, L1125, L1126, L1194, L1195, L1196, L1197, L1198, L1199, L1200, L1201, L1202, L1203, L1204, L1205, L1206, L1207, L1208 | D51 · 3차원 핫스타트 배열 순서 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:69` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:70` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:71` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:72` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:73` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:74` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:75` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:76` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:77` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:78` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:79` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:80` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:81` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:82` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:83` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:84` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:85` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:86` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:87` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:88` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:89` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:90` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:91` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:92` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:93` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:94` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:95` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:96` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:97` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:98` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:506` (기존 표의 결론 열) |
| 1647 | L1127 | D52 · 조화 상태의 시작 조건 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:99` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:507` (기존 표의 결론 열) |
| 1648 | L1136, L1137, L1138, L1139 | D53 · 조화 load vector 제어 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:100` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:101` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:102` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:103` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:508` (기존 표의 결론 열) |
| 1649 | L1140 | D54 · 평균·분산 상태 조건 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:104` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:509` (기존 표의 결론 열) |
| 1650 | L1148 | D55 · 핫스타트 binary 전용 설명 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:105` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:510` (기존 표의 결론 열) |
| 1651 | L1150, L1151 | D63 · 전용 핫스타트 writer의 지원 범위 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:107` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:108` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:515` (기존 표의 결론 열) |
| 1652 | L1152 | D57 · 재시작 DTDP 변경 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:106` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:511` (기존 표의 결론 열) |
| 1653 | L1167, L1168, L1174, L1178 | D65 · 합치기 관측소 수 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:143` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:289` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:290` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:291` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:517` (기존 표의 결론 열) |
| 1654 | L1172, L1177 | D17 · POST41의 마지막 SIGMA | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:144` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:113` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:475` (기존 표의 결론 열) |
| 1655 | L1179 | D16·D17 · POST44가 보존하는 native 형식 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:109` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:114` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:474` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:475` (기존 표의 결론 열) |
| 1656 | L1185 | 합치기의 NFREQ 검사 범위 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:566` (결론 문장) |
| 1657 | L1187, L1188, L1191 | 일반 합치기의 형식과 충돌 표지 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:567` (결론 문장) |
| 1658 | L1190, L1210, L1500 | D63 · POSTHOT의 상태 보존 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:145` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:109` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:515` (기존 표의 결론 열) |
| 1659 | L1192 | 전용 sparse vector의 기록 수 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:146` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:568` (결론 문장) |
| 1660 | L1217 | D61 · SWAN 기존 출력 네 파일 제한 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:287` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:514` (기존 표의 결론 열) |
| 1661 | L1226 | D64 · windDrag.173 이름과 제어 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:288` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:516` (기존 표의 결론 열) |
| 1662 | L1338, L1503 | fort.56 디버그 구현의 호출 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:569` (결론 문장) |
| 1663 | L1348 | ESLNodes.63 추가 레코드 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:570` (결론 문장) |
| 1664 | L1349 | fort.69 진단 파일 레코드 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:571` (결론 문장) |
| 1666 | L1447, L1449 | N02·N04 · 출력 위치별 허용 형식 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:572` (결론 문장) |
| 1667 | L1448 | N03 · ASCII 숫자 헤더 공간 수 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:573` (결론 문장) |
| 1668 | L1450 | N05 · netCDF 미지원 빌드 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:574` (결론 문장) |
| 1669 | L1451, L1460, L1461 | N06·N15·N16 · 형식 제어 부호 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:459` (결론 문장)<br>`models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:575` (결론 문장) |
| 1670 | L1452 | N07 · 3차원 레코드의 성분 수 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:576` (결론 문장) |
| 1671 | L1453 | N08 · XDMF 소스 파일명 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:577` (결론 문장) |
| 1672 | L1454 | N09 · 현재 판의 fill 값 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:578` (결론 문장) |
| 1673 | L1455 | N10 · ch1 물리량 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:181` (결론 문장) |
| 1674 | L1456 | N11 · NODECODE와 NNODECODE 저장 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:182` (결론 문장) |
| 1675 | L1457 | N12 · 핫스타트 교대 쓰기의 예외 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:183` (결론 문장) |
| 1676 | L1458 | N13 · 재시작 직후 조화 출력 절차 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:184` (결론 문장) |
| 1677 | L1459 | N14 · 직접·전용 핫스타트 지원 구분 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-hotstart.md:185` (결론 문장) |
| 1678 | L1462 | N17 · NFREQ 출처와 주파수 손실 주장 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:460` (결론 문장) |
| 1679 | L1463 | N18 · 모든 파일의 첫 레코드 일반화 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:461` (결론 문장) |
| 1680 | L1464 | N19 · 압력 파일의 잘못된 인용 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:462` (결론 문장) |
| 1681 | L1465 | N20 · fort.41 제어 이름 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:56` (결론 문장) |
| 1682 | L1467 | N22 · 재시작 연속성 설명의 추가 범위 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:579` (결론 문장) |
| 1683 | L1468 | N23 · 합치기 예외 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:580` (결론 문장) |
| 1684 | L1470 | N24 · 일반 출력과 핫스타트 제어 혼동 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md:463` (결론 문장) |
| 1685 | L1497 | TOUT와 STATIM의 실제 시간 단계 변환 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md:581` (결론 문장) |
| 1686 | L1499 | 지역 3차원 binary 핫스타트 길이 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:147` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-hotstart.md:186` (결론 문장) |

### ADCIRC-theory-vs-code.md

| §5 줄 | 보고서 행 ID | 항목 | 결론 | 반영 위치(노트:줄) |
|---:|---|---|---|---|
| 1062 | 159행 (`1.15`) | v44.XX 식 (1.15)의 끝 등호 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:72` (기존 표의 결론 열) |
| 1063 | 163행 (`1.19`)<br>164행 (`1.20`)<br>165행 (`1.21`) | v44.XX 요소 평균 수심 첨자 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:82` (결론 문장) |
| 1064 | 173행 (`1.29`) | v44.XX 수위 증분의 시간 단위 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:50` (기존 표의 결론 열) |
| 1065 | 183행 (`2.5`)<br>184행 (`2.6`)<br>360행 (`30a`)<br>361행 (`30b`)<br>364행 (`32a`)<br>365행 (`32b`) | 대칭 수평 응력의 입력 점성 배율 | C 문서 누락 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:52` (기존 표의 결론 열) |
| 1066 | 185행 (`2.7`)<br>187행 (`2.9`)<br>190행 (`2.12`)<br>289행 (`PDF-BOTTOM-RHO-20`)<br>290행 (`PDF-BOTTOM-RHO-21`) | 정규화한 바닥 응력의 밀도 중복 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:53` (기존 표의 결론 열) |
| 1067 | 188행 (`2.10`)<br>189행 (`2.11`) | 유량 운동량의 추가 수심 나눗셈 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:54` (기존 표의 결론 열) |
| 1068 | 191행 (`2.13`)<br>194행 (`2.16`) | 2D 마찰 수심의 시간 수준 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:55` (기존 표의 결론 열) |
| 1069 | 192행 (`2.14`)<br>193행 (`2.15`) | 유량 운동량 우변 코리올리 시간 수준 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:56` (기존 표의 결론 열) |
| 1070 | 204행 (`3.5`)<br>206행 (`3.7`)<br>207행 (`3.8`)<br>208행 (`3.9`)<br>209행 (`3.10`)<br>210행 (`3.11`)<br>214행 (`3.15`)<br>215행 (`3.16`)<br>216행 (`3.17`)<br>217행 (`3.18`)<br>218행 (`3.19`)<br>219행 (`3.20`)<br>343행 (`17a`)<br>344행 (`17b`) | 3D 수평 응력의 같은 z 보간 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:64` (기존 표의 결론 열) |
| 1071 | 239행 (`5.1`)<br>240행 (`5.2`)<br>241행 (`5.3`)<br>244행 (`5.6`)<br>245행 (`5.7`) | 생략 전의 완전한 3D 구면식 | D 문서에만 있음 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:83` (결론 문장) |
| 1072 | 243행 (`5.5`) | 구면 연속식의 곡률 부호 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:84` (결론 문장) |
| 1073 | 269행 (`6.15`) | 3D 경계 중앙 속도 첨자 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:73` (기존 표의 결론 열) |
| 1074 | 272행 (`6.18`)<br>273행 (`6.19`)<br>274행 (`6.20`) | 수위 법선 기울기 0 경계 | D 문서에만 있음 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:85` (결론 문장) |
| 1075 | 281행 (`PDF-TIME-QN`)<br>797행 (`TIME-WEIGHTS`) | 경계 유량의 세 시간 가중 설명 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:51` (기존 표의 결론 열) |
| 1076 | 283행 (`PDF-NODAL-STRESS`) | 절점 응력 평균의 구현과 기호 대응 | F 표기 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:86` (결론 문장) |
| 1077 | 287행 (`PDF-KSLIP-LINEAR`) | 선형 마찰계수의 정의 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:87` (결론 문장) |
| 1078 | 291행 (`PDF-LATERAL-IBP-VELOCITY`) | 비보존형 부분적분 뒤의 수심 근사 | F 표기 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:88` (결론 문장) |
| 1079 | 292행 (`PDF-LATERAL-IBP-FLUX`) | 보존형 부분적분의 불필요한 미분 기호 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:89` (결론 문장) |
| 1080 | 294행 (`PDF-VERTICAL-STRESS-DIAG`)<br>368행 (`34a`)<br>369행 (`34b`) | ISLIP=0 바닥 응력의 좌표 배율 | E 코드 결함 후보 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:65` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:148` (코드 결함 후보 표) |
| 1081 | 295행 (`PDF-RADIATION-SUPPORT`) | 수위 방사 경계 지원 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:90` (결론 문장) |
| 1082 | 299행 (`PDF-FE-FACTORIAL`) | 삼각형 임의 차수 적분 항등식 | D 문서에만 있음 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:91` (결론 문장) |
| 1083 | 305행 (`PDF-FE-RULE2A-REMOVED`) | original 면적 적분의 현재 선택 경로 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:70` (기존 표의 결론 열) |
| 1084 | 329행 (`10b`) | 1992년 no-slip 적용 높이 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:92` (결론 문장) |
| 1085 | 331행 (`12`) | 1992년 로그 마찰의 높이 원점 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:93` (결론 문장) |
| 1086 | 354행 (`27`)<br>619행 (`PDF-TIDAL-L0`)<br>667행 (`PDF-TIDAL-L0-1993_Westerink02`)<br>703행 (`PDF-TIDAL-L0-1994_Blain03`)<br>741행 (`PDF-TIDAL-L0-1994_Westerink01`)<br>780행 (`PDF-TIDAL-L0-1995_Hench`)<br>882행 (`TIDE-NTIP-1`) | 장주기 조석의 위도 함수 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:62` (기존 표의 결론 열) |
| 1087 | 357행 (`29a`) | Darcy–Weisbach 계수 입력·변환 | D 문서에만 있음 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:94` (결론 문장) |
| 1088 | 359행 (`29c`) | Manning 변환의 고정 수심과 총 수심 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:95` (결론 문장) |
| 1089 | 386행 (`46a`)<br>388행 (`47a`)<br>389행 (`47b`)<br>393행 (`51`) | 1992년 회전 마찰 텐서·진단 Cf | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:96` (결론 문장) |
| 1090 | 413행 (`66`)<br>414행 (`67`)<br>447행 (`85`)<br>448행 (`86`)<br>458행 (`89`)<br>459행 (`90`)<br>460행 (`91`) | 1992년 GWCE 점성항의 시간 수준 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:97` (결론 문장) |
| 1091 | 415행 (`68`) | 1992년 경계 τ₀Q 시간 가중 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:98` (결론 문장) |
| 1092 | 416행 (`69`)<br>417행 (`70`)<br>418행 (`71`)<br>419행 (`72`)<br>484행 (`99`)<br>486행 (`101`)<br>487행 (`102`)<br>489행 (`104`)<br>492행 (`107a`)<br>494행 (`107c`)<br>495행 (`107d`)<br>496행 (`108a`)<br>497행 (`108b`) | 1992년 외부 운동량의 암시적 수평 점성 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:99` (결론 문장) |
| 1093 | 424행 (`74a`)<br>425행 (`74b`) | 코리올리 계수와 유량의 요소 평균 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:100` (결론 문장) |
| 1094 | 435행 (`81a`)<br>436행 (`81b`)<br>437행 (`81c`)<br>438행 (`81d`)<br>441행 (`83a`)<br>442행 (`83b`)<br>443행 (`83c`)<br>444행 (`83d`)<br>452행 (`87d`)<br>453행 (`87e`)<br>454행 (`87f`)<br>480행 (`98a`)<br>481행 (`98b`)<br>482행 (`98c`)<br>483행 (`98d`) | 1992년 test·trial 및 합 첨자 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:74` (기존 표의 결론 열) |
| 1095 | 477행 (`97b`)<br>479행 (`97d`) | 1992년 V 이류의 미분 방향 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:101` (결론 문장) |
| 1096 | 485행 (`100`)<br>488행 (`103`) | 1992년 코리올리의 부호 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:75` (기존 표의 결론 열) |
| 1097 | 500행 (`111`)<br>501행 (`112`)<br>502행 (`113a`)<br>503행 (`113b`)<br>504행 (`113c`)<br>505행 (`113d`) | 1992년 외부 모드 검증 지표 | D 문서에만 있음 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:102` (결론 문장) |
| 1098 | 511행 (`114`)<br>512행 (`115`)<br>513행 (`116a`)<br>514행 (`116b`)<br>515행 (`117a`)<br>516행 (`117b`)<br>517행 (`118a`)<br>518행 (`118b`)<br>519행 (`119`)<br>520행 (`120`)<br>523행 (`123`)<br>524행 (`124`)<br>525행 (`125`)<br>526행 (`126`)<br>527행 (`127`)<br>529행 (`129`)<br>530행 (`130`)<br>531행 (`131`)<br>532행 (`132`)<br>533행 (`133`)<br>534행 (`134`)<br>536행 (`136`)<br>537행 (`137`)<br>538행 (`138`)<br>539행 (`139`)<br>540행 (`140`)<br>575행 (`175`)<br>578행 (`177`)<br>579행 (`178`)<br>580행 (`179`)<br>581행 (`180`)<br>582행 (`181`)<br>583행 (`182`)<br>584행 (`183a`)<br>585행 (`183b`)<br>586행 (`183c`)<br>587행 (`184`)<br>588행 (`185`)<br>589행 (`186a`)<br>590행 (`186b`)<br>592행 (`188`)<br>593행 (`189`)<br>594행 (`190a`)<br>595행 (`190b`)<br>596행 (`191a`)<br>597행 (`191b`)<br>598행 (`192a`)<br>599행 (`192b`)<br>600행 (`193`)<br>601행 (`194`)<br>602행 (`195`)<br>603행 (`196a`)<br>604행 (`196b`)<br>605행 (`197`)<br>606행 (`198`)<br>607행 (`199`) | 1992년 DSS 1·2 내부 모드 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:103` (결론 문장) |
| 1099 | 521행 (`121`)<br>522행 (`122`)<br>528행 (`128`)<br>535행 (`135`) | DSS 시험의 축약식·항등식 | D 문서에만 있음 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:104` (결론 문장) |
| 1100 | 541행 (`141`)<br>542행 (`142`)<br>543행 (`143`)<br>544행 (`144`)<br>545행 (`145`)<br>546행 (`146`)<br>547행 (`147`)<br>548행 (`148`)<br>549행 (`149`)<br>550행 (`150`)<br>551행 (`151`)<br>552행 (`152`)<br>553행 (`153`)<br>554행 (`154`)<br>555행 (`155`)<br>556행 (`156`)<br>557행 (`157`)<br>558행 (`158`)<br>559행 (`159`)<br>560행 (`160`)<br>561행 (`161`)<br>562행 (`162`)<br>563행 (`163`)<br>564행 (`164`)<br>565행 (`165`)<br>566행 (`166`)<br>567행 (`167`)<br>568행 (`168`)<br>569행 (`169`)<br>570행 (`170`)<br>571행 (`171`)<br>572행 (`172`)<br>573행 (`173`)<br>574행 (`174`) | DSS 정상·주기 해석해와 검증 구성 | D 문서에만 있음 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:105` (결론 문장) |
| 1101 | 608행 (`200`)<br>609행 (`201`)<br>610행 (`202`)<br>611행 (`203`)<br>612행 (`204`)<br>613행 (`205`) | Grant–Madsen 파랑·흐름 바닥 폐합 | D 문서에만 있음 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:106` (결론 문장) |
| 1102 | 621행 (`PDF-SOLVER-LU`) | GWCE의 일회 LU 분해 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:69` (기존 표의 결론 열) |
| 1103 | 622행 (`PDF-GRID-QUADRILATERAL`) | 4절점 사각형 유동 요소 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:107` (결론 문장) |
| 1104 | 634행 (`4`)<br>679행 (`4`)<br>753행 (`4`) | 후속 보고서 조석 위상의 분수 범위 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:63` (기존 표의 결론 열) |
| 1105 | 640행 (`10`)<br>685행 (`10`)<br>759행 (`10`) | 후속 GWCE의 수위 시간미분 괄호 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:77` (기존 표의 결론 열) |
| 1106 | 646행 (`11`)<br>647행 (`12`)<br>653행 (`13`)<br>654행 (`14`)<br>765행 (`11`)<br>766행 (`12`) | 지역별 조석 진폭·위상 검증 지표 | D 문서에만 있음 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:108` (결론 문장) |
| 1107 | 661행 (`A2`)<br>773행 (`A2`)<br>774행 (`A3`) | 지역 지각의 Greenwich 변환 | D 문서에만 있음 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:109` (결론 문장) |
| 1108 | 691행 (`11`)<br>692행 (`12`)<br>693행 (`13`)<br>694행 (`14`) | HURWIN의 대기 경계층 방정식 | D 문서에만 있음 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:110` (결론 문장) |
| 1109 | 695행 (`15`) | Blain 지수 기압 법칙 | F 표기 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:111` (결론 문장) |
| 1110 | 715행 (`4`) | Report 2 조석의 경도 위상 누락 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:112` (결론 문장) |
| 1111 | 717행 (`6`) | Report 2 x 운동량의 V 누락 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:113` (결론 문장) |
| 1112 | 719행 (`8`) | Report 2 GWCE의 횡방향 이류 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:114` (결론 문장) |
| 1113 | 728행 (`12`)<br>729행 (`13`) | Report 2 시간간격·격자 권고 | D 문서에만 있음 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:115` (결론 문장) |
| 1114 | 730행 (`14`) | Report 2 이차 마찰의 지수·수위 기호 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:116` (결론 문장) |
| 1115 | 740행 (`PDF-WETDRY-OLD`) | Report 2의 wetting/drying 부재 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:71` (기존 표의 결론 열) |
| 1116 | 752행 (`3`)<br>758행 (`9`) | Hench y 운동량의 회전 부호 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:76` (기존 표의 결론 열) |
| 1117 | 804행 (`TIME-THETA`)<br>805행 (`TIME-DISP`)<br>806행 (`TIME-EXPLICIT-1D-L`)<br>807행 (`TIME-EXPLICIT-1D-C`)<br>808행 (`TIME-EXPLICIT-2D-L`)<br>809행 (`TIME-EXPLICIT-2D-C`)<br>810행 (`TIME-GWCE-UNCOND`)<br>811행 (`TIME-GWCE-CR-CI`)<br>812행 (`TIME-GWCE-CR-CE`)<br>813행 (`TIME-GWCE-CR-LI`)<br>814행 (`TIME-GWCE-CR-LE`)<br>815행 (`TIME-NONCENTER`) | 시간 가중치의 분석 관계·안정성 조건 | D 문서에만 있음 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:117` (결론 문장) |
| 1118 | 816행 (`TIME-DOC-TAU-TYPO`) | 시간과 역시간을 비교한 τ₀ 조건 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:118` (결론 문장) |
| 1119 | 823행 (`TAU-MINMAX-TABLE`) | τ₀ 값표의 최소·최대 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:119` (결론 문장) |
| 1120 | 824행 (`TAU-1`) | TAU0=−1의 D=10 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:57` (기존 표의 결론 열) |
| 1121 | 825행 (`TAU-2`) | TAU0=−2의 D=1 누락 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:58` (기존 표의 결론 열) |
| 1122 | 826행 (`TAU-FRACTION`) | TAU0 소수 자리 출력 선택 | E 코드 결함 후보 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:59` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:149` (코드 결함 후보 표) |
| 1123 | 833행 (`TAU-7-VAR-DESC`) | 시간평균 이전 τ₀ 변수 설명 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:120` (결론 문장) |
| 1124 | 834행 (`TAU-TK-TENSOR`) | 시간 가변 τ₀의 텐서 마찰 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:121` (결론 문장) |
| 1125 | 835행 (`TAU-UPDATE`) | τ₀ 갱신의 CGWCE_HDP 진입 | C 문서 누락 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:60` (기존 표의 결론 열) |
| 1126 | 844행 (`FRICTION-ALLOWED`)<br>845행 (`MANNING-ALLOWED`) | NOLIBF=3 허용 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:122` (결론 문장) |
| 1127 | 867행 (`KG-VISC-GRAD`) | KG 점성 미분의 방향 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:123` (결론 문장) |
| 1128 | 874행 (`WIND-Z0-MARINE`) | Charnock 해상 거칠기의 풍속 지수 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:61` (기존 표의 결론 열) |
| 1129 | 891행 (`3D-ISLIP-1`)<br>893행 (`3D-ISLIP-3`) | ISLIP=1·3의 옛 KP 법칙 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:66` (기존 표의 결론 열) |
| 1130 | 894행 (`3D-Z0-MANNING`) | 3D Manning 거칠기의 κ | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:124` (결론 문장) |
| 1131 | 909행 (`3D-IEVC-20`) | IEVC=20의 실제 연직 보간식 | C 문서 누락 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:125` (결론 문장) |
| 1132 | 918행 (`3D-IEVC-42`) | IEVC=42의 추가 H | E 코드 결함 후보 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:68` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:150` (코드 결함 후보 표) |
| 1133 | 921행 (`3D-THETA-INPUT`) | THETA 입력 줄의 IEVC 조건 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:126` (결론 문장) |
| 1134 | 922행 (`3D-THETA-ROLES`) | MY2.5 THETA 역할의 뒤바뀜 | B 문서 오기 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:67` (기존 표의 결론 열) |
| 1135 | 989행 (`B01`) | B01 총 수심 GWCE 강성 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:127` (결론 문장) |
| 1136 | 990행 (`B02`) | B02 중력·분산 보정 | C 문서 누락 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:128` (결론 문장) |
| 1137 | 991행 (`B03`) | B03 수위 기울기 제한 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:129` (결론 문장) |
| 1138 | 992행 (`B04`) | B04 수위 흡수층 | C 문서 누락 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:130` (결론 문장) |
| 1139 | 993행 (`B05`) | B05 predictor-corrector | C 문서 누락 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:131` (결론 문장) |
| 1140 | 994행 (`B06`) | B06 절점 τ₀ 선택·평균 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:132` (결론 문장) |
| 1141 | 995행 (`B07`) | B07 Smagorinsky와 제한값 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:133` (결론 문장) |
| 1142 | 996행 (`B08`) | B08 2D 마찰의 시간간격 상한 | C 문서 누락 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:134` (결론 문장) |
| 1143 | 997행 (`B09`) | B09 Manning 수로·장벽 보정 | C 문서 누락 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:135` (결론 문장) |
| 1144 | 998행 (`B10`) | B10 교각 마찰 | C 문서 누락 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:136` (결론 문장) |
| 1145 | 999행 (`B11`) | B11 NOLIBF=3 운동량 분산 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:137` (결론 문장) |
| 1146 | 1000행 (`B12`) | B12 비등방 내부파 항력 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:138` (결론 문장) |
| 1147 | 1001행 (`B13`) | B13 Garratt 상한 | C 문서 누락 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:139` (결론 문장) |
| 1148 | 1002행 (`B14`) | B14 Powell·SWAN 끌림 선택 | C 문서 누락 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:140` (결론 문장) |
| 1149 | 1003행 (`B15`) | B15 얼음의 바람 끌림 보정 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:141` (결론 문장) |
| 1150 | 1004행 (`B16`) | B16 방향별 육상 거칠기·수관 | C 문서 누락 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:142` (결론 문장) |
| 1151 | 1005행 (`B17`) | B17 FullTIP와 Love 수 | C 문서 누락 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:143` (결론 문장) |
| 1152 | 1006행 (`B18`) | B18 공간별 SAL | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:144` (결론 문장) |
| 1153 | 1007행 (`B19`) | B19 3D 마찰의 상한·하한 | C 문서 누락 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:145` (결론 문장) |
| 1154 | 1008행 (`B20`) | B20 같은 z의 수평 응력 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:146` (결론 문장) |
| 1155 | 1009행 (`B21`) | B21 biharmonic·Leith 점성 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:147` (결론 문장) |
| 1156 | 1010행 (`B22`) | B22 속도 Gaussian 필터 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:148` (결론 문장) |
| 1157 | 1011행 (`B23`) | B23 MY2.5 수면 생산 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:149` (결론 문장) |
| 1158 | 1012행 (`B24`) | B24 난류 점성·스칼라 확산 제한 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:150` (결론 문장) |
| 1159 | 1013행 (`B25`) | B25 경압 구적·cubic 보간 | C 문서 누락 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:151` (결론 문장) |
| 1160 | 1014행 (`B26`) | B26 스칼라 ALP4·biharmonic 확산 | C 문서 누락 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:152` (결론 문장) |
| 1161 | 1015행 (`B27`) | B27 분산 대각값 제한 | C 문서 누락 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:153` (결론 문장) |
| 1162 | 1016행 (`B28`) | B28 JCG scaling·종료 | A 판 차이 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:154` (결론 문장) |
| 1163 | 1024행 (`C01`) | C01 DTDP의 계산 역할 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:22` (결론 문장) |
| 1164 | 1025행 (`C02`) | C02 시간 가중치와 FTHETA | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:23` (결론 문장)<br>`models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:121` (결론 문장) |
| 1165 | 1026행 (`C03`) | C03 TAU0=−5의 필수 다음 줄 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:24` (결론 문장) |
| 1166 | 1027행 (`C04`) | C04 τ₀ 문서 값과 실제 분기 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md:73` (결론 문장) |
| 1167 | 1028행 (`C05`) | C05 TK와 GWCE 좌변 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:82` (결론 문장)<br>`models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:89` (결론 문장) |
| 1168 | 1029행 (`C06`) | C06 KP의 잔존 계산 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:71` (결론 문장) |
| 1169 | 1030행 (`C07`) | C07 Manning 조건·보정 누락 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:101` (결론 문장) |
| 1170 | 1031행 (`C08`) | C08 추가 마찰 분기·수치 상한 누락 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:73` (결론 문장) |
| 1171 | 1032행 (`C09`) | C09 장주기 함수의 구체식 누락 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:51` (결론 문장) |
| 1172 | 1033행 (`C10`) | C10 ETRF 입력·Love 수 선택 누락 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:52` (결론 문장) |
| 1173 | 1034행 (`C11`) | C11 FullTIP의 모든 성분 보장 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:73` (결론 문장) |
| 1174 | 1035행 (`C12`) | C12 v44.XX 구체적 차이 누락 | C 문서 누락 | `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md:155` (결론 문장) |
| 1175 | 1036행 (`C13`) | C13 현행 매개변수 문서의 오류 누락 | C 문서 누락 | `models/ADCIRC/manual-notes/06-parameter-definitions.md:40` (결론 문장) |

### ADCIRC-features-vs-code.md

| §5 줄 | 보고서 행 ID | 항목 | 결론 | 반영 위치(노트:줄) |
|---:|---|---|---|---|
| 784 | W01 (116줄)<br>W02 (117·702줄)<br>W03 (118줄) | 1995년 DCA·NWA 후보 기법 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:83` (결론 문장) |
| 785 | W06 (121줄) | 혼합 마찰식의 Manning형 매개변수 | F 표기 차이 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:123` (결론 문장) |
| 786 | W08 (123줄)<br>W15 (130줄) | 습윤·건조 인터페이스 no-slip | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:84` (결론 문장) |
| 787 | W09 (124·703줄) | 최소 수심의 단계별 증가 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:50` (결론 문장) |
| 788 | W10 (125·704줄)<br>W19 (134·705줄)<br>W23 (138·706줄)<br>K07 (571줄) | 최소 습윤·건조 대기 단계 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:111` (결론 문장) |
| 789 | W11 (126줄) | 수위 경사와 바람 응력의 공동 습윤 조건 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:85` (결론 문장) |
| 790 | W13 (128줄) | 절점 곱 이외의 요소 마스크 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:112` (결론 문장) |
| 791 | W17 (132줄) | 노출 문턱의 등호 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:51` (결론 문장) |
| 792 | W18 (133줄) | 노출 수심 하한 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:52` (결론 문장) |
| 793 | W21 (136줄)<br>K02 (566줄) | 재침수 유속의 후보 절점 선택 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:86` (결론 문장) |
| 794 | W25 (140·707줄) | 지정 유량 경계의 일괄 습윤 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:87` (결론 문장) |
| 795 | W26 (141줄)<br>K06 (570줄) | 장벽 수신 이후의 요소 비활성화 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:113` (결론 문장) |
| 796 | W30 (145줄) | 구판 권고값과 현재 입력 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:53` (결론 문장) |
| 797 | W31 (146줄) | 경사면 상류 흐름의 적용 한계 주장 | H 코드 대조 대상 아님 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:88` (결론 문장) |
| 798 | B03 (156줄) | 경계 유형의 안정성·해상도 권고 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:40` (결론 문장) |
| 799 | B18 (171줄) | fort.39의 조건부 읽기 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:41` (결론 문장) |
| 800 | B20 (173줄)<br>B22 (175줄)<br>B24 (177줄)<br>B29 (182·708줄) | 경계 연결·열거 규칙과 검사 범위 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:42` (결론 문장) |
| 801 | B31 (184·709줄) | 지정 법선 유량의 부호 | F 표기 차이 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:43` (결론 문장) |
| 802 | B33 (186줄)<br>K08 (572줄) | 외부 위어 최소 수두 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:44` (결론 문장) |
| 803 | B34 (187줄) | 외부 위어 ramp 계수 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:45` (결론 문장) |
| 804 | B35 (188줄)<br>B48 (201줄) | 위어 계산 시점의 수위 배열 이름 | F 표기 차이 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:46` (결론 문장) |
| 805 | B40 (193줄)<br>B44 (197줄) | 내부 위어 상류 문턱 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:47` (결론 문장) |
| 806 | B42 (195줄)<br>B46 (199줄) | 내부 위어 등호·소수 근사 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:48` (결론 문장) |
| 807 | B50 (203줄) | 관류의 최소 상류 수두와 천단 등호 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:49` (결론 문장) |
| 808 | B53 (206줄)<br>B54 (207줄) | 관류 식의 연산자 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:50` (결론 문장) |
| 809 | B57 (210줄)<br>B59 (212줄)<br>B61 (214줄)<br>B63 (216줄) | v40.02 관류의 수두 경계 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:51` (결론 문장) |
| 810 | B69 (222줄)<br>B70 (223줄)<br>K11 (575줄)<br>C12 (661줄) | TVW의 분 단독 입력 검사 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:151` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-topic-map.md:65` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-weir-boundary.md:88` (결론 문장) |
| 811 | B76 (229줄) | 일정표 시작 오프셋의 기준 시각 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:89` (결론 문장) |
| 812 | R01 (240줄)<br>R02 (241줄)<br>C34 (683줄) | 파랑 방사 응력 발산의 부호 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:77` (결론 문장) |
| 813 | R13 (252줄) | SWAN POINTS·TABLE 명령과 내부 표기 | F 표기 차이 | `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:78` (결론 문장) |
| 814 | R14 (253줄) | SWAN TABLE의 실제 병렬 출력 위치 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:79` (결론 문장) |
| 815 | R16 (255줄)<br>R22 (261줄)<br>R24 (263줄)<br>C35 (684줄) | SWAN 출력 제어와 추가 절차 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:80` (결론 문장) |
| 816 | R18 (257줄)<br>R19 (258줄)<br>R20 (259줄) | ADCIRC 출력에 없는 SWAN IVTYPE | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:81` (결론 문장) |
| 817 | R21 (260줄) | SWAN 출력 수정 위치 안내 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:82` (결론 문장) |
| 818 | P02 (272줄) | 교각 속성 이름 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:102` (결론 문장) |
| 819 | P05 (275줄)<br>P09 (279줄) | 현행 교각 문서의 Yarnell·항력 계수식 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:103` (결론 문장) |
| 820 | P06 (276줄)<br>P07 (277줄)<br>P15 (285줄) | 교각 관계의 유효 범위·입력 권고 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:104` (결론 문장) |
| 821 | P08 (278줄) | 정상 단방향 운동량 평형의 의미 | F 표기 차이 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:105` (결론 문장) |
| 822 | P12 (282줄) | 구판 교각 항력의 제곱근 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:106` (결론 문장) |
| 823 | P13 (283·728줄)<br>P14 (284·729줄)<br>C14 (663줄) | 교각 Fr의 중복 제곱 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:152` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:107` (결론 문장)<br>`models/ADCIRC/source-analysis/adcirc-topic-map.md:59` (기존 표의 결론 열) |
| 824 | P17 (287줄) | 교각 계수 입력 파일 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:108` (결론 문장) |
| 825 | I02 (296·710줄)<br>I04 (298·711줄) | 별도 얼음 마찰·질량 방정식 | D 문서에만 있음 | `models/ADCIRC/manual-notes/19-ice-coverage.md:124` (결론 문장) |
| 826 | I06 (300줄)<br>K25 (589줄)<br>C24 (673줄) | 구판 얼음 적용 범위와 SWAN 결합 | A 판 차이 | `models/ADCIRC/manual-notes/19-ice-coverage.md:38` (결론 문장) |
| 827 | I09 (303줄)<br>C21 (670줄)<br>C22 (671줄) | 얼음 문서의 0% 항력 자릿수 | B 문서 오기 | `models/ADCIRC/manual-notes/19-ice-coverage.md:67` (결론 문장) |
| 828 | I13 (307줄)<br>I29 (323줄) | 기본 얼음 항력법 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-topic-map.md:61` (기존 표의 결론 열) |
| 829 | I15 (309줄)<br>C19 (668줄) | 얼음 유형의 NWS 인코딩 | A 판 차이 | `models/ADCIRC/manual-notes/19-ice-coverage.md:68` (결론 문장)<br>`models/ADCIRC/source-analysis/adcirc-topic-map.md:61` (기존 표의 결론 열) |
| 830 | I23 (317줄) | 압력·바람 출력 번호 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-topic-map.md:61` (기존 표의 결론 열) |
| 831 | V01 (331·712줄) | 연직 요소 벽의 lumped 집계 조건 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-topic-map.md:65` (기존 표의 결론 열) |
| 832 | V04 (334줄) | 위어 유량 계수 SB·SP의 설명 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:52` (결론 문장) |
| 833 | V05 (335줄)<br>K32 (596줄) | 연직 요소 벽 유량의 추가 조건 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:64` (결론 문장) |
| 834 | V06 (336줄) | 연직 요소 벽의 높은 쪽·낮은 쪽 입력 배치 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:65` (결론 문장) |
| 835 | V07 (337줄) | 연직 요소 벽 높이의 분할 파일명 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:66` (결론 문장) |
| 836 | V08 (338줄) | 연직 요소 벽의 월류 계수 권고 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:67` (결론 문장) |
| 837 | V11 (341줄)<br>K28 (592줄) | 두 절점 그룹의 회전 반환 조건 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:153` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-topic-map.md:65` (기존 표의 결론 열) |
| 838 | V18 (348줄) | 준1차원·CFL 완화의 문서상 설명 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:53` (결론 문장) |
| 839 | D02 (357줄) | 수위 보정 추종 성능의 문서상 조건 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:52` (결론 문장) |
| 840 | D03 (358줄) | 초기 v53 수위 보정 경고 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:122` (결론 문장) |
| 841 | D04 (359줄) | 보정 활성화 조건 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:53` (결론 문장) |
| 842 | D19 (374줄) | 보정 출력 파일명 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-topic-map.md:60` (기존 표의 결론 열) |
| 843 | D23 (378줄)<br>K34 (598줄) | 보정의 직접 수위 증분 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-topic-map.md:60` (기존 표의 결론 열) |
| 844 | Q01 (386줄) | ADCIRC2D+의 v55·v56 범위 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:29` (결론 문장) |
| 845 | Q03 (388·713줄) | 외부 BPG의 중첩 적분 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:30` (결론 문장) |
| 846 | Q04 (389·731줄) | 외부 결합의 자유수면 항 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:31` (결론 문장) |
| 847 | Q07 (392줄)<br>K46 (610줄) | 내부 조석 소산 비율의 예외 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:71` (결론 문장) |
| 848 | Q08 (393줄) | 조석 잔차 소산의 적용 경로 누락 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:72` (결론 문장) |
| 849 | Q22 (407줄)<br>C30 (679줄) | 밀도 강제 문자열의 대소문자 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:32` (결론 문장) |
| 850 | T01 (415줄) | 내부 조석 기능의 최초 지원 판 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:156` (결론 문장) |
| 851 | T02 (416줄)<br>T03 (417줄) | 내부 조석 변환의 강제력·수심 권고 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:157` (결론 문장) |
| 852 | T05 (419줄) | 내부 조석 5열 입력 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:158` (결론 문장) |
| 853 | T07 (421줄) | 비결합 마찰의 사전 수심 정규화 | F 표기 차이 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:159` (결론 문장) |
| 855 | T10 (424줄)<br>K43 (607줄)<br>K45 (609줄) | 초임계 기복의 마찰 제한 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:160` (결론 문장) |
| 856 | A01 (432·730줄)<br>A02 (433·730줄)<br>K49 (613줄) | ALI 보정량의 실제 제곱 적용 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-topic-map.md:63` (기존 표의 결론 열) |
| 857 | A05 (436줄)<br>K51 (615줄) | IM에 따른 ALI 자동 활성화 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-topic-map.md:63` (기존 표의 결론 열) |
| 858 | A08 (439줄) | ALI가 사용하는 수심 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:25` (결론 문장) |
| 859 | S02 (448·714줄) | sponge 강도의 단위 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-boundary-conditions.md:64` (결론 문장) |
| 860 | S03 (449줄)<br>K52 (616줄) | sponge 입력 열 수 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-boundary-conditions.md:65` (결론 문장) |
| 861 | S04 (450줄)<br>K54 (618줄) | sponge 유형별 동작 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-boundary-conditions.md:66` (결론 문장) |
| 862 | S06 (452줄) | OceanMesh2D 속성 생성 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-boundary-conditions.md:67` (결론 문장) |
| 863 | S07 (453·715줄) | SPONGEDIST와 fort.92 출력 조건 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-topic-map.md:66` (기존 표의 결론 열) |
| 864 | H02 (462줄) | GAHM 주변 기압 기호 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:320` (결론 문장) |
| 865 | H07 (467줄) | Holland B의 경험 범위 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:321` (결론 문장) |
| 866 | H10 (470줄) | Rossby 수의 독립 변수 | F 표기 차이 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:322` (결론 문장) |
| 867 | H18 (478줄) | ATCF 입력의 통상 시간 간격 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:171` (결론 문장) |
| 868 | H20 (480줄)<br>K61 (625줄)<br>C38 (687줄) | 폭풍 이동속도 경험 보정 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:233` (결론 문장) |
| 869 | H23 (483줄) | 이동 보정 비율의 극값 설명에서 빠진 분기 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:234` (결론 문장) |
| 870 | H24 (484줄)<br>K66 (630줄)<br>C40 (689줄) | 최대풍속 반경 안쪽 유입각 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:289` (결론 문장) |
| 871 | H28 (488·716줄)<br>H29 (489·717줄) | GAHM 성분식의 각도·풍속 정규화 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:290` (결론 문장) |
| 872 | H30 (490줄)<br>C37 (686줄) | GAHM 수렴 종료 기준 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:137` (결론 문장) |
| 873 | H33 (493줄) | 유입각의 반경 방향 연속성 | F 표기 차이 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:291` (결론 문장) |
| 874 | H35 (495줄) | 각도 보간의 절대각·상대각 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:292` (결론 문장) |
| 875 | H38 (498줄)<br>H39 (499줄)<br>H40 (500줄)<br>C39 (688줄) | GAHM 반경 가중치·바깥 영역 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:293` (결론 문장) |
| 876 | H43 (503줄) | 관측 isotach 재현 설명의 수렴·대체값 조건 누락 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:138` (결론 문장) |
| 877 | G01 (511줄)<br>G02 (512줄)<br>G03 (513줄)<br>G04 (514줄)<br>G05 (515줄)<br>G06 (516줄)<br>G07 (517줄) | 외부 subgrid 표 생성 기능 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:117` (결론 문장) |
| 878 | F01 (526·718줄)<br>F02 (527줄)<br>F03 (528·719줄) | 총압·밀도 편차 압력의 정규화 | F 표기 차이 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:111` (결론 문장) |
| 879 | F07 (532·720줄)<br>F08 (533·721줄)<br>F11 (536·723줄)<br>F12 (537·724줄) | 경압항의 sigma 미분과 같은 z 보간 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:112` (결론 문장) |
| 880 | F09 (534줄) | 경압 정규화 기준 밀도 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:113` (결론 문장) |
| 881 | F10 (535·722줄)<br>F13 (538줄)<br>F14 (539줄)<br>F15 (540줄) | 압력 성분의 분리·상쇄 가정 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:114` (결론 문장) |
| 882 | F16 (541줄)<br>K73 (637줄) | 하층 EOS-3의 표층 영압 밀도 재사용 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:115` (결론 문장)<br>`models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:154` (코드 결함 후보 표) |
| 884 | F18 (543줄) | 밀도 다항식 T³ 지수 누락 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:116` (결론 문장) |
| 885 | F24 (549·725줄) | 요소 면적과 압력 구배 정규화 | F 표기 차이 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:57` (결론 문장) |
| 886 | F26 (551·726줄) | 경압 구배 수평 합의 상한 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:58` (결론 문장) |
| 887 | F29 (554줄)<br>F32 (557줄) | 경압 구배 정의의 중복 합 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:59` (결론 문장) |
| 888 | F31 (556·727·731줄) | native 경압 적분과 외부 BPG 소비 경로 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:60` (결론 문장) |
| 889 | K01 (565줄) | subgrid 침수·노출 수심 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:89` (결론 문장) |
| 890 | K03 (567줄) | 음의 침수 수위차 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:90` (결론 문장) |
| 891 | K04 (568줄)<br>C03 (652줄) | 시변 수심 침수 분기 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:91` (결론 문장) |
| 892 | K05 (569줄) | 장벽 수취 절점의 침수 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:92` (결론 문장) |
| 893 | K09 (573줄) | 장벽·관의 수두차 하한 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:54` (결론 문장) |
| 894 | K10 (574줄) | 위어 수위 평균의 빌드 조건 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:55` (결론 문장) |
| 895 | K12 (576줄) | 시변 장벽의 미지정 표식 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:90` (결론 문장) |
| 896 | K13 (577줄) | 방사 응력 TYPE=1 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:83` (결론 문장) |
| 897 | K14 (578줄) | SWAN 파력 평균과 성분 제한 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:84` (결론 문장) |
| 898 | K15 (579줄) | Marcel 경계 파력 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:85` (결론 문장) |
| 899 | K16 (580줄) | 파력의 계산값과 출력값 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:86` (결론 문장) |
| 900 | K17 (581줄) | SWAN 출력 읽기 오류의 처리 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-swan-coupling.md:87` (결론 문장) |
| 901 | K18 (582줄)<br>C13 (662줄) | 교각 입력의 유효 길이 변환 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:109` (결론 문장) |
| 902 | K19 (583줄) | 교각 마찰 시간 간격 상한 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:110` (결론 문장) |
| 903 | K20 (584줄) | Lupkes 얼음 항력의 계수 | C 문서 누락 | `models/ADCIRC/manual-notes/19-ice-coverage.md:125` (결론 문장) |
| 904 | K21 (585줄) | 얼음 농도 범위 처리 | C 문서 누락 | `models/ADCIRC/manual-notes/19-ice-coverage.md:126` (결론 문장) |
| 905 | K22 (586줄) | RaysIce의 저농도 분기 | C 문서 누락 | `models/ADCIRC/manual-notes/19-ice-coverage.md:127` (결론 문장) |
| 906 | K23 (587줄) | 얼음·기상 형식 조합 검사 | C 문서 누락 | `models/ADCIRC/manual-notes/19-ice-coverage.md:69` (결론 문장) |
| 907 | K24 (588줄) | OWI 얼음 초기 스냅샷 생략 | C 문서 누락 | `models/ADCIRC/manual-notes/19-ice-coverage.md:70` (결론 문장) |
| 908 | K26 (590줄) | 연직 요소 벽의 흐름 방향 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:68` (결론 문장) |
| 909 | K27 (591줄) | 연직 요소 벽의 제외 요소 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:69` (결론 문장) |
| 910 | K29 (593줄) | 연직 요소 벽의 법선 성분 제거 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:70` (결론 문장) |
| 911 | K30 (594줄) | 연직 요소 벽의 유형 11 누락 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:155` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-weir-boundary.md:71` (결론 문장) |
| 912 | K31 (595줄)<br>C11 (660줄) | 연직 요소 벽의 잠김 상태 전환 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:72` (결론 문장) |
| 913 | K33 (597줄) | 젖은 둘레와 Manning 마찰 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:111` (결론 문장) |
| 914 | K35 (599줄) | 길이가 0인 동적 보정 램프 | E 코드 결함 후보 | `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:156` (코드 결함 후보 표)<br>`models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:54` (결론 문장) |
| 915 | K36 (600줄) | 동적 수위 보정 입력 검사 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:55` (결론 문장) |
| 916 | K37 (601줄) | 동적 수위 보정의 관측점 출력 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:271` (결론 문장) |
| 917 | K38 (602줄) | 자유수면 경압항의 빌드 조건 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:33` (결론 문장) |
| 918 | K39 (603줄) | 잘못된 표면 밀도 자료 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:34` (결론 문장) |
| 919 | K40 (604줄) | sponge 내부의 경압·분산 제거 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:35` (결론 문장) |
| 920 | K41 (605줄) | CDisp 제한과 분산 입력 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:73` (결론 문장) |
| 921 | K42 (606줄) | Nycander 주파수 허용 범위 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:161` (결론 문장) |
| 922 | K44 (608줄) | 내부 조석 결합의 작은 분모 보호 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:162` (결론 문장) |
| 923 | K47 (611줄) | UNTIDE 초기 평균 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:94` (결론 문장) |
| 924 | K48 (612줄) | Munk_filter의 호출 상태 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:163` (결론 문장) |
| 925 | K50 (614줄) | ALI의 Cs=0 처리 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:26` (결론 문장) |
| 926 | K53 (617줄) | sponge 유형 선택 검사 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-boundary-conditions.md:68` (결론 문장) |
| 927 | K55 (619줄) | sponge의 기상·경압 강제 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-boundary-conditions.md:69` (결론 문장) |
| 928 | K56 (620줄) | sponge 기본 이산화 설정 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-boundary-conditions.md:70` (결론 문장) |
| 929 | K57 (621줄) | sponge 대안 분할법 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-boundary-conditions.md:71` (결론 문장) |
| 930 | K58 (622줄) | sponge 목표 자료의 합성 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-boundary-conditions.md:72` (결론 문장) |
| 931 | K59 (623줄) | sponge 운동량 완화 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-boundary-conditions.md:73` (결론 문장) |
| 932 | K60 (624줄) | GAHM 남반구 처리 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:323` (결론 문장) |
| 933 | K62 (626줄) | GAHM isotach 개수 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:172` (결론 문장) |
| 934 | K63 (627줄) | GAHM 방위 보간의 경계 처리 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:294` (결론 문장) |
| 935 | K64 (628줄) | GAHM isotach 수별 반경 보간 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:295` (결론 문장) |
| 936 | K65 (629줄) | GAHM 음의 반경 해 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:173` (결론 문장) |
| 937 | K67 (631줄) | GAHM 출력의 범위 제한 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:324` (결론 문장) |
| 938 | K68 (632줄) | GAHM 외곽 cutoff의 비활성 상태 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:325` (결론 문장) |
| 939 | K69 (633줄)<br>C32 (681줄) | native 3D 밀도 적분 위치 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:117` (결론 문장) |
| 940 | K70 (634줄) | 같은 높이 보간의 수심 하한 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:61` (결론 문장) |
| 941 | K71 (635줄) | 경압 평균의 유효 요소 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:62` (결론 문장) |
| 942 | K72 (636줄) | EOS 입력 범위 제한 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-3d-mode.md:118` (결론 문장) |
| 943 | K74 (638줄)<br>C43 (692줄) | subgrid lookup 파일 읽기 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:94` (기존 표의 결론 열)<br>`models/ADCIRC/source-analysis/adcirc-topic-map.md:64` (기존 표의 결론 열) |
| 944 | K75 (639줄) | subgrid 계수별 입력 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:95` (기존 표의 결론 열) |
| 945 | K76 (640줄) | subgrid 표 바깥 수위 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:96` (기존 표의 결론 열) |
| 946 | K77 (641줄) | subgrid 표 내부 보간 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:97` (기존 표의 결론 열) |
| 947 | K78 (642줄) | subgrid 보간 예외 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md:98` (기존 표의 결론 열) |
| 948 | C01 (650줄) | HABSMIN 용도 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:54` (결론 문장) |
| 949 | C02 (651줄) | 보통 W1의 수위차 절점 선택 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:93` (결론 문장) |
| 950 | C04 (653줄) | NODEDRYMIN·NODEWETMIN 조정 효과 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:114` (결론 문장) |
| 951 | C05 (654줄) | DELETA의 원문 위치 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:94` (결론 문장) |
| 952 | C06 (655줄) | H0·VELMIN의 표준 기본값이라는 설명 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:55` (결론 문장) |
| 953 | C07 (656줄) | 재침수의 보편 조건 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:95` (결론 문장) |
| 954 | C08 (657줄) | H0=0.1의 필수성 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:56` (결론 문장) |
| 955 | C09 (658줄) | 위어 BARMIN의 실제 적용 수두 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:56` (결론 문장) |
| 956 | C10 (659줄) | 자유·잠긴 월류 분류 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-weir-boundary.md:57` (결론 문장) |
| 957 | C15 (664줄)<br>C17 (666줄) | 내부 조석 항력과 평균 유속 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md:164` (결론 문장)<br>`models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:89` (결론 문장) |
| 958 | C16 (665줄) | UNTIDE와 Munk_filter 혼합 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-tidal-forcing.md:90` (결론 문장) |
| 959 | C18 (667줄) | 얼음 농도의 유일 사용처 | B 문서 오기 | `models/ADCIRC/manual-notes/19-ice-coverage.md:39` (결론 문장) |
| 960 | C20 (669줄) | ICE CUBE 다항식의 출처 | B 문서 오기 | `models/ADCIRC/manual-notes/19-ice-coverage.md:128` (결론 문장) |
| 961 | C23 (672줄) | 얼음 기본 문자열의 빌드 조건 | C 문서 누락 | `models/ADCIRC/manual-notes/19-ice-coverage.md:129` (결론 문장) |
| 962 | C25 (674줄) | ADCIRC 얼음 농도와 SWAN 감쇠 입력의 연결 누락 | E 코드 결함 후보 | `models/ADCIRC/manual-notes/19-ice-coverage.md:40` (결론 문장)<br>`models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md:157` (코드 결함 후보 표) |
| 963 | C26 (675줄) | 얼음 노트 목록의 판·조건 요약 | C 문서 누락 | `models/ADCIRC/README.md:17` (결론 문장) |
| 964 | C27 (676줄)<br>C28 (677줄) | 운동량 분산과 내부 조석 자료 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:74` (결론 문장) |
| 965 | C29 (678줄) | 외부 BPG 노트의 자유수면식 누락 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:36` (결론 문장) |
| 966 | C31 (680줄) | native BPG2D와 외부 입력 | B 문서 오기 | `models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:272` (결론 문장) |
| 967 | C36 (685줄) | 외부 GAHM C++ 재구현과 ADCIRC Fortran의 판 차이 | A 판 차이 | `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md:139` (결론 문장) |
| 968 | C41 (690줄) | 특수 기능 지도의 정적 근거 누락 | C 문서 누락 | `models/ADCIRC/source-analysis/adcirc-topic-map.md:58` (기존 표의 결론 열) |
| 969 | C42 (691줄) | 기능 지도 중 DG 구현과 시변 지형의 현재 범위 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-topic-map.md:62` (기존 표의 결론 열) |
| 970 | 보고서 732줄 | 문서상 검증 사례의 판과 적용 조건 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-topic-map.md:73` (결론 문장) |
| 971 | 보고서 733줄 | 외부 subgrid 생성 도구와 ADCIRC의 읽기 범위 | D 문서에만 있음 | `models/ADCIRC/source-analysis/adcirc-topic-map.md:74` (결론 문장) |

## 고친 노트

수정한 노트는 아래 34개다. 아래 노트의 last_source_check를 `2026-10-12 (recovery 차이 결론 반영)`으로 바꿨다. 기존 citation_status는 모두 유지했다.

- `models/ADCIRC/README.md`
- `models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md`
- `models/ADCIRC/manual-notes/05-input-files-reference.md`
- `models/ADCIRC/manual-notes/06-parameter-definitions.md`
- `models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md`
- `models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md`
- `models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md`
- `models/ADCIRC/manual-notes/19-ice-coverage.md`
- `models/ADCIRC/source-analysis/adcirc-3d-mode.md`
- `models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md`
- `models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md`
- `models/ADCIRC/source-analysis/adcirc-baseline-anatomy.md`
- `models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md`
- `models/ADCIRC/source-analysis/adcirc-boundary-conditions.md`
- `models/ADCIRC/source-analysis/adcirc-fort-files-reference.md`
- `models/ADCIRC/source-analysis/adcirc-gwce-implementation.md`
- `models/ADCIRC/source-analysis/adcirc-hotstart.md`
- `models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md`
- `models/ADCIRC/source-analysis/adcirc-momentum-implementation.md`
- `models/ADCIRC/source-analysis/adcirc-nodal-attributes.md`
- `models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md`
- `models/ADCIRC/source-analysis/adcirc-parallel-implementation.md`
- `models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md`
- `models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md`
- `models/ADCIRC/source-analysis/adcirc-swan-coupling.md`
- `models/ADCIRC/source-analysis/adcirc-tidal-forcing.md`
- `models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md`
- `models/ADCIRC/source-analysis/adcirc-topic-map.md`
- `models/ADCIRC/source-analysis/adcirc-weir-boundary.md`
- `models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md`
- `models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md`
- `models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md`
- `models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md`
- `models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md`

## 확인한 범위

§5의 A–F·H 묶음마다 최종 결론 문장과 반영 줄의 일치를 검사했다. X·G 묶음에 새 반영 위치가 없음을 검사했다. 모든 E 묶음의 결함 후보 표 위치를 검사했다. 수정한 결론 표의 열 수를 검사했다. frontmatter의 날짜와 citation_status를 검사했다. 다섯 보고서의 변경 전후 SHA-256이 같음을 확인했다.

근거 원문은 보고서의 인용을 옮겼다. 사용자 지정 기존 후보 세 건의 원문은 추가로 열어 확인했다. 모델 실행과 컴파일은 하지 않았다. 수치 결과와 물리 타당성은 검증하지 않았다. Git 상태를 바꾸는 명령은 실행하지 않았다. 다른 모델 노트와 대조 보고서는 수정하지 않았다.
