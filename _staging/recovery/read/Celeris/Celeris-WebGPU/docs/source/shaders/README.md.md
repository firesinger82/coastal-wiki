---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/README.md
lines: 46
sha256: 39d7fba8e39b8035dfb6675620bc92dd451efacb29051e11871e6a2f113ad8a3
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# README.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/`의 WGSL 셰이더

구간은 1행부터 46행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | JavaScript가 바인드 그룹(bind group)을 만들고 WGSL이 GPU 계산·시각화를 수행하며 transect는 제외한다(3–5). `Pass0.wgsl`은 이웃 수심, `Pass1.wgsl`은 표준 재구성, `Pass1_HighOrder.wgsl`은 넓은 MUSCL/TVD, `Pass2.wgsl`은 HLL, `Pass2_HighOrder_HLLC.wgsl`은 현재 `main.js` 고차 선택, `Pass2_HighOrder_HLLEM.wgsl`은 대안이다(9–14). `Pass3_NLSW.wgsl`, `Pass3_NLSW_Spherical.wgsl`(`grid_type == 2`), `Pass3_Bous.wgsl`, `Pass3A_COULWAVE.wgsl`, `Pass3B_COULWAVE.wgsl`, `Pass3_COULWAVE.wgsl`은 각 방정식 적분/보조항이다(15–18). WGSL은 각 pass가 읽고 쓰고 계산할 내용을 정의한다(3). NLSW 두 변형은 source/time integration을 맡는다(15–16). `Pass3_Bous.wgsl`은 source/time integration과 분산항을 맡는다(17). [11-04 전수 검증 보완] |
| 20–34 | `BoundaryPass.wgsl`은 경계·습윤/건조, `Pass_Breaking.wgsl`은 쇄파, `Update_TriDiag_coef*.wgsl`은 암시 계수, `TriDiag_PCR*.wgsl`은 병렬 순환 축소(Parallel Cyclic Reduction), `CalcMeans.wgsl`, `CalcWaveHeight.wgsl`, `ExtractTimeSeries.wgsl`, `Copytxf32_txf16.wgsl`은 진단·회수·표시 포장이다(22–26). 퇴적물 활성 경로는 `SedTrans_Pass1.wgsl`, `SedTrans_Pass3.wgsl`, `SedTrans_UpdateBottom.wgsl`, 구형/prototype은 `SedTrans_Pass3_old.wgsl`, `SedTrans_Pass3_wBedUpdate.wgsl`, `SedTrans_UpdateBottom_testing.wgsl`이다(30–33). `Pass_Breaking.wgsl`은 와점성 항도 맡는다(23). `SedTrans_Pass1.wgsl`은 농도 재구성이다(30). `SedTrans_Pass3.wgsl`은 부유사 갱신과 침식/퇴적이다(31). `SedTrans_UpdateBottom.wgsl`은 퇴적물 변화에 따른 지형 갱신이다(32). [11-04 전수 검증 보완] |
| 35–46 | 렌더는 `vertex.wgsl`·`fragment.wgsl`의 `2D`, `vertex3D.wgsl`의 `3D` 물 표면, `skybox.*.wgsl`, `model.*.wgsl`, prototype `duck.*.wgsl`, 실험 `fragment_testing.wgsl`이다(37–42). handler 문서의 자원과 셰이더 문서의 해석을 함께 읽으라고 적는다(46). `skybox.*.wgsl`은 3D skybox다(39). `model.*.wgsl`은 단순 model/box 렌더다(40). `duck.*.wgsl`은 glTF형 textured model prototype이다(41). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
