# Celeris transect_version/js 전수 검증 — code-7

각 기록의 frontmatter `file:`이 가리키는 원문을 대조했다.
원문은 기록 구간마다 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
코드 실행은 하지 않았다.
행 수는 판독 표의 구간 행 수와 해당 원문 행 수로 구분한다.
정정·보완은 아래 변경 목록의 구간·유형별 항목 수이다.
한 구간에 정정과 보완이 함께 있으면 각 유형에 한 번씩 센다.
이상 없음은 변경하지 않은 대조 완료 구간 행 수이다.
`File_Loader.js.md`의 243–272·433–490 구간에는 정정과 보완이 함께 있다.
기록 경로의 공통 접두사는 `_staging/recovery/read/Celeris/Celeris-WebGPU/transect_version/js/`이다.
아래 기록별 집계는 24개 기록의 115개 구간 행과 원문 5,157행을 포함한다.
모든 기록의 frontmatter와 구간 경계는 작업 전 내용과 일치한다.
모든 원문의 SHA-256은 각 기록의 frontmatter 값과 일치한다.

| 기록 | 상태 | 대조한 구간 행 수 | 대조한 원문 행 수 |
|---|---|---:|---:|
| Config_Pipelines.js.md | 완료 | 6 | 283 |
| Copy_Data_to_Textures.js.md | 완료 | 13 | 555 |
| Create_Textures.js.md | 완료 | 4 | 100 |
| File_Loader.js.md | 완료 | 14 | 527 |
| File_Writer.js.md | 완료 | 19 | 657 |
| Handler_AddDisturbance.js.md | 완료 | 2 | 108 |
| Handler_BoundaryPass.js.md | 완료 | 3 | 148 |
| Handler_CalcMeans.js.md | 완료 | 3 | 187 |
| Handler_CalcWaveHeight.js.md | 완료 | 2 | 93 |
| Handler_Copytxf32_txf16.js.md | 완료 | 2 | 121 |
| Handler_ExtractTimeSeries.js.md | 완료 | 2 | 120 |
| Handler_Model.js.md | 완료 | 2 | 58 |
| Handler_MouseClickChange.js.md | 완료 | 2 | 120 |
| Handler_Pass0.js.md | 완료 | 2 | 69 |
| Handler_Pass1.js.md | 완료 | 2 | 111 |
| Handler_Pass2.js.md | 완료 | 3 | 215 |
| Handler_Pass3.js.md | 완료 | 10 | 572 |
| Handler_PassBreaking.js.md | 완료 | 3 | 135 |
| Handler_Render.js.md | 완료 | 10 | 390 |
| Handler_SedTrans_Pass1.js.md | 완료 | 2 | 124 |
| Handler_SedTrans_Pass3.js.md | 완료 | 3 | 189 |
| Handler_SedTrans_UpdateBottom.js.md | 완료 | 2 | 109 |
| Handler_Skybox.js.md | 완료 | 2 | 57 |
| Handler_Tridiag.js.md | 완료 | 2 | 109 |

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| Config_Pipelines.js.md:22–60 | 깊이 설정 주석의 권장 설명 누락 | 보완: 선택 사항이지만 권장한다는 주석을 추가 | 52 |
| Config_Pipelines.js.md:61–110 | 깊이 설정 주석의 권장 설명 누락 | 보완: 선택 사항이지만 권장한다는 주석을 추가 | 102 |
| Copy_Data_to_Textures.js.md:1–36 | 단일점 섬 제거 주석의 조건·계산·로그와 배열 복사 설명 누락 | 보완: 주석의 초기값·반복·건조 조건·계수 갱신·로그 및 배열 복사 설명을 인용 | 6–35 |
| Copy_Data_to_Textures.js.md:37–90 | 주석 처리된 y방향 검사·경계 설정 누락; else 유무 미표기 | 보완: 실행 코드와 구분하여 y방향 반복·좌표 제한·경계 조건과 대입식을 인용; 조건별 닫힘과 else 없음 명시 | 49–63, 55–57 |
| Copy_Data_to_Textures.js.md:135–179 | 배열 복사·256바이트 패딩 설명 누락 | 보완: 패딩 요구를 설명하는 원문 주석을 추가 | 138–140 |
| Copy_Data_to_Textures.js.md:180–224 | 패딩 주석의 설명 누락 | 보완: 실제 계산식과 구분하여 패딩 주석을 추가 | 183–185 |
| Copy_Data_to_Textures.js.md:225–279 | 배열 복사 설명과 현재 좌표·중심의 차이라는 설명 누락; else 유무 미표기 | 보완: 256바이트 패딩 및 중심 좌표와의 차이 설명을 추가; 조건별 닫힘과 else 없음 명시 | 228–239, 245–247 |
| Copy_Data_to_Textures.js.md:280–325 | 초기조건이라는 주석 표현과 배열 복사 설명 누락 | 보완: 초기조건 배치와 256바이트 패딩 주석을 추가 | 281–285 |
| Copy_Data_to_Textures.js.md:326–389 | 배열 복사와 계수 계산의 주석 설명 일부 누락 | 보완: 256바이트 패딩과 인접 수심·1차 미분·계수 계산 주석을 추가 | 329–376 |
| Copy_Data_to_Textures.js.md:414–477 | y방향 코드와 다른 주석의 coefMatx·x방향 표기 누락 | 보완: 주석을 그대로 보존하고 실제 코드의 y방향·coefMaty와 구분 | 415–464 |
| Copy_Data_to_Textures.js.md:502–520 | 주석의 2D·3D 설명과 이미지 로드 설명 누락; else 유무 미표기 | 보완: 주석 설명을 추가하고 실제 분기 조건과 구분; 조건별 닫힘과 else 없음 명시 | 504–512, 508–510 |
| File_Loader.js.md:1–35 | else 유무 미표기 | 보완: 비정상 응답의 else 없음과 오류 출력·null 반환을 명시 | 25–28 |
| File_Loader.js.md:36–84 | 검사 실패 시 반환과 else 유무가 요약에 없음 | 보완: 열 수·숫자 검사 실패의 오류 출력·null 반환·else 없음을 명시 | 43–53 |
| File_Loader.js.md:85–144 | 오류 처리 요약·else 유무·depth 주석 누락 | 보완: 요청·형식·NaN 오류의 출력·null 반환·else 없음과 주석의 depth 표현을 추가 | 102–135 |
| File_Loader.js.md:145–205 | 오류 처리 요약·else 유무·depth 주석 누락 | 보완: 요청·형식·NaN 오류의 출력·null 반환·else 없음과 주석의 depth 표현을 추가 | 162–195 |
| File_Loader.js.md:206–242 | else 유무와 예외 전 오류 출력 미표기 | 보완: 비정상 응답의 예외 및 파싱 오류의 출력 후 재던짐을 명시 | 220–239 |
| File_Loader.js.md:243–272 | 실패 처리 요약과 함수 주석의 텍스처 설명 누락 | 보완: 로그·null 반환·else 없음 및 주석과 실제 이미지 반환을 구분 | 249–270 |
| File_Loader.js.md:273–315 | else 유무·위도 라디안 변환이라는 주석·컨테이너 크기 설명 누락 | 보완: 분기와 주석의 표현을 실제 식과 구분하여 추가 | 278–304 |
| File_Loader.js.md:316–342 | 추가 매개변수·위성 보기 주석 설명 누락 | 보완: 주석의 추가·해제 안내와 실행 코드의 satellite 설정을 구분 | 332–338 |
| File_Loader.js.md:433–490 | 실제 네 모서리 반환 | 정정: 좌하단·우상단 두 모서리의 위도·경도 반환 | 478–489 |
| File_Loader.js.md:398–432 | y 오프셋의 거리 설명과 경도 선형 계산 설명 누락 | 보완: 좌하단 간 거리의 높이 정규화 및 경도 선형 계산 설명 추가 | 414–418 |
| File_Loader.js.md:433–490 | 이미지 높이 전체에서 도/픽셀을 일정하게 가정한다는 설명 등 누락 | 보완: 타일 배율·경도 도/픽셀·위도 비선형성과 단순화 가정 주석을 추가 | 437–471 |
| File_Loader.js.md:491–509 | 검사 실패 시 예외·else 유무 미표기 | 보완: 실패 응답의 상태 문자열 포함 예외와 else 없음을 명시 | 494–496 |
| File_Writer.js.md:1–48 | 저장 전 필요에 따라 변환할 수 있다는 설명 누락 | 보완: Float32Array 뷰 생성 예시를 포함한 저장 전 변환 주석 추가 | 46–46 |
| File_Writer.js.md:49–68 | 주석의 2차원 배열 설명·채널 대입식 누락 | 보완: 실제 1차원 배열과 주석의 표현을 구분하고 비실행 대입식 추가 | 52–62 |
| File_Writer.js.md:69–102 | 배열 반환 전제·지리 맥락에 맞춘 메타데이터 조정 안내 누락 | 보완: 배열 또는 typed array 전제와 메타데이터 조정 안내 추가 | 71–74 |
| File_Writer.js.md:125–169 | 첫 파일·비동기 및 검증·후처리 안내 누락; 오류 처리 종류·else 유무 미표기 | 보완: 주석에 적힌 입력·검증·후처리 안내 추가; JSON 처리·파일 미선택 오류 출력과 키 검사 else 없음 명시 | 126–166, 143–162 |
| File_Writer.js.md:170–214 | RGBA8 전제와 즉시 복제 이유 누락 | 보완: RGBA8 호환성 전제 및 detached buffer 오류 방지 설명 추가 | 186–212 |
| File_Writer.js.md:215–251 | BGRA 입력 설명과 색 공간 변환 문제 회피 목적 누락 | 보완: BGRA→RGBA 순서 및 컨텍스트 설정의 주석상 목적 추가 | 215–228 |
| File_Writer.js.md:252–296 | RGBA8 전제와 detached buffer 오류 방지 설명 누락 | 보완: 호환성 전제와 복제 이유의 주석 추가 | 268–294 |
| File_Writer.js.md:297–329 | 입력 BGRA와 출력 RGBA 순서 미표기 | 보완: 적색·청색 교환의 입력·출력 채널 순서 추가 | 297–299 |
| File_Writer.js.md:330–368 | 필요한 경우라는 주석의 한정 누락 | 보완: 주석의 한정과 실제 무조건 변환 루프를 구분 | 357–357 |
| File_Writer.js.md:369–394 | SharedArrayBuffer 제약의 상세·변환 필요 가능성 누락; 실패 시 반환만 요약 | 보완: 대부분의 브라우저·서버에 보안상 기본 제공되지 않는다는 주석 및 형식 변환 가능성 추가; 오류 출력 후 반환하는 순서를 명시 | 369–388, 379–392 |
| File_Writer.js.md:395–413 | 동영상 생성 실패의 출력·반환 요약 누락 | 보완: 생성 실패 시 오류 출력 후 반환을 명시 | 399–402 |
| File_Writer.js.md:553–574 | else 유무 미표기 | 보완: 첫 출력 분기의 닫힘과 else 없음을 명시 | 558–573 |
| File_Writer.js.md:575–612 | 독립 분기와 else 유무 미표기 | 보완: 여섯 출력 플래그가 독립적이며 else가 없음을 명시 | 575–609 |
| File_Writer.js.md:613–657 | 오류 처리 및 대기 이유 일부 누락 | 보완: Promise 거부·반환·오류 출력·else 없음과 다운로드 시작 대기 이유 추가 | 624–648 |
| Handler_AddDisturbance.js.md:1–71 | 유니폼 매개변수 예시와 binding 3 주석의 2nd 표기 누락 | 보완: 시간 등 매개변수 예시 및 실제 binding·visibility와 다른 주석을 보존 | 6–32 |
| Handler_BoundaryPass.js.md:1–57 | 시간 등 유니폼 매개변수 예시 누락 | 보완: 유니폼 주석의 매개변수 예시를 추가 | 7–7 |
| Handler_CalcMeans.js.md:1–73 | 매개변수 예시·fragment 표기·쓰기 설명 누락 | 보완: 주석의 역할 설명을 실제 선언과 구분하여 추가 | 6–66 |
| Handler_CalcMeans.js.md:74–126 | 12번 주석의 계산 결과 쓰기 설명 누락 | 보완: 주석의 쓰기 설명을 실제 읽기 텍스처 선언과 구분 | 115–115 |
| Handler_CalcWaveHeight.js.md:1–60 | 시간 등 매개변수 예시 누락 | 보완: 유니폼 주석의 매개변수 예시 추가 | 6–6 |
| Handler_Copytxf32_txf16.js.md:1–80 | 매개변수 예시·fragment 주석 누락 | 보완: 매개변수 예시와 fragment 표기를 실제 COMPUTE 선언과 구분 | 7–68 |
| Handler_ExtractTimeSeries.js.md:1–79 | 매개변수 예시·fragment 주석 누락 | 보완: 매개변수 예시와 fragment 표기를 실제 COMPUTE 선언과 구분 | 6–57 |
| Handler_Model.js.md:1–33 | 시간 등 매개변수 예시 누락 | 보완: 유니폼 주석의 매개변수 예시 추가 | 6–6 |
| Handler_MouseClickChange.js.md:1–79 | 시간 등 매개변수 예시 누락 | 보완: 유니폼 주석의 매개변수 예시 추가 | 6–6 |
| Handler_Pass0.js.md:1–44 | 시간 등 매개변수 예시 누락 | 보완: 유니폼 주석의 매개변수 예시 추가 | 7–7 |
| Handler_Pass1.js.md:1–74 | 매개변수 예시와 입력 텍스처의 fragment 설명 누락 | 보완: 매개변수 예시 및 주석과 실제 COMPUTE 선언의 차이 추가 | 7–22 |
| Handler_Model.js.md:34–58 | 샘플러를 선형 샘플러로 단정 | 정정: 생성 설정을 확인하지 않은 샘플러의 성질 대신 실제 인수 이름을 명시 | 35–51 |
| Handler_Pass0.js.md:45–69 | uniformBuffer까지 뷰인 것으로 읽히는 서술 | 정정: 버퍼 자원과 텍스처 뷰를 구분 | 49–65 |
| Handler_Pass1.js.md:75–111 | uniformBuffer까지 뷰인 것으로 읽히는 서술 | 정정: 버퍼 자원과 텍스처 뷰를 구분 | 79–107 |
| Handler_Pass2.js.md:1–65 | 시간 등 매개변수 예시 누락 | 보완: 유니폼 주석의 매개변수 예시 추가 | 7 |
| Handler_Pass3.js.md:1–84 | 매개변수 또는 fragment 샘플링 주석 설명 누락 | 보완: 원문 주석을 COMPUTE 선언과 구분하여 추가 | 7–77 |
| Handler_Pass3.js.md:85–160 | 매개변수 또는 fragment 샘플링 주석 설명 누락 | 보완: 원문 주석을 COMPUTE 선언과 구분하여 추가 | 86–113 |
| Handler_Pass3.js.md:161–201 | 매개변수 또는 fragment 샘플링 주석 설명 누락 | 보완: 원문 주석을 COMPUTE 선언과 구분하여 추가 | 162–189 |
| Handler_Pass3.js.md:202–255 | 6–10번을 모두 기울기 이력으로 요약 | 정정: 예측 기울기를 포함하는 실제 자원 이름을 각각 명시 | 233–250 |
| Handler_Pass3.js.md:298–377 | 매개변수·읽기 텍스처 역할·7번 주석의 6th 표기 누락 | 보완: 주석의 매개변수·단계·쓰기 설명과 binding 7 번호 불일치 추가 | 302–365 |
| Handler_Pass3.js.md:424–478 | 매개변수·읽기 텍스처의 fragment·쓰기 주석 설명 누락 | 보완: 원문 주석을 실제 단계·읽기 텍스처 선언과 구분 | 428–461 |
| Handler_Pass3.js.md:479–522 | 9번의 fragment 샘플링 주석 설명 누락 | 보완: 주석과 실제 COMPUTE 선언의 차이를 추가 | 510–510 |
| Handler_PassBreaking.js.md:1–65 | 시간 등 매개변수 예시 누락 | 보완: 유니폼 주석의 매개변수 예시 추가 | 7 |
| Handler_PassBreaking.js.md:91–135 | uniformBuffer까지 뷰인 것으로 읽히는 서술 | 정정: 버퍼 자원과 텍스처 뷰를 구분 | 95–131 |
| Handler_Render.js.md:1–74 | 시간 등 매개변수 예시 누락 | 보완: 유니폼 주석의 매개변수 예시 추가 | 7–7 |
| Handler_Render.js.md:75–145 | binding 8–14 주석 번호 불일치 누락 | 보완: 실제 binding 8–14와 주석의 9th–15th를 구분 | 76–129 |
| Handler_Render.js.md:146–178 | 18번 필터 샘플링 설명 누락 | 보완: 18번 텍스처 주석의 필터 샘플링 설명 추가 | 165–165 |
| Handler_Render.js.md:266–295 | 로고 분기의 else 유무와 글꼴 사슬 구별 미표기 | 보완: 로고 if의 닫힘·else 없음과 별도 글꼴 if/else 사슬을 구분 | 267–286 |
| Handler_SedTrans_Pass1.js.md:1–83 | 매개변수 예시 또는 입력 텍스처의 fragment 설명 누락 | 보완: 매개변수 예시 및 주석과 실제 선언의 차이 추가 | 7–31 |
| Handler_SedTrans_Pass3.js.md:1–83 | 매개변수 예시 또는 입력 텍스처의 fragment 설명 누락 | 보완: 매개변수 예시 및 주석과 실제 선언의 차이 추가 | 7–7 |
| Handler_SedTrans_Pass1.js.md:84–124 | uniformBuffer까지 뷰인 것으로 읽히는 서술 | 정정: 버퍼 자원과 텍스처 뷰를 구분 | 88–120 |
| Handler_SedTrans_Pass3.js.md:129–189 | 4–6번을 모두 기울기 이력으로 요약 | 정정: 예측 기울기를 포함하는 실제 자원 이름을 각각 명시 | 152–161 |
| Handler_SedTrans_UpdateBottom.js.md:1–72 | 매개변수 예시 또는 fragment 주석 설명 누락 | 보완: 누락한 원문 주석 설명을 실제 선언과 구분하여 추가 | 7–40 |
| Handler_Skybox.js.md:1–33 | 매개변수 예시 또는 fragment 주석 설명 누락 | 보완: 누락한 원문 주석 설명을 실제 선언과 구분하여 추가 | 6–6 |
| Handler_Tridiag.js.md:1–72 | 매개변수 예시 또는 fragment 주석 설명 누락 | 보완: 누락한 원문 주석 설명을 실제 선언과 구분하여 추가 | 7–7 |
| Handler_SedTrans_UpdateBottom.js.md:73–109 | uniformBuffer까지 뷰인 것으로 읽히는 서술 | 정정: 버퍼 자원과 텍스처 뷰를 구분 | 77–105 |
| Handler_Tridiag.js.md:73–109 | uniformBuffer까지 뷰인 것으로 읽히는 서술 | 정정: 버퍼 자원과 텍스처 뷰를 구분 | 77–105 |
| File_Loader.js.md:243–272 | Blob 반환 뒤 표시 설정 변경으로 서술 | 정정: 표시 설정을 2로 변경한 뒤 Blob을 반환하는 순서로 정정 | 254–258 |
| File_Writer.js.md:514–552 | 완료 콜백이 다운로드 후 렌더를 시작하는 것으로 서술 | 정정: 콜백의 다운로드와 콜백 밖 render 호출을 구분 | 541–550 |

정정 12, 보완 64, 이상 없음 41
