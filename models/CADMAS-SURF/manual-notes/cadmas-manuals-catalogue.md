---
title: "CADMAS 매뉴얼 카탈로그 — 튜토리얼·일문중복·STOC-CADMAS 連成·STR(CADMAS) 결합층·Pre/post 매뉴얼 (26 PDF 전수 인벤토리)"
model: CADMAS-SURF
component: manual-notes
canonical_source: self
has_source_needed: true
verification_method: "Multiscale-...-Tsunami/ 전 PDF 26종 인벤토리(find+pdfinfo). 심층노트 4종(SURF3D 영문·2F 영문·STR 영문·AGENT 영문) 외 잔여 카탈로그. 특성화 read: STOC-CADMAS_Manual_Japanese.pdf:1-2(STOC↔CADMAS 連成계산 절차, MESH-MULTI/MESH 입력)·Program Instructions(CADMAS)_English.pdf:1(CADMAS-STR Coupled Analysis = sf_* 결합층 변수/서브루틴 SF_STRUCT.h ICPL)·View3DKai Manual_English.pdf:1(중앙대 해안·항만연구실 GUI). 일문=영문 중복·튜토리얼=절차. 미번역 일문 상세=source-needed."
citation_status: verified
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

`Simulators/CADMAS-SURF-3D/Manual/STOC-CADMAS_Manual_Japanese.pdf`(9p). **STOC-CADMAS 連成계산 방법·절차 개요** — STOC(광역 정수압) ↔ CADMAS-SURF/3D(국소 VOF) 결합 워크플로. 입력파일은 CADMAS-MESH-MULTI(STOC격자) + CADMAS-MESH(CADMAS격자)로 작성. STOC단체·CADMAS단체 알고리즘은 개별자료 참조. → 소스 [STOC 결합](../source-analysis/cadmas-surf3d-timestep-nesting-stoc-coupling.md#c-stoc-결합-정수압-광역-stoc-mlic--cadmas-국소)의 매뉴얼측. ⚠ 일문만, 상세 절차 source-needed(번역 필요).

## B. STR(CADMAS) Coupled Analysis (영문 23p / 일문 25p) — sf_* 결합층 문서

`Simulators/STR3D/Manual/CADMAS-STR_Program Instructions(CADMAS)_{English,Japanese}.pdf`. *"CADMAS-STR Coupled Analysis Section Program Description — variables and subroutines added to CADMAS in order to add coupled analysis with STR"*(En p.1). `SF_STRUCT.h`/`SF_STRUCT` COMMON·`ICPL` 등 = **소스 [sf_* 구조결합 엔진](../source-analysis/cadmas-2f-structure-coupling-cutcell.md)의 매뉴얼측 문서**(2F 본매뉴얼엔 부재였던 sf_* 가 여기 문서화). CADMAS측에 추가된 결합 변수/서브루틴 설명. 심층 cross-confirm 가치 있으나 본 카탈로그선 식별만.

## C. 튜토리얼 (절차, 6 PDF)

| 튜토리얼 | p | 내용 |
|---|--:|---|
| CADMAS-SURF3D_Tutorial En/Ja | 13/12 | SURF/3D 실행 절차 예제 |
| CADMAS-2F_Tutorial En/Ja | 13/12 | 2F 실행 절차 예제 |
| AGENT_Tutorial En/Ja | 21/25 | AGENT 피난 실행 예제 |

입력파일 작성→실행→가시화 절차. canonical 메커닉 아님(절차 how-to). 케이스 구축 시 참조.

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
| STOC-CADMAS 連成 | 1 | 🟡 식별(일문 상세 source-needed) |
| STR(CADMAS) 결합층 | 2 | 🟡 식별(sf_* 매뉴얼측, 심층 후속가능) |
| 튜토리얼 | 6 | ✅ 카탈로그(절차) |
| 일문 중복 | 5 | ✅ 영문노트가 canonical |
| Pre/post | 7 | 🟡 바이너리툴 내부 source-needed |

> **26 PDF 전수 인벤토리 완료.** 영문 기술매뉴얼 = 소스 cross-confirm 심층. 잔여(일문상세·바이너리툴 내부·튜토리얼 절차)는 케이스·번역 필요 시 후속.
