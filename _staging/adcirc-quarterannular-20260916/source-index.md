# 선정 근거와 판단 범위

## 고정 로컬 판본

- S: `models/ADCIRC/raw/source_code/adcirc/`, HEAD `6037225ce4573efd3c1f8877a5dc908d01c199a8`.
- T: `models/ADCIRC/raw/source_code/adcirc-testsuite/`, HEAD `72bb573073ea89e538890f9352dd8e92bae562f5`.
- Q: T의 `adcirc/adcirc_quarterannular-2d-netcdf/`.
- 선택 파일 해시·줄 범위: [local-source-index.json](local-source-index.json), 검토용 줄 번호 발췌: [source-extracts.txt](source-extracts.txt). 범위 외 코드 전수 판독이나 실제 solver 실행의 기록이 아니다.
- 여섯 NetCDF control의 SHA·차원·변수·판본 global attribute를 읽기 전용으로 기계 추출: [control-metadata.json](control-metadata.json). 숫자 결과의 물리·수치 검증은 하지 않았다.

## 공식 설명과 원 논문

- [ADCIRC quarter-annular 공식 예제](https://adcirc.org/home/documentation/example-problems/quarter-annular-harbor-with-tidal-forcing-example/): linear 2DDI/3D의 해석해 존재 설명, 배포 입력의 finite amplitude/advection/quadratic friction, 기하·출력 설정. Opus와 Codex가 2026-09-16 웹 본문을 확인했다. 로컬 미러는 `models/ADCIRC/raw/manuals/website_markdown/home/documentation/example-problems/quarter-annular-harbor-with-tidal-forcing-example/index.md:405–427`.
- [2D 하위 예제](https://adcirc.org/home/documentation/example-problems/quarter-annular-harbor-with-tidal-forcing-example/2d-quarter-annular-harbor-with-tidal-forcing/): serial와 hotstart 변형의 비교 설명. 선형 해석해와의 정량 검증 결과로 사용하지 않는다.
- [Lynch & Gray 1978 원문 PDF](https://ccht.ccee.ncsu.edu/wp-content/uploads/sites/10/2019/05/Lynch-1978-JHY.pdf): Opus가 원문 링크를 확보하고 CLI 후속에서 다운로드·이미지 판독했다. 인쇄면 1410–1412, 1414–1415(PDF 3–5, 7–8쪽)의 식 (1)–(2), (6)–(9), (20)–(25)만 근거로 사용한다. 전체 논문 판독을 주장하지 않는다. [다운로드 해시·판독 범위](lynch1978-provenance.json), [후속 사실 추출](opus-followup.md)에 기록했다. 최초 WebFetch의 10 MB 제한과 후속 보조 shell 명령 거부 이력은 원본 JSON에 남기고, 주 실행자가 허용된 파일 읽기로 SHA를 보완했다.
- [CCHT wind-driven setup](https://ccht.ccee.ncsu.edu/analytic-solution-for-wind-driven-setup/): 위 원 논문의 위치를 찾는 탐색 자료로만 사용. 이 페이지의 바람 유발 해를 조석·이차수심 해로 대체하지 않는다.

## 역할과 검토

[Opus 사실 추출](opus-evidence.md)은 수집 자료이며 최종 판단이 아니다. [실제 모델 영수증](claude-model-check.json)은 주 작업 모델 `claude-opus-5`를 확인한다. 인증은 기존 Claude Max 구독의 Claude Code CLI이며 별도 API 키를 사용하지 않았다. CLI의 보조 Haiku 호출은 주 분석 모델의 대체가 아니다.

Codex는 입력의 비선형성과 선형 해석해의 조건 차이, 회귀 비교의 대상/제외 범위, control 판본 표기의 의미를 판정하고 문서 후보에 반영한다. 원문 식 (20a), (23), (25d–e)에서 n=2·j=0의 무차원 반경식을 도출하고 식 (2)에서 속도식을 얻었다. [독립 유량 유한차분·경계 대조](analytic-expression-check.json)는 전사/부호 오류 확인이며 ADCIRC 실행·수렴성 또는 물리 검증 결과가 아니다. 문서 한정 검토와 과학적 사람 승인·실제 수치/물리 검증을 분리한다.
