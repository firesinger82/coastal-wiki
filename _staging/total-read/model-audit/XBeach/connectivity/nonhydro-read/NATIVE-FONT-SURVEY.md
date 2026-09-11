# 보고서 본문 글꼴 정의의 판독

2026-09-11 AI 구조 분석. [영수증](native-font-survey.json), [재현](survey_native_fonts.py), [검증](validate_native_fonts.py).

[Wiris MTEF5 명세](https://docs.wiris.com/en_US/mathtype-mtef-v5-mathtype-40-and-later)의 본문 내 ENCODING_DEF/FONT_DEF/FONT_STYLE_DEF 레코드를 지원했다. 정의 순서와 인코딩/글꼴 인덱스를 검사하며 미정의 참조·지원하지 않는 스타일은 거부한다. 기존 파서와 과거 영수증은 보존한다.

원본 보고서의 388개 Equation Native가 모두 기계적으로 읽힌다. 이전 386개의 구조 출력은 그대로다. 새 두 개는 ObjectPool/_1324462750과 _1324464983이다. 각각 offset 231/387에서 EuclidMath2 인코딩을 정의하고 Euclid Math Two 글꼴과 스타일을 추가한다. 마지막 CHAR는 MTCode F093, typeface -1, font position 84다. 두 구조 전체를 영수증에 저장했다. F093의 시각 모양이나 수학적 의미는 아직 판정하지 않는다. 검사한 시스템 font 목록과 Windows Fonts 경로에서는 해당 Euclid 글꼴을 찾지 못했으며, 다른 경로의 존재 여부까지 단정하지 않는다.

전체 원본 재추출·결과 재현, 388개 고유 스트림 집합, 기존 출력 일치, 새 두 스트림의 전체 절단/후행 데이터 거부, 독립 글꼴 정의 fixture와 미정의 참조/스타일 거부를 검증했다. 본문 배치·작은 네모 글리프·수학적 의미 대조는 남아 있다. 전체 gate NOT_PASSED·신규 사람 승인 없음.
