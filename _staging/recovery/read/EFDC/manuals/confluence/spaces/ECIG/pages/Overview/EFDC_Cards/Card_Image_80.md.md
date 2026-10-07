---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_80.md
lines: 86
sha256: f841e3592d7d94e1d5fbfb4ae267cdcb982a6708446e71addc530e75d4e97568
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_80.md — 판독 구간 기록

구간은 1행부터 86행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 원문 메타데이터(frontmatter) — 문서 ID·제목·space·URL·버전·갱신 시각·계층 경로를 적는다(1–9). |
| 10–28 | C80 CONTROLS FOR 3D FIELD OUTPUT / 형식·층 — 3차원장(3D field)의 ASCII 정수·부동소수점 출력 조건을 제시한다(14–16). 문자 배열(character array) 및 두 HDF 형식은 활성화되지 않았다고 적는다(18–22). 잔차 변수(residual variable) 형식 제어, 마지막 기준 시간 기간(reference time period) 동안 순간 변수(inst variable)의 출력 횟수, 늘이지 않은 물리 수직층(unstretched physical vertical layer) 수를 설명한다(24–28). 주석 표식과 빈 줄을 포함한다(11–28). 원문: `C80 CONTROLS FOR 3D FIELD OUTPUT` (10); `\* IS3DO: 1 TO WRITE TO 3D ASCI INTEGER FORMAT FILES, JS3DVAR.LE.2 SEE\|` (14); `\*             1 TO WRITE TO 3D ASCI FLOAT POINT FORMAT FILES, JS3DVAR.EQ.3 C57\|` (16); `\*             2 TO WRITE TO 3D CHARACTER ARRAY FORMAT FILES (NOT ACTIVE)` (18); `\*             3 TO WRITE TO 3D HDF IMAGE FORMAT FILES (NOT ACTIVE)` (20); `\*             4 TO WRITE TO 3D HDF FLOATING POINT FORMAT FILES (NOT ACTIVE)` (22); `\* ISR3DO: SAME AS IS3DO EXCEPT FOR RESIDUAL VARIABLES` (24); `\* NP3DO: NUMBER OF WRITES PER LAST REF TIME PERIOD FOR INST VARIABLES` (26); `\* KPC: NUMBER OF UNSTRETCHED PHYSICAL VERTICAL LAYERS` (28). |
| 29–60 | C80 CONTROLS FOR 3D FIELD OUTPUT / 그래픽 격자·재작성 — `NWGG`가 양수일 때 곡선 좌표 격자(curvilinear grid)를 덮는 직교 좌표 3차원 그래픽 격자(Cartesian 3D graphics grid overlay)의 물 셀 수를 정의한다고 적는다(30–34). 양수 조건에서 출력 첨자는 그래픽 격자의 셀 첨자라고 적는다(34–38). `GCELL.INP`는 EFDC가 아니라 격자 생성 코드 `GEFDC.F`가 사용하며, EFDC는 `GCELLMP.INP`에서 덮는 격자의 정보를 읽는다고 적는다(40–46). `NWGG`가 0이면 첨자는 `CELL.INP`로 정의한 EFDC 격자에 속한다고 적는다(46–48). 재작성 옵션의 전체 격자 출력과 특정 조건에서의 비권고, 후처리기(post processor) 사용 권고 및 개발자 문의 문구를 포함한다(50–60). 모든 조건과 파일명을 원문대로 옮긴다. 빈 줄을 포함한다(29–59). 원문: `\* NWGG: IF NWGG IS GREATER THAN ZERO, NWGG DEFINES THE NUMBER OF !2877\|` (30); `\*              WATER CELLS IN CARTESIAN 3D GRAPHICS GRID OVERLAY OF THE` (32); `\*              CURVILINEAR GRID. FOR NWGG>0 AND EFDC RUNS ON A CURVILINEAR` (34); `\*              GRID, I3DMI,I3DMA,J3DMI,J3DMA REFER TO CELL INDICES ON THE` (36); `\*             ON THE CARTESIAN GRAPHICS GRID OVERLAY DEFINED BY FILE` (38); `\*             GCELL.INP. THE FILE GCELL.INP IS NOT USED BY EFDC, BUT BY` (40); `\*             THE COMPANION GRID GENERATION CODE GEFDC.F. INFORMATION` (42); `\*             DEFINING THE OVERLAY IS READ BY EFDC.F FROM THE FILE` (44); `\*             GCELLMP.INP. IF NWGG EQUALS 0, I3DMI,I3DMA,J3DMI,J3DMA REFER` (46); `\*             TO INDICES ON THE EFDC GRID DEFINED BY CELL.INP.` (48); `\*             ACTIVATION OF THE REWRITE OPTION I3DRW=1 WRITES TO THE FULL` (50); `\*             GRID DEFINED BY CELL.INP AS IF CELL.INP DEFINES A CARTESIAN` (52); `\*             GRID. IF NWGG EQ 0 AND THE EFDC COMP GRID IS CO, THE REWRITE` (54); `\*              OPTION IS NOT RECOMMENDED AND A POST PROCESSOR SHOULD BE USED` (56); `\*             TO TRANSFER THE SHORT FORM, I3DRW=0, OUTPUT TO AN APPROPRIATE` (58); `\*              FORMAT FOR VISUALIZATION. CONTACT DEVELOPER FOR MORE DETAILS` (60). |
| 61–82 | C80 CONTROLS FOR 3D FIELD OUTPUT / 첨자·배열·표고 — 출력 배열의 I·J 최소 및 최대 첨자를 정의한다(62–68). 활성 물 셀만 출력하는 옵션과 격자 조건에 따른 방향 교정 재작성 옵션을 적는다(70–76). 늘이지 않기(unstretching)에 사용하는 최대 수면 표고(surface elevation)와 최소 저면 표고(bottom elevation)의 조건을 적는다(78–80). 주석 표식과 빈 줄을 포함한다(61–82). 원문: `\* I3DMI: MINIMUM OR BEGINNING I INDEX FOR 3D ARRAY OUTPUT` (62); `\* I3DMA: MAXIMUM OR ENDING I INDEX FOR 3D ARRAY OUTPUT` (64); `\* J3DMI: MINIMUM OR BEGINNING J INDEX FOR 3D ARRAY OUTPUT` (66); `\* J3DMA: MAXIMUM OR ENDING J INDEX FOR 3D ARRAY OUTPUT` (68); `\* I3DRW: 0 FILES WRITTEN FOR ACTIVE CO WATER CELLS ONLY` (70); `\*              1 REWRITE FILES TO CORRECT ORIENTATION DEFINED BY GCELL.INP` (72); `\*              AND GCELLMP.INP FOR CO WITH NWGG.GT.O OR BY CELL.INP IF THE` (74); `\*              COMPUTATIONAL GRID IS CARTESIAN AND NWGG.EQ.0` (76); `\* SELVMAX: MAXIMUM SURFACE ELEVATION FOR UNSTRETCHING (ABOVE MAX SELV )` (78); `\* BELVMIN: MINIMUM BOTTOM ELEVATION FOR UNSTRETCHING (BELOW MIN BELV)` (80). |
| 83–86 | C80 입력 예시 — 입력 열 제목과 수치 값 행을 제시한다(84·86). 값 행은 원문 예시이며 기본값이라는 표시는 없다. 빈 줄을 포함한다(83·85). 원문: `C80 IS3DO ISR3DO NP3DO KPC NWGG I3DMI I3DMA J3DMI J3DMA I3DRW SELVMAX BELVMIN` (84); `          0          0             0          1        0        1        62       1          118       0          15         -315` (86). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14–16·30행: 주석 끝에 `SEE|`·`C57|`·`!2877|`가 남아 있다.
- 14–16·54·70·74행: `JS3DVAR`와 `CO`를 사용하지만 이 파일에는 두 이름의 정의가 없다.
- 34·74행: 34행은 `NWGG>0`, 74행은 `NWGG.GT.O`로 적는다. 후자의 마지막 문자는 숫자 `0`이 아닌 알파벳 `O`이다.

