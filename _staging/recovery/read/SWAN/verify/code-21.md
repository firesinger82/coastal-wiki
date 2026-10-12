# SWAN swanparll.ftn 전수 대조 기록 — code-21

대상 기록은 `_staging/recovery/read/SWAN/swan/src/swanparll.ftn.md`다.
원문은 기록의 `file:`이 지정한 `models/SWAN/raw/source_code/swan/src/swanparll.ftn`이다.
대상은 원문 1–2887행과 겹치는 구간 행이다.
경계 구간 2812–2951행은 전체를 대조한다.
각 구간의 원문은 `nl -ba <원문> | sed -n 'A,Bp'`로 연다.
전처리 표시는 `models/SWAN/raw/source_code/swan/switch.pl` 82–105행을 기준으로 대조한다.
정정·보완·이상 없음은 구간 행을 단위로 센다.
같은 구간에 오류와 누락이 함께 있으면 정정으로 센다.

| 기록 | 대조한 구간 행 수 | 대조한 원문 범위 | 정정 | 보완 | 이상 없음 |
|---|---:|---|---:|---:|---:|
| [swan/src/swanparll.ftn.md](../swan/src/swanparll.ftn.md) | 44 | 1–2951행 전체 | 2 | 28 | 14 |

대조한 원문은 구간 경계에서 합산한 2951행이다.
각 구간은 158행 이하로 열었으며 출력 잘림은 없었다.
정정한 구간은 304–328행과 2097–2136행이다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [swan/src/swanparll.ftn.md:134–185](../swan/src/swanparll.ftn.md) | MPI·NCOH 경로를 비결합 선택으로만 표시했다. | `!MPI!NCOH` 문장의 활성화 조건을 `-mpi` 선택 및 `-coh` 미선택으로 명시했다. | 140·157·173; switch.pl 25·34·89·99–100 |
| [swan/src/swanparll.ftn.md:186–210](../swan/src/swanparll.ftn.md) | PARLL 값과 MPI 상수 대입을 요약했다. | PARLL의 두 분기와 MPI 상수의 대입문을 원문으로 인용했다. | 188–205 |
| [swan/src/swanparll.ftn.md:304–328](../swan/src/swanparll.ftn.md) | 구간 전체를 MPI 경로라고 적었다. NCOH의 스위치 조건을 생략했다. | MPI 표시가 있는 범위를 304–324행으로 한정했다. NCOH 호출에 `-coh` 미선택 조건을 명시했다. | 304–326; switch.pl 89·99–100 |
| [swan/src/swanparll.ftn.md:431–453](../swan/src/swanparll.ftn.md) | NCOH를 비결합 경로로만 표시했다. | MPI 호출에 필요한 `-coh` 미선택 조건을 명시했다. | 437; switch.pl 89·99–100 |
| [swan/src/swanparll.ftn.md:562–586](../swan/src/swanparll.ftn.md) | NCOH를 비결합 경로로만 표시했다. | MPI 호출에 필요한 `-coh` 미선택 조건을 명시했다. | 569–570; switch.pl 89·99–100 |
| [swan/src/swanparll.ftn.md:701–725](../swan/src/swanparll.ftn.md) | NCOH를 비결합 경로로만 표시했다. | MPI_RECV 호출에 필요한 `-coh` 미선택 조건을 명시했다. | 708–709; switch.pl 89·99–100 |
| [swan/src/swanparll.ftn.md:726–833](../swan/src/swanparll.ftn.md) | TIMG를 시간 측정 선택으로만 표시했다. | TIMG 주석에 대응하는 `-timg` 스위치를 명시했다. | 814–815; switch.pl 22·84 |
| [swan/src/swanparll.ftn.md:834–857](../swan/src/swanparll.ftn.md) | TIMG와 NCOH의 스위치 조건을 생략했다. | TIMG에 `-timg` 선택을 명시했다. MPI_BCAST에 `-mpi` 선택 및 `-coh` 미선택을 명시했다. | 841–843·852; switch.pl 84·89·99–100 |
| [swan/src/swanparll.ftn.md:982–1047](../swan/src/swanparll.ftn.md) | NCOH의 스위치 조건과 IDSPLC의 초기값 인용이 빠졌다. 주 프로세스 조건의 종료 행을 생략했다. | `-coh` 미선택 조건을 명시했다. `IDSPLC(0) = 0`을 인용했다. 주 프로세스 조건의 종료 위치와 MPI 호출이 조건 밖이라는 사실을 명시했다. | 989–997·1010–1032; switch.pl 89·99–100 |
| [swan/src/swanparll.ftn.md:1144–1161](../swan/src/swanparll.ftn.md) | SWINT·SWREAL 분기만 나열했다. | 두 자료형 분기에 별도 ELSE가 없음을 명시했다. | 1152–1156 |
| [swan/src/swanparll.ftn.md:1162–1271](../swan/src/swanparll.ftn.md) | TIMG 호출 안내의 선택 스위치가 빠졌다. | `!TIMG!` 주석에 대응하는 `-timg` 스위치를 명시했다. | 1249–1250; switch.pl 22·84 |
| [swan/src/swanparll.ftn.md:1272–1297](../swan/src/swanparll.ftn.md) | TIMG·NCOH의 스위치 조건을 생략했다. 배열 복사를 요약했다. | 시간 측정과 MPI 호출의 선택 조건을 명시했다. 배열 복사문과 오류 조건 종료 위치를 명시했다. | 1278–1290; switch.pl 84·89·99–100 |
| [swan/src/swanparll.ftn.md:1298–1407](../swan/src/swanparll.ftn.md) | TIMG 호출 안내의 선택 스위치가 빠졌다. | `!TIMG!` 주석에 대응하는 `-timg` 스위치를 명시했다. | 1385–1386; switch.pl 22·84 |
| [swan/src/swanparll.ftn.md:1408–1431](../swan/src/swanparll.ftn.md) | TIMG·NCOH의 스위치 조건을 생략했다. 배열 복사를 요약했다. | 시간 측정과 MPI 호출의 선택 조건을 명시했다. 배열 복사문과 오류 조건 종료 위치를 명시했다. | 1414–1426; switch.pl 84·89·99–100 |
| [swan/src/swanparll.ftn.md:1556–1579](../swan/src/swanparll.ftn.md) | 방향별 주소 증분과 초기값을 요약했다. ELSE 유무를 생략했다. | 방향별 대입과 첫 부분 초기값을 원문으로 인용했다. IDIR 분기에 별도 ELSE가 없음을 명시했다. | 1563–1578 |
| [swan/src/swanparll.ftn.md:1580–1631](../swan/src/swanparll.ftn.md) | 점 소유권 대입과 NPREM·NCURPT 초기값을 요약했다. 중첩 조건과 루프의 종료 행을 묶었다. | 소유권 대입과 점 수 초기값을 원문으로 인용했다. 각 조건과 루프의 종료 행을 명시했다. | 1591·1601·1612·1621–1628 |
| [swan/src/swanparll.ftn.md:1762–1784](../swan/src/swanparll.ftn.md) | 방향별 주소 증분과 초기값을 요약했다. ELSE 유무를 생략했다. | 방향별 대입과 첫 부분 초기값을 원문으로 인용했다. IDIR 분기에 별도 ELSE가 없음을 명시했다. | 1768–1783 |
| [swan/src/swanparll.ftn.md:1785–1819](../swan/src/swanparll.ftn.md) | 앞쪽과 뒤쪽 점 수의 초기값을 요약했다. | NBACK과 NFORW의 0 초기화를 원문으로 인용했다. | 1802·1812 |
| [swan/src/swanparll.ftn.md:1820–1867](../swan/src/swanparll.ftn.md) | 소유권의 다음 부분 인덱스와 NINPRT 대입을 요약했다. 바깥 조건 종료 행의 대응을 생략했다. | `LPARTS(1,JPART+1)`을 포함한 소유권 대입과 점 수 대입을 인용했다. 바깥 조건 및 루프의 종료 위치를 명시했다. | 1825·1844·1850–1864 |
| [swan/src/swanparll.ftn.md:2015–2063](../swan/src/swanparll.ftn.md) | 재귀 부분 수와 IWORK의 번호·크기 초기값을 요약했다. | NP와 IWORK의 초기 대입을 원문으로 인용했다. | 2021·2048·2050 |
| [swan/src/swanparll.ftn.md:2064–2096](../swan/src/swanparll.ftn.md) | J·ISSUCC 대입과 구간 시작 시 열린 바깥 블록의 종료 위치를 생략했다. | J·ISSUCC 대입을 원문으로 인용했다. 바깥 조건과 IP 루프의 종료 위치를 명시했다. | 2076–2077·2092·2120–2131 |
| [swan/src/swanparll.ftn.md:2097–2136](../swan/src/swanparll.ftn.md) | J 복귀와 GOTO의 조건을 구분하지 않았다. GOTO를 차이의 반복 감소로 요약했다. | J 복귀는 J>JEND 조건 안에 있음을 명시했다. GOTO는 그 조건 밖에서 잔여 차이를 재검사한다고 정정했다. 바깥 블록 종료 위치와 ISSUCC 재초기화 부재를 명시했다. | 2099–2131 |
| [swan/src/swanparll.ftn.md:2256–2305](../swan/src/swanparll.ftn.md) | 방향·점 수 초기값과 소유권·부분 번호 대입을 요약했다. | 초기 대입을 원문으로 인용했다. 소유권 대입의 `(IX,IY)` 인덱스를 명시했다. | 2265–2290 |
| [swan/src/swanparll.ftn.md:2464–2503](../swan/src/swanparll.ftn.md) | WFR·JAC 경로에서 경계 최댓값의 0 초기화를 요약했다. | 두 경로의 MXL·MYL 초기 대입을 원문으로 인용했다. | 2479·2482·2486–2487 |
| [swan/src/swanparll.ftn.md:2504–2554](../swan/src/swanparll.ftn.md) | 빈 경계와 작업 배열의 초기 대입을 요약했다. 두 조건의 종료 위치를 생략했다. | 경계·배열 초기값을 원문으로 인용했다. 경계 여부와 크기 계산이 각각 앞 조건 밖임을 종료 행으로 명시했다. | 2516–2553 |
| [swan/src/swanparll.ftn.md:2555–2626](../swan/src/swanparll.ftn.md) | 오프셋·이웃 번호·송수신 위치 대입의 인덱스를 요약했다. 오류 메시지 내용을 생략했다. | JOFFS·IPOWN·IWORK·ICSEND·ICRECV의 인덱스를 포함한 대입을 인용했다. 이웃 수 초과 오류 보고와 RETURN을 명시했다. | 2568–2569·2584–2586·2594–2598·2607–2614 |
| [swan/src/swanparll.ftn.md:2627–2648](../swan/src/swanparll.ftn.md) | 이웃 수와 겹침 미지수 수의 대입을 요약했다. | IBLKAD·NOVLU의 대입문을 원문으로 인용했다. | 2630·2636–2637 |
| [swan/src/swanparll.ftn.md:2756–2795](../swan/src/swanparll.ftn.md) | 전체 크기 저장과 경계·배열 초기 대입을 요약했다. | 전체 크기와 경계의 대입을 원문으로 인용했다. IBLKAD·IPOWN의 0 초기화를 인용했다. | 2763·2768–2774·2787 |
| [swan/src/swanparll.ftn.md:2796–2811](../swan/src/swanparll.ftn.md) | 지역 점 수를 세기 전 MCGRD의 초기값을 요약했다. | `MCGRD = 1` 초기 대입을 원문으로 인용했다. | 2801 |
| [swan/src/swanparll.ftn.md:2812–2951](../swan/src/swanparll.ftn.md) | 착수 시 기록은 JAC·TIMG 호출 안내만 적었다. 대조 중 처리 순서 보완이 반영되었다. | 반영된 처리 순서 설명을 원문과 확인했다. `-jac`와 `-timg`를 함께 선택해도 TIMG가 남음을 보완했다. `-jac` 미선택 결과를 명시했다. | 2915–2916; switch.pl 84–85 |

이상 없음으로 분류한 구간은 1–32·33–133·211–303·329–430·454–561·587–700·858–981·1048–1143·1432–1555·1632–1761·1868–2014·2137–2255·2306–2463·2649–2755행이다.

대상 구간의 조건·계산 대입·초기값·분기 의미·바깥 블록·전처리 표시를 원문과 대조했다.
frontmatter와 구간 경계는 보존했다.
원문의 SHA-256은 frontmatter의 값과 일치했다.
모델은 실행하지 않았다.

정정 2, 보완 28, 이상 없음 14
