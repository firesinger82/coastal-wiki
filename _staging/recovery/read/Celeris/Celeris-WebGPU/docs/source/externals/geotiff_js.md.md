---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/externals/geotiff_js.md
lines: 15
sha256: fd874e002059c180e9dbd4b5772dbbccb45f7fc54fa71d7bd8f9e887aa5c837b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# geotiff_js.md — 판독 구간 기록

설명 대상 코드 파일: `externals/geotiff.js`

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | `externals/geotiff.js` 원문 링크와 브라우저 GeoTIFF 출력·해석을 지원하려는 로컬 라이브러리 설명이다(1–7). |
| 9–15 | `File_Writer.js`의 `downloadGeoTiffData()`가 `GeoTIFF`를 참조하지만 현재 readback 서명에 비해 오래된 경로로 보인다고 적는다(11). 활성 출력은 텍스트·이진 텍스처(texture) 회수, JPEG·영상 슬라이스·GIF·JSON 설정이다(11). 외부 의존성으로 취급하고 사용 전 `File_Writer.js`·라이브러리 API·브라우저 가용성·채널 순서를 확인하라고 적는다(15). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11: 문서는 `downloadGeoTiffData()`가 현재 readback 함수 서명에 비해 오래된 경로로 보인다고 적는다.
