# SWAN swancom3.ftn 판독 기록 전수 대조

대상 기록은 `_staging/recovery/read/SWAN/swan/src/swancom3.ftn.md`이다.
원문은 frontmatter의 `models/SWAN/raw/source_code/swan/src/swancom3.ftn`이다.
원문 2,904행의 SHA-256은 frontmatter와 일치한다.
대상 기록의 구간 행은 63개이다.
각 구간의 원문을 `nl -ba <원문> | sed -n 'A,Bp'`로 열어 대조했다.
원문을 여는 명령마다 200행 이하를 출력했다.
전처리 표시의 기준은 `models/SWAN/raw/source_code/swan/switch.pl` 82–105행이다.
원문 1–2904행에 대응하는 구간 행 63개를 모두 대조했다.
말미의 코드 사실 20개도 같은 원문과 대조했다.

| 기록 | 대조한 구간 행 수 | 대조한 원문 행 수 | 대조한 코드 사실 수 |
|---|---|---|---|
| `_staging/recovery/read/SWAN/swan/src/swancom3.ftn.md` | 63 | 2,904 (1–2904행) | 20 |

아래 집계는 위 기록의 구간 행과 코드 사실을 각각 한 항목으로 센 값이다.
정정과 보완을 함께 한 구간 행 7개는 정정에만 센다.
보완 수는 정정 없이 보완한 항목 수이다.
이상 없음 수는 대조 후 고치지 않은 항목 수이다.

| 대조 대상 | 정정 | 보완 | 이상 없음 |
|---|---|---|---|
| 구간 행 63개 | 9 | 29 | 25 |
| 코드 사실 20개 | 2 | 1 | 17 |
| 합계 83개 | 11 | 30 | 42 |

아래 표의 기록 경로는 `_staging/recovery/read/SWAN/`을 기준으로 적었다.
원문 행의 `swancom3.ftn`은 위 frontmatter 원문을 가리킨다.
원문 행의 `switch.pl`은 `models/SWAN/raw/source_code/swan/switch.pl`을 가리킨다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| swan/src/swancom3.ftn.md:1–29 | WNDPAR를 1·2세대 바람 입력으로 요약했다. | 정정: 루틴 목록의 목적을 초기 추정 스펙트럼용 DOLPHIN-B 식으로 고쳤다. | swancom3.ftn:10–19 |
| swan/src/swancom3.ftn.md:100–171 | 소스항의 방향 조건을 생략·일반화했다. 수식은 설명으로만 남겼다. | 정정·보완: 세 소스항의 에너지·방향 조건을 구분했다. A·B·TAU·Elim·ALPHA·Edml의 주석 수식을 행별로 인용했다. | swancom3.ftn:115–169 |
| swan/src/swancom3.ftn.md:172–193 | SPCDIR 방향 단위와 SPCSIG의 상대 주파수 의미를 생략했다. | 보완: 방향 단위 radians와 sigma-space 상대 주파수 의미를 추가했다. | swancom3.ftn:174–180 |
| swan/src/swancom3.ftn.md:194–259 | PWIND(1..13) 수치를 나열했지만 주석 원문은 인용하지 않았다. | 보완: 계수 이름과 주석 값을 원문대로 인용했다. | swancom3.ftn:246–258 |
| swan/src/swancom3.ftn.md:260–350 | 해빙 인자와 구조 주석의 조건·계산을 설명으로만 남겼다. | 보완: 해빙 인자 두 식과 점유율 합 조건을 인용했다. 구조 주석의 분기와 A + B E 계산을 추가했다. | swancom3.ftn:279–310 |
| swan/src/swancom3.ftn.md:351–400 | IWIND=1·2 선택의 나머지 ELSE 유무를 적지 않았다. | 보완: 나머지 ELSE가 없으며 402행 ENDIF에서 닫힌다고 추가했다. | swancom3.ftn:378–402 |
| swan/src/swancom3.ftn.md:451–503 | GROWW 분기 사슬의 나머지 ELSE 유무를 적지 않았다. | 보완: 503행 END IF로 닫히는 사슬에 나머지 ELSE가 없음을 추가했다. | swancom3.ftn:473–503 |
| swan/src/swancom3.ftn.md:504–548 | 구간 시작의 두 DO 블록 종료를 묶어서 적었다. | 보완: IDDUM 루프와 IS 루프의 닫힘 행을 각각 명시했다. | swancom3.ftn:527–528 |
| swan/src/swancom3.ftn.md:601–672 | 방법 주석의 마찰 속도·항력·주파수 식을 설명으로만 남겼다. | 보완: SWIND1·2의 주파수 식과 Wu·Janssen의 분기·계산식 및 3세대 주파수 식을 주석 그대로 인용했다. | swancom3.ftn:642–670 |
| swan/src/swancom3.ftn.md:673–752 | 구조 주석의 풍속 조건과 IWIND별 계산 구분을 생략했다. | 보완: 상수 바람 조건과 IWIND=1·2 및 IWIND=3의 주석상 계산 구분을 인용했다. | swancom3.ftn:675–681·736–744 |
| swan/src/swancom3.ftn.md:811–875 | 풍향을 스펙트럼 중심 방향 ±π로 이동한다고 적었다. 그림의 방향 경계값도 생략했다. | 정정·보완: 하한 미만에서는 2*PI를 더한다. 뒤의 별도 검사에서 상한 초과이면 2*PI를 뺀다. 그림에 적힌 IDWMAX 135도와 IDWMIN 325도를 인용했다. | swancom3.ftn:811–829 |
| swan/src/swancom3.ftn.md:929–985 | 구간 시작의 IDRAG 선택문과 보간 분기의 종료·나머지 ELSE 유무를 생략했다. | 보완: 975행과 961행의 닫힘 및 나머지 ELSE 부재를 추가했다. 바깥 IWIND 분기 범위도 명시했다. | swancom3.ftn:906–986·1093 |
| swan/src/swancom3.ftn.md:986–1011 | 구간 시작의 IWIND 선택문과 내부 IDRAG 선택문의 닫힘 행을 생략했다. | 보완: 바깥 IWIND 선택문은 1093행에서 닫힌다. 내부 IDRAG 선택문은 1084행에서 닫힌다. | swancom3.ftn:906·986–1011·1084–1093 |
| swan/src/swancom3.ftn.md:1012–1058 | 보간 분기의 나머지 ELSE 부재와 구간을 감싸는 선택문 종료를 생략했다. | 보완: 1044행에서 닫히는 보간 사슬에 나머지 ELSE가 없음을 추가했다. 1045행 ELSE의 소속과 바깥 선택문 종료를 명시했다. | swancom3.ftn:992–1093 |
| swan/src/swancom3.ftn.md:1059–1094 | IDRAG·IWIND 분기 사슬의 나머지 ELSE 유무와 Hwang 주석의 풍속 조건을 생략했다. | 보완: IDRAG=1..6과 IWIND의 두 분기 사슬에는 나머지 ELSE가 없음을 추가했다. 70 m/s 조건은 주석으로 구분했다. | swancom3.ftn:1065–1093 |
| swan/src/swancom3.ftn.md:1175–1218 | 적분 범위만 요약하고 주석의 적분식을 생략했다. | 보완: ETOTW 이중 적분과 ETOTW(d) 적분 및 방향 적분의 원문을 인용했다. | swancom3.ftn:1185–1216 |
| swan/src/swancom3.ftn.md:1219–1298 | 변수 설명 주석의 차분식과 에너지 영역 조건을 생략했다. | 보완: DUM_DS의 LOGSIG(IS+1) - FPM과 ETOTW의 a > apm 및 180도 영역 주석을 추가했다. | swancom3.ftn:1245–1249 |
| swan/src/swancom3.ftn.md:1299–1352 | 계산 앞의 FPM 수식·주파수 값 주석을 생략했다. | 보완: minimum FPM 주석과 8 rad/s = 1.27 Hz 표기를 인용했다. | swancom3.ftn:1303–1305 |
| swan/src/swancom3.ftn.md:1394–1423 | 목적 주석을 비성장 성분의 하한 제한으로 바꾸어 요약했다. 상한과 ALPHA 수식을 생략했다. | 정정·보완: 목적 주석의 에너지 밀도 조건을 원문대로 구분했다. A(s,t)와 MIN을 쓰는 ALPHA 주석식을 인용했다. | swancom3.ftn:1396–1421 |
| swan/src/swancom3.ftn.md:1424–1493 | GROWW 주석의 부등호와 구조 주석의 분기를 생략했다. | 보완: 성장·소산 조건의 원문을 인용했다. 구조 주석의 else if와 실행 코드의 독립된 두 IF를 구분했다. | swancom3.ftn:1438–1440·1462–1469·1500–1503 |
| swan/src/swancom3.ftn.md:1585–1615 | 선형 입력·필터·Jacobian·FPM 식을 설명으로만 남겼다. | 보완: 1.5*10^-3 계수와 주파수 필터 및 Jacobian·FPM의 주석식을 행별로 인용했다. | swancom3.ftn:1600–1613 |
| swan/src/swancom3.ftn.md:1672–1720 | 큰 응력 기여를 단정적으로 요약했다. 응력 적분·sigma^-3·해빙 수식과 대안 꺾임 주파수를 생략했다. | 정정·보완: 응력 기여가 클 수 있다는 저자의 관찰로 고쳤다. 근사 설명의 수식과 해빙 인자 및 대안 fpm을 추가했다. | swancom3.ftn:1672–1706 |
| swan/src/swancom3.ftn.md:1755–1795 | ARGU의 주석식과 A/sigma 계산에 대한 주석을 생략했다. | 보완: 기존 ARGU 식의 주석과 A가 아니라 A/sigma를 계산한다는 설명을 추가했다. | swancom3.ftn:1758–1766 |
| swan/src/swancom3.ftn.md:1796–1841 | 응력 적분 앞의 EN=sig*ac2 주석식을 생략했다. | 보완: EN=sig*ac2 관계와 AC2 인자를 제거했다는 주석 설명을 추가했다. | swancom3.ftn:1805 |
| swan/src/swancom3.ftn.md:1902–1939 | Snyder–Komen 입력·Wu 마찰 속도·FPM 주석식을 설명으로만 남겼다. | 보완: 성장률 B와 Sin, Wu 식, FPM 식을 원문 행별로 인용했다. | swancom3.ftn:1918–1937 |
| swan/src/swancom3.ftn.md:1996–2040 | 해빙 수식과 !/T의 스위치 처리 여부를 생략했다. | 보완: 해빙 인자의 원문 식을 인용했다. !/T는 switch.pl의 어떤 분기에서도 제거하지 않는 주석 표시임을 추가했다. | swancom3.ftn:1999–2002·2035; switch.pl:82–106 |
| swan/src/swancom3.ftn.md:2162–2188 | Janssen 입력의 방법 주석에서 Sin·B 수식을 생략했다. | 보완: Sin·B와 주석의 지수·분모를 원문 행별로 인용했다. | swancom3.ftn:2178–2183 |
| swan/src/swancom3.ftn.md:2189–2274 | 인수 설명 주석에 없는 TAUWV를 포함했다. PWIND 수치와 해빙 식은 인용하지 않았다. | 정정·보완: 해당 구간의 주석 목록에서 TAUWV를 제거했다. PWIND 주석 값과 해빙 인자 수식을 인용했다. | swancom3.ftn:2189–2237·2257–2260 |
| swan/src/swancom3.ftn.md:2359–2389 | 구간 시작 ELSE와 뒤의 IS 루프의 닫힘 행을 생략했다. | 보완: 2331행 선택문은 2587행에서 닫힌다. 2378행 IS 루프는 2439행에서 닫힌다. | swancom3.ftn:2331·2359–2439·2587 |
| swan/src/swancom3.ftn.md:2390–2440 | TAUDIR 계산이 시험 출력 조건 안에 있음을 명시하지 않았다. 두 루프의 닫힘 행을 묶어서 적었다. | 정정·보완: TAUDIR의 ATAN2·영값·MOD 계산은 ITEST≥40·TESTFL 안에 있음을 명시했다. 각 바깥 블록의 닫힘을 추가했다. | swancom3.ftn:2423–2439·2587 |
| swan/src/swancom3.ftn.md:2441–2508 | GOTO 5000의 정확한 도착 위치와 바깥 ELSE의 닫힘을 생략했다. | 보완: GOTO 5000은 두 루프 뒤의 2507행으로 이동함을 명시했다. 바깥 선택문은 2587행에서 닫힌다. | swancom3.ftn:2491–2507·2587 |
| swan/src/swancom3.ftn.md:2509–2532 | 구간 전체를 감싸는 ELSE의 닫힘 행을 생략했다. | 보완: 2359행 ELSE가 속한 2331행 선택문은 2587행에서 닫힌다고 명시했다. | swancom3.ftn:2331·2359·2587 |
| swan/src/swancom3.ftn.md:2533–2569 | 보정에 사용하는 두 응력의 이름을 생략했다. 수렴 이동을 종료로만 요약했다. | 정정·보완: TAUNEW 보정은 TAUTOT과 TAUW의 평균이다. 수렴하면 2568행으로 이동하여 TAUTOT 갱신을 건너뛴다. 바깥 선택문의 닫힘을 명시했다. | swancom3.ftn:2563–2570·2587 |
| swan/src/swancom3.ftn.md:2589–2647 | SWINEB의 인자를 단순한 속도비 제곱으로 요약했다. | 정정: XFAC2는 (UFRIC/CW1 + ZALP)의 제곱이다. SWINEB는 RHOAW·BETA·XFAC2·COS2·SIGMA의 곱이다. | swancom3.ftn:2609·2619–2622 |
| swan/src/swancom3.ftn.md:2730–2752 | Yan의 주석식을 설명으로만 남겼다. | 보완: X의 정의와 네 계수를 포함한 Yan 식을 원문 행별로 인용했다. | swancom3.ftn:2744–2751 |
| swan/src/swancom3.ftn.md:2753–2822 | ICEWIND 인자를 설명으로만 남겼다. | 보완: 해빙 인자 두 식과 물·얼음 점유율 합 조건을 원문대로 인용했다. | swancom3.ftn:2805–2808 |
| swan/src/swancom3.ftn.md:코드 사실 910–911·977–984 | WIND10 재정의를 Wu 항력비라고만 적었다. | 정정: WIND10에는 현재 풍속과 기준 풍속 15의 Wu 항력계수 비의 제곱근을 곱한다고 고쳤다. | swancom3.ftn:910–911·977–984 |
| swan/src/swancom3.ftn.md:코드 사실 1071–1074 | USCAP 상한 적용 뒤 CDFAC를 곱한다고 적었다. | 정정: 실제 곱하는 인자는 SQRT(CDFAC)라고 고쳤다. | swancom3.ftn:1071–1074 |
| swan/src/swancom3.ftn.md:코드 사실 1755–1794·1797–1813 | 선형 입력 저장 조건에서 SIGMA≥0.7*FPM을 생략했다. | 보완: ANYWND와 주파수 하한을 함께 검사하는 조건을 추가했다. | swancom3.ftn:1755–1794·1797–1813 |
| swan/src/swancom3.ftn.md:30–99 | 수정 이력의 FPM 설정식을 생략했다. | 보완: FPM=SIGPKD라는 수정 이력 주석을 인용했다. | swancom3.ftn:89 |
| swan/src/swancom3.ftn.md:401–450 | 한계 스펙트럼 주석의 주파수·파수 변환 표기를 생략했다. | 보완: f^-5에서 k^-3으로 변환하는 표기와 주석의 문헌 참조를 추가했다. | swancom3.ftn:410–413 |

기록에서 단일 행 번호에 직접 연결된 인용 818개를 추출하여 원문 문자열과 행 번호의 일치를 확인했다.
원문의 `!ESMF` 표시 9행은 `-esmf`로 활성화된다(switch.pl:21·82–83).
원문 2035행의 `!/T`는 접두부 제거 규칙에 없으므로 주석으로 남는다(switch.pl:82–106).
기록의 frontmatter와 구간 경계는 변경하지 않았다.
원문 파일의 SHA-256은 작업 전후에 같았다.
모델은 실행하지 않았다.
쓰기 대상은 요청한 판독 기록과 이 검증표뿐이다.

정정 11, 보완 30, 이상 없음 42
