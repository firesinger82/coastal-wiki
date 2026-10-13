# SWAN 대상 노트 6개 추가·수정 줄 전수 대조

검증일: 2026-10-13.

대상은 사용자가 지정한 노트 6개이다. 각 노트의 검증 시작 시점에 `git diff -U0 HEAD -- <노트>`로 얻은 `+` 줄을 센다. `+++` 파일 표지는 제외한다. 빈 줄과 frontmatter 줄은 포함한다. 정정 수와 보완 수는 수정한 대상 줄 수이다. 줄 번호는 각 노트의 검증 완료 시점을 기준으로 적는다.

원문은 저장소에 있는 SWAN 코드, 과거 커밋의 코드, 웹 문서 HTML, PDF이다. 결론 분류와 결론 문장은 사용자가 지정한 보고서의 최종 태그와 대조한다. 노트를 마칠 때마다 대조 범위와 판정을 아래에 추가한다.

## 노트별 결과

### 1. swan-tech-ch4-5-bc-2d-setup.md — 완료

대조한 `+` 줄은 121줄이다. 정정은 16줄이다. 보완은 0줄이다. 기준 명령은 이 문서 첫머리의 `git diff -U0 HEAD`이다. 대상 줄 범위는 7–8, 22, 37, 47–50, 58–59, 63–65, 70–72, 89, 93–96, 100–104, 106–112, 118–129, 133–134, 141–149, 158, 162–164, 168–228이다.

R3의 대상 행 50개를 최종 결론과 대조했다. BC-005는 git 판정 E와 대조했다. SU-011은 git 판정 D와 대조했다. 결론 분류는 모두 유지한다. `NT-019`의 마름점 문장은 같은 최종 보고서 `SU-037`의 제외값 조건과 코드에 맞춰 좁혔다. 인용된 현재 코드와 과거 커밋의 줄을 열었다. swantech PDF 65–66·90·125–134쪽과 swanuse PDF 20·37·64–65·86–87·141쪽의 관련 문장을 대조했다. PDF 130–131쪽 이미지는 첨자·화살표·괄호를 확인하는 데 사용했다. 웹 HTML의 다중 줄 문장도 대조했다. 상대 링크는 모두 존재한다. 대상 줄에는 절대 경로와 이중 대괄호가 없다. 검증 한계 문장은 제거했다. 이 노트의 대상 줄에는 mermaid 상자가 없다.

노트 경로: `models/SWAN/manual-notes/swan-tech-ch4-5-bc-2d-setup.md`.

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| swan-tech-ch4-5-bc-2d-setup.md:8 | 과거 검증 방법과 `R1–R8 반영` | 이번 121줄의 실제 대조 범위 | 본 작업의 원문 대조와 `SWAN-notes-apply-3.md:17`의 대상 범위 |
| swan-tech-ch4-5-bc-2d-setup.md:22 | 연결 노트 `§6` | 연결 노트 `§5` | `swan-tech-ch2-obstacles-diffraction-setup.md:129`의 `## 5. Wave-induced set-up` |
| swan-tech-ch4-5-bc-2d-setup.md:94 | (5.14)의 바깥 대괄호 | 인쇄 원문의 소괄호 | swantech PDF 130쪽 / 인쇄 122쪽 (5.14) |
| swan-tech-ch4-5-bc-2d-setup.md:112 | (5.22)의 첫 `a`에 벡터 화살표 | 인쇄 원문대로 화살표 없음 | swantech PDF 130쪽 / 인쇄 122쪽 (5.22)의 `a_(1)` |
| swan-tech-ch4-5-bc-2d-setup.md:127 | (5.24) 둘째 줄의 바깥 대괄호 | 인쇄 원문의 소괄호 | swantech PDF 131쪽 / 인쇄 123쪽 (5.24) |
| swan-tech-ch4-5-bc-2d-setup.md:129 | 첫 `x`의 화살표 생략 | 첫 좌표 차의 두 `x`에 화살표 생략 | swantech PDF 131쪽 / 인쇄 123쪽 (5.24) |
| swan-tech-ch4-5-bc-2d-setup.md:141 | 영구 마름점은 주소 1 공유 | 좌표나 수심이 제외값인 점은 주소 1 공유 | `src/swanpre1.ftn:5126`의 `KGRPNT(IX,IY) = 1`; 5134·5141·5166행의 제외값 검사; 5168행의 유효점 주소 대입; R3:SU-037 최종 결론 |
| swan-tech-ch4-5-bc-2d-setup.md:171 | SIP를 `동일 기법`으로 설명 | 작용평형식의 SIP 해법으로 설명 | swantech PDF 90쪽 / 인쇄 82쪽의 SIP; PDF 134쪽 / 인쇄 126쪽의 set-up SOR |
| swan-tech-ch4-5-bc-2d-setup.md:186 | 원논문 계수와 같다는 판정을 하지 않는다는 한계 문장 | 코드의 성장곡선 계수와 4장의 생략을 대조한다는 범위 문장 | `src/swanmain.ftn:9071–9078`; swantech PDF 126쪽 / 인쇄 118쪽; R3:CP-020의 C 분류 유지 |
| swan-tech-ch4-5-bc-2d-setup.md:194 | NT-019의 영구 마름점 문장 | 제외값 조건으로 한정 | `src/swanpre1.ftn:5123–5169`; R3:SU-037 최종 결론 |
| swan-tech-ch4-5-bc-2d-setup.md:204 | `(5.2)를첨자로` | `(5.2)를 첨자로` | swantech PDF 127–128쪽의 (5.2)·(5.4) |
| swan-tech-ch4-5-bc-2d-setup.md:212 | SU-019의 (5.13) 바깥 대괄호 | 인쇄 원문의 소괄호 | swantech PDF 129쪽 / 인쇄 121쪽 (5.13) |
| swan-tech-ch4-5-bc-2d-setup.md:214 | SU-021의 (5.14) 바깥 대괄호 | 인쇄 원문의 소괄호 | swantech PDF 130쪽 / 인쇄 122쪽 (5.14) |
| swan-tech-ch4-5-bc-2d-setup.md:219 | SU-029의 첫 `a`에 벡터 화살표 | 인쇄 원문대로 화살표 없음 | swantech PDF 130쪽 / 인쇄 122쪽 (5.22) |
| swan-tech-ch4-5-bc-2d-setup.md:222 | SU-032의 바깥 대괄호와 첫 `x` 설명 | 소괄호와 첫 좌표 차의 두 `x` 설명 | swantech PDF 131쪽 / 인쇄 123쪽 (5.24) |
| swan-tech-ch4-5-bc-2d-setup.md:228 | 계수 2의 인용 줄 `11864` | `11863` | `src/swancom1.ftn:11863`의 `SETPI = RHS(INDX) - AMAT(INDX,2)*SETUP(INDXLB)`; 11864행은 계수 3 |

기계 확인 후보: 사용자 지정 후보 없음. 직접 인용 대조에서 현재·과거 코드의 인용 내용은 일치했다. 위 표의 수식 전사와 문장·줄 번호만 정정했다. 미해결 항목은 없다.

### 2. swan-tech-ch2-dissipation-detailed.md — 완료

대조한 `+` 줄은 60줄이다. 정정은 5줄이다. 보완은 0줄이다. 대상 줄 범위는 7, 12, 22, 24, 79, 85–87, 99–100, 116, 156–157, 170, 190–191, 193, 204, 206–208, 212–250이다.

R2·R5·R7의 대상 행 24개를 최종 결론과 대조했다. 결론 분류는 모두 유지한다. SS-511의 조건은 원문 코드의 선행 조건으로 한정했다. 나머지 결론 차이는 `해석:` 표지의 생략과 쪽 번호 표기의 풀어쓰기로 확인했다. 코드의 방향 인자·소산 계수·Newton 분모·KTETA·BKD·GEN4 조건을 대조했다. swantech PDF 19·25·29–36·122–123쪽과 swanuse PDF 69–73·138–139쪽을 확인했다. `node16.html`의 (2.44)–(2.75)는 PDF (2.43)–(2.74)에 대응한다. PDF 35쪽 이미지로 지수함수 밖 `/β²` 표기를 확인했다. 상대 링크는 모두 존재한다. 대상 줄에는 절대 경로와 이중 대괄호와 검증 한계 문장이 없다. 이 노트의 대상 줄에는 mermaid 상자가 없다.

노트 경로: `models/SWAN/manual-notes/swan-tech-ch2-dissipation-detailed.md`.

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| swan-tech-ch2-dissipation-detailed.md:7 | 과거 검증 방법과 `R1–R8 반영` | 이번 60줄의 R2·R5·R7 및 원문 대조 범위 | 본 작업의 대조; `SWAN-notes-apply-1.md:18,37` |
| swan-tech-ch2-dissipation-detailed.md:190 | KOMEN 인자 `[cds2] [stpm] [delta] [pwtail]` | `[cds2] [stpm] [powst] [delta] [powk]` | swanuse PDF 71쪽 / 인쇄 63쪽; `src/swanpre1.ftn:2468–2472`의 CDS2·STPM·POWST·DELTA·POWK 읽기. PWTail은 2489행의 JANSSEN 인자다. |
| swan-tech-ch2-dissipation-detailed.md:216 | (2.16) 우변 `S_tot` | 우변 `S_tot/σ` | swantech PDF 19쪽 / 인쇄 11쪽 (2.16) |
| swan-tech-ch2-dissipation-detailed.md:233 | 수식 구분자 없는 `(C_{ds})` | `$C_{ds}$` | swantech PDF 32쪽의 계수 기호; `src/swancom2.ftn:2542–2545` |
| swan-tech-ch2-dissipation-detailed.md:241 | `BB≥1`이면 BJ 포화라는 설명과 TG 코드 인용 | BJ 외부 조건을 명시하고 `BB=QB=1`의 0 대입을 구분 | `src/swancom2.ftn:2110–2124`. 2110–2111행은 `REAL(ABS(BB - DBLE(QB))) .GT. 0.`을 요구한다. 2136–2137행과 `src/swancom1.ftn:6005`는 TG 분기다. SS-511의 C 분류와 인쇄식의 단순 연장을 쓰지 않는다는 최종 결론은 유지한다. |

기계 확인 후보 `website/modifications/modifications.htm:749`: 오판이다. `The numerical`은 749행에서 시작한다. `approximation of the fraction of breakers in the surfzone has changed (more accurate).`는 750–754행에 이어진다. 노트 249행의 인용과 H 분류는 맞다. 노트는 수정하지 않았다.

미해결 항목은 없다.

### 3. swan-output-writers-implementation.md — 완료

대조한 `+` 줄은 41줄이다. 정정은 3줄이다. 보완은 3줄이다. 대상 줄 범위는 6, 11, 34, 39–43, 52, 54, 56, 65, 67, 69, 119, 148, 157, 167, 175, 178, 186, 191–192, 204–221이다.

R6·R8의 대상 행 11개를 최종 결론과 대조했다. O-025는 git 판정 D와 대조했다. O-110·O-112는 git 판정 E와 대조했다. 결론 분류와 결론 문장은 유지한다. 출력 분기·정수화·단위 변환·보간·파일 열기와 스위치 원문을 확인했다. swanuse PDF 98·109·114–117쪽과 인용 웹 문장을 대조했다. 과거 커밋의 인용도 직접 열었다. 상대 링크는 모두 존재한다. 대상 줄에는 절대 경로와 이중 대괄호와 검증 한계 문장이 없다. 이 노트의 대상 줄에는 mermaid 상자가 없다.

노트 경로: `models/SWAN/source-analysis/swan-output-writers-implementation.md`.

| 구분 | 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| 정정 | swan-output-writers-implementation.md:6 | 과거 마이그레이션 설명과 `R1–R8 반영` | 이번 41줄의 실제 대조 범위 | 본 작업의 원문 대조; `SWAN-notes-apply-6.md:31` |
| 보완 | swan-output-writers-implementation.md:54 | 기본 형식의 초기값 인용 없음 | FLT_BLOCK·DEC_BLOCK 초기값 인용 추가 | `src/swmod2.ftn:212`의 `FLT_BLOCK = '(6E12.4)'`; 220행의 `DEC_BLOCK = 4` |
| 보완 | swan-output-writers-implementation.md:157 | FOR의 파일 형식 문자 판별만 인용 | 실제 unit 재사용 분기와 OPEN 인용 추가 | `src/ocpmix.ftn:1842–1847`의 `IUNIT = IUTTM`; 1869–1873행의 OPEN |
| 보완 | swan-output-writers-implementation.md:178 | FOR의 파일 형식 문자 판별만 인용 | 실제 unit 재사용 분기와 OPEN 인용 추가 | `src/ocpmix.ftn:1842–1847,1869–1873` |
| 정정 | swan-output-writers-implementation.md:211 | 데이터 전 WRITE가 9번 있다는 문장 | 시각 분기 중 하나를 선택해 9행을 기록한다는 문장 | `src/swanout2.ftn:514–544`. NREF WRITE 문장은 10개다. 522행과 525행은 양자택일이다. |
| 정정 | swan-output-writers-implementation.md:220 | `2030행의 점 순회` | `2024행의 점 순회` | `src/swanout2.ftn:2024`의 `DO 290 IP = 1, MIP`. 2030행은 YP 대입이다. |

기계 확인 후보 `src/swanout2.ftn:2003`의 `의 SPEC 전체 문자열 비교는`: 오판이다. 노트 215행의 실제 인용은 `b2ae30e:src/swanout2.ftn:2003`이다. 원문은 `IF (RTYPE.EQ.'SPEC') THEN`이다. 한국어 연결 문구는 코드 인용이 아니다.

기계 확인 후보 `src/swanout2.ftn:2007`의 `과`: 오판이다. 노트 215행은 `7ee8981:src/swanout2.ftn:2007`을 가리킨다. 이 줄도 `IF (RTYPE.EQ.'SPEC') THEN`이다. 현재 `43e9bbb`에서는 2011행이다.

기계 확인 후보 `src/swn_outnc.ftn90:614`의 `의 R 전용 판별은`: 오판이다. 노트 216행의 실제 인용은 `b2ae30e:src/swn_outnc.ftn90:614`이다. 원문은 `if (RTYPE(3:3) .eq. 'R') lspcaux%relative = .true.`이다.

기계 확인 후보 `src/swn_outnc.ftn90:608`의 `과`: 오판이다. `7ee8981`과 `43e9bbb`의 608행은 모두 `if (RTYPE(3:3) .eq. 'R') lspcaux%relative = .true.`이다. 한국어 연결 문구를 인용문과 짝지은 검사 오류다.

미해결 항목은 없다.

### 4. swan-whitecapping.md — 완료

대조한 `+` 줄은 36줄이다. 정정은 2줄이다. 보완은 2줄이다. 대상 줄 범위는 6, 11, 16, 46, 97–98, 108, 136–138, 178, 183, 186, 196, 216–237이다.

R2·R5·R7의 대상 행 12개를 최종 결론과 대조했다. 결론 분류와 결론 문장은 유지한다. 백파 선택·계수 초기값·UP/DOWN 정규화·행렬 가산·GEN4 자동 대입을 현재 코드에서 확인했다. CSM의 도입·정규화·제거 문장은 웹 HTML과 대조했다. 인용된 과거 커밋도 직접 열었다. `122b595`와 `43e9bbb`의 src Fortran 원문에서 `Cumulative Steepness`와 단어 `CSM`의 검색 결과는 없었다. swantech PDF 29–33쪽과 swanuse PDF 67·69·71·138쪽을 대조했다. 상대 링크는 모두 존재한다. 대상 줄에는 절대 경로와 이중 대괄호와 검증 한계 문장이 없다. 이 노트의 대상 줄에는 mermaid 상자가 없다.

노트 경로: `models/SWAN/source-analysis/swan-whitecapping.md`.

| 구분 | 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| 정정 | swan-whitecapping.md:6 | 과거 마이그레이션 설명과 `R1–R8 반영` | 이번 36줄의 실제 대조 범위 | 본 작업의 R2·R5·R7 및 원문 대조 |
| 정정 | swan-whitecapping.md:16 | 선택지 개수와 바람·백파의 양방향 조합 요구 설명 | 선택 범위·호출·행렬 가산을 명시하고 오류 수준 1의 메시지로 설명 | `src/swancom1.ftn:7505–7515`; `src/swancom2.ftn:2645–2650,2893–2897`; `src/swanmain.ftn:6419–6445`의 `CALL MSGERR (1, ...)` |
| 보완 | swan-whitecapping.md:97 | GEN3 WESTH의 CDS2 생략값만 인용 | WCAP AB의 같은 생략값 인용 추가 | `src/swanpre1.ftn:2511`의 `CALL INREAL ('CDS2', PWCAP(1), 'STA', 5.0E-5)` |
| 보완 | swan-whitecapping.md:137 | UP/DOWN의 나눗셈만 인용 | 분자 D의 정의와 원문 추가 | `src/SdsBabanin.ftn90:192`의 `DEDENS=EDENS-EDENST`; 195행의 `DEDENS=MAX(0.0,DEDENS)` |

기계 확인 후보 `src/swanmain.ftn:6674`의 WESTH·XNL 조건문: 오판이다. 조건문은 6674–6675행에 이어진다. 6677행의 재대입과 함께 노트 226행의 인용에 일치한다. 줄 끝 판 번호도 원문의 일부다.

기계 확인 후보 `website/modifications/modifications.htm:326`: 오판이다. `Alternative approximations for two physical processes are available:`은 326–330행에 걸친 문장이다. 시작 줄 326은 맞다.

기계 확인 후보 `website/modifications/modifications.htm:813`: 오판이다. 물리 선택의 오류 처리 설명은 813–827행에 걸친 문장이다. 노트 237행의 인용과 시작 줄 813은 맞다.

미해결 항목은 없다.

### 5. swan-wind-formulations-implementation.md — 완료

대조한 `+` 줄은 28줄이다. 정정은 3줄이다. 보완은 0줄이다. 대상 줄 범위는 6, 11, 29, 32, 154–155, 157, 159, 164, 192–210이다.

R2·R7의 대상 행 9개를 최종 결론과 대조했다. 결론 분류는 모두 유지한다. SS-501의 쪽 번호와 SS-503의 항목 설명은 원문에 맞췄다. 나머지 결론 차이는 `해석:` 표지의 생략과 쪽 번호 표기의 풀어쓰기로 확인했다. GEN1의 천해 하한·CFPM·GEN1/2 풍속 보정·항력 상한·선형 입력 필터·Janssen 반복·Yan 음의 성장률 제거·ST6 선형 응력 1% 상한을 코드와 대조했다. swantech PDF 27–29·32·58–60쪽과 swanuse PDF 36·66–67·69쪽을 확인했다. PDF 28쪽 이미지로 (2.36)의 수식을 대조했다. `settings.htm:43–44`와 `node23.html:295–312`를 확인했다. 상대 링크는 모두 존재한다. 대상 줄에는 절대 경로와 이중 대괄호와 검증 한계 문장이 없다. 이 노트의 대상 줄에는 mermaid 상자가 없다.

노트 경로: `models/SWAN/source-analysis/swan-wind-formulations-implementation.md`.

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| swan-wind-formulations-implementation.md:6 | 과거 마이그레이션 설명과 `R1–R8 반영` | 이번 28줄의 실제 대조 범위 | 본 작업의 R2·R7 및 원문 대조; `SWAN-notes-apply-1.md:26,44` |
| swan-wind-formulations-implementation.md:202 | (2.34)–(2.35)를 PDF 28쪽 / 인쇄 20쪽으로 인용 | PDF 27–28쪽 / 인쇄 19–20쪽으로 정정 | swantech PDF 27쪽의 (2.34); PDF 28쪽의 (2.35). C 분류와 고풍속 제한의 세부가 생략됐다는 결론은 유지한다. |
| swan-wind-formulations-implementation.md:204 | 새 총응력이 파랑 응력보다 작으면 복귀 | 작거나 같으면 복귀 | `src/swancom3.ftn:2563`의 `IF ( TAUNEW .LE. TAUW ) TAUNEW = .5 * (TAUTOT + TAUW)` |

기계 확인 후보: 사용자 지정 후보 없음. 인용 조건문·수식·수치·단위와 원문 줄은 위 정정 후 일치한다. 미해결 항목은 없다.

### 6. swan-adcirc-coupling.md — 완료

대조한 `+` 줄은 19줄이다. 정정은 2줄이다. 보완은 1줄이다. 대상 줄 범위는 6–7, 23, 33, 51, 65, 135, 172–183이다.

R5·R7의 대상 행 3개를 최종 결론과 대조했다. H-1204는 `SWAN-git-verify-A.md:112`의 최종 D 판정과 대조했다. 분류 설명을 최종 보고서와 같게 고쳤다. 결론 문장은 유지한다. `122b595`와 `43e9bbb`의 인용 줄을 직접 열었다. `122b595`의 날짜는 2023-02-28이다. 현재 코드의 IDRAG 대입에는 ADCIRC 결합 전용 초기 대입이 없다. MPI·COH·ADCIRC 스위치의 치환 순서와 주 프로그램 우회 주석을 확인했다. Triangle·Easymesh 파일명의 확장자 결합을 코드에서 확인했다. CICE ADCICE의 읽기와 `IICE.GT.2`인 소산 호출을 구분했다. 매뉴얼 PDF 4종에서 CICE·ADCICE·WBICETH 검색 결과는 없었다. 웹의 41.01 patch A 항목을 확인했다. 상대 링크는 모두 존재한다. 대상 줄에는 절대 경로와 이중 대괄호와 검증 한계 문장이 없다. 이 노트의 대상 줄에는 mermaid 상자가 없다.

노트 경로: `models/SWAN/source-analysis/swan-adcirc-coupling.md`.

| 구분 | 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| 정정 | swan-adcirc-coupling.md:6 | 과거 마이그레이션 설명과 `R1–R8 반영` | 이번 19줄의 실제 대조 범위 | 본 작업의 R5·R7·git 판정 A 및 원문 대조 |
| 보완 | swan-adcirc-coupling.md:33 | Triangle·Easymesh 키워드 분기만 인용 | 확장자를 붙이는 원문 인용 추가 | `src/SwanReadTriangleGrid.ftn90:87,136`의 `.node`·`.ele`; `src/SwanReadEasymeshGrid.ftn90:80,114`의 `.n`·`.e` |
| 정정 | swan-adcirc-coupling.md:182 | `D 문서에만 있음` | `D 현재 해당 구현 없음` | R7 H-1204 최종 행 1080; `SWAN-git-verify-A.md:112`; `website/modifications/modifications.htm:1201,1204`; 현재·과거 `swanmain.ftn`의 초기화 |

기계 확인 후보: 사용자 지정 후보 없음. `!MPI!NCOH`와 줄 끝 판 번호는 원문과 일치한다. 미해결 항목은 없다.

## 전체 완료 집계

| 노트 | 대조한 `+` 줄 | 정정 줄 | 보완 줄 |
|---|---:|---:|---:|
| swan-tech-ch4-5-bc-2d-setup.md | 121 | 16 | 0 |
| swan-tech-ch2-dissipation-detailed.md | 60 | 5 | 0 |
| swan-output-writers-implementation.md | 41 | 3 | 3 |
| swan-whitecapping.md | 36 | 2 | 2 |
| swan-wind-formulations-implementation.md | 28 | 3 | 0 |
| swan-adcirc-coupling.md | 19 | 2 | 1 |
| 합계 | 305 | 31 | 6 |

수량은 검증 시작 시점의 `git diff -U0 HEAD`와 완료 후 같은 명령의 결과를 대조해 확인했다. 각 노트의 `+` 줄 수는 변하지 않았다. 수정한 37줄은 모두 검증 시작 시점의 대상 줄에 속한다. 정정한 31줄에는 `[10-13 전수 검증 정정]`을 붙였다. 보완한 6줄에는 `[10-13 전수 검증 보완]`을 붙였다.

기계 확인 후보 8건은 모두 원문을 열어 오판으로 판정했다. 각 판정은 해당 노트의 결과에 한 줄씩 기록했다. HTML의 다중 줄 문장은 시작 줄부터 끝까지 대조했다. 과거 커밋 인용은 해당 커밋의 파일에서 대조했다. 소스의 전처리 표식과 줄 끝 판 번호는 원문에 있는 그대로 인정했다.

대상 줄에는 최종 A 분류 행이 없다. 과거 A였던 H-1204는 git 판정 A 보고서의 최종 D 분류와 일치한다. 대상 줄에는 mermaid 상자가 없다. 상대 링크의 대상 파일은 모두 존재한다. 절대 경로·이중 대괄호·검증 한계 문장은 대상 줄에 없다. frontmatter 6개는 YAML 파싱을 통과했다. 대상 노트의 `git diff --check HEAD`는 오류 없이 끝났다. 미해결 항목은 없다.
