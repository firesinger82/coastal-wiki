---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/File_Writer_js.md
lines: 30
sha256: 7506a2213259aa2d5531dcf34edf21ac78b93bb7caf3a114ff0b07fbc5b676ef
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# File_Writer_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/File_Writer.js`

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | GPU 텍스처(texture)를 CPU로 회수해 과학 자료·영상·GIF·JSON을 다운로드한다(1–7). `readTextureData()`는 `rgba32float`를 패딩 버퍼로 복사·매핑하고 `1-based` 채널을 `Float32Array`로 추출한다. `downloadTextureData()`는 그 다운로드 wrapper, `writeSurfaceData()`는 지형·eta·운동량·속도·난류, `TexturetoImageData()`는 BGRA를 `ImageData`로 변환한다(11–15). `writeNestedGridBoundaryTimeSeriesData()`는 사각형의 `four` 출력 텍스처를 종료 시 한 번 읽고 경계형 `5` 텍스트를 쓴다. 다중 사각형은 완료 항목당 `filePrefix`를 쓰며 전용 임계값 또는 `nestedEtaWriteThreshold`가 `greater than zero`이면 적어도 한 면 관측점 eta 절댓값이 초과할 때까지 앞 표본을 자른다. 시간은 shifted/global 시계를 유지해 별도 시작 메타파일이 필요 없다(14). `readTextureData()`는 한 채널을 평탄한 배열로 추출한다(11). 다중 사각형에서는 완료 사각형마다 출력 함수를 한 번 호출한다(14). `nestedEtaWriteThreshold`는 사각형별 임계값의 fallback이다(14). [11-04 전수 검증 보완] |
| 17–30 | `saveRenderedImageAsJPEG()`는 `txScreen`의 BGRA를 RGBA로 바꿔 canvas에서 JPEG로 쓴다. `saveTextureSlicesAsImages()`는 `3D` 슬라이스, `createAnimatedGifFromTexture()`는 `3D` 프레임과 로컬 GIF worker, `createAndDownloadVideoFromTexture()`는 존재하나 SharedArrayBuffer 제약으로 비활성/제한적이다(19–22). `downloadObjectAsFile()`은 JSON형 객체, `handleFileSelect()`·`loadJsonIntoCalcConstants()`는 구성 입력이다(26). 패딩 행·`rgba32float`/BGRA·채널 번호에 주의하며 `downloadGeoTiffData()`는 현재 `readTextureData()` 서명에 비해 오래된 것으로 보인다고 적는다(30). `downloadObjectAsFile()`의 예시는 현재 config다(26). 구성 JSON은 file input으로 로드한다(26). `downloadGeoTiffData()`는 사용 전에 감사해야 한다고 안내한다(30). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22: 문서는 `createAndDownloadVideoFromTexture()`를 SharedArrayBuffer 제약으로 비활성/제한적이라고 적는다.
- 30: 문서는 `downloadGeoTiffData()`와 현재 `readTextureData()` 서명의 차이를 후속 확인 대상으로 적는다.
