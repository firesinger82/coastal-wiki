# CADMAS-2F_Manural_English.pdf p.91–108 전수 대조

검증일은 2026-11-04다.
검증자는 codex gpt-6-astra다.
이 문서는 원문과 구분되는 AI 검증 기록이다.

- 원본 PDF: `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Manual/CADMAS-2F_Manural_English.pdf`.
- 수정 기록: [p091-108.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Manual/CADMAS-2F_Manural_English.pdf/p091-108.md).
- 이미지 디렉터리: `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/`.
- 아래 근거의 `cad-2f-manual-NNN.png`는 이 디렉터리의 파일이다.

## 대조 범위와 결과

PDF p.91–108의 300 dpi PNG 18개를 이미지 보기 도구로 각각 직접 열었다.
대조한 쪽 수는 지정 범위의 18쪽이다.
내용을 고친 쪽 수는 p.101·102·104의 3쪽이다.
보완한 쪽 수는 이 3쪽이다.
기존 내용의 오기를 정정한 쪽은 없다.
나머지 15쪽은 기존 기록과 일치한다.
표의 쪽 행 18개를 유지했다.
기존 frontmatter는 유지했다.
frontmatter에는 지정된 `verified_by` 한 줄만 추가했다.
원본 PDF의 SHA-256은 기록의 값과 일치한다.

| 쪽 | 결과 | 대조한 내용 |
|---|---|---|
| p.91 | 일치 | Table 0-4-14·15의 캡션, 파일명, 변수명, 자료형, 선택값, 출력 시간 원소 설명. |
| p.92 | 일치 | 앞 쪽에서 이어지는 Table 0-4-15의 출력 시간 원소와 RTRVAL·PRTOLD·PRTNOW·DMTBT0. |
| p.93 | 일치 | Table 0-4-16·17의 캡션, 파일명, 격자 수, 계산 여부, 병렬화 변수. |
| p.94 | 일치 | 앞 쪽에서 이어지는 Table 0-4-17의 셀 번호, virtual 조건, 버퍼 수, 배열 범위. |
| p.95 | 일치 | Table 0-4-18·19의 캡션, 좌표 범위, IBCTYP의 차원과 모든 선택값, IDAMP. |
| p.96 | 일치 | 앞 쪽에서 이어지는 Table 0-4-19의 IDAMP 원소와 IDROP 처리 조건. |
| p.97 | 일치 | Table 0-4-20의 전체 변수와 자료형, 물리량 설명, 기호의 기준선, BCTYP 차원. |
| p.98 | 일치 | 앞 쪽에서 이어지는 Table 0-4-20의 조파 경계 원소, Table 0-4-21의 캡션과 개방 경계 원소, DAMP. |
| p.99 | 일치 | 앞 쪽에서 이어지는 Table 0-4-21의 DAMP 원소와 WBUB 조건, Table 0-4-22의 전체 변수와 선택값. |
| p.100 | 일치 | Table 0-4-23의 캡션, 파일명, 전체 변수와 자료형, 시간 간격 설명. |
| p.101 | 보완 | 절 제목, 본문 전체 문장, Table 0-4-24의 캡션, 격자 배열의 모든 식, UU와 참조 번호. |
| p.102 | 보완 | 앞 쪽에서 이어지는 배열명 끝부분, Table 0-4-24의 전체 변수와 식, 참조 번호. |
| p.103 | 일치 | Table 0-4-25의 캡션, 전체 변수와 설명의 대응, 식, 참조 번호, 다음 쪽으로 이어지는 AE. |
| p.104 | 보완 | 앞 쪽에서 이어지는 배열명 끝부분, Table 0-4-25의 전체 변수, 별도 변수명이 없는 설명, 식과 기호, 참조 번호. |
| p.105 | 일치 | 앞 쪽에서 이어지는 배열명 끝부분, WKBC의 자료형·설명·참조. |
| p.106 | 일치 | Table 0-4-26의 캡션, NF·INDX·INDY·INDZ·INDC의 차원과 모든 선택값, 참조 번호. |
| p.107 | 일치 | Table 0-4-27의 캡션, INDB 차원, 좌표 식, 방향과 경계조건 선택값, 참조 번호. |
| p.108 | 일치 | 앞 쪽에서 이어지는 INDB 선택값, INDS의 차원과 식, INDBK·INDBE의 모든 선택값과 이류항 평가 조건, 참조 번호. |

## 정정·보완 목록

정정 항목은 없다.
아래 목록은 보완한 내용이다.

| 쪽 | 이전 | 새 | 근거 |
|---|---|---|---|
| p.101 | 본문 첫 문장의 표 범위 설명이 없었다. | Table 0-4-24부터 Table 0-4-28까지 주 루틴에서 선언한 실체 전역 변수의 상세 설명을 제시한다는 안내를 추가했다. 기존 배열 변수 설명과 동적 결정 설명은 문장을 나누어 유지했다. | `cad-2f-manual-101.png`의 4.4.3 제목 아래 본문 첫 문장은 `Table 0-4-24 to Table 0-4-28 show the detailed explanation of substantial global variables declared by the main routine.`이다. 마지막 문장은 `It is determined dynamically.`이다. |
| p.102 | 상단의 `MK)`를 이 쪽 행에 적지 않았다. | p.101의 `UU(NUMI,NUMJ,NU`에서 이어지는 배열명 끝부분이라고 추가했다. | `cad-2f-manual-101.png`의 마지막 변수명과 `cad-2f-manual-102.png`의 맨 위 왼쪽 셀. |
| p.104 | 상단의 `MK)`를 이 쪽 행에 적지 않았다. | p.103의 `AE(NUMI,NUMJ,NU`에서 이어지는 배열명 끝부분이라고 추가했다. | `cad-2f-manual-103.png`의 마지막 변수명과 `cad-2f-manual-104.png`의 맨 위 왼쪽 셀. |

## 확대 확인과 원문 표기

p.97의 `Cμ`, `σk`, `σ e`, `C1`, `C2`, `C3`, `κ`를 부분 확대했다.
이 기호들의 같은 기준선 표기는 기존 기록과 일치한다.
p.99 상단의 DAMP 원소 번호와 위치 설명을 부분 확대했다.
p.101의 격자 식과 `84, J):`를 부분 확대했다.
p.104의 시간 의존 식과 `ν t`를 부분 확대했다.
p.107·108의 좌표 식을 각각 부분 확대했다.
확대 이미지는 지정 PNG에서 메모리 안에서 잘라 보았다.
별도 이미지 파일은 쓰지 않았다.

원문 p.93의 `Parallelization related (real)`과 `I*4`를 그대로 유지했다.
원문 p.95의 `IBCTYP(2, 4)`와 내용 칸의 `(3, *)`, `(4, *)`를 그대로 유지했다.
원문 p.101의 `84, J):`를 그대로 유지했다.
원문 p.102–104의 식에서 `CM`을 `CM0`로 바꾸지 않았다.
원문 p.103–104의 변수명과 설명 대응을 재배치하지 않았다.
원문 p.104의 `CC((NUMI,NUMJ,NUMK,LEQC)`를 그대로 유지했다.
원문 p.104의 `WK01-` 다음 줄에는 `17(NUMI,NUMJ,NU`가 인쇄되어 있다.
원문 p.108의 값 `2` 설명에 없는 여는 괄호를 추가하지 않았다.
이 사항들은 기존 기록 끝의 「판독 중 확인된 사실」에도 남아 있다.

이 범위에는 일본어 문장이 없다.
이 범위에는 그림 자체가 없다.
표의 `Figure` 번호는 참조 번호다.
이 범위에는 물리 단위나 수치 기본값이 별도로 제시되지 않는다.
이번 작업은 지정한 이미지와 판독 기록의 대조다.
모델 코드의 구현이나 물리적 타당성은 검증하지 않았다.

## 열지 못한 이미지

없음.
지정된 18개 PNG를 모두 열었다.
이미지에서 판독하지 못한 항목은 없다.

마지막 집계는 쪽 행 기준이다.
정정 0, 보완 3, 일치 15
