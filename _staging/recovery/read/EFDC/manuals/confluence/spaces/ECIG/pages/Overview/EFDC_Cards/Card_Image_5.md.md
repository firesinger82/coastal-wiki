---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_5.md
lines: 76
sha256: 61bde13d4d0a4740a2b3ca37728376ac7bcda4ccf7de0fe928c834f3c1c948f5
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_5.md — 판독 구간 기록

구간은 1행부터 76행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(frontmatter) — 페이지 ID 30310445(2), 제목 Card Image 5(3), space ECIG(4), 원문 URL(5), 버전 1(6), 수정 시각 2018-01-08T08:06:08.975Z(7), 문서 경로(8)와 구분선(1·9)을 포함한다. |
| 10–26 | C5 MOMENTUM ADVEC AND HORIZ DIFF SWITCHES AND MISC SWITCHES / 운동량·연계 — 운동량 이류(momentum advection)의 중앙 차분(central difference)·상류 차분(upwind difference)·연구용 실험 옵션과 수평 운동량 확산(horizontal momentum diffusion) 옵션을 제시한다(14–22). 마지막 평균 질량 수송 평균 기간의 평균 수평 전단 분산(mean horizontal shear dispersion) 텐서 계산 및 외부 모델 연계 파일의 선택값을 정의한다(24·26). 3TL 전용·연구용 조건과 옵션 값 원문: `\* ISCDMA: 1 FOR CENTRAL DIFFERENCE MOMENTUM ADVECTION (USED FOR 3TL ONLY)` (14); `\*                0 FOR UPWIND DIFFERENCE MOMENTUM ADVECTION (USED FOR 3TL ONLY)` (16); `\*                2 FOR EXPERIMENTAL UPWIND DIFF MOM ADV (FOR RESEARCH PURPOSES)` (18); `\* ISHDMF: 1 TO ACTIVE HORIZONTAL MOMENTUM DIFFUSION` (20); `\*                2 TO ACTIVE HORIZONTAL MOMENTUM DIFFUSION WITH WATER COLUMN DIFFUSION` (22); `\* ISDISP: 1 CALCULATE MEAN HORIZONTAL SHEAR DISPERSION TENSOR OVER LAST MEAN MASS TRANSPORT AVERAGING PERIOD` (24); `\* ISWASP: 4 OR 5 TO WRITE FILES FOR WASP4 OR WASP5 MODEL LINKAGE, 17-WASP7HYDRO, 99 - CE-QUAL-ICM` (26). |
| 27–44 | 습윤·건조(wetting and drying) 옵션 — 비활성화, 일정·가변 습윤 깊이, 비선형 반복(non-linear iteration) 사용 여부, 셀 마스킹(cell masking), 셀 면 기반 가변 습윤·건조를 설명한다(28–44). HWET·ITERHPM의 카드 참조와 음수 옵션의 SAME AS 조건을 그대로 옮긴다. 원문: `\* ISDRY: 0 NO WETTING & DRYING OF SHALLOW AREAS` (28); `\*             1 CONSTANT WETTING DEPTH SPECIFIED BY HWET ON CARD 11` (30); `\*                WITH NONLINEAR ITERATIONS SPECIFIED BY ITERHPM ON CARD C3` (32); `\*             2 VARIABLE WETTING DEPTH CALCULATED INTERNALLY IN CODE` (34); `\*                 WITH NONLINEAR ITERATIONS SPECIFIED BY ITERHPM ON CARD C3` (36); `\*           11 SAME AS 1, WITHOUT NONLINEAR ITERATION` (38); `\*          -11 SAME AS 11 BUT WITH CELL MASKING` (40); `\*           99 VARIABLE WETTING & DRYING USING CELL FACES` (42); `\*         -99 SAME AS 11 BUT WITH CELL MASKING` (44). |
| 45–60 | 난류·강체 덮개·식생 옵션 — 난류 강도(turbulent intensity) 이류 방식, 자유수면이 없는 강체 덮개(rigid lid) 모드, 식생 저항(vegetation resistance), 진단 파일, 층류(laminar flow) 옵션과 외부 모드(external mode)의 암시적(implicit) 저면·식생 저항을 정의한다(46–58). 이름·적용 조건 원문: `\* ISQQ: 1 TO USE STANDARD TURBULENT INTENSITY ADVECTION SCHEME` (46); `\* 2 RESEARCH TURBULENT INTENSITY ADVECTION SCHEME` (48); `\* ISRLID: 1 TO RUN IN RIGID LID MODE (NO FREE SURFACE)` (50); `\* ISVEG: 1 TO IMPLEMENT VEGETATION RESISTANCE` (52); `\* 2 IMPLEMENT WITH DIAGNOSTICS TO FILE CBOT.LOG` (54); `\* ISVEGL: 1 TO INCLUDE LAMINAR FLOW OPTION IN VEGETATION RESISTANCE` (56); `\* ISITB: 1 FOR IMPLICIT BOTTOM & VEGETATION RESISTANCE IN EXTERNAL MODE` (58). |
| 61–72 | 셀 부분집합·내부 압력 경사 — HMD 계산용 셀 부분집합(subset of cells)과 파일 이름을 제시한다(62). 내부 압력 경사(internal pressure gradient)의 기존·Jacobian·유한체적(finite volume) 공식 옵션을 정의한다(64–68). 원문: `\* IHMDSUB: 1 TO USE A SUBSET OF CELLS FOR HMD CALCULATIONS, MAPHMD.INP` (62); `\* IINTPG: 0 ORIGINAL INTERNAL PRESSURE GRADIENT FORMULATION` (64); `\*              1 JACOBIAN FORMULATION` (66); `\*              2 FINITE VOLUME FORMULATION` (68). |
| 73–76 | C5 입력 형식 — 빈 줄과 열 이름·값의 두 줄을 포함한다(73–76). 제시된 수치를 기본값으로 표시하지 않는다. 원문: `C5 ISCDMA   ISHDMF   ISDISP   ISWASP   ISDRY   ISQQ   ISRLID   ISVEG   ISVEGL   ISITB   IHMDSUB   IINTPG` (74); `         0               0             0            0              0           1          0           1            0            0           0             0` (76). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14·16·62: 본문은 `3TL`과 `HMD` 표기를 사용한다. 이 파일에는 두 표기의 별도 정의가 없다.

