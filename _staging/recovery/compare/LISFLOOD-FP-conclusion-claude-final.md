# LISFLOOD-FP 결론 전수 검증 뒤 Claude 최종 조정 (10-21)

이 파일은 `LISFLOOD-FP-conclusion-verify-*.md`의 최종 결론보다 우선한다.

## 1 8.3 패치가 고친 8.2 결함의 분류 통일

대조 단계 규칙은 8.3 패치가 고친 8.2 결함을 E로 두고 결론 문장에 "8.2 결함, 8.3에서 고침"을 적는 것이다. 전수 검증에서 같은 유형의 행 가운데 LG1-131, LI1-317, LV1-287은 E였고 LI2-352, LI1-369는 A였다. LN1-127도 같은 유형이다. 세 행을 E로 통일한다.

| 행 ID | 전수 검증 결론 | 최종 결론 | 근거 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|
| LI2-352 | A | E·강함(8.2 결함, 8.3에서 고침) | `LISFLOOD-FP-conclusion-verify-LI2.md`의 같은 행 근거; 8.3 배포 README.md:32; `lisflood-8.2-to-8.3.patch:98–133` | v8.2 CUDA 최대 수심 버퍼는 ghost를 뺀 크기여서 결함이었다(8.2 결함, 8.3에서 고침). 현재 최대 수심 배열은 ghost를 포함한 device 버퍼이고, 출력 때 전체 크기를 host로 복사한다. |
| LI1-369 | A | E·강함(8.2 결함, 8.3에서 고침) | `LISFLOOD-FP-conclusion-verify-LI1.md`의 같은 행 근거; `lisflood-8.2-to-8.3.patch:75–89,110–112`; `VersionHistory.h:31–32` | 8.2 CUDA maxH 배열은 초기화되지 않았다(8.2 결함, 8.3에서 고침). 8.3은 0으로 초기화하고, 빈 NODATA 셀의 질량 갱신을 생략한다. |
| LN1-127 | A | E·중간(8.2 빌드 결함, 8.3에서 고침) | `LISFLOOD-FP-conclusion-verify-LN1.md`의 같은 행 근거; 8.3 배포 README.md:37; `lisflood-8.2-to-8.3.patch:264–268` | v8.2 루트의 `format` 파일(내용 `5`)은 macOS에서 C++ 표준 헤더 이름을 가렸다(8.2 빌드 결함, 8.3에서 고침). 8.3 패치는 이 파일을 삭제한다. |

## 2 검증 모델 비교 시험에서 찾은 1행 (11-04)

사용자 지시(11-04)로 `LISFLOOD-FP-conclusion-verify-LB1a.md`와 같은 지시문을 Codex `gpt-6.1-sol`과 `gpt-6.1-terra`로 다시 돌렸다. 세 모델의 결론이 갈린 행을 Claude가 쪽 이미지와 코드로 판정했다. 그중 LB1-136은 전수 검증 결론 A가 틀렸다. 사용자가 B로 고치라고 지시했다. 같은 보 식을 다룬 LV1-220·LT1-164·LT1-406·LB1-386도 같은 근거로 B로 고쳤다(사용자 승인 11-04). Claude가 user manual.pdf p.29·40, user manual.docx p.34·45(변환본), user manual +bridge.docx p.29(변환본)의 쪽 이미지를 열어 식과 계수 문장을 확인했다. 1.4·1.7이 `C·L·H^{1.5}` 꼴의 계수라는 점은 외부 원문으로 확인했다. [hydraulics-and-hydrology] PAGE-61 식 (5.1)은 자유 월류를 `q = m(η − z_crest)^{3/2}`, `m = (2/3)√((2/3)g) ≈ 3.1 ft^{0.5}/s`로 적는다(쪽 이미지 확인). 이 m은 SI 단위에서 1.7049이다. SFINCS 코드도 광정 보에 `cweir = 1.7049`(`sfincs_structures.f90:651`)와 `qstruc = Cd*cweir*h1**1.5`(`:679`)를 쓴다.

| 행 ID | 전수 검증 결론 | 최종 결론 | 근거 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|
| LB1-136 | A | B 문서 오기 | user manual +bridge.docx p.29(변환본) 쪽 이미지: 식 `Q = CL(2gH)^{1.5}`, `C = Weir flow Coefficient. Default value would be 1.4`, `Qcoeff is the weir discharge coefficient, typically ranging from 0.5-1.7 and taking a value if 1.4 for a standard broad crested weir.`, Buscot 예제 계수 `1.7`; `weir_flow.cpp:85–88`; `v8.0:weir_flow.cpp:85–88`; `input.cpp:161–163`. 분류 기준 B의 "식의 계산 오류"와 "같은 쪽 안의 모순"에 해당한다. 전수 검증은 "문서는 C의 차원을 정하지 않는다"고 보았으나, 같은 쪽이 C의 값을 적으므로 식과 계수값의 모순을 판정할 수 있다. | user manual +bridge.docx p.29(변환본)의 인쇄식은 `Q = CL(2gH)^{1.5}`이다. 같은 쪽의 기본값 1.4와 예제값 1.7을 이 식에 넣으면 `C·L·H^{1.5}`의 `(2g)^{1.5}`배(약 86.9배)이다. 같은 쪽의 식과 계수값이 서로 맞지 않으므로 문서 판 시점에도 식이 틀렸다. |
| LV1-220 | A | B 문서 오기 | user manual.docx p.45(변환본) 식 (5)와 `C is the Weir flow Coefficient (default value 1.4)`; p.34(변환본) `C is the weir flow coefficient, typically ranging from 0.5-1.7 and taking a value if 1.4 for a standard broad crested weir.`와 예제 계수 `1.7`; LB1-136과 같은 근거 | user manual.docx p.45(변환본) 식 (5) `Q = CL(2gH)^{1.5}`에 같은 문서의 계수값 1.4·1.7을 넣으면 `C·L·H^{1.5}`의 `(2g)^{1.5}`배이다. 같은 문서의 식과 계수값이 서로 맞지 않으므로 문서 판 시점에도 식이 틀렸다. |
| LT1-164 | A | B 문서 오기 | user manual.pdf p.40 식 (5)와 `C is the Weir flow Coefficient (default value 1.4)`; p.29 같은 계수 범위 문장과 예제 계수 `1.7`; LB1-136과 같은 근거 | user manual.pdf p.40 식 (5) `Q = CL(2gH)^{1.5}`에 같은 문서의 계수값 1.4·1.7을 넣으면 `C·L·H^{1.5}`의 `(2g)^{1.5}`배이다. 같은 문서의 식과 계수값이 서로 맞지 않으므로 문서 판 시점에도 식이 틀렸다. |
| LT1-406 | A | B 문서 오기 | 노트가 옮긴 user manual.pdf p.40 식 (5)와 기본값 1.4; LT1-164와 같은 근거 | LT1-164와 같다. 현재 파서는 `Cd=1.4`를 생략 기본값으로 대입하지 않는다. |
| LB1-386 | A | B 문서 오기 | 노트가 옮긴 user manual.pdf p.40·user manual +bridge.docx p.29(변환본) 인쇄식; LB1-136·LT1-164와 같은 근거 | 두 문서의 인쇄식 `Q = CL(2gH)^{1.5}`는 같은 문서의 계수값 1.4·1.7과 맞지 않는다. 접근속도수두 차이와 계수 차이는 따로 적는다. |
