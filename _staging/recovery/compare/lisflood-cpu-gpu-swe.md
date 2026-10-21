# CPU 해법과 GPU 해법 대조 1: 충격 포착 해법

분류별 개수: C 31, E 32, F 10, H 11, X 0. 합계 84행(§5.2의 고유 행 ID 기준).

## 1 요약

이 보고서는 LISFLOOD-FP 8.3 패치를 적용한 위키 원자료를 정적으로 대조한다.
코드 인용의 기준 경로는 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/`이다.
`package:`는 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP-8.3-package/`이다.
`note:`는 `models/LISFLOOD-FP/`이다.
인용 뒤의 백틱은 원문이다.
여러 줄 식은 아래의 원문 블록을 함께 읽는다.
식 변형을 설명하는 문장은 `해석:`으로 표시한다.
이 보고서는 모델 실행 결과를 제시하지 않는다.

배포본은 `package:README.md:3-5`에서 `LISFLOOD-FP 8.2 with faster, reproducible CUDA solvers and a new GPU back end`와 `The numerical method of 8.2 is` / `unchanged.`를 적는다.
이 설명은 아래의 조건별 코드 대조를 대신하지 않는다.
CPU의 실행 경로는 `lisflood.cpp:787`의 `fv1::solve(Fnameptr, &Fps, Statesptr, Parptr, Solverptr, BCptr,`와 `lisflood.cpp:792`의 `dg2::solve(Fnameptr, &Fps, Statesptr, Parptr, Solverptr, BCptr,`이다.
`dg2new.cpp`는 비교 대상에 포함한다.
현재 CPU 진입점은 `lisflood.cpp:794-796`에서 `//dg2new::DG2Solver solver(Fnameptr, &Fps, Statesptr, Parptr, Solverptr,` / `//        BCptr, Stageptr, Arrptr, verbosemode);` / `//solver.solve();`로 주석 처리되어 있다.

FV1의 CPU·CUDA·Metal 구현은 모두 수심과 두 운동량을 갱신한다.
세 구현은 두 방향의 플럭스를 갱신 전 상태에서 계산한다.
CUDA와 Metal의 중간 배열은 x 방향 기여를 보관한다.
이 중간 배열을 근거로 시간 적분을 차원 분리로 부르면 안 된다.
근거는 §2.2의 호출 인수와 원문 식이다.

§5.2의 비일치 결론은 84행이다.
E 32행은 정적 코드 결함 후보이다.
이 중 2행은 비활성 dg2new에 속한다.
이 중 다른 2행은 8.3에서 수정된 8.2 결함이다.
이 개수는 실행으로 재현한 오류 수가 아니다.

CPU·CUDA의 수위 지정 점 원천은 FMIN을 쓴다(LG1-024).
Metal의 같은 처리는 max를 쓴다.
CPU DG2의 y 최소 수심 검사는 H1x를 읽는다(LG1-050).
CUDA의 같은 검사는 H1y를 읽는다.
CUDA의 시간 간격·강우·질량 장부는 상태 갱신과 별도로 대조했다(LG1-017, 127~129, 145).
8.3의 최대 수심 버퍼 수정과 플럭스 루프 장벽 추가는 현재 남은 후보와 구분했다(LG1-130~131).

### 1.1 전처리와 판정 조건

| 조건 | 원문 근거 | 대조에 적용한 조건 |
|---|---|---|
| 기본 수치 형식 | `config.default.cmake:2` `add_compile_definitions(_NUMERIC_MODE=1)`; `lisflood.h:75-77` `#if _NUMERIC_MODE == 1` / `#define NUMERIC_TYPE double` / `#define NUMERIC_TYPE_NAME "double"` | 기본 CMake는 double이다. float 대조는 `_NUMERIC_MODE=0` 조건을 따로 적는다. |
| float 분기 | `lisflood.h:86-88` `#else` / `#define NUMERIC_TYPE float` / `#define NUMERIC_TYPE_NAME "float"` | CUDA의 `NUMERIC_TYPE`은 무조건 float가 아니다. |
| Metal 형식 | `metal/fv1/metal_fv1_kernels.metal:115-118` `struct FlowVector {` / `float H;   // water height` / `float HU;  // x-momentum` / `float HV;  // y-momentum` | Metal 커널은 float이다. 호스트 배열은 변환된다. |
| CUDA 빌드 | `CMakeLists.txt:73-77` `if (CMAKE_CUDA_COMPILER)` / `enable_language(CUDA)` / `set_property(TARGET lisflood PROPERTY CUDA_SEPARABLE_COMPILATION ON)` / `add_compile_definitions(CUDA THRUST_IGNORE_CUB_VERSION_CHECK)` | CUDA 컴파일러가 있는 빌드의 경로를 대조한다. |
| Metal 빌드·선택 | `CMakeLists.txt:232-235` `if (APPLE)` / `add_subdirectory(metal)` / `if (METAL_ENABLED)` / `target_link_libraries(lisflood PRIVATE ${METAL_LIBRARY})`; `lisflood.cpp:782` `if (Statesptr->cuda == ON && metal_is_available())` | Apple 빌드에서 Metal이 준비되고 GPU를 요청한 FV1 경로이다. |
| 다른 최적화 매크로 | `config.default.cmake:3-8` `add_compile_definitions(_ONLY_RECT=1)` / `add_compile_definitions(_PROFILE_MODE=0)` / `add_compile_definitions(_DISABLE_WET_DRY=0)` / `add_compile_definitions(_CALCULATE_Q_MODE=1)` / `add_compile_definitions(_SGM_BY_BLOCKS=0)` / `add_compile_definitions(_BALANCE_TYPE=0)` | 대상 SWE 식에 이 매크로의 분기가 있는지 별도로 검색했다. 같은 판의 차이를 이 매크로로 자동 설명하지 않는다. |

`rg -n '^#if|^#elif|^#else|^#endif|RESULT_CHECK' swe cuda/fv1 cuda/fv2 cuda/dg2 cuda/cuda* metal`은 SWE의 `_MSC_VER` reduction 분기와 강우의 `_NETCDF` 분기를 찾았다.
이 검색은 대상 계산식에서 `_ONLY_RECT`, `_CALCULATE_Q_MODE`, `_DISABLE_WET_DRY`, `_BALANCE_TYPE`, `RESULT_CHECK`, `_PROFILE_MODE`의 수식 선택 분기를 찾지 못했다.
따라서 이 매크로들은 아래의 FV1·DG2 식 차이에 대한 반대 근거가 아니다.

## 2 대조 표

표의 `같음`은 적힌 조건에서 계산식과 분기가 대응한다는 뜻이다.
`같음`은 장치 간 비트 일치를 뜻하지 않는다.
`다름`은 결과에 영향을 줄 수 있는 조건 또는 식 차이를 뜻한다.
모든 비일치 행은 §5에서 C·E·F·H·X 중 하나로 분류한다.
메모리 배치와 실행 최적화는 H로 분리한다.

### 2.1 FV1 상태·재구성·리만 해법

| 행 ID | 계산 항목 | CPU 원문 | CUDA 원문 | Metal 원문 | 판정과 이유 |
|---|---|---|---|---|---|
| LG1-001 | 실행되는 CPU DG2와 별도 구현 | `lisflood.cpp:792` `dg2::solve(Fnameptr, &Fps, Statesptr, Parptr, Solverptr, BCptr,`; `lisflood.cpp:796` `//solver.solve();` | `CMakeLists.txt:108-113`에 `cuda/dg2/cuda_dg2_solver.cu`를 포함한다. | FV1만 구현한다. `metal/metal_integrate.cpp:8` 이후의 전달 경로는 §2.7에서 다룬다. | 다름. `dg2new`의 식을 기본 CPU 결과로 인용하지 않는다. H. |
| LG1-002 | 수치 형식 | `lisflood.h:76` `#define NUMERIC_TYPE double`; `lisflood.h:87` `#define NUMERIC_TYPE float` | `cuda/cuda_flow.cuh:11-13` `NUMERIC_TYPE H;` / `NUMERIC_TYPE HU;` / `NUMERIC_TYPE HV;` | `metal/fv1/metal_fv1_kernels.metal:116-118`의 float 필드 | 다름. 동일 정밀도 대조에는 CPU·CUDA의 float 빌드가 필요하다. 수학적 변수 표기와 부동소수점 재현성을 구분한다. F는 변수 표현에 한정한다. |
| LG1-003 | 수면과 계면 바닥 | `swe/fv1/modifiedvars.cpp:331` `return Z + H;`; `:19` `Zstar_x = getmax(Z_neg, Z_pos);`; `:33` `Zstar_y = getmax(Z_neg, Z_pos);` | `cuda/cuda_flow.cu:47` `NUMERIC_TYPE ETA = H + Z;`; CUDA 바닥 초기화는 §2.6에서 인용한다. | `metal/fv1/metal_fv1_kernels.metal:361` `Zstar_x[idx] = max(Z_neg, Z_pos);`; `:380` `Zstar_y[idx] = max(Z_neg, Z_pos);` | 같음. 경계 바닥은 내부 바닥을 ghost에 복사한 조건이다. Metal의 기준면 이동은 별도 행이다. |
| LG1-004 | 정수압 수심 재구성 | `swe/fv1/modifiedvars.cpp:93` `Hstar_neg_x = getmax(C(0.0), ETA - Zstar_x);`; 나머지 면은 `:106`, `:119`, `:132` | `cuda/cuda_flow.cu:48` `return FMAX(C(0.0), ETA - Zstar);` | `metal/fv1/metal_fv1_kernels.metal:392` `S.H = max(0.0f, U.H + Z - Zstar);` | 같음. 모두 재구성 수심의 하한을 0으로 둔다. |
| LG1-005 | 운동량 재구성 | `swe/fv1/modifiedvars.cpp:256` `return Hstar_value * U;` | `cuda/cuda_flow.cu:12` `return { Hstar, Hstar*speed(HU), Hstar*speed(HV) };` | `metal/fv1/metal_fv1_kernels.metal:393-394` `S.HU = S.H * u;` / `S.HV = S.H * v;` | 같음. 속도 분기의 임계값 차이는 LG1-006이다. |
| LG1-006 | 재구성 속도의 등호 | `swe/fv1/modifiedvars.cpp:346-349` `if (H > Solverptr->DepthThresh)` / `{` / `NUMERIC_TYPE discharge = discharge_component[j*Parptr->xsz + i];` / `return discharge / H;` | `cuda/cuda_flow.cu:56-58` `if (H >= cuda::solver_params.DepthThresh)` / `{` / `return discharge/H;` | `metal/fv1/metal_fv1_kernels.metal:389-390` `float u = (U.H > depth_thresh) ? U.HU / max(U.H, 1e-6f) : 0.0f;` / `float v = (U.H > depth_thresh) ? U.HV / max(U.H, 1e-6f) : 0.0f;` | 다름. `H == DepthThresh`에서 CUDA만 속도를 복원한다. |
| LG1-007 | HLL 건조 단락·파속·신호속도 | `swe/hll_include.h:1` `if (H_neg <= DepthThresh && H_pos <= DepthThresh)`; 식 원문은 아래 Q1이다. | `cuda/cuda_hll.cu:24-25` `if (u_neg.H <= cuda::solver_params.DepthThresh &&` / `u_pos.H <= cuda::solver_params.DepthThresh)`; `:49-52`는 Q1과 대응한다. | `metal/fv1/metal_fv1_kernels.metal:126` `if (H_neg <= depth_thresh && H_pos <= depth_thresh) {`; `:139-141`는 Q1과 대응한다. | 같음. Metal의 추가 보호 분기는 LG1-010이다. |
| LG1-008 | HLL 중간 질량·법선·접선 플럭스 | `swe/hll_include.h:77-100`의 Q2 | `cuda/cuda_hll.cu:94-114`의 Q2 대응식 | `metal/fv1/metal_fv1_kernels.metal:180-190`의 Q2 대응식 | 같음. 중간 영역에서 접선 플럭스는 접촉파 부호로 속도를 선택한다. |
| LG1-009 | y 방향 좌표와 운동량 | `swe/hll.cpp:38-40` `HLL(Solverptr, H_neg, HV_neg, -HU_neg, H_pos, HV_pos, -HU_pos,` / `H_flux, HV_flux, HU_flux);` / `HU_flux = -HU_flux;` | `cuda/cuda_hll.cu:10-15` `FlowVector u_neg_rotated = { u_neg.H, u_neg.HV, -u_neg.HU };`와 `return { F_rotated.H, -F_rotated.HV, F_rotated.HU };` | `metal/fv1/metal_fv1_simulate.mm:579` `d_HV[gpu_idx] = -(float)h_HV[cpu_idx];`; `:725` `h_HV[cpu_idx] = -(NUMERIC_TYPE)d_HV[gpu_idx];` | 다름. 해석: Metal의 남향 양의 좌표를 호스트의 북향 양의 좌표로 되돌리면 같은 보존식이다. F. |
| LG1-010 | Metal HLL 보호 연산 | CPU는 `swe/hll_include.h:33` `NUMERIC_TYPE A_neg = SQRT(g * H_neg);`에서 원 수심을 쓴다. | `cuda/cuda_hll.cu:46` `NUMERIC_TYPE A_neg = SQRT(cuda::physical_params.g * u_neg.H);` | `metal/fv1/metal_fv1_kernels.metal:123-124` `float H_neg = max(U_neg.H, 0.0f);` / `float H_pos = max(U_pos.H, 0.0f);`; `:156-157` `s_neg = min(s_neg, 0.0f);` / `s_pos = max(s_pos, 0.0f);`; `:172` `if (abs(denom) < 1e-10f) return FlowVector{0.0f, 0.0f, 0.0f};` | Metal에만 있음. 음수 수심 보호와 영 분모 근처의 단락을 별도로 적어야 한다. 단방향 신호속도 절단만으로는 다른 HLL 플럭스라고 판정하지 않는다. |

Q1. CPU HLL의 파속 추정 원문은 `swe/hll_include.h:33-39`이다.

```cpp
NUMERIC_TYPE A_neg = SQRT(g * H_neg);
NUMERIC_TYPE A_pos = SQRT(g * H_pos);

NUMERIC_TYPE H_star = pow(C(0.5)*(A_neg+A_pos) + C(0.25)*(U_neg - U_pos),
		C(2.0))	/ g;
NUMERIC_TYPE U_star = C(0.5)*(U_neg + U_pos) + A_neg - A_pos;
NUMERIC_TYPE A_star = SQRT(g*H_star);
```

Q2. CPU 중간 플럭스 원문은 `swe/hll_include.h:75-102`이다.

```cpp
else if (S_neg < C(0.0) && S_pos >= C(0.0))
{
	NUMERIC_TYPE H_flux_mid =
		(S_pos*H_flux_neg - S_neg*H_flux_pos + S_neg*S_pos*(H_pos-H_neg))
		/
		(S_pos - S_neg);
	NUMERIC_TYPE HU_flux_mid =
		(S_pos*HU_flux_neg - S_neg*HU_flux_pos + S_neg*S_pos*(HU_pos-HU_neg))
		/
		(S_pos - S_neg);

	H_flux = H_flux_mid;
	HU_flux = HU_flux_mid;

	NUMERIC_TYPE S_mid =
		(S_neg*H_pos*(U_pos - S_pos) - S_pos*H_neg*(U_neg - S_neg))
		/
		(H_pos*(U_pos-S_pos) - H_neg*(U_neg - S_neg));

	if (S_neg < C(0.0) && S_mid >= C(0.0))
	{
		HV_flux = H_flux_mid * V_neg;
	}
	else
	{
		HV_flux = H_flux_mid * V_pos;
	}
}
```

해석: `s_neg`와 `s_pos`를 0까지 절단해도 두 신호속도가 같은 부호인 영역에서는 각각 좌측 또는 우측 물리 플럭스를 선택한다.
Metal의 작은 분모 단락은 이 식 변형과 별개의 추가 조건이다.

Q1 보충. CUDA의 파속 추정 원문은 `cuda/cuda_hll.cu:46-52`이다.

```cpp
	NUMERIC_TYPE A_neg = SQRT(cuda::physical_params.g * u_neg.H);
	NUMERIC_TYPE A_pos = SQRT(cuda::physical_params.g * u_pos.H);

	NUMERIC_TYPE H_star = POW(C(0.5)*(A_neg+A_pos) + C(0.25)*(U_neg - U_pos),
			C(2.0))	/ cuda::physical_params.g;
	NUMERIC_TYPE U_star = C(0.5)*(U_neg + U_pos) + A_neg - A_pos;
	NUMERIC_TYPE A_star = SQRT(cuda::physical_params.g*H_star);
```

Metal의 파속 추정 원문은 `metal/fv1/metal_fv1_kernels.metal:139-141`이다.

```cpp
    float h_star = pow(0.5f*(a_neg + a_pos) + 0.25f*(u_neg - u_pos), 2.0f) / g;
    float u_star = 0.5f*(u_neg + u_pos) + a_neg - a_pos;
    float a_star = sqrt(g * h_star);
```

| 구성식 | CPU 원문 | CUDA 원문 | Metal 원문 | 판정 |
|---|---|---|---|---|
| HLL의 질량·이류·압력 플럭스 | `swe/hll_include.h:61-63` `NUMERIC_TYPE H_flux_neg = HU_neg;` / `NUMERIC_TYPE HU_flux_neg = U_neg*HU_neg + C(0.5)*g*H_neg*H_neg;` / `NUMERIC_TYPE HV_flux_neg = HV_neg*U_neg;` | `cuda/cuda_hll.cu:75-77` `u_neg.HU,` / `U_neg * u_neg.HU + C(0.5) * cuda::physical_params.g * u_neg.H * u_neg.H,` / `u_neg.HV*U_neg` | `metal/fv1/metal_fv1_kernels.metal:160-162` `U_neg.HU,` / `u_neg*U_neg.HU + 0.5f * g * H_neg * H_neg,` / `U_neg.HV * u_neg` | 같음. 우측 상태도 같은 식이다. |
| 왼쪽 건조 전선 | `swe/hll_include.h:44` `S_neg = U_pos - C(2.0)*A_pos;` | `cuda/cuda_hll.cu:57` `S_neg = U_pos - C(2.0)*A_pos;` | `metal/fv1/metal_fv1_kernels.metal:145` `s_neg = u_pos - 2.0f*a_pos;` | 같음. 왼쪽이 건조한 조건이다. |
| 왼쪽 습윤 신호속도 | `swe/hll_include.h:48` `S_neg = min(U_neg - A_neg, U_star - A_star);` | `cuda/cuda_hll.cu:61` `S_neg = FMIN(U_neg - A_neg, U_star - A_star);` | `metal/fv1/metal_fv1_kernels.metal:147` `s_neg = min(u_neg - a_neg, u_star - a_star);` | 같음. Metal의 후속 절단은 LG1-010이다. |
| 오른쪽 건조 전선 | `swe/hll_include.h:54` `S_pos = U_neg + C(2.0)*A_neg;` | `cuda/cuda_hll.cu:67` `S_pos = U_neg + C(2.0)*A_neg;` | `metal/fv1/metal_fv1_kernels.metal:151` `s_pos = u_neg + 2.0f*a_neg;` | 같음. 오른쪽이 건조한 조건이다. |
| 오른쪽 습윤 신호속도 | `swe/hll_include.h:58` `S_pos = max(U_pos + A_pos, U_star + A_star);` | `cuda/cuda_hll.cu:71` `S_pos = FMAX(U_pos + A_pos, U_star + A_star);` | `metal/fv1/metal_fv1_kernels.metal:153` `s_pos = max(u_pos + a_pos, u_star + a_star);` | 같음. Metal의 후속 절단은 LG1-010이다. |

Q2 보충. CUDA의 중간 플럭스·접촉파 원문은 `cuda/cuda_hll.cu:94-115`이다.

```cpp
		F.H =
			(S_pos*F_neg.H - S_neg*F_pos.H + S_neg*S_pos*(u_pos.H-u_neg.H))
			/
			(S_pos - S_neg);
		F.HU =
			(S_pos*F_neg.HU - S_neg*F_pos.HU + S_neg*S_pos*(u_pos.HU-u_neg.HU))
			/
			(S_pos - S_neg);

		NUMERIC_TYPE S_mid =
			(S_neg*u_pos.H*(U_pos - S_pos) - S_pos*u_neg.H*(U_neg - S_neg))
			/
			(u_pos.H*(U_pos-S_pos) - u_neg.H*(U_neg - S_neg));

		if (S_neg < C(0.0) && S_mid >= C(0.0))
		{
			F.HV = F.H * V_neg;
		}
		else
		{
			F.HV = F.H * V_pos;
		}
```

Metal의 중간 플럭스·접촉파 원문은 `metal/fv1/metal_fv1_kernels.metal:180-191`이다.

```cpp
        F.H = (s_pos * F_neg.H - s_neg * F_pos.H + s_pos * s_neg * (U_pos.H - U_neg.H)) / denom;
        F.HU = (s_pos * F_neg.HU - s_neg * F_pos.HU + s_pos * s_neg * (U_pos.HU - U_neg.HU)) / denom;
        
        // Transverse momentum flux (HV) using S_mid logic from hll_include.h
        float s_mid = (s_neg * H_pos * (u_pos - s_pos) - s_pos * H_neg * (u_neg - s_neg)) 
                    / (H_pos * (u_pos - s_pos) - H_neg * (u_neg - s_neg));
        
        if (s_mid >= 0.0f) {
            F.HV = F.H * v_neg;
        } else {
            F.HV = F.H * v_pos;
        }
```

세 구현의 갱신식은 질량 플럭스, 두 운동량 이류, 정수압, 바닥 경사, Manning 마찰을 포함한다.
근거는 위 질량·이류·압력 플럭스와 Q3~Q5의 갱신식이다.
강우와 점 원천은 플럭스 바깥에서 수심을 갱신한다.
근거는 Q7과 LG1-123이다.

### 2.2 FV1 보존식·마찰·시간 간격

| 행 ID | 계산 항목 | CPU 원문 | CUDA 원문 | Metal 원문 | 판정과 이유 |
|---|---|---|---|---|---|
| LG1-011 | 두 방향 보존식의 조합 | `swe/fv1.cpp:441-442`의 Q3 | `cuda/fv1/cuda_fv1_solver.cu:537-541`의 Q3. y 플럭스는 `:424` `FlowVector U_neg = Uold[(j+1)*cuda::pitch + i];`와 `:428` `U_pos = Uold[j*cuda::pitch + i];`를 읽는다. | `metal/fv1/metal_fv1_kernels.metal:555` `U_c = FlowVector{H_old[idx], HU_old[idx], HV_old[idx]};`; `:615-617`의 Q3 | 다름. 해석: 음수 수심 절단을 제외하면 같은 비분리 보존식을 다른 연산 순서로 쓴다. Metal 절단은 LG1-015이다. F. |
| LG1-012 | FV1 바닥 원천항의 수심 시점 | `swe/fv1.cpp:441-442`에서 H를 먼저 바꾼다. `:450-452`의 Q4가 `bed_source_x`를 부른다. `swe/fv1/modifiedvars.cpp:329` `NUMERIC_TYPE H = Arrptr->H[j*Parptr->xsz + i];` | `cuda/fv1/cuda_fv1_solver.cu:372` `NUMERIC_TYPE ETA = U_neg.H + Z_neg;`; `:467` `NUMERIC_TYPE ETA = U_pos.H + Z_pos;` | `metal/fv1/metal_fv1_kernels.metal:501` `float ETA = U_c.H + Z_c;`; `:611`도 같은 행이다. | 다름. CPU의 Hstar는 갱신 전 값이다. CPU의 Zdagger는 갱신 후 H를 사용한다. 두 GPU는 모두 갱신 전 상태를 사용한다. |
| LG1-013 | Manning 마찰의 기본식 | `swe/fv1.cpp:141-152`의 Q5 | `cuda/fv1/cuda_fv1_solver.cu:244-256`은 Q5의 `Tstep`을 `cuda::dt`로 바꾼다. | `metal/fv1/metal_fv1_kernels.metal:317`, `:330-337`은 같은 방향별 분모를 쓴다. | 같음. 전역 n 또는 raster n을 선택한다. 마찰이 켜진 경우에만 건조·저속 운동량을 0으로 만든다. |
| LG1-014 | Metal 마찰의 작은 값 보호 | `swe/fv1.cpp:128-129` `NUMERIC_TYPE U = HU/H;` / `NUMERIC_TYPE V = HV/H;` | `cuda/fv1/cuda_fv1_solver.cu:230-231`도 원 H로 나눈다. | `metal/fv1/metal_fv1_kernels.metal:311` `float h_safe = max(h, MIN_SAFE_H);`; `:329` `float speed_safe = speed + 1e-12f; // Very small epsilon`; `:317` `float Cf = params.g * n * n / pow(h_safe, 0.33333333f);` | Metal에만 있음. `MIN_SAFE_H`는 `:12`에서 `1e-6f`이다. 임계값을 작게 설정하면 H 보호가 활성화된다. 속도 분모의 epsilon은 별도의 정규화이다. |
| LG1-015 | 최종 음수 수심 절단 | `swe/fv1.cpp:441-442`는 절단하지 않는다. | `cuda/fv1/cuda_fv1_solver.cu:469` `H = U0.H - cuda::dt * (F_n.H - F_s.H)/cuda::geometry.dy;` | `metal/fv1/metal_fv1_kernels.metal:615` `float h_next = max(0.0f, H_int[idx] - solver.dt * (F_s.H - F_n.H) / geom.dy);` | Metal에만 있음. Metal의 질량 계수는 경계 플럭스와 배수량을 집계한다. 이 절단으로 생기는 체적은 따로 집계하지 않는다. |
| LG1-016 | 내부 셀 CFL 식 | `swe/fv1.cpp:606-611`의 Q6 | `cuda/fv1/cuda_fv1_solver.cu:86-95`의 Q6 | `metal/fv1/metal_fv1_kernels.metal:658-663`의 Q6 | 같음. 임계값과 집계 대상 차이는 다음 행에서 다룬다. |
| LG1-017 | 첫 간격·원천항에 쓰는 CUDA dt | `swe/fv1.cpp:23-30`은 adaptive일 때 `Solverptr->Tstep = 1e-6;`를 쓴다. | `cuda/cuda_solver.cu:11` `__managed__ NUMERIC_TYPE lis::cuda::dt;`; `cuda/cuda_solver.templates.cu:23-39`는 adaptive 분기에서 dt에 값을 대입하지 않는다. `cuda/fv1/cuda_fv1_simulate.cu:142-162`의 Q7은 원천항 뒤에 dt를 갱신한다. | `metal/fv1/metal_fv1_simulate.mm:1026-1029`의 Q7은 첫 간격을 CPU와 맞춘다. | 다름. CUDA의 첫 adaptive 원천항은 정적 초기값 dt=0을 읽는다. 이후 원천항은 직전 dt를 읽는다. 흐름 갱신은 새 dt를 읽는다. |
| LG1-018 | FV1 CFL 집계 대상 | `swe/fv1.cpp:594-596`은 내부 `j<Parptr->ysz`, `i<Parptr->xsz`만 순회한다. | `cuda/fv1/cuda_fv1_solver.cu:73-75`의 Q6은 ghost를 포함한다. | `metal/fv1/metal_fv1_kernels.metal:640-643`은 `gid+1`의 내부 셀만 순회한다. | 다름. CUDA는 지정 경계 상태의 CFL도 제한한다. 건조 ghost의 max_dt도 전역 최소에 참여한다. |
| LG1-019 | Metal의 fixed time step 옵션 | `swe/fv1.cpp:61` `if (Statesptr->adaptive_ts == ON)` | `cuda/cuda_solver.templates.cu:76` `if (adaptive)` | `metal/fv1/metal_fv1_simulate.mm:1024` `NUMERIC_TYPE adaptive_dt = computeTimestep();`; `:1027` `adaptive_dt = states->adaptive_ts == ON ? (NUMERIC_TYPE)1e-6 : max_dt;` | 다름. Metal은 첫 간격 이후 `adaptive_ts`를 검사하지 않는다. |
| LG1-020 | Metal CFL 건조 임계값 | `swe/fv1.cpp:599` `if (H > Solverptr->DepthThresh)` | `cuda/fv1/cuda_fv1_solver.cu:79` `if (H > cuda::solver_params.DepthThresh)` | `metal/fv1/metal_fv1_kernels.metal:648` `if (h > DEPTH_THRESH) {`; `:11` `#define DEPTH_THRESH 1e-3f` | 다름. Metal의 재구성·마찰은 입력 depth_thresh를 쓰지만 CFL은 고정 임계값을 쓴다. |

Q3. CPU 보존식은 `swe/fv1.cpp:441-442`이다.

```cpp
			H = H - Solverptr->Tstep *
				((H_e - H_w)/Parptr->dx + (H_n - H_s)/Parptr->dy);
```

CUDA 호출은 `cuda/fv1/cuda_fv1_solver.cu:537-541`이다.

```cpp
	update_flow_variables_x<<<grid_size, cuda::block_size>>>
			(Uold, Ux, DEM, Zstar_x, mass_stats);

	update_flow_variables_y<<<grid_size, cuda::block_size>>>
			(Uold, Ux, U, DEM, Zstar_y, mass_stats);
```

CUDA의 y 갱신은 `cuda/fv1/cuda_fv1_solver.cu:459-472`이다.
중간 배열을 읽는 행은 `FlowVector U0 = Uint[j*cuda::pitch + i];`이다.
갱신식 원문은 다음과 같다.

```cpp
				H = U0.H - cuda::dt * (F_n.H - F_s.H)/cuda::geometry.dy;
				HU = U0.HU - cuda::dt * (F_n.HU - F_s.HU)/cuda::geometry.dy;
				HV = U0.HV - cuda::dt * ((F_n.HV - F_s.HV)/cuda::geometry.dy
					- bed_source_y(Zstar_s, Zstar_n, Ustar_pos.H, Hstar_n, ETA));
```

Metal의 y 갱신은 `metal/fv1/metal_fv1_kernels.metal:615-617`이다.

```cpp
    float h_next = max(0.0f, H_int[idx] - solver.dt * (F_s.H - F_n.H) / geom.dy);
    float hu_next = HU_int[idx] - solver.dt * (F_s.HU - F_n.HU) / geom.dy;
    float hv_next = HV_int[idx] - solver.dt * ((F_s.HV - F_n.HV) / geom.dy - bed_src);
```

Q4. CPU 운동량식은 `swe/fv1.cpp:450-452`이다.

```cpp
			HU = HU - Solverptr->Tstep *
				((HU_e - HU_w)/Parptr->dx + (HU_n - HU_s)/Parptr->dy
				 - bed_source_x(Parptr, Solverptr, Arrptr, i, j));
```

바닥 원천항 자체는 세 구현이 같은 정수압 형식을 쓴다.
CPU 원문은 `swe/fv1.cpp:481-482`이다.

```cpp
	return -Solverptr->g * C(0.5)*(Hstar_neg + Hstar_pos)
		* (Zdagger_neg - Zdagger_pos)/Parptr->dx;
```

CPU의 Zdagger 원문은 `swe/fv1/modifiedvars.cpp:314-317`이다.

```cpp
	NUMERIC_TYPE Zstar_value = Zstar[Zstar_j*(Parptr->xsz+1) + Zstar_i];
	NUMERIC_TYPE ETA = eta(Parptr, Arrptr, ETA_i, ETA_j);

	return Zstar_value - getmax(C(0.0), -(ETA - Zstar_value));
```

해석: 수면이 두 계면 바닥보다 높으면 Zdagger는 Zstar와 같다.
LG1-012의 차이는 수면이 계면 바닥 아래로 내려가는 가지에서 결과에 영향을 줄 수 있다.

| 바닥항 함수식 | CPU 원문 | CUDA 원문 | Metal 원문 |
|---|---|---|---|
| x | `swe/fv1.cpp:481-482` `return -Solverptr->g * C(0.5)*(Hstar_neg + Hstar_pos)` / `* (Zdagger_neg - Zdagger_pos)/Parptr->dx;` | `cuda/fv1/cuda_fv1_solver.cu:273-274` `return -cuda::physical_params.g * C(0.5) * (Hstar_w + Hstar_e)` / `* (Zdagger_e - Zdagger_w)/cuda::geometry.dx;` | `metal/fv1/metal_fv1_kernels.metal:277` `return -g * 0.5f * (Hstar_w + Hstar_e) * (Zdagger_e - Zdagger_w) / dx;` |
| y | `swe/fv1.cpp:499-500` `return -Solverptr->g * 0.5*(Hstar_neg + Hstar_pos)` / `* (Zdagger_neg - Zdagger_pos)/Parptr->dy;` | `cuda/fv1/cuda_fv1_solver.cu:289-290` `return -cuda::physical_params.g * C(0.5) * (Hstar_s + Hstar_n)` / `* (Zdagger_n - Zdagger_s)/cuda::geometry.dy;` | `metal/fv1/metal_fv1_kernels.metal:284` `return -g * 0.5f * (Hstar_n + Hstar_s) * (Zdagger_s - Zdagger_n) / dy;` |

해석: y 바닥항의 Metal 부호는 LG1-009의 HV 부호 변환을 적용하면 대응한다.
이 대응은 LG1-012의 수심 시점 차이를 없애지 않는다.

Q5. CPU 마찰식은 `swe/fv1.cpp:141-152`이다.

```cpp
			NUMERIC_TYPE Cf = Solverptr->g*n*n / pow(H, C(1.0)/C(3.0));
			NUMERIC_TYPE speed = SQRT(U*U+V*V);

			NUMERIC_TYPE Sf_x = -Cf*U*speed;
			NUMERIC_TYPE Sf_y = -Cf*V*speed;
			NUMERIC_TYPE D_x = C(1.0) + Solverptr->Tstep*Cf / H
				* (C(2.0)*U*U+V*V)/speed;
			NUMERIC_TYPE D_y = C(1.0) + Solverptr->Tstep*Cf / H
				* (U*U+C(2.0)*V*V)/speed;

			HU += Solverptr->Tstep*Sf_x/D_x;
			HV += Solverptr->Tstep*Sf_y/D_y;
```

CUDA 마찰식의 대응 원문은 `cuda/fv1/cuda_fv1_solver.cu:244-256`이다.

```cpp
			NUMERIC_TYPE Cf = cuda::physical_params.g * n * n /
				POW(H, C(1.0)/C(3.0));
			NUMERIC_TYPE speed = SQRT(U*U+V*V);

			NUMERIC_TYPE Sf_x = -Cf*U*speed;
			NUMERIC_TYPE Sf_y = -Cf*V*speed;
			NUMERIC_TYPE D_x = C(1.0) + cuda::dt*Cf / H
				* (C(2.0)*U*U+V*V)/speed;
			NUMERIC_TYPE D_y = C(1.0) + cuda::dt*Cf / H
				* (U*U+C(2.0)*V*V)/speed;

			HU += cuda::dt*Sf_x/D_x;
			HV += cuda::dt*Sf_y/D_y;
```

Metal의 Cf는 `metal/fv1/metal_fv1_kernels.metal:317` `float Cf = params.g * n * n / pow(h_safe, 0.33333333f);`이다.
Metal 마찰 갱신의 원문은 같은 파일의 `:329-337`이다.

```cpp
        float speed_safe = speed + 1e-12f; // Very small epsilon
        float denom_x = 1.0f + solver.dt * Cf / h_safe * (2.0f * u * u + v * v) / speed_safe;
        float denom_y = 1.0f + solver.dt * Cf / h_safe * (u * u + 2.0f * v * v) / speed_safe;
        
        float Sf_x = -Cf * u * speed;
        float Sf_y = -Cf * v * speed;
        
        HU[idx] = hu + solver.dt * Sf_x / denom_x;
        HV[idx] = hv + solver.dt * Sf_y / denom_y;
```

해석: y 운동량과 y 마찰력의 부호가 함께 바뀐다.
속력과 방향별 분모의 제곱항은 그 부호 변환에 영향을 받지 않는다.
안전 값에 따른 정확한 식 차이는 LG1-014에 남는다.

Q6. CPU CFL 식은 `swe/fv1.cpp:606-611`이다.

```cpp
				NUMERIC_TYPE dt_x = Solverptr->cfl*Parptr->dx
					/ (FABS(U)+SQRT(Solverptr->g*H));
				NUMERIC_TYPE dt_y = Solverptr->cfl*Parptr->dy
					/ (FABS(V)+SQRT(Solverptr->g*H));

				dt = (std::min)({dt, dt_x, dt_y});
```

CUDA 순회 조건은 `cuda/fv1/cuda_fv1_solver.cu:73-75`이다.

```cpp
	for (int j=global_j; j<cuda::geometry.ysz+2; j+=blockDim.y*gridDim.y)
	{
		for (int i=global_i; i<cuda::pitch; i+=blockDim.x*gridDim.x)
```

CUDA wet 셀별 식은 `cuda/fv1/cuda_fv1_solver.cu:86-91`이다.

```cpp
				NUMERIC_TYPE dt_x = cuda::solver_params.cfl * cuda::geometry.dx
					/ (FABS(U)+SQRT(cuda::physical_params.g * H));
				NUMERIC_TYPE dt_y = cuda::solver_params.cfl * cuda::geometry.dy
					/ (FABS(V)+SQRT(cuda::physical_params.g * H));

				dt[j*cuda::pitch + i] = FMIN(dt_x, dt_y);
```

건조 가지의 전체 대입식은 `cuda/fv1/cuda_fv1_solver.cu:95` `dt[j*cuda::pitch + i] = cuda::solver_params.max_dt;`이다.

Metal 셀별 식은 `metal/fv1/metal_fv1_kernels.metal:658-664`이다.

```cpp
        float dt_x = geom.dx / (abs(u) + c);
        float dt_y = geom.dy / (abs(v) + c);
        
        dt_field[idx] = cfl * min(dt_x, dt_y);
    } else {
        dt_field[idx] = max_dt;
    }
```

Q7. CUDA 순서는 `cuda/fv1/cuda_fv1_simulate.cu:155-162`이다.
동적·균일 강우 호출은 그 앞의 `:142-153`이다.

```cpp
		stats_collector.zero_instantaneous_mass();
		cuda::Boundary::update_time_series(solver.t);
		cuda::Boundary::update_point_sources(d_U.H, DEM,
				stats_collector.instantaneous_mass());
		stats_collector.accumulate_mass();
		stats_collector.zero_instantaneous_mass();
		solve->update_ghost_cells();
		dynamic_dt.update_dt();
```

Metal의 첫 간격 분기는 `metal/fv1/metal_fv1_simulate.mm:1026-1029`이다.

```cpp
    if (is_first_step) {
      adaptive_dt = states->adaptive_ts == ON ? (NUMERIC_TYPE)1e-6 : max_dt;
      is_first_step = false;
    }
```

### 2.3 FV1 경계·점 원천·NoData

| 행 ID | 계산 항목 | CPU 원문 | CUDA 원문 | Metal 원문 | 판정과 이유 |
|---|---|---|---|---|---|
| LG1-021 | 수위 경계의 내부 상태 | `swe/fv1.cpp:531-532` `H_outside = FMAX(C(0.0), BCptr->BC_Val[bc_i] - Z);` / `//H_inside = H_outside;` | `cuda/cuda_boundary.cu:400-403` `case HFIX2:` / `case HVAR3:` / `U_const.H = U_outside.H;` / `break;` | `metal/fv1/metal_fv1_kernels.metal:64-67`은 out만 바꾼다. | 다름. CUDA만 리만 문제의 내부 수심도 외부 지정 수심으로 바꾼다. |
| LG1-022 | 유량 경계의 접선 운동량·작은 유량 기준 | `swe/fv1.cpp:549` `if (FABS(HU_outside) > C(1e-12))`; `:558` `HV_outside = HV_inside;` | `cuda/cuda_boundary.cu:355-356` `U_outside.HV = C(0.0);` / `if (FABS(U_outside.HU) > C(1e-6))` | `metal/fv1/metal_fv1_kernels.metal:70` `if (abs(out.Qn) > 1e-12f) {`; `:77` `out.Qt = in.Qt;` | 다름. CUDA의 유량 경계는 접선 운동량을 제거한다. CUDA의 수심 보정 문턱은 CPU·Metal보다 크다. |
| LG1-023 | FREE·벽 경계의 접선 복사 | `swe/fv1.cpp:526`과 `:578` `HV_outside = HV_outside;` | `cuda/cuda_boundary.cu:342` `FlowVector U_outside = { U_const.H, U_const.HU, U_const.HV };` | `metal/fv1/metal_fv1_kernels.metal:81`과 `:85` `out.Qt = in.Qt;` | 다름. CPU 호출자는 outside 운동량을 0으로 초기화한다. CPU는 접선 운동량을 복사하지 않는다. |
| LG1-024 | HFIX·HVAR 점 원천의 수심 | `swe/fv1.cpp:207` `NUMERIC_TYPE H_new = FMIN(C(0.0), BCptr->PS_Val[ps_i] - Z);`; `swe/dg2.cpp:144`도 `min`이다. | `cuda/cuda_boundary.cu:115-116` `NUMERIC_TYPE H_new = FMIN(C(0.0),` / `cuda::boundaries.PS_value[i] - Z);` | `metal/fv1/metal_fv1_simulate.mm:924`과 `:931` `float h_new = std::max(0.0f, h_target - z);` | 다름. CPU·CUDA는 양의 목표 수심을 0으로 만든다. CPU·CUDA는 지반 아래 목표 수위에서 음수 수심을 만든다. |
| LG1-025 | QFIX·QVAR 점 원천의 단위 | `swe/fv1.cpp:228` `H += Q * Parptr->dx * Solverptr->Tstep / Parptr->dA;` | `cuda/cuda_boundary.cu:128` `Hvalue += discharge * cuda::dt / cuda::geometry.dx;`; `:131` `discharge * cuda::geometry.dx);` | `metal/fv1/metal_fv1_simulate.mm:938` `float Q_total = is_q_type ? (val * dx) : val;`; `:944` `float dH = (Q_total * dt) / cell_area;` | 다름. 해석: 정사각 셀에서 세 식은 같다. CUDA 식의 직사각 셀 확장은 CPU 식과 다르다. 입력 격자 제약은 §2.6에서 확인한다. F. |
| LG1-026 | 작은 점 원천 무시 | CPU는 `swe/fv1.cpp:202-240`의 switch에서 바로 적용한다. | CUDA는 `cuda/cuda_boundary.cu:109-134`의 switch에서 바로 적용한다. | `metal/fv1/metal_fv1_simulate.mm:937` `if (std::abs(val) > 1e-9f) {` | Metal에만 있음. 이 문턱은 유량형과 수위형에서 서로 다른 단위의 val에 적용된다. |
| LG1-027 | NoData 배수의 수심·운동량 | `swe/fv1.cpp:174` `if (FABS(Z - Parptr->nodata_elevation) < 1e-6)`; `:178` `H = C(0.0);` | `cuda/cuda_boundary.cu:284` `if (FABS(Z - cuda::solver_params.nodata_elevation) < C(1e-6))`; `:288` `Hval = C(0.0);` | `metal/fv1/metal_fv1_kernels.metal:911-915`의 Q8 | 다름. Metal은 NoData 판별 허용차를 1로 둔다. Metal은 HU·HV도 0으로 만든다. CPU·CUDA는 이 함수에서 H만 0으로 만든다. |
| LG1-028 | NoData 수치 기준면 | CPU는 `swe/fv1/modifiedvars.cpp:328` `NUMERIC_TYPE Z = Arrptr->DEM[j*Parptr->xsz + i];`의 원 지형을 사용한다. | CUDA는 `cuda/cuda_dem.cu:84-85`에서 원 NoData를 지정 NoData로 치환한다. | `metal/fv1/metal_fv1_simulate.mm:531` `dem_offset = any_valid ? (float)min_valid : 0.0f;`; `:537` `gpu_nodata = (float)(max_valid - min_valid) + kMargin;  // wall`; `:539` `gpu_nodata = -kMargin;                                   // pit` | Metal에만 있음. 유효 지형의 일정 기준면 이동은 식 변형이다. NoData를 ±1000 m 여유로 재배치하는 부분은 단순 기준면 이동이 아니다. |
| LG1-029 | CPU 배수 질량 집계의 동시 갱신 | `swe/fv1.cpp:167` `#pragma omp parallel for`; `:180-181` `accumulate_point_flux_stats(BCptr,` / `-Hold*Parptr->dA/Solverptr->Tstep);`; `swe/stats.cpp:58` `BCptr->Qin += Q;`; `:62` `BCptr->Qout -= Q;` | `cuda/cuda_boundary.cu:88` `atomicAdd(&(mass_stats->in), discharge);`; `:92` `atomicAdd(&(mass_stats->out), -discharge);` | `metal/fv1/metal_fv1_kernels.metal:912`은 atomic_add_float를 쓴다. | 다름. CPU 배수는 병렬 루프에서 공유 Qin·Qout을 보호하지 않는다. CPU 경계 집계는 `swe/stats.cpp:78`의 reduction을 쓴다. |

Q8. Metal 배수 원문은 `metal/fv1/metal_fv1_kernels.metal:911-916`이다.

```cpp
    if (abs(z - nodata) < 1.0f) {
        if (H[idx] > 0.0f) atomic_add_float(&mass_totals[2], H[idx] * geom.dx * geom.dy);
        H[idx] = 0.0f;
        HU[idx] = 0.0f;
        HV[idx] = 0.0f;
    }
```

### 2.4 DG2 CPU·CUDA

이 절의 CPU는 실제 진입점인 `swe/dg2.cpp`이다.
별도 구현 `swe/dg2new.cpp`는 §2.5에 둔다.
Metal에는 DG2 계산 경로가 없다.
근거는 `lisflood.cpp:778-796`의 FV1 전용 Metal 분기와 CPU DG2 호출이다.

| 행 ID | 계산 항목 | CPU 원문 | CUDA 원문 | 판정 | 이유 |
|---|---|---|---|---|---|
| LG1-040 | 상태 계수와 면 값 | `swe/dg2.cpp:759-767`은 H·HU·HV의 평균·x 기울기·y 기울기를 연결한다. `swe/dg2/modifiedvars.cpp:654` `return constant + SQRT(C(3.0))*slope;`; `:659` `return constant - SQRT(C(3.0))*slope;` | `cuda/dg2/cuda_dg2_flow.cu:88-89`의 Q9. `get_0`, `neg_x`, `pos_x`, `neg_y`, `pos_y`가 대응한다. | 같음 | 각 변수에 같은 정규화의 선형 기저를 쓴다. |
| LG1-041 | 정수압 재구성과 수정 계수 | `swe/dg2/modifiedvars.cpp:104` `Hstar_neg_x = getmax(C(0.0), ETA_neg_x - Zstar_x);`; `:234` `if (H >= Solverptr->DepthThresh)`; `:281` `return (Hstar_neg_x - Hstar_pos_x)/(C(2.0)*SQRT(C(3.0)));` | `cuda/dg2/cuda_dg2_solver.cu:244` `Ustar_neg = U_w.neg_x().star(Z_neg, Zstar);`; `:273-274`의 Q9 | 같음 | Hstar의 평균·기울기 복원은 같다. HUstar·HVstar도 각 면의 유속을 유지한다. CPU DG2의 등호는 CUDA와 같다. |
| LG1-042 | 지배식의 평균·기울기 연산자 | `swe/dg2.cpp:819` `U_inc.H = -((H_e - H_w)/Parptr->dx + (H_n - H_s)/Parptr->dy);`; `:885-890`의 Q10 | `cuda/dg2/cuda_dg2_solver.cu:278-282`의 Q10. y 방향은 `:368-372`이다. | 같음 | 평균은 플럭스 차분을 쓴다. 기울기는 두 면 플럭스와 두 가우스점 물리 플럭스를 쓴다. |
| LG1-043 | 바닥 원천항의 평균·기울기 | `swe/dg2.cpp:961` `return C(2.0)*SQRT(C(3.0)) * Solverptr->g * Hstar * Zdagger / Parptr->dx;`; `:993` `return C(2.0) * Solverptr->g * Hstar * Zdagger;` | `cuda/dg2/cuda_dg2_solver.cu:165-166`의 Q10 | 다름 | 해석: CPU는 바깥의 음의 부호와 기울기 연산자 계수를 포함시킨다. CUDA는 완성된 음의 원천항을 더한다. 두 식은 같다. F. |
| LG1-044 | RK2 시간 적분 | `swe/dg2.cpp:704-705`, `:749-750`의 Q11 | `cuda/dg2/cuda_dg2_solver.cu:391-438`의 Q11 | 다름 | 해석: x·y 기여를 별도 커널에서 누적하지만 각 단계는 같은 입력 상태를 읽는다. 같은 RK2이다. F. |
| LG1-045 | 마찰용 가우스점의 평균값 시점 | `swe/dg2/friction.cpp:27` `friction(Solverptr, H, HU, HV, n);` 다음에 `:33-40`의 Q12를 읽는다. | `cuda/dg2/cuda_dg2_solver.cu:651` `FlowCoeffs U(Uref);`; `:653-667`에서 가우스점을 먼저 만들고 `:673` `friction(n, U.H, Uref.HU, Uref.HV);`를 부른다. | 다름 | CPU는 이미 마찰을 적용한 평균 운동량으로 가우스점을 만든다. CUDA는 마찰 전 평균 운동량으로 가우스점을 만든다. |
| LG1-046 | 마찰의 저속 가지 | `swe/dg2/friction.cpp:91-94`의 Q12는 운동량을 유지한다. | `cuda/dg2/cuda_dg2_solver.cu:616-622`의 Q12는 HU·HV를 0으로 만든다. | 다름 | 같은 SpeedThresh의 다른 결과이다. FV1 CPU의 저속 가지와 CPU DG2의 저속 가지도 다르다. |
| LG1-047 | 마찰의 건조 평균 셀 | `swe/dg2/friction.cpp:25` `if (H <= Solverptr->DepthThresh) continue;` | `cuda/dg2/cuda_dg2_solver.cu:673-683`은 평균과 네 가우스점에 friction을 적용한다. | 다름 | CPU는 평균 수심이 임계값 이하이면 가우스점 마찰도 건너뛴다. CUDA는 각 점의 수심으로 판단한다. |
| LG1-048 | 기울기 제한의 기본 분기·minmod | `swe/dg2/slope_limiter.cpp:298` `if (stencil_minH <= C(0.30) * Solverptr->maxH) return local_slope;`; `:320-327`의 Q13 | `cuda/dg2/cuda_dg2_slope_limit.cu:15` `if (stencil_minH <= C(0.30)*cuda::dg2::maxH) return local_slope;`; `:36-43`의 같은 minmod 식 | 같음 | 깊이 분기와 Krivodonova 판정 후의 minmod 계산은 대응한다. |
| LG1-049 | 기울기 제한의 작은 norm 기준 | `swe/dg2/slope_limiter.cpp:314` `if (FABS(norm) > C(1e-12))` | `cuda/dg2/cuda_dg2_slope_limit.cu:30` `if (FABS(norm) > C(1e-6))` | 다름 | 임계값 사이에서는 CPU만 DS를 계산한다. float·double 전처리 분기는 없다. |
| LG1-050 | y 방향 최소 수심의 기울기 | `swe/dg2/slope_limiter.cpp:381` `NUMERIC_TYPE backward_H1x = U.H1x[(j + 1) * Parptr->xsz + i];`; `:383`, `:385`도 H1x이다. | `cuda/dg2/cuda_dg2_slope_limit.cu:101` `NUMERIC_TYPE backward1y = flow.H1y[(j+1)*cuda::pitch + i];`; `:103`, `:105`도 H1y이다. | 다름 | CPU의 y stencil이 x 기울기를 읽는다. 같은 CPU 함수의 `eta1y`와 `HU1y` 제한은 y 기울기를 읽는다. |
| LG1-051 | CUDA 최소 수심 검사 중 읽기·쓰기 | CPU는 `swe/dg2/slope_limiter.cpp:121-126`에서 scratch에 결과를 쓴다. `:171-172`에서 별도 루프로 H1x에 반영한다. | `cuda/dg2/cuda_dg2_solver.cu:810-812`의 Q14. `cuda/dg2/cuda_dg2_slope_limit.cu:79`은 이웃 `flow.H1x`를 읽는다. | CUDA에만 있음 | limiter 커널이 이웃의 H1x·H1y를 읽는 동안 같은 커널의 다른 스레드가 그 필드를 덮어쓴다. 복사해 둔 slopes 배열은 이 최소 수심 검사에 사용하지 않는다. |
| LG1-052 | limit_slopes=ON에서 둘레의 접선 기울기 | `swe/dg2/slope_limiter.cpp:109`은 모든 j의 x 내부 셀을 제한한다. `:211-213`은 y 내부 행의 모든 i를 제한한다. | `cuda/dg2/cuda_dg2_solver.cu:926` `zero_perimeter_slopes(DEM, Uold);`; `:734-739`는 북쪽 둘레의 두 방향 기울기를 모두 0으로 만든다. | 다름 | CUDA는 limiter를 적용한 뒤에도 둘레 전체의 두 방향 기울기를 없앤다. CPU는 limiter가 꺼진 가지에서만 zero_perimeter_slopes를 부른다. |
| LG1-053 | limiter에 쓰는 전역 maxH | `swe/dg2.cpp:62` `if (Parptr->limit_slopes == ON) Solverptr->maxH = maxH(Parptr, Arrptr);`는 강우·점 원천보다 앞선다. | `cuda/dg2/cuda_dg2_solver.cu:917` `maxH.update(Uold);`는 강우·점 원천 뒤이다. `cuda/dg2/cuda_dg2_slope_limit.cu:299-300`은 ghost 포함 elements를 reduction한다. | 다름 | 0.30 분기의 기준 상태와 집계 영역이 다르다. |
| LG1-054 | 얇은 수심 기울기 제거 | `swe/dg2.cpp:1066` `return H <= C(10.0) * Solverptr->DepthThresh; // thin layer depth is 10*thresh`; `:39`은 호출을 주석 처리한다. | `cuda/dg2/cuda_dg2_solver.cu:485` `if (U.H <= C(10.0)*cuda::solver_params.DepthThresh)`; `:882-893`은 호출 가능한 wrapper를 제공한다. | 같음 | 대상 simulate·RK 호출 경로는 이 제거 함수를 호출하지 않는다. 함수가 있다는 이유로 매 단계 제거한다고 쓰면 안 된다. |
| LG1-055 | RK 단계 뒤 건조 운동량 제거 | `swe/dg2.cpp:1201` `if (H[j*Parptr->xsz + i] < Solverptr->DepthThresh)`; `:1203-1208`은 평균과 운동량 기울기를 0으로 만든다. | `cuda/dg2/cuda_dg2_solver.cu:456` `if (U.H < cuda::solver_params.DepthThresh)`; `:458-463`은 같은 여섯 계수를 0으로 만든다. | 같음 | 두 구현 모두 이 함수에서 H·H1x·H1y를 절단하지 않는다. |
| LG1-056 | DG2 CFL | `swe/dg2.cpp:1174-1176`은 dt·dt_x·dt_y의 최소이다. `:1093-1151`은 네 경계 상태도 검사한다. | `cuda/dg2/cuda_dg2_solver.cu:75-79`의 같은 식. `:98-105`은 ghost를 포함한다. | 같음 | 두 구현 모두 평균 상태와 경계 상태를 제한한다. 강우·점 원천에 사용한 dt와 흐름 dt의 시간 순서는 LG1-017과 별도로 주의한다. |
| LG1-057 | FREE 경계의 건조 수심·기울기 | `swe/dg2.cpp:618-621`의 Q14는 H_const와 H_outside만 0으로 만든다. | `cuda/dg2/cuda_dg2_solver.cu:518-523`의 Q14는 H1x·H1y도 0으로 만든다. | 다름 | CPU는 첫 경계 갱신과 단계별 플럭스 갱신에서 평균 H를 바꿀 수 있다. CUDA는 ghost 갱신에서 수심 기울기도 없앤다. |
| LG1-058 | RK2 경계 질량 | `swe/dg2.cpp:79` `accumulate_boundary_flux_stats(Parptr, Solverptr, BCptr, Arrptr);`는 두 RK 단계 뒤 한 번 호출한다. | `cuda/dg2/cuda_dg2_solver.cu:264` `update_mass_stats_x(mass_stats, F_e.H, i, j, C(0.5));`; `:353`도 0.5를 쓴다. | 다름 | CPU의 FHx·FHy에는 둘째 단계 플럭스만 남는다. CUDA는 각 단계 플럭스의 절반을 적분한다. |
| LG1-059 | DG2의 NoData 배수 | `swe/dg2.cpp:74-85`에는 배수 호출이 없다. | `cuda/dg2/cuda_dg2_simulate.cu:170-174`의 Q14는 drain_nodata를 적용한다. | CUDA에만 있음 | CPU FV1의 배수 호출을 CPU DG2에도 있다고 일반화하면 안 된다. |

Q9. DG2 계수 재구성 원문은 `cuda/dg2/cuda_dg2_flow.cu:88-89`이다.

```cpp
	return { H + SQRT(C(3.0))*H1x, HU + SQRT(C(3.0))*HU1x,
		HV + SQRT(C(3.0))*HV1x };
```

수정 계수 복원은 `cuda/dg2/cuda_dg2_solver.cu:273-274`이다.

```cpp
				FlowVector Ustar_0x = C(0.5)*(Ustar_pos + Ustar_neg);
				FlowVector Ustar_1x = (Ustar_neg - Ustar_pos)/(C(2.0)*SQRT(C(3.0)));
```

Q10. CPU 기울기 연산자는 `swe/dg2.cpp:885-890`이다.

```cpp
	U_inc.H1x = -SQRT(C(3.0))/Parptr->dx*(H_w + H_e - H_g1_flux - H_g2_flux);
	U_inc.HU1x = -SQRT(C(3.0))/Parptr->dx*(HU_w + HU_e
			- HU_g1_flux - HU_g2_flux
			+ bed_source_1x(Parptr, Solverptr, Arrptr, U, i, j));
	U_inc.HV1x = -SQRT(C(3.0))/Parptr->dx*(HV_w + HV_e
			- HV_g1_flux - HV_g2_flux);
```

CUDA 기울기 연산자는 `cuda/dg2/cuda_dg2_solver.cu:278-282`이다.

```cpp
					Lx.set_0(-(F_e - F_w)/cuda::geometry.dx);
					Lx.set_1x(-SQRT(C(3.0))/cuda::geometry.dx * (F_w + F_e
								- (Ustar_0x - Ustar_1x).physical_flux_x()
								- (Ustar_0x + Ustar_1x).physical_flux_x()));
					Lx += bed_source_x(Ustar_0x.H, Ustar_1x.H, DEM, U_w, i, j);
```

CUDA 바닥 원천항은 `cuda/dg2/cuda_dg2_solver.cu:165-166`이다.

```cpp
	Sbx.HU = -C(2.0)*SQRT(C(3.0)) * g*Hstar_0x*Zdagger_1x / cuda::geometry.dx;
	Sbx.HU1x = -C(2.0)*SQRT(C(3.0)) * g*Hstar_1x*Zdagger_1x / cuda::geometry.dx;
```

해석: CPU의 `bed_source_1x`에 `-sqrt(3)/dx`를 곱하면 CUDA의 `Sbx.HU1x`가 된다.
이 변형은 y 방향의 HV1y에도 성립한다.
두 코드의 가우스점은 수정 평균에서 수정 기울기를 빼거나 더한 값이다.
근거는 `swe/dg2/modifiedvars.cpp:664` `return constant - slope;`, `:669` `return constant + slope;`와 `cuda/dg2/cuda_dg2_flow.cu:116` `return { H - H1x, HU - HU1x, HV - HV1x };`이다.

Q11. CPU RK2는 `swe/dg2.cpp:704-705`, `:749-750`이다.

```cpp
	field_int[j*Parptr->xsz + i] = field_n[j*Parptr->xsz + i]
		+ Solverptr->Tstep * increment;
```

```cpp
	field_n[j*Parptr->xsz + i] = C(0.5)*(field_n[j*Parptr->xsz + i]
		+ field_int[j*Parptr->xsz + i] + Solverptr->Tstep * increment);
```

CUDA 네 호출의 완전한 반환식은 `cuda/dg2/cuda_dg2_solver.cu:391-392`, `:406-407`, `:421-423`, `:437-438`이다.

```cpp
	update_flow_variables_x(DEM, Uold, Ux, [&](int i, int j, FlowCoeffs Lx)
			{ return Uold[j*cuda::pitch + i] + cuda::dt*Lx; }, mass_stats);
```

```cpp
	update_flow_variables_y(DEM, Uold, Uint, [&](int i, int j, FlowCoeffs Ly)
			{ return Ux[j*cuda::pitch + i] + cuda::dt*Ly; }, mass_stats);
```

```cpp
	update_flow_variables_x(DEM, Uint, Ux, [&](int i, int j, FlowCoeffs Lx)
			{ return C(0.5)*(Uold[j*cuda::pitch + i] + 
					Uint[j*cuda::pitch + i] + cuda::dt*Lx); }, mass_stats);
```

```cpp
	update_flow_variables_y(DEM, Uint, U, [&](int i, int j, FlowCoeffs Ly)
			{ return Ux[j*cuda::pitch + i] + C(0.5)*cuda::dt*Ly; }, mass_stats);
```

Q12. CPU는 평균 운동량 마찰 뒤에 다음 가우스점 운동량을 읽는다.
원문 위치는 `swe/dg2/friction.cpp:33-40`이다.

```cpp
                NUMERIC_TYPE HU_x_lower = gauss_lower(Arrptr->HU, Arrptr->HU1x,
                        Parptr, i, j);
                NUMERIC_TYPE HU_x_upper = gauss_upper(Arrptr->HU, Arrptr->HU1x,
                        Parptr, i, j);
                NUMERIC_TYPE HV_x_lower = gauss_lower(Arrptr->HV, Arrptr->HV1x,
                        Parptr, i, j);
                NUMERIC_TYPE HV_x_upper = gauss_upper(Arrptr->HV, Arrptr->HV1x,
                        Parptr, i, j);
```

CPU 저속 가지는 `swe/dg2/friction.cpp:91-94`이다.

```cpp
	if (FABS(U) <= Solverptr->SpeedThresh && FABS(V) <= Solverptr->SpeedThresh)
	{
		return;
	}
```

CUDA 저속 가지는 `cuda/dg2/cuda_dg2_solver.cu:616-622`이다.

```cpp
    if (FABS(U) <= cuda::solver_params.SpeedThresh
		&& FABS(V) <= cuda::solver_params.SpeedThresh)
    {
        HU = C(0.0);
        HV = C(0.0);
        return;
    }
```

Q13. CPU minmod 적용 조건과 식은 `swe/dg2/slope_limiter.cpp:320-328`이다.

```cpp
	if (FMAX(DS_backward, DS_forward) >= Solverptr->krivodonova_threshold)
	{
		return minmod
		(
			local_slope,
			(local_const - backward_const) / SQRT(C(3.0)),
			(forward_const - local_const) / SQRT(C(3.0))
		);
	}
```

Q14. CUDA limiter의 읽기·쓰기 순서는 `cuda/dg2/cuda_dg2_solver.cu:810-812`이다.

```cpp
			NUMERIC_TYPE minH_x = Stencil::minH_x(flow, i, j);
			Stencil ETA_stencil_x = slopes.ETA_stencil_x(DEM._0, flow.H, i, j);
			U.H1x = ETA_stencil_x.limit(cuda::geometry.dx, minH_x) - Z1x;
```

CPU FREE 건조 처리는 `swe/dg2.cpp:618-621`이다.

```cpp
		if (H_const <= Solverptr->DepthThresh){
			H_const = C(0.0);
		    H_outside = C(0.0);
	    }
```

CUDA FREE 건조 처리는 `cuda/dg2/cuda_dg2_solver.cu:518-523`이다.

```cpp
			if (cuda::boundaries.BC_type[Boundary::index_w(i, j)] == FREE1 && flow[j * cuda::pitch + i].H <= cuda::solver_params.DepthThresh) {
				flow[j * cuda::pitch + i].H = C(0.0);
				flow[j * cuda::pitch + i].H1x = C(0.0);
				flow[j * cuda::pitch + i].H1y = C(0.0);
				U_outside.H = C(0.0);
			}
```

CUDA DG2 배수 호출은 `cuda/dg2/cuda_dg2_simulate.cu:170-174`이다.

```cpp
		if (pars.drain_nodata)
		{
			cuda::Boundary::drain_nodata_water(d_U.H, d_DEM._0, 
					stats_collector.instantaneous_mass(), grid_size);
		}
```

### 2.5 별도 CPU 구현 dg2new

| 행 ID | 계산 항목 | dg2new 원문 | 실행되는 CPU·CUDA 원문 | 판정 | 이유 |
|---|---|---|---|---|---|
| LG1-080 | 면 값·정수압 수정·공간 연산자 | `swe/dg2new.cpp:643` `H + SQRT(C(3.0))*H1_hat,`; `:690` `DEM_LR = FMAX(DEM_L, DEM_R);`; `:702` `star_left.H = FMAX(C(0.0), left.ETA - DEM_LR);`; `:710-713`의 Q15 | `swe/dg2/modifiedvars.cpp:443` `return Zstar - getmax(C(0.0), -(ETA - Zstar));`; 공간 연산자는 LG1-042·043이다. | 다름 | 해석: ndir에 따라 현재 셀 수면으로 DEM_LR를 낮추는 부분은 Zdagger를 계면별로 계산하는 다른 표기이다. F. 속도 임계값은 LG1-086이다. |
| LG1-081 | y 물리 플럭스의 질량 성분 | `swe/dg2new.cpp:747-752`의 Q15 | `swe/flux.cpp:28` `physical_flux(Solverptr, H, HV, HU, H_flux, HV_flux, HU_flux);`; `cuda/cuda_flow.cu:37` `return { HV, HU*HV/H, HV*HV/H + C(0.5)*cuda::physical_params.g*H*H };` | 다름 | dg2new의 y 질량 플럭스는 HU이다. 다른 두 구현은 HV이다. |
| LG1-082 | fixed time step에서 최종 상태 반영 | `swe/dg2new.cpp:769` `if (Statesptr->adaptive_ts == OFF) return;`; 실제 배열 복사는 `:789` `Arrptr->H[j*Parptr->xsz+i] = H_new[j*Parptr->xsz+i];`부터 시작한다. | CPU `swe/dg2.cpp:749-750`은 매번 최종 상태를 쓴다. CUDA `cuda/dg2/cuda_dg2_solver.cu:938-940`도 매번 최종 상태를 쓴다. | 다름 | dg2new의 fixed 분기는 H_new와 기울기를 다음 단계 상태로 반영하지 않는다. |
| LG1-083 | 경계·지형 취급 | `swe/dg2new.cpp:42` `Arrptr->DEM[j*Parptr->xsz+i] = C(0.0);`; `:45` `Arrptr->H[j*Parptr->xsz+i] = C(0.0);`; `:300` `// FIXME: BC treatment`; `:304-306`은 내부 셀만 순회한다. | `swe/dg2.cpp:217-220`은 지정 경계를 구성한다. CUDA는 `cuda/dg2/cuda_dg2_solver.cu:515-516`에서 Boundary::outside_x를 부른다. | 다름 | 미완성 경계 처리를 명시한 비활성 구현이다. 이 경로의 경계를 정식 CPU 경계로 보고하지 않는다. H. |
| LG1-084 | 원천항·제한·통계·최대 수심 | `swe/dg2new.cpp:101-109`은 `apply_friction();`, `rk_stage1();`, `rk_stage2();`, `update_Tstep();`, `update_mass_stats();`, `write_solution();`를 호출한다. | `swe/dg2.cpp:60-79`에는 강우·점 원천·경계·선택적 limiter·최대 수심·경계 질량 집계가 있다. | 실행되는 CPU·CUDA에만 있음 | dg2new의 solve는 이 처리를 호출하지 않는다. 기존 자료의 dg2new 설명에 이 제한을 넣어야 한다. |
| LG1-085 | 첫 dt·건조 등호 | `swe/dg2new.cpp:178` `Solverptr->Tstep = 1e-5;`; `:338` `if (Arrptr->H_int[j*Parptr->xsz+i] <= Solverptr->DepthThresh)` | `swe/dg2.cpp:43` `Solverptr->Tstep = 1e-6;`; `:1201`의 `<` 분기 | 다름 | dg2new는 더 큰 첫 간격과 `<=` 건조 판정을 쓴다. 실제 기본 CPU 경로에 이 값을 옮기면 안 된다. |
| LG1-086 | dg2new 면 속도의 등호 | `swe/dg2new.cpp:676` `if (left.H > Solverptr->DepthThresh)` | `swe/dg2/modifiedvars.cpp:234` `if (H >= Solverptr->DepthThresh)`; CUDA도 `cuda/cuda_flow.cu:56`에서 `>=`를 쓴다. | 다름 | dg2new는 임계값과 정확히 같은 면 수심에서 운동량을 재구성하지 않는다. |

Q15. dg2new의 수정 지형은 `swe/dg2new.cpp:710-713`이다.

```cpp
    if (delta > C(0.0))
    {
        DEM_LR -= delta;
    }
```

해석: `delta=max(0,Zstar-ETA)`이면 `DEM_LR-=delta`는 Zdagger 식과 같다.
dg2new의 y 물리 플럭스는 `swe/dg2new.cpp:747-752`이다.

```cpp
        return
        {
            HU,
            HU*HV/H,
            HV*HV/H + (Solverptr->g/C(2.0))*(H*H)
        };
```

### 2.6 CUDA FV2와 FV1·DG2

FV2를 CPU DG2의 GPU 번역으로 취급하지 않는다.
`cuda/fv2/cuda_fv2_flow.cu:67-68`의 계면식은 DG2와 다른 기울기 정규화를 쓴다.
`cuda/fv2/cuda_fv2_solver.cu:235-239`에는 DG2의 기울기 공간 연산자가 없다.

| 행 ID | 계산 항목 | FV1·DG2 원문 | CUDA FV2 원문 | 판정 | 이유 |
|---|---|---|---|---|---|
| LG1-100 | FV2 계면 기울기 | DG2는 `cuda/dg2/cuda_dg2_flow.cu:88-89`에서 sqrt(3)을 곱한다. FV1은 셀 평균을 쓴다. | `cuda/fv2/cuda_fv2_flow.cu:67-68` `return { H + C(0.5) * H1x, HU + C(0.5) * HU1x,` / `HV + C(0.5) * HV1x };` | 다름 | 해석: 계면값만 비교하면 FV2 기울기=2sqrt(3)×DG2 기울기 변환이 가능하다. 이 변환은 기울기 진화식까지 같게 만들지 않는다. F. |
| LG1-101 | 기울기 진화 | DG2는 `cuda/dg2/cuda_dg2_solver.cu:279-281`에서 `Lx.set_1x`를 계산한다. | `cuda/fv2/cuda_fv2_solver.cu:235-239`의 Q16은 평균 성분만 갱신한다. | DG2에만 있음 | FV2는 이웃 평균에서 기울기를 다시 만든다. `limit_slopes`를 끄면 이 재구성도 호출하지 않는다. |
| LG1-102 | FV2 제한 함수와 얕은 수심 | DG2는 LG1-048의 0.30×maxH와 Krivodonova·minmod를 쓴다. | `cuda/fv2/cuda_fv2_slope_limit.cu:15` `if (stencil_minH <= C(0.09)) return C(0.0);`; `:36-42`의 Q16 | 다름 | FV2는 0.09 m 문턱과 beta=1.25의 비율 제한을 쓴다. `mesh_delta`와 `krivodonovathresh`는 이 식에 쓰이지 않는다. |
| LG1-103 | FV2 지형 | DG2 `cuda/dg2/cuda_dg2_dem.cu:235` `return _0[idx] + SQRT(C(3.0))*_1x[idx];` | `cuda/fv2/cuda_fv2_dem.cu:28-31`은 인접 `_0`의 최대만 쓴다. | DG2에만 있음 | FV2는 DEM1x·DEM1y를 읽지 않는다. |
| LG1-104 | 평균 바닥 원천항 | FV1은 LG1-012의 정수압 원천항이다. DG2는 LG1-043이다. | `cuda/fv2/cuda_fv2_solver.cu:127` `NUMERIC_TYPE Zdagger_1x = (Zdagger_e - Zdagger_w) / C(2.0);`; `:132` `Sbx.HU = -C(2.0) * g*Hstar_0x*Zdagger_1x / cuda::geometry.dx;` | 다름 | 해석: 2와 1/2를 소거하면 FV1 형식의 평균 수심×지형차가 된다. FV2의 수면은 재구성 면 수심을 쓴다. F는 원천항의 대수적 계수에만 적용한다. |
| LG1-105 | RK2·CFL·HLL·건조 운동량 | CPU DG2 RK2는 LG1-044이다. 공통 HLL은 LG1-007·008이다. | `cuda/fv2/cuda_fv2_solver.cu:338-385`의 네 RK 반환식; `:75-79`의 CFL; `:403` `if (U.H < cuda::solver_params.DepthThresh)` | 같음 | FV2도 두 RK 단계 뒤 건조 운동량을 제거한다. FV2는 DG2처럼 평균 수심·경계 상태로 CFL을 제한한다. |
| LG1-106 | FV2 마찰 계수 | DG2는 평균과 가우스점에 마찰을 적용한다. | `cuda/fv2/cuda_fv2_solver.cu:547` `friction(n, U.H, Uref.HU, Uref.HV);` | DG2에만 있음 | FV2는 평균 운동량에만 마찰을 적용한다. FV2는 재구성 단계에서 기울기를 다시 만든다. |
| LG1-107 | 균일 강우 옵션 | FV1 `cuda/fv1/cuda_fv1_simulate.cu:149-153`과 DG2 `cuda/dg2/cuda_dg2_simulate.cu:147-152`는 균일 강우를 호출한다. | `cuda/fv2/cuda_fv2_solver.cu:754-760`의 update_uniform_rain은 `return;`뿐이다. `cuda/fv2/cuda_fv2_simulate.cu:134-139`는 동적 강우만 호출한다. | FV1·DG2에만 있음 | FV2에서 rainfall 옵션을 켜도 이 루프는 균일 강우를 적용하지 않는다. |
| LG1-108 | FV2 출력 계수 | CPU·CUDA DG2는 평균과 기울기 파일을 출력한다. | `cuda/fv2/cuda_fv2_snapshot.cu:32` `writer_H = write_async(U.H, ".wd", 0, call_gzip);`; `:41-42`는 평균 HU·HV만 출력한다. | DG2에만 있음 | FV2의 Snapshot은 기울기 파일을 출력하지 않는다. |

Q16. FV2의 공간 갱신은 `cuda/fv2/cuda_fv2_solver.cu:235-239`이다.

```cpp
				FlowCoeffs Lx = {};
				Lx.set_0(-(F_e - F_w)/cuda::geometry.dx);

				Lx += bed_source_x(Ustar_0x.H, DEM, U_w, i, j);
				U_out[j*cuda::pitch + i] = rk_op(i, j, Lx);
```

FV2 제한 함수의 마지막 부분은 `cuda/fv2/cuda_fv2_slope_limit.cu:36-42`이다.

```cpp
	NUMERIC_TYPE beta = C(1.25);

	NUMERIC_TYPE phi = FMAX(C(0.0), FMAX(FMIN(beta * r, C(1.0)), FMIN(r, beta)));

	NUMERIC_TYPE limiter = phi * b_jump;

	return limiter;
```

FV2의 `copy_slopes`는 `cuda/fv2/cuda_fv2_solver.cu:576-581`에서 여섯 scratch 기울기를 0으로 쓴다.
FV2의 여섯 stencil 생성 함수는 `cuda/fv2/cuda_fv2_slope_limit.cu:98-210`에서 이웃의 평균만 읽는다.
따라서 DG2의 기울기 보존·제한 과정과 FV2의 평균 기반 재구성 과정을 구분해야 한다.

### 2.7 공통 입력·강우·질량·출력

| 행 ID | 계산 항목 | CPU 원문 | CUDA 원문 | Metal 원문 | 판정과 이유 |
|---|---|---|---|---|---|
| LG1-120 | 초기 상태의 0 초기화·DG2 유량 기울기 | `swe/fields.cpp:10` `Arrptr->HU = memory_allocate_zero_numeric_legacy(Parptr->xsz*Parptr->ysz);`; `swe/dg2/fields.cpp:239` `read_ascfile(hu1x, Parptr, Arrptr->HU1x, "Loading startfile Qx1x\n", verbose);` | `cuda/cuda_util.cu:53` `checkCudaErrors(cudaMallocHost(&ptr, size));`; `cuda/cuda_simulate.cu:35` `if (states.startfile == ON)`; `:83` `if (states.startq2d == ON)`; DG2 run의 `:58-59`는 평균 HU·HV만 초기화한다. | `metal/fv1/metal_fv1_simulate.mm:491-493`은 두 flow 버퍼를 memset한다. `:577-579`는 호스트 초기 상태를 복사한다. | 다름. CUDA 할당 함수에는 0 초기화가 없다. 시작 파일이 없는 필드와 DG2 운동량 기울기에는 해당 초기화 경로가 없다. |
| LG1-121 | H 점 원천이 읽는 DEM의 위치 | CPU는 `swe/fv1.cpp:206`에서 호스트 DEM을 읽는다. | `cuda/fv1/cuda_fv1_simulate.cu:157` `cuda::Boundary::update_point_sources(d_U.H, DEM,`; `cuda/cuda_boundary.cu:665` `cuda::update_point_sources<<<1, CUDA_BLOCK_SIZE>>>(H, DEM, mass_stats);` | Metal은 `metal/fv1/metal_fv1_simulate.mm:923` `float z = arrays->DEM[py * xsz + px];`를 호스트에서 읽는다. | 다름. CUDA 호출은 d_DEM 대신 일반 호스트 DEM을 커널에 전달한다. DG2·FV2도 DEM._0을 전달한다. pageable 호스트 메모리 접근을 지원하지 않는 CUDA 장치에서는 결함 후보이다. |
| LG1-122 | 경계 인덱스·보간 | `swe/boundary.cpp:37` `return 2*Parptr->xsz + 2*Parptr->ysz - j - 1;`; `:23` `return a1*values[i] + a2*values[i - 1];` | `cuda/cuda_boundary.cu:433` `return 2*cuda::geometry.xsz + 2*cuda::geometry.ysz - j;`; `:31` `return a1*values[i] + a2*values[i - 1];` | `metal/fv1/metal_fv1_kernels.metal:457-458`의 west/east 식; `:568-569`의 north/south 식. 호스트는 `metal/fv1/metal_fv1_simulate.mm:874-875`에서 InterpolateTimeSeries를 부른다. | 다름. 해석: ghost 인덱스에서 1을 빼면 같은 둘레 인덱스이다. CPU·CUDA 보간은 범위 밖에서 끝값을 쓴다. F. |
| LG1-123 | 원천항 순서·균일 강우 지원 | `swe/fv1.cpp:43-45` `rain.update_H(Parptr, Solverptr, Arrptr);` / `update_point_sources(Parptr, Solverptr, BCptr, Arrptr);` / `apply_friction(Parptr, Solverptr, Arrptr);` | FV1·DG2는 동적 강우와 균일 강우를 점 원천보다 먼저 적용한다. `cuda/fv1/cuda_fv1_simulate.cu:149-152`에 rainfall 분기가 있다. | `metal/fv1/metal_fv1_simulate.mm:1046` `applyPointSources();` 다음에 `:1050` `if (states->rainfall == ON) {`와 `:1072`의 동적 강우 분기가 온다. | 다름. CPU SWE 루프에는 균일 Rainfall 호출이 없다. Metal은 점 원천 뒤에 강우를 적용한다. H 지정 원천과 강우는 일반적으로 순서를 바꿀 수 없다. |
| LG1-124 | 동적 강우 격자의 공간 대응 | `rain/rain.tpp:113` `int tile_i = i * Parptr->dx / geometry_.dx;`; `:118` `if (tile_i < geometry_.xsz && tile_j >= 0)` | `cuda/cuda_rain.cu:21` `int tile_i = (i-1) * cuda::geometry.dx / cuda::rain_geometry.dx;`; `:27`도 x 상한·y 하한만 검사한다. | `metal/fv1/metal_fv1_kernels.metal:755` `float x_offset = dem_geom.blx - rain_geom.blx;`; `:763-764`의 Q17은 네 경계를 검사한다. | 다름. Word 매뉴얼 p.37은 같은 원점과 정수배 타일을 요구한다. 이 허용 조건에서 CPU·CUDA의 원점 처리는 결함 근거가 아니다. Metal은 원점 차이와 네 경계를 추가 처리한다. |
| LG1-125 | 동적·균일 강우의 음수 처리 | `rain/rain.tpp:178-180`의 Q17은 부호를 제한하지 않는다. | 동적 강우 `cuda/cuda_rain.cu:58` `Hval += rate_at_cell(rain_data, i, j) * cuda::dt;`; 균일 강우 `cuda/fv1/cuda_fv1_solver.cu:127` `Hval += cell_rain;` | 동적 강우 `metal/fv1/metal_fv1_kernels.metal:794` `if (rate > 0.0f) {`; 균일 강우 `:738` `float increment = max(-H[idx], rain_rate * dt);` | 다름. Metal 동적 강우는 음수를 버린다. Metal 균일 강우는 현재 수심만큼만 제거한다. |
| LG1-126 | Metal 동적 강우 업로드 간격 | CPU는 `rain/rain.tpp:167` `update_time(Solverptr->t);` 뒤 현재 data를 쓴다. | CUDA는 `cuda/fv1/cuda_fv1_simulate.cu:144` `rain.update_time(solver.t);` 뒤 현재 data를 쓴다. | `metal/fv1/metal_fv1_simulate.mm:1075` `if (time >= last_rain_time + 1.0 \|\| last_rain_time < 0) {` | Metal에만 있음. 1 s 미만 간격의 강우 자료 변경은 다음 업로드까지 GPU에 반영되지 않을 수 있다. |
| LG1-127 | 강우의 질량 장부 | `rain/rain.tpp:184` `Parptr->RainTotalLoss += total_rain_mass;`; `swe/stats.cpp:14-15`의 Q18은 이 값을 Verror에 넣지 않는다. | `cuda/cuda_rain.cu:58`은 H만 바꾼다. `cuda/stats.cpp:74` `C(0.0) /*Parptr->RainTotalLoss - (Parptr->InfilTotalLoss + Parptr->EvapTotalLoss)*/` | `metal/fv1/metal_fv1_simulate.mm:1104-1105` `boundCs->VolInMT += (NUMERIC_TYPE)interval_rain_vol;` / `pars->RainTotalLoss += (NUMERIC_TYPE)interval_rain_vol;`; 균일 강우도 `:696-697`에서 넣는다. | 다름. CPU SWE와 CUDA의 Verror는 강우 체적 증가를 유입으로 상쇄하지 않는다. Metal은 강우를 유입 체적에도 넣는다. |
| LG1-128 | CUDA Qerror의 누적 시간 | `swe/stats.cpp:16` `Solverptr->Qerror = Solverptr->Verror / Parptr->MassInt;` | `cuda/cuda_stats.cu:83` `cumulative_time += cuda::dt;`; `:118` `(net_source_flux - volume_change)/time`; FV1 run의 `:159`, `:176`은 단계마다 두 번 accumulate_mass를 부른다. | Metal은 호스트의 update_mass_stats를 재사용한다. | 다름. CUDA는 원천항 집계와 플럭스 집계 양쪽에서 시간을 더한다. 고정 dt이면 분모가 적분한 물리 시간의 두 배가 된다. |
| LG1-129 | 초기 체적 기준 | `swe/fv1.cpp:32` `Solverptr->vol1 = DomainVol(Statesptr, Parptr, nullptr, Arrptr, nullptr);`; `swe/dg2.cpp:50`도 같다. | `cuda/cuda_stats.cuh:35` `NUMERIC_TYPE previous_volume = C(0.0);`; `cuda/cuda_stats.cu:93` `NUMERIC_TYPE volume_change = current_volume - previous_volume;` | `metal/fv1/metal_fv1_simulate.mm:1386` `solver.vol1 = DomainVol(&states, &pars, nullptr, &arrays, nullptr);` | 다름. 선택한 CUDA run은 초기 수심의 실제 체적을 previous_volume에 넣지 않는다. 초기 저류가 있으면 첫 체적 오차에 포함된다. |
| LG1-134 | 침수 면적 기준 | `swe/stats.cpp:36` `if (Arrptr->H[j*Parptr->xsz + i] > C(0.01)) FloodArea += Parptr->dA;` | `cuda/cuda_stats.cu:45` `histogram_levels[1] = DepthThresh;`; `:141` `return histogram_counts[1] * geometry.dx * geometry.dy;` | Metal은 CPU flood_area를 사용한다. | 다름. 기본 DepthThresh=0.001이면 CUDA는 CPU의 0.01 기준과 다른 면적을 출력한다. 값의 출처는 `lisflood.cpp:174`이다. |
| LG1-135 | 격자 속도·수면·최대 수심 값 | `swe/stats.cpp:139-140` `Vx = HU / H;` / `Vy = HV / H;`; `:165` `maxH = FMAX(maxH, Arrptr->H[j*Parptr->xsz + i]);` | `cuda/cuda_snapshot.cu:23` `return discharge[idx] / H[idx];`; `:46` `return DEM[idx] + H[idx];`; `cuda/cuda_max_field.cu:26` `maxHvalue = FMAX(maxHvalue, H[j*cuda::pitch+i]);` | Metal은 HV 부호를 복원한 뒤 CPU 출력을 쓴다. 최대 수심은 `metal/fv1/metal_fv1_kernels.metal:990` `maxH[idx] = max(maxH[idx], H[idx]);`이다. | 같음. 시점별 셀 수심의 최대이다. 초기 상태 자체를 최대 수심에 먼저 넣는 호출은 이 루프들에 없다. |
| LG1-136 | 건조 관측점의 속력 | `swe/output.cpp:84-86` `else` / `{` / `speed = C(0.0);` | `cuda/cuda_sample.cu:33-41`의 Q18은 wet일 때만 speed를 쓴다. | Metal simulate는 관측점 속력 쓰기를 호출하지 않는다. | 다름. CUDA dry 가지는 sample_buf.speed를 쓰지 않는다. 나중 writer는 그 위치를 읽는다. |
| LG1-137 | stage·velocity 관측점 파일 | CPU FV1은 `swe/fv1.cpp:74-81`에서 save_stages와 voutput_stage를 처리한다. | `cuda/fv1/cuda_fv1_simulate.cu:104-116`은 Sampler를 설정한다. `:181`에서 sample을 호출한다. | `metal/fv1/metal_fv1_simulate.mm:1413-1460`에는 write_depth_samples·write_speed_samples 호출이 없다. | CPU·CUDA에만 있음. Metal이 CPU write_solution을 재사용한다는 사실로 stage·velocity 지원을 추론하면 안 된다. |
| LG1-138 | 격자 파일 옵션·기울기 출력 | `swe/output.cpp:113` `if (Statesptr->save_depth == ON)`; `:178` `if (Statesptr->binary_out == ON)`; `swe/dg2/dg2_output.cpp:13`도 save_depth 조건이다. | `cuda/dg2/cuda_dg2_snapshot.cu:38-40`은 wd·wd1x·wd1y를 무조건 쓴다. `cuda/fv1/cuda_fv1_snapshot.cu:32`도 wd를 쓴다. 공통 writer는 ASCII이다. | Metal은 CPU write_solution·write_max_field를 호출한다. | 다름. CUDA는 이 Snapshot 경로에서 save_depth와 binary_out을 CPU와 같이 적용하지 않는다. |
| LG1-139 | 공통 checkpoint 함수의 호출 여부 | 기본 CPU 초기화·출력과의 전체 checkpoint 대조는 이 작업의 목적이 아니다. | `cuda/cuda_simulate.cu:149`, `:331`에 read_checkpoint·write_checkpoint가 있다. 선택한 FV1·FV2·DG2 run은 두 함수를 호출하지 않는다. | `metal/fv1/metal_fv1_simulate.mm:1344-1487`도 이 CUDA 함수를 사용하지 않는다. | 대조 대상 아님. 공통 파일의 함수 존재를 세 SWE run의 재시작 지원 근거로 쓰지 않는다. H. |
| LG1-140 | 침투·증발·routing·강우 mask | `swe/fv1.cpp:43-50`, `swe/dg2.cpp:62-79`의 루프에는 Infiltration·Evaporation·Routing 호출이 없다. | 선택한 CUDA run에도 이 호출이 없다. | `metal/fv1/metal_fv1_simulate.mm:1347-1351`의 Q19는 rainfallmask·routing을 명시적으로 거부한다. | 다름. Metal만 거부를 명시한다. 침투·증발·routing은 Word 매뉴얼도 FV1·DG2 적용에서 제외한다. 지원 대상 밖 옵션의 거부 방식은 H로 분류한다. |
| LG1-141 | 단면 유량 출력 | CPU FV1·DG2 solve에는 CalcVirtualGauge 호출이 없다. | 선택한 CUDA run에도 CalcVirtualGauge 호출이 없다. | `metal/fv1/metal_fv1_simulate.mm:1431-1440`의 Q19가 FHx·FHy를 합하고 면 폭을 곱한다. | Metal에만 있음. Metal은 출력 시점에 CPU 플럭스를 재계산한 단면 유량을 쓴다. 적분 중 GPU 경계 플럭스와 같은 시점이라고 간주하지 않는다. |
| LG1-142 | 질량 파일의 Qin·Qout 의미 | `swe/stats.cpp:44-45`는 매 단계 Qin·Qout을 0으로 만든다. 마지막 단계의 값을 출력한다. | `cuda/cuda_stats.cu:96-97`, `:116`은 마지막 instantaneous_mass를 출력한다. 점 원천의 집계 범위는 LG1-145에서 판정한다. | `metal/fv1/metal_fv1_simulate.mm:699-700`은 마지막 동기화 이후 경계·배수 체적을 elapsed로 나눈다. 점 원천 Qin·Qout은 매 단계 직접 더한다. | 다름. Metal의 경계 Qin·Qout은 구간 평균이다. CPU·CUDA는 마지막 단계의 경계 유량을 쓴다. |
| LG1-143 | 정사각 격자와 raster 읽기 | CPU의 해당 SWE 식은 dx·dy를 별도로 쓴다. | `cuda/io.cpp:18` `geometry.dy = geometry.dx;`; `:70` `if (expected.xsz != candidate.xsz \|\| expected.ysz != candidate.ysz)` | Metal은 호스트의 dx·dy를 각각 float로 복사한다. | 다름. 해석: CUDA ASCII 입력의 정사각 셀 조건에서 LG1-025의 식 변형은 유효하다. 읽기 함수는 크기 외에 원점·cellsize 일치를 검사하지 않는다. |
| LG1-145 | CUDA 순간 Qin·Qout의 점 원천 누락 | `swe/stats.cpp:113-116`은 점 원천을 담은 Qin·Qout에 경계 유량을 더한다. | `cuda/cuda_stats.cuh:36` `MassStats* d_instantaneous_mass; /**< through BCs/PSs during timestep*/`; `cuda/fv1/cuda_fv1_simulate.cu:159-160` `stats_collector.accumulate_mass();` / `stats_collector.zero_instantaneous_mass();`; `cuda/cuda_stats.cu:116` `h_instantaneous_mass,` | `metal/fv1/metal_fv1_simulate.mm:951` `boundCs->Qin += Q_total;`; `:954` `boundCs->Qout -= Q_total;` | 다름. CUDA의 누적 체적에는 점 원천이 들어간다. 순간 Qin·Qout에는 점 원천이 빠진다. 자기 주석과 CPU의 집계 범위에 어긋난다. |
| LG1-146 | FV1 통계 직전 ghost 제거 | CPU 통계는 내부 셀 배열만 합한다. | `cuda/fv1/cuda_fv1_solver.cu:516-517`은 `zero_ghost_cells_north_south<<<1, CUDA_BLOCK_SIZE>>>(U);`와 east_west(U)를 호출한다. 현재 상태는 `:550` `return Uold;`이다. | Metal 통계는 copyFromGPU의 내부 셀 복사만 사용한다. | 다름. CUDA FV1은 통계 직전 현재 Uold 대신 다른 버퍼 U의 ghost를 지운다. StatsCollector의 ghost 포함 합산을 보호하지 못한다. |
| LG1-147 | 입력 NoData 치환 허용차 | `swe/input.cpp:27` `if (FABS(field[i + j*Parptr->xsz] - no_data_value) < C(1e-12))` | `cuda/io.cpp:115` `if (FABS(value - no_data_value) < C(1e-5)) value = C(0.0);`; 지형 기울기 load_slope는 치환을 호출하지 않는다. | Metal은 호스트 입력 결과를 받는다. | 다름. 정확히 같은 NoData 값은 같은 결과이다. NoData 근처 값과 기울기 파일의 치환 정책은 다르다. |
| LG1-148 | startelev의 음수 수심 방지 | `input.cpp:1187` `Arrptr->H[i + j*Parptr->xsz] = getmax(Arrptr->H[i + j*Parptr->xsz] - Arrptr->DEM[i + j*Parptr->xsz], C(0.0));` | `cuda/io.cpp:136` `H_value = H_value - DEM_value;` | Metal은 CPU 입력 결과를 복사한다. | 다름. 지반 아래 초기 수위에서 CUDA는 음수 수심을 허용한다. CPU는 0으로 절단한다. |

Q17. Metal 강우 격자의 전체 범위 조건은 `metal/fv1/metal_fv1_kernels.metal:763-768`이다.

```cpp
    if (tile_i >= 0 && tile_i < rain_geom.xsz && 
        tile_j >= 0 && tile_j < rain_geom.ysz) {
         // Rain data is row-major (y * xsz + x)
         return rain_data[tile_j * rain_geom.xsz + tile_i];
    }
    return 0.0f;
```

CPU 동적 강우의 적용식은 `rain/rain.tpp:178-180`이다.

```cpp
            NUMERIC_TYPE inc = rate_at_cell(Parptr, i, j) * Solverptr->Tstep;
            H += inc;
            total_rain_mass += inc*Parptr->dA;
```

Q18. CPU 체적 오차는 `swe/stats.cpp:14-16`이다.

```cpp
	Solverptr->Verror = BCptr->VolInMT - BCptr->VolOutMT -
		(Solverptr->vol2 - Solverptr->vol1);
	Solverptr->Qerror = Solverptr->Verror / Parptr->MassInt;
```

CUDA wet 관측점 속력 가지는 `cuda/cuda_sample.cu:33-41`이다.

```cpp
			if (Hval > cuda::solver_params.DepthThresh)
			{
				NUMERIC_TYPE HUval = HU[cuda::sample_points.idx[i]];
				NUMERIC_TYPE HVval = HV[cuda::sample_points.idx[i]];

				NUMERIC_TYPE speed = SQRT(HUval/Hval * HUval/Hval
						+ HVval/Hval * HVval/Hval);
				sample_buf.speed[buf_offset + i] = speed;
			}
```

Q19. Metal 옵션 거부 조건은 `metal/fv1/metal_fv1_simulate.mm:1347-1351`이다.

```cpp
  if (states.rainfallmask == ON || states.routing == ON) {
    fprintf(stderr, "ERROR: Metal FV1 does not support rainfallmask or rainfallrouting; "
                    "use unmasked rainfall or dynamicrainfile.\n");
    std::exit(EXIT_FAILURE);
  }
```

단면 유량의 식은 `metal/fv1/metal_fv1_simulate.mm:1431-1441`이다.

```cpp
          NUMERIC_TYPE unit_discharge =
              CalcVirtualGauge(i, pars.xsz + 1, arrays.FHx, arrays.FHy, &stage);

          // Convert unit discharge (m2/s) to discharge (m3/s)
          // Q = q * width
          NUMERIC_TYPE discharge = 0.0;
          if (stage.gauge_dir[i] == North || stage.gauge_dir[i] == South) {
            discharge = unit_discharge * pars.dx;
          } else {
            discharge = unit_discharge * pars.dy;
          }
```

### 2.8 8.3 패치와 계산 외 처리

`v8.2:`의 기준 경로는 `_staging/recovery/extract/LISFLOOD-FP/external/v8.2/LISFLOOD-FP/`이다.
이 절은 공식 압축 해제본의 원문을 대조한다.
이 절은 현재 코드의 차이를 A로 분류하지 않는다.

| 행 ID | 항목 | 비교할 원문 | 판정 | 이유 |
|---|---|---|---|---|
| LG1-130 | 최대 수심 배열 크기·초기화 | `v8.2:cuda/cuda_max_field.cu:96-97` `if (acceleration) {` / `maxH = GhostRaster::allocate_pinned_H(geometry); //// change to allocate_pinned_H()`; 현재 `cuda/cuda_max_field.cu:97-98` `maxH = GhostRaster::allocate_device(geometry);` / `cudaMemset(maxH, 0, lis::GhostRaster::elements(geometry)*sizeof(NUMERIC_TYPE));` | 다름 | 8.2 결함이다. 커널은 ghost pitch로 썼지만 선택될 수 있는 allocate_pinned_H는 내부 크기뿐이었다. 8.3은 전체 크기 GPU 배열과 초기화로 고쳤다. |
| LG1-131 | 반복 패스 끝의 공유 배열 보호 | `v8.2:cuda/fv1/cuda_fv1_solver.cu:379-382`의 마지막 갱신 뒤에는 동기화가 없다. 현재 `cuda/fv1/cuda_fv1_solver.cu:380-381` `// shared memory is rewritten in the next pass: wait for every reader` / `__syncthreads();` | 다름 | 8.2 결함이다. 다음 grid-stride 패스가 F·Hstar를 다시 쓰기 전에 모든 읽기를 끝내야 한다. 8.3은 FV1·FV2·DG2의 두 방향에 같은 장벽을 넣었다. |
| LG1-132 | 건조 NoData의 atomic 생략 | `package:lisflood-8.2-to-8.3.patch:79` `+`로 추가한 `if (Hold == C(0.0)) continue; // dry: nothing to add to the mass balance`; 현재 `cuda/cuda_boundary.cu:289`도 같은 조건이다. | 다름 | 해석: 양의 dt에서 0인 배수량을 더하지 않는 최적화이다. 습윤 셀 배수식은 그대로다. H. |
| LG1-133 | 최대 수심 출력 정밀도 인수 | `cuda/fv1/cuda_fv1_simulate.cu:98-99`의 Q20은 여섯 번째 인수에 pars.output_precision을 준다. `cuda/cuda_max_field.cuh:20-21` `int acceleration,` / `int precision = DEFAULT_PRECISION` | 다름 | 현재 FV1·FV2·DG2 호출은 출력 정밀도를 acceleration 자리에 전달한다. 실제 precision에는 기본값이 들어간다. 8.3 배열 수정은 이 인수 불일치를 고치지 않았다. |
| LG1-150 | CPU 계수 생성·downscale 유틸리티 | `swe/dg2/fields.cpp:47-49`의 Q20; `:77-80`의 Q20 | CPU에만 있음 | 평균·기울기 생성과 2×2 자식 중심값 평가는 전후처리이다. 대응 GPU 런타임 이산화와 같은 기능이라고 비교하지 않는다. H. |
| LG1-151 | 사용하지 않는 Metal 플럭스 경로 | `metal/fv1/metal_fv1_simulate.mm:766` `void updateBoundaryFluxes() {`; `metal/fv1/metal_fv1_kernels.metal:921` `kernel void accumulate_outflow(` | 대조 대상 아님 | 정의와 pipeline 생성은 있지만 step에서 호출·dispatch하지 않는다. 실제 질량은 update_flow_x/y의 account_boundary가 집계한다. H. |
| LG1-152 | 메모리·장치 API·벡터 조립 | `cuda/cuda_geometry.cu:30-32`의 cudaMemcpy; `cuda/cuda_unifiedallocator.templates.cu:7` `return static_cast<T*>(malloc_unified(sizeof(T) * n));`; `cuda/cuda_atomic.cuh:14-16`의 atomicCAS | 다름 | pinned·device·shared·unified 메모리, CUB 작업 공간, Metal pipeline, 버퍼 전송, 성분별 산술 연산자는 저장·실행 방식이다. H. 초기화가 계산값에 영향을 주는 사례는 LG1-120으로 분리했다. |
| LG1-153 | 공통 CUDA 파일의 ACC 전용 함수 | `cuda/cuda_boundary.cu:679-681`의 Q20; `cuda/cuda_rain.cu:91` `lis::cuda::DynamicRain::updateACC`; `cuda/cuda_max_field.cu:35` `update_max_field_ACC` | 대조 대상 아님 | update_H의 WDweight와 분리된 Q/H 점 원천은 선택한 SWE run에서 호출되지 않는다. ACC 내부로 분석을 확장하지 않는다. H. |
| LG1-155 | 성능·이론 서지 | `package:README.md:41-60`의 배포본 시험·성능 설명; `metal/CMakeLists.txt:7-9`의 재현성 설명 | 대조 대상 아님 | 시험 사례의 일치·속도 주장은 이 정적 대조의 실행 검증이 아니다. H. |

Q20. 최대 수심 호출의 전체 인수는 `cuda/fv1/cuda_fv1_simulate.cu:98-99`이다.

```cpp
	MaxField max_field(filenames.resrootname, geometry, pitch, offset,
			grid_size, pars.output_precision);
```

같은 인수 모양은 `cuda/fv2/cuda_fv2_simulate.cu:90-91`, `cuda/dg2/cuda_dg2_simulate.cu:95-96`에도 있다.
기본 정밀도의 출처는 `lisflood.h:130` `#define DEFAULT_PRECISION 6`이다.

CPU 계수 생성식은 `swe/dg2/fields.cpp:47-49`이다.

```cpp
				F[j*Parptr->xsz + i] = C(0.25)*(NW+NE+SW+SE);
				F1x[j*Parptr->xsz + i] = (NE+SE-NW-SW)/(C(4.0)*SQRT(C(3.0)));
				F1y[j*Parptr->xsz + i] = (NE+NW-SE-SW)/(C(4.0)*SQRT(C(3.0)));
```

CPU downscale 식은 `swe/dg2/fields.cpp:77-80`이다.

```cpp
			F[jj * Parptr->xsz + ii] = WD0 - C(0.5) * SQRT(C(3.0)) * WD1x + C(0.5) * SQRT(C(3.0)) * WD1y;
			F[jj * Parptr->xsz + ii + 1] = WD0 + C(0.5) * SQRT(C(3.0)) * WD1x + C(0.5) * SQRT(C(3.0)) * WD1y;
			F[jj * Parptr->xsz + ii + (2 * Parptr->xsz)] = WD0 - C(0.5) * SQRT(C(3.0)) * WD1x - C(0.5) * SQRT(C(3.0)) * WD1y;
			F[jj * Parptr->xsz + ii + (2 * Parptr->xsz) + 1] = WD0 + C(0.5) * SQRT(C(3.0)) * WD1x - C(0.5) * SQRT(C(3.0)) * WD1y;
```

ACC용 wrapper의 호출 순서는 `cuda/cuda_boundary.cu:679-681`이다.

```cpp
	cuda::update_point_sources_Q << <1, CUDA_BLOCK_SIZE >> > (H, mass_stats);
	cuda::update_H << <grid_size, cuda::block_size >> > (H, Qx, Qy, drycheck);
	cuda::update_point_sources_H << <1, CUDA_BLOCK_SIZE >> > (H, DEM, mass_stats);
```

패치 근거는 `package:lisflood-8.2-to-8.3.patch:98-112`의 할당 교체와 `:121-133`의 출력 시 복사·해제 교체이다.
FV1 동기화 추가 행은 같은 패치의 `:196-197`, `:216-217`이다.
DG2 동기화 추가 행은 같은 패치의 `:153-154`, `:173-174`이다.
FV2 동기화 추가 행은 같은 패치의 `:239-240`, `:259-260`이다.
현재 `VersionHistory.h:31-32`도 최대 수심·건조 NoData·플럭스 동기화를 8.3 변경으로 적는다.

### 2.9 계산 루틴 대조 범위

파일 집계는 `swe/**`, `cuda/{fv1,fv2,dg2}/**`, `cuda/` 직하와 `metal/**`의 코드·헤더·CMake 파일 목록에서 셌다.
집계 파일은 114개이다.
이 집계는 `swe` 33개, `cuda/fv1` 8개, `cuda/fv2` 12개, `cuda/dg2` 12개, `cuda/` 직하 43개, `metal` 6개로 나뉜다.
헤더의 선언은 대응 정의와 연결했다.
헤더의 실제 성분별 연산자는 같은 성분끼리 연산하는지 확인했다.
선언만 있는 헤더에 새 계산 루틴이 있다고 세지 않았다.

| 파일 묶음 | 확인한 루틴·계산 | 대조 위치 |
|---|---|---|
| `swe/fv1.cpp`, `fv1.h` | solve, apply_friction, drain_nodata_water, update_point_sources, update_fluxes, update_fluxes_on_boundaries, update_flow_variables, bed_source_x/y, set_boundary_values, Tstep_from_cfl | LG1-003~029, 120~146 |
| `swe/fv1/modifiedvars.cpp`, `.h` | initialise_Zstar, update_Hstar, HUstar/HVstar의 neg/pos·x/y, discharge_star, Zdagger의 neg/pos·x/y, Zdagger, eta, speed | LG1-003~006, 012 |
| `swe/hll.cpp`, `hll.h`, `hll_include.h`, `flux.cpp`, `flux.h` | HLL/HLL_x/HLL_y, physical_flux/physical_flux_x/physical_flux_y | LG1-007~010, 042, 081 |
| `swe/boundary.cpp`, `.h` | linear_interpolate, boundary_index_w/e/n/s | LG1-122 |
| `swe/fields.cpp`, `.h` | allocate_swe_fields, deallocate_swe_fields | LG1-120, 152 |
| `swe/dg2.cpp`, `dg2.h` | solve, update_point_sources, update_boundary_values, rk_stage1/2, update_fluxes·경계 플럭스, set_boundary_values, update_intermediate/final_coefficients와 단일 계수 함수, set_initial/intermediate_coefficients, L/L0/L1x/L1y, 네 bed_source, maxH, thin_depth, zero_thin_depth_slopes, Tstep_from_cfl/min_dt, zero_discharge | LG1-024, 040~059 |
| `swe/dg2/modifiedvars.cpp`, `.h` | 지형·수심·운동량 수정, H/HU/HV의 star0x/0y/1x/1y, Zdagger1x/1y·네 면 값, eta·eta1x/1y·네 면 값, limit_neg/pos와 gauss_lower/upper의 배열·스칼라 overload | LG1-040~043 |
| `swe/dg2/friction.cpp`, `.h` | apply_friction, friction | LG1-045~047 |
| `swe/dg2/slope_limiter.cpp`, `.h` | zero_perimeter_slopes, apply_slope_limiter_x/y, apply_slope_limiter, limit_slope, minmod, stencil_minH_x/y | LG1-048~054 |
| `swe/dg2/fields.cpp`, `.h` | 두 initialise_field, downscale, initialise_h_from_eta, read_dem_slopes, zero_dem_perimeter_slopes, read_h_slopes, read_discharge_slopes, write_dem·write_DScaled·write_startfile, allocate_fields·boundary allocate, deallocate_fields·boundary deallocate | LG1-040~041, 120, 150, 152. 수위 초기화의 `H=max(0,eta-Z)`, `H1x=-Z1x`, `H1y=-Z1y`는 `swe/dg2/fields.cpp:135-137`이다. |
| `swe/dg2new.cpp`, `.h` | 생성자·소멸자, 네 입력 함수, set_first_Tstep·print_Tstep, 마찰 overload 세 개, RK 단계 overload 네 개, space_operator·dg2_operator·local_face_value·wetting_drying·flux_x/y, update_Tstep overload 두 개, update_mass_stats·write_solution·malloc_new_fields, 성분별 벡터 연산자 | LG1-080~085, 001, 152 |
| `swe/stats.cpp`, `.h`, `output.cpp`, `.h`, `input.cpp`, `.h`, `dg2/dg2_output.cpp`, `.h` | flood_area·update_mass_stats·zero_flux_stats·두 flux 집계·update_velocity·update_max_field, read_ascfile, write_mass_stats·depth/speed_samples·solution·max_field·field·solution_slopes | LG1-029, 058, 127~143 |
| `cuda/fv1/cuda_fv1_solver.cu`, `.cuh` | 두 zero_ghost_cells 커널, update_dt_per_element, update_uniform_rain_func, update_ghost_cells, apply_friction, bed_source_x/y, update_flow_variables_x/y, Solver의 해당 wrapper·d_U, 빈 FloodplainQ·zero_thin_depth_slopes·updateMaxFieldACC, 생성자·소멸자 | LG1-003~029, 120~146, 152 |
| `cuda/dg2/cuda_dg2_solver.cu`, `.cuh` | 위 공통 루틴, min_dt, 네 RK 커널, zero_discharge·zero_thin_depth_slopes, friction·apply_friction, copy_slopes·limit_slopes·두 zero_perimeter_slopes 커널, Solver wrapper | LG1-040~059, 120~146 |
| `cuda/fv2/cuda_fv2_solver.cu`, `.cuh` | 공통 ghost·CFL·경계·마찰·네 RK·건조 제거·기울기 복사/재구성, 빈 uniform_rain·thin_depth·ACC wrapper | LG1-100~108, 120~146 |
| `cuda/{fv1,fv2,dg2}/cuda_*_flow.cu`, `.cuh` | FlowCoeffs·FlowCoeffsRef 생성·대입·set_0/1x/1y·get_0, 면 값·가우스점, 성분별 연산자, Flow[]·allocate/copy/free | LG1-040~047, 100, 120, 152 |
| `cuda/{fv2,dg2}/cuda_*_dem.cu`, `.cuh`, `cuda/cuda_dem.cu`, `.cuh` | load·load_slope·두 initialise_Zstar·지형 면 값·Zdagger·둘레 기울기 제거·ghost 바닥 복사·장치 초기화/해제 | LG1-003~004, 041~043, 103~104, 143 |
| `cuda/{fv2,dg2}/cuda_*_slope_limit.cu`, `.cuh` | Stencil::limit·minH_x/y·네 면 평가·DG2 minmod·여섯 stencil 생성, Slopes allocate/free, MaxH 생성·update·소멸 | LG1-048~053, 102, 152 |
| `cuda/{fv1,fv2,dg2}/cuda_*_simulate.cu`, `.cuh` | run·초기화·강우·경계·원천·시간 간격·흐름·배수·통계·출력 순서, DG2 initialise_H·initialise_H_slope | LG1-017~020, 059, 107, 120~146 |
| `cuda/{fv1,fv2,dg2}/cuda_*_snapshot.cu`, `.cuh` | Snapshot 생성·write·write_maxes·wait | LG1-108, 135~139, 151 |
| `cuda/cuda_flow.cu`, `.cuh`, `cuda_hll.cu`, `.cuh` | FlowVector::star·calculate_Hstar·speed·physical_flux_x/y·성분별 연산자, HLL::x/y | LG1-004~010, 041~042 |
| `cuda/cuda_boundary.cu`, `.cuh` | linear_interpolate·time_series 갱신·BC/PS 값 갱신, 일반·Q/H 분리 점 원천, update_H, 일반·ACC 배수, inside/outside_x/y, 일반·ACC 둘레 인덱스, initialise_BC/PS/all_time_series·free_device | LG1-021~027, 121~122, 132, 153 |
| `cuda/cuda_solver.cu`, `.cuh`, `cuda_solver.templates.cu`, `params.h` | 매개변수 복사·update_mass_stats_x/y, DynamicTimestep·DynamicTimestepACC 생성·update·해제 | LG1-016~018, 043~044, 058, 128, 152~153 |
| `cuda/cuda_simulate.cu`, `.cuh` | initialise_H/discharge/manning·nullify_max·update_geometry·load_boundaries·print_device_info·read/write_checkpoint | LG1-120~121, 129, 139, 143, 152 |
| `cuda/cuda_rain.cu`, `.cuh` | rate_at_cell·rate_at_cell_ACC, DynamicRain::update·updateACC, NETCDF 분기 | LG1-123~127, 153 |
| `cuda/cuda_stats.cu`, `.cuh`, `stats.cpp`, `.h` | accumulate_mass·zero_instantaneous/cumulative_mass·create_entry·area·volume, Stats::need_to_write·write·header | LG1-127~129, 134, 142, 145 |
| `cuda/cuda_max_field.cu`, `.cuh` | update_max_field·update_max_field_ACC, MaxField 생성·update·updateACC·write·소멸 | LG1-130~135 |
| `cuda/cuda_sample.cu`, `.cuh`, `sample.cpp`, `.h` | sample·sample_ACC, Sampler 전송·기록·버퍼 관리, Sample::initialise/free, StageFile·GaugeFile 생성·open·header·write·소멸 | LG1-135~137, 142, 152~153 |
| `cuda/cuda_snapshot.cu`, `.cuh`, `cuda_snapshot.templates.cu`, `io.cpp`, `io.h`, `io.templates.cpp` | VelocityWriter·ElevationWriter, Snapshot 예약·write_if_needed·write_max_files·enable_*·비동기 쓰기, AsciiRaster header/read/write/replace_no_data/match_dimensions, StartFile load/zero_no_data/subtract_dem | LG1-135~139, 143, 152 |
| `cuda/ghostraster.cpp`, `.h`, `cuda_geometry.cu`, `.cuh`, `cuda_util.cu`, `.cuh`, `cuda_util.templates.cu`, `cuda_unifiedallocator.cu`, `.cuh`, `cuda_unifiedallocator.templates.cu`, `cuda_atomic.cuh` | elements·pitch·offset의 일반/ACC 변형, 모든 allocate/copy/free, device query·sync·symbol copy·UnifiedAllocator·구형 장치 double atomicAdd | LG1-120, 130~133, 146, 152~153 |
| `metal/fv1/metal_fv1_kernels.metal` | atomic_add_float·account_boundary·set_boundary_values·hll_x/y·bed_source_x/y·apply_friction·두 compute_zstar·star_state·두 update_flow·compute_dt_per_cell·zero_ghost_cells·uniform/dynamic rain·rate_at_cell·update_ghost_cells·drain_nodata_cells·accumulate_outflow·update_max_field | LG1-003~028, 123~142, 151~152 |
| `metal/fv1/metal_fv1_simulate.mm`, `.h`, `metal_integrate.cpp`, `.h`, `metal/CMakeLists.txt` | SimulatorImpl init·pipeline/buffer 생성·copyTo/FromGPU·copyMaxFromGPU·uploadState·updateBoundaryFluxes·updateBoundaryValues·applyPointSources·computeTimestep·step·syncMassTotals, Simulator wrapper·simulate·metal_is_available·run_metal_fv1 | LG1-001~002, 009~028, 123~142, 151~152, 155 |

`dg2::initialise_field`의 NoData 가지는 `swe/dg2/fields.cpp:38-43`에서 네 꼭짓점 중 하나라도 NoData이면 평균을 NULLVAL로 쓴다.
이 함수는 두 기울기를 0으로 쓴다.
`swe/input.cpp:27-29`의 read_ascfile은 NoData와 `1e-12` 이내인 값을 0으로 쓴다.
CUDA의 StartFile::zero_no_data_values는 `cuda/io.cpp:115`에서 `1e-5` 기준을 쓴다.
지형 기울기 로더 `cuda/dg2/cuda_dg2_dem.cu:99-106`은 이 StartFile 치환 함수를 호출하지 않는다.

## 3 코드에만 있는 처리

이 절은 한 구현에만 있는 처리와 지원 범위를 모은다.
이 절의 행은 §2와 같은 행 ID를 사용한다.
배포본 주석이 처리 목적을 설명하면 그 설명도 판정에 사용했다.

| 기능·옵션 | 해당 구현 | 비교 결과 | 근거 행 |
|---|---|---|---|
| FV2의 평균 기반 기울기 재구성 | CUDA FV2 | CPU FV1·DG2 및 Metal FV1에는 같은 FV2 경로가 없다. | LG1-100~108 |
| 기울기 진화·가우스점 체적 플럭스·가우스점 마찰 | CPU·CUDA DG2 | FV1에는 기울기 계수가 없다. FV2는 평균 기반 재구성을 쓴다. | LG1-040~047, 101, 106 |
| limitslopes | CPU·CUDA DG2, CUDA FV2 | 기본은 OFF이다. DG2와 FV2의 제한식은 다르다. | `lisflood.cpp:148` `Params.limit_slopes = OFF;`; `pars.cpp:980` `Parptr->limit_slopes = ON;`; LG1-048~053, 102 |
| krivodonovathresh | CPU·CUDA DG2 | FV2의 Stencil::limit는 이 값을 쓰지 않는다. | LG1-048~049, 102 |
| 재구성의 H==DepthThresh 속도 복원 | CUDA FV1, CPU·CUDA DG2 | CPU·Metal FV1과 dg2new는 엄격한 `>`를 쓴다. | LG1-006, 041, 086 |
| HLL·마찰의 추가 작은 값 보호 | Metal FV1 | 수심 안전 하한, 작은 HLL 분모 단락, 마찰 속도 epsilon이 있다. | LG1-010, 014 |
| 최종 H의 0 하한 | Metal FV1 | CPU·CUDA FV1은 같은 위치에서 절단하지 않는다. | LG1-015 |
| 전역 지형 기준면 이동·별도 NoData 값 | Metal FV1 | HU·HV 부호 변환과 구분해야 한다. | LG1-009, 028 |
| FREE6의 transmissive 처리 | Metal FV1 | `metal/fv1/metal_fv1_kernels.metal:78` `} else if (type == BC_FREE \|\| type == BC_FREE6) {`는 FREE6도 복사한다. CPU·CUDA SWE switch는 FREE1만 별도 처리한다. | LG1-149 |
| 균일 rainfall | CUDA FV1·DG2, Metal FV1 | CPU FV1·DG2와 CUDA FV2 루프는 적용하지 않는다. | LG1-107, 123 |
| 동적 강우의 x 원점 이동·전체 영역 검사 | Metal FV1 | CPU·CUDA 대응 함수에는 같은 보정이 없다. | LG1-124 |
| drain_nodata | CPU FV1, CUDA FV1·FV2·DG2, Metal FV1 | CPU DG2 루프에는 호출이 없다. | LG1-027, 059 |
| stage·velocity 관측점 출력 | CPU FV1·DG2, CUDA FV1·FV2·DG2 | Metal FV1 simulate에는 기록 호출이 없다. | LG1-136~137 |
| 가상 단면 유량 출력 | Metal FV1 | 선택한 CPU·CUDA SWE 루프에는 호출이 없다. | LG1-141 |
| binary_out·save_depth 적용 | CPU FV1·DG2, Metal FV1 | CUDA Snapshot은 ASCII 수심을 무조건 쓴다. | LG1-138 |
| 평균 외의 여섯 운동량·수심 기울기 파일 | CPU·CUDA DG2 | FV2 Snapshot에는 기울기 출력이 없다. | LG1-108, 138 |
| 배수 후 운동량 제거 | Metal FV1 | CPU·CUDA 배수 함수는 H만 0으로 만든다. | LG1-027 |

LG1-149의 FREE6는 새 입력 키워드 지원을 뜻하지 않는다.
커널의 enum과 switch가 받는 숫자 6의 동작을 뜻한다.
CPU의 `swe/fv1.cpp:574-579`와 CUDA의 `cuda/cuda_boundary.cu:362-365`는 이 값에 기본 벽 분기를 적용한다.
이 차이는 문서가 설명하지 않는 추가 enum 처리로 C로 분류한다.

### 3.1 문서·주석에서 찾은 반대 근거

매뉴얼 텍스트 검색은 `rg -n -i '\b(FV1|FV2|DG2|CUDA|Metal|HLL|Krivodonova)\b'`로 수행했다.
검색 대상은 `_staging/recovery/extract/LISFLOOD-FP/pdf/lf-manual-{pdf,docx,bridge-docx}.txt`이다.
PDF·bridge 텍스트는 이 검색어와 일치하지 않았다.
Word 텍스트는 FV1·DG2·CUDA 설명과 옵션 적용 제외를 포함한다.
따라서 세 매뉴얼을 모두 SWE 이전 내용이라고 취급하지 않았다.

직접 연 쪽 이미지는 `user manual.docx p.15(변환본)`, `p.22(변환본)`, `p.24(변환본)`, `p.37(변환본)`이다.
Word p.15는 FV1·DG2의 CUDA 실행을 적는다.
Word p.22의 rainfall 적용 칸은 `All 2D models except FV1, DG2`이다.
같은 쪽의 infiltration·evaporation 적용 칸은 `All 2D models except FV1, DG2, Roe`이다.
같은 쪽의 drain_nodata 적용 칸은 `All 2D models`이다.
Word p.24의 speedthresh 설명은 `friction is not applied when the speed is below this threshold`이다.
이 설명은 저속 운동량을 유지하는 CPU DG2 경로를 뒷받침한다.
이 설명은 CUDA가 저속 운동량을 0으로 만드는 이유를 설명하지 않는다.
Word p.37은 `The rainfall file must have the same origin as the DEM`이라고 적는다.
같은 쪽은 강우 타일 크기를 DEM 셀 크기의 정수배로 요구한다.

README·INSTALL·VersionHistory 검색은 `rg -n -i 'fv1|fv2|dg2|metal|slope|manning|friction|cfl|nodata|rainfall|point.source|time.step|boundary|splitt'`로 수행했다.
코드 README는 CUDA 자동 빌드와 NetCDF 강우 의존성을 적는다.
VersionHistory는 8.0의 FV1·DG2 추가와 8.3의 수정 세 묶음을 적는다.
이 검색은 §2의 작은 값·경계 상태·시간 장부 차이에 대한 구현 간 설명을 찾지 못했다.
Metal 코드에는 안전 하한·부동소수점 조건 개선·NoData 재배치의 목적 주석이 있다.
따라서 이 보호 처리는 곧바로 결함으로 분류하지 않았다.
§5의 C는 구현 간 계산 차이를 주석·문서가 설명하지 않은 항목이다.
일반적인 안전 연산의 목적 주석과 CPU·CUDA·Metal 사이의 계산 조건 설명은 구분한다.

Shaw et al. (2021)의 [공식 논문](https://gmd.copernicus.org/articles/14/3577/2021/gmd-14-3577-2021.html)은 Eqs. (8)–(9)의 RK 단계와 Eq. (17)의 방향별 누적을 구분한다.
해석: LG1-044의 네 CUDA 커널은 이 방향별 누적과 대응한다.
이 확인은 코드만 보고 차원 분리라고 부르지 않을 근거이다.
Sharifian et al. (2023)의 [공식 논문](https://gmd.copernicus.org/articles/16/2391/2023/index.html)은 이 작업에서 서지와 대상 해법만 확인했다.
이 보고서는 그 논문을 FV2의 0.09·1.25 계수 근거로 쓰지 않는다.
이 보고서는 FV2 계수의 타당성을 판정하지 않고 코드에 있는 값을 기록한다.
따라서 그 타당성을 외부 원문 필요 X 행으로 새로 만들지 않았다.

## 4 노트 대조와 수정안

이 절은 현재 노트를 고치지 않는다.
아래 문장은 수정안이다.
아래의 `note:` 경로는 §1에서 정한 모델 디렉터리를 기준으로 한다.

| 관련 행 ID | 현재 노트의 원문 | 코드 대조 | 노트 수정안 |
|---|---|---|---|
| LG1-160 | `note:README.md:11` `- **버전**: **v8.2** (2024-07-29). **8.x 특징 = GPU multiwavelet DG2 + dynamic resolution adaptivity**(비균일격자 acc_nugrid).`; `:13`은 언어를 C++ + CUDA로 적는다. | `VersionHistory.h:23` `#define LF_Release "8.3"`; `package:README.md:3-5`는 8.2 기반 Metal 추가를 적는다. | “분석 대상은 공식 8.2 배포본에 공식 8.3 패치를 적용한 코드이다. 내부 버전 숫자는 checkpoint 호환을 위해 8.1.0으로 남는다. Apple 빌드는 Metal FV1 경로를 포함한다.” |
| LG1-001 | `note:source-analysis/lisflood-fp-architecture-source-map.md:61` `**dg2new = multiwavelet 적응**`; `:83` ``- `swe/dg2new.cpp` — DG2 multiwavelet 적응 격자(v8.2 핵심, Kesserwani)`` | `lisflood.cpp:794-796`은 dg2new 호출을 주석 처리한다. `swe/dg2new.cpp:304-306`은 고정 xsz·ysz 내부만 순회한다. | “dg2new는 균일 격자 CPU DG2의 비활성 별도 구현이다. 이 파일을 적응 격자 해법으로 분류하지 않는다.” |
| LG1-001 | `note:source-analysis/lisflood-fp-swe-fv1-dg2.md:291` ``**이 코드는 `lisflood.cpp:784`에서 주석 처리되어 빌드/실행에 포함되지 않는다.**`` | CMake 소스 목록은 dg2new를 제외한다. `makefile:31` `swe/dg2new.cpp \`는 legacy Make 소스 목록에 포함한다. | “현재 CMake 목록은 dg2new를 빌드하지 않는다. legacy Make 목록은 파일을 컴파일한다. main의 실행 호출은 주석 처리되어 있다.” |
| LG1-011 | `note:source-analysis/lisflood-fp-cuda-gpu.md:102` `### 4.1 차원분리(dimensional splitting) 업데이트`; `:114`는 “$U^x$ 를 입력”이라고 적는다. | Q3의 y 커널은 Uold로 플럭스를 계산한다. Uint는 x 기여 누적 배열이다. | “CUDA FV1은 갱신 전 상태로 x·y 플럭스를 계산하는 비분리 Euler 갱신이다. x 커널이 중간 배열을 쓴다. y 커널은 같은 Uold의 y 기여를 중간 배열에 더한다.” |
| LG1-012 | `note:source-analysis/lisflood-fp-swe-fv1-dg2.md:154-156`은 “면 $H^\star$ 평균을 쓰는 것이 정수해(lake-at-rest) 보존의 핵심 — well-balanced 이산화.”라고 적는다. | Q4의 CPU는 H를 갱신한 뒤 Zdagger의 eta를 다시 읽는다. | “Hstar는 갱신 전 상태이다. 현재 CPU 구현은 바닥 원천항의 Zdagger에 갱신 후 수심을 읽는다. CUDA·Metal은 갱신 전 수심을 읽는다. 부분 건조 가지의 차이는 결함 후보로 별도 기록한다.” |
| LG1-011 | `note:source-analysis/lisflood-fp-cuda-gpu.md:111` `$$HU=HU^0-\frac{\Delta t}{\Delta x}\big[(F_e.HU-F_w.HU)-S_{bed,x}\big]$$` | Q3에서 bed_source_x는 이미 dx로 나누어진 가속도형 항이다. | “코드의 괄호를 보존하여 `HU = U0.HU - dt * ((F_e.HU - F_w.HU)/dx - bed_source_x(...));`로 제시한다. Sbed를 플럭스 차분과 같은 괄호 안에 넣고 다시 dx로 나누지 않는다.” |
| LG1-024 | `note:source-analysis/lisflood-fp-cuda-gpu.md:161` ``- `HFIX2/HVAR3`(수위지정): $H_{new}=\min(0, \text{val}-Z)$, 변화량을 discharge 로 질량통계 누적.`` | CPU·CUDA는 실제 min을 쓴다. Metal과 수위 경계는 max를 쓴다. | “원문은 min이다. 이를 설명 없이 max로 고쳐 인용하지 않는다. 양의 목표 수심이 0이 되고 지반 아래 목표 수위에서 음수가 되는 결함 후보를 덧붙인다.” |
| LG1-021~023 | `note:source-analysis/lisflood-fp-swe-fv1-dg2.md:249`은 FREE를 “내부값 복사”로 적는다. `note:source-analysis/lisflood-fp-cuda-gpu.md:168`은 수위·유량·벽 상태를 한 줄로 요약한다. | CPU FREE·벽의 접선 self-assignment와 CUDA의 H 내부값 변경·Q 접선 제거가 있다. | “각 경계에서 내부·외부 상태를 나누어 적는다. CPU의 접선 self-assignment는 그대로 인용한다. CUDA의 수위 내부값 변경과 Q 경계 접선 0을 별도 행으로 쓴다.” |
| LG1-045~053 | `note:source-analysis/lisflood-fp-swe-fv1-dg2.md:192-195`는 두 RK 단계의 공통 파이프라인을 적는다. `:233`은 thin_depth 조건을 적는다. | Q12~Q14의 마찰·limiter 차이와 LG1-054의 미호출을 구분해야 한다. | “기본 RK 파이프라인은 유지한다. 가우스점 마찰의 상태 시점과 저속 가지를 별도로 적는다. y 최소 수심의 H1x 및 CUDA 최소 수심 검사의 동시 읽기·쓰기를 후보로 적는다. thin_depth 함수는 단계별 호출 근거가 아니다.” |
| LG1-081~085 | `note:source-analysis/lisflood-fp-swe-fv1-dg2.md:276`은 “동일 DG2 수학”이라고 적는다. `:289`는 면 재구성을 “$\pm\sqrt3$ 가우스점”이라고 적는다. | dg2new flux_y는 HU를 질량 플럭스로 반환한다. fixed 분기는 최종 상태 복사보다 먼저 반환한다. 면 값과 가우스점은 서로 다르다. | “DG2와 유사한 공간 연산자를 쓰는 비활성 구현이다. y 질량 플럭스와 fixed 상태 반영의 결함 후보를 적는다. 면 중심은 평균±sqrt(3)×기울기이다. 가우스점은 평균±기울기이다.” |
| LG1-058, 127~129, 134, 142, 145~146 | `note:source-analysis/lisflood-fp-cuda-gpu.md:181`은 가장자리 atomicAdd를 질량보존 통계로 요약한다. | atomicAdd의 존재만으로 강우·초기 체적·시간 분모·RK 가중치가 맞는지 알 수 없다. | “통계 장부는 상태 갱신과 별도로 대조한다. CPU DG2는 마지막 RK 플럭스만 집계한다. CUDA는 두 단계의 절반을 집계한다. CUDA의 시간 이중 누적과 초기 체적 0을 후보로 적는다. 침수 면적 기준과 강우 장부도 따로 적는다. 점 원천의 누적 체적 집계와 순간 Qin·Qout 누락도 구분한다.” |
| LG1-123, 140 | `note:manual-notes/lisflood-fp-user-manual.md:125`는 rainfall을 “전 2D”로 적는다. | 직접 본 Word 매뉴얼 p.22는 FV1·DG2를 제외한다. 현재 CUDA FV1·DG2와 Metal은 균일 강우 코드가 있다. | “PDF 기반 적용 범위를 Word 매뉴얼 또는 현재 backend에 자동 적용하지 않는다. CPU FV1·DG2는 동적 강우를 호출한다. CUDA FV1·DG2와 Metal FV1은 균일 강우도 호출한다. CUDA FV2는 동적 강우만 호출한다.” |
| LG1-100~108, 137~141 | `note:source-analysis/lisflood-fp-cuda-gpu.md:21-24`의 solver 표는 fv1·dg2·acc·acc_nugrid만 적는다. | CUDA FV2와 8.3 Metal FV1이 추가 대조 대상이다. | “FV2를 독립 행에 추가한다. Metal FV1을 별도 행에 추가한다. 세 FV1의 경계·원천·CFL·출력 차이를 링크한다.” |
| LG1-155 | `note:source-analysis/lisflood-fp-cuda-gpu.md:226`은 차원 분리를 포함한 완전한 1차 SWE라고 적는다. `:229`는 네 solver family가 같은 HLL을 공유한다고 적는다. | 이번 직접 대조가 확인한 HLL 공유 범위는 CUDA FV1·FV2·DG2이다. | “비분리 FV1 보존식으로 고친다. 공통 인프라와 실제 HLL 호출 공유를 구분한다. ACC·적응 해법의 내부 공유 여부는 이 보고서의 결론으로 확장하지 않는다.” |

LG1-160은 계산식 판정이 아닌 분석 대상 식별과 문서 목차 정정이다.
따라서 §5는 이 행을 H로 분류한다.

## 5 차이 결론

분류별 개수: C 31, E 32, F 10, H 11, X 0. 합계 84행(§5.2의 고유 행 ID 기준).

E는 정적 코드 결함 후보이다.
E의 강도는 원문 사이의 모순이 얼마나 직접적인지를 뜻한다.
강도는 실제 입력에서 오류를 재현했다는 뜻이 아니다.
8.3에서 고친 E는 8.2 결함으로 명시한다.
비활성 dg2new의 E는 현재 CPU 실행 경로와 구분한다.
C는 구현 간 계산 차이와 적용 제약의 설명 누락이다.
F는 적힌 조건에서 성립하는 변수·좌표·대수 표현의 대응이다.
F를 비트 일치나 전체 해법의 동등성으로 확대하지 않는다.
H는 이 계산 대조의 완료 조건으로 삼지 않는 항목이다.
이 작업은 A·B·D를 사용하지 않는다.

### 5.1 결론 전 반대 근거 확인

LG1-006의 등호 차이는 마찰이 운동량을 먼저 0으로 만들면 사라질 수 있다.
마찰이 꺼진 상태의 경계값에는 그 보정이 없다.
LG1-012의 Zdagger 차이는 수면이 두 면 바닥보다 높으면 사라진다.
평탄 지형과 완전 습윤 셀의 일치는 부분 건조 가지의 반박이 아니다.
LG1-017에서 fixed CUDA 분기는 생성자에서 dt=max_dt를 대입한다.
따라서 첫 dt=0 지적은 adaptive 분기에 한정한다.
CPU DG2도 강우·점 원천 뒤에 Tstep을 재계산한다(`swe/dg2.cpp:63-70`).
CPU DG2 역시 원천항과 흐름의 dt가 달라질 수 있다.
CPU FV1과 Metal FV1은 이 순서 차이를 공유하지 않는다.

LG1-045의 코드에는 가우스점 상태 시점을 바꾼다는 주석이 없다.
비활성 dg2new는 `swe/dg2new.cpp:238-246`에서 원 평균을 보관한 채 평균과 가우스점의 마찰 결과를 각각 만든다.
이 경로는 CUDA의 원 상태 사용을 뒷받침한다.
LG1-046의 CUDA 저속 0 처리는 CPU FV1과 같다.
이 사실은 CPU DG2의 유지 가지와 다른 이유를 설명하지 않는다.
LG1-047의 마찰 차이는 건조 제거를 거친 뒤 사라질 수 있다.
그러나 두 구현은 마찰 뒤에 면 플럭스를 계산한다.
건조 제거는 각 RK 단계 뒤에 있다.
LG1-049는 부동소수점 형식에 따라 norm 문턱을 선택하지 않는다.
따라서 float 최적화라는 해석만으로 `1e-12`와 `1e-6`의 차이를 소거하지 않는다.
LG1-051의 8.3 공유 배열 장벽은 limiter의 전역 H1x·H1y를 보호하지 않는다.
limiter 커널은 별도 커널이다.

LG1-120의 `lis::GhostRaster::allocate`는 `new [...]()`로 0 초기화한다.
그러나 CUDA Flow는 `cuda::GhostRaster::allocate_pinned`를 사용한다.
이 둘은 다른 함수이다.
현재 MaxField의 명시적 cudaMemset도 Flow 전체의 초기화를 대신하지 않는다.
[NVIDIA Runtime API](https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/group__CUDART__MEMORY.html)는 cudaMalloc이 메모리를 초기화하지 않는다고 명시한다.
LG1-121의 일반 호스트 DEM 포인터는 pageable 호스트 메모리 접근을 지원하는 장치에서는 직접 읽을 수 있다.
따라서 모든 CUDA 장치에서 실패한다고 단정하지 않는다.
선택한 호출은 해당 장치 능력에 따른 분기를 두지 않는다.

LG1-124의 원점 차이는 Word p.37의 같은 원점 입력 조건에서 사라진다.
해석: 같은 blx·bly와 양의 셀 크기에서 내부 DEM 행의 강우 tile_j는 강우 y 상한을 넘지 않는다.
따라서 Metal의 추가 원점 보정·범위 검사를 이유로 CPU·CUDA에 E를 부여하지 않았다.
`rain/rain.tpp:35`, `:45`의 has_same_origin·is_tile_size_multiple_of_grid는 이 대조 대상 호출 경로에서 사용되지 않는다.
LG1-128의 두 accumulate_mass는 유량 집계를 나누려는 구조이다.
그러나 cumulative_time도 각 호출마다 늘어난다.
LG1-129의 checkpoint reader에는 previous_volume을 읽는 행이 있다.
선택한 CUDA SWE run은 그 reader를 호출하지 않는다.
LG1-145의 점 원천 체적은 첫 accumulate_mass에서 누적 장부에 들어간다.
따라서 이 후보는 점 원천 체적이 장부 전체에서 사라진다는 주장이 아니다.
문제는 두 번째 집계 뒤의 순간 Qin·Qout이 점 원천을 포함하지 않는다는 점이다.
`cuda/cuda_stats.cuh:36`의 BCs/PSs 주석은 두 집계 사이의 초기화를 설명하지 않는다.
LG1-146의 U와 Uold는 서로 다른 Flow 객체를 참조한다.
`cuda/fv1/cuda_fv1_solver.cu:543`의 `std::swap(Uold, U);`는 두 객체의 내용을 교환한다.
이 교환은 이름 U를 현재 상태의 다른 이름으로 만들지 않는다.

### 5.2 차이별 결론 표

| 행 ID | 항목 | 결론 | 근거(원문 인용) | 노트에 쓸 결론 문장 |
|---|---|---|---|---|
| LG1-001 | dg2new의 선택·빌드 | H | `lisflood.cpp:796` `//solver.solve();`; `makefile:31` `swe/dg2new.cpp \` | dg2new는 별도 비활성 CPU 구현이다. 컴파일 목록과 실행 선택을 구분한다. |
| LG1-002 | 수치 형식 | F | `lisflood.h:76` `#define NUMERIC_TYPE double`; `:87` `#define NUMERIC_TYPE float`; Metal FlowVector는 float이다(`metal/fv1/metal_fv1_kernels.metal:116-118`). | 같은 보존변수를 쓰지만 수치 형식은 빌드별로 다르다. 식 대응은 부동소수점 재현성을 보장하지 않는다. |
| LG1-006 | 재구성의 임계값 등호 | E·중간 | `swe/fv1/modifiedvars.cpp:346` `if (H > Solverptr->DepthThresh)`; `cuda/cuda_flow.cu:56` `if (H >= cuda::solver_params.DepthThresh)`; Metal `metal/fv1/metal_fv1_kernels.metal:389`은 `>`이다. | 마찰을 끈 FV1에서 임계값과 같은 수심의 재구성 속도는 CPU·Metal과 CUDA가 다르다. |
| LG1-009 | Metal y 좌표 | F | `metal/fv1/metal_fv1_simulate.mm:579` `d_HV[gpu_idx] = -(float)h_HV[cpu_idx];`; `:725` `h_HV[cpu_idx] = -(NUMERIC_TYPE)d_HV[gpu_idx];` | Metal의 남향 운동량은 입출력 부호 변환으로 CPU의 북향 운동량과 대응한다. |
| LG1-010 | Metal HLL 보호 | C | `metal/fv1/metal_fv1_kernels.metal:123` `float H_neg = max(U_neg.H, 0.0f);`; `:172` `if (abs(denom) < 1e-10f) return FlowVector{0.0f, 0.0f, 0.0f};` | Metal HLL의 안전 연산과 작은 분모 단락을 구현별 조건으로 적는다. 신호속도 절단만으로 식 차이를 단정하지 않는다. |
| LG1-011 | FV1 방향별 누적 | F | `cuda/fv1/cuda_fv1_solver.cu:540-541`의 Q3은 y 커널에 `(Uold, Ux, U, DEM, Zstar_y, mass_stats);`를 전달한다. | CUDA·Metal FV1은 같은 이전 상태의 두 방향 기여를 누적한다. 이 구조를 차원 분리로 부르지 않는다. |
| LG1-012 | CPU FV1 바닥항의 상태 시점 | E·중간 | `swe/fv1.cpp:441-442`의 Q3 뒤 `:450-452`의 Q4가 바닥항을 부른다. `swe/fv1/modifiedvars.cpp:329` `NUMERIC_TYPE H = Arrptr->H[j*Parptr->xsz + i];`; GPU는 Q4의 이전 상태 eta를 쓴다. | CPU FV1은 Hstar와 Zdagger에 다른 시점의 수심을 사용할 수 있다. 부분 건조 가지의 결함 후보이다. |
| LG1-014 | Metal 마찰의 작은 값 보호 | C | `metal/fv1/metal_fv1_kernels.metal:311` `float h_safe = max(h, MIN_SAFE_H);`; `:329` `float speed_safe = speed + 1e-12f; // Very small epsilon` | Metal 마찰의 안전 수심과 속도 epsilon은 기본 Manning 식에 추가한 조건이다. |
| LG1-015 | Metal 최종 수심 절단 | C | `metal/fv1/metal_fv1_kernels.metal:615`의 Q3은 max(0,...)를 쓴다. `cuda/fv1/cuda_fv1_solver.cu:469`은 절단 없이 H를 대입한다. | Metal FV1은 최종 수심을 0으로 절단한다. 이 체적 보정의 별도 질량 계수는 없다. |
| LG1-017 | 원천항과 흐름의 dt | E·강함 | `cuda/cuda_solver.cu:11` `__managed__ NUMERIC_TYPE lis::cuda::dt;`; adaptive 생성자에 dt 대입이 없다. Q7은 원천항을 먼저 적용한다. CPU DG2도 `swe/dg2.cpp:63-70`의 순서를 쓴다. | CUDA SWE와 CPU DG2는 원천항의 간격과 흐름의 간격이 달라질 수 있다. CUDA adaptive의 첫 원천항은 dt=0을 읽는다. |
| LG1-018 | FV1 CFL 영역 | C | `cuda/fv1/cuda_fv1_solver.cu:73-75`의 Q6은 `ysz+2`와 pitch를 순회한다. CPU `swe/fv1.cpp:594-596`은 내부만 순회한다. | CUDA FV1은 ghost 상태까지 CFL 최소에 포함한다. CPU·Metal FV1은 내부만 포함한다. |
| LG1-019 | Metal fixed 옵션 | E·강함 | `metal/fv1/metal_fv1_simulate.mm:1024` `NUMERIC_TYPE adaptive_dt = computeTimestep();`; `:1027`의 adaptive_ts 검사는 첫 단계 안에만 있다. CPU `swe/fv1.cpp:61`은 매번 검사한다. | Metal FV1은 fixed 옵션을 첫 단계 이후 유지하지 않는다. |
| LG1-020 | Metal CFL 임계값 | E·강함 | `metal/fv1/metal_fv1_kernels.metal:11` `#define DEPTH_THRESH 1e-3f`; `:648` `if (h > DEPTH_THRESH) {`; 같은 커널의 마찰은 `:306` `if (h > solver.depth_thresh) {`이다. | Metal CFL의 고정 임계값은 입력 depththresh와 불일치할 수 있다. |
| LG1-021 | 지정 수위의 내부 상태 | E·중간 | `swe/fv1.cpp:532` `//H_inside = H_outside;`; `cuda/cuda_boundary.cu:402` `U_const.H = U_outside.H;`; Metal은 out만 바꾼다(`metal/fv1/metal_fv1_kernels.metal:64-67`). | CUDA의 지정 수위 경계는 내부 리만 상태의 수심도 바꾼다. CPU·Metal과 다른 경계식이다. |
| LG1-022 | 지정 유량의 접선·문턱 | E·중간 | `swe/fv1.cpp:558` `HV_outside = HV_inside;`; `cuda/cuda_boundary.cu:355` `U_outside.HV = C(0.0);`; `:356`은 1e-6, CPU `:549`는 1e-12이다. | CUDA 유량 경계는 접선 운동량과 미소 유량 수심 보정 기준에서 CPU·Metal과 다르다. |
| LG1-023 | CPU FREE·벽 접선 | E·강함 | `swe/fv1.cpp:526`, `:578` `HV_outside = HV_outside;`; 호출자는 `:329`에서 HV_outside를 0으로 둔다. Metal `metal/fv1/metal_fv1_kernels.metal:81` `out.Qt = in.Qt;` | CPU FV1의 FREE·벽 경계는 접선 운동량 복사를 누락한 후보이다. |
| LG1-024 | 지정 수위 점 원천의 min | E·강함 | `swe/fv1.cpp:207` `NUMERIC_TYPE H_new = FMIN(C(0.0), BCptr->PS_Val[ps_i] - Z);`; CUDA Q8 앞 표도 FMIN이다. Metal `metal/fv1/metal_fv1_simulate.mm:931` `float h_new = std::max(0.0f, h_target - z);`; 같은 CPU 경계 `swe/fv1.cpp:531`도 FMAX이다. | CPU·CUDA의 수위형 점 원천은 min/max 반전 결함 후보이다. 원문 min을 보존하여 인용한다. |
| LG1-025 | 점 유량의 셀 폭 | F | `swe/fv1.cpp:228` `H += Q * Parptr->dx * Solverptr->Tstep / Parptr->dA;`; `cuda/cuda_boundary.cu:128` `Hvalue += discharge * cuda::dt / cuda::geometry.dx;`; `cuda/io.cpp:18` `geometry.dy = geometry.dx;` | 정사각 셀에서는 두 점 유량 수심식이 같다. 직사각 셀로 일반화하지 않는다. |
| LG1-026 | Metal 작은 점 원천 | C | `metal/fv1/metal_fv1_simulate.mm:937` `if (std::abs(val) > 1e-9f) {` | Metal은 작은 점 원천 갱신을 생략한다. 유량형과 수위형에서 val의 단위가 다르다. |
| LG1-027 | Metal 배수의 판별·운동량 | C | Q8의 `if (abs(z - nodata) < 1.0f) {`와 HU·HV=0; CPU `swe/fv1.cpp:174`의 허용차는 1e-6이다. | Metal NoData 배수는 더 넓은 판별 허용차와 운동량 제거를 사용한다. |
| LG1-028 | Metal 지형 조건 개선 | C | `metal/fv1/metal_fv1_simulate.mm:537` `gpu_nodata = (float)(max_valid - min_valid) + kMargin;  // wall`; `:539` `gpu_nodata = -kMargin;                                   // pit`; `:580` `d_DEM[gpu_idx] = dem - dem_offset;` | 유효 지형의 일정 이동과 NoData의 별도 재배치를 구분한다. 전자만으로 후자까지 동일한 식이라고 일반화하지 않는다. |
| LG1-029 | CPU 배수 통계의 공유 갱신 | E·강함 | `swe/fv1.cpp:167` `#pragma omp parallel for`; `swe/stats.cpp:62` `BCptr->Qout -= Q;`; CUDA `cuda/cuda_boundary.cu:92`는 atomicAdd이다. CPU의 다른 경계 집계 `swe/stats.cpp:78`은 reduction이다. | OpenMP CPU FV1 배수는 공유 유입·유출 계수를 동시 갱신할 수 있다. |
| LG1-043 | DG2 바닥항 부호·계수 | F | CPU `swe/dg2.cpp:993` `return C(2.0) * Solverptr->g * Hstar * Zdagger;`; CUDA `cuda/dg2/cuda_dg2_solver.cu:166` `Sbx.HU1x = -C(2.0)*SQRT(C(3.0)) * g*Hstar_1x*Zdagger_1x / cuda::geometry.dx;`; Q10에 바깥 계수를 인용했다. | DG2 바닥항은 연산자 바깥 계수를 포함하면 같은 식이다. |
| LG1-044 | DG2 방향별 RK2 | F | `swe/dg2.cpp:749-750`의 Q11; `cuda/dg2/cuda_dg2_solver.cu:437-438`의 Q11은 `return Ux[j*cuda::pitch + i] + C(0.5)*cuda::dt*Ly;`를 반환한다. | CUDA의 방향별 커널 누적은 CPU와 같은 RK2이다. |
| LG1-045 | CPU DG2 가우스점 마찰 상태 | E·강함 | `swe/dg2/friction.cpp:27` `friction(Solverptr, H, HU, HV, n);` 뒤 Q12의 gauss_lower/upper가 평균 HU·HV를 읽는다. CUDA `cuda/dg2/cuda_dg2_solver.cu:651-673`은 원 상태 U를 먼저 보관한다. | CPU DG2는 마찰 후 평균 운동량을 가우스점 마찰에 다시 사용한다. CUDA·dg2new와 다른 상태 시점이다. |
| LG1-046 | DG2 저속 운동량 | E·중간 | `swe/dg2/friction.cpp:91-94`의 Q12는 return뿐이다. CUDA `cuda/dg2/cuda_dg2_solver.cu:619-620` `HU = C(0.0);` / `HV = C(0.0);` | 저속 DG2의 운동량은 CPU가 유지하고 CUDA가 제거한다. |
| LG1-047 | 건조 평균 셀의 마찰 | E·중간 | `swe/dg2/friction.cpp:25` `if (H <= Solverptr->DepthThresh) continue;`; CUDA `cuda/dg2/cuda_dg2_solver.cu:673` `friction(n, U.H, Uref.HU, Uref.HV);`와 `:675-678`의 네 점 호출 | CPU DG2의 평균 건조 셀은 가우스점 마찰도 건너뛴다. CUDA는 각 점 수심으로 판단한다. |
| LG1-049 | DG2 limiter norm 문턱 | E·중간 | `swe/dg2/slope_limiter.cpp:314` `if (FABS(norm) > C(1e-12))`; `cuda/dg2/cuda_dg2_slope_limit.cu:30` `if (FABS(norm) > C(1e-6))`; 양쪽 DS식은 Q13 앞에 대조했다. | CPU·CUDA DG2의 작은 norm 처리는 같은 Krivodonova 조건을 활성화하지 않을 수 있다. |
| LG1-050 | CPU y 최소 수심의 잘못된 축 | E·강함 | `swe/dg2/slope_limiter.cpp:381` `NUMERIC_TYPE backward_H1x = U.H1x[(j + 1) * Parptr->xsz + i];`; CUDA `cuda/dg2/cuda_dg2_slope_limit.cu:101`은 H1y를 읽는다. CPU y 제한의 `:219`는 eta1y이다. | CPU DG2의 y 최소 수심 검사가 x 기울기를 쓰는 축 혼동 후보이다. |
| LG1-051 | CUDA limiter의 동시 읽기·쓰기 | E·중간 | Q14의 `Stencil::minH_x(flow, i, j);` 뒤 `U.H1x = ...`; `cuda/dg2/cuda_dg2_slope_limit.cu:79`은 이웃 `flow.H1x`를 읽는다. CPU는 scratch를 별도 반영한다. | CUDA DG2 limiter의 최소 수심 검사는 다른 스레드가 바꾸는 기울기를 읽을 수 있다. |
| LG1-052 | limiter ON의 둘레 처리 | C | CPU `swe/dg2.cpp:319-326`은 limiter와 둘레 0 처리를 선택한다. CUDA `cuda/dg2/cuda_dg2_solver.cu:926` `zero_perimeter_slopes(DEM, Uold);`는 limiter 뒤에도 실행한다. | CUDA DG2는 limiter 사용 여부와 관계없이 둘레의 두 방향 기울기를 제거한다. |
| LG1-053 | limiter maxH의 시점·범위 | C | `swe/dg2.cpp:62`의 maxH는 강우 전이다. `cuda/dg2/cuda_dg2_solver.cu:917` `maxH.update(Uold);`는 강우 뒤이다. CUB 집계 elements는 ghost를 포함한다. | DG2의 0.30×maxH 분기는 CPU·CUDA에서 다른 기준 상태를 사용할 수 있다. |
| LG1-057 | FREE 건조 기울기 제거 | C | CPU `swe/dg2.cpp:618-621`의 Q14는 H만 바꾼다. CUDA `cuda/dg2/cuda_dg2_solver.cu:520-521`은 H1x·H1y도 0으로 만든다. | CUDA DG2는 FREE 건조 경계에서 수심 기울기도 제거한다. |
| LG1-058 | CPU DG2의 RK 질량 가중치 | E·강함 | `swe/dg2.cpp:75-79`는 두 RK 뒤 한 번 집계한다. CUDA `cuda/dg2/cuda_dg2_solver.cu:264`는 `C(0.5)` 가중치로 각 단계의 F_e.H를 넣는다. Q11의 RK2는 두 공간 기여의 평균이다. | CPU DG2 질량 장부는 둘째 RK 플럭스만 사용한다. 상태 갱신의 RK 가중치와 맞지 않을 수 있다. |
| LG1-059 | CPU DG2 배수 미호출 | E·중간 | `swe/dg2.cpp:74-85`에 배수가 없다. `cuda/dg2/cuda_dg2_simulate.cu:172-173`의 Q14는 drain_nodata_water를 부른다. Word p.22의 적용 칸은 `All 2D models`이다. | drain_nodata는 CPU FV1과 GPU SWE에서 실행되지만 CPU DG2 루프에는 적용되지 않는다. |
| LG1-080 | dg2new 수정 지형식 | F | `swe/dg2new.cpp:712` `DEM_LR -= delta;`; `swe/dg2/modifiedvars.cpp:443` `return Zstar - getmax(C(0.0), -(ETA - Zstar));`; delta 원문은 `swe/dg2new.cpp:695`, `:699`이다. | dg2new의 방향별 수정 지형은 현재 셀을 기준으로 한 Zdagger의 다른 표현이다. |
| LG1-081 | dg2new y 질량 플럭스 | E·강함·비활성 | `swe/dg2new.cpp:747-752`의 Q15는 첫 성분이 `HU,`이다. `cuda/cuda_flow.cu:37`의 첫 성분은 HV이다. CPU `swe/flux.cpp:28`도 HV를 법선 질량 플럭스로 전달한다. | 비활성 dg2new의 flux_y는 y 질량 플럭스에 HU를 쓰는 결함 후보이다. |
| LG1-082 | dg2new fixed 상태 반영 | E·강함·비활성 | `swe/dg2new.cpp:769` `if (Statesptr->adaptive_ts == OFF) return;`가 `:789`의 `Arrptr->H[j*Parptr->xsz+i] = H_new[j*Parptr->xsz+i];` 호출 경로보다 앞선다. | 비활성 dg2new의 fixed 분기는 최종 수심·기울기를 다음 상태로 복사하지 않는다. |
| LG1-083 | dg2new 미완성 경계 | H | `swe/dg2new.cpp:300` `// FIXME: BC treatment`; `:304-306`은 둘레를 제외한다. 현재 main은 이 solver를 호출하지 않는다. | dg2new의 경계 시제품을 기본 CPU 경계로 설명하지 않는다. |
| LG1-084 | dg2new의 빠진 주변 처리 | C | `swe/dg2new.cpp:101-109`은 마찰·RK·시간·통계·출력만 부른다. `swe/dg2.cpp:63-79`의 강우·점 원천·선택적 제한·최대값·경계 집계와 다르다. | dg2new에는 실제 DG2 solve의 원천항·limiter·질량 주변 처리가 연결되지 않는다. |
| LG1-085 | dg2new 첫 dt·건조 등호 | C | `swe/dg2new.cpp:178` `Solverptr->Tstep = 1e-5;`; `swe/dg2.cpp:43` `Solverptr->Tstep = 1e-6;`; Q11 뒤 건조 조건은 `<`이다. | dg2new의 첫 간격과 건조 등호는 기본 DG2와 다르다. |
| LG1-086 | dg2new 면 속도의 문턱 | C | `swe/dg2new.cpp:676` `if (left.H > Solverptr->DepthThresh)`; `swe/dg2/modifiedvars.cpp:234` `if (H >= Solverptr->DepthThresh)` | 비활성 dg2new와 기본 DG2는 임계값과 같은 면 수심에서 다르게 운동량을 재구성한다. |
| LG1-100 | FV2 면 값 정규화 | F | `cuda/fv2/cuda_fv2_flow.cu:67-68`의 0.5×기울기와 `cuda/dg2/cuda_dg2_flow.cu:88-89`의 sqrt(3)×기울기 | 계면 값은 기울기의 2sqrt(3) 배율 변환으로 대응한다. 이 변환은 해법 전체를 같게 하지 않는다. |
| LG1-101 | FV2 기울기 공간 연산자 부재 | C | Q16의 `Lx.set_0(-(F_e - F_w)/cuda::geometry.dx);`; DG2 Q10에는 `Lx.set_1x(...)`도 있다. | FV2는 DG2 기울기 공간 연산자를 사용하지 않는다. 기울기는 선택적 재구성 단계가 만든다. |
| LG1-102 | FV2 제한식 | C | `cuda/fv2/cuda_fv2_slope_limit.cu:15` `if (stencil_minH <= C(0.09)) return C(0.0);`; `cuda/fv2/cuda_fv2_slope_limit.cu:36` `NUMERIC_TYPE beta = C(1.25);` | FV2의 고정 수심 문턱과 비율 제한을 DG2의 Krivodonova·minmod와 구분한다. |
| LG1-103 | FV2 지형 평균만 사용 | C | `cuda/fv2/cuda_fv2_dem.cu:28-31`은 DEM._0의 최대이다. DG2 `cuda/dg2/cuda_dg2_dem.cu:235` `return _0[idx] + SQRT(C(3.0))*_1x[idx];` | CUDA FV2는 DG2 지형 기울기 파일을 사용하지 않는다. |
| LG1-104 | FV2 바닥항 대수 | F | `cuda/fv2/cuda_fv2_solver.cu:127` `NUMERIC_TYPE Zdagger_1x = (Zdagger_e - Zdagger_w) / C(2.0);`; `:132`의 -2×g×Hstar×Zdagger_1x/dx | 계수 2를 소거하면 정수압 평균 수심과 수정 지형 차분의 곱이다. 재구성 수면의 정의는 FV1과 구분한다. |
| LG1-106 | FV2 평균 마찰 | C | `cuda/fv2/cuda_fv2_solver.cu:547` `friction(n, U.H, Uref.HU, Uref.HV);`; DG2 `cuda/dg2/cuda_dg2_solver.cu:675-678`은 네 가우스점에도 적용한다. | FV2는 평균 운동량에만 마찰을 적용한다. |
| LG1-107 | FV2 균일 강우 미연결 | C | `cuda/fv2/cuda_fv2_solver.cu:754-760`의 update_uniform_rain은 `return;`뿐이다. `cuda/fv2/cuda_fv2_simulate.cu:134-139`는 DynamicRain만 호출한다. | CUDA FV2는 이 루프에서 균일 rainfall을 적용하지 않는다. |
| LG1-108 | FV2 기울기 출력 부재 | C | `cuda/fv2/cuda_fv2_snapshot.cu:32`는 H, `:41-42`는 HU·HV를 쓴다. DG2 `cuda/dg2/cuda_dg2_snapshot.cu:39-40`은 H1x·H1y도 쓴다. | FV2 출력은 DG2의 기울기 결과 파일을 제공하지 않는다. |
| LG1-120 | 초기값 누락 | E·강함 | `cuda/cuda_util.cu:53` `checkCudaErrors(cudaMallocHost(&ptr, size));`; `cuda/dg2/cuda_dg2_simulate.cu:58-59`는 평균 HU·HV만 초기화한다. CPU `swe/dg2/fields.cpp:308-311`은 운동량 기울기를 0 할당한다. | CUDA의 시작 파일 없는 필드·ghost·DG2 운동량 기울기에는 명시적 초기화 경로가 빠져 있다. |
| LG1-121 | 점 원천의 호스트 DEM | E·중간 | `cuda/fv1/cuda_fv1_simulate.cu:157` `cuda::Boundary::update_point_sources(d_U.H, DEM,`; `cuda/cuda_dem.cu:75` `DEM = lis::GhostRaster::allocate(geometry);`; 흐름은 `:169-170`에서 d_DEM을 가진 Solver를 쓴다. | CUDA 수위형 점 원천의 DEM 포인터는 일반 호스트 메모리를 읽지 못하는 장치에서 실패할 수 있다. |
| LG1-122 | ghost 좌표·보간 | F | `swe/boundary.cpp:37`의 `- j - 1`과 `cuda/cuda_boundary.cu:433`의 `- j`; `swe/boundary.cpp:23`, `cuda/cuda_boundary.cu:31`의 보간식은 `a1*values[i] + a2*values[i - 1]`이다. | ghost 인덱스를 내부 0 기반 좌표로 환산하면 경계 인덱스와 시계열 보간은 같다. |
| LG1-123 | 균일 강우·원천항 순서 | C | `swe/fv1.cpp:43-44`는 동적 강우 다음 점 원천이다. CUDA `cuda/fv1/cuda_fv1_simulate.cu:149-153`은 균일 강우도 호출한다. Metal `metal/fv1/metal_fv1_simulate.mm:1046`은 점 원천을 먼저 적용한다. | 균일 강우의 지원과 H 원천·강우의 적용 순서는 backend별로 기록한다. |
| LG1-124 | Metal 강우 원점·범위 확장 | C | `metal/fv1/metal_fv1_kernels.metal:755` `float x_offset = dem_geom.blx - rain_geom.blx;`; Q17의 네 경계 검사; Word p.37은 같은 원점을 요구한다. | 문서가 허용한 같은 원점 조건에서 CPU·CUDA 식을 결함으로 판정하지 않는다. Metal의 추가 원점 보정과 범위 검사는 확장 처리이다. |
| LG1-125 | 강우 부호 처리 | C | `cuda/cuda_rain.cu:58`은 부호 제한 없이 더한다. Metal `metal/fv1/metal_fv1_kernels.metal:794` `if (rate > 0.0f) {`; `:738` `float increment = max(-H[idx], rain_rate * dt);` | Metal은 동적 음수 강우를 버린다. Metal의 균일 음수 강우는 현재 수심으로 제한된다. |
| LG1-126 | Metal 강우 캐시 | C | `metal/fv1/metal_fv1_simulate.mm:1075` `if (time >= last_rain_time + 1.0 \|\| last_rain_time < 0) {` | Metal의 강우 자료는 업로드 간격 1 s 조건을 거친다. 짧은 자료 간격의 결과를 CPU·CUDA와 같다고 일반화하지 않는다. |
| LG1-127 | 강우 질량 장부 | E·강함 | `rain/rain.tpp:180` `total_rain_mass += inc*Parptr->dA;`; `swe/stats.cpp:14-15`의 Verror에는 이 강우가 없다. Metal `metal/fv1/metal_fv1_simulate.mm:1104` `boundCs->VolInMT += (NUMERIC_TYPE)interval_rain_vol;` | CPU SWE·CUDA의 강우 체적은 Verror 유입 장부에 빠져 있다. Metal은 강우를 유입 체적에도 넣는다. |
| LG1-128 | CUDA 시간 이중 누적 | E·강함 | `cuda/cuda_stats.cu:83` `cumulative_time += cuda::dt;`; FV1 `cuda/fv1/cuda_fv1_simulate.cu:159`, `:176`의 두 accumulate_mass; `cuda/cuda_stats.cu:118`은 그 시간으로 나눈다. | CUDA Qerror의 시간 분모는 두 질량 집계 호출 때문에 물리 적분 시간과 달라질 수 있다. |
| LG1-129 | CUDA 초기 체적 0 | E·강함 | `cuda/cuda_stats.cuh:35` `NUMERIC_TYPE previous_volume = C(0.0);`; CPU `swe/fv1.cpp:32`는 DomainVol로 초기 체적을 기록한다. 선택한 CUDA run에는 그 대입이 없다. | 초기 저류가 있는 CUDA SWE의 첫 질량 오차에는 초기 체적이 포함될 수 있다. |
| LG1-130 | 최대 수심 배열 | E·강함·8.2에서 발생·8.3에서 수정 | `v8.2:cuda/cuda_max_field.cu:97` `maxH = GhostRaster::allocate_pinned_H(geometry); //// change to allocate_pinned_H()`; `package:lisflood-8.2-to-8.3.patch:111-112` `+	maxH = GhostRaster::allocate_device(geometry);` / `+	cudaMemset(maxH, 0, lis::GhostRaster::elements(geometry)*sizeof(NUMERIC_TYPE));` | 8.2의 최대 수심 배열 크기·초기화 결함은 8.3이 고쳤다. 현재 미수정 결함으로 보고하지 않는다. |
| LG1-131 | grid-stride 공유 배열 재사용 | E·강함·8.2에서 발생·8.3에서 수정 | `v8.2:cuda/fv1/cuda_fv1_solver.cu:379-382`에는 패스 끝 장벽이 없다. `package:lisflood-8.2-to-8.3.patch:196-197` `+			// shared memory is rewritten in the next pass: wait for every reader` / `+			__syncthreads();` | FV1·FV2·DG2의 반복 패스 끝 공유 배열 보호 결함은 8.3이 고쳤다. |
| LG1-132 | 0 배수량 atomic 생략 | H | `cuda/cuda_boundary.cu:289` `if (Hold == C(0.0)) continue; // dry: nothing to add to the mass balance`; `package:lisflood-8.2-to-8.3.patch:79` `+				if (Hold == C(0.0)) continue; // dry: nothing to add to the mass balance` | 건조 NoData의 0 추가 생략은 배수식을 바꾸지 않는 최적화이다. |
| LG1-133 | 최대 수심 정밀도 인수 | E·강함 | Q20의 여섯 번째 인수 `pars.output_precision`과 `cuda/cuda_max_field.cuh:20-21`의 `int acceleration,` / `int precision = DEFAULT_PRECISION` | CUDA SWE의 .max 정밀도에는 사용자 지정값이 전달되지 않는 인수 결함 후보가 남아 있다. |
| LG1-134 | 침수 면적 문턱 | C | `swe/stats.cpp:36`은 H>0.01을 센다. `cuda/cuda_stats.cu:45` `histogram_levels[1] = DepthThresh;` | CPU·Metal과 CUDA의 침수 면적 문턱을 구분한다. |
| LG1-136 | 건조 관측점 속력 미대입 | E·강함 | Q18에는 wet 속력 대입만 있다. `cuda/sample.cpp:253-254`는 `sample_buf.speed[offset+p]`를 읽는다. CPU `swe/output.cpp:86` `speed = C(0.0);` | CUDA의 건조 관측점 속력은 0으로 기록되지 않고 미정 또는 이전 값일 수 있다. |
| LG1-137 | Metal 관측점 기록 부재 | C | `swe/fv1.cpp:76` `write_depth_samples(Fptr, Parptr, Solverptr, Stageptr, Arrptr);`; Metal `metal/fv1/metal_fv1_simulate.mm:1413-1460`에는 해당 호출이 없다. | Metal FV1의 격자 출력 지원과 stage·velocity 관측점 지원을 구분한다. |
| LG1-138 | CUDA 격자 출력 옵션 | C | `swe/output.cpp:113` `if (Statesptr->save_depth == ON)`; `cuda/dg2/cuda_dg2_snapshot.cu:38` `writer_H = write_async(U.H, ".wd", 0, call_gzip);` | CUDA Snapshot은 수심 저장과 binary_out 옵션을 CPU처럼 분기하지 않는다. |
| LG1-139 | 공통 checkpoint 함수 | H | `cuda/cuda_simulate.cu:147` `//read_checkpoint(filenames, states, pars, solver, BCptr, CSTypePtr, Arrptr, verbose);`; 선택한 run에는 read/write_checkpoint 호출이 없다. | 공통 함수의 정의만으로 CUDA SWE checkpoint 지원을 단정하지 않는다. |
| LG1-140 | 지원 제외 옵션의 거부 | H | Word p.22는 infiltration·evaporation에서 FV1·DG2를 제외한다. Metal Q19는 `states.rainfallmask == ON \|\| states.routing == ON`에서 종료한다. | SWE 지원 대상 밖 옵션과 backend의 오류 메시지 차이를 계산식 차이와 분리한다. |
| LG1-141 | Metal 가상 단면 | C | `metal/fv1/metal_fv1_simulate.mm:1432` `CalcVirtualGauge(i, pars.xsz + 1, arrays.FHx, arrays.FHy, &stage);`; Q19의 전체 조건과 식은 이 결과에 dx 또는 dy를 곱한다. | Metal 가상 단면 출력은 호스트에서 재계산한 플럭스를 사용한다. |
| LG1-142 | Qin·Qout의 시간 의미 | C | `metal/fv1/metal_fv1_simulate.mm:699` `boundCs->Qout += (NUMERIC_TYPE)(out / elapsed);`; CPU `swe/stats.cpp:45` `BCptr->Qout = C(0.0);`; CUDA `cuda/cuda_stats.cu:116`은 h_instantaneous_mass를 반환한다. | Metal 경계 유량은 동기화 구간 평균이다. CPU·CUDA는 마지막 단계의 경계 유량을 쓴다. 점 원천 누락은 LG1-145에서 별도로 판정한다. |
| LG1-143 | raster 기하 검사 | C | `cuda/io.cpp:18` `geometry.dy = geometry.dx;`; `:70` `if (expected.xsz != candidate.xsz \|\| expected.ysz != candidate.ysz)` | CUDA의 ASCII 입력은 정사각 셀이다. 보조 raster의 원점·셀 크기 일치는 이 검사에서 확인하지 않는다. |
| LG1-145 | CUDA 순간 점 원천 유량 누락 | E·강함 | `cuda/cuda_stats.cuh:36` `MassStats* d_instantaneous_mass; /**< through BCs/PSs during timestep*/`; `cuda/fv1/cuda_fv1_simulate.cu:160` `stats_collector.zero_instantaneous_mass();`; `cuda/cuda_stats.cu:116` `h_instantaneous_mass,`; CPU `swe/stats.cpp:113` `BCptr->Qin += Qin;` | CUDA의 누적 체적 집계와 순간 유량 출력을 구분한다. 순간 Qin·Qout은 주석의 PSs와 달리 점 원천을 포함하지 않는다. |
| LG1-146 | 현재 FV1 ghost를 지우지 않음 | E·강함 | `cuda/fv1/cuda_fv1_solver.cu:516` `zero_ghost_cells_north_south<<<1, CUDA_BLOCK_SIZE>>>(U);`; `:550` `return Uold;`; `cuda/cuda_stats.cu:33`은 ghost 포함 elements를 쓴다. | CUDA FV1의 통계 전 ghost 제거는 현재 상태 버퍼를 대상으로 하지 않는다. |
| LG1-147 | NoData 치환 차이 | C | `swe/input.cpp:27`의 1e-12와 `cuda/io.cpp:115`의 1e-5; 지형 기울기는 `cuda/dg2/cuda_dg2_dem.cu:105` `AsciiRaster::read(file, array, geometry, pitch, offset);`만 호출한다. | 입력 NoData 허용차와 지형 기울기 치환 여부를 해법별로 적는다. |
| LG1-148 | 초기 수위의 음수 수심 | E·강함 | `input.cpp:1187`의 max(H-DEM,0); `cuda/io.cpp:136` `H_value = H_value - DEM_value;`; 같은 CUDA 재구성 `cuda/cuda_flow.cu:48`은 FMAX(0,...)이다. | CUDA startelev는 지반 아래 수위에서 음수 초기 수심을 만드는 결함 후보이다. |
| LG1-149 | Metal FREE6 enum | C | `metal/fv1/metal_fv1_kernels.metal:78` `} else if (type == BC_FREE \|\| type == BC_FREE6) {`; CPU `swe/fv1.cpp:574-579`는 기본 벽 분기이다. | Metal의 숫자 6 경계는 transmissive 처리이다. 이 사실을 새 입력 키워드 지원으로 확대하지 않는다. |
| LG1-150 | CPU 계수 생성·downscale | H | Q20의 네 꼭짓점 평균·기울기와 자식 중심 평가식; `swe/dg2/fields.cpp:55` `void dg2::downscale` | 전후처리의 계수 변환을 GPU 런타임 솔버 동등성의 조건으로 삼지 않는다. |
| LG1-151 | 미호출 Metal 보조 경로 | H | `metal/fv1/metal_fv1_simulate.mm:766` `void updateBoundaryFluxes() {`; 정의 외 호출이 없다. 실제 step은 `metal/fv1/metal_fv1_kernels.metal:488-489`, `:598-599`의 account_boundary를 쓴다. | 미호출 flux buffer·accumulate_outflow를 실제 Metal 질량식으로 인용하지 않는다. |
| LG1-152 | 저장·실행 기반 구조 | H | `cuda/cuda_util.cu:34` `checkCudaErrors(cudaMemcpy(dst, src, count, cudaMemcpyDefault));`; `metal/CMakeLists.txt:13`의 metallib 컴파일 | 메모리·장치 관리와 비동기 파일 기록은 수치식 비교에서 별도 처리한다. |
| LG1-153 | 공통 파일의 ACC 처리 | H | `cuda/cuda_boundary.cu:679-681`의 Q20; `cuda/cuda_rain.cu:91` `lis::cuda::DynamicRain::updateACC` | ACC 전용 계산은 선택한 SWE 경로의 비교 완료 조건에 포함하지 않는다. |
| LG1-155 | 성능·사례·외부 이론 | H | `package:README.md:41-60`의 시험·성능 주장; `metal/CMakeLists.txt:8-9`의 재현성 주석 | 정적 식 대조는 실행 성능·비트 재현성·수치 검증을 확인하지 않는다. |
| LG1-160 | 현재 노트의 대상 판·목차 | H | `note:README.md:11`의 `**v8.2**`; `VersionHistory.h:23` `#define LF_Release "8.3"`; `lisflood.cpp:783` `run_metal_fv1(*Fnameptr, &Fps, *Statesptr, *Parptr, *Solverptr, *BCptr,` | 원자료의 8.3 패치와 Metal FV1 진입점을 노트의 대상 식별에 반영한다. |

### 5.3 확인 범위와 종료 기록

§2.9는 대상 파일의 계산 루틴을 대조 행에 연결한다.
§3은 구현별 기능·옵션을 모은다.
§4는 현재 노트의 원문과 수정안을 제시한다.
§5.2는 모든 비일치 행에 하나의 분류를 부여한다.
보고서 작성 중 지정 파일만 수정했다.
모델을 빌드하거나 실행하지 않았다.
비트 일치·질량 오차 크기·파속·수렴성·성능을 실행 검증하지 않았다.
외부 논문의 계수 타당성은 이 코드 대조의 완료 조건에 넣지 않았다.

분류별 개수: C 31, E 32, F 10, H 11, X 0. 합계 84행(§5.2의 고유 행 ID 기준). 열지 못한 파일: 없음(§2.9의 대상 코드·헤더·CMake 114개 기준).
