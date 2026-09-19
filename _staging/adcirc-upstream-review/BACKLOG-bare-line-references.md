# BACKLOG — ADCIRC bare line reference hygiene (117건 / 12노트)

> 등록 2026-09-20. **이번 snapshot update 범위 밖**(사용자 결정). 별도 semantic resolution task.

## 목적

파일명이 생략된 ADCIRC source line reference(예: `` (`:2271`) ``)가 새 baseline `e8b62a70` 에서도 **동일한 source location** 을 가리키는지 안전하게 재해석한다. 116건(파일명 명시 참조)과 달리 old→new mapping 을 기계적으로 확정할 수 없다 — 참조 대상 파일을 문맥에서 재구성해야 한다.

## 현황 (2026-09-20 실측, `rg '\`:L?\d+'`)

| 노트 | 건수 |
|---|---:|
| `models/ADCIRC/source-analysis/adcirc_asgs_operational_system.md` | 29 |
| `models/ADCIRC/source-analysis/adcirc-hotstart.md` | 26 |
| `models/ADCIRC/source-analysis/adcirc-3d-mode.md` | 16 |
| `models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md` | 15 |
| `models/ADCIRC/source-analysis/adcirc-swan-coupling.md` | 11 |
| 나머지 7개 노트 | 20 |
| **합계** | **117** |

## 각 참조에서 확인할 것

1. 해당 노트의 주변 문맥(절 제목·바로 앞 문장)
2. 직전에 명시된 source file / section context
3. 참조된 symbol 또는 인용 코드
4. old baseline `6037225` 에서의 실제 source file·줄 내용
5. new baseline `e8b62a70` 에서의 대응 위치(내용 동일성 포함)

파일을 하나로 확정할 수 없으면 **AMBIGUOUS** 로 남기고 자동 갱신하지 않는다.

## 참고 자료 (이미 준비됨)

- `_staging/adcirc-upstream-review/` — compare.json, patches/, NOTE_REFERENCES.csv, review-only-precheck.csv
- rollback 자산: `models/ADCIRC/raw/source_code/adcirc.old-6037225`(6037225 트리), `/opt/coastal-snapshots/adcirc-6037225.tar.zst`
- old↔new 줄 매핑은 두 트리를 직접 대조해 재생성 가능(패치 없이도 difflib 로 산출)

## 범위 밖

- 노트 본문의 기술 서술 재작성
- 파일명 명시 참조(이번 116건에서 처리 완료)
- 다른 모델의 bare reference
