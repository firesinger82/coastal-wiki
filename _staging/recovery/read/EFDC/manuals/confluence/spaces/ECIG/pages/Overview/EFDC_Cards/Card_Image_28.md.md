---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_28.md
lines: 51
sha256: b142b5b293ccc9e3c127c23a3133ea201a0a081e59cc2d3db9d2471a0a1bda18
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_28.md — 판독 구간 기록

구간은 1행부터 51행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | C28 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 제트·플룸(jet/plume) 해법 및 출력 제어 제목을 제시한다(10). 빈 줄과 주석 표식도 포함한다(11–13). 원문: ` C28 JET/PLUME SOLUTION CONTROL AND OUTPUT CONTROL PARAMETERS ` (10). |
| 14–29 | 해법 제어 — 식별자, 제트·플룸 길이 방향 요소(element)의 최대 수, 최대 반복 수를 정의한다(14–18). 연행(entrainment)은 전단(shear)과 강제 연행(forced entrainment)의 최댓값 또는 합을 사용한다(20–22). 정지 조건은 지정 요소 수, 중심선(centerline)의 저면·수면 관통, 경계의 저면·수면 관통을 구분한다(24–28). 원문: ` \* ID: ID COUNTER FOR JET/PLUME ` (14); ` \* NJEL: MAXIMUM NUMBER OF ELEMENTS ALONG JET/PLUME LENGTH ` (16); ` \* NJPMX: MAXIMUM NUMBER OF ITERATIONS ` (18); ` \* ISENT: 0 USE MAXIMUM OF SHEAR AND FORCED ENTRAINMENT ` (20); ` \*           1 USE SUM OF SHEAR AND FORCED ENTRAINMENT ` (22); ` \* ISTJP: 0 STOP AT SPECIFIED NUMBER OF ELEMENTS ` (24); ` \*            1 STOP WHEN CENTERLINE PENETRATES BOTTOM OR SURFACE ` (26); ` \*            2 STOP WITH BOUNDARY PENETRATES BOTTOM OR SURFACE ` (28). |
| 30–47 | 갱신·출력·취수 위치 — 시간 단계 수로 지정하는 갱신 빈도와 ASCII·이진(binary) 출력 옵션, 수직 출력 지점 수, 진단 파일을 제시한다(30–38). ICAL=2일 때 상류 취수 셀의 I·J·K 인덱스를 사용한다고 적는다(40–44). 원문: ` \* NUDJP: FREQUENCY FOR UPDATING JET/PLUME (NUMBER OF TIME STEPS) ` (30); ` \* IOJP: 1 FOR FULL ASCII, 2 FOR COMPACT ASCII OUTPUT AT EACH UPDATE ` (32); ` \*          3 FOR FULL AND COMPACT ASCII OUTPUT, 4 FOR BINARY OUTPUT ` (34); ` \* IPJP: NUMBER OF SPATIAL PRINT/SAVE POINT IN VERTICAL ` (36); ` \* ISDJP: 1 WRITE DIAGNOSTICS TO JPLOG\_\_.OUT ` (38); ` \* IUPJP: I INDEX OF UPSTREAM WITHDRAWAL CELL IF ICAL=2 ` (40); ` \* JUPJP: J INDEX OF UPSTREAM WITHDRAWAL CELL IF ICAL=2 ` (42); ` \* KUPJP: K INDEX OF UPSTREAM WITHDRAWAL CELL IF ICAL=2 ` (44). |
| 48–51 | C28 입력 예시 — Markdown의 빈 표 머리글과 구분선(48–49), 열 이름(50), Jet/Plume 주석이 붙은 입력 값(51)을 제시한다. 원문: ` \| C28 \| ID \| NJEL \| NJPMX \| ISENT \| ISTJP \| NUDJP \| IOJP \| IPJP \| ISDJP \| IUPJP \| JUPJP \| KUPJP \| ! ID \| ` (50); ` \|  \| 1 \| 10 \| 150 \| 0 \| 0 \| 40 \| 0 \| 1 \| 1 \| 0 \| 0 \| 0 \| ! Jet/Plume \| ` (51). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 32–34·50–51행: `IOJP` 설명은 옵션 1·2·3·4를 제시한다. 입력 예시의 `IOJP` 값은 `0`이며 이 파일은 옵션 0의 뜻을 적지 않는다.
