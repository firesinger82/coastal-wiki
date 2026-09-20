# EFDC BATCH B2 semantic-review 제안

대상: `3ed76b6e` → `3b382fd0` (v12.5), `phase2-B2.json`의 16건만. 최종 판정자는 Claude이며 이 산출물은 migration 승인·적용이 아니다.

사용자 분류 기준을 우선하고 DESIGN-v2-DRAFT.md의 IMPACT CLASSIFICATION·range 규칙을 참조했다. B1 판정은 사용하거나 전파하지 않았다. 네트워크·sudo·git 명령을 실행하지 않았고 허용된 CSV/MD만 작성했다.

| 제안 분류 | 건수 |
|---|---:|
| UPDATE_REQUIRED | 1 |
| REVIEW_ONLY | 15 |
| NO_ACTION | 0 |
| UNRESOLVED_RULE_GAP | 0 |
| UNRESOLVED_SOURCE_REFERENCE | 0 |

## UPDATE_REQUIRED

- **B2-16** — `efdc_transport_scheme.md:65`, 문맥 `:67-77`. C6 세 번째 입력이 `ldum`에서 실제 scalar `ISQUICK`으로 바뀌었다(old input:306, new input:311-325). 노트의 `-` 표기는 낡았고 ISADAC/ISFCT 설명에는 ISQUICK 조건이 필요하다. new calconc:198-204는 ISQUICK=1일 때 QUICKEST를 호출하고 :228,250은 기존 anti-diffusion을 ISQUICK=0으로 제한한다. 이것은 단순 설명 보강이 아니라 사용자가 지정한 dummy→parameter 기준에 해당한다.

## 개별 판정

| id | 노트 위치 | 제안 | 근거 요약 |
|---|---|---|---|
| B2-1 | efdc_dispersion.md:241 | REVIEW_ONLY | ZBRWALL 필드의 위치·read·broadcast는 유지된다. 이 hunk가 표의 측벽 거칠기 의미나 0.002 예시를 바꾼다는 근거는 없다. |
| B2-2 | efdc_dispersion.md:256 | REVIEW_ONLY | AHO<0 면적 배율, AHD<0 AHMAP 읽기·broadcast·local mapping, AHDXY 대입은 유지된다. 출력 rank 제한은 실제 내부 변경이나 노트의 확산계수 설정 알고리즘을 바꾸지 않는다. |
| B2-3 | efdc_hydraulic_structures.md:21 | REVIEW_ONLY | C23 입력 목록은 동일하고 C32/C32A/C32B 블록(old 1607-1830, new +97)은 내용 동일하다. qctl 관련 old 6344-6671도 +151로 동일. 넓은 범위의 다른 기능 변경을 이 입력 카드 source-basis 주장에 전파하지 않는다. |
| B2-4 | efdc_wetdry.md:19 | REVIEW_ONLY | 노트 source-basis의 HDRY/HWET read·broadcast 및 HDRYICE=0.91*HDRY, HDRYWAV=1.2*HWET은 그대로다. HDRYWAV 식은 기존 범위 끝 바로 다음 old 571/new 593에서 확인. |
| B2-5 | efdc_wetdry.md:45 | REVIEW_ONLY | §B의 C11에서 HDRY/HWET을 읽고 HDRYICE/HDRYWAV를 파생한다는 문장을 개별 확인했다. read 548→570, 파생식 570-571→592-593. |
| B2-6 | efdc_vertical.md:20 | REVIEW_ONLY | source-basis 중 KC를 C9A에서 읽는 근거는 유지된다. KC read의 dummy 필드들도 동일하다. |
| B2-7 | efdc_vertical.md:20 | REVIEW_ONLY | source-basis의 sigma fraction 입력은 여전히 C10의 KDUM,DZCK(K) read이다. |
| B2-8 | efdc_vertical.md:30 | REVIEW_ONLY | §A의 KC를 C9A에서 읽는다는 명시적 주장을 확인: old 515-516→new 537-538. |
| B2-9 | efdc_vertical.md:31 | REVIEW_ONLY | §A의 DZCK(K) 입력은 그대로이며 인용 531은 read 자체가 아니라 do K=1,KC이다(old read 532→new 554). |
| B2-10 | efdc_turbulence.md:22 | REVIEW_ONLY | AHO/AHD/AVO/ABO/AVMX/ABMX 등 C12 입력, C12A ISTOPT(0), C12B ISGOTM 및 Init_GOTM 조건부 호출 유지. |
| B2-11 | efdc_turbulence.md:67 | REVIEW_ONLY | 이 후보가 인용하는 background mixing 입력의 C12 연결은 유지된다. calavb depth-normalization 문장을 이 input 변경과 혼동하지 않는다. |
| B2-12 | efdc_turbulence.md:107 | REVIEW_ONLY | ISTOPT(0) read·broadcast가 그대로며 ISGOTM 필드로 대체되거나 GOTM 선택자로 변경되지 않았다. |
| B2-13 | efdc_turbulence.md:115 | REVIEW_ONLY | ISGOTM은 계속 C12B에서 읽으며 ISGOTM>0일 때 Init_GOTM 호출도 동일하다. |
| B2-14 | efdc-tidal-forcing-conventions-v12.md:28 | REVIEW_ONLY | NPFORT>=1의 RAD=PI2*PFPH/TCP, CPFAM0=PFAM*COS(RAD), SPFAM0=PFAM*SIN(RAD)는 913-915→944-946로 그대로 대응한다. echo 식별자 저장 변경은 PFAM/PFPH의 물리 의미 변경이 아니다. |
| B2-15 | efdc-tidal-forcing-conventions-v12.md:28 | REVIEW_ONLY | NPFORT=0의 RAD와 AMP=G*PFAM, PCBS/PSBS cos/sin 식이 old 982-985→new 1023-1026으로 유지된다. NPFORT=1 다항 합성과 G 곱도 동일. |
| B2-16 | efdc_transport_scheme.md:65 | UPDATE_REQUIRED | 노트 §4 입력 예시의 세 번째 -는 이제 실제 전역 transport 선택자다. NS별 ISADAC/ISFCT 필드는 남지만 ISQUICK=1이면 QUICKEST로 dispatch하고 기존 anti-diffusion 경로는 ISQUICK=0 조건을 갖는다. |

## 교집합 및 근거 검사

- 모든 candidate에서 old citation interval과 patch hunk의 old interval을 폐구간으로 교차 계산했다. hunk의 context 줄에만 걸린 경우도 기록하되 실제 +/- 변경과 구별했다. CSV `changed_hunk`에 모든 교집합을 남겼다.
- 입력 patch의 모든 context/삭제/추가 줄을 로컬 old/new 전문과 대조하고 hunk 사이의 동일 구간까지 확인했다. patch가 전문과 일치한다. 원래 note_line과 wiki_claim도 16건 모두 일치한다.
- B2-2: 2개 hunk 교차. 앞 hunk는 old 3722의 주석만 걸리며 channel 삽입은 인용 앞이다. 내부 old 3792 PRINT는 실제로 master-only로 바뀌므로 전체를 line-only로 처리하지 않았다. AHO/AHD 계산·AHMAP 입력은 유지된다.
- B2-3: 5,320줄 broad citation에 29개 hunk 교차. 변경 전후 양 끝만 비교하지 않았다. 내부 변경을 검토하고 주장한 C23·C32·C32A·C32B의 입력 근거를 개별 확인했다. C32 계열 old 1607-1830/new 1704-1927 및 qctl 관련 old 6344-6671/new 6495-6822는 전체 내용 동일성을 별도로 검사했다. 다른 입력/초기화 기능 변경을 이 카드 목록 주장에 전파하지 않는다.
- B2-4·5: HDRYWAV 파생식은 기존 인용 끝보다 한 줄 뒤(old 571/new 593)에 있다. 이 인접 줄도 근거에 포함했다. 기존 인용 폭의 문제를 이번 의미 변경으로 오인하지 않았다.
- B2-6·7과 B2-8·9는 각각 source-basis와 본문 문장을 독립 대조했다. C9A/C10의 오류처리 이동은 실제 변경이나 KC/DZCK 입력의 카드·필드 의미는 유지된다.
- B2-10~13: echo 출력의 실행 rank/위치 변경은 인정하되 노트의 난류 parameter 입력·선택자 역할·Init_GOTM 호출 관계와 구별했다.
- B2-14·15: 같은 노트 문장이지만 각각 C17 변환과 C18 변환 범위를 개별 대조했다. echo용 dummy 저장이 바뀌어도 PFAM/PFPH 물리 입력 의미나 cos/sin/G 변환은 바뀌지 않았다.

## Claude 검토 대기

REVIEW_ONLY 15건은 각 CSV reason에 적은 근거로 의미 수정 불필요를 제안하지만, 줄 좌표와 broad citation의 최종 disposition은 Claude 검토 대기다. NO_ACTION이나 자동 LINE_REFERENCE_ONLY로 종결하지 않았다. 일부 인용 줄 자체가 동일해도 교차 hunk의 인접 오류처리·echo 변경과 좌표 이동을 함께 기록했다. UNRESOLVED 목록은 없다.

## 무변경 및 검증

`models/`에 쓰기 작업을 수행하지 않았다. 검토 대상 노트 7개와 old input.f90의 SHA-256은 작성 전후 8/8 일치를 확인했다. 그 외 models 전체 파일을 별도 감사하지 않았으며 models 잠금은 우회하지 않았다. CSV는 14개 지정 필드, 첫 열 id, 입력과 같은 순서의 고유 ID 16개를 갖는다.
