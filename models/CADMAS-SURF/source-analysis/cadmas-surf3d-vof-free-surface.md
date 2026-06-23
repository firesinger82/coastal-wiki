---
title: "CADMAS-SURF/3D VOF 자유수면 — donor-acceptor(Hirt-Nichols)·NF 셀상태 머신·기포/물방울 (vf_f1cal·fconv·feuler·fnfini·fnfprv·fcut01)"
model: CADMAS-SURF
component: src (VOF free-surface tracking)
canonical_source: self
verification_method: "CADMAS-SURF/3D-MG 소스 직접 read (raw/.../CADMAS-SURF-3D/Source code/). vf_fconv.f 헤더 'ドナーアクセプタ'(:6) + donor/acceptor 부호선택(:62-72)·Hirt-Nichols MIN(FVX,FVM) 클램프(:96-99) + vf_f1cal.f 드라이버 호출순서(:123-231) + vf_feuler.f 명시적 Euler 보존형(:48-52) + vf_fnfini.f NF분류 fluid/gas/잠정표면7(:5-6·36-194) + vf_fnfprv.f 표면방향 1-6 max-F(:67-217) + vf_fcut01.f [0,1]클리핑·FSUM/FCUT(:5·34-56) + vf_fconvs.f PLIC 경사보정(:8·44-49) + 기포 vf_fbubup.f/물방울 vf_fdropf.f TimerDoor법. file:line 직접 인용."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-23
related:
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-smac-velocity-pressure-solver.md
---

# CADMAS-SURF/3D VOF 자유수면 추적

> CADMAS 의 **정의적 메커닉** — 자유수면을 **VOF(Volume Of Fluid)법**으로 추적. F함수(`FF`)=유체체적률, `NF`=셀상태 인덱스. 스킴은 **donor-acceptor(Hirt-Nichols 계열)**, 명시적 Euler 보존형 이류, 경사 자유수면에 한해 PLIC 재구성 옵션. 드라이버 `VF_F1CAL`(`vf_a1main.f:1104`). 경로 루트 → [architecture-source-map](cadmas-surf3d-architecture-source-map.md).

## 1. 스킴 판정 — donor-acceptor (Hirt-Nichols), PLIC 아님(기본)

기본 이류 루틴 헤더가 명시: `vf_fconv.f:6` — `VF_FCONV:VOF関数Fの移流項によるフラックスの計算(ドナーアクセプタ)`. 변형 루틴도 type0=donor-acceptor 확인: `vf_fconvs.f:45` `= 0:斜面無し(ドナーアクセプタ使用)`. **기본 경로는 geometric VOF-PLIC 가 아니라 donor-acceptor**.

## 2. F 드라이버 파이프라인 (vf_f1cal.f)

헤더 `VF_F1CAL:VOF関数Fの計算およびNFの設定`(`vf_f1cal.f:17`). 순서:
1. 면플럭스 `FLFU/V/W`·소스 `QF` 영초기화 (`vf_f1cal.f:123-134`)
2. **이류 플럭스**: `ISCMFF=0`→`VF_FCONV`(donor-acceptor, `:139-140`), `≠0`→`VF_FCONVS`(경사보정, `:142-145`) — 분기 `vf_f1cal.f:138`
3. 소스 `VF_FGENE`(造波 등, `:155`)
4. **시간적분** `VF_FEULER`(`:160`/`:162`)
5. 해저변형 보정 `VF_FSEABT`(`ISEABT`, `:166-168`)
6. 표면셀 보정 `VF_FMOD1`(`:185`)
7. **클리핑+공간적분** `VF_FCUT01`(`:188`)
8. NF 직전값 저장(`:197-203`) → **NF 재구성** `VF_FNFINI`(`:207`), 기포 `VF_FBUBUP`(`:208-211`), 물방울 `VF_FDROPF`(`:212-217`), 표면방향 `VF_FNFPRV`(`:218`)
9. 기체→유체 전환셀 압력 핸드오프(`:223-231`)

## 3. donor-acceptor 이류 커널 (vf_fconv.f)

x/y/z 동일구조(x블록 `:55-104`). x면 기준:
- 면 Courant 플럭스 `C=DTNOW*GGX*UU`, `AC=ABS(C)` (`vf_fconv.f:60-61`)
- **donor/acceptor 부호선택**: `C≥0`→`LA=I, LD=I-1`; else `LA=I-1, LD=I` (`vf_fconv.f:62-72`). `LD`=donor(풍상), `LA`=acceptor
- donor F `FD=FF(LD)`, acceptor F `FA=FF(LA)`
- 표면방향 스위치: donor 의 NF 법선이 면에 횡이면 `FAD←FD`(평행계면은 donor 값 이류, `vf_fconv.f:89-93`)
- **Hirt-Nichols 경계 플럭스**: `CFX=MAX((FDM-FAD)*AC-(FDM-FD)*V,0)`, `FVX=FAD*AC+CFX`, `FVM=FD*V`, 플럭스=**둘의 최소** `MIN(FVX,FVM)` (`vf_fconv.f:96-99`) — donor 가용유체 `FD*V` 로 캡(overfill 방지, donor-acceptor 의 정의적 클램프). 캡 발동 시 `NLIM(LD)=1`(`:100`)

## 4. 명시적 Euler 보존형 이류 (vf_feuler.f)

헤더 `VF_FEULER:VOF関数Fの時間積分を計算(Euler法)`(`vf_feuler.f:6`). 비장애물셀(`NF≠-1`)에서:
```
DF = Δx⁻¹(FLFU(I+1)-FLFU(I)) + Δy⁻¹(FLFV(J+1)-FLFV(J)) + Δz⁻¹(FLFW(K+1)-FLFW(K)) + DTNOW*QF
FF = (G0*FF + DF) / GGV
```
(`vf_feuler.f:48-52`). 보존성은 공유 면플럭스(셀 I 의 I+1면 유출 = I+1 의 유입)에 기반. `G0`=시간의존 공극(`GGV/GGV0`).

## 5. NF 셀상태 머신 (vf_fnfini.f + vf_fnfprv.f)

**1단계 분류** `VF_FNFINI`(헤더 `:5-6` `NFを流体セル、気体セルおよび表面セルに分類 / 表面セルは暫定的に7`):
- 비장애물셀 유체 `NF=0` 리셋(`:36-42`)
- `F<FLOWER` & 6면 모두 full-fluid 이웃 없음 → **기체 `NF=8`**(`:48-99`)
- 기체 인접 비기체셀 → **잠정 표면셀 `NF=7`**(반복, `INDS` 푸시, `:108-194`)

**2단계 방향결정** `VF_FNFPRV`(헤더 `:5-6` `表面セルの向きを暫定NFにより決定`): 잠정표면셀(`NF=7`)마다 6방향 중 "유체측 & 반대편 기체측" 후보를 가중 F합 `FS` 로 점수화, **최대 F 방향**의 NF 코드 부여 — z-→`5`(`:67`), z+→`6`(`:97`), y-→`3`(`:127`), y+→`4`(`:157`), x-→`1`(`:187`), x+→`2`(`:217`). [데이터모델 NF=1~6 범례](cadmas-surf3d-architecture-source-map.md#3-데이터모델-vf_a1mainf38-218-변수사전)와 정확히 일치.

## 6. 경계·보존 — 클리핑과 진단 (vf_fcut01.f)

헤더 `VF_FCUT01:VOF関数Fのカットオフ(0.0=<F=<1.0)と空間積分の計算`(`vf_fcut01.f:5`). 셀체적 `V=Δx·Δy·Δz·GGV`(`:40`):
- `F>FUPPER`: `FCUT += (F-1)*V`, **F=1 클램프**(`:41-43`)
- `F<FLOWER`: `FCUT += (F-0)*V`, **F=0 클램프**(`:44-46`)
- `FSUM += F*V`(클리핑 후, `:48`), 둘 다 MPI reduce(`VF_P1SUMD`, `:53-56`)

> **FCUT** = [0,1] 클리핑이 주입/제거한 유체체적(보존오차 모니터), **FSUM** = 전유체체적. 메인루프 스텝출력(`vf_a1main.f:956`)이 소비. 1차 boundedness 는 donor-acceptor `MIN` 플럭스, FCUT01 은 잔차 안전클립.

## 7. 경사 자유수면 PLIC 옵션 (vf_fconvs.f)

`ISCMFF≠0` 시 선택. 헤더 `VOF関数Fの移流項…(傾斜を考慮)`(`vf_fconvs.f:8`). 중심차분으로 계면 **법선벡터** `(S1,S2,S3)` 산출·정규화(`:168-173·342-347`), 경사 type `ISTYP`(`:351-359`, 범례 `:44-49`)면 **piecewise-linear 평면**(Youngs형) 재구성(`VF_FSLP2A/3A`·`FSLP2F/3F`, `:362-470`). 비경사면은 vf_fconv 와 **동일 donor-acceptor 커널**로 fallback(`MIN(FVX,FVM)` `:444·524·604`). 즉 순수 geometric VOF 가 아니라 **donor-acceptor + 경사면 PLIC bolt-on**.

## 8. 기포·물방울 서브모델 (TimerDoor법)

쇄파 시 공기연행·비말 처리. 둘 다 플럭스가 아닌 **타이머 게이트 매개적 체적교환**:
- **기포 상승** `VF_FBUBUP`(헤더 `TimerDoor法による気泡の上昇` `vf_fbubup.f:5`): 상승간격 `DTBUB=Δz/WBUB`(`:36`) 경과 시 상부셀→부분유체셀로 하향 이동 `FMOVE=MIN((1-F)·V0, F(K1)·V1)`(`:45-47`) — 동일체적 교환=보존
- **물방울 자유낙하** `VF_FDROPF`(헤더 `TimerDoor法による水滴の自由落下と流れ落ち` `vf_fdropf.f:7`): 기체셀 내 고립수(`F>FLOWER & NF=8`)에 이웃유체평균 속도 부여(`:70-245`), X/Y/Z 3 스윕(`:304-644`), Z 스윕은 운동학 낙하시간 `X=√(2·GRZ0·Δz)`·중력가속 `DROPWW-Δt·GRZ0`(`:554·589-605`). 각 이동 `FMOVE=MIN(...)` 체적보존.
