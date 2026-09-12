# XBeach lifecycle 상태 계약 재판정 — 2026-09-12

기존 XB-SC-001~012의 모델 상태 생산·소비·호출 계약을 원본 코드와 대조한 후속 기록이다. 초기화·hotstart·스텝·출력·종료 및 XBeach 자체 BMI/dynamic/Python 호출만 포함한다. MPI 구현체나 Jumpshot 내부는 범위 밖이다.

- `adjudication.json`: 12개 판정, 적용 조건, 원본 인용·SHA, 네 진입점 계열. 기존 원장의 해시를 연결하며 기존 원장을 수정하지 않는다.
- `claude-review.json`, `claude-followup.json`, `review-response.json`: 독립 원문 검토와 수정 처리. 사람 승인 영수증이 아니다.
- `canonical/`, `canonical.patch`, `install-manifest.json`: 위키 문서 다섯 경로의 검토본, 변경 내역, 설치 전후 해시.
- `probe_lifecycle.py`, `error_path_probe.f90`, `saved_getter_probe.f90`, `probe-results.json`: 원문 함수 추출을 이용한 한정 재현. 오류 1의 직렬 종료와 선언 초기화 local의 저장 수명을 확인한다.
- `validate_evidence.py`, `validation.json`: 원문 인용·프로브·설치 파일·기존 불변 292개를 결속한다. 해시 검사를 의미 검토나 사람 승인으로 대체하지 않는다.

재검증은 저장소 루트에서 다음 명령으로 한다.

```sh
python3 _staging/total-read/model-audit/XBeach/connectivity/lifecycle/resolution-20260912/validate_evidence.py
```

최소 재현을 다시 만들 때만 아래 명령을 사용한다. `gfortran`이 필요하며 임시 디렉터리에서 빌드한다. 원본 솔버는 변경하지 않는다.

```sh
python3 _staging/total-read/model-audit/XBeach/connectivity/lifecycle/resolution-20260912/probe_lifecycle.py
```

프로브의 출력·로그 또는 `compute_dt` 주변은 stub이다. MPI 초기화 경고 5·6 뒤 `outputext`의 반환값 미대입은 소스 경로로 확인했으며 전체 MPI 실행을 재현한 결과가 아니다. Getter 프로브의 수치는 실제 시간간격이 아니다. 전체 entry/build/mode·도달 파일 대응, 남은 모델 수식 대조, 새 주장에 필요한 사람 검토는 별도로 남는다.
