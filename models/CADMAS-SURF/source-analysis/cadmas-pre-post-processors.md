---
title: "CADMAS Pre/Post 4툴 — ViewKai(GFCONV 병렬출력 변환기, 소스) + CADMAS-MESH·MESH-MULTI·VR(바이너리 전용, 매뉴얼 출처)"
model: CADMAS-SURF
component: src (pre/post processors)
canonical_source: self
has_source_needed: true
verification_method: "Pre and post-processors/ 전수 조사 (raw/.../Pre and post-processors/). ViewKai/Source code/ 9 Fortran77 직접 read: gf_a1main.f:5·80(CADMAS-SURF/3D-MP 병렬 그래픽 변환)·gf_a2init.f:25-34(per-rank UNFORMATTED→data.grp)·gf_vald.f:32-49(staggered 격자 gather)·GF_CONV.h:2-13. MESH/MESH-MULTI/VR = ReadMe.md:2 purpose 직접 인용(바이너리 .exe만, 소스 부재 → 내부 카드/포맷 source-needed). file:line/ReadMe 인용. G9e disclosed-gap: 바이너리 3툴 내부 = source-needed(매뉴얼 PDF 필요)."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-24
related:
  - models/CADMAS-SURF/source-analysis/cadmas-2f-structure-coupling-cutcell.md
  - models/CADMAS-SURF/README.md
---

# CADMAS Pre/Post 4툴

> repo 의 전·후처리 4툴. **3개(MESH·MESH-MULTI·VR)는 Windows 바이너리(.exe)만 배포** — 소스 미포함, 정체는 `ReadMe.md`로 확인하되 내부 카드/포맷은 `source-needed`(매뉴얼 PDF 필요). **ViewKai만 소스(~700줄 Fortran77)** — 실은 렌더러가 아니라 병렬출력 gather 변환기. 경로 루트: `raw/.../Pre and post-processors/`.

## 1. CADMAS-MESH — STL→메시/공극 전처리 (바이너리)

`CADMAS-MESH/ReadMe.md:2`: *"reads obstacle data from STL data, performs porous calculation and mesh generation"* — STL 구조물 → **공극(porous) 계산 + 메시 생성** → CADMAS-SURF/3D·3D2F·STOC 입력. 배포 = `Installer/CADMAS-MESH_setup.exe`(52MB NSIS), 매뉴얼 영/일 PDF. **소스 부재** → 입력카드·공극알고리즘은 source-needed(매뉴얼). 개념상 solver `sf_mdporo`([cut-cell 공극](cadmas-2f-structure-coupling-cutcell.md))과 같은 γ/공극 엔진이나 코드 대조 불가.

## 2. CADMAS-MESH-MULTI — STOC 지형/영역 메시 전처리 (바이너리)

`CADMAS-MESH-MULTI/ReadMe.md:2`: *"[STOC] input data creation … reads topographic data, divides it into regions, and generates meshes"* — **지형 → 영역분할(nested) → STOC-ML/IC 격자**. 지형포맷: GEBCO·GTOPO30·ETOPO1/2·J-EGG500·X,Y(`ReadMe.md:4-11`). 배포 = `CADMAS-MESH-MULTI-x64-setup.exe`(25MB). 소스 부재 → source-needed.

## 3. CADMAS-VR — STOC/CADMAS/AGENT 결과 시각화 (바이너리)

`CADMAS-VR/ReadMe.md:2`: *"visualizing output data from [STOC], [CADMAS-SURF/3D], [CADMAS-SURF/3D2F], and [AGENT]"* — 4 시뮬레이터 출력 GUI 시각화. 배포 = `CadmasVR_Setup.exe`(27MB PE32 GUI). 출력 그래픽 포맷(VTK/EnSight/독자) 불명 → source-needed(매뉴얼).

## 4. ★ ViewKai — GFCONV 병렬출력 변환기 (유일 소스)

`ViewKai/Source code/` = **9 Fortran77 + 헤더 + Makefile, 766줄**. ⚠️ ReadMe는 "visualizing tool"이라 하나 실제 소스는 **렌더러가 아니라 `GFCONV` = CADMAS-SURF/3D-MP(다중프로세스) 병렬 그래픽출력을 단일 직렬파일로 gather 변환**(실제 GUI View3DKai는 repo 부재, 매뉴얼만).

- 헤더 `gf_a1main.f:5`: `GF_A1MAIN:CADMAS-SURF/3D-MPの並列用グラフィックデータを変換する`, 배너 `:80 ##### CADMAS-SURF/3D-MP GF_CONV START`
- 제어흐름(`gf_a1main.f:31-64`): `GF_A2INIT`(전 rank 헤더)→전역배열 `XX/YY/ZZ/VAL/IVAL` 할당(`:48-52`)→`GF_A3GRID`(격자조립)→`GF_A4TRAN`(스텝별 gather, EOF까지)
- **IO 포맷**(load-bearing): 입력=per-rank Fortran `UNFORMATTED`(`OPEN(...FORM='UNFORMATTED')`, 5자리 rank명 `data.grp00000...`, `gf_a2init.f:25-34`·`gf_vald.f:28-30`), 출력=단일 `data.grp`(`STATUS='NEW'`, 마지막 rank, `gf_a2init.f:33`). **VTK/EnSight 아닌 독자 CADMAS 바이너리 레코드**
- gather 변환(`gf_vald.f:32-49`): rank 로컬블록을 분해인덱스(`MYIS/MYIE/MYGIS`)로 전역배열 매핑, `ISW=0/1/2/3`로 **staggered(MAC) 격자** cell/face 구분. 필드: NF(int `GF_VALI`)·U/V/W(staggered)·P/F/k 등(cell `GF_VALD`)
- 공유: solver의 병렬출력 레코드 레이아웃+분해 인덱스 관례(`GF_CONV.h:2-13·44-60`) = solver 병렬 그래픽 writer의 역(inverse). 빌드 `mpif90`(`Makefile:13`, 직렬이나 solver 툴체인 공유)

> 결론: Pre/post 4툴 중 **ViewKai만 소스 검수 가능**(GFCONV 변환기, verified). MESH·MESH-MULTI·VR 은 바이너리 배포 → 정체는 ReadMe verified, **내부는 source-needed**(매뉴얼 PDF). MESH 류는 잠재적으로 substantial(공극엔진)이나 코드 부재로 감사 불가.
