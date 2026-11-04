---
title: "Celeris 논문과 WebGPU 코드의 차이"
model: Celeris
doc: web-ref
canonical_source: external
citation_status: verified
verification_method: "2026-11-04 Celeris recovery 대조 보고서 반영"
last_source_check: "2026-11-04 (recovery 대조 반영)"
note_author: "Codex"
note_date: 2026-11-04
layer: 2
depends_on: []
source_scope: Celeris-WebGPU/docs, Celeris-WebGPU/js, Celeris-WebGPU/shaders
---

# Celeris 논문과 WebGPU 코드의 차이


## 문서와 코드 차이 (11-04 대조)

코드는 plynett/plynett.github.io main `ebca435`(2026-07-20)의 Celeris-WebGPU이다. 문서는 같은 커밋의 `docs/`·`README`이다. 논문은 Tavakkol & Lynett 2017(CPC), Tavakkol & Lynett 2020(CPC), Lynett et al. 2026(JWPCOE)이다.

코드 인용의 기준 경로는 `models/Celeris/raw/source_code/Celeris-WebGPU/`이다. 결론은 행별 최종 근거의 문장과 인용을 옮긴 AI 정리이다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| lynett2026:CP3-100 | 선형 구조물 편집 | Lynett 2026 p.4 지형 편집 설명. | `shaders/MouseClickChange.wgsl:98–100` `let crest_half_width = 0.5 * globals.designcomponent_CrestWidth;`<br>`let side_distance = max(0.0, r - crest_half_width);`<br>`return globals.designcomponent_CrestElev - globals.designcomponent_SideSlope * side_distance;`<br>확인한 원문: Lynett 2026 p.1 게재일, p.4 지형 편집 설명; `d778fe7:shaders/MouseClickChange.wgsl:86–100` 및 해당 diff; `shaders/MouseClickChange.wgsl:86–100` | A 판 차이 | d778fe7(2026-06-02)은 논문 게재 후 선형 구조물 형상 편집을 추가했다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP3RF.md)) |
| lynett2026:CP3-109 | 충격 파원과 이동바닥 | Lynett 2026 p.6 Fig.2 파원 메뉴. | `shaders/AddDisturbance.wgsl:182,187,196,203,210`은 각각 `if (globals.disturbanceType == 1) {      // solitary wave`, `} else if (globals.disturbanceType == 2) {   // earthquake`, `} else if (globals.disturbanceType == 3) {   // submerged landslide`, `} else if (globals.disturbanceType == 4) {   // subaerial landslide`, `} else if (globals.disturbanceType == 5) {   // prescribed depth motion`이다.<br>확인한 원문: Lynett 2026 p.6 Fig.2 파원 메뉴; `shaders/AddDisturbance.wgsl:182–239`; `js/main.js:507` | C 문서 누락 | 충격 파원과 이동바닥의 선택을 기록한다. `disturbanceType == 2` 분기의 earthquake 호출은 주석 처리되어 있다. 배 압력 파일의 존재를 활성 기능으로 세지 않는다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP3RF.md)) |
| tavakkol2017:CP1-002 | 배포 라이선스 설명 | Tavakkol 2017 p.1 `Licensing provisions: GNU General Public License 3 (GPL)`; Tavakkol 2017 p.11도 GPL 배포를 설명한다. | `README.md:82` `` This project is licensed under the **MIT License**. See the `LICENSE` file for details. ``<br>확인한 원문: Tavakkol 2017 p.1·2·11; Tavakkol 2020 p.1; `69827ba:README.md:82`; `README.md:82` | A 판 차이 | 논문의 GPL 배포 설명은 2017년 Advent에 한정한다. 이전 구현(논문이 밝힌 구현) 기준, 그 코드는 이 저장소 이력에 없다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP1.md)) [11-04 전수 검증 정정] |
| tavakkol2017:CP1-088 | 작은 파고의 무차원화 | Tavakkol 2017 p.7 작은 파고 설정의 `\Delta x/h`, `\Delta t(g/h)^{0.5}`와 Tavakkol 2017 p.2의 총수심 `h` 정의 | `shaders/Pass3_Bous.wgsl:123` `let h_here = in_state_here.x - B_here;`<br>확인한 원문: Tavakkol 2017 p.2 h·d 정의, p.3 균일 격자 설명, p.7 §4.1; `shaders/Pass3_Bous.wgsl:123` | B 문서 오기 | 작은 파고 설정의 h 표기는 총수심 정의와 일정 격자 설정에 맞지 않는다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP1.md)) |
| tavakkol2017:CP1-089 | 무차원 비의 단위 | Tavakkol 2017 p.7 `100<L/d<1000\ \mathrm m` | `js/constants_load_calc.js:27` `dx: 1.0,  // Cell size in the x direction.`<br>확인한 원문: Tavakkol 2017 p.7 §4.1; `js/constants_load_calc.js:27` | B 문서 오기 | 무차원 L/d의 상한 뒤 m는 단위 표기 오기이다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP1.md)) |
| tavakkol2017:CP1-091 | Fig. 7 시간 기호 | Tavakkol 2017 p.8 Fig. 7 캡션 `t(g/h)^{0.5}=15,20,25,45`; 패널 내부 표기는 `t\sqrt{g/d}=15,20,25,45`; 실선 수치·점 실험 | `js/main.js:2624` `total_time = frame_count * calc_constants.dt + calc_constants.start_time_shift;  //simulation time - at this point, we know values at times n-1 and previous.  We are predicted values at n`<br>확인한 원문: Tavakkol 2017 p.8 Fig.7 캡션·패널; `js/main.js:2624` | B 문서 오기 | Fig. 7의 캡션 h와 패널 d는 서로 다르다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP1.md)) |
| tavakkol2017:CP1-093 | 식 (37) 천퇴 부호 | Tavakkol 2017 p.8 식 (37) `z=\begin{cases}0&0\le x<10.67-G\\(10.67-G-x)/25&10.67-G\le x<18.29-G\\0.3048&18.29-G\le x\end{cases}` | 현재 일반 커널은 `shaders/Pass3_Bous.wgsl:117` `let B_here = textureLoad(txBottom, idx, 0).z;`로 입력 지형을 읽는다. 식 (37)을 하드코딩하지 않는다.<br>확인한 원문: Tavakkol 2017 p.8 식 (37)·§4.2; `shaders/Pass3_Bous.wgsl:117` | B 문서 오기 | 식 (37)의 가운데 구간 부호는 상승 천퇴 설명과 내부적으로 맞지 않는다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP1.md)) |
| tavakkol2017:CP1-108 | Fig. 15(c) 파고 | Tavakkol 2017 p.11 Fig. 15 `H/d = 0.04 (a), 0.09 (b), and 0.018 (c)`; 실선 수치·x 표식 측정 | 논문 내부 대조: p.9 본문과 p.10 Fig. 13, p.11 Fig. 14는 가장 큰 사례를 0.18이라고 적는다.<br>확인한 원문: Tavakkol 2017 p.9 §4.3, p.10 Fig.13, p.11 Fig.14·15 | B 문서 오기 | Fig. 15(c)의 0.018은 같은 논문의 가장 큰 파고 0.18과 다르다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP1.md)) |
| tavakkol2017:CP1-165 | 계측점 그림 번호 | Tavakkol 2017 p.9 `Gauges #6 and #9 ... gauge #22 ... (Fig. 11).` | 논문 내부 대조: p.9 Fig. 10 캡션 `Experimental setup of the conical island. The gauge locations are shown by dots`; Fig. 11은 네 시계열<br>확인한 원문: Tavakkol 2017 p.9 §4.3 본문·Fig.10·Fig.11 | B 문서 오기 | 계측점 배치는 Fig. 10이며 Fig. 11은 시계열이다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP1.md)) |
| tavakkol2020:CP2-003 | Base의 VR 지원 | Tavakkol 2020 p.1 “view the simulations in a virtual reality headset” | [2020 대조 보고서 §5.2 검색 D1](../../../_staging/recovery/compare/celeris-tavakkol2020-vs-code.md). 활성 호스트의 VR 세션 진입 코드는 검색되지 않았다.<br>확인한 원문: Tavakkol 2020 p.1–2; `README.md:25`; 현재 rg -i 및 전체 이력 git log -S 재검색 | A 판 차이 | Base 논문은 VR 헤드셋 지원을 명시한다. 이 설명을 현재 WebGPU의 VR 지원 근거로 사용하지 않는다. Tavakkol 2020(CPC)의 이전 구현 기준, 그 코드는 이 저장소 이력에 없다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP2.md)) [11-04 전수 검증 보완] |
| tavakkol2020:CP2-101 | Oculus Rift 대상 | Tavakkol 2020 p.11 “targeted ... Oculus Rift headsets”; “as of 2019” | [2020 대조 보고서 §5.2 검색 D1](../../../_staging/recovery/compare/celeris-tavakkol2020-vs-code.md). VR API와 headset 구현은 범위 내 소스·이력에서 검색되지 않았다.<br>확인한 원문: Tavakkol 2020 p.11 §4.6.1; `README.md:25`; 현재 rg -i 및 전체 이력 git log -S 재검색 | A 판 차이 | Oculus Rift는 논문이 설명하는 Celeris VR의 대상 장치이다. 이를 현재 WebGPU의 지원 장치 목록으로 옮기지 않는다. Tavakkol 2020(CPC)의 이전 구현 기준, 그 코드는 이 저장소 이력에 없다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP2.md)) [11-04 전수 검증 보완] |
| tavakkol2020:CP2-104 | VR 이동·회전 조종 | Tavakkol 2020 p.11 “left controller ... move”; “right ... rotate”; “physically rotating” | [2020 대조 보고서 §5.2 검색 D1](../../../_staging/recovery/compare/celeris-tavakkol2020-vs-code.md). `js/main.js:4259` `} else if (event.button === 0 && event.ctrlKey && calc_constants.viewType == 2) {`는 마우스 탐색 분기이다.<br>확인한 원문: Tavakkol 2020 p.11 §4.6.2 및 Fig. 11; `js/main.js:4258–4262`; 현재 rg -i 및 전체 이력 git log -S 재검색 | A 판 차이 | Celeris VR은 왼손 조종기로 이동하고 오른손 조종기로 회전한다. 사용자는 몸을 돌려서도 시선을 회전할 수 있다. 현재 마우스 조작 분기는 이 VR 조종 기능의 구현 근거가 아니다. Tavakkol 2020(CPC)의 이전 구현 기준, 그 코드는 이 저장소 이력에 없다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP2.md)) [11-04 전수 검증 보완] |
| tavakkol2020:CP2-120 | Fig. 15 상대파고 | Tavakkol 2020 p.13 “maximum horizontal run-up for H/d = 0.018” | 논문 내부 대조: Tavakkol 2020 p.12의 `H/d=0.18`와 Tavakkol 2020 p.13 Fig. 14의 `H/d=0.18`<br>확인한 원문: Tavakkol 2020 p.12; p.13 Fig. 14–15 | B 문서 오기 | Fig. 15 캡션은 `H/d=0.018`로 인쇄되었다. 같은 시험의 본문·Fig. 14 조건은 `H/d=0.18`이다. ([최종 근거](../../../_staging/recovery/compare/Celeris-conclusion-verify-CP2.md)) |
