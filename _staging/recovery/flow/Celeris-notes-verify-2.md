# Celeris 노트 전수 대조 — 두 번째 몫

- 대상: `models/Celeris/source-analysis/celeris-transect-version.md`.
- 착수 시 전체 348줄을 순서대로 116줄씩 나눴다.
- 담당 범위: 착수 시 117–232줄, 총 116줄. 빈 줄과 표 구분 줄도 포함한다.
- 상태: 담당 범위 대조 완료.
- 기계 확인 불일치 후보: 사용자 제공 후보 없음.

## 완료 기록

- [celeris-transect-version.md](../../../models/Celeris/source-analysis/celeris-transect-version.md)의 117–232줄을 모두 대조했다.
- 대조한 줄 수는 116줄이다. 담당 범위는 모두 차이 표 행이다. 담당 범위에 frontmatter와 mermaid 블록은 없다.
- 정정은 2줄이다. 보완은 1줄이다. 착수 시 내용과 최종 내용을 비교한 변경 줄은 147·202·217줄이다.
- 각 행의 분류와 결론을 [최종 배정표](../assign/Celeris-final-conclusions.tsv), [CT1a 최종 근거](../compare/Celeris-conclusion-verify-CT1a.md), [CT1b 최종 근거](../compare/Celeris-conclusion-verify-CT1b.md)와 대조했다.
- 담당 행에서 센 분류는 A 56행, C 6행, E 중간 1행, E 강함 2행, F 51행이다. 분류 변경은 없다.
- A 행의 과거 판 원문은 노트에 적힌 커밋과 파일을 `git show`로 열었다. [AD3 판 대조](../compare/Celeris-version-verify-AD3.md)와 [E2 판 대조](../compare/Celeris-version-verify-E2.md)의 해당 행도 대조했다. 과거 판 대조와 최종 결론이 다른 경우에는 최종 결론의 이유를 적용했다.
- [원 보고서 §4](../compare/celeris-transect-vs-main.md#4-노트-대조와-수정안)와 [반영 기록 1](Celeris-notes-apply-1.md), [반영 기록 2](Celeris-notes-apply-2.md)를 대조했다. 담당 범위는 새 차이 표이며 기존 본문을 대체한 줄은 없다.
- 최종 검사에서 경로·줄 인용 723개를 열었다. 현재 판 인용은 568개다. 이전 커밋 인용은 155개다. 이 수는 중복 인용을 포함한다.
- 코드 원문 칸의 인용 토막 3,384개는 각각 지정한 원문 줄·범위에 포함된다. 표의 `\|` 이스케이프를 해제한 뒤 글자를 비교했다. 결론 칸의 조건문·식은 별도로 대조했다.
- 대조한 현재 원문 파일에 대한 `git diff -U0 ebca435 -- <파일 목록>`의 출력은 비어 있다.
- 담당 범위의 상대 링크 116개는 모두 노트 위치에서 실제 파일로 연결된다. 절대 사용자 경로, 홈 약식 경로, 위키 링크 표기는 없다.
- 아래 정정·보완을 제외한 결론은 최종 근거와 같다. 문서 원문으로 위장한 설명 인용은 없다. 작업 한계 문장은 정정 후 담당 범위에 없다.
- 모델 실행과 git 쓰기 명령은 수행하지 않았다. 미해결 항목은 없다.

아래 집계는 담당 범위의 행별 원문 인용 검사 결과다. 원문 인용 수는 중복을 포함한다.

| 노트 줄 | 행 ID 범위 | 대조 줄 수 | 원문 인용 수 | 결과 |
|---|---|---:|---:|---|
| 117–146 | CT1-088–127 중 노트에 있는 모든 행 | 30 | 198 | 정정 없음 |
| 147–176 | CT1-128–162 중 노트에 있는 모든 행 | 30 | 207 | 147줄 정정 |
| 177–206 | CT1-163–197 중 노트에 있는 모든 행 | 30 | 178 | 202줄 보완 |
| 207–232 | CT1-198–223 중 노트에 있는 모든 행 | 26 | 140 | 217줄 정정 |
| 합계 | 담당 범위 전체 | 116 | 723 | 정정 2줄·보완 1줄 |

## 정정·보완 목록

1. 정정 — `models/Celeris/source-analysis/celeris-transect-version.md:147`, CT1-128.
   - 전: 결론 칸에 “예제 내부는 판독하지 않는다.”가 있었다.
   - 후: 해당 문장을 삭제했다. 결론 칸 끝에 `[11-04 전수 검증 정정]`을 붙였다.
   - 근거: 최신 사용자 지시의 작업 한계 문장 제거 기준이다. 유지한 기능 결론은 `transect_version/js/constants_load_calc.js:168`의 `"./examples/Hermosa_Beach_CA_COULWAVE/"`, 같은 파일 174줄의 `colorMap_choice: 2,`, `js/constants_load_calc.js:220`의 `colorMap_choice: 0,`과 같다. CT1b의 CT1-128 기능 결론과 판 차이 커밋은 유지했다.
2. 보완 — `models/Celeris/source-analysis/celeris-transect-version.md:202`, CT1-193.
   - 전: 결론은 `if (near_dry > 0. )`를 설명하지만 해당 행의 transect 원문 범위는 199–298줄이었다.
   - 후: 원문 칸에 `transect_version/shaders/Pass3_Bous.wgsl:194`와 `if (near_dry > 0. )`를 추가했다. 결론 칸 끝에 `[11-04 전수 검증 보완]`을 붙였다.
   - 근거: 194줄의 조건문이 286줄의 Psi1x 식과 287줄의 Psi2x 식을 감싼다. CT1b의 CT1-193 결론은 유지했다.
3. 정정 — `models/Celeris/source-analysis/celeris-transect-version.md:217`, CT1-208.
   - 전: 결론 칸의 식은 `Psi1x+Psi2x`였다.
   - 후: 결론 칸의 식을 `Psi1x + Psi2x`로 고쳤다. 결론 칸 끝에 `[11-04 전수 검증 정정]`을 붙였다.
   - 근거: `transect_version/shaders/Pass3_COULWAVE.wgsl:492`의 활성 source 식은 `breaking_x + (Psi1x + Psi2x) + press_x`다. 합산의 의미와 CT1b의 CT1-208 분류는 유지했다.

세 줄은 각각 `apply_patch` 직전에 다시 읽었다. 각 패치는 대상 노트 한 줄만 변경했다.

## 기계 확인 후보 판정

- 사용자 제공 후보: 없음.
- 자체 검사 CT1-122: TSV의 E 표시는 강도를 생략한다. 최종 근거 CT1a는 중간이다. 노트의 중간 표시는 맞다.
- 자체 검사 CT1-183: TSV의 E 표시는 강도를 생략한다. 최종 근거 CT1b는 강함이다. 노트의 강함 표시는 맞다.
- 자체 검사 CT1-196: TSV의 E 표시는 강도를 생략한다. 최종 근거 CT1b는 강함이다. 노트의 강함 표시는 맞다.
- 자체 검사 CT1-128: 작업 한계 문장이 남아 있었다. 147줄에서 삭제했다.
- 자체 검사 CT1-183의 `U/2`: 원문 인용이 아니라 두 활성 면속도가 U인 경우의 대입 결과다. `(0 + U + 0 + U) / 4.0`과 같다. 정정하지 않았다.
- 자체 검사 CT1-186의 `v=0`: 원문 인용이 아니라 1D 환원 가정이다. CT1b의 조건과 같다. 정정하지 않았다.
- 자체 검사 CT1-193의 조건문: 원문 글자는 맞지만 해당 행에 적힌 원문 범위를 벗어났다. 202줄에 원문 194줄 인용을 보완했다.
- 자체 검사 CT1-205의 `v=0`: 원문 인용이 아니라 횡방향 항 제거의 가정이다. CT1b의 조건과 같다. 정정하지 않았다.
- 자체 검사 CT1-208의 `Psi1x+Psi2x`: 활성 source의 합산은 맞다. 원문 공백을 보존하도록 217줄을 정정했다.
- 자체 검사 CT1-214의 `y 미분=0`: 원문 인용이 아니라 본판 식에 대입하는 가정이다. CT1b의 조건과 같다. 정정하지 않았다.
- 자체 검사 CT1-214의 `Q=0`: 원문 인용이 아니라 횡운동량 가정이다. CT1b의 조건과 같다. 정정하지 않았다.

E 세 행은 모두 호출 조건이 있는 활성 경로다. 이 범위에는 “호출되지 않는 경로”라고 표시해야 하는 E 행이 없다. CT1-122의 반복 초기화는 `transect_version/js/main.js:2152–2173,3390–3406,3431`과 `transect_version/js/Time_Series.js:82–104`에서 대조했다. CT1-183은 같은 판의 `Pass1.wgsl:154–178`, `CalcMeans.wgsl:42–43`, `Pass3A_COULWAVE.wgsl:34–41`, `js/main.js:1593–1595`에서 대조했다. CT1-196은 같은 판의 `Pass3_Bous.wgsl:264–287,382–396`, `Update_TriDiag_coef.wgsl:62–69`, `js/main.js:1051–1057,1606–1607`에서 대조했다.
