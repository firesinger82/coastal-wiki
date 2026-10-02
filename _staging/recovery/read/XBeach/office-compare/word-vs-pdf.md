# XBeach Word 판 ↔ PDF 판 대조 (2026-10-02, 기계 대조)

대상: `source_code/trunk/doc/manual/XBeach_manual_kingsday.docx`, `XBeach_manual_master.docx`, `source_code/trunk/doc/reports/non-hydrostatic_report_draft.doc` ↔ 같은 이름의 PDF.

방법: Word 판을 LibreOffice로 텍스트 변환(`_staging/recovery/extract/XBeach/office/`), PDF는 opendataloader-pdf markdown(`--use-struct-tree`, `_staging/recovery/extract/XBeach/pdf-md/`). Word 판의 12단어 이상 문단마다 6단어 연속 묶음이 PDF 텍스트에 몇 % 있는지 셈. 50% 미만 문단만 따로 확인.

| 문서 | Word 문단(12단어 이상) | PDF 텍스트에서 50% 미만 | 확인 결과 |
|---|--:|--:|---|
| kingsday | 766 | 10 | 모두 PDF에 있음: 그림·표 캡션의 Word 필드 코드("Figure Equation Chapter 2 Section 1…"), 표 셀 줄바꿈, 하이픈 차이(quasi-explicit ↔ quasiexplicit) |
| master | 825 | 11 | 같음 |
| non-hydrostatic | 312 | 9 | Word 텍스트 변환에서 수식 개체가 빠져 문장이 끊긴 것(예: "A cell with its centre at  is bounded by…") — PDF 판에는 수식 포함 |

결론: Word 판에만 있는 실질 내용은 찾지 못했다. Word 판은 PDF 판 판독 기록(`manuals/pdfs/`, `manuals/reports/`)으로 갈음한다. 처음 텍스트 형식(`-f text`) 추출에서는 글머리표 목록이 빠져 "Word에만 있음" 64·111·35건으로 잘못 잡혔고, markdown 추출로 바로잡았다.
