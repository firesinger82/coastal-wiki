# 수식 이동 보정의 한정 판독

2026-09-11 AI 구조 분석. [영수증](native-nudge-survey.json), [판독기](inspect_nudge_records.py), [검증](validate_native_nudge.py).

[Wiris MTEF5 공식 명세](https://docs.wiris.com/en_US/mathtype-mtef-v5-mathtype-40-and-later)의 검색 인덱스 발췌로 nudge의 2/6바이트 형식을 확인했다. LINE/CHAR/TMPL/PILE의 위치 보정과 LINE 간격 필드를 읽어 원시 값·바이트 위치를 보존한다. 이동 보정이 있는 MATRIX/EMBELL은 여전히 미지원이다. 옵션 12를 줄 간격으로 일괄 해석하지 않으며 CHAR에서는 이동 보정과 8비트 font encoding의 조합이다.

4개 추가 수용으로 현재 463개 기계적 수용·본문 미지원 20개·접두부 미해결 3개다. 기존 459개의 전체 구조 출력은 동일하다. 남은 본문은 색상 참조 12개·RULER 불일치 8개다. 기존 판독기·영수증·원본은 유지한다. 전체 gate NOT_PASSED·신규 사람 승인 없음.

검증: 전체 재추출/재현과 기존 출력 대조, 새 원본의 절단/후행 바이트 거부, 독립 short/long nudge 및 LINE 간격 순서 fixture, 미지원 옵션 거부. 위치 값의 구조 판독을 렌더 픽셀 일치나 수학적 의미 검증으로 간주하지 않는다.
