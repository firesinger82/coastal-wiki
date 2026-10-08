---
title: "EFDC internal mode — CALUVW 전단(shear) 연직 implicit 솔버 (완전 implicit tridiag + Sherman-Morrison)"
topic: general
canonical_source: self
citation_status: verified
has_source_needed: false
verification_method: "caluvw.f90(1429줄)·calexp.f90(전단 RHS :1355-1400)·aaefdc.f90(CDZ 계수 :2462-2504)·hdmt.f90/hdmt2t.f90(호출부)·GOTM_Turbulence/mod_gotm.f90(364줄, 결합 인터페이스) 직접 read (2026-07-11, EFDC+ 12.4 sha 3ed76b6). 모든 식·라인 verbatim 인용."
note_author: "Claude Fable 5 (source-code direct read)"
note_date: 2026-07-11
related:
  - models/EFDC/source-analysis/efdc_hydro_core.md
  - models/EFDC/source-analysis/efdc_vertical.md
  - models/EFDC/source-analysis/efdc_turbulence.md
  - models/EFDC/source-analysis/efdc_bottom_friction.md
  - concepts/currents/time-integration-cross-model.md
last_source_check: 2026-10-08 (recovery 재판독 대조)
---

# EFDC CALUVW — 내부모드 전단 연직 implicit 솔버

> [[efdc_hydro_core]] §C 가 CALUVW 의 barotropic 보정(3단계)을, [[efdc_vertical]] 이 W·층구조를 커버 — 본 노트는 그 사이의 **전단 방정식 연직 implicit 시간적분**([[time-integration-cross-model]] §5 가 지적한 미커버 갭)을 채운다. ADCIRC 의 대응물은 [[adcirc-3d-vssol-vertical-scheme]] (VSSOL).

## 1. 정체 — 속도가 아니라 "전단"을 푼다

- `CALUVW` = "Calculates internal solution at time level (N+1)" (caluvw.f90:9 헤더, Craig 2011 F90+OMP 재작성). 호출: HDMT(3TL, hdmt.f90:772/791)·HDMT2T(2TL, hdmt2t.f90:650/660) — external CALPUV 이후.
- **미지수 = 층간 전단 `DU/DV`** (layer interface 간 속도차의 flux 형, m²/s) — 속도 자체를 푸는 ADCIRC VSSOL 과 정식화가 다름. 깊이평균은 external 이 이미 확정 → 내부모드는 연직 구조(전단)만 담당, 마지막에 rank-one 제약으로 재결합(§4).

## 2. RHS 조립 (calexp.f90) — explicit 항의 층차

```fortran
DU(L,K) = CDZFU(L,K)*( H1U(L)*(U1(L,K+1)-U1(L,K))*DELTI
        + DXYIU(L)*(FCAX(L,K+1)-FCAX(L,K) + FBBX(L,K) + SNLT*(FX(L,K)-FX(L,K+1))) )
```
3TL 전단 우변은 이전 속도 U1과 H1U를 사용한다. (`calexp.f90:1309` — `DU(L,K) = CDZFU(L,K)*( H1U(L)*(U1(L,K+1)-U1(L,K))*DELTI + DXYIU(L)*(FCAX(L,K+1)-FCAX(L,K)   + FBBX(L,K) + SNLT*(FX(L,K)-FX(L,K+1))) )`) 2TL 전단 우변은 현재 저장 상태 U와 HU를 사용한다. (`calexp2t.f90:1395` — `DU(L,K) = CDZFU(L,K)*( HU(L)*( U(L,K+1)-U(L,K) )*DELTI + DXYIU(L)*( FCAX(L,K+1)-FCAX(L,K)   + FBBX(L,K) + SNLT*(FX(L,K)-FX(L,K+1)) ) )   ! *** M2/S2`)

- CALEXP의 바람 주입은 ISTL=2를 검사한다. (`calexp.f90:1318` — `if( (ISTL == 2 .and. NWSER > 0) .or. (ISTL == 2 .and. iGOTM_Test > 0 ) )then`) HDMT는 ISTL=3에서 CALTSXY(0)를 호출한다. (`calexp.f90:1318` — `if( (ISTL == 2 .and. NWSER > 0) .or. (ISTL == 2 .and. iGOTM_Test > 0 ) )then`; `hdmt.f90:749` — `call CALTSXY(0)`) 그 뒤 HDMT는 DU/DV에 TSX/TSY를 주입한다. (`calexp.f90:1326` — `DU(L,KS) = DU(L,KS) - CDZUU(L,KS)*TSX(L)`; `hdmt.f90:757` — `DU(L,KS) = DU(L,KS) - CDZUU(L,KS)*TSX(L)`; `hdmt.f90:758` — `DV(L,KS) = DV(L,KS) - CDZUV(L,KS)*TSY(L)`)
- 마스크 SUB/SVB 적용 (:1397-1398).

## 3. 연직 확산 — 완전 implicit tridiagonal (θ knob 없음)

CALUVW 의 전단 solve (caluvw.f90:392-462, SGZ-aware — 셀별 최하활성층 `KSZU/KSZV`):

- CALAVB의 해당 분기에서 AVUI=2/(AV(L,K)+AV(LWC(L),K))이다. (`calavb.f90:291` — `AVUI(L,K) = 2.0/( AV(L,K) + AV(LWC(L),K) )`; `caluvw.f90:406` — `CMU = 1.+RCDZM*HU(L)*AVUI(L,K)`) CALUVW는 이 면 계수를 전단 계의 대각에 사용한다. (`calavb.f90:291` — `AVUI(L,K) = 2.0/( AV(L,K) + AV(LWC(L),K) )`; `caluvw.f90:406` — `CMU = 1.+RCDZM*HU(L)*AVUI(L,K)`)
- **전진소거(Thomas, in-place)**: `EU = 1/(CMU − RCDZL·CU1(L,K-1))`, `CU1 = RCDZU·EU`, `DU = (DU − RCDZL·DU(k-1))·EU` (:407-409). 보조해 `UUU` 도 동시 소거 (:410, §4 용).
- **바닥 행(K=KSZU)**: RHS 에 저면항력 `− RCDZL·RCXX(L)·UHE(L)·HUI(L)` (:419), `UUU(KSZU)=EU` 시드 (:420).
- **후진대입**: `DU(K) -= CU1(K)·DU(K+1)` (:455-462, DU·DV·UUU·VVV 4계 동시).
- 저면항력 계수 `RCXX/RCYY` 3분기 (:305-346): 3TL(ISTL=3) `STBX·√(V1U²+U1²)` 전 스텝값 / corrector·2TL 기하평균 `STBX·√(Q1·Q2)`(old·new) / `AVCON1` 상수-AVO 모드 `AVCON1/√(H1U·HU)`. STBX 유도는 [[efdc_bottom_friction]].

## 4. ★Sherman-Morrison rank-one 보정 (:466-497)

저면항력 행이 전단계(全 K)와 결합하는 rank-one 구조를 Sherman-Morrison 으로 처리:

```fortran
CRU = CDZRU(L,K)*RCXX(L)*AVUI(L,K)
AAU(L) = Σ CRU·DU(L,K) ;  BBU(L) = 1 + Σ CRU·UUU(L,K)   ! :475-485
AAU(L) = AAU(L)/BBU(L)                                    ! :488
DU(L,K) = SUB3D·DZGU·HU·AVUI·( DU(L,K) − AAU(L)·UUU(L,K) ) ! :495 — 물리 전단 flux 로 변환
```

계수 테이블은 setup 에서 사전계산 (aaefdc.f90): `CDZLU = −SGZU(k+1)/(SGZU(k)+SGZU(k+1))` (:2462)·`CDZMU = 0.5·SGZU(k)·SGZU(k+1)` (:2504)·`CDZRU = CDZRU·DZGU·CDZLU(KSZU)` (:2503) — 층 지오메트리만의 함수(시불변, SGZ 셀별).

## 5. 속도 재구성과 후속 단계

1. 깊이평균 갱신: `UHE(L) += CDZDU(L,K)·DU(L,K)` (:517).
2. **top-down marching**: `UHDYF(L,KC) = UHE·SUB` (:525) → `UHDYF(L,K) = SUB3D·(UHDYF(L,K+1) − DU(L,K))` (:531) → `×DYU` 로 m³/s (:536-542).
3. blocked layer face 옵션(NBLOCKED, 수문·취수구 층 차단) 별도 재구성 (:551-).
4. CALUVW는 barotropic 보정과 W 연속식 계산을 수행한다. (`caluvw.f90:1302` — `if( ISINWV == 1 )then`; `caluvw.f90:1319` — `if( KC > 1 .and. ISPNHYDS >= 1 ) CALL CALPNHS`; `caluvw.f90:613` — `TVARE(L) = TVARE(L) - UHDYE(L)`; `caluvw.f90:733` — `W(L,K) = W(L,K-1) - 0.5*DXYIP(L)  &`) CALUVW는 Courant 진단 뒤 CALPNHS를 호출한다. (`caluvw.f90:1319` — `if( KC > 1 .and. ISPNHYDS >= 1 ) CALL CALPNHS`) CALPNHS 조건은 KC>1과 ISPNHYDS>=1이다. (`caluvw.f90:1319` — `if( KC > 1 .and. ISPNHYDS >= 1 ) CALL CALPNHS`)

## 6. GOTM 결합 (ISGOTM)

- `ISGOTM > 0` 시 `Advance_GOTM(ISTL)` 호출 (hdmt.f90:598 / hdmt2t.f90:537) — `GOTM_Turbulence/mod_gotm.f90`(364줄) 이 인터페이스: 수평 셀별 1D 컬럼으로 `do_turbulence` 호출, `tke/eps/Lgs`·표저면 응력 `GTAUS/GTAUB`·`z0s/z0b`·성층 `NN`·전단 `SS` 교환 (:286-295), 결과 eddy viscosity 가 `AVUI` 경유로 본 노트의 계에 유입.

Advance_GOTM은 앞쪽 계수 계산 분기에 있다. (`hdmt2t.f90:537` — `call Advance_GOTM(ISTL)`; `hdmt.f90:598` — `call Advance_GOTM(ISTL)`; `GOTM_Turbulence/mod_gotm.f90:292` — `call do_turbulence(IT, NLAYER, DELT, DEPTH, GTAUS, GTAUB, z0s_gotm, z0b_gotm, HPK1d, NN1d, SS1d)`) DO_TURBULENCE 내부는 확인하지 않음. (`GOTM_Turbulence/mod_gotm.f90:292` — `call do_turbulence(IT, NLAYER, DELT, DEPTH, GTAUS, GTAUB, z0s_gotm, z0b_gotm, HPK1d, NN1d, SS1d)`)

- **판정(2026-07-11)**: `GOTM_Turbulence/` 나머지 32파일 = **vendored 3rd-party GOTM 라이브러리**(gotm.net; cmue_*, tke 계열) — CADMAS 의 MUMPS·SWAN OCP 와 동급의 T티어 외부코드로 **위키 검수 범위 밖**. EFDC 자체 MY2.5 계열은 [[efdc_turbulence]] canonical.

## 7. ★Findings / 함정

- **θ knob 없음** — 연직확산 implicitness 는 사용자 조정 불가(항상 완전 implicit). fort.15 스타일 3-knob(ADCIRC Alp1/2/3)와 대비되는 설계.
- 3TL 일반 단계에도 HDMT가 새 바람을 내부 모드 DU/DV에 주입한다. (`hdmt.f90:757` — `DU(L,KS) = DU(L,KS) - CDZUU(L,KS)*TSX(L)`; `hdmt.f90:758` — `DV(L,KS) = DV(L,KS) - CDZUV(L,KS)*TSY(L)`) CALEXP2T 주입은 NWSER>0을 검사한다. (`calexp2t.f90:1401` — `if( NWSER > 0 )then`)
- **전단 정식화의 함의**: 내부모드가 깊이평균을 건드리지 않으므로 external↔internal 정합은 별도 barotropic 보정(hydro_core §C)이 담당 — 그 보정 없으면 mass drift.
- **Sherman-Morrison 보조해 UUU/VVV** — 디버깅 시 DU 배열이 소거 중간엔 미보정 상태임에 주의(:495 최종 변환 전후 단위·의미 다름: 소거계 무차원 → 물리 m²/s).
- **RCXX 의 시간분기** — 3TL full step 은 old 값(U1)만, corrector 는 old·new 기하평균: 같은 STBX 라도 스텝 종류별 유효 drag 상이.

CALUVW가 읽는 STBX/STBY는 앞 계산의 값이다. (`caluvw.f90:327` — `RCXX(L) = STBX(L)*SQRT(Q1*Q2)`)

- CFL 축적(:1302-)은 **진단 전용**(ISINWV=1) — EFDC 의 안정성은 external semi-implicit + internal 완전 implicit 이 담당, 이류 explicit 성분만 dt 제약.

## 연결

- [[efdc_hydro_core]] — external/internal 결합·3TL/2TL·barotropic 보정(§C)·CALPNHS(§F)
- [[efdc_vertical]] — 층구조(SGZ)·W 연속식
- [[efdc_turbulence]] — MY2.5 QQ/QQL(자체 난류), AV 공급원
- [[efdc_bottom_friction]] — STBX/STBY 유도(caltbxy)
- [[adcirc-3d-vssol-vertical-scheme]] — ADCIRC 대응물(속도 정식화·θ³·복소 tridiag) 대비
- [[time-integration-cross-model]] §4·§5 — 12모델 연직 implicit 대조
