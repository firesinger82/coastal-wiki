# Claude Fable 5.1 검토 원문

**판정: 블로커 없음.** 조사 패킷은 지정 근거와 일치하며, 기존 게이트를 완화하거나 옛 메타데이터를 승인으로 바꾸는 서술이 없다. 아래는 소폭 수정 권고다.

## 대조 결과 (일치 확인)

- 집계: readiness.json 모델별 합계 = 437(verified 433 + draft 4), 폴더 수·갭 수·XBeach 미승인 14편 모두 README 표와 일치. 미승인 14편은 실제 frontmatter `not-issued` 14건과 정확히 대응.
- AUDIT-LEDGER: "done = ≥1 노트 실질 커버"(26행), snapshot 판정(35행), XBeach §7 9월 갱신 — README 44행 서술과 일치.
- PROGRESS.md: 옛 표(20–34행)의 ADCIRC·ROMS·Delft3D·EFDC 코어 부분·7모델 미착수 — README 46행과 일치. 3행 Jumpshot/MSI 보충은 재사용되지 않음.
- FUNWAVE preflight: 277/34/29/5/93 수치 일치. XBeach remaining.json R1–R3 `open`, R4 `open_after_prerequisites` — "미완 유지" 서술 정확.
- ADCIRC: timestep.F 1536행 `TPMUL=RampTip*ETRF(J)*TPK(J)*FFT(J)`, 1554행 ELSE 분기 가산, 1520–1521행 full-formula 경로, `SALTMUL` 분리 — observations A 정확. 노트 146행 "ETRF=0 → full potential"은 코드와 반대라는 판정 타당. read_input.F 3410–3456행(NBFR→BOUNTAG/AMIG/FF/FACE→ELEVALPHA→EMO/EFA) 서술 정확.
- SWASH: CheckPrep 1076–1078행 0.15, 1080–1082행 0.3, 조건 `psurf(2)==-1` — observations B 정확. 비교 노트 46·56행 무조건 β 0.3, 65행에는 조건 존재 — "표에 누락" 판정 타당. 모델 노트 78행과 정합.
- 순서: README §1·§4가 사용자 정정(수집→모델별 확인→연결→비교) 반영. 16·49행에서 고정 감사 범위 불변 명시. `semantic_read_or_human_approval_issued: false` 유지.

## 소견

1. **낮음 — README.md:3.** 첫 문장 "verified 433"이 frontmatter 표기라는 점이 20행에야 나온다. 수정: `verified 433`을 `frontmatter citation_status 기준 verified 433`으로.

2. **낮음 — collect.py:88, 137 / README.md:20.** 미승인 정정은 `not-issued` 리터럴만 잡는다. 현재는 다른 값이 없어 결과가 맞지만, `pending` 같은 값이 생기면 조용히 "미승인 아님"으로 빠진다. 수정: `unknown`·`not-issued` 외 값을 별도 키로 집계하거나, README 20행에 "`not-issued` 표기 기준"을 한 구절 추가.

3. **낮음 — collect.py:44–48 / README.md:20.** 노트 집계는 `git ls-files` 추적 파일 한정이고, `source-analysis/` 하위 폴더(예: failure-patterns·playbooks)도 노트로 센다. `_archive`·`_staging` 하위는 없음을 확인했다. 수정: README 20행에 "추적 파일·하위 폴더 포함" 명시.

4. **낮음 — observations.md:10.** `tidePotential%active()` 참 경로에서 `compute()`가 ETRF를 적용하는지는 이번 범위(1518–1557행)로 판단 불가. 현재 문장은 "다른 경로가 있다"까지만 말한다. 수정: "그 경로의 ETRF 적용 여부는 미확인" 한 구절 추가. 정정안 작성 시 노트 106행이 인용하는 1501–1503행도 대조 대상에 포함.

5. **낮음 — observations.md:18.** CheckPrep 1065–1068행(β가 양수도 -1도 아니면 경고 후 0.3 강제)이 빠져 있다. 비교표 정정안이 "0.3 기본"의 세 번째 경로를 놓칠 수 있다. 수정: 해당 조건 한 줄 추가.

6. **낮음 — README.md:24–38 "확보된 문서 진입점" 열.** SFINCS RST 제목만 문서, EFDC+ 12.4 본체, Celeris 원논문 서지만 확인 등은 이번 검토 지정 근거 밖이라 대조하지 않았다. 결함 지적이 아니라 미검증 표시다. observations.md:11의 harmonic-prep 115·182–183행 인용도 동일.

## 누락된 한계·미지지 주장

- 미지지 주장은 발견하지 못했다. "13개 모델 모두 본체·문서 있음"은 존재 확인(exists=true)으로 뒷받침되고, 22·40행에서 수집 완결과 구분한다.
- README:53의 "직접 모델 노트 수"가 frontmatter `related` 제외·본문 링크 한정임은 명시되어 있다.
- SWASH 비교표 정정과 ADCIRC ETRF 정정 모두 canonical `verified` 노트 변경이므로 README 71·73행대로 독립 검토·사람 결정을 거쳐야 한다. 패킷은 이를 요구하고 있고, 이번 검토는 그 승인이 아니다.

## 다음 작업 적정성

§4 첫 묶음(ADCIRC 조석 두 노트, 종료 조건 3항, 전체 감사·변환기 제작 제외)은 구체적이고 한정적이다. 새 비교 노트 증설을 잡지 않은 점도 사용자 순서와 맞다. 추가 감사 프로그램 제안은 없다.

## 이 검토의 한계

validation.md·fable-review.json·plan.md 이력 본문은 읽지 않았다. plan.md 5행의 포인터 존재만 확인했다.
