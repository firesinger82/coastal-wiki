2026-10-13 SWAN 판독 기록 전수 대조 결과.

각 기록의 구간표 행마다 frontmatter의 `file:` 원문을 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
한 번에 연 원문 구간은 모두 200행 이하였다.
조건·계산식·주석 수식·기본값·명령·분기 의미·바깥 블록 종료·전처리 표식을 대조했다.
오류와 누락은 대조한 구간 행에서 바로 수정했다.

| 기록 | 대조한 구간표 행 수 | 대조한 원문 행 수 | 정정 | 보완 | 정정·보완 동시 | 이상 없음 |
|---|---:|---:|---:|---:|---:|---:|
| [swan/README.md.md](../swan/README.md.md) | 15 | 288 | 0 | 1 | 0 | 14 |
| [swan/bin/swanrun.bat.md](../swan/bin/swanrun.bat.md) | 6 | 86 | 0 | 0 | 0 | 6 |
| [swan/bin/swanrun.md](../swan/bin/swanrun.md) | 8 | 137 | 1 | 0 | 0 | 7 |
| [swan/misc/swan.edt.md](../swan/misc/swan.edt.md) | 15 | 345 | 1 | 0 | 0 | 14 |
| [swan/src/CMakeLists.txt.md](../swan/src/CMakeLists.txt.md) | 11 | 133 | 0 | 3 | 0 | 8 |
| [swan/src/SdsBabanin.ftn90.md](../swan/src/SdsBabanin.ftn90.md) | 67 | 2708 | 16 | 36 | 8 | 23 |
| [swan/src/SwanBndStruc.ftn90.md](../swan/src/SwanBndStruc.ftn90.md) | 7 | 223 | 1 | 1 | 1 | 6 |
| 합계 | 129 | 3920 | 19 | 41 | 9 | 78 |

행 수는 대상 기록의 구간표와 그 구간이 덮는 원문에서 셌다.
원문 행 수에는 주석과 빈 줄을 포함했다.
정정과 보완은 각각 해당 표식이 붙은 구간표 행 수이다.
같은 구간에서 정정과 보완을 함께 했으면 양쪽에 한 번씩 셌다.
정정·보완 동시 9행은 위 합계의 정정과 보완에 중복 포함된다.
이상 없음은 수정하지 않은 구간표 행 수이다.
`swan.edt`의 추가 사실 정정은 같은 오류를 다룬 170–188 구간에 포함했다.

원문 행 번호는 각 기록의 `file:`을 기준으로 한다.
`switch.pl`은 `models/SWAN/raw/source_code/swan/switch.pl`이다.
전처리 제거 규칙은 82–105행에서 확인했다.
`!NRL`의 지원 여부는 인수 처리 19–38행도 확인했다.

정정·보완 목록의 구분은 새 요지 맨 앞에 적었다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [swan/README.md.md:38–71](../swan/README.md.md) | Ninja의 빌드 방식과 도구 다운로드로 묶음. | 보완. CMake의 설명을 구별했다. Ninja가 최신 대상을 다시 빌드하지 않는다는 부정문을 인용했다. | 44–54 |
| [swan/bin/swanrun.md:100–119](../swan/bin/swanrun.md) | 명령 치환의 마지막 역따옴표와 인용 닫는 백틱이 붙어 인라인 코드 인용이 닫히지 않음. | 정정. 103·104행 명령 전체를 각각 하나의 인라인 코드로 인용하도록 구분자를 고쳤다. 명령 내용은 유지했다. | 103–104 |
| [swan/misc/swan.edt.md:170–188](../swan/misc/swan.edt.md) | 추가 사실에 BIPHase·TRAnsfer 모두 닫는 선택지 기호가 없다고 씀. | 정정. BIPHase는 181행의 >로 닫힌다. TRAnsfer에는 대응하는 >가 없다. 구간 행과 추가 사실을 함께 고쳤다. | 180–183 |
| [swan/src/CMakeLists.txt.md:1–7](../swan/src/CMakeLists.txt.md) | 운영체제 IF/ELSEIF와 종료만 기록함. | 보완. ELSE가 없음을 적었다. 두 조건이 거짓일 때 SWITCHES를 설정하지 않음을 적었다. | 2–6 |
| [swan/src/CMakeLists.txt.md:51–69](../swan/src/CMakeLists.txt.md) | Intel의 UNIX/WIN32 분기에서 ELSE 부재를 표시하지 않음. | 보완. 53–57행 사슬에 ELSE가 없음을 적었다. 두 조건이 거짓일 때 이 사슬의 옵션 설정이 없음을 적었다. | 51–57 |
| [swan/src/CMakeLists.txt.md:123–133](../swan/src/CMakeLists.txt.md) | 실행 스크립트의 WIN32/UNIX 선택만 기록함. | 보완. 선택 사슬에 ELSE가 없음을 적었다. 두 조건이 거짓이면 스크립트 설치가 선택되지 않음을 적었다. | 129–133 |
| [swan/src/SdsBabanin.ftn90.md:1–111](../swan/src/SdsBabanin.ftn90.md) | EDENS·KDS 관계와 T1·T2 방법을 포괄적으로 요약함. | 보완. 주석의 정규화식·에너지식·임계 스펙트럼식·적분 범위·단위를 인용했다. L 지수 설명과 재보정 단서를 추가했다. | 16·44–60·75–91 |
| [swan/src/SdsBabanin.ftn90.md:112–154](../swan/src/SdsBabanin.ftn90.md) | 배열과 지역 변수 선언으로 요약함. | 보완. 선언 주석의 정규화식·차이식·단위·ELIM 적용 조건을 인용했다. | 116·124·129–130·150 |
| [swan/src/SdsBabanin.ftn90.md:155–200](../swan/src/SdsBabanin.ftn90.md) | ELIM 민감도 주석을 포함한다고만 씀. 주석 대안식을 생략함. | 보완. ELIM 적용 조건과 사례 한정의 민감도 미관찰을 적었다. 주석 처리한 ANAR 대안식과 진단 조건을 인용했다. | 178·181·197–199 |
| [swan/src/SdsBabanin.ftn90.md:201–226](../swan/src/SdsBabanin.ftn90.md) | 실행되는 ELIM=0.0만 인용함. | 보완. 주석 처리한 최대 에너지 기반 ELIM 대안식을 인용했다. | 201–203 |
| [swan/src/SdsBabanin.ftn90.md:260–310](../swan/src/SdsBabanin.ftn90.md) | !NRL을 -nrl로 활성화되는 진단 코드라고 씀. | 정정. 동봉 switch.pl에 -nrl과 !NRL 제거 규칙이 없음을 적었다. 진단 블록이 주석으로 남음을 적었다. | 262–294; switch.pl:19–38·82–105 |
| [swan/src/SdsBabanin.ftn90.md:311–400](../swan/src/SdsBabanin.ftn90.md) | Donelan 풍입력 방법을 요약하면서 주석 수식을 생략함. | 보완. Sin과 B·E의 관계식을 인용했다. 방향 단위를 적었다. | 364·368 |
| [swan/src/SdsBabanin.ftn90.md:401–469](../swan/src/SdsBabanin.ftn90.md) | 환산 변경 이력·고주파 과대 추정·꼬리 기울기를 포괄적으로 요약함. | 보완. 주석의 환산식·계수·기본값·조건·재보정 비교와 부정문을 보존했다. 주석 속 실험 결과임을 구별했다. | 408–468 |
| [swan/src/SdsBabanin.ftn90.md:470–503](../swan/src/SdsBabanin.ftn90.md) | AINV 비교식과 입력·실험 수치를 생략함. | 보완. 입력 예시와 다섯 비교식을 인용했다. 실험 수치와 기원 불확실성·추정 방향을 적었다. | 472–498 |
| [swan/src/SdsBabanin.ftn90.md:504–540](../swan/src/SdsBabanin.ftn90.md) | !NRL 선언이 -nrl로 활성화된다고 씀. | 정정. 해당 스위치와 제거 규칙이 없어서 주석으로 남음을 적었다. | 531; switch.pl:19–38·82–105 |
| [swan/src/SdsBabanin.ftn90.md:541–572](../swan/src/SdsBabanin.ftn90.md) | 각주파수와 방향 간격으로 적분한다고 씀. | 정정. SPCSIG 곱셈과 방향 합산을 구별했다. 주파수 적분으로 오해할 수 있는 설명을 고쳤다. | 542–549 |
| [swan/src/SdsBabanin.ftn90.md:541–572](../swan/src/SdsBabanin.ftn90.md) | KUIK 비교 예시를 주석이라고만 적음. | 보완. 주석의 rmsdir 계산식을 인용했다. | 565–567 |
| [swan/src/SdsBabanin.ftn90.md:605–642](../swan/src/SdsBabanin.ftn90.md) | 실행식만 인용하고 Donelan 표기의 주석 수식을 생략함. | 보완. BETA와 GAMMA의 관계 및 Sin 수식을 주석으로 구별해 인용했다. | 630–633 |
| [swan/src/SdsBabanin.ftn90.md:664–710](../swan/src/SdsBabanin.ftn90.md) | RDCOEF 권장값·기본값을 한국어로만 적고 비교 계수를 생략함. | 보완. RDCOEF 주석 원문과 Zieger 비교 계수·버전을 추가했다. ANYWND 제거 이유를 보존했다. | 670–684 |
| [swan/src/SdsBabanin.ftn90.md:711–730](../swan/src/SdsBabanin.ftn90.md) | 작용밀도 우변 변환 이유와 MEMSINB 저장 목적만 요약함. | 보완. 주석의 B*N·SWINEB*AC2·S_IN·총 풍입력 표현을 인용했다. | 712–719 |
| [swan/src/SdsBabanin.ftn90.md:731–767](../swan/src/SdsBabanin.ftn90.md) | !NRL 출력 블록이 -nrl로 활성화된다고 씀. | 정정. 해당 규칙이 없어서 주석으로 남는다고 고쳤다. | 732–749; switch.pl:19–38·82–105 |
| [swan/src/SdsBabanin.ftn90.md:731–767](../swan/src/SdsBabanin.ftn90.md) | 풍향·풍속 출력의 변환식과 변수를 생략함. | 보완. THETAW 각도 변환식과 TEMP2·UFRIC 출력문을 인용했다. | 753·755 |
| [swan/src/SdsBabanin.ftn90.md:768–861](../swan/src/SdsBabanin.ftn90.md) | 총응력·선형 입력·벡터 응력 설명을 요약하면서 주석 수식을 생략함. | 보완. 응력 분해식·선형 입력식·방향 적분식·스칼라 및 벡터 응력식을 인용했다. 선형 응력의 과거 설명과 후속 변경을 구별했다. | 803–854 |
| [swan/src/SdsBabanin.ftn90.md:913–944](../swan/src/SdsBabanin.ftn90.md) | 마지막 주파수 간격의 한계 설명이라고만 씀. | 보완. 주석의 차분식을 인용했다. 10 Hz 초과 시 EXIT로 루프를 끝내는 행을 적었다. | 926–936 |
| [swan/src/SdsBabanin.ftn90.md:945–972](../swan/src/SdsBabanin.ftn90.md) | !NRL 진단 출력을 실행 단계로 설명하고 -nrl로 활성화된다고 씀. | 정정. 제거 규칙이 없는 진단 주석으로 고쳤다. | 964–970; switch.pl:19–38·82–105 |
| [swan/src/SdsBabanin.ftn90.md:945–972](../swan/src/SdsBabanin.ftn90.md) | f의 -2승 꼬리와 단위 변환만 요약함. | 보완. 주석의 꼬리 유도식과 변환 전후 단위를 인용했다. | 953–961 |
| [swan/src/SdsBabanin.ftn90.md:973–1028](../swan/src/SdsBabanin.ftn90.md) | 풍속 제한·대체 방법을 포괄적으로 요약함. | 보완. 상한의 미분 조건과 대안의 풍속 조건·수치·단위를 보존했다. 주석의 비교 사례임을 적었다. | 982–989·1003–1023 |
| [swan/src/SdsBabanin.ftn90.md:1029–1066](../swan/src/SdsBabanin.ftn90.md) | !NRL을 -nrl 활성화 출력으로 적음. | 정정. 지원 규칙이 없는 출력 주석으로 고쳤다. ELSE에 실행되는 로그가 없음을 적었다. | 1043–1045·1061–1065; switch.pl:19–38·82–105 |
| [swan/src/SdsBabanin.ftn90.md:1067–1097](../swan/src/SdsBabanin.ftn90.md) | !NRL 진단이 -nrl로 활성화된다고 씀. | 정정. 지원 규칙이 없는 !NRL 진단 주석으로 고쳤다. | 1071–1076·1085–1087; switch.pl:19–38·82–105 |
| [swan/src/SdsBabanin.ftn90.md:1098–1134](../swan/src/SdsBabanin.ftn90.md) | !NRL 진단이 -nrl로 활성화된다고 씀. | 정정. 지원 규칙이 없는 !NRL 진단 주석으로 고쳤다. | 1113–1115; switch.pl:19–38·82–105 |
| [swan/src/SdsBabanin.ftn90.md:1135–1164](../swan/src/SdsBabanin.ftn90.md) | !NRL 진단이 -nrl로 활성화된다고 씀. | 정정. DEBUG.DAT 기록과 STOP이 주석으로 남음을 적었다. 실제 NaN 메시지·STOP과 바깥 ISOL 조건을 구별했다. | 1136–1162; switch.pl:19–38·82–105 |
| [swan/src/SdsBabanin.ftn90.md:1135–1164](../swan/src/SdsBabanin.ftn90.md) | 첫 경고 메시지 원문을 생략함. | 보완. no solution found 출력문을 인용했다. | 1137–1140 |
| [swan/src/SdsBabanin.ftn90.md:1165–1202](../swan/src/SdsBabanin.ftn90.md) | !NRL 진단이 -nrl로 활성화된다고 씀. | 정정. 지원 규칙이 없는 !NRL 진단 주석으로 고쳤다. | 1166–1181; switch.pl:19–38·82–105 |
| [swan/src/SdsBabanin.ftn90.md:1165–1202](../swan/src/SdsBabanin.ftn90.md) | 주석 처리된 S_IN1D_L 초기화를 생략함. | 보완. 0 초기화는 주석임을 인용했다. 방향 적분값이 유지되는 순서를 적었다. | 1173·1182·1187 |
| [swan/src/SdsBabanin.ftn90.md:1203–1278](../swan/src/SdsBabanin.ftn90.md) | 감소계수 방법과 응력 방법 차이를 포괄적으로 요약함. | 보완. U/C 조건·응력 상한식·반복 종료 비교를 인용했다. 상반된 시간 측정 주석의 수치를 구별했다. | 1207–1255 |
| [swan/src/SdsBabanin.ftn90.md:1333–1363](../swan/src/SdsBabanin.ftn90.md) | -nrl로 !NRL만 제거한 뒤 나머지 !가 남는다고 설명함. | 정정. 동봉 switch.pl에는 해당 규칙이 없어서 !NRL! 전체가 그대로 남음을 적었다. | 1348–1353; switch.pl:19–38·82–105 |
| [swan/src/SdsBabanin.ftn90.md:1466–1497](../swan/src/SdsBabanin.ftn90.md) | 주석의 A와 A/sigma 구별을 생략함. | 보완. 계산량이 A/sigma라는 주석의 부정을 보존했다. | 1470–1473 |
| [swan/src/SdsBabanin.ftn90.md:1498–1525](../swan/src/SdsBabanin.ftn90.md) | !NRL 감소비 출력이 -nrl로 활성화된다고 씀. | 정정. 해당 규칙이 없는 출력 주석으로 고쳤다. | 1520–1523; switch.pl:19–38·82–105 |
| [swan/src/SdsBabanin.ftn90.md:1498–1525](../swan/src/SdsBabanin.ftn90.md) | 밀도 안내 주석의 수치를 생략함. | 보완. 공기·물 밀도 수치를 주석으로 구별해 인용했다. | 1499·1515 |
| [swan/src/SdsBabanin.ftn90.md:1526–1561](../swan/src/SdsBabanin.ftn90.md) | 각 빈의 FILTER를 출력한다고 씀. !NRL을 -nrl 활성화 블록으로 설명함. | 정정. 재계산하지 않은 스칼라 FILTER의 출력임을 적었다. !NRL 적분·출력은 주석으로 남는다고 고쳤다. | 1466–1468·1526–1560; switch.pl:19–38·82–105 |
| [swan/src/SdsBabanin.ftn90.md:1562–1583](../swan/src/SdsBabanin.ftn90.md) | 풍향 출력을 요약하고 각도 변환식을 생략함. | 보완. THETAW 변환식을 인용했다. 두 ITEST 블록의 종료 행을 적었다. | 1564–1578 |
| [swan/src/SdsBabanin.ftn90.md:1638–1682](../swan/src/SdsBabanin.ftn90.md) | 해빙 가중계수의 두 표현과 조건 검사 목적을 요약함. | 보완. 두 가중계수식·수면 비율 정의·적용식을 인용했다. 조건 검사가 결과를 바꾸지 않는다는 주석을 보존했다. | 1671–1679 |
| [swan/src/SdsBabanin.ftn90.md:1724–1791](../swan/src/SdsBabanin.ftn90.md) | 궤도속도 설명의 부정과 주석 처리한 CDSV·SWDIS 관계를 생략함. | 보완. RMS 속도 진폭의 구별을 보존했다. 주석 선언값과 SWDIS 비율식을 인용했다. | 1767·1780·1789 |
| [swan/src/SdsBabanin.ftn90.md:1792–1849](../swan/src/SdsBabanin.ftn90.md) | 문헌별 수치 비교와 전달·비례 관계를 포괄적으로 요약함. | 보완. fe·Re_crit의 판본별 값과 불확실성을 보존했다. 작용밀도 전달식·단위·진폭 및 주파수 비례식을 인용했다. | 1793–1848 |
| [swan/src/SdsBabanin.ftn90.md:1867–1906](../swan/src/SdsBabanin.ftn90.md) | 물 점성 문헌과 주석 처리된 KDS_PHILLIPS 루프를 요약함. | 보완. 감쇠식·점성계수·KDS 계산 및 누적식을 인용했다. 루프 전체의 주석 상태를 표시했다. | 1869–1876·1889–1892 |
| [swan/src/SdsBabanin.ftn90.md:1907–1978](../swan/src/SdsBabanin.ftn90.md) | Reynolds 수별 주석 수식과 fe 계산식을 생략함. | 보완. 두 조건과 소산식·fe 계수식을 인용했다. 원문의 E와 F 표기를 유지했다. | 1943–1952 |
| [swan/src/SdsBabanin.ftn90.md:1979–2023](../swan/src/SdsBabanin.ftn90.md) | RMS 속도 진폭의 구별과 주석 CDSV·SWDIS 관계를 생략함. | 보완. URMSTOP의 부정을 보존했다. 주석 선언값과 SWDIS 비율식을 인용했다. | 1993·2007·2016 |
| [swan/src/SdsBabanin.ftn90.md:2065–2145](../swan/src/SdsBabanin.ftn90.md) | 소산식 설명을 주석으로 적는다고만 씀. | 보완. Zieger 소산식과 SWDIS의 비율식 주석을 인용했다. | 2099·2144 |
| [swan/src/SdsBabanin.ftn90.md:2146–2178](../swan/src/SdsBabanin.ftn90.md) | AC2 방향 적분만으로 SIGDENS를 만든다고 씀. | 정정. SPCSIG 곱셈을 포함한 방향 적분으로 고쳤다. KTHETA에 복사하는 값은 AC2임을 구별했다. | 2147–2154 |
| [swan/src/SdsBabanin.ftn90.md:2146–2178](../swan/src/SdsBabanin.ftn90.md) | RMS 방향 퍼짐 비교 호출을 주석이라고만 적음. | 보완. 주석의 rmsdir 계산식을 인용했다. | 2170–2172 |
| [swan/src/SdsBabanin.ftn90.md:2179–2194](../swan/src/SdsBabanin.ftn90.md) | ANAR를 역적분이라고 부름. | 정정. AINV의 역수로 고쳤다. | 2183·2189 |
| [swan/src/SdsBabanin.ftn90.md:2179–2194](../swan/src/SdsBabanin.ftn90.md) | SQRTBN 대체식은 주석이라고만 씀. | 보완. 주석 처리한 대체식을 인용했다. | 2192 |
| [swan/src/SdsBabanin.ftn90.md:2195–2219](../swan/src/SdsBabanin.ftn90.md) | 응력 전달에 관한 주석이라고만 씀. | 보완. 해양 응력으로 보내야 한다는 설명과 대기 응력으로 보내면 안 된다는 부정을 보존했다. | 2203–2204 |
| [swan/src/SdsBabanin.ftn90.md:2220–2273](../swan/src/SdsBabanin.ftn90.md) | 배열 전체 크기를 사용하지 않는 이유는 주석이라고만 씀. | 보완. np=size(x) 주석과 부분 충전 배열이라는 이유를 인용했다. | 2263 |
| [swan/src/SdsBabanin.ftn90.md:2274–2319](../swan/src/SdsBabanin.ftn90.md) | A1 시도 이력을 주석이라고만 씀. | 보완. 과거 A1 값과 시도별 수치·Hs 차이를 현재 대입과 구별했다. | 2309–2313 |
| [swan/src/SdsBabanin.ftn90.md:2383–2418](../swan/src/SdsBabanin.ftn90.md) | WAGE 범위 검사와 최종 CD 검사가 주석이라고만 씀. | 보완. 주석의 조건·거칠기·항력·마찰속도식을 모두 인용했다. 실제 2398행 ENDIF와 주석 ENDIF를 구별했다. | 2385–2408 |
| [swan/src/SdsBabanin.ftn90.md:2532–2557](../swan/src/SdsBabanin.ftn90.md) | 작용밀도 꼬리의 -3승과 감소계수 설명으로 요약함. | 보완. Sin의 -2승 유도식과 GENC0의 -3승 변환식을 인용했다. 감소 규모와 적용 설명을 보존했다. | 2535–2542 |
| [swan/src/SdsBabanin.ftn90.md:2675–2708](../swan/src/SdsBabanin.ftn90.md) | KUIK 진단 출력이 -nrl로 활성화된다고 씀. | 정정. 해당 규칙이 없어 주석으로 남는다고 고쳤다. | 2698–2701; switch.pl:19–38·82–105 |
| [swan/src/SwanBndStruc.ftn90.md:99–132](../swan/src/SwanBndStruc.ftn90.md) | 시작·끝 좌표와 x/y 증가·감소로 설명함. | 정정. 계산 격자의 시작·끝 인덱스와 인덱스 증분으로 고쳤다. | 99–130 |
| [swan/src/SwanBndStruc.ftn90.md:99–132](../swan/src/SwanBndStruc.ftn90.md) | ELSE 부재를 표시하지 않음. | 보완. ELSE가 없음을 적었다. 131행 ENDIF 종료를 적었다. | 99–131 |

대상 원문 7개의 SHA-256은 기존 frontmatter의 해시와 일치했다.
대상 기록의 frontmatter와 구간 경계는 유지했다.
모델은 실행하지 않았다.
원문과 노트는 수정하지 않았다.
git 작업은 하지 않았다.

정정 19, 보완 41, 이상 없음 78
