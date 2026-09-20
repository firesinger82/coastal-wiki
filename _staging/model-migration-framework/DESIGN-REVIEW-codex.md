[CRITICAL DESIGN FLAWS]

검토일: 2026-09-20. 판정: **현 설계 그대로의 자동 수정·migration 완료 판정은 보류 권고**. tree 비교, 3단계 영향 분류, historical 불변, Claude 재판정, 사람 적용 게이트는 유지할 수 있다. 아래는 그 구조 안에서 필요한 보완이다. 이 리뷰는 AI 분석이며 migration 실행·소스 의미 재검증 결과가 아니다. 네트워크와 raw 소스는 읽지 않았다. 자료에 나타난 사실과 설계상 반례를 구분하고, 실제 upstream에서 발생했는지 확인하지 못한 것은 미확인으로 표시한다.

이하 `DESIGN`은 `_staging/model-migration-framework/DESIGN.md`, `P/`는 `_staging/adcirc-upstream-review/`, `S/`는 `_staging/source-snapshots-20260919/`이다. 파일:줄은 검토 당시 원문 기준이다.

- **C1 — 미해석을 무영향으로 바꾸는 조기 종료.** DESIGN:85-89는 해석된 참조 파일과 변경 파일의 교집합이 0이면 **전체 NO_ACTION**으로 끝낸다. 그러나 bare·symbol-only·산문·제외 영역의 파일 소속을 모두 확정했다는 전제도, 미해석 참조가 이 종료를 막는 규칙도 없다. 새 트리에서만 심볼을 찾으면 삭제된 심볼의 old 파일을 교집합에 넣지 못한다. 실제 `P/bare-reference-resolution.csv:43`의 `wind.F`는 adcirc/asgs 두 후보로 미해결이다. 파일 집합에서 빠졌다고 무영향인 것은 아니다. 또한 `P/SNAPSHOT-UPDATE-PLAN.md:47`은 직접 소스 인용 외 README·AUDIT-LEDGER의 PR OPEN 요약도 동반 영향 후보로 명시한다. 원 파일 인용 여부만으로 산문 속 같은 주장을 배제할 수 없다. **R2 적용 필요.**

- **C2 — 줄 범위 양 끝의 일치를 전체 내용 동일성으로 취급.** DESIGN:66은 양 끝 줄 확인만으로 자동 갱신을 허용한다. 시작·끝이 그대로인 채 가운데 조건·식·항목이 변경되는 경우를 차단하지 못한다. 실제 파일럿에는 `nodalattr.F:636-686 → 657-709` 범위 내부의 `swan_local_control` 추가와 카탈로그 의미 수정이 함께 있었다(`P/SNAPSHOT-UPDATE-PLAN.md:53-56`). 이 사례의 양 끝 바이트가 실제 동일했는지는 미확인이나, 내부 변경을 검사해야 한다는 요구는 확인된다. 단일 줄·파일+심볼 역시 동일 문자열이 반복되거나 바깥 분기 조건이 바뀌면 동일 근거를 보장하지 않는다. **R3 적용 필요.**

- **C3 — 새로 채집한 설치본을 historical 근거로 명명하고 바로 비교 회로에 투입.** DESIGN:121-125는 오늘의 설치본 manifest를 historical로 고정한 뒤 git과 같은 회로로 진행한다. 이는 오늘의 바이트 증거이지 노트 작성 당시 바이트 증거가 아니다. LISFLOOD-FP의 3,170/1,672 파일 차이뿐 아니라 XBeach 3개 노트가 별도 source copy를 참조했다는 확정 기록이 있다(`S/provenance-final.csv:18,30`; `S/provenance-readme.md:176-177`). 불일치 상태를 기록하는 것만으로는 잘못된 old 기준의 줄 갱신을 막지 못한다. **R5의 적용 중단 조건 필요.**

- **C4 — local patch의 구문적 적용 가능성을 근거 보존으로 대체.** DESIGN:132-135에는 패치 보관·`git apply --check`만 있고, 새 base에 실제 적용한 결과의 해시와 노트 근거를 검토하는 단계가 없다. upstream에서 호출 계약·자료형·배열 의미·컴파일 조건이 다른 파일에서 바뀌면 patch 문맥은 맞아도 의미는 틀릴 수 있다. FUNWAVE-GPU의 실제 의미 충돌 발생 여부는 미확인이다. 다만 그 노트 재현에 세 파일의 local patch가 필요하다는 사실은 확정돼 있다(`S/provenance-final.csv:16`). 순수 old/new base 비교와 순수 new staging 설치만 하면 이미 존재하는 근거를 잃는다. **R6 적용 필요.**

- **C5 — 검증 범위가 없는 note 단위 validated 기록과 미완료 REVIEW_ONLY의 완료 허용.** historical 불변·line maintenance 규칙 자체는 적절하다(DESIGN:139-148). 하지만 `note-status.csv`에서 파일럿의 `validation_kind`·검증일·검증 대상 참조를 없앴고(DESIGN:183), 완료 조건은 REVIEW_ONLY 중 줄 이동만 다룬다(DESIGN:208). 실제 파일럿 `REVIEWED_NO_CHANGE` 10건은 **참조 기계 검사**이며, 17건은 줄 검사, 2건만 의미 수정이다(`S/provenance-notes-adcirc.csv`, 예 :26-27,42). 파일·심볼 존재를 확인한 것을 노트 전체 semantic validation으로 승격할 틈이 있다. AMBIGUOUS를 수정하지 않았다는 사실도 해결 또는 사용자 보류 결정을 뜻하지 않는다. **R7·R9 적용 필요.**

[MAJOR RISKS]

- **M1 — “SWAN/SWASH file:line 0”이라는 실측 전제가 원문과 모순된다.** DESIGN:58-59 및 :223의 핵심 사례를 그대로 받아들일 수 없다. `models/SWAN/source-analysis/swan-setup-solver-swancom1-crosswalk.md:33-34`에 `swancom1.ftn:9970-9984`, `:10001-10015`가 있고, `models/SWASH/source-analysis/swash-bottom-friction-wind.md:23-30`에는 `.ftn90:36`, `.ftn90:66-67` 등이 있다. 읽기 전용 진단 정규식 `\b[\w.-]+\.ftn(?:90)?:L?\d+`로 raw 제외 Markdown을 검색하면 SWAN 68노트 중 11노트에서 170회, SWASH 26노트 중 20노트에서 440회 일치한다. 이 수는 frontmatter·코드블록을 포함하고 복수 범위를 완전히 파싱하지 않은 **부분 문법 검색 수**이며, 설계의 전체 수치를 대체하지 않는다. 본문 예만으로도 0건은 반증된다. 원 집계 방법이 제공되지 않아 원인은 미확인이다. 확장자 누락 등을 점검해야 한다. **R1.**

- **M2 — 최근 파일명·근접 심볼은 bare reference 소속의 증명이 아니다.** SWASH 바닥마찰 노트 :106은 한 문장에 `SwashUBotFrict.ftn90:254`와 `SwashBotFrict.ftn90:298`을 비교한다. 같은 줄의 어느 파일인지 먼저 결정하지 않으면 nearest-file 규칙이 잘못 붙을 수 있다. :61-65에는 설명·수식과 bare 줄이 함께 있고, :81-85에는 코드블록 안 줄 참조가 있다. 단순 60줄 창은 절·표·비교 문장의 범위를 표현하지 못한다. `TimeLoc`처럼 공통 심볼은 ±6줄에 있어도 repo를 확정하지 못한다. **R3.**

- **M3 — changed hunk 밖 의미 변화가 배제된다.** DESIGN:110의 UPDATE_REQUIRED 진입 조건은 좁은 근거와 hunk 겹침이다. 참조한 식이 그대로여도 호출자, 입력 기본값, 상수, include, 선택 분기가 바뀌면 그 식에 대한 주장이 달라질 수 있다. 실제 SWASH 바닥마찰 노트 :51-55는 계산 파일과 `SwashReadInput.ftn90`의 옵션·기본값을 함께 설명하고, `models/EFDC/source-analysis/efdc_hydro_core.md:33`은 직접 file:line 없이 다른 노트의 확산 계산을 연결한다. 이들에서 이번 upstream 의미 변경이 발생했는지는 미확인이다. 다만 직접 교집합이 semantic 영향의 필요조건이라는 설계 가정은 성립하지 않는다. 이는 의존성 전체 분석 요구가 아니다. 노트가 주장한 입력·호출·설정 관계까지만 확인하고 불확실하면 보류하면 된다. **R2.**

- **M4 — rename/move/split/merge의 old/new 식별이 없다.** `changed-files.csv`는 R을 허용하지만 path 하나뿐이며 `REFERENCES.csv`에도 old/new repo·path가 없다(DESIGN:179-180). 삭제된 old path와 new path 양쪽을 교집합에 넣는 규칙, 여러 파일로 분할·합쳐진 근거의 보류 규칙이 없다. 파일만 인용한 경우에도 rename이면 인용 수정이 필요하므로 DESIGN:68의 “수정 불필요”는 틀린 일반화다. ADCIRC는 삭제·rename이 없었다(`P/SNAPSHOT-UPDATE-PLAN.md:35`; manifest C는 ADD 1/MODIFY 30). Delft3D의 실제 rename/split 발생 여부는 제공 범위에서 미확인이다. **R4.**

- **M5 — 두 번째 migration에서 좌표 기준과 historical이 갈라진다.** ADCIRC의 historical은 `6037225`지만 줄 이동을 반영한 인용은 `e8b62a70` 좌표이고 일부는 미수정·AMBIGUOUS다(`S/provenance-notes-adcirc.csv:37`; `P/BACKLOG-bare-line-references.md:45-62`). 다음 migration에서 historical을 old 좌표로 쓰면 중복 이동하고, 현재 설치본을 무조건 old로 쓰면 보류된 과거 인용을 오결한다. DESIGN의 참조별 스키마에는 현재 인용이 속한 snapshot이 없다. `S/manifest.csv:4`의 pinned는 이전 값인 반면 `S/provenance-final.csv:4`의 current local은 새 값이라는 입력 충돌도 이미 존재한다. **R7·R8.**

- **M6 — 다중 저장소의 산출물 충돌과 note 집계 손실.** DESIGN:174는 “저장소마다”라고 하지만 디렉터리 키는 model+date뿐이다. 같은 날 ADCIRC/adcirc와 ADCIRC/asgs, EFDC 두 repo를 처리하면 같은 파일명이 충돌한다. hotstart의 `wind.F` 사례와 EFDC-GVC/mainline 비교 노트(`models/EFDC/source-analysis/efdc_gvc_legacy.md:7,19`)처럼 노트 하나가 복수 repo를 참조할 때 단일 historical/current 값으로 덮어쓸 위험도 있다. **R8.**

- **M7 — 적용 전 검토 바이트와 적용 바이트의 결속이 부족하다.** DESIGN:154-157에 pre-apply gate와 backup은 있지만 그때 확인할 note/source/patch hash, 중간 실패 처리, source·note·provenance의 결합된 복구 조건은 명시되지 않는다. ADCIRC 계획은 목표 tip가 달라지면 중단하도록 구체화했었다(`P/SNAPSHOT-UPDATE-PLAN.md:23-24`). staging과 설치본이 서로 같아도 둘 다 검토 이후 바뀌었다면 안전하지 않다. 실제 중간 실패는 미확인. **R8·R10.**

[MINOR RISKS]

- **N1 — 파일럿 비교 단위가 다르다.** DESIGN:168의 “21→2”에서 21은 Codex의 commit×file 변경 단위이고(`P/codex-impact-review.md:5`), 2는 최종 UPDATE_REQUIRED **노트** 수다. 중간 Claude 판정은 5 UPDATE_REQUIRED/24 REVIEW_ONLY, 최종은 2/27/35 NO_ACTION이다. 같은 단위의 과잉 판정률처럼 사용하면 안 된다. Claude 독립 검토 원칙은 유지하되 정확한 단위를 남긴다.

- **N2 — BEHIND 14와 잔여 13의 기준일이 섞인다.** DESIGN:23,28은 기준 상태와 ADCIRC 완료 후 잔여 집합을 구분하지 않는다. `S/README.md`의 초기 UNKNOWN 29 및 후속 보완 상태도 시점이 다르다. current/upstream 값에 수집일과 적용 전후를 붙여야 한다. 원격의 지금 상태는 이번 네트워크 금지 범위에서 미확인이다.

- **N3 — 역할표의 네트워크 책임 공백.** DESIGN:163은 네트워크 수집을 Claude에 맡기고 :164는 staging clone을 Codex에 맡긴다. 네트워크 차단 전제하에서는 Claude가 고정한 archive/clone을 넘기거나 로컬 복제로 한정해야 한다. 역할 자체를 바꿀 필요는 없다.

- **N4 — 비용 상한이 파일 수에만 의존한다.** DESIGN:10,102,200의 교집합 크기는 읽을 patch 크기의 상한이 아니다. 단일 거대 파일, 줄바꿈 일괄 변경, 코드 생성 결과만으로도 작업량이 커진다. 파일 수뿐 아니라 changed lines·patch bytes·broad/미해석 참조 수로 사전 예산을 결정한다. Delft3D의 실제 patch 크기는 미확인이다.

[MISSING FAILURE MODES]

- **F1 — 기존 인용 오류·서로 다른 source copy·PR 전용 좌표.** `P/codex-impact-review.md:13`은 “노트 좌표가 baseline 좌표라는 조건부 대조”이고 기존 오인용 검증은 하지 않았다고 명시한다. XBeach 별도 copy는 실제 확인된 문제다. 시작 전 old 인용의 유효성을 검사하지 않으면 잘못된 줄도 안전하게 이동한 것처럼 보인다. 기존 오류를 migration이 만든 오류와 구분해야 한다(R3·R5·R7).

- **F2 — 문법을 부분 인식하고 성공 처리.** ADCIRC에서 이미 `[file=... line=...]`, `file:1-3,5-7` 후속 범위를 보완했다(`P/codex-impact-review.md:12`). SWASH :51의 `SwashBotFrict.ftn90:106,128`도 단일 start/end로 표현되지 않는다. SWAN 표 :40-58의 backtick 없는 `:43` 등도 필요하다. 괄호·링크·표·복수 범위 중 일부만 파싱했다면 전체 인용을 처리 완료로 세지 않는 규칙이 빠졌다(R1).

- **F3 — frontmatter·코드블록에 실제 근거가 존재.** SWASH 노트 :7의 verification_method와 :81-85의 인용 코드, SWAN crosswalk :71-75의 주석 줄번호가 실제 사례다. 자동 치환 제외는 타당하지만 영향 탐지에서 빠지거나 “별도 보고”가 완료 게이트와 연결되지 않으면 stale 근거를 남긴다. historical 검증 기록은 원형 보존하고, current 설명으로 제시한 코드와 구분해야 한다(R1·R7·R9).

- **F4 — generated/vendor/submodule의 표현 차이.** 파일 manifest(path·size·sha256)는 gitlink의 대상 commit, symlink 대상·형식, 실행 bit를 표현하지 않는다. checkout이 포인터만 가진 경우 실제 소스 확보 여부도 별개다. LFS·submodule·symlink가 대상 저장소에 실제 존재하는지는 미확인이다. vendor가 모두 무관하지는 않다. ADCIRC 변경 31개 중 11개가 thirdparty/swan이며, `!ADC/!NADC` 표식은 조건 선택 지점이었다(`P/SNAPSHOT-UPDATE-PLAN.md:33`; `P/codex-impact-review.md:15`). 생성 입력과 생성 결과 중 무엇을 인용했는지, 모델 호출·빌드 인터페이스가 바뀌었는지까지만 확인하고, 부속 도구 내부 전수 분석으로 확장하지 않는다(R4·R8).

- **F5 — archive 포장 구조·부분 추출·동일 이름의 다른 배포본.** 서로 다른 archive 최상위 폴더, 포함/제외 규칙, 배포 채널이 다른 파일을 동명으로 합치면 ADD/DELETE 또는 동일 파일 판정이 잘못될 수 있다. LISFLOOD-FP의 파일 수 불일치 원인은 미확인이므로 “부분 추출이었다”라고 확정해서도 안 된다. archive hash·출처·추출 범위와 로컬 snapshot hash를 별도로 보존해야 한다(R5).

- **F6 — git diff에 담기지 않는 local 자산.** `git diff HEAD`만으로 untracked/ignored 파일, 외부 패치 의존 파일을 재현할 수 없고 binary payload 보관 정책도 없다. FUNWAVE-GPU에서 세 추적 파일 외 필수 자산이 있는지는 미확인이다. 무조건 모두 패치에 넣는 대신 필요한 자산을 목록화하고 보존·제외를 결정해야 한다(R6).

- **F7 — old commit 미확보·비선형 전환·API patch 부재.** shallow 추가 fetch 실패, 목표 branch 이동, unrelated/diverged tree, 파일 목록은 있지만 patch가 없는 경우의 중단 규칙이 없다. 두 tree의 차이는 계산할 수 있어도 “동일 계열 upgrade”가 자동 성립하지 않는다. 현 manifest의 BEHIND 기록이 미래 실행 시 이를 보장하지 않는다(R8·R9).

- **F8 — 부분 적용·재실행·권한 복구 실패.** source rename 이후 복사 실패, note 수정 후 provenance 기록 실패, 중간 종료 후 재실행이 별도 상태로 표현되지 않는다. 특히 SCOPED EDIT의 성공 경로 “즉시 relock”만으로 실패 경로의 재잠금은 보장되지 않는다. 발생 사실은 미확인이며 설계상 처리 누락이다(R10).

[OVER-AUTOMATION RISKS]

자동 수정 범위는 **repo·snapshot·경로·old 인용이 확정되고, 유일한 old→new 대응에서 인용 범위 전체가 동일한 줄번호 갱신**으로 제한하는 것이 적절하다. 이것도 semantic validation은 아니다. high/medium이라는 이름, 60줄 창, ±6줄 심볼, 파일 존재를 이 조건 대신 사용해서는 안 된다. file+symbol의 high도 동명 정의·호출·주석을 구분했다는 증거가 없으면 후보 신뢰도에 불과하다.

3단계 classification을 늘리지 않고 별도 `decision_state=NEEDS_USER_DECISION`과 이유·영향 범위를 둔다. 다음 조건은 읽기 전용 조사 결과까지 만든 뒤 **적용·완료 판정을 멈춰야 한다**.

1. old snapshot과 노트 근거의 관계를 복원하지 못함, non-git manifest 범위 불명, 충돌 provenance를 둔 채 전환하려 함.
2. 영향 가능성이 남은 AMBIGUOUS·미해석·제외 영역을 해결하지 않은 채 설치를 진행하려 함. 단순 탐지 때마다 사용자를 부르는 대신 Claude 검토로도 해결되지 않은 건을 묶어 보류 범위 승인을 받는다.
3. local patch의 의미 유지 미확인, 재적용 결과가 기존 승인 패치 의도를 바꿈, 재현에 필요한 파일이 누락됨.
4. source identity/목표 SHA/검토 hash 불일치, rename·split·merge 대응 미확정, 불완전 tree/patch를 근거로 완료하려 함. 먼저 차단·재조사하고 목표나 범위 변경이 필요할 때 사용자 결정으로 넘긴다.
5. UPDATE_REQUIRED 본문 변경이 승인 범위를 넘음, 또는 unresolved REVIEW_ONLY를 보류한 상태로 완료하려 함.
6. 대형 교집합의 승인 예산을 넘거나, 모델 인터페이스 밖 의존성 분석으로 범위를 넓혀야 한다고 판단함.

사용자 보류는 “validated”가 아니다. 보류가 있는 운영 전환 완료와 근거 검증 완료를 별도 열로 남겨야 한다.

[UNDER-AUTOMATION RISKS]

- 문법별 탐지·해석·미해석·제외 수를 대조하는 coverage 검사가 없다. M1 같은 0건 오측정을 조기에 잡는 일은 자동화에 적합하다. 전체 framework 구현 전에 알려진 실제 인용 예가 탐지 집계에 포함되는지를 acceptance에 넣는다(R1).
- old/new 양쪽 파일·심볼 후보 수집, 모든 복수 범위 보존, rename 후보와 소멸 심볼 보고를 자동화하면 안전한 사람 검토가 쉬워진다. 이를 자동 귀속·자동 의미 승인과 분리한다(R2·R4).
- REVIEW_ONLY 전 행에 최종 처리 결과 또는 보류 결정을 강제하고, “의미 검증 증거 없이 validated”, “AMBIGUOUS에 자동 치환”, “unresolved가 있는데 전체 NO_ACTION”을 검사하는 것은 기계적으로 가능하다(R7·R9).
- A/B/C/D 목록·해시·포함 규칙의 일관성, 목표 SHA 및 승인된 note hash 재확인, 적용 전후 권한 확인은 자동화에 적합하다(R8·R10). 이번 자료에서 A=D는 1,314행 전부 일치했고 B는 1,313행, C는 ADD 1/MODIFY 30이었다. 이 성공은 해당 manifest의 파일 바이트 대조 증거이며 symlink·mode·복합 패치 검증을 대신하지 않는다.

[RECOMMENDED DESIGN CHANGES]

아래 변경은 현 단계·분류·역할을 유지하는 보완이다. 각 항목의 ⑴은 관련 절, ⑵는 사례, ⑶은 수정, ⑷는 미수정 영향이다.

- **R1 — 인용 집계와 coverage를 검증 가능하게 만들기.** ⑴ REFERENCE GRAMMAR, INPUTS, FAILURE MODES #5/#10, ACCEPTANCE( DESIGN:42,47-72,194,199,206-209). ⑵ SWAN crosswalk :33과 SWASH 바닥마찰 :23의 explicit 인용, ADCIRC review :12의 복수 범위. ⑶ 0건 전제 재측정; 사용한 코퍼스·문법·제외 기준을 남기고 `.ftn/.ftn90`, bracket 문법, 복수 범위를 보존한다. 제외 영역도 탐지 ledger에는 남기되 자동 수정하지 않는다. 탐지 후보가 resolved/unresolved/excluded 중 하나로 빠짐없이 귀속되게 한다. ⑷ 파서 누락이 무영향 판정과 잘못된 파일럿 선택으로 이어진다.

- **R2 — 교집합을 우선순위 필터로 제한하기.** ⑴ GOALS #2, CHANGE DETECTION [1]-[6], IMPACT CLASSIFICATION(DESIGN:10,81-115). ⑵ `P/bare-reference-resolution.csv:43`, `P/SNAPSHOT-UPDATE-PLAN.md:47`, EFDC hydro core :33. ⑶ old/new 양쪽에서 symbol-only 후보를 수집하고 미해석 후보는 조기 종료를 막는다. 직접 교집합 0은 “해석된 직접 참조의 교집합 0”으로만 기록한다. 변경된 모델 인터페이스·상수·설정 및 영향 주장과 연결된 요약을 제한적으로 확인하고, 이를 못 닫으면 REVIEW_ONLY+pending으로 남긴다. hunk 겹침 없이도 의미 불일치 증거가 있으면 UPDATE_REQUIRED가 가능해야 한다. ⑷ 삭제 심볼·간접 주장·암묵 참조가 전체 NO_ACTION으로 사라진다.

- **R3 — 자동 줄 수정에 증거 조건 추가.** ⑴ REFERENCE GRAMMAR, FAILURE MODES #2/#4, ACCEPTANCE #4(DESIGN:65-70,191-193,208). ⑵ SWASH 바닥마찰 :106의 복수 파일, ADCIRC nodal 카탈로그 변경 계획 :53-56. ⑶ 절·표·문장별 모든 파일 후보와 repo를 고려하고 근접 심볼은 보조 증거로만 쓴다. old 좌표 타당성, 유일한 대응, 전체 범위 동일성·연속성, 중간 삽입/삭제 없음, 승인된 치환 범위를 확인한다. 여러 대응·복합 범위 일부 실패·semantic 의문은 보고만 한다. ⑷ 다른 파일/복제 코드로 이동하거나 내부 의미 변경을 line-only로 위장한다.

- **R4 — 경로 전환과 비텍스트 변경 보존.** ⑴ CHANGE DETECTION, OUTPUT SCHEMA, FAILURE MODES(DESIGN:99-102,179-181). ⑵ ADCIRC 계획 :35와 manifest C는 rename·삭제를 검증하지 않았다. ⑶ `repo_id`, `old_path`, `new_path`, object type/mode를 기록하고 양쪽 경로로 교집합을 만든다. rename은 후보이며 split/merge·생성물·vendor·submodule은 참조 범위의 대응 증거가 없으면 pending으로 둔다. 파일만 인용한 경로 변경·삭제도 수정 후보다. ⑷ 새 경로만 남겨 old 인용을 놓치거나 경로가 존재한다는 이유로 다른 구현을 같은 근거로 취급한다.

- **R5 — non-git의 observed와 historical 구분.** ⑴ NON-GIT FALLBACK, PROVENANCE MODEL, ACCEPTANCE(DESIGN:121-125,143-146,205-210). ⑵ `S/provenance-final.csv:18,26,30`. ⑶ 오늘 만든 manifest를 `observed_local_snapshot`으로 기록한다. archive 출처·배포 식별자·hash·추출 규칙·누락 범위를 고정하고 old/new 비교 범위가 동일한지 확인한다. 노트가 그 old copy를 봤다는 근거가 없으면 historical은 unknown/conflicting으로 보존한다. 비교 보고는 가능하지만 줄 수정·검증 승격·설치 진행은 근거 복원 또는 명시적 보류 결정 전까지 막는다. ⑷ 불완전 추출·다른 배포본을 정상 old/new 전환으로 오인한다.

- **R6 — local patch를 실제 목표 snapshot에 포함.** ⑴ LOCAL-PATCH HANDLING, CHANGE DETECTION, LOCKING/APPLY, ACCEPTANCE #1(DESIGN:127-135,154,205). ⑵ `S/provenance-final.csv:16`의 Makefile_cuda·etauv_solver_gpu.F·mod_cuda.F. ⑶ old base+실제 patch 결과를 보존하고 새 base+승인 patch 결과를 staging에서 생성·해시 검증하는 것을 요건화한다. `apply --check` 성공 뒤에도 패치가 의존하는 모델 호출·빌드 인터페이스의 변경 여부를 Claude가 검토한다. binary/untracked 등 필요 자산도 목록화한다. 검증 불가 시 NEEDS_USER_DECISION이며, 빌드·실행 검증이 필요하면 별도 범위로 요청한다. ⑷ 패치가 유실되거나 의미 충돌 상태를 BASE_SHA_PLUS_LOCAL_PATCH 재현 가능으로 기록한다.

- **R7 — 검증 종류·범위·인용 좌표 기준 유지.** ⑴ PROVENANCE MODEL, OUTPUT SCHEMA, ACCEPTANCE #6(DESIGN:139-148,180-183,210). ⑵ `S/provenance-notes-adcirc.csv:26-27,37,42,47`. ⑶ `validation_kind`, `validated_on`, 검증한 ref/claim 식별자, reviewer/evidence와 미검증 범위를 보존한다. mechanical/semantic 기록을 혼합하지 않고 note 요약이 전체 검증을 뜻하지 않게 한다. 참조별 `citation_snapshot`을 남겨 historical과 현재 줄 좌표를 분리한다. historical은 repo별 사실과 불확실성을 그대로 유지한다. ⑷ REVIEWED_NO_CHANGE나 line-only가 의미 승인으로 보이고 다음 migration에서 좌표를 잘못 이동한다.

- **R8 — 입력·산출물을 repo와 목표 바이트에 결속.** ⑴ REPOSITORY CLASSIFICATION, INPUTS, CHANGE DETECTION [0]/[2], OUTPUT SCHEMA, ROLE SPLIT(DESIGN:23-43,79,98-100,163-164,174-184). ⑵ `S/manifest.csv:4`와 `S/provenance-final.csv:4`의 설치 시점 차이, EFDC 2 repo(:14-15). ⑶ model+repo+old/new 식별자 또는 고유 run ID를 출력 키로 쓰고 파일 덮어쓰기를 막는다. 실제 설치본과 수집 기록 불일치 시 먼저 재조사한다. 목표 SHA/배포 hash·note hash·patch hash와 diff/manifest의 생성 조건을 고정한다. old object 미확보·불완전 patch·잘린 결과는 완전한 비교로 세지 않는다. 네트워크 확보와 로컬 계산의 전달 계약을 명시한다. ⑷ 저장소 결과가 섞이거나 검토하지 않은 바이트를 적용한다.

- **R9 — unresolved와 보류를 acceptance에 연결.** ⑴ IMPACT CLASSIFICATION, FAILURE MODES #11, ACCEPTANCE(DESIGN:106-115,200,204-212). ⑵ 파일럿 precheck는 463행 중 FILE_REF_OK 262, NO_CHANGE 84, LINE_REFERENCE_UPDATE 116, IN_CHANGED_REGION 1이며 bare AMBIGUOUS도 1건 남았다. ⑶ REVIEW_ONLY 전건에 검사 종류·최종 disposition·미해결 이유를 기록한다. 사용자 보류는 범위·위험·후속 조치와 연결하고 semantic 검증 성공으로 세지 않는다. 초안 classification, Claude 확정, 사용자 결정의 상태를 분리한다. coverage와 의미 증거 없이는 validate-all/broken-reference 0만으로 완료하지 않는다. ⑷ 파일 존재 검사와 unresolved 방치만으로 migration 검증 완료가 가능해진다.

- **R10 — 적용 실패와 복구도 gate에 포함.** ⑴ LOCKING/APPLY, ACCEPTANCE #1/#7/#8(DESIGN:154-157,205,211-212). ⑵ ADCIRC 계획 :23-24의 tip/예상 변경 확인과 :92-94의 source·wiki 별도 복구. ⑶ 승인 hash를 적용 직전 재확인하고 source·notes·provenance의 이전/목표 상태를 함께 남긴다. 중간 실패 시 relock·중단·복구·재개 조건을 명시하고 backup 검증 대상에 필요한 자산을 포함한다. A/B는 source 설치와 note 수정을 각각 수행할 수 있는 승인 절차로 연결한다. 커밋 분리는 유지하되 대응하는 run 식별자를 공유한다. ⑷ 부분 전환을 완료로 보거나 source만 되돌리고 새 노트 좌표를 남긴다.

- **R11 — 파일럿은 commit 수가 아닌 실제 시험 범위로 선정.** ⑴ GOALS #2, FAILURE MODES #11, PILOT ROLLOUT ORDER(DESIGN:10,200,216-228). ⑵ `S/manifest.csv:15`는 +1만 보여주고 해당 변경의 파일·hunk는 제공하지 않는다. ⑶ EFDC 계획은 유지하되 변경 파일·인용 교집합·줄 이동·의미 변경·broad/ambiguous 포함 여부를 사전에 확인한다. 모델 전체 참조 수를 그 repo의 실제 시험량으로 쓰지 않는다. SWAN/SWASH 문법 예와 ADCIRC 미해결 사례는 읽기 전용 파서 검토에 먼저 포함한다. 비용 예산은 파일 수·patch 크기·미해석 수로 정한다. ⑷ 작은 commit을 낮은 위험·충분한 검증 범위로 오인한다.

전 절 검토 대응은 다음과 같다. 신규 framework나 의존성 전체 분석을 요구하지 않으며, NON-GOALS의 빌드·실행 제외는 유지한다.

| DESIGN 절 | 검토 결과/보완 |
|---|---|
| GOALS | 직접 교집합만으로 의미 영향 완결 불가; R2/R11 |
| NON-GOALS | hygiene·upstream 전수 리뷰·빌드 제외 유지; 해결 불가 시 범위 확대 대신 R9 보류 |
| REPOSITORY CLASSIFICATION | 중첩 유형 유지; 시점·local 상태 고정 R6/R8, N2 |
| INPUTS | corpus·실제 설치본·원장 시점 대조 R1/R8 |
| REFERENCE GRAMMAR | 0건 전제 반증, bare·범위·제외영역 보완 R1/R3 |
| CHANGE DETECTION PIPELINE | 조기 종료·old/new 경로·간접 영향 R2/R4/R8 |
| IMPACT CLASSIFICATION | 3단계 유지, 별도 pending·근거 기반 승격 R2/R9 |
| NON-GIT FALLBACK | observed/historical, 동일 비교 범위 R5 |
| LOCAL-PATCH HANDLING | 재적용 결과와 의미 검토 R6 |
| PROVENANCE MODEL | 네 축 유지, 검증 종류·좌표 기준 R7 |
| LOCKING / APPLY PROCEDURE | 잠금·backup 유지, 결합 복구 R10 |
| CODEX / CLAUDE ROLE SPLIT | 독립 검토 유지, 네트워크 전달 계약 R8; 비교 단위 N1 |
| OUTPUT SCHEMA | repo 키·양쪽 경로·검증 범위 R4/R7/R8 |
| FAILURE MODES | 기존 11개 유지·조건 강화, F1-F8와 R9 추가 |
| ACCEPTANCE CRITERIA | coverage·미해결 disposition·복합 목표 해시 R6/R7/R9/R10 |
| PILOT ROLLOUT ORDER | EFDC 조건부, 문법 시험 선행 R11 |

요청한 여섯 공격 지점도 모두 검토했다: parser=C1/C2/M1/M2/F2/F3, large diff=M3/M4/N4/F4, non-git=C3/F5, local patch=C4/F6, provenance=C5/M5/F1, automation=C1/C2/C5 및 위 자동화 경계.

[PILOT SUITABILITY]

**EFDC/EFDCPlus_Stable은 조건부로 적합하다. 현재 자료만으로 “변경이 작고 참조 처리를 실질적으로 시험한다”는 결론은 미확인이다.**

- 장점: `S/manifest.csv:15`에 +1 commit, `S/provenance-final.csv:15`에 CLEAN/BASE_SHA/EXPLICIT_MATCH가 기록돼 있다. `models/EFDC/source-analysis/efdc_hydro_core.md:19-39`는 explicit·bare·파일 단위·노트 연결을 함께 제공한다. 인프라 및 혼합 문법의 두 번째 적용 후보로 합리적이다.
- 한계: 510/247은 모델 집계이며 EFDC-GVC와 매뉴얼 참조가 섞여 있다. 어떤 노트가 EFDCPlus 변경 hunk와 교차하는지, 새 commit이 코드인지 문서인지, rename이나 줄 이동이 있는지는 미확인이다. +1 commit만으로 낮은 실패 비용을 보장하지 않는다. 네트워크/raw 금지 때문에 이 리뷰에서는 그 diff를 확보하지 않았다.
- 권고: EFDC 순서는 유지하되 **고정된 old/new 변경 목록과 실제 참조 교집합을 먼저 검토**한다. 유의미한 교집합이 없으면 NO_ACTION 경로 검증 성공으로만 기록하고, migration framework 전반 검증 성공으로 확대하지 않는다. R1-R10 중 해당 경로의 차단 결함을 먼저 보완해야 한다.
- 대안: EFDC가 무교집합·메타데이터 변경뿐이라면 다음 후보인 ROMS/roms(+6, `S/manifest.csv:20`)에서 실제 교집합을 확인한 뒤 선택할 수 있다. ROMS의 현재 diff 적합성도 미확인이다. SWAN은 실제 BEHIND(:27)이므로 비-GitHub·혼합 인용 시험 후보지만 “file:line 없는 모델”이라는 이유로 선택하면 안 된다. SWASH는 CURRENT(:28)이므로 업데이트를 만들어 시험하지 말고 읽기 전용 문법 사례로 사용한다. non-git·local patch·rename/split 경로는 EFDC 파일럿 성공으로 검증됐다고 간주하지 않는다.

DESIGN 전 절과 여섯 검토 지점을 다뤘으므로 여기서 종료한다. 이 리뷰 파일 외 쓰기, 구현, wiki 수정, migration 실행은 수행하지 않았다.
