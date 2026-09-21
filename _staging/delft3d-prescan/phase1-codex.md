# Delft3D Phase 1 의미 검토

`phase1-task.md` 계약에 따라 `delft3d_dflowfm_data_io.md`의 입력 45건만 판정했다. 위키 문장 수정안이나 좌표 일괄 치환안은 포함하지 않는다.

**요약**

| 판정 | 건수 |
|---|---:|
| UPDATE_REQUIRED | 2 |
| REVIEW_ONLY | 19 |
| NO_ACTION | 22 |
| UNRESOLVED | 2 |
| 합계 | 45 |

- `D1-29` — `BEHAVIOR_CHANGE`: `unc_create`가 `overwrite_cmode=.true.`일 때 전역 cmode 합성을 생략한다. 기존 3인자 호출의 합성 동작은 유지된다.
- `D1-40` — `INTERFACE_CHANGE`: ext 포맷 버전의 활성 상수가 `2.02 → 3.00`으로 변경되었다. 구버전 입력 호환성까지 판정하지 않았다.
- 39개의 `REANCHOR` 행 모두 직접 대응 위치를 찾았다. 근거 위치를 찾은 것과 위키 주장의 의미를 입증한 것은 별개다. `D1-25`는 위치를 찾았지만 전역 보장이 미해결이며, `D1-45`도 같은 미해결 주장을 포함한다.

판정 단위는 **각 입력 행의 ref가 뒷받침하는 주장**이다. 동일한 노트 줄에 여러 인용이 있으면 다른 인용의 변경을 자동 전파하지 않았다. 예를 들어 `D1-28`은 함수 진입점/래퍼 역할이고 `D1-29`는 cmode 합성 대입문이다. CSV의 `wiki_claim`은 노트 원문 전체 줄을 유지했으며 입력에서 300자로 잘린 `D1-30`, `D1-31`, `D1-37`은 같은 노트 줄에서 복원했다. 제목만 들어 있는 `D1-13`과 `D1-18`은 각각 바로 아래 해당 설명까지 읽어 의미를 판정했다.

`semantic_meaning_changed`는 주장에 대한 `true` / `false` / `unknown`이다. 소스 내부 변경이 있다는 뜻과 구별한다. `NO_ACTION`은 의미 수정이 불필요하다는 뜻이며 옛 줄 번호가 새 버전에서도 유효하다는 뜻은 아니다. `REVIEW_ONLY`는 주장 자체는 유지되지만 모듈 이동·생성 코드·인접 동작 변경 등의 검토 근거가 있는 경우다. `reason_type`은 UPDATE_REQUIRED에만 지정했다. HIGH는 직접 소스 근거로 이 판정을 지지하는 경우, MEDIUM은 일부 근거를 찾았지만 주장 전체가 입증되지 않은 경우다.

**UNRESOLVED 목록**

| ID | 노트 줄 | 확인된 근거 | 남은 불확실성 |
|---|---:|---|---|
| D1-25 | 164 | `dflowfm_data/unstruc_netcdf_data.f90:18-24`; `dflowfm_io/unstruc_netcdf.f90:895-905,916-942,987-992` | 설계 주석은 모든 NetCDF를 래퍼로 열어야 한다는 **should** 규약이다. 래퍼의 등록/종료 구현은 확인되지만 모든 실제 호출 경로가 이를 따른다는 전역 보장은 이 근거로 확인되지 않는다. |
| D1-45 | 240 | `dflowfm_io/unstruc_netcdf.f90:44,895-992`; 위 데이터 모듈 `18-24` | 모든 파일을 추적 리스트로 관리한다는 동일한 전역 단언이 미해결이다. 추적 기능 제거 또는 새 버전의 추적 누락을 발견했다는 뜻이 아니다. |

대상 6파일에서는 주석을 제외한 `nf90_open`/`nf90_create` 호출이 구판 `unstruc_netcdf.f90:2474,2500`, 신판 `:900,934`의 두 래퍼 안에만 있었다. 이것을 전체 엔진의 모든 I/O 경로에 대한 증명으로 확대하지 않았다. 두 미해결 행을 해결하려고 45건 밖의 I/O 전수 감사로 확장하지 않고 반환한다.

**재앵커 근거**

아래 경로는 모두 `src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/` 기준이다. `cmake/`와 `CMakeLists.txt`만 kernel 디렉터리 기준이다. 옛 좌표는 `513eccd`, 새 좌표는 `231bbf2` 기준이다. CSV에는 저장소 상대 전체 경로, 원문 발췌, 추가 문맥과 행별 판정 이유를 담았다.

| ID | 원 인용 | 새 주 앵커 | 판정 | 근거 요지 |
|---|---|---|---|---|
| D1-1 | `m_flow.f90:160-161` | `dflowfm_data/m_flow.f90:165-166` | NO_ACTION | s0/s1 수위·시점·단위 유지; dimension 표기만 변경 |
| D1-2 | `m_flow.f90:171` | `dflowfm_data/m_flow.f90:176` | NO_ACTION | hs=s1-bl 역할 주석 유지 |
| D1-3 | `m_flow.f90:166-167` | `dflowfm_data/m_flow.f90:171-172` | NO_ACTION | vol0/vol1 시작/끝 총부피 유지 |
| D1-4 | `m_flow.f90:164-165` | `dflowfm_data/m_flow.f90:169-170` | NO_ACTION | a0/a1 저류면적 유지 |
| D1-5 | `m_flow.f90:192-194` | `dflowfm_data/m_flow.f90:197-199` | NO_ACTION | ucx/ucy/ucz 성분 유지 |
| D1-6 | `m_flow.f90:199` | `dflowfm_data/m_flow.f90:204` | NO_ACTION | ucmag 속도 크기 유지 |
| D1-7 | `m_flow.f90:295-296` | `dflowfm_data/m_flow.f90:300-301` | NO_ACTION | u0/u1 시작/끝 유속 유지 |
| D1-8 | `m_flow.f90:298` | `dflowfm_data/m_flow.f90:303` | NO_ACTION | 활성 q1 선언과 q0 재사용 설계 주석 유지 |
| D1-9 | `m_flow.f90:304` | `dflowfm_data/m_flow.f90:309` | NO_ACTION | au의 u점 흐름면적 유지 |
| D1-10 | `m_flow.f90:300` | `dflowfm_data/m_flow.f90:305` | NO_ACTION | 활성 qa 선언에 같은 advection 식 주석 |
| D1-11 | `m_flow.f90:269-270` | `dflowfm_data/m_flow.f90:274-275` | NO_ACTION | salinity(ppt), [1e-3] 유지 |
| D1-12 | `m_flow.f90:275-276` | `dflowfm_data/m_flow.f90:280-281` | NO_ACTION | temperature(degC) 유지 |
| D1-13 | `m_flow.f90:49-156` | `dflowfm_data/m_flow.f90:49-161` | REVIEW_ONLY | 문서의 층 구조는 유지; 미기술 stretching 설정 변경 |
| D1-14 | `m_flow.f90:128-129` | `dflowfm_data/m_flow.f90:133-134` | NO_ACTION | kbot/ktop 압축 셀 인덱스 유지 |
| D1-15 | `m_flow.f90:132-133` | `dflowfm_data/m_flow.f90:137-138` | NO_ACTION | Lbot/Ltop 압축 엣지 인덱스 유지 |
| D1-16 | `m_flow.f90:106` | `dflowfm_data/m_flow.f90:111` | NO_ACTION | 활성 zws 선언 및 보조 도해 유지 |
| D1-17 | `m_flowgeom.f90:134` | `dflowfm_data/m_flowgeom.f90:136` | NO_ACTION | kcu 코드값 유지; LINK_* 사용 권고만 추가 |
| D1-18 | `m_transport.f90:33-43` | `dflowfm_data/m_transport.f90:30-40` | NO_ACTION | 명시적으로 인용한 헤더 주석 유지; 대소문자만 변경 |
| D1-19 | `m_transport.f90:40,55-56` | `dflowfm_data/m_transport.f90:37;55-56` | NO_ACTION | 헤더 주석 + 활성 itra1/itran 선언 유지 |
| D1-20 | `m_transport.f90:48` | `dflowfm_data/m_transport.f90:47` | NO_ACTION | Fortran 대소문자만 변경 |
| D1-21 | `m_transport.f90:52-53` | `dflowfm_data/m_transport.f90:52-53` | NO_ACTION | ised1/isedn 동일; 직전 ioxy 추가 |
| D1-22 | `m_transport.f90:62` | `dflowfm_data/m_transport.f90:62` | NO_ACTION | 2차원 constituents 선언 동일 |
| D1-23 | `unstruc_netcdf.f90:85-86` | `dflowfm_data/unstruc_netcdf_data.f90:26-27` | REVIEW_ONLY | 상수값 동일, 데이터 모듈로 이동 |
| D1-24 | `unstruc_netcdf.f90:5285-5312` | `dflowfm_io/unstruc_netcdf.f90:3727-3759` | REVIEW_ONLY | iconv 분기 유지; UGRID 빈 격자 return 추가 |
| D1-25 | `unstruc_netcdf.f90:71-77` | `dflowfm_data/unstruc_netcdf_data.f90:18-24` | UNRESOLVED | 선언/래퍼 확인; 모든 NetCDF 경로 추적은 입증 안 됨 |
| D1-26 | `unstruc_netcdf.f90:74` | `dflowfm_data/unstruc_netcdf_data.f90:21` | REVIEW_ONLY | maxopenfiles=50 동일, 모듈 이동 |
| D1-27 | `unstruc_netcdf.f90:75-77` | `dflowfm_data/unstruc_netcdf_data.f90:22-24` | REVIEW_ONLY | 추적 배열·카운터 동일, 모듈 이동 |
| D1-28 | `unstruc_netcdf.f90:2490` | `dflowfm_io/unstruc_netcdf.f90:916-942` | REVIEW_ONLY | 래퍼 역할 유지; optional 인자 추가는 검토 사항 |
| D1-29 | `unstruc_netcdf.f90:2498` | `dflowfm_io/unstruc_netcdf.f90:924-934` | UPDATE_REQUIRED | overwrite_cmode=true이면 전역 cmode 합성 생략 |
| D1-30 | `unstruc_netcdf.f90:104-125` | `dflowfm_data/unstruc_netcdf_data.f90:45-66` | REVIEW_ONLY | 19개 금지 속성 동일; 실제 복사 호출 확인 |
| D1-31 | `unstruc_netcdf.f90:127-133` | `dflowfm_data/unstruc_netcdf_data.f90:68-74` | REVIEW_ONLY | 3개 환경 속성과 DFM_META_ 처리 유지 |
| D1-32 | `unstruc_netcdf.f90:139-185` | `dflowfm_data/unstruc_netcdf_data.f90:80-126` | REVIEW_ONLY | 타입 필드 동일; TODO 주석만 추가 |
| D1-33 | `unstruc_netcdf.f90:181` | `dflowfm_data/unstruc_netcdf_data.f90:122` | REVIEW_ONLY | idx_curtime 의미·초기값 동일 |
| D1-34 | `unstruc_netcdf.f90:190` | `dflowfm_data/unstruc_netcdf_data.f90:128-136` | REVIEW_ONLY | 활성 ncid/id_tsp 구성 유지; 모듈 이동 |
| D1-35 | `unstruc_netcdf.f90:97,232-243` | `dflowfm_data/unstruc_netcdf_data.f90:38;173-184` | REVIEW_ONLY | MAX_ID_VAR=4와 활성 변수 ID 배열 유지 |
| D1-36 | `unstruc_netcdf.f90:1380,1411,1349,1711` | `python/generate_unc_put_var_map.py:18-24;31-46;68-85;103-121;418-451` | REVIEW_ONLY | 생성기로 이동; 네 함수 이름과 위치별 put 유지 |
| D1-37 | `unc_write_his.F90:49-64` | `dflowfm_io/unc_write_his.F90:49-66` | REVIEW_ONLY | 기존 구조물 ID 유지; 신규 ID 및 파일 길이 변화 검토 |
| D1-38 | `unstruc_model.f90:60-61` | `dflowfm_data/m_unstruc_model_data.f90:24-25` | REVIEW_ONLY | 활성 MDU 버전 1.09 유지, 모듈 이동 |
| D1-39 | `unstruc_model.f90:63-73` | `dflowfm_data/m_unstruc_model_data.f90:27-37` | REVIEW_ONLY | MDU history 주석 자체가 동일하게 이동 |
| D1-40 | `unstruc_model.f90:76-77` | `dflowfm_data/m_unstruc_model_data.f90:40-41` | UPDATE_REQUIRED | 현재 ext 상수는 3/0; history 2.02에 정박 금지 |
| D1-41 | `unstruc_model.f90:101` | `dflowfm_data/m_unstruc_model_data.f90:65` | REVIEW_ONLY | md_ptr 선언 이동; 활성 tree_create/prop_inifile 확인 |
| D1-42 | `unstruc_model.f90:103` | `dflowfm_data/m_unstruc_model_data.f90:67` | REVIEW_ONLY | md_ident/runid 선언 그대로 이동 |
| D1-43 | `unstruc_model.f90:113-122` | `dflowfm_data/m_unstruc_model_data.f90:77-86` | REVIEW_ONLY | 파일명 변수군 그대로 이동 |
| D1-44 | `m_flow.f90:128-133` | `dflowfm_data/m_flow.f90:133-138` | NO_ACTION | 모듈 전역 층 압축 인덱스 유지 |
| D1-45 | `unstruc_netcdf.f90:44,2469-2558` | `dflowfm_io/unstruc_netcdf.f90:44;895-992` | UNRESOLVED | 추적 래퍼 유지; 모든 파일 추적 보장은 미확인 |

**주석·모듈 분리·생성 코드의 처리**

- 배열 후보는 이름의 문자열 일치만 보지 않고 주석 처리되지 않은 선언의 타입, rank, allocatable/target 속성과 역할 주석을 대조했다. `D1-18`은 원래 헤더 주석 자체, `D1-39`는 history 주석 자체를 인용하므로 그 주석을 문서 근거로 사용했다. 이것을 현재 실행 동작의 근거로 바꾸지 않았다.
- NetCDF 데이터는 `dflowfm_data/unstruc_netcdf_data.f90`의 `m_unstruc_netcdf_data`로 이동했고, 원 모듈의 `unstruc_netcdf.f90:64`가 이를 사용한다. MDU 데이터는 `m_unstruc_model_data.f90`로 이동했고 `unstruc_model.f90:44`가 이를 사용한다. 삭제 hunk만으로 심볼 소멸을 판정하지 않았다.
- `D1-40`의 새 파일 `m_unstruc_model_data.f90:44`에 남은 `2.02`는 이력 주석이다. 현재 값은 활성 parameter 선언 `:40-41`의 `3/0`이다.
- `D1-29`는 새 코드 `unstruc_netcdf.f90:924-932`의 조건 전체를 읽었다. 남아 있는 `ior` 대입 두 줄만 골라 구판과 같다고 판정하지 않았다.
- `D1-36`은 `python/generate_unc_put_var_map.py:18-24,31-46,418-451`에서 네 함수 이름·타입·함수 본문 생성 관계를 확인했다. 메모리에서 생성한 네 본문 모두 활성 `select case (iloc)`와 `nf90_put_var` 호출을 가진다. CMake `cmake/unc_put_var_map.cmake:6-19`, `CMakeLists.txt:87-88,121-123`이 생성 및 라이브러리 편입을 연결하고 `unstruc_netcdf.f90:66`이 생성 모듈을 사용한다. 빌드 산출물의 줄 번호를 추측하지 않았으며 생성 파일을 소스 트리에 쓰지 않았다.
- `D1-36`의 상세 signature와 구현은 완전히 같지 않다. 생성기 `:36,43-45`는 `iloc_in`/`values` 및 타입별 default_value를 사용한다. `:68-84`에는 remapping/표면 출력 분기가 있다. 위키가 주장하는 네 helper의 위치코드별 put 역할은 유지되어 REVIEW_ONLY로 반환한다.
- `D1-32`의 time 차원은 신판 `unstruc_netcdf.f90:3940-3944`에서 옵션에 따라 고정 길이 또는 unlimited다. 구판 `unstruc_netcdf.f90:5484-5488`에도 같은 고정 길이/unlimited 실행 분기가 있었다. 선언 주석의 유일한 unlimited 차원이라는 설명을 항상 unlimited라는 실행 보장으로 확대하지 않았다.
- 동일 원문 줄에 있는 파일 길이는 `unc_write_his.F90`가 1,741→1,790, `unstruc_netcdf.f90`가 18,974→16,909로 달라졌다. 이 수치 차이는 기록하되 구조물 ID 보유/파일 추적 동작의 변화로 대신 판정하지 않았다.

**검증 기록과 범위**

- 구 snapshot HEAD: `513eccdbe249919b3e5e62063dc91eb9fdf2347f`. 신 snapshot HEAD: `231bbf266cbb2d6de83a0b63ec8fdbf151a72382`.
- 입력 CSV SHA-256: `884cc810ae1098a1604631a156ffbff9c6e0b74764de49e262291626041dc5b5`.
- 검토 노트 SHA-256: `dda6cd87e9cf58739e3fdf3795a4230ce635ec3866e570c874446c2ab5fa3a81`.
- 구판 6파일과 신판 11파일(원 6파일 + 직접 이동된 선언 2파일 + 해당 함수 생성기/빌드 연결 3파일)의 읽은 내용이 각 고정 커밋 blob과 바이트 단위로 일치함을 확인했다. 의존 라이브러리 내부는 조사하지 않았다.
- 입력 45행과 산출 45행의 ID·순서·note_line, 필수 11열, 판정 합계, UPDATE_REQUIRED reason_type 및 모든 인용 범위의 실제 파일 경계를 검사했다. 제공 hunk 발췌도 두 snapshot 원문과 일치했다. 최종 CSV의 근거 좌표 147범위와 정확한 소스 발췌 1,367줄을 원문과 대조했다.
- 선언·정적 호출 흐름의 의미 검토다. 모델 실행/컴파일 검증을 수행했다는 뜻은 아니다. `models/`와 snapshot은 읽기만 했고 위키·권한·Git 설정을 변경하지 않았다.
- 완료 조건: 45건 모두 판정 또는 근거 한계를 명시한 UNRESOLVED로 반환. 추가 후보를 만들지 않았다.
