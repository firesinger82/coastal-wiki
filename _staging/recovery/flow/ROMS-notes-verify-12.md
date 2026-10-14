# ROMS 노트 전수 대조 12

- 작업일: 2026-10-14.
- 대상: `roms_include_cppdefs-differences-1.md` 전체 줄과 `roms_bottom_boundary_layer.md`·`roms_wetting_drying.md`의 작업 시작 시점 `git diff -U0 HEAD` 추가 줄.
- 대조 기준: 현재 소스코드, 인용된 과거 커밋, 위키 원문, 비교 보고서의 최종 전수 검증 기록.
- 집계 기준: 빈 줄과 frontmatter를 포함한다. 정정 수와 보완 수는 변경한 대상 줄 수로 센다.
- 기계 확인 불일치 후보: 사용자 제공 목록에 없음.

## 작업 시작 시점의 대상 줄

| 노트 | 대상 줄 수 | 시작 시점 줄 범위 |
|---|---:|---|
| `roms_include_cppdefs-differences-1.md` | 264 | 1–264 전체 |
| `roms_bottom_boundary_layer.md` | 100 | 2, 6–7, 20–21, 26–31, 33–38, 42–53, 55–67, 71–75, 79–83, 85, 87–89, 93–96, 98–137 |
| `roms_wetting_drying.md` | 91 | 7–8, 19–20, 23, 27, 29–35, 38–50, 54–57, 62–67, 71–83, 85–86, 93–96, 98–105, 108–111, 115–138 |

대상 줄 수 합계는 위 표의 455줄이다.

노트별 완료 결과는 대조를 마친 순서대로 아래에 덧붙인다.

## roms_include_cppdefs-differences-1.md — 완료

- 대조한 줄 수: 전체 264줄이다. 시작 시점 범위는 1–264이다.
- 정정 수: 0줄이다.
- 보완 수: 1줄이다.
- 차이 표 230행의 ID와 분류를 `note-job-2.tsv`의 해당 파일 배정과 대조했다.
- 차이 표 230행의 결론을 생물 보고서와 빌드·옵션·이력 보고서의 최종 §5 및 전수 검증 기록과 대조했다.
- 현재 코드와 위키의 인용 위치를 열어 조건·부정·선택 순서·수식·수량을 대조했다.
- `RBH-0005`의 과거 소스를 `git show`로 열었다. 커밋 `55c2f307`의 날짜는 2008-03-18이다. `04f6a3a3`의 날짜는 2008-08-08이다. `e8719fb7`의 날짜는 2011-09-23이다. 노트는 `ROMS-git-verify-A1.md:33`의 판정을 유지한다.
- E 행의 강도는 `RBH-1742`·`RBH-3031`·`RBH-3049`가 강함이다. `RBH-3048`·`RBH-3134`·`RBH-3166`은 중간이다. 각 강도는 보고서 최종 판정과 같다.
- `biology:NT-012`는 생물 보고서 §4의 아홉 옵션 목록을 반영했다.
- frontmatter와 판본 정보를 대조했다. 위키 수집일은 `manifest.json`의 2026-05-03과 같다. 코드 HEAD와 저자 날짜는 `57aecf58`, 2026-09-18이다. 코드 버전 문자열은 `ROMS/Modules/mod_ncparam.F:653`의 `4.3`이다.
- 상대 링크의 대상 파일은 모두 존재한다. 절대 로컬 경로와 `[[`는 없다. 미수행 작업을 남기는 한계 문장은 없다. Mermaid 블록은 없다.
- 기계 확인 후보 판정: 사용자 제공 후보 없음.
- 미해결 항목: 없음.

### 보완 목록

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `models/ROMS/source-analysis/roms_include_cppdefs-differences-1.md:36` (`biology:OP-002`) | 코드 근거가 ECB 설명인 `cppdefs.h:483`만 가리켰다. | `fennel.h:393`과 `fennel.h:1225`의 실제 Fennel 조건문을 추가했다. 결론 칸 끝에 `[10-14 전수 검증 보완]`을 붙였다. | `ROMS/Nonlinear/Biology/fennel.h:393,1225`의 `# if defined RW14_CO2_SC`. `roms-biology-vs-code.md:1267`의 OP-002 본문 행이 두 위치를 인용한다. |

정정 목록은 없다.

## roms_bottom_boundary_layer.md — 완료

- 대조한 줄 수: 작업 시작 시점 `git diff -U0 HEAD`의 추가 줄 100줄이다. 범위는 위의 대상 줄 표와 같다.
- 정정 수: 3줄이다.
- 보완 수: 0줄이다.
- 차이 표 33행의 분류와 결론은 혼합·경계·강제, 출력·메타데이터, 퇴적물·해빙·식생 보고서의 최종 §5와 같다.
- 본문 수정은 `RMF1-944`–`RMF1-948`, `RMF1-972`, `RN1-035`–`RN1-038`의 수정안과 대조했다. 근거 없는 우열·적용 권고와 입력·출력 혼동을 제거한 변경은 해당 수정안에 근거한다.
- 인용 뒤에 원문 발췌가 없는 본문 문장도 해당 소스 범위를 열어 대조했다. 두 Fortran 블록은 원문과 같다.
- `RMF1-816`의 B 판정과 계수·단위 설명은 외부 원문 보고서의 Liang 식 (6) 판정과 같다. 최종 보완 기록은 이 판정을 바꾸지 않았다.
- `OMD-V043`은 A8의 확정 판정과 출력 보고서 최종 기록에 따라 C를 유지한다. `roms-2.0:External/varinfo.dat:701–708`과 `roms-4.1:ROMS/External/varinfo.yaml:1431`을 열어 단위 환산과 방향 메타데이터를 대조했다.
- `OMD-Y091`은 E2 및 출력 보고서의 강함 판정을 유지한다. YAML의 잘못된 type과 출력 코드의 명시적 `r2dvar`를 구분했다.
- frontmatter의 소스 파일 줄 수는 실제 `ssw_bbl.h` 1849줄, `mb_bbl.h` 730줄, `sg_bbl.h` 1149줄과 같다. 이 수는 해당 세 파일의 `wc -l` 결과이다.
- 상대 링크의 대상 파일은 모두 존재한다. 절대 로컬 경로와 `[[`는 없다. 미수행 작업을 남기는 한계 문장은 없다. Mermaid 블록은 없다.
- 기계 확인 후보 판정: 사용자 제공 후보 없음.
- 미해결 항목: 없음.

### 정정 목록

아래 줄 번호는 시작 시점과 정정 후가 같다. 세 줄 모두 끝에 `[10-14 전수 검증 정정]`을 붙였다. Frontmatter의 표지는 YAML 주석으로 붙였다.

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `models/ROMS/source-analysis/roms_bottom_boundary_layer.md:7` | `verification_method`의 거칠기 식은 `zoBF=ar·rheight²/rlength`였다. | `zoBF(i,j)=ar*rheight(i,j)**2/(rlength(i,j)+eps)`로 고쳤다. | `ROMS/Nonlinear/BBL/ssw_bbl.h:510`의 대입식. `RMF1-810`의 코드 근거도 같은 줄을 인용한다. |
| `models/ROMS/source-analysis/roms_bottom_boundary_layer.md:37` | `Ubot`·`Vbot`·`Ur`·`Vr` 출력 근거가 `ssw_bbl.h:895–903`이었다. | 범위를 `ssw_bbl.h:894–903`으로 고쳤다. | 894행은 `Ubot(i,j)=Ub(i,j)*anglew`이다. 895·902·903행은 각각 `Ur`·`Vbot`·`Vr` 대입이다. `RMF1-948`의 원문 범위는 이 네 대입을 포함한다. |
| `models/ROMS/source-analysis/roms_bottom_boundary_layer.md:75` | SG를 성층을 고려한 BBL이라고 단정했다. 파일 전체 줄 수와 변수명만 붙였다. | 소스 머리말이 파랑 경계층 해의 2층 와점성 분포를 설명한다는 문장으로 고쳤다. | `ROMS/Nonlinear/BBL/sg_bbl.h:10–13`은 `2-layer eddy viscosity`를 명시한다. 같은 파일 17–19행의 `stratified`는 참고 논문 제목이다. `RN1-038`의 수정안은 코드 구조와 적용 주장을 구분한다. |

보완 목록은 없다.

## roms_wetting_drying.md — 완료

- 대조한 줄 수: 작업 시작 시점 `git diff -U0 HEAD`의 추가 줄 91줄이다. 범위는 위의 대상 줄 표와 같다.
- 정정 수: 2줄이다.
- 보완 수: 0줄이다.
- 차이 표 15행의 분류와 결론을 입력, 혼합·경계·강제, 출력·메타데이터, 이론·수치, 도구 안내 보고서의 최종 §5 및 전수 검증 기록과 대조했다.
- 본문 수정은 `RI1-1047`, `RMF1-939`–`RMF1-943`의 수정안과 대조했다. DCRIT 기본값 주장과 다른 모델 대비 성능·하향 권고를 제거한 변경은 해당 수정안에 근거한다.
- `RMF1-942`는 기존 마스크 합성식을 유지하도록 한 수정안과 같다.
- 본문의 코드 인용과 세 Fortran 발췌 블록을 원문에서 대조했다. 위키 인용문은 `WET_DRY.wiki:13`과 Markdown 변환본 22행의 표시 글자와 같다.
- `RMF1-803`의 A 판정은 `ROMS-git-verify-A7.md:72`와 같다. 커밋 `71bd6f1e`의 날짜는 2008-03-18이다. `b7229401`의 날짜는 2008-12-05이다. `d2530aaa`의 날짜는 2022-02-27이다. `roms-3.1:ROMS/External/varinfo.dat:2445–2451`의 옛 출력 이름과 현재 YAML의 이름을 대조했다.
- 이 노트의 차이 표에는 E 행이 없다.
- `wetdry.F`의 928줄 표기는 해당 파일의 `wc -l` 결과와 같다.
- 상대 링크의 대상 파일은 모두 존재한다. 절대 로컬 경로와 `[[`는 없다. 미수행 작업을 남기는 한계 문장은 없다. Mermaid 블록은 없다.
- 기계 확인 후보 판정: 사용자 제공 후보 없음.
- 미해결 항목: 없음.

### 정정 목록

아래 줄 번호는 시작 시점과 정정 후가 같다. 두 줄 모두 끝에 `[10-14 전수 검증 정정]`을 붙였다. Frontmatter의 표지는 YAML 주석으로 붙였다.

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| `models/ROMS/source-analysis/roms_wetting_drying.md:8` | `verification_method`가 DCRIT 입력 예제 0.10 m를 `WET_DRY.md`의 내용으로 묶었다. | One-way flux의 위키 근거와 DCRIT 입력 예제의 `User/External/roms.in:404` 근거를 분리했다. | `WET_DRY.wiki:12`는 0.10 m를 default라고 부른다. `User/External/roms.in:404`는 `DCRIT == 0.10d0`를 m 단위로 지정한다. 입력 보고서 `RI1-1047`의 수정안은 이를 코드 기본값이 아닌 입력 예제로 구분한다. |
| `models/ROMS/source-analysis/roms_wetting_drying.md:93` | `rmask_wet_avg`를 `AINT(avg·cff)`로 이진화한다고 적었다. | SOLVE3D 경로의 실제 대입 `wetdry(i,j)=AINT(rmask_wet_avg(i,j)*cff)`를 적었다. | `ROMS/Nonlinear/wetdry.F:217`의 SOLVE3D 조건, 221–234행의 누적, 254–258행의 종료 후 계산. 258행의 대입 대상은 `wetdry`이며 `rmask_wet_avg`가 아니다. |

보완 목록은 없다.

## 최종 집계

| 노트 | 대조한 대상 줄 | 정정 줄 | 보완 줄 |
|---|---:|---:|---:|
| `roms_include_cppdefs-differences-1.md` | 264 | 0 | 1 |
| `roms_bottom_boundary_layer.md` | 100 | 3 | 0 |
| `roms_wetting_drying.md` | 91 | 2 | 0 |
| 합계 | 455 | 5 | 1 |

- 대조한 대상 줄 수는 작업 시작 시점에 고정한 범위에서 셌다. 정정·보완 줄 수는 대상 노트의 해당 표지가 있는 줄에서 셌다.
- 세 노트의 차이 표 278행은 최종 보고서와 분류·결론이 일치한다. 이 수는 230행·33행·15행의 합계이다. 노트에 추가한 git 근거와 근거 강도는 해당 확정 판정과 별도로 대조했다.
- 세 노트의 frontmatter는 YAML 파싱을 통과했다. 차이 표의 각 행은 6칸이다.
- 대상 노트의 상대 링크 검사에서 누락 파일은 없다. 절대 로컬 경로, `[[`, 미수행 작업을 남기는 한계 문장은 없다.
- 읽기 전용 `git diff --check HEAD --`의 지정 파일 검사에서 오류는 없다.
- 대상 줄의 대조를 모두 마쳤다. 미해결 항목은 없다.
