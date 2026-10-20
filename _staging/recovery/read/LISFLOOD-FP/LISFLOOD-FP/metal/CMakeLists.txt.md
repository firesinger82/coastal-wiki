---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/metal/CMakeLists.txt
lines: 35
sha256: 0a245f4bae8edab8b05f6eb79138d57d616db49c367fd5798cad05d9c67edc02
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# CMakeLists.txt — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | 첫 줄은 `# Metal GPU back end for the FV1 solver (Apple Silicon)` (1)이라는 주석이다. 이 주석은 Apple Silicon의 FV1 해법(solver)을 위한 Metal 그래픽 처리 장치(graphics processing unit, GPU) 후단(back end)을 설명한다. `find_library(METAL_FRAMEWORK Metal)` (3)로 Metal 프레임워크(framework)를 찾는다. `find_library(FOUNDATION_FRAMEWORK Foundation)` (4)로 Foundation 프레임워크를 찾는다. 빈 줄도 이 구간에 포함한다(2·5). |
| 6–10 | 조건은 `if(METAL_FRAMEWORK AND FOUNDATION_FRAMEWORK)` (6)이다. 참 분기의 주석 원문은 `# The kernels are compiled to a metallib next to the executable, which loads` (7), `# it at run time. -fno-fast-math keeps the GPU arithmetic identical to the` (8), `# CPU solver's, so the verification cases are bit-for-bit reproducible.` (9)이다. 주석은 커널(kernel)을 실행 파일 옆의 metallib로 컴파일하고 실행 중 불러온다고 설명한다. 주석은 `-fno-fast-math`가 GPU 연산을 중앙 처리 장치(central processing unit, CPU) 해법과 같게 하여 검증 사례를 비트 단위로 재현한다고 설명한다. 이 구간은 그 설명에 대한 실행 검증을 포함하지 않는다. 경로 설정은 `set(METALLIB ${CMAKE_BINARY_DIR}/metal_fv1_kernels.metallib)` (10)이다. |
| 11–20 | 시작 시 6행 `if(METAL_FRAMEWORK AND FOUNDATION_FRAMEWORK)`의 참 분기 안이다. `add_custom_command(` (11)는 `OUTPUT ${METALLIB}` (12)를 생성물로 지정한다. 첫 실행 명령은 `COMMAND xcrun -sdk macosx metal -fno-fast-math` (13)이며, 이어지는 인수 줄은 `-c ${CMAKE_CURRENT_SOURCE_DIR}/fv1/metal_fv1_kernels.metal` (14), `-o ${CMAKE_BINARY_DIR}/metal_fv1_kernels.air` (15)이다. 두 번째 실행 명령은 `COMMAND xcrun -sdk macosx metallib ${CMAKE_BINARY_DIR}/metal_fv1_kernels.air` (16)이며, 이어지는 인수 줄은 `-o ${METALLIB}` (17)이다. 의존 파일 지정은 `DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/fv1/metal_fv1_kernels.metal` (18)이다. 표시 문구와 명령 블록의 끝은 `COMMENT "Compiling Metal FV1 kernels")` (19)이다. `add_custom_target(metal_shaders DEPENDS ${METALLIB})` (20)로 생성물을 요구하는 대상을 추가한다. |
| 21–32 | 시작 시 6행 `if(METAL_FRAMEWORK AND FOUNDATION_FRAMEWORK)`의 참 분기 안이다. 빈 줄 뒤에 `add_library(lisflood-metal STATIC` (22)로 정적 라이브러리(static library)를 선언한다. 소스 목록의 원문은 `${CMAKE_CURRENT_SOURCE_DIR}/metal_integrate.cpp` (23), `${CMAKE_CURRENT_SOURCE_DIR}/fv1/metal_fv1_simulate.mm)` (24)이다. `add_dependencies(lisflood-metal metal_shaders)` (25)로 앞선 생성 대상에 의존한다. 포함 경로 명령은 `target_include_directories(lisflood-metal PUBLIC ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_SOURCE_DIR})` (26)이다. 연결 명령은 `target_link_libraries(lisflood-metal PUBLIC ${METAL_FRAMEWORK} ${FOUNDATION_FRAMEWORK} lisflood-base)` (27)이다. 컴파일러 옵션은 `target_compile_options(lisflood-metal PRIVATE -fobjc-arc)` (28)이다. 전처리 매크로(preprocessor macro) 정의는 `target_compile_definitions(lisflood-metal PUBLIC METAL_ENABLED)` (29)이다. 부모 범위로 보내는 설정은 `set(METAL_ENABLED TRUE PARENT_SCOPE)` (31), `set(METAL_LIBRARY lisflood-metal PARENT_SCOPE)` (32)이다. 빈 줄도 포함한다(21·30). |
| 33–35 | 시작 시 6행 `if(METAL_FRAMEWORK AND FOUNDATION_FRAMEWORK)`의 조건 블록 안이다. `else()` (33)는 그 조건이 거짓일 때의 분기이다. 실행할 CMake 명령은 `message(WARNING "Metal framework not found: building without the Metal back end")` (34)이다. `endif()` (35)로 조건 블록과 파일을 끝낸다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10·13–19: Metal 컴파일 생성물의 파일명은 `metal_fv1_kernels.air`와 `metal_fv1_kernels.metallib`로 고정되어 있다. 두 생성물의 경로는 `${CMAKE_BINARY_DIR}`를 사용한다.
- 31–35: 참 분기만 부모 범위의 `METAL_ENABLED`와 `METAL_LIBRARY`를 설정한다. 거짓 분기는 경고만 출력하며 두 변수를 설정하거나 지우는 명령을 포함하지 않는다.
