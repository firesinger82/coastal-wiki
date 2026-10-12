# ShorelineS source-analysis recovery 대조 반영 (2)

입력은 [R1 §4·§5](../compare/ShorelineS-theory-vs-code.md#4-노트-대조와-수정안), [R2 §4·§5](../compare/ShorelineS-inputs-vs-code.md#4-노트-대조와-수정안), [R3 §4·§7·§8](ShorelineS-callflow.md#7-노트-수정안과-확인-범위)이다.
커밋 근거는 [git 판정](../compare/ShorelineS-git-verify.md), [입력 git 판정](../compare/ShorelineS-git-verify-inputs.md), [이론 D 행 git 판정](../compare/ShorelineS-git-verify-dtheory.md)이다.

## 노트별 추가·수정 줄 범위

줄 범위는 최종 노트의 줄 번호이다. 범위는 반영 전 본문과 최종 본문의 줄 대조에서 얻었다. 차이 표 행 수는 각 노트의 `## 문서와 코드 차이 (10-12 대조)` 표에서 센 값이다.

| 노트 | 추가·수정 줄 범위 | 차이 표 행 수 |
|---|---|---|
| [shorelines-architecture-map.md](../../../models/ShorelineS/source-analysis/shorelines-architecture-map.md:7) | 7–8, 21, 23, 25, 27, 29, 31–36, 38, 40, 42–62, 82, 84–85, 94–95, 97–329 | 87 |
| [shorelines-transport-formulations.md](../../../models/ShorelineS/source-analysis/shorelines-transport-formulations.md:2) | 2, 7–8, 19, 23, 25–32, 34–36, 41, 43–44, 47–50, 54–56, 58–96 | 29 |
| [shorelines-coastline-change.md](../../../models/ShorelineS/source-analysis/shorelines-coastline-change.md:7) | 7–8, 22–24, 38–41, 47–49, 51–66 | 6 |
| [shorelines-wave-dune-spit-modules.md](../../../models/ShorelineS/source-analysis/shorelines-wave-dune-spit-modules.md:7) | 7–8, 20–21, 24–33, 38–47, 51–56, 58, 60, 62, 64–105 | 32 |
| [shorelines-diffraction-mud-topology.md](../../../models/ShorelineS/source-analysis/shorelines-diffraction-mud-topology.md:7) | 7–8, 23–27, 31–49, 68, 74–92 | 9 |

모든 담당 노트의 `last_source_check`는 `2026-10-12 (recovery 대조 반영)`이다.
모든 담당 노트의 `verification_method`에는 `2026-10-12 recovery 대조 보고서 R1·R2·R3 반영`을 넣었다.
`citation_status`는 기존 `verified`를 유지했다.

## 노트별 반영한 행 ID

아래 목록은 차이 표, 본문 수정안, 코드 결함 후보 절에 반영한 행 ID를 합친 목록이다.

### shorelines-architecture-map.md

- R1: FT1c, K007, K014, K015, K016, K022, K023, K024, K025, K026, K028, K037, K038, K039, M036, M058, M070, MU20b, MU20c
- R2: F01, F20, K01, K02, K03, K13, K15, K17, K19, K20, K21, N07, N09, N10, N12, N17, N21, N22, N24, N25, P029, P065, P109, P116, P179, P185, P195, P204, U01, U02, U03, U04, U05, U08, U12, U14, U15, U16, U17, U18, U19, U20, U21, U22, U23, U24, U25, V02, V11, V31, V35, V36
- R3: M01, M02, M03, M04, M05, M06, M07, M08, M09, M10, M11, M12, M13, M14, M15, M16, M17, M19, M20, M21, N01, N02, N03, N04, N05, N06, N09, N10, N11, N12, N13, N14, N15, N16, N17, N18, N19, V01, V02, V03, V04, V05, V06

### shorelines-transport-formulations.md

- R1: K002, K006, K007, K008, K011, K012, K013, K015, K030, K031, K032, K033, K037, K038, K043, M035, M036
- R2: K03, K04, K05, K07, K08, K09, N02, N03, N07, N11, N13, N14, N15, N16, N25, U01
- R3: M07, N06

### shorelines-coastline-change.md

- R1: F001, F005, FU01, K001, K029, K032, K036, K042
- R2: K16, N23, U06, U07
- R3: N09, V01

### shorelines-wave-dune-spit-modules.md

- R1: K003, K004, K005, K009, K017, K018, K019, K020, K021, K022, K027, K040, K041, K044, K045, M050a, M050b, M052a, M077, MU20b, MU20c, MU21
- R2: K06, K10, K11, K12, K14, N04, N08, N18, N19, N20, U09, U10, U11, U12, U13, U14, V10, V18
- R3: M16, N10, N11, N12

### shorelines-diffraction-mud-topology.md

- R1: K009, K010, K034, K035, K036, MU12
- R2: K18, N05, N06, N20
- R3: N12, V01

## 노트 수정안 반영

R1 §4의 source-analysis 대상 수정안은 10행이다. 이 값은 R1 §4의 대상 노트 열에서 센 값이다.
R2 §4의 source-analysis 대상 수정안은 9행이다. 이 값은 R2 §4에서 담당 노트의 경로와 줄 번호를 가진 행을 센 값이다.
R2의 해당 행 ID는 N06, N12, N13, N15, N16, N18, N20, N23, N25이다.
R3 §7의 source-analysis 대상 수정안은 10행이다. 이 값은 R3 §7의 대상 노트 열에서 센 값이다.
R3의 해당 행 ID는 N01, N02, N03, N04, N05, N06, N09, N10, N11, N12이다.
R2:N15의 TIDEPROF 지역 `alpha=1.0`과 `gamma=0.78`을 유지했다.
R2:N23의 `MUD.used` 조건을 유지했다.
R3 §7의 시간 루프 교체안을 아키텍처 노트에 넣었다.
사구 시간 구간, QSmax 안정성 간격, 공통 dt, 구간별 수집·복원은 아키텍처 노트의 별도 문단에 넣었다.

## 코드 결함 후보 절

아키텍처 노트의 코드 결함 후보 표는 28행이다. 이 수는 해당 표의 본문 행을 센 값이다.
출처 E 행은 36개이다. 이 수는 R1 §5의 11행, R2 §5의 19행, R3 §8의 6행을 합한 값이다.
다음 목록은 같은 코드 원인으로 묶은 출처 행 ID이다.
- R1:M036 · R1:FT1c
- R1:K024 · R2:P116 · R2:N21
- R1:K025 · R3:V04
- R1:K026 · R2:K21
- R2:P029 · R2:N25
- R2:P179 · R3:V03
- R2:K03 · R2:N07

R1:K026의 중간 강도와 R2:K21의 강한 근거를 같은 표 행에 각각 적었다.
도입 커밋과 날짜는 git 판정 보고서의 기재를 옮겼다.
R1:M036·R1:FT1c, R1:M058, R1:M070의 도입 커밋 칸은 `—`이다. 입력 보고서는 이 항목들의 도입 커밋을 기재하지 않는다.

## 형식과 원문 확인

차이 표는 지정한 여섯 열을 사용한다.
코드 결함 후보 표는 지정한 일곱 열을 사용한다.
새 코드 인용의 원문 문자열을 입력 보고서의 인용과 대조했다.
담당 노트의 상대 링크는 저장소 링크 검증기의 파일 검사로 통과했다.
담당 노트의 링크는 모두 상대 경로이다.
담당 노트에는 금지한 이중 대괄호 문자열이 없다.
R3 §4의 두 Mermaid 코드 블록은 아키텍처 노트의 블록과 바이트 문자열이 같다.
각 상자에는 원문의 file:line을 유지했다.
첫 그림은 렌더된 SVG의 node 요소 18개와 flowchart-link 요소 18개이다.
두 번째 그림은 렌더된 SVG의 node 요소 54개와 flowchart-link 요소 56개이다.
이 수는 로컬 Mermaid 렌더 결과에서 센 값이다.
librsvg로 렌더한 두 그림에서 함수명, 줄 위치, 조건, 구간 반복 연결선을 확인했다.
SVG와 PNG는 메모리에서 처리했다.

## 넣지 않은 행과 이유

담당 범위에서 넣지 않은 행은 없다.
R1·R2의 문서 쪽 M*, MU*, Q*, F*, FT*, I*, IT*, P* 행은 차이 표의 담당 범위 밖이다.
해당 행 중 E 행은 아키텍처 노트의 코드 결함 후보 절에 모두 넣었다.
manual-notes 대상 본문과 models/ShorelineS/README.md는 쓰기 범위 밖이다.
