---
title: "CADMAS 매뉴얼 카탈로그 — 튜토리얼·일문중복·STOC-CADMAS 連成·STR(CADMAS) 결합층·Pre/post 매뉴얼 (26 PDF 전수 인벤토리)"
model: CADMAS-SURF
component: manual-notes
canonical_source: self
has_source_needed: true
verification_method: "Multiscale-...-Tsunami/ 전 PDF 26종 인벤토리(find+pdfinfo). 심층노트 4종(SURF3D 영문·2F 영문·STR 영문·AGENT 영문) 외 잔여 카탈로그. 특성화 read: STOC-CADMAS_Manual_Japanese.pdf:1-2(STOC↔CADMAS 連成계산 절차, MESH-MULTI/MESH 입력)·Program Instructions(CADMAS)_English.pdf:1(CADMAS-STR Coupled Analysis = sf_* 결합층 변수/서브루틴 SF_STRUCT.h ICPL)·View3DKai Manual_English.pdf:1(중앙대 해안·항만연구실 GUI). STOC 일문 자료 PDF p.1–9의 대조 보고서 반영. 튜토리얼 입력 키워드·파일명·셀 값을 모델 입력 대조의 근거로 사용.; 2026-11-04 CADMAS-SURF recovery 대조 보고서 반영"
citation_status: verified
last_source_check: "2026-11-04 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-24
related:
  - models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md
  - models/CADMAS-SURF/manual-notes/cadmas-2f-manual-compressibility.md
  - models/CADMAS-SURF/manual-notes/cadmas-str-manual-fem-theory-input.md
  - models/CADMAS-SURF/manual-notes/cadmas-agent-manual.md
  - models/CADMAS-SURF/source-analysis/cadmas-2f-structure-coupling-cutcell.md
---

# CADMAS 매뉴얼 카탈로그 (26 PDF 전수)

> repo 의 전 매뉴얼 26 PDF 인벤토리. **심층노트 4종**(아래) 외 잔여를 카탈로그. 경로 루트: `raw/.../Multiscale-...-Tsunami/`.

## 심층 노트 (별도 작성)
| 매뉴얼 | p | 노트 |
|---|--:|---|
| CADMAS-SURF3D_Manural_English | 150 | [governing-equations](cadmas-surf3d-english-manual-governing-equations.md) |
| CADMAS-2F_Manural_English | 160 | [2f-manual-compressibility](cadmas-2f-manual-compressibility.md) |
| CADMAS-STR Manual+Program Instructions_English | 18+113 | [str-manual-fem-theory-input](cadmas-str-manual-fem-theory-input.md) |
| CADMAS-AGENT_Manual_English | 30 | [agent-manual](cadmas-agent-manual.md) |

## A. STOC-CADMAS 連成 (일문 9p) — STOC↔CADMAS 결합 유일 문서

`STOC-CADMAS_Manual_Japanese.pdf`는 9쪽의 연성 계산 자료다. p.4는 광역·국소 영역의 시스템 구성 그림이다. p.5–7은 전처리기 절차다. data.env는 첫 줄에 영역 수 1을 쓰고 다음 줄에 `'a08_cad' 64 -1`을 쓴다. 자료의 표지는 판 번호와 날짜를 표시하지 않는다([KU1-060·065–068·076 최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KU1.md)). [11-04 대조 정정]

## B. STR(CADMAS) Coupled Analysis (영문 23p / 일문 25p) — sf_* 결합층 문서

`Simulators/STR3D/Manual/CADMAS-STR_Program Instructions(CADMAS)_{English,Japanese}.pdf`. *"CADMAS-STR Coupled Analysis Section Program Description — variables and subroutines added to CADMAS in order to add coupled analysis with STR"*(En p.1). `SF_STRUCT.h`/`SF_STRUCT` COMMON·`ICPL` 등 = **소스 [sf_* 구조결합 엔진](../source-analysis/cadmas-2f-structure-coupling-cutcell.md)의 매뉴얼측 문서**(2F 본매뉴얼엔 부재였던 sf_* 가 여기 문서화). CADMAS측에 추가된 결합 변수/서브루틴 설명. 심층 cross-confirm 가치 있으나 본 카탈로그선 식별만.

## C. 튜토리얼 (절차, 6 PDF)

| 튜토리얼 | p | 내용 |
|---|--:|---|
| CADMAS-SURF3D_Tutorial En/Ja | 13/12 | SURF/3D 실행 절차 예제 |
| CADMAS-2F_Tutorial En/Ja | 13/12 | 2F 실행 절차 예제 |
| AGENT_Tutorial En/Ja | 21/25 | AGENT 피난 실행 예제 |

튜토리얼의 입력 키워드·파일명·셀 값은 모델 입력 대조의 근거로 사용한다([KA1-519 최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KA1.md)). 전처리기·시각화 절차는 H로 구분한다([KU1-013·017·024·033 수정안](../../../_staging/recovery/compare/cadmas-tutorials-build-vs-code.md)). [11-04 대조 정정]

## D. 일문 중복 (영문 심층노트의 번역본, 5 PDF)

`CADMAS-SURF3D_Manual_Japanese`(142)·`CADMAS-2F_Manual_Japanese`(147)·`CADMAS-STR_Manual_Japanese`(18)·`CADMAS-STR_Program Instructions_Japanese`(117)·`CADMAS-AGENT_Manual_Japanese`(31). 영문 심층노트와 **동일 내용 일문본** → 별도 추출 불요(영문 노트가 canonical). 영문 미존재 항목 발생 시만 일문 참조.

## E. Pre/post 매뉴얼 (7 PDF) — 바이너리 3툴 + View3DKai

[Pre/post 4툴 소스노트](../source-analysis/cadmas-pre-post-processors.md)의 매뉴얼측(바이너리 3툴 내부=매뉴얼이 유일 출처):
| 매뉴얼 | p | 툴 |
|---|--:|---|
| CADMAS-MESH_Manual En/Ja | 47/47 | STL→공극/메시 전처리(CADMAS-SURF/3D·2F·STOC 입력) |
| CADMAS-MESH MULTI_Manual En/Ja | 54/47 | STOC 지형→영역분할 메시 |
| CADMAS-VR_Manual En/Ja | 97/98 | STOC/CADMAS/AGENT 결과 시각화 GUI |
| View3DKai Manual_English | 11 | ViewKai([GFCONV](../source-analysis/cadmas-pre-post-processors.md#4--viewkai--gfconv-병렬출력-변환기-유일-소스)) gather 출력 시각화 GUI (중앙대 해안·항만연구실) |

> 바이너리 3툴(MESH·MESH-MULTI·VR)의 입력카드/출력포맷은 **소스 부재 → 이 매뉴얼이 유일 출처**(source-needed 해소하려면 page 인용 필요). MESH 류는 공극엔진(잠재 substantial)이나 코드 미배포.

## 커버리지 종합

| 분류 | PDF 수 | 상태 |
|---|--:|---|
| 영문 기술매뉴얼 심층 | 5 | ✅ 노트 5(SURF3D·2F·STR 2·AGENT) |
| STOC-CADMAS 連成 | 1 | PDF p.1–9 대조 보고서 반영([KU1 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KU1.md)) | [11-04 대조 정정]
| STR(CADMAS) 결합층 | 2 | 🟡 식별(sf_* 매뉴얼측, 심층 후속가능) |
| 튜토리얼 | 6 | ✅ 카탈로그(절차) |
| 일문 중복 | 5 | ✅ 영문노트가 canonical |
| Pre/post | 7 | 🟡 바이너리툴 내부 source-needed |

PDF 인벤토리와 문서 항목의 코드 대조는 서로 다른 범위다([KU1-916 수정안](../../../_staging/recovery/compare/cadmas-tutorials-build-vs-code.md)). 튜토리얼 입력과 STOC 연성 자료의 대조 결과는 이 노트에 기록한다. [11-04 대조 정정]

문서와 코드 차이 표는 [cadmas-tutorials-build-differences.md](cadmas-tutorials-build-differences.md)에 있다.

## 문서와 코드 차이 (11-04 대조)

비교한 판: 코드는 github.com/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami `da7668f`(2024-08-30, 커밋 1개)의 Simulators/이며, 문서는 CADMAS-SURF3D_Tutorial_English 및 CADMAS-2F_Tutorial_English이다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| tutorials-build:KU1-013 | 밀도·동점성계수 입력 | `MATE DENSITY 1000.0`<br>`MATE K-VISC 1.0D-6`<br>`density of water`<br>`kinematic viscosity coefficient of water` | `3D2F/vf_iimate.f:36–61` `ELSEIF (TEXT(IS(2):IE(2)).EQ.'DENSITY') THEN`<br>`IF (NWD.LT.3) CALL VF_A2ERR('VF_IIMATE','SYNTAX ERROR.')`<br>`CALL VF_ZSTOR(RHO0(1),TEXT(IS(3):IE(3)))`<br>`IF (RHO0(1).LT.ZERO)`<br>`&              CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')`<br>`IF (NWD.LT.4) THEN`<br>`RHO0(2)=RHO0(1)`<br>`ELSE`<br>`CALL VF_ZSTOR(RHO0(2),TEXT(IS(4):IE(4)))`<br>`IF (RHO0(2).LT.ZERO)`<br>`&                CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')`<br>`ENDIF`<br><br>`CD    -- MATE K-VISCを解釈する --`<br>`ELSEIF (TEXT(IS(2):IE(2)).EQ.'K-VISC') THEN`<br>`IF (NWD.LT.3) CALL VF_A2ERR('VF_IIMATE','SYNTAX ERROR.')`<br>`CALL VF_ZSTOR(ANU0(1),TEXT(IS(3):IE(3)))`<br>`IF (ANU0(1).LT.0.0D0)`<br>`&              CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')`<br>`IF (NWD.LT.4) THEN`<br>`ANU0(2)=ANU0(1)`<br>`ELSE`<br>`CALL VF_ZSTOR(ANU0(2),TEXT(IS(4):IE(4)))`<br>`IF (ANU0(2).LT.0.0D0)`<br>`&                CALL VF_A2ERR('VF_IIMATE','INVALID VALUE.')`<br>`ENDIF`; `3D2F/vf_a2dflt.f:170–173` `RHO0(1)=1.0D+3`<br>`RHO0(2)=1.0D0`<br>`ANU0(1)=1.0D-6`<br>`ANU0(2)=1.5D-5` | C 문서 누락 | 3D2F에서 밀도·동점성계수를 한 값만 지정하면 두 상에 같은 값이 적용된다. 확인한 원문: 2F tutorial p.7; `3D2F/vf_iimate.f:36–61`; `3D2F/vf_a2dflt.f:170–173`. |
| tutorials-build:KU1-017 | 조파 함수 형식 | `MODEL WAVE-BC direction wave-making function` | `3D/vf_iimdl.f:50–52` `IF (NWD.LT.4) CALL VF_A2ERR('VF_IIMDL','SYNTAX ERROR.')`<br>`IF     (TEXT(IS(4):IE(4)).EQ.'FUNC'  ) THEN`<br>`IF     (TEXT(IS(5):IE(5)).EQ.'STREAM' ) THEN` | B 문서 오기 | 조파 함수 형식은 `MODEL WAVE-BC {DIR} FUNC {TYPE}`로 적는다. 확인한 원문: 3D·2F tutorial p.7; `3D/vf_iimdl.f:50–66`. |
| tutorials-build:KU1-024 | 경계 조건 형식 | `B.C. D Boundary conditions for flow velocity and pressure`<br>`B.C. D Boundary conditions for VOF function F` | `3D/vf_iiboun.f:142–149` `IP=IP+1`<br>`IF (NWD.LT.IP) CALL VF_A2ERR('VF_IIBOUN','SYNTAX.')`<br><br>`CD    -- 流速・圧力の境界条件 --`<br>`IF     (TEXT(IS(IP):IE(IP)).EQ.'VP') THEN`<br>`IP=IP+1`<br>`IF (NWD.LT.IP) CALL VF_A2ERR('VF_IIBOUN','SYNTAX.')`<br>`IF     (TEXT(IS(IP):IE(IP)).EQ.'SLIP') THEN`; `3D/vf_iiboun.f:220–222` `ELSEIF (TEXT(IS(IP):IE(IP)).EQ.'F') THEN`<br>`IP=IP+1`<br>`IF (NWD.LT.IP) CALL VF_A2ERR('VF_IIBOUN','SYNTAX ERROR.')` | B 문서 오기 | 기본 경계 형식은 `B.C. D VP {조건}`과 `B.C. D F {조건}`이다. 확인한 원문: 3D·2F tutorial p.8; `3D/vf_iiboun.f:142–150,220–232`. |
| tutorials-build:KU1-033 | 압력 시계열 참조 절 | `set in 5-8-(1)` | (코드 대조 없음, 문서 내 참조) 3D tutorial p.9; 2F tutorial p.9 제목 `4. Creating the ‘data.in’ file`, 세부 `8. Output file control settings`, `(ii)` time series | B 문서 오기 | 압력 시계열 입력의 참조를 4-8-(ii)로 정정한다. 확인한 원문: 3D·2F tutorial p.9,12. |

최종 근거는 [CADMAS-SURF-conclusion-verify-KU1.md](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KU1.md)이고 대조 보고서는 [cadmas-tutorials-build-vs-code.md](../../../_staging/recovery/compare/cadmas-tutorials-build-vs-code.md)이다.
