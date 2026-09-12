# XBeach 빌드·모드·선택 수식 대응 — 2026-09-12

이번 기록은 모델 자체 빌드 선언, 전체 `src` 파일 역할, wave/nonh dispatcher 여섯 경로, Kingsday/Master의 파수 보정 및 지형 갱신 수식 대조를 다룬다. 부속 의존성 내부는 제외한다.

- `build-map.json` / `map_builds.py`: Autotools와 모델 프로젝트·solution, 실제 파일 집합·역할, 생성 include 소비자. `module_use_index`는 구문상 발견 인덱스이며 모든 루틴 실행 도달성의 증명이 아니다.
- `contracts.json` / `record_contracts.py`: 모드 가드·피호출 정의·정확한 원문 인용·문서/페이지 SHA. (2.5)의 보정량 의미와 B.37/C.37의 구현 분기를 기록한다.
- `generation-probe.json` / `probe_generation.py`: 원본 Python 생성기를 임시 복사본에서 실행했다. Mako/Python 버전은 영수증에 기록한다. Windows frozen 실행물이나 전체 solver build의 재현을 주장하지 않는다.
- `canonical/`, `canonical.patch`, `install-manifest.json`: 위키 문서 여섯 경로의 검토본과 변경 전후 SHA. `install_canonical.py`는 이 경로만 설치하고 기존 소유권·권한을 유지한다.
- `claude-review.json`은 사용량 한도로 중단된 시도다. `codex-review.txt`, `codex-review-events.jsonl`, `review-response.json`에 저장소의 Codex review 경로를 통한 독립 원문 검토·반영을 남긴다. 새 사람 승인 영수증이 아니다.
- `validation.json`, `validate_evidence.py`: 인용·집합·생성물·기존 불변 292개 및 설치 상태 검사.

저장소 루트에서 `python3 _staging/total-read/model-audit/XBeach/connectivity/build-mode-20260912/validate_evidence.py`로 근거를 재검사한다. 생성만 재현할 때는 Mako가 설치된 Python으로 같은 디렉터리의 `probe_generation.py`를 실행한다. 메타데이터 추출은 `map_builds.py`, 계약 원문 결속은 `record_contracts.py`이며, 기존 raw·승인 이력을 쓰지 않는다.

이 결과 이후 남는 실행 연결 검토는 경계 종류·표사 공식·선택 기능에서 실제 호출에 도달하는 조건과 전체 루틴 범위다. 매뉴얼은 이번 두 수식 묶음 밖의 모델 의미 대응을 계속해야 한다. 빌드/파일 수나 생성 성공을 이 잔여의 완료 근거로 쓰지 않는다.

독립 Codex 검토는 현재 검토본에 남은 구체적 반영 차단 오류가 없다고 결론 냈다. 생성기 인용의 끝 행을 268에서 실제 262로 교정하고 범위 검사를 추가했다. 검토본 여섯 경로를 설치했으며 `validation.json`의 installed_files=6은 최종 manifest의 바이트 일치를 뜻한다. 실제 솔버 빌드·실행, 신규 사람 승인은 포함하지 않는다.
