# SWASH 노트 전수 대조 7

대상은 사용자가 지정한 노트 네 개다.
기존 파일의 대상 줄은 작업 시작 시 `git diff -U0 HEAD -- <노트>`의 추가 줄이다.
새 파일의 대상 줄은 전체 줄이다.
삭제 줄은 보고서의 삭제 근거를 별도로 대조한다.
대조 줄 수에는 frontmatter와 빈 줄을 포함한다.
정정 수와 보완 수는 이번 검증에서 바꾼 대상 줄 수로 센다.
같은 줄의 사실과 인용을 함께 바꾸면 정정 한 건으로 센다.
완료한 노트의 결과는 아래에 순서대로 추가한다.

## swash-initialization-grid.md — 완료

대조한 추가 줄은 92개다.
삭제 줄은 별도로 10개를 대조했다.
정정은 10줄이다.
보완은 3줄이다.
줄 번호는 이번 검증 전후에 같다.

| 대상 추가 줄 | 대조 근거와 결과 |
|---|---|
| 7–8 | apply-7의 frontmatter 반영 기록과 대조했다. 기존 검증 방법과 10-15 반영 날짜를 유지한다. |
| 52–60, 62–64 | SwashInit:121–161, SwashReadInput:527–554,580–584, SwashCheckPrep:889–918,1219와 SI1-120·503·708을 대조했다. 미지정 밀도 조건을 고쳤다. |
| 89–91, 93–97 | SwashInputGrid:149–388, SwashReadInput:2398–2400, SwashCheckPrep:342–354,2266–2269와 SI1-513·515·517·709를 대조했다. 대기압 누락과 끊긴 문장을 고쳤다. 94는 빈 줄이다. |
| 123–125 | SwashInit:266, ocpmix:691–699, SwashInputField:233–240,348–425와 SI1-259·260을 대조했다. 다음 파일 이름 읽기는 첫 층 뒤이다. 125는 빈 줄이다. |
| 146–151 | ocpids:111,154, SwashInitCompGrid:240–300, swanparll:3520–3543와 SG1-902·ST2-422를 대조했다. |
| 209, 213–219, 302 | SwashLayerIntfaces:46–48,76–84, SwashLayUIntfaces:44–116, SwashServices:531–585와 ST1-328·ST2-383을 대조했다. 층 1은 최상층이다. |
| 303–354 | 차이 표 43행의 모든 칸을 보고서 §5의 해당 ID와 대조했다. 표의 현재 코드 인용과 과거 커밋 인용을 각각 열었다. 제목·빈 줄·표 머리·출처 링크·판본 문장도 포함한다. |

현재 코드의 추가 대조 파일은 SwashGeometrics, SwashInitSteady, SwashUpdateDepths, SwashUpdateData, swanser, misc/swash.edt, switch.pl이다.
매뉴얼 대조는 swashuse PDF p.20·23·33–35·37–55·75·90·127·144·155–156과 swashtech PDF p.42·52·57·63–65·109·117의 해당 주장이다.
식·숫자·문법 판정에는 swashuse p.34·40·45·48–50·54·90·156과 swashtech p.57·63의 쪽 이미지도 사용했다.
Eckart 식에 온도 14와 염분 31을 대입한 산술값은 1023.040852547279 kg/m³이다.
SI1-120의 반올림 값 1023.04085와 일치한다.
A 행 SI1-259의 커밋은 AD §3의 `9d03fff`, 날짜는 2024-05-07과 일치한다.
E 행 SI1-229는 약함을 유지한다.
E 행 SI1-260·513은 강함을 유지한다.
차이 표의 결론 분류 43개는 최종 보고서와 같다.

| 정정·보완 위치 | 전 → 후 | 근거 원문 |
|---|---|---|
| swash-initialization-grid.md:54 정정 | `idens=0`만 조건으로 제시 → `idens == 0 .and. .not. rhow /= -999.` | SwashCheckPrep:894–899. SG1-889·ST1-292도 미지정 조건을 명시한다. |
| swash-initialization-grid.md:89 정정 | NONSTAT 목록에서 대기압 누락 → 대기압 포함 | SwashReadInput:2398–2400은 `igrd = 13`이다. SwashInputGrid:267–273은 13을 금지하지 않는다. SwashUpdateData:2517–2518은 이 입력장을 갱신한다. |
| swash-initialization-grid.md:93 정정 | `acur(20,21)만`에서 문장 중단 → 입력층 설정·1층 금지·허용량을 완전한 문장으로 복구 | SwashInputGrid:294–299. SI1-517. |
| swash-initialization-grid.md:124 정정 | 두 번째 층에서 목록 단위 0 읽기 → 첫 층을 읽은 뒤 목록 단위 0 읽기 | SwashInputField:394–396은 `k < ifllay(igr1)` 분기다. SI1-260 최종 §5와 E1. |
| swash-initialization-grid.md:149 보완 | `:251–253` → `:250–251` | SwashInitCompGrid:250의 `kpart == 2`와 :251의 `LORB = .true.`를 함께 가리킨다. |
| swash-initialization-grid.md:325 정정 | 두 번째 층에서 데이터 파일 닫기 → 첫 층을 읽은 뒤 데이터 파일 닫기 | SwashInputField:394–396. SI1-260 최종 §5와 E1. |
| swash-initialization-grid.md:327 정정 | 깨진 `<`와 백틱의 `br>swashuse` 결합 → 정상 `<br>swashuse` | SI1-503. swashuse p.155와 misc/swash.edt:9의 EPSHU 근거를 코드 인용과 분리한다. |
| swash-initialization-grid.md:328 정정 | 같은 줄바꿈 파손 → 정상 `<br>swashuse` | SI1-511. swashuse p.40·127의 가변층 필수 조건을 코드 인용과 분리한다. |
| swash-initialization-grid.md:329 정정 | 간격 정의 p.43 → p.45. SPRCON 조건이 빠진 결론 → 최종 §5의 영역·각도 검사와 더 큰 입력 간격 조건 반영 | swashuse p.45 이미지. SwashCheckPrep:948. swanser:1881–1932,1603–1604. SI1-513 최종 §5. |
| swash-initialization-grid.md:331 정정 | 허용 인덱스에서 13 누락 및 줄바꿈 파손 → 13 포함 및 정상 `<br>` | SwashReadInput:2398–2400. SwashInputGrid:267–273. |
| swash-initialization-grid.md:332 보완 | COMPUTE의 같은 허용오차 주장에 직접 인용 없음 → `SwashReadInput:492–493` 추가 | `mod(tfinc-tinic,dt) > 0.01*dt .and. mod(tfinc-tinic,dt) < 0.99*dt`. |
| swash-initialization-grid.md:341 정정 | 반복된 NONSTAT 허용량에서 대기압 누락 → 모든 반복에 대기압 포함 | SwashReadInput:2398–2400. SwashInputGrid:267–273. BOTTOM 금지의 B 결론은 유지한다. |
| swash-initialization-grid.md:354 보완 | 자동 분할 분기의 내부만 인용 → PARLL·KPART 진입 조건도 인용 | SwashInitCompGrid:240–247. SG1-902와 conclusion-sample의 ST2-422. |

SI1-515·709 보고서에도 대기압 누락이 있다.
SI1-513 보고서의 입력 간격 쪽 번호도 p.43으로 되어 있다.
위 세 항목은 직접 연 원문에 따라 노트를 정정했다.
쓰기 범위에 포함되지 않은 보고서는 수정하지 않았다.
이는 분류 변경이 아니다.

삭제된 HEAD 줄 7은 apply-7의 검증 방법 갱신에 해당한다.
HEAD 51–52는 SI1-120·503의 후속 처리 추가에 해당한다.
HEAD 54·79·81은 SI1-708·709·513의 수정안에 해당한다.
HEAD 127은 SG1-902의 분할 기본값 정정에 해당한다.
HEAD 185는 ST1-328의 경계면 표현 정정에 해당한다.
HEAD 189·272의 미확인 문장은 ST2-383의 공유 sigmacoor 판독으로 대체했다.
HEAD 79에서 함께 옮긴 연직 비균일 설명의 잘린 부분은 이번 검증에서 복구했다.
삭제 근거가 없는 유효 설명의 소실은 남아 있지 않다.

| 기계 확인 후보 | 판정 |
|---|---|
| 8756667:src/SwashCheckPrep.ftn90:787 `if ( idens == 0 ) then` | 과거 커밋 원문과 일치한다. 현재 파일과 비교한 오탐이다. 유지한다. |
| 8756667:src/SwashInputGrid.ftn90:252 `if ( KEYWIS ('NONSTAT') ) then` | 과거 커밋 원문과 일치한다. 유지한다. |
| 8756667:src/ocpmix.ftn:969 `ARR(IX,IY,1) = ARR(IX,IY,1) / VFAC` | 과거 커밋의 3차원 배열 원문과 일치한다. 유지한다. |
| 8756667:src/ocpmix.ftn:995 `CASE(5)` | 과거 커밋의 CASE(5)와 판 주석 40.02가 일치한다. 유지한다. |
| 8756667:src/ocpmix.ftn:1144 `990  IF (ITEST.GE.100 .OR. IDLA.LT.0) THEN` | 과거 커밋의 라벨과 조건이 일치한다. 유지한다. |
| 9d03fff:src/SwashInputField.ftn90:384 `if ( k < ifllay(igr1) ) then` | 과거 커밋 :384–386의 연속 세 줄과 일치한다. 유지한다. |
| a79b2c6:src/ocpmix.ftn:1063 `!     *** End of data file, in case SERIES/LAYERS next file is opened` | 과거 커밋의 주석과 일치한다. :1066–1076의 닫기·다음 이름 읽기도 확인했다. 유지한다. |
| 9d03fff:src/SwashInputField.ftn90:386 `read (iflndf(igr1), '(a)', end=901) filenm` | 과거 커밋 원문과 일치한다. 인용은 유지한다. 층 교체 시점의 한국어 설명은 :124·325에서 정정했다. |
| 9d03fff:src/SwashCheckPrep.ftn90:307 `if ( ifllay(20) /= kpmax .and. ifllay(20) /= 1 ) ...` | 과거 커밋의 전체 조건과 오류 문장이 일치한다. 유지한다. |
| 8756667:src/SwashInputGrid.ftn90:366 `if ( xpg(igrid1) /= xpc ...` | 과거 커밋의 전체 동일성 조건과 일치한다. 유지한다. |
| 8756667:src/SwashInputGrid.ftn90:255 첫 번째 인용 | 과거 커밋의 BOTTOM 금지 조건과 일치한다. 유지한다. |
| 8756667:src/SwashInputGrid.ftn90:255 두 번째 인용 | 같은 과거 조건의 반복 인용이다. 원문과 일치하므로 유지한다. |
| source-analysis/swash-initialization-grid.md:185 `! 최상층 = 바닥 + 수심 = 자유수면` | 반영 전 노트의 오기 인용이다. HEAD 삭제 줄과 ST1-328 §4·§5가 일치한다. 현재 본문의 사실 단언이 아니므로 유지한다. |

상대 링크 17개의 파일 대상이 존재한다.
절대 경로와 위키 링크 표기는 없다.
미완 항목은 없다.
Mermaid 블록은 없다.
대상 파일의 `git diff --check`는 통과했다.

## swash-bottom-friction-wind.md — 완료

대조한 추가 줄은 70개다.
삭제 줄은 별도로 9개를 대조했다.
정정은 6줄이다.
보완은 1줄이다.
줄 번호는 이번 검증 전후에 같다.

| 대상 추가 줄 | 대조 근거와 결과 |
|---|---|
| 7–8 | apply-8의 frontmatter 반영 기록과 대조했다. 검증 방법과 날짜를 유지한다. |
| 54, 56–57 | SwashInit:313, SwashReadInput:777–806, SwashBotFrict:47,104, SwashExpDep2DHflow:869,905와 ST1-338·339를 대조했다. |
| 110 | swashuse p.38, SwashCheckPrep:206,210과 ST2-406을 대조했다. 비구조 REPEATING 금지가 명시되어 있다. |
| 177–179, 244 | SwashReadInput:840–841, SwashWindStress:439–442와 SI2-287을 대조했다. |
| 213–219 | swashuse p.74–76, SwashCheckPrep:3110, SwashWindStress:135,391–401,962–989, SwashUWindStress:441–458, SwashExpDep1DHflow:465–473,721과 SI2-030·038을 대조했다. 219는 빈 줄이다. |
| 228–231 | SwashExpDepUflow:667–673,1040, SwashExpLayUflow:1076–1084와 ST2-370을 대조했다. 다층의 바람 암시적 항은 k=1에 더한다. 231은 빈 줄이다. |
| 258, 260–266 | SwashBotFrict:71–77,298, SwashUBotFrict:71–77,109–131,254, SwashWindStress:73–75,437, SwashUWindStress:75–77,312, SwashReadInput:777–806,840–841, SwashExpDepUflow:687–758, misc/swash.edt:148과 SI2-287·ST1-338·339·ST2-359·363·367을 대조했다. |
| 267–307 | 차이 표 30행의 모든 칸을 보고서 §5의 해당 ID와 대조했다. 현재 코드와 과거 커밋 인용을 열었다. 빈 줄·제목·표 머리·출처 링크·판본 문장도 포함한다. |

표의 추가 대조 파일은 SwashModule1, SwashUpdateData, SwashUpdateUData다.
매뉴얼 대조는 swashuse PDF p.34·38·73–78과 swashtech PDF p.63–64·94·109의 해당 주장이다.
식·숫자·단위는 swashuse p.74–77과 swashtech p.63–64·94의 쪽 이미지와 대조했다.
FIT 인쇄 계수의 극댓값 풍속은 `31.5*2.97/(2*1.49)=31.394295302013425` m/s이다.
SI2-009의 31.3942953 m/s와 일치한다.
차이 표의 결론 분류 30개는 최종 보고서와 같다.
E 행 SI2-030·ST1-294·ST2-371은 중간을 유지한다.
A 분류 행은 없다.

| 정정·보완 위치 | 전 → 후 | 근거 원문 |
|---|---|---|
| swash-bottom-friction-wind.md:217 정정 | 1DH 전체의 연속시간 응력식 → relwnd가 참인 1DH의 식 | SwashWindStress:391–393의 `if ( relwnd ) then`에서 유속을 뺀다. SwashExpDep1DHflow:465–473은 같은 조건에서 암시적 계수를 만든다. |
| swash-bottom-friction-wind.md:218 보완 | 분모 :721만 인용 → wndimp 생성 :465–473 추가 | SwashExpDep1DHflow:473의 `wndimp(nm) = cwndu(nm) / max(1.e-3,hum(nm))`를 :721에서 사용한다. |
| swash-bottom-friction-wind.md:266 정정 | 선형 마찰 구현에 swashuse p.76–77 인용 → SwashExpDepUflow:687–702 인용 | 해당 매뉴얼 쪽에는 LINEAR 선택이 없다. 소비자의 `irough == 11` 분기와 :702의 속력 인자 없는 식이 직접 근거다. ST2-359도 이 차이를 구별한다. |
| swash-bottom-friction-wind.md:283 정정 | SI2-038의 무조건 1DH 식 → relwnd 조건 명시 | SwashWindStress:391–393, SwashExpDep1DHflow:465–473을 코드 칸에 보탰다. 보고서의 조건 생략도 원문에 맞춰 바로잡았다. C 분류와 정규화 결론은 유지한다. |
| swash-bottom-friction-wind.md:288 정정 | 수심 하한을 §3에서 참조 → 아래 ST1-295 참조 | 보고서 §3과 노트 §3의 내용이 다르다. 노트 :292의 ST1-295가 수심 하한을 설명한다. 최종 부호의 직접 근거 SwashExpDep2DHflow:1360도 보탰다. |
| swash-bottom-friction-wind.md:293 정정 | 두 분모의 결과가 초당 단위 → 두 cbot 식의 단위가 초당 단위 | SwashExpDep2DHflow:869,905의 cbot는 각각 k/h와 cf·속력/h다. :1356의 시간 적분 분모는 1+dt·cbot를 포함하므로 무차원이다. 보고서의 같은 표현도 원문에 맞춰 바로잡았다. |
| swash-bottom-friction-wind.md:294 정정 | 마른 면 결함 후보를 제3절에서 판정 → theory-unstructured 보고서 §5 ST2-365의 E 강함 판정 링크 | 보고서 ST2-365 최종 결론. SwashExpDepUflow:718,789의 `cbot = 0.`는 마른 면 ELSE 안에서 배열 전체를 초기화한다. |

| 삭제된 HEAD 줄 | 보고서 근거와 판정 |
|---|---|
| 7 | apply-8의 대조 반영 기록을 검증 방법에 추가했다. 기존 방법은 유지했다. |
| 53 | ST1-338은 카드 생략과 방법 생략을 구별하도록 한다. 기존 내용은 유지했고 구문 표기 공백과 반영 표지만 바뀌었다. |
| 55 | ST1-339 §4·§5는 옵션 1의 무차원 계수와 옵션 11의 m/s 계수를 구별하도록 한다. 새 :56–57이 이를 반영한다. |
| 108 | ST2-406 §4·§5와 swashuse p.38이 비구조 REPEATING 금지를 확정한다. 추정 문장 삭제는 근거가 있다. |
| 175, 229 | SI2-287 §4·§5가 BETA와 HEIGHT의 뒤바뀐 설명을 바로잡는다. 실패 복귀값은 새 :179에 유지했다. |
| 243 | ST2-363·367과 인용 원문의 반복식·상수를 확인했다. 동일성의 범위를 반복식·상수로 한정한 새 :258은 근거가 있다. |
| 245 | SI2-287·ST1-338·339·ST2-359의 입력·소비 경로로 미정독 항목이 해결되었다. 새 :260–266에 사실 문장을 반영했다. |
| 246 | ST2-359는 계수 생성과 소비자를 구별한다. 소비자의 irough=11 분기가 선형 마찰을 구현하므로 기존 추정 삭제는 근거가 있다. |

| 기계 확인 후보 | 원문 판정 |
|---|---|
| src/SwashWindStress.ftn90:984 뒤 `부터, 비구조 식은` | SI2-030의 과거 커밋 경로 뒤 설명문을 코드 인용으로 묶은 오판이다. 8756667:src/SwashWindStress.ftn90:984의 보수 임계값을 확인했다. 유지한다. |
| src/SwashUWindStress.ftn90:458 뒤 `부터 존재한다.` | 같은 행의 설명문을 코드 인용으로 묶은 오판이다. 9b8a012:src/SwashUWindStress.ftn90:458과 일치한다. 유지한다. |
| src/SwashWindStress.ftn90:984 뒤 `와` | ST1-294의 두 커밋 비교에서 연결어를 코드로 읽은 오판이다. 8756667의 :984와 7949227의 :984를 열어 같은 조건임을 확인했다. 유지한다. |
| src/SwashWindStress.ftn90:984 뒤 `가 같으며 최초 문서` | 같은 비교의 설명문을 코드로 읽은 오판이다. E2의 SI2-030과 두 커밋 원문이 일치한다. 유지한다. |
| source-analysis/swash-bottom-friction-wind.md:55의 옵션 1·11 단위 문장 | 반영 전 노트의 오기 인용이다. HEAD 삭제 줄과 ST1-339 §4·§5가 일치한다. 현재 사실 단언이 아니므로 인용은 유지한다. |

상대 링크 7개의 파일 대상이 존재한다.
절대 경로와 위키 링크 표기는 없다.
미완 항목은 없다.
Mermaid 블록은 없다.
대상 파일의 `git diff --check`는 통과했다.

## swash-floating-rigid-body.md — 완료

대조한 추가 줄은 50개다.
삭제 줄은 별도로 4개를 대조했다.
정정은 5줄이다.
보완은 3줄이다.
줄 번호는 이번 검증 전후에 같다.

| 대상 추가 줄 | 대조 근거와 결과 |
|---|---|
| 7–8 | apply-7의 frontmatter 반영 기록과 해당 소스 파일·모듈 정의를 대조했다. |
| 18, 25–27 | SwashFloatObjects:314–322, SwashMotionRigidBod:44–50,84, SwashHydroLoads:45–56,170–184, SwashForcesRigidBod:44–51,93–97, SwashFlobjOutp:103–126, SwashReadInput:1071–1088, SwashCheckPrep:1872–1874,1900–1906과 SI1-563을 대조했다. 26은 빈 줄이다. |
| 75–85 | SwashReadInput:1001–1027,1226, SwashCheckPrep:1378–1429와 SI1-569 §4·SI1-566을 대조했다. ALPHA와 가속도 완화 RELAX의 입력을 구별한다. 85는 빈 줄이다. |
| 210–211 | SO1-305 §4의 연결 지시와 outputs §2.4의 SO1-171–183을 대조했다. SwashFlobjOutp:140–196의 출력 환산과 swashuse p.117–118의 단위를 확인했다. 211은 빈 줄이다. |
| 220–226 | SwashComputStruc:92–107,138–177, SwashCheckPrep:1435–1443과 SI1-567·568·569를 대조했다. 수렴 기준은 절댓값의 최댓값을 사용한다. |
| 227–250 | 차이 표 14행의 모든 칸을 최종 보고서 §5의 해당 ID와 대조했다. 모든 현재 코드 인용과 필요한 과거 커밋 원문을 열었다. 빈 줄·제목·표 머리·출처 링크·판본 문장도 포함한다. |

표의 추가 대조 파일은 SwashInit, SwashUpdKBCrigb, SwashDecOutQ, ocpcre, swanser, switch.pl, misc/swash.edt다.
매뉴얼 대조는 swashuse PDF p.22·69–73·100·117–118·157의 해당 주장이다.
식·숫자·문법·단위는 p.69–73·117–118·157의 쪽 이미지와 대조했다.
차이 표의 결론 분류 14개는 최종 보고서와 같다.
SG1-612는 E 강함을 유지한다.
도입 커밋 5d279d7과 날짜 2022-12-27은 E2의 최종 git 판정과 같다.
8756667:SwashReadInput:892–893의 직접 수치 판독과 5d279d7:930의 선행 INKEYW를 각각 열었다.
7949227:983의 선행 INKEYW는 현재 코드와 같다.
A 분류 행은 없다.

| 정정·보완 위치 | 전 → 후 | 근거 원문 |
|---|---|---|
| swash-floating-rigid-body.md:25 보완 | 모드·운동 진입부만 인용 → 여섯 자유도의 입력 선택 인용 추가 | SwashReadInput:1071–1088은 SURGE·SWAY·HEAVE·ROLL·PITCH·YAW와 ALL을 읽는다. |
| swash-floating-rigid-body.md:27 정정 | 1D가 SURGE·HEAVE·PITCH를 활성화 → SWAY·ROLL·YAW를 끄고 나머지 입력 선택을 유지 | SwashCheckPrep:1872–1874가 입력 dof를 복사한다. :1900–1906은 세 성분에만 .false.를 대입한다. SI1-563 §5도 비활성화로 서술한다. |
| swash-floating-rigid-body.md:81 보완 | CH의 :1014만 인용 → HHT :1007·WBZ :1010 추가 | 세 분기 모두 `call INREAL ('RHO', pship(5), 'STA', 1.0)`이다. |
| swash-floating-rigid-body.md:223 정정 | 이전 최대 변위 → 이전 변위 절댓값의 최댓값 | SwashComputStruc:92–93은 각각 `maxval(abs(xfot0))`와 `maxval(abs(xfor0))`이다. :95–96의 max 식에 이 값이 들어간다. 보고서 SI1-567의 축약 설명을 원문대로 구체화했다. |
| swash-floating-rigid-body.md:224 보완 | 회전 단위에 보고서만 인용 → SwashComputStruc:160,175–177 추가 | 회전 잔차를 출력할 때 180/pi를 곱해 degree로 바꾼다. 비교하는 내부 잔차는 라디안이다. |
| swash-floating-rigid-body.md:243 정정 | 깨진 br·문서명 표기 → HTML 줄바꿈과 swashuse | SI1-562의 최종 근거 칸과 대조했다. 문서명 앞의 백틱이 잘못 들어갔다. |
| swash-floating-rigid-body.md:249 정정 | 깨진 br·문서명 표기 → HTML 줄바꿈과 swashuse | SI1-570의 최종 근거 칸과 대조했다. KBC 상세 설명은 실제 p.73에 있다. |
| swash-floating-rigid-body.md:250 정정 | 문서 칸에 코드 인용·코드 칸에 문서 설명 → 두 칸을 교환하고 문서 쪽 명시 | SO1-287, swashuse p.117–118, SwashDecOutQ:201–209, SwashFlobjOutp:85–88. 결론 C와 부유체 수만큼의 열이라는 결론은 유지한다. |

| 삭제된 HEAD 줄 | 보고서 근거와 판정 |
|---|---|
| 7 | apply-7의 대조 반영 기록을 검증 방법에 추가했다. 기존 방법은 유지했다. |
| 17, 24 | SI1-563 §4는 무조건 6DOF라는 설명을 2D의 선택 가능성과 1D의 세 자유도 제한으로 바꾸도록 한다. 새 :18·25–27이 반영한다. |
| 204 | SI1-569 §4는 읽기 기본값·준비 보정·절대·상대 수렴 기준의 추가를 지시한다. SI1-567·568과 SwashComputStruc:92–160으로 FSI 반복·중간 변위·수렴 판정의 미확인이 해소되었다. pship의 사용 인덱스는 새 입력·준비 문장과 본문의 적분·KBC 인용으로 연결된다. |

사용자가 지정한 기계 확인 후보는 이 노트에 없다.
상대 링크 4개의 파일 대상이 존재한다.
절대 경로와 위키 링크 표기는 없다.
미완 항목은 없다.
Mermaid 블록은 없다.
대상 파일의 `git diff --check`는 통과했다.

## swash-turbulence-closure.md — 완료

대조한 추가 줄은 28개다.
삭제 줄은 별도로 4개를 대조했다.
정정은 3줄이다.
보완은 1줄이다.
줄 번호는 이번 검증 전후에 같다.

| 대상 추가 줄 | 대조 근거와 결과 |
|---|---|
| 7–8 | apply-4의 frontmatter 반영 기록과 본문의 소스 인용을 대조했다. |
| 29 | SwashReadInput:1253–1291, SwashPrintSettings:264–279, SwashReynoldsStress:56–64,161–176,245,656과 swashuse p.79–80을 대조했다. 수평 점성 비활성 문구의 선행 조건을 고쳤다. |
| 136–138 | SwashHorzVisc:116–147,217–236, SwashModule1:446–449, SwashReadInput:1288–1291과 SI2-288 §4·§5를 대조했다. 미분형 식에는 dx를 다시 나누지 않는다. |
| 190–191 | SwashHDiffZplane1DH:122–124,140–163,275–298, SwashHDiffZplane2DH:298–319, SwashAntiCreep1DH:119,143–163과 SI2-284를 대조했다. 제한자의 부호 조건을 명시했다. |
| 204–223 | 차이 표 9행의 모든 칸을 최종 보고서 §5의 해당 ID와 대조했다. 모든 현재 코드 인용과 8756667의 과거 인용을 열었다. 빈 줄·제목·표 머리·출처 링크·판본 문장도 포함한다. |

표의 추가 대조는 SwashCheckPrep:712–753,1053, SwashInit:329, SwashVertVisc:56–86, SwashKepsMod1DH:87–88,546–574, SwashReynoldsStress:78–80, SwashUHorzVisc:127–359, misc/swash.edt:199다.
매뉴얼 대조는 swashuse PDF p.34·78–80·86–88·142와 swashtech PDF p.92의 해당 주장이다.
식·숫자·단위는 swashuse p.34·79–80·87–88·142와 swashtech p.92의 쪽 이미지와 대조했다.
차이 표의 결론 분류 9개는 최종 보고서와 같다.
SI2-070의 F는 physics 보고서 끝 전수 검증 기록의 B→F 정정과 일치한다.
8756667:src/SwashKepsMod1DH.ftn90:566에도 cfk 곱이 있으므로 AD의 이력 사실은 유지한다.
A·E 분류 행은 없다.

| 정정·보완 위치 | 전 → 후 | 근거 원문 |
|---|---|---|
| swash-turbulence-closure.md:29 정정 | iturb<2만으로 수평 점성 비활성 문구 출력 → ihvisc가 1·2·3이 아닌 경로의 iturb<2로 한정 | SwashPrintSettings:264–271의 ELSE IF 순서. iturb=1·2·3 선택의 근거도 SwashReadInput:1253–1273으로 맞췄다. ReynoldsStress:245,656은 iturb=3의 비선형 항 분기다. |
| swash-turbulence-closure.md:136 보완 | csmag·lmix의 모듈 입력 설명에 직접 인용 없음 → 선언과 입력 대입 인용 추가 | SwashModule1:446,449는 parameter가 아닌 real 변수다. SwashReadInput:1288,1291에서 입력값을 읽는다. |
| swash-turbulence-closure.md:190 정정 | MUSCL 식의 적용 조건 생략 → 같은 부호 조건·그 밖의 grad=0·끝점 flux=0 명시 | SwashHDiffZplane1DH:280–290,294–298과 SI2-284. 축약 flux는 원문의 곱셈식으로 적었다. 같은 확산계수·상한이라는 설명도 AntiCreep1DH:119,143–163과 대조했다. |
| swash-turbulence-closure.md:218 정정 | 논문 대조를 포함하지 않는다는 한계 문장 → 확인한 표준·비선형 상수값 | SwashVertVisc:56, SwashKepsMod1DH:87–88, SwashReynoldsStress:78–80. swashuse p.79–80은 모델 이름과 관계를 설명한다. 이 행의 C 분류는 유지한다. |

| 삭제된 HEAD 줄 | 보고서 근거와 판정 |
|---|---|
| 7 | apply-4의 대조 반영 기록을 검증 방법에 추가했다. 기존 방법은 유지했다. |
| 28 | apply-4가 이미 해소된 iturb=2 작업 메모를 사실 문장으로 바꿨다. SwashReadInput:1253–1273과 SwashPrintSettings:274–279가 선택과 이름을 확정한다. |
| 135 | SI2-288 §4·§5가 미분형 식의 중복 /dx를 지적한다. 새 :137–138의 차분·미분 구별은 SwashHorzVisc:133,139와 일치한다. 전단 식과 입력 변수 설명은 새 :136에 유지했다. |
| 187 | SI2-284와 apply-4가 2DH 미정독 메모를 원문 flux로 바꾼다. SwashHDiffZplane2DH:315의 식과 새 :191이 일치한다. 1DH flux·확산계수 설명은 새 :190에 유지했다. |

사용자가 지정한 기계 확인 후보는 이 노트에 없다.
상대 링크 5개의 파일 대상이 존재한다.
절대 경로와 위키 링크 표기는 없다.
미완 항목은 없다.
Mermaid 블록은 없다.
대상 파일의 `git diff --check`는 통과했다.

## 최종 집계

| 노트 | 추가 줄 대조 | 삭제 줄 근거 대조 | 정정 | 보완 |
|---|---:|---:|---:|---:|
| swash-initialization-grid.md | 92 | 10 | 10 | 3 |
| swash-bottom-friction-wind.md | 70 | 9 | 6 | 1 |
| swash-floating-rigid-body.md | 50 | 4 | 5 | 3 |
| swash-turbulence-closure.md | 28 | 4 | 3 | 1 |
| 합계 | 240 | 27 | 24 | 8 |

수량의 근거는 작업 시작 시 저장한 네 파일의 `git diff -U0 HEAD` 추가·삭제 줄 목록과 이번 수정 전후의 줄별 비교다.
이번에 바꾼 32줄은 모두 원래 대상 추가 줄 안에 있다.
수정 전후의 각 노트 줄 수는 같다.
기계 확인 후보 18개의 개별 판정을 모두 기록했다.
후보의 인용 불일치 경보는 모두 오판이다.
차이 표 96행의 분류는 최종 보고서와 같다.
상대 링크 33개의 파일 대상이 모두 존재한다.
네 노트의 표 열 구조와 수정 표지를 확인했다.
네 노트의 `git diff --check`가 모두 통과했다.
미해결 항목은 없다.

대조 240, 정정 24, 보완 8
