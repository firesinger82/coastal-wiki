# XBeach 연결 물리 추적: wave–flow–sediment–morphology 피드백

이 문서는 `models/XBeach/raw/source_code/trunk/src/xbeachlibrary`의 동결 소스에서 연결 계산만 추적한 phase-2 작업물이다. 기존 281개 소스의 이중 판독과 closure 원장을 출발점으로 삼되, 판정은 `libxbeach.executestep`의 실제 호출 순서, 각 모듈의 mode guard, 배열 대입, MPI 교환, Makefile 포함 여부를 원문에서 다시 대조했다. 원문 SHA-256, physical-LF 행 번호, CR을 보존한 정확 인용, 상태별 단위·부호·격자 위치는 [connectivity.json](connectivity.json)에 있다. 이 범위 결과는 기존 closure·raw·canonical·HG·crosswalk를 변경하거나 전체 모델 감사를 완료했다고 주장하지 않는다.

한 유체 스텝의 연결 순서는 다음과 같다.

```text
prior zb/zs/hh/H
  -> wet/dry masks -> dt and t -> wave/gw/flow boundaries
  -> ship ph -> stationary|surfbeat wave -> vegetation
  -> groundwater -> hydrostatic flow + optional nonh predictor/corrector
  -> sediment transport -> morfac-scaled bed update
  -> next-step depth/mask/wave/groundwater/vegetation feedback
```

핵심 시간 관계는 세 가지다. 첫째, surfbeat가 만든 `Fx/Fy`, `urms`, `ust`는 같은 스텝 유동과 표사에 들어가지만, 식생 `Dveg`는 파랑 뒤에 계산되므로 다음 surfbeat 스텝에 쓰인다. stationary에서는 이 지연이 다음 `wavint` 파랑 재계산까지 늘어난다. 반면 식생 `Fvegu/Fvegv`는 유동 전에 만들어져 같은 스텝 운동량에 들어간다. 둘째, 지하수는 유동보다 먼저 실행되어 이전 nonh 보정의 `pres`를 시간평균하고, 그 결과 `infil`은 같은 스텝 표면수 연속식에 `-infil`로 들어간다. 셋째, 표사는 유동 뒤에 현재 Eulerian 속도와 파랑 궤도·비대칭 성분을 사용하고, 지형은 `morfac*dt/(1-por)`로 같은 스텝 끝에 갱신된다.

모드별 연결은 명확히 갈린다. stationary는 `wavint` 또는 새 경계에서만 복사응력과 Stokes drift를 다시 만들고 그 사이 값을 유지한다. 다방향 surfbeat는 방향별 action·roller를 매 `dt` 전진시킨다. `single_dir=1` surfbeat는 방향장을 `wavint`에 갱신하면서 에너지는 매 스텝 전진시킨다. nonh는 `swave=0`으로 강제되고 `flow` 안에서 압력 예측·보정을 두 번 호출한다. `nonhq3d=0`은 1층, `nonhq3d=1`은 축약 2층이며, 후자는 `ny=0`에서 2DV, `ny>0`에서 코드명이 3D인 2DH 경로를 탄다. 표사 입력 `q3d`와 비정수압 입력 `nonhq3d`는 서로 다른 스위치다.

격자는 `(nx+1,ny+1)` 공유 저장을 쓰되 의미가 다르다. `zs/zb/hh/E/R`은 수위·파랑점, `uu/qx/Fx`는 u 면, `vv/qy/Fy`는 v 면에 놓인다. 2DH 복사응력 발산과 Exner 갱신은 u/v 면 플럭스를 eta 중심으로 모은다. true 1D는 `ny=0`, `j=1` 분기를 사용하며 y 방향 수송 대신 지형식의 `lsgrad` 항만 남는다. MPI에서는 외부 경계를 physics 전에 적용하고, `ee/rr`, `uu/vv`, `zs`, 지하수장, `zb`를 각 소비 직전 또는 생산 직후에 교환한다. Makefile은 이 연결에 등장한 모든 런타임 모듈을 무조건 소스 목록에 넣고, `USEMPI`는 halo 호출을 전처리기로 켠다.

현재 소스에서 닫히지 않는 연결 문제는 네 건이다.

1. 다분급 지형 갱신의 `D50top`·`D90top` 대입 왼쪽에 `(i,j)`가 없어, 루프의 각 스칼라가 배열 전체를 덮는다. 다음 스텝 지하수 침투는 `D50top(i,j)`를 읽으므로 마지막 순회 셀 값이 전 영역에 전달될 수 있다.
2. 지형 침식–지하수 보정에서 `tempexchange=(zb-gwlevel)*por`는 길이인데 `infil [m/s]`에 그대로 더한다. 바로 위 퇴적 분기는 `dt`로 나누므로 단위 불일치가 코드 내부에서도 드러난다. 다음 `gwflow`가 flow 소비 전에 `infil=0`으로 초기화하므로 확인된 영향 범위는 다음 연속식 강제보다 스텝 직후 BMI·출력 상태다.
3. `gwflow` 결합 지형 갱신은 공극수 때문에 `zs-zb`를 바꿀 수 있지만 `hh`를 다시 만들지 않는다. 다음 스텝은 flow 끝에서 `hh`를 갱신하기 전에 wet mask와 파랑을 계산하므로 이 결합에서 한 스텝 오래된 수심이 노출된다. 지하수 없는 핵심 지형분기는 `zs`와 `zb`를 같은 양만큼 옮겨 `hh`를 보존한다.
4. `q3d`는 이 스냅샷의 실행 소스에서 직접 분기되지 않고 `kmax`, `nz`를 통한 간접 경로만 확인된다. `FORM_VANRIJN1993`도 같은 Q3D 입력을 켜지만 `vsm_u_XB` 호출에서는 명시적으로 제외된다. `transus`의 q3d 로컬 배열은 할당 뒤 사용되지 않는다. 이는 이 소스판의 범위 제한 판정이며 다른 판본으로 일반화하지 않는다.

`connectivity.json`의 14개 edge는 이 범위의 대표 상태전달 계약 후보로서 생산자·소비자·상태·호출시점·guard·배열범위·단위/부호를 고정한다. 전체 XBeach subroutine 호출의 분모나 전수 edge 목록은 아니다. 6개 mode contract는 stationary, 두 surfbeat 형태, nonh 1층, nonh 축약 2층 1D/2DH를 별도로 기록한다. 향후 embedded 도움말 자료가 코드 의미를 보강하더라도 소스 실행경로와 충돌하는 설명은 별도 판본 증거로 남겨야 한다.
