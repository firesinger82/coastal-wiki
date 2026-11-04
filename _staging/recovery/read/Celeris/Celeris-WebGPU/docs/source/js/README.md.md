---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/README.md
lines: 38
sha256: 6e793948c11754339da01a42c839b8c20dc70775a45d30773e3581754f4f978a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# README.md — 판독 구간 기록

설명 대상 코드 파일: `js/`의 JavaScript 모듈

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | JavaScript는 자료 로딩·GPU 자원·바인드 그룹(bind group)·WGSL 실행·텍스처(texture) 복사·UI·출력을 맡으며 중심은 `main.js`다(3–5). `main.js`는 초기화/루프/UI, `constants_load_calc.js`는 설정/파생값, `Config_Pipelines.js`는 pipeline, `Create_Textures.js`는 할당, `Copy_Data_to_Textures.js`는 지형/파랑/초기/계수 포장, `Wave_Generator.js`는 `txWaves`용 sine/TMA, `Run_Compute_Shader.js`는 실행/복사, `Run_Tridiag_Solver.js`는 PCR을 맡는다(9–16). JavaScript는 무거운 수치 작업을 직접 수행하지 않는 browser 제어 계층이다(3). 다른 모듈 대부분은 `main.js`에 입력을 공급하거나 좁은 shader binding 계약을 만들거나 GPU에서 자료를 회수한다(5). `main.js`는 bootstrap·WebGPU 초기화·simulation loop·UI event·render loop·출력 trigger를 맡는다(9). `Config_Pipelines.js`는 compute/render pipeline을 모두 만든다(11). `Create_Textures.js`는 buffer도 할당한다(12). `Wave_Generator.js`는 UI에서 선택한 파랑 행을 업로드 전에 만든다(14). [11-04 전수 검증 보완] |
| 18–38 | `File_Loader.js`는 입력·영상, `File_Writer.js`는 출력, `display_parameters.js`는 DOM·로그, `Time_Series.js`는 tooltip·관측값 회수, `Model_Loaders.js`는 단순 모델/prototype glTF, `site.js`는 현재 비활성 placeholder다(20–25). `Handler_*.js`의 바인딩 순서는 JavaScript/WGSL API다(29). 변경 시 WGSL `@binding`, `main.js`의 모든 호출, `Create_Textures.js` 형식, 대응 셰이더 문서를 갱신한다(31–36). 일부 오래된 주석보다 실제 번호·인수를 우선하라고 적는다(38). [11-04 전수 검증 정정] `File_Loader.js`는 격자·wave file·overlay·image bitmap·cube map·선택 사용자 파일을 로드한다(20). `File_Writer.js`는 texture·image·GIF·config·time surface·readback 자료를 출력한다(21). `display_parameters.js`는 DOM status/config 패널을 갱신하고 console log를 페이지로 돌린다(22). handler는 대응 WGSL pass의 layout과 bind group을 정의한다(29). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
