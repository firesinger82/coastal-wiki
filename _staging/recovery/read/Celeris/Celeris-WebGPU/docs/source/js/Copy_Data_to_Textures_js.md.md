---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Copy_Data_to_Textures_js.md
lines: 47
sha256: 4b4b79244f45cee49b1f48498a8cf3e29cf17dce9e0a0e5dbb23c7885027b1dc
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Copy_Data_to_Textures_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Copy_Data_to_Textures.js`

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | CPU 배열을 GPU 텍스처(texture) 채널로 포장하는 모듈이다(1–7). `copyBathyDataToTexture()`는 `txBottom`의 북·동면/중심고·near-dry와 단일 건조섬 제거, `copyWaveDataToTexture()`는 `BoundaryPass.wgsl`용 진폭·주기·방향·위상, `copyBoundaryTimeSeriesDataToTexture()`는 경계형 `5` 위치·`eta/hu/hv`, `copySphericalMetricDataToTexture()`는 `Pass3_NLSW_Spherical.wgsl` 구면 계량, `copyTSlocsToTexture()`는 관측 좌표다(11–15). `copyInitialConditionDataToTexture()`는 `writeStateFlag`별 eta/u/v, `copyConstantValueToTexture()`는 단일 RGBA, `copyTridiagXDataToTexture()`·`copyTridiagYDataToTexture()`는 Boussinesq/COULWAVE 계수, `copyImageBitmapToTexture()`·`copy2DDataTo3DTexture()`는 영상·`2D`→`3D` 복사다(16–19). 변환 대상은 지형·파랑·초기 조건·상수·삼중대각 계수이며 shader가 기대하는 정확한 채널 배치를 만든다(7). 고립된 한 셀 건조섬은 업로드 전에 제거한다(11). 경계 시계열은 `BoundaryPass.wgsl`이 읽는 측면별 텍스처에 저장한다(13). 구면 계량은 위도 의존 인자다(14). 초기 조건은 상태형 텍스처에 저장한다(16). 단일 RGBA 값으로 텍스처 전체를 채운다(17). 삼중대각 계수는 지형에서 미리 계산한다(18). [11-04 전수 검증 보완] |
| 21–47 | 행은 필요한 곳에서 `256-byte` 경계로 패딩한다(23). 지형 `r/g/b/a`는 북면/동면/중심/near-dry, 수치 계수 `a,b,c,d`는 RGBA의 하/대각/상/우변이다(25–32). 경계형 `5`는 `row 0`의 `r`에 위치, `rows 1..N`에 `[eta, hu, hv, 0]`, 마지막에 영행을 추가한다(34). `txSphericalMetrics`의 `r/g/b/a`는 `1 / (R * cos(phi_center))`, `cos(phi_north_face)`, `cos(phi_south_face)`, `tan(phi_center) / R`다(36–41). `grid_type == 2`에서 `lat_LL`은 좌하단 모서리이며 중심 `lat_LL + (j + 0.5) * dy`, 남/북면 `lat_LL + j * dy` / `lat_LL + (j + 1) * dy`를 쓴다(43). 변경 시 `Pass1`, `Update_neardry`, `Update_TriDiag_coef*`, PCR을 함께 확인하라고 적는다(47). 패딩 대상은 CPU buffer이며 WebGPU copy alignment를 맞춘다(23). 계수의 RGBA 마지막 성분은 우변 또는 placeholder다(32). 마지막 영행은 공급 시계열 이후 시각에 사용한다(34). data upload 변경도 wet/dry 동작·암시 solver 안정성·경계 강제를 바꿀 수 있어 수치적으로 중요하다고 설명한다(47). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
