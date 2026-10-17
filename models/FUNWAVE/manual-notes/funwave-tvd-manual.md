---
title: "FUNWAVE-TVD User's Manual (v3.0, 2016) 발췌"
model: FUNWAVE
citation_status: verified
verification_method: "doc/funwave_tvd_3.0.pdf → raw/manuals/funwave_tvd_3.0.md (opendataloader-pdf 변환) 직접 인용. 2026-06-13. 2026-10-18 FUNWAVE recovery 대조 보고서 반영"
last_source_check: "2026-10-18 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-13
source_scope: FUNWAVE-TVD
---

# FUNWAVE-TVD User's Manual (v3.0) 발췌

> 출처: `doc/funwave_tvd_3.0.pdf` (Release Dec 2016) → `raw/manuals/funwave_tvd_3.0.md`(변환본, gitignore). 원 개발 Kirby et al. 1998.

## 1. Abstract (verbatim 요지)

완전비선형 Boussinesq(FUNWAVE, Kirby 1998 시초)의 신버전. 개선점:
1. **더 완전한 fully nonlinear Boussinesq 방정식 set**
2. **MUSCL-TVD solver + adaptive Runge-Kutta** time stepping
3. **viscosity 쇄파 + shock-capturing 쇄파** 둘 다
4. **wetting-drying** moving boundary (HLL 결합)
5. **parallel** computation 옵션

도출: conservation form 이론식 + 압력경사항 재배열(numerically **well-balanced**) + 수치scheme + 예제. 참조: Shi et al. 2012a(Cartesian) / Kirby et al. 2012(spherical).

## 2. 매뉴얼 구성 (TOC)

- §2 이론: 2.3 Cartesian conservative fully nonlinear Boussinesq / 2.4 spherical weakly nonlinear
- §3 수치: 3.6.1 Sponge layer / 3.7 Wavemaker(3.7.1 internal wavemaker theory)
- 예제 + benchmark

## 3. 버전 이력 (1.0→3.0)

- 1.0→1.1: grid nesting, wind effect, spherical 조파, 시간평균 properties
- 1.1→2.0에서 구면 모드에 기준높이 유속을 쓰는 약비선형 Boussinesq 정식화를 구현했다. 매뉴얼의 인용은 Kirby 등 (2012)이다. `-DZALPHA`는 구면 기준높이 유속 선택이다. PHI_COLL과 CAL_DISPERSION에서는 중첩 경계의 분산항 경계조건을 제거했다. GET_Eta_U_V_HU_HV의 삼중대각 풀이에는 중첩 경계조건을 추가했다. 근거: `funwave_tvd_3.0.pdf p.9`, `FUNWAVE-TVD/src/init.F:665–680`, `FUNWAVE-TVD/src/bc.F:1031–1050`, `FUNWAVE-TVD/src/dispersion.F:189–211`, `FUNWAVE-TVD/src/etauv_solver.F:424–434`, [v21-manual §4 FV1-550](../../../_staging/recovery/compare/funwave-v21-manual-vs-code.md#4-노트-대조와-수정안). [10-18 대조 정정] [10-18 전수 검증 정정]
- 2.0→2.1: **공간변화 friction**(friction matrix·Manning), 출력 효율
- 2.1→2.2: **sponge layer 개선** — LD-type가 TVD와 결합 시 2dx sawtooth noise 장기누적 → **friction-type·viscous-type sponge 추가**

## 4. 본 위키 연결

- 소스 구조: [`../source-analysis/funwave-source-map.md`](../source-analysis/funwave-source-map.md)
- 빌드(`-DZALPHA` 등 FLAG): [`../source-analysis/funwave-build-and-blackwell-port.md`](../source-analysis/funwave-build-and-blackwell-port.md)
- 입력(격자·수심·wavemaker): §3.7 wavemaker theory ↔ WK_IRR/WK_DATA2D ([`source-map`](../source-analysis/funwave-source-map.md) §3)

## 문서와 코드 차이 (10-18 대조)

문서 판: FUNWAVE-TVD 3.0 문서 "Release Dec 2016"(공개 저장소 PDF 마지막 변경 `fef45a7`, 2018-02-24), 2.1 매뉴얼 `b9c035d`(2016-11-03). 코드 판: 공개 저장소 `github.com/fengyanshi/FUNWAVE-TVD` HEAD `b4c322e`(2025-01-24), `FUNWAVE-TVD/src/main.F:47` `!    VERSION 3.0`.

근거 보고서는 [v21-manual §4·5](../../../_staging/recovery/compare/funwave-v21-manual-vs-code.md#4-노트-대조와-수정안)다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| v21-manual:FV1-151 | GET_Eta_U_V_HU_HV | `funwave_tvd_2.1_manual.pdf` p.29: “GET_Eta_U_V_HU_HV ... Froude number cap ... TRIG ... TRIG_PERIODIC ... TRIDx and TRIDy.” | `FUNWAVE-TVD/src/etauv_solver.F:365` `SUBROUTINE GET_Eta_U_V_HU_HV`; `FUNWAVE-TVD/src/etauv_solver.F:468` `call TRIDx_ser(myA,myC,myD,myF)`; `FUNWAVE-TVD/src/etauv_solver.F:545` `CALL TRIDy_periodic (myA,myC,myD,myF)`; [git 이력 판정](../../../_staging/recovery/compare/FUNWAVE-git-verify-AD2.md), `2e72b18:etauv_solver.F:358` `call TRIDx_ser(myA,myC,myD,myF)` | B | 해당 이름과 유속 상한 처리는 존재한다. 직렬 호출은 `TRIDx_ser,TRIDy_ser`다. 주기 호출은 `TRIDy_periodic`이다. 병렬 비주기 호출은 `TRIDx,TRIDy`다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
| v21-manual:FV1-550 | 노트 manual-notes/funwave-tvd-manual.md:35 | `models/FUNWAVE/manual-notes/funwave-tvd-manual.md:35` `` - 1.1→2.0: spherical 더 완전한 Boussinesq(Kirby 2012, weakly nonlinear, zα 기준). **`-DZALPHA`** 옵션(nesting scheme 개선: PHI_COLL·CAL_DISPERSION·GET_Eta_U_V tridiagonal BC) `` | `models/FUNWAVE/manual-notes/funwave-tvd-manual.md:35`의 원문은 §4 FV1-550에 인용했다. 현재 근거: `FUNWAVE-TVD/src/etauv_solver.F:365` `SUBROUTINE GET_Eta_U_V_HU_HV`; `FUNWAVE-TVD/src/etauv_solver.F:468` `call TRIDx_ser(myA,myC,myD,myF)`; `FUNWAVE-TVD/src/etauv_solver.F:545` `CALL TRIDy_periodic (myA,myC,myD,myF)`; [git 이력 판정](../../../_staging/recovery/compare/FUNWAVE-git-verify-AD2.md), `2e72b18:etauv_solver.F:358` `call TRIDx_ser(myA,myC,myD,myF)` | B | 호출 이름을 GET_Eta_U_V_HU_HV로 적는다. ZALPHA의 구면 기준높이 유속 선택과 중첩 경계 보정을 별도 사실로 적는다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
