# LISFLOOD-FP 노트 추가·수정 줄 전수 대조 6

작업일: 2026-10-21.

## 대상과 집계 방법

- 대상은 `models/LISFLOOD-FP/source-analysis/lisflood-fp-channel-sgc.md`와 `models/LISFLOOD-FP/web-refs/lisflood-fp-official-resources.md`다.
- 검증 시작 시 `git diff -U0 HEAD -- <노트>`의 추가 줄을 고정하여 대조한다.
- 새 파일이면 전체 줄을 대조한다.
- 빈 줄, frontmatter, 제목, 표 구분선도 대조 줄 수에 포함한다.
- 정정 수와 보완 수는 검증에서 바꾼 원래 줄 수로 센다.
- 같은 줄에서 의미 정정과 인용 보완을 함께 하면 정정으로 한 번 센다.

검증 시작 시 두 노트 모두 기존 파일이었다.
아래 줄 번호는 검증 시작 시 노트의 줄 번호다.

| 노트 | 대상 줄 수 | 대상 줄 범위 |
|---|---:|---|
| `source-analysis/lisflood-fp-channel-sgc.md` | 155 | 7–8, 12, 21, 35–36, 55, 68, 74–75, 94–95, 114, 127–129, 137, 162–165, 170, 179–180, 185, 193–196, 218–343 |
| `web-refs/lisflood-fp-official-resources.md` | 59 | 2, 7–8, 12–13, 24–27, 36–54, 59–82, 84, 86–91 |

줄 수의 출처는 검증 시작 시 각 노트의 `git diff -U0 HEAD` 추가 줄이다.

## 진행 상태

- `source-analysis/lisflood-fp-channel-sgc.md`: 완료. 대상 155줄을 대조했다. 정정 5줄이다. 인용 보완 2줄이다.
- `web-refs/lisflood-fp-official-resources.md`: 완료. 대상 59줄을 대조했다. 정정 4줄이다. 보완은 없다.

## 기계 확인 후보 판정

- 사용자 지정 후보 없음.

## 1. 하도·SGC 노트 대조 완료

대상 노트: `models/LISFLOOD-FP/source-analysis/lisflood-fp-channel-sgc.md`.
대조한 줄은 위 범위표의 155줄 전부다.
이 중 차이 표는 232–343줄의 112행이다.
나머지 43줄에는 frontmatter, 본문, 빈 줄, 표 제목과 구분선이 포함된다.
정정은 5줄이다.
보완은 2줄이다.
줄을 삽입하거나 삭제하지 않았으므로 아래 줄 번호는 정정 후에도 같다.

차이 표의 분류와 결론은 `LISFLOOD-FP-final-conclusions.tsv` 및 각 행의 `conclusion-verify`와 대조했다.
최우선 `conclusion-claude-final`의 조정 행도 확인했다.
본문은 배정표의 보고서 §4 수정안과 `LISFLOOD-FP-callflow.md` §6의 해당 노트 항목을 대조했다.
코드 인용은 현재 원자료와 명시된 v8.0·v8.1·v8.2 배포본에서 열었다.
반영 전 노트 인용은 `git show bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-channel-sgc.md`의 해당 줄을 대조했다.
현재 코드와 구판의 차이를 판정할 때 배포판 8.3과 내부 숫자 판 8.1.0을 구분했다.

문서의 식·숫자·표는 지정된 쪽 이미지로 대조했다.
PDF는 p.1–2, 5, 10, 12, 15–25, 27–30, 32–34, 40–42를 열었다.
일반 DOCX는 변환본 p.5, 19–27, 29, 32–34, 38–39, 45를 열었다.
교량 DOCX는 변환본 p.1, 21–24, 29–30, 32, 35, 41, 47을 열었다.
DOCX p.5의 변경 추적은 쪽별 판독 기록 `LISFLOOD-FP user manual.docx/p001-018.md`의 p.5와도 대조했다.

### 정정·보완 목록

아래 노트 줄 번호의 기준 파일은 `models/LISFLOOD-FP/source-analysis/lisflood-fp-channel-sgc.md`다.
코드 경로의 기준은 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/`다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `lisflood-fp-channel-sgc.md:162` | 보완 | 공극률 네 방식의 인용 `input.cpp:1007–1055,1065–1076` → `1085–1146`도 추가했다. | `input.cpp:1095`는 PBOUND 면적 배열을 읽는다. `1102–1106`은 네 방향 경계 배열을 읽는다. `1138–1143`은 PBVAR 높이층별 경계 배열을 읽는다. 최종 LI2-307·308과 같다. |
| `lisflood-fp-channel-sgc.md:193` | 보완 | DEM을 z0·z1에 복사한다는 문장에 `lisflood_processing.cpp:53–68`만 인용 → `sgm_fast.cpp:606–607`을 추가했다. | `lisflood2/lisflood_processing.cpp:53–68`은 DEM을 `sg_cell_dem`에 저장한다. `lisflood2/sgm_fast.cpp:606–607`은 `z0 = weirs->cell_pair.sg_cell_dem[weir_pair_id0];`와 z1 대입을 실행한다. 최종 LB1-151·395와 같다. |
| `lisflood-fp-channel-sgc.md:195` | 정정 | 계수 입력 인용 `input.cpp:175–187` → `161–163`으로 고쳤다. 전형값 문장에 `user manual.pdf p.29`를 덧붙였다. | `input.cpp:161–162`의 `sscanf`가 `Weir_Cd`, `Weir_hc`, `Weir_m`, `Weir_w`를 읽는다. `175–187`은 W 방향 배치다. PDF p.29는 계수 1.4와 modular limit 0.9를 전형값으로 적는다. |
| `lisflood-fp-channel-sgc.md:222` | 정정 | “DOCX 판 이력 맨 위 5.9” → 기존 머리글 5.9.6과 5.9 위에 삽입된 8.0(2020-07-20)을 구분했다. `VersionHistory.h:21–23`의 숫자 판 인용 → `16–18`로 고쳤다. 8.3 DOI 귀속 → README가 밝힌 8.2 DOI와 8.3 변경 적용 관계로 고쳤다. | DOCX p.5 이미지에는 밑줄 `8.0`, `Jul 20 2020` 행이 있다. 최종 LV1-001은 기존 본문과 삽입 이력을 구분한다. `VersionHistory.h:16–18`은 8·1·0이다. `23`은 `LF_Release "8.3"`이다. 8.3 패키지 `README.md:19–24`의 DOI는 8.2의 `13121102`이다. 최종 LB1-408은 이 README를 8.3 DOI `13121119`의 근거로 쓰지 않도록 정정한다. |
| `lisflood-fp-channel-sgc.md:257` | 정정 | LB1-369의 `p.29–30·(변환본)user manual +bridge.docx p.35` → `p.29–30(변환본); 같은 문서 p.35(변환본)`으로 고쳤다. | 교량 DOCX p.29–30은 구조물 설명이다. p.35의 `-v` 행은 진단 메시지 출력을 설명한다. 잘못 이어 붙인 쪽 인용을 분리했다. 최종 E 강함 결론은 유지했다. |
| `lisflood-fp-channel-sgc.md:275` | 정정 | LV1-145의 `v8.0:input.cpp:1021–1055` → `v8.0:input.cpp:992–1026`으로 고쳤다. | v8.0 `input.cpp:992`가 방식 토큰을 읽는다. `995·1001·1007·1013`이 PFIX·PVAR·PBOUND·PBVAR를 판별한다. `1026`이 같은 파일의 숫자 배열을 읽는다. 기존 인용 범위에는 토큰 판별이 없다. 최종 A 결론은 유지했다. |
| `lisflood-fp-channel-sgc.md:338` | 정정 | LT1-199의 “p.42 그림 1과 제한사항” → “p.41 그림 1과 p.42 제한사항”으로 고쳤다. | PDF p.41 이미지에 Figure 1이 있다. p.42에 Bridge limitations and notes가 있다. 최종 LT1-199의 근거 쪽수도 p.41·42다. 최종 C 결론은 유지했다. |

각 정정 줄에는 `[10-21 전수 검증 정정]`을 붙였다.
각 보완 줄에는 `[10-21 전수 검증 보완]`을 붙였다.
표의 표시는 결론 문장 칸 끝에 붙였다.

상대 Markdown 링크 12개가 실제 파일 또는 디렉터리를 가리킨다.
frontmatter의 관련 노트 경로도 실제 파일을 가리킨다.
절대 사용자 경로, `~/`, 위키 링크 구문은 없다.
Mermaid 블록은 없다.
작업의 미완료를 뜻하는 한계 문장은 없다.
LB1-145의 구판 문서 시험 경고와 LI2-314의 입력값 검사 부재는 원문 내용이다.
기계 확인 후보는 사용자 지정 목록이 없으므로 해당 없음이다.
이 노트의 미해결 항목은 없다.

## 2. 공식 자료 노트 대조 완료

대상 노트: `models/LISFLOOD-FP/web-refs/lisflood-fp-official-resources.md`.
대조한 줄은 위 범위표의 59줄 전부다.
이 중 차이 표는 80–82줄의 3행이다.
나머지 56줄에는 frontmatter, 본문, 빈 줄, 제목, 링크 및 표 구분선이 포함된다.
정정은 4줄이다.
보완은 없다.
줄을 삽입하거나 삭제하지 않았으므로 아래 줄 번호는 정정 후에도 같다.

차이 표의 LN1-232·LN1-248·LT1-421은 배정표와 최종 분류 TSV를 대조했다.
각 행의 결론과 근거는 LN1·LT1 최종 검증 기록을 대조했다.
본문의 LV1-286–288·LI2-342 및 LN1-127은 현재 코드, v8.2 코드, 패치 원문과 최종 결론을 대조했다.
LN1-127에는 `conclusion-claude-final`의 우선 판정을 적용했다.
보고서 §4의 LN1-232·248, LT1-421, LI2-342, LI1-371, LV1-001·286–288, LB1-408 수정안을 확인했다.
callflow §6의 공식 자료 노트 항목도 대조했다.

8.2 메타데이터의 기록은 `bf804e23`의 공식 자료 노트와 모델 README에서 확인했다.
현재 8.3 패키지 `README.md:19–39,141–142`와 `LICENSE:1–2`를 열었다.
`VersionHistory.h:16–23,31–32`의 내부 숫자 판과 배포판 표시를 구분했다.
CUDA 최대 수심 배열은 v8.2의 생성자·호출 인수·격자 크기·커널 접근과 현재의 device 할당·0 초기화·host 복사를 대조했다.
flux 동기화는 v8.2와 현재 FV1의 공유 배열 쓰기·읽기·barrier 위치를 대조했다.
DG2 전처리 기본값은 v8.2의 두 전처리 파일과 현재 파일을 대조했다.
NoData 생략 조건은 패치 `75–89`에서 원문 그대로 확인했다.
적응격자 서지는 `cuda/adaptive/cuda_adaptive_simulate.cu:104`의 코드 내 인용과 대조했다.
dg2new의 비활성 설명은 `lisflood.cpp:790–796`의 주석 처리와 연결된 SWE 노트에서 확인했다.
연결 설명은 SFINCS README 및 해당 개념 노트와 대조했다.

### 정정 목록

아래 노트 줄 번호의 기준 파일은 `models/LISFLOOD-FP/web-refs/lisflood-fp-official-resources.md`다.

| 노트:줄 | 구분 | 전 → 후 | 근거 원문 |
|---|---|---|---|
| `lisflood-fp-official-resources.md:27` | 정정 | 공식 8.3 패치에 DOI `10.5281/zenodo.13121119` 귀속 → 배포 설명·패치 원문 링크와 공식 8.2에 8.3 변경을 적용하는 관계를 적었다. | 8.3 패키지 `README.md:19–24`가 직접 적은 DOI는 8.2의 `13121102`이다. 최종 LB1-408은 이 줄을 8.3 DOI의 근거로 쓰지 않도록 정정한다. |
| `lisflood-fp-official-resources.md:51` | 정정 | format 파일의 내용 `5`만 설명 → macOS C++ 표준 헤더 이름 가림을 적었다. E·중간을 반영했다. “8.2 빌드 결함, 8.3에서 고침”을 반영했다. | 최우선 `LISFLOOD-FP-conclusion-claude-final.md`의 LN1-127 결론이다. `v8.2:format:1`은 `5`다. 8.3 패키지 `README.md:37`은 표준 헤더 이름 가림을 적는다. 패치 `264–268`은 파일을 삭제한다. |
| `lisflood-fp-official-resources.md:76` | 정정 | 8.3 DOI `13121119`를 포함한 판 설명 → 8.2 DOI와 8.3 변경 적용 관계로 고쳤다. 내부 숫자 판과 릴리스 이름을 각각 인용했다. | 최종 LB1-408 및 8.3 패키지 `README.md:19–24`다. `VersionHistory.h:16–18`은 8·1·0이다. `23`은 `#define LF_Release "8.3"`이다. |
| `lisflood-fp-official-resources.md:80` | 정정 | LN1-232의 경로 접두사가 인라인 코드 밖에 있던 `../LISFLOOD-FP-8.3-package/` + `LICENSE:1–2` → 전체 경로와 줄 번호를 하나의 인라인 코드 인용으로 고쳤다. | 노트의 코드 경로 기준과 형제 패키지 정의에 따라 `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP-8.3-package/LICENSE:1–2`를 가리킨다. 원문 표제는 `GNU GENERAL PUBLIC LICENSE`와 `Version 3, 29 June 2007`이다. 최종 A 결론은 유지했다. |

각 정정 줄에는 `[10-21 전수 검증 정정]`을 붙였다.
차이 표의 표시는 결론 문장 칸 끝에 붙였다.
상대 Markdown 링크 22개가 실제 파일을 가리킨다.
절 링크의 제목도 대상 보고서에서 확인했다.
frontmatter의 관련 노트 경로 2개도 실제 파일을 가리킨다.
절대 사용자 경로, `~/`, 위키 링크 구문은 없다.
Mermaid 블록은 없다.
작업의 미완료를 뜻하는 한계 문장은 없다.
기계 확인 후보는 사용자 지정 목록이 없으므로 해당 없음이다.
이 노트의 미해결 항목은 없다.

## 최종 집계

| 노트 | 대조한 대상 줄 | 정정 | 보완 |
|---|---:|---:|---:|
| `source-analysis/lisflood-fp-channel-sgc.md` | 155 | 5 | 2 |
| `web-refs/lisflood-fp-official-resources.md` | 59 | 4 | 0 |
| 합계 | 214 | 9 | 2 |

집계는 시작 시 고정한 `git diff -U0 HEAD`의 추가 줄과 실제 정정 표시를 대조한 결과다.
시작 시 대상 줄 214줄과 정정 후 줄을 다시 대조했다.
정정·보완 목록의 11줄 외에는 검증 시작 상태를 유지했다.
차이 표 115행의 최종 분류와 결론 문장은 정정 표시를 제외하면 검증 시작 상태와 같다.
본문 LN1-127의 분류 누락은 최우선 Claude 조정에 따라 정정했다.
두 노트에 대한 `git diff --check`는 통과했다.
쓰기 대상은 지정된 노트 두 개와 이 DELIVERABLE이다.
대상 줄을 모두 대조했으므로 작업을 종료한다.
