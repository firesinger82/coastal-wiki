# UNRESOLVED 234 전수 분류 (2026-09-22)

resolver 가 `UNRESOLVED` 로 남긴 참조를 전수 조사했다. 결론부터 —
**대부분은 결함이 아니다.** "해소되지 않았다" 와 "인용이 틀렸다" 는 다른 말이다.

## 분류 결과

파서 anomaly(저자 이니셜 6건 등 12건)를 제외한 **222건**:

| 분류 | 건수 | 성격 | 조치 |
|---|---:|---|---|
| `ABSENT_FROM_SNAPSHOT` | **114** | 스냅샷에 없는 소스 파일 | 개별 확인 — 아래 참조 |
| `WIKI_PATH` | 43 | 위키 내부 경로(`_staging/…/evidence.json`, `textbook/sources.yml`) | 소스 참조가 아니다. 파서 범위 문제 |
| `RUNTIME_OR_INPUT` | 37 | 실행 입력·설정(`params.txt`·`tide.txt`·`i4dvar.in`·`partmesh.txt`) | 소스 트리에 없는 게 정상 |
| `OUTSIDE_SOURCE_CODE` | 17 | `raw/` 안에 있으나 `raw/source_code/` 밖(예제·매뉴얼 첨부) | 색인 범위 밖. 파일은 실재 |
| `GLOB_PATTERN` | 11 | 와일드카드(`CUDA 8 *_gpu.F`) | 파일 인용이 아니다 |

## `ABSENT_FROM_SNAPSHOT` 114건도 상당수가 의도적이다

표본 확인에서 두 유형이 드러났다.

**① 미병합 PR 파일 — 인용이 의도적이다.**
`models/ADCIRC/source-analysis/adcirc-dg-continuity-solver.md` 는 `dg.F90`·`slopelimiter.F90`·
`dg_integration.F90` 을 인용하는데, 이 노트는 **PR #502(미병합 WIP)** 를 GitHub API 로 읽어 쓴 것이다.
노트 스스로 "상태 경고 (WIP): PR 자체 checklist 모두 unchecked" 라 적고 있다.
그 파일들이 우리 pinned 스냅샷에 없는 것은 **정상**이며, 인용은 PR 을 가리킨다.

**② 부재 자체를 기술한 인용.**
`roms_4dvar.md` 는 `multiscale_driver.h`·`multiscale_sum_B.h` 를 "**부재**" 로 명시한다
(§I 재검증 2026-09-20). 없는 파일을 가리키는 것이 그 문장의 요지다.

따라서 114건을 일괄 "stale 인용" 으로 처리하면 안 된다. 필요한 것은
**인용이 스냅샷 밖을 의도적으로 가리키는지** 를 노트별로 가르는 일이다.

## 이번에 고친 것 — 파서: 저자 이니셜

`E.F`·`A.F` 6건은 논문 저자 이니셜이었다.

```
Fairall, C.W., E.F. Bradley, D.P. Rogers, J.B. Edson, G.S. Young (1996)
                ^^^^ 파서가 `E.F` 를 file 참조로 잡았다
```

`refparser._anomaly` 에 `BIBLIOGRAPHIC_INITIALS` 추가 — **단일 대문자 stem + 단일 대문자 확장자**
조합만 억제한다.

**두 번의 위험한 안을 기각했다.**

| 기각안 | 왜 |
|---|---|
| "짧은 stem 은 참조가 아니다" | `io.F`·`bc.F`·`gp.c`·`df.c`·`oc.c` 등 **실참조 19건**이 죽는다(ROMS 실측, failure mode 30) |
| "서지 줄 전체를 억제한다" | 그 줄들에 `lisflood.cpp`·`lmd_vmix.F`·`swancom2.ftn` 등 **실참조 11건**이 함께 있었다 |

채택안의 안전성은 실측으로 확인했다 — `^[A-Z]\.[A-Z]$` 형태의 실파일은 `models/*/raw` 전체에 **0건**이고,
위키에서 그 형태가 서지 줄 밖에 쓰인 사례도 0건이다.
게이트 fixture 2종(이니셜 탐지) + 규칙검사 1종(짧은 stem 실참조가 살아 있는지) 추가.

## 남은 일

1. `ABSENT_FROM_SNAPSHOT` 114 — 노트별로 "의도적 스냅샷 밖 인용" 과 "실제 stale" 을 가른다.
   전자는 DESIGN 의 `AHEAD_OF_SNAPSHOT` 계열 상태로 기록해 매 집계에서 빠지게 하는 편이 낫다.
2. `WIKI_PATH` 43 · `GLOB_PATTERN` 11 — 파서가 소스 참조로 잡지 않도록 범위를 좁힌다.
   둘 다 모양이 뚜렷해 안전하게 처리 가능하나, 위 두 기각 사례를 고려해 **안전성 실측 후** 반영한다.
3. `RUNTIME_OR_INPUT` 37 · `OUTSIDE_SOURCE_CODE` 17 — 조치 불요. 분류 기록으로 충분하다.

`triage.csv` 에 222건 전건의 분류를 남겼다.
