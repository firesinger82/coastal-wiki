---
title: "FUNWAVE-TVD 2D 방향스펙트럼 조파 source-analysis — WK_DATA2D (SWAN→Boussinesq nesting: 내부소스 vs ABS 경계)"
topic: funwave-wk-data2d-spectral-wavemaker
canonical_source: self
citation_status: verified
verification_method: "FUNWAVE-TVD raw source 직접 read: src/wavemaker.F(3299)+sources.F+sponge.F — Wei-Kirby D_gen(:803)·±60° directional cull(:239) file:line 직접 검증. 소스주석 primary Wei-Kirby(:824)·Salatin2021(sponge.F:103). 조파 개괄은 funwave-physics-sources.md §2에 있다. 2026-10-18 FUNWAVE recovery 대조 보고서 반영" # [10-18 전수 검증 정정]
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-07
verification_by: "Claude Opus 4.8 (1M context) — wavemaker.F:238-246·801-805 직접 read 검증"
verification_date: 2026-07-07
last_source_check: "2026-10-18 (recovery 대조 반영)"
related:
  - models/FUNWAVE/source-analysis/funwave-physics-sources.md
  - models/FUNWAVE/source-analysis/funwave-dispersion-solver.md
  - concepts/waves/06-model-application.md
source_scope: FUNWAVE-TVD
---

# FUNWAVE-TVD 2D 방향스펙트럼 조파 — `WK_DATA2D` (SWAN nesting)

> 소스: [`src/wavemaker.F`](../raw/source_code/FUNWAVE-TVD/src/wavemaker.F)(3299) + `sources.F`(:150-165) + `sponge.F`(:77-156).
> WK_DATA2D는 NumFreq×NumDir 성분 자료를 내부 조파원으로 읽는다. 소스 주석은 SWAN과 관측 자료에서 변환한 성분을 언급한다. 근거: `FUNWAVE-TVD/src/wavemaker.F:196–243,291–293`. 조파 개괄은 [funwave-physics-sources.md](funwave-physics-sources.md)의 §2에 있다. 모델 적용은 [파랑 모델 적용](../../../concepts/waves/06-model-application.md)에 연결한다. [10-18 전수 검증 정정]
> **2 경로**: (A) **내부소스** `WK_WAVEMAKER_2D_SPECTRAL_DATA`→`CALCULATE_Cm_Sm` / (B) **absorbing-generating 경계** `CALCULATE_DATA2D_Cm_Sm`→`ABSORBING_GENERATING_BC`.

## 0. 구조
| 서브루틴 | 라인 | 역할 |
|---|---|---|
| WK_DATA2D reader | wavemaker.F:196-340 | WaveCompFile 읽기(NumFreq/NumDir/PeakPeriod/freq·dir축/WAVE_COMP 2D진폭/opt Phase2D) + direction cull |
| `WK_WAVEMAKER_2D_SPECTRAL_DATA` | :627-819 | 성분별 fully-dispersive wavenumber + Wei-Kirby `D_gen` + Gaussian width |
| `CALCULATE_Cm_Sm` | :831-891 | 공간 source 배열 `Cm/Sm` 조립 |
| `CALCULATE_DATA2D_Cm_Sm` | :903-1042 | 경계경로: Airy Newton + `Cm_eta/Sm_eta/Cm_u/Sm_u/Cm_v/Sm_v` |
| apply(내부소스) | sources.F:150-165 | `WaveMaker_Mass=Σ AA(Cm·cosωt+Sm·sinωt)`, ramp `AA=tanh` |
| `ABSORBING_GENERATING_BC` | sponge.F:77-156 | Ein2D/Uin2D/Vin2D 재구성 + tide relaxation |

## 1. 스펙트럼 입력 + ★±60° cull (:196-340)

WK_DATA2D 파일의 둘째 행에는 첨두주기를 초 단위로 쓴다. (`FUNWAVE-TVD/src/wavemaker.F:203`; inputs:FI1-093) [10-18 대조 정정]

진폭 파일은 방향별 행에 주파수 값을 나열한다. (`FUNWAVE-TVD/src/wavemaker.F:210–212`; inputs:FI1-095) [10-18 대조 정정]

`IF(WaveMaker(1:9)=='WK_DATA2D')THEN` 경로는 `IF(ABS(Dire(I)).LT.60.0_SP)THEN`을 만족하는 성분만 남긴다. (`FUNWAVE-TVD/src/wavemaker.F:196,239`; theory-numerics:FT1-255) [10-18 대조 정정]

`IF(INPUT_WAVE_PHASE)THEN`에서 `Phase2D(J,I)=Phase2D(J,I)*0.005555555555556*pi`로 입력 위상을 변환한다. (`FUNWAVE-TVD/src/wavemaker.F:295–299`; gpu-vs-tvd:FG1-139) [10-18 대조 정정]

## 2. 내부소스 경로 (A)
```fortran
! Nwogu α=-0.39 fully-dispersive wavenumber:
alpha1=α+1/3 ; tb=ω²h/g ; tc=1+tb·α ; wkn=√((tc-√(tc²-4α1·tb))/(2α1))/h   ! :774-793
! Wei-Kirby 내부소스 진폭:
D_gen = 2·AMP_WK·cosθ·(ω²-α1·g·k⁴h³)/(ω·k·rI·(1-α(kh)²))                    ! :803-805
rlamda=k·sinθ ; beta_gen=80/δ²/L² ; rI=√(π/beta)·exp(-rl_gen²/4beta)       ! :798-801, width=δL/2 :810
! 공간 조립:
Cm(i,j,kf)=Σ_θ D_gen·exp(-beta·(x-Xc)²)·cos(rlamda·y+φ)  ; Sm=sin         ! :874-882
! 시간적분(sources.F):
WaveMaker_Mass = Σ AA·(Cm·cosωt + Sm·sinωt) ; AA=tanh(π·FreqPeak·t/Time_ramp)  ! sources.F:151-163
```

## 3. 경계 경로 (B)
```fortran
! ★Airy(선형) 분산 Newton — 내부소스의 fully-dispersive 와 다름:
Fk=g·k·tanh(kh)-σ² ; k←k-Fk/Fkdif ; |Fk|≤1e-8 or Iter>1000   ! :937-943
Cm_eta=Σ_dir Amp·cos(k·sinθ·Y+k·cosθ·X) ; Sm_eta=sin          ! :1004-1009
Cm_u=Σ Amp·σ·cosh(k·Zlev)/sinh(kh)·cosθ·cos(...) ; Zlev=|1+Beta_ref|·Dep_Ser   ! :960,1010-1033
! sponge.F: Ein2D=Σ(Cm_eta·cos+Sm_eta·sin); Eta=Ein2D+(Eta-Ein2D)·SPONGE_TIDE_WEST  :115-140
```

## 4. 주요 findings (code≠manual/intent)
- ±60도 경계값은 포함하지 않는다. (`FUNWAVE-TVD/src/wavemaker.F:239`; theory-numerics:FT1-255) [10-18 대조 정정]
- **★두 경로 분산관계 상이**: 내부소스=fully-dispersive Nwogu(α=-0.39, :792), 경계=선형 Airy(:937). **동일 스펙트럼이 경로 선택에 따라 다른 wavenumber**.
- **★생성경계가 η만 강제**(속도 relaxation 주석처리 sponge.F:142-143), Cm_u/Sm_u 는 계산되나 미사용 → 배열이 암시하는 full η+velocity ABS-gen BC 아니라 elevation-forced.
- **위상 처리 경로간 불일치**: 내부소스는 Phase2D 적용(:295-316), 경계는 `+Phase_Ser` 주석처리(sponge.F:113) → σt 만.
- 위상 자료가 없으면 난수 rad 값을 만든다. (`FUNWAVE-TVD/src/wavemaker.F:303–314`; inputs:FI1-283) [10-18 대조 정정]
- **속도 평가 준위 = Nwogu reference depth**(`Zlev=|1+Beta_ref|·Dep_Ser`:960) — "depth-averaged" 단순해석과 다름.

## 5. Primary sources
- **Wei, Kirby, Grilli & Subramanya 1995 / Wei-Kirby 1999** — 내부소스 wavemaker(`D_gen` 폐형 §2, 소스주석 :824).
- **Chen et al. 2000** — fully nonlinear Boussinesq(Nwogu α=-0.39 §2).
- **Shi et al. 2012** *Ocean Modelling* 43-44 — FUNWAVE-TVD reference(source function + ABS-gen BC).
- **Salatin et al. 2021** JGR-Oceans e2021JC017641 — WK_NEW_DATA2D·ABS-gen 가속(소스 in-code sponge.F:103).

## 6. 관련
- [funwave-physics-sources.md](funwave-physics-sources.md) — §2에 조파 개괄이 있다. [10-18 전수 검증 정정]
- [funwave-dispersion-solver.md](funwave-dispersion-solver.md) — Boussinesq 분산항과 삼중대각 풀이를 정리한다. [10-18 전수 검증 정정]
- [`concepts/waves/06-model-application.md`](../../../concepts/waves/06-model-application.md) — 정온도 SWAN→Boussinesq nesting(WK_DATA2D 가 그 연결)

## 문서와 코드 차이 (10-18 대조)

이 절은 [배정표](../../../_staging/recovery/assign/FUNWAVE-note-job-7.tsv)가 지정한 WK_DATA2D 입력·방향 필터·위상 처리와 GPU 국소 식의 차이를 수록한다.
근거 보고서는 [theory-numerics](../../../_staging/recovery/compare/funwave-theory-numerics-vs-code.md), [inputs](../../../_staging/recovery/compare/funwave-inputs-vs-code.md), [v21-manual](../../../_staging/recovery/compare/funwave-v21-manual-vs-code.md), [gpu-vs-tvd](../../../_staging/recovery/compare/funwave-gpu-vs-tvd.md)이다.
최종 분류는 각 보고서의 차이 결론 절과 끝의 10-18 전수 검증 기록을 따른다.
GPU와 TVD의 코드만 대조한 행은 문서 원문 칸에 `—`를 쓴다.

문서 판: FUNWAVE-TVD 3.0 문서 "Release Dec 2016", 공개 저장소에서 PDF 마지막 변경 `fef45a7 2018-02-24`; 2.1 매뉴얼·code_analysis `b9c035d 2016-11-03`; 코드 판: 공개 저장소 `github.com/fengyanshi/FUNWAVE-TVD` HEAD `b4c322e 2025-01-24`, `FUNWAVE-TVD/src/main.F:47` `!    VERSION 3.0`; GPU 판 `github.com/dryuanye/FUNWAVE-GPU` `7f892ba 2019-11-26`과 로컬 수정 3파일(`src/etauv_solver_gpu.F`, `src/mod_cuda.F`, `src/Makefile_cuda`).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| theory-numerics:FT1-255 | 3.0 p.30의 방향 스펙트럼 입력 설명에는 성분 삭제 조건이 없다. | funwave_tvd_3.0.pdf p.30: 3.0 p.30의 방향 스펙트럼 입력 설명에는 성분 삭제 조건이 없다. | `FUNWAVE-TVD/src/wavemaker.F:239` `IF(ABS(Dire(I)).LT.60.0_SP)THEN`;<br>`FUNWAVE-TVD/src/wavemaker.F:243` `WaveCompTmp(J,DireCount) = WAVE_COMP(J,I)`;<br>`FUNWAVE-TVD/src/wavemaker.F:196–199,238–246`; `FUNWAVE-TVD/src/io.F:870,1850` | C | `IF(WaveMaker(1:9)=='WK_DATA2D')THEN` 경로는 `IF(ABS(Dire(I)).LT.60.0_SP)THEN`을 만족하는 성분만 남긴다. ±60도 경계값은 포함하지 않는다. C 판정은 3.0 p.30에 이 삭제 조건이 없는 점이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| inputs:FI1-089 | WAVEMAKER=WAVE_DATA | `funwave_tvd_3.0.pdf p.37`: “2D directional spectrum data specified in WaveCompFile. Need Xc_WK, Yc_WK, DEP_WK, Delta_WK.”<br>`WAVEMAKER = WAVE_DATA` | `FUNWAVE-TVD/src/io.F:1850`: `IF(WaveMaker(1:13)=='WK_NEW_DATA2D'.OR.WaveMaker(1:9)=='WK_DATA2D')THEN`; `FUNWAVE-TVD/src/io.F:1926`: `CALL READ_STRING(WaveCompFile,FILE_NAME,'WaveCompFile',ierr)`<br>`7b93138:src/io.F:523` `IF(WaveMaker(1:9)=='WK_DATA2D')THEN`; `7b93138:src/io.F:549` `CALL READ_LOGICAL(WAVE_DATA,FILE_NAME,'WAVE_DATA',ierr)`; `fef45a7:src/io.F:1721` `IF(WaveMaker(1:9)=='WK_DATA2D')THEN` | B | WAVEMAKER의 선택값 WK_DATA2D와 과거 논리 입력 WAVE_DATA를 구분한다. 과거 논리 입력 WAVE_DATA는 WAVEMAKER 선택값과 별개다. FI1-305도 같은 선택값을 가리킨다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| inputs:FI1-093 | peak_freq | `funwave_tvd_3.0.pdf p.38`: `peak_freq (real)` | `FUNWAVE-TVD/src/wavemaker.F:203`: `READ(1,*)PeakPeriod`; `FUNWAVE-TVD/src/wavemaker.F:324`: `FreqPeak = 1.0_SP/PeakPeriod`<br>`7b93138:src/wavemaker.F:204` `READ(1,*)PeakPeriod`; `7b93138:src/wavemaker.F:239` `FreqPeak = 1.0_SP/PeakPeriod`; `fef45a7:src/wavemaker.F:204` `READ(1,*)PeakPeriod` | B | WK_DATA2D 파일의 둘째 행에는 첨두주기를 초 단위로 쓴다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| inputs:FI1-095 | 진폭 행렬 배치 | `funwave_tvd_3.0.pdf p.38`: `2D array of wave magnitude ((amp(I,J),I=1,ndir),J=1,nfreq)` | `FUNWAVE-TVD/src/wavemaker.F:210–212`: `DO I=1,NumDir`<br>`         READ(1,*)(WAVE_COMP(J,I),J=1,NumFreq)`<br>`       ENDDO`<br>`7b93138:src/wavemaker.F:211` `DO I=1,NumDir`; `7b93138:src/wavemaker.F:212` `READ(1,*)(WAVE_COMP(J,I),J=1,NumFreq)`; `7b93138:src/wavemaker.F:213` `ENDDO`; `fef45a7:src/wavemaker.F:212` `READ(1,*)(WAVE_COMP(J,I),J=1,NumFreq)` | B | 진폭 파일은 방향별 행에 주파수 값을 나열한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| inputs:FI1-283 | 선택 위상·방향 필터 | funwave_tvd_3.0.pdf p.38 | `FUNWAVE-TVD/src/wavemaker.F:213–215`: `DO I=1,NumDir`<br>`         READ(1,*,END=110)(Phase2D(J,I),J=1,NumFreq)`<br>`       ENDDO`; `FUNWAVE-TVD/src/wavemaker.F:299`: `Phase2D(J,I)=Phase2D(J,I)*0.005555555555556*pi`; `FUNWAVE-TVD/src/wavemaker.F:312`: `Phase2D(J,I)=rand(0)*2.0_SP*pi`; `FUNWAVE-TVD/src/wavemaker.F:239`: `IF(ABS(Dire(I)).LT.60.0_SP)THEN`; `FUNWAVE-TVD/src/wavemaker.F:252`: `NumDir=DireCount` | C | 3.0 PDF p.38의 WK_DATA2D 형식에는 선택 위상과 방향각 필터가 없다. 진폭 뒤 같은 방향 행 배치로 위상을 degree 단위로 읽고 rad로 바꾼다. 위상 자료가 없으면 난수 rad 값을 만든다. `IF(ABS(Dire(I)).LT.60.0_SP)THEN`에서 방향과 진폭을 남기고 NumDir를 줄인다. 이 사실을 모든 입력 배열의 재배열 보장으로 확대하지 않는다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
| v21-manual:FV1-449 | 2.1 p.37 `WaveCompFile`에 대한 `funwave_tvd_3.0.pdf` p.38의 다른 형식: `nfreq(integer) ndir(integer)`, `peak_freq (real)`, 주파수 목록, 방향 목록, `((amp(I,J),I=1,ndir),J=1,nfreq)`. | funwave_tvd_2.1_manual.pdf p.37: `WaveCompFile`;<br>funwave_tvd_3.0.pdf p.38: `nfreq(integer) ndir(integer)`, `peak_freq (real)`, 주파수 목록, 방향 목록, `((amp(I,J),I=1,ndir),J=1,nfreq)` | `FUNWAVE-TVD/src/wavemaker.F:198` `READ(1,*)NumFreq,NumDir`; `FUNWAVE-TVD/src/wavemaker.F:203` `READ(1,*)PeakPeriod`; `FUNWAVE-TVD/src/wavemaker.F:324` `FreqPeak = 1.0_SP/PeakPeriod`; `FUNWAVE-TVD/src/wavemaker.F:210–212` `DO I=1,NumDir` / `READ(1,*)(WAVE_COMP(J,I),J=1,NumFreq)` / `ENDDO`; [git 이력 판정](../../../_staging/recovery/compare/FUNWAVE-git-verify-AD2.md), `2e72b18:wavemaker.F:204` `READ(1,*)PeakPeriod` | B | 첫 두 정수는 같다. 다음 스칼라는 주파수가 아니라 대표 주기다. 문서는 한 행에 방향 성분을 놓는다. 코드는 한 행에 주파수 성분을 놓는다. 주파수·방향 개수가 다르면 문서의 배열 순서를 그대로 읽을 수 없다. 2016년 코드도 이 순서를 사용한다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| v21-manual:FV1-475 | 2차원 성분표의 위상 배열 | funwave_tvd_3.0.pdf p.38의 `WaveCompFile` 2차원 형식은 진폭 배열 뒤의 위상 배열을 적지 않는다. funwave_tvd_2.1_manual.pdf p.37의 3열 형식과도 다르다. | `FUNWAVE-TVD/src/wavemaker.F:213–215` `DO I=1,NumDir` / `READ(1,*,END=110)(Phase2D(J,I),J=1,NumFreq)` / `ENDDO`; `FUNWAVE-TVD/src/wavemaker.F:196–198` `IF(WaveMaker(1:9)=='WK_DATA2D')THEN` / `OPEN(1,FILE=TRIM(WaveCompFile))` / `READ(1,*)NumFreq,NumDir`; `FUNWAVE-TVD/src/wavemaker.F:210–215` `DO I=1,NumDir` / `READ(1,*)(WAVE_COMP(J,I),J=1,NumFreq)` / `ENDDO` / `DO I=1,NumDir` / `READ(1,*,END=110)(Phase2D(J,I),J=1,NumFreq)` / `ENDDO`; `FUNWAVE-TVD/src/wavemaker.F:229–230` `109    INPUT_WAVE_PHASE = .TRUE.` / `110    CONTINUE`; `FUNWAVE-TVD/doc/funwave_tvd_3.0.tex:1201–1211` | C | C는 3.0 매뉴얼 p.38의 2차원 WaveCompFile 형식에서 위상 배열을 생략한 점이다. WK_DATA2D 분기는 진폭 배열 뒤에서 같은 주파수·방향 순서의 Phase2D 배열을 읽는다. `READ(1,*,END=110)(Phase2D(J,I),J=1,NumFreq)`는 EOF이면 110 표제로 이동한다. 2.1 매뉴얼 p.37의 per·amp·pha 3열 형식은 별도 입력이다. [10-18 결론 검증 보완] |
| gpu-vs-tvd:FG1-139 | wavemaker.F / WAVEMAKER_INITIALIZATION | — | `FUNWAVE-GPU/src/wavemaker.F:55` `SUBROUTINE WAVEMAKER_INITIALIZATION`; `FUNWAVE-TVD/src/wavemaker.F:55` `SUBROUTINE WAVEMAKER_INITIALIZATION`; 변경 이력 334bb51 2019-12-06, 746ffdf 2021-11-01<br>`FUNWAVE-TVD/src/wavemaker.F:214` `READ(1,*,END=110)(Phase2D(J,I),J=1,NumFreq)`<br>`FUNWAVE-TVD/src/wavemaker.F:220` `if(myid.eq.0)then` [문맥: `# if defined (PARALLEL)`]<br>`FUNWAVE-TVD/src/wavemaker.F:295` `IF(INPUT_WAVE_PHASE)THEN`<br>`FUNWAVE-TVD/src/wavemaker.F:299` `Phase2D(J,I)=Phase2D(J,I)*0.005555555555556*pi` | A | 현재 TVD의 WAVEMAKER_INITIALIZATION은 스펙트럼 파일의 Phase2D 입력과 새 조파 초기화를 추가한다. `IF(INPUT_WAVE_PHASE)THEN`에서 `Phase2D(J,I)=Phase2D(J,I)*0.005555555555556*pi`로 입력 위상을 변환한다. [10-18 결론 검증 보완]<br>git 판정: `334bb51 2019-12-06`; `746ffdf 2021-11-01`. |
| gpu-vs-tvd:FG1-432 | 자료형 2D 내부 조파 식 | — | `FUNWAVE-GPU/src/moment_gpu.F:2278` `WK_Source=WK_Source+TANH(PI/(Time_ramp/FreqPeak)*TIME)*(Cm_d(I,J,kf) &`<br>`*COS(OMGN2D_d(KF)*TIME) &`<br>`+Sm_d(I,J,kf)*SIN(OMGN2D_d(KF)*TIME))`<br>`ENDDO`<br>`WaveMaker_Mass_d(I,J)=WK_Source`;<br>`e42e17d:src/sources.F:138–142` `WK_Source=WK_Source+TANH(PI/(Time_ramp/FreqPeak)*TIME)*(Cm(I,J,kf) &`<br>`*COS(OMGN2D(KF)*TIME) &`<br>`+Sm(I,J,kf)*SIN(OMGN2D(KF)*TIME))`<br>`ENDDO`<br>`WaveMaker_Mass(I,J)=WK_Source`. 현재 TVD는 이 조각을 변경했다. 현재 대응식은 `FUNWAVE-TVD/src/sources.F:150–163`에 있다. | F | 식 자체는 같다. WK_DATA2D의 정수 선택 누락은 FG1-605다. [10-18 전수 검증 보완] |
| gpu-vs-tvd:FG1-885 | missing part 변경 이력 주석 | — | `FUNWAVE-GPU/src/wavemaker.F:651` `Cm(i,j,kf)=Cm(i,j,kf) &`<br>`!             +D_gen(kf,ktheta)*exp(-beta_gen(kf)*((I-Ibeg +npx*Mglob/px)*DX-Xc)**2) &`<br>`!ykchoi Jan/23/2018`<br>`+D_gen(kf,ktheta)*exp(-beta_gen(kf)*((I-Ibeg + (iista-1) )*DX-Xc)**2) &`<br>`*cos(rlamda(kf,ktheta) &`<br>`![ykchoi Jan/23/2018 --- missing part`<br>`!          *((J-Jbeg  +npy*Nglob/py)*DY-ZERO)+phi1(kf,ktheta))`<br>`*((J-Jbeg  +(jjsta - 1) )*DY-ZERO)+phi1(kf,ktheta))`<br>`!ykchoi Jan/23/2018] --- missing part`<br>`FUNWAVE-TVD/src/wavemaker.F:855` `Cm(i,j,kf)=Cm(i,j,kf) &`<br>`!             +D_gen(kf,ktheta)*exp(-beta_gen(kf)*((I-Ibeg +npx*Mglob/px)*DX-Xc)**2) &`<br>`!ykchoi Jan/23/2018`<br>`+D_gen(kf,ktheta)*exp(-beta_gen(kf)*((I-Ibeg + (iista-1) )*DX-Xc)**2) &`<br>`*cos(rlamda(kf,ktheta) &`<br>`![ykchoi Jan/23/2018 --- missing part`<br>`!          *((J-Jbeg  +npy*Nglob/py)*DY-ZERO)+phi1(kf,ktheta))`<br>`*((J-Jbeg  +(jjsta - 1) )*DY-ZERO)+phi1(kf,ktheta))`<br>`!ykchoi Jan/23/2018] --- missing part` | F | missing part 주석 사이의 위상 계산은 활성 코드다. 현재 TVD의 같은 Cm 누적식과 일치한다. 이 행의 F는 해당 국소식의 대응이다. [10-18 결론 검증 정정] [10-18 결론 검증 보완] |
