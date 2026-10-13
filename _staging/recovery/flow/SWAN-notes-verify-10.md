# SWAN 노트 추가 줄 전수 대조 — 2026-10-13

대상은 사용자 지정 노트 6개의 작업 시작 시점 `git diff -U0 HEAD -- <노트>`에 있는 모든 `+` 줄이다.
줄 수에는 frontmatter와 빈 줄을 포함한다.
노트별 완료 기록의 줄 번호는 정정 후 파일을 기준으로 한다.
정정 수와 보완 수는 이 작업에서 변경한 줄 수로 센다.
시작 diff 밖의 연동 변경은 해당 노트의 완료 기록에서 따로 밝힌다.
원문은 로컬 코드, 과거 커밋의 코드, 로컬 HTML, PDF와 지정 보고서의 최종 판정이다.

| 노트 | 시작 시점 + 줄 수 | 상태 | 정정 수 | 보완 수 |
|---|---:|---|---:|---:|
| `models/SWAN/manual-notes/swan-programming-rules.md` | 73 | 완료 | 10 | 1 |
| `models/SWAN/manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md` | 87 | 완료 | 4 | 2 |
| `models/SWAN/source-analysis/swan-setup-solver-swancom1-crosswalk.md` | 58 | 완료 | 18 | 1 |
| `models/SWAN/manual-notes/swan-tech-ch2-governing-equations.md` | 49 | 완료 | 4 | 1 |
| `models/SWAN/manual-notes/swan-tech-ch6-iterative-solvers.md` | 29 | 완료 | 0 | 0 |
| `models/SWAN/source-analysis/swan-grid-readers.md` | 29 | 완료 | 6 | 3 |

시작 시점 대상 줄은 위 표의 합계인 325줄이다.

## 노트별 완료 기록

### swan-programming-rules.md — 완료

시작 diff의 73줄을 대조했다.
대상 줄은 `7–8, 44, 49, 66–68, 111, 147, 156–158, 160–220`이다.
frontmatter의 반영 날짜와 보고서 반영 기록을 확인했다.
차이 표 52행의 분류와 결론은 R7 §5 최종본과 일치한다.
현재 코드 인용과 `7ee8981`, `43e9bbb`, `2980d1a`의 코드 인용을 각각 원문과 대조했다.
swanpgr PDF 7·9–13·15·19·21–23·25·27–29·31·33–35·37·39–49·51쪽을 대조했다.
swanimp PDF 15·21·28쪽과 swanuse PDF 36쪽을 대조했다.
인용한 HTML의 시작 줄과 이어지는 문장을 대조했다.
swanpgr PDF 12쪽 이미지에서도 `=<` 인쇄를 확인했다.
직속 `src/*.ftn`·`src/*.ftn90`의 기본 `-unix` 치환 집계를 재현했다.
현재 집계는 총 75파일, STRACE 호출 62파일, 호출행 292개이다.
`7ee8981` 집계는 총 76파일, STRACE 호출 63파일, 호출행 293개이다.
SWREAD 19–3696행의 `^ {6,}CALL\b` 집계는 `7ee8981`과 `43e9bbb`에서 각각 591문장이다.
N-023의 `0dabfa4`와 2026-07-13은 `SWAN-git-verify-A.md:132`와 일치한다.

| 구분 | 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| 정정 | `models/SWAN/manual-notes/swan-programming-rules.md:111` | `swmod + 3-digit`의 예를 `swmod1`·`swmod2`와 일치한다고 설명했다. | 세 자리 기호는 문서의 예시임을 밝혔다. 실제 일반 모듈 이름을 별도 문장으로 적었다. | swanpgr PDF 37쪽: `could for example be followed by a 3-digit symbol`. swanimp PDF 21쪽: `swmod1.f, swmod2.f`. |
| 보완 | `models/SWAN/manual-notes/swan-programming-rules.md:165` | 노트 인용의 시점을 밝히지 않았다. | N-022·N-023·N-024의 노트 인용과 줄 번호가 보고서에 보존된 반영 전 노트임을 밝혔다. | R7:1202–1204의 반영 전 노트 인용. |
| 정정 | `models/SWAN/manual-notes/swan-programming-rules.md:215` | `Git 전체 이력에서`. 분류는 `D 문서에만 있음`. | `41.45부터 43e9bbb까지 조사한 Git 이력에서`. 분류는 `D 현재 해당 구현 없음`. | `SWAN-git-verify-D.md:66`의 검색 범위는 `41.45부터 43e9bbb까지`이다. R7:976의 P-053 최종 분류. |
| 정정 7줄 | `models/SWAN/manual-notes/swan-programming-rules.md:176,185,195,201,203,205,216` | P-010·P-019·P-031·P-039·P-041·P-043·P-054의 `B 문서 오기`. | 보고서 최종 분류의 `B 문서·노트 오기`. | R7:936,945,956,962,964,966,977의 해당 행 분류. |
| 정정 | `models/SWAN/manual-notes/swan-programming-rules.md:219` | N-023의 `A 판 차이`. | `A 확정 (0dabfa4 2026-07-13)`. | R7:1203의 최종 분류. `SWAN-git-verify-A.md:132`의 커밋 판정. |

### swan-tech-ch2-obstacles-diffraction-setup.md — 완료

시작 diff의 87줄을 대조했다.
frontmatter의 범위·식 번호·반영 날짜를 대조했다.
swantech PDF 60–66쪽의 식·조건·그림을 대조했다.
PDF 63·64쪽 이미지로 그림 2.4의 범례와 식 (2.136)의 음수를 확인했다.
HTML node26·node28·node29·node30의 식 본문과 표시 번호를 대조했다.
swanuse PDF 36·87쪽과 HTML SET·OBSTACLE·DIFFRACTION 절을 대조했다.
코드의 FREEBOARD QUAY 분기, 회절 평활, DYNDEP 조건, 복사응력 정규화와 set-up 조립을 확인했다.
차이 표 24행의 분류는 R3 최종본과 같다.
22행의 결론 문장은 R3 §5 최종본과 같다.
NT-007은 보고서 내부의 부호 충돌을 원문으로 판정했다.
R3:625의 양수 판독은 PDF 64쪽 이미지 및 HTML node29:77과 다르다.
R3:458의 OQ-017 최종 정정은 같은 부호를 음수로 판정한다.
노트는 원문의 음수와 올바른 회절 보정식을 유지했다.
NT-007 행에는 해당 원문과 OQ-017의 정정 근거를 보완했다.
OQ-009의 두 제한이 같다는 문구는 두 부등식을 만족한다는 문구로 정정했다.
이 차이는 보고서 문구를 원문의 부등식과 코드의 상한·하한 적용 순서로 판정한 결과이다.

| 구분 | 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| 정정 | `models/SWAN/manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md:8` | HTML 식 번호 차이를 모두 `+40 offset`으로 설명했다. | PDF (2.131)–(2.135), 번호 없는 자유고 식, PDF (2.136)–(2.145)의 대응을 구분했다. | swantech PDF 61–66쪽. HTML node26:89–249, node28:66·88, node29:86–247, node30:66–122. |
| 정정 | `models/SWAN/manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md:23` | HTML 식 번호 차이를 모두 `+40 offset`으로 설명했다. | 자유고 식 이후의 번호 차이가 42임을 반영했다. | 위와 같은 PDF·HTML의 식 표시 번호. |
| 정정 | `models/SWAN/manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md:32` | 방향 스펙트럼 조건만으로 합리적인 표현이 가능하다고 설명했다. | 깊은 음영역을 관심 대상으로 삼지 않는 조건과 원문의 불확실성 표현을 복원했다. | swantech PDF 61쪽: `it seems`, `unless one is interested in the wave field deep into the shadow zone`. |
| 보완 | `models/SWAN/manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md:85` | `무류와 정수심`을 원문의 명시적 가정처럼 적었다. | 원문의 무류 조건과 수심 시간변화에 관한 해석을 구분했다. | swantech PDF 64쪽: `In a simplest case, we assume there are no currents.` 코드 `swancom5.ftn:1543–1548`의 `CAST2` 분기. |
| 보완 | `models/SWAN/manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md:185` | NT-007에 기본 방향 전파속도의 실제 원문 인용이 없었다. | PDF·HTML의 음수와 R3:OQ-017의 최종 정정을 명시했다. | swantech PDF 64쪽 이미지. HTML node29:77의 `c_{\theta,0} = -\frac{1}{k}`. R3:458. |
| 정정 | `models/SWAN/manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md:191` | 비가 임계값 이하이면 `두 제한이 같다`고 적었다. | 코드 결과가 문서의 두 부등식을 만족한다고 적었다. | swantech PDF 62쪽 (2.135). `swanser.ftn:3185–3186`의 상한 적용 후 하한 적용. |

### swan-setup-solver-swancom1-crosswalk.md — 완료

시작 diff의 58줄을 대조했다.
차이 표 8행의 분류와 결론은 R3·R5 최종본과 일치한다.
모든 소스 인용과 서브루틴 선언 위치를 대조했다.
SWAN-git-verify-D의 SU-011과 과거 커밋 `43e9bbb:src/swanmain.ftn:1197`을 대조했다.
swanuse PDF 86–87·95쪽 및 HTML SETUP·NUMERIC 절을 대조했다.
swantech PDF 65–66쪽의 정규화와 PDF 127–133쪽의 2D set-up 설명을 대조했다.
서브루틴 개수 오류를 고치기 위해 시작 diff 밖의 제목·frontmatter·집계·표 제목 5줄도 연동 정정했다.
누락된 SOURCE의 행 1줄을 보완했다.
시작 diff 안의 정정은 13줄이다.

이 표의 노트 경로는 `models/SWAN/source-analysis/swan-setup-solver-swancom1-crosswalk.md`이다.

| 구분 | 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| 연동 정정 5줄 | `swan-setup-solver-swancom1-crosswalk.md:2,10,14,34,38` | 서브루틴 19개. 기존 노트 연결 13개. | 선언 20개. 기존 노트 연결 14개. | `src/swancom1.ftn`의 `^\s+SUBROUTINE` 선언 20개. SOURCE의 선언은 6823행이다. |
| 정정 | `swan-setup-solver-swancom1-crosswalk.md:35` | `GPL-3.0` | `GPL-3.0-or-later` | `swancom1.ftn:9974–9975`: `either version 3 of the License, or` / `(at your option) any later version`. |
| 정정 | `swan-setup-solver-swancom1-crosswalk.md:36` | Cycle II 유산이라는 해석과 10001–10015행만으로 저자를 인용했다. | 실제 Updates의 날짜와 Authors의 담당자를 구분했다. | `swancom1.ftn:9994,9997,10001,10011`. |
| 정정 | `swan-setup-solver-swancom1-crosswalk.md:45` | SACCUR를 `curvature stopping`과 연결했다. | 연속 두 반복의 파고·평균주기 변화 기준으로 설명했다. | `swancom1.ftn:4513–4534`. R8:N1-011. |
| 정정 | `swan-setup-solver-swancom1-crosswalk.md:47` | ACTION의 역할을 스펙트럼 bin 범위 결정으로 적었다. | 수송·굴절 항 조립으로 고쳤다. | `swancom1.ftn:5212–5213,5381–5495`의 전파 해법 호출 및 행렬 인수. |
| 정정 | `swan-setup-solver-swancom1-crosswalk.md:49` | SOLPRE의 실인용 담당을 schemes 노트로 연결했다. | SOLPRE 호출을 실제로 인용하는 propagation 노트로 연결했다. | `swan-propagation-implementation.md:89`의 `swancom1.ftn:3644–3653`. |
| 정정 | `swan-setup-solver-swancom1-crosswalk.md:50` | SOLMAT를 행렬 조립으로 설명했다. | Thomas 삼중대각 해법으로 고쳤다. 호출 인용 링크를 고쳤다. | `swancom1.ftn:6312–6330`. |
| 정정 | `swan-setup-solver-swancom1-crosswalk.md:51` | SOLMT1을 행렬 조립 변형으로 설명했다. | 방향 주기 경계 결합과 명시적 주파수 전파를 가진 선형계 해법으로 고쳤다. | `swancom1.ftn:6555–6567`. |
| 정정 | `swan-setup-solver-swancom1-crosswalk.md:52` | PHILIM을 Hersbach–Janssen 제한기로 설명했다. | Phillips 평형 수준에 따른 제한기로 고쳤다. | `swancom1.ftn:7910–7929`. R8:N1-009의 PHILIM·HJLIM 구분. |
| 정정 | `swan-setup-solver-swancom1-crosswalk.md:54` | RESCALE에 Tolman 1991 귀속과 schemes 실인용 링크를 붙였다. | 실제 작용밀도 재분배 동작과 propagation의 호출 인용을 적었다. | `swancom1.ftn:8201–8206`. `swan-propagation-implementation.md:172–174`. |
| 정정 | `swan-setup-solver-swancom1-crosswalk.md:55` | SWSIP 실인용 담당을 schemes 노트로 연결했다. | 호출을 인용하는 propagation 노트로 연결했다. | `swan-propagation-implementation.md:94`의 `swancom1.ftn:3693`. |
| 정정 | `swan-setup-solver-swancom1-crosswalk.md:58` | SWSTPC의 신설 판을 41.01로 적었다. | 신설 판을 40.41로 고쳤다. | `swancom1.ftn:9613`: `40.41, Jun. 04: New subroutine`. |
| 보완 | `swan-setup-solver-swancom1-crosswalk.md:61` | SOURCE 행이 없었다. | SOURCE 선언과 원천항 조립 근거를 넣었다. | `swancom1.ftn:6823,7291–7294,7454–7458`. |
| 정정 | `swan-setup-solver-swancom1-crosswalk.md:63` | `19 중 13`이라는 집계와 종결 표현을 썼다. | 코드 선언 20개와 표의 14·4·2개 분류를 적었다. | 코드 선언 집계 및 정정 후 역할 표. |
| 정정 | `swan-setup-solver-swancom1-crosswalk.md:154` | Dirichlet 분기를 `Eq 5.23-24 Neumann half-cell`과 연결했다. | `Eq 5.6 Dirichlet 경계`와 연결했다. | swantech PDF 128쪽 (5.6). `swancom1.ftn:11781–11802`. |

### swan-tech-ch2-governing-equations.md — 완료

시작 diff의 49줄을 대조했다.
차이 표 15행의 분류와 결론은 R1 §5 최종본과 일치한다.
swantech PDF 15–21쪽의 통계 정의·전파식·구면 Jacobian을 대조했다.
PDF 60쪽의 파랑·흐름 설명과 PDF 116·153쪽의 복사응력 식을 대조했다.
현재 코드의 KSCIP1 분기·유리식 계수, 구면 플럭스, 복사응력 적분과 힘의 단위를 대조했다.
웹 수정 이력 596–598행의 Padé 설명을 확인했다.

이 표의 노트 경로는 `models/SWAN/manual-notes/swan-tech-ch2-governing-equations.md`이다.

| 구분 | 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| 정정 | `swan-tech-ch2-governing-equations.md:7` | 인쇄 7–12쪽을 PDF 15–19쪽과 같다고 적었다. | 이번 대조 범위인 인쇄 7–13쪽과 PDF 15–21쪽을 적었다. | 각 PDF 쪽의 인쇄 쪽 번호. |
| 정정 | `swan-tech-ch2-governing-equations.md:23` | 인쇄 7–12쪽 범위와 SWAN의 모든 verified 식의 1차 출처라는 표현을 썼다. | 실제 대조 범위와 §2.1·§2.2의 주제를 적었다. | swantech PDF 15–21쪽의 절 제목과 식. |
| 보완 | `swan-tech-ch2-governing-equations.md:177` | Longuet-Higgins–Stewart의 연도를 식 (2.16)만으로 인용했다. | 세 논문 연도와 작용량 수지 채택을 설명하는 §2.4의 PDF 쪽을 보탰다. | swantech PDF 60쪽: `Longuet-Higgins and Stewart (1960, 1961, 1962)`와 `action balance equation has been adopted`. |
| 정정 | `swan-tech-ch2-governing-equations.md:204` | 방향 굴절 속도에 GSE 보정 노트를 연결했다. | 방향 굴절과 GSE의 공간 확산을 구분했다. | `SwanGSECorr.ftn90:40`: `Computes waveage-dependent diffusion terms in x-y space`. |
| 정정 | `swan-tech-ch2-governing-equations.md:230` | GSE 노트를 식 (2.13)의 방향 굴절 보정으로 설명했다. | 파령 의존 공간 확산으로 설명했다. | 같은 `SwanGSECorr.ftn90:40`. |

### swan-tech-ch6-iterative-solvers.md — 완료

시작 diff의 29줄을 대조했다.
frontmatter의 식 번호와 PDF·HTML의 대응을 확인했다.
차이 표 7행의 분류와 결론은 R1·R7 최종본과 일치한다.
swantech PDF 89–90·135–136쪽과 swanuse PDF 95쪽을 대조했다.
HTML swantech node78–80과 swanuse node29:521–639를 대조했다.
SIP의 보정 인자·대각 보강·잔차 기준·실패 복구를 코드와 대조했다.
SWSOR의 완화계수·최대 갱신량·실패 복구를 코드와 대조했다.
현재 소스 저장소에서 대소문자를 무시한 `call\s+swsor` 검색은 0건이다.
해법 선택 분기와 SWSIP 호출 위치는 `swancom1.ftn:3656–3715`와 일치한다.
웹 수정 이력 336–347행과 599–600행의 여러 줄에 걸친 문장이 노트의 인용과 일치한다.
정정과 보완은 없다.

### swan-grid-readers.md — 완료

시작 diff의 29줄을 대조했다.
네 루틴의 작성자·신설 판·신설 월과 각 읽기 문장을 대조했다.
READGRID UNSTRUCTURED는 swanuse PDF 43쪽 / 인쇄 35쪽에 있다.
swantech §8.2는 PDF 145쪽 / 인쇄 137쪽에 있다.
ADCIRC의 경계 목록 처리와 Triangle의 속성 분기를 확인했다.
Easymesh의 노드 읽기는 좌표와 경계표지를 소비한다.
격자 객체의 구성과 시간 단계 루틴의 객체 참조를 확인했다.
R4:T1-312의 분류와 결론 문장은 보고서 최종본과 일치한다.
해당 행의 과거 노트 인용은 R4 §4에 보존된 반영 전 문구임을 보완했다.

이 표의 노트 경로는 `models/SWAN/source-analysis/swan-grid-readers.md`이다.

| 구분 | 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| 정정 | `swan-grid-readers.md:6` | READGRID UNSTRUCTURED를 `p.34`로 인용했다. | PDF 43쪽 / 인쇄 35쪽으로 고쳤다. | swanuse PDF 42쪽 / 인쇄 34쪽은 READGRID COORDINATES이다. PDF 43쪽 / 인쇄 35쪽은 READGRID UNSTRUCTURED이다. |
| 정정 | `swan-grid-readers.md:45` | 리더를 결합의 핵심 경로와 41.20 확장의 기반이라고 단정했다. | 실제 격자 읽기 호출과 결합 확장의 이력 주석을 각각 적었다. | `SwanReadGrid.ftn90:73–77`. `SwanReadADCGrid.ftn90:95,122,135,148–176`. `SwanCompUnstruc.ftn90:38,56`. |
| 보완 | `swan-grid-readers.md:94` | 배열과 격자 객체를 공통 변환이라는 화살표로 묶었다. | 리더의 배열 저장과 이후 격자 객체 구성을 구분했다. | 세 리더의 `use SwanGriddata`와 읽기 문장. `SwanGridTopology.ftn90:50–51,70–88`. |
| 정정 | `swan-grid-readers.md:102` | Easymesh의 소비 속성을 `단일`로 적었다. | 좌표·노드 경계표지·삼각형 연결로 고쳤다. | `SwanReadEasymeshGrid.ftn90:105`: `xcugrd(j), ycugrd(j), vmark(j)`. 같은 파일 132행의 `kvertc(1,j), kvertc(2,j), kvertc(3,j), line`. |
| 정정 | `swan-grid-readers.md:107` | 분야·라이선스도 있는 표 전체를 소비 필드로 한정한다고 적었다. | 소비 필드 설명의 대상을 속성 행으로 한정했다. 경계 읽기 위치를 명시했다. | 표의 실제 행 구성. `SwanReadADCGrid.ftn90:148–176`. |
| 정정 | `swan-grid-readers.md:113` | READGRID UNSTRUCTURED를 `p.34`로 인용했다. | PDF 43쪽 / 인쇄 35쪽으로 고쳤다. 격자 생성 절의 쪽도 명시했다. | swanuse PDF 43쪽. swantech PDF 145쪽. |
| 보완 | `swan-grid-readers.md:115` | 시간 단계 루틴에 좌표·연결 사용이라는 설명만 붙였다. | 격자 객체를 거치는 연결과 직접 참조 원문을 보탰다. | `SwanGridTopology.ftn90:70–88`. `SwanCompUnstruc.ftn90:323–324`. |
| 정정 | `swan-grid-readers.md:116` | fort.14 리더를 결합의 격자 경로로만 설명했다. | 링크의 격자 읽기 절과 결합 인터페이스 절을 구분했다. | `swan-adcirc-coupling.md` §A·§B. `SwanReadGrid.ftn90:73–77`. |
| 보완 | `swan-grid-readers.md:139` | 삭제된 `다중 (NodeAttribute)`를 현재 노트 101행처럼 인용했다. | R4 §4에 보존된 반영 전 노트 인용임을 밝혔다. | `swan-inputs-setup-vs-code.md:257,360`. |

## 기계 확인 후보 판정

- `swan-programming-rules.md:217`, BAD `README.md:30`: 오판이다. `models/SWAN/raw/source_code/swan/README.md:30`에 `This Readme provides a brief overview of software installation and configuration instructions for users and developers.`가 그대로 있다. 노트 인용을 유지했다.
- `swan-tech-ch6-iterative-solvers.md:88`, BAD `website/modifications/modifications.htm:336`: 오판이다. HTML 336–347행을 이어 읽으면 SIP 적용 조건과 BiCGSTAB 대비 4–5배 문장이 노트의 인용과 일치한다. 인용 시작 줄 336도 맞다. 노트 인용을 유지했다.

## 최종 확인

전체 대상 325줄의 대조를 마쳤다.
정정은 42줄이다.
보완은 8줄이다.
정정에는 시작 diff 밖의 개수 연동 정정 5줄이 포함된다.
보완에는 누락된 SOURCE 행 1줄이 포함된다.
정정·보완한 50줄에는 지정 태그가 있다.
정정 후 `git diff -U0 HEAD`의 대상 노트 추가 줄은 총 331줄이다.
이는 시작 대상 325줄에 연동 정정 5줄과 SOURCE 행 1줄이 더해진 결과이다.
차이 표 107행의 분류 문구는 보고서 최종본과 일치한다.
결론 문장은 105행에서 보고서의 최종 결론을 유지했다.
NT-007과 OQ-009는 위 완료 기록에 적은 원문 판정으로 정리했다.
최종 추가 줄의 상대 링크 88개는 모두 실제 파일을 가리킨다.
대상 노트 6개의 frontmatter는 YAML로 읽힌다.
대상 노트에는 금지된 절대 경로와 이중 대괄호가 없다.
지정된 미완료 표현도 없다.
시작 대상 줄에는 mermaid 상자가 없다.
`git diff --check`의 오류는 0건이다.
미해결 항목은 0건이다.

아래 범위는 작업 시작 시점의 줄 번호이다.
빈 줄과 frontmatter도 범위에 포함된다.

| 노트 | 대조한 시작 + 줄 범위 |
|---|---|
| `swan-programming-rules.md` | `7–8, 44, 49, 66–68, 111, 147, 156–158, 160–220` |
| `swan-tech-ch2-obstacles-diffraction-setup.md` | `5, 7–8, 11, 21, 23, 32, 70, 74, 76, 79, 81, 83, 85–89, 92, 95, 98–101, 103, 105–107, 112, 115–123, 129, 135, 138, 141–142, 147, 151–152, 159, 161–162, 166, 168–169, 173–207` |
| `swan-setup-solver-swancom1-crosswalk.md` | `7, 11, 13, 16, 20–25, 30, 35–36, 42–43, 45, 47, 49–52, 54–55, 57–58, 62, 80–82, 94, 109–111, 116–117, 131, 141–144, 151, 153, 155, 162–176` |
| `swan-tech-ch2-governing-equations.md` | `7–8, 23, 80, 108–110, 177, 186, 190, 192, 202–205, 210–211, 223–254` |
| `swan-tech-ch6-iterative-solvers.md` | `7–8, 20, 29, 39–40, 53, 59–61, 63, 72–89` |
| `swan-grid-readers.md` | `6–7, 45, 94, 101–103, 107–109, 113–117, 123, 125, 127–128, 130–139` |
