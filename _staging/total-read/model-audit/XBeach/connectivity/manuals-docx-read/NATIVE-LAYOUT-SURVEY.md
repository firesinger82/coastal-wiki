# 수식 배치 레코드의 한정 판독

2026-09-11 AI 구조 분석. [영수증](native-layout-survey.json), [판독기](inspect_layout_records.py), [재현](survey_native_layout.py), [검증](validate_native_layout.py).

[Wiris MTEF5 명세](https://docs.wiris.com/en_US/mathtype-mtef-v5-mathtype-40-and-later)의 공식 검색 인덱스 발췌를 대조했다. 비이동 행렬, 이름 없는 process RGB, 세 가지 SIZE 형식, LINE/PILE의 명시적 RULER를 한정 지원한다. 행렬은 행×열과 LINE 수를 대조하고, 경계선 packed 바이트는 비트 순서를 추정하지 않고 보존한다. RGB 성분은 범위를 검사하며 색상 참조는 앞서 정의된 1 이상 인덱스만 허용한다. SIZE의 명시 크기는 부호 있는 원시 값을 보존한다.

기존 수용 441개 출력은 동일하고 18개가 추가되어 459개를 기계적으로 수용했다. 남은 27개는 색상 인덱스 0을 포함한 정의되지 않은 참조 12개, 예상 RULER 태그 불일치 8개, 이동 보정/줄 간격 옵션 4개, 접두부 미해결 3개다. 색상 0을 임의 기본색으로 처리한 중간 시도는 채택하지 않았다. 이 거부 결과는 원본 손상 판정이 아니다.

전체 재추출·재현, 기존 출력 일치, 실제 새 레코드별 절단·후행 바이트 거부, 독립 행렬/RGB/RULER/SIZE fixture와 잘못된 개수·옵션·참조·범위 거부를 검증한다. RULER 구현의 fixture 통과를 원본의 불일치 8개 해결로 해석하지 않는다. 원본·과거 파서·영수증 유지. 전체 gate NOT_PASSED·신규 사람 승인 없음. 수학적 의미와 렌더 충실도는 별도 확인 대상이다.
