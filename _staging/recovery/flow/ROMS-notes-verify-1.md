# ROMS 노트 전수 대조 기록 (10-14)

대상 노트는 `models/ROMS/source-analysis/roms_biology-differences-2.md`이다.
대조 범위는 새 파일의 전체 줄이며 frontmatter와 빈 줄을 포함한다.
판정 기준은 원문과 사용자가 지정한 보고서의 최종 검증 기록이다.
완료한 노트의 줄 수, 정정, 보완, 기계 확인 후보 판정을 아래에 기록한다.

## models/ROMS/source-analysis/roms_biology-differences-2.md

대상은 [roms_biology-differences-2.md](../../../models/ROMS/source-analysis/roms_biology-differences-2.md)의 1–169줄이다.
파일 전체 169줄을 대조했다.
정정한 줄은 30줄이다.
인용을 새로 추가한 보완은 0줄이다.
줄 수와 줄 번호는 수정 전후에 같다.
각 수는 대상 파일의 물리 줄과 `[10-14 전수 검증 정정]`·`[10-14 전수 검증 보완]` 표식을 기준으로 셌다.

| 대조 범위 | 줄 수 | 대조 내용과 근거 |
|---|---:|---|
| 1–14 | 14 | frontmatter를 확인했다. 모델 목록과 7파일 구조는 `ROMS/Nonlinear/Biology/biology.F:11–106`에 대응한다. 공통 수송은 `ROMS/Nonlinear/step3d_t.F:405,925,1375`의 전체 추적자 반복과 대응한다. |
| 15–24 | 10 | 부모 노트와 보고서 링크를 확인했다. 위키 수집일은 `manifest.json`의 `fetched_at`과 같다. 코드 HEAD는 `57aecf589a408b1e5490d2db7f9bd0196062a44e`이다. 코드 날짜는 2026-09-18이다. 버전 문자열은 `ROMS/Modules/mod_ncparam.F:653`의 `4.3`이다. |
| 25–26 | 2 | 표 머리글과 구분자의 열 수는 각각 6개이다. |
| 27–120 | 94 | biology의 CF-045부터 CF-138까지 최종 결론과 원문을 대조했다. ECB의 pCO₂ 선택 조건을 정정했다. |
| 121–133 | 13 | biology의 CM-124, NT-002부터 NT-008까지, NT-026, UN-015, UN-016, WK-029, WK-030을 대조했다. 부모 노트 인용은 저장소 HEAD의 반영 전 원문과 대조했다. |
| 134–156 | 23 | outputs-metadata의 배정 행 전체를 대조했다. 변수 이름 생성, 철 경계 인덱스, 과거 변수 이름과 입력 단위를 확인했다. |
| 157–169 | 13 | sediment-ice-vegetation의 배정 행 전체를 대조했다. 굴 유생 조건·단위·식과 Fennel 저층 복귀를 확인했다. |

표의 143행은 [note-job-14.tsv](../assign/note-job-14.tsv)의 해당 노트 배정 143행과 일치한다.
분류는 A 1행, B 12행, C 105행, D 1행, E 6행, F 18행이다.
분류는 각 보고서 §5와 끝의 전수 검증 기록을 반영한 최종 판정과 모두 일치한다.
E 6행의 강도는 강함 4행과 중간 2행이다.
E의 적용 조건과 후보 표현을 유지했다.

결론 116행은 검증 표식을 제외하면 보고서 §5의 문장과 같다.
A인 OMD-SN302는 보고서의 커밋에 작성일을 함께 표기한 행이다.
`98adef8a`의 작성일은 2023-05-17이다.
이 날짜는 [ROMS-git-verify-A7.md:98](../compare/ROMS-git-verify-A7.md)의 판정과 같다.
읽기 전용 `git show`에서 `river_alkalinity`를 `river_TAlk`로 바꾼 변경도 확인했다.
나머지 결론 26행은 보고서의 분류와 판단을 유지하면서 원문의 조건·계수 이름·단위 변환에 맞게 정정했다.
해당 26행은 ECB 24행과 RBO1-007·RBO1-003이다.

수정 후 인용 위치 5,137회를 원문과 대조했다.
이 수는 현재 코드 5,048회, 위키 55회, 부모 노트 HEAD 15회, 과거 코드 19회의 합이다.
중복을 제외한 위치는 4,290개이다.
인용 대상의 파일·판 조합은 60개이다.
백틱 인용과 HTML code 인용을 함께 확인했다.
백틱 인용 없이 적힌 `ROMS/External/varinfo.yaml:2760`의 검색 결과도 원문과 일치한다.
수정 후 인용문과 줄 번호의 불일치는 0건이다.

`ROMS/`·`User/`·`Data/`의 기준은 `models/ROMS/raw/source_code/roms/`이다.
아래의 `HEAD:models/ROMS/source-analysis/roms_biology.md`는 저장소 루트의 HEAD 판이다.
위키 인용의 기준은 `models/ROMS/raw/manuals/wiki/wikitext/`이다.

### 정정 목록

각 행은 변경한 한 줄을 기록한다.
전·후 칸은 해당 줄에서 바꾼 부분이다.
모든 정정 표식은 대상 노트의 결론 문장 칸 끝에 붙였다.

| 노트 위치와 행 ID | 전 | 후 | 근거 원문 |
|---|---|---|---|
| [roms_biology-differences-2.md:81](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-099 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되면 pCO2_water_RZ를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`와 `ROMS/Nonlinear/Biology/ecb.h:1380`의 `CALL pCO2_water_RZ`. |
| [roms_biology-differences-2.md:82](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-100 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되면 pCO2_water_RZ를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`와 `ROMS/Nonlinear/Biology/ecb.h:1380`의 `CALL pCO2_water_RZ`. |
| [roms_biology-differences-2.md:83](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-101 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되면 pCO2_water_RZ를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`와 `ROMS/Nonlinear/Biology/ecb.h:1380`의 `CALL pCO2_water_RZ`. |
| [roms_biology-differences-2.md:84](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-102 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되면 pCO2_water_RZ를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`와 `ROMS/Nonlinear/Biology/ecb.h:1380`의 `CALL pCO2_water_RZ`. |
| [roms_biology-differences-2.md:85](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-103 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되면 pCO2_water_RZ를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`와 `ROMS/Nonlinear/Biology/ecb.h:1380`의 `CALL pCO2_water_RZ`. |
| [roms_biology-differences-2.md:86](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-104 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되면 pCO2_water_RZ를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`와 `ROMS/Nonlinear/Biology/ecb.h:1380`의 `CALL pCO2_water_RZ`. |
| [roms_biology-differences-2.md:87](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-105 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되면 pCO2_water_RZ를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`와 `ROMS/Nonlinear/Biology/ecb.h:1380`의 `CALL pCO2_water_RZ`. |
| [roms_biology-differences-2.md:88](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-106 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되면 pCO2_water_RZ를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`와 `ROMS/Nonlinear/Biology/ecb.h:1380`의 `CALL pCO2_water_RZ`. |
| [roms_biology-differences-2.md:89](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-107 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되면 pCO2_water_RZ를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`와 `ROMS/Nonlinear/Biology/ecb.h:1380`의 `CALL pCO2_water_RZ`. |
| [roms_biology-differences-2.md:90](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-108 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되면 pCO2_water_RZ를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`와 `ROMS/Nonlinear/Biology/ecb.h:1380`의 `CALL pCO2_water_RZ`. |
| [roms_biology-differences-2.md:91](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-109 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ가 정의되지 않은 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되지 않으면 pCO2_water를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`, `ROMS/Nonlinear/Biology/ecb.h:1388`의 `#else`, `ROMS/Nonlinear/Biology/ecb.h:1389`의 `CALL pCO2_water`. |
| [roms_biology-differences-2.md:92](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-110 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ가 정의되지 않은 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되지 않으면 pCO2_water를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`, `ROMS/Nonlinear/Biology/ecb.h:1388`의 `#else`, `ROMS/Nonlinear/Biology/ecb.h:1389`의 `CALL pCO2_water`. |
| [roms_biology-differences-2.md:93](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-111 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ가 정의되지 않은 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되지 않으면 pCO2_water를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`, `ROMS/Nonlinear/Biology/ecb.h:1388`의 `#else`, `ROMS/Nonlinear/Biology/ecb.h:1389`의 `CALL pCO2_water`. |
| [roms_biology-differences-2.md:94](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-112 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ가 정의되지 않은 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되지 않으면 pCO2_water를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`, `ROMS/Nonlinear/Biology/ecb.h:1388`의 `#else`, `ROMS/Nonlinear/Biology/ecb.h:1389`의 `CALL pCO2_water`. |
| [roms_biology-differences-2.md:95](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-113 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ가 정의되지 않은 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되지 않으면 pCO2_water를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`, `ROMS/Nonlinear/Biology/ecb.h:1388`의 `#else`, `ROMS/Nonlinear/Biology/ecb.h:1389`의 `CALL pCO2_water`. |
| [roms_biology-differences-2.md:96](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-114 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ가 정의되지 않은 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되지 않으면 pCO2_water를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`, `ROMS/Nonlinear/Biology/ecb.h:1388`의 `#else`, `ROMS/Nonlinear/Biology/ecb.h:1389`의 `CALL pCO2_water`. |
| [roms_biology-differences-2.md:97](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-115 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ가 정의되지 않은 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되지 않으면 pCO2_water를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`, `ROMS/Nonlinear/Biology/ecb.h:1388`의 `#else`, `ROMS/Nonlinear/Biology/ecb.h:1389`의 `CALL pCO2_water`. |
| [roms_biology-differences-2.md:98](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-116 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ가 정의되지 않은 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되지 않으면 pCO2_water를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`, `ROMS/Nonlinear/Biology/ecb.h:1388`의 `#else`, `ROMS/Nonlinear/Biology/ecb.h:1389`의 `CALL pCO2_water`. |
| [roms_biology-differences-2.md:99](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-117 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ가 정의되지 않은 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되지 않으면 pCO2_water를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`, `ROMS/Nonlinear/Biology/ecb.h:1388`의 `#else`, `ROMS/Nonlinear/Biology/ecb.h:1389`의 `CALL pCO2_water`. |
| [roms_biology-differences-2.md:100](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-118 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ가 정의되지 않은 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되지 않으면 pCO2_water를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`, `ROMS/Nonlinear/Biology/ecb.h:1388`의 `#else`, `ROMS/Nonlinear/Biology/ecb.h:1389`의 `CALL pCO2_water`. |
| [roms_biology-differences-2.md:101](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-119 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ가 정의되지 않은 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되지 않으면 pCO2_water를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`, `ROMS/Nonlinear/Biology/ecb.h:1388`의 `#else`, `ROMS/Nonlinear/Biology/ecb.h:1389`의 `CALL pCO2_water`. |
| [roms_biology-differences-2.md:102](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-120 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ가 정의되지 않은 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되지 않으면 pCO2_water를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`, `ROMS/Nonlinear/Biology/ecb.h:1388`의 `#else`, `ROMS/Nonlinear/Biology/ecb.h:1389`의 `CALL pCO2_water`. |
| [roms_biology-differences-2.md:103](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-121 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ가 정의되지 않은 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되지 않으면 pCO2_water를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`, `ROMS/Nonlinear/Biology/ecb.h:1388`의 `#else`, `ROMS/Nonlinear/Biology/ecb.h:1389`의 `CALL pCO2_water`. |
| [roms_biology-differences-2.md:104](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:CF-122 | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되면 pCO2_RZ가 정의되지 않은 분기가 활성화된다. ` | ` NONLINEAR·BIOLOGY 조건에서 ECB가 선택되고 pCO2_RZ가 정의되지 않으면 pCO2_water를 사용한다. ` | `ROMS/Nonlinear/Biology/ecb.h:1379`의 `#ifdef pCO2_RZ`, `ROMS/Nonlinear/Biology/ecb.h:1388`의 `#else`, `ROMS/Nonlinear/Biology/ecb.h:1389`의 `CALL pCO2_water`. |
| [roms_biology-differences-2.md:124](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:NT-004 | ` verification_method: "ROMS/Nonlinear/Biology/ ` | ` verification_method: "models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/ ` | `HEAD:models/ROMS/source-analysis/roms_biology.md:6`의 `models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/`. |
| [roms_biology-differences-2.md:125](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:NT-005 | ` verification_method: "ROMS/Nonlinear/Biology/ ` | ` verification_method: "models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/ ` | `HEAD:models/ROMS/source-analysis/roms_biology.md:6`의 `models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/`. |
| [roms_biology-differences-2.md:129](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · biology:NT-026 | ` - 본 노트 = **프레임워크 + 모델 카탈로그 + Fennel/NPZD 구조** 레벨. 개별 모델의 reaction rate 식 line-by-line(fennel.h 2375 등)은 미포함(후속 deep 후보). ` | ` - 본 노트 = **프레임워크 + 모델 카탈로그 + Fennel/NPZD 구조** 레벨. ` | `HEAD:models/ROMS/source-analysis/roms_biology.md:73`의 첫 문장. [biology 보고서:1541,2032](../compare/roms-biology-vs-code.md)의 NT-026 수정안. |
| [roms_biology-differences-2.md:154](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · outputs-metadata:OMD-SN245 | ``` `ROMS/Nonlinear/Biology/ecosim_var.h:522` ``<br>ROMS/Nonlinear/Biology/ecosim_var.h:523 `#ifdef DIAGNOSTICS_BIO`<br>ROMS/Nonlinear/Biology/ecosim_var.h:524 `` ``` | `` `ROMS/Nonlinear/Biology/ecosim_var.h:523` `#ifdef DIAGNOSTICS_BIO` `` | `ROMS/Nonlinear/Biology/ecosim_var.h:522,524`는 빈 줄이다. `ROMS/Nonlinear/Biology/ecosim_var.h:523`은 `#ifdef DIAGNOSTICS_BIO`이다. |
| [roms_biology-differences-2.md:158](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · sediment-ice-vegetation:RBO1-007 | ` 탁도 인자 turb_ef와 그 절편·최대값은 무차원이다. ` | ` 탁도 인자 turb_ef와 선형 절편 turb_axis 및 지수식 계수 turb_base는 무차원이다. ` | `ROMS/Nonlinear/Biology/oyster_floats.h:327–330`의 지수식과 선형식. `User/External/behavior_oyster.in:302`의 `Turbidity base factor, {b}`. [sediment 보고서:1093,1491](../compare/roms-sediment-ice-vegetation-vs-code.md)의 판정 이유. |
| [roms_biology-differences-2.md:164](../../../models/ROMS/source-analysis/roms_biology-differences-2.md) · sediment-ice-vegetation:RBO1-003 | ` Lsize>turb_size에서 조회 성장률*Gfactor*turb_ef를 사용한다. Lsize≤turb_size에서는 Larvae_GR0*Gfactor를 사용한다. ` | `` `IF (Lsize.gt.turb_size(ng)) THEN`에서는 `track(ibrhs,nfp1,l)=Grate*Gfactor*turb_ef*sec2day`를 사용한다. ELSE에서는 `track(ibrhs,nfp1,l)=Larvae_GR0(ng)*Gfactor*sec2day`를 사용한다. `` | `ROMS/Nonlinear/Biology/oyster_floats.h:325,332–334`의 조건문과 두 성장률 식. [sediment 보고서:1084,1592](../compare/roms-sediment-ice-vegetation-vs-code.md)의 원문 인용. |

### 기계 확인 후보 판정

| 후보 | 대상 위치 | 판정 | 근거와 조치 |
|---|---|---|---|
| HEAD@wiki의 부모 노트 6줄 인용 첫 번째 | `models/ROMS/source-analysis/roms_biology-differences-2.md:124` · biology:NT-004 | 실제 불일치 | 원문 경로의 `models/ROMS/raw/source_code/roms/`가 빠져 있어 복원했다. |
| HEAD@wiki의 부모 노트 6줄 인용 두 번째 | `models/ROMS/source-analysis/roms_biology-differences-2.md:125` · biology:NT-005 | 실제 불일치 | 원문 경로의 `models/ROMS/raw/source_code/roms/`가 빠져 있어 복원했다. |
| `behavior_oyster.in.wiki:22`의 `for turbidity < 0.1 g/l` | `models/ROMS/source-analysis/roms_biology-differences-2.md:165` · sediment-ice-vegetation:RBO1-006 | 오탐 | 원문 span 안의 표시 글자가 인용과 같으므로 유지했다. |

### 최종 확인

- 노트의 상대 링크 7개는 모두 실제 파일을 가리킨다.
- 보고서 링크의 `5-차이-결론` 절도 모두 존재한다.
- frontmatter의 related는 실제 부모 노트를 가리킨다.
- 대상 노트에 mermaid 블록은 없다.
- 대상 노트에 사용자 홈 절대 경로와 이중 대괄호는 없다.
- 대상 노트에서 후속 작업 한계 문구를 제거했다.
- 대상 노트에 실행·확인 미수행이나 미검수를 선언하는 한계 문장은 없다.
- 외부 원문 보고서의 마지막 「Claude 확인과 보완」에는 이 노트의 행 ID가 없다.
- A 판정은 [ROMS-git-verify-A7.md](../compare/ROMS-git-verify-A7.md)의 OMD-SN302와 대조했다.
- D 판정은 [ROMS-git-verify-D1.md](../compare/ROMS-git-verify-D1.md)의 OMD-Y241과 대조했다.
- E 판정은 biology 최종 검증 기록과 [ROMS-git-verify-E1.md](../compare/ROMS-git-verify-E1.md)·[ROMS-git-verify-E2.md](../compare/ROMS-git-verify-E2.md)의 해당 행과 대조했다.
- 변경한 30줄 외의 139줄은 작업 시작본과 같다.
- 수정 후 표 143행은 모두 6열을 유지한다.
- 대상 노트에 줄 끝 공백은 없다.
- 지정한 두 파일에 대한 `git diff --check HEAD`는 통과했다.

상태: 완료.
미해결 항목: 0건.
