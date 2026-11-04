---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/architecture/DATA_AND_TEXTURES.md
lines: 131
sha256: 393d466ed3216677997a5372869e95eb8280892854a35b556972ae132b81ccca
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# DATA_AND_TEXTURES.md — 판독 구간 기록

구간은 1행부터 131행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | JavaScript가 할당·복사한 텍스처(texture)를 WGSL이 고정 바인딩으로 읽고 쓴다고 설명한다(3). `txState`·`txNewState`의 `r`은 자유수면, `g`는 x 운동량 `P`/`hu`, `b`는 y 운동량 `Q`/`hv`, `a`는 거품·추적자·표시 스칼라다(7–12). `txstateUVstar`·`current_stateUVstar`는 암시 분산성(dispersive) 풀이 중간 상태이며 NLSW는 통과 복사, Boussinesq/COULWAVE는 PCR의 우변·해다(14). `txBottom`의 `r/g/b`는 북면/동면/중심 바닥고이며 `a`의 양수는 초기 건조지에서 멀고 음수는 가깝다(18–23). 로더가 면고·플래그를 계산하며 `Update_neardry.wgsl`이 변경 후 플래그를 갱신한다(25). `txBottomInitial`은 초기 바닥·이동 바닥·누적 변위용, `txHardBottom`은 비침식 하한이다(27). 전통적인 모델의 CPU 행렬에 해당하는 배열 대부분을 여기서는 WebGPU 텍스처로 둔다(3). `a`의 스칼라 용도는 모드에 따라 달라진다(12). near-dry 갱신은 대화식 지형 편집·교란·퇴적물 변경 뒤 수행한다(25). `txBottomInitial`은 이동 바닥 교란과 누적 퇴적물 바닥 변화 출력에 쓰인다(27). [11-04 전수 검증 보완] |
| 29–61 | `Pass1` 출력 `txH`의 `x`, `y`, `z`, `w`는 북·동·남·서면 수심이다. `txU`, `txV`, `txC`도 같은 면 순서의 속도·농도다(31–38). `Pass2`의 `txXFlux`·`txYFlux` 채널 `x/y/z/w`는 질량/자유수면·x 운동량·y 운동량·스칼라 유량이다(42–47). `txXFlux_Sed`·`txYFlux_Sed`는 농도 등급당 채널이며 현재 주로 `class 1`, 배치는 `four classes`를 수용한다(49). `txBreaking`의 `x/y/z/w`는 쇄파 시작·경과 표식/와점성/쇄파 전면·강도/Smagorinsky 보조 자리다(53–58). `txDissipationFlux`는 `Pass3_Bous`·`Pass3_COULWAVE`의 점성 가중 운동량 경사를 저장한다(60). `txU`는 x 속도이며 `txV`는 y 속도다(34–35). 면 채널 순서는 퇴적물 재구성과 진단에서도 재사용한다(38). `x`가 북면이고 `y`가 동면이므로 변경 전에 shader 문서를 읽으라고 안내한다(38). `txBreaking.w`는 Smagorinsky/subgrid 항의 placeholder다(58). `txDissipationFlux`는 쇄파 운동량 확산을 추가하는 데 쓰인다(60). [11-04 전수 검증 보완] |
| 62–94 | Boussinesq·COULWAVE의 x/y 암시 계는 병렬 순환 축소(Parallel Cyclic Reduction)로 푼다(64). `coefMatx`, `coefMaty`는 초기 계수, `newcoef_x`, `newcoef_y`와 `txtemp_PCRx`, `txtemp_PCRy`는 교대 갱신 계수다. `txtemp2_PCRx`, `txtemp2_PCRy`는 방향별 최종 반복에서만 쓰는 해다(66–69). 계수 채널 `r/g/b/a`는 하대각 `a`/대각 `b`/상대각 `c`/우변이다(71–76). COULWAVE는 먼저 속도형 우변을 저장하고 마지막 PCR에서 수심으로 운동량으로 바꾼다(78). 활성 solver는 `coefMat*` 사전 복사·`txtemp_PCR*` 반복 후 복사 대신 바인드 그룹(bind group)을 선택한다(80). `txCW_groupings`는 `3D` `rgba32float`이며 `Layer 0`: `u`, `v`, `du`, `dv`; `Layer 1`: `za`, `dzadx`, `dzady`, unused; `Layer 2`: `S`, `T`, `d2udxdy`, `d2vdxdy`; `Layer 3`: `dSdx`, `dSdy`, `dTdx`, `dTdy`; `Layer 4`: `E1`, `E2`, `E`, `dvdx - dudy`; `Layer 5`: `EzST`, `TzS2`, `uSxvSy`, `uTxvTy`다(84–91). `Pass3A_COULWAVE`·`Pass3B_COULWAVE`의 `2D` 출력을 층에 복사하고 `Pass3_COULWAVE`가 읽는다(93). 계수 채널 설명은 일반적인 배치라는 한정을 갖는다(71). 우변 채널은 PCR 반복 중 값이다(76). COULWAVE는 국소 수심으로 속도를 운동량으로 바꾼다(78). 제거한 복사의 목적지는 두 경우 모두 `newcoef_*`다(80). JavaScript는 현재 계수 텍스처를 읽고 다음 텍스처에 쓰는 bind group을 선택한다(80). `Pass3_COULWAVE`는 층별로 grouped texture를 읽는다(93). [11-04 전수 검증 보완] |
| 95–116 | `txRenderVarsf16`은 `rgba16float` `2D-array` 캐시다. `Layer 0`은 수면·최대 수면·바닥·거품/추적자, `Layer 1`은 u·v·unused·평균 절대 와도, `Layer 2`는 바닥·hard bottom·가용 세굴 깊이·unused다(97–103). `txScreen`은 영상/GIF, `txDraw`는 `2D` 색상 막대/로고, `txOverlayMap`은 선택 영상, `txSamplePNGs`는 난류·설계·화살표 배열, `txCube_Skybox`는 `3D` 환경 큐브다(105–111). `txTimeSeries_Locations`는 격자 좌표이며 `ExtractTimeSeries.wgsl`이 `txTimeSeries_Data`를 쓴다. `element 0`은 tooltip, `elements 1..N`은 관측점이다(115). 이 캐시는 렌더링 때 full `rgba32float` simulation 텍스처에 걸리는 부하를 줄인다(103). `txScreen`은 현재 렌더 화면을 보관한다(107). `txDraw`는 colorbar text와 logo를 위한 2D canvas overlay다(108). [11-04 전수 검증 보완] |
| 117–131 | 경계형 `5`는 선택 `rgba32float` 텍스처 `txBoundaryTimeSeriesSouth`, `txBoundaryTimeSeriesNorth`, `txBoundaryTimeSeriesWest`, `txBoundaryTimeSeriesEast`를 쓴다(119). 각 측면 `row 0`은 위치, `rows 1..N`은 시간 자료, 마지막 추가 행은 종료 후 영값이다. 자료는 `[eta, hu, hv, 0]`이며 JavaScript가 공통 시간 구간을 `BoundaryPass`에 보내고 셰이더가 경계 좌표를 보간한다(121). 중첩 출력은 활성 사각형마다 임시 `rgba32float` 텍스처 `four`개를 할당한다. 남/북 폭은 x면 관측점 수, 서/동 폭은 y면 관측점 수, 높이는 제한된 표본 수, 픽셀은 `[eta, hu, hv, 0]`다(125–129). `ExtractNestedBoundaryTimeSeries.wgsl`이 요청 시간에만 쓰며 다중 사각형은 독립 uniform·표본 인덱스·임계값·접두사·지연 readback을 쓴다. 모두 표본 수집을 끝낸 뒤 완료 사각형을 한 번씩 읽고 경계형 `5` 호환 텍스트를 쓴다(131). 임시 텍스처는 capture 시작 시 동적으로 할당한다(125). 다중 사각형은 동일 shader와 texture layout을 활성 사각형마다 한 번씩 재사용한다(131). JavaScript는 실제 표본 시각을 별도로 기록한다(131). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
