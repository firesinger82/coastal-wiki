---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_81.md
lines: 54
sha256: 224ce2edc4834210eac1902a29d74514cb0d06b5e01c7b6dfaa9d90b420f1421
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_81.md — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 원문 메타데이터(frontmatter) — 문서 ID·제목·space·URL·버전·갱신 시각·계층 경로를 적는다(1–9). |
| 10–34 | C81 OUTPUT ACTIVATION AND SCALES FOR 3D FIELD OUTPUT — 3차원장(3D field) 출력 변수의 순서를 바꾸지 말라는 지시와 활성화 조건을 적는다(14–16). 스케일 변환(scaling) 없음·자동 변환·다음 두 열 지정 변환·최대 스케일 값 승수 변환의 옵션을 설명한다(18–32). 자동 변환과 지정 변환의 값 범위, 프레임별 스케일 출력 파일, `I4`·`F7.2` 형식을 제시한다(20–32). 부동소수점 형식 옵션은 두 출력 제어 값이 반드시 1이어야 한다고 적는다(32). 주석 표식과 빈 줄을 포함한다(11–34). 원문: `C81 OUTPUT ACTIVATION AND SCALES FOR 3D FIELD OUTPUT` (10); `\* VARIABLE: DUMMY VARIBLE ID (DO NOT CHANGE ORDER)` (14); `\* IS3(VARID): 1 TO ACTIVATE THIS VARIBLES` (16); `\* JS3(VARID): 0 FOR NO SCALING OF THIS VARIABLE` (18); `\*                     1 FOR AUTO SCALING OF THIS VARIABLE OVER RANGE 0<VAL<255` (20); `\*                        AUTO SCALES FOR EACH FRAME OUTPUT IN FILES OUT3D.DIA AND` (22); `\*                       ROUT3D.DIA OUTPUT IN I4 FORMAT` (24); `\*                    2 FOR SCALING SPECIFIED IN NEXT TWO COLUMNS WITH OUTPUT` (26); `\*                       DEFINED OVER RANGE 0<VAL<255 AND WRITTEN IN I4 FORMAT` (28); `\*                    3 FOR MULTIPLIER SCALING BY MAX SCALE VALUE WITH OUTPUT` (30); `\*                       WRITTEN IN F7.2 FORMAT (IS3DO AND ISR3DO MUST BE 1)` (32). |
| 35–54 | C81 입력 예시 — 입력 열 제목과 세 속도(velocity) 성분, 염분(salinity)·수온(temperature)·염료(dye)·점착성 퇴적물(cohesive sediment)·비점착성 퇴적물(non-cohesive sediment)·독성 오염물질(toxic contaminant)의 값 행을 제시한다(36–54). 값 행은 원문 예시이며 기본값이라는 표시는 없다. 빈 줄을 포함한다(35–53). 원문: `C81 VARIABLE IS3D JS3D SMAX SMIN` (36); `          'U VEL'       0       0      0       0` (38); `          'V VEL'       0       0      0       0` (40); `         'W VEL'       0       0      0       0` (42); `         'SAL'           0       0      0       0` (44); `       'TEMP'          0       0      0       0` (46); `        'DYE'           0       0      0       0` (48); `        'SED'           0       0      0       0` (50); `        'SND'           0       0      0       0` (52); `        'TOX'           0       0      0       0` (54). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 16·18·36행: 활성화·스케일 변환 설명의 이름은 `IS3(VARID)`·`JS3(VARID)`이고 입력 열 제목의 이름은 `IS3D`·`JS3D`이다. 이 파일에는 두 표기의 대응 관계를 명시한 문장이 없다.
- 26·30·36행: 다음 두 열과 최대 스케일 값은 설명에 등장하지만 `SMAX`·`SMIN` 이름으로 된 정의는 없다.

