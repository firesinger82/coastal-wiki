# Celeris 차이 결론 재대조 — CD1c

## 1 요약

대상은 `celeris-docs-architecture-vs-code.md`의 §5에 실제로 있는 CD1-351–CD1-525 행이다. 행 번호는 CD1 ID의 숫자로 해석했다. §5의 표 순번 351–525를 뜻하지 않는다.

대상 행 수는 46행이다. 이 수는 §5에서 해당 ID 범위를 추출하여 셌다. 최종 결론은 A 2행, B 1행, C 0행, D 0행, E 0행, F 0행, H 34행, 일치 9행이다. 보고서 분류에서 바뀐 행은 12행이다. 분류를 유지한 행은 34행이다. 모든 개수는 아래 표를 기준으로 셌다.

인용을 보완한 행은 2행이다. CD1-484·497에서 문장 분리로 빠진 적용 문맥을 복원했다. 원문 인용의 철자·코드 줄을 고친 행은 0행이다. 본문과 §5에서 추출한 문서·코드 인용 238개는 해당 원문 줄과 일치했다. 이 수에는 본문과 결론에 반복된 인용이 포함된다.

현재 소스 기준은 `ebca435`이다. 표의 파일 경로는 `models/Celeris/raw/source_code/Celeris-WebGPU/`를 기준으로 한다. 논문 쪽수는 PDF 쪽수다. 2017·2020 논문의 PDF p.1은 제공된 쪽 이미지를 직접 열었다. 판 판정 열은 AD1·AD2·AD3·E1·E2에서 같은 보고서와 같은 행 ID를 찾은 결과다. 외부 문헌 기록 CP3-013·CP3-017은 이 범위의 행 근거에 해당하지 않는다.

바뀜은 보고서 분류와 최종 분류의 차이를 뜻한다. 이유와 노트 문장의 보완은 별도로 적었다. 이 기록은 원문에 근거한 판정이다. 모델 실행이나 수치 검증은 수행하지 않았다.

## 2 행별 최종 결론 표

### 2.1 CD1-351–CD1-447

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽, 커밋) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| CD1-351 | H 코드 대조 대상 아님 | - | 일치 | 예 | `ebca435:docs/architecture/DATA_AND_TEXTURES.md:31`<br>`ebca435:shaders/Pass1.wgsl:124–169` | 도입 형식이지만 면 재구성과 저장이라는 수치 동작을 단언한다. Pass1의 실제 저장문이 이 서술과 일치한다. | Pass1은 면에서 재구성한 수심·x방향 속도·y방향 속도·스칼라 농도를 각각 txH·txU·txV·txC에 저장한다. |
| CD1-357 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/DATA_AND_TEXTURES.md:38`<br>`ebca435:shaders/Pass1.wgsl:124–139` | 문장은 채널 규약을 바꾸기 전에 셰이더 문서를 읽으라는 변경 지침이다. 북면 x·동면 y의 설명은 Pass1의 재구성 채널과도 일치한다. | x가 북면이고 y가 동면이라는 규약을 유지하라는 변경 지침이다. |
| CD1-358 | H 코드 대조 대상 아님 | - | 일치 | 예 | `ebca435:docs/architecture/DATA_AND_TEXTURES.md:42`<br>`ebca435:shaders/Pass2.wgsl:122–137` | 도입 형식이지만 플럭스 생성자와 저장 대상을 명시한다. Pass2의 실제 저장문이 이 서술과 일치한다. | Pass2는 x방향 수치 플럭스를 txXFlux에 저장한다. Pass2는 y방향 수치 플럭스를 txYFlux에 저장한다. |
| CD1-365 | H 코드 대조 대상 아님 | - | 일치 | 예 | `ebca435:docs/architecture/DATA_AND_TEXTURES.md:53`<br>`ebca435:shaders/Pass_Breaking.wgsl:140–144`<br>`ebca435:js/main.js:2651–2655` | 쇄파 상태의 저장 대상은 코드와 대조할 수 있다. 임시 출력은 txBreaking으로 복사된다. | txBreaking은 쇄파 상태를 저장한다. `if(calc_constants.useBreakingModel == 1)` 경로에서 Pass_Breaking의 임시 출력이 txBreaking으로 복사된다. |
| CD1-376 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/DATA_AND_TEXTURES.md:71` | 이 행은 `Coefficient channels are generally:`라는 목록 도입구다. 개별 계수 채널 서술은 이 행의 인용에 없다. | PCR 채널 목록의 도입 문구다. |
| CD1-396 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/DATA_AND_TEXTURES.md:103` | 원문은 렌더 캐시의 성능 목적을 설명한다. 사용자의 H 기준에 해당한다. | 반정밀도 캐시의 성능 목적을 설명한다. 실제 성능은 측정하지 않았다. |
| CD1-397 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/DATA_AND_TEXTURES.md:105` | 이 행은 렌더 텍스처 목록의 도입구다. 그림 표시 전용 영역은 H다. | 기타 렌더 텍스처 목록의 도입 문구다. |
| CD1-415 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:3` | 원문은 docs 디렉터리의 논문 계보 안내 목적을 설명한다. | 논문 계보 가이드의 목적을 밝힌다. 원논문을 대신하지 않는다고 명시한다. |
| CD1-416 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:3` | 원문은 이 안내가 논문 원문을 대체하지 않는다고 명시한다. | 논문 계보 가이드의 목적을 밝힌다. 원논문을 대신하지 않는다고 명시한다. |
| CD1-419 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:9` | 이 행은 구현 연결 목록의 도입구다. | 구현 연결 목록의 도입 문구다. |
| CD1-424 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:18`<br>`docs/Tavakkol_2017_Celeris_GPU_accelerated_Computer_Physics_Communications.pdf` PDF p.1(인쇄 p.117), 쪽 이미지 직접 확인 | 인용 문장은 2017 연구가 개념적 선행 연구라는 계보 설명이다. 플랫폼 차이를 명시하는 다음 문장은 CD1-425에서 판정한다. | 2017 구현의 계보·플랫폼 설명이다. |
| CD1-425 | H 코드 대조 대상 아님 | - | A 판 차이 | 예 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:18`<br>`ebca435:js/main.js:238–254`<br>`ebca435:js/main.js:1537–1543`<br>`docs/Tavakkol_2017_Celeris_GPU_accelerated_Computer_Physics_Communications.pdf` PDF p.1(인쇄 p.117), 쪽 이미지 직접 확인<br>`git log --all --format= --name-only -- '*.cpp' '*.cs' '*.unity' '*.sln' '*.vcxproj'`: 출력 없음; `fd57bb7:shaders/Pass1.compute:1–28` | 2017 논문 PDF p.1은 Direct3D와 C++·HLSL을 명시한다. 현재 코드는 WebGPU와 WGSL을 사용한다. 사용자의 이전 구현 기준을 적용하여 H를 A로 바꾼다. 이력에는 2023년 HLSL 셰이더 조각이 있다. 논문 당시의 C++ 또는 C# 프로그램 전체는 없다. 셰이더 조각의 존재를 논문 당시 프로그램 전체의 존재로 간주하지 않았다. | 2017 논문은 Direct3D를 사용하는 C++·HLSL 구현을 설명한다. 현재 구현은 WebGPU와 WGSL을 사용한다. 이전 구현(논문이 밝힌 구현) 기준, 그 코드는 이 저장소 이력에 없다. |
| CD1-426 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:20` | 이 행은 2017 계보와 현재 구현의 연결 목록 도입구다. | 2017 계보와 현재 구현의 연결 목록 도입 문구다. |
| CD1-430 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:25` | 원문은 상호작용 시각화와 빠른 피드백을 설계 목표로 서술한다. 측정 성능을 제시하지 않는다. | 상호작용 시각화와 피드백을 설계 목표로 설명한다. 성능 측정값은 아니다. |
| CD1-431 | H 코드 대조 대상 아님 | - | A 판 차이 | 예 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:29`<br>`ebca435:js/main.js:238–254`<br>`ebca435:js/main.js:1537–1543`<br>`docs/Tavakkol_2020_Celeris_Base_interactive_Computer_Physics_Communications.pdf` PDF p.1, 쪽 이미지 직접 확인<br>`git log --all --format= --name-only -- '*.cpp' '*.cs' '*.unity' '*.sln' '*.vcxproj'`: 출력 없음; `fd57bb7:shaders/Pass1.compute:1–28` | 2020 논문 PDF p.1은 Unity3D와 C#·HLSL을 명시한다. 논문은 지도 중첩·실시간 계측 그래프·360° 영상 기능도 명시한다. 사용자의 이전 구현 기준을 적용하여 H를 A로 바꾼다. 이력에는 2023년 HLSL 셰이더 조각이 있다. 논문 당시의 C++ 또는 C# 프로그램 전체는 없다. 셰이더 조각의 존재를 논문 당시 프로그램 전체의 존재로 간주하지 않았다. | 2020 논문은 Unity3D와 C#·HLSL을 사용하는 Celeris Base를 설명한다. 논문은 지도 중첩·실시간 계측 그래프·360° 영상 기능을 설명한다. 현재 구현은 WebGPU 브라우저 프로그램이다. 이전 구현(논문이 밝힌 구현) 기준, 그 코드는 이 저장소 이력에 없다. |
| CD1-432 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:31` | 이 행은 2020 계보와 현재 구현의 연결 목록 도입구다. | 2020 구현과의 연결 목록 도입 문구다. |
| CD1-433 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:33` | 핵심 서술은 상호작용 설계 정신의 계승이라는 문서의 해석이다. 플랫폼 변경은 CD1-431에서 따로 판정한다. | 워크플로 계승에 대한 문서의 해석이다. 2020 Unity 실행 환경을 WebGPU 코드 오류로 판단하지 않는다. |
| CD1-435 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:35` | 원문은 경계 처리·시각화·리소스 관리의 중요도를 평가한다. | 경계·시각화·리소스 관리의 설계상 중요도를 설명한다. |
| CD1-436 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:39` | 인용은 `If you are modifying numerical kernels:`라는 독해 지침의 적용 조건이다. | 수치 커널 변경자를 위한 독해 지침의 조건문이다. |
| CD1-437 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:41` | 원문은 문서 읽기 순서를 안내한다. 해당 행은 계산 동작의 차이를 주장하지 않는다. | 권장 논문 읽기 순서다. |
| CD1-438 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:41` | 원문은 문서 읽기 순서를 안내한다. 해당 행은 계산 동작의 차이를 주장하지 않는다. | 권장 논문 읽기 순서다. |
| CD1-439 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:42` | 원문은 문서 읽기 순서를 안내한다. 해당 행은 계산 동작의 차이를 주장하지 않는다. | 권장 논문 읽기 순서다. |
| CD1-440 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:42` | 원문은 문서 읽기 순서를 안내한다. 해당 행은 계산 동작의 차이를 주장하지 않는다. | 권장 논문 읽기 순서다. |
| CD1-441 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:43` | 원문은 문서 읽기 순서를 안내한다. 해당 행은 계산 동작의 차이를 주장하지 않는다. | 권장 문서 읽기 순서다. |
| CD1-442 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:43` | 원문은 문서 읽기 순서를 안내한다. 해당 행은 계산 동작의 차이를 주장하지 않는다. | 권장 문서 읽기 순서다. |
| CD1-443 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:44` | 원문은 문서 읽기 순서를 안내한다. 해당 행은 계산 동작의 차이를 주장하지 않는다. | 권장 셰이더 설명 읽기 순서다. |
| CD1-444 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:44` | 원문은 문서 읽기 순서를 안내한다. 해당 행은 계산 동작의 차이를 주장하지 않는다. | 권장 셰이더 설명 읽기 순서다. |
| CD1-445 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:46` | 인용은 `If you are modifying UI, visualization, or scenario loading:`이라는 독해 지침의 적용 조건이다. | UI·시각화·로딩 변경자를 위한 독해 지침의 조건문이다. |
| CD1-446 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:48` | 원문은 문서 읽기 순서를 안내한다. 해당 행은 계산 동작의 차이를 주장하지 않는다. | 권장 논문 읽기 순서다. |
| CD1-447 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:48` | 원문은 문서 읽기 순서를 안내한다. 해당 행은 계산 동작의 차이를 주장하지 않는다. | 권장 논문 읽기 순서다. |

### 2.2 CD1-448–CD1-512

| 행 ID | 보고서 결론 | 판 판정 결론(없으면 -) | 최종 결론(E는 강도 포함) | 바뀜(예/아니오) | 확인한 원문(파일:줄, 문서 쪽, 커밋) | 이유 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|---|---|---|
| CD1-448 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:49` | 원문은 문서 읽기 순서를 안내한다. 해당 행은 계산 동작의 차이를 주장하지 않는다. | 권장 논문 읽기 순서다. |
| CD1-449 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:49` | 원문은 문서 읽기 순서를 안내한다. 해당 행은 계산 동작의 차이를 주장하지 않는다. | 권장 논문 읽기 순서다. |
| CD1-450 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:50` | 원문은 문서 읽기 순서를 안내한다. 해당 행은 계산 동작의 차이를 주장하지 않는다. | 권장 파일별 설명 읽기 순서다. |
| CD1-451 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/REFERENCE_PAPERS.md:50` | 원문은 문서 읽기 순서를 안내한다. 해당 행은 계산 동작의 차이를 주장하지 않는다. | 권장 파일별 설명 읽기 순서다. |
| CD1-457 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/SIMULATION_PIPELINE.md:9` | 인용은 프레임별 책임 목록의 도입구다. | 프레임별 작업 목록의 도입 문구다. |
| CD1-467 | H 코드 대조 대상 아님 | - | 일치 | 예 | `ebca435:docs/architecture/SIMULATION_PIPELINE.md:24`<br>`ebca435:shaders/Pass3_NLSW.wgsl:248–250`<br>`ebca435:js/Run_Tridiag_Solver.js:37–59`<br>`ebca435:js/main.js:2678–2682` | 도입 문장은 유한체적 갱신과 선택적 분산 보정이라는 계산 구조를 서술한다. NLSW에서 암시적 풀이를 복사로 대체하는 코드가 이 구조와 일치한다. | 시간단계는 유한체적 플럭스에 따른 갱신을 포함한다. 분산 모드는 암시적 풀이를 추가한다. `if (calc_constants.NLSW_or_Bous == 0)` 경로는 암시적 풀이 대신 중간 상태를 txNewState에 복사한다. |
| CD1-484 | B 문서 오기 | B 문서 오기(AD2) | 일치 | 예 | `ebca435:docs/architecture/SIMULATION_PIPELINE.md:36`<br>`ebca435:docs/architecture/SIMULATION_PIPELINE.md:34–36`<br>`ebca435:js/main.js:2693–2732`<br>`ebca435:js/main.js:2853–2861`<br>`ebca435:js/Run_Tridiag_Solver.js:37–40`<br>`afc1fe7:docs/architecture/SIMULATION_PIPELINE.md:34–36,53`; `afc1fe7:js/main.js:2070–2109` | AD2의 B와 다르다. 원문에는 `after the implicit solve`가 있다. 바로 앞 문장은 `NLSW mode skips the solve by copying the intermediate state to txNewState`라고 한정한다. 이 문맥은 NLSW에 두 번째 디스패치를 요구하지 않는다. 문서 시점 코드도 동일하다. 인용 보완: 분리된 문장에 앞 문장의 적용 범위를 복원했다. | 문서는 암시적 풀이 뒤에 BoundaryPass를 다시 실행한다고 설명한다. 코드의 재실행 조건은 `if (calc_constants.NLSW_or_Bous > 0)`이다. NLSW는 암시적 풀이를 건너뛴다. NLSW는 첫 경계 처리 결과를 txNewState로 복사한다. |
| CD1-489 | B 문서 오기 | B 문서 오기(AD2) | H 코드 대조 대상 아님 | 예 | `ebca435:docs/architecture/SIMULATION_PIPELINE.md:39`<br>`ebca435:docs/architecture/SIMULATION_PIPELINE.md:39`<br>`afc1fe7:docs/architecture/SIMULATION_PIPELINE.md:39` | AD2의 B와 다르다. 이 행의 문서 인용은 `14.`라는 목록 번호뿐이다. 시간단계와 렌더 자료 생성 주기의 모순은 별도 문장인 CD1-490에서 판정한다. | 이 행의 인용 `14.`는 시간단계 목록의 번호다. 계산 동작에 대한 문장은 CD1-490에서 판정한다. |
| CD1-490 | B 문서 오기 | B 문서 오기(AD2) | B 문서 오기 | 아니오 | `ebca435:docs/architecture/SIMULATION_PIPELINE.md:39`<br>`ebca435:docs/architecture/SIMULATION_PIPELINE.md:14–15`<br>`ebca435:js/main.js:2614–2615`<br>`ebca435:js/main.js:2910–2931`<br>`ebca435:js/main.js:2979–2980`<br>`afc1fe7:docs/architecture/SIMULATION_PIPELINE.md:14–15,39`; `afc1fe7:js/main.js:2282–2306` | AD2의 B를 유지한다. 문서는 시간단계별 진단 목록에 렌더 변수 생성을 포함한다. 같은 문서의 프레임 순서는 시간 반복 뒤에 렌더 자료 생성을 둔다. 문서 시점 코드도 시간 반복 밖에서 이를 실행한다. | 면 속도·통계는 시간단계마다 갱신한다. 렌더 캐시는 반복문 밖에서 프레임마다 한 번 만든다. |
| CD1-491 | H 코드 대조 대상 아님 | - | 일치 | 예 | `ebca435:docs/architecture/SIMULATION_PIPELINE.md:43`<br>`ebca435:js/main.js:1090`<br>`ebca435:shaders/Pass3_NLSW.wgsl:257–265` | 도입 문장도 설정값으로 시간적분을 선택한다는 동작을 단언한다. timeScheme을 전달하는 코드와 셰이더 분기가 일치한다. | 설정의 timeScheme은 Pass3 균일 버퍼에 전달된다. 셰이더는 `if (globals.timeScheme == 0)`에서 단일 명시적 갱신을 선택한다. 다른 경로는 pred_or_corrector로 예측 단계와 보정 단계를 구분한다. |
| CD1-497 | B 문서 오기 | B 문서 오기(AD2) | 일치 | 예 | `ebca435:docs/architecture/SIMULATION_PIPELINE.md:53`<br>`ebca435:docs/architecture/SIMULATION_PIPELINE.md:53`<br>`ebca435:js/main.js:2693–2732`<br>`ebca435:js/main.js:2757–2758`<br>`ebca435:js/main.js:2823–2826`<br>`ebca435:js/main.js:2853–2861`<br>`afc1fe7:docs/architecture/SIMULATION_PIPELINE.md:34–36,53`; `afc1fe7:js/main.js:2070–2109` | AD2의 B와 다르다. 같은 문단은 첫 처리를 `before the implicit solve`로 설명한다. 다음 문장은 삼중대각 풀이가 운동량을 바꾸는 상황을 설명한다. 따라서 두 번이라는 수량은 암시적 풀이 전후의 처리 쌍을 뜻한다. 모든 모드의 시간단계당 총 호출 횟수를 뜻하지 않는다. 인용 보완: 첫 문장만 떼어 낸 인용에 같은 문단의 범위를 복원했다. | 문서의 두 번 경계 처리는 암시적 풀이 전후의 처리 쌍을 설명한다. 풀이 뒤 재실행 조건은 `if (calc_constants.NLSW_or_Bous > 0)`이다. `if (calc_constants.timeScheme == 2)`에서는 보정 단계도 이 처리 구조를 반복한다. |
| CD1-500 | H 코드 대조 대상 아님 | - | 일치 | 예 | `ebca435:docs/architecture/SIMULATION_PIPELINE.md:57`<br>`ebca435:js/main.js:1537–1593`<br>`ebca435:js/main.js:1618–1631`<br>`ebca435:js/Config_Pipelines.js:6–13` | 도입 문장은 설정에 따른 셰이더 로딩과 컴파일을 서술한다. 파일 선택 분기와 파이프라인 생성이 이를 구현한다. | main.js는 설정에 따라 WGSL 파일을 선택한다. 선택된 소스는 createComputePipeline을 통해 셰이더 모듈과 계산 파이프라인으로 만들어진다. |
| CD1-507 | H 코드 대조 대상 아님 | - | 일치 | 예 | `ebca435:docs/architecture/SIMULATION_PIPELINE.md:66`<br>`ebca435:docs/source/shaders/Pass2_HighOrder_HLLEM_wgsl.md:7–11`<br>`ebca435:shaders/Pass2_HighOrder_HLLEM.wgsl:1–30`<br>`ebca435:js/main.js:1537–1593` | 이 문장은 변경 권고가 아니라 대안·실험용 셰이더 파일의 존재를 서술한다. HLLEM 파일이 존재한다. 현재 main.js는 HLLC를 선택한다. main.js 전체에서 `Pass2_HighOrder_HLLEM` 검색 결과는 0건이다. | 저장소에는 현재 main.js가 선택하지 않는 대안 셰이더가 있다. Pass2_HighOrder_HLLEM.wgsl은 그 예다. 현재 고차 경로는 Pass2_HighOrder_HLLC.wgsl을 선택한다. |
| CD1-508 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/SIMULATION_PIPELINE.md:66` | 원문은 변경 전에 현재 main.js의 활성 경로를 확인하라는 지침이다. | 파일의 존재와 활성 호출을 구분하라는 변경 지침이다. |
| CD1-510 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/WEBGPU_BINDING_PATTERN.md:5` | 원문은 바인딩 번호를 인터페이스로 취급하라는 변경 지침이다. | 바인딩 번호를 인터페이스로 취급하라는 지침이다. |
| CD1-512 | H 코드 대조 대상 아님 | - | H 코드 대조 대상 아님 | 아니오 | `ebca435:docs/architecture/WEBGPU_BINDING_PATTERN.md:9` | 이 행은 핸들러의 책임 목록을 여는 문구다. | 핸들러 책임 목록의 도입 문구다. |

대상 46행: 유지 34, 변경 12

