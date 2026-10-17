# FUNWAVE 판독 기록 전수 대조 (2026-10-17)

대상은 사용자 지정 기록 12개다.
원문은 각 기록 frontmatter의 `file:` 경로다.
대조 단위는 기록 표의 구간 행이다.
원문 행 수에는 주석과 빈 행을 포함한다.
원문은 구간마다 `nl -ba`와 `sed -n 'A,Bp'`로 열었다.
모델은 실행하지 않았다.

현재 상태: 대상 기록 12개 대조 완료.
표의 기록 경로는 `_staging/recovery/read/FUNWAVE/` 기준이다.
대조한 구간 행 수는 대상 기록 표에서 센 165행이다.
대조한 원문 행 수는 각 구간의 양 끝을 포함해 센 3951행이다.
정정·보완은 해당 표지가 붙은 구간 행을 각각 센다.
두 표지가 함께 붙은 구간 행 4개는 정정과 보완에 모두 포함한다.
이상 없음은 두 표지가 모두 없는 구간 행을 센다.
원문의 SHA-256은 대상 기록 12개의 frontmatter 값과 모두 일치했다.
각 기록의 frontmatter와 구간 경계는 보존했다.
`wavemaker.F`에는 `!$cuf`, `attributes(global)`, `<<<...>>>`, `!$acc`, `!$omp` 지시가 없다.

| 기록 | 상태 | 대조한 구간 행 수 | 대조한 원문 행 수 | 정정 | 보완 | 두 표지 모두 | 이상 없음 |
|---|---|---:|---:|---:|---:|---:|---:|
| FUNWAVE-GPU/src/wavemaker.F.md | 완료 | 59 | 2430 | 5 | 46 | 4 | 12 |
| FUNWAVE-TVD/GNUMake/Essential/Make_Essential.md | 완료 | 17 | 264 | 0 | 8 | 0 | 9 |
| FUNWAVE-TVD/GNUMake/Essential/Make_Essential_gcc10.md | 완료 | 17 | 266 | 0 | 8 | 0 | 9 |
| FUNWAVE-TVD/GNUMake/Makefile.md | 완료 | 8 | 104 | 0 | 0 | 0 | 8 |
| FUNWAVE-TVD/GNUMake/Old_Version_Makefiles/Makefile-Jim-SGI.md | 완료 | 8 | 111 | 0 | 0 | 0 | 8 |
| FUNWAVE-TVD/GNUMake/Old_Version_Makefiles/Makefile-Jim-intel.md | 완료 | 8 | 111 | 0 | 0 | 0 | 8 |
| FUNWAVE-TVD/GNUMake/Old_Version_Makefiles/Makefile-Koehr-Meteo-intel.md | 완료 | 8 | 112 | 0 | 0 | 0 | 8 |
| FUNWAVE-TVD/GNUMake/Old_Version_Makefiles/Makefile-Koehr-Sediment-intel.md | 완료 | 8 | 112 | 0 | 0 | 0 | 8 |
| FUNWAVE-TVD/GNUMake/Old_Version_Makefiles/Makefile-Koehr-Vessel-Sediment-intel.md | 완료 | 8 | 112 | 0 | 0 | 0 | 8 |
| FUNWAVE-TVD/GNUMake/Old_Version_Makefiles/Makefile-Koehr-Vessel-intel.md | 완료 | 8 | 112 | 0 | 0 | 0 | 8 |
| FUNWAVE-TVD/GNUMake/Old_Version_Makefiles/Makefile-Koehr-intel.md | 완료 | 8 | 112 | 0 | 0 | 0 | 8 |
| FUNWAVE-TVD/GNUMake/Old_Version_Makefiles/Makefile-Lightning-Cray.md | 완료 | 8 | 105 | 0 | 0 | 0 | 8 |
| 합계 | 완료 | 165 | 3951 | 5 | 62 | 4 | 102 |

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| FUNWAVE-GPU/src/wavemaker.F.md:67–105 | myid 조건과 MPI_FINALIZE의 범위가 모호했다. 비활성 Yc_WK 식을 생략했다. | 메시지 출력의 myid 조건과 MPI_FINALIZE 호출을 구분했다. 주석의 네 식과 전처리 중첩을 인용했다. (정정·보완) | 67–105·189·194 |
| FUNWAVE-GPU/src/wavemaker.F.md:106–140 | MPI 호출 범위가 모호했다. 초기값·증가식·주석 식과 바깥 조건식을 생략했다. | MPI 호출이 myid 조건 밖임을 명시했다. 누락된 식과 조건식 및 종료 행을 인용했다. (정정·보완) | 67·86·106–140·174·188–194 |
| FUNWAVE-GPU/src/wavemaker.F.md:141–175 | MPI 호출 범위가 모호했다. 초기값·증가식·주석 식과 바깥 조건식을 생략했다. | MPI 호출이 myid 조건 밖임을 명시했다. 식·바깥 조건식과 ELSE 없는 종료를 보완했다. (정정·보완) | 67·86·106–107·141–175·188–194 |
| FUNWAVE-GPU/src/wavemaker.F.md:176–213 | 바깥 조건을 이름으로만 표시했다. 188·189행 종료를 묶어 설명했다. | 바깥 조건식을 인용했다. 각 ENDIF의 실제 대상과 원문 주석의 불일치를 명시했다. (보완) | 67·86·106·176–194 |
| FUNWAVE-GPU/src/wavemaker.F.md:214–273 | 바깥 조건식을 생략했다. 카운터 기본값과 필터 후 인덱스 대응을 말로만 설명했다. | 바깥 조건식과 종료 행을 보완했다. 기본값과 방향 압축의 배열 인덱스를 인용했다. (보완) | 196·217–234·325 |
| FUNWAVE-GPU/src/wavemaker.F.md:274–310 | 바깥 조건식과 CRAY 분기의 식을 생략했다. | WK_DATA2D 조건식과 종료 행을 명시했다. CRAY 분기의 위상 식을 직접 인용했다. (보완) | 196·281–289·325 |
| FUNWAVE-GPU/src/wavemaker.F.md:311–345 | 바깥 조건식을 생략했다. T_brk 대입을 설명으로만 적었다. | WK_DATA2D 조건식과 두 T_brk 대입식을 인용했다. (보완) | 196·311–338 |
| FUNWAVE-GPU/src/wavemaker.F.md:346–389 | EqualEnergy 뒤 호출의 바깥 범위를 명시하지 않았다. 종료 대상을 묶어 설명했다. | CALCULATE_Cm_Sm은 EqualEnergy 밖이며 CARTESIAN 안임을 명시했다. 종료 대상을 구분했다. (보완) | 346–389 |
| FUNWAVE-GPU/src/wavemaker.F.md:462–494 | 바깥 조건식과 초기값·증가식을 생략했다. 루프 뒤 계산의 범위를 명시하지 않았다. | 조건식과 대입식을 인용했다. WHILE 밖의 계산과 바깥 블록 종료를 구분했다. (보완) | 449–493·527·555–568 |
| FUNWAVE-GPU/src/wavemaker.F.md:495–528 | 바깥 조건식과 초기값·증가식을 생략했다. ELSE 없는 부호 분기를 표시하지 않았다. | 조건식과 대입식을 인용했다. 루프 뒤 범위와 ELSE 없는 종료를 명시했다. (보완) | 449–463·495–568 |
| FUNWAVE-GPU/src/wavemaker.F.md:529–569 | 바깥 조건식을 생략했다. Dir2D 대입과 출력 단위 변환을 말로만 요약했다. | 닫힌 부호 분기와 남은 바깥 조건을 구분했다. 배열 인덱스·기본값·도 단위 변환을 인용했다. (보완) | 449–462·527–568 |
| FUNWAVE-GPU/src/wavemaker.F.md:570–605 | 배열의 인덱스 대응과 오류 메시지를 생략했다. 분기 밖의 대상을 이름 없이 적었다. | 성분 대입과 오류 메시지를 인용했다. 584행 조건 종료 후에도 두 성분 루프 안임을 명시했다. (보완) | 573–604 |
| FUNWAVE-GPU/src/wavemaker.F.md:643–688 | Cm/Sm 초기값을 말로 적었다. 주석의 좌표식을 생략했다. | ZERO 초기값과 비활성 npx/npy 좌표식 네 개를 인용했다. (보완) | 643–668 |
| FUNWAVE-GPU/src/wavemaker.F.md:689–746 | 반복 횟수와 Stokes_Drift_Ser 기본값을 말로 적었다. | 두 초기 대입식을 직접 인용했다. (보완) | 731·744 |
| FUNWAVE-GPU/src/wavemaker.F.md:747–796 | 초기 대입과 주석 식을 생략했다. PERIODIC 종료 위치를 명시하지 않았다. | ZERO 초기값과 주석의 Zlev·좌표식을 인용했다. 공간 루프는 PERIODIC 조건 밖임을 명시했다. (보완) | 748–796 |
| FUNWAVE-GPU/src/wavemaker.F.md:873–905 | 초기값·증가식·선택 대입을 말로 적었다. 바깥 블록 종료를 생략했다. | 대입식을 인용했다. WHILE 밖 계산의 조건과 ELSE 없는 부호 분기 종료를 명시했다. (보완) | 873–944 |
| FUNWAVE-GPU/src/wavemaker.F.md:906–945 | SMALL 임계 조건을 비영 방향이라는 이름으로만 적었다. 초기값·증가식과 ELSE 없는 종료를 생략했다. | ABS(InputRAD)>SMALL 조건식을 인용했다. 대입식과 각 블록 종료를 보완했다. (보완) | 873–944 |
| FUNWAVE-GPU/src/wavemaker.F.md:946–986 | 방향 분기를 이름으로만 적었다. Hmo/Hrms 변환 이력의 제거와 예외를 생략했다. | 종료된 조건식을 명시했다. 출력 단위 식과 연도별 변경·Hrms 입력 예외를 보완했다. (보완) | 873·944·950–984 |
| FUNWAVE-GPU/src/wavemaker.F.md:987–1047 | CRAY 분기의 위상 식을 같은 식이라고만 적었다. | CRAY 분기의 식을 직접 인용했다. (보완) | 1039–1040 |
| FUNWAVE-GPU/src/wavemaker.F.md:1048–1078 | 에너지 초기값과 배열 대입을 말로 적었다. | EF 초기값과 Ef10000 인덱스를 인용했다. (보완) | 1048·1071 |
| FUNWAVE-GPU/src/wavemaker.F.md:1079–1113 | 초기값과 주파수 보정 인덱스를 설명으로만 적었다. goto 목적지 행을 생략했다. | 기본값·이전 성분 대입과 goto 대상 1097행을 인용했다. (보완) | 1080–1111 |
| FUNWAVE-GPU/src/wavemaker.F.md:1114–1151 | ktotal 대입과 sumAG 초기값을 인용하지 않았다. | 두 대입식을 직접 인용했다. (보완) | 1118·1128 |
| FUNWAVE-GPU/src/wavemaker.F.md:1152–1199 | 주석의 총에너지·Hrms 식과 비활성 ap·theta 식을 생략했다. | 주석 식 네 개를 실행식과 구분해 인용했다. (보완) | 1152·1168·1174·1176 |
| FUNWAVE-GPU/src/wavemaker.F.md:1200–1235 | 기본값과 주석의 Zlev 식을 생략했다. 성분 저장 인덱스를 말로 요약했다. | 기본값·성분 저장식·주석 식을 인용했다. 저장 구간과 IF 종료를 구분했다. (보완) | 1163–1165·1204–1234 |
| FUNWAVE-GPU/src/wavemaker.F.md:1236–1276 | Theta_Per 인덱스와 주석의 옛 좌표식을 생략했다. PERIODIC 종료를 명시하지 않았다. | 누락 식을 인용했다. 공간 루프가 PERIODIC 조건 밖임을 명시했다. (보완) | 1239–1258 |
| FUNWAVE-GPU/src/wavemaker.F.md:1317–1385 | Ef 기본값과 Hmo/Hrms 이력의 예외를 생략했다. | ZERO 초기값과 연도별 변환 변경·Hrms 입력 예외를 명시했다. (보완) | 1325–1330·1384 |
| FUNWAVE-GPU/src/wavemaker.F.md:1386–1420 | CRAY 분기의 위상 식을 같은 식이라고만 적었다. | CRAY 분기의 식을 직접 인용했다. (보완) | 1389–1390 |
| FUNWAVE-GPU/src/wavemaker.F.md:1421–1467 | ktotal·sumAG 대입과 총에너지 주석 식을 생략했다. | 대입식·주석 식과 방향 분기 종료 행을 보완했다. (보완) | 1425·1435·1457–1459 |
| FUNWAVE-GPU/src/wavemaker.F.md:1468–1527 | 주석 식과 SMALL 대입을 생략했다. 성분 저장 인덱스와 분기 종료를 명시하지 않았다. | 주석 식·대입식을 인용했다. 계산과 저장이 속한 블록을 명시했다. (보완) | 1474–1523 |
| FUNWAVE-GPU/src/wavemaker.F.md:1528–1581 | 기본값과 주석 식을 생략했다. PERIODIC 종료를 명시하지 않았다. | ZERO 초기값과 Zlev·옛 좌표 주석 식을 인용했다. 공간 루프의 범위를 명시했다. (보완) | 1528–1564 |
| FUNWAVE-GPU/src/wavemaker.F.md:1622–1667 | Hmo/Hrms 변환 이력의 입력 예외를 생략했다. | 입력 파고가 Hrms인 경우의 예외를 명시했다. (보완) | 1630–1633 |
| FUNWAVE-GPU/src/wavemaker.F.md:1668–1698 | fm을 최대 주파수로 설명했다. EF 초기값 인용을 생략했다. | 분기 기준을 원문 변수 fm으로 바로잡았다. EF 초기값을 인용했다. (정정·보완) | 1668·1683–1684 |
| FUNWAVE-GPU/src/wavemaker.F.md:1699–1732 | 초기값·주파수 보정 인덱스와 goto 대상 행을 생략했다. | 대입식과 k 루프 밖 goto 대상 1719행을 인용했다. (보완) | 1701–1730 |
| FUNWAVE-GPU/src/wavemaker.F.md:1733–1774 | ktotal 대입과 sumAG 초기값을 인용하지 않았다. | 두 대입식을 직접 인용했다. (보완) | 1737·1744 |
| FUNWAVE-GPU/src/wavemaker.F.md:1775–1834 | 주석의 Hrms·ap·theta·성분별 위상속도·파장 식을 생략했다. | 주석 식을 실행식과 구분해 인용했다. wkn 조건 종료 행을 보완했다. (보완) | 1782–1829 |
| FUNWAVE-GPU/src/wavemaker.F.md:1835–1879 | 초기값·증가식과 ELSE 없는 부호 분기를 생략했다. 1840행 주석과 실행 조건의 차이를 적지 않았다. | 대입식·주석의 비교 연산자·루프 종료와 Theta 대입의 범위를 보완했다. (보완) | 1777–1779·1835–1878 |
| FUNWAVE-GPU/src/wavemaker.F.md:1880–1919 | 바깥 조건을 이름으로만 적었다. 두 ENDDO의 잘못된 원문 주석을 구분하지 않았다. | PERIODIC 종료와 남은 루프를 명시했다. 실제 루프 종료 대상을 밝혔다. (보완) | 1777–1779·1835·1878·1892–1893 |
| FUNWAVE-GPU/src/wavemaker.F.md:1920–1966 | Ef 초기값을 인용하지 않았다. | Ef의 ZERO 대입을 직접 인용했다. (보완) | 1965 |
| FUNWAVE-GPU/src/wavemaker.F.md:1990–2034 | ktotal·sumAG 대입과 비활성 각도 출력식을 생략했다. | 대입식과 주석의 진단 출력식을 인용했다. (보완) | 1994·2001·2019 |
| FUNWAVE-GPU/src/wavemaker.F.md:2081–2127 | 초기값·증가식과 ELSE 없는 부호 분기를 생략했다. 2086행 주석과 실행 조건의 차이를 적지 않았다. | 대입식·주석의 비교 연산자·루프 종료와 Theta 대입의 범위를 보완했다. (보완) | 2037–2039·2081–2124 |
| FUNWAVE-GPU/src/wavemaker.F.md:2128–2164 | 바깥 조건을 이름으로만 적었다. 두 ENDDO의 잘못된 원문 주석을 구분하지 않았다. | PERIODIC 종료와 남은 루프를 명시했다. 실제 루프 종료 대상을 밝혔다. (보완) | 2037–2039·2081·2124·2138–2139 |
| FUNWAVE-GPU/src/wavemaker.F.md:2213–2243 | 주석의 theta 변환식을 생략했다. 주기·진폭의 열 대응을 묶어 설명했다. | 주석 식과 주기 1열·진폭 2열 대입을 직접 인용했다. (보완) | 2235·2242–2243 |
| FUNWAVE-GPU/src/wavemaker.F.md:2244–2279 | 주석의 폭 대입식과 바깥 루프식을 인용하지 않았다. | 주석 식·루프식과 오류 검사 조건의 종료 행을 보완했다. (보완) | 2240·2254·2258 |
| FUNWAVE-GPU/src/wavemaker.F.md:2311–2338 | 격자 간격 대입과 주석의 옛 좌표식을 생략했다. | DXg/DYg 대입과 npx/npy 좌표식을 직접 인용했다. (보완) | 2318–2330 |
| FUNWAVE-GPU/src/wavemaker.F.md:2339–2357 | 바깥 루프 범위를 인용하지 않았다. 조파 영역의 ELSE 없는 종료를 묶어 설명했다. | 루프식을 인용했다. 영역 밖에는 nu_break 대입이 없는 조건 종료를 명시했다. (보완) | 2311–2312·2341–2356 |
| FUNWAVE-GPU/src/wavemaker.F.md:2358–2393 | 세 경계 배열의 초기값을 말로 적었다. | 세 ZERO 대입을 직접 인용했다. (보완) | 2388–2390 |
| FUNWAVE-TVD/GNUMake/Essential/Make_Essential.md:23–41 | 바깥 분기의 종료 위치와 최종 else 없는 PARALLEL 선택을 생략했다. | 각 endif의 종료 대상과 PARALLEL 선택의 최종 else 부재를 명시했다. (보완) | 25–40·80–81 |
| FUNWAVE-TVD/GNUMake/Essential/Make_Essential.md:42–56 | 바깥 조건식을 생략했다. PARALLEL 사슬의 최종 else 부재를 명시하지 않았다. | 바깥 조건식과 종료 행을 인용했다. 두 PARALLEL 사슬의 최종 else 부재를 명시했다. (보완) | 25–56·80–81 |
| FUNWAVE-TVD/GNUMake/Essential/Make_Essential.md:57–72 | 바깥 DEF_FC·컴파일러 조건식을 행 번호와 이름으로만 적었다. | 바깥 조건식과 PGI에서 Onyx로 바뀌는 위치 및 종료 행을 명시했다. (보완) | 25–30·50·57–81 |
| FUNWAVE-TVD/GNUMake/Essential/Make_Essential.md:73–83 | 바깥 DEF_FC·컴파일러·Onyx 조건식을 생략했다. | 구간 시작에 열려 있는 바깥 조건식을 직접 인용했다. (보완) | 25–30·58·73–81 |
| FUNWAVE-TVD/GNUMake/Essential/Make_Essential.md:84–97 | 디버그·컴파일러 선택의 최종 else 부재를 명시하지 않았다. | 두 조건의 else 부재를 명시했다. (보완) | 86–97 |
| FUNWAVE-TVD/GNUMake/Essential/Make_Essential.md:98–113 | 디버그·컴파일러 선택의 최종 else 부재를 명시하지 않았다. | 두 조건의 else 부재를 명시했다. (보완) | 99–110 |
| FUNWAVE-TVD/GNUMake/Essential/Make_Essential.md:114–140 | 세 플래그 조건의 독립 관계와 else 부재를 명시하지 않았다. | 세 조건이 중첩되지 않음을 명시했다. 각 종료와 else 부재를 밝혔다. (보완) | 129–139 |
| FUNWAVE-TVD/GNUMake/Essential/Make_Essential.md:168–192 | 바깥 EXEC 조건식과 내부 선택 사슬의 최종 else 부재를 생략했다. | EXEC 조건식을 인용했다. 각 내부 조건의 종료와 else 부재를 명시했다. (보완) | 158·168–189 |
| FUNWAVE-TVD/GNUMake/Essential/Make_Essential_gcc10.md:23–41 | 바깥 분기의 종료 위치와 최종 else 없는 PARALLEL 선택을 생략했다. | 각 endif의 종료 대상과 PARALLEL 선택의 최종 else 부재를 명시했다. (보완) | 25–40·80–81 |
| FUNWAVE-TVD/GNUMake/Essential/Make_Essential_gcc10.md:42–56 | 바깥 조건식을 생략했다. PARALLEL 사슬의 최종 else 부재를 명시하지 않았다. | 바깥 조건식과 종료 행을 인용했다. 두 PARALLEL 사슬의 최종 else 부재를 명시했다. (보완) | 25–56·80–81 |
| FUNWAVE-TVD/GNUMake/Essential/Make_Essential_gcc10.md:57–72 | 바깥 DEF_FC·컴파일러 조건식을 행 번호와 이름으로만 적었다. | 바깥 조건식과 PGI에서 Onyx로 바뀌는 위치 및 종료 행을 명시했다. (보완) | 25–30·50·57–81 |
| FUNWAVE-TVD/GNUMake/Essential/Make_Essential_gcc10.md:73–83 | 바깥 DEF_FC·컴파일러·Onyx 조건식을 생략했다. | 구간 시작에 열려 있는 바깥 조건식을 직접 인용했다. (보완) | 25–30·58·73–81 |
| FUNWAVE-TVD/GNUMake/Essential/Make_Essential_gcc10.md:84–97 | 디버그·컴파일러 선택의 최종 else 부재를 명시하지 않았다. | 두 조건의 else 부재를 명시했다. (보완) | 86–97 |
| FUNWAVE-TVD/GNUMake/Essential/Make_Essential_gcc10.md:98–115 | 디버그·컴파일러 선택의 최종 else 부재를 명시하지 않았다. | 두 조건의 else 부재를 명시했다. (보완) | 99–112 |
| FUNWAVE-TVD/GNUMake/Essential/Make_Essential_gcc10.md:116–142 | 세 플래그 조건의 독립 관계와 else 부재를 명시하지 않았다. | 세 조건이 중첩되지 않음을 명시했다. 각 종료와 else 부재를 밝혔다. (보완) | 131–141 |
| FUNWAVE-TVD/GNUMake/Essential/Make_Essential_gcc10.md:170–194 | 바깥 EXEC 조건식과 내부 선택 사슬의 최종 else 부재를 생략했다. | EXEC 조건식을 인용했다. 각 내부 조건의 종료와 else 부재를 명시했다. (보완) | 160·170–191 |
| FUNWAVE-GPU/src/wavemaker.F.md:840–872 | MPI_FINALIZE를 그 조건 밖이라고 적어 바깥 전처리 조건의 유지 여부가 모호했다. | myid 조건 밖이며 PARALLEL 또는 MGPU 전처리 조건 및 입력 방향 범위 조건 안임을 명시했다. (정정) | 859–870 |

정정 5, 보완 62, 이상 없음 102
