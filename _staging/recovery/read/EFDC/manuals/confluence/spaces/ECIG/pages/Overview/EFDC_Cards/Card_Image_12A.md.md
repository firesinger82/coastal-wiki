---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_12A.md
lines: 61
sha256: aecb4d2067610d33a806c3130b74f1eb401578f2d6a07badeb6c11a78dd23a51
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_12A.md — 판독 구간 기록

구간은 1행부터 61행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(metadata) — 페이지 ID(2), 제목(3), space(4), 원문 URL(5), 버전(6), 갱신 시각(7), 문서 계층 경로(8)를 기록한다. `---` 구분자를 포함한다(1·9). |
| 10–25 | C12A TURBULENCE CLOSURE OPTIONS / 안정도 함수 — 난류 폐쇄(turbulence closure) 옵션 제목과 `ISSTAB`의 0·1·2·3·4 안정도 함수(stability functions) 선택을 설명한다(10–24). 각 선택에는 `ISQQ=1` 조건을 적는다. 이 선택이 C6의 `ISTOPT(0)`보다 우선한다고 적는다(22). 옵션·조건 원문: `\* ISSTAB: 0 FOR GALPERIN et al. STABILITY FUNCTIONS IN CALAVBOLD (ISQQ=1)` (14); `\*               1 FOR GALPERIN et al. STABILITY FUNCTIONS (ISQQ=1)` (16); `\*               2 FOR KANTHA AND CLAYSON (1994) STABILITY FUNCTIONS (ISQQ=1)` (18); `\*               3 FOR KANTAH (2003) STABILITY FUNCTIONS (ISQQ=1)` (20); `\*                  (NOTE: OPTION SELECTED HERE OVERRIDES ISTOPT(0) ON C6)` (22); `\*               4 VINCON-LEITE, ET.AL. (2014) APPROACH (ISQQ=1)` (24). `KANTAH (2003)` 철자를 유지했다(20). 주석용 `\*` 줄과 빈 줄을 포함한다. |
| 26–39 | C12A / 폐쇄 함수·최대값·필터·출력 — `ISSQL`의 비례 또는 상수 설정, `ISSTAB=3` 예외와 명시되지 않은 옵션의 비활성 조건, 최대 점성·확산계수 활성화, 평균·제곱근 필터(filter) 선택 및 출력 파일 선택을 적는다(26–38). `THIS OPTION`의 대상을 임의로 지정하지 않았다(32). 매개변수·조건 원문: `\* ISSQL: 0 SETS QQ AND QQL STABILITY FUNCTIONS PROPORTIONAL TO` (26); `\*                  MOMENTUM STABILITY FUNCTIONS (EXCEPT FOR ISSTAB=3)` (28); `\*            1 SETS QQ AND QQL STABILITY FUNCTIONS TO CONSTANTS` (30); `\* (FOR ISSTAB = 0,1,2) THIS OPTION NOT ACTIVE` (32); `\* ISAVBMX: SET TO 1 TO ACTIVATE MAX VISCOSITY AND DIFFUSIVITY OF AVMX AND ABMX` (34); `\* ISFAVB: SET TO 1 OR 2 TO AVG OR SQRT FILTER AVO AND AVB` (36); `\* ISINWV: SET TO 2 TO WRITE EE\_ARRAYS.OUT` (38). 빈 줄을 포함한다. |
| 40–57 | C12A / 길이 규모·벽 근접·식생·경계 — `ISLLIM`의 0·1·2 길이 규모(length scale) 및 RIQMAX 제한, `IFPROX`의 0·1·2 벽 근접 함수(wall proximity function), 사용하지 않는 식생(vegetation) 난류 생성 옵션과 경계 셀 운동량 보정 계수의 0 TO 1 범위를 설명한다(40–54). 매개변수·범위·조건 원문: `\* ISLLIM: 0 FOR NO LENGTH SCALE AND RIQMAX LIMITATIONS` (40); `\*             1 LIMIT RIQMAX IN STABILITY FUNCTION ONLY` (42); `\*             2 DIRECTLY LIMIT LENGTH SCALE AND LIMIT RIQMAX IN STABILITY FUNCTION` (44); `\* IFPROX: 0 FOR NO WALL PROXIMITY FUNCTION` (46); `\*               1 FOR PARABOLIC OVER DEPTH WALL PROXIMITY FUNCTION` (48); `\*               2 FOR OPEN CHANNEL WALL PROXIMITY FUNCTION` (50); `\* ISVTURB: SET TO 1 TO INCLUDE VEGETATION GENERATED TURBULENCE PRODUCTION (NOT USED)` (52); `\* BC\_EDGEFACTOR: BOUNDARY CELLS MOMENTUM CORRECTION FACTOR (0 TO 1)` (54). 주석용 `\*` 줄과 빈 줄을 포함한다(55–57). |
| 58–61 | C12A / 입력 예시 표 — 빈 표 첫 행, 구분 행, 아홉 매개변수 헤더와 입력 예시를 포함한다(58–61). 예시를 기본값으로 표시하지 않았다. 입력 표 원문: `\| C12A \| ISSTAB \| ISSQL \| ISAVBMX \| ISFAVB \| ISINWV \| ISLLIM \| IFPROX \| ISVTURB \| BC\_EDGEFACTOR \|` (60); `\|  \| 1 \| 0 \| 0 \| 2 \| 0 \| 2 \| 0 \| 0 \| 0 \|` (61). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14–24·26–36·40–44행: 이 파일에는 조건·참조에 쓰인 `ISQQ`, `ISTOPT(0)`, `QQ`, `QQL`, `AVO`, `AVB`, `AVMX`, `ABMX`, `RIQMAX`의 정의가 없다.
- 32행: `(FOR ISSTAB = 0,1,2) THIS OPTION NOT ACTIVE`는 옵션 이름을 명시하지 않는다.

