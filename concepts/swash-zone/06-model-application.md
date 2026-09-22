---
title: "처오름을 모델에서 꺼내는 일 — 출력 설계 3종 대조(SWASH·XBeach·Celeris)와 게이지의 함정"
topic: swash-zone
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "[[03-analysis-methods]] §3 이 세운 A(매개변수화)/B(shoreline 해상) 축에서, B 경로 안의 '처오름 값을 실제로 어떻게 꺼내는가' 를 채운다. [[04-code-and-tools]] 는 어느 모델이 swash 를 해상하는지(모델 선택)까지 다루고 출력 경로는 다루지 않는다. SWASH 측 단언은 verified [[swash-wetting-drying-runup]](SwashRunupHeight·SwashDryWet·SwashBreakPoint·SwashUpdateDepths 직접 read)로 소급. XBeach 측은 **본 세션에서 소스 직접 read** — `ncoutput.F90:913-996`(runup 추출 루프)·`:1708-1727`(rugrowindex)·`varoutput.F90:182-191`·`params.F90:1255-1261`(nrugauge/nrugdepth/rugdepth 범위)·`params.F90:1796-1807`(rugdepth≤eps 승격). 인용한 코드·주석은 전부 해당 라인 verbatim 확인. XBeach `eps` 기본값 0.005 m 는 verified [[wetting-drying-cross-model]] 표에서 소급(params.F90:1398). **한계**: FUNWAVE·Celeris 의 처오름 출력 경로는 본 위키 노트에 기록이 없어 '미조사' 로 남겼다 — 부재로 단정하지 않았다. XBeach 발견 2건은 models/ 잠금 때문에 아직 `models/XBeach/source-analysis/` 에 반영하지 못했다(§6)."
note_author: "Claude Opus 5 (1M context)"
note_date: 2026-09-22
related:
  - concepts/swash-zone/03-analysis-methods.md
  - concepts/swash-zone/04-code-and-tools.md
  - models/SWASH/source-analysis/swash-wetting-drying-runup.md
  - models/XBeach/source-analysis/xbeach_output.md
  - concepts/compound-flooding/wetting-drying-cross-model.md
---

# 처오름을 모델에서 꺼내는 일

> [[03-analysis-methods]] §3 은 처오름을 얻는 두 경로를 세웠다 —
> **A. 매개변수화**(식으로 계산해 입력한다) vs **B. shoreline 해상**(결과로 얻는다).
> B 를 골랐다고 끝이 아니다. **모델이 물가선을 풀었다는 것과 당신이 $R_{2\%}$ 를 손에 쥐는 것은 다른 일이다.**
> [[04-code-and-tools]] 가 "어느 모델을 쓸까" 까지 답했다면, 이 노트는 그 다음 질문을 맡는다.

## 1. B 경로 안의 두 번째 축

물가선을 해상하는 모델에서 처오름 값을 꺼내는 설계는 둘로 갈린다.

| | **모델이 계산해 준다** | **사용자가 게이지로 뽑는다** |
|---|---|---|
| 대표 | SWASH `SwashRunupHeight` | XBeach runup gauge(`nrugauge`) |
| 산출 | 보간된 **수직 처오름 수위** 스칼라 | 교차 지점의 `xz`·`yz`·`zs` 시계열 |
| 위치 선정 | 모델이 찾는다 | **사용자 책임** |
| 제약 | 강한 기하 전제(아래 §2) | 격자·임계 설정에 종속(§3) |

A 경로(ShorelineS)에서는 처오름이 **입력**이었다. B 경로에서는 출력인데,
**그 출력을 만드는 규칙 자체가 모델마다 다르고 문서에 잘 드러나지 않는다.**

## 2. SWASH — 모델이 계산해 주지만, 1D 다

SWASH 는 처오름 높이를 출력량(115번)으로 직접 낸다. 자유표면과 (바닥 + 임계 `delrp`) 의
교차점을 **선형보간**해 수직 수위를 만든다.[^sw-algo]

$$rh = s_1(m_r) + (\delta_{rp} - h_s(m_r))\cdot\frac{s_1(m_r{+}1) - s_1(m_r)}{h_s(m_r{+}1) - h_s(m_r)}$$

문제는 전제다. 소스 주석이 직접 말한다 —
***"we restrict ourselves to 1D only and wave propagation is pointing eastward!"***[^sw-1d]

- **1D 전용.** 2D·비구조격자 처오름 출력 경로는 본 위키 검수 범위에서 확인되지 않았다(원 노트가 `source-needed` 로 명시).[^sw-1d]
- **동쪽 전파 전제.** 좌측 경계가 파 입사 경계가 아니면 경고 후 계산을 생략한다.[^sw-1d]

즉 **2D SWASH 로 처오름을 재려면 이 출력량은 쓸 수 없고, 사용자가 마스크·수위장에서 직접 뽑아야 한다.**
대신 쓸 수 있는 것이 침수 latch 다 — 수심이 `hrunp` 를 한 번이라도 넘은 셀은 `hindun=1` 로
**영구 기록**되므로 최대 침수선은 2D 로도 얻는다.[^sw-latch]

## 3. XBeach — 게이지는 점이 아니라 **행**이다

`nrugauge` 로 처오름 게이지를 최대 50개 놓을 수 있고, 각 게이지는 `x y stationid` 로 좌표를 받는다.[^xb-npoints]
그런데 추출 루틴을 읽으면 **x 좌표는 쓰이지 않는다.**

게이지는 `rugrowindex` 라는 **격자 행 인덱스 하나**로 환원되고(변수 주석: *"Array with row index
where runup gauge can be found"*), 그 값은 사용자 좌표의 **y 성분만** 가져온다
(`rugrowindex = ypoints(npoints+1:)`).[^xb-row] 추출 루프는 그 행의 **전 cross-shore 구간**
(`xmin+1 .. xmax`)을 훑는다.[^xb-scan]

```fortran
do j=xmin+1,xmax
   if ((sl%hh(j,  rugy)<=par%rugdepth(ird)) .and. &
   &   (sl%hh(j-1,rugy)> par%rugdepth(ird)) ) then
      idumhl=j-1
      exit
   endif
enddo
```

**수심이 임계를 가로지르는 첫 지점**을 찾아 그 셀의 `xz`·`yz`·`zs` 를 그대로 낸다.
코드 주석도 못박는다 — *"rugy now contains the local y-coordinate / rugx is not used"*.[^xb-scan]

실무 함의 셋.

1. **점을 찍었다고 생각하면 오해다.** 같은 행에 게이지를 둘 놓으면 같은 결과가 나온다.
   게이지가 고르는 것은 측선(cross-shore transect)이지 지점이 아니다.
2. **보간이 없다.** SWASH 가 교차점을 선형보간하는 것과 달리 XBeach 는 **교차 셀의 값을 그대로** 낸다.
   따라서 **처오름 해상도가 cross-shore 격자 간격에 직접 묶인다.**
3. **미검출은 `huge(0.d0)`**, MPI 에서는 **최솟값 reduce** 로 합쳐진다.[^xb-scan]

### ★ 처오름 임계는 침수-건조 임계 아래로 못 내려간다

`rugdepth` 는 여러 개(`nrugdepth`, 1–10) 지정해 한 게이지에서 복수 임계의 물가선을 동시에 받을 수 있다.
기본값은 **0.0** 이다.[^xb-rugdepth]

그런데 초기화 단계에서 `rugdepth ≤ eps` 인 항목은 전부 `(1+ε)·eps` 로 **올려진다**(경고 1줄과 함께).[^xb-clamp]
`eps` 는 XBeach 의 침수-건조 임계이고 기본값은 **0.005 m** 다.[^xb-eps]

따라서:

- **기본 설정에서 처오름 임계 = 침수-건조 임계**다. `rugdepth` 를 건드리지 않으면 0.0 이 아니라 `eps` 가 쓰인다.
- `eps` 를 안정성 때문에 키우면 **처오름 정의가 같이 움직인다.** 수치 설정 하나가
  물리량 정의를 바꾸는 결합이고, 로그의 경고 한 줄 말고는 드러나지 않는다.

[[03-analysis-methods]] 가 ShorelineS 에서 본 `runupform` 함정과 성격이 같다 —
**조용히 다른 정의가 적용되고 실행은 정상 종료한다.**

## 4. FUNWAVE·Celeris — 기록이 없다

두 모델 모두 물가선을 해상하지만(04 §2), **처오름을 꺼내는 전용 출력 경로는 본 위키 노트에 기록이 없다.**

- **Celeris**: shoreline 안정화가 셰이더 내부에 있다 — 최소수심 `delta` 와 이웃 bathy 차로 `h_cut`
  을 만들고 방향별 dry 플래그를 집계한다.[^ce-shore] 이것은 **안정화**이지 처오름 출력이 아니다.
- **FUNWAVE**: 검수된 12개 source-analysis 노트에 runup·shoreline 출력 언급이 없다.

이것은 **부재가 아니라 미조사**다. [[compound-flooding/04-code-and-tools]] 에서 LISFLOOD-FP 의 조석 부재를
전수 grep 으로 확인했던 것과 달리, 여기서는 세어 보지 않았다. §6 에 남긴다.

## 5. 물가선이 흔들리는 곳에서 물가선을 재는 일

처오름 추출은 모두 침수-건조 마스크나 수심장 위에 얹혀 있다. 그런데 처오름대는
**그 마스크가 가장 불안정한 곳**이다.

- **SWASH: breaking 점은 마스크상 dry 로 처리된다.** bore-front breaking 으로 판정된 점은
  비정수압 압력을 0 으로 놓아 정수압(bore)으로 전환하고, 이어서 `brks==1 → wets=0` 으로
  **수위점 마스크에서 dry 처리**한다.[^sw-brk] 처오름대는 bore collapse 가 상시 일어나는 곳이므로
  이 전환이 잦다.
- **SWASH: dry 임계가 실행 중에 커진다.** 수위가 바닥 아래로 내려가면 `epsdry` 를 `-1.01·hs` 로
  키워 안정화하고, 1 cm 를 넘으면 치명 오류로 중단한다 —
  *"INSTABLE: water level is too far below the bottom level!"* + *"Please reduce the time step!"*[^sw-eps]
  즉 **임계가 고정 상수가 아니다.**
- **XBeach: 위 §3 의 `eps` 종속.**

세 모델의 마스크 임계·판정 방식 자체의 대조는 [[wetting-drying-cross-model]] 가 8모델로 이미 다뤘다.
여기서 더할 것은 하나다 — **그 임계들이 침수 판정에만 쓰이는 것이 아니라 처오름의 정의에도 들어간다.**

## 6. 워크플로 권고와 남은 것

**권고**(본 노트가 확인한 범위에서):

| 상황 | 방법 |
|---|---|
| 1D SWASH, 동향 입사 | `SwashRunupHeight` 출력량 115 를 그대로 쓴다 |
| 2D SWASH | 115 는 쓰지 않는다. `hindun` latch 로 최대 침수선, 시계열 처오름은 수위장에서 직접 추출 |
| XBeach | 게이지 좌표의 **y(행)만 의미 있음**을 전제로 측선을 고른다. `rugdepth` 를 **명시**하고 `eps` 와의 관계를 기록한다 |
| 어느 쪽이든 | 실행 로그의 `rugdepth`·`epsdry` 경고를 검수 항목에 넣는다 |

**남은 것**:

- **XBeach 발견 2건의 `models/` 반영 미완** — "게이지=행" 과 "rugdepth≥eps 승격" 은 모델 메커닉이므로
  절대규칙 #6 상 [[xbeach_output]] 에 있어야 한다. `models/` 가 잠금 상태라 **SCOPED EDIT 승인 대기**.
  현재는 본 노트가 유일한 기록이다.
- **FUNWAVE·Celeris 처오름 출력 경로 미조사** — §4. 부재로 단정하지 않았다. `source-needed`
- **$R_{2\%}$ 까지 가는 후처리 미작성** — 위 방법들이 주는 것은 물가선 **시계열**이다.
  거기서 setup·swash 를 분리하고 초과확률 2% 를 뽑는 단계는 [[03-analysis-methods]] §4 가
  `source-needed` 로 남긴 scalogram·스펙트럼 분리와 같은 자리다.
- **한국 해빈 검증 사례** — [[04-code-and-tools]] §6 의 잔여와 동일. `source-needed`
- **2D SWASH 처오름의 실제 추출 예제** — 권고만 했고 실행해 보지 않았다.

## 출처

[^sw-algo]: [[swash-wetting-drying-runup]] §3.1 — `SwashRunupHeight` 는 동쪽(ml)에서 서쪽(mfu)으로 스캔해 최초로 `hs(nm) > delrp` 인 점 `mr` 을 찾고(`SwashRunupHeight.ftn90:103-117`), 자유표면과 (바닥+임계) 교차점을 선형보간해 `rh` 를 산출한다(`:134`). 출력량 115 번에 저장(`:154`). Purpose 주석: *"Calculates wave runup height for the purpose of output"*(`:40`), Method: *"Based on the intersection between free surface and bottom level + threshold for runup"*(`:44`).
[^sw-1d]: [[swash-wetting-drying-runup]] §3 — Note 주석 verbatim: *"we restrict ourselves to 1D only and wave propagation is pointing eastward!"*(`SwashRunupHeight.ftn90:46`). 좌측 경계가 파 입사(`ibl(1)` 2/3/7)가 아니면 경고 후 계산 생략(`:94-101`, *"no waves are imposed on west side"*). 같은 노트 §3 말미와 §8 이 "2D/비구조격자 runup **출력** 경로" 를 `source-needed` 로 명시한다.
[^sw-latch]: [[swash-wetting-drying-runup]] §4.4 — `hindun(nm) /= 1. .and. hs(nm) > hrunp` 이면 `hindun(nm) = 1.`(`SwashUpdateDepths.ftn90:804-806`). 원 노트 표현: "수심이 runup threshold `hrunp` 를 한 번이라도 넘으면 침수표시(1) 영구 기록 — maximum inundation 추적용 latch".
[^sw-brk]: [[swash-wetting-drying-runup]] §2.2·§2.3 — breaking 판정 시 `q(nm,:)=0` 으로 비정수압 압력을 0 으로 놓아 정수압 전환(`SwashBreakPoint.ftn90:123`), 루프 후 `wets(nm)==1 .and. brks(nm)==1` 이면 `wets(nm)=0`(`:238-242`). 주석: *"re-update mask array for wetting and drying at water level points by taking into account the breaking points"*(`:236`). 판정식은 `dsdt > alpha*sqrt(g*hs)`(onset)·`beta*sqrt(g*hs)`(재개시).
[^sw-eps]: [[swash-wetting-drying-runup]] §4.1 — `hs < -epsdry` 시 `epsdry` 를 `-1.01*hs` 로 키우고(`SwashUpdateDepths.ftn90:122-123`), 병렬 reduce 후 `epsdry > 0.01`(1 cm) 이면 치명 오류 *"INSTABLE: water level is too far below the bottom level!"* + *"Please reduce the time step!"*(`:176-182`, `:419-425`). 마지막에 `epshu = epsdry` 로 face 임계 동기화(`:186`, `:429`).
[^xb-npoints]: `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/params.F90:1256-1257` — `par%npoints = readkey_int('params.txt','npoints', 0, 0, 50)`, `par%nrugauge = readkey_int('params.txt','nrugauge', 0, 0, 50)`. 좌표 입력 형식(`x y stationid`)과 `pointtypes`(0=point, 1=rugauge)는 [[xbeach_output]] "Point / runup gauge output" 절(`params.F90:2219-2305`, `:2417-2524`).
[^xb-row]: `ncoutput.F90:113` 변수 선언 주석 verbatim: *"Array with row index where runup gauge can be found"*. 값 할당은 `ncoutput.F90:1720` 의 `rugrowindex = ypoints(par%npoints+1:)` — 즉 사용자 좌표 중 **y 성분(행 인덱스)만** 취한다. Fortran 출력 경로도 동일(`varoutput.F90:182-191`, 주석 *"Make rugrowindex with row number (per subprocess) with runup gauge"*).
[^xb-scan]: `ncoutput.F90:932-965` — `space_global_to_local(sl,1,rugrowindex(iru),rugx,rugy)` 로 전역 x 인덱스 **1** 과 `rugrowindex` 를 변환한 뒤, 주석 verbatim *"rugy now contains the local y-coordinate / rugx is not used"*(`:937-938`). 탐색 루프는 `do j=xmin+1,xmax` 로 그 행의 전 구간을 훑으며 `hh(j,rugy) <= rugdepth(ird) .and. hh(j-1,rugy) > rugdepth(ird)` 인 첫 `j` 에서 `idumhl=j-1` 후 `exit`(`:957-964`). 출력은 교차 셀의 `xz(idumhl,rugy)`·`yz`·`zs`(`:987-989`) — 보간 없음. 미검출 시 `tempvectorr = huge(0.d0)`(`:930`)이고 주석이 밝히듯 *"The runup values are collected in xomaster, using xmpi_reduce, taking the minimum values"*(`:925-926`).
[^xb-rugdepth]: `params.F90:1260-1261` — `par%nrugdepth = readkey_int('params.txt','nrugdepth',1,1,10)`(기본 1, 범위 1–10), `par%rugdepth = readkey_dblvec('params.txt','rugdepth',par%nrugdepth,size(par%rugdepth),0.0d0,0.0d0,0.1d0)`(기본 **0.0**, 범위 0.0–0.1). 게이지당 출력 벡터 길이는 `1 + nrugdepth*3`(`ncoutput.F90:915`, `:773` 주석).
[^xb-clamp]: `params.F90:1796-1807` — 주석 *"fix minimum runup depth"* 아래, `nrugauge>0` 이면 배열 잔여분을 `(1.0d0 + epsilon(0.d0))*par%eps` 로 채우고, `minval(par%rugdepth) <= par%eps` 인 경우 `where(par%rugdepth<=par%eps) par%rugdepth = (1.0d0 + epsilon(0.d0))*par%eps` 로 승격한 뒤 경고를 출력한다 — *"Warning: Setting rugdepth to minimum value greater than eps ("*. 기본값 0.0 은 항상 이 분기에 걸린다.
[^xb-eps]: [[wetting-drying-cross-model]] §1 표(XBeach 행) — `eps` 기본 0.005 m, 범위 0.001–0.1(`params.F90:1398`). 같은 표가 XBeach 의 cell/face 마스크 판정(`compute_wetcells`, `wetcells.F90:108-111`, `:75-77`)을 함께 기록한다.
[^ce-shore]: [[celeris-breaking-boundary]] — "경계 강제 이후 셰이더 끝에서 shoreline 안정화(`:490-590`). `delta`(최소 수심)와 이웃 bathy 차로 `h_cut` 계산(`:527-531`), 각 방향 dry 플래그(`:533-543`), `sum_dry` 집계(`:545`)."
