# Claude 실제 구조 대조 후속 검토 원문

AI 검토 의견이며 정책 채택·구현 승인이 아니다. preview 파일 부재 지적은 검토 시작 당시 상태이며 현재 파일은 준비됐다. 최종 처리는 review-response.md에 기록한다.

조사 문서·초안·이전 검토를 읽고 CONVENTIONS §2/§8/§8.1, `models/INDEX.md`, `fts5_index.py`, `concepts/_template/README.md`, 루트 README를 대조했다. 파일은 수정하지 않았다.

## 먼저, 이번 수정으로 해소된 것

`_template/README.md:8` "6개 파일 채우기" vs CONVENTIONS §8 "최소 시작 2파일"은 실재하는 문구 충돌이므로 P1 정정으로 두는 판단이 맞다(새 정책 도입 아님). `models/INDEX.md`는 10행 + `:18` 자기 stale 선언이 실측과 일치하고, `ALLOW = {"concepts","models","textbook","experience"}`(`fts5_index.py:19`)도 조사 기록대로다. §8.1 `:158`에 "탐색용 cross-link는 claim 복제 없는 범위에서 양방향 허용"이 실제로 있으므로 탐색/근거 구분 인용도 유효하다. 이 항목들은 다시 검토 과제로 올리지 않는다.

## 남은 실질 문제와 최소 수정

**1. §3의 `navigation-preview.md`가 존재하지 않는다.** 이 폴더의 파일은 9개이고 그중에 없다. P0 산출물 목록(§6)에도 없다. → 링크를 지우거나 P0 산출물로 명시. 둘 중 하나 선택.

**2. §2 표의 물리 변경 열이 P1 8파일보다 넓게 읽힌다.** "models: 모델 README에서 기존 노트 연결"은 13개 README, "textbook: 이론 노트 진입 링크 추가"는 편집 대상 파일이 P1 목록에 아예 없다. → §2 표 아래 한 줄: "이 표는 채택 후 목표이고, P1의 실제 편집은 §6의 8파일뿐이다. 나머지 모델·토픽은 P3 이후 별도 판단."

**3. `models/INDEX.md` 상태열 제거가 §2 `:43`과 충돌할 수 있다.** 규칙은 "INDEX.md는 비-verified 항목을 상태 컬럼으로 표시"다. P1 행은 "stale 집계 상태의 중복 관리 해소"라고만 써서 상태열 삭제로도 집행 가능하다. → 허용 변경을 "13개 진입 링크 + 상태 컬럼 유지(값의 기준은 AUDIT-LEDGER 링크로 위임), 노트 수·완료율 집계만 제거"로 고정. 루트 INDEX에 적용한 "상태·disclosed-gap 노출 유지"를 여기에도 같은 문장으로 건다.

**4. 템플릿 정정 범위가 문구 한 줄인지 표까지인지 불명.** `:8` 코드블록 주석 외에 `:11-20`의 "단계 파일" 01–06 표가 6파일 인상을 만든다. → "허용 변경 = README 본문의 생성 안내 문구(코드블록 주석 + 단계 파일 표 머리말)에 한정. 템플릿 파일 추가·삭제 없음"으로 명시.

**5. `plan.md`가 P1(8개)과 P2(5개) 양쪽에 있다.** 고정 묶음이 겹치면 P2에서 P1 포인터가 조용히 바뀔 수 있다. → P2 행에 "plan.md 편집은 §4 delta 기록 추가에 한정, P1의 최상단 포인터 블록은 수정하지 않음"을 추가.

**6. 빠진 영역 두 종류.** ① 루트 거버넌스 문서(BOUNDARY·RUNS-CHANNEL·SYNC)와 `.claude/skills`(coastal-audit·coastal-promote — 작업 규범 4가 완료 게이트로 지목하는 대상)가 README 안내 대상 정의에 없다. → P1의 README 허용 변경에 이 두 행을 포함. ② 루트 `swan_prd.md`·`swan_ecs.md`는 현황 문서에만 있고 계획에서 역할이 정해지지 않았다. → 이번에 처분하지 말고 §7에 "미분류 루트 문서, 이번 묶음에서 이동·삭제·재분류하지 않음"으로 유보 등재.

**7. §7의 검색 경계 서술이 실제보다 좁고 `standards` 성격을 틀리게 쓴다.** ALLOW는 4개 root 화이트리스트라 `data`·`references`·`research`도 함께 밖이고, `standards/kds-64`는 현황 문서 기준 원자료가 아니라 변환본 34개다. → "현재 검색은 concepts·models·textbook·experience 4개 root만 포함한다. standards(기준 변환본)·examples·data·references는 모두 대상 밖이며, 편입 여부는 이번 안내 개선과 분리해 결정한다"로 교체.

**8. waves README의 상태 표기 의무가 XBeach 쪽에만 걸려 있다.** XBeach README 행에는 "draft·감사 미완 표시 유지"가 있으나 waves 행에는 없다. waves README `:7-17` 상태표는 verified 일색이라, 아래에 XBeach draft 노트 링크를 붙이면 상태가 섞여 보인다. → waves 행 허용 변경에 "링크 대상의 현재 citation_status를 함께 표기"를 추가(§2 `:44` 강등 판정은 근거 인용이 아니므로 발생하지 않음을 P1 산출물에 한 줄로 남긴다).

## 판정

**MODIFY** — 방향(폴더 유지·안내 정합·유한 파일럿·R3 승격)은 유지하고, 위 8개는 전부 문구 수준 수정이다. 계획에 대한 의견일 뿐 채택·구현 승인이 아니다. 이 밖의 새 설계나 추가 검토 라운드는 필요하지 않다고 본다.
