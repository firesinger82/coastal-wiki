---
title: "CADMAS-SURF/3D 조파·경계 — 造波소스(Brorsen-Larsen형)·파이론(Stokes5/cnoidal3/stream-function B)·방사경계(Sommerfeld)·대수칙벽 (vf_cwmsrc·cwmak·bwuwn·bwuwt·cloglw·clogks)"
model: CADMAS-SURF
component: src (wave generation + boundary conditions)
canonical_source: self
verification_method: "CADMAS-SURF/3D-MG 소스 직접 read (raw/.../CADMAS-SURF-3D/Source code/). 造波소스 vf_cwmsrc.f(:7·142) + 주입 vf_bsuwn.f:89-120(factor-2 대칭면플럭스) + 파이론 IWVTYP vf_cwmak0.f:17-20(=-2 Stokes5·=-1 cnoidal3·>0 stream-function B·=-3/-4 외부테이블) + 구현 vf_wstk0.f/wcnd0.f/wsfmb2.f + 造波경계 IB=5 vf_bwuwn.f:160-480(사각입사) + 방사경계 Sommerfeld vf_bwuwn.f:483-619(ALN=MIN(C·Δt/Δx,1)) + 대수칙 vf_bwuwt.f:118-176→smooth vf_cloglw.f Newton(:6-7·43-44)/rough vf_clogks.f 폐형(:29-30). INDB코드 vf_a1main.f:159-168. file:line 직접 인용."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-23
related:
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-vof-free-surface.md
---

# CADMAS-SURF/3D 조파·경계조건

> CADMAS 의 입사파 생성(造波)과 개·방사·벽 경계처리. 조파는 **내부 造波소스법**(Brorsen-Larsen형)과 **유입 造波경계**(IB=5) 두 메커니즘, 파이론 4종(+외부테이블 2채널). 개경계는 **Sommerfeld 방사**, 벽은 **대수칙**(평활/완전조면). INDB 경계코드 → [architecture-source-map §3](cadmas-surf3d-architecture-source-map.md#3-데이터모델-vf_a1mainf38-218-변수사전). 경로 루트 동일.

## A. 조파 (造波) — 두 메커니즘

### A-1. 내부 造波소스법 (vf_cwmsrc.f → vf_bsuwn.f)

헤더 `VF_CWMSRC:造波ソースのための流速を計算する`(`vf_cwmsrc.f:7`), 출력 `SRCUV`(造波소스 속도, `:27`). 위상별 속도프로파일(`:78-83`)·ramp-up `AW`(`:84-89`)·연직스케일 `VWS=(WVZ+D)/(VAL+D)`(순간수주 정합, `:127`)→`SRCUV=UN·VWS·AW`(`:142`). 소스라인 방향은 `ISCTYP(1)` 부호(x선/y선, `:46-66`), 파타입 `N=ISCTYP(2)`(`:69`).

**실제 주입**은 `VF_BSUWN` 의 `CD -- 造波ソース --` 블록(`vf_bsuwn.f:89-120`): 소스라인 양측 면속도에 플럭스 `Q=2.0·Δx⁻¹·SRCUV`(`:98`) 추가, `UU(I+1)=UU(I+1)+Δx·Q/GGX(I+1)`(`:101`). **factor-2 대칭 면주입 + 내부 격자열** = 전형적 **내부 造波 source method(Brorsen-Larsen / source-function형)** — 경계 유입이 아님.

### A-2. 유입 造波경계 IB=5 (vf_bwuwn.f)

`CD -- 造波境界 --`(`vf_bwuwn.f:160`), `CD -- 法線方向への造波境界 --`(`:259-480`). 경계면 속도 `BCU=UN·VWS·AW·SA`(`:397-399`), **사각입사**(oblique) 지원(방향코사인 `SA/SB/SC`, 각처리 `:298-329`).

### A-3. 파이론 (IWVTYP) — Stokes5·cnoidal3·stream-function B (+외부테이블)

선택자 `IWVTYP`(3 커널 동일문서 `vf_cwmak0.f:17-20`·`cwmak1.f:15-18`·`cwmak2.f:15-20`):

| `IWVTYP` | 이론 | 인용 |
|---|---|---|
| `-2` | **Stokes 5차** (第5次近似) | `vf_cwmak0.f:18`; init `VF_STK0(N=5)` `:29-35`; 구현 `vf_wstk0.f` |
| `-1` | **Cnoidal 3차** (第3次近似) | `vf_cwmak0.f:19`; `VF_CND0(N=3)` `:36-42`; 구현 `vf_wcnd0.f` |
| `>0` | **Stream-function 법 B** (流れ関数法B, 임의차수 N) | `vf_cwmak0.f:20·43-55`; 구현 `vf_wsfmb2.f`(헤더 `:4`) |
| `-3` | **외부 테이블**(매트릭스데이터) | `vf_cwmak0.f:56-57` → `VF_CWMTB1/2` |
| `-4` | **제2 외부테이블** | `vf_cwmak0.f:58-59` → `VF_CWMTB12/22` |

> **고립파(solitary) 미지원** — IWVTYP 열거에 없음. Stokes5/cnoidal3 는 내부 CGS 작업(`*100`/`*0.01` 단위변환 `vf_cwmak0.f:30-35`), stream-function 은 SI. 외부테이블(`DMTB*`, `vf_a1main.f:253-262`)은 깊이별·위상별 속도/수위 시계열 외부공급(보간 `vf_cwmtb1.f`수위·`vf_cwmtb2.f`속도), 제2테이블은 반대측 등 제2 조파경계용.

## B. 개·방사 경계 + 대수칙 벽

### B-1. 방사(개)경계 — Sommerfeld형 (vf_bwuwn.f:483-619)

`CD -- 法線方向への開境界 --`(`vf_bwuwn.f:482`), `IBCTYP(1,JD)=2` 키. 위상속도 `C=BCTYP(6,JD)`(`:484`)의 **Sommerfeld/Orlanski 방사**:
- Courant 완화계수 `ALN=MIN(C·Δt/Δx, 1)`(`:501`, y측 `:568`), 접선 `ALT=MIN(2·ALN,1)`(`:502`)
- 풍상셀로의 대류 blend `BCU=(1-ALN)·BCU + ALN·UB(풍상)`(`:513`, y `:581`) — `UB/VB/WB`=전스텝 속도(`:51-53`) → 이산 `∂u/∂t + C·∂u/∂n = 0`
- 접선 `vf_bwuwt.f` 의 `IB=7` 블록은 **빈 stub**(`:178-179`) — 법선 blend 가 처리. INDB 의 `IB=7` 법선/접선도 빈 stub 으로 이 섹션에 위임.

### B-2. 대수칙 벽 — IB=6 평활 / IB=8 완전조면 (vf_bwuwt.f)

벽마찰은 **접선속도**에 적용(헤더 `…スリップ、フリー、対数則、完全粗面` `vf_bwuwt.f:5-7`). `IB=6.OR.IB=8` 블록(`:118-176`): 접선성분 `V1,V2`·벽거리 `DL=Δx/2`(`:123`)·접선속 `VA=√(V1²+V2²)`(`:151`):
- IB=6 → `VF_CLOGLW(DL,VA,VT)`(`:160`), IB=8 → `VF_CLOGKS(DL,VA,BCVI,VT)`(`:162`, `BCVI`=조도)
- 벽전단 피드백 `VA=DL/AN·VT²/VA`, `V1=V1-VA·V1`, `V2=V2-VA·V2`(`:164-166`)

**평활 대수칙** `VF_CLOGLW`(헤더 `対数則を満たす摩擦速度` `vf_cloglw.f:5`): Newton 반복(max20, eps1e-10, `:31-33·40-50`)으로 마찰속도 해. 식(헤더 `:6-7`): `F=vt/κ·log(dl·vt/ν)+vt·A−Va`, `F'=1/κ·log(dl·vt/ν)+1/κ+A`. 코드 `F=XX·AKR·W+XX·AKA0−VA`(`:43`).

**완전조면 대수칙** `VF_CLOGKS`(헤더 `完全粗面の摩擦速度` `vf_clogks.f:5`): 폐형(반복없음) `XX=LOG(DL/BKS)/AKK0+AKA0+3.0`, `VT=VA/XX`(`:29-30`), `BKS`=조도. = `u/uτ=(1/κ)ln(y/k_s)+B_r`.

> 상수: κ=`AKK0`=0.4·B=`AKA0`=5.5(`vf_a2dflt.f:175-176`, 로그출력 `LG-K`/`LG-A` `vf_ol1ini.f:277-278`).

## C. 표면셀 속도 보조 (vf_bsuw*)

개·벽 경계(IB코드)가 아니라 **자유표면셀** 처리(혼동주의):
- `vf_bsuwn.f:6` 표면셀-기체셀 법선속도(연속식) + 造파소스 주입(§A-1)
- `vf_bsuwn3.f:5` 구배제로 변형 / `vf_bsuwt.f:5` 비계산면 속도0·자유표면 접선 / `vf_bsuwt2.f:5` 자유표면 접선 재설정(특수)
- `vf_bsuwem.f:5-7` 砕波(쇄파)시 특수 기체셀 코너 속도보정

> ⚠️ provenance 주의: `vf_bwuwn3.f` 는 부재 — `vf_bsuwn3.f`(표면셀)가 실재. 방사경계는 INDB `IB=7` 스위치가 아니라 `IBCTYP=2` 특수경계 섹션에서 처리.
