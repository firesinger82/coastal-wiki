# SWAN recovery 노트 반영 2 — 2026-10-13

담당 노트 10개에 수정안과 차이 결론을 반영했다. 차이 표는 아래 담당 노트에서 센 135행이다. 행 배정은 문서 근거의 주제와 노트 제목을 기준으로 했다.

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

`last_source_check`는 `2026-10-13 (recovery 대조 반영)`이다. `verification_method`에는 `2026-10-13 recovery 대조 보고서 R1–R8 반영`을 덧붙였다. `citation_status`는 기존 값을 유지했다.

## 노트별 추가·수정 줄 범위

줄 번호는 반영 후 파일 기준이다. 상대 링크 변환도 줄 범위에 포함했다.

| 노트 | 추가·수정 줄 범위 (노트:줄) | 수정안 반영 | 차이 표 행 수 |
|---|---|---|---|
| [models/SWAN/manual-notes/swan-tech-ch2-governing-equations.md](../../../models/SWAN/manual-notes/swan-tech-ch2-governing-equations.md) | swan-tech-ch2-governing-equations.md:7–8; swan-tech-ch2-governing-equations.md:23; swan-tech-ch2-governing-equations.md:80; swan-tech-ch2-governing-equations.md:108–111; swan-tech-ch2-governing-equations.md:177; swan-tech-ch2-governing-equations.md:186; swan-tech-ch2-governing-equations.md:190–192; swan-tech-ch2-governing-equations.md:202–205; swan-tech-ch2-governing-equations.md:210–211; swan-tech-ch2-governing-equations.md:223–254 | R1 §4 TN-008; R1 §4 TN-018–023 | 15 |
| [models/SWAN/manual-notes/swan-action-balance.md](../../../models/SWAN/manual-notes/swan-action-balance.md) | swan-action-balance.md:10–11; swan-action-balance.md:62–64; swan-action-balance.md:112; swan-action-balance.md:121; swan-action-balance.md:125; swan-action-balance.md:131; swan-action-balance.md:134–135; swan-action-balance.md:237–249 | R2 §4 SS-741; R2 §4 SS-742; R2 §4 SS-743 | 3 |
| [models/SWAN/manual-notes/swan-tech-ch3-breaking-source.md](../../../models/SWAN/manual-notes/swan-tech-ch3-breaking-source.md) | swan-tech-ch3-breaking-source.md:7–8; swan-tech-ch3-breaking-source.md:21; swan-tech-ch3-breaking-source.md:27; swan-tech-ch3-breaking-source.md:55; swan-tech-ch3-breaking-source.md:66–69; swan-tech-ch3-breaking-source.md:72; swan-tech-ch3-breaking-source.md:76–78; swan-tech-ch3-breaking-source.md:89; swan-tech-ch3-breaking-source.md:94–107 | R2 §4 SS-719 | 2 |
| [models/SWAN/manual-notes/swan-tech-ch3-discretization.md](../../../models/SWAN/manual-notes/swan-tech-ch3-discretization.md) | swan-tech-ch3-discretization.md:7–8; swan-tech-ch3-discretization.md:22; swan-tech-ch3-discretization.md:71; swan-tech-ch3-discretization.md:77; swan-tech-ch3-discretization.md:101–108; swan-tech-ch3-discretization.md:111; swan-tech-ch3-discretization.md:139; swan-tech-ch3-discretization.md:144–174 | R1 §4 TN-055, TN-058–063 | 17 |
| [models/SWAN/manual-notes/swan-tech-ch3-refraction-limiter.md](../../../models/SWAN/manual-notes/swan-tech-ch3-refraction-limiter.md) | swan-tech-ch3-refraction-limiter.md:7–8; swan-tech-ch3-refraction-limiter.md:83; swan-tech-ch3-refraction-limiter.md:90–93; swan-tech-ch3-refraction-limiter.md:102; swan-tech-ch3-refraction-limiter.md:114; swan-tech-ch3-refraction-limiter.md:120–122; swan-tech-ch3-refraction-limiter.md:128; swan-tech-ch3-refraction-limiter.md:140–173 | R1 §4 TN-106, TC-003–005 | 21 |
| [models/SWAN/manual-notes/swan-tech-ch3-solution-iteration-limiter.md](../../../models/SWAN/manual-notes/swan-tech-ch3-solution-iteration-limiter.md) | swan-tech-ch3-solution-iteration-limiter.md:7–8; swan-tech-ch3-solution-iteration-limiter.md:21; swan-tech-ch3-solution-iteration-limiter.md:39; swan-tech-ch3-solution-iteration-limiter.md:42–43; swan-tech-ch3-solution-iteration-limiter.md:54–57; swan-tech-ch3-solution-iteration-limiter.md:64; swan-tech-ch3-solution-iteration-limiter.md:69; swan-tech-ch3-solution-iteration-limiter.md:72–77; swan-tech-ch3-solution-iteration-limiter.md:89–97; swan-tech-ch3-solution-iteration-limiter.md:102; swan-tech-ch3-solution-iteration-limiter.md:116; swan-tech-ch3-solution-iteration-limiter.md:120–135; swan-tech-ch3-solution-iteration-limiter.md:145; swan-tech-ch3-solution-iteration-limiter.md:165–167; swan-tech-ch3-solution-iteration-limiter.md:177–179; swan-tech-ch3-solution-iteration-limiter.md:183–235 | R1 §4 TN-070, TN-073; R1 §4 TN-074–082; R1 §4 TN-079–080; R2 §4 SS-718; R8 §6 N1-009; R8 §6 N1-010; R8 §6 N1-011; R8 §6 T1-002·T1-003·T1-010의 노트 대조 문단 | 39 |
| [models/SWAN/manual-notes/swan-tech-ch6-iterative-solvers.md](../../../models/SWAN/manual-notes/swan-tech-ch6-iterative-solvers.md) | swan-tech-ch6-iterative-solvers.md:7–8; swan-tech-ch6-iterative-solvers.md:20; swan-tech-ch6-iterative-solvers.md:29; swan-tech-ch6-iterative-solvers.md:39–40; swan-tech-ch6-iterative-solvers.md:53; swan-tech-ch6-iterative-solvers.md:59–63; swan-tech-ch6-iterative-solvers.md:72–89 | R1 §4 TN-170–175 | 7 |
| [models/SWAN/manual-notes/swan-tech-ch7-parallel.md](../../../models/SWAN/manual-notes/swan-tech-ch7-parallel.md) | swan-tech-ch7-parallel.md:7–8; swan-tech-ch7-parallel.md:21; swan-tech-ch7-parallel.md:28; swan-tech-ch7-parallel.md:46–48; swan-tech-ch7-parallel.md:80–81; swan-tech-ch7-parallel.md:93–110 | R1 §4 TN-176, TN-178, TN-185 | 6 |
| [models/SWAN/manual-notes/swan-tech-ch8-unstructured-grid-scheme.md](../../../models/SWAN/manual-notes/swan-tech-ch8-unstructured-grid-scheme.md) | swan-tech-ch8-unstructured-grid-scheme.md:7–8; swan-tech-ch8-unstructured-grid-scheme.md:22; swan-tech-ch8-unstructured-grid-scheme.md:51; swan-tech-ch8-unstructured-grid-scheme.md:98–101; swan-tech-ch8-unstructured-grid-scheme.md:104–107; swan-tech-ch8-unstructured-grid-scheme.md:112–114; swan-tech-ch8-unstructured-grid-scheme.md:118–120; swan-tech-ch8-unstructured-grid-scheme.md:124–153 | R1 §4 TN-190, TN-203–204; R8 §6 T1-014의 노트 대조 문단; R8 §6 식 (8.16) 유지 행 | 16 |
| [models/SWAN/manual-notes/swan-tech-ch8-unstructured-ops.md](../../../models/SWAN/manual-notes/swan-tech-ch8-unstructured-ops.md) | swan-tech-ch8-unstructured-ops.md:7–8; swan-tech-ch8-unstructured-ops.md:22; swan-tech-ch8-unstructured-ops.md:53–56; swan-tech-ch8-unstructured-ops.md:59; swan-tech-ch8-unstructured-ops.md:82–88; swan-tech-ch8-unstructured-ops.md:91–93; swan-tech-ch8-unstructured-ops.md:99–104; swan-tech-ch8-unstructured-ops.md:116–118; swan-tech-ch8-unstructured-ops.md:122–144 | R1 §4 TN-211, TN-218, TN-222–224 | 9 |

## 반영한 차이 행 ID (보고서별)

행 ID 목록은 담당 노트의 `문서와 코드 차이 (10-13 대조)` 표와 대응한다.

### R1

[확정 보고서](../compare/swan-theory-numerics-vs-code.md#5-차이-결론). 반영 행은 94개이다(위 담당 노트 차이 표의 R1 행 ID 집계).

- `R1:TN-001`, `R1:TN-003`, `R1:TN-004`, `R1:TN-005`, `R1:TN-006`, `R1:TN-008`, `R1:TN-017`, `R1:TN-021`, `R1:TN-023`, `R1:TN-026`, `R1:TN-027`, `R1:TN-028`, `R1:TN-031`, `R1:TN-034`, `R1:TC-001`.

- `R1:TN-044`, `R1:TN-045`, `R1:TN-055`, `R1:TN-056`, `R1:TN-057`, `R1:TN-058`, `R1:TN-059`, `R1:TN-063`, `R1:TN-066`, `R1:TC-018`, `R1:TC-019`, `R1:TC-020`, `R1:TC-021`, `R1:TC-022`, `R1:TC-023`.

- `R1:TC-025`, `R1:TN-068`, `R1:TN-070`, `R1:TN-073`, `R1:TN-074`, `R1:TN-075`, `R1:TN-076`, `R1:TN-077`, `R1:TN-078`, `R1:TN-080`, `R1:TN-081`, `R1:TN-082`, `R1:TN-085`, `R1:TN-087`, `R1:TN-088`.

- `R1:TN-089`, `R1:TC-007`, `R1:TC-024`, `R1:TN-094`, `R1:TN-095`, `R1:TN-096`, `R1:TN-098`, `R1:TN-099`, `R1:TN-100`, `R1:TN-101`, `R1:TN-102`, `R1:TN-104`, `R1:TN-106`, `R1:TN-107`, `R1:TN-108`.

- `R1:TN-112`, `R1:TC-002`, `R1:TC-003`, `R1:TC-004`, `R1:TC-005`, `R1:TC-006`, `R1:TN-171`, `R1:TN-172`, `R1:TN-173`, `R1:TN-174`, `R1:TN-175`, `R1:TN-176`, `R1:TN-178`, `R1:TN-183`, `R1:TN-185`.

- `R1:TN-186`, `R1:TN-187`, `R1:TN-188`, `R1:TN-190`, `R1:TN-191`, `R1:TN-194`, `R1:TN-201`, `R1:TN-203`, `R1:TN-204`, `R1:TC-016`, `R1:TN-211`, `R1:TN-218`, `R1:TN-220`, `R1:TN-222`, `R1:TN-223`.

- `R1:TN-224`, `R1:TC-008`, `R1:TC-014`, `R1:TC-015`.

### R2

[확정 보고서](../compare/swan-theory-sources-vs-code.md#5-차이-결론). 반영 행은 9개이다(위 담당 노트 차이 표의 R2 행 ID 집계).

- `R2:SS-361`, `R2:SS-362`, `R2:SS-363`, `R2:SS-718`, `R2:SS-511`, `R2:SS-719`, `R2:SS-741`, `R2:SS-742`, `R2:SS-743`.

### R3

[확정 보고서](../compare/swan-theory-obstacles-setup-qc-bc-vs-code.md#5-차이-결론). 반영 행은 0개이다(위 담당 노트 차이 표의 R3 행 ID 집계).

차이 표 반영 행은 없다. 해당 차이 행은 아래 다른 작업 담당 목록에 기록했다.

### R7

[확정 보고서](../compare/swan-implementation-history-vs-code.md#5-차이-결론). 반영 행은 16개이다(위 담당 노트 차이 표의 R7 행 ID 집계).

- `R7:H-139`, `R7:H-534`, `R7:H-949p`, `R7:H-1227`, `R7:H-1331`, `R7:H-1346`, `R7:H-1358`, `R7:H-213p`, `R7:H-219`, `R7:H-219p`, `R7:H-336p`, `R7:H-599`, `R7:H-695`, `R7:H-778`, `R7:H-789`.

- `R7:H-1228`.

### R8

[확정 보고서](../flow/SWAN-callflow.md#8-차이-결론). 반영 행은 16개이다(위 담당 노트 차이 표의 R8 행 ID 집계).

- `R8:T1-002`, `R8:T1-003`, `R8:T1-004`, `R8:T1-005`, `R8:T1-006`, `R8:T1-007`, `R8:T1-008`, `R8:T1-010`, `R8:T1-011`, `R8:T1-015`, `R8:N1-009`, `R8:N1-010`, `R8:N1-011`, `R8:T1-009`, `R8:T1-012`.

- `R8:T1-014`.

## 다른 작업 담당

아래 행은 담당 목록 밖의 노트가 문서 근거와 주제에 더 가깝다. 이 목록은 각 보고서 차이 결론의 행 ID에서 반영 행과 일치 행을 제외한 집합이다.

### R1

QC·곡선격자·복사응력·장애물·스펙트럼 적분·변환의 담당 노트이다. 대표 노트는 [swan-tech-ch3-qc-curvilinear](../../../models/SWAN/manual-notes/swan-tech-ch3-qc-curvilinear.md)와 [swan-tech-ch3-obstacles-spectral-ops](../../../models/SWAN/manual-notes/swan-tech-ch3-obstacles-spectral-ops.md)이다.

- `R1:TN-115`, `R1:TN-116`, `R1:TN-117`, `R1:TN-118`, `R1:TN-120`, `R1:TN-121`, `R1:TN-122`, `R1:TN-123`, `R1:TN-127`, `R1:TN-134`, `R1:TN-138`, `R1:TN-139`, `R1:TN-140`, `R1:TN-145`, `R1:TN-147`.

- `R1:TN-148`, `R1:TN-153`, `R1:TN-156`, `R1:TN-158`, `R1:TN-161`, `R1:TN-162`, `R1:TN-163`, `R1:TN-164`, `R1:TN-165`, `R1:TN-166`, `R1:TN-168`, `R1:TC-009`, `R1:TC-010`, `R1:TC-011`, `R1:TC-012`.

- `R1:TC-013`.

### R2

바람·백파·바닥 마찰·비선형 상호작용·식생·얼음·Bragg·GEN1/2·ST6·원천항 조립의 상세 노트가 담당한다. 대표 노트는 [swan-tech-ch2-sources-sinks](../../../models/SWAN/manual-notes/swan-tech-ch2-sources-sinks.md), [swan-tech-ch2-dissipation-detailed](../../../models/SWAN/manual-notes/swan-tech-ch2-dissipation-detailed.md), [swan-tech-ch2-nonlinear-detailed](../../../models/SWAN/manual-notes/swan-tech-ch2-nonlinear-detailed.md), [swan-tech-ch2-vegetation-ice-bragg-gen12](../../../models/SWAN/manual-notes/swan-tech-ch2-vegetation-ice-bragg-gen12.md)이다.

- `R2:SS-036`, `R2:SS-038`, `R2:SS-039`, `R2:SS-201`, `R2:SS-049`, `R2:SS-051`, `R2:SS-055`, `R2:SS-056`, `R2:SS-057`, `R2:SS-204`, `R2:SS-205`, `R2:SS-210`, `R2:SS-067`, `R2:SS-212`, `R2:SS-214`.

- `R2:SS-077`, `R2:SS-084`, `R2:SS-088`, `R2:SS-089`, `R2:SS-215`, `R2:SS-216`, `R2:SS-217`, `R2:SS-231`, `R2:SS-232`, `R2:SS-090`, `R2:SS-091`, `R2:SS-233`, `R2:SS-234`, `R2:SS-235`, `R2:SS-093`.

- `R2:SS-236`, `R2:SS-094`, `R2:SS-095`, `R2:SS-100`, `R2:SS-219`, `R2:SS-220`, `R2:SS-106`, `R2:SS-107`, `R2:SS-108`, `R2:SS-222`, `R2:SS-109`, `R2:SS-112`, `R2:SS-113`, `R2:SS-115`, `R2:SS-116`.

- `R2:SS-270`, `R2:SS-274`, `R2:SS-287`, `R2:SS-118`, `R2:SS-119`, `R2:SS-121`, `R2:SS-126`, `R2:SS-127`, `R2:SS-129`, `R2:SS-501`, `R2:SS-502`, `R2:SS-503`, `R2:SS-504`, `R2:SS-506`, `R2:SS-507`.

- `R2:SS-508`, `R2:SS-509`, `R2:SS-510`, `R2:SS-512`, `R2:SS-513`, `R2:SS-514`, `R2:SS-515`, `R2:SS-516`, `R2:SS-517`, `R2:SS-518`, `R2:SS-519`, `R2:SS-520`, `R2:SS-521`, `R2:SS-522`, `R2:SS-523`.

- `R2:SS-524`, `R2:SS-525`, `R2:SS-526`, `R2:SS-527`, `R2:SS-528`, `R2:SS-529`, `R2:SS-530`, `R2:SS-531`, `R2:SS-532`, `R2:SS-533`, `R2:SS-534`, `R2:SS-535`, `R2:SS-536`, `R2:SS-537`, `R2:SS-538`.

- `R2:SS-539`, `R2:SS-540`, `R2:SS-701`, `R2:SS-702`, `R2:SS-703`, `R2:SS-704`, `R2:SS-705`, `R2:SS-706`, `R2:SS-707`, `R2:SS-708`, `R2:SS-709`, `R2:SS-710`, `R2:SS-711`, `R2:SS-712`, `R2:SS-713`.

- `R2:SS-714`, `R2:SS-715`, `R2:SS-716`, `R2:SS-717`, `R2:SS-720`, `R2:SS-721`, `R2:SS-722`, `R2:SS-723`, `R2:SS-724`, `R2:SS-725`, `R2:SS-726`, `R2:SS-727`, `R2:SS-728`, `R2:SS-729`, `R2:SS-730`.

- `R2:SS-731`, `R2:SS-733`, `R2:SS-734`, `R2:SS-735`, `R2:SS-736`, `R2:SS-737`, `R2:SS-738`, `R2:SS-739`, `R2:SS-740`.

### R3

장애물·회절·set-up·경계·초기화·QC의 담당 노트이다. 대표 노트는 [swan-tech-ch2-obstacles-diffraction-setup](../../../models/SWAN/manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md), [swan-tech-ch4-5-bc-2d-setup](../../../models/SWAN/manual-notes/swan-tech-ch4-5-bc-2d-setup.md), [swan-tech-ch2-7-qcm-theory](../../../models/SWAN/manual-notes/swan-tech-ch2-7-qcm-theory.md)이다.

- `R3:OQ-003`, `R3:OQ-006`, `R3:OQ-009`, `R3:OQ-013`, `R3:OQ-014`, `R3:OQ-015`, `R3:OQ-017`, `R3:OQ-018`, `R3:OQ-019`, `R3:OQ-020`, `R3:OQ-022`, `R3:OQ-023`, `R3:OQ-024`, `R3:OQ-025`, `R3:OQ-027`.

- `R3:OQ-029`, `R3:OQ-030`, `R3:SU-001`, `R3:SU-002`, `R3:SU-003`, `R3:SU-004`, `R3:SU-005`, `R3:SU-006`, `R3:SU-007`, `R3:SU-008`, `R3:SU-009`, `R3:SU-010`, `R3:SU-011`, `R3:SU-012`, `R3:SU-013`.

- `R3:SU-014`, `R3:SU-015`, `R3:SU-016`, `R3:SU-019`, `R3:SU-020`, `R3:SU-021`, `R3:SU-024`, `R3:SU-026`, `R3:SU-027`, `R3:SU-028`, `R3:SU-029`, `R3:SU-030`, `R3:SU-031`, `R3:SU-032`, `R3:SU-033`.

- `R3:SU-035`, `R3:SU-037`, `R3:SU-038`, `R3:SU-041`, `R3:QC-001`, `R3:QC-002`, `R3:QC-003`, `R3:QC-004`, `R3:QC-005`, `R3:QC-006`, `R3:QC-007`, `R3:QC-008`, `R3:QC-009`, `R3:QC-010`, `R3:QC-011`.

- `R3:QC-012`, `R3:QC-013`, `R3:QC-014`, `R3:QC-015`, `R3:QC-016`, `R3:QC-017`, `R3:QC-018`, `R3:QC-019`, `R3:QC-020`, `R3:QC-022`, `R3:QC-023`, `R3:QC-024`, `R3:QC-025`, `R3:QC-026`, `R3:QC-027`.

- `R3:QC-028`, `R3:QC-029`, `R3:QC-030`, `R3:QC-031`, `R3:QC-032`, `R3:QC-033`, `R3:QC-034`, `R3:QC-035`, `R3:QC-036`, `R3:QC-037`, `R3:QC-038`, `R3:QC-039`, `R3:QC-040`, `R3:QC-041`, `R3:QC-042`.

- `R3:QC-044`, `R3:QC-045`, `R3:QC-046`, `R3:QC-047`, `R3:QC-048`, `R3:QC-049`, `R3:QC-050`, `R3:QC-051`, `R3:QC-052`, `R3:QC-053`, `R3:QC-054`, `R3:QC-055`, `R3:QC-056`, `R3:QC-057`, `R3:QC-058`.

- `R3:QC-059`, `R3:QC-060`, `R3:QC-061`, `R3:QC-063`, `R3:QC-064`, `R3:QC-065`, `R3:QC-066`, `R3:QC-067`, `R3:QC-068`, `R3:QC-069`, `R3:QC-073`, `R3:QC-074`, `R3:QC-075`, `R3:QC-076`, `R3:QC-078`.

- `R3:QC-079`, `R3:QC-080`, `R3:QC-081`, `R3:QC-082`, `R3:QC-083`, `R3:QC-086`, `R3:QC-087`, `R3:QC-089`, `R3:BC-005`, `R3:BC-006`, `R3:BC-007`, `R3:BC-011`, `R3:BC-013`, `R3:BC-014`, `R3:BC-015`.

- `R3:SU-042`, `R3:CP-001`, `R3:CP-002`, `R3:CP-003`, `R3:CP-004`, `R3:CP-005`, `R3:CP-006`, `R3:CP-007`, `R3:CP-008`, `R3:CP-010`, `R3:CP-011`, `R3:CP-012`, `R3:CP-013`, `R3:CP-014`, `R3:CP-015`.

- `R3:CP-016`, `R3:CP-017`, `R3:CP-018`, `R3:CP-019`, `R3:CP-020`, `R3:CP-021`, `R3:CP-023`, `R3:CP-024`, `R3:CP-025`, `R3:CP-026`, `R3:CP-028`, `R3:CP-029`, `R3:CP-030`, `R3:CP-031`, `R3:NT-001`.

- `R3:NT-002`, `R3:NT-003`, `R3:NT-004`, `R3:NT-005`, `R3:NT-006`, `R3:NT-007`, `R3:NT-008`, `R3:NT-009`, `R3:NT-010`, `R3:NT-011`, `R3:NT-012`, `R3:NT-013`, `R3:NT-014`, `R3:NT-015`, `R3:NT-016`.

- `R3:NT-017`, `R3:NT-018`, `R3:NT-019`, `R3:NT-020`, `R3:NT-021`, `R3:NT-022`, `R3:NT-023`, `R3:NT-024`, `R3:NT-025`, `R3:NT-026`, `R3:NT-027`, `R3:NT-028`, `R3:NT-029`, `R3:NT-030`, `R3:NT-031`.

- `R3:NT-032`, `R3:NT-033`, `R3:NT-034`, `R3:NT-035`, `R3:NT-036`, `R3:NT-037`, `R3:NT-038`, `R3:NT-039`, `R3:NT-040`, `R3:NT-041`, `R3:NT-042`, `R3:NT-043`, `R3:NT-044`, `R3:NT-045`, `R3:NT-046`.

- `R3:NT-047`, `R3:NT-049`, `R3:NT-052`.

### R4

사용자 매뉴얼의 실행·입력·명령·출력 시각·경계 규약을 다루는 담당 노트이다. 대표 노트는 [swan-usage-general](../../../models/SWAN/manual-notes/swan-usage-general.md)과 [swan-command-setup-grid-reference](../../../models/SWAN/manual-notes/swan-command-setup-grid-reference.md)이다.

- `R4:T1-001`, `R4:T1-003`, `R4:T1-004`, `R4:T1-005`, `R4:T1-006`, `R4:T1-007`, `R4:T1-009`, `R4:T1-011`, `R4:T1-012`, `R4:T1-013`, `R4:T1-014`, `R4:T1-015`, `R4:T1-018`, `R4:T1-020`, `R4:T1-024`.

- `R4:T1-037`, `R4:T1-038`, `R4:T1-039`, `R4:T1-050`, `R4:T1-054`, `R4:T1-055`, `R4:T1-058`, `R4:T1-060`, `R4:T1-061`, `R4:T1-062`, `R4:T1-066`, `R4:T1-084`, `R4:T1-085`, `R4:T1-088`, `R4:T1-089`.

- `R4:T1-095`, `R4:T1-096`, `R4:T1-097`, `R4:T1-136`, `R4:T1-137`, `R4:T1-144`, `R4:T1-147`, `R4:T1-174`, `R4:T1-175`, `R4:T1-176`, `R4:T1-182`, `R4:T1-185`, `R4:T1-187`, `R4:T1-191`, `R4:T1-192`.

- `R4:T1-194`, `R4:T1-220`, `R4:T1-221`, `R4:T1-222`, `R4:T1-223`, `R4:T1-224`, `R4:T1-225`, `R4:T1-226`, `R4:T1-227`, `R4:T1-228`, `R4:T1-229`, `R4:T1-230`, `R4:T1-231`, `R4:T1-232`, `R4:T1-233`.

- `R4:T1-234`, `R4:T1-235`, `R4:T1-236`, `R4:T1-237`, `R4:T1-238`, `R4:T1-239`, `R4:T1-240`, `R4:T1-241`, `R4:T1-250`, `R4:T1-251`, `R4:T1-252`, `R4:T1-253`, `R4:T1-254`, `R4:T1-300`, `R4:T1-301`.

- `R4:T1-302`, `R4:T1-303`, `R4:T1-304`, `R4:T1-305`, `R4:T1-306`, `R4:T1-307`, `R4:T1-308`, `R4:T1-309`, `R4:T1-310`, `R4:T1-311`, `R4:T1-312`, `R4:T1-313`.

### R5

물리·수치 명령, Appendix A 출력량 및 관련 소스 구현의 담당 노트이다. 대표 노트는 [swan-command-physics-reference](../../../models/SWAN/manual-notes/swan-command-physics-reference.md), [swan-command-numerics-output-reference](../../../models/SWAN/manual-notes/swan-command-numerics-output-reference.md), [swan-output-variable-definitions](../../../models/SWAN/manual-notes/swan-output-variable-definitions.md)이다.

- `R5:PN-003`, `R5:PN-008`, `R5:PN-011`, `R5:PN-012`, `R5:PN-014`, `R5:PN-015`, `R5:PN-016`, `R5:PN-018`, `R5:PN-021`, `R5:PN-024`, `R5:PN-025`, `R5:PN-032`, `R5:PN-038`, `R5:PN-041`, `R5:PN-042`.

- `R5:PN-045`, `R5:PN-046`, `R5:PN-048`, `R5:PN-051`, `R5:PN-052`, `R5:PN-053`, `R5:PN-058`, `R5:PN-059`, `R5:PN-060`, `R5:PN-061`, `R5:PN-064`, `R5:PN-065`, `R5:PN-066`, `R5:PN-068`, `R5:PN-070`.

- `R5:PN-072`, `R5:PN-074`, `R5:PN-075`, `R5:PN-078`, `R5:PN-192`, `R5:PN-081`, `R5:PN-082`, `R5:PN-083`, `R5:PN-084`, `R5:PN-085`, `R5:PN-087`, `R5:PN-090`, `R5:PN-092`, `R5:PN-093`, `R5:PN-095`.

- `R5:PN-098`, `R5:PN-099`, `R5:PN-101`, `R5:PN-102`, `R5:PN-104`, `R5:PN-106`, `R5:PN-110`, `R5:PN-116`, `R5:PN-118`, `R5:PN-120`, `R5:PN-121`, `R5:PN-123`, `R5:PN-125`, `R5:PN-126`, `R5:PN-127`.

- `R5:PN-128`, `R5:PN-129`, `R5:PN-131`, `R5:PN-134`, `R5:PN-137`, `R5:PN-142`, `R5:PN-143`, `R5:PN-144`, `R5:PN-145`, `R5:PN-146`, `R5:PN-147`, `R5:PN-148`, `R5:PN-149`, `R5:PN-150`, `R5:PN-151`.

- `R5:PN-152`, `R5:PN-153`, `R5:PN-154`, `R5:PN-155`, `R5:PN-156`, `R5:PN-157`, `R5:PN-158`, `R5:PN-159`, `R5:PN-160`, `R5:PN-161`, `R5:PN-162`, `R5:PN-163`, `R5:PN-164`, `R5:PN-165`, `R5:PN-166`.

- `R5:PN-167`, `R5:PN-168`, `R5:PN-169`, `R5:PN-170`, `R5:PN-171`, `R5:PN-172`, `R5:PN-173`, `R5:PN-174`, `R5:PN-175`, `R5:PN-189`, `R5:PN-190`, `R5:PN-191`, `R5:PN-176`, `R5:PN-177`, `R5:PN-178`.

- `R5:PN-179`, `R5:PN-180`, `R5:PN-181`, `R5:PN-182`, `R5:PN-183`, `R5:PN-184`, `R5:PN-185`, `R5:PN-186`, `R5:PN-187`, `R5:PN-188`.

### R6

출력 명령·출력량·스펙트럼 파일·출력 구현의 담당 노트이다. 대표 노트는 [swan-command-numerics-output-reference](../../../models/SWAN/manual-notes/swan-command-numerics-output-reference.md), [swan-output-variable-definitions](../../../models/SWAN/manual-notes/swan-output-variable-definitions.md), [swan-spectral-file-format](../../../models/SWAN/manual-notes/swan-spectral-file-format.md)이다.

- `R6:O-002`, `R6:O-010`, `R6:O-011`, `R6:O-012`, `R6:O-014`, `R6:O-015`, `R6:O-017`, `R6:O-018`, `R6:O-020`, `R6:O-022`, `R6:O-024`, `R6:O-025`, `R6:O-028`, `R6:O-029`, `R6:O-031`.

- `R6:O-032`, `R6:O-033`, `R6:O-034`, `R6:O-036`, `R6:O-045`, `R6:O-046`, `R6:O-049`, `R6:O-050`, `R6:O-051`, `R6:O-052`, `R6:O-055`, `R6:O-056`, `R6:O-058`, `R6:O-059`, `R6:O-061`.

- `R6:O-063`, `R6:O-067`, `R6:O-073`, `R6:O-074`, `R6:O-075`, `R6:O-076`, `R6:O-077`, `R6:O-085`, `R6:O-086`, `R6:O-090`, `R6:O-091`, `R6:O-093`, `R6:O-097`, `R6:O-098`, `R6:O-099`.

- `R6:O-104`, `R6:O-105`, `R6:O-106`, `R6:O-107`, `R6:O-108`, `R6:O-110`, `R6:O-111`, `R6:O-112`, `R6:O-113`, `R6:O-114`, `R6:O-116`, `R6:O-118`, `R6:O-119`, `R6:O-120`, `R6:O-121`.

- `R6:O-122`, `R6:O-123`, `R6:O-124`, `R6:O-125`, `R6:O-126`, `R6:O-127`, `R6:O-128`, `R6:O-129`, `R6:O-130`, `R6:O-131`, `R6:O-132`, `R6:O-133`, `R6:O-134`, `R6:O-135`, `R6:O-136`.

- `R6:O-137`, `R6:O-138`, `R6:O-139`, `R6:O-140`, `R6:N-001`, `R6:N-002`, `R6:N-003`, `R6:N-004`, `R6:N-005`, `R6:N-006`, `R6:N-007`, `R6:N-008`, `R6:N-009`, `R6:N-010`, `R6:N-011`.

- `R6:N-012`, `R6:N-013`, `R6:N-014`, `R6:N-015`, `R6:N-016`, `R6:N-017`, `R6:N-018`, `R6:N-019`, `R6:N-020`, `R6:N-021`, `R6:N-022`.

### R7

설치·빌드·실행·프로그래밍 규칙·물리 설정·출력 이력 및 해당 노트 수정안의 담당이다. 대표 노트는 [swan-implementation-manual](../../../models/SWAN/manual-notes/swan-implementation-manual.md), [swan-programming-rules](../../../models/SWAN/manual-notes/swan-programming-rules.md), [swan-parallel-implementation](../../../models/SWAN/source-analysis/swan-parallel-implementation.md)이다. R7:S-019의 수렴 설정 권고는 NUMERIC 명령 노트가 담당한다.

- `R7:I-003`, `R7:I-008`, `R7:I-013`, `R7:I-015`, `R7:I-016`, `R7:I-022`, `R7:I-024`, `R7:I-025`, `R7:I-029`, `R7:I-030`, `R7:I-032`, `R7:I-033`, `R7:I-043`, `R7:I-045`, `R7:I-048`.

- `R7:I-049`, `R7:I-052`, `R7:I-053`, `R7:I-056`, `R7:I-057`, `R7:I-058`, `R7:I-059`, `R7:R-003`, `R7:R-006`, `R7:R-007`, `R7:R-010`, `R7:P-001`, `R7:P-002`, `R7:P-003`, `R7:P-006`.

- `R7:P-007`, `R7:P-008`, `R7:P-009`, `R7:P-010`, `R7:P-011`, `R7:P-012`, `R7:P-013`, `R7:P-014`, `R7:P-015`, `R7:P-016`, `R7:P-017`, `R7:P-018`, `R7:P-019`, `R7:P-021`, `R7:P-023`.

- `R7:P-024`, `R7:P-025`, `R7:P-026`, `R7:P-027`, `R7:P-028`, `R7:P-029`, `R7:P-030`, `R7:P-031`, `R7:P-033`, `R7:P-034`, `R7:P-035`, `R7:P-036`, `R7:P-037`, `R7:P-039`, `R7:P-040`.

- `R7:P-041`, `R7:P-042`, `R7:P-043`, `R7:P-044`, `R7:P-045`, `R7:P-046`, `R7:P-047`, `R7:P-048`, `R7:P-049`, `R7:P-050`, `R7:P-051`, `R7:P-052`, `R7:P-053`, `R7:P-054`, `R7:P-055`.

- `R7:Q-002`, `R7:Q-005`, `R7:Q-007`, `R7:Q-008`, `R7:Q-018`, `R7:ED-040`, `R7:ED-043`, `R7:ED-044`, `R7:ED-045`, `R7:ED-046`, `R7:ED-051`, `R7:ED-052`, `R7:H-47p`, `R7:H-112`, `R7:H-131`.

- `R7:H-133p`, `R7:H-170p`, `R7:H-195`, `R7:H-202`, `R7:H-228p`, `R7:H-291`, `R7:H-306`, `R7:H-326`, `R7:H-333`, `R7:H-374p`, `R7:H-472`, `R7:H-480p`, `R7:H-492`, `R7:H-501`, `R7:H-529`.

- `R7:H-531`, `R7:H-532`, `R7:H-538`, `R7:H-566`, `R7:H-583`, `R7:H-587`, `R7:H-589`, `R7:H-591`, `R7:H-601`, `R7:H-686`, `R7:H-749`, `R7:H-755`, `R7:H-813`, `R7:H-837`, `R7:H-840`.

- `R7:H-846`, `R7:H-849`, `R7:H-852`, `R7:H-855`, `R7:H-858`, `R7:H-861`, `R7:H-864`, `R7:H-867`, `R7:H-870`, `R7:H-873`, `R7:H-890`, `R7:H-894`, `R7:H-903`, `R7:H-910`, `R7:H-913`.

- `R7:H-921`, `R7:H-936`, `R7:H-940`, `R7:H-944`, `R7:H-945`, `R7:H-955`, `R7:H-959`, `R7:H-961`, `R7:H-966`, `R7:H-968`, `R7:H-979`, `R7:H-1006`, `R7:H-1056`, `R7:H-1081`, `R7:H-1088`.

- `R7:H-1097`, `R7:H-1121`, `R7:H-1123`, `R7:H-1124`, `R7:H-1128`, `R7:H-1134`, `R7:H-1149`, `R7:H-1150`, `R7:H-1151`, `R7:H-1170`, `R7:H-1174`, `R7:H-1180`, `R7:H-1182`, `R7:H-1183`, `R7:H-1197`.

- `R7:H-1204`, `R7:H-1205`, `R7:H-1208`, `R7:H-1212`, `R7:H-1214`, `R7:H-1215`, `R7:H-1229`, `R7:H-1234`, `R7:H-1240`, `R7:H-1242`, `R7:H-1162e`, `R7:H-1257`, `R7:H-1263`, `R7:H-1268`, `R7:H-1273`.

- `R7:H-1274`, `R7:H-1275`, `R7:H-1305`, `R7:H-1319`, `R7:H-1336`, `R7:H-1337`, `R7:H-1350`, `R7:H-1354`, `R7:H-1360`, `R7:H-1371`, `R7:H-1373`, `R7:H-1375`, `R7:H-1386`, `R7:H-1388`, `R7:H-1389`.

- `R7:H-1390`, `R7:H-1397`, `R7:H-1398`, `R7:H-1399`, `R7:H-1418`, `R7:H-1419`, `R7:H-1447`, `R7:H-1455`, `R7:H-1464`, `R7:H-1480`, `R7:H-1482`, `R7:H-1504`, `R7:H-1514`, `R7:H-1531`, `R7:H-1547`.

- `R7:H-1596`, `R7:H-1603`, `R7:H-1611`, `R7:H-1620`, `R7:H-1638`, `R7:F-010`, `R7:D-002`, `R7:D-003`, `R7:D-005`, `R7:D-007`, `R7:D-008`, `R7:D-009`, `R7:D-010`, `R7:D-011`, `R7:D-012`.

- `R7:S-001`, `R7:S-002`, `R7:S-003`, `R7:S-006`, `R7:S-012`, `R7:S-016`, `R7:S-018`, `R7:S-019`, `R7:S-056`, `R7:C-001`, `R7:C-002`, `R7:C-003`, `R7:C-004`, `R7:C-005`, `R7:C-006`.

- `R7:C-007`, `R7:C-008`, `R7:C-009`, `R7:C-010`, `R7:C-011`, `R7:C-012`, `R7:C-013`, `R7:C-014`, `R7:C-015`, `R7:C-016`, `R7:C-017`, `R7:C-019`, `R7:C-020`, `R7:C-021`, `R7:C-023`.

- `R7:C-024`, `R7:C-025`, `R7:C-026`, `R7:C-028`, `R7:N-001`, `R7:N-002`, `R7:N-003`, `R7:N-005`, `R7:N-006`, `R7:N-007`, `R7:N-008`, `R7:N-009`, `R7:N-010`, `R7:N-011`, `R7:N-012`.

- `R7:N-013`, `R7:N-014`, `R7:N-015`, `R7:N-016`, `R7:N-017`, `R7:N-018`, `R7:N-019`, `R7:N-020`, `R7:N-021`, `R7:N-022`, `R7:N-023`, `R7:N-024`, `R7:N-025`, `R7:N-026`, `R7:N-027`.

- `R7:N-028`, `R7:N-029`, `R7:N-030`, `R7:N-031`, `R7:N-033`, `R7:N-035`.

### R8

COMPUTE·NUMERIC 명령 설명, 배열 수명·저장 구조, 시간 단계·비정렬 소스 구현 및 출력 분기의 담당이다. 대표 노트는 [swan-command-numerics-output-reference](../../../models/SWAN/manual-notes/swan-command-numerics-output-reference.md), [swan-data-structures-implementation](../../../models/SWAN/source-analysis/swan-data-structures-implementation.md), [swan-unstructured-time-step](../../../models/SWAN/source-analysis/swan-unstructured-time-step.md)이다. R8:T1-013은 swanuse의 시간 간격·반복 권고이므로 명령 노트가 담당한다.

- `R8:T1-001`, `R8:T1-013`, `R8:N1-001`, `R8:N1-002`, `R8:N1-003`, `R8:N1-004`, `R8:N1-005`, `R8:N1-006`, `R8:N1-007`, `R8:N1-008`, `R8:N1-012`, `R8:N1-013`, `R8:N1-014`.

## 일치 행 처리

일치 행은 차이 표에서 제외했다. 아래 목록은 입력 보고서 차이 결론 절에 남아 있는 일치 행이다.

- `R1:TN-150`, `R1:TC-017`.

- `R2:SS-202`, `R2:SS-364`, `R2:SS-505`.

- `R3:CP-009`, `R3:CP-022`, `R3:CP-027`.

- `R5:PN-132`.

- `R7:I-009`, `R7:I-010`, `R7:I-011`, `R7:I-012`, `R7:I-026`, `R7:I-028`, `R7:P-020`, `R7:C-018`, `R7:C-022`, `R7:C-027`.

R2:SS-364의 흐름 관련 권고·입력 금지 구분은 solution 노트 본문에 반영했다. R8 §6의 식 (8.16) 유지 행은 unstructured-grid-scheme 노트의 식을 그대로 유지했다.

## 담당 범위인데 넣지 않은 행과 이유

없음.

## 반영 확인

각 차이 행 ID는 담당 노트 하나에 배정했다. 차이 표의 일치 행은 없다. 모든 담당 노트의 frontmatter와 상대 링크 형식을 확인했다. 식 (8.16)은 수정 전 원문과 같다.

### R6

[확정 보고서](../compare/swan-outputs-vs-code.md#5-차이-결론). 반영 행은 0개이다(위 담당 노트 차이 표의 R6 행 ID 집계).

차이 표 반영 행은 없다. 해당 차이 행은 아래 다른 작업 담당 목록에 기록했다.

### R5

[확정 보고서](../compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론). 반영 행은 0개이다(위 담당 노트 차이 표의 R5 행 ID 집계).

차이 표 반영 행은 없다. 해당 차이 행은 아래 다른 작업 담당 목록에 기록했다.

### R4

[확정 보고서](../compare/swan-inputs-setup-vs-code.md#5-차이-결론). 반영 행은 0개이다(위 담당 노트 차이 표의 R4 행 ID 집계).

차이 표 반영 행은 없다. 해당 차이 행은 아래 다른 작업 담당 목록에 기록했다.
