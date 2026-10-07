---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_32.md
lines: 94
sha256: 413299e914a565eecba7374dc134d0ded23b8083e90c555a3e171a77f7e36cc4
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_32.md — 판독 구간 기록

구간은 1행부터 94행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | C32 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 수면 표고(surface elevation) 또는 압력(pressure)에 의존하는 유량 자료 제목을 제시한다(10). 빈 줄과 주석 표식도 포함한다(11–13). 원문: ` C32 SURFACE ELEV OR PRESSURE DEPENDENT FLOW INFORMATION ` (10). |
| 14–47 | 셀 위치와 유량 제어 유형(flow control type) — 상류·취수 셀과 하류·환수 셀의 I·J 인덱스를 정의한다(14–20). 유량 제어는 상류 수심·수위 유량 관계 곡선(stage rating curve), 수위 또는 압력 차 표, 가속 유동, 두 수면 표고, 하부 현(lower chord), 수리 구조물(hydraulic structure) 옵션을 구분한다(22–46). EE8.1 표기도 원문대로 옮긴다(44·46). 원문: ` \* IQCTLU: I INDEX OF UPSTREAM OR WITHDRAWAL CELL ` (14); ` \* JQCTLU: J INDEX OF UPSTREAM OR WITHDRAWAL CELL ` (16); ` \* IQCTLD: I INDEX OF DOWNSTREAM OR RETURN CELL ` (18); ` \* JQCTLD: J INDEX OF DOWNSTREAM OR RETURN CELL ` (20); ` \* NQCTYP: FLOW CONTROL TYPE ` (22); ` \*                = -1 FLOW AS FUNCTION OF UPSTREAM DEPTH (STAGE RATING CURVED) ` (24); ` \*                = 0 FLOW AS FUNCTION OF ELEVATION OR PRESSURE DIFFERCENCE TABLE ` (26); ` \*                = 1 SAME AS 0 WITH ACCELERATING FLOW (E.G. TIDAL INLET) ` (28); ` \*                = 2 FLOW DERIVED FROM UPSTREAM AND DOWNSTREAM WS ELEVATIONS ` (30); ` \*                = 3 LOWER CHORD OPTION USING UPSTREAM DEPTH WHEN WSEL > BQCLCE ` (32); ` \*                = 4 LOWER CHORD OPTION USING ELEVATION DIFFERENCE WHEN WSEL > BQCLCE ` (34); ` \*                = 5 CULVERT ` (36); ` \*                = 6 SLUICE GATE ` (38); ` \*                = 7 WEIR ` (40); ` \*                = 8 ORIFICE ` (42); ` \*                = 9 FLOATING SKIMMER WALL (EE8.1) ` (44); ` \*                = 10 SUBMERGED WEIR (EE8.1) ` (46). |
| 48–59 | 제어 표와 승수 — 제어 특성 표(control characterization table)의 식별자와 상류 유량 승수 스위치를 정의한다(48–50). 정상 유량 및 U면·V면·두 면의 자료 단위와 곱하는 값을 구분한다(52–58). 원문: ` \* NQCTLQ: ID NUMBER OF CONTROL CHARACTERIZATION TABLE ` (48); ` \* NQCMUL: MULTIPLIER SWITCH FOR FLOWS FROM UPSTREAM CELL ` (50); ` \*                = 0 MULT BY 1. FOR CONTROL TABLE IN (L\*L\*L/T) ` (52); ` \*                = 1 MULT BY DY FOR CONTROL TABLE IN (L\*L/T) ON U FACE ` (54); ` \*                = 2 MULT BY DX FOR CONTROL TABLE IN (L\*L/T) ON V FACE ` (56); ` \*                = 3 MULT BY DX+DY FOR CONTROL TABLE IN (L\*L/T) ON U&V FACES ` (58). |
| 60–75 | 수두(head)와 하부 현 — 상류 및 하류 수두 오프셋(offset)의 m 단위를 제시한다(60–64). NQCTYP=-1 또는 3일 때 수심 대신 표고를 쓰는 설정을 설명한다(62). 미사용 항목, 하부 현 표고, 하부 현 위에서 요구하는 최소 단계 수의 적용 조건을 적는다(66–72). 원문: ` \* HQCTLU: OFFSET FOR UPSTREAM HEAD (m) ` (60); ` \* SET TO CELL'S BOTTOM ELEVATION TO USE ELEVATION INSTEAD OF DEPTH FOR NQCTYP = -1 or 3 ` (62); ` \* HQCTLD: OFFSET FOR DOWNSTREAM HEAD (m) ` (64); ` \* QTCLMU: NOT USED ` (66); ` \* QTCLMD: NOT USED ` (68); ` \* BQCLCE: LOWER CHORD ELEVATION (m) [ONLY USED IF NQCTYP = 3 OR 4] ` (70); ` \* NQCMINS: MINIMUM NUMBER OF STEPS REQUIRED ABOVE LOWER CHORD [ONLY USED IF NQCTYP = 3 OR 4] ` (72). |
| 76–85 | 하부 현 조회 표(lookup table)의 수두 결정 — HUP와 HDW 제목(76) 및 NQCTYP=3·4의 계산식을 제시한다(78·80·82). 조건과 계산식 전체를 원문 그대로 옮긴다. 원문: ` \* \*\*\* LOOKUP TABLE HEAD DETERMINATION (HUP & HDW) FOR LOW CHORD ` (76); ` \* \*\*\* NQCTYP = 3: HUP = HP(LU) + HCTLUA(NCTLT) + HQCTLU(NCTL) ` (78); ` \* \*\*\* NQCTYP = 4: HUP = HP(LU) + BELV(LU) + HCTLUA(NCTLT) + HQCTLU(NCTL) ` (80); ` \* \*\*\* NQCTYP = 4: HDW = HP(LD) + BELV(LD) + HCTLDA(NCTLT) + HQCTLD(NCTL) ` (82). |
| 86–93 | 수리 구조물 설정 — 유량 분배 계수(discharge distribution factor)는 NQCTYP>4에서만 사용한다(86). 수리 구조물 정의 변경 횟수와 두 시각 사이 전이 시간(transition time)의 초 단위를 제시하며 두 항목은 개발 중이라고 적는다(88–90). 원문: ` \*HS\_FACTOR: DISCHARGE DISTRIBUTION FACTOR (ONLY USED FOR NQCTYP>4) ` (86); ` \*HS\_NTIMES: NUMBER OF TIMES HYDRAULIC STRUCTURE DEFINITION CHANGES (IN DEVELOPMENT) ` (88); ` \*HS\_TRANSITION: NUMBER OF SECONDS TO TRANSITION FROM TIME (T) TO TIME (T+1) (IN DEVELOPMENT) ` (90). |
| 94–94 | C32 입력 형식 — 입력 열 이름만 제시한다(94). 파일은 이 줄에서 끝난다. 원문: ` C32 IQCTLU JQCTLU IQCTLD JQCTLD NQCTYP NQCTLQ NQCMUL HQCTLU HQCTLD QTCLMU QTCLMD BQCLCE NQCMINS FACTOR NTIMES TRANSIT ` (94). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 78–82행: 수두 계산식의 `HP`, `BELV`, `HCTLUA`, `HCTLDA`, `LU`, `LD`, `NCTLT`, `NCTL`은 이 파일에 기호 정의가 없다.
- 86·88·90·94행: 설명 항목은 `HS\_FACTOR`, `HS\_NTIMES`, `HS\_TRANSITION`으로 적는다. 입력 열 이름의 끝 세 항목은 `FACTOR`, `NTIMES`, `TRANSIT`으로 적는다. 이 파일은 두 표기의 대응을 명시하지 않는다.
