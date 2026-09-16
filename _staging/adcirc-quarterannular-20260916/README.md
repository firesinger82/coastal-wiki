# ADCIRC 공개 조석 예제 근거 보강 — 2026-09-16

상태: **Codex 독립 검토에서 차단 사항 없음 확인 후 기존 두 문서에 반영 완료**. 공개 quarter-annular 예제의 기준해·설정·코드·출력 비교 근거를 한정 보강했다. 실제 ADCIRC 실행·수치/물리 검증 완료가 아니다.

## 범위와 역할

- 대상: `models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md`와 `models/ADCIRC/source-analysis/adcirc-topic-map.md`의 조석 검증 안내.
- 원문: 공식 quarter-annular 예제 설명, 고정 ADCIRC/testsuites 판본의 해당 입력·출력·비교 코드, 해석해 조건을 확인하는 데 필요한 공개 1차 문헌 구간.
- 2026-09-16 사용자 지시: 오늘 코드 분석·자료 수집은 Claude Opus에 맡기고 고급 추론·판단·분석은 Codex가 담당한다. 이 묶음의 원문 사실 추출은 Opus, 근거 판정·문서 반영·최종 검토는 Codex가 수행한다. 과거 Fable 지정의 해당 역할보다 현재 사용자 지시가 우선한다. 실제 응답 모델을 기록한다.
- 기존 노트의 인용 보강 예외를 적용하며 새 거버넌스 계획 사이클을 반복하지 않는다. 새 파일 체계·모델 전체 감사·부속 라이브러리 내부 조사로 확대하지 않는다.
- 실제 ADCIRC 실행, 격자/시간 민감도 실험, 관측 검증은 이 문서 보강의 산출물이 아니다. 원본 자료와 기존 사람 게이트·보호 파일 권한을 유지한다.

## 완료 조건

1. 선택한 예제의 경계·강제·선형/비선형 설정과 출력 비교 대상을 출처로 연결한다.
2. 저장된 control 출력과 해석해/관측의 증거 역할을 구분하고, 해석해 적용 조건과 미확인 범위를 표시한다.
3. 비교 코드의 tolerance·대상 변수·누락 출력 범위를 정확히 기록한다. 회귀 PASS를 수치/물리 검증 완료로 표현하지 않는다.
4. 후보 patch와 원문 대응표를 검토하고 필요한 수정·검사를 마친 뒤 기존 권한을 보존해 두 노트에 반영한다.
5. 현재 작업 포인터를 갱신하고 필수 staged 검사·커밋·푸시를 마친다. 기존 `plan.md`의 미커밋 6줄과 `interfaces-20260912`는 그대로 보존한다.

## 반영한 근거

- Lynch & Gray (1978)의 선정 원문 식에서 선형·일정 마찰·극좌표 조석의 조건을 확인했다. n=2·j=0의 특수형과 속도식을 도출하고, 전사/부호·반경 경계조건을 수식 수준에서 별도 확인했다.
- 비선형·이차 마찰을 켠 testsuite 입력을 선형 해석해의 동일 조건으로 간주하지 않는다. tanh ramp, 512 대 1236 hotstart 간격, NetCDF4 출력 선택의 코드 근거를 구분했다.
- control 여섯 NetCDF 파일의 판본 표기와 비교기의 대상/제외 범위를 확인했다. 요청된 fort.51–54 조화출력은 이 케이스의 자동 비교 YAML 목록에 없다.
- 기능 지도에서 이 한정 근거로 연결한다. 실제 회귀 실행, 해석해와 동일한 ADCIRC 입력/계산, 보존·민감도·관측 검증 및 목적별 허용치는 미완이다.

## 근거·검토·검사

[선정 원문](source-index.md), [Opus 사실 추출](opus-evidence.md)·[후속 PDF/입력 판독](opus-followup.md), [실제 Opus 모델](claude-model-check.json), [논문 해시](lynch1978-provenance.json), [control header](control-metadata.json), [수식 전사 확인](analytic-expression-check.json), [판정 기록](review-disposition.md), [Codex 독립 최종 검토](codex-final-review.txt), [반영 patch](changes.patch), [설치 manifest](install-manifest.json), [사전 검사](preflight.json), [설치·보존 확인](installation-checks.json).

두 canonical 문서는 후보 SHA와 일치하고 소유권/444 권한을 보존했다. 기존 미커밋 작업은 이번 커밋 대상에서 제외했다. 다섯 필수 staged validator는 커밋 훅에서 모두 통과했다. 설정 감사에서 제안한 Codex·스킬 변경은 적용하지 않았다.

## 세션 종료 기록 — 2026-09-16

- 문서 보강과 현재 작업 포인터를 커밋 `ab749343e1220e3e9d8386a6e80c8c1acaed5a93`에 저장하고 `origin/main`에 푸시했다. 이 문서 보강의 완료 조건은 충족했다.
- Claude는 기존 Claude Code CLI의 Claude Max 구독 인증으로 사용했다. 별도 API 키 호출은 사용하지 않았다.
- 기존 `plan.md`의 미커밋 6줄과 `_staging/total-read/model-audit/XBeach/connectivity/interfaces-20260912/`는 별도 작업으로 그대로 보존했다.
- 사용자 요청에 따라 여기서 종료한다. 실제 ADCIRC 실행·수치/물리 검증은 미수행이며, 향후 요청으로 재개할 때 선형 해석해와 동일한 입력·실행 환경·판정 기준부터 고정한다. 과거 전체 감사는 자동 재개하지 않는다.
