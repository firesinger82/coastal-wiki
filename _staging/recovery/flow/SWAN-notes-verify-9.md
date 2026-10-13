# SWAN 노트 추가·수정 줄 원문 대조

검증일: 2026-10-13.

대상은 사용자 지정 노트 6개의 작업 시작 시점 `git diff -U0 HEAD -- <노트>`에 있는 `+` 줄이다.
frontmatter, 빈 줄, 표 구분선, 코드 울타리도 줄 수에 포함한다.
현재 코드, 과거 커밋 원문, 로컬 HTML, PDF, 결론 근거 보고서의 최종 판정을 대조한다.
정정 수와 보완 수는 각각 표지를 붙여 변경한 노트 줄 수로 센다.
노트의 줄 번호는 각 노트 검증 완료 시점의 번호이다.

| 대상 노트 | 시작 시점 + 줄 수 | 대조한 + 줄 수 | 정정 수 | 보완 수 | 상태 |
|---|---:|---:|---:|---:|---|
| `models/SWAN/source-analysis/swan-propagation-implementation.md` | 83 | 83 | 2 | 0 | 완료 |
| `models/SWAN/source-analysis/swan-quasi-coherent.md` | 57 | 57 | 2 | 0 | 완료 |
| `models/SWAN/manual-notes/swan-tech-ch3-refraction-limiter.md` | 46 | 46 | 6 | 0 | 완료 |
| `models/SWAN/manual-notes/swan-tech-ch3-discretization.md` | 44 | 44 | 1 | 0 | 완료 |
| `models/SWAN/source-analysis/swan-main-boundary-init-sourcemap.md` | 25 | 25 | 5 | 0 | 완료 |
| `models/SWAN/manual-notes/README.md` | 24 | 24 | 0 | 0 | 완료 |
| 합계 | 279 | 279 | 16 | 0 | 완료 |

## 노트별 검증 기록

### swan-propagation-implementation.md

- 대조한 시작 시점 `+` 줄은 6–7, 34, 70–73, 75, 77–79, 85, 91–98, 100, 143, 152–154, 180, 182, 184, 186, 188, 194–195, 197, 199, 203, 205, 211, 267–312이다.
- 위 범위의 줄 수는 `git diff -U0 HEAD`에서 센 83줄이다.
- R1 §4·§5, R5 §5, R8 §8의 해당 행 분류와 결론을 대조했다.
- T1-007은 R8:758의 최종 F 판정과 일치한다.
- 현재 코드의 인용 구간과 조건문을 대조했다.
- `2980d1a:src/swancom1.ftn:9791–9795`에서 TN-080의 STOPC 논리식을 확인했다.
- swantech PDF 16·18·90–92·99·135–136쪽과 swanuse PDF 93–95·141쪽을 대조했다.
- HTML의 여러 줄에 걸친 문장을 인용 시작 줄에서 이어 읽었다.
- 소스 저장소 `git show`의 HEAD는 `43e9bbb`, 날짜는 2026-07-13이다.
- `src/swanmain.ftn:965`의 버전은 `VERNUM = 41.51`이다.
- 소스 저장소 전체의 대소문자 무시 `call\s+swsor` 검색 결과는 0건이다.
- frontmatter의 반영일과 반영 범위는 `SWAN-notes-apply-4.md:27,133`과 일치한다.
- 추가 줄의 상대 링크 60개는 모두 실제 파일을 가리킨다.
- 추가 줄에 개인 절대 경로, 이중 대괄호, 사용자 지정 한계 문장이 없다.
- 추가 줄에 mermaid 상자는 없다.

정정 목록:

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `models/SWAN/source-analysis/swan-propagation-implementation.md:275` | `IF (SND.GE.2.5) THEN` | `IF (SND .GE. 2.5) THEN` | `src/swanser.ftn:699`의 `IF (SND .GE. 2.5) THEN`과 공백을 맞췄다. TN-003의 C 결론은 유지했다. |
| `models/SWAN/source-analysis/swan-propagation-implementation.md:290` | `IF (SND.GE.2.5) THEN` | `IF (SND .GE. 2.5) THEN` | 같은 원문의 조건문을 TC-001에도 적용했다. TC-001의 C 결론은 유지했다. |

기계 확인 후보: 이 노트에 지정된 후보는 없다.

### swan-quasi-coherent.md

- 대조한 시작 시점 `+` 줄은 6–7, 21, 65–66, 74, 83, 85–87, 91, 93, 95, 99, 101, 103, 109, 112–113, 119–121, 125–130, 134–162이다.
- 위 범위의 줄 수는 `git diff -U0 HEAD`에서 센 57줄이다.
- R1·R3·R5의 해당 행 분류와 최종 결론을 대조했다.
- CP-016의 누락 범위는 아래 원문에 따라 정정했다.
- 나머지 결론은 최종 보고서와 의미가 같다.
- NT-038은 보고서의 정량 근거 사용 금지 결론을 유지한다.
- 현재 코드의 FFT 대상, 야코비안, 기울기 분기, QC 쇄파 제어를 인용 위치에서 대조했다.
- `SwanQCM.ftn90`은 3464줄이다.
- 이 파일의 subroutine 선언은 중첩 선언을 포함하여 12개이다.
- CP-012–015와 QC-086의 과거 인용은 `b2ae30e`, `7ee8981`, `43e9bbb`의 `git show HASH:src/SwanQCM.ftn90`으로 대조했다.
- 이 행들의 E·강함 판정은 `SWAN-git-verify-E.md:32,37–40`과 같다.
- swantech PDF 68–70·74–75·111–114쪽과 swanuse PDF 37·90–91·94쪽을 대조했다.
- 웹 `swanuse/node23.html:451–478`과 `node28.html:3421–3446`을 대조했다.
- [Akrish 외 (2020)의 TU Delft 최종본](https://pure.tudelft.nl/ws/portalfiles/portal/71750151/modelling_statistical_wave_interferences_over_shear_currents.pdf) A2-4–A2-6에서 작용 변수와 정규화 식을 대조했다.
- 추가 줄의 상대 링크 13개는 모두 실제 파일을 가리킨다.
- 추가 줄에 개인 절대 경로, 이중 대괄호, 사용자 지정 한계 문장이 없다.
- 추가 줄에 mermaid 상자는 없다.

정정 목록:

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `models/SWAN/source-analysis/swan-quasi-coherent.md:7` | `Tech §2.7 ... p.58-64` 등 쪽 체계가 불명확한 검증 범위 | 이번 대조의 코드·PDF 쪽·논문 인쇄 쪽을 명시했다. | 식 (2.147)은 swantech PDF 68쪽 / 인쇄 60쪽이다. 식 (2.153)·(2.154)는 PDF 74쪽 / 인쇄 66쪽이다. SCAT 설명은 swanuse PDF 90–91쪽 / 인쇄 82–83쪽이다. |
| `models/SWAN/source-analysis/swan-quasi-coherent.md:152` | NUMERIC 절에 QC 초기화의 입사파고 배율이 없다고 서술했다. | `[dabs] × Hinc`의 문서 설명을 명시했다. C를 격자·보간·영값·sweep 재사용의 구현 세부로 한정했다. | swanuse PDF 94쪽 / 인쇄 86쪽: `less than [dabs] ×Hinc`, `Hinc is the representative incident wave height`. `src/SwanQCM.ftn90:350`: `PNUMS(2) = PNUMS(2) * hsi`. |

CP-016의 원 문장은 R3:603의 최종 보고서와 같았다.
PDF 원문은 그 문장의 누락 주장을 반박한다.
이번 판정은 노트에서 그 누락 주장만 제거한다.
보고서 파일은 쓰기 대상이 아니므로 변경하지 않았다.

기계 확인 후보: 이 노트에 지정된 후보는 없다.

### swan-tech-ch3-refraction-limiter.md

- 대조한 시작 시점 `+` 줄은 7–8, 83, 90–92, 102, 114, 120–122, 128, 140–173이다.
- 위 범위의 줄 수는 `git diff -U0 HEAD`에서 센 46줄이다.
- R1 §5와 R7 §5의 해당 행 분류와 결론은 일치한다.
- H-1227은 R7:1086의 C 판정과 일치한다.
- swantech PDF 100–110쪽과 swanuse PDF 95·141쪽을 대조했다.
- swantech PDF 102쪽 이미지에서 식 (3.35)와 시간 척도의 절댓값 기호를 확인했다.
- 굴절 속도 정의는 swantech PDF 18쪽의 식 (2.13)과 대조했다.
- `2980d1a:src/swancom5.ftn:1373–1377`의 제거 주석과 2023-02-27 날짜를 확인했다.
- `122b595:src/swancom5.ftn:1671,1714`의 제한식은 현재 코드와 같다.
- TN-108의 D 판정은 `SWAN-git-verify-D.md`와 일치한다.
- 코드의 제한 스위치, 굴절 기울기, 구면 보정 순서, 일반 주석을 대조했다.
- `switch.pl:82–105`는 지정된 접두사만 제거한다.
- 이 전처리는 일반 주석인 `!if ( dpmax > drat * dpmin )`를 활성화하지 않는다.
- 추가 줄의 상대 링크 10개는 모두 실제 파일을 가리킨다.
- 추가 줄에 개인 절대 경로, 이중 대괄호, 사용자 지정 한계 문장이 없다.
- 추가 줄에 mermaid 상자는 없다.

정정 목록:

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `models/SWAN/manual-notes/swan-tech-ch3-refraction-limiter.md:7` | `online HTML +15 offset` | HTML 식 번호와 PDF 식 번호의 차이는 일정하지 않다고 정정했다. | HTML node51의 에너지식 (3.46)은 PDF (3.31)에 대응한다. node52의 방향 CFL 식 (3.62)은 PDF (3.38)에 대응한다. |
| `models/SWAN/manual-notes/swan-tech-ch3-refraction-limiter.md:83` | `PNUMS(35) = 0.` | `PNUMS(35) = 0.0` | `src/swanmain.ftn:1331`의 수치 표기를 그대로 옮겼다. |
| `models/SWAN/manual-notes/swan-tech-ch3-refraction-limiter.md:128` | `REFRLIM (α_θ=0.9)`를 방향 CFL 제한의 명령으로 기술했다. | `NUMERIC CTHETA`로 정정했다. | swanuse PDF 95쪽은 CTHETA의 방향 CFL 제한과 활성화 계수 0.9를 설명한다. |
| `models/SWAN/manual-notes/swan-tech-ch3-refraction-limiter.md:140` | BSBT/GSE/hybrid가 semi-Lagrangian 기반을 공유한다고 기술했다. | 연결 노트가 공간·스펙트럼 이산화를 정리한다고 기술했다. | swantech PDF 104–105쪽의 semi-Lagrangian 해석은 특정 1차 풍상·음해법 Euler 근사에 대한 설명이다. 이를 나열한 모든 해법의 공통 기반으로 확대하지 않았다. |
| `models/SWAN/manual-notes/swan-tech-ch3-refraction-limiter.md:142` | 굴절 속도 정의를 식 (2.14)로 연결했다. | 식 (2.13)으로 정정했다. | swantech PDF 18쪽에서 (2.13)은 전파 속도이고 (2.14)는 파수 벡터이다. |
| `models/SWAN/manual-notes/swan-tech-ch3-refraction-limiter.md:162` | `PNUMS(35) = 0.`; HTML 473–485행 | `PNUMS(35) = 0.0`; HTML 471–485행 | `src/swanmain.ftn:1331`과 `swanuse/node29.html:471`의 기본 비활성 문장을 반영했다. |

기계 확인 후보 판정:

- `website/modifications/modifications.htm:695` 후보는 오탐이다. 노트 172줄의 전체 인용은 원문 695–713행에 걸쳐 있다. 줄바꿈을 연결하면 인용 문장과 같다. 노트는 유지했다.
- `website/modifications/modifications.htm:778` 후보는 오탐이다. 노트 173줄의 전체 인용은 원문 778–788행에 걸쳐 있다. `c<sub>q</sub>`와 `kd&lt;3.0`의 HTML 표기를 읽으면 노트의 `cq`와 `kd<3.0`에 대응한다. 노트는 유지했다.

### swan-tech-ch3-discretization.md

- 대조한 시작 시점 `+` 줄은 7–8, 22, 71, 77, 101, 103–107, 111, 139, 144–174이다.
- 위 범위의 줄 수는 `git diff -U0 HEAD`에서 센 44줄이다.
- R1 §5와 R7:H-1331의 분류와 최종 결론은 일치한다.
- TC-023의 E·중간 판정은 `SWAN-git-verify-E.md:29`와 일치한다.
- swantech PDF 19–20·78–87쪽과 swanuse PDF 92·141쪽을 대조했다.
- 식 (3.9)의 분모는 현재 시간항에서 `12Δx`이다.
- 같은 식의 이전 시간항 분모는 `4Δx`이다.
- 식 (3.14)·(3.15)의 두 이동 방향과 혼합 계수는 원문과 같다.
- HTML node37–41의 식 번호를 PDF와 대조했다.
- HTML의 (3.20)·(3.21)은 PDF의 (3.14)·(3.15)에 대응한다.
- 현재 코드의 소수 계수, GSE 교차차분, 혼합 매개변수, 차수 전환, 명시 주파수 CFL, 음수 제거 조건을 대조했다.
- `src/swancom1.ftn:6678–6684`에서 ANYBLK 행의 대각 1과 나머지 계수 0을 확인했다.
- `src/SwanGSECorr.ftn90:143–144`에서 Dss·Dnn 구현을 확인했다.
- 추가 줄의 상대 링크 9개는 모두 실제 파일을 가리킨다.
- 추가 줄에 개인 절대 경로, 이중 대괄호, 사용자 지정 한계 문장이 없다.
- 추가 줄에 mermaid 상자는 없다.

정정 목록:

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `models/SWAN/manual-notes/swan-tech-ch3-discretization.md:147` | `action balance source-analysis` | 작용수지식과 원천항을 정리한 매뉴얼 노트라고 기술했다. | 실제 대상은 `models/SWAN/manual-notes/swan-action-balance.md`이다. 해당 노트의 제목은 `SWAN Action Balance + Source Terms`이다. |

기계 확인 후보: 이 노트에 지정된 후보는 없다.

### swan-main-boundary-init-sourcemap.md

- 대조한 시작 시점 `+` 줄은 6–7, 40, 50–51, 57–59, 64–80이다.
- 위 범위의 줄 수는 `git diff -U0 HEAD`에서 센 25줄이다.
- R3:NT-044·NT-045, R4:T1-011·T1-192·T1-240·T1-305, R7:H-1447의 분류와 최종 결론은 일치한다.
- T1-011의 E·강함 판정은 `SWAN-git-verify-E.md`와 일치한다.
- swanuse PDF 19·64쪽을 대조했다.
- `website/modifications/modifications.htm:1447–1448`의 영 파고 경고 문장을 대조했다.
- 현재 코드에서 RESPEC 방향 분포, SVALQI 영역 판정, FLFILE 시간 보간, SWINCO 초기화 분기를 대조했다.
- `src/swanmain.ftn:8332–8337`의 FAC 계수는 1.2·1.096·1.01이다.
- 이 코드 줄의 `41.99` 표지는 원문에 있다.
- 기본 초기화의 방향 지수는 풍속 조건의 THEN 분기에서 2이다.
- 같은 조건의 ELSE 분기에서 방향 지수는 0이다.
- SSHAPE 호출의 마지막 인수 2는 방향 표현 방식이다.
- 앞의 방향 지수와 이 인수를 구분했다.
- 추가 줄의 상대 링크 7개는 모두 실제 파일을 가리킨다.
- 추가 줄에 개인 절대 경로, 이중 대괄호, 사용자 지정 한계 문장이 없다.
- 추가 줄에 mermaid 상자는 없다.

정정 목록:

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `models/SWAN/source-analysis/swan-main-boundary-init-sourcemap.md:6` | `swanmain.ftn (9338행` | `swanmain.ftn (9343행` | 현재 소스 파일의 전체 줄 수는 9343이다. |
| `models/SWAN/source-analysis/swan-main-boundary-init-sourcemap.md:40` | 도 단위 확산에 역제곱식을 조건 없이 적용한다고 기술했다. 방향 분포의 바닥값을 일괄 1.E-10으로 기술했다. | DSPR≠0일 때만 역제곱식을 적용한다고 기술했다. DSPR=0이면 MS=1000이라고 기술했다. 두 방향 분기의 CDIR 식을 각각 명시했다. | `src/swanmain.ftn:8341–8344`: `IF (DSPR.NE.0.) THEN`, `MS = MAX (FAC*DSPR**(-2) - 2., 1.)`, ELSE의 `MS = 1000.`. 8367행은 `CDIR = CTOT * MAX (ACOS**MS, 1.E-10)`이다. 8369행은 `CDIR = 1.E-10`이다. |
| `models/SWAN/source-analysis/swan-main-boundary-init-sourcemap.md:59` | 내부점 조건을 항상 4방 이웃으로 기술했다. 시드 분기를 무풍으로만 기술했다. | x 방향 이웃과 해당 점은 항상 검사한다고 기술했다. y 방향 이웃은 1차원이 아닐 때 검사한다고 기술했다. 시드는 풍속 조건의 ELSE 분기에 대입한다고 기술했다. | `src/swanmain.ftn:9028–9041`의 `IF (.NOT.ONED) THEN`과 해당 점 검사. 9065행의 `IF (WSLOC .GT. 1.E-10) THEN`에 대응하는 ELSE에서 9086–9089행의 시드 값을 대입한다. |
| `models/SWAN/source-analysis/swan-main-boundary-init-sourcemap.md:64` | 경계·입력장을 모두 무음 동결로 기술했다. RESPEC 읽기오류를 실행 비종결로 단정했다. | 경계 파일 소진의 수준 1 메시지를 명시했다. 입력장의 종료 처리문을 명시했다. RESPEC 설명은 읽기오류 분기의 IERR 미설정으로 한정했다. | `src/swanmain.ftn:8019`의 `CALL MSGERR (1, 'data on boundary file exhausted')`. 8735–8754행의 `IFLTIM(IGR1) = 1.E10`. 8507–8512행은 MSGERR 호출 후 IERR 대입 없이 RETURN한다. |
| `models/SWAN/source-analysis/swan-main-boundary-init-sourcemap.md:76` | `src/swanmain.ftn:4896`에 `ZERO=1`이라는 원문이 있다고 표시했다. | 호출의 다섯째 인수 1이 ZERO에 전달된다고 설명했다. | 4896행의 `WLVL = SVALQI (XP, YP, 7, WLEVL, 1 ,IX ,IY)`. 5309행의 `REAL FUNCTION SVALQI (XP, YP, IGRID, ARRINP, ZERO ,IXC ,IYC)`. E·강함 결론은 유지했다. |

기계 확인 후보 판정:

- `src/swanmain.ftn:4896`의 `ZERO=1` 후보는 실제 인용 오류이다. 원문은 ZERO에 1을 전달하는 함수 호출이다. 노트 76줄을 함수 인수 설명으로 정정했다.

### manual-notes/README.md

- 대조한 시작 시점 `+` 줄은 1–4, 6–25이다.
- 위 범위의 줄 수는 `git diff -U0 HEAD`에서 센 24줄이다.
- frontmatter의 날짜와 반영 내용은 `SWAN-notes-apply-7.md:10,24`와 일치한다.
- swanimp PDF 1쪽의 문서 판은 Cycle III 41.51이다.
- swanimp PDF 5쪽의 목차는 설치·빌드·초기화 파일·실행 안내를 포함한다.
- 연결한 구현 매뉴얼 노트의 §5는 전처리 스위치를 다룬다.
- swanpgr PDF 1쪽의 문서 판은 Version 1.3이다.
- swanpgr PDF 51쪽 / 인쇄 45쪽의 Log sheet에서 v1.3 날짜는 March 22, 2006이다.
- 연결한 프로그래밍 규칙 노트에는 R7 대조 표가 있다.
- 연결한 문서 체계 노트에는 공식 문서 목차와 수정 이력·패치 대조 표가 있다.
- `models/SWAN/README.md:48–61`에 안내한 R1–R8 범위와 링크가 있다.
- `src/swanmain.ftn:965,967–968`에 버전 41.51과 BUGFIX A·B가 있다.
- 소스 저장소 `git show -s`에서 HEAD는 `43e9bbb`, 날짜는 2026-07-13이다.
- patch B 커밋 `0dabfa4`의 날짜도 2026-07-13이다.
- 이 README에는 개별 차이 결론 행이 없다.
- 담당 노트에 결론을 배정했다는 설명은 반영 기록과 같다.
- 추가 줄의 상대 링크 4개는 모두 실제 파일을 가리킨다.
- 추가 줄에 개인 절대 경로, 이중 대괄호, 사용자 지정 한계 문장이 없다.
- 추가 줄에 mermaid 상자는 없다.

정정 목록: 없음.

기계 확인 후보: 이 노트에 지정된 후보는 없다.

## 최종 확인

- 시작 시점 대상 279줄을 모두 대조했다.
- 완료 시점 `git diff -U0 HEAD`의 추가 줄 수도 279줄이다.
- 정정 표지는 16줄에 있다.
- 인용만 추가한 보완은 0줄이다.
- 정정 목록의 노트 줄 번호는 실제 표지 위치와 일치한다.
- 추가 줄의 상대 링크 103개는 모두 실제 파일을 가리킨다.
- 추가 줄에서 개인 절대 경로와 이중 대괄호는 0건이다.
- 추가 줄에서 사용자 지정 한계 문장은 0건이다.
- 대상 frontmatter 6개는 YAML로 해석된다.
- 차이 결론 표의 열 수는 유지된다.
- `DEP\|WNUM`의 파이프는 Markdown 표를 위한 이스케이프이다.
- 대상 노트의 `git diff --check`는 오류 없이 끝났다.
- 지정된 기계 확인 후보 3건 중 실제 인용 오류는 1건이다.
- 나머지 기계 확인 후보 2건은 HTML 줄바꿈·표기 때문에 생긴 오탐이다.
- 미해결 항목은 0건이다.
