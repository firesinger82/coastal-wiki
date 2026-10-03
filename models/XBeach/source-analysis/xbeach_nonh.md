---
title: "XBeach nonh — pres/dp 압력 예측·보정, 1층·reduced 2층 및 MPI 호출"
topic: xbeach
canonical_source: self
citation_status: verified
verification_method: "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/nonh.F90 (3471) 직접 read — nonh_cor(146 entry, 2회/step), nonhq3d 분기(1-layer nonh_1lay_pred/cor vs reduced 2-layer nonh_2lay_pred/cor_2dV/3d, 174-249), 5-diagonal pressure matrix mat+rhs+dp, solver_solvemat(686/1412/2164) file:line 인용. Pieter Bart Smit 2009/2014."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — projection 압력보정·2-layer·predictor-corrector verbatim"
verification_date: 2026-06-03
related:
  - models/XBeach/source-analysis/xbeach_flow_solver.md
  - models/XBeach/source-analysis/xbeach_mode_dispatch.md
  - models/XBeach/source-analysis/xbeach_wave_action_balance.md
source_correction_date: 2026-09-12
source_correction_by: "Codex"
source_correction_scope: "선박 `ph`와 비정수압 `pres/dp`, 정수 dispatch 및 현재 MPI 구현을 구분"
source_correction_human_approval: not-issued
---

> **2026-09-12 AI 출처 정정**: 선박 `ph`와 비정수압 `pres/dp`, 정수 dispatch 및 현재 MPI 구현을 구분. 기존 `verification_*`는 이전 검증 이력이며 이번 정정의 새 사람 승인이 아니다. [원문 구간·SHA와 연결 판정](../../../_staging/total-read/model-audit/XBeach/connectivity/runtime-20260912/evidence.json)을 따르며 원본 솔버는 수정하지 않았다.

# XBeach nonh 압력 보정의 실행 연결

현재 입력 이름은 `wavemodel=nonh`다. 이 모드의 압력 상태는 **`s%pres`**, 선형계의 해·보정 작업 배열은 **`dp`**다. `ph`는 선박 압력수두 [m]이며 nonh 압력의 별칭이 아니다. (`params.F90:70-79`; `variables.def:256`; `nonh.F90:683-697`)

## 1. 유동과 압력의 호출 순서

`flow`는 일반 운동량 갱신 뒤 `wavemodel==WAVEMODEL_NONH`이면 `nonh_cor(...,0)`을 호출한다. 이어 `secorder==1`의 `flow_secondorder_advUV`를 거쳐 `nonh_cor(...,1)`을 호출한다. predictor에서 기존 압력의 명시적 기여를 넣는 부분도 `secorder==1` 조건을 가진다. (`flow_timestep.F90:563-658`; `nonh.F90:1234-1262, 1844-1883, 2858-2935`)

## 2. `nonhq3d`의 정수 분기

| `nonhq3d` | 공간 조건 | `ipredcor==0` | 그 외 (`flow`는 1을 전달) |
|---|---|---|---|
| 1 | `ny==0` | `nonh_2lay_pred_2dV` | `nonh_2lay_cor_2dV` |
| 1 | `ny!=0` | `nonh_2lay_pred_3d` | `nonh_2lay_cor_3d` |
| default (통상 0) | 별도 ny 분기 없음 | `nonh_1lay_pred` | `nonh_1lay_cor` |

이는 `nonh.F90:201-247`의 `SELECT CASE`와 내부 IF를 전사한 표다. `.true./.false.` 논리형 SELECT가 아니다. 각 루틴 내부의 공간 경계·wet 조건은 별도로 적용된다.

## 3. 압력 저장과 속도 보정

세 corrector는 `solver_solvemat(mat,rhs,dp,nx,ny,par)`로 압력 선형계를 풀고 속도를 보정한다. 1층 경로는 `s%pres += dp`를 수행한다. 두 reduced 2층 경로는 `secorder==1`이면 `s%pres += dp`, 그 외에는 `s%pres = dp`를 사용한다. (`nonh.F90:683-697, 1411-1422, 2162-2176`)

이 값은 nonh 루틴 내부의 수평·연직 속도 보정에 쓰인다. 기존 설명의 `dp → ph → g∂(zs+ph)` 연결은 잘못된 귀속이었다. `flow`의 `zs+ph` 경사는 선박 외력 경로이며 비정수압 보정과 별도로 읽어야 한다. (`nonh.F90:1234-1262`; `flow_timestep.F90:131-149`; [[xbeach_flow_solver]])

### 3.1 보고서 압력항 식과 코드의 부호 대조

비정수압 보고서(non-hydrostatic_report_draft)는 바닥을 $z=-d$로 정의한다(인쇄 3쪽·PDF 13쪽 Figure 2-2). 따라서 코드의 `zb`는 보고서의 $-d$에 해당한다.

- 보고서 식 (2.15)의 첫 표현 $\frac{H_{i+1,j}\bar p_{i+1,j}-H_{i,j}\bar p_{i,j}}{\Delta x}-p_{i+\frac12,j}\frac{d_{i+\frac12,j}-d_{i-\frac12,j}}{\Delta x}$에 $H=\eta+d$, $\bar p=\frac12p$, $p_{i+\frac12,j}=\frac12(p_{i+1,j}+p_{i,j})$를 넣으면 $\frac{(\eta_{i+1,j}+d_{i,j})p_{i+1,j}-(\eta_{i,j}+d_{i+1,j})p_{i,j}}{2\Delta x}$가 된다(Claude 전개).
- 보고서는 같은 식의 마지막 표현을 $(\eta^{n+1}_{i,j}-d^{n+1}_{i+1,j})$로 인쇄한다(인쇄 15쪽·PDF 25쪽, 쪽 이미지로 확인). 식 (2.18)과 (2.19)도 같은 자리에 $-d$를 인쇄한다(인쇄 16쪽·PDF 26쪽).
- 코드는 `au(1,i,j) = - (s%zs(i+1,j) - s%zb(i  ,j))*vol`, `au(0,i,j) = + (s%zs(i  ,j) - s%zb(i+1,j))*vol`이다(`nonh.F90:1194-1195`). v 방향도 같은 형태다(`nonh.F90:1217-1218`). `zb=-d`를 넣으면 두 괄호는 모두 $\eta+d$ 형태다. 따라서 코드는 첫 표현을 전개한 식과 같다. 보고서 마지막 표현의 $-d$는 첫 표현과 맞지 않는 인쇄 부호다.
- 보고서 식 (1.13)은 y 이류항 앞에 $-$를, 식 (1.17)은 $+$를 인쇄한다(인쇄 6쪽·PDF 16쪽). 코드의 u 운동량 잔차는 x 이류항과 y 이류항을 같은 부호로 더한다: `dudt = (s%ududx(i,j)+s%vdudy(i,j)-s%viscu(i,j) &`(`flow_timestep.F90:564`). 따라서 코드는 식 (1.17)의 부호와 같다.
- 확인하지 않은 것: 이 부호 차이가 계산 결과에 주는 영향은 모델 실행으로 확인하지 않았다. 코드는 보고서의 인쇄 오기와 무관하게 첫 표현의 전개와 일치한다.

## 4. MPI 빌드와 실제 guard

`nonh.F90:42-43`의 MPI 제외 문장은 오래된 주석이다. 현재 조사한 MPI 프로젝트에 이 소스가 포함되고, 구현 안에는 `#ifdef USEMPI`로 감싼 `xmpi_shift_ee` 호출이 있다. 이를 `#ifdef CMPI`에 의해 모듈 전체가 제외된다고 설명할 근거는 없다. (`nonh.F90:1446-1449, 1872-1883, 2237-2241, 2927-2935`; [[xbeach-build-mode-connectivity]])

이 판정은 소스와 빌드 포함 관계다. 모든 MPI·nonh 옵션 조합의 수치 실행 검증을 뜻하지 않는다.

## 5. 연결

- [[xbeach_flow_solver]] — 운동량·2차 보정·압력 호출 순서
- [[xbeach_mode_dispatch]] — 파랑 모드 선택
- [[xbeach_wave_action_balance]] — stationary/surfbeat 파랑 계산
- [[xbeach-build-mode-connectivity]] — 컴파일 대상과 실행 모드 근거
