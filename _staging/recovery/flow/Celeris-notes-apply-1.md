# Celeris 노트 반영 작업 1

배정표: [Celeris-note-job-1.tsv](../assign/Celeris-note-job-1.tsv).

배정표의 159행을 `models/Celeris/source-analysis/celeris-transect-version.md`에 반영한다.

## 파일별 반영 결과

### 단면판 대조 노트

파일: [celeris-transect-version.md](../../../models/Celeris/source-analysis/celeris-transect-version.md).

- 추가 범위: `models/Celeris/source-analysis/celeris-transect-version.md:1–189`.
- 배정표의 159행을 추가했다.
- 노트 첫머리에 본판 소스 맵의 상대 링크를 추가했다.
- 각 행에 최종 근거 파일의 결론 문장과 확인한 원문을 옮겼다.
- 각 행에 보고서의 문서 원문과 코드 원문을 옮겼다.
- 이 새 파일을 직접 지정한 기존 노트 수정안 행은 없다.
- 넣지 않은 배정 행은 없다.

### 본판 소스 맵

파일: [celeris-source-map.md](../../../models/Celeris/source-analysis/celeris-source-map.md).

- frontmatter 수정 범위: `models/Celeris/source-analysis/celeris-source-map.md:5–6`.
- 기준판 추가 범위: `models/Celeris/source-analysis/celeris-source-map.md:15`.
- COULWAVE 저장 층 정정 범위: `models/Celeris/source-analysis/celeris-source-map.md:27–31`.
- 고차 flux와 시간 적분 정정 범위: `models/Celeris/source-analysis/celeris-source-map.md:47–55`.
- 기존 생성·호출 대응표 정정 범위: `models/Celeris/source-analysis/celeris-source-map.md:158–179`.
- 차이 표 링크 추가 범위: `models/Celeris/source-analysis/celeris-source-map.md:211–212`.
- 이 파일에 추가한 배정표 행은 0행이다.
- 수정안 `CP1-138`, `CP1-153`, `CP2-166`, `CD2-462`, `CT1-356`을 반영했다.
- 수정안 `CP3-041·090·099·108`의 소스 맵 대상 부분을 반영했다.
- 수정안 `CD1-1359`부터 `CD1-1380`까지를 반영했다.
- 수정안 `RF-013·source-map 인용표`를 반영했다.
- `CP1-138`의 보정 횟수 설명에는 최종 근거 `CP1-039`를 적용했다.
- `CP1-138`의 교차항 설명에는 최종 근거 `CP1-031`을 적용했다.
- 유지 대상 `CD2-461`의 본문은 그대로 두었다.
- 두 노트의 `last_source_check`를 `2026-11-04 (recovery 대조 반영)`으로 설정했다.
- 두 노트의 `verification_method`에 `2026-11-04 Celeris recovery 대조 보고서 반영`을 기록했다.
- 기존 `citation_status`는 유지했다.
- 넣지 않은 담당 수정안 행은 없다.

## 반영 확인

- 배정표 행 수는 `Celeris-note-job-1.tsv`에서 센 159행이다.
- 차이 표 행 수는 새 노트에서 센 159행이다.
- 배정표의 행 ID 집합과 차이 표의 행 ID 집합은 같다.
- 중복 행은 없다.
- 모든 행의 최종 분류가 지정된 근거 파일의 최종 분류와 같다.
- 모든 행의 결론 문장이 지정된 근거 파일의 노트용 결론 문장과 같다.
- 모든 행의 확인한 원문이 지정된 근거 파일의 인용과 같다.
- 논문 약칭 `P17`과 `P20`은 각각 `Tavakkol 2017`과 `Tavakkol 2020`으로 풀어 적었다.
- 배정표에서 센 분류별 행 수는 A 71행, C 10행, E 3행, F 75행이다.
- 모든 A 행의 결론 문장에 근거 커밋이 있다.
- 모든 E 행의 결론 문장에 근거 강도가 있다.
- Markdown 파서에서 센 표 본문 칸 수는 954개다.
- 표 머리와 대조 절은 각각 하나다.
- 두 노트의 frontmatter는 YAML 파싱을 통과했다.
- 두 노트의 상대 링크 대상 파일이 모두 있다.
- 두 노트에 금지된 경로와 문자열이 없다.
- 소스 맵의 수정분은 `git diff --check`를 통과했다.
- 넣지 않은 배정 행과 담당 수정안 행은 없다.
