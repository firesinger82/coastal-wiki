# SWASH 노트 전수 대조 기록 1

대상 노트: `models/SWASH/source-analysis/swash-timestepping-update-driver.md`.

기준은 작업 시작 시 `git diff -U0 HEAD -- models/SWASH/source-analysis/swash-timestepping-update-driver.md`이다.
추가·수정 대상은 311줄이다.
대상 범위는 시작 시 노트의 7–8, 63–67, 73–79, 145, 159–163, 245–535줄이다.
삭제 대상은 HEAD의 7, 62줄이다.
빈 줄과 frontmatter를 포함한다.
정정·보완 수는 수정한 대상 줄을 기준으로 센다.

기계 확인 불일치 후보: 없음.

검증 상태: 완료.

## 대상 줄 대조 원장

아래 노트 줄 번호는 작업 시작 시와 완료 시에 동일하다.
노트의 전체 줄 수는 535줄로 유지했다.
각 범위에는 빈 줄, 제목, 표 구분선과 코드 블록 경계도 포함했다.
표의 줄 수를 합하면 최초 diff의 추가·수정 줄 311줄과 같다.

| 노트 줄 | 줄 수 | 대조 근거와 결과 |
|---|---:|---|
| 7–8 | 2 | frontmatter의 판독 대상 파일과 `SwashInit.ftn90:79`의 `VERNUM = 12.01`을 확인했다. recovery 반영 날짜는 `SWASH-notes-apply-7.md`의 해당 노트 기록과 일치한다. 기존 인용 방법 설명은 보존되어 있다. |
| 63–67 | 5 | `SwashMain.ftn90:271–325`, `SwashModule1.ftn90:629–631,661–666`, swashuse PDF p.99–100, swashtech PDF p.98을 대조했다. SG1-926의 기존 조건 유지 지시와 ST2-151의 보충 지시를 반영했다. 63줄을 정정했다. |
| 73–79 | 7 | callflow §6.2·RF-012·RF-016과 대조했다. `SwashReadInput.ftn90:2811–2817`이 백업을 호출한다. `SwashBackup.ftn90:300–328`, `SwashInitCond.ftn90:392–425`의 정점 순회와 `SwashInitCompUgrid.ftn90:119,121,134`의 셀·면 할당이 다르다. E·강함은 E2 판정과 같다. |
| 145 | 1 | `SwashUpdateData.ftn90:221–250`의 이전 시간 저장과 `SwashComputStruc.ftn90:107–181`의 FSI 재진입을 대조했다. 재진입 경로에는 이전 시간 저장 호출이 없다. callflow §6.2와 일치한다. |
| 159–163 | 5 | `SwashCheckPrep.ftn90:3844–3847`의 초기 rtur, `SwashUpdateData.ftn90:2571`, `SwashVertVisc.ftn90:72`, `SwashComputStruc.ftn90:125,254,261`을 대조했다. 첫 단계와 이후 단계의 난류 상태 설명은 RF-010 최종 결론과 일치한다. |
| 245–251 | 7 | 흐름도 제목과 callflow §4 상대 링크를 확인했다. |
| 252–324 | 73 | 시작·종료 Mermaid 블록은 callflow §4.1과 문자열이 같다. 상자의 file:line을 원문과 대조했다. `Swash.ftn90:56–67`, `SwashMain.ftn90:126–390`, `SwashReadInput.ftn90:286–294,506,2811–2840`, `SwashCheckPrep.ftn90:5974`, `SwashModule2.ftn90:475,499`에서 분기와 연결을 확인했다. |
| 325–327 | 3 | 빈 줄과 구조 격자 흐름도 제목이다. |
| 328–444 | 117 | 구조 격자 Mermaid 블록은 callflow §4.2와 문자열이 같다. `SwashComputFlow.ftn90:74–196`의 1D·2D·층 수·mtimei·mimetic·lsubg 분기와 `SwashComputStruc.ftn90:107–261`의 호출 순서를 확인했다. 압력 분기의 상자에 적힌 솔버 선언·호출 줄도 확인했다. |
| 445–447 | 3 | 빈 줄과 비구조 격자 흐름도 제목이다. |
| 448–503 | 56 | 비구조 격자 Mermaid 블록은 callflow §4.3과 문자열이 같다. `SwashCompUFlow.ftn90:70–110`, `SwashCompUnstruc.ftn90:67–112`, `SwashCompUTurb.ftn90:75–79`와 각 Uflow 압력 솔버 호출을 대조했다. |
| 504–513 | 10 | 출처 링크와 여섯 칸의 표 머리말을 확인했다. 510줄의 판 정보는 AD §1–2와 일치한다. 판 문자열의 코드 인용과 AD 링크를 보완했다. |
| 514–535 | 22 | 차이 표의 22개 행을 각 보고서의 최종 결론과 현재 코드·매뉴얼·과거 커밋 원문에 대조했다. 행별 근거는 아래에 기록했다. |

## 삭제 줄의 근거

| HEAD 줄 | 삭제된 내용 | 판정과 근거 |
|---|---|---|
| 7 | 기존 `verification_method` 한 줄 | 기존 설명 전체가 현재 7줄에 남아 있다. `2026-10-15 SWASH recovery 대조 보고서 반영`만 덧붙였다. `SWASH-notes-apply-7.md`의 반영 기록이 이를 뒷받침한다. |
| 62 | 시간 간격 설명과 `mtimei`·`pnums`의 `source-needed, 본 배정 외 파일` 괄호 | SG1-926은 20단계 조건과 EXPL 조건을 유지하도록 지시한다. ST2-151은 매뉴얼과의 차이를 연결하도록 지시한다. 현재 63–67줄은 이 내용을 보존한다. 삭제한 미확인 괄호는 `SwashModule1.ftn90:250,629–631,661–666`과 이번 판독 기록 `read/SWASH/swash/src/SwashModule1.ftn90.md`로 해결했다. 63줄에 선언 인용을 보탰다. |

## 차이 표 22행의 대조

이 기록에서 코드 파일명은 `models/SWASH/raw/source_code/swash/src/` 기준이다.
`misc/`와 `README.md`는 `models/SWASH/raw/source_code/swash/` 기준이다.
보고서는 `_staging/recovery/compare/swash-<보고서명>-vs-code.md`의 §5를 사용했다.
callflow는 `_staging/recovery/flow/SWASH-callflow.md`의 §8을 사용했다.
각 보고서 끝의 10-15 전수 검증 기록을 적용했다.

| 노트 줄·행 ID | 최종 분류 | 원문 대조 결과 |
|---|---|---|
| 514 · RF-002 | C | swashtech PDF p.111의 9장 미작성 문장과 p.98의 운동량·연속방정식 순서를 구별했다. swashuse PDF p.123–124의 명령 순서도 존재한다. 수송·난류 호출은 `SwashComputStruc.ftn90:254,261`과 같다. |
| 515 · RF-010 | C | `SwashReadInput.ftn90:1253–1273`의 난류 선택, `SwashUpdateData.ftn90:2571`, `SwashVertVisc.ftn90:72`의 점성계수 식, `SwashComputStruc.ftn90:125,261`의 순서를 확인했다. 결론의 활성 조건과 시차는 유지했다. 이전 노트 줄 번호를 정정했다. |
| 516 · RF-012 | C | `SwashReadInput.ftn90:2811–2817`의 별도 백업 호출과 `SwashMain.ftn90:263`의 출력을 구별했다. 이전 노트 줄 번호를 정정했다. |
| 517 · SG1-101 | C | swashuse PDF p.135의 명시적 적분 문장은 p.99–100의 두 방법 설명과 구별된다. `SwashReadInput.ftn90:1864–1865`, `SwashCheckPrep.ftn90:607–612`, `8756667:src/SwashReadInput.ftn90:1375–1383`을 확인했다. 최종 보고서의 B→C 정정이 이전 AD의 B 판정보다 우선한다. |
| 518 · SG1-105 | C | swashuse PDF p.136·99에는 20단계 유지 조건이 없다. `SwashMain.ftn90:271–291`의 동적·명시적·CFL 하한·20단계 조건을 확인했다. 두 매뉴얼 판독 기록과 원본 README.md·misc/swash.edt의 검색 결과도 최종 보고서와 같다. |
| 519 · SG1-901 | C | `SwashMain.ftn90:271–303,325`에서 반감·배증·istep 초기화·시간 전진 순서를 확인했다. 코드 인용의 조건문과 수치가 원문과 같다. |
| 520 · SI2-255 | C | `SwashFlowDP.ftn90:108–110,123–124`의 수위 하한과 가상점 복사를 확인했다. `SwashReadInput.ftn90:2144`의 DPS/BOTC 별칭을 확인했다. swashuse PDF p.97–98의 본문 누락과 p.161의 DPSopt 도식을 구별했다. |
| 521 · SI2-285 | C | `SwashComputStruc.ftn90:233,247,254,261`의 순서와 조건을 확인했다. `SwashDryWet.ftn90:85`, `SwashUDryWet.ftn90:84`의 엄격한 `>` 비교를 확인했다. 계산 호출에는 `!TIMG` 접두어가 없다. |
| 522 · SI2-286 | C | `SwashUpdateData.ftn90:203–217`의 적용 조건과 `mod(it-1,ifpco)`를 확인했다. `SwashCheckPrep.ftn90:5495`의 단위 대각 대입을 확인했다. `SwashReadInput.ftn90:1559–1561`의 NONE은 빈도 −1을 설정한다. swashuse PDF p.89–93 본문과 p.160 부록을 구별했다. |
| 523 · SI1-064 | B | `SwashCheckPrep.ftn90:2024,2634`, `SwashUpdateFld.ftn90:106,115–117,230–239`로 첫 호출의 `F*(1-dt/(TBEGINP-timco+dt))`를 확인했다. swashuse PDF p.22의 0 가정과 다르다. 식의 적용 범위를 첫 호출로 명시했다. 보고서 §5 링크와 초기화 인용을 넣었다. |
| 524 · SI1-065 | B | `SwashUpdateFld.ftn90:119–125,230–239`의 `1.e10` 시각과 잔여 보간을 확인했다. swashuse PDF p.22의 마지막 값 유지 문장과 구별했다. 마지막 입력 시각에 계산 시각이 맞는 예외는 유지했다. |
| 525 · SI1-527 | C | swashuse PDF p.20의 삼선형 보간 설명을 확인했다. `SwashUpdateFld.ftn90:237–258`의 성분 보간, `vtot > 0.` 조건, 크기 보정식과 ELSE 대입을 모두 확인했다. |
| 526 · SI1-567 | C | swashuse PDF p.72의 수렴 설명과 `SwashComputStruc.ftn90:92–96`의 절대·상대 혼합식을 대조했다. 회전값에 대한 도 단위 변환은 같은 파일 175–177줄의 출력에서 수행한다. 내부 회전값은 라디안이다. |
| 527 · SI1-568 | C | swashuse PDF p.72의 50회 기본값·0.3 권고와 p.73의 relax 범위·기본값을 구별했다. `SwashCheckPrep.ftn90:1435–1443`, `SwashComputStruc.ftn90:187–201`을 확인했다. 문서 쪽, 깨진 마크업과 출력 조건을 정정했다. |
| 528 · SO1-276 | C | swashuse PDF p.124의 STOP 설명과 `SwashReadInput.ftn90:286–294`, `SwashMain.ftn90:146,232,263`을 확인했다. NOCO 반환 뒤에도 준비·출력 경로가 남는다. 문서·코드 칸을 정정했다. |
| 529 · SO1-277 | C | `SwashMain.ftn90:162–183,345–351`, `SwashPrintGridInfo.ftn90:158–160`, `SwashModule2.ftn90:125–126`을 확인했다. 오류 수준·ITEST·nds 조건과 닫는 태그는 원문과 같다. 문서·코드 칸을 정정했다. |
| 530 · ST2-135 | C | swashtech PDF p.94–95의 공간 Coriolis 힘과 내적 0을 확인했다. swashuse PDF p.83에는 시간 가중식이 없다. `misc/swash.edt:186`, `SwashReadInput.ftn90:1382–1385`, `SwashExpDepUflow.ftn90:865–882,957`의 선택·가중식을 확인했다. |
| 531 · ST2-151 | C | swashtech PDF p.98과 swashuse PDF p.99의 시간 간격 설명을 확인했다. `SwashMain.ftn90:271–291`의 20단계 조건을 구별했다. 비구조 기본 반암시적 방법은 swashuse PDF p.100과 `SwashCheckPrep.ftn90:607–612`에 있다. |
| 532 · ST2-349 | C | swashtech PDF p.68·98과 swashuse PDF p.97–98을 확인했다. `SwashInit.ftn90:394`, `SwashFlowUDP.ftn90:137,154–160`의 세 꼭짓점 평균·내부 면 최솟값·경계 셀 대입이 원문과 같다. |
| 533 · ST2-350 | B | swashuse PDF p.97의 비구조 전면 금지와 `SwashReadInput.ftn90:2144–2154`, `SwashFlowUDP.ftn90:81–168`의 MIN·MEAN 지원이 다르다. 최종 보고서의 C→B 정정을 유지했다. 최초 공개판과 12.01 배포판에도 같은 분기가 있다. |
| 534 · ST2-377 | C | `SwashInit.ftn90:309`, `SwashReadInput.ftn90:1385`, `SwashExpDepUflow.ftn90:867,882,957`에서 기본 0.1과 가중치 1.6·−0.6을 확인했다. 에너지 보존을 추가로 단정하지 않은 결론을 유지했다. |
| 535 · ST2-417 | C | swashuse PDF p.22·41–48과 swashtech PDF p.113을 대조했다. `SwashUpdateUData.ftn90:1303–1340`의 입력장 갱신과 LogLaw/BotFrict 분기를 확인했다. 모든 마찰을 매 단계 재계산한다는 일반화는 없다. |

차이 표에서 센 분류는 C 19행과 B 3행이다.
이 표에는 A 행과 E 행이 없다.
본문 77–78줄의 RF-016은 `SWASH-git-verify-E2.md`의 E·강함을 유지한다.
`SWASH-git-verify-E1.md`와 `SWASH-conclusion-sample.md`에는 이 노트의 결론을 추가로 변경하는 대상 행이 없다.

## 정정·보완 목록

아래 경로의 줄 번호는 완료 노트 기준이다.
정정과 보완은 한 줄을 중복 계산하지 않았다.
같은 표 행에서 여러 오류를 고친 경우에는 정정 한 줄로 셌다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `models/SWASH/source-analysis/swash-timestepping-update-driver.md:63` | 정정 | `20스텝 안정`, `timco += dt`, `암시적 ... dt 고정`이라는 압축 설명 → 동적 명시적 적분의 반감·배증 조건, 같은 dt 유지 조건, 실제 istep 증가문, 반암시적 자동 조정 제외를 문장별로 적었다. mtimei·pnums 선언 인용을 붙였다. | `SwashMain.ftn90:271–295`의 `nstatc == 1`, `mtimei == 1`, `cflmax > pnums(3)`, `cflmax < pnums(2)`, `if ( .not. istep < 20 ) then`. 같은 파일 289줄은 `the time step has been constant for the last 20 integration steps`라고 적는다. 303·325줄은 실제 시간 전진과 `istep = istep + 1`이다. `SwashModule1.ftn90:250,629–631,661–666`은 모듈·변수 선언이다. SG1-926·ST2-151의 조건 유지 지시와 같다. |
| `models/SWASH/source-analysis/swash-timestepping-update-driver.md:229` | 보완 | `Commdata2/3/4·Timecomm ... 나머지는 source-needed` → 같은 파일에 해당 네 모듈이 선언되어 있다는 사실과 선언 줄 인용. | `SwashModule1.ftn90:125`의 `module SwashCommdata2`, 250줄의 `module SwashCommdata3`, 769줄의 `module SwashCommdata4`, 860줄의 `module SwashTimecomm`. `read/SWASH/swash/src/SwashModule1.ftn90.md`의 같은 구간 판독과 일치한다. 사용자 지시 6에 따라 최초 diff 밖의 잔존 미완 문장 한 줄을 해결했다. |
| `models/SWASH/source-analysis/swash-timestepping-update-driver.md:510` | 보완 | 판 정보를 한 줄에 나열하고 직접 근거 링크를 생략 → 사실별 문장과 코드 판 문자열 인용 및 AD §1–2 링크. | `SwashInit.ftn90:79`의 `VERNUM = 12.01`. `compare/SWASH-git-verify-AD.md:26–44`의 문서 기준 `7949227 2026-05-06`, 코드 기준 `a486d5f 2026-05-26`, 후속 변경 `608ffd7`·`9554c98`. |
| `models/SWASH/source-analysis/swash-timestepping-update-driver.md:515` | 정정 | RF-010의 현재 노트 인용 `:144`와 현재에도 시차 설명이 빠졌다는 표현 → 현재 호출 설명의 `:157` 및 대조 전 §6.2의 누락이라는 범위. | 노트 157줄의 수직 점성 호출 설명. `flow/SWASH-callflow.md:3412,3459`는 수정 전 노트의 누락을 판정한다. `SwashUpdateData.ftn90:2571`은 `if ( iturb /= 0 ) call SwashVertVisc`이다. |
| `models/SWASH/source-analysis/swash-timestepping-update-driver.md:516` | 정정 | RF-012의 출력 행 인용 `:51`과 현재에도 백업 진입점이 빠졌다는 표현 → 현재 출력 행 `:52` 및 대조 전 노트의 누락이라는 범위. | 노트 52줄의 `SwashOutput` 출력 행. `flow/SWASH-callflow.md:3418,3461`은 수정 전 노트를 판정한다. `SwashMain.ftn90:263`은 `call SwashOutput`이다. |
| `models/SWASH/source-analysis/swash-timestepping-update-driver.md:523` | 정정 | SI1-064의 `timco < TBEGINP이면`과 노트 내 대상을 잘못 가리키는 `5절에서 ... 적는다` → 첫 SwashUpdateFld 호출로 식의 범위를 한정하고 inputs-setup 보고서 §5를 링크했다. fricf 초기화 인용도 넣었다. | `compare/swash-inputs-setup-vs-code.md:740`은 첫 UpdateFld 호출의 식을 유도한다. `SwashCheckPrep.ftn90:2024`는 `if ( istat == 0 ) fricf = 0.`이다. 같은 파일 2634줄은 `fricf(indx,2) = cf`이다. `SwashUpdateFld.ftn90:106,115–117,230–239`는 복사·분기·보간을 수행한다. |
| `models/SWASH/source-analysis/swash-timestepping-update-driver.md:527` | 정정 | SI1-568의 `p.72 ... 기본 0.3·50회`, 깨진 `<`·백틱·`br>` 표기, iamout만 적은 출력 조건 → p.72의 50회 기본값·0.3 권고와 p.73의 0.3 기본값을 분리했다. 문서 인용을 문서 칸에 넣었다. 이동 강체·MASTER 조건을 명시했다. | swashuse PDF p.72는 `maximum number of iterations is set to 50`와 `proposed a fixed low value of 0.3`을 적는다. p.73은 `Default: [relax] = 0.3.`을 적는다. `SwashComputStruc.ftn90:187`은 `if ( ifloat == 2 .and. INODE == MASTER ) then`이다. 189–201줄의 미수렴 처리는 PRINT 쓰기이다. |
| `models/SWASH/source-analysis/swash-timestepping-update-driver.md:528` | 정정 | SO1-276의 문서 칸에 코드 원문, 코드 칸에 `문서에 없음` → 문서 칸에는 swashuse PDF p.124의 설명 범위를 적었다. 코드 인용과 git 근거는 코드 칸으로 합쳤다. | swashuse PDF p.124의 STOP 설명. `SwashReadInput.ftn90:290–292`의 `comput = 'NOCO'`. `SwashMain.ftn90:146,232`의 STOP·NOCO 분기. `compare/swash-outputs-vs-code.md:642`의 C 결론을 유지했다. |
| `models/SWASH/source-analysis/swash-timestepping-update-driver.md:529` | 정정 | SO1-277의 문서 칸에 코드 원문, 코드 칸에 `문서에 없음`과 추가 코드 → 문서 누락 표기를 문서 칸으로 옮겼다. 모든 코드 인용은 코드 칸으로 합쳤다. | `SwashMain.ftn90:183,347–349`, `SwashPrintGridInfo.ftn90:158–160`, `SwashModule2.ftn90:125–126`. `compare/swash-outputs-vs-code.md:643`의 조건과 C 결론을 유지했다. |

## 원문·형식 확인 결과

매뉴얼은 쪽별 판독 기록과 추출 텍스트를 대조했다.
수치·식·명령 도식은 swashuse PDF p.72,73,97,98,99,100,136,160,161과 swashtech PDF p.95,98의 쪽 이미지로 확인했다.
PDF 쪽과 인쇄 쪽은 8쪽 차이이다.
노트의 쪽 번호는 PDF 쪽이다.

과거 코드 인용은 공개 사본에서 읽기 전용 `git show`로 확인했다.
확인한 원문은 `8756667:src/SwashReadInput.ftn90:1375–1383`, `8756667:src/SwashUpdateFld.ftn90:100–125,230–253`, `8756667:src/SwashFlowUDP.ftn90:78–170`, `7949227:src/SwashFlowUDP.ftn90:78–170`의 해당 인용 구간이다.
커밋 HASH·날짜와 후속 변경의 관련 여부는 AD·E2의 해당 판정과 일치한다.

Mermaid 3개 블록은 완료 노트에서도 보고서 §4와 문자열이 같다.
대조한 내용은 상자 선언, file:line, 분기 조건과 간선이다.
차이 표의 행 ID 22개는 `assign/SWASH-note-job-7.tsv`의 이 노트 배정과 같다.
각 표 행은 여섯 칸이다.
표 행의 백틱은 모두 짝을 이룬다.
노트의 상대 링크 15곳은 모두 실제 파일을 가리킨다.
링크에 적힌 절 앵커도 존재한다.
노트에는 사용자 홈 절대 경로와 이중 대괄호 링크가 없다.
노트에는 잔존 source-needed·미검수·미확인·후속 대상·다음 후보 문장이 없다.
빌드·실행 검증을 요구하는 할 일 항목도 없다.
기계 확인 불일치 후보는 사용자 제공 목록대로 없다.

이번 수정은 시작 노트와 비교하여 63,229,510,515,516,523,527,528,529의 9줄이다.
정정 태그는 7줄에 있다.
보완 태그는 2줄에 있다.
차이 표의 정정 태그는 결론 문장 칸 끝에 있다.
대상 노트의 읽기 전용 `git diff --check HEAD -- <노트>`는 통과했다.
최종 HEAD diff는 추가 312줄과 삭제 3줄이다.
최초 diff와의 차이는 사용자 지시 6에 따라 보완한 기존 229줄 한 줄이다.

## 완료 — swash-timestepping-update-driver.md

추가·수정 대상 311줄을 모두 대조했다.
최초 삭제 대상 2줄의 근거를 별도로 확인했다.
최초 diff 밖의 잔존 미완 문장 1줄도 원문 인용으로 해결했다.
검증 방식은 코드·매뉴얼·보고서의 정적 대조이다.
미해결 항목은 없다.
마지막 줄의 대조 수는 작업 시작 시 diff의 추가·수정 줄 수이다.
정정·보완 수는 이번에 바꾼 노트 줄 수이다.

대조 311, 정정 7, 보완 2
