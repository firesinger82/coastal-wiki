# SWASH 판독 기록 전수 대조 — code-48

대조일은 2026-10-15이다.
대상 원문은 각 기록의 frontmatter `file:`에 지정된 파일이다.
각 구간의 원문을 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
원문 출력 한 건의 최대 길이는 83행이었다.
모든 구간에서 조건·수치 대입·계수·초기값·주석 수식·분기 의미·바깥 블록의 종료 행을 대조했다.
기록 끝의 코드 사실 목록도 같은 원문 전체와 대조했다.

| 기록 | 대조한 구간 행 | 대조한 코드 사실 행 | 대조한 원문 행 | 정정 | 보완 | 이상 없음 |
|---|---:|---:|---:|---:|---:|---:|
| [SwashUServ.ftn90.md](../swash/src/SwashUServ.ftn90.md) | 61 | 10 | 2,823 | 2 | 57 | 14 |
| [SwashUSpongLayer.ftn90.md](../swash/src/SwashUSpongLayer.ftn90.md) | 7 | 4 | 232 | 1 | 6 | 4 |
| [SwashUWindStress.ftn90.md](../swash/src/SwashUWindStress.ftn90.md) | 12 | 5 | 466 | 0 | 8 | 9 |
| [SwashUpdDepu.ftn90.md](../swash/src/SwashUpdDepu.ftn90.md) | 14 | 4 | 465 | 1 | 13 | 5 |
| 합계 | 94 | 23 | 3,986 | 4 | 84 | 32 |

구간 행 수는 각 기록 표의 구간 행을 센 값이다.
코드 사실 행 수는 각 기록 끝의 목록 항목을 센 값이다.
원문 행 수는 빈 행과 주석을 포함한다.
정정과 보완은 해당 표시가 붙은 기록 행 수이다.
두 표시가 함께 붙은 3개 행은 정정과 보완 양쪽에 포함했다.
중복 집계 행은 `SwashUServ.ftn90.md:299–369`, `SwashUServ.ftn90.md:636–706`, `SwashUpdDepu.ftn90.md:42–95`이다.
이상 없음은 수정 표시가 없는 구간 행과 코드 사실 행을 합친 값이다.

아래 목록의 원문 행은 해당 기록의 `file:` 파일을 기준으로 한다.
코드 사실 번호는 각 기록 끝의 목록 순서이다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [SwashUServ.ftn90.md:17–99](../swash/src/SwashUServ.ftn90.md) (보완) | 입력 배열 선언과 ient 초기값을 축약했다. | 입력 배열과 ient의 선언을 원문 그대로 인용했다. | 69–71,78 |
| [SwashUServ.ftn90.md:100–139](../swash/src/SwashUServ.ftn90.md) (보완) | uvc 초기화식과 반복문 종료 행을 생략했다. | uvc 초기화식을 인용하고 반복문 종료 행을 명시했다. | 107,109–118,151–159 |
| [SwashUServ.ftn90.md:140–162](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 루프 원문과 방향 부호 분기의 ELSE 부재를 생략했다. | 루프 원문·종료 행과 ELSE 부재를 명시했다. | 109–118,140–159 |
| [SwashUServ.ftn90.md:163–244](../swash/src/SwashUServ.ftn90.md) (보완) | ient 초기값을 요약했다. | 초기 선언을 원문 인용했다. | 219 |
| [SwashUServ.ftn90.md:245–298](../swash/src/SwashUServ.ftn90.md) (보완) | 발산 초기화식을 요약했다. 방향 부호 분기의 ELSE 부재를 생략했다. | 초기값과 ELSE 부재를 원문에 맞게 추가했다. | 247–248,269–273 |
| [SwashUServ.ftn90.md:299–369](../swash/src/SwashUServ.ftn90.md) (정정·보완) | 대칭 양의 정부호를 가정이라는 구분 없이 기술했다. RILU 평균 설명과 Ax=b 인용을 생략했다. | 주석의 가정을 명시했다. RILU 설명·가중치·선형계 식을 보완했다. | 346,360–368 |
| [SwashUServ.ftn90.md:370–400](../swash/src/SwashUServ.ftn90.md) (보완) | ient 초기값을 요약했다. | 초기 선언을 원문 인용했다. | 392 |
| [SwashUServ.ftn90.md:401–428](../swash/src/SwashUServ.ftn90.md) (보완) | 종료 기준의 주석 식과 reps·amod 대입을 요약했다. | 종료 부등식과 아래첨자 및 계수 대입을 인용했다. | 408–409,425–427 |
| [SwashUServ.ftn90.md:429–478](../swash/src/SwashUServ.ftn90.md) (보완) | CSR 주소 계산과 전처리 배열 초기값을 요약했다. | CSR 인덱스·주소 저장과 초기화 대입을 원문 인용했다. | 433–474 |
| [SwashUServ.ftn90.md:479–544](../swash/src/SwashUServ.ftn90.md) (보완) | 잔차·전진대입 초기값과 허용오차 변경식을 요약했다. | 초기값·LU 주석식·대입 범위·허용오차 변경식과 조건 종료 행을 추가했다. | 483,493–509,519–543 |
| [SwashUServ.ftn90.md:545–594](../swash/src/SwashUServ.ftn90.md) (보완) | 반복 안의 초기값·LU 주석식·대입 범위를 요약했다. | 초기값과 주석식 및 전진·후진 범위·반복 종료 행을 인용했다. | 545–585,615 |
| [SwashUServ.ftn90.md:595–635](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 반복문과 잔차 초기화식을 요약했다. 출력 분기의 ELSE 부재를 생략했다. | 반복문 원문·종료 행과 잔차 초기화식 및 ELSE 부재를 명시했다. | 545,595–632 |
| [SwashUServ.ftn90.md:636–706](../swash/src/SwashUServ.ftn90.md) (정정·보완) | 대칭 양의 정부호를 가정이라는 구분 없이 기술했다. RILU 평균 설명과 Ax=b 인용을 생략했다. | 주석의 가정을 명시했다. RILU 설명·가중치·선형계 식을 보완했다. | 683,697–705 |
| [SwashUServ.ftn90.md:707–759](../swash/src/SwashUServ.ftn90.md) (보완) | ient 초기 선언과 종료 기준의 주석 식을 생략했다. | 초기 선언과 종료 부등식·아래첨자를 원문 인용했다. | 729,745–746 |
| [SwashUServ.ftn90.md:760–786](../swash/src/SwashUServ.ftn90.md) (보완) | CSR 주소 계산과 전처리 초기화를 요약했다. | 복원 인덱스와 배열 초기화 대입을 인용했다. | 770–785 |
| [SwashUServ.ftn90.md:787–815](../swash/src/SwashUServ.ftn90.md) (보완) | CSR 소거 주소와 초기값을 요약했다. | 소거 인덱스·주소 저장·초기화를 원문 인용했다. | 789–811 |
| [SwashUServ.ftn90.md:816–881](../swash/src/SwashUServ.ftn90.md) (보완) | 초기값과 LU 주석식·대입 범위·허용오차 변경식을 요약했다. | 초기값·주석식·대입 범위·허용오차 변경식과 조건 종료 행을 추가했다. | 820–878 |
| [SwashUServ.ftn90.md:882–931](../swash/src/SwashUServ.ftn90.md) (보완) | 반복 안의 초기값·LU 주석식·대입 범위를 요약했다. | 초기값과 주석식 및 전진·후진 범위·반복 종료 행을 인용했다. | 882–922,952 |
| [SwashUServ.ftn90.md:932–972](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 반복문과 잔차 초기화식을 요약했다. 출력 분기의 ELSE 부재를 생략했다. | 반복문 원문·종료 행과 잔차 초기화식 및 ELSE 부재를 명시했다. | 882,932–969 |
| [SwashUServ.ftn90.md:973–1035](../swash/src/SwashUServ.ftn90.md) (보완) | RILU 설명을 구체적으로 적지 않았다. 가중치 값을 원문 인용하지 않았다. | ILU와 MILU의 평균이라는 설명과 amod 값을 원문에 맞게 보완했다. | 1028–1030 |
| [SwashUServ.ftn90.md:1036–1099](../swash/src/SwashUServ.ftn90.md) (보완) | 초기값·가중치·CSR 주소 계산을 요약했다. | 선언·초기값·가중치와 주소 대입을 원문 인용했다. | 1048,1064–1093 |
| [SwashUServ.ftn90.md:1151–1183](../swash/src/SwashUServ.ftn90.md) (보완) | ient 선언과 대각 초기화 대입을 요약했다. | 초기 선언과 대각 인덱스 대입을 인용했다. | 1162,1180 |
| [SwashUServ.ftn90.md:1184–1210](../swash/src/SwashUServ.ftn90.md) (보완) | 탐색 플래그와 rval 대입을 요약했다. | 플래그·원소 대입을 인용했다. 일치 후에도 탐색 루프가 계속됨을 명시했다. | 1190–1201 |
| [SwashUServ.ftn90.md:1211–1263](../swash/src/SwashUServ.ftn90.md) (보완) | 전처리 선형계의 주석 식을 생략했다. | Ax=b를 원문 인용했다. | 1258 |
| [SwashUServ.ftn90.md:1264–1318](../swash/src/SwashUServ.ftn90.md) (보완) | 계수 주석 식과 종료 부등식을 요약했다. ient 초기 선언을 생략했다. | 계수 식·종료 부등식·아래첨자와 초기 선언을 원문 인용했다. | 1286,1293–1302 |
| [SwashUServ.ftn90.md:1319–1372](../swash/src/SwashUServ.ftn90.md) (보완) | 허용오차·CSR 인덱스·초기값을 요약했다. 전처리 분기의 ELSE 부재를 생략했다. | 계수·인덱스·초기값과 ELSE 부재·종료 행을 명시했다. | 1321–1371 |
| [SwashUServ.ftn90.md:1373–1419](../swash/src/SwashUServ.ftn90.md) (보완) | 잔차·노름 초기값과 복사 및 허용오차 대입을 요약했다. | 초기값·복사·허용오차 대입과 조건 종료 행을 인용했다. | 1377–1418 |
| [SwashUServ.ftn90.md:1420–1443](../swash/src/SwashUServ.ftn90.md) (보완) | rho 초기화와 LU 주석식을 요약했다. 반복 조건의 닫힘을 생략했다. | 초기값·주석식과 GOTO 반복의 조건 범위를 명시했다. | 1420–1442,1680–1682 |
| [SwashUServ.ftn90.md:1444–1509](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 반복 조건을 이름으로만 적었다. 초기값·대입 범위와 ELSE 부재를 생략했다. | 반복 조건식·종료 행과 대입 초기값·범위 및 ELSE 부재를 명시했다. | 1420,1444–1508,1682 |
| [SwashUServ.ftn90.md:1510–1553](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 반복 조건과 초기값을 요약했다. 오류 이동 목적지를 생략했다. | 반복 조건식·초기값·조건 종료 행과 GOTO 목적지를 명시했다. | 1420,1512–1552,1682–1684 |
| [SwashUServ.ftn90.md:1554–1621](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 반복 조건과 LU 주석식·초기값·대입 범위를 요약했다. ELSE 부재를 생략했다. | 반복 조건식·종료 행과 LU 주석식·대입 초기값·범위 및 ELSE 부재를 명시했다. | 1420,1554–1620,1682 |
| [SwashUServ.ftn90.md:1622–1664](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 반복 조건과 초기값·ELSE 기본값을 요약했다. 오류 이동 목적지를 생략했다. | 조건식·초기값·기본값과 조건 종료 행 및 GOTO 목적지를 명시했다. | 1420,1624–1663,1682–1684 |
| [SwashUServ.ftn90.md:1665–1706](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 반복 조건과 잔차 초기값을 요약했다. 출력 분기의 ELSE 부재를 생략했다. | 반복 조건식·종료 범위와 잔차 초기값 및 ELSE 부재를 명시했다. | 1420,1665–1703 |
| [SwashUServ.ftn90.md:1707–1779](../swash/src/SwashUServ.ftn90.md) (보완) | RILU 평균 설명과 가중치·선형계 식의 인용을 생략했다. | RILU 평균 설명과 amod 값·Ax=b를 추가했다. | 1766–1774 |
| [SwashUServ.ftn90.md:1780–1839](../swash/src/SwashUServ.ftn90.md) (보완) | irow 선언·계수 주석 식·종료 부등식과 초기 선언을 요약했다. | irow·ient 선언과 계수 식·종료 부등식·아래첨자를 원문 인용했다. | 1803–1804,1813–1823 |
| [SwashUServ.ftn90.md:1840–1868](../swash/src/SwashUServ.ftn90.md) (보완) | 반복 계수·열 조회·초기값을 요약했다. | 계수·열 조회·초기값과 루프 종료 행을 인용했다. | 1844–1867,1947–1948 |
| [SwashUServ.ftn90.md:1869–1906](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 루프를 이름으로만 적었다. irow 조회와 IF 종료 행을 생략했다. | 루프 원문·종료 행과 열 조회 및 독립 IF 범위를 명시했다. | 1851–1852,1869–1905,1947–1948 |
| [SwashUServ.ftn90.md:1907–1949](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 루프와 열 조회·조건 종료 행을 요약했다. | 바깥 루프 원문·종료 행과 irow 조회·독립 IF 범위를 명시했다. | 1851–1852,1907–1948 |
| [SwashUServ.ftn90.md:1950–2000](../swash/src/SwashUServ.ftn90.md) (보완) | 전처리 초기값·CSR 주소와 해 복사를 요약했다. | 초기값·소거 인덱스·주소 대입과 해 복사를 인용했다. | 1954–1997 |
| [SwashUServ.ftn90.md:2001–2050](../swash/src/SwashUServ.ftn90.md) (보완) | 반복 변수·배열·노름 초기값과 잔차 복사를 요약했다. | 초기값과 복사 대입을 원문 인용했다. | 2001–2045 |
| [SwashUServ.ftn90.md:2051–2093](../swash/src/SwashUServ.ftn90.md) (보완) | 허용오차·내적 초기값과 LU 주석식을 요약했다. 반복 조건 종료 행을 생략했다. | 대입 원문과 주석식 및 각 조건의 종료 행을 명시했다. | 2054–2092,2292 |
| [SwashUServ.ftn90.md:2094–2143](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 반복 조건과 대입 초기값·전진후진 순서를 요약했다. | 조건식·종료 행과 초기값 및 층·셀·열 대입 순서를 인용했다. | 2066,2096–2135,2292 |
| [SwashUServ.ftn90.md:2144–2187](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 반복 조건·초기값·LU 주석식을 요약했다. 오류 이동 목적지를 생략했다. | 조건식·초기값·주석식과 조건 종료 행 및 GOTO 목적지를 명시했다. | 2066,2144–2184,2292–2294 |
| [SwashUServ.ftn90.md:2188–2235](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 반복 조건과 대입 초기값·전진후진 순서를 요약했다. | 조건식·종료 행과 초기값 및 층·셀·열 대입 순서를 인용했다. | 2066,2188–2227,2292 |
| [SwashUServ.ftn90.md:2236–2270](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 반복 조건·초기값·ELSE 기본값과 오류 이동 목적지를 요약했다. | 조건식·초기값·기본값과 조건 종료 행 및 GOTO 목적지를 명시했다. | 2066,2236–2269,2292–2294 |
| [SwashUServ.ftn90.md:2271–2323](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 반복 조건과 잔차 초기값·해 복사를 요약했다. 출력 분기의 ELSE 부재를 생략했다. | 조건식·종료 범위와 초기값·해 복사 및 ELSE 부재를 명시했다. | 2066,2271–2320 |
| [SwashUServ.ftn90.md:2324–2382](../swash/src/SwashUServ.ftn90.md) (보완) | 헤비사이드 함수의 조건과 값을 한국어로만 요약했다. | 구간별 함수 정의 세 행을 원문 인용했다. | 2373–2375 |
| [SwashUServ.ftn90.md:2400–2446](../swash/src/SwashUServ.ftn90.md) (보완) | 초기 선언과 p·s의 주석 의미를 요약했다. | 초기 선언과 도함수 주석 및 해 변수의 의미를 추가했다. | 2409,2420,2424 |
| [SwashUServ.ftn90.md:2447–2477](../swash/src/SwashUServ.ftn90.md) (보완) | 행렬 복사·해와 노름 초기값·허용오차 변경식을 요약했다. | 각 대입식을 원문 인용하고 조건 종료 행을 명시했다. | 2449–2476 |
| [SwashUServ.ftn90.md:2478–2516](../swash/src/SwashUServ.ftn90.md) (보완) | Newton 해 복사·셀별 해 조회·분기별 도함수 대입을 요약했다. | 대입 원문과 조건·반복 종료 행을 명시했다. | 2478–2506,2563 |
| [SwashUServ.ftn90.md:2517–2564](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 반복문과 노름 초기값을 요약했다. 이웃 셀 분기의 ELSE 부재를 생략했다. | 반복문 원문·종료 행과 노름 초기값 및 ELSE 부재를 명시했다. | 2478,2536–2563 |
| [SwashUServ.ftn90.md:2565–2585](../swash/src/SwashUServ.ftn90.md) (보완) | 출력 분기 사슬의 ELSE 부재를 생략했다. | ELSE 부재와 조건 종료 행을 명시했다. | 2569–2582 |
| [SwashUServ.ftn90.md:2627–2672](../swash/src/SwashUServ.ftn90.md) (보완) | ient 초기값을 요약했다. | 초기 선언을 원문 인용했다. | 2651 |
| [SwashUServ.ftn90.md:2673–2727](../swash/src/SwashUServ.ftn90.md) (보완) | CSR 초기값과 이웃 셀 열 대입을 요약했다. 방향 분기의 ELSE 부재를 생략했다. | 초기값·이웃 열 대입과 ELSE 부재 및 블록 종료 행을 명시했다. | 2684–2726 |
| [SwashUServ.ftn90.md:2728–2762](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 루프와 열 순서 초기화·교환·저장식을 요약했다. | 루프 원문·종료 행과 인덱스 교환의 정확한 대입 순서를 인용했다. | 2691–2693,2730–2759,2817–2819 |
| [SwashUServ.ftn90.md:2763–2804](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 루프와 층별 독립 조건의 종료 행을 생략했다. | 루프 원문·종료 행과 독립 IF 범위 및 대각 탐색 범위를 명시했다. | 2691–2693,2763–2803,2817–2819 |
| [SwashUServ.ftn90.md:2805–2823](../swash/src/SwashUServ.ftn90.md) (보완) | 바깥 루프와 IF의 종료 행을 요약했다. | 루프 원문과 정확한 종료 행 및 마지막 ia 대입의 소속을 명시했다. | 2691–2693,2805–2821 |
| [SwashUSpongLayer.ftn90.md:50–98](../swash/src/SwashUSpongLayer.ftn90.md) (보완) | ient 초기값을 문장으로만 요약했다. | 초기값 선언을 원문 그대로 인용했다. | 72 |
| [SwashUSpongLayer.ftn90.md:99–144](../swash/src/SwashUSpongLayer.ftn90.md) (보완) | 경계 선택·최소 거리 갱신을 요약했다. | 선택 대입식과 경계 면 반복문 및 IF 종료 행을 인용했다. | 108–109,118,137–143 |
| [SwashUSpongLayer.ftn90.md:145–164](../swash/src/SwashUSpongLayer.ftn90.md) (보완) | 바깥 루프와 기본값을 요약했다. | 바깥 루프 원문·종료 행과 경계 저장·기본값 및 ELSE 부재를 추가했다. | 106,111,145–163,230 |
| [SwashUSpongLayer.ftn90.md:165–193](../swash/src/SwashUSpongLayer.ftn90.md) (보완) | 바깥 루프와 꼭짓점 선택 블록의 종료 행을 생략했다. | 루프 원문과 각 블록 종료 행을 명시했다. | 106,165–190,208,228–230 |
| [SwashUSpongLayer.ftn90.md:194–209](../swash/src/SwashUSpongLayer.ftn90.md) (보완) | 바깥 루프와 최소 거리 대입을 요약했다. | 루프 원문·종료 행과 최소 거리 및 경계 셀 대입을 인용했다. | 106,165,172,201–208,228–230 |
| [SwashUSpongLayer.ftn90.md:210–232](../swash/src/SwashUSpongLayer.ftn90.md) (보완) | 바깥 루프와 기본값을 요약했다. | 바깥 루프 원문·종료 행과 경계 저장·기본값 및 ELSE 부재를 추가했다. | 106,165,210–230 |
| [SwashUSpongLayer.ftn90.md:코드 사실 4](../swash/src/SwashUSpongLayer.ftn90.md) (정정) | 감쇠 블록의 부정 비교 조건을 dmin<=width로 바꿔 적었다. | 원문의 .not. dmin > width 조건을 그대로 적었다. | 145,210 |
| [SwashUWindStress.ftn90.md:1–59](../swash/src/SwashUWindStress.ftn90.md) (보완) | 로그 분포 수식을 설명으로 대체했다. Cd 정의를 원문 형태로 인용하지 않았다. | 주석의 분수식 세 행과 Cd 정의를 그대로 인용했다. | 47–49,58 |
| [SwashUWindStress.ftn90.md:60–126](../swash/src/SwashUWindStress.ftn90.md) (보완) | ient 초기값과 10 m 보정계수를 요약했다. | 초기 선언과 바람 보정의 방향을 명시했다. | 87,93 |
| [SwashUWindStress.ftn90.md:127–146](../swash/src/SwashUWindStress.ftn90.md) (보완) | 입력 계수 대입을 원문 그대로 인용하지 않았다. | alpha와 wcrstp 대입식을 인용했다. | 133–134 |
| [SwashUWindStress.ftn90.md:215–263](../swash/src/SwashUWindStress.ftn90.md) (보완) | 일정 항력계수와 상대 바람의 ELSE 대입을 요약했다. | 계수·바람 대입식을 인용하고 분기 종료 행을 명시했다. | 221–226,249–254,429 |
| [SwashUWindStress.ftn90.md:264–297](../swash/src/SwashUWindStress.ftn90.md) (보완) | iwind 바깥 분기를 조건식 없이 지칭했다. ELSE 대입을 요약했다. | 분기 사슬의 조건과 종료 행 및 바람 성분 대입을 인용했다. | 221,264–294,327–329,429 |
| [SwashUWindStress.ftn90.md:298–330](../swash/src/SwashUWindStress.ftn90.md) (보완) | 바깥 조건을 이름으로 적었다. 반복 초기값과 이전 값 복사를 요약했다. | 바깥 조건·종료 행과 nit·sold 대입을 원문 인용했다. | 264–270,298–329,429 |
| [SwashUWindStress.ftn90.md:331–378](../swash/src/SwashUWindStress.ftn90.md) (보완) | iwind 바깥 조건과 ELSE 대입을 요약했다. | 분기 사슬 원문·종료 행과 바람 성분 대입을 인용했다. | 221,331,358–363,429 |
| [SwashUWindStress.ftn90.md:379–429](../swash/src/SwashUWindStress.ftn90.md) (보완) | iwind 바깥 조건과 ELSE 대입을 요약했다. | 분기 사슬 원문·종료 행과 바람 성분 대입을 인용했다. | 221,379,404–409,429 |
| [SwashUpdDepu.ftn90.md:42–95](../swash/src/SwashUpdDepu.ftn90.md) (정정·보완) | 격자 이웃 인덱스를 상하류 포인터로 단정했다. ient 선언을 요약했다. | 원문의 격자 위치로 고쳤다. 초기값 선언을 인용했다. | 59,61–78 |
| [SwashUpdDepu.ftn90.md:96–146](../swash/src/SwashUpdDepu.ftn90.md) (보완) | 격자 매핑을 이름으로 요약했다. | 1차원 매핑 대입과 조건 종료 행을 인용했다. | 98,108–109,123,135–136,463 |
| [SwashUpdDepu.ftn90.md:147–169](../swash/src/SwashUpdDepu.ftn90.md) (보완) | 바깥 oned 조건과 계수·격자 매핑을 요약했다. | 바깥 조건식·종료 행과 계수·매핑 대입을 원문 인용했다. | 98,149–168,200–202,463 |
| [SwashUpdDepu.ftn90.md:170–208](../swash/src/SwashUpdDepu.ftn90.md) (보완) | 바깥 oned·corrdep 조건을 이름으로만 적었다. 속도 분기 사슬의 ELSE 부재를 생략했다. | 바깥 조건 원문과 종료 행 및 ELSE 부재를 명시했다. | 98,149,159,170–207,463 |
| [SwashUpdDepu.ftn90.md:209–241](../swash/src/SwashUpdDepu.ftn90.md) (보완) | 바깥 oned 조건과 매핑을 요약했다. | oned 조건식·종료 행과 2차원 매핑을 인용했다. | 98,209–237,313,463 |
| [SwashUpdDepu.ftn90.md:242–270](../swash/src/SwashUpdDepu.ftn90.md) (보완) | 바깥 풍상 분기 조건과 매핑을 요약했다. | 바깥 조건식·종료 행과 v점 매핑을 인용했다. | 98,211,249–266,313,463 |
| [SwashUpdDepu.ftn90.md:271–314](../swash/src/SwashUpdDepu.ftn90.md) (보완) | 바깥 depcds 조건의 부정과 매핑 원문을 생략했다. | 부정 조건과 ELSE 소속·종료 행 및 매핑을 인용했다. | 98,211,271,280–281,300–313,463 |
| [SwashUpdDepu.ftn90.md:315–349](../swash/src/SwashUpdDepu.ftn90.md) (보완) | 바깥 조건과 계수·반복 끝점·격자 매핑을 요약했다. | 조건식·종료 행과 계수·끝점·매핑 대입을 인용했다. | 98,317–344,380–382,444,463 |
| [SwashUpdDepu.ftn90.md:350–383](../swash/src/SwashUpdDepu.ftn90.md) (보완) | 바깥 조건을 이름으로만 적었다. 속도 분기 사슬의 ELSE 부재를 생략했다. | 바깥 조건·루프 원문과 종료 행 및 ELSE 부재를 명시했다. | 98,317,331–333,350–382,444,463 |
| [SwashUpdDepu.ftn90.md:384–390](../swash/src/SwashUpdDepu.ftn90.md) (보완) | 바깥 조건과 반복 끝점 대입을 요약했다. | 바깥 조건식·종료 행과 nend 대입을 인용했다. | 98,317,385–389,444,463 |
| [SwashUpdDepu.ftn90.md:391–409](../swash/src/SwashUpdDepu.ftn90.md) (보완) | 바깥 조건과 격자 매핑을 요약했다. | 바깥 조건식·종료 행과 v점 매핑을 인용했다. | 98,317,391–404,440–444,463 |
| [SwashUpdDepu.ftn90.md:410–445](../swash/src/SwashUpdDepu.ftn90.md) (보완) | 바깥 조건을 이름으로만 적었다. 속도 분기 사슬의 ELSE 부재를 생략했다. | 바깥 조건·루프 원문과 종료 행 및 ELSE 부재를 명시했다. | 98,317,391–393,410–444,463 |
| [SwashUpdDepu.ftn90.md:446–465](../swash/src/SwashUpdDepu.ftn90.md) (보완) | 바깥 oned 조건과 건조점 기본값을 요약했다. | 바깥 조건식·종료 행과 hu·hv 기본값을 인용했다. | 98,448–449,463 |

수정하지 않은 행은 다음과 같다.

| 기록 | 이상 없는 구간 행 | 이상 없는 코드 사실 행 |
|---|---|---|
| SwashUServ.ftn90.md | 1–16, 1100–1150, 2383–2399, 2586–2626 | 1–10 |
| SwashUSpongLayer.ftn90.md | 1–49 | 1–3 |
| SwashUWindStress.ftn90.md | 147–183, 184–214, 430–438, 439–466 | 1–5 |
| SwashUpdDepu.ftn90.md | 1–41 | 1–4 |

층 방향은 각 원문의 주석과 인덱스 용도를 확인했다.

| 원문 | 확인한 내용 | 원문 행 |
|---|---|---|
| SwashUServ.ftn90 | 주석은 ks·ke를 수직 인덱스의 처음·끝으로 설명한다. k는 수직 층 반복 변수이다. 이 파일에는 k=1을 최상층으로 명시한 주석이 없다. 기록은 k-1을 아래층으로 해석하지 않는다. | 69–81, 1808, 2637, 2657 |
| SwashUSpongLayer.ftn90 | k=1..3은 셀 꼭짓점 선택 반복이다. 이 반복은 수직 층 반복이 아니다. | 77–78, 178–190 |
| SwashUWindStress.ftn90 | perot 호출은 수직 범위 1..1을 전달한다. 이 파일에는 해당 인덱스의 상하 방향을 명시한 주석이 없다. 기록에는 상하 방향 해석을 추가하지 않았다. | 215–217, 244–247 |
| SwashUpdDepu.ftn90 | 입력 u·v의 주석은 수심 평균 속도라고 명시한다. 이 파일에는 수직 층 반복이 없다. | 54–55, 96–465 |

전처리 규칙은 [switch.pl 57–66행](../../../../../models/SWASH/raw/source_code/swash/switch.pl)을 대조했다.
해당 규칙은 각 스위치 변수가 `TRUE`에 일치할 때 대응하는 행 첫머리 표시를 제거한다.
규칙의 표시는 `!TIMG`, `!MPI`, `!F95`, `!DOS`, `!UNIX`, `!/Cray`, `!/SGI`, `!/impi`, `!CVIS`, `!MatL4`이다.
네 대상 원문에서 이 표시로 시작하는 행은 0개였다.

수정 후 조건·계산식·기본값의 인용 누락 후보를 다시 확인했다.
백틱 인용 문자열과 직접 붙은 행 번호의 보조 점검에서 불일치는 없었다.
Markdown 표의 구분자 오류는 없었다.
네 기록의 구간 경계와 frontmatter는 변경하지 않았다.
네 원문의 SHA-256은 대조 전 값과 일치했다.
모델은 실행하지 않았다.

정정 4, 보완 84, 이상 없음 32
