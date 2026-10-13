---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/biology.F
lines: 131
sha256: e539db3e3211e69f84892f47535381c7e52ab1dad440fd953eee26b7ab591dcb
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# biology.F — 판독 구간 기록

구간은 1행부터 131행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | 1행은 `cppdefs.h`를 끼워 넣는다. NONLINEAR와 BIOLOGY가 모두 정의된 전처리 경로를 연다(2). 빈 줄·C 형식 주석 시작·git 식별자·구분선(3–7). 생태계 모형(ecosystem model)을 사용자가 수정·추가할 수 있다는 설계 설명 주석(8–10). 전처리 원문: `#include "cppdefs.h"` (1); `#if defined NONLINEAR && defined BIOLOGY` (2). |
| 11–36 | 시작 시 2행 `#if defined NONLINEAR && defined BIOLOGY` 안. 생태계 모형이 일곱 종류의 파일로 구성된다는 주석(11). 첫 종류는 source·sink 이산화(discretization) 방정식 헤더이다(13–23). ecb.h·ecosim.h·fennel.h·hypoxia_srm.h·nemuro.h·npzd_Franks.h·npzd_iron.h·npzd_Powell.h·red_tide.h와 대응 선택 매크로를 나열한다(15–23). 두 번째 종류는 내부 매개변수 선언의 *_mod.h이다(25–35). 이 목록은 주석이며 include 실행문은 아니다. |
| 37–60 | 시작 시 2행 `#if defined NONLINEAR && defined BIOLOGY` 안. 세 번째 종류는 매개변수 표준 입력 스크립트(standard input script) 목록이다(37–47). bio_ECB.in·ecosim.in·bio_Fennel.in·hypoxia_srm.in·nemuro.in·npzd_Franks.in·npzd_iron.in·npzd_Powell.in·red_tide.in을 나열한다(39–47). 네 번째 종류는 입력 매개변수를 읽는 *_inp.h 목록이다(49–59). 구분 주석·빈 주석 포함. |
| 61–86 | 시작 시 2행 `#if defined NONLINEAR && defined BIOLOGY` 안. 다섯 번째 종류는 `varinfo.yaml` 메타데이터(metadata)를 읽으면서 모형 변수 인덱스를 지정하는 *_var.h 목록이다(61–72). 여섯 번째 종류는 모든 출력 NetCDF 파일에 입력 매개변수를 정의하는 *_def.h 목록이다(74–85). 각각 앞 목록의 아홉 모형에 해당하는 파일명을 주석으로 나열한다. 빈 주석 포함. |
| 87–108 | 시작 시 2행 `#if defined NONLINEAR && defined BIOLOGY` 안. 일곱 번째 종류는 출력 NetCDF 파일에 입력 매개변수를 쓰는 *_wrt.h 목록이다(87–98). 헤더 파일은 ROMS/Nonlinear/Biology에 있고, 꺾쇠 괄호 include를 통해 프로젝트 디렉터리에서 수정본을 사용할 수 있다는 주석(101–104). 빌드 스크립트를 확인하라는 문구가 있다(104). 그 스크립트 내부는 이 판독 범위에 포함하지 않았다. C 주석 종료와 빈 줄(105–108). |
| 109–127 | 시작 시 2행 `#if defined NONLINEAR && defined BIOLOGY` 안. 하나의 #if/#elif 체인으로 생태계 모형 헤더를 선택한다. BIO_FENNEL은 `fennel.h`(109–110), ECB는 `ecb.h`(111–112), ECOSIM은 `ecosim.h`(113–114), HYPOXIA_SRM은 `hypoxia_srm.h`(115–116), NEMURO는 `nemuro.h`(117–118), NPZD_FRANKS는 `npzd_Franks.h`(119–120), NPZD_IRON은 `npzd_iron.h`(121–122), NPZD_POWELL은 `npzd_Powell.h`(123–124), RED_TIDE는 `red_tide.h`(125–126)를 끼워 넣는다. 127행은 내부 선택 조건을 닫는다. 포함 파일 내부는 이 판독 범위에 포함하지 않았다. 전처리 원문: `# if defined BIO_FENNEL` (109); `#  include <fennel.h>` (110); `# elif defined ECB` (111); `#  include <ecb.h>` (112); `# elif defined ECOSIM` (113); `#  include <ecosim.h>` (114); `# elif defined HYPOXIA_SRM` (115); `#  include <hypoxia_srm.h>` (116); `# elif defined NEMURO` (117); `#  include <nemuro.h>` (118); `# elif defined NPZD_FRANKS` (119); `#  include <npzd_Franks.h>` (120); `# elif defined NPZD_IRON` (121); `#  include <npzd_iron.h>` (122); `# elif defined NPZD_POWELL` (123); `#  include <npzd_Powell.h>` (124); `# elif defined RED_TIDE` (125); `#  include <red_tide.h>` (126); `# endif` (127). |
| 128–131 | 시작 시 2행 `#if defined NONLINEAR && defined BIOLOGY` 안. 128행 ELSE는 NONLINEAR와 BIOLOGY가 모두 정의된 조건의 불성립 경로이다. 본문 없는 `MODULE biology_mod`와 `END MODULE biology_mod`를 둔다(129–130). 131행은 바깥 전처리 조건을 닫는다. 전처리 원문: `#else` (128); `#endif` (131). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 109–127: 생태계 모형 선택 체인에는 최종 #else가 없다. 바깥 NONLINEAR·BIOLOGY 조건이 참이어도 나열한 모형 매크로 중 하나도 정의되지 않으면 이 체인에서 헤더를 끼워 넣지 않는다. 빈 biology_mod 모듈은 바깥 조건의 불성립 경로에만 있다(128–131).
