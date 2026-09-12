# 조건부 수식 20개의 원본 미리보기 대조

2026-09-12 AI 시각 판독. [영수증](receipt.json)에 원본 DOCX/문단/관계 ID/WMF와 렌더 PDF·PNG 해시를 저장했다. 네 contact sheet에 있는 20개를 모두 확인했다. 원본 WMF는 LibreOffice Draw로 PDF 변환하고 pdftoppm 180 dpi로 표시했다. 추출·렌더 재현은 상위 `render_conditional_previews.py`이며 검토 영수증을 덮어쓰지 않고 preparation.json을 만든다.

수식들은 지하수 침투·수평 흐름, 속도 크기와 시간 필터, 평형 농도, 임계 속도 혼합, 방향 분산 관계다. 본체는 모두 보이고 이 검사 크기에서 새로운 네모 글리프는 관측하지 않았다. 개별 관측은 영수증에 있다.

원본 표기 문제를 확인했다. Kingsday oleObject133/Master143의 첫 침투식과 Master81의 침투식은 분수 뒤 `1` 앞에 연산자가 보이지 않으며 Native 문자 목록에도 그 위치의 +/minus가 없다. Kingsday70 대응식은 d_infill과 +1을 쓰고, Master81은 delta_infill을 쓴다. 판본을 섞어 자동 수정하거나 수학적 의도를 추정하지 않았다.

색상 인덱스 0의 의미나 태그 없는 RULER 해석이 규격상 확정됐다는 뜻은 아니다. Native 문자 순회 문자열은 진단용이며 분수·근호·첨자 구조를 평탄한 수식으로 읽으면 안 된다. 모든 수식의 수학적 검증·전체 모델 판독 완료와도 구분한다. 원본/과거 영수증·전체 gate NOT_PASSED 유지, 신규 사람 승인 없음.
