# XBeach 고정 잔여의 초기 정정 R3-C1~C4

2026-09-12 AI 출처 정정. 입력은 `e11a8c8`의 기존 노트와 [고정 잔여 목록](../remaining-20260912/remaining.json)이다. 원본 솔버·매뉴얼과 기존 승인 기록은 보존한다.

| 잔여 ID | 반영 내용 | 문서 |
|---|---|---|
| R3-C1 | 활성 `waveparamsnew`와 빌드 미포함 경계 prototype 구분; bound 장파의 성분 쌍 곱·위상·진폭 부호 | wave boundary generation, wave boundary |
| R3-C2 | stationary와 surfbeat single_dir의 `wave_stationary_directions` 호출·방향 격자·시간 조건 | wave action balance, wave stationary |
| R3-C3 | `intrasedtr` 명시 입력 가능; 12개 입력과 실제 네 공식 루틴/여섯 값의 호출 구분 | intrawave sediment transport, morphology |
| R3-C4 | 기존 침투식의 원본 표기 차이와 암시적 근·전체 스텝 평균·가용수 제한 대조 | manual equation contracts, 모델 README |

[원문 인용과 재사용 근거](evidence.json), [전후 해시와 정확한 설치 대상](install-manifest.json), [변경분](canonical.patch)을 기록했다. 기존 verified 노트의 검증 이력과 이번 정정은 날짜·범위로 구분하며, 새 매뉴얼 계약은 draft-unsourced를 유지한다.

[Fortran 한정 재현](probe-results.json)은 원본 상수와 `transus` SELECT를 그대로 추출하고 네 호출을 표식 루틴으로 대체했다. 12개 form 값 × bulk 0/1의 24조합에서 호출 및 SELECT 뒤 도달/조기 복귀를 확인했다. 입력 parser·공식 본문·전체 solver·MPI 실행 검증은 아니다. 침투식의 세 대수 예는 [기존 기록](../infiltration-document-code-comparison.json)을 재사용한다.

재생성은 `prepare_canonical.py`(동결 git 원문 기준), `record_evidence.py`(소스 인용), `probe_dispatch.py`(컴파일 재현) 순서다. `validate.py`는 설치 전, `validate.py --installed`는 설치 뒤 바이트를 검사한다. 보호 문서 설치는 `install_canonical.py --check`로 먼저 확인하고 승인된 정확한 대상만 `--apply`로 반영한다. 이전 배치의 설치 validator와 동결 remaining validator를 현재 문서 해시에 맞춰 재작성하지 않는다.

[최초·최종 독립 Codex 검토](review-response.json)에서 남은 반영 차단 오류는 없었다. 최종 manifest 해시를 확인한 뒤 8개 대상에 설치했으며, [설치 검증](validation.json)은 원문 36구간·링크 32개·불변 292개와 검토/후보/설치 바이트를 확인했다. 파일 소유자와 권한도 유지했다. [후속 상태](../remaining-20260912/progress.json)에 초기 네 정정만 반영 완료로 기록했다. 전체 R1/R2의 종결, R3 전체 종결, R4 최종 승인으로 승격하지 않는다. 후속 작업은 기존 근거의 미연결 루틴/조건 대조와 수식 위치별 대응 결속이다.

원본 SELECT와 상수의 바이트 일치를 위해 `dispatch-probe.f90`에 추출한 CRLF·행말 공백을 보존했다. 이 원문 구간은 `git diff --check`의 공백 경고 대상이며 임의 정규화하지 않는다. 나머지 변경 파일의 공백 검사와 저장소 필수 훅은 별도로 확인한다.
