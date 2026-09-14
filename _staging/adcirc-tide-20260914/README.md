# ADCIRC 조석 입력 — 첫 근거 묶음 (2026-09-14)

최종 구축 계획의 첫 적용이다. 두 기존 조석 노트에서 NBFR 입력·노드/분조 순서·위상/시간 기준·ETRF 항을 대조한다. [근거와 확인 범위](evidence.json)는 해당 로컬 판본에 한정한다. ADCIRC 전체 기능 지도·두 노트 전체 재검증·실제 실행·수치/물리 검증 완료를 뜻하지 않는다.

| 기능/조건 | 문서·방정식·구현 대응 | 이번 확인 | 남은 실행/자료 확인 |
|---|---|---|---|
| 주기 수위 경계 입력 | 공식 fort.15 NBFR→BOUNTAG/AMIG/FF/FACE→ALPHAE/EMO/EFA. 로컬 read_input.F:3410–3456의 ELEVALPHA | 설명의 추가 `[blank or ELEVALPHA line]`은 독립 입력 레코드로 존재하지 않음. 배열 첫 첨자는 분조, 둘째는 경계 노드 | 실제 입력 파일의 분조 수·헤더·노드 수/순서 대조 |
| 경계 노드 전달 | mesh.F:1822–1834가 NBDV의 경계 구간/구간 내 순서로 NBD 구성 → read_input.F:3493–3496 로그 → gwce.F:1646–1649 수위 적용 | 전체 노드 번호 정렬이 아니라 경계 목록 순서라는 근거 연결 | 사용할 fort.14의 노드와 보간된 조석값 대응은 아직 미확인 |
| 위상·시간 | read_input.F:3436,3496 degree→radian; timestep.F:257–258 TimeH; gwce.F:1644–1649 분조 합성 | EFA를 빼는 위상과 STATIM/REFTIM의 일(day)·내부 초 기준 확인 | 외부 DB 판본별 위상/기준시각 규약·단위·결측·보간 품질은 아직 미확인 |
| 조석 퍼텐셜 | CTIP/NTIP 가드 read_input.F:1705–1731; timestep.F:1517–1556 | 전통 분조 경로의 ETRF=0은 해당 ETRF 곱 항을 0으로 함. 경계 수위 합성과 SAL 계수는 별도 | full-formula 내부·다른 초기화 경로·전체 SAL 동작은 이번 수정 근거로 일반화하지 않음 |
| 입력 신뢰성과 결과 적합성 | 확인할 지형/조석 원자료, 변환 이력, 독립 관측/기준해 및 오차 기준을 정해야 함 | 확인 방법의 필요한 요소를 식별 | 개별 데이터·실행 로그·보존/민감도·관측 검증은 수행하지 않음 |

공식 [fort.15 형식](https://adcirc.github.io/adcirc/technical_reference/input_files/fort15.html)과 [parameter definitions](https://adcirc.github.io/adcirc/technical_reference/parameter_definitions/index.html)의 해당 항목만 대조했다. 공식 문서의 ALPHAE/EALPHA와 로컬 구현의 ELEVALPHA는 그 판본의 이름을 함께 적는다. 웹 문서 현재판과 로컬 코드 snapshot의 전역 일치를 주장하지 않는다.

정정 범위는 입력 블록의 불필요한 줄, harmonic-prep 예제의 배열 첨자 순서, ETRF=0 설명 및 이와 직접 연결된 조건·근거 표기다. 외부 DB 위상규약·지역 성능·SAL 정량값의 source-needed는 유지한다. 실제 입력자료를 검사했다거나 모델 실행이 통과했다고 쓰지 않는다.

반영 완료: [Fable 5.1 검토](fable-review.md)와 [Codex 최종 검토](../build-method-20260914/codex-final-review.txt)를 거쳤다. Fable의 두 비차단 제안(수위 가산항의 정확한 표현·verification_method 범위)을 반영했고, Codex는 추가 `NTIP=0`/필수 `NBFR=0` 구분 정정까지 확인했다. [정정 패치](corrections.patch)와 실제 두 노트의 SHA가 일치한다([설치 확인](installation.json)).

Codex가 지적한 설치기의 `assert` 최적화 취약점은 명시 예외 검사로 고쳤다. 임시 fixture에서 최적화 모드의 정상 설치·후보 변조·대상 변조·manifest SHA 변조·허용 외 대상 5건을 확인했다. 일반 승인 실행은 OS 디렉터리 권한으로 실패하여, 동일한 해시·두 파일 제한으로 승인된 sudo 설치를 수행했다. 기존 파일/디렉터리 권한을 넓히지 않았다.

이 완료는 위 한정 설명의 정정 반영이다. 전체 노트의 다른 주장, ADCIRC 기능 전체, 실제 입력자료 품질·모델 실행·수치/물리 적합성은 완료 판정하지 않는다. 다음은 모델 기능 지도와 필요한 입력/검증 근거의 범위 확정이다.
