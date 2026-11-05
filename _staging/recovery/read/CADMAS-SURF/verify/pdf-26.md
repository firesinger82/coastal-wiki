# CADMAS-STR Program Instructions — p.1–18 전수 대조

검증일은 2026-11-04다.
검증자는 codex gpt-6-astra다.
원본 PDF는 `models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Manual/CADMAS-STR_Program Instructions_English.pdf`다.
대상 기록은 [p001-018.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Manual/CADMAS-STR_Program%20Instructions_English.pdf/p001-018.md)다.
기존 검증 결과 파일은 없었다.

## 대조 범위와 집계

대조한 쪽 수는 PDF p.1–18의 18쪽이다.
내용을 정정하거나 보완한 쪽 수는 아래 변경 목록의 서로 다른 쪽 번호를 센 7쪽이다.
정정한 쪽은 p.17의 1쪽이다.
보완한 쪽은 p.4, p.9, p.10, p.13, p.14, p.18의 6쪽이다.
내용이 일치한 쪽은 p.1, p.2, p.3, p.5, p.6, p.7, p.8, p.11, p.12, p.15, p.16의 11쪽이다.
마지막 줄의 수치는 변경 항목 수가 아니라 쪽 수다.
정정·보완·일치의 쪽 집계는 중복되지 않는다.

지정된 300 dpi PNG를 이미지 보기 도구로 모두 직접 열었다.
p.6–18의 작은 수식 기호는 원본 PNG의 해당 영역을 메모리에서 잘라 확대해서 확인했다.
확대 이미지는 파일로 저장하지 않았다.
철자 참고에는 지정된 텍스트 추출본을 사용했다.
판독 판단에는 PNG를 우선했다.

이미지 경로의 공통 디렉터리는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/`다.

| 쪽 | 직접 연 이미지 | 판정 | 대조 내용 |
|---|---|---|---|
| p.1 | cad-str-instr-001.png | 일치 | 표지 제목과 본문 부재. |
| p.2 | cad-str-instr-002.png | 일치 | 목차의 모든 항목과 쪽 번호 및 모듈·파일 이름. |
| p.3 | cad-str-instr-003.png | 일치 | 빈 쪽. |
| p.4 | cad-str-instr-004.png | 보완 | 기능 목록의 모든 항목과 단방향·양방향 연성 설명. |
| p.5 | cad-str-instr-005.png | 일치 | 두 흐름도의 제목·블록·파일명·화살표 방향·교환 자료 표기. |
| p.6 | cad-str-instr-006.png | 일치 | 절 제목과 기호 정의 및 식 ①·②와 번호 없는 전개. |
| p.7 | cad-str-instr-007.png | 일치 | 경계조건과 식 ③ 및 벡터 성분과 참고문헌·보간식. |
| p.8 | cad-str-instr-008.png | 일치 | 보간·미분 행렬과 절점 변수 정의 및 각 항의 이산화. |
| p.9 | cad-str-instr-009.png | 보완 | 식 ④·⑤와 시간 증분·β 범위 및 번호 없는 전개와 연결 문구. |
| p.10 | cad-str-instr-010.png | 보완 | 구성법칙 참고문헌과 힘·압력하중 증분식 및 new·old 첨자와 연결 문구. |
| p.11 | cad-str-instr-011.png | 일치 | 식 ⑥·⑦와 FTO·FTI·FCO·FCM·FCMD·FCD·FCK·FCP 표기 및 대응 위치. |
| p.12 | cad-str-instr-012.png | 일치 | 앞 쪽에서 이어지는 압력하중의 번호 없는 식과 본문 부재. |
| p.13 | cad-str-instr-013.png | 보완 | 식 ⑧·⑨와 기호 정의 및 가중잔차 전개와 경계 종류. |
| p.14 | cad-str-instr-014.png | 보완 | 식 ⑩의 이어지는 부분과 참고문헌 상세 및 보간·미분 행렬과 변수 정의. |
| p.15 | cad-str-instr-015.png | 일치 | 각 항의 이산화와 식 ⑪·⑫ 및 α 범위와 시간차분 전개. |
| p.16 | cad-str-instr-016.png | 일치 | 압력 시간차분과 식 ⑬·⑭ 및 번호 없는 대입식. |
| p.17 | cad-str-instr-017.png | 정정 | 이 쪽의 [5] 제목과 앞 쪽 절 번호의 구분 및 우변 전개와 FLO·FLI 표기. |
| p.18 | cad-str-instr-018.png | 보완 | 절 제목과 연성·분리 해법의 모든 문단 및 식 ⑮·⑯·⑰. |

## 정정·보완 목록

| p.N | 이전 | 새 | 근거 |
|---|---|---|---|
| p.4 | 다음 쪽 흐름도 안내가 없었다. | 다음 쪽에 흐름도를 제시한다고 적었다. | p.4 [2] 첫 문단의 `A flow diagram is shown on next page.` 보완. |
| p.4 | 교환 자료의 두 전달 방향만 적었다. | 이 두 자료를 서로 교환하면서 계산이 진행된다는 문장을 추가했다. | p.4 (2) ②의 `The calculation proceeds by exchanging the following data with each other.` 보완. |
| p.9 | 힘 증분식 바로 앞의 독립 문구가 없었다. | `In this time`과 ‘이때’라는 뜻을 추가했다. | p.9 맨 아래 힘 증분식 바로 위. 보완. |
| p.10 | 첫 번째 `Base on`이 없었다. | 앞의 관계에 근거하여 다음 식을 제시한다는 연결 문구로 기록했다. | p.10 구성법칙 참고문헌 아래의 독립 문구. 보완. |
| p.10 | 압력하중 증분식 바로 앞의 독립 문구가 없었다. | `In this time`과 ‘이때’라는 뜻을 추가했다. | p.10 압력하중 증분식 바로 위. 보완. |
| p.10 | 두 번째 `Base on`이 없었다. | 앞의 관계에 근거하여 다음 식을 제시한다는 연결 문구로 기록했다. | p.10 압력하중 증분식 바로 아래. 보완. |
| p.13 | [2]의 영문 제목이 없었다. | `Application of the weighted residual method`를 추가했다. | p.13 [2] 제목. 보완. |
| p.13 | S₁의 조건만 적었다. | S₁을 제1종 경계(`Type 1 boundary`)로 명시했다. | p.13 S₁ 정의. 조건식은 인쇄대로 유지했다. 보완. |
| p.13 | S₂의 조건만 적었다. | S₂를 제2종 경계(`Type 2 boundary`)로 명시했다. | p.13 S₂ 정의. 보완. |
| p.14 | Yagawa와 Yoshimura의 1995년 책 Chapter 5로 줄였다. | `Motoki Yagawa and Shinobu Yoshimura, Finite Element Method, Computational Mechanics and CAE Series 1, Baifukan, 1995, Chapter 5`를 기록했다. | p.14 [3] 첫 문단의 첫 번째 참고문헌. 보완. |
| p.14 | MacNeal의 1976년 `The PENTA Solid Element`로 줄였다. | 오면체 요소의 보간함수라는 대상을 명시했다. `MacNeal, R.H., The PENTA Solid Element, MSC Internal Memo No. RHM-43, Oct. 22, 1976`을 기록했다. | p.14 [3] 첫 문단의 두 번째 참고문헌. 보완. |
| p.17 | `2.1.2 [5] Correspondence with variables in the program`으로 시작했다. | 2.1.2는 앞 쪽에서 이어지는 절임을 명시했다. 이 쪽에서 시작하는 제목은 [5]임을 구분했다. | p.17 상단에는 [5]만 인쇄되어 있다. 2.1.2 제목은 p.13에 있다. 정정. |
| p.18 | 계수의 자릿수 차이와 CG법 수렴의 관계를 영어로만 인용했다. | 계수들 사이의 큰 자릿수 차이를 한국어로 설명했다. 이 차이가 원문이 section 3에서 설명한다고 지칭한 병렬 CG법의 수렴에 불리하다는 뜻을 추가했다. | p.18 2.1.4 첫 문단의 `However` 문장. 보완. |

## 형식과 원문 표기의 처리

기록의 쪽별 표는 18행으로 유지했다.
기존 frontmatter 값은 모두 유지했다.
frontmatter에는 요청한 `verified_by` 한 줄만 추가했다.
각 쪽 행 끝에는 해당 검증 표지를 추가했다.

p.7, p.8, p.9, p.10, p.11, p.12, p.14, p.15, p.16의 기존 ‘계속’ 표시는 ‘앞 쪽에서 이어지는 절’이라는 표현으로 통일했다.
이 표현 정리는 이미 기록된 쪽 경계의 뜻을 유지한다.
표현 정리만 한 p.7, p.8, p.11, p.12, p.15, p.16은 내용 일치로 집계했다.

인쇄된 수식의 첨자·부호·식 번호는 기존 기록과 일치했다.
수식은 수정하지 않았다.
p.5의 `Displacemen`은 원문 그대로 유지했다.
p.13의 S₁ 조건은 원문 그대로 유지했다.
p.17의 설명문이 식 ⑥을 참조하는 표기도 유지했다.
p.17의 전개에서 압력 상선이 사라지는 표기도 유지했다.
p.18 식 ⑯의 G와 상선 없는 R도 유지했다.
원문 표기의 불일치는 기록 끝의 ‘판독 중 확인된 사실’에 남겼다.
이 절에는 p.4의 MPMD 괄호 표기와 p.6의 `equation if motion` 표기도 추가했다.
이 절에는 p.18의 section 3 참조와 p.2 목차의 3절 제목도 추가했다.

p.1–18에는 일본어 문장이 없다.
p.1–18에는 입력 키워드별 기본값을 나열한 표가 없다.
p.2의 목차 쪽 번호는 모두 대조했다.
p.9의 β 범위와 p.15의 α 범위는 모두 대조했다.
원문에 없는 단위나 기본값은 추가하지 않았다.

## 열지 못한 이미지

없음.
지정된 cad-str-instr-001.png부터 cad-str-instr-018.png까지 모두 열었다.

정정 1, 보완 6, 일치 11
