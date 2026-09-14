# ADCIRC 기능 지도·조석 확인 방법 (2026-09-14)

[BUILD-PLAN](../../BUILD-PLAN.md)의 다음 묶음. 기존 61개 노트를 기능/공통 자료에 연결하고, 기존 토픽 지도와 조석 노트를 재사용한다.

- [계획](PLAN.md): Fable 5.1 초안과 [Codex 비판 검토](codex-plan-review.txt)의 두 P2를 반영. 분류/지원 조건/기존 코드 위치를 구별하고 자료 범위·해상도·결측·오차·보간 확인을 추가했다.
- [근거 범위](evidence.json), [선정 원문](source-extracts.txt): 동봉 docs·코드의 전체 SHA와 문서 절. testsuite의 일부 작업 파일은 HEAD와 CRLF만 다르며 정규화 비교도 기록했다.
- [61개 노트 대응](note-inventory.json): 기존 metadata와 제목 기반 탐색 분류이며 전체 주장 감사가 아니다. 모든 노트가 기능 또는 공통 자료에 대응한다.
- [예제 가용성](baseline-availability.json): quarter-annular 입력과 지정 control 출력은 존재한다. 존재 확인만 수행했다.
- [후보 변경](changes.patch), [적용 manifest](install-manifest.json): ADCIRC 네 파일에 한정. 지도는 source-needed, 이전 토픽 지도의 verified/사람 승인 비승계. [before](before/)와 git에 원래 내용 보존.
- [검사](checks.json): 의도된 경로에서 후보 링크·분류·출처 해시 검사. 실제 실행·수치/물리 검증이 아니다.

[Fable 내용 검토](fable-review.md)는 차단 없음. 누락된 3개 문서 구간·전체 선정 범위와 README 문헌 색인 설명을 보완했다. 추가로 공식 quarter-annular 입력의 NTIP=0/NTIF=0/NBFR=1 구분을 원문에 인용했으며 Codex 최종 검토 대상으로 명시했다. [실제 모델 확인](claude-model-check.json): 계획·검토 모두 claude-fable-5-1, Opus 대체 없음. CLI 보조 Haiku 사용은 별도 기록이다.

[Codex 최종 검토](codex-final-review.txt)에서도 도입된 결함·차단 없음. 공식 예제의 추가 NTIP/NTIF/NBFR 구분과 네 파일 설치 manifest/가드를 확인했다. 검토된 네 파일의 후보/설치 SHA가 일치하며([적용 확인](installation.json)), 기존 디렉터리 권한을 바꾸지 않고 승인된 sudo 설치로 반영했다. XBeach 불변 292파일도 동일하다.

반영 파일: 기능 지도, 조석 harmonic-prep 확인 방법, forcing 노트의 탐색 링크, ADCIRC README. 필수 훅은 커밋에서 검사하며 전체 모델 완료나 새 과학적 사람 승인으로 취급하지 않는다.

다음 과학 근거 작업은 외부 조석 DB의 판본별 위상·노달보정·단위·품질 문서와 변환/보간 확인 방법, 독립 관측 및 기준해·목적별 오차 기준 확보다. 새 지도·절차 작성만으로 입력/실행/물리 검증을 완료 처리하지 않는다. 과거 모델 감사·XBeach 292개 불변 집합·미커밋 6줄과 interfaces-20260912는 보존한다.
