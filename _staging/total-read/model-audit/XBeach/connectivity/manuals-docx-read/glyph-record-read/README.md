# 선택 수식의 Native 문자·구조 판독

2026-09-11 AI 분석. 원본 바이트(`*.bin`)와 파생 구조 판독(`*.json`)을 구분한다. [영수증](receipt.json)은 이전 원본 preview/OLE 추출 근거와 원본 DOCX SHA에 결속된다.

- Kingsday/Master (2.5): 441바이트 Native의 offset 322·430에 MTCode 0x223C `∼`, typeface 11, font position 58이 있다. selector 29 템플릿의 두 번째 LINE에 들어 있다. 원본 WMF 렌더의 네모 위첨자 위치에 대응하지만 렌더 실패의 정확한 원인은 확인하지 않았다.
- Kingsday B.37/Master C.37: 721바이트 Native 첫 PILE 줄의 offset 464에 `0`, 469에 `a`가 연속 CHAR 레코드로 존재한다. 둘째 줄은 `0`으로 끝난다. 따라서 a는 원본에 저장된 문자다. 오타인지 다른 의미인지는 미확정이며 삭제하지 않았다.

한정 파서는 [Wiris MTEF5 명세](https://docs.wiris.com/en_US/mathtype-mtef-v5-mathtype-40-and-later)의 앞서 조회한 검색 인덱스 발췌를 따른다. 전체 명세를 내려받았다고 주장하지 않는다. 접두부 28바이트는 불투명하게 보존한다. 설정 영역 검증에만 합성 END를 붙이며 실제 수식의 공백 판정으로 쓰지 않는다. 본체 시작 offset 220은 이 네 스트림에 명시적으로 한정한다. 미지원 레코드·옵션, 절단, 종료 뒤 데이터는 거부한다.

`characters`는 저장 레코드 순회 목록이며 평탄화한 수학식이 아니다. 전체 수식 의미·일반 OLE 해독·글꼴 동등성을 보장하지 않는다. 선택한 네 개의 구조·문자 판독 외에 DOCX OLE 477개는 아직 구조 판독하지 않았고, 기존 5개는 본체 부재만 확인했다. 전체 gate는 NOT_PASSED, 신규 사람 승인은 없다.

상위 `validate_resume_evidence.py`가 원본 재추출·이전 근거·전체 해시·구조 재현·문자 위치·전체 절단·미지원/후행 바이트 거부·문자 변조 반영 및 독립 최소 본체 검사를 실행한다. 원본과 기존 렌더는 변경하지 않았다.
