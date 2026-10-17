# FUNWAVE 노트 전수 검증 2/2

- 대상 노트: `models/FUNWAVE/manual-notes/funwave-user-manual-full.md`.
- `git diff -U0 HEAD -- models/FUNWAVE/manual-notes/funwave-user-manual-full.md`의 추가 줄은 435줄이다.
- 순서대로 앞 218줄과 뒤 217줄로 나눴다.
- 담당 범위는 추가 줄 순번 219–435이다.
- 담당 범위는 노트 368–584행이다.
- 첫 줄의 행 ID는 `inputs:FI1-315`이다.
- 마지막 줄의 행 ID는 `callflow:RF-025`이다.
- 같은 노트의 다른 담당 구간은 수정하지 않는다.
- 상태: 완료. 이 노트의 배정된 2/2 구간은 대조를 마쳤다.
- 처음 표시된 diff는 도구가 중간을 잘랐다. 노트 수정 전에 명령 내부에서 전체 추가 줄을 다시 세어 범위를 확정했다.

## 대조 결과

- 대조한 추가 줄은 217줄이다.
- 정정한 줄은 33줄이다.
- 인용을 보완한 줄은 5줄이다.
- 정정·보완 없이 유지한 줄은 179줄이다.
- 아래 행별 대조 기록의 217개 ID가 집계 근거이다.
- 분류별 줄 수는 A 32줄, B 109줄, C 56줄, D 10줄, E 5줄, F 5줄이다.
- A 32행의 HASH·날짜는 `FUNWAVE-git-verify-AD1.md`·`AD2.md`·`AD3.md`의 같은 항목과 일치한다.
- E 강도는 FV1-043·FV1-470이 강함이다.
- E 강도는 FV1-444·FV1-474·FV1-510이 중간이다.
- 결론의 문서명·수식 표기·검증 표식을 제외한 문장은 보고서 최종 결론과 일치한다.
- FV1-411의 보고서 내부 참조는 실제 보고서 절로 연결했다.
- 수정 후 코드 인용 1,203개를 파일·줄 범위로 다시 검사했다.
- 이 검사에서 현재 파일과 과거 git 객체 129개를 읽었다.
- 상대 Markdown 링크 7개는 모두 실제 파일을 가리킨다.
- 담당 217줄에는 frontmatter와 mermaid 블록이 없다.
- 담당 줄에는 `/home/firesinger/`와 `[[`가 없다.
- 담당 줄에는 `실행하지 않았다`·`확인하지 않았다`·`미검수`·`후속 대상` 문장이 없다.
- 미해결 항목은 0개이다.

| 보고서 계열 | 노트 행 | 대조 줄 수 | 정정 | 보완 | 유지 |
|---|---|---:|---:|---:|---:|
| inputs | 368–370 | 3 | 0 | 0 | 3 |
| examples | 371–404 | 34 | 5 | 0 | 29 |
| v21-manual | 405–522 | 118 | 10 | 5 | 103 |
| v21-examples | 523–531 | 9 | 3 | 0 | 6 |
| aux-docs-build | 532–577 | 46 | 11 | 0 | 35 |
| callflow | 578–584 | 7 | 4 | 0 | 3 |
| 합계 | 368–584 | 217 | 33 | 5 | 179 |

현재 코드의 `src/...`는 `models/FUNWAVE/raw/source_code/FUNWAVE-TVD/src/...`를 뜻한다.
과거 `HASH:경로:줄`은 TVD 외부 저장소의 해당 git 객체를 뜻한다.
옛 노트 인용은 읽기 전용 HEAD diff로 복원한 수정 전 줄과 대조했다.
식과 수치는 쪽별 판독 기록과 300 dpi 쪽 이미지로 대조했다.
최종 판정은 각 비교 보고서의 전수 검증 기록과 최종 집계를 기준으로 삼았다.

## 정정·보완 목록

수정 위치는 `models/FUNWAVE/manual-notes/funwave-user-manual-full.md`의 행 번호이다.
정정 표식과 보완 표식은 각각 결론 문장 칸 끝에 붙였다.

| 번호 | 노트:줄 | 행 ID | 구분 | 전 → 후 | 근거 원문 |
|---:|---|---|---|---|---|
| 1 | `funwave-user-manual-full.md:372` | `examples:FX1-006` | 정정 | `F 표기 차이` → `F 표현 차이` | examples 보고서 §5 FX1-006의 최종 분류. 보고서 `funwave-examples-vs-code.md:835`. |
| 2 | `funwave-user-manual-full.md:373` | `examples:FX1-043` | 정정 | 현재 키 읽기 뒤의 `Friction_Matrix` 두 곳 → 두 낱말을 제거했다. 옛 키의 과거 코드 인용은 유지했다. | `src/io.F:2738`; `9bae2f6:src/io.F:2660`; `24a88c3:src/io.F:750`. 보고서 `funwave-examples-vs-code.md:838`. |
| 3 | `funwave-user-manual-full.md:374` | `examples:FX1-044` | 정정 | 현재 키 읽기 뒤의 `Cd_file` 두 곳 → 두 낱말을 제거했다. 옛 키의 과거 코드 인용은 유지했다. | `src/io.F:2753`; `9bae2f6:src/io.F:2675`; `24a88c3:src/io.F:751`. 보고서 `funwave-examples-vs-code.md:839`. |
| 4 | `funwave-user-manual-full.md:376` | `examples:FX1-339` | 정정 | 현재 키 읽기 뒤의 `Friction_Matrix` 두 곳 → 두 낱말을 제거했다. 옛 키의 과거 코드 인용은 유지했다. | `src/io.F:2738`; `9bae2f6:src/io.F:2660`; `24a88c3:src/io.F:750`. 보고서 `funwave-examples-vs-code.md:856`. |
| 5 | `funwave-user-manual-full.md:379` | `examples:FX1-437` | 정정 | 현재 키 읽기 뒤의 `Friction_Matrix` 두 곳 → 두 낱말을 제거했다. 옛 키의 과거 코드 인용은 유지했다. | `src/io.F:2738`; `9bae2f6:src/io.F:2660`; `24a88c3:src/io.F:750`. 보고서 `funwave-examples-vs-code.md:863`. |
| 6 | `funwave-user-manual-full.md:414` | `v21-manual:FV1-133` | 정정 | `DO ISTAGE=1,3` 뒤의 검색어 `CORRECTOR` → 검색어를 제거했다. 실제 CORRECTOR 주석은 유지했다. | `b9c035d:src/main.F:214`; `cab9425:main.F:65`; v21-manual 보고서 FV1-133의 검색어 설명. 보고서 `funwave-v21-manual-vs-code.md:1887`. |
| 7 | `funwave-user-manual-full.md:415` | `v21-manual:FV1-168` | 정정 | fluxes.F 주석 뒤의 검색어 `PREDICTOR` → 검색어를 제거했다. 원문 주석은 유지했다. | `b9c035d:src/fluxes.F:94`; `cab9425:main.F:61`; v21-manual 보고서 FV1-168의 검색어 설명. 보고서 `funwave-v21-manual-vs-code.md:1893`. |
| 8 | `funwave-user-manual-full.md:422` | `v21-manual:FV1-301` | 정정 | `CALL INITIALIZATION` 뒤의 `HOT_START`·`READ_LOGICAL` → 호출문 뒤에 섞인 검색어를 제거했다. | `src/main.F:214`는 `CALL INITIALIZATION`이다. v21-manual 보고서 FV1-301. 보고서 `funwave-v21-manual-vs-code.md:1567`. |
| 9 | `funwave-user-manual-full.md:423` | `v21-manual:FV1-302` | 정정 | FileNumber_HOTSTART 선언 뒤의 `READ_INTEGER` → 선언 뒤의 검색어를 제거했다. | `src/mod_global.F:145`의 정수 선언. v21-manual 보고서 FV1-302. 보고서 `funwave-v21-manual-vs-code.md:1568`. |
| 10 | `funwave-user-manual-full.md:435` | `v21-manual:FV1-392` | 보완 | STATIONS_FILE 읽기와 직교 격자 입력 인용 → 구면 입력 분기와 위도·경도 변환식을 추가했다. | `src/io.F:84–89,4172–4174,4197–4198`; `dum2`는 경도 격자 번호에 쓰인다. `dum1`은 위도 격자 번호에 쓰인다. 보고서 `funwave-v21-manual-vs-code.md:1585`. |
| 11 | `funwave-user-manual-full.md:441` | `v21-manual:FV1-411` | 정정 | `결함 후보는 §3에 둔다.` → `v21-manual 보고서 §3의 FV1-471`로 가는 상대 링크를 넣었다. | v21-manual 보고서 §3 FV1-471; `src/dispersion.F:480–484`. 보고서 `funwave-v21-manual-vs-code.md:1591`. |
| 12 | `funwave-user-manual-full.md:445` | `v21-manual:FV1-432` | 정정 | `src/nesting.F:98–114`의 인용 `DO` → `IF(N_COUPLING_EAST.GT.0)THEN` | `src/nesting.F:98–114`에는 여는 DO가 없다. v21-manual 보고서 FV1-432. 보고서 `funwave-v21-manual-vs-code.md:1595`. |
| 13 | `funwave-user-manual-full.md:447` | `v21-manual:FV1-444` | 정정 | 원문 인용 뒤의 `cab9425:src/` → 존재하지 않는 경로를 제거했다. | 실제 객체는 `cab9425:init.F:332`이다. v21-manual 보고서 FV1-444는 `cab9425:src/`의 부재를 설명한다. 보고서 `funwave-v21-manual-vs-code.md:1915`. |
| 14 | `funwave-user-manual-full.md:449` | `v21-manual:FV1-453` | 보완 | 줄 번호 없는 `93c0053:src/io.F`와 MAX·MIN 식의 나열 → MAX와 MIN에 각각 과거 커밋·줄 번호를 붙였다. | `d69acc3:src/io.F:2739`는 MAX이다. `93c0053:src/io.F:2947`은 MIN이다. 보고서 `funwave-v21-manual-vs-code.md:1654`. |
| 15 | `funwave-user-manual-full.md:456` | `v21-manual:FV1-470` | 정정 | 원문 인용 뒤의 `cab9425:src/` → 존재하지 않는 경로를 제거했다. | 실제 객체는 `cab9425:etauv_solver.F:412`이다. v21-manual 보고서 FV1-470. 보고서 `funwave-v21-manual-vs-code.md:1916`. |
| 16 | `funwave-user-manual-full.md:457` | `v21-manual:FV1-474` | 정정 | 원문 인용 뒤의 `cab9425:src/` → 존재하지 않는 경로를 제거했다. | 실제 객체는 `cab9425:etauv_solver.F:334`이다. v21-manual 보고서 FV1-474. 보고서 `funwave-v21-manual-vs-code.md:1920`. |
| 17 | `funwave-user-manual-full.md:464` | `v21-manual:FV1-506` | 보완 | 건조 면의 영 플럭스에 대한 직접 인용 없음 → MASK 조건과 네 면의 P·Q 영 대입을 추가했다. | `src/bc.F:223–224,241,258,275,291`. 보고서 `funwave-v21-manual-vs-code.md:1607`. |
| 18 | `funwave-user-manual-full.md:468` | `v21-manual:FV1-510` | 정정 | 원문 인용 뒤의 `cab9425:src/` → 존재하지 않는 경로를 제거했다. | 실제 객체는 `cab9425:init.F:332`이다. v21-manual 보고서 FV1-510. 보고서 `funwave-v21-manual-vs-code.md:1921`. |
| 19 | `funwave-user-manual-full.md:477` | `v21-manual:FV1-519` | 보완 | 성분표 셋째 열의 위상 단위에 대한 직접 인용 없음 → `COS(2.0_SP*PI/WAVE_COMP(kf,1)*TIME-WAVE_COMP(kf,3))` 인용을 추가했다. | `src/sources.F:138`. 보고서 `funwave-v21-manual-vs-code.md:1611`. |
| 20 | `funwave-user-manual-full.md:490` | `v21-manual:FV1-532` | 보완 | 관측점 파일 읽기 인용 → 구면 입력 분기와 위도·경도 변환식을 추가했다. | `src/io.F:84–89,4172–4174,4197–4198`. 보고서 `funwave-v21-manual-vs-code.md:1623`. |
| 21 | `funwave-user-manual-full.md:523` | `v21-examples:FV2-059` | 정정 | `src/io.F:2634`의 `# endif` 뒤에 붙은 `Gamma2 = 0.0` → 문서 입력값을 코드 칸에서 제거했다. | `src/io.F:2634`; 구면 예제의 문서 입력은 문서 칸에 유지했다. 보고서 `funwave-v21-examples-vs-code.md:707`. |
| 22 | `funwave-user-manual-full.md:524` | `v21-examples:FV2-062` | 정정 | `src/io.F:2636` 뒤의 `-DZALPHA`·`funwave_tvd_3.0.tex` → 코드에 없는 문서 검색어를 제거했다. | `src/io.F:2636`은 Beta_ref 읽기 문장이다. 보고서 `funwave-v21-examples-vs-code.md:708`. |
| 23 | `funwave-user-manual-full.md:526` | `v21-examples:FV2-310` | 정정 | `src/io.F:616`의 `STOP` 뒤에 붙은 `funwave_tvd_3.0.tex` → 코드에 없는 문서 파일명을 제거했다. | `src/io.F:616`. 보고서 `funwave-v21-examples-vs-code.md:729`. |
| 24 | `funwave-user-manual-full.md:564` | `aux-docs-build:FN1-904` | 정정 | `bfc2f8c:src/samples.F:45`; cab6d74 선언 뒤의 `-DSAMPLES` → `bfc2f8c:samples.F:45`로 고쳤다. 선언 뒤의 문서 플래그를 제거했다. | `bfc2f8c:samples.F:45`; `cab6d74:src/samples.F:56`. 보고서 `funwave-aux-docs-build-vs-code.md:956`. |
| 25 | `funwave-user-manual-full.md:566` | `aux-docs-build:FN1-906` | 정정 | 코드 칸의 `HOT START`, `INI UVZ`, `FileNumber HOTSTART`, `DEPTH TYPE`, `DATA`, `FLAT`, `DEPTH FLAT`, `SLOPE`, `SLP`, `Xslp`, `DEPTH FLAT`, `RESULT FOLDER`, `TOTAL TIME`, `PLOT INTV`, `INT UVZ` → 정정 전 노트의 입력 목록을 코드 칸에서 제거했다. 문서 칸의 원래 인용은 유지했다. | `src/io.F:712`는 INI_UVZ 읽기 문장이다. aux-docs-build 보고서 FN1-906은 목록을 옛 노트 인용으로 제시한다. 보고서 `funwave-aux-docs-build-vs-code.md:958`. |
| 26 | `funwave-user-manual-full.md:567` | `aux-docs-build:FN1-907` | 정정 | `bfc2f8c:src/misc.F:106` → `bfc2f8c:misc.F:106` | 실제 git 객체 `bfc2f8c:misc.F:106`. 보고서 `funwave-aux-docs-build-vs-code.md:959`. |
| 27 | `funwave-user-manual-full.md:568` | `aux-docs-build:FN1-908` | 정정 | `bfc2f8c:src/mod_global.F:383`; `ELSE` 뒤의 `VISCOSITY BREAKING` → `bfc2f8c:mod_global.F:383`으로 고쳤다. 공백 키를 코드 칸에서 제거했다. | `bfc2f8c:mod_global.F:383`; `src/masks.F:180`은 ELSE이다. 보고서 `funwave-aux-docs-build-vs-code.md:960`. |
| 28 | `funwave-user-manual-full.md:569` | `aux-docs-build:FN1-909` | 정정 | 코드 칸의 `SWE ETA DEP` 두 곳 → 옛 노트의 공백 키를 코드 칸에서 제거했다. | `src/io.F:2715`; `src/masks.F:180`. 보고서 `funwave-aux-docs-build-vs-code.md:961`. |
| 29 | `funwave-user-manual-full.md:571` | `aux-docs-build:FN1-911` | 정정 | `bfc2f8c:src/io.F:308`; 코드 칸의 `WIND FILE`·`time(s), wu, wv(m/s)` → `bfc2f8c:io.F:308`로 고쳤다. 문서 입력 표현을 코드 칸에서 제거했다. | `bfc2f8c:io.F:308`; `src/mod_meteo.F:54,340`은 전처리 조건과 설정 호출이다. 보고서 `funwave-aux-docs-build-vs-code.md:963`. |
| 30 | `funwave-user-manual-full.md:572` | `aux-docs-build:FN1-912` | 정정 | 시간 완화식 뒤의 `Delta WK`·`Time ramp`·`Theta WK`·`Sigma Theta` 목록 두 곳 → 옛 노트의 입력 이름을 코드 칸에서 제거했다. | `src/sources.F:136`; `cab6d74:src/sources.F:125`. 보고서 `funwave-aux-docs-build-vs-code.md:964`. |
| 31 | `funwave-user-manual-full.md:574` | `aux-docs-build:FN1-914` | 정정 | `Eta)` 뒤의 `GAUSIAN`·`AMP`·`Xc`·`Yc`·`WID` → 문서의 옵션 목록을 코드 칸에서 제거했다. | `src/init.F:935–938`; 실제 선택 문자열은 INI_GAU이다. 보고서 `funwave-aux-docs-build-vs-code.md:966`. |
| 32 | `funwave-user-manual-full.md:575` | `aux-docs-build:FN1-915` | 정정 | 코드 칸에서 따로 반복된 `PERIODIC` 두 곳 → 별도 낱말을 제거했다. 실제 읽기·조건 인용은 유지했다. | `src/io.F:2260`; `src/tridiagnal.F:232`는 `# endif`이다. 보고서 `funwave-aux-docs-build-vs-code.md:967`. |
| 33 | `funwave-user-manual-full.md:576` | `aux-docs-build:FN1-916` | 정정 | `Cd_fixed = 0.0_SP` 뒤의 `Cd fixed` → 옛 노트의 공백 키를 코드 칸에서 제거했다. | `src/io.F:2779`. 보고서 `funwave-aux-docs-build-vs-code.md:968`. |
| 34 | `funwave-user-manual-full.md:577` | `aux-docs-build:FN1-917` | 정정 | `DO ISTAGE=1,3` 뒤의 `Time Scheme`·`Runge Kutta`·`Predictor Corrector` → 옛 노트의 적분기 표기를 코드 칸에서 제거했다. | `src/main.F:380`. 보고서 `funwave-aux-docs-build-vs-code.md:969`. |
| 35 | `funwave-user-manual-full.md:579` | `callflow:RF-003` | 정정 | `init.F:895`에 IF와 CALL을 함께 인용했다. `init.F:1331`의 유속 조건 뒤에 ETA 읽기를 붙였다. → 호출 범위를 `895–896`으로 고쳤다. `1331–1333`의 조건부 U·V 읽기와 `1339`의 ETA 읽기를 분리했다. | `src/init.F:895–896,1331–1339`. 보고서 `FUNWAVE-callflow.md:3061`. |
| 36 | `funwave-user-manual-full.md:582` | `callflow:RF-010` | 정정 | 과거 `main.F:246`과 현재 `main.F:483` 뒤의 네 문장에 백틱·줄바꿈이 섞였다. → 과거 범위를 `246–250`으로 고쳤다. 현재 범위를 `483–487`로 고쳤다. IF·CALL·ENDIF·ENDDO를 각각 코드 인용으로 표시했다. | `24a88c3:src/main.F:246–250`; `src/main.F:483–487`. 보고서 `FUNWAVE-callflow.md:3068`. |
| 37 | `funwave-user-manual-full.md:583` | `callflow:RF-019` | 정정 | `cab9425:main.F:65` 주석 뒤의 `-G` → git 검색 옵션을 코드 인용에서 제거했다. | `cab9425:main.F:65`는 CORRECTOR 주석이다. callflow 보고서 RF-019. 보고서 `FUNWAVE-callflow.md:3077`. |
| 38 | `funwave-user-manual-full.md:584` | `callflow:RF-025` | 정정 | SAMPLES 조건 뒤의 `-DSAMPLES: include all samples, default is no sample included.` → 문서 설명을 코드 칸에서 제거했다. | `b9c035d:src/init.F:744`는 `# if defined(SAMPLES)`이다. 문서 설명은 2.1 매뉴얼 p.34에 있다. 보고서 `FUNWAVE-callflow.md:3083`. |

## 기계 확인 후보 판정

요청에 적힌 순서를 유지했다.
중복된 후보도 각각 한 줄로 기록했다.
수정 전 노트의 인용은 비교 대상의 과거 문장으로 판정했다.

| 번호 | 기계 확인 후보 | 원문 대조 판정 |
|---:|---|---|
| 01 | src/init.F:744 — `; ` | 구분자 오판이다. `b9c035d:src/init.F:744`의 원문은 `# if defined(SAMPLES)`이다. RF-025에 섞인 문서 설명은 별도로 제거했다. |
| 02 | src/dispersion.F:388 — `; ` | 구분자 오판이다. `b9c035d:src/dispersion.F:388–389`의 U1pp 식을 열어 대조했다. 식과 인용은 일치한다. |
| 03 | src/dispersion.F:388 — 공백 | 공백 경계 오판이다. 같은 `b9c035d:src/dispersion.F:388–389`의 식을 대조했다. Beta_2의 계수·부호는 일치한다. |
| 04 | src/sources.F:169 — `; ` | 구분자 오판이다. `7b93138:src/sources.F:169–188`을 대조했다. 인용 뒤의 세미콜론은 노트의 인용 구분자이다. |
| 05 | src/mod_global.F:134 — B 결론 칸이 붙은 후보 | 표 칸 경계 오판이다. `24a88c3:src/mod_global.F:134–135`에서 MinDepth는 0.001이다. MinDepthFrc는 0.5이다. 현재 입력 누락값 0.1은 `src/io.F:2933–2935`와 일치한다. |
| 06 | 수정 전 노트:55 — `M = H\{u_\alpha + u_2\}` | 수정 전 노트 인용이다. HEAD diff에서 복원한 55행과 일치한다. 현재 식이라고 새로 주장하는 문장이 아니다. |
| 07 | src/fluxes.F:462 — `; ` | 구분자 오판이다. `7b93138:src/fluxes.F:462–463`의 PL 식을 대조했다. Gamma1·MASK9·U4xL 항과 부호가 일치한다. |
| 08 | src/main.F:214 — `; ` | 구분자 오판이다. `b9c035d:src/main.F:214`는 `DO ISTAGE=1,3`이다. 뒤의 세미콜론은 노트의 인용 구분자이다. |
| 09 | src/sponge.F:248 — B 결론 칸이 붙은 후보 | 표 칸 경계 오판이다. `7b93138:src/sponge.F:248–250`에서 `ri` 계산과 TANH의 `/10.0`를 대조했다. 식 (89)과 코드식이 다르다는 보고서 결론은 유지한다. |
| 10 | src/wavemaker.F:1061 — `; ` | 구분자 오판이다. `7b93138:src/wavemaker.F:1061–1063`의 10000회 반복과 주파수 분할을 대조했다. |
| 11 | 수정 전 노트:152 — `INT UVZ` | 수정 전 노트 인용은 HEAD 152행과 일치한다. 현재 키는 `src/io.F:712`의 INI_UVZ이다. FN1-906의 코드 칸에 섞인 옛 표기는 제거했다. |
| 12 | 수정 전 노트:174 — `WAVE DATA` | 수정 전 노트 인용은 HEAD 174행과 일치한다. FV1-520은 문서 WAVE_DATA와 현재 WK_DATA2D를 구분한다. 해당 결론은 보고서와 같다. |
| 13 | 수정 전 노트:205 — `Cd fixed` | 수정 전 노트 인용은 HEAD 205행과 일치한다. 현재 입력 키는 Cd이다. 내부 변수는 Cd_fixed이다. FN1-916의 코드 칸에 섞인 공백 키는 제거했다. |
| 14 | 수정 전 노트:210 — `Time Scheme` | 수정 전 노트 인용은 HEAD 210행과 일치한다. 실제 Time_Scheme 읽기와 3단계 RK 실행은 구분되어 있다. FN1-917의 코드 칸에 섞인 공백 키는 제거했다. |
| 15 | 수정 전 노트:224 — `STATION FILE` | 수정 전 노트 인용은 HEAD 224행과 일치한다. 실제 키는 `src/io.F:3361`의 STATIONS_FILE이다. FV1-392·532에는 구면 좌표 근거를 보완했다. |
| 16 | 수정 전 노트:129 — 대소문자·verbatim 문장 | 수정 전 노트 인용은 HEAD 129행과 일치한다. FX1-901은 밑줄을 잃은 표를 verbatim으로 부를 수 없다고 판정한다. 보고서 최종 결론과 같다. |
| 17 | 수정 전 노트:238 — `핵심 input.txt verbatim 발췌:` | 수정 전 노트 인용은 HEAD 238행과 일치한다. FX1-902·FV2-400은 밑줄과 한 줄 한 대입을 복원하도록 판정한다. 보고서 최종 결론과 같다. |
| 18 | 수정 전 노트:218 — C1·C2 기본값 0.65 / 0.15 | 수정 전 노트 인용은 HEAD 218행과 일치한다. FX1-903·FV1-531·FV2-402는 예제의 0.15와 현재 Cbrk2 누락값 0.35를 구분한다. 3.0 p.26·41과 해당 코드 입력 분기를 대조했다. |
| 19 | 수정 전 노트:201 — 점성 쇄파·shock-capturing 기본값 | 수정 전 노트 인용은 HEAD 201행과 일치한다. `6233886:src/io.F:2597`의 TRUE 변경과 2019-06-16 날짜는 git 판정과 같다. FN1-908의 코드 칸에 섞인 문서 키는 제거했다. |
| 20 | 수정 전 노트:202 — H/d 비 약 0.80 | 수정 전 노트 인용은 HEAD 202행과 일치한다. FX1-905·FV1-527·FN1-909의 현재 조건은 `src/masks.F:177–185`와 같다. 분자는 ABS(Eta)이다. 해당 조건은 VISCOSITY_BREAKING이 거짓일 때 적용된다. |
| 21 | 수정 전 노트:224 — `NumberStations` | 수정 전 노트 인용은 HEAD 224행과 일치한다. FX1-907의 `NumberStations>0` 조건은 현재 파일 읽기 분기와 같다. 구면 좌표 조건은 FV1-532에 직접 인용을 보완했다. |
| 22 | 수정 전 노트:210 — `Runge Kutta` | 수정 전 노트 인용은 HEAD 210행과 일치한다. 현재 `src/main.F:380`은 `DO ISTAGE=1,3`이다. FN1-917의 코드 칸에 섞인 옛 표기는 제거했다. |
| 23 | src/io.F:762 — `; ` | 구분자 오판이다. `739a08d:src/io.F:762`는 Time_Scheme 문자열 읽기이다. 뒤의 세미콜론은 노트의 인용 구분자이다. |
| 24 | 수정 전 노트:215 — lab 0.001 / field 0.01 | 수정 전 노트 인용은 HEAD 215행과 일치한다. 3.0 p.41의 권고값과 현재 입력 누락값을 FX1-911에서 구분한다. 병합식은 `src/io.F:2948–2949`와 같다. |
| 25 | 수정 전 노트:236 — §5.1, p.45~46 | 수정 전 노트 인용은 HEAD 236행과 일치한다. FX1-919의 정정 결론은 §5.1이 p.47까지 이어진다는 것이다. 마지막 Grid B 입력 p.79와 그림 25 p.80도 이미지로 대조했다. |
| 26 | FUNWAVE-TVD/src/io.F:2577 — `DISPERSION,Gamma1,Gamma2,Beta_ref` | 연속 원문이 아닌 입력 이름 목록이다. 각각 `src/io.F:2577,2591,2606,2620`에 있다. 노트의 인용 범위 2577–2635 안에 포함된다. |
| 27 | doc/funwave_tvd_3.0.tex:208 — `; ` | 구분자 오판이다. `24a88c3:doc/funwave_tvd_3.0.tex:208`의 병렬 주기 경계 설명을 대조했다. 뒤의 세미콜론은 노트의 인용 구분자이다. |
| 28 | FUNWAVE-TVD/src/io.F:2689 — 두 입력 이름, 첫 번째 | 연속 원문이 아닌 입력 이름 목록이다. FV1-115의 VISCOSITY_BREAKING은 2689행에 있다. SWE_ETA_DEP는 2713행에 있다. 둘 다 인용 범위 2689–2715에 포함된다. |
| 29 | FUNWAVE-TVD/src/nesting.F:98 — `DO` | 실제 불일치이다. 98–114행에는 여는 DO가 없다. 노트 445행 FV1-432의 인용을 `IF(N_COUPLING_EAST.GT.0)THEN`으로 정정했다. |
| 30 | doc/funwave_tvd_3.0.tex:208 — 표 칸 경계 | 표 칸 경계 오판이다. `24a88c3:doc/funwave_tvd_3.0.tex:208`과 3.0 p.11의 설명이 일치한다. 표 구분자는 TeX 원문 인용이 아니다. |
| 31 | FUNWAVE-TVD/src/io.F:2689 — 두 입력 이름, 두 번째 | FV1-504의 입력 이름 목록이다. `src/io.F:2689,2713`과 일치한다. TRUE 기본값과 ELSE에서만 적용되는 비율 조건을 각각 io.F·masks.F에서 대조했다. |
| 32 | FUNWAVE-TVD/src/io.F:2689 — 두 입력 이름, 세 번째 | FV1-527의 입력 이름 목록이다. `src/io.F:2689,2713`과 일치한다. `src/masks.F:177–185`의 조건·분자·분모도 일치한다. |
| 33 | 수정 전 노트:232 — `station은` | 수정 전 노트 인용은 HEAD 232행과 일치한다. FI1-316·FV2-401의 현재 관측점 번호 네 자리 판정은 출력 원문과 같다. 장 출력 번호 다섯 자리와 구분한다. |

## A 분류 HASH·날짜 대조

아래 행 수는 A 분류 노트 행을 기준으로 센 값이다.
같은 커밋을 인용한 반복 행도 각각 셌다.

| HASH | 날짜 | 노트 행 수 | git 판정 보고서의 근거 줄 |
|---|---|---:|---|
| `395bcc8` | 2017-06-14 | 1 | `FUNWAVE-git-verify-AD1.md:83` |
| `9bae2f6` | 2019-07-25 | 5 | `FUNWAVE-git-verify-AD1.md:85`; `FUNWAVE-git-verify-AD1.md:86`; `FUNWAVE-git-verify-AD1.md:87`; `FUNWAVE-git-verify-AD1.md:88`; `FUNWAVE-git-verify-AD2.md:96` |
| `6233886` | 2019-06-16 | 7 | `FUNWAVE-git-verify-AD1.md:90`; `FUNWAVE-git-verify-AD1.md:91`; `FUNWAVE-git-verify-AD2.md:83`; `FUNWAVE-git-verify-AD2.md:85`; `FUNWAVE-git-verify-AD2.md:92`; `FUNWAVE-git-verify-AD2.md:100`; `FUNWAVE-git-verify-AD3.md:129` |
| `2fcff96` | 2017-06-07 | 7 | `FUNWAVE-git-verify-AD2.md:74`; `FUNWAVE-git-verify-AD2.md:81`; `FUNWAVE-git-verify-AD2.md:82`; `FUNWAVE-git-verify-AD2.md:86`; `FUNWAVE-git-verify-AD2.md:90`; `FUNWAVE-git-verify-AD2.md:91`; `FUNWAVE-git-verify-AD3.md:130` |
| `cab9425` | 2016-03-02 | 1 | `FUNWAVE-git-verify-AD1.md:39` |
| `ca113a8` | 2019-07-19 | 3 | `FUNWAVE-git-verify-AD2.md:78`; `FUNWAVE-git-verify-AD2.md:80`; `FUNWAVE-git-verify-AD2.md:88` |
| `dcc84ba` | 2017-07-13 | 3 | `FUNWAVE-git-verify-AD2.md:79`; `FUNWAVE-git-verify-AD2.md:87`; `FUNWAVE-git-verify-AD3.md:127` |
| `43d92c9` | 2017-05-10 | 3 | `FUNWAVE-git-verify-AD2.md:84`; `FUNWAVE-git-verify-AD2.md:89`; `FUNWAVE-git-verify-AD3.md:128` |
| `562cb98` | 2018-11-27 | 2 | `FUNWAVE-git-verify-AD2.md:93`; `FUNWAVE-git-verify-AD1.md:92`; `FUNWAVE-git-verify-AD2.md:101` |

## 담당 줄별 대조 기록

노트 행 번호는 이 작업 종료 시의 번호이다.
추가 줄 순번은 작업 시작 시 HEAD diff에서 확정한 번호이다.
각 행의 문서 인용·코드 인용·분류·결론을 모두 대조했다.
식·숫자·조건·플래그는 해당 원문과 대조했다.
상대 링크와 금지 표기는 담당 줄 전체를 검사했다.

최종 보고서는 [inputs](../compare/funwave-inputs-vs-code.md), [examples](../compare/funwave-examples-vs-code.md), [v21-manual](../compare/funwave-v21-manual-vs-code.md), [v21-examples](../compare/funwave-v21-examples-vs-code.md), [aux-docs-build](../compare/funwave-aux-docs-build-vs-code.md), [callflow](FUNWAVE-callflow.md)이다.

| 추가 줄 순번 | 노트 행 | 행 ID | 최종 분류 | 보고서 최종 결론 줄 | 결과 |
|---:|---:|---|---|---|---|
| 219 | 368 | `inputs:FI1-315` | B 문서 오기 | `funwave-inputs-vs-code.md:524` | 유지 |
| 220 | 369 | `inputs:FI1-316` | B 문서 오기 | `funwave-inputs-vs-code.md:525` | 유지 |
| 221 | 370 | `inputs:FI1-317` | A 판 차이 | `funwave-inputs-vs-code.md:474` | 유지 |
| 222 | 371 | `examples:FX1-004` | B 문서 오기 | `funwave-examples-vs-code.md:833` | 유지 |
| 223 | 372 | `examples:FX1-006` | F 표현 차이 | `funwave-examples-vs-code.md:835` | 정정 |
| 224 | 373 | `examples:FX1-043` | A 판 차이 | `funwave-examples-vs-code.md:838` | 정정 |
| 225 | 374 | `examples:FX1-044` | A 판 차이 | `funwave-examples-vs-code.md:839` | 정정 |
| 226 | 375 | `examples:FX1-303` | B 문서 오기 | `funwave-examples-vs-code.md:852` | 유지 |
| 227 | 376 | `examples:FX1-339` | A 판 차이 | `funwave-examples-vs-code.md:856` | 정정 |
| 228 | 377 | `examples:FX1-404` | B 문서 오기 | `funwave-examples-vs-code.md:859` | 유지 |
| 229 | 378 | `examples:FX1-420` | B 문서 오기 | `funwave-examples-vs-code.md:862` | 유지 |
| 230 | 379 | `examples:FX1-437` | A 판 차이 | `funwave-examples-vs-code.md:863` | 정정 |
| 231 | 380 | `examples:FX1-439` | B 문서 오기 | `funwave-examples-vs-code.md:864` | 유지 |
| 232 | 381 | `examples:FX1-603` | B 문서 오기 | `funwave-examples-vs-code.md:874` | 유지 |
| 233 | 382 | `examples:FX1-702` | B 문서 오기 | `funwave-examples-vs-code.md:880` | 유지 |
| 234 | 383 | `examples:FX1-738` | B 문서 오기 | `funwave-examples-vs-code.md:888` | 유지 |
| 235 | 384 | `examples:FX1-740` | C 문서 누락 | `funwave-examples-vs-code.md:889` | 유지 |
| 236 | 385 | `examples:FX1-778` | B 문서 오기 | `funwave-examples-vs-code.md:891` | 유지 |
| 237 | 386 | `examples:FX1-780` | C 문서 누락 | `funwave-examples-vs-code.md:892` | 유지 |
| 238 | 387 | `examples:FX1-801` | C 문서 누락 | `funwave-examples-vs-code.md:893` | 유지 |
| 239 | 388 | `examples:FX1-802` | C 문서 누락 | `funwave-examples-vs-code.md:894` | 유지 |
| 240 | 389 | `examples:FX1-803` | A 판 차이 | `funwave-examples-vs-code.md:895` | 유지 |
| 241 | 390 | `examples:FX1-805` | C 문서 누락 | `funwave-examples-vs-code.md:897` | 유지 |
| 242 | 391 | `examples:FX1-819` | C 문서 누락 | `funwave-examples-vs-code.md:911` | 유지 |
| 243 | 392 | `examples:FX1-820` | C 문서 누락 | `funwave-examples-vs-code.md:912` | 유지 |
| 244 | 393 | `examples:FX1-821` | C 문서 누락 | `funwave-examples-vs-code.md:913` | 유지 |
| 245 | 394 | `examples:FX1-901` | B 문서 오기 | `funwave-examples-vs-code.md:918` | 유지 |
| 246 | 395 | `examples:FX1-902` | B 문서 오기 | `funwave-examples-vs-code.md:919` | 유지 |
| 247 | 396 | `examples:FX1-903` | B 문서 오기 | `funwave-examples-vs-code.md:920` | 유지 |
| 248 | 397 | `examples:FX1-904` | A 판 차이 | `funwave-examples-vs-code.md:921` | 유지 |
| 249 | 398 | `examples:FX1-905` | B 문서 오기 | `funwave-examples-vs-code.md:922` | 유지 |
| 250 | 399 | `examples:FX1-906` | B 문서 오기 | `funwave-examples-vs-code.md:923` | 유지 |
| 251 | 400 | `examples:FX1-907` | C 문서 누락 | `funwave-examples-vs-code.md:924` | 유지 |
| 252 | 401 | `examples:FX1-908` | B 문서 오기 | `funwave-examples-vs-code.md:925` | 유지 |
| 253 | 402 | `examples:FX1-910` | B 문서 오기 | `funwave-examples-vs-code.md:927` | 유지 |
| 254 | 403 | `examples:FX1-911` | C 문서 누락 | `funwave-examples-vs-code.md:928` | 유지 |
| 255 | 404 | `examples:FX1-919` | C 문서 누락 | `funwave-examples-vs-code.md:936` | 유지 |
| 256 | 405 | `v21-manual:FV1-011` | A 판 차이 | `funwave-v21-manual-vs-code.md:1478` | 유지 |
| 257 | 406 | `v21-manual:FV1-042` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1510` | 유지 |
| 258 | 407 | `v21-manual:FV1-043` | E 코드 결함 후보 | `funwave-v21-manual-vs-code.md:1511` | 유지 |
| 259 | 408 | `v21-manual:FV1-052` | F 표기 차이 | `funwave-v21-manual-vs-code.md:1515` | 유지 |
| 260 | 409 | `v21-manual:FV1-074` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1518` | 유지 |
| 261 | 410 | `v21-manual:FV1-075` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1519` | 유지 |
| 262 | 411 | `v21-manual:FV1-101` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1520` | 유지 |
| 263 | 412 | `v21-manual:FV1-112` | A 판 차이 | `funwave-v21-manual-vs-code.md:1524` | 유지 |
| 264 | 413 | `v21-manual:FV1-115` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1526` | 유지 |
| 265 | 414 | `v21-manual:FV1-133` | D 문서에만 있음 | `funwave-v21-manual-vs-code.md:1887` | 정정 |
| 266 | 415 | `v21-manual:FV1-168` | D 문서에만 있음 | `funwave-v21-manual-vs-code.md:1893` | 정정 |
| 267 | 416 | `v21-manual:FV1-198` | D 문서에만 있음 | `funwave-v21-manual-vs-code.md:1905` | 유지 |
| 268 | 417 | `v21-manual:FV1-271` | A 판 차이 | `funwave-v21-manual-vs-code.md:1482` | 유지 |
| 269 | 418 | `v21-manual:FV1-274` | A 판 차이 | `funwave-v21-manual-vs-code.md:1483` | 유지 |
| 270 | 419 | `v21-manual:FV1-276` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1564` | 유지 |
| 271 | 420 | `v21-manual:FV1-282` | A 판 차이 | `funwave-v21-manual-vs-code.md:1484` | 유지 |
| 272 | 421 | `v21-manual:FV1-283` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1566` | 유지 |
| 273 | 422 | `v21-manual:FV1-301` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1567` | 정정 |
| 274 | 423 | `v21-manual:FV1-302` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1568` | 정정 |
| 275 | 424 | `v21-manual:FV1-321` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1569` | 유지 |
| 276 | 425 | `v21-manual:FV1-324` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1570` | 유지 |
| 277 | 426 | `v21-manual:FV1-328` | A 판 차이 | `funwave-v21-manual-vs-code.md:1485` | 유지 |
| 278 | 427 | `v21-manual:FV1-329` | A 판 차이 | `funwave-v21-manual-vs-code.md:1486` | 유지 |
| 279 | 428 | `v21-manual:FV1-337` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1649` | 유지 |
| 280 | 429 | `v21-manual:FV1-338` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1650` | 유지 |
| 281 | 430 | `v21-manual:FV1-340` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1574` | 유지 |
| 282 | 431 | `v21-manual:FV1-348` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1576` | 유지 |
| 283 | 432 | `v21-manual:FV1-375` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1578` | 유지 |
| 284 | 433 | `v21-manual:FV1-380` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1579` | 유지 |
| 285 | 434 | `v21-manual:FV1-381` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1580` | 유지 |
| 286 | 435 | `v21-manual:FV1-392` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1585` | 보완 |
| 287 | 436 | `v21-manual:FV1-401` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1586` | 유지 |
| 288 | 437 | `v21-manual:FV1-402` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1587` | 유지 |
| 289 | 438 | `v21-manual:FV1-408` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1588` | 유지 |
| 290 | 439 | `v21-manual:FV1-409` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1589` | 유지 |
| 291 | 440 | `v21-manual:FV1-410` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1590` | 유지 |
| 292 | 441 | `v21-manual:FV1-411` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1591` | 정정 |
| 293 | 442 | `v21-manual:FV1-412` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1592` | 유지 |
| 294 | 443 | `v21-manual:FV1-417` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1593` | 유지 |
| 295 | 444 | `v21-manual:FV1-425` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1594` | 유지 |
| 296 | 445 | `v21-manual:FV1-432` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1595` | 정정 |
| 297 | 446 | `v21-manual:FV1-435` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1596` | 유지 |
| 298 | 447 | `v21-manual:FV1-444` | E 코드 결함 후보 | `funwave-v21-manual-vs-code.md:1915` | 정정 |
| 299 | 448 | `v21-manual:FV1-445` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1597` | 유지 |
| 300 | 449 | `v21-manual:FV1-453` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1654` | 보완 |
| 301 | 450 | `v21-manual:FV1-457` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1658` | 유지 |
| 302 | 451 | `v21-manual:FV1-460` | A 판 차이 | `funwave-v21-manual-vs-code.md:1487` | 유지 |
| 303 | 452 | `v21-manual:FV1-461` | A 판 차이 | `funwave-v21-manual-vs-code.md:1488` | 유지 |
| 304 | 453 | `v21-manual:FV1-462` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1599` | 유지 |
| 305 | 454 | `v21-manual:FV1-463` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1661` | 유지 |
| 306 | 455 | `v21-manual:FV1-464` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1600` | 유지 |
| 307 | 456 | `v21-manual:FV1-470` | E 코드 결함 후보 | `funwave-v21-manual-vs-code.md:1916` | 정정 |
| 308 | 457 | `v21-manual:FV1-474` | E 코드 결함 후보 | `funwave-v21-manual-vs-code.md:1920` | 정정 |
| 309 | 458 | `v21-manual:FV1-500` | F 표기 차이 | `funwave-v21-manual-vs-code.md:1601` | 유지 |
| 310 | 459 | `v21-manual:FV1-501` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1602` | 유지 |
| 311 | 460 | `v21-manual:FV1-502` | F 표기 차이 | `funwave-v21-manual-vs-code.md:1603` | 유지 |
| 312 | 461 | `v21-manual:FV1-503` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1605` | 유지 |
| 313 | 462 | `v21-manual:FV1-504` | A 판 차이 | `funwave-v21-manual-vs-code.md:1489` | 유지 |
| 314 | 463 | `v21-manual:FV1-505` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1606` | 유지 |
| 315 | 464 | `v21-manual:FV1-506` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1607` | 보완 |
| 316 | 465 | `v21-manual:FV1-507` | A 판 차이 | `funwave-v21-manual-vs-code.md:1490` | 유지 |
| 317 | 466 | `v21-manual:FV1-508` | A 판 차이 | `funwave-v21-manual-vs-code.md:1491` | 유지 |
| 318 | 467 | `v21-manual:FV1-509` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1608` | 유지 |
| 319 | 468 | `v21-manual:FV1-510` | E 코드 결함 후보 | `funwave-v21-manual-vs-code.md:1921` | 정정 |
| 320 | 469 | `v21-manual:FV1-511` | A 판 차이 | `funwave-v21-manual-vs-code.md:1492` | 유지 |
| 321 | 470 | `v21-manual:FV1-512` | A 판 차이 | `funwave-v21-manual-vs-code.md:1493` | 유지 |
| 322 | 471 | `v21-manual:FV1-513` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1609` | 유지 |
| 323 | 472 | `v21-manual:FV1-514` | A 판 차이 | `funwave-v21-manual-vs-code.md:1494` | 유지 |
| 324 | 473 | `v21-manual:FV1-515` | A 판 차이 | `funwave-v21-manual-vs-code.md:1495` | 유지 |
| 325 | 474 | `v21-manual:FV1-516` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1610` | 유지 |
| 326 | 475 | `v21-manual:FV1-517` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1865` | 유지 |
| 327 | 476 | `v21-manual:FV1-518` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1866` | 유지 |
| 328 | 477 | `v21-manual:FV1-519` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1611` | 보완 |
| 329 | 478 | `v21-manual:FV1-520` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1612` | 유지 |
| 330 | 479 | `v21-manual:FV1-521` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1613` | 유지 |
| 331 | 480 | `v21-manual:FV1-522` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1614` | 유지 |
| 332 | 481 | `v21-manual:FV1-523` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1615` | 유지 |
| 333 | 482 | `v21-manual:FV1-524` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1616` | 유지 |
| 334 | 483 | `v21-manual:FV1-525` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1617` | 유지 |
| 335 | 484 | `v21-manual:FV1-526` | A 판 차이 | `funwave-v21-manual-vs-code.md:1496` | 유지 |
| 336 | 485 | `v21-manual:FV1-527` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1618` | 유지 |
| 337 | 486 | `v21-manual:FV1-528` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1619` | 유지 |
| 338 | 487 | `v21-manual:FV1-529` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1620` | 유지 |
| 339 | 488 | `v21-manual:FV1-530` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1621` | 유지 |
| 340 | 489 | `v21-manual:FV1-531` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1622` | 유지 |
| 341 | 490 | `v21-manual:FV1-532` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1623` | 보완 |
| 342 | 491 | `v21-manual:FV1-533` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1624` | 유지 |
| 343 | 492 | `v21-manual:FV1-534` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1867` | 유지 |
| 344 | 493 | `v21-manual:FV1-535` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1625` | 유지 |
| 345 | 494 | `v21-manual:FV1-536` | A 판 차이 | `funwave-v21-manual-vs-code.md:1497` | 유지 |
| 346 | 495 | `v21-manual:FV1-537` | B 문서 오기 | `funwave-v21-manual-vs-code.md:1626` | 유지 |
| 347 | 496 | `v21-manual:FV1-601` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1669` | 유지 |
| 348 | 497 | `v21-manual:FV1-602` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1670` | 유지 |
| 349 | 498 | `v21-manual:FV1-604` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1672` | 유지 |
| 350 | 499 | `v21-manual:FV1-605` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1673` | 유지 |
| 351 | 500 | `v21-manual:FV1-606` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1674` | 유지 |
| 352 | 501 | `v21-manual:FV1-633` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1702` | 유지 |
| 353 | 502 | `v21-manual:FV1-634` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1703` | 유지 |
| 354 | 503 | `v21-manual:FV1-644` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1713` | 유지 |
| 355 | 504 | `v21-manual:FV1-645` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1714` | 유지 |
| 356 | 505 | `v21-manual:FV1-646` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1715` | 유지 |
| 357 | 506 | `v21-manual:FV1-647` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1716` | 유지 |
| 358 | 507 | `v21-manual:FV1-648` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1717` | 유지 |
| 359 | 508 | `v21-manual:FV1-649` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1718` | 유지 |
| 360 | 509 | `v21-manual:FV1-650` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1719` | 유지 |
| 361 | 510 | `v21-manual:FV1-651` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1720` | 유지 |
| 362 | 511 | `v21-manual:FV1-652` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1721` | 유지 |
| 363 | 512 | `v21-manual:FV1-653` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1722` | 유지 |
| 364 | 513 | `v21-manual:FV1-654` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1723` | 유지 |
| 365 | 514 | `v21-manual:FV1-655` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1724` | 유지 |
| 366 | 515 | `v21-manual:FV1-656` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1725` | 유지 |
| 367 | 516 | `v21-manual:FV1-657` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1726` | 유지 |
| 368 | 517 | `v21-manual:FV1-658` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1727` | 유지 |
| 369 | 518 | `v21-manual:FV1-659` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1728` | 유지 |
| 370 | 519 | `v21-manual:FV1-660` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1729` | 유지 |
| 371 | 520 | `v21-manual:FV1-661` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1730` | 유지 |
| 372 | 521 | `v21-manual:FV1-662` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1731` | 유지 |
| 373 | 522 | `v21-manual:FV1-663` | C 문서 누락 | `funwave-v21-manual-vs-code.md:1732` | 유지 |
| 374 | 523 | `v21-examples:FV2-059` | B 문서 오기 | `funwave-v21-examples-vs-code.md:707` | 정정 |
| 375 | 524 | `v21-examples:FV2-062` | C 문서 누락 | `funwave-v21-examples-vs-code.md:708` | 정정 |
| 376 | 525 | `v21-examples:FV2-267` | A 판 차이 | `funwave-v21-examples-vs-code.md:716` | 유지 |
| 377 | 526 | `v21-examples:FV2-310` | C 문서 누락 | `funwave-v21-examples-vs-code.md:729` | 정정 |
| 378 | 527 | `v21-examples:FV2-400` | B 문서 오기 | `funwave-v21-examples-vs-code.md:741` | 유지 |
| 379 | 528 | `v21-examples:FV2-401` | B 문서 오기 | `funwave-v21-examples-vs-code.md:742` | 유지 |
| 380 | 529 | `v21-examples:FV2-402` | B 문서 오기 | `funwave-v21-examples-vs-code.md:743` | 유지 |
| 381 | 530 | `v21-examples:FV2-411` | A 판 차이 | `funwave-v21-examples-vs-code.md:750` | 유지 |
| 382 | 531 | `v21-examples:FV2-408` | B 문서 오기 | `funwave-v21-examples-vs-code.md:861` | 유지 |
| 383 | 532 | `aux-docs-build:FN1-102` | D 문서에만 있음 | `funwave-aux-docs-build-vs-code.md:725` | 유지 |
| 384 | 533 | `aux-docs-build:FN1-103` | D 문서에만 있음 | `funwave-aux-docs-build-vs-code.md:726` | 유지 |
| 385 | 534 | `aux-docs-build:FN1-106` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:727` | 유지 |
| 386 | 535 | `aux-docs-build:FN1-107` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:728` | 유지 |
| 387 | 536 | `aux-docs-build:FN1-109` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:729` | 유지 |
| 388 | 537 | `aux-docs-build:FN1-114` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:730` | 유지 |
| 389 | 538 | `aux-docs-build:FN1-115` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:731` | 유지 |
| 390 | 539 | `aux-docs-build:FN1-116` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:732` | 유지 |
| 391 | 540 | `aux-docs-build:FN1-117` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:733` | 유지 |
| 392 | 541 | `aux-docs-build:FN1-122` | C 문서 누락 | `funwave-aux-docs-build-vs-code.md:737` | 유지 |
| 393 | 542 | `aux-docs-build:FN1-128` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:738` | 유지 |
| 394 | 543 | `aux-docs-build:FN1-129` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:739` | 유지 |
| 395 | 544 | `aux-docs-build:FN1-138` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:743` | 유지 |
| 396 | 545 | `aux-docs-build:FN1-148` | D 문서에만 있음 | `funwave-aux-docs-build-vs-code.md:746` | 유지 |
| 397 | 546 | `aux-docs-build:FN1-158` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:750` | 유지 |
| 398 | 547 | `aux-docs-build:FN1-173` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:751` | 유지 |
| 399 | 548 | `aux-docs-build:FN1-174` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:752` | 유지 |
| 400 | 549 | `aux-docs-build:FN1-175` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:753` | 유지 |
| 401 | 550 | `aux-docs-build:FN1-176` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:754` | 유지 |
| 402 | 551 | `aux-docs-build:FN1-209` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:760` | 유지 |
| 403 | 552 | `aux-docs-build:FN1-218` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:762` | 유지 |
| 404 | 553 | `aux-docs-build:FN1-242` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:766` | 유지 |
| 405 | 554 | `aux-docs-build:FN1-247` | C 문서 누락 | `funwave-aux-docs-build-vs-code.md:767` | 유지 |
| 406 | 555 | `aux-docs-build:FN1-251` | C 문서 누락 | `funwave-aux-docs-build-vs-code.md:768` | 유지 |
| 407 | 556 | `aux-docs-build:FN1-263` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:771` | 유지 |
| 408 | 557 | `aux-docs-build:FN1-264` | C 문서 누락 | `funwave-aux-docs-build-vs-code.md:772` | 유지 |
| 409 | 558 | `aux-docs-build:FN1-267` | C 문서 누락 | `funwave-aux-docs-build-vs-code.md:773` | 유지 |
| 410 | 559 | `aux-docs-build:FN1-269` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:774` | 유지 |
| 411 | 560 | `aux-docs-build:FN1-707` | C 문서 누락 | `funwave-aux-docs-build-vs-code.md:907` | 유지 |
| 412 | 561 | `aux-docs-build:FN1-752` | C 문서 누락 | `funwave-aux-docs-build-vs-code.md:924` | 유지 |
| 413 | 562 | `aux-docs-build:FN1-755` | C 문서 누락 | `funwave-aux-docs-build-vs-code.md:927` | 유지 |
| 414 | 563 | `aux-docs-build:FN1-757` | C 문서 누락 | `funwave-aux-docs-build-vs-code.md:929` | 유지 |
| 415 | 564 | `aux-docs-build:FN1-904` | A 판 차이 | `funwave-aux-docs-build-vs-code.md:956` | 정정 |
| 416 | 565 | `aux-docs-build:FN1-905` | C 문서 누락 | `funwave-aux-docs-build-vs-code.md:957` | 유지 |
| 417 | 566 | `aux-docs-build:FN1-906` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:958` | 정정 |
| 418 | 567 | `aux-docs-build:FN1-907` | A 판 차이 | `funwave-aux-docs-build-vs-code.md:959` | 정정 |
| 419 | 568 | `aux-docs-build:FN1-908` | A 판 차이 | `funwave-aux-docs-build-vs-code.md:960` | 정정 |
| 420 | 569 | `aux-docs-build:FN1-909` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:961` | 정정 |
| 421 | 570 | `aux-docs-build:FN1-910` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:962` | 유지 |
| 422 | 571 | `aux-docs-build:FN1-911` | A 판 차이 | `funwave-aux-docs-build-vs-code.md:963` | 정정 |
| 423 | 572 | `aux-docs-build:FN1-912` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:964` | 정정 |
| 424 | 573 | `aux-docs-build:FN1-913` | F 표기 차이 | `funwave-aux-docs-build-vs-code.md:965` | 유지 |
| 425 | 574 | `aux-docs-build:FN1-914` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:966` | 정정 |
| 426 | 575 | `aux-docs-build:FN1-915` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:967` | 정정 |
| 427 | 576 | `aux-docs-build:FN1-916` | B 문서 오기 | `funwave-aux-docs-build-vs-code.md:968` | 정정 |
| 428 | 577 | `aux-docs-build:FN1-917` | D 문서에만 있음 | `funwave-aux-docs-build-vs-code.md:969` | 정정 |
| 429 | 578 | `callflow:RF-001` | A 판 차이 | `FUNWAVE-callflow.md:3059` | 유지 |
| 430 | 579 | `callflow:RF-003` | D 문서에만 있음 | `FUNWAVE-callflow.md:3061` | 정정 |
| 431 | 580 | `callflow:RF-004` | D 문서에만 있음 | `FUNWAVE-callflow.md:3062` | 유지 |
| 432 | 581 | `callflow:RF-006` | B 문서 오기 | `FUNWAVE-callflow.md:3064` | 유지 |
| 433 | 582 | `callflow:RF-010` | B 문서 오기 | `FUNWAVE-callflow.md:3068` | 정정 |
| 434 | 583 | `callflow:RF-019` | D 문서에만 있음 | `FUNWAVE-callflow.md:3077` | 정정 |
| 435 | 584 | `callflow:RF-025` | B 문서 오기 | `FUNWAVE-callflow.md:3083` | 정정 |

## 완료 확인

- 담당 추가 줄 순번 219–435가 행별 대조 기록에 각각 한 번씩 있다.
- 정정·보완 목록 38건은 수정 후 노트의 해당 행과 일치한다.
- 나머지 담당 179행은 작업 시작 시 내용과 일치한다.
- 기계 확인 후보 33건의 판정을 모두 기록했다.
- 정정·보완 표식은 해당 결론 문장 칸 끝에 있다.
- 노트의 상대 링크와 검증 기록의 상대 링크는 모두 실제 파일을 가리킨다.
- 읽기 전용 `git diff --check`는 오류 없이 끝났다.
- 미해결 항목은 0개이다.
