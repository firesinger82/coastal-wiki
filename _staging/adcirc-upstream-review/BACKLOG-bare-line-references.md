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

## 진행 기록 (2026-09-20)

snapshot migration 범위에서 **줄 이동 58건만** 갱신했다(9개 노트). 나머지는 그대로 둔다.

| 구분 | 건수 | 처리 |
|---|---:|---|
| 줄 이동 발생 (adcirc repo, 이번 변경 파일) | 58 | **갱신 완료** — old/new 줄 내용 동일성 확인 후 번호만 수정 |
| 대응 위치 동일 (adcirc 무이동 + asgs 등 미교체 repo) | 59 | 미수정 |
| AMBIGUOUS | 1 | 미수정 |

### 남은 과제 1 — bare reference 정규화 (117건)

`` (`:2271`) `` 형태를 file-qualified 형태로 바꾸는 작업. **문서 품질 개선(reference hygiene)** 이며 snapshot migration 과 분리한다. RESOLVED_CONTEXTUAL 99건은 문맥으로 파일을 특정한 것이라, 파일명을 본문에 박아 넣는 것은 더 강한 변경이다 — 별도 검토·승인 필요. 해석 결과는 `bare-reference-resolution.csv`(status·evidence·confidence 포함).

### 남은 과제 2 — AMBIGUOUS 1건

`models/ADCIRC/source-analysis/adcirc-hotstart.md` 의 `` `:2936-2970` ``.
- 문맥 후보 파일: `wind.F` (노트 155행에서 마지막 명시)
- 동명 파일 2곳: `adcirc:src/wind.F`, `asgs:output/wind.F`
- 현재 문맥만으로 고유 특정 불가 → 이번 migration 에서 선택하지 않음. hotstart 절의 인용 내용과 두 파일의 해당 구간을 사람이 대조해야 확정 가능.
