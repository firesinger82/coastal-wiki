검토 결과다. 검토 모델은 Claude Fable 5.1(`claude-fable-5-1`)이며 파일은 수정하지 않았다.

**차단 지적: 없음.** 새 확인 방법 절과 기능 지도의 NTIP/NTIF·AMIG 불일치 설명, 코드 구간, 회귀검사 구간, README 집계는 모두 원문과 일치한다.

**중요 지적(비차단, 최소 수정 권고)**

1. **근거 기록에 빠진 S 문서 3개.** 지도가 "항목 확인"으로 쓴 다음 주장은 원문 대조 결과 사실이지만, 그 원문이 `evidence.json`·`source-extracts.txt`·지도 말미 "S의 근거 구간"(candidate/adcirc-topic-map.md:92) 어디에도 없다.
   - F03 NOLIBF, F09 NOLIFA, F14 Ramping 항목(:33, :39, :44)은 `docs/user_guide/model_configuration/model_parameters/index.rst:10–18`(nolibf·nolifa·ramping 목차)에서만 확인된다. `[dcfg]`가 가리키는 `model_configuration/index.rst`에는 이 항목이 직접 없다.
   - F08 "[경계 분류][dbc] 항목/형식 확인"(:38)은 `boundary_conditions/index.rst:6–12`가 근거인데 evidence.json에 없다.
   - "이론 안내는 v44.XX 보고서와 이후 기능 보강을 구분한다"(:20)는 `docs/theory/index.rst:4–8`이 지지하지만 S 범위에도 `web_accessed`에도 없다.
   - 최소 수정: 세 구간을 evidence.json(sha256 포함)과 source-extracts.txt에 추가하고, :92 목록에 넣는다.
2. **"S의 근거 구간" 목록이 실제 대조 범위보다 좁다.** :92는 evidence.json에 있는 `tides/index.rst:1–72`, `parameter_definitions/index.rst` 5구간, `fort51.rst`, `examples/index.rst`, `physics_parameters/index.rst`, `initial_conditions/index.rst`, `running_adcirc/index.rst`를 빼놓고 "실제 대조 범위는 이 구간…에 한정"이라 적었다. 목록을 보완하거나 "전체 구간·해시는 `_staging/.../evidence.json`"으로 위임하는 한 문장으로 바꾸면 된다.

**경미**

- README `web-refs/` 행을 1→2로 고쳤으나 비고는 official-resources만 언급한다. `adcirc-foundational-papers.md`를 비고에 추가 권고.

**확인 통과 항목**

- **불일치 설명의 원문 지지.** 개요 `tides/index.rst:17`은 NTIP를 "분조 수"로, `:31`은 AMIG를 "amplitude"로 쓴다. 상세 정의 `:452–459`(NTIP 0/1/2), `:758–759`(NTIF 분조 수), `:789–790`(AMIG 주파수), `:800–801`(EMO 진폭)과 코드 `read_input.F:1705–1709`(NTIP 0–2 검사), `:3338–3349`(NTIF 반복), `:3431–3441`(PER=2π/AMIG), `gwce.F:1642–1649`(AMIG×시간+FACE, EMO×cos)가 노트 서술과 일치한다. "웹 조회에서도 같은 표현"은 evidence.json의 `web_accessed` 기록으로만 확인했고 독립 재조회는 하지 않았다.
- **추가 코드 구간.** `mesh.F:1822–1834`는 NBD가 세그먼트 순서대로 누적됨을 보여 "분조당 NETA개 행 ↔ fort.14 경계 순서" 주장에 맞다. `read_input.F:1717–1731, 3434, 3485–3497`은 실제 fort.16 로그 위치다.
- **분류/조건 대조/기존 노트 구분.** 지도 :23의 3단 정의가 표 각 행에 일관되게 적용됐고, 기존 노트 링크 39편은 모두 실재한다. verified 비승계는 frontmatter `historical_verification`·`source_correction_human_approval: not-issued`·harmonic-prep `evidence_extension_human_approval: not-issued`로 명시됐다.
- **조석 품질 확인표.** 범위·해상도, 결측·품질·오차, 변환·보간 독립 확인, 위상·시각·노달보정 중복, 기준면 항목이 모두 있고 각 행이 미확정 상태를 `source-needed`로 표기한다.
- **실행/회귀/수치/물리 구분.** `test_list.yaml:423–434`(6개 netcdf 출력), `adcirctest.py:429–445`(control 대조), README tolerance 0.00001을 회귀 수준으로만 두고, 수치 검증(기준해·보존·민감도)과 물리 검증(독립 관측)을 별도 항목으로 분리했다. 전지구 M2 예제는 v55 이상·NTIP=2·전지구 조화분해로 원문(`global_astronomical_m2_tide.rst:8–15, 32, 38–41`)과 맞다.
- **README count.** source-analysis에 `citation_status`가 있는 노트 38편(현재 전부 verified, 지도 전환 후 37+1), manual-notes 21, web-refs 2, 합계 61로 note-inventory.json과 일치한다.
- **링크·훅.** 상대경로 깊이와 앵커(`<a id>`)는 정확하며 link validator는 fragment를 무시한다. 새 frontmatter 키를 거부하는 검증기는 없다.

실제 모델 실행, 과학적 사람 승인, ADCIRC 전체 완료 판정은 발급하지 않는다.
