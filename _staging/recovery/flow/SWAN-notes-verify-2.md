# SWAN 노트 추가 줄 전수 대조 (2026-10-13)

## 대조 범위와 집계 기준

- 작업 시작 시 `git -C /home/firesinger/coastal-wiki diff -U0 HEAD -- <노트>`에서 `+++` 파일 머리말을 제외한 모든 `+` 줄을 고정했다.
- `swan-foundation.md`의 대상은 207줄이다. 시작 시 줄 번호는 6–7, 28, 32–34, 60, 68, 161, 186, 224, 226–421이다.
- `swan-nesting-io-implementation.md`의 대상은 24줄이다. 시작 시 줄 번호는 6, 11, 34–36, 46–47, 69, 95, 102, 112, 114, 133–144이다.
- 위 수에는 frontmatter, 빈 줄, 제목, 표 구분선, mermaid 문법 줄을 포함했다.
- 정정 수와 보완 수는 각각 해당 표지를 붙인 대상 줄 수로 센다. 같은 대상 줄의 여러 수정은 한 줄로 센다.
- 원문은 지정된 로컬 코드, 과거 커밋의 파일, HTML, PDF를 사용한다. 결론은 지정된 보고서의 최종 `[10-13 ...]` 판정과 대조한다.

## 진행 기록

| 노트 | 대상 + 줄 수 | 상태 | 정정 수 | 보완 수 |
|---|---:|---|---:|---:|
| [swan-foundation.md](../../../models/SWAN/source-analysis/swan-foundation.md) | 207 | 완료 | 14 | 17 |
| [swan-nesting-io-implementation.md](../../../models/SWAN/source-analysis/swan-nesting-io-implementation.md) | 24 | 완료 | 4 | 7 |

## swan-foundation.md — 완료

작업 시작 시의 추가·수정 207줄을 모두 대조했다. 정정은 14줄이다. 보완은 17줄이다. 이 수는 아래 목록의 구분 열을 센 값이다. 수정은 기존 줄 안에서 처리했으므로 완료 시의 대상 줄 번호도 시작 시와 같다.

### 대조 범위별 결과

| 대상 줄 | + 줄 수 | 원문 대조 결과 |
|---|---:|---|
| 6–7 | 2 | frontmatter의 YAML 형식을 확인했다. 검증 방법을 이번 실제 대조 범위로 바꿨다. 반영일은 SWAN-notes-apply-4.md의 작성일과 같다. |
| 28, 32–34 | 4 | 원문 경로와 상대 링크를 확인했다. swanmain.ftn:965–968의 버전·패치 선언을 확인했다. git show의 커밋 날짜·제목으로 HEAD와 실제 patch B를 구별했다. |
| 60, 68, 161 | 3 | 기본 전파법과 국소 전환 조건을 코드와 R1·R5에 대조했다. 정렬 격자라는 적용 범위를 복원했다. |
| 186, 224 | 2 | SWOMPU와 SwanCompUnstruc의 역할은 R8 §2와 같다. 반영 기록은 SWAN-notes-apply-4.md:26,66,81과 같다. |
| 226–276 | 51 | 시작·명령 읽기·시간 단계·종료 그림의 모든 상자 위치와 연결을 swanmain.ftn, swanpre1.ftn, ocpmix.ftn, bin/swanrun에 대조했다. 중첩 IF와 surfbeat 조건을 복원했다. |
| 277–321 | 45 | 정렬 그림의 모든 상자 위치와 연결을 swancom1.ftn에 대조했다. 3463행의 GOTO 333과 3542행의 GOTO 330이 초기 추정 전후의 SWTRCF 순서를 설명한다. !WFR!MPI와 !JAC 경로를 구별했다. |
| 322–365 | 44 | 비정렬 그림의 모든 상자 위치와 연결을 SwanCompUnstruc.ftn90에 대조했다. 1007행의 goto 20과 1075행의 goto 10이 초기 추정 전후의 SWTRCF 순서를 설명한다. !GRAPH·!FXFRO·!METIS 조건을 확인했다. |
| 366–411 | 46 | 결함 후보 39행의 분류·강도를 R1–R7 §5, R8 §8 및 SWAN-git-verify-E.md:23–61에 대조했다. 강함 31행·중간 7행·약함 1행을 유지했다. 인용한 현재·과거 코드, PDF 식·단위·쪽, 로컬 웹 원문을 대조했다. |
| 412–421 | 10 | 차이 표의 R4:T1-039는 B이다. R5:PN-099는 C이다. R8:T1-001은 B이다. 명령 반복·300개 상한·INIT 조건과 PDF·HTML 인용을 확인했다. |

위 범위표의 + 줄 수 합계는 207이다. 제목·빈 줄·표 구분선·mermaid 문법 줄도 각 범위의 집계에 포함했다. 대상 행 ID에는 A 분류가 없다. 과거 커밋은 지정된 원본 저장소에서 읽기 전용 git show로 열었다. git log 검색 결과에 대한 노트의 서술은 SWAN-git-verify-E.md의 해당 행과 대조했다.

PDF 대조에는 swantech의 1·30·41·63·70·90–91·112–114·121–122·125쪽과 swanuse의 1·19·33·40·56–58·61·64·84–85·94·102·112·114·116–117·120·126–127·132·142·151쪽을 사용했다. swanimp와 swanpgr의 판 표기는 각각 PDF 1쪽에서 대조했다. 본문에서 쓰는 PDF 쪽과 인쇄 쪽을 구별했다.

### 정정·보완 목록

위치는 저장 완료 시의 줄 번호이다. 코드 원문 위치는 `models/SWAN/raw/source_code/swan/`를 기준으로 한다. R 번호는 사용자가 지정한 대조 보고서를 뜻한다.

| 노트:줄 | 구분 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| `swan-foundation.md:6` | 정정 | 2026-07-17의 코퍼스·검색 청크 설명을 현재 verification_method에 유지 | 이번 대조의 기준 diff·범위·원문 종류를 명시 | 최초 diff의 + 줄 207개; SWAN-notes-apply-4.md:26,66,81; 본 검증 기록 |
| `swan-foundation.md:32` | 정정 | manuals 검색 컬렉션의 약 902청크를 Source basis로 제시 | 현재 대조한 원문 파일과 코드·웹 인용 기준을 명시 | 지정된 로컬 PDF 4종의 파일 존재; 로컬 HTML 195파일; R8 판독 기준 |
| `swan-foundation.md:68` | 보완 | PROPSL = 1만 인용; 비정렬·PROP BSBT 근거 위치 생략 | 국소 전환 조건문과 비정렬 호출·PROP BSBT 대입 위치를 인용 | src/swancom1.ftn:3135–3141,3229–3233; src/SwanTranspAc.ftn90:129; src/SwanTranspX.ftn90:43; src/swanpre1.ftn:793–795; src/swanmain.ftn:4090–4095 |
| `swan-foundation.md:161` | 정정 | 정상 계산의 기본 전파법 | 정렬 격자 정상 계산의 기본 전파법 | src/swanmain.ftn:1179; src/SwanTranspX.ftn90:43,126–150; R1 TN-046 |
| `swan-foundation.md:236` | 보완 | SWMAIN 호출 위치 생략 | SWMAIN 호출 115행 추가 | src/swanmain.ftn:115 CALL SWMAIN; :384 CALL SWINIT (INERR) |
| `swan-foundation.md:237` | 보완 | SWREAD 호출 위치 생략 | SWREAD 호출 399행 추가 | src/swanmain.ftn:399 CALL SWREAD (COMPUT) |
| `swan-foundation.md:247` | 정정 | SWINCO는 ICOND.EQ.1 | NSTATC.EQ.1 내부의 ICOND.EQ.1로 호출 조건 명시 | src/swanmain.ftn:544–551의 중첩 IF; :561 IT0 = 1 |
| `swan-foundation.md:250` | 정정 | COMPUT.NE.#quot;NOCO#quot; | 원문의 작은따옴표 NOCO로 복원 | src/swanmain.ftn:610 IF (COMPUT.NE.'NOCO' .AND. IT.GT.0) THEN |
| `swan-foundation.md:254` | 정정 | BNDCHK·LSRFB 조건 | HSOBND와 IEM 조건 구별; ntf.LT.0 복원 | src/swanmain.ftn:640 IF ( BNDCHK ) THEN; :646 IF ( LSRFB .AND. ntf.LT.0 ) THEN |
| `swan-foundation.md:261` | 보완 | STOP 대입 줄까지만 인용 | RETURN 504행 추가 | src/swanpre1.ftn:504 RETURN |
| `swan-foundation.md:262` | 보완 | NOCO 대입 줄만 인용 | RETURN 504행 추가 | src/swanpre1.ftn:502 COMPUT = 'NOCO'; :504 RETURN |
| `swan-foundation.md:264` | 정정 | SWMAIN 정상 종료 처리 | 정상 STOP과 오류 분기가 공유하는 종료 정리로 명명 | src/swanmain.ftn:411 GOTO 900; :699 IF (LEVERR.GT.MAXERR) GOTO 900; :705 900 CONTINUE |
| `swan-foundation.md:274` | 보완 | 판정 함수 본문만 인용 | SWINITMPI 뒤의 STPNOW 호출 위치 추가 | src/swanmain.ftn:111 IF (STPNOW()) GOTO 999; src/ocpmix.ftn:1482–1488 |
| `swan-foundation.md:284` | 정정 | SWCOMP의 위치 swancom1.ftn:941 | 실제 호출 위치 swanmain.ftn:620 | src/swancom1.ftn:941은 STRACE 호출; src/swanmain.ftn:620은 CALL SWCOMP |
| `swan-foundation.md:290` | 정정 | !WFR | !WFR!MPI | src/swancom1.ftn:1964,1968의 원문 접두사 !WFR!MPI |
| `swan-foundation.md:329` | 정정 | SwanCompUnstruc.ftn90:319 | 실제 호출 위치 swanmain.ftn:625 | src/SwanCompUnstruc.ftn90:319는 strace 호출; src/swanmain.ftn:625는 CALL SwanCompUnstruc |
| `swan-foundation.md:363` | 보완 | PLTSRC 호출 위치만 인용 | 루틴 종료 1678행 추가 | src/SwanCompUnstruc.ftn90:1620 call PLTSRC; :1678 end subroutine SwanCompUnstruc |
| `swan-foundation.md:369` | 보완 | P·A·M 정의 없음 | 세 웹 원문의 상대 링크와 줄 번호 기준 추가 | SWAN-git-verify-E.md:13의 P·A·M 정의; 로컬 파일 존재 |
| `swan-foundation.md:374` | 보완 | 식 (3.85)와 i·k 범위를 PDF 121쪽만 인용 | i=1,2 및 k=0,1이 이어지는 PDF 122쪽 추가 | swantech PDF 121쪽 식 (3.85); PDF 122쪽 첫 문장 with i=1,2 ... and k=0,1 |
| `swan-foundation.md:382` | 정정 | 식은 −u(x,y) | 창 함수를 곱하기 전 유속 차이는 −u(x,y) | swantech PDF 113쪽의 Δu 식에는 W(x′)W(y′)가 있다; src/SwanQCM.ftn90:1097–1098의 차분 뒤 :1105에서 tukeywin 호출 |
| `swan-foundation.md:384` | 보완 | swantech PDF 63쪽으로 파고비 정의를 설명 | 자유고 배율과 명시적인 파고비 정의의 출처를 구별 | swantech PDF 63쪽 §2.5.3; swanuse PDF 84쪽 [reflc] 정의 |
| `swan-foundation.md:388` | 보완 | 114쪽 | swantech PDF 114쪽 / 인쇄 106쪽 | swantech PDF 114쪽 second order central differences; swantech PDF 112쪽은 비정상에 Stelling and Leendertse를 권고 |
| `swan-foundation.md:389` | 보완 | (2.149)의 분산 관계 | 책·PDF 쪽·인쇄 쪽 추가 | swantech PDF 70쪽 / 인쇄 62쪽 식 (2.149) |
| `swan-foundation.md:390` | 보완 | (3.45)의 이동량 | 책·PDF 쪽·인쇄 쪽 추가 | swantech PDF 113쪽 / 인쇄 105쪽 식 (3.45)의 kx−qx/2, ky−qy/2 |
| `swan-foundation.md:395` | 보완 | 노트 안에 없는 T1-085를 참조 | Appendix B의 실제 쪽과 원문 구절을 명시 | swanuse PDF 132쪽의 숫자 변수 이름 지정 규칙 |
| `swan-foundation.md:397` | 보완 | PN-084의 위치 생략 | 해당 결론 표의 상대 링크 추가 | R5:405 PN-084; src/swanpre1.ftn:1948–1949 |
| `swan-foundation.md:405` | 정정 | PDF 117쪽에 없는 absolute frequency spectrum을 직접 인용 | PDF 117쪽의 ABS 설명을 그대로 인용 | swanuse PDF 117쪽 / 인쇄 109쪽 ABS 설명 |
| `swan-foundation.md:408` | 보완 | O-137의 위치 생략 | 해당 결론 표의 상대 링크 추가 | R6:500 O-137; src/swanout1.ftn:2417의 JTURB2 출력 |
| `swan-foundation.md:415` | 정정 | 전체 매뉴얼을 41.51로 묶음; HEAD와 patch B를 한 구절로 표기 | swanpgr Version 1.3과 나머지 PDF 41.51을 구별; 병합 HEAD와 실제 patch B 커밋을 구별 | git show -s: 43e9bbb Merge branch ...; 0dabfa4 updated src (patch B); 두 날짜 2026-07-13; swantech·swanuse·swanimp PDF 1쪽은 41.51; swanpgr PDF 1쪽은 Version 1.3 |
| `swan-foundation.md:419` | 정정 | COMPUTE 뒤 무시 설명에서 HOTFILE·STOP 예외 생략 | 예외 구절을 원문대로 복원 | swanuse PDF 33쪽 / 인쇄 25쪽; W/online_doc/swanuse/node21.html:53–54 |
| `swan-foundation.md:420` | 보완 | unless a command INIT appears | 두 COMPUTE 사이의 INIT라는 원문 조건까지 인용 | swanuse PDF 120쪽 / 인쇄 112쪽; W/online_doc/swanuse/node34.html:102–104 |

### 기계 확인 후보 판정

- `swan-foundation.md:384`의 BAD `src/swanser.ftn:4157`은 오판이다. `b2ae30e:src/swanser.ftn:4157–4161`에는 제곱 없는 REF0 식과 `!         >>> should REF0 not be squared? <<<`가 있다. 한국어 설명을 인용문으로 잘못 짝지은 후보이다. 해당 코드 인용은 유지했다.
- `swan-foundation.md:385`의 BAD `src/swanpre1.ftn:1200`은 오판이다. `b2ae30e:src/swanpre1.ftn:1200–1208`의 음수 검사와 GAMT·GAMR 배타 분기는 `7ee8981`·`43e9bbb`의 1217–1225행과 같다. 접속어 `과`는 인용문이 아니다. 노트는 유지했다.
- `swan-foundation.md:386`의 BAD `src/swancom5.ftn:5658`은 오판이다. `7ee8981:src/swancom5.ftn:5658–5665`에는 MSC 조건과 두 CKTAIL 합이 그대로 있다. 쉼표는 인용문이 아니다. 노트는 유지했다.

추가 자동 후보인 393·394·395행의 `\|`는 Markdown 표 구분자 이스케이프이다. 원문에는 `|`가 있다. 이스케이프를 해제한 인용은 원문과 일치하므로 유지했다.

### 완료 확인

추가·수정 줄의 상대 링크가 가리키는 파일은 모두 존재한다. 절대 홈 경로와 이중 대괄호는 없다. 사용자가 금지한 한계 문장은 없다. 코드 인용의 스위치 표지와 줄 끝 판 번호는 원문과 같다. 정정·보완 뒤에도 최초 대상 207줄은 모두 diff의 + 줄이다. 이 노트의 미해결 항목은 0개이다.

## swan-nesting-io-implementation.md — 완료

작업 시작 시의 추가·수정 24줄을 모두 대조했다. 정정은 4줄이다. 보완은 7줄이다. 이 수는 아래 목록의 구분 열을 센 값이다. 수정은 기존 줄 안에서 처리했으므로 완료 시의 대상 줄 번호도 시작 시와 같다.

### 대조 범위별 결과

| 대상 줄 | + 줄 수 | 원문 대조 결과 |
|---|---:|---|
| 6, 11 | 2 | frontmatter의 YAML 형식을 확인했다. 검증 방법을 이번 실제 대조 범위로 바꿨다. 반영일은 SWAN-notes-apply-6.md와 같다. |
| 34–36 | 3 | UF는 UNKNOWN·FORMATTED이다. 이미 열린 파일의 unit 재사용 분기와 OPEN 지정자를 src/ocpmix.ftn:1778–1800,1820–1847,1869–1873에서 확인했다. |
| 46–47 | 2 | UF의 문자열 정의를 확인했다. NINT 반올림은 src/swanser.ftn:5575의 ASCII writer에 한정했다. |
| 69, 95 | 2 | CGRID의 MDC·FLOW·FHIGH·MSC 입력을 확인했다. 과거 2980d1a:src/swanpre1.ftn:2123–2166과 현재 2169–2213의 SET 분기를 대조했다. R4:T1-300과 SWAN-git-verify-D의 결론은 D이다. |
| 102, 112, 114 | 3 | 반복된 UF 설명과 파일 재사용 설명에도 실제 정의·분기 위치를 보탰다. |
| 133–144 | 12 | 문서·코드 판과 표 구조를 확인했다. R6의 최종 O-010·O-011·O-028·N-009는 B이다. O-012는 E·강함이다. 결론 문장과 범위를 유지했다. |

위 범위표의 + 줄 수 합계는 24이다. 제목·빈 줄·표 구분선도 각 범위의 집계에 포함했다. 대상 줄에는 mermaid 상자가 없다. 대상 행 ID에는 A 분류가 없다. NGRID의 입력 분기는 src/swanpre2.ftn:785–1008 전체로 확인했다. PDF 인용은 swanuse의 96·101·102·118쪽과 대조했다. PDF 쪽과 인쇄 쪽은 각각 96/88·101/93·102/94·118/110이다. 문서 판은 swanuse PDF 1쪽에서 확인했다.

### 정정·보완 목록

코드 원문 위치는 `models/SWAN/raw/source_code/swan/`를 기준으로 한다. R 번호는 사용자가 지정한 대조 보고서를 뜻한다.

| 노트:줄 | 구분 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| `swan-nesting-io-implementation.md:6` | 정정 | 과거 마이그레이션 설명을 verification_method에 유지 | 이번 검증의 실제 범위와 원문 종류를 명시 | 최초 diff의 + 줄 24개; SWAN-notes-apply-6.md:34; 본 검증 기록 |
| `swan-nesting-io-implementation.md:36` | 보완 | 파일 재사용 문장에 직접 인용 없음 | OPENED 분기와 OPEN 지정자를 인용 | src/ocpmix.ftn:1820–1847,1869–1873; SWSPEC의 src/swanout2.ftn:1895–1901 |
| `swan-nesting-io-implementation.md:46` | 보완 | UF 문자 인덱스만 인용 | UNKNOWN·FORMATTED 문자열 정의 추가 | src/ocpmix.ftn:1778–1779의 FISTAT·FORM DATA |
| `swan-nesting-io-implementation.md:47` | 정정 | 밀도 표는 NINT | WRSPEC의 ASCII 밀도 표로 범위를 한정 | src/swanser.ftn:5571–5575; src/swanout2.ftn:1880–1885는 NetCDF 별도 경로 |
| `swan-nesting-io-implementation.md:69` | 보완 | 지원하지 않는 SET 선택의 과거 코드만 인용 | 현재 SET 분기와 D 확정 보고서 링크 추가 | 2980d1a:src/swanpre1.ftn:2123–2166; 현재 src/swanpre1.ftn:2169–2213; R4:348 T1-300 |
| `swan-nesting-io-implementation.md:95` | 보완 | 주파수·방향 격자 설명에 MDC만 인용 | FLOW·FHIGH·MSC 입력 근거 추가 | src/swanpre1.ftn:1730,1739–1741 |
| `swan-nesting-io-implementation.md:102` | 보완 | UF 문자 인덱스만 인용 | UNKNOWN·FORMATTED 문자열 정의 추가 | src/ocpmix.ftn:1778–1779의 FISTAT·FORM DATA |
| `swan-nesting-io-implementation.md:112` | 보완 | UF 문자 인덱스만 인용 | UNKNOWN·FORMATTED 문자열 정의 추가 | src/ocpmix.ftn:1778–1779의 FISTAT·FORM DATA |
| `swan-nesting-io-implementation.md:114` | 보완 | 파일 재사용의 근거로 UF 인덱스만 제시 | 실제 OPENED·unit 대입과 OPEN 위치를 제시 | src/ocpmix.ftn:1842–1847,1869–1873 |
| `swan-nesting-io-implementation.md:143` | 정정 | SWCMSP가 VaDens/EnDens를 기록한다고 설명 | SWSPEC의 이름 기록과 SWCMSP의 값 계산을 구별 | src/swanout2.ftn:1719,1965,1971,2082,2277; R6:247 O-100 |
| `swan-nesting-io-implementation.md:144` | 정정 | 현재 노트 줄 번호처럼 남은 이전 문장 인용; unit 근거 생략 | 수정 전 인용임을 명시; 실제 unit 재사용 분기 추가 | 최초 git diff의 삭제 줄 33·110; R6:512 N-009; src/ocpmix.ftn:1842–1847,1869–1873 |

### 기계 확인 후보 판정

- `swan-nesting-io-implementation.md:142`의 BAD `src/swanpre2.ftn:839`은 오판이다. `b2ae30e:src/swanpre2.ftn:839`에는 `READ(NDS, 100, END=950, ERR=910) XG(I),YG(I),VM(I)`가 있다. `7ee8981`과 `43e9bbb`의 839행도 같다. 한국어 설명 `에 같은 READ가 있다.`를 인용문으로 잘못 짝지은 후보이다. 노트는 유지했다.

### 완료 확인

추가·수정 줄의 상대 링크가 가리키는 파일과 Markdown 절이 모두 존재한다. 절대 홈 경로와 이중 대괄호는 없다. 사용자가 금지한 한계 문장은 없다. 정정·보완 뒤에도 최초 대상 24줄은 모두 diff의 + 줄이다. 이 노트의 미해결 항목은 0개이다.

## 전체 집계

두 노트의 추가·수정 231줄을 모두 대조했다. 이 수는 최초 diff의 207줄과 24줄의 합이다. 정정은 18줄이다. 보완은 24줄이다. 이 수는 각 노트의 수정 목록과 줄 끝 표지를 각각 합산한 값이다. 기계 확인 후보 4건은 모두 원문과 일치하므로 오판으로 판정했다. 미해결 항목은 0개이다.
