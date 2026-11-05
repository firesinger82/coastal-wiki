# CADMAS-SURF 노트 반영 job 4

대상은 [job 4 배정표](../assign/CADMAS-SURF-note-job-4.tsv)의 148개 행이다.
기존 노트에는 다른 배정 작업의 행이 있다.
기존 행을 보존하고 배정 행의 중복을 검사한다.

## 파일별 결과

- [연성 차이 노트](../../../models/CADMAS-SURF/source-analysis/cadmas-3d2f-vs-3d-coupling-differences.md):6: verification_method에 job 4 대조 범위를 추가했다.
- `models/CADMAS-SURF/source-analysis/cadmas-3d2f-vs-3d-coupling-differences.md:22–25`: 아키텍처 노트 상대 링크와 job 4 배정표·최종 근거 링크를 추가했다.
- `models/CADMAS-SURF/source-analysis/cadmas-3d2f-vs-3d-coupling-differences.md:38–185`: 배정 행 148개를 추가했다.
- 넣은 행 수는 job 4 배정표의 148개 행과 같다.
- 기존 표의 다른 배정 행 148개는 원문 그대로 보존했다.
- 이 노트 경로를 직접 가리키는 보고서 §4 수정안 행은 없다.
- 넣지 않은 배정 행은 없다.

- [아키텍처 소스맵](../../../models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md):152: 연성 차이 표로 가는 상대 링크를 추가했다.
- 아키텍처 소스맵에는 표 행을 추가하지 않았다.
- 두 노트의 last_source_check는 `2026-11-04 (recovery 대조 반영)`이다.
- 두 노트의 verification_method에는 `2026-11-04 CADMAS-SURF recovery 대조 보고서 반영`이 있다.
- 두 노트의 기존 citation_status는 유지했다.

## 수정안 행

이번 배정 행 ID는 KD1-019부터 KD1-715 사이의 배정표 지정 행이다.
새 연성 차이 노트 경로를 직접 가리키는 보고서 노트 수정안 행은 없다.
아키텍처 소스맵은 이번 작업의 지정 문장을 추가했다.
아키텍처 소스맵의 기존 대조 정정 본문은 보존했다.

## 확인 결과

배정표 148개 행의 ID·분류·최종 결론 문장을 최종 검증 파일과 대조했다.
누락 행은 0개이다.
중복 행은 0개이다.
추가한 행의 표 열 수는 모두 6개이다.
차이 절과 표 머리는 각각 하나이다.
상대 링크의 대상 파일이 존재한다.
지정한 세 파일의 `git diff --check`가 통과했다.
