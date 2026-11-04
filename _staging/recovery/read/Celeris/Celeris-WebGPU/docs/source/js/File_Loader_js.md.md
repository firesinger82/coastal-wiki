---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/File_Loader_js.md
lines: 43
sha256: f79baa9a8a2d4616866c9b6f395cc78cfdafbd9cee6a2c4a983391ad055d7245
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# File_Loader_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/File_Loader.js`

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 시나리오·영상을 CPU 자료로 읽는 모듈이다(1–7). 공백 구분 격자는 `WIDTH x HEIGHT`다. `loadDepthSurface()`는 사용자 입력이 없으면 예제 `bathy.txt`를 읽고 바깥 `three cells`를 인접 내부 값으로 평탄화한다(11). 선택 `loadInitCondSurface()`, `loadFrictionSurface()`, `loadHardBottomSurface()`는 `Copy_Data_to_Textures.js`용 수치 격자를 반환한다(13–19). 모듈은 번들 예제 자산과 사용자 선택 파일을 모두 처리한다(7). CPU 구조체는 이후 GPU 텍스처로 복사된다(7). 외곽 평탄화는 경계/ghost-cell 동작의 가장자리 자료 민감도를 줄인다(11). [11-04 전수 검증 보완] |
| 21–30 | `loadWaveData()`는 `waves.txt`의 첫 행 파랑 개수와 후속 매개변수를 읽는다(23). `loadBoundaryTimeSeriesData()`는 경계형 `5`의 `ts_west_file`, `ts_east_file`, `ts_south_file` 및 측면 키를 사용하며 업로드가 설정 경로보다 우선한다. 관측점 수·위치·`time eta1 hu1 hv1 ...`를 읽고 활성 파일은 같은 시간 벡터여야 한다. 첫 시간을 `calc_constants.start_time_shift`로 복사해 자식 격자가 부모/전역 시계를 쓴다(25). 로컬 또는 Google Static Maps 영상을 로드하고 Mercator식 스케일·오프셋을 계산한다(27). HTTP·비영상·디코딩 오류를 즉시 보고해 초기화가 overlay 없이 계속할 수 있게 한다(29). 파랑 매개변수는 boundary shader가 소비한다(23). `Start Here` 패널의 업로드는 서버 예제 트리 밖 파일도 쓰게 한다(25). Google Static Maps 요청은 시나리오 좌표로 구성한다(27). Mercator식 값은 render shader가 image pixel과 model 좌표를 정렬하는 데 쓴다(27). Google overlay 없이 초기화를 계속하는 것은 API key가 origin을 거절할 수 있는 localhost 실행에서 중요하다(29). [11-04 전수 검증 보완] |
| 31–43 | 일반 bitmap·사용자 overlay·Skybox 면을 로드한다(33–37). `createTextureFromImage()`는 `device.queue` 대신 `context.queue`를 참조하여 오래된 것으로 보이며 현재는 주로 다른 곳에서 업로드한다고 적는다(39). 텍스트 parser는 설정 크기와 일치를 가정하며 새 입력 해석은 여기, 채널 포장은 `Copy_Data_to_Textures.js`로 분리하라고 적는다(43). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 39: 문서는 `createTextureFromImage()`의 `context.queue` 참조를 적고 현재 `device.queue` 경로와의 차이를 지적한다.
