---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/cppdefs.h
lines: 83
sha256: e52d50e8e893eb7e8c3a78d364e8e5eb2ef6a3e3528ffa717f753b3710f3c3cd
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# cppdefs.h — 판독 구간 기록

구간은 1행부터 83행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 머리말은 모든 .F90의 포함 파일이며 GOTM 컴파일에 필요한 정의라고 설명한다(1–4). PATH_MAX=255, stderr=0, stdout=6을 정의한다(6–9). STDOUT/STDERR는 Fortran write 매크로(macro)이며 LEVEL0..4의 들여쓰기와 FATAL 접두어를 정의한다(12–19). LINE은 구분선 문자열이다(21). 원문(조건·반복·대입·호출, 등장 순서): `#define PATH_MAX	255` (6); `#define stderr		0` (8); `#define stdout		6` (9); `#define STDOUT write(stdout,*)` (12); `#define STDERR write(stderr,*)` (13); `#define LEVEL0 STDERR` (14); `#define LEVEL1 STDERR '   ',` (15); `#define LEVEL2 STDERR '       ',` (16); `#define LEVEL3 STDERR '           ',` (17); `#define LEVEL4 STDERR '               ',` (18); `#define FATAL  STDERR 'FATAL ERROR: ',` (19); `#define LINE "------------------------------------------------------------------------"` (21). |
| 23–43 | 변수 형상(shape) 코드 POINT/Z/T/XY/XYT/XYZT를 0..5로 정의한다(23–29). 파일 형식 RAWBINARY/ASCII/NETCDF/GRADS/OPENDX는 0..4다(31–35). READING=0·WRITING=1을 정의한다(37–39). 0 나눗셈 회피 주석 아래 SMALL=1e−8을 정의한다(41–42). 원문(조건·반복·대입·호출, 등장 순서): `#define POINT           0` (24); `#define Z_SHAPE         1` (25); `#define T_SHAPE         2` (26); `#define XY_SHAPE        3` (27); `#define XYT_SHAPE       4` (28); `#define XYZT_SHAPE      5` (29); `#define RAWBINARY       0` (31); `#define ASCII           1` (32); `#define NETCDF          2` (33); `#define GRADS           3` (34); `#define OPENDX          4` (35); `#define READING 0` (38); `#define WRITING 1` (39); `#define SMALL 1e-8` (42). |
| 44–61 | SINGLE을 정의한 직후 해제한다(45–46). #ifdef SINGLE 경로는 selected_real_kind(6)과 0.0/0.5/1.0을 사용한다(48–53). #else 경로는 selected_real_kind(13)과 0.0d0/0.5d0/1.0d0을 사용한다(54–60). MPI_REAL/MPI_DOUBLE_PRECISION 매크로 정의 두 줄은 Fortran 주석으로 적혀 있다(50·56). 원문(조건·반복·대입·호출, 등장 순서): `#define SINGLE` (45); `#undef  SINGLE` (46); `#ifdef SINGLE` (48); `#define REALTYPE real(kind = selected_real_kind(6))` (49); `#define _ZERO_ 0.0` (51); `#define _HALF_ 0.5` (52); `#define _ONE_  1.0` (53); `#else` (54); `#define REALTYPE real(kind = selected_real_kind(13))` (55); `#define _ZERO_ 0.0d0` (57); `#define _HALF_ 0.5d0` (58); `#define _ONE_  1.0d0` (59); `#endif` (60). |
| 62–70 | NetCDF 출력 실수 정밀도(real precision)를 별도로 선택한다(62). #ifdef _NCDF_SAVE_DOUBLE_ 경로는 NF90_DOUBLE과 selected_real_kind(13)을 정의한다(63–65). #else는 NF90_REAL과 selected_real_kind(6)을 정의한다(66–69). 원문(조건·반복·대입·호출, 등장 순서): `#ifdef _NCDF_SAVE_DOUBLE_` (63); `#define NCDF_FLOAT_PRECISION NF90_DOUBLE` (64); `#define NCDF_REAL real(kind = selected_real_kind(13))` (65); `#else` (66); `#define NCDF_FLOAT_PRECISION NF90_REAL` (67); `#define NCDF_REAL real(kind = selected_real_kind(6))` (68); `#endif` (69). |
| 71–83 | 비국소 플럭스(non-local flux) NONLOCAL을 해제한다(71–72). KPP 난류 모형(turbulence model) 매크로에서 KPP_SHEAR·KPP_INTERNAL_WAVE·KPP_CONVEC·KPP_IP_FC·KPP_SALINITY는 정의한다(74–77·80·82). KPP_DDMIX·KPP_TWOPOINT_REF·KPP_CLIP_GS는 해제한다(78–79·81). 마지막 빈 줄을 포함한다(83). 원문(조건·반복·대입·호출, 등장 순서): `#undef NONLOCAL` (72); `#define KPP_SHEAR` (75); `#define KPP_INTERNAL_WAVE` (76); `#define KPP_CONVEC` (77); `#undef KPP_DDMIX` (78); `#undef KPP_TWOPOINT_REF` (79); `#define KPP_IP_FC` (80); `#undef KPP_CLIP_GS` (81); `#define KPP_SALINITY` (82). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 45–60: SINGLE은 정의 직후 해제한다. 이 파일 안에서 다시 정의하는 문장이 없으므로 뒤 #ifdef SINGLE의 선택 경로는 #else에 있는 selected_real_kind(13)이다.
- 48–69: 계산용 REALTYPE 분기와 NetCDF 출력용 NCDF_REAL 분기는 서로 다른 매크로를 검사한다. 후자는 _NCDF_SAVE_DOUBLE_ 여부를 이 파일 밖에서 받는다.
