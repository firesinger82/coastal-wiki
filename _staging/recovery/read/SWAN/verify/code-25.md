# SWAN swanpre2.ftn 전수 대조 — code-25

검증일은 2026-10-13이다.
대상 기록은 `_staging/recovery/read/SWAN/swan/src/swanpre2.ftn.md`이다.
원문은 기록 frontmatter의 `models/SWAN/raw/source_code/swan/src/swanpre2.ftn`이다.

| 기록 | 대조한 구간 행 수 | 대조한 원문 행 수 | 대조 범위 |
|---|---:|---:|---|
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md) | 58 | 3368 | 기록 15–72행의 구간 1–137부터 3323–3368까지 |

행 수는 원문 1–3330행과 겹치는 기록 구간에서 집계했다.
경계 구간 3323–3368행은 전체를 대조했다.
각 구간은 `nl -ba <원문> | sed -n 'A,Bp'`로 200행 이하씩 열었다.
원문의 조건·계산식·상수·주석 수식·분기 의미·오류 처리·블록 소속을 대조했다.
`!NCF`와 `!METIS`의 활성화는 `swan/switch.pl` 82–105행 규칙으로 확인했다.
마지막 구간의 바깥 IF 종료를 확인하기 위해 원문 3612행과 3873행도 보조 참조했다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):138–175 | FOUND 초기화와 800의 참 설정을 서술로만 기록했다. | 보완. FOUND의 거짓 초기화와 참 설정을 원문 대입식으로 인용했다. | 144, 171 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):319–367 | OPSTMP%PSTYPE·LOPS의 상수 대입식 인용이 빠졌다. | 보완. OPSTMP%PSTYPE·LOPS의 상수 대입식을 원문으로 인용했다. | 350, 359 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):401–456 | OPTG=3과 OPTG=1 분기의 최종 ELSE 유무를 적지 않았다. ALPC 저장은 서술로만 기록했다. OPSTMP%PSTYPE·OPSTMP%PSTYPE·LOPS의 상수 대입식 인용도 빠졌다. | 보완. 최종 ELSE가 없는 조건열의 종료 행을 적었다. 각도 저장 대입식을 인용했다. OPSTMP%PSTYPE·OPSTMP%PSTYPE·LOPS의 상수 대입식도 인용했다. | 403, 419, 433, 441; 409, 420, 448 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):457–531 | CURVE의 MIP 초기값과 첫 점 저장 후 값이 인용되지 않았다. OPSTMP%PSTYPE·LOPS의 상수 대입식 인용도 빠졌다. | 보완. MIP의 0 초기화와 1 설정을 원문으로 인용했다. OPSTMP%PSTYPE·LOPS의 상수 대입식도 인용했다. | 468, 478; 467, 524 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):532–603 | POINTS 분기가 다음 구간으로 이어진다고 적었다. 점 수와 파일 판독 상태의 초기값 인용이 빠졌다. OPSTMP%PSTYPE·LOPS의 상수 대입식 인용도 빠졌다. | 정정·보완. POINTS 분기는 602행에서 닫힌다고 바로잡았다. MIP·IOSTAT·NDS·PP·FRST·IERR 초기값을 인용했다. OPSTMP%PSTYPE·LOPS의 상수 대입식도 인용했다. | 542, 546–556, 561, 601–602; 541, 596 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):604–659 | 첫 광선의 MIP=1을 서술로만 적었다. OPSTMP%PSTYPE의 상수 대입식 인용도 빠졌다. | 보완. MIP 초기값 대입식을 인용했다. OPSTMP%PSTYPE의 상수 대입식도 인용했다. | 621; 620 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):660–693 | LOPS의 상수 대입식 인용이 빠졌다. | 보완. LOPS의 상수 대입식을 원문으로 인용했다. | 681 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):694–745 | 광선 집합 형식 오류 이후의 이동을 적지 않았다. BOTDEP·MIP·FRST 설정의 인용이 빠졌다. OPSTMP%PSTYPE의 상수 대입식 인용도 빠졌다. | 보완. MSGERR 다음 GOTO 800을 적었다. BOTDEP 설정과 빈 목록 초기값을 인용했다. OPSTMP%PSTYPE의 상수 대입식도 인용했다. | 709, 712, 726–736; 732 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):746–793 | 목표 수심 미발견 진단에서 좌표 오프셋 계산을 빠뜨렸다. LOPS의 상수 대입식 인용도 빠졌다. | 보완. 진단에 출력되는 두 끝점의 오프셋 계산을 인용했다. LOPS의 상수 대입식도 인용했다. | 747–748; 778 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):794–845 | UNSTRUC 상태값과 파일·할당 초기값 및 NVTX 판독의 오류 이동이 인용되지 않았다. OPSTMP%PSTYPE의 상수 대입식 인용도 빠졌다. | 보완. PP·IOSTAT·NDS·ISTAT 설정을 인용했다. NVTX READ의 END=950과 ERR=910을 인용했다. OPSTMP%PSTYPE의 상수 대입식도 인용했다. | 809, 812–813, 821–822; 806 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):846–900 | 846행을 EASY 참 분기 안으로 적었다. 초기값과 헤더 READ의 오류 이동이 인용되지 않았다. | 정정·보완. 846행이 EASY 조건열의 ELSE임을 명시했다. IOSTAT·NDS·ISTAT·PP와 헤더 READ를 인용했다. | 846, 848–858, 897–900 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):901–959 | 최종 ELSE의 부재와 점 수 초기화가 빠졌다. 각 변의 기본 분할 수·길이 및 시작점 갱신이 빠졌다. | 보완. 조건열의 종료와 ELSE 부재를 적었다. MIP·DYN·변별 분할 수·길이·시작점 설정을 인용했다. | 910–942 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):960–1012 | 960행을 구조 격자 참 분기 안으로 적었다. NGR 분기가 이어진다고 적었다. 오류 경로의 메시지 차이와 초기값 인용이 빠졌다. LOPS의 상수 대입식 인용도 빠졌다. | 정정·보완. 960행 ELSE와 981행 ENDIF의 범위를 바로잡았다. NGR 종료는 1002행이다. 두 오류 경로와 I·FOUND 대입식을 보완했다. LOPS의 상수 대입식도 인용했다. | 960, 966, 981, 994–1006; 987 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):1013–1158 | 변경 이력에 있는 MXOUTAR 증가식을 생략했다. | 보완. 주석의 6*MIP를 인용했다. 변경 이력의 설명임을 명시했다. | 1085–1086 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):1159–1215 | RTYPE·RTYPE의 상수 대입식 인용이 빠졌다. | 보완. RTYPE·RTYPE의 상수 대입식을 원문으로 인용했다. | 1203, 1209 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):1216–1259 | 노드 번호 파일명의 부분 문자열 범위와 NREF·NVAR·FRST 초기값 인용이 빠졌다. RTYPE의 상수 대입식 인용도 빠졌다. | 보완. WRITE의 ILPOS+1:ILPOS+4 범위와 FORMAT을 인용했다. 초기값을 인용했다. RTYPE의 상수 대입식도 인용했다. | 1225, 1230–1231, 1249, 1256–1257; 1220 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):1304–1342 | ALOCMP의 상수 대입식 인용이 빠졌다. | 보완. ALOCMP의 상수 대입식을 원문으로 인용했다. | 1316, 1321, 1326, 1331, 1336, 1341 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):1343–1397 | ALOCMP의 상수 대입식 인용이 빠졌다. | 보완. ALOCMP의 상수 대입식을 원문으로 인용했다. | 1346, 1351, 1356, 1361, 1366, 1371, 1376, 1381, 1386, 1391, 1396 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):1398–1426 | LADDS 설정을 소스 항 추가 활성화라는 용도로 단정했다. ALOCMP의 상수 대입식 인용도 빠졌다. | 정정·보완. 원문에서 직접 확인되는 LADDS의 참 설정으로 고쳤다. ALOCMP의 상수 대입식도 인용했다. | 1423–1426; 1401, 1406, 1411, 1416, 1421 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):1427–1481 | 171 노드의 필드를 IVTYPE로 표현했다. GOTO와 조건 종료 순서를 뭉뚱그렸다. 최종 ELSE의 부재가 빠졌다. | 정정·보완. 171은 TMP%I에 저장한다고 고쳤다. 두 IF의 종료와 GOTO 순서를 적었다. 최종 ELSE의 부재를 적었다. | 1443, 1467–1469 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):1482–1516 | NSTATM·LC·NREF 설정을 원문 대입식으로 인용하지 않았다. | 보완. 시간 모드와 확장자 상태 및 파일 단위 초기값을 인용했다. | 1485, 1490, 1493, 1502 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):1517–1563 | 하위 디렉터리 경로식을 생략했다. 세 바깥 IF의 종료를 1543–1545행으로 묶었다. LORQ의 상수 대입식 인용도 빠졌다. | 보완. 경로 구성식을 인용했다. PARLL·VTK·시간 정보 조건의 종료 행을 구분했다. LORQ의 상수 대입식도 인용했다. | 1534, 1543–1545; 1556 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):1564–1633 | NREF·NVAR·FRST 초기값과 노드 번호 저장 범위를 인용하지 않았다. RTYPE·RTYPE·RTYPE·RTYPE·RTYPE의 상수 대입식 인용도 빠졌다. | 보완. 초기값과 파일명의 ILPOS+1:ILPOS+4 저장 범위를 인용했다. RTYPE·RTYPE·RTYPE·RTYPE·RTYPE의 상수 대입식도 인용했다. | 1613, 1618, 1628, 1631; 1590, 1592, 1594, 1596, 1600 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):1677–1729 | J 변수와 ALOCMP를 설정한다고만 적었다. | 보완. J 변수에 저장하는 값은 증가한 MCMVAR라고 적었다. ALOCMP의 참 설정을 인용했다. | 1687–1728 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):1730–1797 | J 변수와 ALOCMP를 설정한다고만 적었다. | 보완. J 변수에 저장하는 값은 증가한 MCMVAR라고 적었다. ALOCMP의 참 설정을 인용했다. | 1732–1788 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):1798–1855 | FAC(0) 할당을 netCDF 분기 설명에만 넣었다. 변수 조건열의 최종 ELSE 부재와 NSTATM 대입식이 빠졌다. LORQ의 상수 대입식 인용도 빠졌다. | 정정·보완. 1830행은 일반 행이므로 netCDF 비활성 시 무조건 실행한다고 명시했다. 조건열의 종료·ELSE 부재·루프 범위와 NSTATM 설정을 인용했다. LORQ의 상수 대입식도 인용했다. | 1801, 1814–1816, 1826–1836; 1849 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):1856–1912 | RTYPE 문자 선택 조건열의 최종 ELSE 부재가 빠졌다. 문자 대입식 인용이 빠졌다. RTYPE·RTYPE의 상수 대입식 인용도 빠졌다. | 보완. 최종 ELSE 부재와 1905행 종료를 적었다. 세 번째 문자의 대입식을 인용했다. RTYPE·RTYPE의 상수 대입식도 인용했다. | 1894, 1901–1905; 1886, 1890 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):1913–1949 | 옵션 이름만으로 에너지 척도·압축·격자 메타데이터·보조 변수 제외라는 용도를 단정했다. INKEYW와 초기화 순서가 부정확했다. 파일 설정 인용이 빠졌다. | 정정·보완. 원문 주석의 월별 파일 설명과 정수값 추가 동작만 적었다. INKEYW 뒤 초기화하는 순서를 바로잡았다. NREF와 파일명 저장 범위를 인용했다. | 1914, 1919, 1926–1949 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):1950–1977 | NVAR·NSTATM 설정을 서술로만 적었다. LORQ의 상수 대입식 인용도 빠졌다. | 보완. 두 대입식을 원문으로 인용했다. LORQ의 상수 대입식도 인용했다. | 1951, 1960; 1970 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):1978–2037 | STYPE 오류의 메시지와 GOTO를 생략했다. NREF·NVAR 초기값 및 파일명 인덱스 범위를 인용하지 않았다. RTYPE의 상수 대입식 인용도 빠졌다. | 보완. 형식 오류 메시지 뒤 800으로 이동하는 동작을 적었다. 초기값과 부분 문자열 저장식을 인용했다. RTYPE의 상수 대입식도 인용했다. | 2004–2006, 2018, 2023, 2029; 2015 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):2038–2069 | ONED와 NEST의 종료 위치를 구분하지 않았다. NSTATM·FOUND 대입식을 인용하지 않았다. LORQ의 상수 대입식 인용도 빠졌다. | 보완. ONED 종료 2059행과 NEST 종료 2060행을 구분했다. NSTATM·FOUND 설정을 인용했다. LORQ의 상수 대입식도 인용했다. | 2042, 2059–2060, 2064; 2053 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):2184–2237 | SIRAY 초기값·성공값과 JDMINMAX 저장식 및 루프 문장이 인용되지 않았다. | 보완. 반환값 설정과 탐색 루프를 인용했다. JDMINMAX를 저장하는 조건과 인덱스를 명시했다. | 2184, 2190, 2202–2205, 2215 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):2325–2356 | 다음 노드 탐색을 원문에 없는 ELSE로 적었다. IERR·ALPQ 및 오류 반환값의 인용이 빠졌다. | 정정·보완. 다음 노드 대입은 2334행 END IF 밖에 있다고 고쳤다. 초기값과 오류 반환값을 인용했다. | 2325, 2331–2335, 2344, 2350–2352 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):2450–2478 | IVTYPE 초기값과 역순 반복의 증분 및 일치 번호 저장식을 인용하지 않았다. | 보완. 초기값과 -1 증분의 DO 및 IVTYPE 저장식을 인용했다. | 2450, 2454, 2458 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):2479–2589 | 변경 이력의 방향 퍼짐 검사에서 수치 경계와 예외값 제외가 빠졌다. | 보완. 음의 코사인 지수와 DSPR의 360 초과·0 미만 제한을 주석의 설명으로 적었다. 예외값 제외를 보존했다. | 2549–2550 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):2590–2701 | 구조 주석을 처리 구조가 있다고만 요약하여 UNIF·VAR 안의 PAR·FILE 분기 의미를 생략했다. | 보완. 각 주석 경로의 입력·호출·저장 동작과 VAR 경로의 반복 종료 조건을 적었다. | 2668–2688 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):2702–2743 | 진단 개수 초기화와 좌표 오프셋 계산을 빠뜨렸다. 반복 범위를 인용하지 않았다. | 보완. KOUNTR 초기값과 두 반복 범위를 인용했다. 출력 좌표의 오프셋 식을 인용했다. | 2722–2724, 2736–2737 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):2744–2778 | K·BNDDONE 설정의 인용이 빠졌다. bvertg 열별 인덱스 저장식 일부와 바깥 IF의 종료를 생략했다. | 보완. K 초기값과 열별 저장식 및 BNDDONE 대입식을 인용했다. 두 바깥 IF의 종료 행을 명시했다. | 2749, 2753, 2760, 2764–2765, 2775–2777 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):2779–2838 | PM·DEGR 설정을 인용하지 않았다. 최종 ELSE의 부재와 SIGFR 변환 후 단위가 빠졌다. | 보완. FSHAPE=1과 DSHAPE=1을 인용했다. 2819행 종료와 최종 ELSE 부재를 적었다. 변환 단위 rad/s를 주석에 따라 적었다. | 2809, 2813–2814, 2819, 2831 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):2839–2893 | 경계 개수와 ALOBND 초기값을 서술로만 적었다. LBFILS의 상수 대입식 인용도 빠졌다. | 보완. 다섯 초기값 대입식을 인용했다. LBFILS의 상수 대입식도 인용했다. | 2865–2869; 2888 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):2894–2942 | 격자·바닥 자료 선행 검사에서 오류 메시지와 이동을 생략했다. 경계 초기값을 인용하지 않았다. LBFILS의 상수 대입식 인용도 빠졌다. | 보완. 각 오류 메시지와 GOTO 900을 명시했다. 경계 자료 초기값을 인용했다. LBFILS의 상수 대입식도 인용했다. | 2904–2918; 2937 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):2943–3000 | 선행 자료 검사에서 오류 메시지와 이동을 생략했다. 경계 초기값·DONALL 대입식과 ELSE의 미대입을 적지 않았다. LBFILS의 상수 대입식 인용도 빠졌다. | 보완. 오류 메시지와 GOTO 900을 명시했다. 초기값과 DONALL 설정을 인용했다. WRNKEY 경로에서는 DONALL을 대입하지 않는다고 적었다. LBFILS의 상수 대입식도 인용했다. | 2952–2966, 2980–2986; 2996 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):3001–3062 | 최종 ELSE의 소속과 선행 검사 메시지를 명시하지 않았다. 경계 자료·목록 초기값의 인용이 빠졌다. | 보완. 3002행 ELSE의 소속을 적었다. 각 오류 메시지와 경계 자료·목록 초기값을 보완했다. | 3002, 3032–3060 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):3063–3094 | 초기값과 좌표 모드 대입식 및 오류 진단의 좌표 오프셋을 인용하지 않았다. | 보완. IERR·LOCGRI·IX1·IY1·LFRST1 설정을 인용했다. 진단 좌표의 오프셋을 인용했다. | 3064, 3067–3075, 3090–3091 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):3095–3124 | 병렬 집계의 실제 인수와 비병렬 인덱스 저장식을 인용하지 않았다. 오류 메시지의 좌표 오프셋이 빠졌다. | 보완. SWREDUCE의 IXG2·1·SWINT·SWMAX 인수를 인용했다. 비병렬 인덱스 대입식과 좌표 오프셋을 명시했다. | 3108, 3110, 3114, 3120 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):3125–3157 | 3125행을 LOCGRI 참 분기 안으로 적었다. 종료 위치를 격자·LOCGRI로 묶었다. | 정정·보완. 3125행이 LOCGRI 조건의 ELSE임을 바로잡았다. 각 ENDIF 소속과 비병렬 인덱스 대입식을 명시했다. | 3125, 3145, 3152–3153 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):3158–3199 | 첫 점 처리의 MM·LFRST1 설정과 반복문을 인용하지 않았다. 1차원 Y 인덱스와 오류 좌표식 인용이 빠졌다. | 보완. 첫 점 처리값과 DO 범위를 인용했다. Y 인덱스 유지와 오류 좌표의 -1 계산을 인용했다. | 3165–3170, 3178, 3194–3195 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):3200–3277 | IP 짝홀 분기를 JBG·IXG 조건열의 ELSE처럼 적었다. DET·LFRST1·DXLOC·DYLOC·IXG 설정과 집계 호출 인용이 빠졌다. | 정정·보완. EXIT 조건열은 최종 ELSE 없이 3260행에서 닫힌다고 고쳤다. 짝홀 IF는 별도 조건이라고 적었다. 초기값·간격식·판정값 및 집계 호출을 인용했다. | 3209–3266 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):3278–3322 | 증분과 경계 점 수를 더하는 인덱스를 필요에 따른 처리로 뭉뚱그렸다. 양의 증분·VBC 설정과 루프 인용이 빠졌다. | 정정·보완. 네 조건 경로의 IXI 값과 IXB1·IXB2 갱신을 구분했다. 인덱스 저장식과 IF·DO 종료를 명시했다. | 3282–3318 |
| [swanpre2.ftn.md](../swan/src/swanpre2.ftn.md):3323–3368 | 시작 시점 기록은 3323행을 SEG 참 분기 안으로 적었다. SIDE 경고의 부정 의미가 불명확했다. DIRSI=0·CCW 인용과 바깥 IF 종료가 빠졌다. | 정정·보완. 작업 중 반영된 SEG의 ELSE·설정값·바깥 IF 종료 정정을 원문과 대조하여 유지했다. SIDE를 쓰지 말라는 메시지로 고쳤다. 3355·3365행 ENDIF 소속과 구간 끝의 열린 ELSE를 보완했다. | 3323–3365; 바깥 블록 종료 3612, 3873 |

이상 없음으로 확인한 구간은 1–137, 176–318, 368–400, 1260–1303, 1634–1676, 2070–2183, 2238–2324, 2357–2449이다.
이상 없음 구간은 위 기록의 구간 행에서 8개를 셌다.

3323–3368 구간에는 대조 작업 도중 별도로 반영된 정정이 있었다.
해당 정정은 원문과 대조하여 유지했다.
그 구간에는 경고의 부정 의미와 IF 종료 소속을 추가로 반영했다.

원문의 SHA-256은 대조 전후 모두 `20f0731a97d6eadf39b9c987537fba0397d0fe87a8936c46f8fff3aa5edbaa53`이다.
대상 기록의 frontmatter와 대상 구간 경계는 바꾸지 않았다.
이 작업의 쓰기는 대상 기록의 대상 구간과 이 보고서에 한정했다.
모델은 실행하지 않았다.

집계 단위는 대상 기록의 구간 행이다.
정정과 보완을 함께 적용한 12개 구간 행은 두 항목에 각각 포함했다.
중복을 제외한 대조 구간 행 수는 58이다.

정정 12, 보완 50, 이상 없음 8
