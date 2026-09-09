---
title: "XBeach 승인 소스 보충 60건 — 입력·경계·형태·interface·출력 적용 한계"
topic: xbeach
canonical_source: self
layer: 2
depends_on: []
citation_status: verified
has_source_needed: false
verification_by: "Codex source cross-ref; Claude Sonnet adversarial review"
verification_date: 2026-09-09
verification_method: "Exact source SHA and physical-LF quote cross-reference; scoped adversarial review"
note_author: "Codex"
note_date: 2026-09-09
related:
  - models/XBeach/source-analysis/xbeach_params.md
  - models/XBeach/source-analysis/wave/xbeach_wave_boundary.md
  - models/XBeach/source-analysis/xbeach_morphology.md
  - models/XBeach/source-analysis/xbeach_infrastructure.md
  - models/XBeach/source-analysis/xbeach_output.md
---

# XBeach 승인 소스 보충 60건

> 60건 모두 원본 코드와 최종 crosswalk의 범위를 대조했다. Claude는 고위험 표본을 적대 검토했으며 60건 전량을 독립 재판정한 것은 아니다. `STANDS`는 인용된 조건에서 결함이 유지됨을, `NARROWED`는 최종 문장에 적은 범위에서만 유지됨을 뜻한다. 이 목록은 해당 checkout의 정적 소스 판정이며 실행 재현 결과를 뜻하지 않는다.

기존 메커니즘 노트의 설명을 반복하지 않고, 승인된 보충이 추가하는 실패 조건과 적용 한계를 기록한다. 정확한 인용문·바이트 해시·crosswalk 판정은 closure의 `source-canonical/evidence-ledger.json`, 60건 전량의 앵커 대응은 `mapping-ledger.json`에 있다.

## 입력·초기 상태·시간 제어

| ID | 판정 | 소스 판정과 적용 범위 | 근거 |
|---|---|---|---|
| <a id="xb-sup-filefunctions-f90-b3-d5e4c239"></a>`B3` `trunk/src/xbeachlibrary/filefunctions.F90` | `NARROWED` | 헤더만 있는 LOCLIST를 이 helper가 허용하지만 spectral_wave_init가 뒤에서 위치 1개 이상을 요구해 중단한다. 경계 파일 없이 계산이 진행되는 결함이 아니라 조기 검증 누락이다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/filefunctions.F90:197-200` |
| <a id="xb-sup-initialize-f90-b4-9803067b"></a>`B4` `trunk/src/xbeachlibrary/initialize.F90` | `STANDS` | nx가 너무 작거나 dsu/dnv가 0인 격자를 강제 차단하지 않은 채 경계 열을 복사하고 경사를 metric으로 나눈다. XBeach의 nx 하한은 권고 검사이고 Delft3D 격자 치수는 이를 우회한다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/initialize.F90:395-400` |
| <a id="xb-sup-initialize-f90-b8-9803067b"></a>`B8` `trunk/src/xbeachlibrary/initialize.F90` | `STANDS` | WBCTYPE_PARAMS와 TS_1/TS_2에서는 비엄격 입력 검사를 통과한 Trep=0이 2π/Trep 계산에 도달할 수 있다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/initialize.F90:619-623` |
| <a id="xb-sup-initialize-f90-b11-9803067b"></a>`B11` `trunk/src/xbeachlibrary/initialize.F90` | `STANDS` | hotstart_init_1이 읽은 uu/vv를 뒤의 flow_init가 무조건 0으로 덮고 hotstart_init_2도 다시 읽지 않으므로, 저장된 hotstart 유속은 복원되지 않는다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/initialize.F90:1042-1047` |
| <a id="xb-sup-params-f90-b0-73648b57"></a>`B0` `trunk/src/xbeachlibrary/params.F90` | `STANDS` | all_input은 hotstart 입력값을 읽기 전에 기본 sentinel 값으로 depfile 필요 여부를 판정한다. 따라서 정상적인 새 hotstart 요청도 불필요하게 depfile을 요구한다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90:160-163` |
| <a id="xb-sup-params-f90-b1-73648b57"></a>`B1` `trunk/src/xbeachlibrary/params.F90` | `NARROWED` | 중력·주기·활성 격자간격의 0 또는 음수 값은 권고 검사만 거쳐 위험한 나눗셈과 격자 계산에 도달할 수 있다. 다만 일부 음수 dx/dy는 가변격자 metric fallback 지시이므로 일괄 오류가 아니며, 비종료 각도 정규화 주장은 성립하지 않는다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90:263-266` |
| <a id="xb-sup-params-f90-b2-73648b57"></a>`B2` `trunk/src/xbeachlibrary/params.F90` | `STANDS` | 외부 Delft3D 헤더의 mmax/nmax는 읽기 성공과 Cartesian 표지만 검사한 뒤 nx/ny로 변환된다. 최소 치수 검사가 없어 작은 격자가 후속 할당·경계 인덱싱에 도달한다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90:232-237` |
| <a id="xb-sup-params-f90-b7-73648b57"></a>`B7` `trunk/src/xbeachlibrary/params.F90` | `STANDS` | tint 계열의 엄격 하한이 0이라 출력 간격 0이 허용된다. 해당 출력 종류의 자동 schedule을 실제로 켰을 때만 timestep_init의 나눗셈에 도달하며, 사용하지 않는 출력은 분모가 되지 않는다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90:1227-1231` |
| <a id="xb-sup-params-f90-b8-73648b57"></a>`B8` `trunk/src/xbeachlibrary/params.F90` | `STANDS` | posdwn은 허용된 작은 양수도 0.1 미만이면 -1로 바꾸고 그 이상 양수는 그대로 둔다. 이후 이산 부호 정규화가 없어 깊이 부호·크기 처리가 불연속이다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90:1536-1538` |
| <a id="xb-sup-readkey-f90-b3-1a95b6c3"></a>`B3` `trunk/src/xbeachlibrary/readkey.F90` | `STANDS` | vector reader는 vlength를 결과 길이와 대조하지 않고 prefix만 정의한다. ngd 호출은 엄격 제한되지만 비엄격 nrugdepth는 고정 결과 용량을 넘을 수 있어 실제 overflow 경로가 남는다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/readkey.F90:447-451` |
| <a id="xb-sup-readkey-f90-b6-1a95b6c3"></a>`B6` `trunk/src/xbeachlibrary/readkey.F90` | `STANDS` | parameter cache는 파일명 문자열이 바뀔 때만 갱신된다. 같은 경로의 파일 내용을 실행 중 바꾸고 다시 읽으면 이전 값과 used-key 상태를 계속 반환한다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/readkey.F90:603-607` |
| <a id="xb-sup-readkey-f90-b8-1a95b6c3"></a>`B8` `trunk/src/xbeachlibrary/readkey.F90` | `NARROWED` | 비-master rank의 parmapply 단독 반환에서는 optional parm_str가 정의되지 않는다. 정상 all_input 경로는 이후 parameter 구조 전체를 broadcast하므로 지속적인 MPI 파라미터 손상으로 확대되지는 않는 낮은 수준의 API 계약 결함이다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/readkey.F90:786-791` |
| <a id="xb-sup-readkey-f90-b13-1a95b6c3"></a>`B13` `trunk/src/xbeachlibrary/readkey.F90` | `STANDS` | strippedline은 입력 record의 7-bit printable ASCII 밖 바이트를 진단 없이 공백으로 바꾼다. 비ASCII 파일명과 문자열 파라미터가 cache에 들어가기 전에 변형된다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/readkey.F90:1141-1146` |
| <a id="xb-sup-spaceparams-f90-b7-e13f4e60"></a>`B7` `trunk/src/xbeachlibrary/spaceparams.F90` | `STANDS` | nx=1이면 alfaz 내부 계산이 비어 있고 두 경계 대입이 미정의 값을 서로 복사한다. nx 하한이 비엄격이고 외부 격자에도 강제 하한이 없어 입력 경로에서 배제되지 않는다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/spaceparams.F90:1404-1409` |
| <a id="xb-sup-timestep-f90-b4-24f60002"></a>`B4` `trunk/src/xbeachlibrary/timestep.F90` | `STANDS` | schedule에 같은 시각이 연속되면 counter는 한 번만 증가하고 다음 시각 탐색은 같은 값을 제외한다. 그 출력 종류는 뒤 시각을 놓치지만 모델 시간 루프 전체가 교착된다고 볼 근거는 없다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/timestep.F90:390-394` |
| <a id="xb-sup-timestep-f90-b12-24f60002"></a>`B12` `trunk/src/xbeachlibrary/timestep.F90` | `STANDS` | groundwater가 켜진 분기에서 kx와 조건부 ky를 직접 분모로 쓴다. 입력 하한이 권고 검사라 0·음수 permeability가 이 계산에 도달할 수 있다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/timestep.F90:606-606` |

기존 구조 설명: [xbeach_params.md](xbeach_params.md), [xbeach_initialize.md](xbeach_initialize.md), [xbeach_timestep_control.md](xbeach_timestep_control.md).

## 파·흐름 경계

| ID | 판정 | 소스 판정과 적용 범위 | 근거 |
|---|---|---|---|
| <a id="xb-sup-boundaryconditions-f90-b1-0cbaa20c"></a>`B1` `trunk/src/xbeachlibrary/boundaryconditions.F90` | `STANDS` | TS_1/TS_2 reader는 nt의 I/O 성공만 확인하고 배열 할당 뒤 sum(dataE)/nt를 계산한다. 문법적으로 유효한 nt=0은 차단되지 않는다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/boundaryconditions.F90:164-164` |
| <a id="xb-sup-boundaryconditions-f90-b3-0cbaa20c"></a>`B3` `trunk/src/xbeachlibrary/boundaryconditions.F90` | `NARROWED` | Surfbeat 경계에서는 마른 경계의 평균수심 ht가 보호 없이 분모가 되는 위험이 남는다. 비정수압 경로의 수심 나눗셈은 양의 수심 불변조건으로 일부 보호되고, 유한 양수심에서 cg²=g·h의 정확 공진은 성립하지 않는다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/boundaryconditions.F90:451-453` |
| <a id="xb-sup-boundaryconditions-f90-b4-0cbaa20c"></a>`B4` `trunk/src/xbeachlibrary/boundaryconditions.F90` | `STANDS` | 지원되는 reuse/list 경계 파일의 dtbcfile은 양수 검사 없이 record 번호와 보간 분모에 쓰인다. 내부 생성기의 양수 step은 외부 reuse 파일을 보호하지 않는다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/boundaryconditions.F90:594-597` |
| <a id="xb-sup-boundaryconditions-f90-b10-0cbaa20c"></a>`B10` `trunk/src/xbeachlibrary/boundaryconditions.F90` | `STANDS` | 비정수압 경계 파일에 Z가 없으면 zi에 절대 수면 zs(2,:)를 복사한 뒤 FRONT_NONH 적용에서 zs0를 다시 더한다. taper는 이 기준수위 중복을 제거하지 않는다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/boundaryconditions.F90:1310-1313` |
| <a id="xb-sup-boundaryconditions-f90-b12-0cbaa20c"></a>`B12` `trunk/src/xbeachlibrary/boundaryconditions.F90` | `NARROWED` | cats·Trep 권고 하한은 비엄격이고 table의 Trep도 별도 검사하지 않아 0이면 relaxation 분모가 된다. 기본 hybrid 설정이 아니라 잘못된 사용자·외부 forcing 값에서만 발생한다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/boundaryconditions.F90:1141-1146` |
| <a id="xb-sup-boundaryconditions-f90-b15-0cbaa20c"></a>`B15` `trunk/src/xbeachlibrary/boundaryconditions.F90` | `STANDS` | ny=2이면 transverse velocity의 전역 선택 구간이 비어 dnvsum=0이 될 수 있고, vdnvsum/dnvsum에 0/0이 남는다. MPI reduction은 소유권만 합치며 빈 선택을 보정하지 않는다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/boundaryconditions.F90:1177-1178` |
| <a id="xb-sup-boundaryconditions-f90-b18-0cbaa20c"></a>`B18` `trunk/src/xbeachlibrary/boundaryconditions.F90` | `STANDS` | back-boundary 두 corner의 수위를 계산하면서 front row의 dzs0dn·dnv·zb를 참조한다. 뒤의 lateral 보정 범위는 이 corner를 일반적으로 덮지 않는다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/boundaryconditions.F90:1462-1467` |
| <a id="xb-sup-boundaryconditions-f90-b22-0cbaa20c"></a>`B22` `trunk/src/xbeachlibrary/boundaryconditions.F90` | `STANDS` | MPI 수평 discharge segment의 두 끝점이 rank 밖에 있으면 그 rank를 가로질러도 indomain=false가 된다. 이후 endpoint clipping과 전역 면적 합산은 누락된 local momentum 적용을 복원하지 않는다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/boundaryconditions.F90:1670-1673` |
| <a id="xb-sup-wave-boundary-datastore-f90-b0-189a1372"></a>`B0` `trunk/src/xbeachlibrary/wave_boundary_datastore.f90` | `NARROWED` | randomseed는 scalar인데 consumer가 ALLOCATED/DEALLOCATE 대상으로 사용해 타입 계약이 맞지 않는다. 이 prototype 모듈은 확인한 build source list와 활성 call graph에 없으므로 배포 실행파일의 도달 가능한 결함이 아니라 잠재 통합 결함이다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_boundary_datastore.f90:24-26` |
| <a id="xb-sup-wave-boundary-main-f90-b6-5457f45f"></a>`B6` `trunk/src/xbeachlibrary/wave_boundary_main.f90` | `NARROWED` | 생성 배열 순서는 point,time,direction인데 consumer는 time 자리에 itheta를 고정하고 direction slice를 시간열로 넘긴다. 확인한 build와 활성 call graph에서 제외된 prototype의 잠재 통합 결함이다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_boundary_main.f90:258-262` |
| <a id="xb-sup-wave-boundary-main-f90-b7-5457f45f"></a>`B7` `trunk/src/xbeachlibrary/wave_boundary_main.f90` | `NARROWED` | nonhydrostatic 생성 분기는 hydrostatic 배열을 할당하지 않지만 BUILDXBEACH 보간부는 이를 무조건 참조한다. 확인한 build와 활성 call graph에서 제외된 prototype의 잠재 통합 결함이다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_boundary_main.f90:259-264` |
| <a id="xb-sup-wave-boundary-update-f90-b10-9c364a2c"></a>`B10` `trunk/src/xbeachlibrary/wave_boundary_update.f90` | `NARROWED` | BUILDXBEACH가 없으면 보간부가 pdflocal과 thetagen을 정의하지 않은 채 뒤에서 정규화·사용한다. 확인한 build와 활성 call graph에서 제외된 prototype의 잠재 통합 결함이다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_boundary_update.f90:1583-1588` |
| <a id="xb-sup-wave-boundary-update-f90-b16-9c364a2c"></a>`B16` `trunk/src/xbeachlibrary/wave_boundary_update.f90` | `NARROWED` | generate_ebcf의 BUILDXBEACH logging은 scope에 없는 s%ntheta·s%ny를 참조한다. 확인한 build와 활성 call graph에서 제외된 prototype의 잠재 build 결함이다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_boundary_update.f90:2186-2189` |
| <a id="xb-sup-wave-boundary-update-f90-b20-9c364a2c"></a>`B20` `trunk/src/xbeachlibrary/wave_boundary_update.f90` | `NARROWED` | generate_qbcf가 전달받거나 선언하지 않은 s%ny로 q를 할당한다. 확인한 build와 활성 call graph에서 제외된 prototype의 잠재 build 결함이다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_boundary_update.f90:2514-2516` |
| <a id="xb-sup-wave-directions-f90-b5-c8c7f311"></a>`B5` `trunk/src/xbeachlibrary/wave_directions.F90` | `NARROWED` | 구형 solver는 부분 j 범위에도 full-row mask를 써 배열 extent가 달라진다. 활성 replacement는 일관된 slice를 쓰고 구형 routine은 호출되지 않으므로 현재 실행 경로의 결함은 아니다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_directions.F90:360-360` |
| <a id="xb-sup-waveparams-f90-b11-f224c5c3"></a>`B11` `trunk/src/xbeachlibrary/waveparams.F90` | `NARROWED` | legacy makebcf의 일부 출력 모드에서는 Ampzeta 중간값이 loop 순서에 의존한다. WBCTYPE_PARAMS/JONS_TABLE은 최종 Amp를 써 우회하고, 이 legacy routine 자체도 저장소 내 호출자가 없어 도달 범위가 제한된다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/waveparams.F90:1438-1443` |

기존 구조 설명: [xbeach_wave_boundary.md](wave/xbeach_wave_boundary.md), [xbeach_flow_boundary_conditions.md](xbeach_flow_boundary_conditions.md), [xbeach_wave_boundary_generation.md](xbeach_wave_boundary_generation.md).

## 마찰·형태·비정수압 수치

| ID | 판정 | 소스 판정과 적용 범위 | 근거 |
|---|---|---|---|
| <a id="xb-sup-bedroughness-f90-b5-508ccef2"></a>`B5` `trunk/src/xbeachlibrary/bedroughness.F90` | `STANDS` | infiltration ventilation이 활성일 때 cfu=0이면 regularization 전에 cfu로 나누고 뒤에서도 1/cfu를 평가한다. wetu는 수심 mask라 zero friction을 배제하지 않는다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/bedroughness.F90:360-365` |
| <a id="xb-sup-bedroughness-f90-b6-508ccef2"></a>`B6` `trunk/src/xbeachlibrary/bedroughness.F90` | `STANDS` | infiltration=0이어도 비음수 분기가 blphi를 -1e-4로 바꿔 facbl을 정확히 1보다 크게 만든다. 흐름과 보통의 cfu가 있으면 작은 추가 전단이 남는다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/bedroughness.F90:365-368` |
| <a id="xb-sup-bedroughness-f90-b9-508ccef2"></a>`B9` `trunk/src/xbeachlibrary/bedroughness.F90` | `STANDS` | velocity=0에서 SIGN이 양의 부호를 선택하므로 kbl이 양수인 젖은 face에는 고정 방향의 turbulent bed shear가 남을 수 있다. zero-velocity guard가 없다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/bedroughness.F90:701-703` |
| <a id="xb-sup-morphevolution-f90-b6-765f4740"></a>`B6` `trunk/src/xbeachlibrary/morphevolution.F90` | `STANDS` | pbbedu의 마지막 x face와 pbbedv의 마지막 y face를 채우지 않고 전체 배열 곱에 사용한다. 경계 transport가 0이어도 미정의 multiplier를 읽는 동작은 정의되지 않는다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/morphevolution.F90:485-490` |
| <a id="xb-sup-morphevolution-f90-b15-765f4740"></a>`B15` `trunk/src/xbeachlibrary/morphevolution.F90` | `NARROWED` | suspended와 bed load의 dilatancy 보정식은 서로 다른 비선형 factor를 쓴다. 차이는 srfRhee가 0이 아니고 BDSLPEFFINI_TOTAL 밖인 경우에만 남으며, TOTAL 분기는 Ucrb를 Ucrs로 복사한다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/morphevolution.F90:1594-1599` |
| <a id="xb-sup-nonh-f90-b8-18f471b3"></a>`B8` `trunk/src/xbeachlibrary/nonh.F90` | `STANDS` | y방향 vertical-viscosity flux가 V face에서 hv 대신 hu를 곱한다. wetv는 젖음만 보장하고 방향별 upwind 수심의 동일성을 보장하지 않는다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/nonh.F90:1172-1177` |

기존 구조 설명: [xbeach_bed_friction.md](xbeach_bed_friction.md), [xbeach_morphology.md](xbeach_morphology.md), [xbeach_nonh.md](xbeach_nonh.md).

## Python/C/BMI·MPI interface

| ID | 판정 | 소스 판정과 적용 범위 | 근거 |
|---|---|---|---|
| <a id="xb-sup-libxbeach-py-b10-55640d60"></a>`B10` `trunk/src/pybeach/xbeach/libxbeach.py` | `STANDS` | set_array의 실제 ndarray shape 검사는 assert뿐이라 Python -O에서 사라진다. 뒤의 pointer cast는 원래 배열 extent를 다시 검사하지 않는다. | `models/XBeach/raw/source_code/trunk/src/pybeach/xbeach/libxbeach.py:251-252` |
| <a id="xb-sup-libxbeach-py-b12-55640d60"></a>`B12` `trunk/src/pybeach/xbeach/libxbeach.py` | `STANDS` | set_array는 알 수 없는 native type code를 거부하는 else가 없어 dtype·typename 미정의 상태로 함수명을 만든다. native type query 실패와 Python 3 byte code 불일치도 이 경로를 배제하지 않는다. | `models/XBeach/raw/source_code/trunk/src/pybeach/xbeach/libxbeach.py:259-264` |
| <a id="xb-sup-introspection-f90-b3-870a8c32"></a>`B3` `trunk/src/xbeachlibrary/introspection.F90` | `STANDS` | C entry point의 length개 name buffer를 MAXSTRINGLEN까지 NUL 탐색하는 helper에 넘긴다. Python buffer는 보통 여분 NUL을 갖지만, 정확히 length byte이고 NUL이 없는 직접 C 호출은 할당 범위를 넘겨 읽을 수 있다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/introspection.F90:137-142` |
| <a id="xb-sup-introspection-f90-b4-870a8c32"></a>`B4` `trunk/src/xbeachlibrary/introspection.F90` | `STANDS` | numeric getter는 이름 존재만 확인하고 parameter 실제 type을 검사하지 않는다. integer 이름을 double getter로 요청하거나 그 반대이면 연결되지 않은 component를 참조한다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/introspection.F90:218-223` |
| <a id="xb-sup-iso-c-utils-f90-b2-b63c219f"></a>`B2` `trunk/src/xbeachlibrary/iso_c_utils.f90` | `NARROWED` | strcmp helper는 trim과 Fortran blank-padding 때문에 NUL 앞 trailing space의 C strcmp 의미를 보존하지 않는다. 저장소 내 호출이 없어 현재 BMI 실행 실패가 아니라 잠재 호환성 결함이다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/iso_c_utils.f90:30-34` |
| <a id="xb-sup-libxbeach-f90-b5-1656cceb"></a>`B5` `trunk/src/xbeachlibrary/libxbeach.F90` | `STANDS` | MPI library run이 0~1 step에서 끝나면 t01이 아직 정의되지 않았는데 final이 timing 출력에 넘긴다. writelog_finalize에도 초기화 여부 guard가 없다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/libxbeach.F90:269-274` |
| <a id="xb-sup-xmpi-f90-b2-68c0cec0"></a>`B2` `trunk/src/xbeachlibrary/xmpi.F90` | `STANDS` | processor-grid score와 1,000,000,000 sentinel이 default integer라 큰 domain에서 overflow하거나 모든 후보가 sentinel 이상이면 factorization을 선택하지 못할 수 있다. 뒤의 domain-size 검사는 이를 복구하지 못한다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/xmpi.F90:350-355` |
| <a id="xb-sup-xmpi-f90-b3-68c0cec0"></a>`B3` `trunk/src/xbeachlibrary/xmpi.F90` | `STANDS` | manual mmpi/nmpi 하한은 비엄격이라 음수 두 개가 warning만 남기고 양의 process 수 곱 검사를 통과할 수 있다. 뒤 검사도 이를 배제하지 않아 잘못된 분할 geometry와 divisor로 이어진다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/xmpi.F90:360-365` |

기존 구조 설명: [xbeach_infrastructure.md](xbeach_infrastructure.md).

## 출력·통계

| ID | 판정 | 소스 판정과 적용 범위 | 근거 |
|---|---|---|---|
| <a id="xb-sup-ncoutput-f90-b1-04a33fdb"></a>`B1` `trunk/src/xbeachlibrary/ncoutput.F90` | `STANDS` | NetCDF-only 초기화는 saved drifter counter itd를 설정하지 않지만 출력 시 이를 증가시켜 record index로 쓴다. fortoutput_init만 이 counter를 초기화한다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/ncoutput.F90:1554-1559` |
| <a id="xb-sup-ncoutput-f90-b5-04a33fdb"></a>`B5` `trunk/src/xbeachlibrary/ncoutput.F90` | `STANDS` | point variable의 앞 두 dimension이 x/y가 아니어도 알려진 dimension이면 log만 남기고 point-by-time 변수로 정의·공간 index로 sampling한다. 비공간 rank-2 변수에서 shape 계약이 깨질 수 있다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/ncoutput.F90:491-496` |
| <a id="xb-sup-ncoutput-f90-b12-04a33fdb"></a>`B12` `trunk/src/xbeachlibrary/ncoutput.F90` | `NARROWED` | global·point·mean NetCDF 시간은 morfacopt를 보지 않고 morfac을 곱한다. 불일치는 morfacopt=0이면서 morfac>1인 허용 조합에서만 생기며 morfacopt=1에서는 의도된 변환이다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/ncoutput.F90:1136-1140` |
| <a id="xb-sup-ncoutput-f90-b18-04a33fdb"></a>`B18` `trunk/src/xbeachlibrary/ncoutput.F90` | `STANDS` | varianceupdate는 thetamean을 직접 ATAN2 각도로 저장하지만 NetCDF와 Fortran 출력은 이를 과거 packed 값처럼 다시 decode한다. 중간 collect 단계에서 repack하지 않아 각도가 손상된다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/ncoutput.F90:1500-1505` |
| <a id="xb-sup-ncoutput-f90-b19-04a33fdb"></a>`B19` `trunk/src/xbeachlibrary/ncoutput.F90` | `NARROWED` | 다음 mean interval 갱신이 Fortran-compatible 분기 안에만 있어 NetCDF-only의 비균일 사용자 schedule은 이전 tintm으로 평균 가중한다. 자동 생성된 고정간격 schedule에는 영향이 없다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/ncoutput.F90:1546-1548` |
| <a id="xb-sup-ncoutput-f90-b20-04a33fdb"></a>`B20` `trunk/src/xbeachlibrary/ncoutput.F90` | `STANDS` | morfacopt=1에서 drifter release/end time은 내부 hydrodynamic time으로 환산되지만 drifter NetCDF time은 raw par%t를 쓴다. morfac>1이면 같은 파일의 다른 시간축과 단위가 달라진다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/ncoutput.F90:1554-1559` |
| <a id="xb-sup-ncoutput-f90-b22-04a33fdb"></a>`B22` `trunk/src/xbeachlibrary/ncoutput.F90` | `STANDS` | integer rank-2 mean 변수도 허용되지만 Fortran mean-file record length는 항상 real pointer t%r2에서 구한다. wetz 같은 integer mean 출력에서 잘못된 component를 참조한다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/ncoutput.F90:1815-1820` |
| <a id="xb-sup-ncoutput-f90-b23-04a33fdb"></a>`B23` `trunk/src/xbeachlibrary/ncoutput.F90` | `STANDS` | global Fortran direct-access 파일을 STATUS='UNKNOWN'으로 열어 이전 run보다 적게 쓰면 높은 record가 물리적으로 남는다. dims.dat를 따르는 reader는 새 record 수를 알 수 있지만 파일 자체는 truncate되지 않는다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/ncoutput.F90:1852-1857` |
| <a id="xb-sup-postprocess-f90-b8-3b984856"></a>`B8` `trunk/src/xbeachlibrary/postprocess.F90` | `NARROWED` | 이 helper는 전역 wetz 최소 위치 하나에서 만든 값을 모든 runup gauge에 복사해 논리가 틀리다. 활성 runup 출력은 gauge별 row를 따로 탐색하므로 현재 출력 경로가 아니라 미사용 helper의 잠재 결함이다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/postprocess.F90:505-508` |
| <a id="xb-sup-varianceupdate-f90-b4-04276e42"></a>`B4` `trunk/src/xbeachlibrary/varianceupdate.F90` | `STANDS` | 원형평균의 near-zero guard는 SIGN의 magnitude 인자를 잘못 써 epsilon floor가 아니라 epsilon·abs(cos_sum)을 만든다. 보통 t=0 출력은 gate되지만 반복 zero-dt API 출력 등에서 ATAN2(0,0)를 확실히 막지 못한다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/varianceupdate.F90:346-351` |

기존 구조 설명: [xbeach_output.md](xbeach_output.md).

## 생성 schema·template

| ID | 판정 | 소스 판정과 적용 범위 | 근거 |
|---|---|---|---|
| <a id="xb-sup-generate-py-b3-a9e13e75"></a>`B3` `trunk/scripts/generate.py` | `STANDS` | variable declaration parser는 JSON 필수 key·이름 중복·declaration rank와 shape rank 일치를 검사하지 않는다. 현재 327개 변수는 조건을 만족하지만, 향후 불일치 입력은 선언과 할당 rank가 다른 Fortran을 생성할 수 있다. | `models/XBeach/raw/source_code/trunk/scripts/generate.py:164-166` |
| <a id="xb-sup-generate-py-b4-a9e13e75"></a>`B4` `trunk/scripts/generate.py` | `NARROWED` | variable JSON은 파싱한 name·rank 같은 구조 필드를 검증 없이 덮을 수 있다. parameter 정규식에서는 앞의 greedy comment가 JSON을 소비해 같은 override 경로가 현재 도달되지 않으므로 변수 schema 결함으로 한정된다. | `models/XBeach/raw/source_code/trunk/scripts/generate.py:164-166` |
| <a id="xb-sup-indextos-mako-b2-cd839a46"></a>`B2` `trunk/src/xbeachlibrary/templates/indextos.mako` | `STANDS` | metadata를 single-quoted Fortran literal에 escape 없이 넣는다. 현재 description에는 apostrophe가 없지만 새 설명에 water's 같은 정상 문자열이 들어오면 생성 소스가 깨진다. | `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/templates/indextos.mako:39-43` |

기존 구조 설명: [xbeach_params.md](xbeach_params.md), [xbeach_infrastructure.md](xbeach_infrastructure.md).

## 테스트 harness

| ID | 판정 | 소스 판정과 적용 범위 | 근거 |
|---|---|---|---|
| <a id="xb-sup-testgenmodule-f90-b8-df3206df"></a>`B8` `trunk/test/testgenmodule.F90` | `NARROWED` | master가 초기화 전 a·ia를 aa·iaa로 복사해 미정의 read가 발생한다. 뒤 scattertest가 영역을 덮지만, harness는 현재 xmpi 호출 signature와 맞지 않고 build manifest에도 없어 그대로 실행되는 테스트 결함은 아니다. | `models/XBeach/raw/source_code/trunk/test/testgenmodule.F90:909-913` |

기존 구조 설명: [xbeach_infrastructure.md](xbeach_infrastructure.md).

## 판정 경계

- 활성 build·call graph에서 제외된 prototype, 미사용 helper, 현재 build manifest 밖 test는 배포 실행파일의 기본 경로 문제로 표현하지 않았다.
- 잘못된 입력·외부 forcing·특정 output mode에서만 생기는 항목은 그 조건을 각 문장에 남겼다.
- `STANDS` 40건과 `NARROWED` 20건의 수는 승인 보충 처분 수이며 고유 runtime 결함 수나 실행 실패 수가 아니다.
- 실행·compiler 재현을 수행하지 않았으며, 정적 소스와 최종 crosswalk 밖의 동작은 확인된 사실로 추가하지 않았다.
