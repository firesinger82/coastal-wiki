# Celeris code-2 — 11-04 전수 검증

상태: 완료.

사용자가 지정한 19개 기록의 구간 행 138개를 대조했다.
각 기록의 frontmatter `file:`이 가리키는 원문 5,089행을 대조했다.
각 구간마다 `nl -ba <원문> | sed -n 'A,Bp'`로 원문을 열었다.
각 sed 범위는 200행 이하였다.
구간 표 뒤의 코드 사실 항목도 원문과 대조했다.
정정·보완은 발견한 구간에서 바로 적용했다.
원문 SHA-256과 행 수는 각 기록의 frontmatter와 일치했다.
모델은 실행하지 않았다.
원문·노트·git은 수정하지 않았다.

기록별 대조 결과의 행 수는 각 기록의 구간 표와 원문에서 셌다.
정정·보완 수는 아래 변경 목록의 항목 수다.
같은 구간에 별도 변경 항목이 있으면 각각 센다.
이상 없음 수는 정정·보완하지 않은 구간 행 수다.
코드 사실 항목의 정정은 변경 목록에 별도로 센다.

| 기록 | 대조한 구간 행 수 | 대조한 원문 행 수 | 정정 | 보완 | 이상 없음 | 상태 |
|---|---:|---:|---:|---:|---:|---|
| [Copy_Data_to_Textures.js.md](../Celeris-WebGPU/js/Copy_Data_to_Textures.js.md) | 16 | 642 | 1 | 7 | 9 | 완료 |
| [Create_Textures.js.md](../Celeris-WebGPU/js/Create_Textures.js.md) | 8 | 100 | 0 | 0 | 8 | 완료 |
| [File_Loader.js.md](../Celeris-WebGPU/js/File_Loader.js.md) | 22 | 819 | 1 | 8 | 14 | 완료 |
| [File_Writer.js.md](../Celeris-WebGPU/js/File_Writer.js.md) | 25 | 848 | 4 | 10 | 12 | 완료 |
| [Handler_AddDisturbance.js.md](../Celeris-WebGPU/js/Handler_AddDisturbance.js.md) | 3 | 121 | 0 | 2 | 1 | 완료 |
| [Handler_BoundaryPass.js.md](../Celeris-WebGPU/js/Handler_BoundaryPass.js.md) | 5 | 206 | 0 | 4 | 2 | 완료 |
| [Handler_CalcMeans.js.md](../Celeris-WebGPU/js/Handler_CalcMeans.js.md) | 5 | 200 | 0 | 5 | 2 | 완료 |
| [Handler_CalcWaveHeight.js.md](../Celeris-WebGPU/js/Handler_CalcWaveHeight.js.md) | 3 | 93 | 0 | 2 | 1 | 완료 |
| [Handler_Copytxf32_txf16.js.md](../Celeris-WebGPU/js/Handler_Copytxf32_txf16.js.md) | 3 | 134 | 0 | 2 | 1 | 완료 |
| [Handler_ExtractNestedBoundaryTimeSeries.js.md](../Celeris-WebGPU/js/Handler_ExtractNestedBoundaryTimeSeries.js.md) | 3 | 109 | 0 | 2 | 1 | 완료 |
| [Handler_ExtractTimeSeries.js.md](../Celeris-WebGPU/js/Handler_ExtractTimeSeries.js.md) | 3 | 133 | 0 | 2 | 1 | 완료 |
| [Handler_Model.js.md](../Celeris-WebGPU/js/Handler_Model.js.md) | 2 | 58 | 0 | 1 | 1 | 완료 |
| [Handler_MouseClickChange.js.md](../Celeris-WebGPU/js/Handler_MouseClickChange.js.md) | 3 | 120 | 0 | 2 | 1 | 완료 |
| [Handler_Pass0.js.md](../Celeris-WebGPU/js/Handler_Pass0.js.md) | 2 | 69 | 0 | 1 | 1 | 완료 |
| [Handler_Pass1.js.md](../Celeris-WebGPU/js/Handler_Pass1.js.md) | 3 | 111 | 0 | 2 | 1 | 완료 |
| [Handler_Pass2.js.md](../Celeris-WebGPU/js/Handler_Pass2.js.md) | 5 | 228 | 0 | 4 | 2 | 완료 |
| [Handler_Pass3.js.md](../Celeris-WebGPU/js/Handler_Pass3.js.md) | 12 | 572 | 0 | 10 | 4 | 완료 |
| [Handler_PassBreaking.js.md](../Celeris-WebGPU/js/Handler_PassBreaking.js.md) | 3 | 135 | 0 | 2 | 1 | 완료 |
| [Handler_Render.js.md](../Celeris-WebGPU/js/Handler_Render.js.md) | 12 | 391 | 0 | 9 | 5 | 완료 |

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| Copy_Data_to_Textures.js.md:37–90 | 반경 3의 이웃 | 정정: x·y 각각 ±3의 사각 이웃 | 50–53 |
| Copy_Data_to_Textures.js.md:37–90 | 주석 처리된 경계 검사 누락 | 보완: 비활성 경계 조건과 대입 추가 | 61–63 |
| Copy_Data_to_Textures.js.md:190–241 | 잔여 채널과 매핑 생략 설명 누락 | 보완: B·A와 패딩은 0이며 CPU에서 직접 쓰는 방식 명시 | 207–227 |
| Copy_Data_to_Textures.js.md:242–304 | 시험 초기조건 식과 else 부재 누락 | 보완: 비활성 dx·dy·sigma 식 및 else 없는 분기 명시 | 256–272 |
| Copy_Data_to_Textures.js.md:350–383 | 이전 위도 식을 주석 처리했다고만 기록 | 보완: 비활성 중심·북면·남면 위도식 인용 | 362–364 |
| Copy_Data_to_Textures.js.md:497–561 | y 함수의 원문 주석 불일치 누락 | 보완: 주석의 coefMatx·x direction과 실행 코드의 y 인덱스를 구분 | 498, 527–530 |
| Copy_Data_to_Textures.js.md:585–603 | 주석의 2D·3D 구분 설명 누락 | 보완: 주석 설명과 실제 depth 검사 구분 | 587–593 |
| Copy_Data_to_Textures.js.md:636–642 | export 주석의 grid_type 조건 누락 | 보완: 구면 메트릭 도우미 주석의 조건 인용 | 639 |
| File_Loader.js.md:340–377 | 첫 행 허용 형식과 이전 파싱식 누락 | 보완: 라벨 포함 수량 행 설명과 비활성 식 추가 | 356–358 |
| File_Loader.js.md:445–489 | 업로드 지원 범위 주석 누락 | 보완: 서버 제공 웹 루트 밖의 업로드 설명 추가 | 446, 476 |
| File_Loader.js.md:490–513 | 공통 시각 저장 조건과 중첩 시뮬레이션 시각 의미 누락 | 보완: 바깥 루프 조건·닫힘 및 sharedTimes 조건과 주석 추가 | 462, 500–508 |
| File_Loader.js.md:545–586 | latRad 반환값의 마지막 2 나눗셈 설명 누락 | 보완: ±π 제한 후 2로 나누는 순서 추가 | 553 |
| File_Loader.js.md:587–614 | API 키 주석과 추가 매개변수 예시 누락 | 보완: 배포 시 키 제거·입력화 주석 및 위성 보기 예시 추가 | 590, 607–609 |
| File_Loader.js.md:615–653 | 디코딩 실패 처리의 주석상 목적 누락 | 보완: 지도 없이 초기화 계속 및 미완료 방지라는 주석 설명 추가 | 636, 641–645 |
| File_Loader.js.md:725–781 | 위도당 픽셀 근사값 | 정정: 픽셀당 위도 근사값 | 762–764 |
| File_Loader.js.md:725–781 | 위도 환산 단순화 가정 누락 | 보완: 영상 높이 전체에서 픽셀당 도수가 일정하다는 주석 추가 | 729, 746, 763 |
| File_Writer.js.md:38–71 | GeoTIFF 메타데이터 조정 주석 누락 | 보완: 배열 반환 가정과 사용 맥락별 메타데이터 조정 설명 추가 | 40–43 |
| File_Writer.js.md:124–138 | 자료형·범위 검사 주석 | 정정: 접근 가능성·예상 객체 구조·구조/내용 불일치 처리 및 UI 갱신·재초기화 예시 주석 | 125–135 |
| File_Writer.js.md:139–186 | 텍스처 형식 가정과 복제 이유 누락 | 보완: RGBA8 가정·detached buffer 오류 방지 주석 추가 | 155, 181 |
| File_Writer.js.md:187–223 | BGRA 형식 및 색 공간 설정 이유 누락 | 보완: BGRA에서 RGBA로 교환한다는 주석과 색 공간 변환 문제 방지 목적 명시 | 187–200 |
| File_Writer.js.md:224–268 | 읽기 형식 가정과 복제 이유 누락 | 보완: RGBA8 가정·detached buffer 오류 방지 주석 추가 | 240, 266 |
| File_Writer.js.md:269–284 | 반환 앞에 unmap·destroy가 없음 | 정정: READ 매핑 이후에는 없고 초기 매핑 뒤 unmap은 있음 | 238, 261–282 |
| File_Writer.js.md:343–388 | FFmpeg 제약과 frameData 가정 축약 | 보완: 주석의 불확실성·보안상 기본 미제공 설명 및 변환 필요 가능성 추가 | 343–345, 362 |
| File_Writer.js.md:492–530 | finished 이벤트에서 다운로드 후 gif.render 호출로 읽히는 순서 | 정정: finished 콜백 등록 후 render 호출, 이벤트 발생 때 다운로드 | 519–528 |
| File_Writer.js.md:559–598 | 독립 if의 else 부재 미표기 | 보완: 여섯 조건은 각각 독립 if이며 else 없음 | 559–593 |
| File_Writer.js.md:678–708 | 전역 임계값만 쓰던 이전 식 누락 | 보완: 비활성 임계값 대입식 추가 | 686–688 |
| File_Writer.js.md:709–757 | 이전 시작시각 함수 내부 조건·형식과 이전 루프 누락 | 보완: NaN 유지 삼항식·ASCII 단일 값 및 이전 메타데이터·루프 인용 | 709–741 |
| File_Writer.js.md:758–800 | 이전 접두사 식과 다운로드 루프 인용 누락 | 보완: 비활성 전역 접두사·경계 순회·다운로드 인수 추가 | 765–800 |
| File_Writer.js.md:801–842 | 이전 조건·식 및 별도 시작시각 파일 생략 이유 누락 | 보완: 비활성 임계값·시각·조건·함수 인수 및 첫 기록 시각 설명 추가 | 810–834 |
| File_Writer.js.md:코드 사실 261–282 | 함수 안에 unmap 없음 | 정정: READ 매핑 이후에는 없지만 238행 초기 unmap은 있음 | 238, 261–282 |
| Handler_AddDisturbance.js.md:1–38 | 머리말·바인딩 주석의 원문 설명 누락 | 보완: 다른 파일명 머리말과 fragment 표기·번호 불일치 구분 | 1, 6, 12, 21, 30 |
| Handler_AddDisturbance.js.md:39–80 | 시작 위치의 바인딩 객체와 주석 맥락 누락 | 보완: 38–47행 객체 내부 및 fragment 주석과 COMPUTE 선언 구분 | 38–47, 69–71 |
| Handler_BoundaryPass.js.md:1–48 | uniform 및 입력 주석 설명 누락 | 보완: 시간 등의 매개변수와 fragment 표기 구분 | 7, 13–42 |
| Handler_BoundaryPass.js.md:49–96 | 구간 시작 객체 및 fragment 주석 누락 | 보완: 48–57행 객체 내부와 binding 7·9 주석의 단계 구분 | 48–57, 69–90 |
| Handler_BoundaryPass.js.md:97–137 | 경계 시계열 성분 주석 누락 | 보완: 네 경계의 eta/hu/hv 성분 명시 | 98, 107, 116, 125 |
| Handler_CalcMeans.js.md:1–56 | 시간 매개변수용 uniform 주석 누락 | 보완: 주석상 uniform 예시 추가 | 6 |
| Handler_CalcMeans.js.md:57–104 | 구간 시작의 바인딩 객체 누락 | 보완: 56–64행 객체 내부 명시 | 56–64 |
| Handler_CalcMeans.js.md:105–135 | 구간 시작의 바인딩 객체 누락 | 보완: 104–113행 객체 내부 명시 | 104–113 |
| Handler_CalcMeans.js.md:1–56 | 입력 텍스처 주석의 단계 불일치 누락 | 보완: fragment 주석과 COMPUTE 선언 구분 | 12–50 |
| Handler_CalcWaveHeight.js.md:1–38 | uniform의 주석상 예시 누락 | 보완: 시간 등의 매개변수용 설명 추가 | 6 |
| Handler_CalcWaveHeight.js.md:39–60 | 시작 위치의 바인딩 객체 누락 | 보완: 38–46행 객체 내부 명시 | 38–46 |
| Handler_Copytxf32_txf16.js.md:1–39 | uniform 및 입력 주석 누락 | 보완: 시간 매개변수 예시·fragment 주석 명시 | 7, 13–33 |
| Handler_Copytxf32_txf16.js.md:40–89 | 시작 객체와 입력 주석 누락 | 보완: 39–48행 객체 내부 및 fragment 주석 명시 | 39–79 |
| Handler_ExtractNestedBoundaryTimeSeries.js.md:39–68 | 시작 객체 및 건조 경계 표본의 처리값 누락 | 보완: 38–46행 객체 내부와 0 처리 주석 명시 | 38–56 |
| Handler_ExtractNestedBoundaryTimeSeries.js.md:69–109 | 건조 셀 출력 성분·값 주석 누락 | 보완: eta/hu/hv를 0으로 출력한다는 주석 추가 | 70, 101 |
| Handler_ExtractTimeSeries.js.md:1–38 | uniform·입력 주석 누락 | 보완: 시간 매개변수 예시 및 fragment 주석 추가 | 6, 12–32 |
| Handler_ExtractTimeSeries.js.md:39–88 | 시작 객체·입력 주석 누락 | 보완: 38–46행 객체 내부와 fragment 주석 추가 | 38–78 |
| Handler_Model.js.md:1–33 | uniform 예시 및 linear sampler 주석 누락 | 보완: 시간 등의 매개변수·선형 샘플러 설명 추가 | 6, 22 |
| Handler_MouseClickChange.js.md:1–38 | uniform·입력 주석 누락 | 보완: 시간 매개변수 예시 및 fragment 주석 추가 | 6, 12–32 |
| Handler_MouseClickChange.js.md:39–79 | 시작 객체·입력 주석 누락 | 보완: 38–46행 객체 내부와 fragment 주석 추가 | 38–50 |
| Handler_Pass0.js.md:1–44 | uniform·입력 주석 누락 | 보완: 시간 매개변수 예시 및 fragment 주석 추가 | 7, 13–24 |
| Handler_Pass1.js.md:1–40 | uniform·입력 주석 누락 | 보완: 시간 매개변수 예시 및 fragment 주석 추가 | 7, 13–24 |
| Handler_Pass1.js.md:41–74 | 시작 위치 객체 누락 | 보완: 40–49행 binding 4 객체 내부 명시 | 40–49 |
| Handler_Pass2.js.md:1–57 | uniform·입력 주석 누락 | 보완: 시간 매개변수 예시 및 fragment 주석 추가 | 7, 13–51 |
| Handler_Pass2.js.md:58–113 | 시작 위치 객체·입력 주석 누락 | 보완: 57–65행 객체 내부와 fragment 주석 명시 | 57–107 |
| Handler_Pass2.js.md:114–155 | 시작 위치 객체·입력 주석 누락 | 보완: 113–121행 객체 내부와 fragment 주석 명시 | 113–145 |
| Handler_Pass3.js.md:1–58 | uniform·입력 주석 누락 | 보완: 시간 매개변수 예시 및 fragment 주석 추가 | 7, 13–52 |
| Handler_Pass3.js.md:59–121 | 시작 객체·입력 주석 누락 | 보완: 58–66행 객체 내부와 fragment 주석 명시 | 58–115 |
| Handler_Pass3.js.md:122–161 | 시작 위치 객체 누락 | 보완: 121–130행 binding 13 객체 내부 명시 | 121–130 |
| Handler_Pass3.js.md:162–201 | 시작 객체·입력 주석 누락 | 보완: 161–169행 객체 내부와 fragment 주석 추가 | 161–191 |
| Handler_Pass3.js.md:298–343 | uniform·입력 주석 누락 | 보완: 시간 매개변수 예시와 fragment 주석 추가 | 302, 308–337 |
| Handler_Pass3.js.md:344–377 | 시작 객체·주석 번호 불일치 누락 | 보완: 343–352행 객체 내부와 binding 7의 6th 주석 구분 | 343–365 |
| Handler_Pass3.js.md:424–469 | uniform·입력 주석 누락 | 보완: 시간 매개변수 예시와 fragment 주석 추가 | 428, 434–463 |
| Handler_Pass3.js.md:470–522 | 시작 객체·binding 9 주석 누락 | 보완: 469–478행 객체 내부와 fragment 주석 추가 | 469–478, 510–512 |
| Handler_PassBreaking.js.md:1–39 | uniform의 주석상 예시 누락 | 보완: 시간 등의 매개변수용 설명 추가 | 7 |
| Handler_PassBreaking.js.md:40–90 | 시작 위치 객체 누락 | 보완: 39–47행 binding 4 객체 내부 명시 | 39–47 |
| Handler_Render.js.md:1–39 | uniform 예시 주석 누락 | 보완: 시간 등의 매개변수용 설명 추가 | 7 |
| Handler_Render.js.md:40–102 | 시작 객체·주석 번호 불일치 누락 | 보완: 39–47행 객체 내부 및 binding 8·9·10 주석 번호 추가 | 39–47, 76, 85, 94 |
| Handler_Render.js.md:103–146 | 시작 객체·주석 번호 불일치 누락 | 보완: 102–110행 객체 내부 및 binding 11–14 주석 번호 추가 | 102–110, 112, 121, 129 |
| Handler_Render.js.md:147–178 | 시작 객체·선형/필터 표본화 주석 누락 | 보완: 146–155행 객체 내부와 binding 17·18 설명 추가 | 146–165 |
| File_Loader.js.md:378–397 | 바깥 함수의 닫힘 위치 누락 | 보완: parseBoundaryTimeSeriesText가 431행에서 닫힘 명시 | 350, 431 |
| Handler_BoundaryPass.js.md:49–96 | 바깥 생성 객체의 닫힘 위치 누락 | 보완: entries 134행·생성 호출 135행·함수 136행 닫힘 명시 | 134–136 |
| Handler_CalcMeans.js.md:57–104 | 바깥 생성 객체의 닫힘 위치 누락 | 보완: entries 132행·생성 호출 133행·함수 134행 닫힘 명시 | 132–134 |
| Handler_Pass2.js.md:58–113 | 바깥 생성 객체의 닫힘 위치 누락 | 보완: entries 151행·생성 호출 152행·함수 153행 닫힘 명시 | 151–153 |
| Handler_Pass3.js.md:59–121 | 바깥 생성 객체의 닫힘 위치 누락 | 보완: entries 197행·생성 호출 198행·함수 199행 닫힘 명시 | 197–199 |
| Handler_Pass3.js.md:122–161 | 바깥 생성 객체의 닫힘 위치 누락 | 보완: entries 197행·생성 호출 198행·함수 199행 닫힘 명시 | 197–199 |
| Handler_Render.js.md:40–102 | 바깥 생성 객체의 닫힘 위치 누락 | 보완: entries 174행·생성 호출 175행·함수 176행 닫힘 명시 | 174–176 |
| Handler_Render.js.md:103–146 | 바깥 생성 객체의 닫힘 위치 누락 | 보완: entries 174행·생성 호출 175행·함수 176행 닫힘 명시 | 174–176 |
| Handler_Render.js.md:296–325 | 바깥 함수의 닫힘 위치 누락 | 보완: update_colorbar가 381행에서 닫힘 명시 | 266, 381 |
| Handler_Render.js.md:326–346 | 바깥 함수의 닫힘 위치 누락 | 보완: update_colorbar가 381행에서 닫힘 명시 | 266, 381 |
| Handler_Render.js.md:347–377 | 바깥 함수의 닫힘 위치 누락 | 보완: update_colorbar가 381행에서 닫힘 명시 | 266, 381 |

인용문 검사에서 행 번호가 붙은 백틱 인용 4,146개가 해당 원문 행과 일치했다.
이 검사는 표의 파이프 이스케이프와 인용 양끝 공백을 정규화했다.
File_Loader.js 590행의 API 키는 원문과 대조했으며 기존 기록처럼 문자열 자체를 재기재하지 않았다.

정정 6, 보완 75, 이상 없음 68
