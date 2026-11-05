# CADMAS-SURF 노트 반영 1

배정표는 [CADMAS-SURF-note-job-1.tsv](../assign/CADMAS-SURF-note-job-1.tsv)이다.
배정표의 대상은 109행이다.
각 행의 결론 문장과 확인한 원문은 지정된 최종 결론 근거 행을 따른다.

진행 상태: 완료.

## 새 차이 노트

- 파일: [cadmas-3d2f-vs-3d-io-mpi-differences.md](../../../models/CADMAS-SURF/source-analysis/cadmas-3d2f-vs-3d-io-mpi-differences.md).
- 추가 범위: `models/CADMAS-SURF/source-analysis/cadmas-3d2f-vs-3d-io-mpi-differences.md:1–142`.
- 표 행 범위: `models/CADMAS-SURF/source-analysis/cadmas-3d2f-vs-3d-io-mpi-differences.md:34–142`.
- 넣은 행 수: 배정표 109행 중 109행.
- 결론 문장 출처: KD1a·KD1b·KD1c 최종 근거의 같은 행 ID.
- 보고서 §4에는 새 차이 노트를 직접 가리키는 수정안 행이 없다.
- 넣지 않은 배정 행: 없음.

## 아키텍처 소스맵

- 파일: [cadmas-surf3d-architecture-source-map.md](../../../models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md).
- 표 행 추가: 0행.
- frontmatter 수정 범위: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md:6–7`.
- 파일 수·빌드 수 추가 범위: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md:24–25`.
- 버전·날짜 표지 수정 범위: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md:41–46`.
- MPI·부모·자식 격자 설명 수정 범위: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md:62`, `models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md:69–70`.
- 배열 설명 추가 범위: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md:74–79`.
- VOF·3D2F 경계 설명 수정 범위: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md:99–109`.
- 루프·진단량 설명 수정 범위: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md:130–140`.
- 관련 근거·차이 표 링크 수정 범위: `models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md:146–151`.
- 반영한 수정안 행 ID: `KS1-721`, `KS2-800–805`, `KS3-409`, `KU1-816·222`, `KF2-047·251–328`, `KF2-308·313·363`, `RF-006`.
- `KF2-251–328` 수정안은 3D2F의 배열 선언 위치를 별도 문장으로 연결한다.
- `KF2-251–328` 수정안은 개별 변수 사전 전체를 전재하라는 지시가 아니다.
- `KU1-816·222` 수정안은 파일 수·빌드 수와 소스 날짜 표지를 구분한다.
- `KU1-222` 최종 근거는 날짜 표지를 물성 변경 날짜로 해석하지 않는다.
- 유지한 내용: 3D 배열 설명·NF 범례, 기존 종료식, 반복 머리의 부모·자식 격자 교환, VOF 뒤 경계 재설정.
- 기존 심화 후보 문장은 관련 근거를 가리키는 사실 문장으로 바꿨다.
- 새 차이 노트의 상대 링크를 본문 끝에 넣었다.
- 넣지 않은 담당 수정안: 없음.

## 확인 결과

- 배정표의 109행과 새 노트의 행 ID·순서가 일치한다.
- 새 노트의 분류·결론 문장·확인한 원문은 지정된 최종 근거 109행과 일치한다.
- 새 노트 표의 최종 분류를 센 결과는 A 79행, C 10행, F 20행이다.
- 보고서 본문의 두 원문 칸에서 옮긴 인용 171개는 원본 소스의 지정 줄과 일치한다.
- Markdown 표 파싱 결과는 표 1개, 본문 109행, 행마다 6칸이다.
- 아키텍처 소스맵의 기존 표 줄 수는 반영 전후 모두 29줄이다.
- 유지 대상인 3D 배열 설명·NF 범례·종료식·부모·자식 격자 교환·VOF 뒤 경계 재설정은 반영 전 문장과 일치한다.
- 상대 링크의 대상 파일이 존재한다.
- 대상 노트의 frontmatter와 금지 경로·문자열 검사는 통과했다.
- 대상 경로의 `git diff --check`는 통과했다.
- 넣지 않은 배정 행과 담당 수정안은 없다.
