# FUNWAVE io.F 전수 대조 기록 (2026-10-17)

상태: 완료.

대상 기록은 [FUNWAVE-GPU/src/io.F.md](../FUNWAVE-GPU/src/io.F.md)다.
원문은 `models/FUNWAVE/raw/source_code/FUNWAVE-GPU/src/io.F`다.

| 기록 | 대조한 구간 표 행 수 | 대조한 원문 행 수 | 원문 범위 |
|---|---:|---:|---|
| FUNWAVE-GPU/src/io.F.md | 107 | 4,214 | 1–4214 |

구간 표의 107행을 각각 `nl -ba <원문> | sed -n 'A,Bp'`로 열어 대조했다.
각 원문 출력은 200행 이하로 제한했다.
표 아래의 코드 사실 23항목도 해당 원문과 대조했다.
코드 사실 23항목에는 정정할 내용을 발견하지 않았다.
집계 단위는 구간 표의 행이다.
정정과 보완이 함께 있는 32행은 두 항목에 각각 집계했다.
이상 없음 구간은 1–51, 796–800, 3214–3243이다.

frontmatter와 구간 경계는 변경하지 않았다.
원문의 SHA-256은 frontmatter의 `4913b72a0cf88961dfabc72dc684c42d8dc605166ac146034f131d32cc73fc47`과 일치했다.
원문의 전처리 지시와 활성 조건은 각 구간의 인용에 모두 포함되었다.
행 번호가 붙은 백틱 인용을 원문 문자열과 대조하여 불일치가 없음을 확인했다.
이 파일에는 CUDA Fortran·OpenACC·OpenMP 지시가 없었다.
모델 실행은 하지 않았다.
원문·노트·git에는 쓰기 작업을 하지 않았다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| `FUNWAVE-GPU/src/io.F.md:52–90` (보완) | 전처리·실행 조건의 종료를 일부 행 번호로만 표시 | `# endif`와 `ENDIF`를 인용하여 각 블록의 종료를 명시 | 56·59·62·65·74·86–88 |
| `FUNWAVE-GPU/src/io.F.md:91–121` (보완) | 출력 조건의 종료 일부 누락 | 전처리 및 실행 조건의 종료행을 인용 | 95·101–102·108–109·115–116 |
| `FUNWAVE-GPU/src/io.F.md:122–193` (보완) | FDIR 복사식의 TRIM 및 전처리 종료 인용 누락 | FDIR 식과 각 `# endif`를 원문대로 인용 | 138·157·159·182·187·191 |
| `FUNWAVE-GPU/src/io.F.md:194–219` (보완) | 전처리 종료 인용 누락 | 두 전처리 블록의 # endif를 인용 | 209·218 |
| `FUNWAVE-GPU/src/io.F.md:220–256` (정정·보완) | MPI_FINALIZE도 rank 0 조건 안으로 읽히는 서술 | rank 0 출력·조건 밖 MPI_FINALIZE·전처리 밖 STOP의 범위를 분리하고 종료를 인용 | 222–249·255 |
| `FUNWAVE-GPU/src/io.F.md:257–298` (정정·보완) | MPI_FINALIZE의 rank 범위가 모호하고 중첩 종료 인용 누락 | CARTESIAN 안에서 rank 0 출력과 rank 0 조건 밖의 MPI_FINALIZE를 구분 | 257–297 |
| `FUNWAVE-GPU/src/io.F.md:299–352` (정정·보완) | MPI_FINALIZE의 rank 범위가 모호하고 바깥 조건식 누락 | CARTESIAN 미정의의 중첩 조건 및 오류 처리 범위 명시 | 257·299–351 |
| `FUNWAVE-GPU/src/io.F.md:353–400` (정정·보완) | MPI_FINALIZE 범위 모호 및 바깥 조건식 누락 | 바깥 전처리·StretchGrid 조건을 인용하고 rank 0 출력과 MPI_FINALIZE 범위를 구분 | 257·299·304·353–400 |
| `FUNWAVE-GPU/src/io.F.md:401–435` (정정·보완) | MPI_FINALIZE 범위 모호 및 구간 시작 조건식 누락 | 구간 시작의 네 조건과 닫힘을 인용하고 구면 로그의 범위 명시 | 257·299·304·353·389·401–433 |
| `FUNWAVE-GPU/src/io.F.md:436–466` (보완) | 전처리 종료 인용 누락 | 각 # endif 및 DAT 조건 종료를 인용 | 449·456·464–465 |
| `FUNWAVE-GPU/src/io.F.md:467–490` (정정·보완) | 활성 출력문을 주석·로그로 지칭 | 주석이 아닌 안내 출력문으로 정정하고 전처리 종료를 인용 | 474–475·480·487–488 |
| `FUNWAVE-GPU/src/io.F.md:491–547` (보완) | 전처리 종료 인용 누락 | 네 전처리 종료 및 SLO 종료를 인용 | 504·519·534·545–546 |
| `FUNWAVE-GPU/src/io.F.md:548–565` (보완) | 전처리 종료 인용 누락 | 전처리와 실행 조건의 종료를 구분 | 563–564 |
| `FUNWAVE-GPU/src/io.F.md:566–606` (정정·보완) | MPI_FINALIZE 범위 모호 및 전처리 종료 누락 | rank 0 출력과 MPI_FINALIZE·STOP 범위를 구분 | 574·578–590·604–605 |
| `FUNWAVE-GPU/src/io.F.md:607–647` (보완) | 전처리 종료 인용 누락 | 세 전처리 종료행을 인용 | 619·634·646 |
| `FUNWAVE-GPU/src/io.F.md:648–677` (정정·보완) | MPI_FINALIZE의 rank 범위 모호 | rank 0 출력과 MPI_FINALIZE·STOP의 범위를 분리하고 종료를 인용 | 654·664–676 |
| `FUNWAVE-GPU/src/io.F.md:678–712` (보완) | 바깥 INI_UVZ 조건식 및 전처리 종료 누락 | 바깥 조건과 내부 두 분기의 종료를 인용 | 661·690–711 |
| `FUNWAVE-GPU/src/io.F.md:713–765` (보완) | 바깥 조건식·전처리 종료·HotStartTime 단위 누락 | INI_UVZ와 각 전처리 종료 및 icount 감산의 범위를 명시 | 661·725·738–764 |
| `FUNWAVE-GPU/src/io.F.md:766–795` (보완) | 전처리 종료 인용 누락 | 세 전처리 종료행을 인용 | 772·785·794 |
| `FUNWAVE-GPU/src/io.F.md:801–816` (보완) | 구간 시작의 바깥 조건을 이름으로만 표시 | 바깥 실행·전처리 조건과 종료를 원문대로 인용 | 798·800–815 |
| `FUNWAVE-GPU/src/io.F.md:817–876` (정정·보완) | MPI_FINALIZE의 rank 범위 모호 | rank 0 출력과 MPI_FINALIZE·STOP 범위를 분리 | 820–848·863·874–875 |
| `FUNWAVE-GPU/src/io.F.md:877–936` (정정·보완) | MPI_FINALIZE의 rank 범위 모호 | rank 0 출력과 MPI_FINALIZE·STOP 범위를 분리하고 독립 IF 명시 | 877–936 |
| `FUNWAVE-GPU/src/io.F.md:937–979` (정정·보완) | MPI_FINALIZE 범위 모호 및 WK_TIME 조건식 누락 | 바깥 조건·전처리 종료를 인용하고 오류 처리 범위를 분리 | 877·949–979 |
| `FUNWAVE-GPU/src/io.F.md:980–1027` (보완) | WK_TIME 조건식 및 전처리 종료 누락 | 바깥 조건과 종료를 원문대로 인용 | 877·992·1007·1024–1026 |
| `FUNWAVE-GPU/src/io.F.md:1028–1058` (보완) | 전처리 종료와 바깥 INI_SOL의 계속 여부 누락 | 방향 조건 종료와 INI_SOL의 계속을 구분 | 1046·1056–1057 |
| `FUNWAVE-GPU/src/io.F.md:1059–1112` (정정·보완) | MPI_FINALIZE 범위 모호 및 바깥 조건식 누락 | INI_SOL 조건 및 rank 0 출력·MPI_FINALIZE·STOP의 범위를 명시 | 1028·1060–1111 |
| `FUNWAVE-GPU/src/io.F.md:1113–1158` (정정·보완) | MPI_FINALIZE 범위 모호 | rank 0 출력과 MPI_FINALIZE·STOP의 범위를 분리 | 1115–1157 |
| `FUNWAVE-GPU/src/io.F.md:1159–1200` (정정·보완) | MPI_FINALIZE 범위 모호 및 N_WAVE 조건식 누락 | 바깥 조건 및 오류 처리의 범위 명시 | 1113·1160–1200 |
| `FUNWAVE-GPU/src/io.F.md:1201–1277` (정정·보완) | MPI_FINALIZE 범위 모호 및 활성 ENDIF를 종료 주석으로 표현 | 바깥 조건과 MPI_FINALIZE 범위를 명시하고 활성 ENDIF로 정정 | 1113·1189·1195·1201–1276 |
| `FUNWAVE-GPU/src/io.F.md:1278–1353` (정정·보완) | MPI_FINALIZE 범위 모호 및 활성 ENDIF를 종료 주석으로 표현 | rank 0 조건 밖 MPI_FINALIZE를 명시하고 활성 ENDIF로 정정 | 1282–1352 |
| `FUNWAVE-GPU/src/io.F.md:1354–1399` (정정·보완) | MPI_FINALIZE 범위 모호 | rank 0 출력과 MPI_FINALIZE·STOP의 범위를 분리 | 1356–1398 |
| `FUNWAVE-GPU/src/io.F.md:1400–1457` (정정·보완) | MPI_FINALIZE 범위 모호 및 WK_REG 조건식 누락 | 바깥 조건과 MPI_FINALIZE·STOP 범위를 명시 | 1354·1401–1456 |
| `FUNWAVE-GPU/src/io.F.md:1458–1508` (보완) | WK_REG 조건식 및 전처리 종료 누락 | 바깥 조건과 종료를 인용 | 1354·1469·1483·1506–1507 |
| `FUNWAVE-GPU/src/io.F.md:1509–1555` (정정·보완) | MPI_FINALIZE 범위 모호 | rank 0 출력과 MPI_FINALIZE·STOP의 범위를 분리 | 1513–1554 |
| `FUNWAVE-GPU/src/io.F.md:1556–1598` (정정·보완) | MPI_FINALIZE 범위 모호 및 바깥 복합 조건 누락 | 복합 조건의 두 행을 인용하고 오류 처리 범위를 분리 | 1509–1510·1567·1581·1585–1597 |
| `FUNWAVE-GPU/src/io.F.md:1599–1652` (정정·보완) | MPI_FINALIZE 범위 모호 및 복합 조건식 누락 | 바깥 복합 조건과 오류 처리 범위를 명시 | 1509–1510·1600–1651 |
| `FUNWAVE-GPU/src/io.F.md:1653–1709` (보완) | 바깥 복합 조건식 및 전처리 종료 누락 | 바깥 복합 조건과 내부 세 분기의 종료를 인용 | 1509–1510·1660–1708 |
| `FUNWAVE-GPU/src/io.F.md:1710–1759` (보완) | 바깥 복합 조건식 및 전처리 종료 누락 | 바깥 조건과 종료를 인용 | 1509–1510·1721·1757–1758 |
| `FUNWAVE-GPU/src/io.F.md:1760–1810` (정정·보완) | MPI_FINALIZE 범위 모호 및 ETA_LIMITER 종료 누락 | ETA_LIMITER와 WK_DATA2D의 분리 및 오류 처리 범위를 명시 | 1761–1809 |
| `FUNWAVE-GPU/src/io.F.md:1811–1855` (정정·보완) | MPI_FINALIZE 범위 모호 및 WK_DATA2D 조건식 누락 | 바깥 조건과 오류 처리 범위를 명시 | 1766·1822·1836·1840–1852 |
| `FUNWAVE-GPU/src/io.F.md:1856–1896` (보완) | WK_DATA2D 조건식 및 전처리 종료 누락 | WK_DATA2D의 실제 종료와 조건 밖 EqualEnergy 범위를 인용 | 1766·1867·1884–1895 |
| `FUNWAVE-GPU/src/io.F.md:1897–1935` (정정·보완) | MPI_FINALIZE 범위 모호 및 ABS 전용 조건의 중첩 종료 누락 | 오류 처리와 재판독 조건의 종료 및 ABS 전용 조건의 중첩 명시 | 1898·1904–1934 |
| `FUNWAVE-GPU/src/io.F.md:1936–1961` (보완) | 바깥 조건식과 PeakPeriod 주석의 불필요성 설명 누락 | ABS 복합 조건 인용 및 PeakPeriod 주석·END=991 경로 보완 | 1898·1943·1956–1960 |
| `FUNWAVE-GPU/src/io.F.md:1962–1981` (보완) | 바깥 조건식과 전처리 종료 인용 누락 | ABS·DATA 조건을 인용하고 전처리·IF·루프 종료를 구분 | 1898·1936·1976–1980 |
| `FUNWAVE-GPU/src/io.F.md:1982–2000` (보완) | 바깥 조건식과 Phase_Ser 대입식 및 주석 일부 누락 | ABS·DATA 조건 및 첫 방향 선택 식을 인용하고 주석 보완 | 1898·1936·1982–1988 |
| `FUNWAVE-GPU/src/io.F.md:2001–2054` (정정·보완) | MPI_FINALIZE 범위 모호 및 구간 시작 조건식 누락 | 세 바깥 조건을 인용하고 오류 처리 범위를 분리 | 1898·1936·2000–2053 |
| `FUNWAVE-GPU/src/io.F.md:2055–2088` (정정·보완) | MPI_FINALIZE 범위 모호 및 바깥 조건식 누락 | ABS와 DATA 거짓 분기의 조건을 인용하고 오류 처리 범위를 분리 | 1898·1936·2008·2056–2087 |
| `FUNWAVE-GPU/src/io.F.md:2089–2136` (보완) | 바깥 조건식과 전처리 종료 누락 | ABS·DATA 조건과 내부 세 분기 종료를 인용 | 1898·1936·2008·2100–2134 |
| `FUNWAVE-GPU/src/io.F.md:2137–2162` (보완) | 바깥 조건식과 전처리 종료 누락 | 두 바깥 조건과 각각의 종료를 인용 | 1898·1936·2008·2157–2161 |
| `FUNWAVE-GPU/src/io.F.md:2163–2192` (보완) | 중첩 전처리 종료 인용 누락 | CARTESIAN 내부와 외부의 전처리 종료를 구분 | 2169·2182–2183·2191 |
| `FUNWAVE-GPU/src/io.F.md:2193–2220` (보완) | 전처리 종료 인용 누락 | 전처리와 DIRECT_SPONGE 종료를 구분 | 2218–2219 |
| `FUNWAVE-GPU/src/io.F.md:2221–2253` (보완) | 전처리 종료 인용 누락 | 각 전처리와 DIFFUSION_SPONGE 종료를 인용 | 2231·2244·2251–2252 |
| `FUNWAVE-GPU/src/io.F.md:2254–2286` (보완) | 전처리 종료 인용 누락 | 각 전처리와 FRICTION_SPONGE 종료를 인용 | 2264·2277·2284–2285 |
| `FUNWAVE-GPU/src/io.F.md:2287–2329` (보완) | 전처리 종료 인용 누락 | 각 전처리 종료를 인용 | 2299·2313·2327 |
| `FUNWAVE-GPU/src/io.F.md:2330–2371` (보완) | 바깥 감쇠층 조건식 및 전처리 종료 누락 | 바깥 조건과 전처리 종료를 인용 | 2287·2341·2355·2369 |
| `FUNWAVE-GPU/src/io.F.md:2372–2388` (보완) | 바깥 감쇠층 조건식 및 종료 인용 누락 | 바깥 조건과 두 종료를 구분하여 인용 | 2287·2386–2387 |
| `FUNWAVE-GPU/src/io.F.md:2389–2409` (정정·보완) | 연안류 자체를 균형화한다고 주석을 요약 | 운동량 균형과 연안류 회피라는 주석의 의미로 정정하고 종료를 인용 | 2389–2390·2399·2406–2407 |
| `FUNWAVE-GPU/src/io.F.md:2410–2453` (보완) | 전처리 종료 인용 누락 | 다섯 전처리와 두 실행 분기의 종료를 인용 | 2416·2426·2433–2434·2444·2451–2452 |
| `FUNWAVE-GPU/src/io.F.md:2454–2488` (보완) | 전처리 및 계수 판독 분기 종료 누락 | 세 전처리와 실행 분기 종료를 인용 | 2467·2477–2478·2487 |
| `FUNWAVE-GPU/src/io.F.md:2489–2517` (보완) | 전처리 종료 인용 누락 | 두 전처리 종료를 인용 | 2501·2515 |
| `FUNWAVE-GPU/src/io.F.md:2518–2563` (보완) | 중첩 전처리 종료 인용 누락 | CARTESIAN·ZALPHA 각각의 내부 및 외부 종료를 구분 | 2530·2544·2547·2560·2562 |
| `FUNWAVE-GPU/src/io.F.md:2564–2600` (보완) | Gamma3의 CARTESIAN 밖 범위와 바깥 else의 관계 및 종료 인용 누락 | 두 플래그 미정의 분기 안이라는 제한과 중첩 종료를 명시 | 2584–2600 |
| `FUNWAVE-GPU/src/io.F.md:2601–2648` (보완) | 첫 VISCOSITY_BREAKING 종료 및 SWE_ETA_DEP 판독 범위 누락 | 2622행 종료 뒤 조건 없이 SWE_ETA_DEP를 읽는 사실과 각 종료를 명시 | 2613·2621–2624·2635·2646–2647 |
| `FUNWAVE-GPU/src/io.F.md:2649–2687` (정정·보완) | MPI_FINALIZE 범위 모호 및 ELSE 소속의 종료 누락 | rank 0 밖 MPI_FINALIZE와 ierr ELSE·IN_Cd의 닫힘 명시 | 2660·2665–2685 |
| `FUNWAVE-GPU/src/io.F.md:2688–2715` (보완) | 전처리 종료 인용 누락 | 세 전처리 종료를 인용 | 2699·2706·2714 |
| `FUNWAVE-GPU/src/io.F.md:2716–2752` (보완) | 전처리 종료 인용 누락 | 네 전처리 종료를 인용 | 2728·2735·2743·2751 |
| `FUNWAVE-GPU/src/io.F.md:2753–2792` (보완) | 전처리 종료 인용 누락 | 네 전처리 종료를 인용 | 2763·2771·2784·2791 |
| `FUNWAVE-GPU/src/io.F.md:2793–2828` (보완) | DT/2 안내식 원문과 전처리 종료 및 ELSE 부재 누락 | 안내 문자열·전처리 종료를 인용하고 고정 시간 간격 조건에 ELSE가 없음을 명시 | 2795–2806·2820·2827 |
| `FUNWAVE-GPU/src/io.F.md:2829–2881` (보완) | MIN 안내식 원문 및 전처리 종료 인용 누락 | MIN 안내 문자열과 전처리 종료를 인용 | 2841·2855·2863–2866·2873·2879 |
| `FUNWAVE-GPU/src/io.F.md:2882–2929` (보완) | 전처리 종료 및 내부 VISCOSITY_BREAKING 종료 누락 | SHOW_BREAKING이 계속되는 동안 내부 조건이 닫히는 위치를 명시 | 2888·2902·2919·2927–2928 |
| `FUNWAVE-GPU/src/io.F.md:2930–2972` (보완) | 바깥 조건식 및 WAVEMAKER_Cbrk의 실행 범위 누락 | SHOW_BREAKING 식과 VISCOSITY_BREAKING 종료 뒤 판독 범위를 명시 | 2907·2941·2949–2952·2963·2970–2971 |
| `FUNWAVE-GPU/src/io.F.md:2973–3011` (정정·보완) | MPI_FINALIZE도 rank 0 조건 안으로 읽히는 서술 | rank 0 밖 MPI_FINALIZE 및 병렬 참 분기의 STOP 부재를 명시 | 2988–3002·3009–3010 |
| `FUNWAVE-GPU/src/io.F.md:3012–3032` (보완) | 전처리 종료 인용 누락 | 두 전처리 및 WAVEMAKER_VIS 종료를 구분 | 3022–3023·3031 |
| `FUNWAVE-GPU/src/io.F.md:3033–3084` (보완) | 전처리 종료 인용 누락 | 네 전처리 종료를 인용 | 3044·3058·3072·3083 |
| `FUNWAVE-GPU/src/io.F.md:3085–3098` (보완) | 전처리 종료 인용 누락 | 전처리와 ierr 조건의 종료를 구분 | 3096–3097 |
| `FUNWAVE-GPU/src/io.F.md:3099–3133` (정정·보완) | MPI_FINALIZE 범위 모호 및 중첩 전처리 종료 누락 | COUPLING 조건 안에서 rank 0 출력·MPI_FINALIZE·STOP 범위를 구분 | 3099–3130 |
| `FUNWAVE-GPU/src/io.F.md:3134–3168` (보완) | 주석의 지연 시점과 전처리 종료 인용 누락 | 계산 완료 뒤까지라는 주석의 시점 및 각 전처리 종료를 보완 | 3140·3152·3155–3157·3164 |
| `FUNWAVE-GPU/src/io.F.md:3169–3192` (보완) | 중첩 전처리와 rank 0 종료 인용 누락 | 병렬·직렬 INTEL 분기의 종료와 rank 0 종료를 구분 | 3177–3178·3184–3185 |
| `FUNWAVE-GPU/src/io.F.md:3193–3213` (보완) | 전처리 종료 인용 누락 | 두 전처리 종료를 인용 | 3205·3212 |
| `FUNWAVE-GPU/src/io.F.md:3244–3260` (보완) | 안내식 및 종료 인용과 ierr의 직전 판독 연결 누락 | 100xmax_depth 안내 원문 및 OUT_TMP 판독 뒤 ierr 검사임을 명시 | 3243·3250–3257 |
| `FUNWAVE-GPU/src/io.F.md:3261–3310` (보완) | 분리된 전처리 종료 인용 누락 | rank 0 IF를 삽입하는 두 전처리와 마지막 로그 전처리의 종료를 인용 | 3263·3295–3296·3307 |
| `FUNWAVE-GPU/src/io.F.md:3311–3358` (정정·보완) | MPI_FINALIZE·STOP의 단일 문장 IF 범위 모호 및 초기식 누락 | IF 대상은 WRITE뿐임을 명시하고 초기값·FDIR·최초 호출 식과 종료를 인용 | 3329–3338·3347–3357 |
| `FUNWAVE-GPU/src/io.F.md:3359–3396` (보완) | 바깥 조건식·주석 속 인덱스 식·nsta 대입식 누락 | 중첩 조건과 주석 식 및 nsta 대입을 인용하고 종료를 구분 | 3311·3337·3364–3395 |
| `FUNWAVE-GPU/src/io.F.md:3397–3418` (보완) | 바깥 CARTESIAN 조건식 및 최초 호출 조건 밖이라는 근거 누락 | 바깥 조건식과 최초 호출 종료행을 인용 | 3311·3337·3395·3413–3418 |
| `FUNWAVE-GPU/src/io.F.md:3419–3454` (보완) | 바깥 전처리 조건식과 문자열·최초 호출 대입식 누락 | CARTESIAN 조건과 초기값·FDIR·FirstCallStation 식을 인용 | 3311·3439–3448 |
| `FUNWAVE-GPU/src/io.F.md:3455–3492` (보완) | 바깥 조건식·주석 속 인덱스 식·nsta 대입식 누락 | CARTESIAN 미정의와 최초 호출 조건 및 주석 식·nsta 식을 인용 | 3311·3419·3447·3460–3491 |
| `FUNWAVE-GPU/src/io.F.md:3493–3523` (보완) | 바깥 조건식 및 mask별 출력값 대입식 누락 | CARTESIAN 미정의 조건과 여섯 대입식·mask 종료를 인용 | 3311·3419·3447·3491·3498–3506 |
| `FUNWAVE-GPU/src/io.F.md:3524–3554` (보완) | 바깥 조건식·초기값 및 주석 속 envelope 식 누락 | CARTESIAN 조건과 초기화 대입식·주석의 0.d0 식을 인용 | 3311·3419·3539–3554 |
| `FUNWAVE-GPU/src/io.F.md:3555–3595` (보완) | 바깥 조건식·주석 속 좌표 계산식·nsta 대입식 누락 | 바깥 조건과 주석의 네 행·nsta 대입식 및 각 종료를 인용 | 3311·3419·3548·3560–3594 |
| `FUNWAVE-GPU/src/io.F.md:3596–3636` (보완) | 바깥 조건식·mask별 출력값 대입식 및 전처리 종료 누락 | 바깥 조건과 여섯 대입식 및 mask·시간·CARTESIAN 종료를 인용 | 3311·3419·3548·3594·3603–3635 |
| `FUNWAVE-GPU/src/io.F.md:3637–3697` (보완) | 문자열 초기값·FDIR 식·주석 속 네 자리 계산식·전처리 종료 누락 | 각 초기식과 옛 번호 계산식 및 전처리 종료를 인용 | 3651–3685 |
| `FUNWAVE-GPU/src/io.F.md:3698–3739` (보완) | 출력 경로 대입식의 원문 인용 누락 | FDIR·고정 파일명·번호의 결합식을 모두 인용 | 3700·3702·3711·3716·3721·3726·3731·3736 |
| `FUNWAVE-GPU/src/io.F.md:3740–3780` (보완) | Int2Flo 대입식 및 출력 파일명 식 인용 누락 | 배열 대입식과 모든 파일명 식을 인용하고 중첩 AGE 조건 종료 명시 | 3741–3780 |
| `FUNWAVE-GPU/src/io.F.md:3781–3815` (보완) | 활성·주석 파일명 대입식 및 METEO 종료 인용 누락 | 각 파일명 식과 주석 여부 및 두 종류의 종료를 명시 | 3784·3787–3788·3795–3814 |
| `FUNWAVE-GPU/src/io.F.md:3816–3863` (보완) | 출력 파일명 식 및 중첩 전처리 종료 인용 누락 | 파일명 식과 VESSEL_PANEL_SOURCE·OUT_VESSEL·VESSEL·SEDIMENT 종료를 구분 | 3819–3856 |
| `FUNWAVE-GPU/src/io.F.md:3864–3905` (보완) | 초기값·FDIR 대입식 및 전처리 종료 인용 누락 | 문자열 초기값과 FDIR 식 및 로그 전처리 종료를 인용 | 3875–3879·3890 |
| `FUNWAVE-GPU/src/io.F.md:3906–3930` (보완) | 평균 출력 파일명 대입식 원문 인용 누락 | FDIR·접두어·번호의 여섯 결합식을 인용 | 3907·3911·3915·3919·3921·3923 |
| `FUNWAVE-GPU/src/io.F.md:3931–3984` (보완) | 배열 크기·입력 범위의 원문과 상하 가상 셀 처리의 I 범위 누락 | PHIGLOB 선언·READ 식·바깥 I 루프 및 rank 0 종료를 인용 | 3945·3962–3967·3981–3983 |
| `FUNWAVE-GPU/src/io.F.md:3985–4000` (보완) | 구간 시작의 바깥 조건식과 rank 0 조건의 종료 근거 누락 | 병렬 전처리 및 이미 닫힌 rank 0 IF의 원문을 인용 | 3931·3960·3983 |
| `FUNWAVE-GPU/src/io.F.md:4001–4042` (보완) | 바깥 조건식·xx 부분 배열 식·최종 ELSE 부재 누락 | 정확한 배열 범위와 ELSE 없는 IF/elseif 사슬 및 종료를 명시 | 3931·4018·4023–4041 |
| `FUNWAVE-GPU/src/io.F.md:4043–4074` (보완) | TMP_NAME 초기값 인용 누락 | 문자열 초기값을 인용하고 바깥 전처리의 계속 여부 명시 | 4061·4071–4074 |
| `FUNWAVE-GPU/src/io.F.md:4075–4119` (보완) | 바깥 전처리·FirstCall 대입·FORMAT_LEN 인덱스·DEBUG 출력 및 종료 인용 누락 | PARALLEL·MGPU 미정의 조건 아래 DEBUG 분기와 정확한 형식 문자열 쓰기를 인용 | 4043·4095–4118 |
| `FUNWAVE-GPU/src/io.F.md:4120–4172` (정정·보완) | 선박별 여섯 값 출력으로도 읽히는 순서 서술 및 대입식 누락 | 물리량별 전체 선박 그룹의 출력 순서를 인용하고 초기값·FDIR·조건 종료 보완 | 4135·4141–4170 |
| `FUNWAVE-GPU/src/io.F.md:4173–4214` (보완) | FDIR·FirstCall 대입 및 중첩 전처리 종료 인용 누락 | SEDIMENT 안의 VESSEL·PARALLEL 종료와 대입식을 원문대로 인용 | 4187–4211 |

정정 32, 보완 104, 이상 없음 3
