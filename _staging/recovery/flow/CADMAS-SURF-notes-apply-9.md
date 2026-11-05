# CADMAS-SURF 노트 반영 job 9

대상은 [배정표](../assign/CADMAS-SURF-note-job-9.tsv)의 173행과 지정 노트의 수정안이다.

## 작업 기록

- 새 차이 노트의 배정 행 반영을 마쳤다.
- 기존 지배방정식 노트의 수정안 반영을 마쳤다.

## 파일별 반영 결과

### cadmas-surf3d-manual-differences.md

- 파일: [새 차이 노트](../../../models/CADMAS-SURF/manual-notes/cadmas-surf3d-manual-differences.md).
- 추가 범위: `models/CADMAS-SURF/manual-notes/cadmas-surf3d-manual-differences.md:1–210`.
- 표 범위: `models/CADMAS-SURF/manual-notes/cadmas-surf3d-manual-differences.md:38–210`.
- 넣은 행 수: 배정표 173행과 같은 173행이다.
- 분류별 행 수: 표의 결론 열에서 A 111행, B 38행, C 24행을 셌다.
- 보고서별 행 수: 배정표와 표에서 3d-input 29행, 3d-program 142행, 3d-theory 2행을 셌다.
- 반영한 수정안 행 ID: 보고서 §4에서 새 파일을 직접 가리키는 행은 없다.
- 넣지 않은 배정 행: 없음.

### cadmas-surf3d-english-manual-governing-equations.md

- 파일: [지배방정식 노트](../../../models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md).
- 수정 범위는 다음 파일 위치이다.
  - `models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:6`
  - `models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:24–29`
  - `models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:55`
  - `models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:57`
  - `models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:59–64`
  - `models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:66–67`
  - `models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:69–71`
  - `models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:75–76`
  - `models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:86–89`
  - `models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:100`
  - `models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:102`
  - `models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:104–106`
- 추가 범위는 `models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:11`과 `models/CADMAS-SURF/manual-notes/cadmas-surf3d-english-manual-governing-equations.md:112–121`이다.
- 넣은 배정 표 행 수: 0행이다.
- 반영한 수정안 행 ID는 아래 목록과 같다.

| 수정안 행 ID | 반영 내용 | 반영한 줄 |
|---|---|---|
| 3d-theory:KS1-701 | 연속식의 γ와 PDF 쪽을 정정했다. | 55,57,59 |
| 3d-theory:KS1-702 | 운동량 시간항·점성항·소스 부호와 γ·λ 정의를 정정했다. | 60–64 |
| 3d-theory:KS1-703 | 가상질량의 λ 좌변과 γ 우변을 정정했다. | 66–67,104 |
| 3d-theory:KS1-704 | 저항식의 거리 분모와 코드의 XX(5,I)를 복원했다. | 69–71,105 |
| 3d-theory:KS1-705 | VOF 면 계수를 정정했다. 공극률 차이를 별도로 적었다. | 75–76,106 |
| 3d-theory:KS1-706 | 감쇠계수의 N+1·절댓값과 VEULER 근거를 정정했다. | 86–89 |
| 3d-theory:KS1-707 | 포괄적인 식 단위 확증 표현을 바꿨다. 난류 부력 생성과 조파 스칼라 생성을 일치 목록에서 제외했다. | 24–29,100,102 |
| 3d-program:KS2-816 | Ch2 발췌 범위를 유지했다. 프로그램 구조의 PDF p.58–100을 연결했다. | 24,114 |
| 3d-input:KS3-407 | LC의 정수형·PORO의 R*8·출력의 2-노름을 보충했다. 최종 근거의 KS3-046·234·251을 따랐다. | 116–120 |

- 상호 링크: 새 파일의 22줄과 기존 노트의 112줄에 넣었다.
- 넣지 않은 수정안 행: 없음.

## 확인 결과

- 배정표의 173개 행 ID와 새 표의 173개 행 ID는 순서까지 같다.
- 배정표의 최종 분류와 최종 근거 파일의 분류를 대조했다.
- 새 표의 결론 문장은 최종 근거 파일의 결론 문장과 같다.
- 결론 문장 대조에서는 백틱과 출처 경로 표기만 정규화했다.
- 새 표의 모든 행에 최종 근거 파일의 확인한 원문 위치를 옮겼다.
- Markdown 렌더 결과에서 새 표의 173행은 각각 6칸이다.
- Markdown 렌더 결과에서 기존 노트의 기능표는 17행이며 각 행은 3칸이다.
- Markdown 렌더 결과에서 기존 노트의 대조 요약표는 7행이며 각 행은 4칸이다.
- 두 노트의 frontmatter와 상대 링크를 확인했다.
- 두 노트에서 금지 경로·위키 링크 문자열을 검사했다.
- 배정표와 수정안에서 넣지 않은 행은 없다.
