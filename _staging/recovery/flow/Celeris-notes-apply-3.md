# Celeris 노트 반영 3

배정표: [Celeris-note-job-3.tsv](../assign/Celeris-note-job-3.tsv).

진행 상태: 배정표의 158행과 기존 인프라 노트의 수정안 20개 ID를 반영했다.

## 파일별 결과

- `models/Celeris/source-analysis/celeris-webgpu-infrastructure-differences.md:1–184`를 추가했다.
- frontmatter와 본문 안내는 같은 파일 1–24행이다.
- 차이 표의 머리는 같은 파일 25–26행이다.
- 차이 표의 배정 행은 같은 파일 27–184행이다.
- 넣은 행은 배정표 기준 158행이다.
- 넣은 행의 분류는 A 2행, B 14행, C 142행이다.
- 차이 표에 넣지 않은 배정 행은 없다.
- 이 파일을 직접 가리키는 기존 노트 수정안 행은 없다.

### 기존 인프라 노트

대상: [celeris-webgpu-infrastructure.md](../../../models/Celeris/source-analysis/celeris-webgpu-infrastructure.md).

| 추가·수정 줄 범위 | 내용 | 반영한 수정안 행 ID |
|---|---|---|
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:5–6` | verification_method 구절과 last_source_check | 해당 없음 |
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:17–22` | 주요 2D 상태와 3D 그룹·1D 입력·더미·렌더 캐시 구분 | CP3-117 |
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:31` | 이미지 텍스처의 2D 배열과 cube view | CD2-474 |
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:49` | txState와 Pass2의 입력 구분 | RF-020 |
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:51` | UVstar 시간 이력 | CD1-1327 |
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:55–62` | NLSW 복사, 분산 우변, PCR 해와 경계 입력 | CD1-1328, CD1-341, RF-020 |
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:85` | txHnear 생산자·소비자 | CD1-1329 |
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:109–113` | 쇄파·COULWAVE B 도함수의 생산 시점 | RF-015 |
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:186–188` | 장치 치수 한도와 8192 대체값 | RF-025, CD1-1330 |
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:190–193` | OrderedFunctions 순서와 type-5 로딩 | RF-002, CD1-1331 |
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:197` | bind group 생성 순서 | RF-002 |
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:214` | AB3 예측과 AM4 한 번 보정 | CP1-139, CP2-173, RF-007 |
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:226–228` | 구면 시간간격 분기와 도입 커밋 | CD1-1332 |
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:239–240` | 셰이더 식의 AB3·AM4 계수 | CD1-1333 |
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:246–248` | 평균·파고와 f16·점 시계열의 갱신 주기 | RF-003, RF-011 |
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:255–256` | 평균 카운터 | RF-011 |
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:262–264` | 파고 복사와 카운터 | RF-003, RF-011 |
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:272–276` | 본판 epoch와 transect 비동기 초기화 후보의 중간 강도 | CT1-366 |
| `models/Celeris/source-analysis/celeris-webgpu-infrastructure.md:281–282` | 차이 표의 상대 링크 | 해당 없음 |

이 노트에 넣은 배정 표 행은 0행이다.
배정표의 158행은 모두 새 차이 파일에 들어 있다.
CD2-474는 최종 분류가 H이므로 차이 표 행을 추가하지 않았다.
CD2-474의 기존 본문 수정안은 이미지 텍스처 표기에 반영했다.
직교 시간간격 식과 점 readback의 단일 행 복사 설명은 유지했다.
callflow의 Claude 렌더 확인 절은 흐름도 수정 내역이다.
그 절에는 이 노트를 직접 가리키는 추가 수정안이 없다.

## 최종 확인

- 배정표의 158행과 차이 표의 158행을 행 ID로 대조했다.
- 누락 행은 0행이다.
- 중복 행은 0행이다.
- 배정 외 행은 0행이다.
- 차이 표 158행의 최종 분류·결론 문장·확인한 원문 위치는 지정된 근거 파일의 같은 ID 행과 일치한다.
- RF-018 결론 문장 앞에는 비교 문서 판인 Tavakkol 2017을 명시했다.
- 현재 코드 위치에서 ebca435 접두어를 생략했다.
- 이전 코드 위치에는 커밋 해시를 보존했다.
- 노트 자기 인용에는 d8157c80을 붙였다.
- 보고서의 배정 행에서 추출한 코드 원문 1559개를 소스의 해당 줄과 대조했다.
- 코드 원문 대조에서 문자열 차이는 0개다.
- 차이 표의 모든 행은 6칸이다.
- 차이 절과 표 머리는 각각 1개다.
- 두 노트의 last_source_check와 verification_method를 확인했다.
- 두 노트의 citation_status는 verified다.
- 두 노트에서 금지 경로·이중 대괄호·한계 문장은 발견되지 않았다.
- 두 노트의 상호 링크는 상대 링크다.
- 기존 노트의 직교 시간간격 식과 점 readback 설명을 보존했다.
- 대상 노트의 git diff --check가 통과했다.
- 반영하지 않은 담당 수정안은 없다.
