# SWAN 노트 5개 추가·수정 줄 전수 검증

- 검증일: 2026-10-13.
- 대상은 사용자가 지정한 노트 5개의 작업 시작 시점 `git diff -U0 HEAD -- <노트>`에 표시된 모든 `+` 줄이다.
- 줄 수는 frontmatter와 빈 줄을 포함한다. diff의 `+++` 파일 표지는 제외한다.
- 정정 수와 보완 수는 각각 해당 표지를 붙인 노트 줄 수로 센다.
- 원문은 SWAN 소스 저장소, 해당 저장소의 과거 커밋, 보관 HTML, PDF이다.
- 결론 분류와 결론 문장은 지정된 보고서의 최종 `[10-13 ...]` 판정과 대조한다.
- 노트별 검증을 마칠 때 대조 범위, 원문 근거, 수정 내역, 기계 확인 후보 판정을 아래에 기록한다.

## 완료 기록

### 1. swan-tech-ch2-7-qcm-theory.md — 완료

- 노트: [swan-tech-ch2-7-qcm-theory.md](../../../models/SWAN/manual-notes/swan-tech-ch2-7-qcm-theory.md).
- 시작 시점 `+` 줄 107개를 대조했다. 정정 표지를 붙인 줄은 5개다. 보완 표지를 붙인 줄은 1개다.
- 대조한 시작 줄 번호: 7–8, 21, 27, 37–38, 50–51, 69–71, 73, 89, 94–96, 105, 108–110, 117–118, 120, 125–126, 130–211.
- frontmatter, 본문, 식, 표 머리글, 빈 줄을 모두 포함했다. 행 ID가 있는 표의 71행을 R3 최종본과 대조했다.
- 원문: swantech PDF 67–76쪽 / 인쇄 59–68쪽과 PDF 111–113쪽 / 인쇄 103–105쪽. swanuse PDF 90쪽 / 인쇄 82쪽. 보관 HTML의 swantech node29·31–34·footnode와 swanuse node28. 각 줄이 인용한 현재 소스와 `2980d1a`·`43e9bbb`의 실행문. 공개 41.51 `7ee8981`의 SWQCSURF 호출.
- Akrish et al. (2020)의 작용 변수와 간섭항 가중은 [기관 저장소 원문](https://pure.tudelft.nl/ws/portalfiles/portal/71750151/modelling_statistical_wave_interferences_over_shear_currents.pdf)의 A2-4–A2-6, 식 (2.2)–(2.4)·(2.10)–(2.12)와 대조했다.
- 보고서 판정의 예외를 해소했다. R3:QC-017의 최종 B 판정은 PDF에 실제로 있는 계수 `i`를 누락으로 판단했다. PDF 69쪽의 텍스트와 쪽 이미지 및 HTML node33:82–83은 모두 `i/(4π²)`를 포함한다. 노트는 이 이론 항등식을 H로 정정했다. R3:NT-040의 조건 없는 문장은 같은 보고서의 최종 R3:QC-003에 맞춰 실수 수면과 복소 파면을 구분했다. 보고서 자체는 쓰기 대상 밖이므로 수정하지 않았다.
- 나머지 행의 결론 분류와 결론 문장은 최종 보고서와 의미가 같다. 인용된 FFT 루틴의 설명만 대조했다. Mermaid 상자는 없다. 실제 상대 링크의 대상 파일은 모두 존재한다. 금지된 절대 경로·위키 링크·한계 문장은 없다.

| 노트:줄 | 구분 | 수정 전 | 수정 후 | 근거 원문 |
|---|---|---|---|---|
| swan-tech-ch2-7-qcm-theory.md:8 | 정정 | HTML 번호가 PDF보다 항상 42 크다는 설명. 이 노트의 대조 범위를 R1–R8이라고 기록. | 실제 대조 자료를 기록했다. PDF 번호를 사용한다. HTML 번호에 일정한 차이를 적용하지 않는다. | swantech PDF (2.146)·(2.152)·(2.155). HTML node32:243의 식 표지 2.194, node33:726의 식 표지 2.216, node34:822의 식 표지 2.229. |
| swan-tech-ch2-7-qcm-theory.md:37 | 정정 | 지연 부호나 복소켤레 위치를 항상 바꿔야 한다. | 균질한 실수 수면은 지연 반전에 불변이다. 부호 변경의 조건을 복소 파면 확장으로 한정했다. | swantech PDF 67–68쪽의 R·Γ 정의. HTML node32:55–57,112–172. R3:QC-003 최종 F 판정. |
| swan-tech-ch2-7-qcm-theory.md:133 | 정정 | phase-decoupled 회절을 `QC의 비통계 대안`이라고 설명. | 위상 정보를 생략한 굴절·회절 근사라고 설명했다. 준균질 파동장 가정을 명시했다. | HTML swantech node29:47–53의 `omitting phase information`과 `quasi-homogeneous wave field`. |
| swan-tech-ch2-7-qcm-theory.md:142 | 보완 | 분산식 미분의 결론에 SORDUP 호출과 역야코비안만 제시. | 흐름을 포함한 분산식과 두 방향 속도 계수의 인용을 추가했다. | swantech PDF 70쪽 (2.149). SwanQCM.ftn90:2231–2232의 `cax = cg * kxl / k + real(u)`와 `cay = cg * kyl / k + real(v)`. |
| swan-tech-ch2-7-qcm-theory.md:146 | 정정 | R3:NT-040의 결론에서 실수 수면 조건을 생략. | 복소 파면 확장의 조건을 복원했다. 실수 수면의 지연 대칭을 명시했다. | swantech PDF 67–68쪽. R3:QC-003의 최종 결론. |
| swan-tech-ch2-7-qcm-theory.md:163 | 정정 | PDF 미분식의 중간 계수에서 `i`를 빠뜨려 전사했다. PDF 오기 B라고 판단. | 원문 계수 `i/(4π²)`를 복원했다. 원문에 없는 오기 주장을 삭제했다. 코드 구현 지시가 아닌 항등식 H로 정정했다. | swantech PDF 69쪽 / 인쇄 61쪽의 쪽 이미지와 텍스트. HTML swantech node33:82–83의 `\frac{{\rm i}}{4\pi^2}`. |

기계 확인 후보 판정은 사용자 목록의 순서대로 기록한다.

1. `src/SwanQCM.ftn90:1589` 뒤의 `와 `: 오판이다. 노트 147행은 `2980d1a:src/SwanQCM.ftn90:1589`를 인용한다. 그 줄은 `W(iky,ikx,ic) = ctb * cg / k`다.
2. `src/SwanQCM.ftn90:1593` 뒤의 `의 대응 실행문; [git 판정]...`: 오판이다. 노트 147행의 `43e9bbb:src/SwanQCM.ftn90:1593`은 같은 W 대입문이다. 한국어 연결 문장은 코드 인용문이 아니다.
3. `src/SwanQCM.ftn90:2566` 뒤의 `와 `: 오판이다. 노트 148행의 `2980d1a:src/SwanQCM.ftn90:2566`은 `cfd = cmplx(W)`다. 현재 커밋의 대응 줄은 2570이다.
4. `src/SwanQCM.ftn90:2606` 뒤의 `와 `: 오판이다. 노트 150행의 과거 줄은 `cfd(iys,ixs) = disqc(iyd,ixd) * cfd(iys,ixs)`다. 현재 커밋의 대응 줄은 2610이다.
5. 두 번째 `src/SwanQCM.ftn90:2566` 뒤의 `와 `: 오판이다. 노트 153행도 같은 과거 `cfd = cmplx(W)` 대입문을 인용한다.
6. 두 번째 `src/SwanQCM.ftn90:1589` 뒤의 `와 `: 오판이다. 노트 156행도 같은 과거 W 대입문을 인용한다.
7. `src/SwanQCM.ftn90:1392` 뒤의 `와 `: 오판이다. 노트 157행의 과거 줄은 `call SWQCWIG ( W, dwdx, dwdy, ac2, dep2, rdx, rdy, spcdir, spcsig )`다. 현재 커밋의 대응 줄은 1396이다.
8. `src/SwanQCM.ftn90:859` 뒤의 `와 `: 오판이다. 노트 160행의 과거 줄은 `rft(i,j) = sig - sigp`다. 현재 커밋의 대응 줄은 863이다.
9. `src/SwanQCM.ftn90:1611` 뒤의 `와 `: 오판이다. 노트 164행의 과거 줄은 `dwdx`의 두 방향 중앙 차분식이다. 현재 커밋의 대응 줄 1615와 항·부호가 같다.

### 2. swan-xnl4-exact-quadruplet.md — 완료

- 노트: [swan-xnl4-exact-quadruplet.md](../../../models/SWAN/source-analysis/swan-xnl4-exact-quadruplet.md).
- 시작 시점 `+` 줄 43개를 대조했다. 정정 표지를 붙인 줄은 8개다. 보완 표지를 붙인 줄은 0개다.
- 대조한 시작 줄 번호: 6, 11, 21, 52, 78, 88–89, 118, 120–122, 128, 130, 138–140, 146–147, 150–174.
- 행 ID가 있는 표의 13행을 R2·R7 최종본과 대조했다. 원문은 swantech PDF 39–41쪽 / 인쇄 31–33쪽, PDF 96쪽 / 인쇄 88쪽, swanuse PDF 72쪽 / 인쇄 64쪽, 수정 이력 HTML 306–318·561–564행과 노트가 인용한 소스다.
- `mod_xnl4v5.ftn90`의 8989줄과 행 시작 `subroutine` 선언 28개를 직접 셌다. 네 커밋 `b2ae30e`·`7ee8981`·`0dabfa4`·`43e9bbb`의 2803·6780행을 `git show`로 대조했다. 첫 커밋의 날짜는 2022-08-10이다.
- `122b595`·`43e9bbb`의 src 파일을 `git show`로 읽어 `FD.?RIAM`을 대소문자 구분 없이 검색했다. 일치 줄은 각 커밋에서 0개다. 과거 `swancom4.ftn:2980`과 현재 2978행의 XNL_MAIN 호출은 같다.
- R2:SS-514의 `최대 에너지 밀도`는 현재 실행문과 다르다. 소스의 `nspec`은 파수 공간 작용밀도다. 노트에서 그 변수의 의미와 문턱 식을 정정했다. C 분류는 유지했다. 다른 행의 분류와 최종 결론은 일치한다.
- Mermaid 상자는 없다. 추가·수정 줄의 상대 링크는 모두 존재한다. 금지된 절대 경로·위키 링크·한계 문장은 없다.

| 노트:줄 | 구분 | 수정 전 | 수정 후 | 근거 원문 |
|---|---|---|---|---|
| swan-xnl4-exact-quadruplet.md:6 | 정정 | XNL 근거를 절 시작 쪽 `p.28`로 적었다. 이 노트의 대조 범위를 R1–R8이라고 기록. | XNL의 실제 쪽과 이번 대조 범위를 기록했다. | swantech PDF 39–41쪽의 XNL 본문. PDF 96쪽의 §3.6. swanuse PDF 72쪽의 QUADRUPL. |
| swan-xnl4-exact-quadruplet.md:21 | 정정 | 검증 근거 없는 `high-precision 대체`와 `비-SWAN-team 가장 큰 contributor module`. | WRT 구현과 작성자 및 실제 셈 결과를 기술했다. XNL 선택값 51·52·53의 쪽을 명시했다. | 소스 4–5행. 해당 파일의 전체 줄·subroutine 선언 집계. swantech PDF 39–41쪽. swanuse PDF 72쪽. |
| swan-xnl4-exact-quadruplet.md:52 | 정정 | TU Delft/Alkyon 소속과 `6년 개발`을 단정. | 소스에 있는 ALKYON 표지와 변경 이력의 시작·끝 날짜를 기술했다. | 소스 463–464행의 ALKYON·작성자. 7행의 16/02/1999. 28행의 11/04/2005. |
| swan-xnl4-exact-quadruplet.md:118 | 정정 | 적분식의 곱을 정의하지 않은 `P`로 생략. | 식 (2.81)의 G 인수와 분포 곱 대괄호를 복원했다. | swantech PDF 39쪽 / 인쇄 31쪽 (2.81). |
| swan-xnl4-exact-quadruplet.md:122 | 정정 | 결합계수 기호 `C`. | 원문의 결합계수 기호 `G`. | swantech PDF 39쪽 (2.81) 다음 문장. |
| swan-xnl4-exact-quadruplet.md:130 | 정정 | 비용 배율의 비교 대상과 `보통`을 생략. 주파수 수 40개를 정확한 수로 적음. | 보통 DIA의 10³–10⁴배 계산 노력이라고 명시했다. 이상화 시험에 대한 제한과 권장 격자를 별도 문장으로 기술했다. 약 40개를 복원했다. | swantech PDF 41쪽의 `typically requiring`·`than the DIA`·`about 40`. |
| swan-xnl4-exact-quadruplet.md:165 | 정정 | R2:SS-216의 비용 배율과 주파수 수에서 비교 대상·근삿값을 생략. | 보통 DIA의 10³–10⁴배 계산 노력과 약 40개 주파수로 정정했다. | swantech PDF 41쪽 / 인쇄 33쪽. |
| swan-xnl4-exact-quadruplet.md:167 | 정정 | 필터 문턱을 최대 에너지 밀도의 0.1이라고 설명. | `qf_frac = 0.1`과 `qn_min = qf_frac*qn_max*q_kpow(ik3)`를 구분했다. 최대값의 대상이 작용밀도임을 명시했다. | 소스 7545행의 작용밀도 변환. 7566행의 `qn_max = maxval(nspec)`. 7589행의 문턱 식. 3655행의 `q_kpow`. |

기계 확인 후보 판정은 사용자 목록의 순서대로 기록한다.

10. `src/mod_xnl4v5.ftn90:2803` 뒤의 `과 `: 오판이다. 노트 164행의 `b2ae30e` 인용은 `dnn  = n(isig,iang)*dsigma(isig)*delta`와 일치한다.
11. `src/mod_xnl4v5.ftn90:2803` 뒤의 `의 `: 오판이다. 같은 노트 행의 `7ee8981` 인용도 같은 식이다. 한국어 조사는 코드가 아니다.
12. `src/mod_xnl4v5.ftn90:6780` 뒤의 `과 `: 오판이다. 노트 169행의 `b2ae30e` 인용은 `qd1    = qn3*(qn4-qn2) + qn2*qn4*qn3`와 일치한다.
13. `src/mod_xnl4v5.ftn90:6780` 뒤의 `의 `: 오판이다. 같은 노트 행의 `7ee8981` 인용도 같은 식이다.
14. `website/modifications/modifications.htm:306`의 FD-RIAM 문장: 오판이다. 문장은 306행에서 시작하여 318행까지 이어진다. HTML의 줄바꿈과 태그를 제거하면 인용한 세 문장 전체가 일치한다.

### 3. swan-boundary-implementation.md — 완료

- 노트: [swan-boundary-implementation.md](../../../models/SWAN/source-analysis/swan-boundary-implementation.md).
- 시작 시점 `+` 줄 37개를 대조했다. 정정 표지를 붙인 줄은 2개다. 보완 표지를 붙인 줄은 3개다.
- 대조한 시작 줄 번호: 6–7, 52, 70, 123, 139–141, 206, 214–215, 222, 257–281.
- 행 ID가 있는 표의 16행을 R3·R4·R7 최종본과 대조했다. 결론 분류와 결론 문장은 일치한다. R7:H-566에 덧붙인 기준 커밋과 날짜는 git A 판정과 일치한다.
- 원문: swanuse PDF 20·56–58·61–64·132쪽. swantech PDF 125–126쪽. HTML swanuse node27:138–189와 modifications:550–567. 노트가 인용한 swanmain·swanpre1·swanpre2·swanser·ocpcre·ocpmix·swmod1의 실행문과 조건문.
- `git show`로 `122b595:src/swanpre2.ftn:4471`의 LWDATE 입력문을 대조했다. 커밋 날짜는 2023-02-28이다. 공개판 표기는 41.45다. 현재 4643행의 줄 끝 표지 `41.13`도 원문 그대로다.
- `FSHAPE` 기본값과 경계별 복사, Tm01 반복, CHGBAS 구간 겹침, 경계값 덮어쓰기, 고주파 꼬리, 병렬 경계와 시계·반시계 순회, 이름 입력, CRAY 생략, 파일 이름 길이를 해당 분기와 함께 대조했다.
- Mermaid 상자는 없다. 상대 링크는 모두 존재한다. 금지된 절대 경로·위키 링크·한계 문장은 없다. 사용자 지정 기계 확인 후보는 없다.

| 노트:줄 | 구분 | 수정 전 | 수정 후 | 근거 원문 |
|---|---|---|---|---|
| swan-boundary-implementation.md:6 | 정정 | 과거 마이그레이션 설명과 R1–R8 반영만 검증 방법에 기록. | 이번 원문 대조의 범위와 사용 보고서를 기록했다. | 이 절에 열거한 소스·문서 대조와 R3·R4·R7·git A·E 판정. |
| swan-boundary-implementation.md:139 | 보완 | AC2 덮어쓰기 설명에 공간 가중치 대입만 인용. | SINTRP의 결과 인수와 출력 배열 대입 근거를 추가했다. | swanmain.ftn:6945–6946의 AC2 인수. swanser.ftn:4412·4418의 FL 대입과 4535의 0 초기화. |
| swan-boundary-implementation.md:215 | 보완 | 미지원 SET 선택을 설명하며 CGRID 입력문만 인용. | SET 선택 분기 전체를 추가로 인용했다. | swanpre1.ftn:2169–2213에는 FREQ·DIR·TIMEFORMAT 선택이 없다. |
| swan-boundary-implementation.md:267 | 보완 | 평균주기·방향 분기의 조건문에 직접 줄 위치가 없음. 문서 칸은 비어 있음. | swantech 4장과 MEAN·DSPR 정의 및 조건문 위치를 추가했다. | swantech PDF 125–126쪽. HTML node27:138–189. swanser.ftn:4141·4184–4202·4216–4224. |
| swan-boundary-implementation.md:281 | 정정 | CDATE 문장의 HTML 시작 줄을 566으로 인용. | 문장이 시작하는 567로 정정했다. | modifications.htm:566은 `<li>`다. 실제 문장은 567행의 `The format of CDATE ...`다. |

### 4. swan-bragg-scattering.md — 완료

- 노트: [swan-bragg-scattering.md](../../../models/SWAN/source-analysis/swan-bragg-scattering.md).
- 시작 시점 `+` 줄 44개를 대조했다. 정정 표지를 붙인 줄은 3개다. 보완 표지를 붙인 줄은 3개다.
- 대조한 시작 줄 번호: 6, 11, 20, 51, 58, 62–64, 84, 87, 91, 94, 104, 108–110, 116, 118, 124–126, 130–141, 143–153.
- 행 ID가 있는 표의 9행을 R2·R5 최종본과 대조했다. 결론 분류와 결론 문장은 일치한다. 문장에 중복된 문서 이름과 잘못 붙은 조사는 고쳤다.
- 원문: swantech PDF 57–58쪽 / 인쇄 49–50쪽. swanuse PDF 79–81쪽 / 인쇄 71–73쪽. SwanBraggScat의 자료 선언·평면 적합·분산 배율·보간·세 원천항 루틴·FILBRG. swanpre1의 BRAGG 입력 분기와 swancom1의 IBRAG 호출 분기.
- `kd < 5.` 조건과 입력 격자 끝값 보간을 대조했다. 세 루틴의 `cosdif**2. * fbdif * edif`를 대조했다. 바닥 스펙트럼의 보간과 원천항의 저장을 구분했다. IBRAG=4의 입력과 빈 계산 분기를 대조했다.
- Mermaid 상자는 없다. 상대 링크는 모두 존재한다. 금지된 절대 경로·위키 링크·한계 문장은 없다. 사용자 지정 기계 확인 후보는 없다.

| 노트:줄 | 구분 | 수정 전 | 수정 후 | 근거 원문 |
|---|---|---|---|---|
| swan-bragg-scattering.md:6 | 정정 | Bragg 이론 쪽을 `Tech p.48`로 적었다. 이 노트의 대조 범위를 R1–R8이라고 기록. | Bragg 본문의 실제 PDF 쪽과 이번 대조 범위를 기록했다. | swantech PDF 57–58쪽 / 인쇄 49–50쪽. swanuse PDF 79–81쪽. R2·R5의 해당 행. |
| swan-bragg-scattering.md:63 | 보완 | 반복별 보간·저장 설명에 사용자 매뉴얼만 인용. | 원천항을 저장한다고 명시했다. 해당 대입문을 추가했다. | SwanBraggScat.ftn90:1368의 `membrg(id,is,KCGRD(1)) = cf * DDIR * sbragg`. 사용자 매뉴얼의 바닥 스펙트럼 저장 여부와 구분된다. |
| swan-bragg-scattering.md:94 | 보완 | IMATRA가 우변이라는 설명에 배열 대입문만 인용. | 호출 위치의 우변 설명 주석을 추가했다. | swancom1.ftn:7824–7827의 `store in right hand vector`와 FILBRG 호출. |
| swan-bragg-scattering.md:146 | 정정 | `인쇄 72쪽는`. | `인쇄 72쪽은`. | swanuse PDF 80쪽 / 인쇄 72쪽의 IBRAG 설명은 그대로 유지했다. |
| swan-bragg-scattering.md:152 | 정정 | `swanuse swanuse`와 `인쇄 72쪽와`. | `swanuse`와 `인쇄 72쪽과`. | swanuse PDF 80쪽과 swantech PDF 57쪽의 `bilinear fit` 및 소스 339행은 그대로 유지했다. |
| swan-bragg-scattering.md:153 | 보완 | IBRAG=4 입력 가능성에 입력문 인용이 없음. | IBRAG 정수 입력문을 추가했다. | swanpre1.ftn:3490의 `CALL ININTG ('IBRAG' , IBRAG   , 'STA', 1 )`. R5:PN-158도 이 줄을 근거로 삼는다. |

### 5. swan-gse-correction.md — 완료

- 노트: [swan-gse-correction.md](../../../models/SWAN/source-analysis/swan-gse-correction.md).
- 시작 시점 `+` 줄 34개를 대조했다. 정정 표지를 붙인 줄은 4개다. 보완 표지를 붙인 줄은 6개다.
- 대조한 시작 줄 번호: 6–7, 87, 89, 91, 93, 95–99, 109–112, 115–119, 125–127, 129–139.
- 행 ID가 있는 표의 4행을 R1 최종본과 대조했다. 결론 분류와 결론 문장은 일치한다. 호출 조건은 R8:V12와 일치한다.
- 원문: swantech PDF 81–83쪽 / 인쇄 73–75쪽과 PDF 154쪽 / 인쇄 146쪽. 절 번호는 PDF 79쪽의 §3.2.1 표제와 대조했다. PDF 83쪽의 쪽 이미지에서 평균 이동 거리의 윗줄 표지, 규모별 수치, 부등호를 확인했다.
- SwanGSECorr의 전체 280줄을 읽었다. 계수 계산은 셀 순회보다 앞선다. 경계 절점은 127행에서 반환한다. 현재 시간의 작용밀도는 62행에 정의되어 있다. 정렬 S&L의 이전 시간 작용밀도 차분은 swancom5:3000–3010에 있다.
- 교차차분의 부호와 0.25 계수는 swancom5:3007–3008과 일치한다. 변경 의도와 대각 이웃 위치는 같은 파일 2718–2742의 주석과 일치한다. 회절의 셀별 평균은 SwanDiffPar:252–253·295–296과 대조했다.
- Mermaid 상자는 없다. 상대 링크는 모두 존재한다. 대상 `+` 줄에는 금지된 절대 경로·위키 링크·한계 문장이 없다. 사용자 지정 기계 확인 후보는 없다.

| 노트:줄 | 구분 | 수정 전 | 수정 후 | 근거 원문 |
|---|---|---|---|---|
| swan-gse-correction.md:7 | 정정 | GSE 대조 절을 굴절 근사의 §3.8로 적었다. 이 노트의 대조 범위를 R1–R8이라고 기록. | GSE가 있는 §3.2.1–3.2.2와 §8.6 및 이번 대조 범위를 기록했다. | swantech PDF 79·81–83·154쪽. R1의 해당 행과 R8:V12. |
| swan-gse-correction.md:97 | 보완 | 규모별 권고의 문서 쪽과 활성화 조건이 없음. | 권고 쪽과 WAVAGE 양수 호출 조건을 추가했다. | swantech PDF 83쪽. SwanTranspAc.ftn90:135의 `if ( WAVAGE > 0. ) call SwanGSECorr`. |
| swan-gse-correction.md:109 | 보완 | 정렬·비정렬의 시간 수준을 비교하면서 비정렬 코드만 인용. | 현재 시간 변수 정의와 정렬 AC1 차분의 인용을 추가했다. | SwanGSECorr.ftn90:62의 `action density at current time level`. swancom5.ftn:3000–3010의 AC1 차분. |
| swan-gse-correction.md:111 | 보완 | 회절과 비교하면서 GSE 코드만 인용. | 회절에서 군속도와 파수를 셀별로 평균하는 실행문을 추가했다. | SwanDiffPar.ftn90:252–253·295–296의 각 세 절점 평균. 276·319행의 확산 기울기. |
| swan-gse-correction.md:115 | 정정 | GSE 교차 참조를 §3.8로 표기. | §3.2.1–3.2.2와 §8.6 및 해당 PDF 쪽을 명시했다. | swantech PDF 81–83·154쪽의 GSE 본문. |
| swan-gse-correction.md:116 | 정정 | 전파 구현 노트 전체를 GSE 미적용 경로로 설명. | 연결된 노트의 실제 범위인 지리 공간·스펙트럼 공간 전파 구현으로 설명했다. | 연결된 노트의 B·C절. SwanTranspAc.ftn90:129–135는 공간 전파 뒤에 조건부 GSE를 호출한다. |
| swan-gse-correction.md:119 | 정정 | 여러 모듈을 묶어 SWAN 41.x에 추가되었다고 설명. | 출시 시기 주장 없이 각 구현 노트의 내용을 설명했다. | SwanBraggScat:38·SwanQCM:38·SwanIEM:38은 각각 내부 변경 번호와 다른 작성 시점을 적는다. 배포판 출시 이력의 근거가 아니다. |
| swan-gse-correction.md:125 | 보완 | 정렬·비정렬의 시간 수준을 비교하면서 비정렬 코드만 인용. | 109행과 같은 시간 수준 근거를 추가했다. | SwanGSECorr.ftn90:62. swancom5.ftn:3000–3010. |
| swan-gse-correction.md:136 | 보완 | R1:TC-008의 코드 칸에 비정렬 인용만 있음. | 정렬 차분과 현재 시간 변수 정의를 추가했다. 결론은 유지했다. | SwanGSECorr.ftn90:62. swancom5.ftn:3000–3010. |
| swan-gse-correction.md:139 | 보완 | R1:TN-218의 코드 칸에 GSE 인용만 있음. | 회절의 셀별 평균과 확산 기울기 인용을 추가했다. 결론은 유지했다. | SwanDiffPar.ftn90:252–253·276·295–296·319. |

## 최종 집계와 확인

| 노트 | 대조한 시작 시점 + 줄 | 정정 줄 | 보완 줄 | 기계 후보 |
|---|---:|---:|---:|---:|
| swan-tech-ch2-7-qcm-theory.md | 107 | 5 | 1 | 9건 모두 오판 |
| swan-xnl4-exact-quadruplet.md | 43 | 8 | 0 | 5건 모두 오판 |
| swan-boundary-implementation.md | 37 | 2 | 3 | 없음 |
| swan-bragg-scattering.md | 44 | 3 | 3 | 없음 |
| swan-gse-correction.md | 34 | 4 | 6 | 없음 |
| 합계 | 265 | 22 | 13 | 14건 모두 오판 |

- 시작 시점 diff의 265개 `+` 줄과 최종 diff의 줄 번호 집합이 일치한다. 수정한 35줄은 모두 그 집합 안에 있다. 각 수정 줄의 끝에는 지정된 정정·보완 표지가 있다. 표 행은 마지막 셀의 끝에 표지를 두었다. frontmatter는 YAML 주석으로 표지를 두었다.
- 노트의 행 ID 113개를 해당 보고서의 최종 결론과 대조했다. 원문에 따른 보고서 판정 예외는 위의 R3:QC-017과 R2:SS-514 기록에 명시했다. R3:NT-040은 최종 R3:QC-003의 조건을 적용했다.
- 대상 줄의 상대 링크 83개는 모두 실제 파일을 가리킨다. frontmatter 5개는 YAML 파싱을 통과했다. 대상 노트의 Mermaid 블록 수는 0개다.
- 대상 줄의 절대 경로·위키 링크·지정된 한계 문장 검사에 일치 항목이 없다. 대상 노트의 `git diff --check HEAD -- <노트>`에 오류 출력이 없다.
- 이번 쓰기 대상은 지정된 노트 5개와 이 기록이다. 미해결 항목은 0개다.
