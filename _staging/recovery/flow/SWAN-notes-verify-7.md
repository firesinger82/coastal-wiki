# SWAN 노트 추가 줄 전수 검증 7

- 검증일: 2026-10-13.
- 대상은 사용자가 지정한 노트 6개의 `git diff -U0 HEAD -- <노트>` 추가 줄이다.
- 검증 시작 시 추가 줄을 기준으로 센다. Frontmatter와 빈 줄도 포함한다.
- 현재 소스, 과거 커밋 소스, 로컬 웹 문서, PDF와 결론 근거 보고서의 최종 판정을 대조한다.
- 노트별 완료 기록에는 대조한 추가 줄 수, 정정 수, 보완 수와 변경 근거를 적는다.
- 정정 수와 보완 수는 표지를 붙여 수정한 노트 줄 수로 센다.
- 노트별 완료 기록이 있는 대상만 다음 재개에서 건너뛴다.

## 완료 기록

### 1. swan-command-physics-reference.md — 완료

- 노트: `models/SWAN/manual-notes/swan-command-physics-reference.md`.
- 시작 시 추가 줄 104개를 모두 대조했다. 정정 2줄, 보완 0줄이다.
- 대조 범위: 7–8, 22, 29–30, 33–35, 44, 52–53, 62, 69–70, 80, 91, 98, 101–102, 112–113, 121–123, 125–129, 143, 147, 149, 151, 155–225행.
- R3:NT-047과 R5 차이 표의 분류·결론은 보고서 최종본과 일치했다. PN-061은 git E 판정과도 일치했다. PN-064의 2023-10-16 삭제는 `24a7d67`의 원문 diff로 확인했다.
- swanuse PDF 65–91·137–140쪽의 인용을 대조했다. 회절 평활화의 음수 부호는 PDF 87쪽 이미지에서도 확인했다. swantech PDF 29–36쪽과 웹 node28·node21의 지정 줄도 대조했다.
- Frontmatter의 node28.md 1577줄은 파일의 개행 수와 일치한다. 마지막 개행 없는 줄을 포함한 논리적 줄 수는 1578개이다. ASTD 관련 원천항 파일의 검색 결과는 0건이다. CASTD의 대입·선언 위치도 확인했다.
- 실제 Markdown 상대 링크는 14개 대상에 연결된다. 인라인 식 `cos[pown](θ − θrefl)`은 링크가 아니다. 금지 경로·위키 링크·지정 한계 문장은 없다. 추가 줄에 Mermaid 도표는 없다.

| 노트:줄 | 구분 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| `swan-command-physics-reference.md:128` | 정정 | `1D infragravity (Reniers IEM)` | IEM 활성화와 1D·곡선·비구조 격자 사용 금지를 명시했다. | swanuse PDF 88쪽 / 인쇄 80쪽: `CANNOT BE USED IN CASE OF CURVILINEAR or UNSTRUCTURED GRIDS AND NOT IN 1D-MODE.` R5:PN-073도 같은 실행 조건이다. |
| `swan-command-physics-reference.md:143` | 정정 | `gamma=0.73 = Eq 2.68 Battjes-Stive` | 0.73의 근거를 PDF 36쪽의 관측 자료 평균으로 고쳤다. 식 (2.68)을 쇄파 소산식으로 구분했다. | swantech PDF 36쪽 / 인쇄 28쪽: `with an average of 0.73`. 식 (2.68)은 PDF 35쪽 / 인쇄 27쪽이다. KOMEN 계수는 PDF 30쪽 / 인쇄 22쪽의 `Cds = 2.36 × 10⁻⁵`이다. |

기계 확인 후보: 이 노트에 지정된 후보는 없다.

### 2. swan-diffraction-obstacles.md — 완료

- 노트: `models/SWAN/source-analysis/swan-diffraction-obstacles.md`.
- 시작 시 추가 줄 69개를 모두 대조했다. 정정 11줄, 보완 6줄이다.
- 대조 범위: 6–7, 20–25, 29, 37, 39, 42–43, 46, 48–50, 58, 65, 69–73, 79, 83, 87, 94, 100, 104, 111–112, 115, 124, 131, 135, 137, 142, 149–152, 160, 163–164, 171–172, 193–214행.
- R3의 CP·NT 행과 R5:PN-183·186을 최종 결론과 대조했다. CP-003·004·007의 E 분류와 강도를 유지했다. PN-183에서 빠진 마지막 결론 문장을 복원했다.
- swantech PDF 62–65쪽과 swanuse PDF 83–84·88쪽을 대조했다. 식 (2.138)의 분모는 PDF 64쪽 이미지에서도 확인했다. 웹 node28의 반사 분포·에너지 합 검사와 node29의 회절식을 확인했다.
- Frontmatter의 날짜와 대조 이력을 확인했다. 상대 링크의 대상 파일이 존재한다. 금지 경로·위키 링크·지정 한계 문장은 없다. 추가 줄에 Mermaid 도표는 없다.

| 노트:줄 | 구분 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| `swan-diffraction-obstacles.md:20` | 보완 | DIFFRAC 범위 `2106–2114` | `2106–2120` | `swanpre1.ftn:2115–2118`이 IDIFFR·SMPAR·SMNUM·CGMOD를 읽는다. |
| `swan-diffraction-obstacles.md:22` | 보완 | 속도·평활화 범위가 1608·5717행에서 끝났다. DIFPARAM은 5881행을 가리켰다. | 속도 1606–1631, 평활화 5527–5775, DIFPARAM 5883–5893행을 포함했다. | `swancom5.ftn:1608–1610`의 CAD, 5722–5773행의 이웃 기여, 5892행의 제곱근 대입. |
| `swan-diffraction-obstacles.md:24` | 정정 | `SwanPrepComp:87`, `SwanPropvelX:92`, `SwanPropvelS:269` | 각각 90, 94–98, 270행 | `call SwanFindObstacles ( cross )`; `cax/cay`의 DIFPARAM 곱셈; `if ( IDIFFR /= 0 ) cad...`. |
| `swan-diffraction-obstacles.md:25` | 보완 | `6394–6455` | `6394–6457` | `swanmain.ftn:6457` `IDIFFR = 0`. |
| `swan-diffraction-obstacles.md:29` | 정정 | 구문 근거 `swanpre1.ftn:2106` | `2110–2118` | 2106행은 절 제목이다. 구문은 2110행이고 인수 판독은 2115–2118행이다. |
| `swan-diffraction-obstacles.md:39` | 보완 | eikonal 근거 `44–60` | `44–68` | `SwanDiffPar.ftn90:66–68`의 `delta` 분수와 `k^2 pH`. |
| `swan-diffraction-obstacles.md:46` | 정정 | 무조건 `SQRT(1 + δ)`, 근거 5532·5881행 | TMP가 −1 미만이면 0을 대입한다. 나머지에서 제곱근을 계산한다. | `swancom5.ftn:5889–5892` `IF (TMP.LT.-1.) THEN`, `DIFPARAM(IND) = 0.`, `DIFPARAM(IND) = SQRT(1.+TMP)`. |
| `swan-diffraction-obstacles.md:58` | 정정 | 평활화 식 근거 `5527` | `5529–5530` | `Effectively, E(i,j) = (1-4*alpha) * E(i,j) +`로 시작하는 식. |
| `swan-diffraction-obstacles.md:69` | 보완 | OBSTACLE 구문 `944–958` | `944–964` | `swanpre1.ftn:959`에 `REFLec [reflc]`가 있다. |
| `swan-diffraction-obstacles.md:87` | 정정 | `PRDIF(0)=1` 근거 `3655` | 분기와 대입 `3655–3658` | `swanser.ftn:3658` `PRDIF(0) = 1.`. |
| `swan-diffraction-obstacles.md:104` | 정정 | `Reflection code warns`, 근거 `3611–3619` | 소스 주석의 교차점 제한·모서리 권고, 근거 `3619–3620` | `There should be only one intersection per computational gridcell.` 다음 줄이 sharp edges 권고이다. |
| `swan-diffraction-obstacles.md:111` | 정정 | SwanFindObstacles 호출 `87` | 호출 `90` | `SwanPrepComp.ftn90:90` `call SwanFindObstacles ( cross )`. |
| `swan-diffraction-obstacles.md:124` | 정정 | CAX/CAY 곱셈 `1077–1082` | 적용 조건과 두 대입 `1079–1083` | `IF (IDIFFR.EQ.1 .AND. PDIFFR(3).NE.0.) THEN`. CAY 대입은 1083행이다. |
| `swan-diffraction-obstacles.md:131` | 정정 | SwanTranspAc 근거 `777–1077` | 실제 전달 구간 `1080–1085` | `SwanCompUnstruc.ftn90:1080` `call SwanTranspAc`; 1081행 인수 `cax, cay, cad, cas`. |
| `swan-diffraction-obstacles.md:137` | 보완 | 상태 근거 `swmod2:1325`, `SwanDiffPar:174–204` | 배열 선언 1325–1331과 파고·평균값 대입 174–208행 | `hs(ivert) = 4.*sqrt(etot)`, `k (ivert) = ktot/etot`, `cg(ivert) = ctot/etot`. |
| `swan-diffraction-obstacles.md:171` | 정정 | 여러 교차에서 `warns and may misbehave` | 주석의 사용 제한과 매뉴얼의 탐지 불가 설명 | `swanser.ftn:3619–3620`은 주석이다. swanuse PDF 83쪽 / 인쇄 75쪽: `SWAN is not able to detect this`. |
| `swan-diffraction-obstacles.md:214` | 정정 | PN-183 결론의 마지막 문장 생략 | `BREAKING과 FREEBOARD의 누락 인수도 보충한다.` 복원 | R5 최종 §5 PN-183의 마지막 문장. |

| 기계 확인 후보 | 판정 |
|---|---|
| `src/swanser.ftn:4157` / `에도 제곱 없는 식과 의문 주석이 있다.` | 오판이다. 노트 202행은 현재 코드가 아니라 `b2ae30e:src/swanser.ftn:4157–4161`을 인용한다. 해당 커밋에는 REF0 식과 `should REF0 not be squared?` 주석이 있다. 노트를 유지했다. |
| `src/swanpre1.ftn:1200` / `과` | 오판이다. 노트 203행의 `b2ae30e:src/swanpre1.ftn:1200–1208`에는 음수 검사와 GAMT·GAMR의 배타적인 ELSEIF 분기가 있다. 현재 코드의 1217–1225행과 대응한다. 노트를 유지했다. |
| `src/swancom5.ftn:5658` / `,` | 오판이다. 노트 205행의 `7ee8981:src/swancom5.ftn:5658–5665`에는 MSC 조건과 두 CKTAIL 꼬리 합이 있다. 구두점은 코드 인용이 아니다. 최초 반입과 현재 코드에도 같은 합이 있다. 노트를 유지했다. |

### 3. wave/swan-source-terms-implementation.md — 완료

- 노트: `models/SWAN/source-analysis/wave/swan-source-terms-implementation.md`.
- 시작 시 추가 줄 46개를 모두 대조했다. 정정 1줄, 보완 2줄이다.
- 대조 범위: 6, 11, 42, 47, 102, 107–114, 130, 138–139, 203, 205–206, 212, 218–219, 226, 255–277행.
- R2·R5·R7·R8의 해당 행 분류와 최종 결론을 대조했다. SS-362의 인용 범위만 원문에 맞게 고쳤다. 보고서 최종본의 같은 범위에도 양의 분기 1539–1541행이 빠져 있다.
- swantech PDF 26·34–35·38·96쪽과 swanuse PDF 72–74·77·79·81·139쪽의 해당 문장을 대조했다. 웹의 DIA·마찰·진흙·난류 설명도 대조했다.
- A 행 H-755는 git A 판정과 일치한다. `122b595`의 7547·3742행을 직접 읽었다. `git show -s`의 날짜는 `122b595 2023-02-28`, `43e9bbb 2026-07-13`이다. 40.31의 변경은 웹 616·645–654행의 기록이다.
- Frontmatter의 날짜와 반영 이력을 확인했다. 상대 링크 8개 대상이 존재한다. 금지 경로·위키 링크·지정 한계 문장은 없다. 추가 줄에 Mermaid 도표는 없다.

| 노트:줄 | 구분 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| `wave/swan-source-terms-implementation.md:42` | 보완 | SOURCE의 이름을 7543행의 3파 주석만으로 인용했다. | 루틴 선언 6823행을 추가했다. | `swancom1.ftn:6823` `SUBROUTINE SOURCE (ITER ...`. |
| `wave/swan-source-terms-implementation.md:226` | 보완 | 소스 목록의 SOURCE 근거가 7543행뿐이었다. | 루틴 선언 6823행을 추가했다. | `swancom1.ftn:6823` `SUBROUTINE SOURCE (ITER ...`. |
| `wave/swan-source-terms-implementation.md:266` | 정정 | 양·음의 SFNL 처리를 `1542–1546`행으로 인용했다. | `1539–1546`행으로 고쳤다. | `swancom4.ftn:1539` `IF (SFNL(I,ID).GT.0.) THEN`; 1540행은 IMATRA 가산이다. 1542행부터는 ELSE 분기이다. |

| 기계 확인 후보 | 판정 |
|---|---|
| `website/modifications/modifications.htm:219` / 빠른 DIA 문장 | 오판이다. HTML 219–227행을 태그 제거·공백 연결 후 대조하면 노트 275행의 인용 전체와 일치한다. 219는 시작 줄이다. 노트를 유지했다. |
| `website/modifications/modifications.htm:755` / limiter 문장 | 오판이다. HTML 755–777행을 태그 제거·공백 연결 후 대조하면 노트 276행의 인용 전체와 일치한다. 755는 시작 줄이다. 노트를 유지했다. |

### 4. swan-command-file-reference.md — 완료

- 노트: `models/SWAN/source-analysis/swan-command-file-reference.md`.
- 시작 시 추가 줄 43개를 모두 대조했다. 정정 2줄, 보완 2줄이다.
- 대조 범위: 6–7, 36–39, 58, 73, 165, 201–202, 209–210, 218–219, 221, 263, 265–290행.
- PROJECT의 네 줄 구문은 `swanpre1.ftn:513–534`의 구문 주석·NWLINE·문자열 판독과 일치한다. 마찰값 0.038과 입력장 목록도 현재 입력기와 대조했다.
- R4·R5의 분류와 최종 결론을 대조했다. D 행 T1-300·PN-176은 git D 판정과 일치한다. `2980d1a`의 SET 전체 분기와 ST6 2936행을 읽었다. 현재 SET 2169–2213행과 ST6 2983행도 읽었다.
- swanuse PDF 29·34쪽과 swanimp PDF 27쪽의 파일 이름·unit 인용을 대조했다. 웹 swanimp/node19.html:67의 99999도 일치한다.
- Frontmatter와 Review status의 반영 이력을 확인했다. 상대 링크 2개 대상이 존재한다. 금지 경로·위키 링크·지정 한계 문장은 없다. 추가 줄에 Mermaid 도표는 없다.

| 노트:줄 | 구분 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| `swan-command-file-reference.md:202` | 정정 | 천수·쇄파대에 `MSC=36+`, `MDC=36+`를 권고했다. | 근거 없는 수량 권고를 제거했다. 물리 명령의 원문 쪽을 붙였다. | swanuse PDF 73·75쪽 / 인쇄 65·67쪽의 BREAKING·TRIAD 구문. R5:PN-176은 같은 명령 선택을 제시한다. 두 최소 격자 수는 해당 원문과 최종 보고서에 없다. |
| `swan-command-file-reference.md:218` | 보완 | MODE의 모순된 재지정 오류를 COMPUTE 분기로만 인용했다. | MODE 검사 741–751행을 추가했다. | `swanpre1.ftn:741` `IF (NSTATM.EQ.0) CALL MSGERR (2, 'Mode Nonst incorrect here')`; 750행의 반대 검사. |
| `swan-command-file-reference.md:219` | 보완 | 시작 시각 복원의 근거가 조건문 899행뿐이었다. | 오류와 복원 대입 900–901행을 추가했다. | `swanpre1.ftn:900` `CALL MSGERR (2, 'start time [tbegc] before current time')`; 901행 `TINIC = TIMCO`. |
| `swan-command-file-reference.md:286` | 정정 | 문서 칸이 `2980d1a:src/swanpre1.ftn:2123–2166` 뒤 `과 HEAD의`에서 끝났다. | 과거·현재 SET 범위와 선택 부재 설명을 코드 칸에 복원했다. | R4:T1-300 최종 §5와 git D 판정. 과거 2123–2166행 및 현재 2169–2213행에는 FREQ·DIR·TIMEFORMAT 선택이 없다. |

| 기계 확인 후보 | 판정 |
|---|---|
| `src/swanpre1.ftn:2123` / `과 HEAD의` | 소스 불일치 판정은 오판이다. 해당 인용은 `2980d1a`의 SET 시작 줄이다. 다만 노트 286행의 문장은 실제로 잘려 있었다. 현재 SET 범위 2169–2213행과 누락 설명을 복원했다. |

### 5. swan-schemes-implementation.md — 완료

- 노트: `models/SWAN/source-analysis/swan-schemes-implementation.md`.
- 시작 시 추가 줄 28개를 모두 대조했다. 정정 2줄, 보완 1줄이다.
- 대조 범위: 6–7, 18, 38, 82, 99, 104, 141, 144, 148, 168–185행.
- R1·R3·R5의 해당 행 분류와 최종 결론을 대조했다. TN-044·045의 계수 절단, TN-058·059의 변수 변환, TN-063의 문서 오기 판정은 일치한다.
- swantech PDF 81·84·85쪽은 텍스트와 쪽 이미지를 함께 대조했다. swanuse PDF 92쪽의 PROP·GSE 설명도 대조했다.
- PROP 입력 분기, 기본 대입, 모드 검사, SWFLXD 호출과 제한식, 국소 차수 변경을 원문과 대조했다. 비정렬 GSE의 ac2와 정렬 S&L의 AC1 사용도 대조했다.
- Frontmatter와 Review status의 반영 이력을 확인했다. 상대 링크 4개 대상이 존재한다. 금지 경로·위키 링크·지정 한계 문장은 없다. 추가 줄에 Mermaid 도표는 없다.
- 이 노트에 지정된 기계 확인 후보는 없다.

| 노트:줄 | 구분 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| `swan-schemes-implementation.md:176` | 정정 | 식 (3.9)의 고정 첨자와 적용 sweep 조건이 빠졌다. | 두 항의 첨자 j,l,m을 복원했다. 첫 sweep의 cx>0, cy>0 조건을 명시했다. | swantech PDF 81쪽 / 인쇄 73쪽의 (3.9) 쪽 이미지와 두 식 아래의 `in case of the first sweep, i.e. cx > 0 and cy > 0`. |
| `swan-schemes-implementation.md:177` | 정정 | 식 (3.10)의 고정 첨자와 적용 sweep 조건이 빠졌다. | 두 항의 첨자 i,l,m을 복원했다. 첫 sweep의 cx>0, cy>0 조건을 명시했다. | swantech PDF 81쪽 / 인쇄 73쪽의 (3.10) 쪽 이미지와 같은 조건 문장. |
| `swan-schemes-implementation.md:184` | 보완 | PN-081의 코드 칸에 두 대입문만 있었다. | 대입 조건 4090행을 추가했다. | `swanmain.ftn:4090` `IF ( IDIFFR.EQ.1 ) THEN`. 4094–4095행에서 두 전파 선택을 1로 바꾼다. |

### 6. swan-adcirc-coupling-implementation.md — 완료

- 노트: `models/SWAN/source-analysis/swan-adcirc-coupling-implementation.md`.
- 시작 시 추가 줄 15개를 모두 대조했다. 정정 2줄, 보완 1줄이다.
- 대조 범위: 6–7, 100–101, 127, 172–181행.
- R7:I-058의 최종 결론과 git D 판정을 대조했다. 두 coupler 파일은 현재 소스 트리에도 없다. 과거 `2980d1a:switch.pl`의 전처리 치환과 현재 97·99행을 직접 읽었다.
- swanimp PDF 8–10쪽의 목록을 대조했다. 8쪽은 `swan4151.tar.gz`의 목록임을 명시한다. 10쪽 / 인쇄 4쪽에는 두 파일명이 있다. Git 배포에 대한 결론을 tarball 부재 판정으로 확대하지 않았다.
- ADC 격자 선택, SwanReadADCGrid 호출, fort.14 파일명, 비정렬 계산 분기를 대조했다.
- Frontmatter의 날짜와 반영 이력을 확인했다. 상대 링크 2개 대상이 존재한다. 금지 경로·위키 링크·지정 한계 문장은 없다. 추가 줄에 Mermaid 도표는 없다.
- 이 노트에 지정된 기계 확인 후보는 없다.

| 노트:줄 | 구분 | 전 | 후 | 근거 원문 |
|---|---|---|---|---|
| `swan-adcirc-coupling-implementation.md:101` | 보완 | 파일 부재 문장에 매뉴얼 목록과 전처리 스위치만 인용했다. | 파일 부재를 판정한 git D 보고서 I-058 링크를 추가했다. | `SWAN-git-verify-D.md:65`의 현재 경로 0파일과 조사한 Git 이력의 0커밋 판정. |
| `swan-adcirc-coupling-implementation.md:127` | 정정 | `Coupled ADCIRC-SWAN` 실행의 경로로 표기했다. | 원문이 입증하는 ADCIRC fort.14 격자 판독 실행으로 범위를 고쳤다. | `swanpre1.ftn:1478–1492`의 ADC 선택·격자 판독기 호출. `SwanReadGrid.ftn90:73–77`의 SwanReadADCGrid 호출. `SwanReadADCGrid.ftn90:95`의 파일명. `swanmain.ftn:618–627`의 격자별 계산 분기. R7:I-058은 조사한 Git 배포에 coupler 두 파일이 없다고 판정한다. |
| `swan-adcirc-coupling-implementation.md:181` | 정정 | 분류 설명은 `D 문서에만 있음`이었다. | 최종 보고서의 `D 현재 해당 구현 없음`으로 맞췄다. | `swan-implementation-history-vs-code.md:923`의 I-058 최종 분류. 결론 문장은 유지했다. |

## 최종 집계

| 노트 | 대조한 추가 줄 | 정정 줄 | 보완 줄 | 상태 |
|---|---:|---:|---:|---|
| swan-command-physics-reference.md | 104 | 2 | 0 | 완료 |
| swan-diffraction-obstacles.md | 69 | 11 | 6 | 완료 |
| wave/swan-source-terms-implementation.md | 46 | 1 | 2 | 완료 |
| swan-command-file-reference.md | 43 | 2 | 2 | 완료 |
| swan-schemes-implementation.md | 28 | 2 | 1 | 완료 |
| swan-adcirc-coupling-implementation.md | 15 | 2 | 1 | 완료 |
| 합계 | 305 | 20 | 12 | 완료 |

- 집계 근거는 시작 시 저장한 `git diff -U0 HEAD`의 추가 줄 목록과 최종 동일 명령의 추가 줄 목록이다.
- 시작 목록의 305줄은 최종 목록에도 모두 있다. 이번 정정으로 원래 추가 줄 범위 밖에 생긴 추가 줄은 0개이다.
- 변경한 32줄에는 해당 정정·보완 표지가 모두 있다. 줄 번호는 변경 전후에 같다.
- 지정된 기계 후보 6건의 판정을 위 노트별 표에 모두 기록했다. 원문 짝짓기 불일치 판정은 6건 모두 오판이다. 그중 명령 파일 노트의 잘린 문장 1건은 별도로 정정했다.
- 상대 링크의 대상 파일 누락은 0개이다. 대상 추가 줄의 절대 홈 경로·위키 링크·지정 한계 문장은 0개이다.
- 대상 추가 줄에는 Mermaid 상자가 없다. 호출 위치 인용은 원문 CALL 행과 대조했다.
- 미해결 항목은 0개이다.
