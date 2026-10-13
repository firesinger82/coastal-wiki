---
file: models/ROMS/raw/source_code/roms/Master/roms_kernel.F
lines: 196
sha256: 5e941668be50020e7d4970766b76040d505f565eb0a9e4e33536a0b80e6ba9ff
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# roms_kernel.F — 판독 구간 기록

구간은 1행부터 196행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–39 | `#include "cppdefs.h"` (1)로 cppdefs.h를 끼워 넣는다. 저작권·라이선스 머리말(2–9). 드라이버 목록 주석은 수반·민감도(sensitivity)·고유모드(eigenmode)·특이벡터(singular vector)·헤시안(Hessian)·증분 4차원 변분 자료동화(incremental 4D-Var)·JEDI·기본 비선형 드라이버 이름을 열거한다(10–39). 열린 전처리 조건은 없다. |
| 40–78 | 열린 전처리 조건은 없다. 최적 섭동(optimal perturbation)·관측·자료동화 분석/예측 민감도·접선 선형/수반 점검·Picard·표현자(representer)·RBL4D-Var·R4D-Var·확률 최적값(stochastic optimals) 드라이버 이름과 설명 주석 및 빈 주석을 포함한다(40–78). 실행문은 없다. |
| 79–113 | 열린 전처리 조건은 없다. 안장점(saddle point) 4D-Var·다중 실행 파일 자료동화·대칭성(symmetry)·선형화(linearization) 점검·접선 선형 자료동화 드라이버 목록 및 구분 주석을 포함한다(79–113). 실행문은 없다. |
| 114–139 | `#if defined AD_SENSITIVITY` (114), `# include "adsen_roms.h"` (115), 빈 줄(116). 같은 선택 사슬의 `#elif defined AFT_EIGENMODES` (117), `# include "afte_roms.h"` (118), `#elif defined FT_EIGENMODES` (119), `# include "fte_roms.h"` (120), `#elif defined FORCING_SV` (121), `# include "fsv_roms.h"` (122), `#elif defined OPT_PERTURBATION` (123), `# include "op_roms.h"` (124), `#elif defined HESSIAN_SV` (125), `# include "hessian_op_roms.h"` (126), `#elif defined HESSIAN_FSV` (127), `# include "hessian_fsv_roms.h"` (128), `#elif defined OPT_OBSERVATIONS` (129), `# include "optobs_roms.h"` (130). `#elif defined STOCHASTIC_OPT` (131) 안에서 `# ifdef HESSIAN_SO` (132), `#   include "hessian_so_roms.h"` (133), `# else` (134), `#   include "so_roms.h"` (135), `# endif` (136). 이어 `#elif defined SO_SEMI` (137), `# include "so_semi_roms.h"` (138), 빈 줄(139). 각 include는 표시된 이름 파일을 끼워 넣는다. |
| 140–150 | 시작 시 114행에서 시작한 전처리 선택 사슬 안. `#elif defined CORRELATION` (140), `# include "correlation.h"` (141), `#elif defined INNER_PRODUCT \|\| defined SANITY_CHECK` (142), `# include "pert_roms.h"` (143), `#elif defined PICARD_TEST` (144), `# include "picard_roms.h"` (145), `#elif defined R_SYMMETRY` (146), `# include "symmetry.h"` (147), `#elif defined TLM_CHECK` (148), `# include "tlcheck_roms.h"` (149), 빈 줄(150). 각 include는 표시된 이름 파일을 끼워 넣는다. |
| 151–168 | 시작 시 114행에서 시작한 전처리 선택 사슬 안. `#elif defined ARRAY_MODES \|\| defined CLIPPING` (151), `# include "array_modes.h"` (152), `#elif defined I4DVAR && !defined SPLIT_I4DVAR` (153), `# include "i4dvar_roms.h"` (154), `#elif defined I4DVAR_ANA_SENSITIVITY` (155), `# include "obs_sen_i4dvar_analysis.h"` (156), `#elif defined JEDI` (157), `# include "jedi_roms.h"` (158), `#elif defined RBL4DVAR && !defined SPLIT_RBL4DVAR` (159), `# include "rbl4dvar_roms.h"` (160), `#elif defined RBL4DVAR_ANA_SENSITIVITY` (161), `# include "obs_sen_rbl4dvar_analysis.h"` (162), `#elif defined RBL4DVAR_FCT_SENSITIVITY` (163), `# include "obs_sen_rbl4dvar_forecast.h"` (164), `#elif defined R4DVAR && !defined SPLIT_R4DVAR` (165), `# include "r4dvar_roms.h"` (166), `#elif defined R4DVAR_ANA_SENSITIVITY` (167), `# include "obs_sen_r4dvar_analysis.h"` (168). 각 include는 표시된 이름 파일을 끼워 넣는다. |
| 169–183 | 시작 시 114행에서 시작한 전처리 선택 사슬 안. `#elif defined SPLIT_I4DVAR` (169), `# include "split_i4dvar_roms.h"` (170), `#elif defined SPLIT_RBL4DVAR` (171), `# include "split_rbl4dvar_roms.h"` (172), `#elif defined SPLIT_R4DVAR` (173), `# include "split_r4dvar_roms.h"` (174), `#elif defined SPLIT_SP4DVAR` (175), `# include "split_sp4dvar_roms.h"` (176), `#elif defined SP4DVAR && !defined SPLIT_SP4DVAR` (177), `# include "sp4dvar_roms.h"` (178), `#elif defined TL_RBL4DVAR` (179), `# include "tl_rbl4dvar_roms.h"` (180), `#elif defined TL_R4DVAR` (181), `# include "tl_r4dvar_roms.h"` (182), 빈 줄(183). 각 include는 표시된 이름 파일을 끼워 넣는다. |
| 184–196 | 시작 시 114행에서 시작한 전처리 선택 사슬 안. 바깥 `#else` (184) 뒤 빈 줄(185). 내부 `# if defined TLM_DRIVER` (186), `#  include "tl_roms.h"` (187), `# elif defined RPM_DRIVER` (188), `#  include "rp_roms.h"` (189), `# elif defined ADM_DRIVER` (190), `#  include "ad_roms.h"` (191), `# else` (192), `#  include "nl_roms.h"` (193), `# endif` (194). 각 include는 표시된 이름 파일을 끼워 넣으며 내부 기본 분기는 nl_roms.h이다. 빈 줄(195)과 바깥 `#endif` (196). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 106·179–180: 목록 주석에는 `tl_rbl4dvar_roms.`로 적혀 있다. TL_RBL4DVAR 분기의 실제 포함 파일은 `tl_rbl4dvar_roms.h`이다.
- 114–196: 드라이버 선택은 하나의 전처리 if/elif/else 사슬이다. 여러 조건이 정의되어도 앞선 참 분기를 선택하는 구조이다. 포함 파일 내부는 이번 판독 범위에 없다.
