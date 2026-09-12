---
title: "XBeach 지형·지하수·Q3D 연결 계약과 적용 한계"
canonical_source: self
citation_status: draft-unsourced
note_author: "Codex"
note_date: 2026-09-12
verification_method: "동결 로컬 소스 직접 추적 및 최소 Fortran 대입 재현; 새 연결 주장 사람 검토 대기"
---

이 노트는 AI가 작성한 연결 검토본이다. 출처를 붙였지만 새 주장에 대한 사람 승인은 아직 받지 않았다. 원본 솔버를 수정하거나 다른 XBeach 판본에 일반화하지 않는다. 아래 행 번호는 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/` 기준 물리 LF 행이다. 소스 SHA와 정확 인용은 [재판정 원장](../../../_staging/total-read/model-audit/XBeach/connectivity/physics/resolution-20260912/adjudication.json)에 고정했다.

## 스텝 순서와 상태 전달

`executestep`은 wet mask → 시간 선택 → 경계 → 파랑 → 식생 → 지하수 → 유동 → 표사 → 지형 순서로 실행한다. 각 옵션은 별도 guard를 가지며, `bed_update` 호출은 `morphology=1`이면서 `setbathy!=1`일 때다. 내부 지형 갱신은 `morstart <= t < morstop`과 `morfac > 0.999`를 추가로 요구한다. 따라서 아래 결과는 해당 분기가 실행되는 경우에 한정한다. (`libxbeach.F90:280-312`; `morphevolution.F90:632-640`)

## 다분급 입경: 셀별 초기화 뒤 로컬 배열 전체 덮어쓰기

초기화에서는 `D50top(i,j)`·`D90top(i,j)`를 해당 셀 최상층 분급비의 가중합으로 만든다. 그러나 `bed_update`의 `ngd>1` 분기는 대입 왼쪽에 `(i,j)`가 없다. 오른쪽 `sum(...)`은 스칼라이므로 매 반복마다 로컬 배열 전체가 같은 값으로 바뀐다. 반복이 비어 있지 않으면 마지막 로컬 셀 `(nx,max(ny,1))`의 값이 로컬 halo를 포함한 배열 전체에 남는다. MPI rank 사이의 값이 동일하다는 뜻은 아니다. (`initialize.F90:1277-1283,1389-1398`; `morphevolution.F90:632-640,1170-1182`)

이 값의 소비도 확인된다. 다분급 White-Colebrook 입경 마찰은 `D90top` 인접값으로 조도를 갱신한다. `gwnonh=1`의 비연결 셀 침투는 `D50top(i,j)`를 넘기며, 국소 침투 함수의 난류 분기에서 Reynolds 수에 사용한다. 따라서 모든 마찰식이나 층류 침투가 같은 영향을 받는다고 말할 수 없다. 공간적으로 동일한 분급비는 이 덮어쓰기를 수치상 드러내지 않을 수 있다. (`bedroughness.F90:220-249`; `groundwater.F90:318-319,605-624,1574-1587`)

다른 소비 경로도 있다. `gwnonh=0`의 정수압 지하수 경로는 `gw_calculate_hydrostatic_w`를 통해 같은 국소 침투 함수에 `D50top`을 넘긴다. McCall 가속도 마찰 분기는 `min(D50top,hu/hv)`를 추가 전단응력에 사용한다. 각각 해당 옵션과 습윤 조건에 한정된다. (`groundwater.F90:512-527,1471-1482,1499-1509`; `bedroughness.F90:275-284,480-495,506-517`)

[최소 재현](../../../_staging/total-read/model-audit/XBeach/connectivity/physics/resolution-20260912/grain_assignment_probe.f90)은 원문 반복문을 그대로 추출하여 `ny=0`과 `ny=2`의 서로 다른 셀 분급비에 적용한다. 이는 Fortran 대입 결과 확인이며 XBeach 전체 계산이나 MPI 실행 검증이 아니다.

## 침식–지하수 교환량: 길이와 속도의 혼합

`infil`의 단위는 m/s이며 표면수에서 지하수로 향하는 값이 양수다. 습윤 퇴적 분기는 `dzbnow*por/dt`를 더한다. 반면 습윤 침식 분기의 `tempexchange=min((zb-gwlevel)*por,0)`는 m 단위인데 이를 `infil`에 그대로 더한다. 같은 `tempexchange`를 수위에 적용하는 것은 길이 갱신이며, 교환속도에 적용한 줄에서는 시간 나눗셈이 없다. (`variables.def:193`; `morphevolution.F90:817-835`)

확인된 결과는 스텝 직후 노출되는 `infil` 상태의 단위 불일치다. 표준 다음 스텝의 `gwflow`는 먼저 `infil=0`으로 초기화하고 교환속도를 새로 합산하고, 이어서 `executestep`이 `flow`를 호출한다. 연속식은 그 새 값을 사용한다. 그러므로 저장된 침식 보정량이 그대로 다음 스텝 연속식으로 누적된다는 주장은 이 경로에서 성립하지 않는다. 전체 질량오차의 크기는 이 정적 추적으로 정하지 않았다. (`groundwater.F90:283-294,538-540`; `libxbeach.F90:304-310`; `flow_timestep.F90:733-751`)

## 지형 갱신 뒤 수심과 다음 wet mask

`flow`는 `hh=max(zs-zb,eps)`를 만든다. 이후 지형–지하수 분기는 `zb`와 다른 양만큼 `zs`를 바꾸며 `bed_update` 안에는 `hh` 재대입이 없다. 다음 스텝의 `compute_wetcells`는 flow보다 먼저 저장된 `hh`로 `wetz`·파랑 wet mask를 만들고, 파랑 함수도 `hh`에서 유효 수심을 계산한다. (`flow_timestep.F90:938-941`; `morphevolution.F90:594-1182`; `libxbeach.F90:280-312`; `wetcells.F90:103-121`; `wave_timestep.F90:53-81`)

예를 들어 습윤 퇴적 셀에서 다른 보정과 수심 하한을 제외하면 `zb`는 `dzbnow`, `zs`는 `(1-por)*dzbnow`만큼 증가하므로 새 기하학적 수심은 이전 `hh - por*dzbnow`다. 저장된 `hh`는 그대로여서 아주 얕은 셀은 새 기하와 다른 wet 판정을 유지할 수 있다. 이것은 조건부 정적 결과이며 모든 셀의 mask 변화나 모든 파랑 모드의 매 스텝 재계산을 뜻하지 않는다. 지하수 없는 습윤 셀의 기본 수위 보정은 `zs`와 `zb`를 같은 양만큼 이동시킨다. 건조·경계·사면붕괴의 모든 분기를 이 예제로 포괄하지 않는다. (`morphevolution.F90:751-769,817-843`; `wetcells.F90:103-121`; `wave_timestep.F90:75-81`)

## Q3D 입력과 실행 분기는 다르다

`nz`는 별도 입력이며 기본값은 1이다. `q3d=1` 또는 `form=FORM_VANRIJN1993`일 때 Q3D 계수를 읽고 `nz=kmax`로 덮는다. 하지만 유동의 수직구조 함수 호출 조건은 **`nz>1 AND form/=FORM_VANRIJN1993`**다. 조건이 거짓이면 `ue_sed=ue`, `ve_sed=ve`다. (`params.F90:122,245,1139-1153`; `flow_timestep.F90:956-986`)

| 입력/상태 | 유동 수직구조 호출 판정 |
|---|---|
| `q3d=1`, `kmax>1`, Van Rijn 1993 이외 | `vsm_u_XB` 분기, 습윤 셀에서 호출 |
| `q3d=1`, `kmax=1` | 깊이평균 속도 대입 |
| Van Rijn 1993 | `kmax/nz`를 설정해도 `vsm_u_XB` 제외; 깊이평균 속도 대입 |
| `q3d=0`, 그 밖의 식, 별도 `nz>1` | 이 호출 guard에는 도달 가능; 전체 설정의 지원·할당 정합성까지 검증한 것은 아님 |

표는 위 인용의 입력 대입 및 `flow` guard를 대조한 결과다. Van Rijn 1993의 연직 농도 적분은 `morphevolution`에 따로 존재하므로 수직구조 함수 제외를 연직 농도 적분 부재로 해석하면 안 된다. (`morphevolution.F90:1748-1757,1815-1830`)
