# Celeris code-4 전수 검증

원문과 기록의 의미를 대조한 결과다. 모델은 실행하지 않았다.

행 수는 기록 표의 구간 행 수와 그 구간에 포함된 원문 행 수로 구분한다. 정정·보완은 해당 표 행에 붙인 표식 수로 센다. 이상 없음은 완료 기록에서 수정하지 않은 구간 행 수로 센다.

대상 18개 기록의 구간 행 154개를 대조했다. 해당 구간의 원문 행 수는 5,135행이다. 한 구간 행에 정정과 보완이 함께 있으면 각각 센다.

기록 경로는 `_staging/recovery/read/Celeris/Celeris-WebGPU/js/`를 기준으로 썼다. 표의 파일명에 `.md`를 붙이면 대상 기록 경로가 된다.

| 기록 | 대조한 구간 행 수 | 대조한 원문 행 수 | 상태 |
|---|---:|---:|---|
| Handler_SedTrans_Pass1.js | 3 | 124 | 완료 |
| Handler_SedTrans_Pass3.js | 5 | 254 | 완료 |
| Handler_SedTrans_UpdateBottom.js | 3 | 135 | 완료 |
| Handler_Skybox.js | 2 | 57 | 완료 |
| Handler_Tridiag.js | 3 | 109 | 완료 |
| Handler_UpdateTrid.js | 2 | 81 | 완료 |
| Handler_Updateneardry.js | 2 | 54 | 완료 |
| Model_Loaders.js | 9 | 236 | 완료 |
| Run_Compute_Shader.js | 5 | 89 | 완료 |
| Run_Tridiag_Solver.js | 3 | 93 | 완료 |
| Time_Series.js | 6 | 184 | 완료 |
| Wave_Generator.js | 13 | 374 | 완료 |
| agent_controls.js | 28 | 949 | 완료 |
| constants_load_calc.js | 23 | 664 | 완료 |
| display_parameters.js | 9 | 251 | 완료 |
| site.js | 1 | 4 | 완료 |
| ../scripts/clean_WebGPUCeleris_output.m | 1 | 5 | 완료 |
| ../river.html | 36 | 1472 | 완료 |

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| Handler_SedTrans_Pass1.js:1–38 | uniform 매개변수 주석 예시 누락 | time 예시 추가 [보완] | 7 |
| Handler_SedTrans_Pass1.js:39–83 | 저장 텍스처 주석과 바깥 블록 종료 행 누락 | 결과 쓰기 주석 및 배열·호출·함수 종료 행 추가 [보완] | 60, 70, 79–81 |
| Handler_SedTrans_Pass3.js:1–83 | uniform 주석 예시 누락 | time 예시 추가 [보완] | 7 |
| Handler_SedTrans_Pass3.js:84–123 | 출력 주석 및 바깥 블록 종료 행 누락 | 주석 설명과 종료 행 추가 [보완] | 85, 95, 105, 115, 169–171 |
| Handler_SedTrans_Pass3.js:124–173 | 종료 위치 미표기 | 배열·호출·함수 종료 행 추가 [보완] | 169–171 |
| Handler_SedTrans_Pass3.js:216–254 | 종료 위치 미표기 | 배열·호출·함수 종료 행 추가 [보완] | 252–254 |
| Handler_SedTrans_UpdateBottom.js:1–38 | 매개변수 예시와 읽기 자원 주석 누락 | time 예시와 주석·코드 구별 추가 [보완] | 7, 13–36 |
| Handler_SedTrans_UpdateBottom.js:39–90 | 자원 설명 주석과 종료 행 누락 | 읽기·쓰기 주석과 바깥 블록 종료 행 추가 [보완] | 40, 49, 59, 69, 78, 86–88 |
| Handler_Skybox.js:1–33 | uniform 주석 예시 누락 | time 예시 추가 [보완] | 6 |
| Handler_Tridiag.js:1–38 | uniform 주석 예시 누락 | time 예시 추가 [보완] | 7 |
| Handler_Tridiag.js:39–72 | 자원 주석과 종료 행 누락 | 쓰기·읽기 주석 및 종료 행 추가 [보완] | 40, 50, 60, 68–70 |
| Handler_UpdateTrid.js:1–52 | 매개변수 예시와 자원 설명 주석 누락 | time 예시와 읽기·쓰기 주석 추가 [보완] | 6, 12, 21, 30, 40 |
| Handler_Updateneardry.js:1–33 | 매개변수 예시와 결과 쓰기 주석 누락 | time 예시와 결과 쓰기 주석 추가 [보완] | 6, 21 |
| Model_Loaders.js:1–19 | models 부재만 빈 배열 반환 조건으로 설명 | 논리 OR의 falsy 조건으로 정정 [정정] | 17 |
| Model_Loaders.js:20–42 | 절반 치수의 주석 근거 누락 | 단위 정육면체 2× 설명 추가 [보완] | 26 |
| Model_Loaders.js:43–66 | 오류 출력 요약 및 주석인 tree 분기 누락 | 오류 출력과 else 부재 및 tree 주석 명시 [보완] | 49–61 |
| Model_Loaders.js:95–128 | 바깥 함수 종료 행과 이전 코드 설명 누락 | 종료 행 및 주석 추가 [보완] | 118, 171 |
| Model_Loaders.js:129–173 | 반환 객체에 관한 주석과 바깥 함수 종료 행 누락 | 주석의 주장으로 구분하여 추가하고 종료 행 명시 [보완] | 162, 171 |
| Model_Loaders.js:174–201 | accessor 존재도 검사한다고 설명 | 검사 대상을 acc.bufferView와 조회한 bufferView로 정정 [정정] | 175–184 |
| Model_Loaders.js:202–225 | 바깥 함수와 switch 종료 행 누락 | 종료 행 추가 [보완] | 217, 224 |
| Run_Compute_Shader.js:55–77 | uniform 쓰기도 명령 인코더에 기록한다고 설명 | queue.writeBuffer와 인코더 기록을 구분 [정정] | 58–71 |
| Run_Tridiag_Solver.js:1–36 | 주석의 copy-free와 PCR 설명 누락 | 복사 없는 PCR 계수 전달 명시 [보완] | 21, 29 |
| Run_Tridiag_Solver.js:37–67 | 비활성 호출·계수 교대 주석 및 종료 행 누락 | 주석과 실제 실행을 구별하고 블록 종료 행 추가 [보완] | 45–66, 92–93 |
| Run_Tridiag_Solver.js:68–93 | else 조건·교대 주석·종료 행 누락 | else의 조건과 주석의 계수 전달 설명 및 종료 행 추가 [보완] | 37, 70–93 |
| Time_Series.js:1–56 | 채널 교환 주석의 BGRA 가정 누락 | 주석의 가정과 무조건 교환을 구분 [보완] | 37–41 |
| Time_Series.js:57–97 | 1D 설명과 epoch 목적 및 복사 주석 차이 누락 | 각 주석의 설명과 실제 복사 범위 구분 [보완] | 57–59, 72, 81 |
| Time_Series.js:98–129 | 비활성 조건·대입식 및 시간 기준 주석 누락 | 이전 초기화 코드와 동기 초기화·시간 기준 및 종료 행 추가 [보완] | 100–107, 122, 128 |
| Time_Series.js:162–184 | 바깥 함수 종료 행 누락 | 종료 행 추가 [보완] | 184 |
| Wave_Generator.js:62–104 | 캐시 키 일치만 반환 조건으로 설명 | cachedTmaResult 조건 포함 [정정] | 69–71 |
| Wave_Generator.js:191–226 | JONSWAP 반환식의 두 곱셈 항 누락 | 지수 감쇠와 gammaS 거듭제곱 항 및 else 부재 추가 [보완] | 199–201, 218–224 |
| Wave_Generator.js:255–288 | else 부재와 보정 미적용 경로 미표기 | 분기별 기본 방향 유지 설명 추가 [보완] | 256–286 |
| Wave_Generator.js:289–338 | else 없는 순차 if 구조 미표기 | 독립 if와 즉시 반환 명시 [보완] | 296–336 |
| Wave_Generator.js:339–346 | 차감 위치를 양끝 한 격자라고 추정 | 원문의 차감식으로 설명 [정정] | 340 |
| agent_controls.js:212–256 | 모든 포워딩 예외에 catch가 적용되는 설명 | console wrapper에 한정한 catch 범위와 진단 주석 명시 [정정] | 219–254 |
| agent_controls.js:450–482 | UI도 반환한다고 설명 | UI 갱신과 결과 객체 반환으로 구분 [정정] | 474–480 |
| agent_controls.js:719–777 | else 없는 명령 분기 구조 미표기 | 독립 if와 즉시 반환 명시 [보완] | 721–775 |
| constants_load_calc.js:97–135 | 선박 운동의 개발 단계 주석 누락 | initial development 설명 추가 [보완] | 97 |
| constants_load_calc.js:327–356 | 추가 플래그 주석의 셰이더 이름 누락 | MouseClickChange.wgsl을 통한 적용 설명 추가 [보완] | 343 |
| constants_load_calc.js:357–395 | 복수 사각형 부재·빈 배열의 의미 누락 | 선택 설정과 기존 동작 유지 조건 추가 [보완] | 387 |
| constants_load_calc.js:401–414 | 파고 출력에도 시작·종료시간이 있는 설명 | 표면 시작·종료와 파고 관련 세 시각으로 구분 [정정] | 401–412 |
| constants_load_calc.js:401–414 | 출력 트리거 단계와 complete.txt 누락 | 2·3·0 전이와 완료 파일 및 객체 종료 행 추가 [보완] | 402, 407–413 |
| constants_load_calc.js:433–450 | 설정 처리에 관한 주석 문장 누락 | loadConfig와 같은 처리 및 스코프 가정 추가 [보완] | 440–441 |
| constants_load_calc.js:451–488 | 주석 처리한 dt·위도 식과 셀 중심의 이유 누락 | 이전 식과 lat_LL 모서리 기준 설명 추가 [보완] | 452, 478–480 |
| constants_load_calc.js:572–600 | 기존 샘플 수 동작 유지 주석과 분기 구조 누락 | 스칼라 동작 유지 및 독립 if 명시 [보완] | 580–593 |
| constants_load_calc.js:616–634 | 대체 침강속도 식을 주석이라고만 요약 | 대체 계산식과 로그를 원문 인용 [보완] | 631–633 |
| constants_load_calc.js:648–664 | 라벨 픽셀 인덱스를 높이 계산으로 설명 | 위치·폭 설정 및 라벨 인덱스로 정정 [정정] | 649–657 |
| display_parameters.js:68–107 | 모형 표시 사슬의 마지막 else 부재 미표기 | 일치하지 않는 값의 이름 미표시 경로 추가 [보완] | 88–101 |
| display_parameters.js:108–142 | 내부 좌표 기준 주석과 이전 반올림 식 누락 | 상대 좌표 유지 설명과 이전 표시 식 추가 [보완] | 123, 134–135 |
| display_parameters.js:165–198 | 직렬화 실패 때 문자열 처리라고만 설명 | 실패 때 고정 문자열 반환과 비객체 변환 구분 [정정] | 181–190 |
| display_parameters.js:222–245 | 마지막 else 부재 미표기 | 미일치 때 기본 문구 유지 설명 추가 [보완] | 224–242 |
| site.js:1–4 | 문서 주소와 안내 문장의 구체 내용 누락 | 원문 주소와 설정 안내 및 코드 작성 문장 추가 [보완] | 1–4 |
| ../river.html:1–180 | CSS를 포괄적으로만 요약하여 선택자·수치·주석 누락 | CSS 전체 속성값과 주석 및 head/body 경계 인용 [보완] | 9–180 |
| ../river.html:207–243 | 구간 시작 전에 207행 div가 이미 열린 것처럼 표기 | 기존 바깥 요소와 구간 첫 행에서 여는 div 구분 [정정] | 189, 207 |
| ../river.html:551–589 | 오른쪽 클릭 안내의 별표와 Design Mode 조건 누락 | 585행 안내 문장 전체 인용 [보완] | 585 |
| ../river.html:1380–1434 | 세 창 제목·일부 접기 버튼·바깥 컨테이너 종료 인용 누락 | Simulation Window·Parameters·Console 제목과 버튼 및 종료 행 추가 [보완] | 1387–1390, 1406–1409, 1415, 1420–1429, 1433 |
| Model_Loaders.js:202–225 | 템플릿 문자열의 백틱이 Markdown 코드 경계와 합쳐짐 | 문자열 자체의 백틱을 보존하도록 인용 정정 [정정] | 215 |
| agent_controls.js:257–273 | 값 형식 검사 사슬의 else 부재 미표기 | 독립 if와 즉시 반환 명시 [보완] | 258–270 |

정정 12, 보완 45, 이상 없음 99
