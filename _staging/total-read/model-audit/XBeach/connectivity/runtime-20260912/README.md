# XBeach R1 실행 연결 보강과 문서 정정

2026-09-12 AI 작업본. 입력은 [동결 잔여](../remaining-20260912/remaining.json)의 빌드 포함 Fortran 57개·Python 2개와 이미 확인한 생성 경로다. 외부 라이브러리 구현은 조사하지 않았다. 원본 솔버와 과거 승인 292개는 보존한다.

[출처 원장](evidence.json)은 선박 압력수두, nonh 압력, 운동량 부호·2차 보정, 식생, 강우, 조도 갱신, 출력 공급자·rank, 로그 및 MPI 오류 콜백의 아홉 연결을 결속한다. 기존 lifecycle·physics·빌드 계약은 원본 해시로 재사용한다.

## 이번 문서 정정

- `ph`는 선박 압력수두이고 nonh 압력은 `pres/dp`다. nonh 입력·정수 분기와 실제 MPI 구현을 정정했다.
- `dudt/dvdt`를 빼는 실제 속도 갱신 부호를 복구했다. 주석 처리된 `flow_secondorder_con`을 활성 계산으로 설명하지 않는다.
- 현재 정상·방향 파랑 계산도 `Dveg`를 소비한다. 파랑/식생/유동의 갱신 순서를 붙였다.
- 강우의 mm/hr→m/s 변환과 같은 스텝 연속식 소비, 지하수와의 순서를 명시했다.
- 활성 출력 공급자는 `ncoutput_module`이며 Fortran과 NetCDF 쓰기 모두 `xomaster` 조건 뒤에 있다.
- 기존 연결 노트와 모델 README에 위 상태 전달을 연결했다.

[설치 대상](install-manifest.json)은 기존 문서 7개이며 [변경분](canonical.patch)으로 검토한다. 기존 verified 이력은 과거 기록으로 보존하고 이번 AI 정정과 구분한다. 연결 검토본의 `draft-unsourced`와 새 사람 승인 미발급 상태를 유지한다.

## 호출 후보와 판정의 구별

[후보 인덱스](index-summary.json)는 주석·문자열·연속행을 처리해 정의와 호출 후보, generic, CPP/실행 제어문 위치를 찾는다. 컴파일러 수준의 Fortran 파싱·타입 해석·경로 증명이 아니다. 특히 generic의 후보 전체를 실제 호출로 취급하지 않는다. 이름 변경·전이 USE·labelled DO/GOTO·조기 복귀·같이 성립할 수 없는 조건은 최종 의미 대조가 필요하다.

[생성 연결](generated-links.json)은 기존 생성 입력을 재실행하고 27개 출력 해시의 일치를 확인했다. 생성물 행은 출력 SHA와 템플릿·소비자에 결속하며 원본 파일의 행처럼 인용하지 않는다. [외부/콜백 경계](interface-boundaries.json)는 모델 호출 지점에서 분석을 멈춘다. 로그 delegate의 `writetolog`는 association 검사 없이 포인터를 호출하므로 선행 등록 전제를 기록했다.

[진입점 처분](entry-dispositions.json)은 CALL이 없는 C export·Fortran generic·프로그램·생성 호출·콜백을 구분한다. 나머지를 사장 코드라고 판정하지 않는다. [Python 연결](python-export-links.json)은 C export와 literal 호출을 연결하고 동적 타입·rank 선택은 별도 미완으로 남긴다.

**R1 전체는 아직 미완이다.** [남은 연결 공백](remaining-gaps.json)은 기존 R1 안의 호출 조건/overload 대조, 미분류 helper·interface, 동적 wrapper·생성 확장으로 특정했다. R2 수식별 대응과 R4 최종 패킷도 이번 결과만으로 완료되지 않는다. 인덱스 개수는 잔여 오류나 완료율이 아니다.

## 재현과 검증

`python3 -B index_calls.py` → 기존 생성 환경의 Python으로 `link_generated.py` → `python3 -B record_evidence.py` → `python3 -B prepare_canonical.py` 순서로 재생성한다. 후보 문서의 기준은 git `9f438b9`다. `validate.py`는 원본/인덱스 참조/생성 결과/정확 인용/대상 바이트/불변 승인 기록을 대조하고, `--installed`는 반영 뒤 검사다. 이 검사와 독립 검토는 수치 solver 실행이나 사람 승인을 대체하지 않는다.

[최초 독립 검토](codex-review.txt)의 P2 한 건은 선박 압력 소비 조건에서 nonh OR 분기가 빠진 문제였다. 원장의 조건을 원문대로 수정했고 [후속 검토](codex-followup.txt)는 해결 및 추가 차단 오류 없음을 확인했다. 일곱 후보 문서의 해시는 최초 검토와 동일하다. [재생성 확인](regeneration-check.json)은 수정된 최종 산출물 23개의 바이트 일치를 기록한다. [검토 반영 기록](review-response.json)과 설치 뒤 `validation.json`, `protection-after.json`은 각각 검토·바이트·보호 상태를 구분해 남긴다.
