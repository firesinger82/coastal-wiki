# SWASH 노트 전수 대조 5

- 작업일: 2026-10-15.
- 대상: 사용자 지정 SWASH 노트 네 파일.
- 대조 기준: 작업 시작 시 `git diff -U0 HEAD -- <노트>`의 모든 추가 줄과 삭제 줄이다. 새 파일은 전체 줄이다. 빈 줄과 frontmatter 줄도 센다.
- 원문 기준: 현재 SWASH 소스, 지정 공개 저장소 사본의 과거 커밋, 매뉴얼 판독 기록과 쪽 이미지다.
- 결론 기준: 지정 보고서의 마지막 `전수 검증 기록 (10-15, …)`을 적용한다.
- 기록 방식: 노트별 완료 시 대조 줄 수, 정정 수, 보완 수, 변경 근거와 기계 확인 후보 판정을 덧붙인다.

## 노트별 대조 결과

### 완료: swash-explicit-depthavg-flow.md

- 노트: `models/SWASH/source-analysis/swash-explicit-depthavg-flow.md`.
- 대조: 추가 113줄과 삭제 6줄로 총 119줄이다. 정정은 6줄이다. 보완은 1줄이다. 정정과 보완을 중복 집계하지 않았다.
- 추가 줄의 시작 시 번호: 7–8, 88–91, 223–226, 247–248, 271–282, 303–304, 308–312, 321–402. 빈 줄과 frontmatter를 포함했다.
- 7–8행은 원본 헤더·버전과 반영 보고서로 확인했다. 88–91행은 초기화·입력·선형 모드 보정으로 확인했다. 223–226행은 Perot 호출과 재구성·이류 루프로 확인했다. 247–248행은 격자 거리 계산으로 확인했다. 271–282행은 세 격자의 CFL 계산과 마스크·수심 정의로 확인했다. 303–304·308–312행은 ITEST 조건·수위 합·에너지 합으로 확인했다. 321–332행은 선언·연결 노트·보고서의 판 정보로 확인했다. 333–402행의 표 머리와 68개 행은 각 원문 및 최종 보고서와 대조했다.
- 차이 표의 분류는 최종 보고서와 같다. ST1-310의 E·중간과 ST2-039의 E·강함은 E2 판정과 같다. A 행은 없다. 과거 커밋 인용은 지정 공개 사본의 원문으로 확인했다.
- 수식·부호·수심·단계 수는 swashtech PDF p.19–22,24–26,44,47,49,55,58–59,63–64,71,75,77,80–81,91–95,98,103,108과 swashuse PDF p.96,98–99,122,135–136,146,161의 쪽 이미지로 확인했다. 나머지 문장과 누락 범위는 해당 판독 기록·추출 텍스트·보고서로 확인했다.
- 상대 링크의 대상 파일은 모두 존재한다. 절대 홈 경로와 `[[`는 없다. Mermaid 블록은 없다. RF-022의 “미확인”은 반영 전 문장의 인용이다. 현재 상태에 대한 미완 항목은 없다.

정정·보완 목록의 줄 번호는 대조 후 노트 기준이다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| swash-explicit-depthavg-flow.md:224 | 정정 | 면 법선 속도를 재구성 → 면 법선 속도 u0로 셀 중심 속도 벡터를 재구성 | `src/SwashExpDepUflow.ftn90:224–226`의 cell-based velocity vector와 perot 호출. `src/SwashUServ.ftn90:148–157`의 두 벡터 성분 합산과 셀 면적 나눗셈. |
| swash-explicit-depthavg-flow.md:361 | 정정 | 추가항은 §3에 기록한다 → theory-framework 보고서 §3 링크 | 노트 §3은 이류 절이다. 보고서 §3은 “코드에만 있는 처리”이다. `src/SwashExpDep2DHflow.ftn90:920–959,1354–1360`에 밀도·기압·식생·다공체 항이 있다. |
| swash-explicit-depthavg-flow.md:366 | 정정 | 시간 가중치·보간은 §3에 기록한다 → 이 표의 ST1-296에 정리되어 있다 | `src/SwashExpDep2DHflow.ftn90:991–1002`의 이전·현재 가중치와 네 점 보간. |
| swash-explicit-depthavg-flow.md:376 | 정정 | 일정 밀도 문장 인용을 삭제한다 → p.19의 실제 원문을 사실로 서술 | swashtech PDF p.19의 `barotropic flow of an incompressible fluid`. theory-framework 최종 검증 기록의 ST1-298 정정. |
| swash-explicit-depthavg-flow.md:389 | 정정 | 아래 전개가 계수를 확인한다 → 결합식의 압력 경사 계수는 1/2 | 이 노트에는 그 전개가 없다. swashtech PDF p.92 식 (5.42)와 `src/SwashExpDepUflow.ftn90:520–521`의 gmat 계수. |
| swash-explicit-depthavg-flow.md:397 | 정정 | 면 속도만 재구성 → 면 수심을 곱하지 않은 면 속도로 셀 중심 속도 벡터 재구성 | `src/SwashUServ.ftn90:148–157`의 입력 u와 출력 uvc. swashtech PDF p.98의 수심 가중 재구성식과 구별했다. C 판정은 유지했다. |
| swash-explicit-depthavg-flow.md:400 | 보완 | “아래 면적 가중 경사”의 원문 위치 없음 → `src/SwashExpDepUflow.ftn90:450–478` 인용 추가 | 456–470행은 상류 꼭짓점의 면적 가중 속도다. 474–478행은 두 방향의 두 경사다. 결론 범위는 그대로다. |

삭제 줄의 근거:

- HEAD 7행: 기존 검증 방법은 보존하고 보고서 반영일을 추가했다. 반영 기록 4와 일치한다.
- HEAD 218행: 이류 재구성과 Coriolis 플럭스 재구성을 혼합한 문장을 나눴다. ST2-146 수정안과 `SwashExpDepUflow:226,948–949`가 근거다.
- HEAD 239행: circumcenter 사이 직접 거리라는 설명을 두 중심–면 중점 거리 합으로 고쳤다. ST2-150 수정안과 `SwanGridFace:384–411`이 근거다.
- HEAD 262행: CFL 설명은 보존했다. 선언 모듈의 추정은 RF-022와 `SwashModule1:250,651`로 교체했다.
- HEAD 283행: 체적 진단이라는 설명은 ST1-310과 `SwashExpDep1DHflow:1626`, `SwashExpDep2DHflow:4905`의 면적·길이 없는 수위 합으로 교체했다. 에너지 설명은 보존했다.
- HEAD 295행: 미검수·source-needed 목록은 선언·단계 선택·선형 솔버 노트의 확인된 연결로 교체했다. RF-022·ST1-324 수정안과 기존 선형 솔버 노트가 근거다. 범위 밖 빌드·실행을 후속 과제로 남기지 않았다.

기계 확인 후보 판정:

- `src/SwashExpDep2DHflow.ftn90:3126` 후보: 오탐이다. 실제 인용은 `8756667:src/SwashExpDep2DHflow.ftn90:3126`이며 원문은 `if ( nm > 1 ) then`이다. “에도”는 인용문이 아니다. 유지했다.
- `src/SwashExpDep2DHflow.ftn90:4805` 후보: 오탐이다. 실제 인용은 `25c79e7:src/SwashExpDep2DHflow.ftn90:4805`이며 `vol = vol + s1(nm)`이다. 11.01 표기는 E2 보고서와 같다. 유지했다.
- `src/SwashExpDep2DHflow.ftn90:4905` 후보: 오탐이다. `7949227:src/SwashExpDep2DHflow.ftn90:4905`와 현재 원문은 모두 `vol = vol + s1(nm)`이다. “가 모두 같다”는 설명이다. 유지했다.
- `src/SwashExpDep1DHflow.ftn90:1133` 후보: 오탐이다. 실제 인용은 `8756667:src/SwashExpDep1DHflow.ftn90:1133`이며 `vol = vol + s1(nm)`이다. 유지했다.
- `src/SwashExpDep1DHflow.ftn90:1625` 후보: 오탐이다. 실제 인용은 `25c79e7:src/SwashExpDep1DHflow.ftn90:1625`이며 `vol = vol + s1(nm)`이다. 유지했다.
- `src/SwashExpDepUflow.ftn90:1048` 후보: 오탐이다. 실제 인용은 `8756667:src/SwashExpDepUflow.ftn90:1048`이며 `vol = vol + s1(icell)`이다. 유지했다.
- `src/SwashImpDepUflow.ftn90:1110` 후보: 오탐이다. 실제 인용은 `8756667:src/SwashImpDepUflow.ftn90:1110`이며 `vol = vol + s1(icell)`이다. 유지했다.
- `src/SwashExpLayUflow.ftn90:2062` 후보: 오탐이다. 실제 인용은 `8756667:src/SwashExpLayUflow.ftn90:2062`이며 `vol = vol + s1(icell)`이다. 유지했다.
- `src/SwashImpLayUflow.ftn90:2127` 후보: 오탐이다. 실제 인용은 `8756667:src/SwashImpLayUflow.ftn90:2127`이며 `vol = vol + s1(icell)`이다. 유지했다.

### 완료: swash-wetting-drying-runup.md

- 노트: `models/SWASH/source-analysis/swash-wetting-drying-runup.md`.
- 시작 diff의 대조는 추가 57줄과 삭제 12줄로 69줄이다. 사용자 항목 6에 따라 남아 있던 미완 문장 191·220행의 수정 전후도 대조했다. 최종 diff는 추가 61줄과 삭제 16줄로 총 77줄이다. 추가된 두 수정 쌍과 diff 문맥 재배치로 표시된 빈 줄 두 쌍을 포함한 수다. 빈 줄은 내용 변경이 없다. 정정은 3줄이다. 보완은 0줄이다.
- 추가 줄의 시작 시 번호: 7–8, 46–48, 81, 127, 167, 171–173, 199, 211, 213, 215–219, 221–258. 빈 줄과 frontmatter를 포함했다.
- 7–8행은 원본 커널·반영 기록 8로 확인했다. 46–48·199행은 Newton 선택과 epshu 설정으로 확인했다. 81행은 쇄파 입력·준비 분기로 확인했다. 127·219행은 swashuse PDF p.118과 RunupHeight의 oned 조건으로 확인했다. 167·215행은 Services의 제한자 식으로 확인했다. 171–173·211행은 COMPUTE 준비와 hindun 대입으로 확인했다. 216–218행은 Init의 초기값으로 확인했다. 221–258행의 설명·표 머리·27개 행은 최종 보고서 및 해당 원문과 대조했다.
- 표 분류와 결론 범위는 각 최종 보고서와 같다. SG1-142의 B와 SI2-159의 C는 각각의 보고서 판정을 유지했다. A·E 행은 없다. SG1-137·140과 SO1-191의 과거 인용은 `8756667` 원문과 AD 판정에 맞는다.
- swashuse PDF p.33,88,119,130,140–142와 swashtech PDF p.58–59,61,74–75,80,98의 식·수치·부호를 쪽 이미지로 확인했다. 다른 인용 쪽은 판독 기록과 추출 텍스트로 확인했다. 두 유출 면 반례의 합은 `0.6+0.6=1.2`이다.
- 상대 링크의 대상 파일은 모두 존재한다. 절대 홈 경로와 `[[`는 없다. Mermaid 블록은 없다. 미완 항목은 없다. 지정된 기계 확인 후보는 이 노트에 없다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| swash-wetting-drying-runup.md:81 | 정정 | BDF이면 β=0.15라는 압축 설명 → isurf=1·β 미지정·기존 BDF 지정 조건을 분리했다. 중앙차분 선택에 pnums(7)=1도 적었다. | `src/SwashReadInput.ftn90:911–923`; `src/SwashCheckPrep.ftn90:1072–1091`. SI2-159·164 및 SG1-121·142의 최종 결론. |
| swash-wetting-drying-runup.md:191 | 정정 | flou=0 가정과 기본값 미확인 → 초기값 -9999 및 그 값을 대입한 가드 조건 | `src/SwashCheckPrep.ftn90:3085`의 `flou = -9999.`. `src/SwashUpdDepu.ftn90:170`과 `src/SwashUpdateDepths.ftn90:301`의 서로 다른 조건. 두 조건의 무조건적 동등성은 주장하지 않는다. |
| swash-wetting-drying-runup.md:220 | 정정 | flou 기본값 확인 필요 → 준비 단계 초기값 -9999와 §6 연결 | `src/SwashCheckPrep.ftn90:3085`. 사용자 항목 6에 따라 기존 미완 항목을 사실로 바꿨다. |

삭제 줄의 근거:

- HEAD 7행: 기존 검증 방법에 반영 기록을 추가했다.
- HEAD 45·194행: epshu=epsdry의 무조건적 설명을 SG1-130과 `SwashCheckPrep:1219`의 inewt=0 조건으로 고쳤다. `SwashUpdateDepths:151–188`도 같은 조건 아래에서 동기화한다.
- HEAD 78행: β=0.15 예외를 SI2-159·164 수정안대로 반영했다.
- HEAD 124·212행: 2D·비구조 RUNUP의 미확인 문장을 SO1-184, swashuse PDF p.118, `SwashRunupHeight:88–90,144–154`의 1D 조건으로 교체했다.
- HEAD 164·210행: 제한자 정의의 미확인 문장을 SI2-243과 `SwashServices:387–443`으로 교체했다.
- HEAD 168·206행: 영구 침수 기록을 한 COMPUTE 구간의 기록으로 고쳤다. SO1-266·299와 `SwashMain:158`, `SwashCheckPrep:3108`, `SwashUpdateDepths:805`가 근거다.
- HEAD 208행: 미확인 절 제목을 확인된 입력·출력 연결로 바꿨다.
- HEAD 211행: 임계값 미확인 문장을 ST2-358과 `SwashInit:121–123`의 세 초기값으로 교체했다.

### 완료: swash-tech-documentation-overview.md

- 노트: `models/SWASH/manual-notes/swash-tech-documentation-overview.md`.
- 대조: 추가 38줄과 삭제 13줄로 총 51줄이다. 정정은 3줄이다. 보완은 2줄이다.
- 추가 줄의 시작 시 번호: 7–8, 21, 39, 56, 59, 67–74, 78–80, 82, 91–93, 95, 98–113. 빈 줄과 frontmatter를 포함했다.
- 7–8행은 현재 대조 자료와 반영 기록 1로 확인했다. 21·39·59·78–80·98–99행은 기술문서 각 장의 실제 내용으로 확인했다. 56행은 PDF p.13–14의 이류·보존 설명으로 확인했다. 67–74행은 PDF p.108과 사용자 설명서 p.96–97 및 입력·준비 분기로 확인했다. 82행은 PDF p.10의 §1.5와 일치한다. 91–93행은 PDF p.115–116과 SIP·BiCGSTAB 호출로 확인했다. 100행은 Geometrics의 원문과 일치한다. 102–113행의 설명·표 머리·4개 행은 최종 보고서와 대조했다.
- 표의 C·B 판정은 유지했다. A·E 행은 없다. `sigmal layers`는 PDF p.109 이미지의 실제 철자다. PDF p.10의 1998년과 참고문헌 번호도 이미지와 같다.
- 상대 링크의 대상 파일은 모두 존재한다. 입력 파싱 노트의 ST2-356 행도 존재한다. 절대 홈 경로와 `[[`는 없다. Mermaid 블록은 없다. “미완성 장”은 원문에 본문이 없다는 사실이다. 검수 미완 항목이 아니다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| swash-tech-documentation-overview.md:7 | 정정 | 현재 없는 /tmp/swashtech.txt의 5010줄과 모호한 페이지 기준 → 현재 판독 기록·추출 텍스트·이미지·소스·최종 보고서 대조 방법 | 지정된 `_staging/recovery/read/SWASH/swash/doc/swashtech.pdf/`와 추출 텍스트를 사용했다. PDF p.65/인쇄 p.57 등으로 두 쪽 체계를 확인했다. 과거 임시 추출물의 줄 수를 현재 검증 근거로 남기지 않았다. |
| swash-tech-documentation-overview.md:93 | 보완 | 보고서·별도 노트만 연결 → BiCGSTAB의 실제 호출 세 곳 추가 | `src/SwashExpDepUflow.ftn90:1440`, `src/SwashImpDepUflow.ftn90:1749`, `src/SwashExpLayUflow.ftn90:2450`. |
| swash-tech-documentation-overview.md:98 | 보완 | 다섯 장에 p.65만 인용 → p.65,109,111,113,117 인용 | 각 쪽의 제4·8·9·10·12장 준비 중 또는 빈 본문 문장. |
| swash-tech-documentation-overview.md:111 | 정정 | 목록에 추가한다·확인 범위를 표시한다 → 제4장 포함 사실과 실제 연결한 면적 식 | ST1-321 수정안, swashtech PDF p.65, `src/SwashGeometrics.ftn90:325–328`. |
| swash-tech-documentation-overview.md:113 | 정정 | 아래 조건 → 조건 | 원문 조건은 같은 행의 앞선 코드 칸에 있다. `src/SwashCheckPrep.ftn90:1072–1109`와 ST2-379의 적용 범위는 유지했다. |

삭제 줄의 근거:

- HEAD 7행: 검증 방법에 이번 보고서 반영을 덧붙인 줄이다. 이번에는 실제 사용한 자료로 다시 정정했다.
- HEAD 20행: 과거 AUDIT-LEDGER의 첫 노트 상태를 지웠다. 문서의 부분 완성 설명은 보존했다. 반영 기록 1과 사용자 항목 6에 맞는다.
- HEAD 38행: “거의 빈약”을 ST1-319 수정안과 PDF p.65–66의 실제 내용으로 고쳤다.
- HEAD 55행: 비선형 안정성 일반화를 ST1-320 수정안의 설계 동기로 고쳤다.
- HEAD 58행: deep-dive 후보를 ST1-319의 확인된 제4장 범위로 교체했다.
- HEAD 66행: 분산 분석 예시와 일반 기본값을 ST2-379 수정안대로 구분했다. PDF p.108의 인용은 보존했다.
- HEAD 70행: sigma를 원문 sigmal로 고쳤다. 제8장의 실제 상태와 §1.5 설명을 분리했다. ST2-209와 PDF p.10,109가 근거다.
- HEAD 72행: 보강 필요 항목을 제8장 본문이 비었다는 확인된 사실로 교체했다. ST2-209와 사용자 항목 6에 맞는다.
- HEAD 81행: SWAN 복사 추정과 SIP 대상의 압력 한정을 지웠다. ST2-216·225와 실제 dq·u1·v1·BiCGSTAB 호출로 교체했다. 깨진 위키 링크도 실제 파일 링크로 교체했다.
- HEAD 83행: 후속 절 제목을 문서 내용 범위로 바꿨다.
- HEAD 86행: ST1-321에 따라 미완성 장 목록에 제4장을 추가했다. 보강 할 일은 확인된 내용 범위로 교체했다.
- HEAD 87–88행: 과거 진행 상태와 후속 후보를 지웠다. 반영 기록 1 및 사용자 항목 6에 맞는다.

기계 확인 후보 판정:

- `manual-notes/swash-tech-documentation-overview.md:38`의 `⚠ 거의 빈약`: 오탐이다. 수정 전 HEAD 38행의 표 셀 인용이다. 작업 시작 diff의 삭제 줄과 일치한다. 현재 제4장 설명은 PDF p.65–66에 맞다. 인용은 유지했다.
- `manual-notes/swash-tech-documentation-overview.md:86`의 미완성 목록: 오탐이다. 수정 전 HEAD 86행의 앞부분 인용이다. 작업 시작 diff의 삭제 줄과 일치한다. 현재 목록에는 제4장이 포함되어 있다. 인용은 유지했다.

### 완료: swash-boundary-spectral-transfer.md

- 노트: `models/SWASH/source-analysis/swash-boundary-spectral-transfer.md`.
- 시작 diff의 대조는 추가 30줄과 삭제 4줄로 34줄이다. 함수 개수 오류의 연결 문장 161행과 사용자 항목 6에 해당하는 196·201–202행의 수정 전후도 대조했다. 최종 diff는 추가 35줄과 삭제 9줄로 총 44줄이다. 추가된 네 수정 쌍과 diff 문맥 재배치로 표시된 빈 줄 한 쌍을 포함한 수다. 빈 줄은 내용 변경이 없다. 정정은 7줄이다. 보완은 2줄이다.
- 추가 줄의 시작 시 번호: 7–8, 101–104, 198–200, 203–223. 빈 줄과 frontmatter를 포함했다.
- 7–8행은 소스의 파일 길이·함수 선언·호출처와 반영 기록 5로 확인했다. 101–104행은 BCspecfile의 투영과 열린 부등식·끝점 대입으로 확인했다. 198–200·203–205행은 Module2의 m_bndspec 선언과 준비 단계의 배열 할당으로 확인했다. 206–223행의 설명·표 머리·8개 행은 최종 setup 보고서·AD 판정·현재 소스·과거 커밋과 대조했다.
- 표의 B·C 판정은 유지했다. A·E 행은 없다. SI1-507의 SOURCE 최초 초기화도 `SwashReadInput:2625–2634`에서 확인했다. 해당 행의 H1 등은 연결된 AD 보고서의 변경 구간 ID다.
- swashuse PDF p.34의 seed 설명과 p.57,59,62–64의 구문·단위·스펙트럼·좌표 설명을 대조했다. p.57,59,62–64는 쪽 이미지도 확인했다. fac의 두 경계는 엄격한 부등식이다. rdist는 선분 길이로 정규화한 거리다.
- 상대 링크의 대상 파일은 모두 존재한다. 절대 홈 경로와 `[[`는 없다. Mermaid 블록은 없다. SI1-712·713의 “미확인”은 반영 전 노트의 인용이다. 현재 상태의 미완 항목은 없다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| swash-boundary-spectral-transfer.md:7 | 정정 | 내부 함수 40개 → 28개 | `src/SwashBCtransferfnc.ftn90:429–4707`의 `real function` 선언을 집계했다. eta 8개와 vel 20개다. |
| swash-boundary-spectral-transfer.md:161 | 정정 | 40=8+32와 잘못된 숫자 자리 설명 → 28=8+20 및 I=층·J=kmax | 선언 전수 집계와 `src/SwashBCtransferfnc.ftn90:313–330,380–397`의 호출 대입. k=1의 맨 위층은 `src/SwashExpLayUflow.ftn90:1060–1068`에서 확인했다. frontmatter의 같은 오류를 본문에 남기지 않았다. |
| swash-boundary-spectral-transfer.md:196 | 정정 | 미확인/source-needed → 배열 선언과 원문 연결 | SI1-712·713 수정안과 `src/SwashModule2.ftn90:294,368–395`, `src/SwashCheckPrep.ftn90:1689–1702`. |
| swash-boundary-spectral-transfer.md:201 | 정정 | 나머지 38개 미전사 → Method의 문헌 안내와 대표 식 두 개의 위치 | `src/SwashBCtransferfnc.ftn90:47–51,499–504,657–663`. 38개라는 수량은 전체 28개와도 맞지 않는다. 원문이 안내하는 문헌을 확인된 사실로 적었다. |
| swash-boundary-spectral-transfer.md:202 | 정정 | 별도 파일·본 노트 범위 외 → 네 함수의 정의 위치 | `src/swanser.ftn:3331` CHGBAS, `src/SwashServices.ftn90:13` disprel, `src/swanser.ftn:3892` GAMMAF, `src/swanser.ftn:174` REFIXY. 각 정의를 직접 열었다. |
| swash-boundary-spectral-transfer.md:216 | 보완 | SPECFile 구문의 쪽 생략 → PDF p.57 추가 | swashuse PDF p.57의 `SPECFile ’fname’ [cycle]` 구문. p.63은 cycle의 뜻을 설명한다. |
| swash-boundary-spectral-transfer.md:218 | 보완 | BOUND 초기화만 직접 인용 → SOURCE 초기화 원문도 추가 | `src/SwashReadInput.ftn90:2625–2634`의 lseed 조건·서로 다른 정수열·false 대입. AD의 SI1-507 판정과 같다. |
| swash-boundary-spectral-transfer.md:222 | 정정 | 미확인 문장을 교체한다는 지시문 → 지시문 삭제 | 같은 행의 확인된 선언 사실과 `src/SwashModule2.ftn90:294,368–369`는 유지했다. |
| swash-boundary-spectral-transfer.md:223 | 정정 | 선언과 allocate를 함께 인용한다 → 두 곳의 차원이 일치한다 | `src/SwashModule2.ftn90:384–385,392–393`과 `src/SwashCheckPrep.ftn90:1689–1690,1699–1700`. |

삭제 줄의 근거:

- HEAD 7행: 기존 검증 방법에 보고서 반영을 추가했다. 이번에는 같은 줄에 있던 함수 개수도 원문 집계로 바로잡았다.
- HEAD 100행: 닫힌 구간 표기를 열린 부등식으로 고쳤다. SI1-714 수정안과 현재 `SwashBCspecfile:841`, `8756667:src/SwashBCspecfile.ftn90:792`가 근거다.
- HEAD 194행: 누적 배열의 선언 모듈·차원 추정을 SI1-713의 선언·할당 원문으로 교체했다.
- HEAD 197행: seed 선언 모듈 추정을 SI1-712 및 현재·7949227의 m_bndspec 선언으로 교체했다.

기계 확인 후보 판정:

- `8756667:src/SwashBCspecfile.ftn90:381` 후보: 오탐이다. 지정 커밋 381행에 `if ( oned .and. mdc /= 0 ) call msgerr (3, 'directional wave spectrum not allowed in 1D mode')`가 그대로 있다. 현재 398행과 같다. 유지했다.
- `7949227:src/SwashBounCond.ftn90:237` 후보: 오탐이다. 지정 커밋 237행에 `if ( lseed ) then`이 그대로 있다. 현재 위치는 235행이다. 유지했다.
- `8756667:src/SwashBCspecfile.ftn90:792` 후보 1: 오탐이다. SI1-714 코드 칸의 과거 인용이다. 지정 커밋 792행은 `if ( fac > -0.001 .and. fac < 1.001 ) then`이다. 유지했다.
- `8756667:src/SwashBCspecfile.ftn90:792` 후보 2: 오탐이다. 같은 행의 결론 칸에서 같은 과거 원문을 반복 인용했다. 엄격한 두 부등호가 일치한다. 유지했다.

## 최종 집계

시작 diff의 대상은 추가 238줄과 삭제 35줄이었다. 이 273줄을 모두 대조했다. 남은 미완 문장과 발견한 수량 오류의 연결 문장 6줄도 수정 전후를 대조했다. 최종 diff에서 재배치된 것으로 표시된 빈 줄 3쌍도 확인했다. 아래 대조 수는 최종 `git diff -U0 HEAD -- <노트>`의 추가 줄과 삭제 줄을 각각 센 합이다. 정정·보완 수는 이번에 붙인 전수 검증 태그가 있는 서로 다른 노트 줄 수다.

| 노트 | 최종 추가 줄 | 최종 삭제 줄 | 대조 합 | 정정 | 보완 |
|---|---:|---:|---:|---:|---:|
| swash-explicit-depthavg-flow.md | 113 | 6 | 119 | 6 | 1 |
| swash-wetting-drying-runup.md | 61 | 16 | 77 | 3 | 0 |
| swash-tech-documentation-overview.md | 38 | 13 | 51 | 3 | 2 |
| swash-boundary-spectral-transfer.md | 35 | 9 | 44 | 7 | 2 |
| 합계 | 247 | 44 | 291 | 19 | 5 |

- 차이 표는 총 107행이다. 각 행의 분류와 E 강도를 최종 보고서에 맞췄다. 이번 정정으로 분류를 바꾼 행은 없다.
- 기계 확인 후보 15개를 각각 원문과 대조했다. 모두 오탐이었다.
- 네 파일의 frontmatter는 YAML로 정상 해석된다. 차이 표의 열 수와 정정 태그 위치도 맞는다.
- 모든 상대 링크의 대상 파일은 존재한다. 대상 노트에 절대 홈 경로와 `[[`는 없다. Mermaid 블록은 없다.
- 반영 전 문장의 인용과 원문 자체의 빈 장 설명은 현재 검수의 미완 항목과 구별했다. 현재 검수의 미해결 항목은 없다.
- 쓰기는 대상 노트 네 파일과 이 기록에 한정했다. git 쓰기·sudo·모델 실행·네트워크 사용은 없었다.

대조 291, 정정 19, 보완 5
