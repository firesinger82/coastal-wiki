# ShorelineS recovery 대조 반영 기록 1

기준일은 2026-10-12이다.
입력은 [R1 이론 대조](../compare/ShorelineS-theory-vs-code.md#4-노트-대조와-수정안), [R2 입력 대조](../compare/ShorelineS-inputs-vs-code.md#4-노트-대조와-수정안), [R3 호출 흐름 대조](ShorelineS-callflow.md#7-노트-수정안과-확인-범위)의 최종 결론이다.
커밋 근거는 [git 판정](../compare/ShorelineS-git-verify.md), [입력 git 판정](../compare/ShorelineS-git-verify-inputs.md), [D 행 git 판정](../compare/ShorelineS-git-verify-dtheory.md)에 연결한다.

## 노트별 추가·수정 줄 범위

줄 번호는 최종 노트의 줄 번호이다.
범위에는 이전 실행의 반영분을 포함한다.

| 노트 | 추가·수정 줄 범위 |
|---|---|
| [매뉴얼](../../../models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md) | models/ShorelineS/manual-notes/shorelines-technical-manual-v1.md:7–8, 24, 28, 60–62, 66–72, 76–85, 98–100, 102–104, 108, 113–117, 129–131, 140–141, 145–147, 150–154, 156, 158–160, 165–169, 173–179, 183–185, 187, 191, 199, 217, 235–236, 239–240, 243, 249, 262–501 |
| [FAQ](../../../models/ShorelineS/manual-notes/shorelines-faq-operational.md) | models/ShorelineS/manual-notes/shorelines-faq-operational.md:7–8, 29–32, 45, 49, 56–111 |
| [2018·2020 논문](../../../models/ShorelineS/manual-notes/shorelines-roelvink2020-frontiers.md) | models/ShorelineS/manual-notes/shorelines-roelvink2020-frontiers.md:7–8, 21, 25, 28, 32–33, 35, 37–38, 40, 42, 48–115 |
| [모델 README](../../../models/ShorelineS/README.md) | models/ShorelineS/README.md:1–5, 10, 18, 21, 26, 28, 30–32, 45, 49–60 |

이번 재개는 매뉴얼 129–131줄의 twopoints 설명을 보완했다.
매뉴얼 145–147줄은 투과파 회전량의 1-Kt 조건을 반영한다.
매뉴얼 235줄과 262줄은 입력 rotfac의 저장과 지역 rotfac의 계산을 구분한다.
R2:N03의 표 행은 매뉴얼 PDF 62쪽을 문서 근거로 사용한다.
이 행은 매뉴얼 노트 384줄에 둔다.
FAQ 49줄의 입력명 수정은 유지한다.
논문 노트와 모델 README의 기존 반영분은 유지한다.

## 반영한 차이 행 ID

아래 수는 담당 노트 차이 표의 고유 행 ID를 센 값이다.

| 보고서 | 반영 행 수 |
|---|---:|
| R1 | 144 |
| R2 | 116 |
| R3 | 27 |
| 합계 | 287 |

### R1

매뉴얼: R1:M002, R1:MU01, R1:M003a, R1:M003b, R1:MU02, R1:M005, R1:M006, R1:M007, R1:M009, R1:M013, R1:M015, R1:M018, R1:M019, R1:M020, R1:M021, R1:M022, R1:M024a, R1:M024b, R1:M025a, R1:M025b, R1:M026a, R1:M026b, R1:M026c, R1:M026d, R1:M027b, R1:M028, R1:M029, R1:M033, R1:M034, R1:M035, R1:MU03, R1:MU05, R1:M036, R1:M037, R1:M038, R1:MU07, R1:M039a, R1:M039c, R1:M039d, R1:M040, R1:MU08, R1:M045, R1:M046, R1:M049, R1:M050a, R1:M050b, R1:M050c, R1:M051, R1:M052a, R1:M053, R1:M054, R1:M055, R1:MU09, R1:MU11, R1:M058, R1:M059, R1:M060, R1:MU12, R1:M061, R1:M062, R1:M063, R1:M064, R1:M065, R1:MU14, R1:MU15b, R1:MU16a, R1:MU16b, R1:MU16c, R1:MU16d, R1:MU16e, R1:M067, R1:MU17, R1:M070, R1:MU18, R1:M071, R1:M072, R1:M073, R1:M074, R1:M075, R1:M076, R1:M077, R1:M078, R1:MU20b, R1:MU20c, R1:MU20d, R1:MU20e, R1:MU21, R1:MU22.

FAQ: R1:Q01, R1:Q02, R1:Q03, R1:Q05a, R1:Q05b, R1:Q05c, R1:Q06, R1:Q07, R1:Q08, R1:Q09.

논문: R1:I01, R1:IT1a, R1:IT1b, R1:IT1c, R1:IT1d, R1:I02, R1:I03, R1:I04, R1:I05, R1:I06, R1:I07a, R1:I07b, R1:I08a, R1:I08b, R1:I08c, R1:I08d, R1:I08e, R1:F002, R1:F003, R1:F004, R1:F005, R1:FU01, R1:F006a, R1:F006b, R1:F007, R1:F008, R1:F009, R1:F010, R1:F011, R1:F012, R1:F013, R1:F014, R1:F015a, R1:F015b, R1:F015c, R1:F015d, R1:F015e, R1:FU02a, R1:FU02b, R1:FU02c, R1:FU02d, R1:FU02e, R1:FT1a, R1:FT1b, R1:FT1c, R1:FT1d.

### R2

매뉴얼: R2:P005, R2:P009, R2:P013, R2:P014, R2:P015, R2:P024, R2:P027, R2:P029, R2:P037, R2:P038, R2:P039, R2:P043, R2:P051, R2:P056, R2:P060, R2:P064, R2:P065, R2:P078, R2:P098, R2:P101, R2:P109, R2:P116, R2:P117, R2:P118, R2:P120, R2:P121, R2:P129, R2:P131, R2:P139, R2:P141, R2:P147, R2:P148, R2:P169, R2:P170, R2:P172, R2:P173, R2:P179, R2:P185, R2:P186, R2:P187, R2:P188, R2:P195, R2:P203, R2:P204, R2:P205, R2:P207, R2:P221, R2:P232, R2:P233, R2:P234, R2:P235, R2:P236, R2:P237, R2:U13, R2:K02, R2:K03, R2:K06, R2:K12, R2:K13, R2:K14, R2:K17, R2:F01, R2:F03, R2:F04, R2:F05, R2:F06, R2:F07, R2:F10, R2:F11, R2:F12, R2:F13, R2:F18, R2:F19, R2:F20, R2:F23, R2:F28, R2:F31, R2:N03, R2:N04, R2:N05, R2:N06, R2:N07, R2:N08, R2:N09, R2:N10, R2:N12, R2:N13, R2:N17, R2:N18, R2:N19, R2:N20, R2:N21, R2:N22, R2:F34, R2:F35, R2:K20, R2:K21, R2:N25.

FAQ: R2:K01, R2:K04, R2:K05, R2:K07, R2:K08, R2:K09, R2:K10, R2:K11, R2:K15, R2:K16, R2:K18, R2:K19, R2:F09, R2:F14, R2:N02, R2:N24.

논문: R2:N14.

모델 README: R2:N11.

### R3

매뉴얼: R3:M01, R3:M02, R3:M03, R3:M04, R3:M05, R3:M06, R3:M07, R3:M08, R3:M09, R3:M10, R3:M11, R3:M12, R3:M13, R3:M14, R3:M15, R3:M16, R3:M17, R3:M19, R3:M20, R3:M21, R3:N15, R3:N16.

FAQ: R3:N17.

논문: R3:N13, R3:N14.

모델 README: R3:N18, R3:N19.

## 노트 수정안 반영

R1 §4의 담당 노트 수정안은 위 본문 줄 범위에 반영했다.
차이 표 목록 외에 본문 수정안으로 연결한 R1 행 ID는 R1:F001, R1:K002, R1:K005, R1:K007, R1:K008, R1:K009, R1:K010, R1:K013, R1:K014, R1:K017, R1:K022, R1:K024, R1:K032, R1:K034, R1:K035, R1:K037, R1:K038, R1:K040, R1:K041, R1:M001이다.
R2 §4의 담당 노트 수정안은 위 본문 줄 범위에 반영했다.
R2:N01은 FAQ 24줄의 griddingmethod=2 전용 smoothfac 설명을 유지했다.
R3 §7의 담당 노트 수정안은 논문 37·42줄, 매뉴얼 81·85줄, FAQ 30줄, 모델 README 28·30–32줄에 반영했다.

## 담당 범위 중 넣지 않은 행

없음.
R1 §5, R2 §5, R3 §8의 담당 행 ID와 담당 노트의 차이 표를 대조했다.
각 차이 행 ID는 담당 노트의 차이 표 한 곳에 있다.
결론 분류와 결론 문장을 최종 보고서와 대조했다.
식과 조건문은 Markdown 표의 이스케이프를 제거한 뒤 원문과 대조했다.
네 노트의 last_source_check는 `2026-10-12 (recovery 대조 반영)`이다.
네 노트의 verification_method에는 `2026-10-12 recovery 대조 보고서 R1·R2·R3 반영`이 한 번씩 있다.
citation_status의 기존값은 유지했다.
