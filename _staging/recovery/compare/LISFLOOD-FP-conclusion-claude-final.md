# LISFLOOD-FP 결론 전수 검증 뒤 Claude 최종 조정 (10-21)

이 파일은 `LISFLOOD-FP-conclusion-verify-*.md`의 최종 결론보다 우선한다.

## 1 8.3 패치가 고친 8.2 결함의 분류 통일

대조 단계 규칙은 8.3 패치가 고친 8.2 결함을 E로 두고 결론 문장에 "8.2 결함, 8.3에서 고침"을 적는 것이다. 전수 검증에서 같은 유형의 행 가운데 LG1-131, LI1-317, LV1-287은 E였고 LI2-352, LI1-369는 A였다. LN1-127도 같은 유형이다. 세 행을 E로 통일한다.

| 행 ID | 전수 검증 결론 | 최종 결론 | 근거 | 노트에 쓸 결론 문장 |
|---|---|---|---|---|
| LI2-352 | A | E·강함(8.2 결함, 8.3에서 고침) | `LISFLOOD-FP-conclusion-verify-LI2.md`의 같은 행 근거; 8.3 배포 README.md:32; `lisflood-8.2-to-8.3.patch:98–133` | v8.2 CUDA 최대 수심 버퍼는 ghost를 뺀 크기여서 결함이었다(8.2 결함, 8.3에서 고침). 현재 최대 수심 배열은 ghost를 포함한 device 버퍼이고, 출력 때 전체 크기를 host로 복사한다. |
| LI1-369 | A | E·강함(8.2 결함, 8.3에서 고침) | `LISFLOOD-FP-conclusion-verify-LI1.md`의 같은 행 근거; `lisflood-8.2-to-8.3.patch:75–89,110–112`; `VersionHistory.h:31–32` | 8.2 CUDA maxH 배열은 초기화되지 않았다(8.2 결함, 8.3에서 고침). 8.3은 0으로 초기화하고, 빈 NODATA 셀의 질량 갱신을 생략한다. |
| LN1-127 | A | E·중간(8.2 빌드 결함, 8.3에서 고침) | `LISFLOOD-FP-conclusion-verify-LN1.md`의 같은 행 근거; 8.3 배포 README.md:37; `lisflood-8.2-to-8.3.patch:264–268` | v8.2 루트의 `format` 파일(내용 `5`)은 macOS에서 C++ 표준 헤더 이름을 가렸다(8.2 빌드 결함, 8.3에서 고침). 8.3 패치는 이 파일을 삭제한다. |
