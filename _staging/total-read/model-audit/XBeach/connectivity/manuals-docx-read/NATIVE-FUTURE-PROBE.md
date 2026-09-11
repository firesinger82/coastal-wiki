# Master 확장 접두부의 구조 판독

2026-09-11 AI 분석. [근거](native-future-probe.json), [재현](probe_future_prefix.py), [검증](validate_future_probe.py).

[Wiris MTEF5 명세](https://docs.wiris.com/en_US/mathtype-mtef-v5-mathtype-40-and-later)의 FUTURE 레코드는 길이를 저장한다. Master oleObject1/45/48의 offset 41에는 tag 100, 길이 3, payload 000000이 있다. payload는 해석하지 않고 바이트 그대로 보존했다. 그 뒤 설정을 끝까지 읽으면 본체 시작은 세 개 모두 offset 204이며 본문 구조를 읽을 수 있다. 원본에서 추출해 재현하고 확장 길이·절단·과대 길이·후행 바이트를 검사한다.

이 세 개는 원래 Master (2.1)/(2.40)/(2.43)의 본문 렌더가 누락되어 EMF로 보충했던 오브젝트다. 파생 구조 JSON은 영수증에 저장했다. 문자 순회는 평탄한 수학식 직렬화가 아니다. 확장 payload의 의미 및 렌더 충실도는 미해결이다. 기존 463개와 합쳐 466개 본문 구조를 읽었지만, 세 개를 무조건 판독 완료로 올리지 않는다. 기존 원본/파서/영수증 보존, 전체 gate NOT_PASSED·신규 사람 승인 없음.
