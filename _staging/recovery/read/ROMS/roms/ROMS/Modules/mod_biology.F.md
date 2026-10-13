---
file: models/ROMS/raw/source_code/roms/ROMS/Modules/mod_biology.F
lines: 140
sha256: 46c9fdfb1e91920f140c4279bb37a0792dd61b19704f365f0ad1cbc3f87d8cde
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# mod_biology.F — 판독 구간 기록

구간은 1행부터 140행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | `cppdefs.h`를 끼워 넣는다(1). 저작권·MIT/X 형식 라이선스 안내(2–8). 주석은 생태계 모델(ecosystem model)의 내부 매개변수 선언과 사용자 정의 설계를 설명한다(10–14). 각 모델은 일곱 종류의 파일로 구성된다는 주석이다(16). 첫 종류는 이산화한 생성·소멸 방정식(discretized source/sink equations) 파일이며 ecb.h·ecosim.h·fennel.h·hypoxia_srm.h·nemuro.h·npzd_Franks.h·npzd_iron.h·npzd_Powell.h·red_tide.h와 대응 매크로를 나열한다(18–28). 이 목록은 주석이며 식 본문은 없다. 전처리 원문: `#include "cppdefs.h"` (1). |
| 30–65 | 주석의 두 번째 종류는 내부 매개변수 선언용 ecb_mod.h부터 red_tide_mod.h까지 아홉 모델 파일이다(30–40). 세 번째 종류는 표준 입력 bio_ECB.in·bio_Fennel.in·ecosim.in·hypoxia_srm.in·nemuro.in·npzd_Franks.in·npzd_iron.in·npzd_Powell.in·red_tide.in이다(42–52). 네 번째 종류는 입력 매개변수 판독용 ecb_inp.h부터 red_tide_inp.h까지이다(54–64). 구분 주석도 포함한다(31·41·53·65). |
| 66–113 | 주석의 다섯 번째 종류는 varinfo.yaml 메타데이터(metadata)를 읽을 때 변수 인덱스를 배정하는 ecb_var.h부터 red_tide_var.h까지이다(66–77). 여섯 번째는 모든 출력 NetCDF 파일에 입력 매개변수를 정의하는 *_def.h, 일곱 번째는 입력 매개변수를 출력하는 *_wrt.h이다(79–103). 이 두 목록도 아홉 모델에 대응한다. 모든 *.h는 ROMS/Nonlinear/Biology에 있으며 프로젝트에서 사용자 정의 파일을 선택할 수 있도록 꺾쇠 포함을 사용한다는 주석을 둔다(106–109). 머리말 종료와 빈 줄을 포함한다(110–113). |
| 114–124 | BIOLOGY 안에서 하나의 if/elif 사슬을 연다(114–115). BIO_FENNEL은 fennel_mod.h, 그 조건 불성립 시 ECB는 ecb_mod.h, 이어 ECOSIM은 ecosim_mod.h, HYPOXIA_SRM은 hypoxia_srm_mod.h, NEMURO는 nemuro_mod.h를 끼워 넣는다(115–124). 포함 파일 내부의 선언·기본값은 이 원문에 없다. 전처리 원문: `#ifdef BIOLOGY` (114); `# if defined BIO_FENNEL` (115); `#  include <fennel_mod.h>` (116); `# elif defined ECB` (117); `#  include <ecb_mod.h>` (118); `# elif defined ECOSIM` (119); `#  include <ecosim_mod.h>` (120); `# elif defined HYPOXIA_SRM` (121); `#  include <hypoxia_srm_mod.h>` (122); `# elif defined NEMURO` (123); `#  include <nemuro_mod.h>` (124). |
| 125–140 | 시작 시 `#ifdef BIOLOGY` (114) 안이며 `# if defined BIO_FENNEL` (115)에서 시작한 if/elif 사슬의 다음 분기이다. 같은 if/elif 사슬에서 NPZD_FRANKS는 npzd_Franks_mod.h, NPZD_IRON은 npzd_iron_mod.h, NPZD_POWELL은 npzd_Powell_mod.h, RED_TIDE는 red_tide_mod.h를 끼워 넣는다(125–132). 내부 else는 내용 없는 mod_biology 모듈을 선언하고 종료한다(133–136). 바깥 BIOLOGY 불성립 else도 같은 빈 모듈을 선언하고 종료한다(137–140). 전처리 원문: `# elif defined NPZD_FRANKS` (125); `#  include <npzd_Franks_mod.h>` (126); `# elif defined NPZD_IRON` (127); `#  include <npzd_iron_mod.h>` (128); `# elif defined NPZD_POWELL` (129); `#  include <npzd_Powell_mod.h>` (130); `# elif defined RED_TIDE` (131); `#  include <red_tide_mod.h>` (132); `# else` (133); `# endif` (136); `#else` (137); `#endif` (140). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 114–136: 모델 선택은 BIO_FENNEL·ECB·ECOSIM·HYPOXIA_SRM·NEMURO·NPZD_FRANKS·NPZD_IRON·NPZD_POWELL·RED_TIDE 순서의 단일 if/elif 사슬이다. 여러 매크로의 동시 정의를 검사하는 오류 지시문은 이 파일에 없다.
