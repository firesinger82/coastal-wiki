# SWAN 노트 추가·수정 줄 전수 검증

검증일은 2026-10-13이다.
대상은 사용자 지정 노트 6개의 `git diff -U0 HEAD -- <노트>`에 나타나는 모든 추가 줄이다.
추가 줄 수에는 frontmatter, 빈 줄, 표 구분 줄, 코드 블록 줄을 포함한다.
각 노트의 검증 시작 시점에 추가 줄 수와 줄 번호를 고정한다.
정정 수와 보완 수는 수정한 기존 추가 줄을 기준으로 센다.
정정 목록의 줄 번호는 해당 노트의 검증 시작 시점을 기준으로 한다.
원문은 현재 소스, 과거 커밋, 저장된 HTML, PDF와 사용자 지정 최종 보고서를 사용한다.
완료한 노트의 결과는 아래에 차례로 덧붙인다.

## 노트별 결과

### 1. swan-tech-ch3-solution-iteration-limiter.md — 완료

대상은 [노트](../../../models/SWAN/manual-notes/swan-tech-ch3-solution-iteration-limiter.md)의 추가 줄 99줄이다.
대상 줄 번호는 7–8, 21, 39, 42–43, 54–56, 64, 69, 72–76, 89–96, 102, 116, 120–132, 134, 145, 165–167, 177, 179, 183–235이다.
정정은 3줄이다.
보완은 2줄이다.
차이 표의 39개 행 ID는 R1·R2·R7 제5절과 R8 제8절의 최종 분류·결론에 대응한다.
R7:H-1228의 `122b595`, `2023-02-28`은 git 판정 A의 114줄과 같다.
과거 커밋 인용은 `git show HASH:path`로 해당 줄을 대조했다.
PDF 원문은 swantech 18·87–96·99–100쪽과 swanuse 72·93–95·141쪽을 대조했다.
식 (3.18)의 노트 정정식과 원문 오기 인용을 구분했다.
식 (3.26)의 분자·분모·부등호·반복 시작값은 PDF 92쪽과 같다.
HTML 인용은 줄바꿈을 연결하여 대조했다.
추가 줄의 상대 링크 17곳은 실제 파일을 가리킨다.
추가 줄에는 개인 절대 경로, 위키 링크 구문, 사용자 지정 한계 문장이 없다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `swan-tech-ch3-solution-iteration-limiter.md:21` | 정정 | `NUMERIC 명령 거의 전부` → 정지 기준·스펙트럼 해법·제한기 설정으로 범위를 명시했다. | swanuse PDF 93–95쪽은 NUMERIC에 CTHETA·CSIGMA·SETUP도 열거한다. swantech PDF 87–100쪽은 이 노트의 §3.3–3.7이다. |
| `swan-tech-ch3-solution-iteration-limiter.md:198` | 보완 | `2120–2121` 뒤의 행렬 조립 인용에 위치가 없었다. → `2188–2190`, `2177–2185`를 추가했다. | `src/swancom2.ftn:2188`은 `IMATDA(ID,IS) = IMATDA(ID,IS) + REAL(SURFA1)`이다. 2190줄은 `IMATRA(ID,IS) = IMATRA(ID,IS) + REAL(DIS0)`이다. |
| `swan-tech-ch3-solution-iteration-limiter.md:211` | 보완 | 코드 근거 칸 `—` → PHILIM·HJLIM 식의 `src/swancom1.ftn:7978–7979,8115–8121`과 외부 대조 보고서 링크를 추가했다. | 8115줄은 `C_HJ = PI2**2*3.0*1.0E-7*DT*SPCSIG(MSC)`이다. 8119–8121줄은 마찰속도 하한과 `DAC2MX` 식이다. 외부 보고서 §1 및 저장된 IFS 식 (3.37)·(3.38)은 방향 정규화 차이를 설명한다. |
| `swan-tech-ch3-solution-iteration-limiter.md:214` | 정정 | `src/swancom1.ftn:7648`의 `CALL SWSNL3` → `src/swancom1.ftn:7653`의 같은 호출. | 7648–7651줄은 후속 반복의 조건문이다. 7653줄에서 `CALL SWSNL3`를 실행한다. |
| `swan-tech-ch3-solution-iteration-limiter.md:217` | 정정 | `src/swanmain.ftn:6586`의 `IQUAD=3` → 6585줄의 조건문과 6586줄의 권고 메시지 호출. | `IF (ICUR.NE.0 .AND. (IQUAD.EQ.1 .OR. IQUAD.EQ.2)) THEN`; `CALL MSGERR(0,'In presence of a current it is recommended to')`. |

기계 확인 후보 판정은 다음과 같다.

- `src/swancom1.ftn:7648` / `CALL SWSNL3`: 실제 오류이다. 노트 214줄을 7653줄로 정정했다.
- `src/swanmain.ftn:6586` / `IQUAD=3`: 실제 오류이다. 노트 217줄을 조건문·권고 메시지 원문으로 정정했다.
- `src/swancom1.ftn:9606` / `, `: 오판이다. 노트 226줄의 대상은 현재 파일이 아니라 `b2ae30e:src/swancom1.ftn:9606`이다. 해당 커밋에 `TMREL = TMABS / SACC2(INDX)`가 있다.
- `src/swancom1.ftn:9855` / `, 현재 `: 오판이다. 노트 226줄의 대상은 `7ee8981:src/swancom1.ftn:9855`이다. 해당 커밋과 현재 파일의 식이 같다.
- `website/modifications/modifications.htm:213`: 오판이다. 노트 231줄의 인용문은 HTML 213–218줄을 연결한 원문과 같다.
- `website/modifications/modifications.htm:219` 첫 번째 후보: 오판이다. 노트 232줄의 인용문은 HTML 219–227줄을 연결한 원문과 같다.
- `website/modifications/modifications.htm:219` 두 번째 후보: 오판이다. 노트 233줄도 같은 HTML 원문을 인용한다.
- `website/modifications/modifications.htm:789`: 오판이다. 노트 234줄의 인용문은 HTML 789–807줄을 연결한 원문과 같다.

이 노트의 미해결 항목은 0개이다.

### 2. swan-tech-ch3-obstacles-spectral-ops.md — 완료

대상은 [노트](../../../models/SWAN/manual-notes/swan-tech-ch3-obstacles-spectral-ops.md)의 추가 줄 56줄이다.
대상 줄 번호는 7–8, 21, 36, 43–44, 47–48, 74–79, 81, 100–103, 111–114, 131, 135–166이다.
정정은 2줄이다.
보완은 2줄이다.
차이 표의 21개 행 ID는 R1·R3 제5절의 최종 분류·결론과 같다.
PDF 원문은 swantech 118–122쪽과 swanuse 21–22쪽을 대조했다.
교차식의 매개변수, 꼬리 적분의 방향 적분, SINTRP의 모멘트와 경계 처리를 코드와 대조했다.
과거 커밋 `b2ae30e`, `7ee8981`, `0dabfa4`, `43e9bbb`의 인용 식은 `git show HASH:path`로 대조했다.
추가 줄의 상대 링크 15곳은 실제 파일을 가리킨다.
추가 줄에는 개인 절대 경로, 위키 링크 구문, 사용자 지정 한계 문장이 없다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `swan-tech-ch3-obstacles-spectral-ops.md:146` | 정정 | E 후보의 문서 칸 `— (문서 누락)` → `— (R1 제3절의 코드 처리 항목)`. | R1 제3절은 `코드에만 있는 처리`이다. 제5절 TC-010의 최종 분류는 `E 코드 결함 후보 (강함)`이다. |
| `swan-tech-ch3-obstacles-spectral-ops.md:147` | 정정 | E 후보의 문서 칸 `— (문서 누락)` → `— (R1 제3절의 코드 처리 항목)`. | R1 제5절 TC-011의 최종 분류는 `E 코드 결함 후보 (강함)`이다. `src/SwanIntgratSpc.ftn90:119–129`는 상한·하한의 배타 분기이다. |
| `swan-tech-ch3-obstacles-spectral-ops.md:131` | 보완 | 끝 가중치와 총량 문턱의 인용만 있었다. → 빈 스펙트럼 처리와 방향·주파수 범위의 위치를 추가했다. | `src/swanser.ftn:4442–4454`의 `FL = W2*FL2`·`FL = W1*FL1`; 4538–4555줄의 `FULCIR`, `DOADD`, `MAX`·`MIN` 반복 경계. |
| `swan-tech-ch3-obstacles-spectral-ops.md:162` | 보완 | TN-168의 코드 칸에 경계 처리 위치가 없었다. → `src/swanser.ftn:4442–4454,4538–4555`를 추가했다. | 위 131줄의 같은 원문이다. |

사용자가 지정한 기계 확인 후보는 이 노트에 없다.
이 노트의 미해결 항목은 0개이다.

### 3. swan-unstructured-time-step.md — 완료

대상은 [노트](../../../models/SWAN/source-analysis/swan-unstructured-time-step.md)의 추가 줄 46줄이다.
대상 줄 번호는 6–7, 55, 85, 95, 98, 103–104, 107, 113, 126–134, 137, 139–140, 142, 144–145, 150–170이다.
정정은 7줄이다.
보완은 1줄이다.
차이 표의 10개 행 ID는 R1 제5절과 R8 제8절의 최종 분류·결론에 대응한다.
T1-014의 `0dabfa4`, `2026-07-13`은 git 판정 A의 133줄과 같다.
`7ee8981`, `0dabfa4`, `43e9bbb`의 실행 목록과 스위치 인용을 해당 커밋 원문과 대조했다.
PDF 원문은 swantech 144·150–151쪽과 swanuse 24·135쪽을 대조했다.
추가 줄의 상대 링크 40곳은 검증 시작 시점에 모두 실제 파일을 가리켰다.
추가 줄에는 개인 절대 경로, 위키 링크 구문, 사용자 지정 한계 문장이 없다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `swan-unstructured-time-step.md:6` | 정정 | frontmatter의 `1684 lines`, `change history 12 versions` → 현재 파일 1678줄과 헤더 변경 이력 15항목. | `src/SwanCompUnstruc.ftn90` 전체 줄을 셌다. 50–64줄의 이력 항목을 셌다. 실제 대조 범위를 헤더·인용 구현부·인용 문서로 명시했다. |
| `swan-unstructured-time-step.md:55` | 정정 | `14 명의 SWAN-team contributor` → 중복 이름을 제외한 저자 6명. | `src/SwanCompUnstruc.ftn90:32–46`의 이름은 Marcel Zijlema, Casey Dietrich, Dirk Rijnsdorp, Ad Reniers, Gal Akrish, Pieter Smit이다. 56줄은 ADCIRC+SWAN 확장 이력이다. |
| `swan-unstructured-time-step.md:107` | 정정 | `QCM 11회`와 문자열 부재에서 추론한 경로 설명 → QCM 문자열 12회·해당 줄 11줄과 실제 호출 위치. | 현재 파일 전체의 대소문자 구분 없는 문자열 집계이다. 1170줄은 `call QCSOURCE`이다. 1134–1156줄은 SOURCE에 `fbd`·`membrg`를 전달한다. Bragg 문자열 3회와 IEM·GSECorr·SpectPart 문자열 부재도 대조했다. |
| `swan-unstructured-time-step.md:131` | 정정 | IEM의 `본 module과 동시 시기` → IEM 생성 이력의 날짜를 명시했다. | `src/SwanIEM.ftn90:38`: `!   41.85, January 2019: New module`. |
| `swan-unstructured-time-step.md:133` | 정정 | 2009년 GSECorr가 `본 module 이전` → GSECorr 2009년 2월과 SwanCompUnstruc 2007년 7월을 구분했다. | `src/SwanGSECorr.ftn90:36`; `src/SwanCompUnstruc.ftn90:50`. |
| `swan-unstructured-time-step.md:151` | 정정 | `vertex↔점`, SINTRP의 `비정형 버전` → 꼭짓점에서 지정점으로 각 bin을 공간 보간한다. | `src/SwanInterpolateAc.ftn90:42–49,273–290`. 290줄은 `acintp(:,:) = acintp(:,:) + ww(k) * ac2(:,:,v(k))`이다. 주파수·방향을 이동하는 SINTRP 식과 다르다. |
| `swan-unstructured-time-step.md:152` | 보완 | 출력 보간 설명의 코드 위치가 없었다. → 목적 주석과 호출 위치를 추가했다. | `src/SwanInterpolateOutput.ftn90:44–51`; `src/swanout1.ftn:1676`의 `CALL SwanInterpolateOutput`. |
| `swan-unstructured-time-step.md:169` | 정정 | 문서 칸의 과거 미확정 설명과 잘린 `근원인` → 과거 84줄의 고정 sweep 수 인용만 남겼다. | R8:N1-007 최종 행과 `src/SwanCompUnstruc.ftn90:124,825–831`은 현행 감소 조건을 확정한다. |

기계 확인 후보 판정은 다음과 같다.

- `src/SwanCompUnstruc.ftn90:848` / `의 원문은 `: 오판이다. `43e9bbb:src/SwanCompUnstruc.ftn90:848`은 인용한 `!GRAPH                ivert = flist(kvert,swpdir)`와 같다.
- `src/SwanCompUnstruc.ftn90:849` / `의 원문은 `: 오판이다. `43e9bbb:src/SwanCompUnstruc.ftn90:849`는 인용한 `!FXFRO                ivert = vlist(kvert,swpdir)`와 같다.

이 노트의 미해결 항목은 0개이다.

### 4. swan-tech-ch2-sources-sinks.md — 완료

대상은 [노트](../../../models/SWAN/manual-notes/swan-tech-ch2-sources-sinks.md)의 추가 줄 60줄이다.
대상 줄 번호는 7, 12, 23, 118, 123, 152, 166–169, 176–178, 193–194, 196–198, 200–203, 207–210, 220, 268, 270–272, 276–304이다.
정정은 3줄이다.
보완은 2줄이다.
차이 표의 10개 행 ID는 R2·R7 제5절의 최종 분류·결론에 대응한다.
H-538의 `2980d1a`, `2023-02-27`은 git 판정 A의 86줄과 같다.
`2980d1a`의 부모 파일은 `IDRAG = 2`를 사용한다.
`2980d1a`와 비교 커밋 `122b595`는 `IDRAG = 1`을 사용한다.
이 차이는 `git show <커밋>:src/swanmain.ftn` 원문에서 대조했다.
PDF 원문은 swantech 21–29·33쪽과 swanuse 66·69·71–72·74쪽을 대조했다.
frontmatter의 PDF 쪽과 인쇄 쪽 대응을 확인했다.
필터 식의 `0.13`, `28`, `2π`와 코드의 상한·고주파 감소 조건을 구분했다.
추가 줄의 상대 링크 23곳은 실제 파일을 가리킨다.
추가 줄에는 개인 절대 경로, 위키 링크 구문, 사용자 지정 한계 문장이 없다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `swan-tech-ch2-sources-sinks.md:23` | 정정 | `SWAN의 모든 6 source/sink term` → 천해의 기본 과정 6개와 별도 보충 과정의 범위를 구분했다. | swantech PDF 22쪽은 `six basic processes`라고 적는다. PDF 21쪽은 식생·해빙·불규칙 해저 산란을 별도 보충 과정으로 열거한다. |
| `swan-tech-ch2-sources-sinks.md:193` | 정정 | 바람 입력 `Eq 2.28-2.37` → `Eq 2.28·2.32–2.37`. | swantech PDF 23–25쪽의 식 (2.29)–(2.31)은 각각 백파·바닥 마찰·쇄파 소산이다. PDF 22·27–28쪽의 인용 식은 바람 입력이다. |
| `swan-tech-ch2-sources-sinks.md:194` | 정정 | `WCAPPING (Komen / Janssen / Van der Westhuysen)` → `WCAPPING KOMEN`·`WCAPPING AB`와 `GEN3 JANSSEN`을 구분했다. | swanuse PDF 71쪽의 WCAPPING 선택지는 KOMEN·AB이다. Janssen 조합은 PDF 66쪽의 GEN3 구문에 있다. |
| `swan-tech-ch2-sources-sinks.md:282` | 보완 | ST6 함수명에 문서 쪽만 있었다. → 두 호출의 코드 위치를 추가했다. | `src/swancom1.ftn:7489`의 `CALL SWIND_DBYB`; `src/swancom2.ftn:2859`의 `CALL CALC_SDS`. |
| `swan-tech-ch2-sources-sinks.md:301` | 보완 | SS-703의 코드 칸에 저자 주석만 있었다. → SWIND_DBYB·CALC_SDS 호출 위치를 추가했다. | 위 282줄의 같은 원문이다. |

기계 확인 후보 `website/modifications/modifications.htm:538`은 오판이다.
노트 304줄의 인용문은 HTML 538–542줄을 연결하고 태그·문자 참조를 해석한 원문과 같다.
`m&sup2;/s&sup3;`는 인용문의 `m²/s³`와 같다.
이 노트의 미해결 항목은 0개이다.

### 5. swan-vtk-output.md — 완료

대상은 [노트](../../../models/SWAN/source-analysis/swan-vtk-output.md)의 추가 줄 35줄이다.
대상 줄 번호는 6, 11, 21, 33, 59, 61, 74, 83, 87, 89–90, 98, 115–120, 122, 124, 126–140이다.
정정은 4줄이다.
보완은 4줄이다.
차이 표의 3개 행 ID는 R6 제5절의 최종 분류·결론에 대응한다.
VTK 파일 3개의 전체 줄 수는 각각 308·207·292줄이다.
각 파일의 32줄과 36줄에서 작성자와 도입 시기를 대조했다.
SWBLKV의 격자별 확장자, 병렬 파일, 시각별 수집 파일 처리를 원문과 대조했다.
DIR의 변수 형식과 실제 스칼라 기록 분기를 대조했다.
벡터의 z 성분은 데이터 기록문의 `0.`과 같다.
PDF 원문은 swanuse 109–110쪽을 대조했다.
절 안내는 swanuse·swantech PDF 7쪽의 목차와 해당 노트의 실제 절을 대조했다.
기존 추가 줄의 상대 링크 9곳은 실제 파일을 가리킨다.
추가 줄에는 개인 절대 경로, 위키 링크 구문, 사용자 지정 한계 문장이 없다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `swan-vtk-output.md:21` | 정정 | VTK 자체를 binary file format으로 정의하고 최신 추가라고 단정했다. → SWAN의 VTK XML·raw appended binary 구현으로 범위를 좁혔다. | `src/SwanVTKWriteHeader.ftn90:277`의 `<AppendedData encoding="raw">`; 파일 3개의 원문 줄 수 합계는 807줄이다. |
| `swan-vtk-output.md:33` | 정정 | 가장 최근 모듈·QC 이후 6개월·team lead라고 적었다. → 파일 머리말의 작성자와 도입 시기로 고쳤다. | 세 VTK 파일의 32줄은 `41.95: Marcel Zijlema`이다. 36줄은 `41.95, July 2022: New subroutine`이다. 비교 대상으로 든 `SwanCompUnstruc.ftn90:63`의 QC 도입은 February 2022이다. |
| `swan-vtk-output.md:87` | 보완 | 대문자 검사인 1216줄만 인용했다. → 소문자 검사인 1217줄을 추가했다. | `src/swanpre2.ftn:1217`의 `&          INDEX (FILENM, '.vt' ).NE.0`. |
| `swan-vtk-output.md:90` | 보완 | 3성분 헤더만 인용했다. → 실제 z 성분 기록문을 추가했다. | `src/SwanVTKWriteData.ftn90:144`의 `data(ip+i,voqr(ivtype)), data(ip+i,voqr(ivtype)+1), 0.`. |
| `swan-vtk-output.md:116` | 정정 | source coverage audit `§3.5` → `§4.1`. | 해당 노트 231줄의 §3.5는 FFT library이다. 247–258줄의 §4.1 표에 VTK 파일 3개가 있다. |
| `swan-vtk-output.md:122` | 정정 | R6의 스펙트럼 형식 절 `§2.5` 링크 → VTK 파일·배열이 있는 `§2.6` 링크. | R6 260줄의 §2.6 제목은 `NetCDF·MAT·VTK와 Appendix C`이다. VTK의 O-116은 268줄에 있다. |
| `swan-vtk-output.md:130` | 보완 | 대문자 검사만 인용했다. → 소문자 검사도 인용했다. | 위 87줄과 같은 `src/swanpre2.ftn:1216–1217`이다. |
| `swan-vtk-output.md:140` | 보완 | N-022 코드 칸에 소문자 검사와 z 성분 기록문이 없었다. → 두 위치를 추가했다. | 위 87·90줄의 원문이다. 최종 B 분류와 결론 문장은 유지했다. |

이 노트에는 사용자가 지정한 기계 확인 후보가 없다.
이 노트의 미해결 항목은 0개이다.

### 6. README.md — 완료

대상은 [노트](../../../models/SWAN/README.md)의 추가 줄 44줄이다.
대상 줄 번호는 1–5, 15, 21–28, 33, 40, 44–45, 48–62, 67–77이다.
정정은 0줄이다.
보완은 2줄이다.
차이 표의 R7:N-033은 R7 제5절의 최종 분류·결론과 같다.
격자 지원 범위 문장은 R3:NT-051의 결론과 같다.
VERNUM과 BUGFIX 인용은 `src/swanmain.ftn:965–968`과 같다.
HEAD·patch B·41.45·41.51의 해시와 날짜는 git 판정 A·D와 같다.
이력 98커밋은 git 판정 D의 11줄과 같다.
이력 기간은 노트 반영 기록 7의 451줄과 같다.
swanuse·swantech·swanimp의 판 정보는 각 PDF 1쪽과 같다.
swanpgr의 판과 마지막 이력은 PDF 51쪽의 표와 같다.
`manual-notes/swan-*.md`에 해당하는 파일은 29개이다.
보고서 연결은 실제 파일과 해당 절을 가리킨다.
기존 추가 줄의 상대 링크 21곳은 실제 파일을 가리킨다.
추가 줄에는 개인 절대 경로, 위키 링크 구문, 사용자 지정 한계 문장이 없다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `README.md:27` | 보완 | 이력 집계에 명령 이름만 있었다. → 이력 수와 기간을 확인할 기록 링크를 추가했다. | `SWAN-git-verify-D.md:11`의 `98커밋`; `SWAN-notes-apply-7.md:450–451`의 `98`과 `2022-07-30~2026-07-13`. |
| `README.md:33` | 보완 | 29노트의 집계 범위와 세 매뉴얼의 판 쪽이 없었다. → 파일 glob과 PDF 1쪽 인용을 추가했다. | `models/SWAN/manual-notes/swan-*.md` 29개; swanuse·swantech·swanimp PDF 1쪽의 `SWAN Cycle III version 41.51`. |

이 노트에는 사용자가 지정한 기계 확인 후보가 없다.
이 노트의 미해결 항목은 0개이다.

## 최종 집계

아래 수는 노트별 추가 줄 목록과 정정·보완 목록을 합산한 값이다.

| 노트 | 대조한 추가 줄 | 정정 줄 | 보완 줄 |
|---|---:|---:|---:|
| swan-tech-ch3-solution-iteration-limiter.md | 99 | 3 | 2 |
| swan-tech-ch3-obstacles-spectral-ops.md | 56 | 2 | 2 |
| swan-unstructured-time-step.md | 46 | 7 | 1 |
| swan-tech-ch2-sources-sinks.md | 60 | 3 | 2 |
| swan-vtk-output.md | 35 | 4 | 4 |
| README.md | 44 | 0 | 2 |
| 합계 | 340 | 19 | 13 |

사용자 지정 기계 확인 후보는 중복 제시된 후보를 포함하여 11건이다.
실제 오류 2건은 노트의 인용 위치·인용문을 정정했다.
오판 9건은 해당 커밋 또는 줄바꿈을 연결한 원문으로 판정했다.
수정한 32줄에는 지정한 정정·보완 표지가 있다.
수정은 검증 시작 시점의 추가 줄 안에서 이루어졌다.
최종 `git diff -U0 HEAD`의 추가 줄 번호와 줄 수는 시작 시점과 같다.
차이 표 84행의 행 ID와 결론 분류를 최종 보고서와 대조했다.
결론 문장의 차이는 경로 접두어, 행 ID 접두어, 쪽 번호 표기, 링크, 이미 검증한 커밋 정보와 해석 표지의 표기 차이이다.
추가 줄의 상대 링크 125곳은 실제 파일을 가리킨다.
이 중 절 링크 39곳은 실제 제목을 가리킨다.
대상 노트에는 Mermaid 코드 블록이 없다.
frontmatter는 YAML로 읽을 수 있다.
Markdown 표의 열 수와 코드 블록의 경계가 맞는다.
추가 줄에는 개인 절대 경로, 위키 링크 구문, 사용자 지정 한계 문장이 없다.
대상 노트의 `git diff --check` 결과에는 오류가 없다.
미해결 항목은 0개이다.
