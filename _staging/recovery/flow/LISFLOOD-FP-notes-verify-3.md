# LISFLOOD-FP 사용자 매뉴얼 노트 전수 검증

- 대상: `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md`.
- 대상 줄: 검증 시작 시 `git diff -U0 HEAD -- models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md`의 모든 추가 줄.
- 상태: 대조 완료.
- 판정 기준: 사용자 지정 원문, 최종 결론, 보고서 수정안, 10-21 Claude 수정 흐름도.
- 기록 방식: 검증 시작 시 줄 번호와 최종 노트 줄 번호는 같다.

검증 시작 시 추가 줄은 312줄이다. 이 수는 지정한 `git diff -U0 HEAD`에서 파일 머리행을 제외한 `+` 줄을 센 값이다. 차이 표는 469–605행의 137행이다. 차이 표의 분류는 A 45행, B 54행, C 24행, D 3행, E 4행, F 7행이다. 이 수는 노트 표와 배정 2의 행 ID를 대조하여 셌다.

기계 확인 후보 판정: `CMakeLists.txt:4`의 `if(NOT DEFINED CMAKE_CUDA_ARCHITECTURES)`는 현재 원문의 4행과 일치한다. 5행은 `set(CMAKE_CUDA_ARCHITECTURES 61)`이다. 이 후보는 검사기 오판이다. 해당 인용은 유지한다.

## 대조 범위

추가 312줄을 모두 대조했다. frontmatter 6줄을 포함했다. 빈 줄 37줄도 대상 줄 수에 포함했다. 줄 수의 기준은 검증 시작 시 저장한 `git diff -U0 HEAD`의 추가 줄 목록이다.

아래 번호는 최종 노트의 줄 번호이다. 정정은 모두 같은 줄 안에서 처리했다. 검증 시작 시 번호와 최종 번호는 같다.

| 구간 | 대조한 추가 줄 수 | 대상 줄 번호 |
|---|---:|---|
| frontmatter | 6 | 7, 10, 12–15 |
| 문서 범위와 판 구분 | 6 | 21, 23–27 |
| 1. 모델과 솔버 | 14 | 33, 45–47, 59–67, 69 |
| 2. parameter file | 38 | 83, 85–86, 88, 92–104, 113, 117, 129–130, 138, 140–146, 159, 168, 172, 179, 181, 183, 193, 200, 205 |
| 3. 입력 파일 | 22 | 211, 236, 247, 249, 251–255, 276, 284–290, 294–298 |
| 5. 실행과 출력 | 49 | 320, 322, 324–325, 328, 336–339, 341, 345–357, 363, 365, 367–369, 375–391, 393, 395, 397–398 |
| 6. 빌드 | 10 | 404, 406, 411, 422, 424, 427–431 |
| 7. 연결 요약 | 11 | 439–449 |
| 차이 표 안내 | 19 | 450–468 |
| 차이 표 | 137 | 469–605 |
| 합계 | 312 | 위 목록 전체 |

기존 문장에서 삭제된 92줄도 교체 근거를 확인하는 데 사용했다. 이 수는 검증 시작 시 같은 diff의 삭제 줄 수이다. 보고서 수정안이 삭제를 뒷받침하지 않는 `.pram` 필드 뜻과 보·교량 입력 설명은 복구했다.

## 정정·보완 내역

정정은 19줄이다. 인용 보완은 3줄이다. 합계 22줄은 모두 위 대상 줄 목록에 속한다. 건수는 아래 내역과 노트의 `[10-21 전수 검증 정정]`·`[10-21 전수 검증 보완]` 표식을 대조하여 셌다.

코드의 `파일:줄`은 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/` 아래를 뜻한다. `v8.0:`은 사용자가 지정한 이전 배포본 루트를 뜻한다. 문서 쪽은 사용자가 지정한 쪽 이미지에서 판독했다. DOCX 쪽은 LibreOffice 변환본 기준이다. `bf804e23:` 인용은 사용자가 지정한 커밋의 노트 원문이다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:7` — 정정.
  전 → 후: “키워드·기본값은 PDF 표(Table 5–14) verbatim.” → “검증 시작 시 git diff -U0 HEAD의 추가 312줄을 대조했다.” 검증 방법에 쪽 이미지·배포본 원문·최종 결론·수정안을 명시했다.
  근거 원문: 검증 시작 시 diff의 추가 줄 목록은 위 대조 범위와 같다. 노트 94–104행은 원문 표의 한국어 설명과 코드 기본값을 함께 적는다. 원문을 그대로 옮겼다는 설명은 이 내용에 맞지 않는다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:46` — 정정.
  전 → 후: 조건 없이 설명한 CFL 상한 → `if(MH > Solverptr->DepthThresh)` 조건의 상한으로 고쳤다. 조건을 통과하지 않을 때 `Solverptr->Tstep=Solverptr->InitTstep;`가 적용됨을 복구했다.
  근거 원문: `fp_acc.cpp:250–276`의 조건문과 `locT=cfl*Parptr->dx/(sqrt(g*MH));`. 최종 LT1-074와 theory 보고서 §4 LT1-403은 수심 조건을 구분한다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:69` — 정정.
  전 → 후: 변수 정의 인용 `(p.11)` → `(user manual.pdf p.10)`.
  근거 원문: user manual.pdf p.10의 식 (2) 아래에 A·Q·h·z·x·t·n·R의 정의가 있다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:92` — 정정.
  전 → 후: “문서 기본값(Buscot)” → “문서 기본값”. 설명 열에 PDF p.15–16 표 5를 붙였다. 적용 열은 문서의 적용 범위로 명시했다.
  근거 원문: user manual.pdf p.15–16 표 5의 saveint 기본값은 1000이다. Buscot 예제의 saveint는 10000.0이다. 두 값을 같은 뜻으로 표시할 수 없다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:113` — 정정.
  전 → 후: 표 안의 이스케이프 없는 논리 OR → Markdown 원문에서 `\|\|`로 표시했다. 조건식의 뜻은 유지했다.
  근거 원문: `infevap.cpp:371`의 `if(h0<Solverptr->DepthThresh || Sfy>=Parptr->RouteSfThresh || Sfx>=Parptr->RouteSfThresh)`. 이스케이프 전에는 두 OR 연산자가 표의 열 구분자로 해석된다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:140` — 보완.
  전 → 후: “증발 시계열 파일” → “증발 시계열 파일(user manual.pdf p.18 표 8)”.
  근거 원문: user manual.pdf p.18 표 8의 `evaporation` 행. 표 8은 p.17에서 p.18로 이어진다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:193` — 정정.
  전 → 후: 표 안의 이스케이프 없는 논리 OR → Markdown 원문에서 `\|\|`로 표시했다. 조건식의 뜻은 유지했다.
  근거 원문: `iterateq.cpp:190`의 `if (Solverptr->t >= Parptr->MassTotal || Statesptr->mint_hk == OFF)`. 이스케이프 전에는 OR 연산자가 표의 열 구분자로 해석된다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:251` — 정정.
  전 → 후: “.bci의 QVAR는 m²s⁻¹” → “latlong이 꺼져 있으면 m²s⁻¹”. latlong이 켜진 경우의 m³s⁻¹ 조건을 복구했다.
  근거 원문: user manual.pdf p.26은 latlong을 쓸 때 QVAR의 .bci 단위를 m³s⁻¹로 구분한다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:276` — 정정.
  전 → 후: Type·m의 뜻을 삭제한 상태 → Type 1은 직사각형, Type 2는 power 단면으로 복구했다. `depth = r*width^p`를 복구했다. 선택 항목 m의 뜻과 문서 기본값 1을 복구했다. 대상이 불명확한 “수심 비” → 같은 폭 w에서 지역 2와 지역 0의 폭 기반 깊이식 비 `w^0.03`으로 명시했다.
  근거 원문: `bf804e23:models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:253`; user manual.pdf p.28–29 표 13과 예제; `input.cpp:2389–2406`; `sgc.cpp:446`. 예제의 두 지역은 r=0.78이 같다. p는 0.30과 0.33이다. files-output 보고서 §4 LI2-059–066은 필드 뜻의 삭제를 지시하지 않는다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:294` — 정정.
  전 → 후: 방향 태그와 문서의 전형값을 삭제한 상태 → N/E/S/W·NF/EF/SF/WF·nb/eb/sb/wb를 복구했다. 보 계수 범위 0.5–1.7과 광정 위어 계수 1.4를 복구했다. modular limit 0.9를 문서의 전형값으로 표시했다. 교량 Cd 0.8과 전이 상한 1.5를 문서의 전형값으로 복구했다. 입력값과 자동 기본 대입을 구분했다.
  근거 원문: `bf804e23:models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:267`; user manual.pdf p.29–30; user manual +bridge.docx p.29·32; `input.cpp:161–246`. files-output 보고서 §4 LI2-069–079의 수정 대상은 입력값을 자동 기본값으로 적은 설명이다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:336` — 보완.
  전 → 후: v8.0의 CFL 재설정과 파서의 순차 처리 설명 → 해당 구문을 가리키는 인용을 붙였다.
  근거 원문: `v8.0:pars.cpp:571–583,954`의 FV1·DG2 선택과 명령 줄 처리. 현재 대응은 `pars.cpp:582–586,630–636,642–656,1027–1036`이다. v8.0의 CFL 0.5·0.33은 `v8.0:pars.cpp:574,582`에 있다. 최종 LV1-184와 같다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:341` — 정정.
  전 → 후: OpenMP 설명의 PDF p.34 → p.35. 삭제된 문서 기본 설정 → 사용 가능한 모든 공유메모리 코어를 쓴다는 설명을 복구했다.
  근거 원문: user manual.pdf p.35는 기본 설정에서 모든 공유메모리 코어를 쓴다고 적는다. 같은 쪽은 `OMP_NUM_THREADS`로 코어 수를 지정한다고 적는다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:347` — 정정.
  전 → 후: `source-analysis/lisflood-fp-io-boundary.md:132–134` → `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md:132–134`.
  근거 원문: 지정된 `git show bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-io-boundary.md`의 132–134행은 checkpoint 설명이다. 현재 같은 번호의 행은 .bci 절이다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:349` — 정정.
  전 → 후: “총 침수 시간과 이 손실 누계” → “총 침수 시간과 침투·증발 누적 손실”.
  근거 원문: `chkpnt.cpp:254,283–286`의 대상은 `totalHtm`, `InfilTotalLoss`, `EvapTotalLoss`이다. `VersionHistory.h:19`의 `LF_CheckVersion`은 0이다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:367` — 정정.
  전 → 후: `.mxe` 인용 `lisflood2/lis2_output.cpp:478–506` → `lisflood2/lis2_output.cpp:478–535`.
  근거 원문: `lisflood2/lis2_output.cpp:534–535`에 확장자를 `.mxe`로 지정하는 writer가 있다. 앞 인용 범위에는 이 분기가 없었다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:368` — 정정.
  전 → 후: `.maxtm` 인용 `lisflood2/lis2_output.cpp:478–510` → `lisflood2/lis2_output.cpp:478–540`.
  근거 원문: `lisflood2/lis2_output.cpp:539–540`에 확장자를 `.maxtm`으로 지정하는 writer가 있다. 앞 인용 범위는 504–509행의 특정 출력 분기까지만 포함했다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:404` — 보완.
  전 → 후: 현대 빌드 설명에 붙은 `README.md:1–2` → `README.md:1–2,64`, `VersionHistory.h:34`, `CMakeLists.txt:72–77`.
  근거 원문: `README.md:1–2`는 CMake 3.13 요구 조건이다. `README.md:64`는 CUDA 빌드 안내이다. `VersionHistory.h:34`는 FV1·DG2 도입 이력이다. `CMakeLists.txt:72–77`은 CUDA 대상의 구성 근거이다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:429` — 정정.
  전 → 후: CUDA 소스 목록 인용 `makefile:31–53` → `makefile:53–85`.
  근거 원문: `makefile:53–85`가 `CUDA_FILES` 목록이다. 변경 전 범위는 이 목록의 대부분을 포함하지 않았다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:452` — 정정.
  전 → 후: “DOCX 판 이력 맨 위는 5.9” → 기존 5.9 위의 8.0·2020-07-20 추가 편집 표시를 명시했다. 근거 없이 적은 8.3 DOI `10.5281/zenodo.13121119` → 배포 README가 밝힌 8.2 DOI와 8.3 변경 적용 관계로 고쳤다. 숫자 판 인용은 `VersionHistory.h:16–18`로 고쳤다. 릴리스 이름 인용은 `VersionHistory.h:23`으로 고쳤다.
  근거 원문: user manual.docx p.5의 변경 추적 표시. `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP-8.3-package/README.md:19–24`는 `source/`가 공식 8.2(`10.5281/zenodo.13121102`)에 8.3 변경을 적용한 것이라고 적는다. 이 범위에는 8.3 DOI가 없다. 최종 LB1-383·408은 문서 판과 배포판 근거를 구분한다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:511` — 정정.
  전 → 후: LV1-177의 “PDF 대조: user manual.pdf p.33과 같음.” → “PDF 대조: user manual.pdf p.34와 같음.” 결론 문장은 유지했다.
  근거 원문: user manual.pdf p.34 표 14의 `-gzip`. 최종 LV1-177의 gzip 판정과 같다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:565` — 정정.
  전 → 후: LI2-205의 `sgm_fast.cpp:3928` → `lisflood2/sgm_fast.cpp:3928`. 결론 문장은 유지했다.
  근거 원문: 현재 코드 루트 아래 실제 파일은 `lisflood2/sgm_fast.cpp`이다. 3928행의 호출을 직접 대조했다. 최종 LI2-205의 hazard 출력 근거와 같다.

- `models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md:576` — 정정.
  전 → 후: LI1-157의 `suffix res_D` → `suffix .res_D`. 항목과 원문 인용의 두 위치를 고쳤다. 결론 문장은 유지했다.
  근거 원문: user manual.pdf p.22의 원문은 “The results files all have the suffix .res_D”이다.

## 최종 판정

차이 표 137행의 ID와 분류는 [배정 2](../assign/LISFLOOD-FP-note-job-2.tsv) 및 [최종 분류](../assign/LISFLOOD-FP-final-conclusions.tsv)와 일치한다. 분류별 수는 A 45행, B 54행, C 24행, D 3행, E 4행, F 7행이다. 각 행의 결론 문장은 배정표가 지정한 `LISFLOOD-FP-conclusion-verify-*.md`의 최종 문장과 대조했다. 원문과 수식 표기 및 문서명 표기 차이는 원래 뜻을 유지한다.

A 행의 근거 판을 대조했다. 8.0 이전 문서의 코드가 배포본에 없다는 구분은 유지했다. 현재 8.3 코드와 v8.0·v8.1·v8.2 인용은 각각 지정된 원문 루트에서 확인했다.

E 행의 강도는 최종 근거와 같다. LB1-393은 중간이다. LI2-123은 중간이다. LI2-190은 약함이다. LI1-352는 강함이다. [Claude 최종 조정](../compare/LISFLOOD-FP-conclusion-claude-final.md)의 LI2-352·LI1-369·LN1-127은 이 노트의 배정 행에 없다. 이 노트의 E 행에는 최종 근거가 요구한 “8.2 결함, 8.3에서 고침” 또는 “호출되지 않는 경로” 표시의 누락이 없다. [외부 근거 최종 절](../compare/LISFLOOD-FP-external-sources.md)의 hazard 문헌 판정도 반영 내용과 같다.

본문은 해당 대조 보고서의 §4 수정안과 원문을 함께 대조했다. 경로와 줄 번호만 붙은 문장도 원문을 열었다. 교체된 기존 문장은 지정된 `bf804e23` 노트와 대조했다. 부정·조건·수량·단위·부호 및 `CUDA`·`METAL_ENABLED`·`_NETCDF` 분기를 확인했다. 8.2에서 8.3으로 달라진 부분은 8.3 배포 문서와 패치로 구분했다.

[실행 흐름 기록](LISFLOOD-FP-callflow.md)의 §4와 Claude 렌더 확인 문단 및 §6을 확인했다. 대상 노트에는 Mermaid 블록이 없다.

노트의 상대 링크 47개는 모두 실제 파일을 가리킨다. 이 수는 Markdown 링크 43개와 frontmatter의 related 경로 4개를 합한 값이다. 금지된 절대 홈 경로·홈 축약 경로·위키 링크 표기는 없다. 요청에서 금지한 미완료 한계 문장은 없다. LB1-387의 HEC-RAS 문장은 문서의 적용 사례와 현재 코드의 검증을 구분하는 최종 결론이므로 유지했다.

최종 `git diff -U0 HEAD`의 추가 줄 목록은 최초 312줄 목록과 같다. 정정·보완한 22줄은 모두 이 목록에 속한다. 모든 표식은 해당 줄 끝에 있다. 차이 표 행의 표식은 결론 문장 칸 끝에 있다. `git diff --check -- models/LISFLOOD-FP/manual-notes/lisflood-fp-user-manual.md`는 오류 없이 끝났다.

대상 노트의 모든 대상 줄에 대한 대조를 완료했다. 미해결 항목은 없다.
